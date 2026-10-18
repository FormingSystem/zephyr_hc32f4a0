---
id: learning.zephyr-docs.kconfig-reference.page-337
title: "`subsys/dap`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第337章\_`subsys/dap`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/dap` 的 9 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CMSIS_DAP_BOARD_NAME"></a>

## 337.1 `CONFIG_CMSIS_DAP_BOARD_NAME`

**提示（Prompt）**：目标开发板名称（Target board name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DAP
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/dap/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dap/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_DAP`](P337_subsys_dap_配置项参考.md#CONFIG_DAP)。

<a id="CONFIG_CMSIS_DAP_BOARD_VENDOR"></a>

## 337.2 `CONFIG_CMSIS_DAP_BOARD_VENDOR`

**提示（Prompt）**：目标开发板厂商（Target board vendor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DAP
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/dap/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dap/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_DAP`](P337_subsys_dap_配置项参考.md#CONFIG_DAP)。

<a id="CONFIG_CMSIS_DAP_DEVICE_NAME"></a>

## 337.3 `CONFIG_CMSIS_DAP_DEVICE_NAME`

**提示（Prompt）**：目标设备名称（Target device name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DAP
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/dap/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dap/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_DAP`](P337_subsys_dap_配置项参考.md#CONFIG_DAP)。

<a id="CONFIG_CMSIS_DAP_DEVICE_VENDOR"></a>

## 337.4 `CONFIG_CMSIS_DAP_DEVICE_VENDOR`

**提示（Prompt）**：目标设备厂商（Target device vendor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DAP
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/dap/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dap/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_DAP`](P337_subsys_dap_配置项参考.md#CONFIG_DAP)。

<a id="CONFIG_CMSIS_DAP_PACKET_COUNT"></a>

## 337.5 `CONFIG_CMSIS_DAP_PACKET_COUNT`

**提示（Prompt）**：请求和响应数据的最大数据包缓冲区数量（Maximum packet buffers for request and response data）

**说明（Help）**

请求和响应数据的最大数据包缓冲区数量（Maximum packet buffers for request and response data）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DAP
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/dap/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dap/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_DAP`](P337_subsys_dap_配置项参考.md#CONFIG_DAP)。

<a id="CONFIG_CMSIS_DAP_PROBE_NAME"></a>

## 337.6 `CONFIG_CMSIS_DAP_PROBE_NAME`

**提示（Prompt）**：调试探针名称（Probe name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DAP
```

**默认值（Defaults）**

```text
"CMSIS-DAP"
```

**定义位置（Location）**：[`subsys/dap/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dap/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_DAP`](P337_subsys_dap_配置项参考.md#CONFIG_DAP)。

<a id="CONFIG_CMSIS_DAP_PROBE_VENDOR"></a>

## 337.7 `CONFIG_CMSIS_DAP_PROBE_VENDOR`

**提示（Prompt）**：调试探针厂商（Probe vendor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DAP
```

**默认值（Defaults）**

```text
"Zephyr"
```

**定义位置（Location）**：[`subsys/dap/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dap/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_DAP`](P337_subsys_dap_配置项参考.md#CONFIG_DAP)。

<a id="CONFIG_DAP"></a>

## 337.8 `CONFIG_DAP`

**提示（Prompt）**：调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL]

**说明（Help）**

调试访问端口支持（Debug Access Port），本快照仅支持 CMSIS DAP

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_DP_DRIVER
```

**定义位置（Location）**：[`subsys/dap/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dap/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_DP_DRIVER`](P081_drivers_dp_配置项参考.md#CONFIG_DP_DRIVER)。

<a id="CONFIG_DAP_BACKEND_USB"></a>

## 337.9 `CONFIG_DAP_BACKEND_USB`

**提示（Prompt）**：USB 后端（USB backend）

**说明（Help）**

使用批量端点（bulk endpoints）的 DAP USB 后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT && CONFIG_DAP
```

**定义位置（Location）**：[`subsys/dap/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dap/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调试访问端口支持（Debug Access Port support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_DAP`](P337_subsys_dap_配置项参考.md#CONFIG_DAP)。

<!-- kconfig-navigation -->

[上一章](P336_subsys_crc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P338_subsys_debug_配置项参考.md)
