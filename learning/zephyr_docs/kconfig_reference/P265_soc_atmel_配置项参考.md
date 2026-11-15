---
id: learning.zephyr-docs.kconfig-reference.page-265
title: "`soc/atmel`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第265章\_`soc/atmel`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/atmel` 的 75 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_ATMEL_SAMD5X_DEFAULT_AS_MAIN"></a>

## 265.1 `CONFIG_SOC_ATMEL_SAMD5X_DEFAULT_AS_MAIN`

**提示（Prompt）**：默认（DEFAULT）

**说明（Help）**

此选择保持所有时钟（clock）的当前状态不变，可能是默认复位状态，也可能是引导加载程序（bootloader）设置的状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd5x:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd5x#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 主时钟源（Main clock source）

<a id="CONFIG_SOC_ATMEL_SAMD5X_OSC32K_PRESCALER"></a>

## 265.2 `CONFIG_SOC_ATMEL_SAMD5X_OSC32K_PRESCALER`

**提示（Prompt）**：XOSC32 通用时钟预分频器（Generic Clock Prescaler）

**说明（Help）**

配置连接到 xosc32 或 osculp32k 的通用时钟输出（generic clock output）的预分频器。在日历模式（calendar mode）下使用实时时钟（RTC）时，应将 GCLK 除以 32，使 RTC 接收到 1024 Hz 参考时钟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_SAMD51 || CONFIG_SOC_SERIES_SAME51 || CONFIG_SOC_SERIES_SAME53 || CONFIG_SOC_SERIES_SAME54) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**默认值（Defaults）**

```text
32 if n
1
```

**取值范围（Ranges）**

```text
[1, 512]
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd5x:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd5x#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMD51`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD51)、[`CONFIG_SOC_SERIES_SAME51`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME51)、[`CONFIG_SOC_SERIES_SAME53`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME53)、[`CONFIG_SOC_SERIES_SAME54`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME54)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD5X_OSCULP32K_AS_MAIN"></a>

## 265.3 `CONFIG_SOC_ATMEL_SAMD5X_OSCULP32K_AS_MAIN`

**提示（Prompt）**：OSCULP32K 超低功耗振荡器（oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd5x:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd5x#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 主时钟源（Main clock source）

<a id="CONFIG_SOC_ATMEL_SAMD5X_XOSC32K"></a>

## 265.4 `CONFIG_SOC_ATMEL_SAMD5X_XOSC32K`

**提示（Prompt）**：外部 32 kHz 晶体振荡器（external crystal oscillator）

**说明（Help）**

设为 `y` 可在启动时启用外部 32 kHz 晶体振荡器（crystal oscillator），随后可将其选为 SoC 的主时钟源（main clock source）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_SAMD51 || CONFIG_SOC_SERIES_SAME51 || CONFIG_SOC_SERIES_SAME53 || CONFIG_SOC_SERIES_SAME54) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd5x:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd5x#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMD51`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD51)、[`CONFIG_SOC_SERIES_SAME51`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME51)、[`CONFIG_SOC_SERIES_SAME53`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME53)、[`CONFIG_SOC_SERIES_SAME54`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME54)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD5X_XOSC32K_AS_MAIN"></a>

## 265.5 `CONFIG_SOC_ATMEL_SAMD5X_XOSC32K_AS_MAIN`

**提示（Prompt）**：XOSC32K 外部振荡器（external oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAMD5X_XOSC32K && <choice>
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd5x:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd5x#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 主时钟源（Main clock source）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAMD5X_XOSC32K`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD5X_XOSC32K)。

<a id="CONFIG_SOC_ATMEL_SAMD5X_XOSC32K_CRYSTAL"></a>

## 265.6 `CONFIG_SOC_ATMEL_SAMD5X_XOSC32K_CRYSTAL`

**提示（Prompt）**：外部 32.768 kHz 时钟使用晶体振荡器（crystal oscillator）

**说明（Help）**

启用晶体振荡器（crystal oscillator）；禁用时，要求 XIN32 上有时钟信号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAMD5X_XOSC32K && (CONFIG_SOC_SERIES_SAMD51 || CONFIG_SOC_SERIES_SAME51 || CONFIG_SOC_SERIES_SAME53 || CONFIG_SOC_SERIES_SAME54) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd5x:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd5x#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 外部 32 kHz 晶体振荡器（external crystal oscillator）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAMD5X_XOSC32K`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD5X_XOSC32K)、[`CONFIG_SOC_SERIES_SAMD51`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD51)、[`CONFIG_SOC_SERIES_SAME51`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME51)、[`CONFIG_SOC_SERIES_SAME53`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME53)、[`CONFIG_SOC_SERIES_SAME54`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME54)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD5X_XOSC32K_GAIN_HS"></a>

## 265.7 `CONFIG_SOC_ATMEL_SAMD5X_XOSC32K_GAIN_HS`

**提示（Prompt）**：XOSC32 高速增益（High Speed gain）

**说明（Help）**

选择此项时，将增益（gain）设为高速（High Speed），替代标准设置（standard）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAMD5X_XOSC32K && (CONFIG_SOC_SERIES_SAMD51 || CONFIG_SOC_SERIES_SAME51 || CONFIG_SOC_SERIES_SAME53 || CONFIG_SOC_SERIES_SAME54) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd5x:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd5x#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 外部 32 kHz 晶体振荡器（external crystal oscillator）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAMD5X_XOSC32K`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD5X_XOSC32K)、[`CONFIG_SOC_SERIES_SAMD51`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD51)、[`CONFIG_SOC_SERIES_SAME51`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME51)、[`CONFIG_SOC_SERIES_SAME53`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME53)、[`CONFIG_SOC_SERIES_SAME54`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME54)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD5X_XOSC32K_STARTUP"></a>

## 265.8 `CONFIG_SOC_ATMEL_SAMD5X_XOSC32K_STARTUP`

**提示（Prompt）**：外部 32 kHz 晶体振荡器启动时间（Startup time）

**说明（Help）**

选择外部 32 kHz 晶体振荡器（crystal oscillator）的启动时间。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAMD5X_XOSC32K && (CONFIG_SOC_SERIES_SAMD51 || CONFIG_SOC_SERIES_SAME51 || CONFIG_SOC_SERIES_SAME53 || CONFIG_SOC_SERIES_SAME54) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**默认值（Defaults）**

```text
0x1
```

**取值范围（Ranges）**

```text
[0x0, 0x6]
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd5x:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd5x#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 外部 32 kHz 晶体振荡器（external crystal oscillator）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAMD5X_XOSC32K`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD5X_XOSC32K)、[`CONFIG_SOC_SERIES_SAMD51`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD51)、[`CONFIG_SOC_SERIES_SAME51`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME51)、[`CONFIG_SOC_SERIES_SAME53`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME53)、[`CONFIG_SOC_SERIES_SAME54`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAME54)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD_32768HZ_RTC_PRESCALER"></a>

## 265.9 `CONFIG_SOC_ATMEL_SAMD_32768HZ_RTC_PRESCALER`

**提示（Prompt）**：32.768 kHz RTC 通用时钟预分频器（Generic Clock Prescaler）

**说明（Help）**

配置连接到 xosc32 或 osc32k 输入的通用时钟输出（generic clock output）的预分频器。在日历模式（calendar mode）下使用实时时钟（RTC）时，应将 GCLK 除以 32，使 RTC 接收到 1024 Hz 参考时钟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_ATMEL_SAMD_XOSC32K || CONFIG_SOC_ATMEL_SAMD_OSC32K) && (CONFIG_SOC_SERIES_SAMD20 || CONFIG_SOC_SERIES_SAMD21 || CONFIG_SOC_SERIES_SAMR21) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**默认值（Defaults）**

```text
32 if n
1
```

**取值范围（Ranges）**

```text
[1, 512]
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAMD_XOSC32K`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD_XOSC32K)、[`CONFIG_SOC_ATMEL_SAMD_OSC32K`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD_OSC32K)、[`CONFIG_SOC_SERIES_SAMD20`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAMR21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD_DEFAULT_AS_MAIN"></a>

## 265.10 `CONFIG_SOC_ATMEL_SAMD_DEFAULT_AS_MAIN`

**提示（Prompt）**：默认（DEFAULT）

**说明（Help）**

此选择保持所有时钟（clock）的当前状态不变，可能是默认复位状态，也可能是引导加载程序（bootloader）设置的状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 主时钟参考（Main clock reference）

<a id="CONFIG_SOC_ATMEL_SAMD_NVM_WAIT_STATES"></a>

## 265.11 `CONFIG_SOC_ATMEL_SAMD_NVM_WAIT_STATES`

**提示（Prompt）**：非易失存储器等待状态（NVM wait states）

**说明（Help）**

为非易失存储器（NVM）设置的等待状态（wait states）。请查阅数据手册，因为这些设置高度依赖器件的工作条件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_SAMD20 || CONFIG_SOC_SERIES_SAMD21 || CONFIG_SOC_SERIES_SAMR21) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMD20`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAMR21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD_OSC32K"></a>

## 265.12 `CONFIG_SOC_ATMEL_SAMD_OSC32K`

**提示（Prompt）**：内部 32.768 kHz RC 振荡器（Internal RC oscillator）

**说明（Help）**

在启动时启用内部 32.768 kHz RC 振荡器（RC oscillator），随后可将其选为 SoC 的主时钟参考（main clock reference）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_SAMD20 || CONFIG_SOC_SERIES_SAMD21 || CONFIG_SOC_SERIES_SAMR21) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMD20`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAMR21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD_OSC32K_AS_MAIN"></a>

## 265.13 `CONFIG_SOC_ATMEL_SAMD_OSC32K_AS_MAIN`

**提示（Prompt）**：OSC32K 振荡器（oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAMD_OSC32K && <choice>
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 主时钟参考（Main clock reference）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAMD_OSC32K`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD_OSC32K)。

<a id="CONFIG_SOC_ATMEL_SAMD_OSC8M"></a>

## 265.14 `CONFIG_SOC_ATMEL_SAMD_OSC8M`

**提示（Prompt）**：内部 8 MHz RC 振荡器（Internal RC oscillator）

**说明（Help）**

在启动时启用内部 8 MHz RC 振荡器（RC oscillator），随后可将其选为 SoC 的主时钟参考（main clock reference）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_SAMD20 || CONFIG_SOC_SERIES_SAMD21 || CONFIG_SOC_SERIES_SAMR21) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMD20`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAMR21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD_OSC8M_AS_MAIN"></a>

## 265.15 `CONFIG_SOC_ATMEL_SAMD_OSC8M_AS_MAIN`

**提示（Prompt）**：OSC8M 振荡器（oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAMD_OSC8M && <choice>
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 主时钟参考（Main clock reference）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAMD_OSC8M`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD_OSC8M)。

<a id="CONFIG_SOC_ATMEL_SAMD_XOSC"></a>

## 265.16 `CONFIG_SOC_ATMEL_SAMD_XOSC`

**提示（Prompt）**：外部 0.4～32 MHz 时钟源（External clock source）

**说明（Help）**

在启动时启用外部 0.4～32 MHz 时钟源（clock source），随后可将其选为 SoC 的主时钟参考（main clock reference）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_SAMD20 || CONFIG_SOC_SERIES_SAMD21 || CONFIG_SOC_SERIES_SAMR21) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMD20`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAMR21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD_XOSC32K"></a>

## 265.17 `CONFIG_SOC_ATMEL_SAMD_XOSC32K`

**提示（Prompt）**：外部 32.768 kHz 时钟源（External clock source）

**说明（Help）**

