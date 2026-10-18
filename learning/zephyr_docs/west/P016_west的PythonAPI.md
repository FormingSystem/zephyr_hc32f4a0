---
id: learning.zephyr-docs.west.west_api
title: west的PythonAPI
kind: reference
status: maintained
domains: [zephyr, west, python]
source_url: https://docs.zephyrproject.org/latest/develop/west/west-apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_west的PythonAPI

原文：[West APIs](https://docs.zephyrproject.org/latest/develop/west/west-apis.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

本页介绍 [west](P014_west官方总入口.md) 提供的 **Python 应用程序编程接口（Python API）**，以及 `zephyr` 仓库中 [west扩展（West Extensions）](P012_扩展命令机制.md)使用的一些附加 API。内容包括命令、配置、旧日志模块、清单解析和辅助工具。

> 译注：下列签名保留原页的参数、默认值、类型显示和返回类型，属于 API 参考，不是可以直接执行的完整 Python 程序。系统规定的配置文件位置以及“返回绝对路径”的 API 语义按原文保留；它们不是作者仓库的绝对地址。文档之间的本地导航使用相对路径。

## 16.1\_west.commands：命令接口

所有**内置命令（Built-in Commands）**和扩展命令都实现为本模块 `WestCommand` 的子类。模块还提供若干异常类型。

### 16.1.1\_WestCommand及实例属性

<a id="west.commands.WestCommand"></a>

```text
class west.commands.WestCommand(name: str, help: str, description: str, accepts_unknown_args: bool = False, requires_workspace: bool = True, verbosity: Verbosity = Verbosity.INF)
```

west 命令的**抽象父类（Abstract Superclass）**。实例属性如下。

<a id="west.commands.WestCommand.name"></a>

`name`

值与传入构造函数的 `name` 相同。

<a id="west.commands.WestCommand.help"></a>

`help`

值与传入构造函数的 `help` 相同。内置命令需要该值，扩展命令会忽略它，见[west议题#927](https://github.com/zephyrproject-rtos/west/issues/927)。

<a id="west.commands.WestCommand.description"></a>

`description`

值与传入构造函数的 `description` 相同。

<a id="west.commands.WestCommand.accepts_unknown_args"></a>

`accepts_unknown_args`

值与传入构造函数的 `accepts_unknown_args` 相同。

<a id="west.commands.WestCommand.requires_workspace"></a>

`requires_workspace`

值与传入构造函数的 `requires_workspace` 相同。0.7.0 新增。

<a id="west.commands.WestCommand.parser"></a>

`parser`

调用 `WestCommand.add_parser()` 创建的**参数解析器（Argument Parser）**。

以下为实例**属性接口（Properties）**。

<a id="west.commands.WestCommand.manifest"></a>

`manifest`

返回当前清单文件的 `west.manifest.Manifest` 实例；如果没有提供该实例，则终止程序。仅从 `do_run()` 方法中使用这一属性才是安全的。0.6.1 新增；0.7.0 起可以赋值。

<a id="west.commands.WestCommand.has_manifest"></a>

`has_manifest`

如果读取 `manifest` 属性会成功而非报错，则为 `True`。

<a id="west.commands.WestCommand.config"></a>

`config`

可赋值属性，返回 `west.configuration.Configuration` 实例；如果没有提供，则终止程序。仅从 `do_run()` 中使用才是安全的。0.13.0 新增。

<a id="west.commands.WestCommand.has_config"></a>

`has_config`

如果读取 `config` 属性会成功而非报错，则为 `True`。0.13.0 新增。

<a id="west.commands.WestCommand.git_version_info"></a>

`git_version_info`

Git 版本信息的**元组（Tuple）**。0.11.0 新增。

<a id="west.commands.WestCommand.color_ui"></a>

`color_ui`

west 配置允许彩色输出时为 `True`，否则为 `False`。1.0.0 新增。

### 16.1.2\_构造函数

<a id="west.commands.WestCommand.__init__"></a>

```text
__init__(name: str, help: str, description: str, accepts_unknown_args: bool = False, requires_workspace: bool = True, verbosity: Verbosity = Verbosity.INF)
```

构造 west 命令的抽象父类。`name`、`help`、`description` 等字段与 `WestCommand.add_parser` 添加的 `argparse.ArgumentParser` 所需关键字参数有所重复。这是有意保留的设计：`argparse` 对 API 稳定性的保证较少，因此这里重复保存这些信息，以便适应将来的变化。

- `name`：使用者输入的命令名。
- `help`：单行命令帮助文本。
- `description`：多行命令说明。
- `accepts_unknown_args`：为真时，命令能在 `WestCommand.run` 中处理任意未知命令行参数；否则传入未知参数是致命错误。
- `requires_workspace`：为真时，命令运行需要 west 工作区；在工作区之外运行是致命错误。
- `verbosity`：命令输出的**详细程度（Verbosity）**，之后可以修改。

版本记录：0.6.0 加入 `requires_installation` 参数，该参数在 0.13.0 删除；0.7.0 加入 `requires_workspace`；0.8.0 的记录说明 `topdir` 可以是任意 `os.PathLike`；0.13.0 删除已弃用的 `requires_installation`；1.0.0 加入 `verbosity`。

> 译注：原页把 `topdir` 的历史说明放在此处，但当前构造函数签名没有这个参数；当前运行入口的 `topdir` 见下方 `run()`。不要据此给当前构造函数传入 `topdir`。

### 16.1.3\_运行、解析和子进程

<a id="west.commands.WestCommand.run"></a>

```text
run(args: Namespace, unknown: list[str], topdir: str | PathLike, manifest: Manifest | None = None, config: Configuration | None = None) → None
```

运行命令。如果**上下文（Context）**不匹配而无法运行，抛出 `west.commands.CommandContextError`；也可能抛出其他异常。

- `args`：通过 `WestCommand.add_parser` 解析出的已知参数。
- `unknown`：命令行中的未知参数；除非 `accepts_unknown_args` 为真，否则必须为空。
- `topdir`：west 工作区顶层目录；在 `WestCommand.do_run` 中可通过字符串属性 `self.topdir` 访问。
- `manifest`：`west.manifest.Manifest` 或 `None`；在 `do_run` 中通过 `self.manifest` 访问。
- `config`：`west.configuration.Configuration` 或 `None`；在 `do_run` 中通过 `self.config` 访问。

0.6.0 加入 `topdir` 参数。

<a id="west.commands.WestCommand.add_parser"></a>

`add_parser(parser_adder) → ArgumentParser`

为命令注册并返回参数解析器，同时将其保存在 `parser` 属性中。`parser_adder` 是调用 `argparse.ArgumentParser.add_subparsers()` 的返回值。

<a id="west.commands.WestCommand.add_pre_run_hook"></a>

`add_pre_run_hook(hook: Callable[[WestCommand], None]) → None`

加入一个恰好在 `do_run()` 之前调用的**钩子（Hook）**。适合将依赖命令完整初始化的工作延后执行。`hook` 是要加入的钩子。1.0.0 新增。

<a id="west.commands.WestCommand.check_call"></a>

`check_call(args, **kwargs)`

先以 `Verbosity.DBG_MORE` 级别记录调用，再运行 `subprocess.check_call(args, **kwargs)`。1.2.0 将 `cwd` 关键字参数替换为接收任意关键字参数的 `**kwargs`。原文另标记“0.11.0 变更”，未提供该次变更的说明。

<a id="west.commands.WestCommand.check_output"></a>

`check_output(args, **kwargs)`

先以 `Verbosity.DBG_MORE` 级别记录调用，再运行 `subprocess.check_output(args, **kwargs)`。1.2.0 将 `cwd` 关键字参数替换为 `**kwargs`。原文另标记“0.11.0 变更”，未提供该次变更的说明。

<a id="west.commands.WestCommand.run_subprocess"></a>

`run_subprocess(args, **kwargs)`

先以 `Verbosity.DBG_MORE` 级别记录调用，再运行 `subprocess.run(args, **kwargs)`。1.2.0 新增。

所有子类都必须提供以下**抽象方法（Abstract Methods）**，用于实现上面的接口。

<a id="west.commands.WestCommand.do_add_parser"></a>

`abstractmethod do_add_parser(parser_adder) → ArgumentParser`

子类用来注册命令行参数的方法。`WestCommand.add_parser` 调用它来注册命令的选项与参数。子类应调用 `parser_adder.add_parser()`，为该子命令添加 `ArgumentParser`，再添加参数；最后必须返回该解析器。`parser_adder` 是 `argparse.ArgumentParser.add_subparsers()` 的返回值。

<a id="west.commands.WestCommand.do_run"></a>

`abstractmethod do_run(args: Namespace, unknown: list[str])`

子类必须实现此方法；运行命令时调用它。`args` 是包含已解析参数的 `argparse.Namespace`；当 `accepts_unknown_args` 为真时，`unknown` 是未解析参数字符串的序列。

### 16.1.4\_命令输出方法

命令需要打印输出时，应使用以下方法。这些方法让代码能从已弃用的 `west.log` 迁移到每命令独立的接口，并为未来版本的 west 全局**安静模式（Quiet Mode）**提供条件。

<a id="west.commands.WestCommand.dbg"></a>

`dbg(*args, level: Verbosity = Verbosity.DBG, end: str = '\n')`

打印详细的调试消息。仅当 `self.verbosity >= level` 时输出。`args` 是要打印的参数序列，`level` 是消息的详细程度级别。1.0.0 新增；1.2.0 加入 `end` 参数。

<a id="west.commands.WestCommand.inf"></a>

`inf(*args, colorize: bool = False, end: str = '\n')`

打印信息消息，仅当 `self.verbosity >= INF` 时输出。`args` 是要打印的参数序列。当 `colorize=True`、配置项 `color.ui` 未定义或为真、且标准输出是终端时，以绿色输出。1.0.0 新增；1.2.0 加入 `end`。

<a id="west.commands.WestCommand.wrn"></a>

`wrn(*args, end: str = '\n')`

打印警告，仅当 `self.verbosity >= WRN` 时输出，消息带有前缀 `"WARNING: "`。当 `color.ui` 未定义或为真，且标准输出是终端时，以黄色输出。`args` 是要打印的参数序列。1.0.0 新增；1.2.0 加入 `end`。

<a id="west.commands.WestCommand.err"></a>

`err(*args, fatal: bool = False, end: str = '\n')`

打印错误，仅当 `self.verbosity >= ERR` 时输出。此方法不会终止程序；需要终止时应使用 `die()`。当 `color.ui` 未定义或为真，且标准输出是终端时，以红色输出。`args` 是要打印的参数序列；`fatal=True` 时前缀为 `"FATAL ERROR: "`，否则为 `"ERROR: "`。1.0.0 新增；1.2.0 加入 `end`。

<a id="west.commands.WestCommand.die"></a>

`die(*args, exit_code: int = 1) → NoReturn`

通过 `err()` 打印致命错误并终止程序。`args` 是要打印的参数序列，`exit_code` 是终止程序时使用的退出码。原文称其等价于 `die(*args, fatal=True)`，随后尝试以给定退出码终止。1.0.0 新增。

> 译注：上述等价调用是原文笔误。核对 [west 1.5.0的命令实现](https://github.com/zephyrproject-rtos/west/blob/v1.5.0/src/west/commands.py)，实际调用的是 `self.err(*args, fatal=True)`；正常情况下随后执行 `sys.exit(exit_code)`。当详细程度达到 `DBG_EXTREME` 时，实现会改为抛出 `RuntimeError` 以显示调用栈，并忽略 `exit_code`。这条实现补充不改变本页所保留的官方签名。

<a id="west.commands.WestCommand.banner"></a>

`banner(*args)`

通过 `inf()` 将 `args` 打印为**横幅（Banner）**，添加前缀 `'=== '`，默认着色。1.0.0 新增。

<a id="west.commands.WestCommand.small_banner"></a>

`small_banner(*args)`

打印较小的横幅：为 `args` 添加前缀 `'– '`，不着色。1.0.0 新增。

### 16.1.5\_Verbosity枚举

从 west v1.0 开始，命令应通过 `WestCommand.dbg()`、`WestCommand.inf()` 等方法输出。以下枚举用于声明输出的详细程度。

<a id="west.commands.Verbosity"></a>

`class west.commands.Verbosity(*values)`

`WestCommand` 实例使用的详细程度级别。该枚举在 1.0.0 新增。

<a id="west.commands.Verbosity.QUIET"></a>

`QUIET = 0`

调用 `WestCommand.dbg()`、`.inf()` 等方法时不打印任何内容。

<a id="west.commands.Verbosity.ERR"></a>

`ERR = 1`

只打印错误消息。

<a id="west.commands.Verbosity.WRN"></a>

`WRN = 2`

只打印错误和警告。

<a id="west.commands.Verbosity.INF"></a>

`INF = 3`

打印错误、警告和信息消息。

<a id="west.commands.Verbosity.DBG"></a>

`DBG = 4`

在信息级别基础上，额外打印 `WestCommand.dbg(…, level=Verbosity.DBG)` 的输出。

<a id="west.commands.Verbosity.DBG_MORE"></a>

`DBG_MORE = 5`

在 `DBG` 基础上，额外打印 `WestCommand.dbg(…, level=Verbosity.DBG_MORE)` 的输出。

<a id="west.commands.Verbosity.DBG_EXTREME"></a>

`DBG_EXTREME = 6`

在 `DBG_MORE` 基础上，额外打印 `WestCommand.dbg(…, level=Verbosity.DBG_EXTREME)` 的输出。

> 译注：原文描述后三级时用了 `INFO`、`DEBUG`、`DEBUG_MORE`；实际枚举成员名为签名中列出的 `INF`、`DBG`、`DBG_MORE`。

### 16.1.6\_命令异常

<a id="west.commands.CommandError"></a>

`class west.commands.CommandError(returncode=1)`

基类为 `RuntimeError`，表示命令失败。

<a id="west.commands.CommandError.returncode"></a>

`returncode`

针对此错误建议采用的程序退出码。

<a id="west.commands.CommandContextError"></a>

`class west.commands.CommandContextError(returncode=1)`

基类为 `CommandError`，表示依赖上下文的命令无法运行。

## 16.2\_west.configuration：配置接口

本模块处理 west 配置文件。west 的文件位置约定类似 Git：**系统级（System）**配置适用于本机所有使用者，**全局／用户级（Global）**配置适用于当前使用者，**本地／工作区级（Local）**配置适用于当前 west 工作区。

| 层级 | 平台 | 官方规定的位置 |
| --- | --- | --- |
| 系统级 | Linux | `/etc/westconfig` |
| 系统级 | macOS | `/usr/local/etc/westconfig` |
| 系统级 | Windows | `%PROGRAMDATA%\west\config` |
| 全局级 | Linux | `~/.westconfig`；若设置了 `$XDG_CONFIG_HOME`，则为 `$XDG_CONFIG_HOME/west/config` |
| 全局级 | macOS | `~/.westconfig` |
| 全局级 | Windows | `os.path.expanduser` 确定的用户主目录中的 `.westconfig` |
| 本地级 | Linux、macOS、Windows | `<workspace-topdir>/.west/config` |

可使用环境变量 `WEST_CONFIG_SYSTEM`、`WEST_CONFIG_GLOBAL`、`WEST_CONFIG_LOCAL` 覆盖相应文件的位置。后读取配置文件中的值覆盖前面的值；本地级优先级最高，系统级最低。

从 west v0.13 开始，推荐使用 `west.configuration.Configuration` 读取配置。编写 west 扩展时，可以通过 `self.config` 访问当前 `Configuration` 对象，见 `WestCommand`。

### 16.2.1\_ConfigFile与Configuration

以下是 west v0.13 起推荐使用的配置 API。

<a id="west.configuration.ConfigFile"></a>

`class west.configuration.ConfigFile(*values)`

west 配置文件类型枚举：`SYSTEM` 是所有使用者共享的系统级配置；`GLOBAL` 是全局或用户级配置；`LOCAL` 是每工作区配置；`ALL` 在适用时表示以上三者。

<a id="west.configuration.Configuration"></a>

`class west.configuration.Configuration(topdir: str | PathLike | None = None)`

表示可用配置选项及其值，允许读取、设置和删除系统、全局、本地配置文件中的选项。设置值会立即影响文件，且不防护并发读取；调用方负责必要的**互斥（Mutual Exclusion）**。

`WEST_CONFIG_*` 环境变量只在创建 `Configuration` 对象时生效，因此可以让不同对象指向不同文件。如果构造时没有提供 `topdir`，也没有定义 `WEST_CONFIG_LOCAL`，该对象不指向任何本地配置文件。0.13.0 新增。

<a id="west.configuration.Configuration.delete"></a>

`delete(option: str, configfile: ConfigFile | None = None) → None`

从指定的一个或多个文件中删除选项。如果 `option` 没有在所指定的 `configfile` 中设置，抛出 `KeyError`。

- `option`：要删除的选项，形如 `'foo.bar'`。
- `configfile=ConfigFile.ALL`：从所有设置了该选项的文件中删除。
- `configfile=None`：只从设置了该选项且优先级最高的文件中删除。
- 其他 `configfile` 值：从指定的 `ConfigFile` 删除。

<a id="west.configuration.Configuration.get"></a>

`get(option: str, default: str | None = None, configfile: ConfigFile = ConfigFile.ALL) → str | None`

以字符串获取选项值。`option` 形如 `'foo.bar'`；`default` 是选项缺失时返回的默认值；`configfile` 指定要从哪类配置文件查找。

<a id="west.configuration.Configuration.getboolean"></a>

`getboolean(option: str, default: bool = False, configfile: ConfigFile = ConfigFile.ALL) → bool`

以布尔值获取选项值。对找到的值应用 `configparser` 模块的布尔转换；非法值抛出 `ValueError`。`option` 形如 `'foo.bar'`；`default` 是选项缺失时的默认值；`configfile` 指定查找的文件类型。

<a id="west.configuration.Configuration.getfloat"></a>

`getfloat(option: str, default: float | None = None, configfile: ConfigFile = ConfigFile.ALL) → float | None`

以浮点数获取选项值。`option` 形如 `'foo.bar'`；`default` 是选项缺失时的默认值；`configfile` 指定查找的文件类型。

<a id="west.configuration.Configuration.getint"></a>

`getint(option: str, default: int | None = None, configfile: ConfigFile = ConfigFile.ALL) → int | None`

以整数获取选项值。`option` 形如 `'foo.bar'`；`default` 是选项缺失时的默认值；`configfile` 指定查找的文件类型。

<a id="west.configuration.Configuration.items"></a>

`items(configfile: ConfigFile = ConfigFile.ALL) → Iterable[tuple[str, Any]]`

返回由“选项、值”对构成的**迭代器（Iterator）**。

<a id="west.configuration.Configuration.set"></a>

`set(option: str, value: Any, configfile: ConfigFile = ConfigFile.LOCAL) → None`

设置配置选项。写入配置文件立即生效。从创建该 `Configuration` 对象开始到调用此方法之间，对并发访问没有保护；如果文件可能在这期间被修改，应先创建新的 `Configuration` 对象再调用此方法，否则会丢失期间发生的修改。

`option` 是形如 `'foo.bar'` 的选项；`value` 是要设置的值；`configfile` 是写入的配置文件类型。

### 16.2.2\_已弃用的配置API

以下 API 也使用 `ConfigFile`，但默认操作一个保存当前工作区配置的全局对象。由于 west API 可用于多个工作区，这被证明是一个不合适的设计；这些 API 自 west v0.13.0 起**弃用（Deprecated）**。

保留它们是为了兼容旧扩展。如果新代码可以要求 west v0.13.0 或更高版本，就不应使用这些 API。

<a id="west.configuration.read_config"></a>

```text
west.configuration.read_config(configfile: ConfigFile | None = None, config: ConfigParser = <configparser.ConfigParser object>, topdir: str | PathLike | None = None) → None
```

将 `configfile` 指定文件的配置读入 `configparser.ConfigParser` 对象 `config`。未提供 `config` 时使用全局 `west.configuration.config`。给出 `configfile` 时只读它指明的文件；未给出时使用 `ConfigFile.ALL`。

如果需要读取本地配置，即选择 `ConfigFile.LOCAL` 或 `ConfigFile.ALL`，按以下顺序确定位置：给出 `topdir` 时读取 `topdir/.west/config`；否则，若环境变量 `WEST_CONFIG_LOCAL` 已设置，使用它指向的文件；再否则搜索文件系统寻找本地配置，找不到时忽略这一情况。

`configfile` 是 `west.configuration.ConfigFile`；`config` 是读入目标配置对象；`topdir` 是读取本地配置的 west 工作区根目录。

0.8.0 删除已弃用的 `read_config` 参数；0.6.0 起忽略因找不到本地配置文件产生的错误。

<a id="west.configuration.update_config"></a>

```text
west.configuration.update_config(section: str, key: str, value: Any, configfile: ConfigFile = ConfigFile.LOCAL, topdir: str | PathLike | None = None) → None
```

在指定配置文件中将 `section.key` 设置为 `value`。

- `section`：配置节，不存在时创建。
- `key`：该节中要设置的键。
- `value`：要写入的值。
- `configfile`：`west.configuration.ConfigFile`，不得为 `ALL`。
- `topdir`：写入本地配置的 west 工作区根目录。

目标文件由 `configfile` 决定。默认的 `ConfigFile.LOCAL` 按顺序选择：已给出 `topdir` 时使用 `topdir/.west/config`；否则使用已设置的 `WEST_CONFIG_LOCAL` 值；再否则通过搜索文件系统查找 west 工作区的本地配置文件，找不到则抛出 `WestNotFound`。

<a id="west.configuration.west.configuration.config"></a>

`west.configuration.config`

模块级全局 `ConfigParser` 实例，保存当前配置。读取前应使用 `west.configuration.read_config()` 初始化。

## 16.3\_west.log：已弃用的日志接口

此模块使用全局状态，使 west 更难进行单元测试，因此已弃用，讨论见[west议题#149](https://github.com/zephyrproject-rtos/west/issues/149)。原文说明不早于 west v2.0 移除。今后的命令应使用等效的 `WestCommand` 方法，例如以 `WestCommand.dbg()` 替代 `west.log.dbg()`。

这些公共输出方法遵循 `color.ui` 配置和详细程度级别；过去曾推荐 `WestCommand` 实例使用它们。

### 16.3.1\_全局详细程度

通过 `set_verbosity()` 设置全局详细程度。

<a id="west.log.set_verbosity"></a>

`west.log.set_verbosity(value)`

设置日志详细程度；`value` 是目标级别，例如 `VERBOSE_VERY`。可用级别如下。

<a id="west.log.VERBOSE_NONE"></a>

`west.log.VERBOSE_NONE = 0`

默认级别，不打印 `dbg()` 消息。

<a id="west.log.VERBOSE_NORMAL"></a>

`west.log.VERBOSE_NORMAL = 1`

打印部分详细消息。

<a id="west.log.VERBOSE_VERY"></a>

`west.log.VERBOSE_VERY = 2`

打印非常详细的消息。

<a id="west.log.VERBOSE_EXTREME"></a>

`west.log.VERBOSE_EXTREME = 3`

打印极其详细的消息。

### 16.3.2\_输出函数

主要函数是 `dbg()`、`inf()`、`wrn()`、`err()`、`die()`。还提供 `inf()` 的两种特殊形式 `banner()` 和 `small_banner()`，用于把输出组织为分节。

<a id="west.log.dbg"></a>

`west.log.dbg(*args, level=1)`

打印详细调试日志消息。`args` 是要打印的参数序列；`level` 是详细程度级别，例如 `VERBOSE_VERY`。仅当 `level` 不大于当前详细程度时打印。

<a id="west.log.inf"></a>

`west.log.inf(*args, colorize=False)`

打印信息消息。`args` 是要打印的参数序列。当 `colorize=True`、`color.ui` 未定义或为真、且标准输出是终端时，以绿色输出。

<a id="west.log.wrn"></a>

`west.log.wrn(*args)`

打印警告，`args` 是要打印的参数序列，消息带有 `"WARNING: "` 前缀。当 `color.ui` 未定义或为真、且标准输出是终端时，以黄色输出。

<a id="west.log.err"></a>

`west.log.err(*args, fatal=False)`

打印错误但不终止程序；需要终止时使用 `die()`。`args` 是要打印的参数序列；`fatal=True` 时使用前缀 `"FATAL ERROR: "`，否则使用 `"ERROR: "`。当 `color.ui` 未定义或为真、且标准输出是终端时，以红色输出。

<a id="west.log.die"></a>

`west.log.die(*args, exit_code=1) → NoReturn`

打印致命错误并终止程序。`args` 是要打印的参数序列，`exit_code` 是程序终止时使用的退出码。原文称其等价于 `die(*args, fatal=True)`，随后尝试以给定退出码终止。

> 译注：这里同样存在等价调用笔误。核对 [west 1.5.0的日志实现](https://github.com/zephyrproject-rtos/west/blob/v1.5.0/src/west/log.py)，实际调用 `err(*args, fatal=True)` 后执行 `sys.exit(exit_code)`；不要递归调用 `die(..., fatal=True)`。

<a id="west.log.banner"></a>

`west.log.banner(*args)`

以 `inf()` 级别将 `args` 输出为横幅，添加前缀 `'=== '`，默认着色。

<a id="west.log.small_banner"></a>

`west.log.small_banner(*args)`

输出较小的横幅，为 `args` 添加前缀 `'– '`，不着色。

## 16.4\_west.manifest：清单解析

本模块提供 west **清单（Manifest）**的解析器与**抽象数据类型（Abstract Data Types）**。主要类是 `Manifest` 和 `Project`，用于表示清单文件的内容。推荐通过 `Manifest.from_topdir()` 解析 west 清单。

### 16.4.1\_常量与函数

<a id="west.manifest.MANIFEST_PROJECT_INDEX"></a>

`west.manifest.MANIFEST_PROJECT_INDEX = 0`

工作区的 `ManifestProject` 实例在 `Manifest.projects` 中的索引。

<a id="west.manifest.MANIFEST_REV_BRANCH"></a>

`west.manifest.MANIFEST_REV_BRANCH = 'manifest-rev'`

指向最近一次 `Project` 更新位置的 Git 修订。

<a id="west.manifest.QUAL_MANIFEST_REV_BRANCH"></a>

`west.manifest.QUAL_MANIFEST_REV_BRANCH = 'refs/heads/manifest-rev'`

`MANIFEST_REV_BRANCH` 的**完全限定引用（Fully Qualified Reference）**。

<a id="west.manifest.QUAL_REFS_WEST"></a>

`west.manifest.QUAL_REFS_WEST = 'refs/west/'`

west 内部使用的 Git 引用命名空间。

<a id="west.manifest.SCHEMA_VERSION"></a>

`west.manifest.SCHEMA_VERSION = '1.2'`

当前 west 程序支持的最新**清单模式版本（Manifest Schema Version）**。当新版 west 引入旧版不支持的清单文件功能时，这个值会改变。west v1.0.x 发布后，它改为 `1.0`，使使用者可以指定“模式版本 1”，不必继续使用此前的 `0.13`。上方常量值 `1.2` 是本页基线中的值。

<a id="west.manifest.manifest_path"></a>

`west.manifest.manifest_path() → str`

返回当前工作区清单文件的绝对路径。可能抛出：在 west 工作区之外调用时的 `west.util.WestNotFound`；配置文件没有 `manifest.path` 键时的 `MalformedConfig`；以及按 `manifest.path` 和 `manifest.file` 确定的位置不存在清单文件时的 `FileNotFoundError`。

<a id="west.manifest.validate"></a>

`west.manifest.validate(data: Any) → dict[str, Any]`

验证清单数据。如果当前 west 版本无法合法加载数据，则抛出异常。即使验证通过，真正加载时仍可能因清单导入无法解析而失败。

返回验证后的 YAML 字典；如果输入是字符串而后续还需要加载，返回值可以直接复用。`data` 是字符串形式或对象形式的 YAML 清单数据。0.13.0 起返回包含已解析 YAML 数据的验证后字典。

### 16.4.2\_Manifest构造与属性

<a id="west.manifest.Manifest"></a>

```text
class west.manifest.Manifest(*, source_data: str | dict | None = None, topdir: str | ~os.PathLike | None = None, config: ~west.configuration.Configuration | None = None, importer: ~typing.Callable[[~west.manifest.Project, str], str | list[str] | None] | None = None, import_flags: ~west.manifest.ImportFlag = <ImportFlag.DEFAULT: 0>, internal_import_ctx: ~west.manifest._import_ctx | None = None)
```

表示 west 清单文件解析后的内容。

<a id="west.manifest.Manifest.__init__"></a>

```text
__init__(*, source_data: str | dict | None = None, topdir: str | ~os.PathLike | None = None, config: ~west.configuration.Configuration | None = None, importer: ~typing.Callable[[~west.manifest.Project, str], str | list[str] | None] | None = None, import_flags: ~west.manifest.ImportFlag = <ImportFlag.DEFAULT: 0>, internal_import_ctx: ~west.manifest._import_ctx | None = None)
```

与直接实例化相比，使用某个**工厂方法（Factory Method）**可能更方便。实例属性如下。

| 属性 | 含义 |
| --- | --- |
| `abspath` | 清单文件的绝对路径，或 `None`。 |
| `posixpath` | 与 `abspath` 相同，但以正斜杠 `/` 分隔。 |
| `relative_path` | 清单文件相对工作区顶层目录的路径，即 `manifest.path` 与 `manifest.file` 的组合，或 `None`。 |
| `yaml_path` | 清单 YAML 中 `self: path:` 字段的值，或 `None`。 |
| `repo_path` | 从工作区顶层目录到清单仓库的相对文件系统路径字符串，或 `None`。 |
| `repo_abspath` | 清单仓库的绝对文件系统路径字符串，符号链接已解析，或 `None`。 |
| `repo_posixpath` | 与 `repo_abspath` 相同，但以正斜杠分隔。 |
| `topdir` | 工作区顶层目录字符串，符号链接已解析，或 `None`。 |
| `projects` | `Project` 实例序列。 |
| `has_imports` | 布尔值：`self:` 或 `projects:` 中存在未被 `import_flags` 或 `manifest.project-filter` 忽略的 `import:` 属性时为 `True`，否则为 `False`。 |
| `group_filter` | 等效于已解析清单及导入清单中的 `group-filter:` 的组过滤值，可能比实际输入数据更简化。 |

`topdir` 与 `source_data` 两个关键字参数必须且只能提供一个：前者从工作区加载清单，后者在没有工作区的情况下加载数据。

提供 `topdir` 时：

- 如果已经加载好所需工作区配置，可同时提供 `config`。解析器利用其中的 `manifest.path` 和 `manifest.file` 找到清单文件；调用方负责保证它确实是从该 `topdir` 正确加载的配置。
- 如果未提供 `config`，构造函数会自行创建正确的 `Configuration` 对象。
- 返回结果中的绝对路径以 `topdir` 为基准。如果 `topdir` 不是绝对路径，会先对它做路径解析，包括解析符号链接；如果已经是绝对路径，则不再进行这一解析。

提供 `source_data` 时：

- 不得同时提供 `config`。
- 除非提供 `importer`，或者用 `import_flags` 忽略导入，否则清单导入会失败。
- 结果中的所有绝对路径，例如 `projects[i].abspath`，都为 `None`。

若给出 `importer`，它必须是**可调用对象（Callable）**。当构造函数必须导入本地文件系统中找不到的清单数据时，以 `importer(project, file)` 的形式调用它：`project` 为 `west.manifest.Project`，`file` 为缺少的清单文件。

回调通常应返回 `refs/heads/manifest-rev` 对应版本的文件内容；为此，可能需要先从项目远程 URL 获取其修订并更新该引用。返回值应是包含清单数据的字符串；若 `file` 是包含 YAML 文件的目录，则应返回字符串列表。返回 `None` 会使这次导入被忽略。

可能抛出的异常为：清单数据无效时的 `MalformedManifest`；导入失败时的 `ManifestImportFailed`；根据模式版本判断当前 west 过旧、无法解析时的 `ManifestVersionError`；无法打开文件时的 `OSError` 或其子类；以及其他参数无效时的 `ValueError`。

完整参数含义：

- `source_data`：已解析 YAML 的 Python 对象，或包含未解析 YAML 的字符串。
- `topdir`：west 工作区顶层目录。
- `config`：可选的、预先从 `topdir` 加载的配置。
- `importer`：提供缺少的清单导入数据。
- `import_flags`：控制导入解析的**位掩码（Bit Mask）**。
- `internal_import_ctx`：仅供内部使用；不要使用它。

版本记录：0.7.0 加入 `importer`、`import_flags` 关键字参数。0.13.0 将所有参数改为只能按关键字传入，删除 `source_file`（改用 `topdir`），且不再抛出 `WestNotFound`；同版加入 `config` 参数，以及 `abspath`、`posixpath`、`relative_path`、`yaml_path`、`repo_path`、`repo_posixpath`、`userdata` 属性。

### 16.4.3\_Manifest工厂方法

<a id="west.manifest.Manifest.from_topdir"></a>

```text
static from_topdir(topdir: str | ~os.PathLike | None = None, config: ~west.configuration.Configuration | None = None, importer: ~typing.Callable[[~west.manifest.Project, str], str | list[str] | None] | None = None, import_flags: ~west.manifest.ImportFlag = <ImportFlag.DEFAULT: 0>) → Manifest
```

根据工作区顶层目录创建 `Manifest`。未给出 `topdir` 时，默认从当前工作目录开始寻找当前 west 工作区的清单文件。`topdir` 是工作区顶层目录，`config`、`importer`、`import_flags` 原样传给 `Manifest()`。0.13.0 新增。

<a id="west.manifest.Manifest.from_file"></a>

```text
static from_file(source_file: str | ~os.PathLike | None = None, importer: ~typing.Callable[[~west.manifest.Project, str], str | list[str] | None] | None = None, import_flags: ~west.manifest.ImportFlag = <ImportFlag.DEFAULT: 0>) → Manifest
```

根据源 YAML 文件创建 `Manifest`。未给出 `source_file` 时，默认从当前工作目录开始寻找并解析当前工作区清单，与 `from_topdir()` 的行为一致。

给出 `source_file` 时，从该文件所在位置开始查找 `topdir`。这个工厂方法特别允许从工作区内任意 Git 仓库中的任意文件加载清单；此时 `manifest.path`、`manifest.file` 无须指向 `source_file`。这适用于在既有工作区中加载替代清单，例如比较两份清单。

找不到 `topdir` 时抛出 `west.util.WestNotFound`，搜索起点为 `source_file` 或当前工作目录；找不到包含 `source_file` 的 Git 仓库时抛出 `CalledProcessError`；还可能抛出 `Manifest` 构造函数的其他异常。

`source_file` 是要加载的源文件；`importer`、`import_flags` 传给 `Manifest()`。

版本记录：0.7.0 加入 `**kwargs`；0.8.0 起 `source_file`、`manifest_path`、`topdir` 可为任意 `os.PathLike`；0.13.0 删除 `manifest_path` 与 `topdir` 参数。

<a id="west.manifest.Manifest.from_data"></a>

```text
static from_data(source_data: str | dict, importer: ~typing.Callable[[~west.manifest.Project, str], str | list[str] | None] | None = None, import_flags: ~west.manifest.ImportFlag = <ImportFlag.DEFAULT: 0>) → Manifest
```

从已解析 YAML 数据创建 `Manifest`，不读取任何配置文件。设返回值为 `m`，则 `m.projects[1].path` 等项目相对路径来自 `source_data`；所有项目绝对路径均为 `None`。可能抛出与 `Manifest` 构造函数相同的异常。

`source_data` 可为已解析 YAML 的 Python 对象，也可为未解析 YAML 字符串；`importer`、`import_flags` 传给 `Manifest`。

0.7.0 加入 `**kwargs`，并允许 `source_data` 为字符串；0.13.0 删除 `manifest_path` 与 `topdir` 参数。

### 16.4.4\_项目查找、解析结果与活动状态

下列方法便于通过名称或其他标识访问子对象。

<a id="west.manifest.Manifest.get_projects"></a>

`get_projects(project_ids: Iterable[str | PathLike], allow_paths: bool = True, only_cloned: bool = False) → list[Project]`

根据 `project_ids` 获取清单中的 `Project` 对象列表。`project_ids` 为空时，返回 `self.projects` 的列表副本；否则，结果顺序与输入标识的顺序相同。

如果包含未知项目标识，或者在 `only_cloned=True` 时发现尚未克隆的项目，抛出 `ValueError`。该异常的 `args` 是二元组：索引 0 为未知项目标识列表，索引 1 为尚未克隆的 `Project` 对象列表。

- `project_ids`：以名称或绝对／相对路径标识的项目序列。先匹配名称；可用 `allow_paths` 禁止路径检查。
- `allow_paths`：为假时，认为输入只包含名称，不包含路径。
- `only_cloned`：为真时，遇到尚未克隆的项目就抛出异常。

0.6.1 新增；0.8.0 起输入序列可以包含任意 `os.PathLike`。

以下为其他方法。

<a id="west.manifest.Manifest.as_dict"></a>

`as_dict(active_only: bool = False) → dict`

返回表示当前对象、已**完全解析（Fully Resolved）**的字典：结果如同全部项目都定义在单一清单中，没有任何 `import` 属性。`active_only` 表示不解析非活动项目。此方法在 0.7.0 新增；`active_only` 在 1.4.0 新增。

<a id="west.manifest.Manifest.as_frozen_dict"></a>

`as_frozen_dict(active_only: bool = False) → dict`

返回表示当前对象的**冻结（Frozen）**字典：所有项目修订都改为其 `QUAL_MANIFEST_REV_BRANCH` 引用所指向的完整 SHA。无法解析某个项目的 SHA 时抛出 `RuntimeError`。`active_only` 表示不冻结非活动项目，在 1.4.0 新增。

<a id="west.manifest.Manifest.as_yaml"></a>

`as_yaml(active_only: bool = False, **kwargs) → str`

返回当前对象的完全解析 YAML 表示，如同全部项目定义在单一清单中且不存在 `import` 属性。`active_only` 表示不解析非活动项目；`kwargs` 传给 `yaml.safe_dump()`。方法在 0.7.0 新增，`active_only` 在 1.4.0 新增。

<a id="west.manifest.Manifest.as_frozen_yaml"></a>

`as_frozen_yaml(active_only: bool = False, **kwargs) → str`

返回当前对象的冻结 YAML 表示，所有项目修订使用 `QUAL_MANIFEST_REV_BRANCH` 所指向的完整 SHA。无法解析项目 SHA 时抛出 `RuntimeError`。`active_only` 表示不冻结非活动项目；`kwargs` 传给 `yaml.safe_dump()`。方法在 0.7.0 新增，`active_only` 在 1.4.0 新增。

<a id="west.manifest.Manifest.is_active"></a>

`is_active(project: Project, extra_filter: Iterable[str] | None = None) → bool`

判断项目是否处于**活动状态（Active）**。

设置了 `manifest.project-filter` 时，按该选项的元素匹配项目名：元素中的正则表达式匹配后，前缀 `+` 表示活动，`-` 表示非活动。多个元素匹配时，最后一个匹配项决定结果。函数相应返回 `True` 或 `False`；使用的是创建这个 `Manifest` 对象时的配置值。

其他情况下，结果取决于项目是否有组，以及组是否启用：

- `project.groups` 为空的项目始终活动，返回 `True`。
- 组列表非空时，只要其中任意组被清单的 `group-filter:` 启用，就返回 `True`；如果有工作区，还同时考虑本地配置 `manifest.group-filter`。
- 所有组都被禁用时返回 `False`。

非活动项目在更新、列出项目、解析导入等场景中通常应视为不在工作区内。

`project` 是要检查的项目；`extra_filter` 是可选的附加组过滤器。0.9.0 新增；1.1.0 起遵循 `manifest.project-filter`，相关选项见[内置配置选项](P003_配置.md)。

> 译注：原文先讨论已配置的项目过滤器，随后讨论组过滤；[west 1.5.0的清单实现](https://github.com/zephyrproject-rtos/west/blob/v1.5.0/src/west/manifest.py)是在“有项目正则匹配”时由最后一次匹配决定结果，没有匹配项则继续按组判断。不能把“设置了过滤器”理解为所有未匹配项目都被禁用。此处与[清单文件](P013_west清单文件.md)中的规则一致。

### 16.4.5\_ImportFlag导入标志

<a id="west.manifest.ImportFlag"></a>

`class west.manifest.ImportFlag(*values)`

解析清单时用于处理导入的位标志。即使指定 `IGNORE` 或 `IGNORE_PROJECTS`，`import:` 中的 `path-prefix:` 仍影响项目自身。例如：

```yaml
manifest:
  projects:
  - name: foo
    import:
      path-prefix: bar
```

无论是否给出 `IGNORE` 或 `IGNORE_PROJECTS`，项目 `foo` 的路径都是 `bar/foo`。这样可以保证：即使忽略了导入的其他项目，该 `Project` 自身的 `path` 仍与正常导入时一致。

> 译注：这是说明 `path-prefix` 关系的原始片段，省略了项目来源。实际清单仍须为 `foo` 提供 `url`，或通过 `remote`／默认远程确定 URL；把上面片段单独交给 west 1.5.0 解析，会因缺少项目来源而报 `MalformedManifest`。忽略导入不会跳过这项清单合法性检查。

<a id="west.manifest.ImportFlag.DEFAULT"></a>

`DEFAULT = 0`

默认值为 `0`：读取文件系统来解析 `self: import:`，运行 Git 来解析 `projects:` 中的导入。

<a id="west.manifest.ImportFlag.IGNORE"></a>

`IGNORE = 1`

忽略 `self:` 和 `projects:` 中通过 `import:` 添加的项目。

<a id="west.manifest.ImportFlag.FORCE_PROJECTS"></a>

`FORCE_PROJECTS = 2`

对 `projects:` 中的导入始终调用 `importer` 回调。

<a id="west.manifest.ImportFlag.IGNORE_PROJECTS"></a>

`IGNORE_PROJECTS = 4`

仅忽略 `projects:` 中通过 `import:` 添加的项目；仍包括 `self:` 中通过 `import:` 添加的项目。

### 16.4.6\_Project项目对象

<a id="west.manifest.Project"></a>

```text
class west.manifest.Project(name: str, url: str, description: str | None = None, revision: str | None = None, path: str | PathLike | None = None, submodules: list[Submodule] | bool = False, clone_depth: int | None = None, west_commands: str | list[str] | None = None, topdir: str | PathLike | None = None, remote_name: str | None = None, groups: list[str] | None = None, userdata: Any | None = None)
```

表示 west 清单定义的项目。属性如下。

| 属性 | 含义 |
| --- | --- |
| `name` | 项目的唯一名称。 |
| `description` | 项目描述。 |
| `url` | 获取项目的 URL。 |
| `revision` | 更新项目时，从 `url` 获取的修订。 |
| `path` | 项目在工作区内的相对路径；已设置 `topdir` 时，相对于该目录。 |
| `abspath` | 本机路径格式的项目绝对路径；`topdir` 为 `None` 时也为 `None`。 |
| `posixpath` | 与 `abspath` 相同，但使用 `/` 作为分隔符。 |
| `clone_depth` | 首次克隆时获取的深度，或 `None`；使用此项时 `revision` 不应为 SHA。 |
| `west_commands` | 声明项目扩展命令的 YAML 文件列表。 |
| `topdir` | 项目所属 west 工作区的顶层目录，或 `None`。 |
| `remote_name` | 克隆时要设置的远程名称，默认 `'origin'`。 |
| `groups` | 清单给出的项目组列表；清单没有指定组时为空列表。 |
| `submodules` | 项目的子模块配置：`Submodule` 对象列表或布尔值。 |
| `userdata` | 清单中解析后的 `userdata` 字段，或 `None`。 |

版本记录：

- 0.7.0 删除 `remote` 属性，因为加入清单导入键后无法继续维持其语义；同版加入 `remote_name` 与 `name_and_path` 属性。
- 0.8.0 起 `west_commands` 始终为列表，此前可能为字符串或 `None`。
- 原文记载 0.9.0 加入 `group_filter`、`submodules` 属性。
- 0.12.0 加入 `userdata`。
- 1.2.0 加入 `description`。

> 译注：版本记录中的 `group_filter` 保留原文写法；本类当前项目组属性是 `groups`，不要据此访问不存在的 `Project.group_filter`。清单级的 `group_filter` 属于 `Manifest`。

**构造函数：**

<a id="west.manifest.Project.__init__"></a>

```text
__init__(name: str, url: str, description: str | None = None, revision: str | None = None, path: str | PathLike | None = None, submodules: list[Submodule] | bool = False, clone_depth: int | None = None, west_commands: str | list[str] | None = None, topdir: str | PathLike | None = None, remote_name: str | None = None, groups: list[str] | None = None, userdata: Any | None = None)
```

构造项目对象。如果 `topdir=None`，绝对路径属性 `abspath`、`posixpath` 也为 `None`。

- `name`：清单中的项目 `name:` 属性。
- `description`：项目描述，或 `None`。
- `url`：获取 URL。
- `revision`：要获取的修订。
- `path`：相对于 `topdir` 的路径；为 `None` 时采用 `name`。
- `submodules`：项目内要拉取的子模块。
- `clone_depth`：首次克隆的深度。
- `west_commands`：项目中的 west 命令规范 YAML 文件路径，相对于项目根目录；也可为这些路径的列表。
- `topdir`：west 工作区顶层目录。
- `remote_name`：克隆项目时设置的远程名称，默认为 `'origin'`。
- `groups`：从清单数据得到、已经转换为字符串并完成验证的项目组列表。

签名中的 `userdata` 对应前述解析后的用户数据属性。0.8.0 起 `path` 与 `topdir` 可为任意 `os.PathLike`；0.7.0 曾对参数做出与此前版本不兼容的修改。

### 16.4.7\_Project的方法

<a id="west.manifest.Project.as_dict"></a>

`as_dict() → dict`

返回当前对象的字典表示，形式与从等效 YAML 清单中解析得到的结果相同。0.7.0 新增。

<a id="west.manifest.Project.git"></a>

```text
git(cmd: str | list[str], extra_args: Iterable[str] = (), capture_stdout: bool = False, capture_stderr: bool = False, check: bool = True, cwd: str | PathLike | None = None) → CompletedProcess
```

在项目仓库中运行 Git 命令。

- `cmd`：Git 命令字符串，或字符串列表。
- `extra_args`：额外传给 Git 的参数序列，主要在 `cmd` 是字符串时有用。
- `capture_stdout=True`：将 Git 标准输出捕获到 `CompletedProcess`，而不直接打印。
- `capture_stderr`：与 `capture_stdout` 类似，但针对标准错误。应谨慎使用，因为它可能使使用者看不到错误消息。
- `check`：启用检查时，Git 返回非零退出码会抛出 `subprocess.CalledProcessError`。
- `cwd`：运行 Git 的目录，默认 `self.abspath`。

0.6.1 加入 `capture_stderr` 关键字参数；0.7.0 起不再对参数调用现已删除的 `Project.format` 方法。

<a id="west.manifest.Project.sha"></a>

`sha(rev: str, cwd: str | PathLike | None = None) → str`

获取项目修订的 SHA。`rev` 是字符串形式的 Git 修订，例如 `HEAD`、`v2.0.0`；`cwd` 是运行命令的目录，默认 `self.abspath`。0.7.0 起捕获标准错误。

<a id="west.manifest.Project.is_ancestor_of"></a>

`is_ancestor_of(rev1: str, rev2: str, cwd: str | PathLike | None = None) → bool`

检查项目中 `rev1` 是否为 `rev2` 的**祖先提交（Ancestor Commit）**。两者可为任何能解析到提交的值；如果指向同一个提交，也返回 `True`，即提交被视为自身的祖先。其他情况返回 `False`。

`rev1` 是可能的祖先，`rev2` 是可能的后代，`cwd` 是命令运行目录，默认 `self.abspath`。0.8.0 起 `cwd` 可为任意 `os.PathLike`。

<a id="west.manifest.Project.is_cloned"></a>

`is_cloned(cwd: str | PathLike | None = None) → bool`

如果 `self.abspath` 看起来是 Git 仓库顶层目录，返回 `True`，否则返回 `False`。`cwd` 是命令运行目录，默认 `self.abspath`。0.6.1 新增；0.8.0 起 `cwd` 可为任意 `os.PathLike`。

<a id="west.manifest.Project.is_up_to_date_with"></a>

`is_up_to_date_with(rev: str, cwd: str | PathLike | None = None) → bool`

检查项目相对于 `rev` 是否已更新到位，是则返回 `True`。等价于 `is_ancestor_of(rev, 'HEAD', cwd=cwd)`。

`rev` 是用于比较的基准修订；`cwd` 是命令运行目录，默认 `self.abspath`。0.8.0 起 `cwd` 可为任意 `os.PathLike`。

<a id="west.manifest.Project.is_up_to_date"></a>

`is_up_to_date(cwd: str | PathLike | None = None) → bool`

检查项目 `HEAD` 相对于清单是否已更新到位，等价于 `is_up_to_date_with(self.revision, cwd=cwd)`。`cwd` 是命令运行目录，默认 `self.abspath`。0.8.0 起 `cwd` 可为任意 `os.PathLike`。

<a id="west.manifest.Project.read_at"></a>

`read_at(path: str | PathLike, rev: str | None = None, cwd: str | PathLike | None = None) → bytes`

读取项目中指定修订下的文件内容，返回字节。`path` 是文件在项目内的相对路径；`rev` 是读取该路径的修订，默认 `self.revision`；`cwd` 是命令运行目录，默认 `self.abspath`。0.7.0 新增；0.8.0 起 `cwd` 可为任意 `os.PathLike`。

<a id="west.manifest.Project.listdir_at"></a>

`listdir_at(path: str | PathLike, rev: str | None = None, cwd: str | PathLike | None = None, encoding: str | None = None) → list[str]`

列出项目在指定修订下某个目录的内容，返回文件及子目录名称的列表。`path` 是项目内相对路径；`rev` 是读取的修订，默认 `self.revision`；`cwd` 是命令运行目录，默认 `self.abspath`；`encoding` 是目录内容的编码，默认 `'utf-8'`。0.7.0 新增；0.8.0 起 `cwd` 可为任意 `os.PathLike`。

### 16.4.8\_ManifestProject与Submodule

<a id="west.manifest.ManifestProject"></a>

```text
class west.manifest.ManifestProject(path: str | PathLike | None = None, west_commands: str | list[str] | None = None, topdir: str | PathLike | None = None, userdata: Any | None = None)
```

将清单仓库表示为一个 `Project`。以下属性具有实际意义。

| 属性 | 含义 |
| --- | --- |
| `name` | 字符串 `"manifest"`。 |
| `topdir` | 此清单项目管理的 west 工作区顶层目录，或 `None`。 |
| `path` | 清单仓库在工作区内的相对路径，或 `None`；设置了 `topdir` 时相对于该目录。 |
| `abspath` | 本机路径格式的清单仓库绝对路径；`topdir` 为 `None` 时也为 `None`。 |
| `posixpath` | 与 `abspath` 相同，但以 `/` 分隔。 |
| `west_commands` | 清单 `self:` 映射中的 `west_commands:` 键；如果 `self` 导入多个含 west 命令的附加文件，它可能是这些条目的列表。 |
| `userdata` | 清单 `self` 下解析后的 `userdata` 字段。 |

为兼容 `Project`，还包含以下可读属性：`url` 是空字符串，因为清单仓库不由 west 自身进行版本控制，尽管 `west init` 能从 Git 远程获取它；`revision` 为 `"HEAD"`；由于没有 URL，`clone_depth` 为 `None`；`groups` 为空列表。

仅支持 `Project` 方法中的有限子集，调用其他方法的结果未规定。

0.8.0 起 `url` 从 `None` 改为空字符串；`abspath` 改用 `os.path.abspath()` 而非 `os.path.realpath()` 创建，以改善对符号链接的支持。

> 译注：原页属性说明把 YAML 键写作 `west_commands:`；实际清单使用 `west-commands:`，Python 属性才是 `west_commands`，参见[清单文件](P013_west清单文件.md)。这里保留两者的区别。

<a id="west.manifest.ManifestProject.as_dict"></a>

`as_dict() → dict`

返回当前对象的字典表示，形式与从等效 YAML 清单解析得到的结果相同。0.6.0 新增。

<a id="west.manifest.Submodule"></a>

`class west.manifest.Submodule(path: str, name: str | None = None)`

表示项目中的 Git 子模块。0.9.0 新增。

### 16.4.9\_清单相关异常

<a id="west.configuration.MalformedConfig"></a>

`class west.configuration.MalformedConfig`

基类为 `Exception`，表示 west 配置格式有误。

<a id="west.manifest.MalformedManifest"></a>

`class west.manifest.MalformedManifest`

基类为 `Exception`，表示因数据无效而导致清单解析失败。

<a id="west.manifest.ManifestVersionError"></a>

`class west.manifest.ManifestVersionError(version: str, file: str | PathLike | None = None)`

基类为 `Exception`，表示清单要求比当前版本更新的 west。0.8.0 起 `file` 参数可为任意 `os.PathLike`。

<a id="west.manifest.ManifestImportFailed"></a>

`class west.manifest.ManifestImportFailed(project: Project | None, imp: Any)`

基类为 `Exception`，表示解析清单所需的某个操作失败。

`project` 属性是缺少清单数据的 `Project` 实例；若数据来自 `manifest: self: import:`，则为 `None`。`imp` 属性是请求导入时解析出的 YAML 数据。

0.8.0 起，当时名为 `filename` 的参数可为任意 `os.PathLike`；0.13.0 将其改名为 `imp`，并允许任意值。

## 16.5\_west.util：辅助工具

本模块提供杂项辅助工具。

### 16.5.1\_工作区查找函数

<a id="west.util.west_dir"></a>

`west.util.west_dir(start: str | PathLike | None = None) → str`

返回工作区 `.west` 目录的绝对路径。从 `start` 指定目录开始，逐级向父目录搜索；未指定时使用当前目录。找不到 `.west` 时抛出 `WestNotFound`。0.8.0 起 `start` 可为任意 `os.PathLike`。

<a id="west.util.west_topdir"></a>

`west.util.west_topdir(start: str | PathLike | None = None, fall_back: bool = True) → str`

与 `west_dir()` 类似，但返回 `.west/` 的父目录，也就是存放各项目仓库的目录。0.8.0 起 `start` 可为任意 `os.PathLike`。

### 16.5.2\_工作区查找异常

<a id="west.util.WestNotFound"></a>

`class west.util.WestNotFound`

基类为 `RuntimeError`，表示当前目录及其任意父目录中都没有 west 工作区。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：west的历史与设计缘由](P015_west的历史与设计缘由.md) · [本模块主线目录](../reading/west.md) · [全部主线](../reading/README.md) · [下一篇：west发行说明](P017_west发行说明.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：west的历史与设计缘由](P015_west的历史与设计缘由.md) · [下一章：west发行说明](P017_west发行说明.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
