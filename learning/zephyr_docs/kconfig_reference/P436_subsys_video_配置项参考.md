---
id: learning.zephyr-docs.kconfig-reference.page-436
title: "`subsys/video`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第436章\_`subsys/video`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/video` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_VIDEO"></a>

## 436.1 `CONFIG_VIDEO`

**提示（Prompt）**：视频子系统（Video subsystem）

**说明（Help）**

启用视频子系统（Video Subsystem）及视频驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_VIDEO_DRIVERS
```

**定义位置（Location）**：[`subsys/video/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/video/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SHELL"></a>

## 436.2 `CONFIG_VIDEO_SHELL`

**提示（Prompt）**：视频命令行（Video Shell）

**说明（Help）**

此命令行提供视频驱动的控制与查询命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_VIDEO
```

**定义位置（Location）**：[`subsys/video/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/video/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 视频子系统（Video subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_VIDEO`](P436_subsys_video_配置项参考.md#CONFIG_VIDEO)。

<a id="CONFIG_VIDEO_SHELL_CTRL_NAME_SIZE"></a>

## 436.3 `CONFIG_VIDEO_SHELL_CTRL_NAME_SIZE`

**提示（Prompt）**：控制字符串标识符的最大长度

**说明（Help）**

视频控制项（Video Control）具有人类可读的名称，该名称会转换为字符串标识符（String Identifier）。此 Kconfig 选项控制字符串标识符的最大长度，超过此长度的名称将被截断。默认值足以容纳所有标准控制项名称。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SHELL && CONFIG_VIDEO
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`subsys/video/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/video/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 视频子系统（Video subsystem） → 视频命令行（Video Shell）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SHELL`](P436_subsys_video_配置项参考.md#CONFIG_VIDEO_SHELL)、[`CONFIG_VIDEO`](P436_subsys_video_配置项参考.md#CONFIG_VIDEO)。

<!-- kconfig-navigation -->

[上一章](P435_subsys_usb_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P437_subsys_zbus_配置项参考.md)
