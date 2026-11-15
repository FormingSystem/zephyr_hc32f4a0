---
id: learning.zephyr-docs.kconfig-reference.page-345
title: "`subsys/gnss`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第345章\_`subsys/gnss`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/gnss` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_GNSS_RTK"></a>

## 345.1 `CONFIG_GNSS_RTK`

**提示（Prompt）**：全球导航卫星系统实时动态差分客户端（GNSS RTK client）【实验性 EXPERIMENTAL】

**说明（Help）**

启用全球导航卫星系统实时动态差分（GNSS RTK）的数据改正客户端（data-correction clients）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/gnss/rtk/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/gnss/rtk/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_GNSS_RTK_PROTOCOL"></a>

## 345.2 `CONFIG_GNSS_RTK_PROTOCOL`

**提示（Prompt）**：GNSS RTK 协议选择（Protocol selection）

**说明（Help）**

选择数据改正（data-correction）使用的 GNSS RTK 协议。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_RTK
```

**默认值（Defaults）**

```text
CONFIG_GNSS_RTK_PROTOCOL_RTCM3
```

**可选项（Choices）**

```text
CONFIG_GNSS_RTK_PROTOCOL_RTCM3
```

**定义位置（Location）**：[`subsys/gnss/rtk/protocol/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/gnss/rtk/protocol/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 全球导航卫星系统实时动态差分客户端（GNSS RTK client）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_GNSS_RTK`](P345_subsys_gnss_配置项参考.md#CONFIG_GNSS_RTK)、[`CONFIG_GNSS_RTK_PROTOCOL_RTCM3`](P345_subsys_gnss_配置项参考.md#CONFIG_GNSS_RTK_PROTOCOL_RTCM3)。

<a id="CONFIG_GNSS_RTK_PROTOCOL_RTCM3"></a>

## 345.3 `CONFIG_GNSS_RTK_PROTOCOL_RTCM3`

**提示（Prompt）**：RTCM3 协议（Protocol）

**说明（Help）**

选择 RTCM3 协议传输 GNSS RTK 改正数据（corrections）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_RTK_PROTOCOL>
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`subsys/gnss/rtk/protocol/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/gnss/rtk/protocol/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 全球导航卫星系统实时动态差分客户端（GNSS RTK client）【实验性 EXPERIMENTAL】 → GNSS RTK 协议选择（Protocol selection）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_RTK_PROTOCOL`](P345_subsys_gnss_配置项参考.md#CONFIG_GNSS_RTK_PROTOCOL)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_GNSS_RTK_SERIAL"></a>

## 345.4 `CONFIG_GNSS_RTK_SERIAL`

**提示（Prompt）**：串行 GNSS RTK 客户端（Serial client）

**说明（Help）**

使用 RTK 串行客户端（Serial client）获取改正数据（data-correction）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GNSS_RTK
```

**主动选择（Selects）**

```text
CONFIG_SERIAL
CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`subsys/gnss/rtk/serial/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/gnss/rtk/serial/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 全球导航卫星系统实时动态差分客户端（GNSS RTK client）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_GNSS_RTK`](P345_subsys_gnss_配置项参考.md#CONFIG_GNSS_RTK)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)。

<!-- kconfig-navigation -->

[上一章](P344_subsys_fs_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P346_subsys_input_配置项参考.md)
