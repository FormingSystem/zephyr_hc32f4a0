---
id: learning.zephyr-docs.west.west_releases
title: west发行说明
kind: reference
status: maintained
domains: [zephyr, west]
source_url: https://docs.zephyrproject.org/latest/develop/west/release-notes.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_west发行说明

原文：[West Release Notes](https://docs.zephyrproject.org/latest/develop/west/release-notes.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

> 译注：本章按官方原顺序翻译各版本记录。“现在”“新增”“不再支持”等描述均以所属版本为时间基准，不是对所有版本的统一要求。历史命令、迁移示例和失效版本警告完整保留；需要当前操作方法时，参见本册相应命令章节。示例中的占位符需替换，历史无效清单不能作为当前配置直接使用。

## 17.1\_v1.5.0

**主要改动（Major Changes）：**支持**自动缓存（Auto-caching）**，向 `west update` 传入 `--auto-cache <directory>` 使用。

**其他改动（Other Changes）：**

- `west update` 允许组合 `--name-cache` 与 `--path-cache`。
- 在清单模式中记录默认修订值。

**错误修复（Bug Fixes）：**

- 允许清单项目列表为空或缺失。
- 冻结或解析清单文件时，使 `manifest.group-filter` 列表顺序具有确定性。

## 17.2\_v1.4.0

**改动：**

- 允许向配置字符串追加数据。为 `<name>` 的值追加内容时，使用 `west config -a <name> <value>`。
- `west manifest` 新增 `--untracked`。在工作区运行 `west manifest --untracked`，打印未被 west 跟踪或管理的全部文件和目录。
- `west list` 新增 `--inactive`，用于打印**非活动项目（Inactive Projects）**。
- `west manifest --resolve` 和 `west manifest --freeze` 支持 `--active-only`，允许在启用了项目过滤或组过滤的工作区进行冻结。

**API改动（API Changes）：**`west.manifest.Manifest` 的 `as_dict()`、`as_frozen_dict()`、`as_yaml()`、`as_frozen_yaml()` 新增可选参数 `active_only`，默认 `False`，用于选择返回全部项目还是仅返回活动项目。

## 17.3\_v1.3.0

**主要改动：**

- 支持 [west命令别名（West Aliases）](P006_命令别名.md)。
- 打包采用 [pyproject TOML规范](https://packaging.python.org/en/latest/specifications/pyproject-toml/)。

**其他改动：**

- 为子模块增加缓存支持。
- 默认按 UTF-8 解码清单文件。
- 将 `west diff`、`west status` 的未知参数传给底层 `git` 命令。
- `west diff` 增加 `--manifest`，允许比较当前工作区与清单修订。
- `west forall` 可使用环境变量；定义了 `WEST_PROJECT_NAME`、`WEST_PROJECT_PATH`、`WEST_PROJECT_ABSPATH`、`WEST_PROJECT_REVISION`、`WEST_PROJECT_URL`、`WEST_PROJECT_REMOTE`。
- 支持早期处理参数 `-q/--quiet`，降低输出详细程度。
- `west init` 增加 `-o/--clone-opt`，将选项传给 `git clone`。
- 支持 Python 3.13，并停止支持 Python 3.8。
- 禁止清单将项目放入 `.west` 目录。
- 为 `west init` 增加 NTFS 兼容处理和 `--rename-delay`。
- 调试级别为 `-vvv` 时，调用 `die` 会打印**栈回溯（Stack Trace）**。

**错误修复：**

- 使用 `'backslashreplace'` 处理子进程输出中格式错误的 UTF 数据，避免崩溃。
- 修复 `west diff` 对存在合并冲突的仓库的处理，改善错误输出并处理 `git diff` 返回码。
- 修复使用 Git 子模块时，`west manifest` 的 `--freeze`、`--resolve` 行为。

## 17.4\_v1.2.0

**主要改动：**新增 `west grep`，可在工作区仓库中运行“grep 工具”。当时支持 `git grep`、[ripgrep](https://github.com/BurntSushi/ripgrep) 和标准 `grep`。

> 译注：原文 ripgrep 链接带 `#readme`；当前返回页面未能确认该锚点，这里指向同一官方仓库主页。

若要在所有已克隆且活动的仓库中获得 `git grep foo` 的结果，可在准备好工具的 west 工作区内运行：

```shell
west grep foo
```

其他调用示例如下：

| 对应搜索工具或选项 | west调用 |
| --- | --- |
| `git grep --untracked` | `west grep --untracked foo` |
| `ripgrep` | `west grep --tool ripgrep foo` |
| `grep --recursive` | `west grep --tool grep foo` |

切换工作区默认搜索工具时，运行相应配置命令：

| 默认工具 | 配置命令 |
| --- | --- |
| `ripgrep` | `west config grep.tool ripgrep` |
| `grep` | `west config grep.tool grep` |

详情可运行 `west help grep`。

**其他改动：**

- 清单每个 `projects:` 元素支持 `description` 字段，示例见[项目定义](P013_west清单文件.md)。
- `west list --format` 的格式字符串接受 `{description}`，输出项目的 `description:` 值。
- `west compare` 始终打印 [manifest-rev分支](P004_工作区.md)的信息。

**错误修复：**如果目标目录已经存在，`west init` 会中止。

**API改动：**

- `WestCommand.check_call()`、`check_output()` 接受可传给底层 `subprocess` 函数的任意关键字参数。
- 新增 `west.commands.WestCommand.run_subprocess()`，封装 `subprocess.run()`；因为已经存在 `run()` 方法，所以不能使用这个名字。
- `WestCommand.dbg()`、`inf()`、`wrn()`、`err()` 均接受 `end` 关键字参数，并传给 `print()`。
- `west.manifest.Project` 新增 `description` 属性，保存清单 `description:` 字段的解析值。

## 17.5\_v1.1.0

**主要改动：**

- 新增 `west compare`，用于比较工作区状态与清单。
- 新增 `manifest.project-filter` 配置，见[内置配置选项](P003_配置.md)。在本版本中，设置该选项后不能使用 `west manifest --freeze` 或 `west manifest --resolve`；此限制可能在后续版本取消。
- 项目名称包含逗号 `,` 或空白字符时产生警告；如果设置了新的 `manifest.project-filter`，则视为错误。警告可能在未来主版本中升级为错误。

**其他改动：**

- `west forall` 接受 `--group`，限制命令只在一个或多个组内运行，详情见 `west help forall`。
- 所有 west 命令输出来自 west API 模块、警告及以上级别的日志。`--verbose` 使用一次还包括信息日志，使用两次还包括调试日志，适用于所有命令。

**错误修复：**改善多处错误消息、调试日志和错误处理。

**API改动：**`west.manifest.Manifest.is_active()` 遵循 `manifest.project-filter` 的值。

## 17.6\_v1.0.1

**主要改动：**支持清单模式版本 `"1.0"`，功能与 `"0.13"` 相同，供不希望在清单 `version:` 中使用 `0.x` 的应用选择。详见[模式版本](P013_west清单文件.md)。

**错误修复：**收到中断信号后，west 不再以成功退出码退出，而是使用平台相关错误码，向调用环境表明进程被中断。

## 17.7\_v1.0.0

**主要改动：**

- [west API](P016_west的PythonAPI.md) 宣布稳定。破坏兼容性的改动将通过从 `v1.x.y` 升到 `v2.x.y` 的主版本变化传达。
- west v1.0 不再兼容 Zephyr v1.14 **长期支持版（Long-Term Support，LTS）**。原文说明它早已由 Zephyr v2.7 LTS 取代；使用 Zephyr v1.14 时，必须使用 west v0.14 或更早版本。
- 与 Zephyr 其余部分一样，本版本要求 Python v3.8 或更高版本。
- west 命令不再接受命令行选项缩写。例如必须写 `west update --keep-descendants`，不能写 `west update --keep-d`。这是针对全部 Zephyr Python 脚本命令行接口的统一变化：命令加入名称相似但行为不同的新选项时，原来的缩写会产生实际问题。

**其他改动：**

- 所有 west 内置函数停止使用 `west.log`。
- `west update` 新增 `--submodule-init-config`，见[提交9ba92b05](https://github.com/zephyrproject-rtos/west/commit/9ba92b054500d75518ff4c4646590bfe134db523)。

**错误修复：**

- 扩展命令加载失败时，有时会直接输出栈回溯；现在改为合理的错误消息。
- `west config` 会拒绝格式错误、选项名中缺少 `.` 的配置参数。

**API改动：**

- west 包加入必要元数据，供 [mypy](https://www.mypy-lang.org/) 等静态分析器自动识别类型注解，见[提交d9f00e24](https://github.com/zephyrproject-rtos/west/commit/d9f00e242b8cb297b56e941982adf231281c6bae)。
- 删除用于兼容 Zephyr v1.14 LTS、此前已弃用的 `west.build` 模块。
- 删除同样用于该兼容目的、此前已弃用的 `west.cmake` 模块。
- 弃用 `west.log`。该模块使用全局状态，作为多个 Python 模块共同依赖的 API 时不便使用。
- [west.commands](P016_west的PythonAPI.md) 增加一些 API，为未来按命令控制全局输出详细程度以及消除包 API 中的全局状态打基础：`west.commands.WestCommand.__init__()` 新增 `verbosity` 关键字参数；`WestCommand` 新增 `color_ui` 属性；新增 `inf()`、`wrn()`、`err()`、`die()`、`banner()`、`small_banner()` 等输出方法，扩展命令应使用它们，而不是直接写 `sys.stdout` 或 `sys.stderr`；另新增原文所称的 `west.commands.VERBOSITY` 枚举。

> 译注：原文枚举名大小写有误。[v1.0.0命令源码](https://github.com/zephyrproject-rtos/west/blob/v1.0.0/src/west/commands.py)定义的是 `west.commands.Verbosity`。

## 17.8\_v0.14.0

**错误修复：**

- 使用损坏的本地配置运行 west 命令时，过去会输出令人困惑的栈回溯；现在输出合理错误消息。
- 修复查找 `zephyr` 仓库的错误。此前在新工作区首次运行 `west build` 等扩展命令时，如果没有在工作区顶层目录执行，首次调用会失败，之后调用却正常。
- 没有权限打开清单文件时，输出合理错误消息，而非栈回溯。

**API改动：**

- `west.manifest.MalformedConfig` 异常类型移到 `west.configuration`。
- `west.manifest.MalformedConfig` 异常类型移到 [west.configuration](P016_west的PythonAPI.md)。（译注：原文重复列出了此项。）
- `west.configuration.Configuration` 在部分情况下改为抛出 `MalformedConfig`，而非 `RuntimeError`。

## 17.9\_v0.13.1

**错误修复：**在工作区之外调用 `west.manifest.Manifest.from_file()` 时，恢复通过 `ZEPHYR_BASE` 环境变量回退查找工作区的行为。

## 17.10\_v0.13.0

**新功能（New Features）：**可通过 `manifest: self: userdata:` 给清单仓库自身关联任意用户数据，例如：

```yaml
manifest:
  self:
    userdata: <any YAML value can go here>
```

**错误修复：**

- 某些情况下 west 报告的清单仓库路径不正确，见[议题#572](https://github.com/zephyrproject-rtos/west/issues/572)。此修复属于 `west.manifest` API 路径处理整体调整的一部分。
- 修复原文所称 `west.Manifest.ManifestProject.__repr__` 的返回值。

**API改动：**

- 新增 `west.configuration.Configuration`，以面向对象接口表示当前系统、全局、工作区本地配置，支持从其中任意一个或全部位置读、写、删除选项。
- `west.commands.WestCommand` 新增 `config` 属性，返回 `Configuration` 对象；未设置时终止程序。在扩展命令的 `do_run()` 实现中始终可以使用。
- 新增布尔属性 `has_config`。原文写为：“当且仅当读取 `self.config` 将终止程序时为 `True`。”
- `west.manifest` 的路径处理做出不向后兼容的整体调整，见[提交56cfe8d1d1](https://github.com/zephyrproject-rtos/west/commit/56cfe8d1d1f3c9b45de3e793c738acd62db52aca)。
- 原文所称 `west.manifest.Manifest.validate()` 现在返回验证后的 Python 字典；如果输入是字符串而后续需要字典，这很有用。
- `west.manifest.Manifest` 新增路径属性 `abspath`、`posixpath`、`relative_path`、`yaml_path`、`repo_path`、`repo_posixpath`；新增 `userdata`，保存 `manifest: self: userdata:` 的解析值或 `None`；新增 `from_topdir()` 工厂方法。
- `west.manifest.ManifestProject` 新增 `userdata`，同样保存 `manifest: self: userdata:` 的解析值或 `None`。
- `west.manifest.ManifestImportFailed` 构造函数可接受任意值，以表示从[映射（Map）](P013_west清单文件.md)或其他复合值导入失败的情况。

> 译注：核对对应的 [v0.13.0命令源码](https://github.com/zephyrproject-rtos/west/blob/v0.13.0/src/west/commands.py)，`has_config=True` 实际表示可安全访问 `self.config`，原文把条件写反了。对应的[清单源码](https://github.com/zephyrproject-rtos/west/blob/v0.13.0/src/west/manifest.py)将 `validate()` 定义为模块级函数 `west.manifest.validate()`；模块名是小写 `west.manifest`，并非 `west.Manifest`。保留上面的原文写法以便对照，实际调用应按源码与[API参考](P016_west的PythonAPI.md)。

**已弃用的配置API：**`west.configuration.config`、`west.configuration.read_config`、`west.configuration.update_config`、`west.configuration.delete_config` 被弃用，改用 `Configuration` 对象。通常从 `WestCommand` 实例的 `self.config` 获取；其他使用场景也可直接创建 `Configuration`。

## 17.11\_v0.12.0

**新功能：**

- west 可在 [MSYS2](https://www.msys2.org/) 平台工作。
- 清单可为每个项目保存任意用户数据，见[仓库用户数据](P013_west清单文件.md)。

**错误修复：**修复 `west list` 在清单仓库上的 `{sha}` 格式键，按预期输出 `N/A`（不适用，Not Applicable）。

**API改动：**新增 `west.manifest.Project.userdata`，支持项目用户数据。

## 17.12\_v0.11.1

**新功能：**`west status` 只为状态非空的项目打印输出。

**错误修复：**

- 清单解析器此前错误地允许项目名包含路径分隔符 `/`、`\`，现在会拒绝这些非法字符。若要把项目放入工作区顶层目录的子目录，使用 `path:`；若要相对于远程 `url-base:` 自定义获取 URL，使用 `repo-path:`，示例见[项目定义](P013_west清单文件.md)。
- v0.10.1 对 `west init --manifest-rev` 默认分支选择的修改，会使清单仓库处于**分离HEAD（Detached HEAD）**状态。内部改用 `git clone` 替代 `git init` 和 `git fetch` 后修复，见[议题#522](https://github.com/zephyrproject-rtos/west/issues/522)。
- `WEST_CONFIG_LOCAL` 现在能正确覆盖默认位置 `<workspace topdir>/.west/config`。
- `west update --fetch=smart` 现在能正确跳过项目修订为**轻量标签（Lightweight Tags）**时的获取；默认模式为 `smart`，它此前对**附注标签（Annotated Tags）**已经正确，仅对轻量标签进行过多余获取。标签类型见[Git标签说明](https://git-scm.com/book/en/v2/Git-Basics-Tagging)。

**其他改动：**修复议题 #522 同时引入新的限制：给出 `west init --manifest-rev` 时，其值必须是分支或标签。此前能用来获取拉取请求的 GitHub `pull/1234/head` 等“伪分支”引用，不能再传给该选项；必须在 `west init` 之后自行获取并检出这些修订。

**API改动：**

- `west.manifest.Manifest.get_projects()` 避免[议题#523](https://github.com/zephyrproject-rtos/west/issues/523)所述边界情况下的不正确结果。
- `west.manifest.Project.sha()` 能正确处理标签修订，包括轻量标签和附注标签。

## 17.13\_v0.11.0

**新功能：**

- `west update` 支持 `--narrow`、`--name-cache`、`--path-cache`；对应的[配置](P003_配置.md)为 `update.narrow`、`update.name-cache`、`update.path-cache`，可用于优化更新速度。
- `west update` 支持 `--fetch-opt`，在更新每个项目、获取远程修订时传给 `git fetch`。

**错误修复：**`west update` 默认同步项目中的 Git 子模块，以避免自首次初始化以来子模块 URL 在清单中改变导致的问题。可将 `update.sync-submodules` 设为 `false` 禁用这一行为。

**其他改动：**修正 `west.manifest` 模块 `Project` 类的**文档字符串（Docstrings）**。

## 17.14\_v0.10.1

**新功能：**`west init` 的 `--manifest-rev`（`--mr`）不再默认使用 `master`，而是查询仓库默认分支名并使用它。这样仓库从 `master` 迁移到 `main` 时，不会破坏那些未传入此选项的脚本。

## 17.15\_v0.10.0

**新功能：**项目 `submodules` 列表中的 `name` 键成为可选项。

**错误修复：**west 检查清单模式版本是否属于[版本说明](P013_west清单文件.md)中明确允许的值。此前只检查它是否比引入 `manifest: version:` 键的 west 版本更新，因而错误地接受了 `0.8.2` 等无效模式版本。

**其他改动：**清单的 `group-filter` 随导入传播。这改变了 v0.9.x 的行为：旧版本只有顶层清单的 `group-filter` 生效，忽略所有导入清单中的组过滤列表。

从 v0.10.0 起，导入清单的组过滤列表也会导入，见[组过滤与导入](P013_west清单文件.md)。未指定 `manifest: version:` 或指定至少 `0.10` 时，新行为生效；只有顶层清单显式设置 `manifest: version: 0.9` 时，才保留旧行为。模式版本规则同见清单章节。

改动原因与背景见[west拉取请求#482](https://github.com/zephyrproject-rtos/west/pull/482)。

## 17.16\_v0.9.1

**错误修复：**`west manifest --resolve` 等命令正确包含组和组过滤信息。

**其他改动：**组合 `import` 与 `group-filter` 时发出警告。这一组合的语义从 v0.10.x 起改变，详情见上面的 v0.10.0 记录。

## 17.17\_v0.9.0

**警告（Warning）：**下述 `west config` 修复存在代价：通过该命令或 `west.configuration` API 设置配置时，会删除配置文件中的注释及其他手工编辑内容。

**警告：**不建议将本版本引入的 `group-filter` 与清单导入组合使用；其行为在 west v0.10 已改变。

**新功能：**

- 清单支持[项目中的Git子模块](P013_west清单文件.md)。除克隆项目仓库自身外，还能在该仓库内克隆 [Git子模块（Git Submodules）](https://git-scm.com/book/en/v2/Git-Tools-Submodules)。
- 清单支持[项目组（Project Groups）](P013_west清单文件.md)。启用或禁用组可决定哪些项目处于活动状态，从而会被 `west update`、`west list`、`west diff`、`west status`、`west forall` 操作。
- `west update` 默认不再更新非活动项目。新增 `--group-filter`，可仅针对本次调用调整启用与禁用的组集合。
- 不指定项目参数运行 `west list`、`west diff`、`west status`、`west forall` 时，默认不打印非活动项目的信息；若命令行显式列出项目，无论活动与否都会包含其输出。
- 这些命令支持 `--all`，包括所有项目，即使项目非活动。
- `west list --format` 支持 `{groups}` 格式键。

**错误修复：**

- `west config` 与 `west.configuration` API 此前不能正确存储某些值，例如含逗号的字符串，现已修复，见[提交36f3f91e](https://github.com/zephyrproject-rtos/west/commit/36f3f91e270782fb05f6da13800f433a9c48f130)。
- 空 `manifest: self: path:` 属于无效清单；west 此前会静默接受，现在会拒绝。
- 修复 `west init -l .` 的行为问题，见[议题#435](https://github.com/zephyrproject-rtos/west/issues/435)。

**API改动：**新增 `west.manifest.Manifest.is_active()`、`west.manifest.Manifest.group_filter`；为 `west.manifest.Project` 增加 `submodules` 属性，并加入 `west.manifest.Submodule` 类型。

**其他改动：**[清单导入](P013_west清单文件.md)支持使用 `allowlist`、`blocklist` 分别替代 `whitelist`、`blacklist`。为保持兼容仍支持旧词，但文档只使用新词，即**允许列表（Allowlist）**与**阻止列表（Blocklist）**。

## 17.18\_v0.8.0

这是一个功能发行版，修改清单模式，在 `import:` 映射中支持 `path-prefix:`，同时包含其他功能与修复。

- 清单导入映射支持 `path-prefix:`，将项目及其导入仓库放入工作区子目录，见[示例3.4：导入子目录](P013_west清单文件.md)。
- west 命令行程序也可通过 `python3 -m west` 运行，更方便在不修改 [PATH环境变量](https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-PATH)的情况下选择特定 Python 解释器。
- 原文的 `west manifest –path` 用于打印 `west.yml` 的绝对路径。
- `west init` 支持 `--mf foo.yml`，以 `foo.yml` 替代 `west.yml` 初始化工作区。
- `west list` 使用 `manifest.path` 配置打印清单仓库路径；该值可能不同于清单数据中的 `self: path:`。要恢复旧行为，需要新选项 `--manifest-path-from-yaml`。
- 多项 Python API 改动，见 [west API](P016_west的PythonAPI.md)。

> 译注：原文 `–path` 使用了排版用短破折号；实际命令选项写为 `west manifest --path`，使用两个 ASCII 连字符。该命令返回绝对路径属于工具语义，示例并未固定读者的仓库位置。

## 17.19\_v0.7.3

错误修复版本：修复一次导入失败后可能使工作区无法使用的问题，详情见[拉取请求#415](https://github.com/zephyrproject-rtos/west/pull/415)。

## 17.20\_v0.7.2

错误修复与小型功能版本：

- 过滤清单导入带来的重复扩展命令。
- 修复原文所称 `west.Manifest.get_projects()` 按路径查找清单仓库时的行为。

## 17.21\_v0.7.1

错误修复与小型功能版本：

- `west update --stats` 输出调用子进程操作的耗时、每个项目在 west Python 进程中花费的时间，以及每个项目的更新总时间。
- `west topdir` 始终打印 POSIX 风格路径。
- 小幅调整控制台输出。

## 17.22\_v0.7.0

主要用户功能是[清单导入（Manifest Imports）](P013_west清单文件.md)：可从多个文件加载清单数据，并解析为一份逻辑清单。

**其他用户可见改动：**

- 本文档及 west API 文档中，将 **west安装（West Installation）**概念更名为 **west工作区（West Workspace）**；新名称对多数人更容易理解。
- 清单支持**模式版本（Schema Version）**。
- `west config` 可在工作区之外运行，例如用 `west config --global section.key value` 设置全局配置。
- 新增 `west topdir`，打印当前 west 工作区根目录。
- `west -vv init` 打印执行的 Git 操作及其结果。
- 强制执行项目不得命名为 `manifest` 的限制。该名称保留给清单仓库，可以使用 `west list manifest` 引用它，而不必只通过 `west list path-to-manifest-repository` 表达。
- 没有名为 `zephyr` 的项目时不再报错，这是让 west 也能用于非 Zephyr 场景的工作之一。
- 修复多项错误。

**开发者可见的API改动：**

- 弃用 `west.build`、`west.cmake`：这些是 Zephyr 专用功能，本不应属于 west。由于 Zephyr v1.14 LTS 依赖它们，仍保留在发行包中，计划在该 Zephyr 版本淘汰后移除。
- `west.commands.WestCommand.requires_installation` 弃用，改用新加入的 `requires_workspace`；新增 `has_manifest`；`manifest` 属性可以赋值。
- `west.configuration` 的调用方在读写配置文件时可指定工作区目录。
- `west.log` 新增 `msg()`。
- `west.manifest` 改用标准 `logging` 模块，替代 `west.log`。
- `west.manifest` 新增 `QUAL_REFS_WEST`、`SCHEMA_VERSION`，删除 `Defaults`。
- 新增 `Manifest.as_dict()`、`Manifest.as_frozen_yaml()`、`Manifest.as_yaml()`。
- `Manifest.from_file()`、`from_data()` 工厂方法更灵活，并减少对全局状态的依赖。
- 新增原文所称 `Manifest.validate()`，以及 `ManifestImportFailed`。
- `ManifestProject` 处于“半弃用（Semi-deprecated）”状态，原文称以后可能删除。
- `Project` 构造函数接受 `topdir` 参数。
- 删除 `Project.format()` 及其调用方，改用 **f字符串（f-strings）**。
- 新增 `Project.name_and_path`、`Project.remote_name`。
- `Project.sha()` 捕获标准错误 `stderr`。
- 删除 `Remote`。

本版本要求 Python 3.6 或更高版本。有些功能可能依赖 Python 字典保持插入顺序；这在 CPython 3.6 中只是实现细节，从 Python 3.7 起成为语言规范的一部分。

## 17.23\_v0.6.3

本次**修订版本（Point Release）**修复已弃用的 `west.cmake` 模块的一处行为错误。

## 17.24\_v0.6.2

本次修订版本修复 v0.6.1 引入的 `west update --fetch=smart` 行为错误。

原文要求所有 v0.6.1 使用者升级。

## 17.25\_v0.6.1

**警告：不要使用本次修订版本，应使用 v0.6.2。**

**用户可见功能：**

- [west update](P011_内置命令.md) 新增 `--fetch` 命令行选项与 `update.fetch` 配置。默认值 `smart` 会跳过本地已有 SHA 和标签的获取。
- 改善 `west diff`、`west status`、`west forall`、`west update` 的错误处理并保持一致。这些命令都可操作多个项目：某个项目相关子进程失败后，继续处理其他项目；只要任一子进程失败，west 进程就返回非零错误码，尤其此前 `west forall` 并非如此。
- [west manifest](P011_内置命令.md) 的错误处理也得到改善。
- [west list](P011_内置命令.md) 在项目未克隆时也能工作，前提是格式字符串只需要从清单文件读取的信息；若需要仓库内数据，例如包含 `{sha}` 格式键，仍会失败。
- 操作 Git 修订的命令及选项接受 SHA 缩写。例如 `west init --mr SHA_PREFIX` 可以工作；此前若不是分支或标签，`--mr` 必须使用完整 40 字符 SHA。

**开发者可见的API改动：**

- 新增 `west.log.banner()`。
- 新增 `west.log.small_banner()`。
- 新增 `west.manifest.Manifest.get_projects()`。
- 新增 `west.manifest.Project.is_cloned()`。
- `west.commands.WestCommand` 实例可在 `do_run()` 调用期间，通过新的 `self.manifest` 属性访问已解析的 `Manifest` 对象；读取时返回该对象，无法解析时中止命令。
- `west.manifest.Project.git()` 新增 `capture_stderr` 关键字参数。

## 17.26\_v0.6.0

### 17.26.1\_不再使用独立引导程序

在 west v0.5.x 中，程序分为**引导程序（Bootstrapper）**和每次安装各自保存的克隆两部分，详见 [Zephyr v1.14的多仓库管理文档](https://docs.zephyrproject.org/1.14.0/guides/west/repo-tool.html)。

这一设计类似 Google Repo，使 west 在初期能快速迭代，但也造成困惑。现在 west 已足够稳定，可以通过 **Python包索引（Python Package Index，PyPI）**整体分发。

从 v0.6.x 起，全部核心 west 命令及辅助类都属于 PyPI 分发的 `west` 包。这减少了复杂性，也让系统中的任意位置都能导入 west 模块，而不再局限于扩展命令。

为向后兼容仍保留 `selfupdate` 命令，但它只会打印错误消息后退出。

### 17.26.2\_清单语法变化

清单中的 `projects` 元素可直接指定获取 URL，例如：

```yaml
manifest:
  projects:
    - name: example-project-name
      url: https://github.com/example/example-project
```

这样设置 `url` 的项目元素不能同时包含 `remote`。

项目名必须唯一。这是支持后续功能所需的限制，但 v0.5.x 无法满足，因为不同项目的 URL 末尾路径组件可能相同，例如旧清单：

```yaml
manifest:
  remotes:
    - name: remote-1
      url-base: https://github.com/remote-1
    - name: remote-2
      url-base: https://github.com/remote-2
  projects:
    - name: project
      remote: remote-1
      path: remote-1-project
    - name: project
      remote: remote-2
      path: remote-2-project
```

现在可使用 `url` 替代 `remote`，将这类清单改写为：

```yaml
manifest:
  projects:
    - name: remote-1-project
      url: https://github.com/remote-1/project
    - name: remote-2-project
      url: https://github.com/remote-2/project
```

`west list` 新增 `{sha}` 格式键，默认格式字符串改为 `"{name:12} {path:28} {revision:40} {url}"`。

可运行 `west manifest --validate` 加载并验证当前清单；此外还修复了一些清单解析相关错误处理问题。

### 17.26.3\_不兼容的API变化

west API 做出不兼容改动；在 v1.0 宣布 API 稳定之前，预计还会继续变化。

- `west.manifest.Project` 构造函数的 `remote`、`defaults` 从位置参数改为关键字参数。新增 `url` 关键字参数；给出时直接使用该 URL，并忽略 `remote`。
- 删除 `west.manifest.MANIFEST_SECTIONS`，因为现在只存在 `manifest` 这一节；同时删除 `west.manifest.Manifest` 工厂方法与构造函数的 `sections` 关键字参数。
- 删除 `west.manifest.SpecialProject`，改用 `west.manifest.ManifestProject`。

## 17.27\_v0.5.x

west v0.5.x 是 Zephyr 项目首次广泛采用的版本，随 Zephyr v1.14 LTS 使用。其文档保存在 [Zephyr v1.14文档](https://docs.zephyrproject.org/1.14.0/guides/west/index.html)中。

主要功能：基于 Git 仓库的多仓库管理，包括 west 自身更新；**分层配置文件（Hierarchical Configuration Files）**；**扩展命令（Extension Commands）**。

## 17.28\_v0.5.x之前的版本

west 仓库中早于 v0.5.x 的标签都是原型，仅具有历史参考价值。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：west的PythonAPI](P016_west的PythonAPI.md) · [本模块主线目录](../reading/west.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：west的PythonAPI](P016_west的PythonAPI.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
