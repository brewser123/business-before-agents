# Guided GitHub Setup for ChatGPT

You do not need to know Git, use a terminal, or write code.

## Easiest option

1. Open ChatGPT and create a private Project for one business assessment.
2. Paste the prompt below into a new chat in that Project.
3. If ChatGPT can use a connected GitHub app in your plan and workspace, allow it to read the public `brewser123/business-before-agents` repository.
4. Follow one step at a time. If GitHub access is unavailable, ChatGPT should guide you through adding the files manually.

ChatGPT's GitHub connection retrieves authorized repository content on demand; it does not create a continuously synchronized copy. For reliable reuse, keep the required framework files as Project sources when that option is available.

Current product guidance:

- GitHub connection: https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt-deep-resear
- ChatGPT Projects: https://help.openai.com/en/articles/10169521-projects-in-chatgpt

## Prompt to paste

```text
I would like to use the Business Before Agents framework, but I am not familiar with GitHub or installing files.

Please read the guided setup at:
https://github.com/brewser123/business-before-agents/blob/v0.1-preview/BOOTSTRAP.md

First, tell me whether you can access that guide and the release's bootstrap.json file. Then follow the guide and help me use the easiest setup method available in this version of ChatGPT.

Please follow these rules:
- Assume I have no experience with GitHub or AI Projects.
- Use plain language and give me only one step at a time.
- Do not ask me to use command-line tools, Git commands, or programming.
- Do not claim the framework is ready until every required file has been verified.
- If you cannot access the files directly, tell me exactly what to click, download, extract, or upload.
- Do not ask me to share confidential business information during setup.
- Stop after setup is complete and wait for me to say: “Start the Business Before Agents discovery interview.”
```

## Important continuity note

A chat may not retain files forever. Keep approved resume checkpoints in private storage the business controls. If a later chat cannot retrieve the Project files or checkpoint, provide them again rather than asking the AI to reconstruct them.