在启动时启用外部 32.768 kHz 时钟源（clock source），随后可将其选为 SoC 的主时钟参考（main clock reference）。外部 OSC32K 的优先级高于内部 OSC32K，一旦启用，就会成为 RTC 的默认 32.768 kHz 时钟源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_SAMD20 || CONFIG_SOC_SERIES_SAMD21 || CONFIG_SOC_SERIES_SAMR21) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMD20`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAMR21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD_XOSC32K_AS_MAIN"></a>

## 265.18 `CONFIG_SOC_ATMEL_SAMD_XOSC32K_AS_MAIN`

**提示（Prompt）**：XOSC32K 外部振荡器（external oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAMD_XOSC32K && <choice>
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 主时钟参考（Main clock reference）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAMD_XOSC32K`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD_XOSC32K)。

<a id="CONFIG_SOC_ATMEL_SAMD_XOSC32K_CRYSTAL"></a>

## 265.19 `CONFIG_SOC_ATMEL_SAMD_XOSC32K_CRYSTAL`

**提示（Prompt）**：外部 32.768 kHz 时钟使用晶体振荡器（crystal oscillator）

**说明（Help）**

启用晶体振荡器（crystal oscillator）；禁用时，要求 XIN32 上有时钟信号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAMD_XOSC32K && (CONFIG_SOC_SERIES_SAMD20 || CONFIG_SOC_SERIES_SAMD21 || CONFIG_SOC_SERIES_SAMR21) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 外部 32.768 kHz 时钟源（External clock source）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAMD_XOSC32K`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD_XOSC32K)、[`CONFIG_SOC_SERIES_SAMD20`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAMR21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD_XOSC_AS_MAIN"></a>

## 265.20 `CONFIG_SOC_ATMEL_SAMD_XOSC_AS_MAIN`

**提示（Prompt）**：XOSC 外部振荡器（external oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAMD_XOSC && <choice>
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 主时钟参考（Main clock reference）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAMD_XOSC`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD_XOSC)。

<a id="CONFIG_SOC_ATMEL_SAMD_XOSC_CRYSTAL"></a>

## 265.21 `CONFIG_SOC_ATMEL_SAMD_XOSC_CRYSTAL`

**提示（Prompt）**：外部 0.4～32 MHz 时钟使用晶体振荡器（crystal oscillator）

**说明（Help）**

启用晶体振荡器（crystal oscillator）；禁用时，要求 XIN 上有时钟信号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAMD_XOSC && (CONFIG_SOC_SERIES_SAMD20 || CONFIG_SOC_SERIES_SAMD21 || CONFIG_SOC_SERIES_SAMR21) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 外部 0.4～32 MHz 时钟源（External clock source）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAMD_XOSC`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD_XOSC)、[`CONFIG_SOC_SERIES_SAMD20`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAMR21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMD_XOSC_FREQ_HZ"></a>

## 265.22 `CONFIG_SOC_ATMEL_SAMD_XOSC_FREQ_HZ`

**提示（Prompt）**：外部 0.4～32 MHz 时钟振荡器频率（clock oscillator frequency）

**说明（Help）**

外部 0.4～32 MHz 时钟振荡器的参考频率（reference frequency）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAMD_XOSC && (CONFIG_SOC_SERIES_SAMD20 || CONFIG_SOC_SERIES_SAMD21 || CONFIG_SOC_SERIES_SAMR21) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**默认值（Defaults）**

```text
8000000
```

**取值范围（Ranges）**

```text
[400000, 32000000]
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.samd2x:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.samd2x#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 外部 0.4～32 MHz 时钟源（External clock source）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAMD_XOSC`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAMD_XOSC)、[`CONFIG_SOC_SERIES_SAMD20`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAMR21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAML_DEBUG_PAUSE"></a>

## 265.23 `CONFIG_SOC_ATMEL_SAML_DEBUG_PAUSE`

**提示（Prompt）**：启动时插入暂停，以允许调试器连接（debugger attach）

**说明（Help）**

曾观察到尝试连接调试器（debugger）时出现问题。在早期启动流程中、配置系统时钟之前插入短暂延迟，可以缓解这些问题。如果将来可能需要连接调试器，请设为 `y`。如果确定永远不会为生成的二进制程序连接调试器，或者要求尽可能短的启动时间，请设为 `n`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_SAML21 || CONFIG_SOC_SERIES_SAMR34 || CONFIG_SOC_SERIES_SAMR35) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.saml2x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.saml2x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAML21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAML21)、[`CONFIG_SOC_SERIES_SAMR34`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR34)、[`CONFIG_SOC_SERIES_SAMR35`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR35)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAML_OPENLOOP_AS_MAIN"></a>

## 265.24 `CONFIG_SOC_ATMEL_SAML_OPENLOOP_AS_MAIN`

**提示（Prompt）**：开环（OPENLOOP）

**说明（Help）**

注意，此模式只能与低压差稳压器（LDO regulator）一起使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.saml2x:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.saml2x#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 主时钟参考（Main clock reference）

<a id="CONFIG_SOC_ATMEL_SAML_OSC16M"></a>

## 265.25 `CONFIG_SOC_ATMEL_SAML_OSC16M`

**提示（Prompt）**：内部 16 MHz RC 振荡器（Internal RC oscillator）

**说明（Help）**

在启动时启用内部 16 MHz RC 振荡器（RC oscillator），随后可将其选为 SoC 的主时钟参考（main clock reference）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_SAML21 || CONFIG_SOC_SERIES_SAMR34 || CONFIG_SOC_SERIES_SAMR35) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.saml2x:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.saml2x#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAML21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAML21)、[`CONFIG_SOC_SERIES_SAMR34`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR34)、[`CONFIG_SOC_SERIES_SAMR35`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR35)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAML_OSC16M_AS_MAIN"></a>

## 265.26 `CONFIG_SOC_ATMEL_SAML_OSC16M_AS_MAIN`

**提示（Prompt）**：OSC16M 振荡器（oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAML_OSC16M && <choice>
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.saml2x:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.saml2x#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 主时钟参考（Main clock reference）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAML_OSC16M`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAML_OSC16M)。

<a id="CONFIG_SOC_ATMEL_SAML_OSC32K"></a>

## 265.27 `CONFIG_SOC_ATMEL_SAML_OSC32K`

**提示（Prompt）**：内部 32.768 kHz RC 振荡器（Internal RC oscillator）

**说明（Help）**

在启动时启用内部 32.768 kHz RC 振荡器（RC oscillator），随后可将其选为 SoC 的主时钟参考（main clock reference）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_SAML21 || CONFIG_SOC_SERIES_SAMR34 || CONFIG_SOC_SERIES_SAMR35) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.saml2x:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.saml2x#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAML21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAML21)、[`CONFIG_SOC_SERIES_SAMR34`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR34)、[`CONFIG_SOC_SERIES_SAMR35`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR35)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAML_OSC32K_AS_MAIN"></a>

## 265.28 `CONFIG_SOC_ATMEL_SAML_OSC32K_AS_MAIN`

**提示（Prompt）**：OSC32K 振荡器（oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAML_OSC32K && <choice>
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.saml2x:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.saml2x#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 主时钟参考（Main clock reference）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAML_OSC32K`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAML_OSC32K)。

<a id="CONFIG_SOC_ATMEL_SAML_XOSC32K"></a>

## 265.29 `CONFIG_SOC_ATMEL_SAML_XOSC32K`

**提示（Prompt）**：外部 32.768 kHz 时钟源（External clock source）

**说明（Help）**

在启动时启用外部 32.768 kHz 时钟源（clock source），随后可将其选为 SoC 的主时钟参考（main clock reference）。译注：原文将 clock source 拼作 cloud source，此处按上下文译为时钟源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_SAML21 || CONFIG_SOC_SERIES_SAMR34 || CONFIG_SOC_SERIES_SAMR35) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.saml2x:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.saml2x#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAML21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAML21)、[`CONFIG_SOC_SERIES_SAMR34`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR34)、[`CONFIG_SOC_SERIES_SAMR35`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR35)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAML_XOSC32K_AS_MAIN"></a>

## 265.30 `CONFIG_SOC_ATMEL_SAML_XOSC32K_AS_MAIN`

**提示（Prompt）**：XOSC32K 外部振荡器（external oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAML_XOSC32K && <choice>
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.saml2x:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.saml2x#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 主时钟参考（Main clock reference）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAML_XOSC32K`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAML_XOSC32K)。

<a id="CONFIG_SOC_ATMEL_SAML_XOSC32K_CRYSTAL"></a>

## 265.31 `CONFIG_SOC_ATMEL_SAML_XOSC32K_CRYSTAL`

**提示（Prompt）**：外部 32.768 kHz 时钟使用晶体振荡器（crystal oscillator）

**说明（Help）**

启用晶体振荡器（crystal oscillator）；禁用时，要求 XIN32 上有时钟信号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAML_XOSC32K && (CONFIG_SOC_SERIES_SAML21 || CONFIG_SOC_SERIES_SAMR34 || CONFIG_SOC_SERIES_SAMR35) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.saml2x:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.saml2x#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 外部 32.768 kHz 时钟源（External clock source）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAML_XOSC32K`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAML_XOSC32K)、[`CONFIG_SOC_SERIES_SAML21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAML21)、[`CONFIG_SOC_SERIES_SAMR34`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR34)、[`CONFIG_SOC_SERIES_SAMR35`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR35)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAMR3X_RADIO_OFF_SETUP"></a>

## 265.32 `CONFIG_SOC_ATMEL_SAMR3X_RADIO_OFF_SETUP`

**提示（Prompt）**：未使用 LoRa 无线电时配置其引脚（Configure LoRa radio pins）

**说明（Help）**

如 DS70005356C 所述，LoRa 无线电的 SPI 引脚没有上拉（pull-up）。因此，在不使用无线电时，保持 CS 为高电平很重要，可避免意外行为和电流消耗增加。为进一步降低功耗，可保持 nRST 引脚为低电平，使无线电处于复位状态（reset state）。启用此选项时，会将 CS 和 nRST 分别配置为高电平和低电平。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_SAMR34 || CONFIG_SOC_SERIES_SAMR35) && (CONFIG_SOC_SERIES_SAML21 || CONFIG_SOC_SERIES_SAMR34 || CONFIG_SOC_SERIES_SAMR35) && CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**默认值（Defaults）**

```text
y if !CONFIG_LORA
```

**定义位置（Location）**：[`soc/atmel/sam0/common/Kconfig.saml2x:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/common/Kconfig.saml2x#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMR34`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR34)、[`CONFIG_SOC_SERIES_SAMR35`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMR35)、[`CONFIG_SOC_SERIES_SAML21`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAML21)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

<a id="CONFIG_SOC_ATMEL_SAM_DISABLE_ERASE_PIN"></a>

## 265.33 `CONFIG_SOC_ATMEL_SAM_DISABLE_ERASE_PIN`

**提示（Prompt）**：禁用 ERASE 擦除引脚（Disable ERASE pin）

**说明（Help）**

复位时，ERASE 引脚配置为系统 IO 模式（System IO mode）。将 ERASE 引脚置为 `1` 会完全擦除 Flash 存储器。设置此项会将该引脚切换到通用 IO 模式（general IO mode），交由 GPIO 模块控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM && !CONFIG_SOC_SERIES_SAM4L && CONFIG_SOC_FAMILY_ATMEL_SAM
```

**定义位置（Location）**：[`soc/atmel/sam/common/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/common/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SERIES_SAM4L`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM4L)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_SOC_ATMEL_SAM_EXT_MAINCK"></a>

## 265.34 `CONFIG_SOC_ATMEL_SAM_EXT_MAINCK`

**提示（Prompt）**：主时钟使用外部晶体振荡器（external crystal oscillator for main clock）

**说明（Help）**

主时钟（main clock）用于驱动锁相环（PLL），进而驱动处理器时钟。如果希望使用外部晶体振荡器驱动主时钟，请设为 `y`。注意，晶体上电后需要稳定，因此会增加约一秒启动时间。此处使用的晶体频率可以为 3～20 MHz。设为 `n` 时，使用运行在 12 MHz 的内部快速 RC 振荡器（fast RC oscillator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM && !CONFIG_SOC_SERIES_SAM4L && CONFIG_SOC_FAMILY_ATMEL_SAM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/atmel/sam/common/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/common/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 时钟（Clocks）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SERIES_SAM4L`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM4L)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_SOC_ATMEL_SAM_EXT_MAINCK_BYPASS"></a>

