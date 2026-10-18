---
id: learning.zephyr-docs.kconfig-reference.page-343
title: "`subsys/fb`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第343章\_`subsys/fb`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/fb` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CHARACTER_FRAMEBUFFER"></a>

## 343.1 `CONFIG_CHARACTER_FRAMEBUFFER`

**提示（Prompt）**：点阵显示屏字符帧缓冲区（Character framebuffer for dot matrix displays）

**说明（Help）**

用于点阵显示屏（dot matrix displays）的字符帧缓冲区（Character framebuffer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/fb/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fb/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

<a id="CONFIG_CHARACTER_FRAMEBUFFER_SHELL"></a>

## 343.2 `CONFIG_CHARACTER_FRAMEBUFFER_SHELL`

**提示（Prompt）**：字符帧缓冲区 Shell（Character Framebuffer shell）

**说明（Help）**

启用向控制台提供帧缓冲区（Framebuffer）命令的 Shell 模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_CHARACTER_FRAMEBUFFER
```

**定义位置（Location）**：[`subsys/fb/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fb/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 点阵显示屏字符帧缓冲区（Character framebuffer for dot matrix displays）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_CHARACTER_FRAMEBUFFER`](P343_subsys_fb_配置项参考.md#CONFIG_CHARACTER_FRAMEBUFFER)。

<a id="CONFIG_CHARACTER_FRAMEBUFFER_USE_DEFAULT_FONTS"></a>

## 343.3 `CONFIG_CHARACTER_FRAMEBUFFER_USE_DEFAULT_FONTS`

**提示（Prompt）**：使用默认字体（Use default fonts）

**说明（Help）**

使用默认字体（default fonts）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CHARACTER_FRAMEBUFFER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/fb/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fb/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 点阵显示屏字符帧缓冲区（Character framebuffer for dot matrix displays）

**配置项引用（Symbol References）**：[`CONFIG_CHARACTER_FRAMEBUFFER`](P343_subsys_fb_配置项参考.md#CONFIG_CHARACTER_FRAMEBUFFER)。

<!-- kconfig-navigation -->

[上一章](P342_subsys_emul_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P344_subsys_fs_配置项参考.md)
