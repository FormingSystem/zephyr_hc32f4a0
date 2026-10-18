---
id: learning.zephyr-docs.kconfig-reference.page-286
title: "`soc/microchip`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第286章\_`soc/microchip`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `soc/microchip` 的 34 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="SB_CONFIG_SOC_SERIES_ATSAMD51"></a>

## 286.1 `SB_CONFIG_SOC_SERIES_ATSAMD51`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMD51 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_ATSAMD51G18A
SB_CONFIG_SOC_ATSAMD51G19A
SB_CONFIG_SOC_ATSAMD51J18A
SB_CONFIG_SOC_ATSAMD51J19A
SB_CONFIG_SOC_ATSAMD51J20A
SB_CONFIG_SOC_ATSAMD51N19A
SB_CONFIG_SOC_ATSAMD51N20A
SB_CONFIG_SOC_ATSAMD51P19A
SB_CONFIG_SOC_ATSAMD51P20A
```

**定义位置（Location）**：[`soc/microchip/sam/sam_d5x_e5x/atsamd51/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sam_d5x_e5x/atsamd51/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`SB_CONFIG_SOC_ATSAMD51G18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAMD51G18A)、[`SB_CONFIG_SOC_ATSAMD51G19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAMD51G19A)、[`SB_CONFIG_SOC_ATSAMD51J18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAMD51J18A)、[`SB_CONFIG_SOC_ATSAMD51J19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAMD51J19A)、[`SB_CONFIG_SOC_ATSAMD51J20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAMD51J20A)、[`SB_CONFIG_SOC_ATSAMD51N19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAMD51N19A)、[`SB_CONFIG_SOC_ATSAMD51N20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAMD51N20A)、[`SB_CONFIG_SOC_ATSAMD51P19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAMD51P19A)、[`SB_CONFIG_SOC_ATSAMD51P20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAMD51P20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`SB_CONFIG_SOC_ATSAMD51G18A`、`SB_CONFIG_SOC_ATSAMD51G19A`、`SB_CONFIG_SOC_ATSAMD51J18A`、`SB_CONFIG_SOC_ATSAMD51J19A`、`SB_CONFIG_SOC_ATSAMD51J20A`、`SB_CONFIG_SOC_ATSAMD51N19A`、`SB_CONFIG_SOC_ATSAMD51N20A`、`SB_CONFIG_SOC_ATSAMD51P19A`、`SB_CONFIG_SOC_ATSAMD51P20A`。

<a id="SB_CONFIG_SOC_SERIES_ATSAME51"></a>

## 286.2 `SB_CONFIG_SOC_SERIES_ATSAME51`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAME51 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_ATSAME51G18A
SB_CONFIG_SOC_ATSAME51G19A
SB_CONFIG_SOC_ATSAME51J18A
SB_CONFIG_SOC_ATSAME51J19A
SB_CONFIG_SOC_ATSAME51J20A
SB_CONFIG_SOC_ATSAME51N19A
SB_CONFIG_SOC_ATSAME51N20A
```

**定义位置（Location）**：[`soc/microchip/sam/sam_d5x_e5x/atsame51/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sam_d5x_e5x/atsame51/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`SB_CONFIG_SOC_ATSAME51G18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME51G18A)、[`SB_CONFIG_SOC_ATSAME51G19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME51G19A)、[`SB_CONFIG_SOC_ATSAME51J18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME51J18A)、[`SB_CONFIG_SOC_ATSAME51J19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME51J19A)、[`SB_CONFIG_SOC_ATSAME51J20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME51J20A)、[`SB_CONFIG_SOC_ATSAME51N19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME51N19A)、[`SB_CONFIG_SOC_ATSAME51N20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME51N20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`SB_CONFIG_SOC_ATSAME51G18A`、`SB_CONFIG_SOC_ATSAME51G19A`、`SB_CONFIG_SOC_ATSAME51J18A`、`SB_CONFIG_SOC_ATSAME51J19A`、`SB_CONFIG_SOC_ATSAME51J20A`、`SB_CONFIG_SOC_ATSAME51N19A`、`SB_CONFIG_SOC_ATSAME51N20A`。

<a id="SB_CONFIG_SOC_SERIES_ATSAME53"></a>

## 286.3 `SB_CONFIG_SOC_SERIES_ATSAME53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAME53 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_ATSAME53J18A
SB_CONFIG_SOC_ATSAME53J19A
SB_CONFIG_SOC_ATSAME53J20A
SB_CONFIG_SOC_ATSAME53N19A
SB_CONFIG_SOC_ATSAME53N20A
```

**定义位置（Location）**：[`soc/microchip/sam/sam_d5x_e5x/atsame53/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sam_d5x_e5x/atsame53/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`SB_CONFIG_SOC_ATSAME53J18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME53J18A)、[`SB_CONFIG_SOC_ATSAME53J19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME53J19A)、[`SB_CONFIG_SOC_ATSAME53J20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME53J20A)、[`SB_CONFIG_SOC_ATSAME53N19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME53N19A)、[`SB_CONFIG_SOC_ATSAME53N20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME53N20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`SB_CONFIG_SOC_ATSAME53J18A`、`SB_CONFIG_SOC_ATSAME53J19A`、`SB_CONFIG_SOC_ATSAME53J20A`、`SB_CONFIG_SOC_ATSAME53N19A`、`SB_CONFIG_SOC_ATSAME53N20A`。

<a id="SB_CONFIG_SOC_SERIES_ATSAME54"></a>

## 286.4 `SB_CONFIG_SOC_SERIES_ATSAME54`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAME54 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_ATSAME54N19A
SB_CONFIG_SOC_ATSAME54N20A
SB_CONFIG_SOC_ATSAME54P19A
SB_CONFIG_SOC_ATSAME54P20A
```

**定义位置（Location）**：[`soc/microchip/sam/sam_d5x_e5x/atsame54/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sam_d5x_e5x/atsame54/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`SB_CONFIG_SOC_ATSAME54N19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME54N19A)、[`SB_CONFIG_SOC_ATSAME54N20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME54N20A)、[`SB_CONFIG_SOC_ATSAME54P19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME54P19A)、[`SB_CONFIG_SOC_ATSAME54P20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATSAME54P20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`SB_CONFIG_SOC_ATSAME54N19A`、`SB_CONFIG_SOC_ATSAME54N20A`、`SB_CONFIG_SOC_ATSAME54P19A`、`SB_CONFIG_SOC_ATSAME54P20A`。

<a id="SB_CONFIG_SOC_SERIES_MEC15XX"></a>

## 286.5 `SB_CONFIG_SOC_SERIES_MEC15XX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip MEC Cortex-M4 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MEC1501_HSZ
```

**定义位置（Location）**：[`soc/microchip/mec/mec15xx/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec15xx/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`SB_CONFIG_SOC_MEC1501_HSZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MEC1501_HSZ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC`、`SB_CONFIG_SOC_MEC1501_HSZ`。

<a id="SB_CONFIG_SOC_SERIES_MEC165XB"></a>

## 286.6 `SB_CONFIG_SOC_SERIES_MEC165XB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip MEC Cortex-M4 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MEC1653B_NSZ
```

**定义位置（Location）**：[`soc/microchip/mec/mec165xb/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec165xb/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`SB_CONFIG_SOC_MEC1653B_NSZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MEC1653B_NSZ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC`、`SB_CONFIG_SOC_MEC1653B_NSZ`。

<a id="SB_CONFIG_SOC_SERIES_MEC172X"></a>

## 286.7 `SB_CONFIG_SOC_SERIES_MEC172X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip MEC Cortex-M4F 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MEC172X_NSZ
SB_CONFIG_SOC_MEC172X_NLJ
```

**定义位置（Location）**：[`soc/microchip/mec/mec172x/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec172x/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`SB_CONFIG_SOC_MEC172X_NSZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MEC172X_NSZ)、[`SB_CONFIG_SOC_MEC172X_NLJ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MEC172X_NLJ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC`、`SB_CONFIG_SOC_MEC172X_NSZ`、`SB_CONFIG_SOC_MEC172X_NLJ`。

<a id="SB_CONFIG_SOC_SERIES_MEC174X"></a>

## 286.8 `SB_CONFIG_SOC_SERIES_MEC174X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip MEC Cortex-M4F 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MEC1743_QLJ
SB_CONFIG_SOC_MEC1743_QSZ
```

**定义位置（Location）**：[`soc/microchip/mec/mec174x/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec174x/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`SB_CONFIG_SOC_MEC1743_QLJ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MEC1743_QLJ)、[`SB_CONFIG_SOC_MEC1743_QSZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MEC1743_QSZ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC`、`SB_CONFIG_SOC_MEC1743_QLJ`、`SB_CONFIG_SOC_MEC1743_QSZ`。

<a id="SB_CONFIG_SOC_SERIES_MEC175X"></a>

## 286.9 `SB_CONFIG_SOC_SERIES_MEC175X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip MEC Cortex-M4F 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MEC1753_QLJ
SB_CONFIG_SOC_MEC1753_QSZ
```

**定义位置（Location）**：[`soc/microchip/mec/mec175x/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec175x/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`SB_CONFIG_SOC_MEC1753_QLJ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MEC1753_QLJ)、[`SB_CONFIG_SOC_MEC1753_QSZ`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MEC1753_QSZ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_MEC`、`SB_CONFIG_SOC_MEC1753_QLJ`、`SB_CONFIG_SOC_MEC1753_QSZ`。

<a id="SB_CONFIG_SOC_SERIES_MIV"></a>

## 286.10 `SB_CONFIG_SOC_SERIES_MIV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip Mi-V 实现（implementation）#。译注：原始提示末尾带有 `#` 字符。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_MIV
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MIV
```

**定义位置（Location）**：[`soc/microchip/miv/miv/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/miv/miv/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_MIV)、[`SB_CONFIG_SOC_MIV`](P285_soc_microchip_配置项参考_1.md#SB_CONFIG_SOC_MIV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_MIV`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CK_GC00"></a>

## 286.11 `SB_CONFIG_SOC_SERIES_PIC32CK_GC00`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CK GC00 Cortex-M33 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CK0512GC00064
SB_CONFIG_SOC_PIC32CK0512GC00100
SB_CONFIG_SOC_PIC32CK1012GC00048
SB_CONFIG_SOC_PIC32CK1012GC00064
SB_CONFIG_SOC_PIC32CK1012GC00100
SB_CONFIG_SOC_PIC32CK1025GC00064
SB_CONFIG_SOC_PIC32CK1025GC00100
SB_CONFIG_SOC_PIC32CK2051GC00064
SB_CONFIG_SOC_PIC32CK2051GC00100
SB_CONFIG_SOC_PIC32CK2051GC00144
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_gc00/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_gc00/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`SB_CONFIG_SOC_PIC32CK0512GC00064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK0512GC00064)、[`SB_CONFIG_SOC_PIC32CK0512GC00100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK0512GC00100)、[`SB_CONFIG_SOC_PIC32CK1012GC00048`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1012GC00048)、[`SB_CONFIG_SOC_PIC32CK1012GC00064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1012GC00064)、[`SB_CONFIG_SOC_PIC32CK1012GC00100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1012GC00100)、[`SB_CONFIG_SOC_PIC32CK1025GC00064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1025GC00064)、[`SB_CONFIG_SOC_PIC32CK1025GC00100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1025GC00100)、[`SB_CONFIG_SOC_PIC32CK2051GC00064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK2051GC00064)、[`SB_CONFIG_SOC_PIC32CK2051GC00100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK2051GC00100)、[`SB_CONFIG_SOC_PIC32CK2051GC00144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK2051GC00144)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`SB_CONFIG_SOC_PIC32CK0512GC00064`、`SB_CONFIG_SOC_PIC32CK0512GC00100`、`SB_CONFIG_SOC_PIC32CK1012GC00048`、`SB_CONFIG_SOC_PIC32CK1012GC00064`、`SB_CONFIG_SOC_PIC32CK1012GC00100`、`SB_CONFIG_SOC_PIC32CK1025GC00064`、`SB_CONFIG_SOC_PIC32CK1025GC00100`、`SB_CONFIG_SOC_PIC32CK2051GC00064`、`SB_CONFIG_SOC_PIC32CK2051GC00100`、`SB_CONFIG_SOC_PIC32CK2051GC00144`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CK_GC01"></a>

## 286.12 `SB_CONFIG_SOC_SERIES_PIC32CK_GC01`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CK GC01 Cortex-M33 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CK0512GC01064
SB_CONFIG_SOC_PIC32CK0512GC01100
SB_CONFIG_SOC_PIC32CK1012GC01048
SB_CONFIG_SOC_PIC32CK1012GC01064
SB_CONFIG_SOC_PIC32CK1012GC01100
SB_CONFIG_SOC_PIC32CK1025GC01064
SB_CONFIG_SOC_PIC32CK1025GC01100
SB_CONFIG_SOC_PIC32CK2051GC01064
SB_CONFIG_SOC_PIC32CK2051GC01100
SB_CONFIG_SOC_PIC32CK2051GC01144
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_gc01/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_gc01/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`SB_CONFIG_SOC_PIC32CK0512GC01064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK0512GC01064)、[`SB_CONFIG_SOC_PIC32CK0512GC01100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK0512GC01100)、[`SB_CONFIG_SOC_PIC32CK1012GC01048`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1012GC01048)、[`SB_CONFIG_SOC_PIC32CK1012GC01064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1012GC01064)、[`SB_CONFIG_SOC_PIC32CK1012GC01100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1012GC01100)、[`SB_CONFIG_SOC_PIC32CK1025GC01064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1025GC01064)、[`SB_CONFIG_SOC_PIC32CK1025GC01100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1025GC01100)、[`SB_CONFIG_SOC_PIC32CK2051GC01064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK2051GC01064)、[`SB_CONFIG_SOC_PIC32CK2051GC01100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK2051GC01100)、[`SB_CONFIG_SOC_PIC32CK2051GC01144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK2051GC01144)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`SB_CONFIG_SOC_PIC32CK0512GC01064`、`SB_CONFIG_SOC_PIC32CK0512GC01100`、`SB_CONFIG_SOC_PIC32CK1012GC01048`、`SB_CONFIG_SOC_PIC32CK1012GC01064`、`SB_CONFIG_SOC_PIC32CK1012GC01100`、`SB_CONFIG_SOC_PIC32CK1025GC01064`、`SB_CONFIG_SOC_PIC32CK1025GC01100`、`SB_CONFIG_SOC_PIC32CK2051GC01064`、`SB_CONFIG_SOC_PIC32CK2051GC01100`、`SB_CONFIG_SOC_PIC32CK2051GC01144`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CK_SG00"></a>

## 286.13 `SB_CONFIG_SOC_SERIES_PIC32CK_SG00`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CK SG00 Cortex-M33 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CK0512SG00064
SB_CONFIG_SOC_PIC32CK0512SG00100
SB_CONFIG_SOC_PIC32CK1012SG00048
SB_CONFIG_SOC_PIC32CK1012SG00064
SB_CONFIG_SOC_PIC32CK1012SG00100
SB_CONFIG_SOC_PIC32CK1025SG00064
SB_CONFIG_SOC_PIC32CK1025SG00100
SB_CONFIG_SOC_PIC32CK1025SG00144
SB_CONFIG_SOC_PIC32CK2051SG00064
SB_CONFIG_SOC_PIC32CK2051SG00100
SB_CONFIG_SOC_PIC32CK2051SG00144
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_sg00/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_sg00/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`SB_CONFIG_SOC_PIC32CK0512SG00064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK0512SG00064)、[`SB_CONFIG_SOC_PIC32CK0512SG00100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK0512SG00100)、[`SB_CONFIG_SOC_PIC32CK1012SG00048`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1012SG00048)、[`SB_CONFIG_SOC_PIC32CK1012SG00064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1012SG00064)、[`SB_CONFIG_SOC_PIC32CK1012SG00100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1012SG00100)、[`SB_CONFIG_SOC_PIC32CK1025SG00064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1025SG00064)、[`SB_CONFIG_SOC_PIC32CK1025SG00100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1025SG00100)、[`SB_CONFIG_SOC_PIC32CK1025SG00144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1025SG00144)、[`SB_CONFIG_SOC_PIC32CK2051SG00064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK2051SG00064)、[`SB_CONFIG_SOC_PIC32CK2051SG00100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK2051SG00100)、[`SB_CONFIG_SOC_PIC32CK2051SG00144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK2051SG00144)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`SB_CONFIG_SOC_PIC32CK0512SG00064`、`SB_CONFIG_SOC_PIC32CK0512SG00100`、`SB_CONFIG_SOC_PIC32CK1012SG00048`、`SB_CONFIG_SOC_PIC32CK1012SG00064`、`SB_CONFIG_SOC_PIC32CK1012SG00100`、`SB_CONFIG_SOC_PIC32CK1025SG00064`、`SB_CONFIG_SOC_PIC32CK1025SG00100`、`SB_CONFIG_SOC_PIC32CK1025SG00144`、`SB_CONFIG_SOC_PIC32CK2051SG00064`、`SB_CONFIG_SOC_PIC32CK2051SG00100`、`SB_CONFIG_SOC_PIC32CK2051SG00144`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CK_SG01"></a>

## 286.14 `SB_CONFIG_SOC_SERIES_PIC32CK_SG01`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CK SG01 Cortex-M33 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CK0512SG01064
SB_CONFIG_SOC_PIC32CK0512SG01100
SB_CONFIG_SOC_PIC32CK1012SG01048
SB_CONFIG_SOC_PIC32CK1012SG01064
SB_CONFIG_SOC_PIC32CK1012SG01100
SB_CONFIG_SOC_PIC32CK1025SG01064
SB_CONFIG_SOC_PIC32CK1025SG01100
SB_CONFIG_SOC_PIC32CK1025SG01144
SB_CONFIG_SOC_PIC32CK2051SG01064
SB_CONFIG_SOC_PIC32CK2051SG01100
SB_CONFIG_SOC_PIC32CK2051SG01144
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_sg01/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_sg01/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`SB_CONFIG_SOC_PIC32CK0512SG01064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK0512SG01064)、[`SB_CONFIG_SOC_PIC32CK0512SG01100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK0512SG01100)、[`SB_CONFIG_SOC_PIC32CK1012SG01048`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1012SG01048)、[`SB_CONFIG_SOC_PIC32CK1012SG01064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1012SG01064)、[`SB_CONFIG_SOC_PIC32CK1012SG01100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1012SG01100)、[`SB_CONFIG_SOC_PIC32CK1025SG01064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1025SG01064)、[`SB_CONFIG_SOC_PIC32CK1025SG01100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1025SG01100)、[`SB_CONFIG_SOC_PIC32CK1025SG01144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK1025SG01144)、[`SB_CONFIG_SOC_PIC32CK2051SG01064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK2051SG01064)、[`SB_CONFIG_SOC_PIC32CK2051SG01100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK2051SG01100)、[`SB_CONFIG_SOC_PIC32CK2051SG01144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CK2051SG01144)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`SB_CONFIG_SOC_PIC32CK0512SG01064`、`SB_CONFIG_SOC_PIC32CK0512SG01100`、`SB_CONFIG_SOC_PIC32CK1012SG01048`、`SB_CONFIG_SOC_PIC32CK1012SG01064`、`SB_CONFIG_SOC_PIC32CK1012SG01100`、`SB_CONFIG_SOC_PIC32CK1025SG01064`、`SB_CONFIG_SOC_PIC32CK1025SG01100`、`SB_CONFIG_SOC_PIC32CK1025SG01144`、`SB_CONFIG_SOC_PIC32CK2051SG01064`、`SB_CONFIG_SOC_PIC32CK2051SG01100`、`SB_CONFIG_SOC_PIC32CK2051SG01144`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CM_GC00"></a>

