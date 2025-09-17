# Coderabbit Quickstart (Project Notes)

This document captures the practical steps to test and use Coderabbit on this repo.

## 1) Install & Authenticate
- Install the Coderabbit VS Code extension
- Authenticate with GitHub when prompted

## 2) Branching for Tests
- Use a dedicated branch (created): `coderabbit-test`
- Push it to GitHub:

```powershell
git push -u origin coderabbit-test
```

## 3) Minimal Config
- A minimal config is in `.github/coderabbit.yml` controlling triggers and scope
- Currently: reviews run on Pull Requests

## 4) Trigger a Review via PR
- Open a PR from `coderabbit-test` → `main` (or `empirical-validation`)
- Add a clear title and description
- Coderabbit will analyze the diff and comment with review feedback

## 5) Tips
- Keep PRs focused for clearer feedback
- Use meaningful commit messages
- Include context in PR description (what/why, risks, test plan)

## 6) Maintenance
- Adjust `.github/coderabbit.yml` as needed (include/exclude paths, comment volume)
- Close or merge PRs after addressing feedback

## 7) Troubleshooting
- If no review appears: ensure PR is open and config exists on target branch
- Check GitHub app permissions if using organization repos
- Re-run checks or re-open the PR after changes

---
Last updated: 2025-09-17
