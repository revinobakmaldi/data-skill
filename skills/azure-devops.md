---
source: microsoft/azure-devops-mcp
source_url: https://github.com/microsoft/azure-devops-mcp
license: MIT
requires_mcp: azure-devops (see mcp/configs/azure-devops-mcp.json)
---

# Skill: azure-devops

Work with Azure DevOps — task management, repos, pipelines, and wikis — directly from Claude Code.

Requires the Azure DevOps MCP server to be connected.
Setup: `claude mcp add azure-devops -- npx -y @azure-devops/mcp YOUR_ORG_NAME`

## Trigger phrases
- "create a work item for..."
- "show me open tasks in sprint..."
- "create a PR for..."
- "what's the status of pipeline..."
- "assign this to..."
- "update the wiki page..."
- "list all bugs in..."

---

## What you can do

### Work Items (Boards)
- Create, update, assign, and close work items (tasks, bugs, user stories, epics)
- Query work items by sprint, assignee, state, or tag
- Add comments, attachments, and links between items
- Move items between states and iterations
- Bulk update multiple work items

### Repositories
- List repos and branches in the project
- Create and review pull requests
- Fetch file content from any branch
- View commits, diffs, and PR comments
- Merge PRs (if authorized)

### Pipelines
- List pipeline definitions
- Queue a new build run
- Check run status and view logs
- Cancel or retry a failed run

### Wiki
- Read and update wiki pages
- Create new pages in a wiki

---

## Common workflows

### Start of sprint — check your tasks
```
List all work items assigned to me in the current sprint that are In Progress or To Do
```

### Create a task from a PR
```
Create a work item of type Task in project [ProjectName], title "Fix null handling in
sales aggregation model", assign to me, add to current sprint, link to PR #42
```

### Daily standup prep
```
Show me all work items I updated or commented on yesterday across project [ProjectName]
```

### PR review
```
List all open pull requests in repo [RepoName] that are waiting for my review
```

### After merging — close the task
```
Update work item #1234 state to Done and add comment "Merged in PR #42"
```

---

## Tips
- Always mention the project name if you work across multiple projects
- Use "current sprint" or "sprint 12" to scope work item queries
- For bulk updates, describe the filter first: "all bugs assigned to me with state Active"
- PR descriptions can be generated from commit messages: "write a PR description based on these commits: [list]"
