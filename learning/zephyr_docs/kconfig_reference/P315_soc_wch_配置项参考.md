---
id: learning.zephyr-docs.kconfig-reference.page-315
title: "`soc/wch`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第315章\_`soc/wch`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/wch` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_CH32H417_BOOT_V5F"></a>

## 315.1 `CONFIG_SOC_CH32H417_BOOT_V5F`

**提示（Prompt）**：早期启动时唤醒 V5F 应用内核（application core）

**说明（Help）**

启用后，V3F 启动内核（boot core）在 `soc_early_init_hook()` 中唤醒 V5F 应用内核；其镜像链接地址为 `0x08010000`，烧录于 Flash 偏移 `0x10000`。单独运行 V3F 且未烧录 V5F 应用镜像时，应禁用此项，防止启动内核跳转到不存在或无效的程序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_CH32H417_V3F && CONFIG_SOC_FAMILY_CH32V
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SOC_EARLY_INIT_HOOK
```

**定义位置（Location）**：[`soc/wch/ch32v/ch32h41x/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/wch/ch32v/ch32h41x/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CH32H417_V3F`](P315_soc_wch_配置项参考.md#CONFIG_SOC_CH32H417_V3F)、[`CONFIG_SOC_FAMILY_CH32V`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CH32V)、[`CONFIG_SOC_EARLY_INIT_HOOK`](P002_kernel_配置项参考_2.md#CONFIG_SOC_EARLY_INIT_HOOK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_CH32V`。

<a id="CONFIG_SOC_CH32H417_V3F"></a>

## 315.2 `CONFIG_SOC_CH32H417_V3F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置针对 CH32H417 非对称多处理片上系统（AMP SoC）中的青稞 QingKe V3F 启动内核。启用 `SOC_CH32H417_BOOT_V5F` 时，启动内核在 `soc_early_init_hook()` 中唤醒 V5F 应用内核，参见 `soc_v3f.c`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_CH32H417
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CH32H417EVT
```

**定义位置（Location）**：[`soc/wch/ch32v/ch32h41x/Kconfig.soc.ch32h417:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/wch/ch32v/ch32h41x/Kconfig.soc.ch32h417#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CH32H417`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CH32H417)、[`CONFIG_BOARD_CH32H417EVT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CH32H417EVT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CH32H417`、`CONFIG_BOARD_CH32H417EVT`。

<a id="CONFIG_SOC_CH32H417_V5F"></a>

## 315.3 `CONFIG_SOC_CH32H417_V5F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置针对 CH32H417 非对称多处理片上系统（AMP SoC）中的青稞 QingKe V5F 应用内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_CH32H417
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CH32H417EVT
```

**定义位置（Location）**：[`soc/wch/ch32v/ch32h41x/Kconfig.soc.ch32h417:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/wch/ch32v/ch32h41x/Kconfig.soc.ch32h417#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_CH32H417`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CH32H417)、[`CONFIG_BOARD_CH32H417EVT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CH32H417EVT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_CH32H417`、`CONFIG_BOARD_CH32H417EVT`。

<a id="CONFIG_VECTOR_TABLE_SIZE"></a>

## 315.4 `CONFIG_VECTOR_TABLE_SIZE`

**提示（Prompt）**：中断和异常向量数量（Number of Interrupt and Exception Vectors）

**说明（Help）**

此选项定义向量表（vector table）中的中断和异常向量总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_CH32V
```

**取值范围（Ranges）**

```text
[20, 256]
```

**定义位置（Location）**：[`soc/wch/ch32v/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/wch/ch32v/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_CH32V`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CH32V)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_CH32V`。

<a id="SB_CONFIG_SOC_CH32H417_V3F"></a>

## 315.5 `SB_CONFIG_SOC_CH32H417_V3F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置针对 CH32H417 非对称多处理片上系统（AMP SoC）中的青稞 QingKe V3F 启动内核。启用 `SOC_CH32H417_BOOT_V5F` 时，启动内核在 `soc_early_init_hook()` 中唤醒 V5F 应用内核，参见 `soc_v3f.c`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_CH32H417
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CH32H417EVT
```

**定义位置（Location）**：[`soc/wch/ch32v/ch32h41x/Kconfig.soc.ch32h417:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/wch/ch32v/ch32h41x/Kconfig.soc.ch32h417#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_CH32H417`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CH32H417)、[`SB_CONFIG_BOARD_CH32H417EVT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CH32H417EVT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_CH32H417`、`SB_CONFIG_BOARD_CH32H417EVT`。

<a id="SB_CONFIG_SOC_CH32H417_V5F"></a>

## 315.6 `SB_CONFIG_SOC_CH32H417_V5F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置针对 CH32H417 非对称多处理片上系统（AMP SoC）中的青稞 QingKe V5F 应用内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_CH32H417
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CH32H417EVT
```

**定义位置（Location）**：[`soc/wch/ch32v/ch32h41x/Kconfig.soc.ch32h417:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/wch/ch32v/ch32h41x/Kconfig.soc.ch32h417#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_CH32H417`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CH32H417)、[`SB_CONFIG_BOARD_CH32H417EVT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CH32H417EVT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_CH32H417`、`SB_CONFIG_BOARD_CH32H417EVT`。

<!-- kconfig-navigation -->

[上一章](P314_soc_ti_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P316_soc_xlnx_配置项参考.md)
