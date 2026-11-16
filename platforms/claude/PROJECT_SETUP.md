# Claude Project Setup

Interface names and data practices can change; verify the current product documentation and account settings before use.

If you are unfamiliar with GitHub or AI Projects, begin with [Guided GitHub Setup for Claude](GITHUB_GUIDED_SETUP.md). It explains how to add the approved repository files to Project Knowledge and provides a plain-language verification prompt.

1. Create a private project dedicated to one business assessment.
2. Review `privacy/PRIVACY.md` and determine which information is suitable for this hosted environment.
3. Add the required files listed in `bootstrap.json` to Project Knowledge and place the operating rules from `core/CONSULTANT.md` in Project Instructions where appropriate.
4. Keep completed business-state and assessment files in private, access-controlled storage.
5. Begin with: **“Start the Business Before Agents discovery interview. Ask one question at a time and request approval at each meaningful checkpoint.”**
6. Reattach or restate the last approved checkpoint when context is uncertain.
7. To stop, ask Claude to pause and create a resume checkpoint, then save the approved checkpoint with the private business-state record.
8. To return, ask Claude to resume from the last approved checkpoint and provide it if the project cannot retrieve it.

A private project is not the same as fully local processing. Confirm the terms and controls that apply to the specific consumer, team, or enterprise account being used.