## 286.15 `SB_CONFIG_SOC_SERIES_PIC32CM_GC00`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM GC00 Cortex-M23 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CM5112GC00048
SB_CONFIG_SOC_PIC32CM5112GC00064
SB_CONFIG_SOC_PIC32CM5112GC00100
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_sg_gc/pic32cm_gc00/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_sg_gc/pic32cm_gc00/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC)、[`SB_CONFIG_SOC_PIC32CM5112GC00048`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5112GC00048)、[`SB_CONFIG_SOC_PIC32CM5112GC00064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5112GC00064)、[`SB_CONFIG_SOC_PIC32CM5112GC00100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5112GC00100)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`、`SB_CONFIG_SOC_PIC32CM5112GC00048`、`SB_CONFIG_SOC_PIC32CM5112GC00064`、`SB_CONFIG_SOC_PIC32CM5112GC00100`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CM_JH00"></a>

## 286.16 `SB_CONFIG_SOC_SERIES_PIC32CM_JH00`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM JH00 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CM2532JH00032
SB_CONFIG_SOC_PIC32CM5164JH00032
SB_CONFIG_SOC_PIC32CM2532JH00048
SB_CONFIG_SOC_PIC32CM5164JH00048
SB_CONFIG_SOC_PIC32CM2532JH00064
SB_CONFIG_SOC_PIC32CM5164JH00064
SB_CONFIG_SOC_PIC32CM2532JH00100
SB_CONFIG_SOC_PIC32CM5164JH00100
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_jh/pic32cm_jh00/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_jh/pic32cm_jh00/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`SB_CONFIG_SOC_PIC32CM2532JH00032`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM2532JH00032)、[`SB_CONFIG_SOC_PIC32CM5164JH00032`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5164JH00032)、[`SB_CONFIG_SOC_PIC32CM2532JH00048`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM2532JH00048)、[`SB_CONFIG_SOC_PIC32CM5164JH00048`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5164JH00048)、[`SB_CONFIG_SOC_PIC32CM2532JH00064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM2532JH00064)、[`SB_CONFIG_SOC_PIC32CM5164JH00064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5164JH00064)、[`SB_CONFIG_SOC_PIC32CM2532JH00100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM2532JH00100)、[`SB_CONFIG_SOC_PIC32CM5164JH00100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5164JH00100)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`、`SB_CONFIG_SOC_PIC32CM2532JH00032`、`SB_CONFIG_SOC_PIC32CM5164JH00032`、`SB_CONFIG_SOC_PIC32CM2532JH00048`、`SB_CONFIG_SOC_PIC32CM5164JH00048`、`SB_CONFIG_SOC_PIC32CM2532JH00064`、`SB_CONFIG_SOC_PIC32CM5164JH00064`、`SB_CONFIG_SOC_PIC32CM2532JH00100`、`SB_CONFIG_SOC_PIC32CM5164JH00100`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CM_JH01"></a>

## 286.17 `SB_CONFIG_SOC_SERIES_PIC32CM_JH01`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM JH01 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CM2532JH01032
SB_CONFIG_SOC_PIC32CM5164JH01032
SB_CONFIG_SOC_PIC32CM2532JH01048
SB_CONFIG_SOC_PIC32CM5164JH01048
SB_CONFIG_SOC_PIC32CM2532JH01064
SB_CONFIG_SOC_PIC32CM5164JH01064
SB_CONFIG_SOC_PIC32CM2532JH01100
SB_CONFIG_SOC_PIC32CM5164JH01100
SB_CONFIG_SOC_PIC32CM1216JH01032
SB_CONFIG_SOC_PIC32CM1216JH01048
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_jh/pic32cm_jh01/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_jh/pic32cm_jh01/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`SB_CONFIG_SOC_PIC32CM2532JH01032`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM2532JH01032)、[`SB_CONFIG_SOC_PIC32CM5164JH01032`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5164JH01032)、[`SB_CONFIG_SOC_PIC32CM2532JH01048`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM2532JH01048)、[`SB_CONFIG_SOC_PIC32CM5164JH01048`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5164JH01048)、[`SB_CONFIG_SOC_PIC32CM2532JH01064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM2532JH01064)、[`SB_CONFIG_SOC_PIC32CM5164JH01064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5164JH01064)、[`SB_CONFIG_SOC_PIC32CM2532JH01100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM2532JH01100)、[`SB_CONFIG_SOC_PIC32CM5164JH01100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5164JH01100)、[`SB_CONFIG_SOC_PIC32CM1216JH01032`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM1216JH01032)、[`SB_CONFIG_SOC_PIC32CM1216JH01048`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM1216JH01048)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`、`SB_CONFIG_SOC_PIC32CM2532JH01032`、`SB_CONFIG_SOC_PIC32CM5164JH01032`、`SB_CONFIG_SOC_PIC32CM2532JH01048`、`SB_CONFIG_SOC_PIC32CM5164JH01048`、`SB_CONFIG_SOC_PIC32CM2532JH01064`、`SB_CONFIG_SOC_PIC32CM5164JH01064`、`SB_CONFIG_SOC_PIC32CM2532JH01100`、`SB_CONFIG_SOC_PIC32CM5164JH01100`、`SB_CONFIG_SOC_PIC32CM1216JH01032`、`SB_CONFIG_SOC_PIC32CM1216JH01048`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CM_PL10"></a>

## 286.18 `SB_CONFIG_SOC_SERIES_PIC32CM_PL10`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM PL10 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CM6408PL10028
SB_CONFIG_SOC_PIC32CM6408PL10032
SB_CONFIG_SOC_PIC32CM6408PL10048
SB_CONFIG_SOC_PIC32CM6408PL10064
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_pl/pic32cm_pl10/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_pl/pic32cm_pl10/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL)、[`SB_CONFIG_SOC_PIC32CM6408PL10028`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM6408PL10028)、[`SB_CONFIG_SOC_PIC32CM6408PL10032`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM6408PL10032)、[`SB_CONFIG_SOC_PIC32CM6408PL10048`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM6408PL10048)、[`SB_CONFIG_SOC_PIC32CM6408PL10064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM6408PL10064)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`、`SB_CONFIG_SOC_PIC32CM6408PL10028`、`SB_CONFIG_SOC_PIC32CM6408PL10032`、`SB_CONFIG_SOC_PIC32CM6408PL10048`、`SB_CONFIG_SOC_PIC32CM6408PL10064`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CM_SG00"></a>

## 286.19 `SB_CONFIG_SOC_SERIES_PIC32CM_SG00`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM SG00 Cortex-M23 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CM5112SG00048
SB_CONFIG_SOC_PIC32CM5112SG00064
SB_CONFIG_SOC_PIC32CM5112SG00100
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_sg_gc/pic32cm_sg00/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_sg_gc/pic32cm_sg00/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC)、[`SB_CONFIG_SOC_PIC32CM5112SG00048`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5112SG00048)、[`SB_CONFIG_SOC_PIC32CM5112SG00064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5112SG00064)、[`SB_CONFIG_SOC_PIC32CM5112SG00100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CM5112SG00100)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`、`SB_CONFIG_SOC_PIC32CM5112SG00048`、`SB_CONFIG_SOC_PIC32CM5112SG00064`、`SB_CONFIG_SOC_PIC32CM5112SG00100`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CX_SG41"></a>

## 286.20 `SB_CONFIG_SOC_SERIES_PIC32CX_SG41`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CX SG41 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CX1025SG41064
SB_CONFIG_SOC_PIC32CX1025SG41080
SB_CONFIG_SOC_PIC32CX1025SG41100
SB_CONFIG_SOC_PIC32CX1025SG41128
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cx_sg/pic32cx_sg41/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cx_sg/pic32cx_sg41/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`SB_CONFIG_SOC_PIC32CX1025SG41064`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CX1025SG41064)、[`SB_CONFIG_SOC_PIC32CX1025SG41080`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CX1025SG41080)、[`SB_CONFIG_SOC_PIC32CX1025SG41100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CX1025SG41100)、[`SB_CONFIG_SOC_PIC32CX1025SG41128`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CX1025SG41128)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`SB_CONFIG_SOC_PIC32CX1025SG41064`、`SB_CONFIG_SOC_PIC32CX1025SG41080`、`SB_CONFIG_SOC_PIC32CX1025SG41100`、`SB_CONFIG_SOC_PIC32CX1025SG41128`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CX_SG60"></a>

## 286.21 `SB_CONFIG_SOC_SERIES_PIC32CX_SG60`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CX SG60 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CX1025SG60100
SB_CONFIG_SOC_PIC32CX1025SG60128
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cx_sg/pic32cx_sg60/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cx_sg/pic32cx_sg60/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`SB_CONFIG_SOC_PIC32CX1025SG60100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CX1025SG60100)、[`SB_CONFIG_SOC_PIC32CX1025SG60128`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CX1025SG60128)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`SB_CONFIG_SOC_PIC32CX1025SG60100`、`SB_CONFIG_SOC_PIC32CX1025SG60128`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CX_SG61"></a>

