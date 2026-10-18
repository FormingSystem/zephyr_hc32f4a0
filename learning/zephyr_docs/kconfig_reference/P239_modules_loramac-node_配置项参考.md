---
id: learning.zephyr-docs.kconfig-reference.page-239
title: "`modules/loramac-node`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第239章\_`modules/loramac-node`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/loramac-node` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HAS_SEMTECH_LORAMAC"></a>

## 239.1 `CONFIG_HAS_SEMTECH_LORAMAC`

**提示（Prompt）**：Semtech LoRaMac 协议栈（Stack）

**说明（Help）**

启用 Semtech 的 LoRaMac 协议栈（stack）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SEMTECH_RADIO_DRIVERS
```

**被选择（Selected by）**

```text
CONFIG_LORAWAN_LORAMAC_NODE
```

**定义位置（Location）**：[`modules/loramac-node/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/loramac-node/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → loramac-node（模块路径 `modules/lib/loramac-node`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SEMTECH_RADIO_DRIVERS`](P239_modules_loramac-node_配置项参考.md#CONFIG_HAS_SEMTECH_RADIO_DRIVERS)、[`CONFIG_LORAWAN_LORAMAC_NODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_LORAMAC_NODE)。

<a id="CONFIG_HAS_SEMTECH_RADIO_DRIVERS"></a>

## 239.2 `CONFIG_HAS_SEMTECH_RADIO_DRIVERS`

**提示（Prompt）**：Semtech LoRa 无线电驱动（Radio Drivers）

**说明（Help）**

启用 Semtech 的无线电驱动（Radio drivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_HAS_SEMTECH_SX1272
CONFIG_HAS_SEMTECH_SX1276
CONFIG_HAS_SEMTECH_SX126X
CONFIG_HAS_SEMTECH_SX1272
CONFIG_HAS_SEMTECH_SX1276
CONFIG_HAS_SEMTECH_SX126X
```

**定义位置（Location）**：[`modules/loramac-node/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/loramac-node/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → loramac-node（模块路径 `modules/lib/loramac-node`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SEMTECH_SX1272`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SEMTECH_SX1272)、[`CONFIG_HAS_SEMTECH_SX1276`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SEMTECH_SX1276)、[`CONFIG_HAS_SEMTECH_SX126X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SEMTECH_SX126X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SEMTECH_SX1272`、`CONFIG_HAS_SEMTECH_SX1276`、`CONFIG_HAS_SEMTECH_SX126X`。

<a id="CONFIG_HAS_SEMTECH_SOFT_SE"></a>

## 239.3 `CONFIG_HAS_SEMTECH_SOFT_SE`

**提示（Prompt）**：Semtech 安全元件软件实现（Secure Element software implementation）

**说明（Help）**

启用 Semtech 的安全元件软件实现（Secure Element software implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SEMTECH_LORAMAC && CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE >= 2048
```

**被弱选择（Implied by）**

```text
CONFIG_LORAWAN_LORAMAC_NODE
```

**定义位置（Location）**：[`modules/loramac-node/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/loramac-node/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → loramac-node（模块路径 `modules/lib/loramac-node`，相对于 west 工作区顶层目录） → Semtech LoRaMac 协议栈（Stack）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SEMTECH_LORAMAC`](P239_modules_loramac-node_配置项参考.md#CONFIG_HAS_SEMTECH_LORAMAC)、[`CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE`](P002_kernel_配置项参考_2.md#CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE)、[`CONFIG_LORAWAN_LORAMAC_NODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_LORAMAC_NODE)。

<!-- kconfig-navigation -->

[上一章](P238_modules_lora-basics-modem_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P240_modules_lvgl_配置项参考.md)