## 265.35 `CONFIG_SOC_ATMEL_SAM_EXT_MAINCK_BYPASS`

**提示（Prompt）**：外部晶体振荡器使用旁路模式（bypass mode）

**说明（Help）**

启用旁路模式（bypass mode）时，会绕过外部晶体振荡器，由外部时钟信号直接驱动主时钟。如果希望直接使用外部时钟信号而非晶体振荡器，请设为 `y`；设为 `n` 则正常使用外部晶体振荡器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAM_EXT_MAINCK && CONFIG_SOC_FAMILY_ATMEL_SAM && !CONFIG_SOC_SERIES_SAM4L && CONFIG_SOC_FAMILY_ATMEL_SAM
```

**定义位置（Location）**：[`soc/atmel/sam/common/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/common/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 时钟（Clocks） → 主时钟使用外部晶体振荡器（external crystal oscillator for main clock）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAM_EXT_MAINCK`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAM_EXT_MAINCK)、[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SERIES_SAM4L`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM4L)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_SOC_ATMEL_SAM_EXT_SLCK"></a>

## 265.36 `CONFIG_SOC_ATMEL_SAM_EXT_SLCK`

**提示（Prompt）**：慢时钟使用外部晶体振荡器（external crystal oscillator for slow clock）

**说明（Help）**

如果希望使用外部 32 kHz 晶体振荡器驱动慢时钟（slow clock），请设为 `y`。注意，晶体上电后需要稳定，因此会增加几秒启动时间。如果不需要准确、精密的定时器，请设为 `n`；慢时钟将由运行在 32 kHz 的内部快速 RC 振荡器（internal fast RC oscillator）驱动。译注：“快速”及 32 kHz 均按原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM && !CONFIG_SOC_SERIES_SAM4L && CONFIG_SOC_FAMILY_ATMEL_SAM
```

**定义位置（Location）**：[`soc/atmel/sam/common/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/common/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 时钟（Clocks）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SERIES_SAM4L`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM4L)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_SOC_ATMEL_SAM_MCK_PRESCALLER"></a>

## 265.37 `CONFIG_SOC_ATMEL_SAM_MCK_PRESCALLER`

**提示（Prompt）**：主时钟预分频器（MCK PRESCALLER）

**说明（Help）**

此预分频器定义主时钟源选择（Master Clock Source Selection，CSS）与自由运行时钟（Free Running clock，FCLK）之间的比值。PRES 的有效值为 1、2、3、4、8、16、32、64。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM && !CONFIG_SOC_SERIES_SAM4L && CONFIG_SOC_FAMILY_ATMEL_SAM
```

**默认值（Defaults）**

```text
2 if CONFIG_SOC_SERIES_SAM4E
1
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`soc/atmel/sam/common/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/common/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 时钟（Clocks） → 锁相环 A（PLL A）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SERIES_SAM4L`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM4L)、[`CONFIG_SOC_SERIES_SAM4E`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM4E)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_SOC_ATMEL_SAM_MDIV"></a>

## 265.38 `CONFIG_SOC_ATMEL_SAM_MDIV`

**提示（Prompt）**：主时钟分频值（MDIV）

**说明（Help）**

此分频值定义处理器时钟（HCLK）与主时钟（MCK）之间的比值；主时钟最大值为 150MHz：`MCK = HCLK / MDIV`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_SAMX7X && CONFIG_SOC_FAMILY_ATMEL_SAM && !CONFIG_SOC_SERIES_SAM4L && CONFIG_SOC_FAMILY_ATMEL_SAM
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 4]
```