## 286.22 `SB_CONFIG_SOC_SERIES_PIC32CX_SG61`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CX SG61 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CX1025SG61100
SB_CONFIG_SOC_PIC32CX1025SG61128
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cx_sg/pic32cx_sg61/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cx_sg/pic32cx_sg61/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`SB_CONFIG_SOC_PIC32CX1025SG61100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CX1025SG61100)、[`SB_CONFIG_SOC_PIC32CX1025SG61128`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CX1025SG61128)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`SB_CONFIG_SOC_PIC32CX1025SG61100`、`SB_CONFIG_SOC_PIC32CX1025SG61128`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CZ_CA80"></a>

## 286.23 `SB_CONFIG_SOC_SERIES_PIC32CZ_CA80`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CZ CA80 Cortex-M7 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CZ2051CA80100
SB_CONFIG_SOC_PIC32CZ2051CA80144
SB_CONFIG_SOC_PIC32CZ2051CA80176
SB_CONFIG_SOC_PIC32CZ2051CA80208
SB_CONFIG_SOC_PIC32CZ4010CA80100
SB_CONFIG_SOC_PIC32CZ4010CA80144
SB_CONFIG_SOC_PIC32CZ4010CA80176
SB_CONFIG_SOC_PIC32CZ4010CA80208
SB_CONFIG_SOC_PIC32CZ8110CA80100
SB_CONFIG_SOC_PIC32CZ8110CA80144
SB_CONFIG_SOC_PIC32CZ8110CA80176
SB_CONFIG_SOC_PIC32CZ8110CA80208
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cz_ca/pic32cz_ca80/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cz_ca/pic32cz_ca80/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`SB_CONFIG_SOC_PIC32CZ2051CA80100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ2051CA80100)、[`SB_CONFIG_SOC_PIC32CZ2051CA80144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ2051CA80144)、[`SB_CONFIG_SOC_PIC32CZ2051CA80176`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ2051CA80176)、[`SB_CONFIG_SOC_PIC32CZ2051CA80208`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ2051CA80208)、[`SB_CONFIG_SOC_PIC32CZ4010CA80100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ4010CA80100)、[`SB_CONFIG_SOC_PIC32CZ4010CA80144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ4010CA80144)、[`SB_CONFIG_SOC_PIC32CZ4010CA80176`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ4010CA80176)、[`SB_CONFIG_SOC_PIC32CZ4010CA80208`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ4010CA80208)、[`SB_CONFIG_SOC_PIC32CZ8110CA80100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ8110CA80100)、[`SB_CONFIG_SOC_PIC32CZ8110CA80144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ8110CA80144)、[`SB_CONFIG_SOC_PIC32CZ8110CA80176`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ8110CA80176)、[`SB_CONFIG_SOC_PIC32CZ8110CA80208`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ8110CA80208)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`SB_CONFIG_SOC_PIC32CZ2051CA80100`、`SB_CONFIG_SOC_PIC32CZ2051CA80144`、`SB_CONFIG_SOC_PIC32CZ2051CA80176`、`SB_CONFIG_SOC_PIC32CZ2051CA80208`、`SB_CONFIG_SOC_PIC32CZ4010CA80100`、`SB_CONFIG_SOC_PIC32CZ4010CA80144`、`SB_CONFIG_SOC_PIC32CZ4010CA80176`、`SB_CONFIG_SOC_PIC32CZ4010CA80208`、`SB_CONFIG_SOC_PIC32CZ8110CA80100`、`SB_CONFIG_SOC_PIC32CZ8110CA80144`、`SB_CONFIG_SOC_PIC32CZ8110CA80176`、`SB_CONFIG_SOC_PIC32CZ8110CA80208`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CZ_CA90"></a>

## 286.24 `SB_CONFIG_SOC_SERIES_PIC32CZ_CA90`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CZ CA90 Cortex-M7 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CZ2051CA90100
SB_CONFIG_SOC_PIC32CZ2051CA90144
SB_CONFIG_SOC_PIC32CZ2051CA90176
SB_CONFIG_SOC_PIC32CZ2051CA90208
SB_CONFIG_SOC_PIC32CZ4010CA90100
SB_CONFIG_SOC_PIC32CZ4010CA90144
SB_CONFIG_SOC_PIC32CZ4010CA90176
SB_CONFIG_SOC_PIC32CZ4010CA90208
SB_CONFIG_SOC_PIC32CZ8110CA90100
SB_CONFIG_SOC_PIC32CZ8110CA90144
SB_CONFIG_SOC_PIC32CZ8110CA90176
SB_CONFIG_SOC_PIC32CZ8110CA90208
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cz_ca/pic32cz_ca90/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cz_ca/pic32cz_ca90/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`SB_CONFIG_SOC_PIC32CZ2051CA90100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ2051CA90100)、[`SB_CONFIG_SOC_PIC32CZ2051CA90144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ2051CA90144)、[`SB_CONFIG_SOC_PIC32CZ2051CA90176`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ2051CA90176)、[`SB_CONFIG_SOC_PIC32CZ2051CA90208`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ2051CA90208)、[`SB_CONFIG_SOC_PIC32CZ4010CA90100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ4010CA90100)、[`SB_CONFIG_SOC_PIC32CZ4010CA90144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ4010CA90144)、[`SB_CONFIG_SOC_PIC32CZ4010CA90176`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ4010CA90176)、[`SB_CONFIG_SOC_PIC32CZ4010CA90208`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ4010CA90208)、[`SB_CONFIG_SOC_PIC32CZ8110CA90100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ8110CA90100)、[`SB_CONFIG_SOC_PIC32CZ8110CA90144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ8110CA90144)、[`SB_CONFIG_SOC_PIC32CZ8110CA90176`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ8110CA90176)、[`SB_CONFIG_SOC_PIC32CZ8110CA90208`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ8110CA90208)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`SB_CONFIG_SOC_PIC32CZ2051CA90100`、`SB_CONFIG_SOC_PIC32CZ2051CA90144`、`SB_CONFIG_SOC_PIC32CZ2051CA90176`、`SB_CONFIG_SOC_PIC32CZ2051CA90208`、`SB_CONFIG_SOC_PIC32CZ4010CA90100`、`SB_CONFIG_SOC_PIC32CZ4010CA90144`、`SB_CONFIG_SOC_PIC32CZ4010CA90176`、`SB_CONFIG_SOC_PIC32CZ4010CA90208`、`SB_CONFIG_SOC_PIC32CZ8110CA90100`、`SB_CONFIG_SOC_PIC32CZ8110CA90144`、`SB_CONFIG_SOC_PIC32CZ8110CA90176`、`SB_CONFIG_SOC_PIC32CZ8110CA90208`。

<a id="SB_CONFIG_SOC_SERIES_PIC32CZ_CA91"></a>

## 286.25 `SB_CONFIG_SOC_SERIES_PIC32CZ_CA91`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CZ CA91 Cortex-M7 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC32CZ2051CA91100
SB_CONFIG_SOC_PIC32CZ2051CA91144
SB_CONFIG_SOC_PIC32CZ2051CA91176
SB_CONFIG_SOC_PIC32CZ4010CA91100
SB_CONFIG_SOC_PIC32CZ4010CA91144
SB_CONFIG_SOC_PIC32CZ4010CA91176
SB_CONFIG_SOC_PIC32CZ4010CA91208
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cz_ca/pic32cz_ca91/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cz_ca/pic32cz_ca91/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`SB_CONFIG_SOC_PIC32CZ2051CA91100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ2051CA91100)、[`SB_CONFIG_SOC_PIC32CZ2051CA91144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ2051CA91144)、[`SB_CONFIG_SOC_PIC32CZ2051CA91176`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ2051CA91176)、[`SB_CONFIG_SOC_PIC32CZ4010CA91100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ4010CA91100)、[`SB_CONFIG_SOC_PIC32CZ4010CA91144`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ4010CA91144)、[`SB_CONFIG_SOC_PIC32CZ4010CA91176`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ4010CA91176)、[`SB_CONFIG_SOC_PIC32CZ4010CA91208`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC32CZ4010CA91208)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`SB_CONFIG_SOC_PIC32CZ2051CA91100`、`SB_CONFIG_SOC_PIC32CZ2051CA91144`、`SB_CONFIG_SOC_PIC32CZ2051CA91176`、`SB_CONFIG_SOC_PIC32CZ4010CA91100`、`SB_CONFIG_SOC_PIC32CZ4010CA91144`、`SB_CONFIG_SOC_PIC32CZ4010CA91176`、`SB_CONFIG_SOC_PIC32CZ4010CA91208`。

