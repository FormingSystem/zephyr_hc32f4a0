# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""P04：由团队定义 userdata 的含义，显式调用 Git 做只读仓库检查。"""

from pathlib import PurePosixPath

from west.commands import WestCommand


class RepoAudit(WestCommand):
    def __init__(self):
        # CLI 名称、简短帮助、完整描述；注册文件的 class 指向本类。
        super().__init__("repo-audit", "Check team repository policy",
                         "Check committed files and tracked changes; never update repositories.")

    def do_add_parser(self, parser_adder):
        parser = parser_adder.add_parser(self.name, description=self.description)
        # 不写项目时检查活动依赖；指定 name 时只选这些项目。
        parser.add_argument("projects", nargs="*", help="Manifest project names")
        return parser

    def _git(self, project, arguments):
        # Project.git 自动补上 git，默认 cwd=project.abspath；不使用 shell。
        # check=False 把非零退出交给我们解释，capture_* 将字节输出交回 Python。
        result = project.git(arguments, check=False,
                             capture_stdout=True, capture_stderr=True)
        if result.returncode:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            self.die(f"{project.name}: git {arguments} failed ({result.returncode}): {detail}")
        return result.stdout.decode("utf-8", errors="replace").strip()

    def do_run(self, args, unknown_args):
        # WestCommand.run 已提供 self.manifest；我们不再手工解析 YAML。
        try:
            projects = (self.manifest.get_projects(args.projects)
                        if args.projects else self.manifest.projects)
        except ValueError:
            self.die("Unknown project name; inspect west list -a first.")
        checked = 0
        for project in projects:
            if project.name == "manifest" or not self.manifest.is_active(project):
                if args.projects:
                    self.die(f"{project.name}: select an active dependency project.")
                continue
            data = project.userdata
            if data is None:
                continue
            if not isinstance(data, dict):
                self.die(f"{project.name}: userdata must be a mapping for this command.")
            if "team-policy" not in data:
                continue
            policy = data["team-policy"]
            # west 的 schema 允许任意 userdata；以下业务规则全部由本扩展负责。
            if not isinstance(policy, dict):
                self.die(f"{project.name}: team-policy must be a mapping.")
            if set(policy) - {"required-files", "require-clean-tracked"}:
                self.die(f"{project.name}: unknown team-policy key.")
            files = policy.get("required-files")
            clean = policy.get("require-clean-tracked", True)
            if not isinstance(files, list) or not files:
                self.die(f"{project.name}: required-files must be a nonempty list.")
            if not isinstance(clean, bool):
                self.die(f"{project.name}: require-clean-tracked must be a boolean.")
            for name in files:
                # Git 树内路径统一用 /，限制为相对于当前项目的文件路径。
                if (not isinstance(name, str) or not name
                        or PurePosixPath(name).is_absolute()
                        or ".." in PurePosixPath(name).parts
                        or "\\" in name or ":" in name):
                    self.die(f"{project.name}: required-files needs relative Git paths.")
            if not project.is_cloned():
                self.die(f"{project.name}: missing repository; run west update first.")
            # 查询 HEAD，随后检查的是该提交中的文件，不是 Python 看到的磁盘文件。
            sha = self._git(project, ["rev-parse", "HEAD"])
            for name in files:
                # 查询对象类型，避免把目录误认成文件，也不读取整个大文件。
                kind = self._git(project, ["cat-file", "-t", f"HEAD:{name}"])
                if kind != "blob":
                    self.die(f"{project.name}: {name} must be a committed file (blob).")
            if clean:
                # 有意只检查已跟踪文件；未跟踪的 __pycache__ 不属于此策略。
                changes = self._git(project, ["status", "--porcelain", "--untracked-files=no"])
                if changes:
                    self.die(f"{project.name}: tracked changes exist:\n{changes}")
            checked += 1
            self.inf(f"PASS {project.name}: HEAD={sha}, files={len(files)}")
        if not checked:
            # 防止没有任何策略时输出看似成功的空报告。
            self.die("No active project has team-policy; add userdata or select another project.")
        self.inf(f"Audited {checked} project(s).")
