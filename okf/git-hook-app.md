---
type: Application
title: "GitHookApp"
description: "Runs the GitHookApp PythonEDA app."
resource: https://github.com/pythoneda-tools-artifact/git-hook/blob/main/pythoneda/tools/artifact/git_hook/application/git_hook_app.py
tags: [application]
generated: { by: pythoneda-grill/deepseek-v4-pro, at: 2026-11-02T19:55:27Z }
sources:
  - id: src
    resource: https://github.com/pythoneda-tools-artifact/git-hook/blob/main/pythoneda/tools/artifact/git_hook/application/git_hook_app.py
    title: pythoneda/tools/artifact/git_hook/application/git_hook_app.py
  - id: readme
    resource: https://github.com/pythoneda-tools-artifact/git-hook/blob/main/README.md
    title: README.md
status: draft
---

Runs the GitHookApp PythonEDA app.

Class name: GitHookApp

Responsibilities:
    - Emits PythonEDA artifact events triggered by git hooks.

Collaborators:
    - Command-line handlers from pythoneda-shared-artifact/infrastructure