<a id="SB_CONFIG_SOC_SERIES_PIC64GX"></a>

## 286.26 `SB_CONFIG_SOC_SERIES_PIC64GX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC64GX 片上系统（SoC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC64
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_PIC64GX1000
```

**定义位置（Location）**：[`soc/microchip/pic64/pic64gx/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic64/pic64gx/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC64`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC64)、[`SB_CONFIG_SOC_PIC64GX1000`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_PIC64GX1000)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC64`、`SB_CONFIG_SOC_PIC64GX1000`。

<a id="SB_CONFIG_SOC_SERIES_POLARFIRE"></a>

## 286.27 `SB_CONFIG_SOC_SERIES_POLARFIRE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip RV64 实现（implementation）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_MIV
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_POLARFIRE
```

**定义位置（Location）**：[`soc/microchip/miv/polarfire/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/miv/polarfire/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_MIV)、[`SB_CONFIG_SOC_POLARFIRE`](P285_soc_microchip_配置项参考_1.md#SB_CONFIG_SOC_POLARFIRE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_MIV`。

<a id="SB_CONFIG_SOC_SERIES_SAMA5D2"></a>

## 286.28 `SB_CONFIG_SOC_SERIES_SAMA5D2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA5D2 Cortex-A 微处理器（Microprocessor）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA5
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_SAMA5D27SOM
SB_CONFIG_SOC_SERIES_SAMA5D29
SB_CONFIG_SOC_SAMA5D21
SB_CONFIG_SOC_SAMA5D22
SB_CONFIG_SOC_SAMA5D225CD1M
SB_CONFIG_SOC_SAMA5D23
SB_CONFIG_SOC_SAMA5D24
SB_CONFIG_SOC_SAMA5D26
SB_CONFIG_SOC_SAMA5D27
SB_CONFIG_SOC_SAMA5D27CD1G
SB_CONFIG_SOC_SAMA5D27CD5M
SB_CONFIG_SOC_SAMA5D27CLD1G
SB_CONFIG_SOC_SAMA5D27CLD2G
SB_CONFIG_SOC_SAMA5D28
SB_CONFIG_SOC_SAMA5D28CD1G
SB_CONFIG_SOC_SAMA5D28CLD1G
SB_CONFIG_SOC_SAMA5D28CLD2G
```

**定义位置（Location）**：[`soc/microchip/sam/sama5/sama5d2/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama5/sama5d2/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA5`](P285_soc_microchip_配置项参考_1.md#SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA5)、[`SB_CONFIG_SOC_SERIES_SAMA5D27SOM`](P286_soc_microchip_配置项参考_2.md#SB_CONFIG_SOC_SERIES_SAMA5D27SOM)、[`SB_CONFIG_SOC_SERIES_SAMA5D29`](P286_soc_microchip_配置项参考_2.md#SB_CONFIG_SOC_SERIES_SAMA5D29)、[`SB_CONFIG_SOC_SAMA5D21`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D21)、[`SB_CONFIG_SOC_SAMA5D22`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D22)、[`SB_CONFIG_SOC_SAMA5D225CD1M`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D225CD1M)、[`SB_CONFIG_SOC_SAMA5D23`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D23)、[`SB_CONFIG_SOC_SAMA5D24`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D24)、[`SB_CONFIG_SOC_SAMA5D26`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D26)、[`SB_CONFIG_SOC_SAMA5D27`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D27)、[`SB_CONFIG_SOC_SAMA5D27CD1G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D27CD1G)、[`SB_CONFIG_SOC_SAMA5D27CD5M`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D27CD5M)、[`SB_CONFIG_SOC_SAMA5D27CLD1G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D27CLD1G)、[`SB_CONFIG_SOC_SAMA5D27CLD2G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D27CLD2G)、[`SB_CONFIG_SOC_SAMA5D28`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D28)、[`SB_CONFIG_SOC_SAMA5D28CD1G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D28CD1G)、[`SB_CONFIG_SOC_SAMA5D28CLD1G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D28CLD1G)、[`SB_CONFIG_SOC_SAMA5D28CLD2G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D28CLD2G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SAMA5D21`、`SB_CONFIG_SOC_SAMA5D22`、`SB_CONFIG_SOC_SAMA5D225CD1M`、`SB_CONFIG_SOC_SAMA5D23`、`SB_CONFIG_SOC_SAMA5D24`、`SB_CONFIG_SOC_SAMA5D26`、`SB_CONFIG_SOC_SAMA5D27`、`SB_CONFIG_SOC_SAMA5D27CD1G`、`SB_CONFIG_SOC_SAMA5D27CD5M`、`SB_CONFIG_SOC_SAMA5D27CLD1G`、`SB_CONFIG_SOC_SAMA5D27CLD2G`、`SB_CONFIG_SOC_SAMA5D28`、`SB_CONFIG_SOC_SAMA5D28CD1G`、`SB_CONFIG_SOC_SAMA5D28CLD1G`、`SB_CONFIG_SOC_SAMA5D28CLD2G`。

<a id="SB_CONFIG_SOC_SERIES_SAMA5D27SOM"></a>

## 286.29 `SB_CONFIG_SOC_SERIES_SAMA5D27SOM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA5D2 系统模组（System-On-Module，SOM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_SAMA5D2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAMA5D27SOM1
SB_CONFIG_SOC_SAMA5D27WLSOM1
```

**定义位置（Location）**：[`soc/microchip/sam/sama5/sama5d2/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama5/sama5d2/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_SAMA5D2`](P286_soc_microchip_配置项参考_2.md#SB_CONFIG_SOC_SERIES_SAMA5D2)、[`SB_CONFIG_SOC_SAMA5D27SOM1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D27SOM1)、[`SB_CONFIG_SOC_SAMA5D27WLSOM1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D27WLSOM1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SAMA5D27SOM1`、`SB_CONFIG_SOC_SAMA5D27WLSOM1`。

<a id="SB_CONFIG_SOC_SERIES_SAMA5D29"></a>

## 286.30 `SB_CONFIG_SOC_SERIES_SAMA5D29`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA5D29 Cortex-A 微处理器（Microprocessor）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_SAMA5D2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAMA5D29
SB_CONFIG_SOC_SAMA5D29TA100
```

**定义位置（Location）**：[`soc/microchip/sam/sama5/sama5d2/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama5/sama5d2/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_SAMA5D2`](P286_soc_microchip_配置项参考_2.md#SB_CONFIG_SOC_SERIES_SAMA5D2)、[`SB_CONFIG_SOC_SAMA5D29`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D29)、[`SB_CONFIG_SOC_SAMA5D29TA100`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA5D29TA100)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SAMA5D29`、`SB_CONFIG_SOC_SAMA5D29TA100`。

<a id="SB_CONFIG_SOC_SERIES_SAMA7D6"></a>

## 286.31 `SB_CONFIG_SOC_SERIES_SAMA7D6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA7D6 Cortex-A 微处理器（Microprocessor）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA7
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAMA7D65
SB_CONFIG_SOC_SAMA7D65D1G
SB_CONFIG_SOC_SAMA7D65D1GN2
SB_CONFIG_SOC_SAMA7D65D2G
SB_CONFIG_SOC_SAMA7D65D2GN8
SB_CONFIG_SOC_SAMA7D65D5M
```

**定义位置（Location）**：[`soc/microchip/sam/sama7/sama7d6/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama7/sama7d6/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA7`](P285_soc_microchip_配置项参考_1.md#SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA7)、[`SB_CONFIG_SOC_SAMA7D65`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7D65)、[`SB_CONFIG_SOC_SAMA7D65D1G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7D65D1G)、[`SB_CONFIG_SOC_SAMA7D65D1GN2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7D65D1GN2)、[`SB_CONFIG_SOC_SAMA7D65D2G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7D65D2G)、[`SB_CONFIG_SOC_SAMA7D65D2GN8`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7D65D2GN8)、[`SB_CONFIG_SOC_SAMA7D65D5M`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7D65D5M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SAMA7D65`、`SB_CONFIG_SOC_SAMA7D65D1G`、`SB_CONFIG_SOC_SAMA7D65D1GN2`、`SB_CONFIG_SOC_SAMA7D65D2G`、`SB_CONFIG_SOC_SAMA7D65D2GN8`、`SB_CONFIG_SOC_SAMA7D65D5M`。

<a id="SB_CONFIG_SOC_SERIES_SAMA7G5"></a>

## 286.32 `SB_CONFIG_SOC_SERIES_SAMA7G5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA7G5 Cortex-A 微处理器（Microprocessor）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA7
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAMA7G54
SB_CONFIG_SOC_SAMA7G54D1G
SB_CONFIG_SOC_SAMA7G54D1GN0
SB_CONFIG_SOC_SAMA7G54D1GN2
SB_CONFIG_SOC_SAMA7G54D2G
SB_CONFIG_SOC_SAMA7G54D2GN4
SB_CONFIG_SOC_SAMA7G54D4G
```

**定义位置（Location）**：[`soc/microchip/sam/sama7/sama7g5/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama7/sama7g5/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA7`](P285_soc_microchip_配置项参考_1.md#SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA7)、[`SB_CONFIG_SOC_SAMA7G54`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7G54)、[`SB_CONFIG_SOC_SAMA7G54D1G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7G54D1G)、[`SB_CONFIG_SOC_SAMA7G54D1GN0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7G54D1GN0)、[`SB_CONFIG_SOC_SAMA7G54D1GN2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7G54D1GN2)、[`SB_CONFIG_SOC_SAMA7G54D2G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7G54D2G)、[`SB_CONFIG_SOC_SAMA7G54D2GN4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7G54D2GN4)、[`SB_CONFIG_SOC_SAMA7G54D4G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMA7G54D4G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SAMA7G54`、`SB_CONFIG_SOC_SAMA7G54D1G`、`SB_CONFIG_SOC_SAMA7G54D1GN0`、`SB_CONFIG_SOC_SAMA7G54D1GN2`、`SB_CONFIG_SOC_SAMA7G54D2G`、`SB_CONFIG_SOC_SAMA7G54D2GN4`、`SB_CONFIG_SOC_SAMA7G54D4G`。

<a id="SB_CONFIG_SOC_SERIES_SMARTFUSION2"></a>

## 286.33 `SB_CONFIG_SOC_SERIES_SMARTFUSION2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip SmartFusion2 系列（series）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_M2S010
```

**定义位置（Location）**：[`soc/microchip/smartfusion2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/smartfusion2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP)、[`SB_CONFIG_SOC_M2S010`](P285_soc_microchip_配置项参考_1.md#SB_CONFIG_SOC_M2S010)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP`。

<a id="SB_CONFIG_UART_MCHP_SERCOM_U2201_5_0_0"></a>

## 286.34 `SB_CONFIG_UART_MCHP_SERCOM_U2201_5_0_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用串行通信 UART 外设 IP（SERCOM UART peripheral IP）版本 5.0.0，标识为 U2201。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/microchip/sam/sam_d5x_e5x/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sam_d5x_e5x/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`。

<!-- kconfig-navigation -->

[上一章](P285_soc_microchip_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P287_soc_native_配置项参考.md)
