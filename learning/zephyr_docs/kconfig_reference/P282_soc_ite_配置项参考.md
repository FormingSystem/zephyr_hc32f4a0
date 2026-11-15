---
id: learning.zephyr-docs.kconfig-reference.page-282
title: "`soc/ite`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第282章\_`soc/ite`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/ite` 的 38 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ILM_MAX_SIZE"></a>

## 282.1 `CONFIG_ILM_MAX_SIZE`

原库同名定义共 2 条；本项为数据库第 8282 条记录，各定义分别保留。

**提示（Prompt）**：指令本地内存大小，单位为 kB（ILM Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT51XXX && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`soc/ite/ec/it51xxx/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it51xxx/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT51XXX`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_ILM_MAX_SIZE--record-8283"></a>

## 282.2 `CONFIG_ILM_MAX_SIZE`

原库同名定义共 2 条；本项为数据库第 8283 条记录，各定义分别保留。

**提示（Prompt）**：指令本地内存大小，单位为 kB（ILM Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
CONFIG_SRAM_SIZE if CONFIG_SRAM_DEPRECATED_KCONFIG_SET
0
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:279`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L279)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SRAM_SIZE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_SIZE)、[`CONFIG_SRAM_DEPRECATED_KCONFIG_SET`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SRAM_DEPRECATED_KCONFIG_SET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT515XX_HW_CRYPTO_OFFSET"></a>

## 282.3 `CONFIG_SOC_IT515XX_HW_CRYPTO_OFFSET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由于 IT515XX 的硬件要求，SHA-256 数据必须放在指定地址范围内，默认为 `0x83E000`～`0x83EFFF`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_IT51XXX_HW_CRYPTO_ACCELERATE && CONFIG_SOC_SERIES_IT51XXX && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
0x03E000
```

**定义位置（Location）**：[`soc/ite/ec/it51xxx/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it51xxx/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 硬件加密运算（HW crypto calculation）

