---
id: learning.zephyr-docs.kconfig-reference.page-260
title: "`soc/ambiq`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第260章\_`soc/ambiq`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/ambiq` 的 21 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_AMBIQ_DMA_BUFF_ALIGNMENT"></a>

## 260.1 `CONFIG_SOC_AMBIQ_DMA_BUFF_ALIGNMENT`

**提示（Prompt）**：DMA 缓冲区的字节对齐（Byte alignment）

**说明（Help）**

此选项指定直接内存访问缓冲区（DMA buffer）的对齐方式。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_AMBIQ
```

**默认值（Defaults）**

```text
CONFIG_DCACHE_LINE_SIZE if CONFIG_DCACHE
1
```

**定义位置（Location）**：[`soc/ambiq/apollo5x/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo5x/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_AMBIQ)、[`CONFIG_DCACHE_LINE_SIZE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_AMBIQ`。

<a id="CONFIG_SOC_AMBIQ_DMA_BUFF_LOCATION"></a>

## 260.2 `CONFIG_SOC_AMBIQ_DMA_BUFF_LOCATION`

**提示（Prompt）**：相对于 `SRAM_BASE_ADDRESS` 的字节偏移（Byte Offset）

**说明（Help）**

此选项指定可缓存直接内存访问缓冲区（cacheable DMA buffer）的起始地址。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_AMBIQ
```

**默认值（Defaults）**

```text
0x50000
```

**定义位置（Location）**：[`soc/ambiq/apollo5x/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo5x/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_AMBIQ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_AMBIQ`。

<a id="CONFIG_SOC_AMBIQ_HAS_PUF"></a>

## 260.3 `CONFIG_SOC_AMBIQ_HAS_PUF`

**提示（Prompt）**：Ambiq 物理不可克隆函数支持（PUF support）

**说明（Help）**

此选项启用 Ambiq 物理不可克隆函数（PUF）支持，真随机数生成器（true random number generator）需要此支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_AMBIQ
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/ambiq/apollo5x/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo5x/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_AMBIQ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_AMBIQ`。

<a id="CONFIG_SOC_APOLLO2"></a>

## 260.4 `CONFIG_SOC_APOLLO2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo2 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_APOLLO2X
```

**被选择（Selected by）**

```text
CONFIG_BOARD_APOLLO2_EVB
```

**定义位置（Location）**：[`soc/ambiq/apollo2x/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo2x/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_APOLLO2X`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_SERIES_APOLLO2X)、[`CONFIG_BOARD_APOLLO2_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_APOLLO2_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_APOLLO2_EVB`。

<a id="CONFIG_SOC_APOLLO3P_BLUE"></a>

## 260.5 `CONFIG_SOC_APOLLO3P_BLUE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo3P Blue 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_APOLLO3X
CONFIG_SOC_AMBIQ_BT_SUPPORTED
```

**被选择（Selected by）**

```text
CONFIG_BOARD_APOLLO3P_EVB
```

**定义位置（Location）**：[`soc/ambiq/apollo3x/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo3x/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_APOLLO3X`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_SOC_AMBIQ_BT_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMBIQ_BT_SUPPORTED)、[`CONFIG_BOARD_APOLLO3P_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_APOLLO3P_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AMBIQ_BT_SUPPORTED`、`CONFIG_BOARD_APOLLO3P_EVB`。

<a id="CONFIG_SOC_APOLLO3_BLUE"></a>

## 260.6 `CONFIG_SOC_APOLLO3_BLUE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo3 Blue 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_APOLLO3X
CONFIG_SOC_AMBIQ_BT_SUPPORTED
```

**被选择（Selected by）**

```text
CONFIG_BOARD_APOLLO3_EVB
CONFIG_BOARD_RAK11720
```

**定义位置（Location）**：[`soc/ambiq/apollo3x/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo3x/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_APOLLO3X`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_SOC_AMBIQ_BT_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMBIQ_BT_SUPPORTED)、[`CONFIG_BOARD_APOLLO3_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_APOLLO3_EVB)、[`CONFIG_BOARD_RAK11720`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RAK11720)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AMBIQ_BT_SUPPORTED`、`CONFIG_BOARD_APOLLO3_EVB`、`CONFIG_BOARD_RAK11720`。

<a id="CONFIG_SOC_APOLLO4P"></a>

## 260.7 `CONFIG_SOC_APOLLO4P`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo4P 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_APOLLO4X
```

**被选择（Selected by）**

```text
CONFIG_BOARD_APOLLO4P_EVB
```

