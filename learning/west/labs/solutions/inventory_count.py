# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""只读的 west 扩展：列出活动项目，可供人或其他程序使用。"""

import json  # 把同一份报告转换成程序容易读取的 JSON 文本。

from west.commands import WestCommand  # 使用 west 提供的命令框架。


class Inventory(WestCommand):
    """声明命令、接收参数，再读取 west 传入的清单。"""

    def __init__(self):
        # west 创建这个对象时，先登记命令名和两段帮助文字。
        super().__init__(
            "inventory",
            "Show active repositories",
            "List active projects; this command does not update repositories.",
        )

    def do_add_parser(self, parser_adder):
        # 登记参数的写法；此处还不读取项目、不打印报告。
        parser = parser_adder.add_parser(self.name, description=self.description)
        parser.add_argument("--format", choices=("text", "json"), default="text")
        # 写了此选项就是 True；省略就是 False，不需要再跟 true。
        parser.add_argument("--require-cloned", action="store_true",
                            help="Fail if an active project has not been cloned")
        parser.add_argument("--count", action="store_true",
                            help="Print the number of active projects")
        return parser

    def do_run(self, args, unknown_args):
        rows = []  # 空列表：接下来为每个活动依赖放入一行报告。
        for project in self.manifest.projects:
            # 清单仓库由 init 定位，不计入依赖；停用项目也跳过。
            if project.name == "manifest" or not self.manifest.is_active(project):
                continue
            # 字典把字段名与值配成一行；is_cloned() 只查询，不下载。
            rows.append({
                "name": project.name,
                "path": project.path,
                "revision": project.revision,
                "cloned": project.is_cloned(),
            })

        # 先完成严格检查，再选择输出格式；缺少任何一个项目就停止。
        if args.require_cloned:
            for row in rows:
                if not row["cloned"]:
                    self.die("An active project is missing; run west update first.")
        # 缺失检查已经完成，计数不会绕过 --require-cloned。
        if args.count:
            self.inf(str(len(rows)))
            return
        if args.format == "json":
            self.inf(json.dumps(rows, ensure_ascii=False, indent=2))
        else:
            # 遍历同一组记录，每个项目输出一行供人阅读的文字。
            for row in rows:
                self.inf(f"{row['name']}: {row['path']} @ {row['revision']} "
                         f"cloned={row['cloned']}")
