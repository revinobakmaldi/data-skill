#!/usr/bin/env python3
"""
data_to_claude.py — Feed structured data to Claude, get analysis back.

Usage:
    python data_to_claude.py --file sales.csv --question "What are the top 3 trends?"
    python data_to_claude.py --file report.json --question "Flag any anomalies"
    cat data.csv | python data_to_claude.py --stdin --question "Summarize this"

Requirements:
    pip install anthropic pandas tabulate
"""

import argparse
import sys
import os
import json
import anthropic
import pandas as pd
from tabulate import tabulate

MODEL = "claude-opus-4-6"
MAX_ROWS = 200  # truncate large datasets to avoid token overflow


def load_data(file_path: str | None, from_stdin: bool) -> pd.DataFrame:
    if from_stdin:
        raw = sys.stdin.read()
        # Try JSON first, then CSV
        try:
            data = json.loads(raw)
            return pd.DataFrame(data if isinstance(data, list) else [data])
        except json.JSONDecodeError:
            from io import StringIO
            return pd.read_csv(StringIO(raw))

    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        return pd.read_csv(file_path)
    elif ext == ".json":
        with open(file_path) as f:
            data = json.load(f)
        return pd.DataFrame(data if isinstance(data, list) else [data])
    elif ext in (".xlsx", ".xls"):
        return pd.read_excel(file_path)
    elif ext == ".parquet":
        return pd.read_parquet(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}. Use .csv, .json, .xlsx, or .parquet")


def format_data_for_prompt(df: pd.DataFrame) -> str:
    total_rows = len(df)
    if total_rows > MAX_ROWS:
        print(f"[info] Dataset has {total_rows} rows — truncating to {MAX_ROWS} for analysis.", file=sys.stderr)
        df = df.head(MAX_ROWS)

    # Include shape, dtypes, basic stats, and the actual data
    shape_info = f"Shape: {total_rows} rows × {len(df.columns)} columns"
    if total_rows > MAX_ROWS:
        shape_info += f" (showing first {MAX_ROWS})"

    dtypes_info = "\n".join(f"  - {col}: {dtype}" for col, dtype in df.dtypes.items())

    # Numeric summary
    numeric_cols = df.select_dtypes(include="number").columns
    stats_section = ""
    if len(numeric_cols) > 0:
        stats = df[numeric_cols].describe().round(2)
        stats_section = f"\nNumeric summary:\n{tabulate(stats, headers='keys', tablefmt='github')}\n"

    # Data sample
    data_table = tabulate(df, headers="keys", tablefmt="github", showindex=False)

    return f"""{shape_info}

Column types:
{dtypes_info}
{stats_section}
Data:
{data_table}"""


def analyze(df: pd.DataFrame, question: str, system_prompt: str | None) -> str:
    data_text = format_data_for_prompt(df)

    default_system = (
        "You are a senior data analyst. You receive structured data and answer questions about it. "
        "Be direct and specific. Lead with the answer, not the setup. "
        "Use numbers from the data to support your points. "
        "If you spot anomalies or noteworthy patterns beyond the question, mention them briefly at the end."
    )

    client = anthropic.Anthropic()
    message = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        system=system_prompt or default_system,
        messages=[
            {
                "role": "user",
                "content": f"Here is the data:\n\n```\n{data_text}\n```\n\nQuestion: {question}"
            }
        ]
    )
    return message.content[0].text


def main():
    parser = argparse.ArgumentParser(description="Feed data to Claude for analysis")
    parser.add_argument("--file", "-f", help="Path to data file (.csv, .json, .xlsx, .parquet)")
    parser.add_argument("--stdin", action="store_true", help="Read data from stdin")
    parser.add_argument("--question", "-q", required=True, help="Question to ask about the data")
    parser.add_argument("--system", "-s", help="Custom system prompt (optional)")
    parser.add_argument("--output", "-o", help="Write output to file instead of stdout")
    args = parser.parse_args()

    if not args.file and not args.stdin:
        parser.error("Provide either --file or --stdin")
    if args.file and args.stdin:
        parser.error("Use either --file or --stdin, not both")

    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    print(f"[info] Loading data...", file=sys.stderr)
    df = load_data(args.file, args.stdin)

    print(f"[info] Sending to Claude ({MODEL})...", file=sys.stderr)
    result = analyze(df, args.question, args.system)

    if args.output:
        with open(args.output, "w") as f:
            f.write(result)
        print(f"[info] Output written to {args.output}", file=sys.stderr)
    else:
        print(result)


if __name__ == "__main__":
    main()
