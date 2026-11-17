# Guided GitHub Setup for Claude

You do not need to know Git, use a terminal, or write code.

## Easiest option

1. Open Claude and create a private Project for one business assessment.
2. In Project Knowledge, select **GitHub**.
3. Choose the public `brewser123/business-before-agents` repository and add `BOOTSTRAP.md`, `bootstrap.json`, and the required files listed in the manifest.
4. Paste the prompt below into a new chat in that Project.
5. Follow one step at a time. Use Claude's **Sync** option after a future framework release.

Claude requires the user to authorize GitHub and select the repository content. A prompt cannot complete those account-level steps by itself.

Current product guidance:

- GitHub integration: https://support.anthropic.com/en/articles/10167454-using-the-github-integration
- Claude Projects: https://support.anthropic.com/en/articles/9517075-what-are-projects

## Prompt to paste

```text
I would like to use the Business Before Agents framework, but I am not familiar with GitHub or installing files.

Please use the GitHub files attached to this chat or Project Knowledge, beginning with BOOTSTRAP.md and bootstrap.json from the v0.1-preview.3 release.

First, tell me whether every required file is available. Then follow BOOTSTRAP.md and guide me through any remaining setup.

Please follow these rules:
- Assume I have no experience with GitHub or Claude Projects.
- Use plain language and give me only one step at a time.
- Do not ask me to use command-line tools, Git commands, or programming.
- Do not claim the framework is ready until every required file has been verified.
- If I download the ZIP, follow BOOTSTRAP.md's checksum instructions before opening it. Compare its SHA-256 with SHA256SUMS.txt attached to the official v0.1-preview.3 GitHub Release. Say “checksum verified” only if you calculated the exact ZIP's hash and it matched. If I use the website checker, call the result user-reported. If neither check is possible, say “checksum not verified” and offer the tagged GitHub files instead. Stop if the checksum differs.
- If files are missing, tell me exactly what to select through Add from GitHub.
- Do not infer or recreate missing framework instructions.
- Do not ask me to share confidential business information during setup.
- Stop after setup is complete and wait for me to say: “Start the Business Before Agents discovery interview.”
```

## Important continuity note

Keep the Project private and save approved resume checkpoints in storage the business controls. If the Project cannot retrieve the checkpoint later, provide it again rather than asking Claude to reconstruct it.
