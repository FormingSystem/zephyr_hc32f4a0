# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""只读的 west 扩展：列出活动项目，可供人或其他程序使用。"""

import json

from west.commands import WestCommand


class Inventory(WestCommand):
    """声明命令、接收参数，再读取 west 传入的清单。"""

    def __init__(self):
        super().__init__(
            "inventory",
            "Show active repositories",
            "List active projects; this command does not update repositories.",
        )

    def do_add_parser(self, parser_adder):
        parser = parser_adder.add_parser(self.name, description=self.description)
        parser.add_argument("--format", choices=("text", "json"), default="text")
        parser.add_argument("--require-cloned", action="store_true",
                            help="Fail if an active project has not been cloned")
        parser.add_argument("--count", action="store_true",
                            help="Print the number of active projects")
        return parser

    def do_run(self, args, unknown_args):
        # 清单仓库由 init 定位，不计入这里的受管依赖项目。
        projects = [p for p in self.manifest.projects
                    if p.name != "manifest" and self.manifest.is_active(p)]
        rows = [{"name": p.name, "path": p.path, "revision": p.revision,
                 "cloned": p.is_cloned()} for p in projects]
        if args.require_cloned and any(not row["cloned"] for row in rows):
            self.die("An active project is missing; run west update first.")
        # 先执行缺失检查，再返回计数，防止计数选项绕过完整性要求。
        if args.count:
            self.inf(str(len(rows)))
            return
        if args.format == "json":
            self.inf(json.dumps(rows, ensure_ascii=False, indent=2))
        else:
            for row in rows:
                self.inf(f"{row['name']}: {row['path']} @ {row['revision']} "
                         f"cloned={row['cloned']}")