**定义位置（Location）**：[`soc/atmel/sam/common/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/common/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 时钟（Clocks） → 锁相环 A（PLL A）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMX7X`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SERIES_SAM4L`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM4L)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_SOC_ATMEL_SAM_PLLA_DIVA"></a>

## 265.39 `CONFIG_SOC_ATMEL_SAM_PLLA_DIVA`

**提示（Prompt）**：锁相环分频值（PLL DIVA）

**说明（Help）**

这是锁相环（PLL）使用的分频值（DIVA）。处理器时钟为 `(MAINCK * (MULA + 1) / DIVA)`。开发板配置文件可以针对特定开发板覆盖此设置。默认条件为 `MULA == N`、`DIVA == 1` 时，PLL 将以主时钟频率的 N+1 倍运行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM && !CONFIG_SOC_SERIES_SAM4L && CONFIG_SOC_FAMILY_ATMEL_SAM
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`soc/atmel/sam/common/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/common/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 时钟（Clocks） → 锁相环 A（PLL A）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SERIES_SAM4L`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM4L)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_SOC_ATMEL_SAM_PLLA_MULA"></a>

## 265.40 `CONFIG_SOC_ATMEL_SAM_PLLA_MULA`

**提示（Prompt）**：锁相环倍频值（PLL MULA）

**说明（Help）**

这是锁相环（PLL）使用的倍频值（MULA）。处理器时钟为 `(MAINCK * (MULA + 1) / DIVA)`。开发板配置文件可以针对特定开发板覆盖此设置。默认条件为 `MULA == N`、`DIVA == 1` 时，PLL 将以主时钟频率的 N+1 倍运行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM && !CONFIG_SOC_SERIES_SAM4L && CONFIG_SOC_FAMILY_ATMEL_SAM
```

**默认值（Defaults）**

```text
6 if CONFIG_SOC_SERIES_SAM3X
9 if CONFIG_SOC_SERIES_SAM4S
19 if CONFIG_SOC_SERIES_SAM4E
24 if CONFIG_SOC_SERIES_SAMX7X
```

**取值范围（Ranges）**

```text
[1, 62]
```

**定义位置（Location）**：[`soc/atmel/sam/common/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/common/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 时钟（Clocks） → 锁相环 A（PLL A）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SERIES_SAM4L`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM4L)、[`CONFIG_SOC_SERIES_SAM3X`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM3X)、[`CONFIG_SOC_SERIES_SAM4S`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM4S)、[`CONFIG_SOC_SERIES_SAM4E`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM4E)、[`CONFIG_SOC_SERIES_SAMX7X`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAMX7X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_SOC_ATMEL_SAM_WAIT_MODE"></a>

## 265.41 `CONFIG_SOC_ATMEL_SAM_WAIT_MODE`

**提示（Prompt）**：CPU 进入等待模式而非睡眠模式（Wait mode instead of Sleep mode）

**说明（Help）**

进行 JTAG 调试时，CPU 时钟（HCLK）不应停止。为此，在主时钟使用外部晶体振荡器时，使 CPU 进入等待模式（Wait mode），而非睡眠模式（Sleep mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ATMEL_SAM_EXT_MAINCK && CONFIG_SOC_FAMILY_ATMEL_SAM && !CONFIG_SOC_SERIES_SAM4L && CONFIG_SOC_FAMILY_ATMEL_SAM
```

**默认值（Defaults）**

```text
y if CONFIG_DEBUG
```

**定义位置（Location）**：[`soc/atmel/sam/common/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/common/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ATMEL_SAM_EXT_MAINCK`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_ATMEL_SAM_EXT_MAINCK)、[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SERIES_SAM4L`](P265_soc_atmel_配置项参考.md#CONFIG_SOC_SERIES_SAM4L)、[`CONFIG_DEBUG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_SOC_SERIES_SAM3X"></a>

## 265.42 `CONFIG_SOC_SERIES_SAM3X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAM3X 微控制器系列支持（MCU Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAM3X4C
CONFIG_SOC_SAM3X4E
CONFIG_SOC_SAM3X8C
CONFIG_SOC_SAM3X8E
CONFIG_SOC_SAM3X8H
```

**定义位置（Location）**：[`soc/atmel/sam/sam3x/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/sam3x/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SAM3X4C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM3X4C)、[`CONFIG_SOC_SAM3X4E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM3X4E)、[`CONFIG_SOC_SAM3X8C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM3X8C)、[`CONFIG_SOC_SAM3X8E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM3X8E)、[`CONFIG_SOC_SAM3X8H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM3X8H)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`、`CONFIG_SOC_SAM3X4C`、`CONFIG_SOC_SAM3X4E`、`CONFIG_SOC_SAM3X8C`、`CONFIG_SOC_SAM3X8E`、`CONFIG_SOC_SAM3X8H`。

<a id="CONFIG_SOC_SERIES_SAM4E"></a>

## 265.43 `CONFIG_SOC_SERIES_SAM4E`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAM4E 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAM4E16E
CONFIG_SOC_SAM4E16C
CONFIG_SOC_SAM4E8E
CONFIG_SOC_SAM4E8C
```

**定义位置（Location）**：[`soc/atmel/sam/sam4e/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/sam4e/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SAM4E16E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4E16E)、[`CONFIG_SOC_SAM4E16C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4E16C)、[`CONFIG_SOC_SAM4E8E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4E8E)、[`CONFIG_SOC_SAM4E8C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4E8C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`、`CONFIG_SOC_SAM4E16E`、`CONFIG_SOC_SAM4E16C`、`CONFIG_SOC_SAM4E8E`、`CONFIG_SOC_SAM4E8C`。

<a id="CONFIG_SOC_SERIES_SAM4L"></a>

## 265.44 `CONFIG_SOC_SERIES_SAM4L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAM4L Cortex-M4 微控制器（microcontroller）支持。器件型号（Part No.）：SAM4LS8C、SAM4LS8B、SAM4LS8A、SAM4LS4C、SAM4LS4B、SAM4LS4A、SAM4LS2C、SAM4LS2B、SAM4LS2A、SAM4LC8C、SAM4LC8B、SAM4LC8A、SAM4LC4C、SAM4LC4B、SAM4LC4A、SAM4LC2C、SAM4LC2B、SAM4LC2A。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAM4LS2A
CONFIG_SOC_SAM4LS2B
CONFIG_SOC_SAM4LS2C
CONFIG_SOC_SAM4LS4A
CONFIG_SOC_SAM4LS4B
CONFIG_SOC_SAM4LS4C
CONFIG_SOC_SAM4LS8A
CONFIG_SOC_SAM4LS8B
CONFIG_SOC_SAM4LS8C
CONFIG_SOC_SAM4LC2A
CONFIG_SOC_SAM4LC2B
CONFIG_SOC_SAM4LC2C
CONFIG_SOC_SAM4LC4A
CONFIG_SOC_SAM4LC4B
CONFIG_SOC_SAM4LC4C
CONFIG_SOC_SAM4LC8A
CONFIG_SOC_SAM4LC8B
CONFIG_SOC_SAM4LC8C
```

**定义位置（Location）**：[`soc/atmel/sam/sam4l/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/sam4l/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SAM4LS2A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LS2A)、[`CONFIG_SOC_SAM4LS2B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LS2B)、[`CONFIG_SOC_SAM4LS2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LS2C)、[`CONFIG_SOC_SAM4LS4A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LS4A)、[`CONFIG_SOC_SAM4LS4B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LS4B)、[`CONFIG_SOC_SAM4LS4C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LS4C)、[`CONFIG_SOC_SAM4LS8A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LS8A)、[`CONFIG_SOC_SAM4LS8B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LS8B)、[`CONFIG_SOC_SAM4LS8C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LS8C)、[`CONFIG_SOC_SAM4LC2A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LC2A)、[`CONFIG_SOC_SAM4LC2B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LC2B)、[`CONFIG_SOC_SAM4LC2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LC2C)、[`CONFIG_SOC_SAM4LC4A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LC4A)、[`CONFIG_SOC_SAM4LC4B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LC4B)、[`CONFIG_SOC_SAM4LC4C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LC4C)、[`CONFIG_SOC_SAM4LC8A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LC8A)、[`CONFIG_SOC_SAM4LC8B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LC8B)、[`CONFIG_SOC_SAM4LC8C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4LC8C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`、`CONFIG_SOC_SAM4LS2A`、`CONFIG_SOC_SAM4LS2B`、`CONFIG_SOC_SAM4LS2C`、`CONFIG_SOC_SAM4LS4A`、`CONFIG_SOC_SAM4LS4B`、`CONFIG_SOC_SAM4LS4C`、`CONFIG_SOC_SAM4LS8A`、`CONFIG_SOC_SAM4LS8B`、`CONFIG_SOC_SAM4LS8C`、`CONFIG_SOC_SAM4LC2A`、`CONFIG_SOC_SAM4LC2B`、`CONFIG_SOC_SAM4LC2C`、`CONFIG_SOC_SAM4LC4A`、`CONFIG_SOC_SAM4LC4B`、`CONFIG_SOC_SAM4LC4C`、`CONFIG_SOC_SAM4LC8A`、`CONFIG_SOC_SAM4LC8B`、`CONFIG_SOC_SAM4LC8C`。

<a id="CONFIG_SOC_SERIES_SAM4S"></a>

## 265.45 `CONFIG_SOC_SERIES_SAM4S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAM4S Cortex-M4 微控制器（microcontroller）支持。器件型号（Part No.）：SAM4S16C、SAM4S16B、SAM4S8C、SAM4S8B、SAM4S4C、SAM4S4B、SAM4S4A、SAM4S2C、SAM4S2B、SAM4S2A。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAM4S2A
CONFIG_SOC_SAM4S2B
CONFIG_SOC_SAM4S2C
CONFIG_SOC_SAM4S4A
CONFIG_SOC_SAM4S4B
CONFIG_SOC_SAM4S4C
CONFIG_SOC_SAM4S8B
CONFIG_SOC_SAM4S8C
CONFIG_SOC_SAM4S16B
CONFIG_SOC_SAM4S16C
CONFIG_SOC_SAM4SA16C
```

**定义位置（Location）**：[`soc/atmel/sam/sam4s/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/sam4s/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_SAM4S2A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4S2A)、[`CONFIG_SOC_SAM4S2B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4S2B)、[`CONFIG_SOC_SAM4S2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4S2C)、[`CONFIG_SOC_SAM4S4A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4S4A)、[`CONFIG_SOC_SAM4S4B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4S4B)、[`CONFIG_SOC_SAM4S4C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4S4C)、[`CONFIG_SOC_SAM4S8B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4S8B)、[`CONFIG_SOC_SAM4S8C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4S8C)、[`CONFIG_SOC_SAM4S16B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4S16B)、[`CONFIG_SOC_SAM4S16C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4S16C)、[`CONFIG_SOC_SAM4SA16C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAM4SA16C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`、`CONFIG_SOC_SAM4S2A`、`CONFIG_SOC_SAM4S2B`、`CONFIG_SOC_SAM4S2C`、`CONFIG_SOC_SAM4S4A`、`CONFIG_SOC_SAM4S4B`、`CONFIG_SOC_SAM4S4C`、`CONFIG_SOC_SAM4S8B`、`CONFIG_SOC_SAM4S8C`、`CONFIG_SOC_SAM4S16B`、`CONFIG_SOC_SAM4S16C`、`CONFIG_SOC_SAM4SA16C`。

<a id="CONFIG_SOC_SERIES_SAMC20"></a>

## 265.46 `CONFIG_SOC_SERIES_SAMC20`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMC20 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAMC20E15A
CONFIG_SOC_SAMC20E16A
CONFIG_SOC_SAMC20E17A
CONFIG_SOC_SAMC20E18A
CONFIG_SOC_SAMC20G15A
CONFIG_SOC_SAMC20G16A
CONFIG_SOC_SAMC20G17A
CONFIG_SOC_SAMC20G18A
CONFIG_SOC_SAMC20J15A
CONFIG_SOC_SAMC20J16A
CONFIG_SOC_SAMC20J17A
CONFIG_SOC_SAMC20J18A
CONFIG_SOC_SAMC20J17AU
CONFIG_SOC_SAMC20J18AU
CONFIG_SOC_SAMC20N17A
CONFIG_SOC_SAMC20N18A
```

**定义位置（Location）**：[`soc/atmel/sam0/samc20/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samc20/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SAMC20E15A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20E15A)、[`CONFIG_SOC_SAMC20E16A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20E16A)、[`CONFIG_SOC_SAMC20E17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20E17A)、[`CONFIG_SOC_SAMC20E18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20E18A)、[`CONFIG_SOC_SAMC20G15A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20G15A)、[`CONFIG_SOC_SAMC20G16A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20G16A)、[`CONFIG_SOC_SAMC20G17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20G17A)、[`CONFIG_SOC_SAMC20G18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20G18A)、[`CONFIG_SOC_SAMC20J15A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20J15A)、[`CONFIG_SOC_SAMC20J16A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20J16A)、[`CONFIG_SOC_SAMC20J17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20J17A)、[`CONFIG_SOC_SAMC20J18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20J18A)、[`CONFIG_SOC_SAMC20J17AU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20J17AU)、[`CONFIG_SOC_SAMC20J18AU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20J18AU)、[`CONFIG_SOC_SAMC20N17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20N17A)、[`CONFIG_SOC_SAMC20N18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC20N18A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SAMC20E15A`、`CONFIG_SOC_SAMC20E16A`、`CONFIG_SOC_SAMC20E17A`、`CONFIG_SOC_SAMC20E18A`、`CONFIG_SOC_SAMC20G15A`、`CONFIG_SOC_SAMC20G16A`、`CONFIG_SOC_SAMC20G17A`、`CONFIG_SOC_SAMC20G18A`、`CONFIG_SOC_SAMC20J15A`、`CONFIG_SOC_SAMC20J16A`、`CONFIG_SOC_SAMC20J17A`、`CONFIG_SOC_SAMC20J18A`、`CONFIG_SOC_SAMC20J17AU`、`CONFIG_SOC_SAMC20J18AU`、`CONFIG_SOC_SAMC20N17A`、`CONFIG_SOC_SAMC20N18A`。

<a id="CONFIG_SOC_SERIES_SAMC21"></a>

## 265.47 `CONFIG_SOC_SERIES_SAMC21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMC21 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAMC21E15A
CONFIG_SOC_SAMC21E16A
CONFIG_SOC_SAMC21E17A
CONFIG_SOC_SAMC21E18A
CONFIG_SOC_SAMC21G15A
CONFIG_SOC_SAMC21G16A
CONFIG_SOC_SAMC21G17A
CONFIG_SOC_SAMC21G18A
CONFIG_SOC_SAMC21J15A
CONFIG_SOC_SAMC21J16A
CONFIG_SOC_SAMC21J17A
CONFIG_SOC_SAMC21J18A
CONFIG_SOC_SAMC21J17AU
CONFIG_SOC_SAMC21J18AU
CONFIG_SOC_SAMC21N17A
CONFIG_SOC_SAMC21N18A
```

**定义位置（Location）**：[`soc/atmel/sam0/samc21/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samc21/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SAMC21E15A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21E15A)、[`CONFIG_SOC_SAMC21E16A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21E16A)、[`CONFIG_SOC_SAMC21E17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21E17A)、[`CONFIG_SOC_SAMC21E18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21E18A)、[`CONFIG_SOC_SAMC21G15A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21G15A)、[`CONFIG_SOC_SAMC21G16A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21G16A)、[`CONFIG_SOC_SAMC21G17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21G17A)、[`CONFIG_SOC_SAMC21G18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21G18A)、[`CONFIG_SOC_SAMC21J15A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21J15A)、[`CONFIG_SOC_SAMC21J16A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21J16A)、[`CONFIG_SOC_SAMC21J17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21J17A)、[`CONFIG_SOC_SAMC21J18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21J18A)、[`CONFIG_SOC_SAMC21J17AU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21J17AU)、[`CONFIG_SOC_SAMC21J18AU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21J18AU)、[`CONFIG_SOC_SAMC21N17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21N17A)、[`CONFIG_SOC_SAMC21N18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMC21N18A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SAMC21E15A`、`CONFIG_SOC_SAMC21E16A`、`CONFIG_SOC_SAMC21E17A`、`CONFIG_SOC_SAMC21E18A`、`CONFIG_SOC_SAMC21G15A`、`CONFIG_SOC_SAMC21G16A`、`CONFIG_SOC_SAMC21G17A`、`CONFIG_SOC_SAMC21G18A`、`CONFIG_SOC_SAMC21J15A`、`CONFIG_SOC_SAMC21J16A`、`CONFIG_SOC_SAMC21J17A`、`CONFIG_SOC_SAMC21J18A`、`CONFIG_SOC_SAMC21J17AU`、`CONFIG_SOC_SAMC21J18AU`、`CONFIG_SOC_SAMC21N17A`、`CONFIG_SOC_SAMC21N18A`。

<a id="CONFIG_SOC_SERIES_SAMD20"></a>

## 265.48 `CONFIG_SOC_SERIES_SAMD20`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMD20 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAMD20E14
CONFIG_SOC_SAMD20E15
CONFIG_SOC_SAMD20E16
CONFIG_SOC_SAMD20E17
CONFIG_SOC_SAMD20E18
CONFIG_SOC_SAMD20G14
CONFIG_SOC_SAMD20G15
CONFIG_SOC_SAMD20G16
CONFIG_SOC_SAMD20G18
CONFIG_SOC_SAMD20G17U
CONFIG_SOC_SAMD20G18U
CONFIG_SOC_SAMD20J14
CONFIG_SOC_SAMD20J15
CONFIG_SOC_SAMD20J16
CONFIG_SOC_SAMD20J17
CONFIG_SOC_SAMD20J18
```

**定义位置（Location）**：[`soc/atmel/sam0/samd20/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samd20/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SAMD20E14`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20E14)、[`CONFIG_SOC_SAMD20E15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20E15)、[`CONFIG_SOC_SAMD20E16`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20E16)、[`CONFIG_SOC_SAMD20E17`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20E17)、[`CONFIG_SOC_SAMD20E18`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20E18)、[`CONFIG_SOC_SAMD20G14`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20G14)、[`CONFIG_SOC_SAMD20G15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20G15)、[`CONFIG_SOC_SAMD20G16`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20G16)、[`CONFIG_SOC_SAMD20G18`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20G18)、[`CONFIG_SOC_SAMD20G17U`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20G17U)、[`CONFIG_SOC_SAMD20G18U`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20G18U)、[`CONFIG_SOC_SAMD20J14`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20J14)、[`CONFIG_SOC_SAMD20J15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20J15)、[`CONFIG_SOC_SAMD20J16`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20J16)、[`CONFIG_SOC_SAMD20J17`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20J17)、[`CONFIG_SOC_SAMD20J18`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD20J18)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SAMD20E14`、`CONFIG_SOC_SAMD20E15`、`CONFIG_SOC_SAMD20E16`、`CONFIG_SOC_SAMD20E17`、`CONFIG_SOC_SAMD20E18`、`CONFIG_SOC_SAMD20G14`、`CONFIG_SOC_SAMD20G15`、`CONFIG_SOC_SAMD20G16`、`CONFIG_SOC_SAMD20G18`、`CONFIG_SOC_SAMD20G17U`、`CONFIG_SOC_SAMD20G18U`、`CONFIG_SOC_SAMD20J14`、`CONFIG_SOC_SAMD20J15`、`CONFIG_SOC_SAMD20J16`、`CONFIG_SOC_SAMD20J17`、`CONFIG_SOC_SAMD20J18`。

<a id="CONFIG_SOC_SERIES_SAMD21"></a>

## 265.49 `CONFIG_SOC_SERIES_SAMD21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMD21 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAMD21E15A
CONFIG_SOC_SAMD21E16A
CONFIG_SOC_SAMD21E17A
CONFIG_SOC_SAMD21E18A
CONFIG_SOC_SAMD21E19A
CONFIG_SOC_SAMD21G15A
CONFIG_SOC_SAMD21G16A
CONFIG_SOC_SAMD21G17A
CONFIG_SOC_SAMD21G18A
CONFIG_SOC_SAMD21G17AU
CONFIG_SOC_SAMD21G18AU
CONFIG_SOC_SAMD21J15A
CONFIG_SOC_SAMD21J16A
CONFIG_SOC_SAMD21J17A
CONFIG_SOC_SAMD21J18A
```

**定义位置（Location）**：[`soc/atmel/sam0/samd21/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samd21/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SAMD21E15A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21E15A)、[`CONFIG_SOC_SAMD21E16A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21E16A)、[`CONFIG_SOC_SAMD21E17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21E17A)、[`CONFIG_SOC_SAMD21E18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21E18A)、[`CONFIG_SOC_SAMD21E19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21E19A)、[`CONFIG_SOC_SAMD21G15A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21G15A)、[`CONFIG_SOC_SAMD21G16A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21G16A)、[`CONFIG_SOC_SAMD21G17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21G17A)、[`CONFIG_SOC_SAMD21G18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21G18A)、[`CONFIG_SOC_SAMD21G17AU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21G17AU)、[`CONFIG_SOC_SAMD21G18AU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21G18AU)、[`CONFIG_SOC_SAMD21J15A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21J15A)、[`CONFIG_SOC_SAMD21J16A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21J16A)、[`CONFIG_SOC_SAMD21J17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21J17A)、[`CONFIG_SOC_SAMD21J18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD21J18A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SAMD21E15A`、`CONFIG_SOC_SAMD21E16A`、`CONFIG_SOC_SAMD21E17A`、`CONFIG_SOC_SAMD21E18A`、`CONFIG_SOC_SAMD21E19A`、`CONFIG_SOC_SAMD21G15A`、`CONFIG_SOC_SAMD21G16A`、`CONFIG_SOC_SAMD21G17A`、`CONFIG_SOC_SAMD21G18A`、`CONFIG_SOC_SAMD21G17AU`、`CONFIG_SOC_SAMD21G18AU`、`CONFIG_SOC_SAMD21J15A`、`CONFIG_SOC_SAMD21J16A`、`CONFIG_SOC_SAMD21J17A`、`CONFIG_SOC_SAMD21J18A`。

<a id="CONFIG_SOC_SERIES_SAMD51"></a>

## 265.50 `CONFIG_SOC_SERIES_SAMD51`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMD51 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAMD51G18A
CONFIG_SOC_SAMD51G19A
CONFIG_SOC_SAMD51J18A
CONFIG_SOC_SAMD51J19A
CONFIG_SOC_SAMD51J20A
CONFIG_SOC_SAMD51N19A
CONFIG_SOC_SAMD51N20A
CONFIG_SOC_SAMD51P19A
CONFIG_SOC_SAMD51P20A
```

**定义位置（Location）**：[`soc/atmel/sam0/samd51/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samd51/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SAMD51G18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD51G18A)、[`CONFIG_SOC_SAMD51G19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD51G19A)、[`CONFIG_SOC_SAMD51J18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD51J18A)、[`CONFIG_SOC_SAMD51J19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD51J19A)、[`CONFIG_SOC_SAMD51J20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD51J20A)、[`CONFIG_SOC_SAMD51N19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD51N19A)、[`CONFIG_SOC_SAMD51N20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD51N20A)、[`CONFIG_SOC_SAMD51P19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD51P19A)、[`CONFIG_SOC_SAMD51P20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMD51P20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SAMD51G18A`、`CONFIG_SOC_SAMD51G19A`、`CONFIG_SOC_SAMD51J18A`、`CONFIG_SOC_SAMD51J19A`、`CONFIG_SOC_SAMD51J20A`、`CONFIG_SOC_SAMD51N19A`、`CONFIG_SOC_SAMD51N20A`、`CONFIG_SOC_SAMD51P19A`、`CONFIG_SOC_SAMD51P20A`。

<a id="CONFIG_SOC_SERIES_SAME51"></a>

## 265.51 `CONFIG_SOC_SERIES_SAME51`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAME51 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAME51J18A
CONFIG_SOC_SAME51J19A
CONFIG_SOC_SAME51J20A
CONFIG_SOC_SAME51N19A
CONFIG_SOC_SAME51N20A
```

**定义位置（Location）**：[`soc/atmel/sam0/same51/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/same51/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SAME51J18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME51J18A)、[`CONFIG_SOC_SAME51J19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME51J19A)、[`CONFIG_SOC_SAME51J20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME51J20A)、[`CONFIG_SOC_SAME51N19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME51N19A)、[`CONFIG_SOC_SAME51N20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME51N20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SAME51J18A`、`CONFIG_SOC_SAME51J19A`、`CONFIG_SOC_SAME51J20A`、`CONFIG_SOC_SAME51N19A`、`CONFIG_SOC_SAME51N20A`。

<a id="CONFIG_SOC_SERIES_SAME53"></a>

## 265.52 `CONFIG_SOC_SERIES_SAME53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAME53 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAME53J18A
CONFIG_SOC_SAME53J19A
CONFIG_SOC_SAME53J20A
CONFIG_SOC_SAME53N19A
CONFIG_SOC_SAME53N20A
```

**定义位置（Location）**：[`soc/atmel/sam0/same53/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/same53/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SAME53J18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME53J18A)、[`CONFIG_SOC_SAME53J19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME53J19A)、[`CONFIG_SOC_SAME53J20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME53J20A)、[`CONFIG_SOC_SAME53N19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME53N19A)、[`CONFIG_SOC_SAME53N20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME53N20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SAME53J18A`、`CONFIG_SOC_SAME53J19A`、`CONFIG_SOC_SAME53J20A`、`CONFIG_SOC_SAME53N19A`、`CONFIG_SOC_SAME53N20A`。

<a id="CONFIG_SOC_SERIES_SAME54"></a>

## 265.53 `CONFIG_SOC_SERIES_SAME54`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAME54 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAME54N19A
CONFIG_SOC_SAME54N20A
CONFIG_SOC_SAME54P19A
CONFIG_SOC_SAME54P20A
```

**定义位置（Location）**：[`soc/atmel/sam0/same54/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/same54/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SAME54N19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME54N19A)、[`CONFIG_SOC_SAME54N20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME54N20A)、[`CONFIG_SOC_SAME54P19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME54P19A)、[`CONFIG_SOC_SAME54P20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAME54P20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SAME54N19A`、`CONFIG_SOC_SAME54N20A`、`CONFIG_SOC_SAME54P19A`、`CONFIG_SOC_SAME54P20A`。

<a id="CONFIG_SOC_SERIES_SAML21"></a>

## 265.54 `CONFIG_SOC_SERIES_SAML21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAML21 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAML21E15B
CONFIG_SOC_SAML21E16B
CONFIG_SOC_SAML21E17B
CONFIG_SOC_SAML21E18B
CONFIG_SOC_SAML21G16B
CONFIG_SOC_SAML21G17B
CONFIG_SOC_SAML21G18B
CONFIG_SOC_SAML21J16B
CONFIG_SOC_SAML21J17B
CONFIG_SOC_SAML21J18B
CONFIG_SOC_SAML21J17BU
CONFIG_SOC_SAML21J18BU
```

**定义位置（Location）**：[`soc/atmel/sam0/saml21/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/saml21/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SAML21E15B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAML21E15B)、[`CONFIG_SOC_SAML21E16B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAML21E16B)、[`CONFIG_SOC_SAML21E17B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAML21E17B)、[`CONFIG_SOC_SAML21E18B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAML21E18B)、[`CONFIG_SOC_SAML21G16B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAML21G16B)、[`CONFIG_SOC_SAML21G17B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAML21G17B)、[`CONFIG_SOC_SAML21G18B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAML21G18B)、[`CONFIG_SOC_SAML21J16B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAML21J16B)、[`CONFIG_SOC_SAML21J17B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAML21J17B)、[`CONFIG_SOC_SAML21J18B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAML21J18B)、[`CONFIG_SOC_SAML21J17BU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAML21J17BU)、[`CONFIG_SOC_SAML21J18BU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAML21J18BU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SAML21E15B`、`CONFIG_SOC_SAML21E16B`、`CONFIG_SOC_SAML21E17B`、`CONFIG_SOC_SAML21E18B`、`CONFIG_SOC_SAML21G16B`、`CONFIG_SOC_SAML21G17B`、`CONFIG_SOC_SAML21G18B`、`CONFIG_SOC_SAML21J16B`、`CONFIG_SOC_SAML21J17B`、`CONFIG_SOC_SAML21J18B`、`CONFIG_SOC_SAML21J17BU`、`CONFIG_SOC_SAML21J18BU`。

<a id="CONFIG_SOC_SERIES_SAMR21"></a>

## 265.55 `CONFIG_SOC_SERIES_SAMR21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMR21 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAMR21E16A
CONFIG_SOC_SAMR21E17A
CONFIG_SOC_SAMR21E18A
CONFIG_SOC_SAMR21E19A
CONFIG_SOC_SAMR21G16A
CONFIG_SOC_SAMR21G17A
CONFIG_SOC_SAMR21G18A
```

**定义位置（Location）**：[`soc/atmel/sam0/samr21/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samr21/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SAMR21E16A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR21E16A)、[`CONFIG_SOC_SAMR21E17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR21E17A)、[`CONFIG_SOC_SAMR21E18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR21E18A)、[`CONFIG_SOC_SAMR21E19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR21E19A)、[`CONFIG_SOC_SAMR21G16A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR21G16A)、[`CONFIG_SOC_SAMR21G17A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR21G17A)、[`CONFIG_SOC_SAMR21G18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR21G18A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SAMR21E16A`、`CONFIG_SOC_SAMR21E17A`、`CONFIG_SOC_SAMR21E18A`、`CONFIG_SOC_SAMR21E19A`、`CONFIG_SOC_SAMR21G16A`、`CONFIG_SOC_SAMR21G17A`、`CONFIG_SOC_SAMR21G18A`。

<a id="CONFIG_SOC_SERIES_SAMR34"></a>

## 265.56 `CONFIG_SOC_SERIES_SAMR34`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMR34 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAMR34J16B
CONFIG_SOC_SAMR34J17B
CONFIG_SOC_SAMR34J18B
```

**定义位置（Location）**：[`soc/atmel/sam0/samr34/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samr34/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SAMR34J16B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR34J16B)、[`CONFIG_SOC_SAMR34J17B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR34J17B)、[`CONFIG_SOC_SAMR34J18B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR34J18B)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SAMR34J16B`、`CONFIG_SOC_SAMR34J17B`、`CONFIG_SOC_SAMR34J18B`。

<a id="CONFIG_SOC_SERIES_SAMR35"></a>

## 265.57 `CONFIG_SOC_SERIES_SAMR35`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMR35 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAMR35J16B
CONFIG_SOC_SAMR35J17B
CONFIG_SOC_SAMR35J18B
```

**定义位置（Location）**：[`soc/atmel/sam0/samr35/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samr35/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SAMR35J16B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR35J16B)、[`CONFIG_SOC_SAMR35J17B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR35J17B)、[`CONFIG_SOC_SAMR35J18B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMR35J18B)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SAMR35J16B`、`CONFIG_SOC_SAMR35J17B`、`CONFIG_SOC_SAMR35J18B`。

<a id="CONFIG_SOC_SERIES_SAMX7X"></a>

## 265.58 `CONFIG_SOC_SERIES_SAMX7X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAM E70／S70／V70／V71 ARM Cortex-M7 微控制器（Microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ATMEL_SAM
```

**被选择（Selected by）**

```text
CONFIG_SOC_ATMEL_SAME70
CONFIG_SOC_ATMEL_SAME70_REVB
CONFIG_SOC_ATMEL_SAMV71
CONFIG_SOC_ATMEL_SAMV71_REVB
```

**定义位置（Location）**：[`soc/atmel/sam/samx7x/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/samx7x/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_ATMEL_SAME70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATMEL_SAME70)、[`CONFIG_SOC_ATMEL_SAME70_REVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATMEL_SAME70_REVB)、[`CONFIG_SOC_ATMEL_SAMV71`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATMEL_SAMV71)、[`CONFIG_SOC_ATMEL_SAMV71_REVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATMEL_SAMV71_REVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`、`CONFIG_SOC_ATMEL_SAME70`、`CONFIG_SOC_ATMEL_SAME70_REVB`、`CONFIG_SOC_ATMEL_SAMV71`、`CONFIG_SOC_ATMEL_SAMV71_REVB`。

<a id="SB_CONFIG_SOC_SERIES_SAM3X"></a>

## 265.59 `SB_CONFIG_SOC_SERIES_SAM3X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAM3X 微控制器系列支持（MCU Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAM3X4C
SB_CONFIG_SOC_SAM3X4E
SB_CONFIG_SOC_SAM3X8C
SB_CONFIG_SOC_SAM3X8E
SB_CONFIG_SOC_SAM3X8H
```

**定义位置（Location）**：[`soc/atmel/sam/sam3x/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/sam3x/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM)、[`SB_CONFIG_SOC_SAM3X4C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM3X4C)、[`SB_CONFIG_SOC_SAM3X4E`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM3X4E)、[`SB_CONFIG_SOC_SAM3X8C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM3X8C)、[`SB_CONFIG_SOC_SAM3X8E`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM3X8E)、[`SB_CONFIG_SOC_SAM3X8H`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM3X8H)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM`、`SB_CONFIG_SOC_SAM3X4C`、`SB_CONFIG_SOC_SAM3X4E`、`SB_CONFIG_SOC_SAM3X8C`、`SB_CONFIG_SOC_SAM3X8E`、`SB_CONFIG_SOC_SAM3X8H`。

<a id="SB_CONFIG_SOC_SERIES_SAM4E"></a>

## 265.60 `SB_CONFIG_SOC_SERIES_SAM4E`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAM4E 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAM4E16E
SB_CONFIG_SOC_SAM4E16C
SB_CONFIG_SOC_SAM4E8E
SB_CONFIG_SOC_SAM4E8C
```

**定义位置（Location）**：[`soc/atmel/sam/sam4e/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/sam4e/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM)、[`SB_CONFIG_SOC_SAM4E16E`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4E16E)、[`SB_CONFIG_SOC_SAM4E16C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4E16C)、[`SB_CONFIG_SOC_SAM4E8E`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4E8E)、[`SB_CONFIG_SOC_SAM4E8C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4E8C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM`、`SB_CONFIG_SOC_SAM4E16E`、`SB_CONFIG_SOC_SAM4E16C`、`SB_CONFIG_SOC_SAM4E8E`、`SB_CONFIG_SOC_SAM4E8C`。

<a id="SB_CONFIG_SOC_SERIES_SAM4L"></a>

## 265.61 `SB_CONFIG_SOC_SERIES_SAM4L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAM4L Cortex-M4 微控制器（microcontroller）支持。器件型号（Part No.）：SAM4LS8C、SAM4LS8B、SAM4LS8A、SAM4LS4C、SAM4LS4B、SAM4LS4A、SAM4LS2C、SAM4LS2B、SAM4LS2A、SAM4LC8C、SAM4LC8B、SAM4LC8A、SAM4LC4C、SAM4LC4B、SAM4LC4A、SAM4LC2C、SAM4LC2B、SAM4LC2A。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAM4LS2A
SB_CONFIG_SOC_SAM4LS2B
SB_CONFIG_SOC_SAM4LS2C
SB_CONFIG_SOC_SAM4LS4A
SB_CONFIG_SOC_SAM4LS4B
SB_CONFIG_SOC_SAM4LS4C
SB_CONFIG_SOC_SAM4LS8A
SB_CONFIG_SOC_SAM4LS8B
SB_CONFIG_SOC_SAM4LS8C
SB_CONFIG_SOC_SAM4LC2A
SB_CONFIG_SOC_SAM4LC2B
SB_CONFIG_SOC_SAM4LC2C
SB_CONFIG_SOC_SAM4LC4A
SB_CONFIG_SOC_SAM4LC4B
SB_CONFIG_SOC_SAM4LC4C
SB_CONFIG_SOC_SAM4LC8A
SB_CONFIG_SOC_SAM4LC8B
SB_CONFIG_SOC_SAM4LC8C
```

**定义位置（Location）**：[`soc/atmel/sam/sam4l/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/sam4l/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM)、[`SB_CONFIG_SOC_SAM4LS2A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LS2A)、[`SB_CONFIG_SOC_SAM4LS2B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LS2B)、[`SB_CONFIG_SOC_SAM4LS2C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LS2C)、[`SB_CONFIG_SOC_SAM4LS4A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LS4A)、[`SB_CONFIG_SOC_SAM4LS4B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LS4B)、[`SB_CONFIG_SOC_SAM4LS4C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LS4C)、[`SB_CONFIG_SOC_SAM4LS8A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LS8A)、[`SB_CONFIG_SOC_SAM4LS8B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LS8B)、[`SB_CONFIG_SOC_SAM4LS8C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LS8C)、[`SB_CONFIG_SOC_SAM4LC2A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LC2A)、[`SB_CONFIG_SOC_SAM4LC2B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LC2B)、[`SB_CONFIG_SOC_SAM4LC2C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LC2C)、[`SB_CONFIG_SOC_SAM4LC4A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LC4A)、[`SB_CONFIG_SOC_SAM4LC4B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LC4B)、[`SB_CONFIG_SOC_SAM4LC4C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LC4C)、[`SB_CONFIG_SOC_SAM4LC8A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LC8A)、[`SB_CONFIG_SOC_SAM4LC8B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LC8B)、[`SB_CONFIG_SOC_SAM4LC8C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4LC8C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM`、`SB_CONFIG_SOC_SAM4LS2A`、`SB_CONFIG_SOC_SAM4LS2B`、`SB_CONFIG_SOC_SAM4LS2C`、`SB_CONFIG_SOC_SAM4LS4A`、`SB_CONFIG_SOC_SAM4LS4B`、`SB_CONFIG_SOC_SAM4LS4C`、`SB_CONFIG_SOC_SAM4LS8A`、`SB_CONFIG_SOC_SAM4LS8B`、`SB_CONFIG_SOC_SAM4LS8C`、`SB_CONFIG_SOC_SAM4LC2A`、`SB_CONFIG_SOC_SAM4LC2B`、`SB_CONFIG_SOC_SAM4LC2C`、`SB_CONFIG_SOC_SAM4LC4A`、`SB_CONFIG_SOC_SAM4LC4B`、`SB_CONFIG_SOC_SAM4LC4C`、`SB_CONFIG_SOC_SAM4LC8A`、`SB_CONFIG_SOC_SAM4LC8B`、`SB_CONFIG_SOC_SAM4LC8C`。

<a id="SB_CONFIG_SOC_SERIES_SAM4S"></a>

## 265.62 `SB_CONFIG_SOC_SERIES_SAM4S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAM4S Cortex-M4 微控制器（microcontroller）支持。器件型号（Part No.）：SAM4S16C、SAM4S16B、SAM4S8C、SAM4S8B、SAM4S4C、SAM4S4B、SAM4S4A、SAM4S2C、SAM4S2B、SAM4S2A。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAM4S2A
SB_CONFIG_SOC_SAM4S2B
SB_CONFIG_SOC_SAM4S2C
SB_CONFIG_SOC_SAM4S4A
SB_CONFIG_SOC_SAM4S4B
SB_CONFIG_SOC_SAM4S4C
SB_CONFIG_SOC_SAM4S8B
SB_CONFIG_SOC_SAM4S8C
SB_CONFIG_SOC_SAM4S16B
SB_CONFIG_SOC_SAM4S16C
SB_CONFIG_SOC_SAM4SA16C
```

**定义位置（Location）**：[`soc/atmel/sam/sam4s/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/sam4s/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM)、[`SB_CONFIG_SOC_SAM4S2A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4S2A)、[`SB_CONFIG_SOC_SAM4S2B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4S2B)、[`SB_CONFIG_SOC_SAM4S2C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4S2C)、[`SB_CONFIG_SOC_SAM4S4A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4S4A)、[`SB_CONFIG_SOC_SAM4S4B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4S4B)、[`SB_CONFIG_SOC_SAM4S4C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4S4C)、[`SB_CONFIG_SOC_SAM4S8B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4S8B)、[`SB_CONFIG_SOC_SAM4S8C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4S8C)、[`SB_CONFIG_SOC_SAM4S16B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4S16B)、[`SB_CONFIG_SOC_SAM4S16C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4S16C)、[`SB_CONFIG_SOC_SAM4SA16C`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAM4SA16C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM`、`SB_CONFIG_SOC_SAM4S2A`、`SB_CONFIG_SOC_SAM4S2B`、`SB_CONFIG_SOC_SAM4S2C`、`SB_CONFIG_SOC_SAM4S4A`、`SB_CONFIG_SOC_SAM4S4B`、`SB_CONFIG_SOC_SAM4S4C`、`SB_CONFIG_SOC_SAM4S8B`、`SB_CONFIG_SOC_SAM4S8C`、`SB_CONFIG_SOC_SAM4S16B`、`SB_CONFIG_SOC_SAM4S16C`、`SB_CONFIG_SOC_SAM4SA16C`。

<a id="SB_CONFIG_SOC_SERIES_SAMC20"></a>

## 265.63 `SB_CONFIG_SOC_SERIES_SAMC20`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMC20 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAMC20E15A
SB_CONFIG_SOC_SAMC20E16A
SB_CONFIG_SOC_SAMC20E17A
SB_CONFIG_SOC_SAMC20E18A
SB_CONFIG_SOC_SAMC20G15A
SB_CONFIG_SOC_SAMC20G16A
SB_CONFIG_SOC_SAMC20G17A
SB_CONFIG_SOC_SAMC20G18A
SB_CONFIG_SOC_SAMC20J15A
SB_CONFIG_SOC_SAMC20J16A
SB_CONFIG_SOC_SAMC20J17A
SB_CONFIG_SOC_SAMC20J18A
SB_CONFIG_SOC_SAMC20J17AU
SB_CONFIG_SOC_SAMC20J18AU
SB_CONFIG_SOC_SAMC20N17A
SB_CONFIG_SOC_SAMC20N18A
```

**定义位置（Location）**：[`soc/atmel/sam0/samc20/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samc20/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`SB_CONFIG_SOC_SAMC20E15A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20E15A)、[`SB_CONFIG_SOC_SAMC20E16A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20E16A)、[`SB_CONFIG_SOC_SAMC20E17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20E17A)、[`SB_CONFIG_SOC_SAMC20E18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20E18A)、[`SB_CONFIG_SOC_SAMC20G15A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20G15A)、[`SB_CONFIG_SOC_SAMC20G16A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20G16A)、[`SB_CONFIG_SOC_SAMC20G17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20G17A)、[`SB_CONFIG_SOC_SAMC20G18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20G18A)、[`SB_CONFIG_SOC_SAMC20J15A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20J15A)、[`SB_CONFIG_SOC_SAMC20J16A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20J16A)、[`SB_CONFIG_SOC_SAMC20J17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20J17A)、[`SB_CONFIG_SOC_SAMC20J18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20J18A)、[`SB_CONFIG_SOC_SAMC20J17AU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20J17AU)、[`SB_CONFIG_SOC_SAMC20J18AU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20J18AU)、[`SB_CONFIG_SOC_SAMC20N17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20N17A)、[`SB_CONFIG_SOC_SAMC20N18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC20N18A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`、`SB_CONFIG_SOC_SAMC20E15A`、`SB_CONFIG_SOC_SAMC20E16A`、`SB_CONFIG_SOC_SAMC20E17A`、`SB_CONFIG_SOC_SAMC20E18A`、`SB_CONFIG_SOC_SAMC20G15A`、`SB_CONFIG_SOC_SAMC20G16A`、`SB_CONFIG_SOC_SAMC20G17A`、`SB_CONFIG_SOC_SAMC20G18A`、`SB_CONFIG_SOC_SAMC20J15A`、`SB_CONFIG_SOC_SAMC20J16A`、`SB_CONFIG_SOC_SAMC20J17A`、`SB_CONFIG_SOC_SAMC20J18A`、`SB_CONFIG_SOC_SAMC20J17AU`、`SB_CONFIG_SOC_SAMC20J18AU`、`SB_CONFIG_SOC_SAMC20N17A`、`SB_CONFIG_SOC_SAMC20N18A`。

<a id="SB_CONFIG_SOC_SERIES_SAMC21"></a>

## 265.64 `SB_CONFIG_SOC_SERIES_SAMC21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMC21 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAMC21E15A
SB_CONFIG_SOC_SAMC21E16A
SB_CONFIG_SOC_SAMC21E17A
SB_CONFIG_SOC_SAMC21E18A
SB_CONFIG_SOC_SAMC21G15A
SB_CONFIG_SOC_SAMC21G16A
SB_CONFIG_SOC_SAMC21G17A
SB_CONFIG_SOC_SAMC21G18A
SB_CONFIG_SOC_SAMC21J15A
SB_CONFIG_SOC_SAMC21J16A
SB_CONFIG_SOC_SAMC21J17A
SB_CONFIG_SOC_SAMC21J18A
SB_CONFIG_SOC_SAMC21J17AU
SB_CONFIG_SOC_SAMC21J18AU
SB_CONFIG_SOC_SAMC21N17A
SB_CONFIG_SOC_SAMC21N18A
```

**定义位置（Location）**：[`soc/atmel/sam0/samc21/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samc21/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`SB_CONFIG_SOC_SAMC21E15A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21E15A)、[`SB_CONFIG_SOC_SAMC21E16A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21E16A)、[`SB_CONFIG_SOC_SAMC21E17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21E17A)、[`SB_CONFIG_SOC_SAMC21E18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21E18A)、[`SB_CONFIG_SOC_SAMC21G15A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21G15A)、[`SB_CONFIG_SOC_SAMC21G16A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21G16A)、[`SB_CONFIG_SOC_SAMC21G17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21G17A)、[`SB_CONFIG_SOC_SAMC21G18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21G18A)、[`SB_CONFIG_SOC_SAMC21J15A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21J15A)、[`SB_CONFIG_SOC_SAMC21J16A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21J16A)、[`SB_CONFIG_SOC_SAMC21J17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21J17A)、[`SB_CONFIG_SOC_SAMC21J18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21J18A)、[`SB_CONFIG_SOC_SAMC21J17AU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21J17AU)、[`SB_CONFIG_SOC_SAMC21J18AU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21J18AU)、[`SB_CONFIG_SOC_SAMC21N17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21N17A)、[`SB_CONFIG_SOC_SAMC21N18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMC21N18A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`、`SB_CONFIG_SOC_SAMC21E15A`、`SB_CONFIG_SOC_SAMC21E16A`、`SB_CONFIG_SOC_SAMC21E17A`、`SB_CONFIG_SOC_SAMC21E18A`、`SB_CONFIG_SOC_SAMC21G15A`、`SB_CONFIG_SOC_SAMC21G16A`、`SB_CONFIG_SOC_SAMC21G17A`、`SB_CONFIG_SOC_SAMC21G18A`、`SB_CONFIG_SOC_SAMC21J15A`、`SB_CONFIG_SOC_SAMC21J16A`、`SB_CONFIG_SOC_SAMC21J17A`、`SB_CONFIG_SOC_SAMC21J18A`、`SB_CONFIG_SOC_SAMC21J17AU`、`SB_CONFIG_SOC_SAMC21J18AU`、`SB_CONFIG_SOC_SAMC21N17A`、`SB_CONFIG_SOC_SAMC21N18A`。

<a id="SB_CONFIG_SOC_SERIES_SAMD20"></a>

## 265.65 `SB_CONFIG_SOC_SERIES_SAMD20`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMD20 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAMD20E14
SB_CONFIG_SOC_SAMD20E15
SB_CONFIG_SOC_SAMD20E16
SB_CONFIG_SOC_SAMD20E17
SB_CONFIG_SOC_SAMD20E18
SB_CONFIG_SOC_SAMD20G14
SB_CONFIG_SOC_SAMD20G15
SB_CONFIG_SOC_SAMD20G16
SB_CONFIG_SOC_SAMD20G18
SB_CONFIG_SOC_SAMD20G17U
SB_CONFIG_SOC_SAMD20G18U
SB_CONFIG_SOC_SAMD20J14
SB_CONFIG_SOC_SAMD20J15
SB_CONFIG_SOC_SAMD20J16
SB_CONFIG_SOC_SAMD20J17
SB_CONFIG_SOC_SAMD20J18
```

**定义位置（Location）**：[`soc/atmel/sam0/samd20/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samd20/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`SB_CONFIG_SOC_SAMD20E14`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20E14)、[`SB_CONFIG_SOC_SAMD20E15`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20E15)、[`SB_CONFIG_SOC_SAMD20E16`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20E16)、[`SB_CONFIG_SOC_SAMD20E17`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20E17)、[`SB_CONFIG_SOC_SAMD20E18`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20E18)、[`SB_CONFIG_SOC_SAMD20G14`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20G14)、[`SB_CONFIG_SOC_SAMD20G15`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20G15)、[`SB_CONFIG_SOC_SAMD20G16`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20G16)、[`SB_CONFIG_SOC_SAMD20G18`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20G18)、[`SB_CONFIG_SOC_SAMD20G17U`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20G17U)、[`SB_CONFIG_SOC_SAMD20G18U`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20G18U)、[`SB_CONFIG_SOC_SAMD20J14`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20J14)、[`SB_CONFIG_SOC_SAMD20J15`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20J15)、[`SB_CONFIG_SOC_SAMD20J16`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20J16)、[`SB_CONFIG_SOC_SAMD20J17`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20J17)、[`SB_CONFIG_SOC_SAMD20J18`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD20J18)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`、`SB_CONFIG_SOC_SAMD20E14`、`SB_CONFIG_SOC_SAMD20E15`、`SB_CONFIG_SOC_SAMD20E16`、`SB_CONFIG_SOC_SAMD20E17`、`SB_CONFIG_SOC_SAMD20E18`、`SB_CONFIG_SOC_SAMD20G14`、`SB_CONFIG_SOC_SAMD20G15`、`SB_CONFIG_SOC_SAMD20G16`、`SB_CONFIG_SOC_SAMD20G18`、`SB_CONFIG_SOC_SAMD20G17U`、`SB_CONFIG_SOC_SAMD20G18U`、`SB_CONFIG_SOC_SAMD20J14`、`SB_CONFIG_SOC_SAMD20J15`、`SB_CONFIG_SOC_SAMD20J16`、`SB_CONFIG_SOC_SAMD20J17`、`SB_CONFIG_SOC_SAMD20J18`。

<a id="SB_CONFIG_SOC_SERIES_SAMD21"></a>

## 265.66 `SB_CONFIG_SOC_SERIES_SAMD21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMD21 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAMD21E15A
SB_CONFIG_SOC_SAMD21E16A
SB_CONFIG_SOC_SAMD21E17A
SB_CONFIG_SOC_SAMD21E18A
SB_CONFIG_SOC_SAMD21E19A
SB_CONFIG_SOC_SAMD21G15A
SB_CONFIG_SOC_SAMD21G16A
SB_CONFIG_SOC_SAMD21G17A
SB_CONFIG_SOC_SAMD21G18A
SB_CONFIG_SOC_SAMD21G17AU
SB_CONFIG_SOC_SAMD21G18AU
SB_CONFIG_SOC_SAMD21J15A
SB_CONFIG_SOC_SAMD21J16A
SB_CONFIG_SOC_SAMD21J17A
SB_CONFIG_SOC_SAMD21J18A
```

**定义位置（Location）**：[`soc/atmel/sam0/samd21/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samd21/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`SB_CONFIG_SOC_SAMD21E15A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21E15A)、[`SB_CONFIG_SOC_SAMD21E16A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21E16A)、[`SB_CONFIG_SOC_SAMD21E17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21E17A)、[`SB_CONFIG_SOC_SAMD21E18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21E18A)、[`SB_CONFIG_SOC_SAMD21E19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21E19A)、[`SB_CONFIG_SOC_SAMD21G15A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21G15A)、[`SB_CONFIG_SOC_SAMD21G16A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21G16A)、[`SB_CONFIG_SOC_SAMD21G17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21G17A)、[`SB_CONFIG_SOC_SAMD21G18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21G18A)、[`SB_CONFIG_SOC_SAMD21G17AU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21G17AU)、[`SB_CONFIG_SOC_SAMD21G18AU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21G18AU)、[`SB_CONFIG_SOC_SAMD21J15A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21J15A)、[`SB_CONFIG_SOC_SAMD21J16A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21J16A)、[`SB_CONFIG_SOC_SAMD21J17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21J17A)、[`SB_CONFIG_SOC_SAMD21J18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD21J18A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`、`SB_CONFIG_SOC_SAMD21E15A`、`SB_CONFIG_SOC_SAMD21E16A`、`SB_CONFIG_SOC_SAMD21E17A`、`SB_CONFIG_SOC_SAMD21E18A`、`SB_CONFIG_SOC_SAMD21E19A`、`SB_CONFIG_SOC_SAMD21G15A`、`SB_CONFIG_SOC_SAMD21G16A`、`SB_CONFIG_SOC_SAMD21G17A`、`SB_CONFIG_SOC_SAMD21G18A`、`SB_CONFIG_SOC_SAMD21G17AU`、`SB_CONFIG_SOC_SAMD21G18AU`、`SB_CONFIG_SOC_SAMD21J15A`、`SB_CONFIG_SOC_SAMD21J16A`、`SB_CONFIG_SOC_SAMD21J17A`、`SB_CONFIG_SOC_SAMD21J18A`。

<a id="SB_CONFIG_SOC_SERIES_SAMD51"></a>

## 265.67 `SB_CONFIG_SOC_SERIES_SAMD51`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMD51 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAMD51G18A
SB_CONFIG_SOC_SAMD51G19A
SB_CONFIG_SOC_SAMD51J18A
SB_CONFIG_SOC_SAMD51J19A
SB_CONFIG_SOC_SAMD51J20A
SB_CONFIG_SOC_SAMD51N19A
SB_CONFIG_SOC_SAMD51N20A
SB_CONFIG_SOC_SAMD51P19A
SB_CONFIG_SOC_SAMD51P20A
```

**定义位置（Location）**：[`soc/atmel/sam0/samd51/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samd51/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`SB_CONFIG_SOC_SAMD51G18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD51G18A)、[`SB_CONFIG_SOC_SAMD51G19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD51G19A)、[`SB_CONFIG_SOC_SAMD51J18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD51J18A)、[`SB_CONFIG_SOC_SAMD51J19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD51J19A)、[`SB_CONFIG_SOC_SAMD51J20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD51J20A)、[`SB_CONFIG_SOC_SAMD51N19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD51N19A)、[`SB_CONFIG_SOC_SAMD51N20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD51N20A)、[`SB_CONFIG_SOC_SAMD51P19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD51P19A)、[`SB_CONFIG_SOC_SAMD51P20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMD51P20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`、`SB_CONFIG_SOC_SAMD51G18A`、`SB_CONFIG_SOC_SAMD51G19A`、`SB_CONFIG_SOC_SAMD51J18A`、`SB_CONFIG_SOC_SAMD51J19A`、`SB_CONFIG_SOC_SAMD51J20A`、`SB_CONFIG_SOC_SAMD51N19A`、`SB_CONFIG_SOC_SAMD51N20A`、`SB_CONFIG_SOC_SAMD51P19A`、`SB_CONFIG_SOC_SAMD51P20A`。

<a id="SB_CONFIG_SOC_SERIES_SAME51"></a>

## 265.68 `SB_CONFIG_SOC_SERIES_SAME51`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAME51 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAME51J18A
SB_CONFIG_SOC_SAME51J19A
SB_CONFIG_SOC_SAME51J20A
SB_CONFIG_SOC_SAME51N19A
SB_CONFIG_SOC_SAME51N20A
```

**定义位置（Location）**：[`soc/atmel/sam0/same51/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/same51/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`SB_CONFIG_SOC_SAME51J18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME51J18A)、[`SB_CONFIG_SOC_SAME51J19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME51J19A)、[`SB_CONFIG_SOC_SAME51J20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME51J20A)、[`SB_CONFIG_SOC_SAME51N19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME51N19A)、[`SB_CONFIG_SOC_SAME51N20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME51N20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`、`SB_CONFIG_SOC_SAME51J18A`、`SB_CONFIG_SOC_SAME51J19A`、`SB_CONFIG_SOC_SAME51J20A`、`SB_CONFIG_SOC_SAME51N19A`、`SB_CONFIG_SOC_SAME51N20A`。

<a id="SB_CONFIG_SOC_SERIES_SAME53"></a>

## 265.69 `SB_CONFIG_SOC_SERIES_SAME53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAME53 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAME53J18A
SB_CONFIG_SOC_SAME53J19A
SB_CONFIG_SOC_SAME53J20A
SB_CONFIG_SOC_SAME53N19A
SB_CONFIG_SOC_SAME53N20A
```

**定义位置（Location）**：[`soc/atmel/sam0/same53/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/same53/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`SB_CONFIG_SOC_SAME53J18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME53J18A)、[`SB_CONFIG_SOC_SAME53J19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME53J19A)、[`SB_CONFIG_SOC_SAME53J20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME53J20A)、[`SB_CONFIG_SOC_SAME53N19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME53N19A)、[`SB_CONFIG_SOC_SAME53N20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME53N20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`、`SB_CONFIG_SOC_SAME53J18A`、`SB_CONFIG_SOC_SAME53J19A`、`SB_CONFIG_SOC_SAME53J20A`、`SB_CONFIG_SOC_SAME53N19A`、`SB_CONFIG_SOC_SAME53N20A`。

<a id="SB_CONFIG_SOC_SERIES_SAME54"></a>

## 265.70 `SB_CONFIG_SOC_SERIES_SAME54`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAME54 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAME54N19A
SB_CONFIG_SOC_SAME54N20A
SB_CONFIG_SOC_SAME54P19A
SB_CONFIG_SOC_SAME54P20A
```

**定义位置（Location）**：[`soc/atmel/sam0/same54/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/same54/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`SB_CONFIG_SOC_SAME54N19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME54N19A)、[`SB_CONFIG_SOC_SAME54N20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME54N20A)、[`SB_CONFIG_SOC_SAME54P19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME54P19A)、[`SB_CONFIG_SOC_SAME54P20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAME54P20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`、`SB_CONFIG_SOC_SAME54N19A`、`SB_CONFIG_SOC_SAME54N20A`、`SB_CONFIG_SOC_SAME54P19A`、`SB_CONFIG_SOC_SAME54P20A`。

<a id="SB_CONFIG_SOC_SERIES_SAML21"></a>

## 265.71 `SB_CONFIG_SOC_SERIES_SAML21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAML21 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAML21E15B
SB_CONFIG_SOC_SAML21E16B
SB_CONFIG_SOC_SAML21E17B
SB_CONFIG_SOC_SAML21E18B
SB_CONFIG_SOC_SAML21G16B
SB_CONFIG_SOC_SAML21G17B
SB_CONFIG_SOC_SAML21G18B
SB_CONFIG_SOC_SAML21J16B
SB_CONFIG_SOC_SAML21J17B
SB_CONFIG_SOC_SAML21J18B
SB_CONFIG_SOC_SAML21J17BU
SB_CONFIG_SOC_SAML21J18BU
```

**定义位置（Location）**：[`soc/atmel/sam0/saml21/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/saml21/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`SB_CONFIG_SOC_SAML21E15B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAML21E15B)、[`SB_CONFIG_SOC_SAML21E16B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAML21E16B)、[`SB_CONFIG_SOC_SAML21E17B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAML21E17B)、[`SB_CONFIG_SOC_SAML21E18B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAML21E18B)、[`SB_CONFIG_SOC_SAML21G16B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAML21G16B)、[`SB_CONFIG_SOC_SAML21G17B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAML21G17B)、[`SB_CONFIG_SOC_SAML21G18B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAML21G18B)、[`SB_CONFIG_SOC_SAML21J16B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAML21J16B)、[`SB_CONFIG_SOC_SAML21J17B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAML21J17B)、[`SB_CONFIG_SOC_SAML21J18B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAML21J18B)、[`SB_CONFIG_SOC_SAML21J17BU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAML21J17BU)、[`SB_CONFIG_SOC_SAML21J18BU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAML21J18BU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`、`SB_CONFIG_SOC_SAML21E15B`、`SB_CONFIG_SOC_SAML21E16B`、`SB_CONFIG_SOC_SAML21E17B`、`SB_CONFIG_SOC_SAML21E18B`、`SB_CONFIG_SOC_SAML21G16B`、`SB_CONFIG_SOC_SAML21G17B`、`SB_CONFIG_SOC_SAML21G18B`、`SB_CONFIG_SOC_SAML21J16B`、`SB_CONFIG_SOC_SAML21J17B`、`SB_CONFIG_SOC_SAML21J18B`、`SB_CONFIG_SOC_SAML21J17BU`、`SB_CONFIG_SOC_SAML21J18BU`。

<a id="SB_CONFIG_SOC_SERIES_SAMR21"></a>

## 265.72 `SB_CONFIG_SOC_SERIES_SAMR21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMR21 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAMR21E16A
SB_CONFIG_SOC_SAMR21E17A
SB_CONFIG_SOC_SAMR21E18A
SB_CONFIG_SOC_SAMR21E19A
SB_CONFIG_SOC_SAMR21G16A
SB_CONFIG_SOC_SAMR21G17A
SB_CONFIG_SOC_SAMR21G18A
```

**定义位置（Location）**：[`soc/atmel/sam0/samr21/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samr21/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`SB_CONFIG_SOC_SAMR21E16A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR21E16A)、[`SB_CONFIG_SOC_SAMR21E17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR21E17A)、[`SB_CONFIG_SOC_SAMR21E18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR21E18A)、[`SB_CONFIG_SOC_SAMR21E19A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR21E19A)、[`SB_CONFIG_SOC_SAMR21G16A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR21G16A)、[`SB_CONFIG_SOC_SAMR21G17A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR21G17A)、[`SB_CONFIG_SOC_SAMR21G18A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR21G18A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`、`SB_CONFIG_SOC_SAMR21E16A`、`SB_CONFIG_SOC_SAMR21E17A`、`SB_CONFIG_SOC_SAMR21E18A`、`SB_CONFIG_SOC_SAMR21E19A`、`SB_CONFIG_SOC_SAMR21G16A`、`SB_CONFIG_SOC_SAMR21G17A`、`SB_CONFIG_SOC_SAMR21G18A`。

<a id="SB_CONFIG_SOC_SERIES_SAMR34"></a>

## 265.73 `SB_CONFIG_SOC_SERIES_SAMR34`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMR34 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAMR34J16B
SB_CONFIG_SOC_SAMR34J17B
SB_CONFIG_SOC_SAMR34J18B
```

**定义位置（Location）**：[`soc/atmel/sam0/samr34/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samr34/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`SB_CONFIG_SOC_SAMR34J16B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR34J16B)、[`SB_CONFIG_SOC_SAMR34J17B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR34J17B)、[`SB_CONFIG_SOC_SAMR34J18B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR34J18B)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`、`SB_CONFIG_SOC_SAMR34J16B`、`SB_CONFIG_SOC_SAMR34J17B`、`SB_CONFIG_SOC_SAMR34J18B`。

<a id="SB_CONFIG_SOC_SERIES_SAMR35"></a>

## 265.74 `SB_CONFIG_SOC_SERIES_SAMR35`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAMR35 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SAMR35J16B
SB_CONFIG_SOC_SAMR35J17B
SB_CONFIG_SOC_SAMR35J18B
```

**定义位置（Location）**：[`soc/atmel/sam0/samr35/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam0/samr35/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`SB_CONFIG_SOC_SAMR35J16B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR35J16B)、[`SB_CONFIG_SOC_SAMR35J17B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR35J17B)、[`SB_CONFIG_SOC_SAMR35J18B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SAMR35J18B)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM0`、`SB_CONFIG_SOC_SAMR35J16B`、`SB_CONFIG_SOC_SAMR35J17B`、`SB_CONFIG_SOC_SAMR35J18B`。

<a id="SB_CONFIG_SOC_SERIES_SAMX7X"></a>

## 265.75 `SB_CONFIG_SOC_SERIES_SAMX7X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Atmel SAM E70／S70／V70／V71 ARM Cortex-M7 微控制器（Microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ATMEL_SAM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_ATMEL_SAME70
SB_CONFIG_SOC_ATMEL_SAME70_REVB
SB_CONFIG_SOC_ATMEL_SAMV71
SB_CONFIG_SOC_ATMEL_SAMV71_REVB
```

**定义位置（Location）**：[`soc/atmel/sam/samx7x/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/atmel/sam/samx7x/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ATMEL_SAM)、[`SB_CONFIG_SOC_ATMEL_SAME70`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATMEL_SAME70)、[`SB_CONFIG_SOC_ATMEL_SAME70_REVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATMEL_SAME70_REVB)、[`SB_CONFIG_SOC_ATMEL_SAMV71`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATMEL_SAMV71)、[`SB_CONFIG_SOC_ATMEL_SAMV71_REVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ATMEL_SAMV71_REVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ATMEL_SAM`、`SB_CONFIG_SOC_ATMEL_SAME70`、`SB_CONFIG_SOC_ATMEL_SAME70_REVB`、`SB_CONFIG_SOC_ATMEL_SAMV71`、`SB_CONFIG_SOC_ATMEL_SAMV71_REVB`。

<!-- kconfig-navigation -->

[上一章](P264_soc_aspeed_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P266_soc_bflb_配置项参考.md)
