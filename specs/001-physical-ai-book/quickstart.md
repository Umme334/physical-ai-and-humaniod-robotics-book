# Quickstart: Writing the Book

## Workflow

1.  **Scaffold**: Create the folder structure defined in `data-model.md`.
2.  **Code First**: For each chapter, write the *code* first.
    - Verify it runs.
    - Verify it meets the "Accessibility" principle (simple, clear).
3.  **Write Content**: Use the `chapter-template.md` to wrap the code in narrative.
    - Paste tested code snippets into the Markdown.
    - Add screenshots (placeholders for now: `![Screenshot of X](assets/x.png)`).
4.  **Review**: Check against the "Constitution Check" (Brevity, Practicality).

## Environment

- **Authoring**: VS Code + Markdown All in One.
- **Code Testing**:
    - ROS 2 Humble (Local or Docker).
    - Python 3.10+.
    - Isaac Sim 2023.1+ (optional for drafting, mandatory for verification).

## Commands

```bash
# Verify code style (if we add linting later)
# ruff check .

# Build book (if using Docusaurus)
# npm run build
```
