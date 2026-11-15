---
id: learning.zephyr-docs.kconfig.kconfig-extensions
title: Kconfig扩展
kind: reference
status: maintained
domains: [zephyr, kconfig]
source_url: https://docs.zephyrproject.org/latest/build/kconfig/extensions.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第5章\_Kconfig扩展

原文：[Kconfig extensions](https://docs.zephyrproject.org/latest/build/kconfig/extensions.html)。读取日期：2026-10-12，`latest`。

Zephyr 使用 [Kconfiglib](https://github.com/zephyrproject-rtos/Kconfiglib) 实现 Kconfig 配置语言。除了[通用Kconfig语法](https://docs.kernel.org/kbuild/kconfig-language.html)，该实现还支持本页列出的扩展。

## 5.1\_在不减弱依赖的情况下补充默认值

`configdefault` 为已有**配置符号（Configuration Symbol）**增加默认值，不会减弱该符号原有的依赖约束。例如：

```kconfig
config FOO
    bool "FOO"
    depends on BAR

configdefault FOO
    default y if FIZZ
```

就默认值与依赖而言，上述内容等价于：

```kconfig
config FOO
    bool "Foo"
    default y if FIZZ
    depends on BAR
```

这里 `FOO`、`BAR`、`FIZZ` 是示例符号。即使 `FIZZ` 使默认值为 `y`，`FOO` 仍受 `BAR` 依赖约束。多处普通符号定义的依赖合并规则见[多个符号定义](https://docs.zephyrproject.org/latest/build/kconfig/setting.html#multiple-symbol-definitions)。

`configdefault` 内只能包含 `default` 字段，但可以放在 `if` 条件块中。下面两种写法等价：

```kconfig
configdefault FOO
    default y if BAR

if BAR
configdefault FOO
    default y
endif # BAR
```

> 译注：这是 Kconfig 文件内容，用于定义配置规则，不是写入 `prj.conf` 的 `CONFIG_...=...` 赋值，也不是终端命令。

## 5.2\_直接展开环境变量

`source` 语句中可直接展开环境变量，无需先定义带 `option env="ENV_VAR"` 的中转符号。原文同时指出 Linux 4.18 起，其 C 实现工具也移除了 `option env`。

推荐用 `$(FOO)` 引用环境变量，而非 `$FOO`，以使用新的 [Kconfig预处理器（Kconfig Preprocessor）](https://docs.kernel.org/kbuild/kconfig-macro-language.html)。旧的 `$FOO` 写法只为向后兼容保留。

## 5.3\_按通配模式包含文件

`source` 支持**通配模式（Glob Pattern）**，包含每个匹配文件，并要求至少匹配一个。例如：

```kconfig
source "foo/bar/*/Kconfig"
```

若匹配到 `foo/bar/baz/Kconfig` 与 `foo/bar/qaz/Kconfig`，就等价于：

```kconfig
source "foo/bar/baz/Kconfig"
source "foo/bar/qaz/Kconfig"
```

若没有文件匹配，则报错。通配规则与 [Python glob模块](https://docs.python.org/3/library/glob.html)相同。

允许没有匹配文件，或普通文件名允许不存在时，可以使用**可选包含（Optional Source）**语句 `osource`。它在没有匹配时不执行任何动作。`source` 与 `osource` 的关系类似 Make 中的 `include` 与 `-include`。

## 5.4\_相对当前文件包含

`rsource` 按包含该语句的 Kconfig 文件所在目录解析相对路径。假设顶层文件为 `foo/Kconfig`，而 `foo/bar/Kconfig` 中写：

```kconfig
source "qaz/Kconfig1"
rsource "qaz/Kconfig2"
```

实际包含的是 `foo/qaz/Kconfig1` 与 `foo/bar/qaz/Kconfig2`。前者沿用顶层基准，后者以当前 Kconfig 文件目录为基准。

`rsource` 允许构建可整体移动的 Kconfig 子树，也支持通配模式。代价是更难追踪某个文件从哪里被包含，因此仅在需要这种相对行为时使用。

`orsource` 结合 `osource` 与 `rsource`：相对当前文件目录查找，且允许不存在。例如：

```kconfig
orsource "Kconfig[12]"
```

这会在当前 Kconfig 文件目录包含 `Kconfig1`、`Kconfig2` 中存在的文件。

## 5.5\_同时设置类型与默认值

除 `def_bool` 外，还提供 `def_int`、`def_hex` 与 `def_string`。这些关键字同时设置符号类型并添加默认值，分别对应整数、十六进制整数与字符串。

## 5.6\_具名选择组

`choice <symbol>` 可以把符号名关联到选择组，形成**具名选择组（Named Choice）**，允许在原定义之外修改它。下面定义名为 `FOOBAR` 的组，默认选项为 `BAR`：

```kconfig
choice FOOBAR
        prompt "Example choice"
        default BAR

config FOO
        bool "Foo"

config BAR
        bool "Bar"

endchoice
```

之后可在其他位置，例如 `Kconfig.defconfig`，覆盖该组的默认选项：

```kconfig
# Note how "prompt" is not present here
choice FOOBAR
    default FOO
endchoice
```

第二段没有重复用户提示 `prompt`，只是通过相同的组名提供默认 `FOO`。

**原文注意：**具名选择组最早来自 Linux，但自 Linux 内核 6.9 起已不再支持，因此现在属于 Kconfiglib 的语言扩展。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Kconfig技巧与最佳实践](P004_Kconfig技巧与最佳实践.md) · [本模块主线目录](../reading/kconfig.md) · [全部主线](../reading/README.md) · [下一篇：Kconfig预处理函数](P006_Kconfig预处理函数.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Kconfig技巧与最佳实践](P004_Kconfig技巧与最佳实践.md) · [返回大纲](大纲.md) · [下一章：Kconfig预处理函数](P006_Kconfig预处理函数.md)

</details>

<!-- reading-navigation:end -->