**配置项引用（Symbol References）**：[`CONFIG_SOC_IT51XXX_HW_CRYPTO_ACCELERATE`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT51XXX_HW_CRYPTO_ACCELERATE)、[`CONFIG_SOC_SERIES_IT51XXX`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT51XXX_CMP_RANGE_ADDR"></a>

## 282.4 `CONFIG_SOC_IT51XXX_CMP_RANGE_ADDR`

**提示（Prompt）**：比较范围地址（Comparison range address）

**说明（Help）**

指定 e-flash 与 SPI Flash 之间的比较范围地址位 `[17:10]`。当 `SOC_IT51XXX_SIGNATURE_FLAG` 的位 `[5]` 置位（`1'b1`）时，此选项必须为 `0xAA`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT51XXX && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
0xAA
```

**取值范围（Ranges）**

```text
[0x0, 0xFF]
```

**定义位置（Location）**：[`soc/ite/ec/it51xxx/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it51xxx/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT51XXX`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT51XXX_CPU_IDLE_GATING"></a>

## 282.5 `CONFIG_SOC_IT51XXX_CPU_IDLE_GATING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项决定是否允许各驱动分别控制能否进入 CPU 空闲模式（CPU idle mode）。禁用时，始终允许进入 CPU 空闲模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT51XXX && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
y if CONFIG_I2C_ITE_IT51XXX && CONFIG_I2C_TARGET
```

**被选择（Selected by）**

```text
CONFIG_I3CM_IT51XXX
CONFIG_I3CS_IT51XXX
CONFIG_SPI_ITE_IT51XXX_FIFO_MODE
```

**定义位置（Location）**：[`soc/ite/ec/it51xxx/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it51xxx/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT51XXX`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_I2C_ITE_IT51XXX`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_IT51XXX)、[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I3CM_IT51XXX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CM_IT51XXX)、[`CONFIG_I3CS_IT51XXX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_IT51XXX)、[`CONFIG_SPI_ITE_IT51XXX_FIFO_MODE`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ITE_IT51XXX_FIFO_MODE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT51XXX_HW_CRYPTO_ACCELERATE"></a>

## 282.6 `CONFIG_SOC_IT51XXX_HW_CRYPTO_ACCELERATE`

**提示（Prompt）**：硬件加密运算（HW crypto calculation）

**说明（Help）**

IT51XXX 硬件（HW）支持加密运算（crypto calculation），其运算速度快于固件（FW）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT51XXX && CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
CONFIG_CRYPTO_IT51XXX_SHA
```

**定义位置（Location）**：[`soc/ite/ec/it51xxx/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it51xxx/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT51XXX`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_CRYPTO_IT51XXX_SHA`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_IT51XXX_SHA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT51XXX_SIGNATURE_DATA_EXTENSION"></a>

## 282.7 `CONFIG_SOC_IT51XXX_SIGNATURE_DATA_EXTENSION`

**提示（Prompt）**：自定义签名扩展（Custom signature extension）

**说明（Help）**

启用附加到向量表（vector table）后的项目专用签名扩展数据。启用后，`signature_custom.S` 被纳入 SoC 向量布局。自定义签名扩展从偏移 `0x50` 开始。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT51XXX && CONFIG_SOC_FAMILY_ITE_EC
```

**定义位置（Location）**：[`soc/ite/ec/it51xxx/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it51xxx/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT51XXX`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT51XXX_SIGNATURE_FLAG"></a>

## 282.8 `CONFIG_SOC_IT51XXX_SIGNATURE_FLAG`

**提示（Prompt）**：硬件镜像签名标志（Hardware mirror signature flag）

**说明（Help）**

硬件镜像签名标志（Hardware mirror signature flag）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT51XXX && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
0xB4
```

**取值范围（Ranges）**

```text
[0x0, 0xFF]
```

**定义位置（Location）**：[`soc/ite/ec/it51xxx/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it51xxx/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT51XXX`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT51XXX_USE_ILM"></a>

## 282.9 `CONFIG_SOC_IT51XXX_USE_ILM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用后，会配置指令本地内存（Instruction Local Memory，ILM），使放在 `.__ram_code` 节中的代码从 RAM 执行。这以 4 千字节为块消耗 RAM，但 ILM 中代码的性能比直接从 Flash 执行更可预测；某些代码（例如写入内部 Flash 的代码）必须从 RAM 执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT51XXX && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_ITE_IT8XXX2
```

**定义位置（Location）**：[`soc/ite/ec/it51xxx/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it51xxx/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT51XXX`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_FLASH_ITE_IT8XXX2`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_ITE_IT8XXX2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_CPU_IDLE_GATING"></a>

## 282.10 `CONFIG_SOC_IT8XXX2_CPU_IDLE_GATING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项决定是否允许各驱动分别控制能否进入 CPU 空闲模式（CPU idle mode）。禁用时，始终允许进入 CPU 空闲模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
CONFIG_I2C_IT8XXX2_CQ_MODE
CONFIG_SPI_ITE_IT8XXX2
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_I2C_IT8XXX2_CQ_MODE`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_IT8XXX2_CQ_MODE)、[`CONFIG_SPI_ITE_IT8XXX2`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ITE_IT8XXX2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_EC_BUS_24MHZ"></a>

## 282.11 `CONFIG_SOC_IT8XXX2_EC_BUS_24MHZ`

**提示（Prompt）**：嵌入式控制器总线为 24MHz（EC bus）

**说明（Help）**

将嵌入式控制器总线（EC bus）频率提高到 24MHz，默认为 8MHz。这可使 EC 寄存器读写延迟降低 50%。注意：在 it81xx2 系列上启用此配置有限制：`ite,it8xxx2-i2c` 节点（i2c0、i2c1、i2c2）的 `clock_frequency` 将固定为 400KHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
CONFIG_SOC_IT82202AX
CONFIG_SOC_IT82302AX
CONFIG_SOC_IT82002AW
CONFIG_SOC_IT82002BW
CONFIG_SOC_IT82202BW
CONFIG_SOC_IT82302BW
CONFIG_SOC_IT82000BW
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT82202AX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82202AX)、[`CONFIG_SOC_IT82302AX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82302AX)、[`CONFIG_SOC_IT82002AW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82002AW)、[`CONFIG_SOC_IT82002BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82002BW)、[`CONFIG_SOC_IT82202BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82202BW)、[`CONFIG_SOC_IT82302BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82302BW)、[`CONFIG_SOC_IT82000BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82000BW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`、`CONFIG_SOC_IT82202AX`、`CONFIG_SOC_IT82302AX`、`CONFIG_SOC_IT82002AW`、`CONFIG_SOC_IT82002BW`、`CONFIG_SOC_IT82202BW`、`CONFIG_SOC_IT82302BW`、`CONFIG_SOC_IT82000BW`。

<a id="CONFIG_SOC_IT8XXX2_EXCEPTIONS_IN_RAM"></a>

## 282.12 `CONFIG_SOC_IT8XXX2_EXCEPTIONS_IN_RAM`

**提示（Prompt）**：将异常处理代码放入 RAM（exception handling code）

**说明（Help）**

将异常处理代码（中断服务程序入口／出口及相关代码，ISR entry/exit）放入指令本地内存（ILM），它的性能特征比直接从 Flash 执行更可靠。当指令缓存（I-cache）压力较大时，这可以显著提高性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SOC_IT8XXX2_USE_ILM
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT8XXX2_USE_ILM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_USE_ILM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_EXT_32K"></a>

## 282.13 `CONFIG_SOC_IT8XXX2_EXT_32K`

**提示（Prompt）**：使用外部 32.768 kHz 时钟源（external clock source）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 锁相环参考时钟的时钟源（Clock source for PLL reference clock）

<a id="CONFIG_SOC_IT8XXX2_FLASH_SIZE_BYTES"></a>

## 282.14 `CONFIG_SOC_IT8XXX2_FLASH_SIZE_BYTES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

可写 Flash 总大小（Total size of writable flash）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
0x0
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:271`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L271)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_GPIO_GROUP_K_L_DEFAULT_PULL_DOWN"></a>

## 282.15 `CONFIG_SOC_IT8XXX2_GPIO_GROUP_K_L_DEFAULT_PULL_DOWN`

**提示（Prompt）**：GPIO K 组和 L 组的引脚未与焊盘键合（not bonding with pad）

**说明（Help）**

在 IT81202（128 引脚封装）上，GPIO K 组和 L 组的引脚未与焊盘键合（not bonding with pad）。因此默认将这些引脚配置为内部下拉（internal pull-down），防止悬空引起漏电流。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_GPIO_H7_DEFAULT_OUTPUT_LOW"></a>

## 282.16 `CONFIG_SOC_IT8XXX2_GPIO_H7_DEFAULT_OUTPUT_LOW`

**提示（Prompt）**：GPIOH7 未与焊盘键合，且在内部悬空（left floating internally）

**说明（Help）**

在 IT81202／IT81302 上，GPIOH7 未与焊盘键合，且在内部悬空。需要为该引脚启用内部下拉（internal pull-down）以防止漏电流，但 IT81202／IT81302 不具备对其下拉的能力。只能将其设为低电平输出，因此初始化时会启用该引脚的低电平输出，以防止漏电。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_GPIO_Q_GROUP_SUPPORTED"></a>

## 282.17 `CONFIG_SOC_IT8XXX2_GPIO_Q_GROUP_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示支持 GPIO-Q 组（GPIO-Q group），并根据 SoC 变体自动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
CONFIG_SOC_IT82000BW
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT82000BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82000BW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`、`CONFIG_SOC_IT82000BW`。

<a id="CONFIG_SOC_IT8XXX2_INT_32K"></a>

## 282.18 `CONFIG_SOC_IT8XXX2_INT_32K`

**提示（Prompt）**：使用精度为 ±2.3% 的内部时钟发生器（internal clock generator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 锁相环参考时钟的时钟源（Clock source for PLL reference clock）

<a id="CONFIG_SOC_IT8XXX2_JTAG_DEBUG_INTERFACE"></a>

## 282.19 `CONFIG_SOC_IT8XXX2_JTAG_DEBUG_INTERFACE`

**提示（Prompt）**：JTAG 调试接口（debug interface）

**说明（Help）**

启用后，将以下五个引脚配置为 JTAG 调试接口（debug interface），原始引脚映射如下：

```text
- GPIOA0 -> TCK
- GPIOA1 -> TDI
- GPIOA4 -> TDO
- GPIOA5 -> TMS
- GPIOA6 -> TRST
```

支持的 I/O 电压为 3.3V。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_KERNEL_IN_RAM"></a>

## 282.20 `CONFIG_SOC_IT8XXX2_KERNEL_IN_RAM`

**提示（Prompt）**：将内核处理代码放入 RAM（kernel handling code）

**说明（Help）**

将内核处理代码（kernel handling code）放入指令本地内存（ILM），可显著提高性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**主动选择（Selects）**

```text
CONFIG_SOC_IT8XXX2_USE_ILM
CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM
CONFIG_KERNEL_NO_LTO if CONFIG_LTO
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:230`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L230)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT8XXX2_USE_ILM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_USE_ILM)、[`CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM)、[`CONFIG_KERNEL_NO_LTO`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_NO_LTO)、[`CONFIG_LTO`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_LCVCO"></a>

## 282.21 `CONFIG_SOC_IT8XXX2_LCVCO`

**提示（Prompt）**：LC 压控振荡器校准（LCVCO calibration）

**说明（Help）**

LC 压控振荡器（LCVCO）是一种高精度时钟控制器，用于校准锁相环（PLL）的频率偏移。启用此选项可使用受支持的 LCVCO 校准，提高 USB 时钟的准确度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_IT8XXX2_INT_32K && CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_IT8XXX2_INT_32K`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_INT_32K)、[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM"></a>

## 282.22 `CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

选择此项表示有某个库需要从代码节（text section）中排除。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
CONFIG_SOC_IT8XXX2_SWITCH_IN_RAM
CONFIG_SOC_IT8XXX2_SERIAL_IN_RAM
CONFIG_SOC_IT8XXX2_KERNEL_IN_RAM
CONFIG_SOC_IT8XXX2_ZEPHYR_IN_RAM
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L209)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT8XXX2_SWITCH_IN_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_SWITCH_IN_RAM)、[`CONFIG_SOC_IT8XXX2_SERIAL_IN_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_SERIAL_IN_RAM)、[`CONFIG_SOC_IT8XXX2_KERNEL_IN_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_KERNEL_IN_RAM)、[`CONFIG_SOC_IT8XXX2_ZEPHYR_IN_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_ZEPHYR_IN_RAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_PLL_FLASH_48M"></a>

## 282.23 `CONFIG_SOC_IT8XXX2_PLL_FLASH_48M`

**提示（Prompt）**：Flash 频率为 48MHz（Flash frequency）

**说明（Help）**

初始化期间，将锁相环（PLL）、CPU 和 Flash 的频率改为 48MHz。设为 `n` 使用默认设置，即 PLL 和 CPU 运行在 48MHz，Flash 频率为 16MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_RAM_CODE_NOINLINE"></a>

## 282.24 `CONFIG_SOC_IT8XXX2_RAM_CODE_NOINLINE`

**提示（Prompt）**：强制 RAM 代码函数不内联（non-inlined）

**说明（Help）**

启用后，带有 `__soc_ram_code` 标记的函数将使用 `noinline` 属性，确保编译器不对其进行内联。这保证函数体留在 RAM 代码节（RAM code section）中，而不会合并到调用者。启用链接时优化（LTO）后更容易发生内联，因此使用 LTO 时默认启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LTO && CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:245`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L245)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LTO`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LTO)、[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_REG_SET_V1"></a>

## 282.25 `CONFIG_SOC_IT8XXX2_REG_SET_V1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项由相应 SoC 的变量选择，并确定 IT81xx2 规格所用的寄存器（register）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
CONFIG_SOC_IT81302BX
CONFIG_SOC_IT81202BX
CONFIG_SOC_IT81302CX
CONFIG_SOC_IT81202CX
CONFIG_SOC_IT81302DX
CONFIG_SOC_IT81202DX
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT81302BX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT81302BX)、[`CONFIG_SOC_IT81202BX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT81202BX)、[`CONFIG_SOC_IT81302CX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT81302CX)、[`CONFIG_SOC_IT81202CX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT81202CX)、[`CONFIG_SOC_IT81302DX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT81302DX)、[`CONFIG_SOC_IT81202DX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT81202DX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`、`CONFIG_SOC_IT81302BX`、`CONFIG_SOC_IT81202BX`、`CONFIG_SOC_IT81302CX`、`CONFIG_SOC_IT81202CX`、`CONFIG_SOC_IT81302DX`、`CONFIG_SOC_IT81202DX`。

<a id="CONFIG_SOC_IT8XXX2_REG_SET_V2"></a>

## 282.26 `CONFIG_SOC_IT8XXX2_REG_SET_V2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项由相应 SoC 的变量选择，并确定 IT82xx2 规格所用的寄存器（register）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
CONFIG_SOC_IT82202AX
CONFIG_SOC_IT82302AX
CONFIG_SOC_IT82002AW
CONFIG_SOC_IT82002BW
CONFIG_SOC_IT82202BW
CONFIG_SOC_IT82302BW
CONFIG_SOC_IT82000BW
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT82202AX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82202AX)、[`CONFIG_SOC_IT82302AX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82302AX)、[`CONFIG_SOC_IT82002AW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82002AW)、[`CONFIG_SOC_IT82002BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82002BW)、[`CONFIG_SOC_IT82202BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82202BW)、[`CONFIG_SOC_IT82302BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82302BW)、[`CONFIG_SOC_IT82000BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82000BW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`、`CONFIG_SOC_IT82202AX`、`CONFIG_SOC_IT82302AX`、`CONFIG_SOC_IT82002AW`、`CONFIG_SOC_IT82002BW`、`CONFIG_SOC_IT82202BW`、`CONFIG_SOC_IT82302BW`、`CONFIG_SOC_IT82000BW`。

<a id="CONFIG_SOC_IT8XXX2_SERIAL_IN_RAM"></a>

## 282.27 `CONFIG_SOC_IT8XXX2_SERIAL_IN_RAM`

**提示（Prompt）**：将串口处理代码放入 RAM（serial handling code）

**说明（Help）**

将串口处理代码（包括 `uart_ns16550.c` 和 `uart_ite_it8xxx2.c`）放入指令本地内存（ILM），可提高性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**主动选择（Selects）**

```text
CONFIG_SOC_IT8XXX2_USE_ILM
CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT8XXX2_USE_ILM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_USE_ILM)、[`CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_SHA256_HW_ACCELERATE"></a>

## 282.28 `CONFIG_SOC_IT8XXX2_SHA256_HW_ACCELERATE`

**提示（Prompt）**：硬件 SHA256 运算（HW SHA256 calculation）

**说明（Help）**

IT8XXX2 硬件（HW）支持 SHA256 运算，速度快于固件（FW）。SHA256 消息、哈希和密钥数据共 512bytes，放在 RAM 中。若启用此配置，由于硬件限制，SHA256 数据必须放在 RAM 的前 4KB 中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
CONFIG_CRYPTO_IT8XXX2_SHA
CONFIG_CRYPTO_IT8XXX2_SHA_V2
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_CRYPTO_IT8XXX2_SHA`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_IT8XXX2_SHA)、[`CONFIG_CRYPTO_IT8XXX2_SHA_V2`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_IT8XXX2_SHA_V2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_SWITCH_IN_RAM"></a>

## 282.29 `CONFIG_SOC_IT8XXX2_SWITCH_IN_RAM`

**提示（Prompt）**：将切换处理代码放入 RAM（switch handling code）

**说明（Help）**

将上下文切换代码（context switching code）放入指令本地内存（ILM），以提高性能。译注：原文写作 content switching，此处按上下文译为上下文切换。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**主动选择（Selects）**

```text
CONFIG_SOC_IT8XXX2_USE_ILM
CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:215`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L215)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT8XXX2_USE_ILM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_USE_ILM)、[`CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_UART_TX_STRATPPING_PIN"></a>

## 282.30 `CONFIG_SOC_IT8XXX2_UART_TX_STRATPPING_PIN`

**提示（Prompt）**：添加软件启动配置引脚支持（software strapping pin）

**说明（Help）**

将嵌入式控制器 UART 发送引脚（EC UART TX）用作 Flash 恢复的软件启动配置引脚（software strapping pin）。复位期间将 UART TX 拉低时，SoC 会进入早期无限循环；此时固件尚未启用硬件看门狗，也尚未进入崩溃或反复启动状态（crash/bootloop）。这样恢复编程器（recovery programmer）便能可靠进入 DBGR 模式并恢复 EC Flash。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:284`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L284)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_USBPD_PHY_V1"></a>