**定义位置（Location）**：[`soc/ambiq/apollo4x/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo4x/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_APOLLO4X`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_BOARD_APOLLO4P_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_APOLLO4P_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_APOLLO4P_EVB`。

<a id="CONFIG_SOC_APOLLO4P_BLUE"></a>

## 260.8 `CONFIG_SOC_APOLLO4P_BLUE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo4 Blue Plus 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_APOLLO4X
CONFIG_SOC_AMBIQ_BT_SUPPORTED
```

**被选择（Selected by）**

```text
CONFIG_BOARD_APOLLO4P_BLUE_KXR_EVB
```

**定义位置（Location）**：[`soc/ambiq/apollo4x/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo4x/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_APOLLO4X`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_AMBIQ_BT_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMBIQ_BT_SUPPORTED)、[`CONFIG_BOARD_APOLLO4P_BLUE_KXR_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_APOLLO4P_BLUE_KXR_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AMBIQ_BT_SUPPORTED`、`CONFIG_BOARD_APOLLO4P_BLUE_KXR_EVB`。

<a id="CONFIG_SOC_SERIES_APOLLO2X"></a>

## 260.9 `CONFIG_SOC_SERIES_APOLLO2X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo2 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_AMBIQ
```

**被选择（Selected by）**

```text
CONFIG_SOC_APOLLO2
```

**定义位置（Location）**：[`soc/ambiq/apollo2x/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo2x/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_AMBIQ)、[`CONFIG_SOC_APOLLO2`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_APOLLO2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_AMBIQ`。

<a id="CONFIG_SOC_SERIES_APOLLO3X"></a>

## 260.10 `CONFIG_SOC_SERIES_APOLLO3X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo3 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_AMBIQ
```

**被选择（Selected by）**

```text
CONFIG_SOC_APOLLO3P_BLUE
CONFIG_SOC_APOLLO3_BLUE
```

**定义位置（Location）**：[`soc/ambiq/apollo3x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo3x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_AMBIQ)、[`CONFIG_SOC_APOLLO3P_BLUE`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_APOLLO3P_BLUE)、[`CONFIG_SOC_APOLLO3_BLUE`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_APOLLO3_BLUE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_AMBIQ`。

<a id="CONFIG_SOC_SERIES_APOLLO4X"></a>

## 260.11 `CONFIG_SOC_SERIES_APOLLO4X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo4 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_AMBIQ
```

**被选择（Selected by）**

```text
CONFIG_SOC_APOLLO4P
CONFIG_SOC_APOLLO4P_BLUE
```

**定义位置（Location）**：[`soc/ambiq/apollo4x/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo4x/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_AMBIQ)、[`CONFIG_SOC_APOLLO4P`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_APOLLO4P)、[`CONFIG_SOC_APOLLO4P_BLUE`](P260_soc_ambiq_配置项参考.md#CONFIG_SOC_APOLLO4P_BLUE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_AMBIQ`。

<a id="CONFIG_SOC_SERIES_APOLLO5X"></a>

## 260.12 `CONFIG_SOC_SERIES_APOLLO5X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo5 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_AMBIQ
```

**被选择（Selected by）**

```text
CONFIG_SOC_APOLLO510
```

**定义位置（Location）**：[`soc/ambiq/apollo5x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo5x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_AMBIQ)、[`CONFIG_SOC_APOLLO510`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_APOLLO510)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_AMBIQ`、`CONFIG_SOC_APOLLO510`。

<a id="SB_CONFIG_SOC_APOLLO2"></a>

## 260.13 `SB_CONFIG_SOC_APOLLO2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo2 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_APOLLO2X
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_APOLLO2_EVB
```

**定义位置（Location）**：[`soc/ambiq/apollo2x/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo2x/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_APOLLO2X`](P260_soc_ambiq_配置项参考.md#SB_CONFIG_SOC_SERIES_APOLLO2X)、[`SB_CONFIG_BOARD_APOLLO2_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_APOLLO2_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_APOLLO2_EVB`。

<a id="SB_CONFIG_SOC_APOLLO3P_BLUE"></a>

## 260.14 `SB_CONFIG_SOC_APOLLO3P_BLUE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo3P Blue 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_APOLLO3X
SB_CONFIG_SOC_AMBIQ_BT_SUPPORTED
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_APOLLO3P_EVB
```

**定义位置（Location）**：[`soc/ambiq/apollo3x/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo3x/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_APOLLO3X`](P260_soc_ambiq_配置项参考.md#SB_CONFIG_SOC_SERIES_APOLLO3X)、[`SB_CONFIG_SOC_AMBIQ_BT_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AMBIQ_BT_SUPPORTED)、[`SB_CONFIG_BOARD_APOLLO3P_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_APOLLO3P_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_AMBIQ_BT_SUPPORTED`、`SB_CONFIG_BOARD_APOLLO3P_EVB`。

<a id="SB_CONFIG_SOC_APOLLO3_BLUE"></a>

## 260.15 `SB_CONFIG_SOC_APOLLO3_BLUE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo3 Blue 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_APOLLO3X
SB_CONFIG_SOC_AMBIQ_BT_SUPPORTED
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_APOLLO3_EVB
SB_CONFIG_BOARD_RAK11720
```

**定义位置（Location）**：[`soc/ambiq/apollo3x/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo3x/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_APOLLO3X`](P260_soc_ambiq_配置项参考.md#SB_CONFIG_SOC_SERIES_APOLLO3X)、[`SB_CONFIG_SOC_AMBIQ_BT_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AMBIQ_BT_SUPPORTED)、[`SB_CONFIG_BOARD_APOLLO3_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_APOLLO3_EVB)、[`SB_CONFIG_BOARD_RAK11720`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RAK11720)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_AMBIQ_BT_SUPPORTED`、`SB_CONFIG_BOARD_APOLLO3_EVB`、`SB_CONFIG_BOARD_RAK11720`。

<a id="SB_CONFIG_SOC_APOLLO4P"></a>

## 260.16 `SB_CONFIG_SOC_APOLLO4P`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo4P 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_APOLLO4X
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_APOLLO4P_EVB
```

**定义位置（Location）**：[`soc/ambiq/apollo4x/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo4x/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_APOLLO4X`](P260_soc_ambiq_配置项参考.md#SB_CONFIG_SOC_SERIES_APOLLO4X)、[`SB_CONFIG_BOARD_APOLLO4P_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_APOLLO4P_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_APOLLO4P_EVB`。

<a id="SB_CONFIG_SOC_APOLLO4P_BLUE"></a>

## 260.17 `SB_CONFIG_SOC_APOLLO4P_BLUE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo4 Blue Plus 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_APOLLO4X
SB_CONFIG_SOC_AMBIQ_BT_SUPPORTED
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_APOLLO4P_BLUE_KXR_EVB
```

**定义位置（Location）**：[`soc/ambiq/apollo4x/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo4x/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_APOLLO4X`](P260_soc_ambiq_配置项参考.md#SB_CONFIG_SOC_SERIES_APOLLO4X)、[`SB_CONFIG_SOC_AMBIQ_BT_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AMBIQ_BT_SUPPORTED)、[`SB_CONFIG_BOARD_APOLLO4P_BLUE_KXR_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_APOLLO4P_BLUE_KXR_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_AMBIQ_BT_SUPPORTED`、`SB_CONFIG_BOARD_APOLLO4P_BLUE_KXR_EVB`。

<a id="SB_CONFIG_SOC_SERIES_APOLLO2X"></a>

## 260.18 `SB_CONFIG_SOC_SERIES_APOLLO2X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo2 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_AMBIQ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_APOLLO2
```

**定义位置（Location）**：[`soc/ambiq/apollo2x/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo2x/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_AMBIQ)、[`SB_CONFIG_SOC_APOLLO2`](P260_soc_ambiq_配置项参考.md#SB_CONFIG_SOC_APOLLO2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_AMBIQ`。

<a id="SB_CONFIG_SOC_SERIES_APOLLO3X"></a>

## 260.19 `SB_CONFIG_SOC_SERIES_APOLLO3X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo3 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_AMBIQ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_APOLLO3P_BLUE
SB_CONFIG_SOC_APOLLO3_BLUE
```

**定义位置（Location）**：[`soc/ambiq/apollo3x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo3x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_AMBIQ)、[`SB_CONFIG_SOC_APOLLO3P_BLUE`](P260_soc_ambiq_配置项参考.md#SB_CONFIG_SOC_APOLLO3P_BLUE)、[`SB_CONFIG_SOC_APOLLO3_BLUE`](P260_soc_ambiq_配置项参考.md#SB_CONFIG_SOC_APOLLO3_BLUE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_AMBIQ`。

<a id="SB_CONFIG_SOC_SERIES_APOLLO4X"></a>

## 260.20 `SB_CONFIG_SOC_SERIES_APOLLO4X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo4 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_AMBIQ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_APOLLO4P
SB_CONFIG_SOC_APOLLO4P_BLUE
```

**定义位置（Location）**：[`soc/ambiq/apollo4x/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo4x/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_AMBIQ)、[`SB_CONFIG_SOC_APOLLO4P`](P260_soc_ambiq_配置项参考.md#SB_CONFIG_SOC_APOLLO4P)、[`SB_CONFIG_SOC_APOLLO4P_BLUE`](P260_soc_ambiq_配置项参考.md#SB_CONFIG_SOC_APOLLO4P_BLUE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_AMBIQ`。

<a id="SB_CONFIG_SOC_SERIES_APOLLO5X"></a>

## 260.21 `SB_CONFIG_SOC_SERIES_APOLLO5X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Apollo5 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_AMBIQ
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_APOLLO510
```

**定义位置（Location）**：[`soc/ambiq/apollo5x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ambiq/apollo5x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_AMBIQ)、[`SB_CONFIG_SOC_APOLLO510`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_APOLLO510)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_AMBIQ`、`SB_CONFIG_SOC_APOLLO510`。

<!-- kconfig-navigation -->

[上一章](P259_soc_alif_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P261_soc_andestech_配置项参考.md)
