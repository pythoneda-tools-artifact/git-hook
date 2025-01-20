# vim: set fileencoding=utf-8
"""
pythoneda/tools/artifact/git_hook/application/git_hook_app.py

This file defines the GitHookApp class.

Copyright (C) 2023-today rydnr's pythoneda-tools-artifact/git-hook

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
from pythoneda.shared.application import enable, PythonEDA
from pythoneda.shared.artifact.events.infrastructure.cli import (
    ForwardStagedChangesCommittedCli,
)
from pythoneda.shared.artifact.infrastructure.dbus import (
    ArtifactDbusSignalEmitter,
)


@enable(ArtifactDbusSignalEmitter)
@enable(ForwardStagedChangesCommittedCli)
class GitHookApp(PythonEDA):
    """
    Runs the GitHookApp PythonEDA app.

    Class name: GitHookApp

    Responsibilities:
        - Emits PythonEDA artifact events triggered by git hooks.

    Collaborators:
        - Command-line handlers from pythoneda-shared-artifact/infrastructure
    """

    def __init__(self):
        """
        Creates a new GitHookApp instance.
        """
        # python_dep_banner is automatically generated by pythoneda-tools-artifact-def/git-hook
        try:
            from pythoneda.tools.artifact.git_hook.application.GitHookBanner_banner import (
                GitHookBanner,
            )

            banner = GitHookBanner()
        except ImportError:
            banner = None

        super().__init__(banner, __file__)
        self.accept_one_shot(True)


if __name__ == "__main__":
    asyncio.run(GitHookApp.main())
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