## 282.31 `CONFIG_SOC_IT8XXX2_USBPD_PHY_V1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项由 SoC 变体自动选择，并设置 USB 供电物理层版本（USBPD PHY version）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
CONFIG_SOC_IT81302BX
CONFIG_SOC_IT81202BX
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT81302BX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT81302BX)、[`CONFIG_SOC_IT81202BX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT81202BX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`、`CONFIG_SOC_IT81302BX`、`CONFIG_SOC_IT81202BX`。

<a id="CONFIG_SOC_IT8XXX2_USBPD_PHY_V2"></a>

## 282.32 `CONFIG_SOC_IT8XXX2_USBPD_PHY_V2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项由 SoC 变体自动选择，并设置 USB 供电物理层版本（USBPD PHY version）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
CONFIG_SOC_IT81302CX
CONFIG_SOC_IT81202CX
CONFIG_SOC_IT81302DX
CONFIG_SOC_IT81202DX
CONFIG_SOC_IT82202AX
CONFIG_SOC_IT82302AX
CONFIG_SOC_IT82002AW
CONFIG_SOC_IT82002BW
CONFIG_SOC_IT82202BW
CONFIG_SOC_IT82302BW
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT81302CX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT81302CX)、[`CONFIG_SOC_IT81202CX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT81202CX)、[`CONFIG_SOC_IT81302DX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT81302DX)、[`CONFIG_SOC_IT81202DX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT81202DX)、[`CONFIG_SOC_IT82202AX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82202AX)、[`CONFIG_SOC_IT82302AX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82302AX)、[`CONFIG_SOC_IT82002AW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82002AW)、[`CONFIG_SOC_IT82002BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82002BW)、[`CONFIG_SOC_IT82202BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82202BW)、[`CONFIG_SOC_IT82302BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT82302BW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`、`CONFIG_SOC_IT81302CX`、`CONFIG_SOC_IT81202CX`、`CONFIG_SOC_IT81302DX`、`CONFIG_SOC_IT81202DX`、`CONFIG_SOC_IT82202AX`、`CONFIG_SOC_IT82302AX`、`CONFIG_SOC_IT82002AW`、`CONFIG_SOC_IT82002BW`、`CONFIG_SOC_IT82202BW`、`CONFIG_SOC_IT82302BW`。

<a id="CONFIG_SOC_IT8XXX2_USE_ILM"></a>

## 282.33 `CONFIG_SOC_IT8XXX2_USE_ILM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用后，会配置指令本地内存（Instruction Local Memory，ILM），使放在 `.__ram_code` 节中的代码从 RAM 执行。这以 4 千字节为块消耗 RAM，但 ILM 中代码的性能比直接从 Flash 执行更可预测；某些代码（例如写入内部 Flash 的代码）必须从 RAM 执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_IT8XXX2_EXCEPTIONS_IN_RAM
CONFIG_SOC_IT8XXX2_SWITCH_IN_RAM
CONFIG_SOC_IT8XXX2_SERIAL_IN_RAM
CONFIG_SOC_IT8XXX2_KERNEL_IN_RAM
CONFIG_SOC_IT8XXX2_ZEPHYR_IN_RAM
CONFIG_SOC_FLASH_ITE_IT8XXX2
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT8XXX2_EXCEPTIONS_IN_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_EXCEPTIONS_IN_RAM)、[`CONFIG_SOC_IT8XXX2_SWITCH_IN_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_SWITCH_IN_RAM)、[`CONFIG_SOC_IT8XXX2_SERIAL_IN_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_SERIAL_IN_RAM)、[`CONFIG_SOC_IT8XXX2_KERNEL_IN_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_KERNEL_IN_RAM)、[`CONFIG_SOC_IT8XXX2_ZEPHYR_IN_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_ZEPHYR_IN_RAM)、[`CONFIG_SOC_FLASH_ITE_IT8XXX2`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_ITE_IT8XXX2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_IT8XXX2_ZEPHYR_IN_RAM"></a>

## 282.34 `CONFIG_SOC_IT8XXX2_ZEPHYR_IN_RAM`

**提示（Prompt）**：将 Zephyr 处理代码放入 RAM（zephyr handling code）

**说明（Help）**

将 Zephyr 处理代码（zephyr handling code）放入指令本地内存（ILM），可显著提高性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IT8XXX2 && CONFIG_SOC_FAMILY_ITE_EC
```

**主动选择（Selects）**

```text
CONFIG_SOC_IT8XXX2_USE_ILM
CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig:238`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig#L238)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IT8XXX2`](P282_soc_ite_配置项参考.md#CONFIG_SOC_SERIES_IT8XXX2)、[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT8XXX2_USE_ILM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_USE_ILM)、[`CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM`](P282_soc_ite_配置项参考.md#CONFIG_SOC_IT8XXX2_LIBRARY_TO_RAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`。

<a id="CONFIG_SOC_SERIES_IT51XXX"></a>

## 282.35 `CONFIG_SOC_SERIES_IT51XXX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ITE IT51XXX 支持（support）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
CONFIG_SOC_IT51XXX
```

**定义位置（Location）**：[`soc/ite/ec/it51xxx/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it51xxx/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`、`CONFIG_SOC_IT51XXX`。

<a id="CONFIG_SOC_SERIES_IT8XXX2"></a>

## 282.36 `CONFIG_SOC_SERIES_IT8XXX2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ITE IT8XXX2 支持（support）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
CONFIG_SOC_IT8XXX2
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ITE_EC)、[`CONFIG_SOC_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ITE_EC`、`CONFIG_SOC_IT8XXX2`。

<a id="SB_CONFIG_SOC_SERIES_IT51XXX"></a>

## 282.37 `SB_CONFIG_SOC_SERIES_IT51XXX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ITE IT51XXX 支持（support）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_IT51XXX
```

**定义位置（Location）**：[`soc/ite/ec/it51xxx/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it51xxx/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ITE_EC)、[`SB_CONFIG_SOC_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_IT51XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ITE_EC`、`SB_CONFIG_SOC_IT51XXX`。

<a id="SB_CONFIG_SOC_SERIES_IT8XXX2"></a>

## 282.38 `SB_CONFIG_SOC_SERIES_IT8XXX2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ITE IT8XXX2 支持（support）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ITE_EC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_IT8XXX2
```

**定义位置（Location）**：[`soc/ite/ec/it8xxx2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/ite/ec/it8xxx2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ITE_EC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ITE_EC)、[`SB_CONFIG_SOC_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_IT8XXX2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ITE_EC`、`SB_CONFIG_SOC_IT8XXX2`。

<!-- kconfig-navigation -->

[上一章](P281_soc_intel_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P283_soc_litex_配置项参考.md)
