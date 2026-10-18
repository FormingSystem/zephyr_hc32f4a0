---
id: learning.zephyr-docs.kconfig-reference.page-285
title: "`soc/microchip`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第285章\_`soc/microchip`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `soc/microchip` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_GPIO_MCHP_PORT_U2210_3_1_0"></a>

## 285.1 `CONFIG_GPIO_MCHP_PORT_U2210_3_1_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 PORT GPIO 外设 IP，标识为 `U2210`，版本为 `3.1.0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_jh/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_jh/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`。

<a id="CONFIG_HAS_MCHP_MEC_I3C"></a>

## 285.2 `CONFIG_HAS_MCHP_MEC_I3C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由支持改进型集成电路间接口（I3C）的 SoC 选择的隐藏符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_MEC165XB
CONFIG_SOC_SERIES_MEC175X
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:277`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L277)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_SOC_SERIES_MEC165XB`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_MEC165XB)、[`CONFIG_SOC_SERIES_MEC175X`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_MEC175X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_MCHP_HEADER_VERBOSE_OUTPUT"></a>

## 285.3 `CONFIG_MCHP_HEADER_VERBOSE_OUTPUT`

**提示（Prompt）**：调试控制台输出（Debug console output）

**说明（Help）**

启用 SPI 生成脚本的打印输出，用于调试（debug）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCHP_MEC_UNSIGNED_HEADER && CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:210`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L210)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_UNSIGNED_HEADER`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_UNSIGNED_HEADER)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_16M"></a>

## 285.4 `CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_16M`

**提示（Prompt）**：SPI Flash 大小为 16M 字节（16M Bytes）

**说明（Help）**

SPI Flash 大小为 16M 字节（16M Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_1M"></a>

## 285.5 `CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_1M`

**提示（Prompt）**：SPI Flash 大小为 1M 字节（1M Bytes）

**说明（Help）**

SPI Flash 大小为 1M 字节（1M Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_256K"></a>

## 285.6 `CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_256K`

**提示（Prompt）**：SPI Flash 大小为 256K 字节（256K Bytes）

**说明（Help）**

SPI Flash 大小为 256K 字节（256K Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_2M"></a>

## 285.7 `CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_2M`

**提示（Prompt）**：SPI Flash 大小为 2M 字节（2M Bytes）

**说明（Help）**

SPI Flash 大小为 2M 字节（2M Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_4M"></a>

## 285.8 `CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_4M`

**提示（Prompt）**：SPI Flash 大小为 4M 字节（4M Bytes）

**说明（Help）**

SPI Flash 大小为 4M 字节（4M Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_512K"></a>

## 285.9 `CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_512K`

**提示（Prompt）**：SPI Flash 大小为 512K 字节（512K Bytes）

**说明（Help）**

SPI Flash 大小为 512K 字节（512K Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_8M"></a>

## 285.10 `CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_8M`

**提示（Prompt）**：SPI Flash 大小为 8M 字节（8M Bytes）

**说明（Help）**

SPI Flash 大小为 8M 字节（8M Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE"></a>

## 285.11 `CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_CHOICE`

**提示（Prompt）**：Flash 大小（Flash size）

**说明（Help）**

设置 SPI Flash 的大小（size）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCHP_MEC_UNSIGNED_HEADER && CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**默认值（Defaults）**

```text
CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_16M
```

**可选项（Choices）**

```text
CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_256K
CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_512K
CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_1M
CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_2M
CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_4M
CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_8M
CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_16M
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_UNSIGNED_HEADER`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_UNSIGNED_HEADER)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_16M`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_16M)、[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_256K`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_256K)、[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_512K`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_512K)、[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_1M`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_1M)、[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_2M`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_2M)、[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_4M`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_4M)、[`CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_8M`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_FLASH_SIZE_8M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_MCHP_MEC_HEADER_FLASH_SPI_MODE"></a>

## 285.12 `CONFIG_MCHP_MEC_HEADER_FLASH_SPI_MODE`

**提示（Prompt）**：Flash SPI 模式（Flash SPI Mode）

**说明（Help）**

这个三位值对应 QMSPI 控制器的时钟空闲状态和输入／输出数据相位。位 `[0:2]` 为 `CPOL:CPHA_MOSI:CPHA_MISO`，请参阅数据手册。默认值为 0，对应 SPI 模式 0 的信号时序。

- 将此字段设为 0，选择模式 0：`CPOL=0, CPHA_MOSI=0, CPHA_MISO=0`。
- 将此字段设为 7，选择模式 3：`CPOL=1, CPHA_MOSI=1, CPHA_MISO=1`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCHP_MEC_UNSIGNED_HEADER && CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_UNSIGNED_HEADER`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_UNSIGNED_HEADER)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_1X"></a>

## 285.13 `CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_1X`

**提示（Prompt）**：SPI Flash 驱动强度倍率为 1（drive strength multiplier）

**说明（Help）**

SPI Flash 大小为 256K 字节（256K Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → Flash 驱动强度（Flash drive strength）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_2X"></a>

## 285.14 `CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_2X`

**提示（Prompt）**：SPI Flash 驱动强度倍率为 2（drive strength multiplier）

**说明（Help）**

SPI Flash 大小为 256K 字节（256K Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → Flash 驱动强度（Flash drive strength）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_4X"></a>

## 285.15 `CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_4X`

**提示（Prompt）**：SPI Flash 驱动强度倍率为 4（drive strength multiplier）

**说明（Help）**

SPI Flash 大小为 512K 字节（512K Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → Flash 驱动强度（Flash drive strength）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_6X"></a>

## 285.16 `CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_6X`

**提示（Prompt）**：SPI Flash 驱动强度倍率为 6（drive strength multiplier）

**说明（Help）**

SPI Flash 大小为 1M 字节（1M Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → Flash 驱动强度（Flash drive strength）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE"></a>

## 285.17 `CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_CHOICE`

**提示（Prompt）**：Flash 驱动强度（Flash drive strength）

**说明（Help）**

设置 SPI Flash 的大小（size）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCHP_MEC_UNSIGNED_HEADER && CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**默认值（Defaults）**

```text
CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_1X
```

**可选项（Choices）**

```text
CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_1X
CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_2X
CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_4X
CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_6X
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_UNSIGNED_HEADER`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_UNSIGNED_HEADER)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_1X`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_1X)、[`CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_2X`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_2X)、[`CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_4X`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_4X)、[`CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_6X`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_DRVSTR_6X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_12"></a>

## 285.18 `CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_12`

**提示（Prompt）**：SPI Flash 时钟速率为 12 MHz（clock rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → SPI Flash 使用的时钟速率（Clock rate）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_16"></a>

## 285.19 `CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_16`

**提示（Prompt）**：SPI Flash 时钟速率为 16 MHz（clock rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → SPI Flash 使用的时钟速率（Clock rate）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_24"></a>

## 285.20 `CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_24`

**提示（Prompt）**：SPI Flash 时钟速率为 24 MHz（clock rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → SPI Flash 使用的时钟速率（Clock rate）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_48"></a>

## 285.21 `CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_48`

**提示（Prompt）**：SPI Flash 时钟速率为 48 MHz（clock rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → SPI Flash 使用的时钟速率（Clock rate）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE"></a>

## 285.22 `CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_CHOICE`

**提示（Prompt）**：SPI Flash 使用的时钟速率（Clock rate）

**说明（Help）**

选择将固件二进制文件从 Flash 加载到 RAM 时使用的 SPI 时钟频率（clock frequency）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCHP_MEC_UNSIGNED_HEADER && CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**默认值（Defaults）**

```text
CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_12
```

**可选项（Choices）**

```text
CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_12
CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_16
CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_24
CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_48
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_UNSIGNED_HEADER`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_UNSIGNED_HEADER)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_12`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_12)、[`CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_16`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_16)、[`CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_24`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_24)、[`CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_48`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_FREQ_MHZ_48)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE"></a>

## 285.23 `CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE`

**提示（Prompt）**：SPI Flash 使用的读取模式（Reading mode）

**说明（Help）**

设置 SPI Flash 可使用的读取模式（reading mode）。支持普通（normal）、快速（fast）、双线（dual）和四线（quad）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCHP_MEC_UNSIGNED_HEADER && CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**默认值（Defaults）**

```text
CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_FAST
```

**可选项（Choices）**

```text
CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_NORMAL
CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_FAST
CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_DUAL
CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_QUAD
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_UNSIGNED_HEADER`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_UNSIGNED_HEADER)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_FAST`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_FAST)、[`CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_NORMAL`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_NORMAL)、[`CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_DUAL`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_DUAL)、[`CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_QUAD`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_QUAD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_DUAL"></a>

## 285.24 `CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_DUAL`

**提示（Prompt）**：SPI Flash 使用双线数据读取模式（dual data reading mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → SPI Flash 使用的读取模式（Reading mode）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_FAST"></a>

## 285.25 `CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_FAST`

**提示（Prompt）**：SPI Flash 以全双工方式运行，使用快速读取模式（full-duplex, fast reading mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → SPI Flash 使用的读取模式（Reading mode）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_NORMAL"></a>

## 285.26 `CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_NORMAL`

**提示（Prompt）**：SPI Flash 以全双工方式运行，频率低于 25 MHz（full-duplex, frequency < 25 MHz）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → SPI Flash 使用的读取模式（Reading mode）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_QUAD"></a>

## 285.27 `CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_QUAD`

**提示（Prompt）**：SPI Flash 使用四线数据读取模式（quad data reading mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → SPI Flash 使用的读取模式（Reading mode）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_READ_MODE_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_CHOICE"></a>

## 285.28 `CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_CHOICE`

**提示（Prompt）**：SPI 引脚转换速率（Slew rate）

**说明（Help）**

设置 SPI 引脚的转换速率（slew rate）。默认为慢转换速率，是高级高性能总线（AHB）时钟速率的一半；快转换速率等于 AHB 时钟速率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCHP_MEC_UNSIGNED_HEADER && CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**默认值（Defaults）**

```text
CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_SLOW
```

**可选项（Choices）**

```text
CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_SLOW
CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_FAST
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_UNSIGNED_HEADER`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_UNSIGNED_HEADER)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_SLOW`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_SLOW)、[`CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_FAST`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_FAST)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_FAST"></a>

## 285.29 `CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_FAST`

**提示（Prompt）**：SPI 引脚转换速率为 AHB 频率的 1 倍（slew rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:188`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L188)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → SPI 引脚转换速率（Slew rate）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_CHOICE)。

<a id="CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_SLOW"></a>

## 285.30 `CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_SLOW`

**提示（Prompt）**：SPI 引脚转换速率为 AHB 频率的 1/2（slew rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_CHOICE>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary） → SPI 引脚转换速率（Slew rate）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_CHOICE`](P285_soc_microchip_配置项参考_1.md#CONFIG_MCHP_MEC_HEADER_SPI_SLEW_RATE_CHOICE)。

<a id="CONFIG_MCHP_MEC_UNSIGNED_HEADER"></a>

## 285.31 `CONFIG_MCHP_MEC_UNSIGNED_HEADER`

**提示（Prompt）**：创建带有 Microchip MEC 二进制头部的未签名输出文件（unsigned output binary）

**说明（Help）**

在 Microchip MEC 系列芯片上，ROM 代码通过标签（TAG）定位头部（Header），由头部指定固件镜像的位置和大小，从而将固件从 Flash 加载到 RAM。启用此项会调用 `mec_spi_gen` 工具，生成包含 TAG、Header 和固件二进制内容的 SPI 镜像。此工具不生成可由启动 ROM（Boot-ROM）认证的签名镜像。如果需要认证及其他全部 Boot-ROM 加载器功能，请使用完整的 Microchip SPI 镜像生成程序。示例请参阅 Microchip 评估板（MCHP EVB）相关内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_MEC172X && CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MEC172X`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_MEC172X)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_MPFS_HAL"></a>

## 285.32 `CONFIG_MPFS_HAL`

**提示（Prompt）**：Microchip PolarFire 片上系统硬件抽象层（SoC hardware abstraction layer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_POLARFIRE && CONFIG_SOC_FAMILY_MICROCHIP_MIV
```

**主动选择（Selects）**

```text
CONFIG_HAS_MPFS_HAL
```

**定义位置（Location）**：[`soc/microchip/miv/polarfire/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/miv/polarfire/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_POLARFIRE`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_POLARFIRE)、[`CONFIG_SOC_FAMILY_MICROCHIP_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MIV)、[`CONFIG_HAS_MPFS_HAL`](P206_modules_Kconfig.microchip_配置项参考.md#CONFIG_HAS_MPFS_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MIV`。

<a id="CONFIG_PINCTRL_MCHP_PORT_U2210_2_2_0"></a>

## 285.33 `CONFIG_PINCTRL_MCHP_PORT_U2210_2_2_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 PORT 引脚控制外设 IP（pinctrl peripheral IP）版本 2.2.0，标识为 U2210。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/microchip/sam/sam_d5x_e5x/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sam_d5x_e5x/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`。

<a id="CONFIG_PINCTRL_MCHP_PORT_U2210_3_1_0"></a>

## 285.34 `CONFIG_PINCTRL_MCHP_PORT_U2210_3_1_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 PORT 引脚控制外设 IP（pinctrl peripheral IP）版本 3.1.0，标识为 U2210。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_jh/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_jh/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`。

<a id="CONFIG_SOC_FAMILY_MICROCHIP_SAMA5"></a>

## 285.35 `CONFIG_SOC_FAMILY_MICROCHIP_SAMA5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA5 Cortex-A 微处理器（Microprocessors）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_SAMA5D2
```

**定义位置（Location）**：[`soc/microchip/sam/sama5/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama5/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMA5D2`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_SAMA5D2)。

<a id="CONFIG_SOC_FAMILY_MICROCHIP_SAMA7"></a>

## 285.36 `CONFIG_SOC_FAMILY_MICROCHIP_SAMA7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA7 Cortex-A 微处理器（Microprocessors）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_SAMA7D6
CONFIG_SOC_SERIES_SAMA7G5
```

**定义位置（Location）**：[`soc/microchip/sam/sama7/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama7/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMA7D6`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_SAMA7D6)、[`CONFIG_SOC_SERIES_SAMA7G5`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_SAMA7G5)。

<a id="CONFIG_SOC_M2S010"></a>

## 285.37 `CONFIG_SOC_M2S010`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip SmartFusion2 M2S010 片上系统（SoC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_SMARTFUSION2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_M2S_HELLO_FPGA_KIT
CONFIG_BOARD_M2S010_MKR_KIT
```

**定义位置（Location）**：[`soc/microchip/smartfusion2/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/smartfusion2/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SMARTFUSION2`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_SMARTFUSION2)、[`CONFIG_BOARD_M2S_HELLO_FPGA_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M2S_HELLO_FPGA_KIT)、[`CONFIG_BOARD_M2S010_MKR_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M2S010_MKR_KIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_M2S_HELLO_FPGA_KIT`、`CONFIG_BOARD_M2S010_MKR_KIT`。

<a id="CONFIG_SOC_MEC1501_DEBUG_AND_ETM_TRACING"></a>

## 285.38 `CONFIG_SOC_MEC1501_DEBUG_AND_ETM_TRACING`

**提示（Prompt）**：通过串行线调试提供调试支持（Serial Wire Debug，SWD）

**说明（Help）**

JTAG 端口处于串行线调试（SWD）模式，并使用串行线查看器（SWV）作为跟踪方式。UART2 可用，但 ADC00～03 不可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/mec15xx/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec15xx/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC1501 调试接口跟踪配置（debug interface trace configuration）

<a id="CONFIG_SOC_MEC1501_DEBUG_AND_SWV_TRACING"></a>

## 285.39 `CONFIG_SOC_MEC1501_DEBUG_AND_SWV_TRACING`

**提示（Prompt）**：通过串行线调试和查看器提供调试支持（Serial Wire Debug and Viewer）

**说明（Help）**

JTAG 端口处于串行线调试（SWD）模式，并使用串行线查看器（SWV）作为跟踪方式。UART2 不可用，ADC00～03 可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/mec15xx/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec15xx/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC1501 调试接口跟踪配置（debug interface trace configuration）

<a id="CONFIG_SOC_MEC1501_DEBUG_AND_TRACING"></a>

## 285.40 `CONFIG_SOC_MEC1501_DEBUG_AND_TRACING`

**提示（Prompt）**：通过启用跟踪的串行线调试提供调试支持（Serial Wire Debug with tracing）

**说明（Help）**

启用 JTAG 端口的串行线调试（SWD）模式。ADC00～03 是否可用，请参阅跟踪选项（tracing options）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/mec15xx/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec15xx/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC1501 调试接口通用配置（debug interface general configuration）

<a id="CONFIG_SOC_MEC1501_DEBUG_DISABLED"></a>

## 285.41 `CONFIG_SOC_MEC1501_DEBUG_DISABLED`

**提示（Prompt）**：禁用调试支持（Disable debug support）

**说明（Help）**

禁用调试端口（debug port），无法启用 JTAG／SWD。忽略 `JTAG_RST#` 引脚。其他所有 JTAG 引脚均可用作 GPIO 或其他非 JTAG 复用功能（alternate functions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/mec15xx/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec15xx/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC1501 调试接口通用配置（debug interface general configuration）

<a id="CONFIG_SOC_MEC1501_DEBUG_WITHOUT_TRACING"></a>

## 285.42 `CONFIG_SOC_MEC1501_DEBUG_WITHOUT_TRACING`

**提示（Prompt）**：通过串行线调试提供调试支持（Serial Wire Debug，SWD）

**说明（Help）**

JTAG 端口处于串行线调试（SWD）模式。UART2 和 ADC00～03 可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/mec15xx/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec15xx/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC1501 调试接口通用配置（debug interface general configuration）

<a id="CONFIG_SOC_MEC1501_PROC_CLK_DIV"></a>

## 285.43 `CONFIG_SOC_MEC1501_PROC_CLK_DIV`

**提示（Prompt）**：处理器时钟分频值（PROC_CLK_DIV）

**说明（Help）**

此分频值定义处理器时钟（HCLK）与主时钟（MCK）之间的比值：`HCLK = MCK / PROC_CLK_DIV`。允许的分频值为 1、3、4、16、48。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_MEC15XX && CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 48]
```

**定义位置（Location）**：[`soc/microchip/mec/mec15xx/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec15xx/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MEC15XX`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_MEC15XX)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_SOC_MEC1501_VCI_PINS_AS_GPIOS"></a>

## 285.44 `CONFIG_SOC_MEC1501_VCI_PINS_AS_GPIOS`

**提示（Prompt）**：将 VCI 模块引脚用作 GPIO（Use VCI block pins as GPIOS）

**说明（Help）**

默认情况下，这些引脚不作为 GPIO，而由硬件控制。如果开发板设计不需要 VCI 引脚模块的硬件逻辑，请设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_MEC15XX && CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/microchip/mec/mec15xx/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec15xx/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MEC15XX`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_MEC15XX)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_SOC_MEC1501_VTR3_1_8V"></a>

## 285.45 `CONFIG_SOC_MEC1501_VTR3_1_8V`

**提示（Prompt）**：VTR3 电源轨接至 1.8V（power rail）

**说明（Help）**

如果更改了开发板上的 VTR3 电源选择跳线（power source jumper），请设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_MEC15XX && CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**定义位置（Location）**：[`soc/microchip/mec/mec15xx/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec15xx/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MEC15XX`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_MEC15XX)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_SOC_MEC172X_DEBUG_AND_ETM_TRACING"></a>

## 285.46 `CONFIG_SOC_MEC172X_DEBUG_AND_ETM_TRACING`

**提示（Prompt）**：通过串行线调试提供调试支持（Serial Wire Debug，SWD）

**说明（Help）**

JTAG 端口处于串行线调试（SWD）模式，并使用嵌入式跟踪宏单元（ETM）作为跟踪方式。I2C09 可用，但 ADC00～03 不可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/mec172x/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec172x/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC172X 调试接口跟踪配置（debug interface trace configuration）

<a id="CONFIG_SOC_MEC172X_DEBUG_AND_SWV_TRACING"></a>

## 285.47 `CONFIG_SOC_MEC172X_DEBUG_AND_SWV_TRACING`

**提示（Prompt）**：通过串行线调试和查看器提供调试支持（Serial Wire Debug and Viewer）

**说明（Help）**

JTAG 端口处于串行线调试（SWD）模式，并使用串行线查看器（SWV）作为跟踪方式。I2C09 不可用，ADC00～03 可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/mec172x/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec172x/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC172X 调试接口跟踪配置（debug interface trace configuration）

<a id="CONFIG_SOC_MEC172X_DEBUG_AND_TRACING"></a>

## 285.48 `CONFIG_SOC_MEC172X_DEBUG_AND_TRACING`

**提示（Prompt）**：通过启用跟踪的串行线调试提供调试支持（Serial Wire Debug with tracing）

**说明（Help）**

启用 JTAG 端口的串行线调试（SWD）模式。ADC00～03 是否可用，请参阅跟踪选项（tracing options）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/mec172x/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec172x/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC172x 调试接口通用配置（debug interface general configuration）

<a id="CONFIG_SOC_MEC172X_DEBUG_DISABLED"></a>

## 285.49 `CONFIG_SOC_MEC172X_DEBUG_DISABLED`

**提示（Prompt）**：禁用调试支持（Disable debug support）

**说明（Help）**

禁用调试端口（debug port），无法启用 JTAG／SWD。忽略 `JTAG_RST#` 引脚。其他所有 JTAG 引脚均可用作 GPIO 或其他非 JTAG 复用功能（alternate functions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/mec172x/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec172x/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC172x 调试接口通用配置（debug interface general configuration）

<a id="CONFIG_SOC_MEC172X_DEBUG_WITHOUT_TRACING"></a>

## 285.50 `CONFIG_SOC_MEC172X_DEBUG_WITHOUT_TRACING`

**提示（Prompt）**：通过串行线调试提供调试支持（Serial Wire Debug，SWD）

**说明（Help）**

JTAG 端口处于串行线调试（SWD）模式。I2C09 和 ADC00～03 可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/mec172x/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec172x/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC172x 调试接口通用配置（debug interface general configuration）

<a id="CONFIG_SOC_MEC_DEBUG_AND_ETM_TRACING"></a>

## 285.51 `CONFIG_SOC_MEC_DEBUG_AND_ETM_TRACING`

**提示（Prompt）**：通过串行线调试提供调试支持（Serial Wire Debug，SWD）

**说明（Help）**

JTAG 端口处于串行线调试（SWD）模式，并使用嵌入式跟踪宏单元（ETM）作为跟踪方式。ETM 会重新分配 5 个引脚，用于时钟和 4 位数据总线。与 ETM 共享的功能请查阅数据手册。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L251)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC 调试接口跟踪配置（debug interface trace configuration）

<a id="CONFIG_SOC_MEC_DEBUG_AND_SWV_TRACING"></a>

## 285.52 `CONFIG_SOC_MEC_DEBUG_AND_SWV_TRACING`

**提示（Prompt）**：通过串行线调试和查看器提供调试支持（Serial Wire Debug and Viewer）

**说明（Help）**

JTAG 端口处于串行线调试（SWD）模式，并使用串行线查看器（SWV）作为跟踪方式。与 SWD、SWV 引脚共享的功能请查阅数据手册。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:258`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L258)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC 调试接口跟踪配置（debug interface trace configuration）

<a id="CONFIG_SOC_MEC_DEBUG_AND_TRACING"></a>

## 285.53 `CONFIG_SOC_MEC_DEBUG_AND_TRACING`

**提示（Prompt）**：通过启用跟踪的串行线调试提供调试支持（Serial Wire Debug with tracing）

**说明（Help）**

启用 JTAG 端口的串行线调试（SWD）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:238`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L238)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC 调试接口通用配置（debug interface general configuration）

<a id="CONFIG_SOC_MEC_DEBUG_DISABLED"></a>

## 285.54 `CONFIG_SOC_MEC_DEBUG_DISABLED`

**提示（Prompt）**：禁用调试支持（Disable debug support）

**说明（Help）**

禁用调试端口（debug port），无法启用 JTAG／SWD。忽略 `JTAG_RST#` 引脚。其他所有 JTAG 引脚均可用作 GPIO 或其他非 JTAG 复用功能（alternate functions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:226`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L226)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC 调试接口通用配置（debug interface general configuration）

<a id="CONFIG_SOC_MEC_DEBUG_WITHOUT_TRACING"></a>

## 285.55 `CONFIG_SOC_MEC_DEBUG_WITHOUT_TRACING`

**提示（Prompt）**：通过串行线调试提供调试支持（Serial Wire Debug，SWD）

**说明（Help）**

JTAG 端口处于串行线调试（SWD）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L233)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MEC 调试接口通用配置（debug interface general configuration）

<a id="CONFIG_SOC_MEC_PROC_CLK_DIV"></a>

## 285.56 `CONFIG_SOC_MEC_PROC_CLK_DIV`

**提示（Prompt）**：处理器时钟分频值（PROC_CLK_DIV）

**说明（Help）**

此分频值定义处理器时钟（HCLK）与 96 MHz 主时钟（MCK）之间的比值：`HCLK = MCK / PROC_CLK_DIV`。允许的分频值为 1、3、4、16、48。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 48]
```

**定义位置（Location）**：[`soc/microchip/mec/Kconfig:266`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/Kconfig#L266)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<a id="CONFIG_SOC_MIV"></a>

## 285.57 `CONFIG_SOC_MIV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip Mi-V 系统实现（system implementation）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_MIV
```

**被选择（Selected by）**

```text
CONFIG_BOARD_M2GL025_MIV
CONFIG_BOARD_SCOBC_V1
```

**定义位置（Location）**：[`soc/microchip/miv/miv/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/miv/miv/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MIV`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_MIV)、[`CONFIG_BOARD_M2GL025_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M2GL025_MIV)、[`CONFIG_BOARD_SCOBC_V1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_SCOBC_V1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_M2GL025_MIV`、`CONFIG_BOARD_SCOBC_V1`。

<a id="CONFIG_SOC_POLARFIRE"></a>

## 285.58 `CONFIG_SOC_POLARFIRE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip MPFS 系统实现（system implementation）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_POLARFIRE
```

**被选择（Selected by）**

```text
CONFIG_SOC_POLARFIRE_U54
CONFIG_SOC_POLARFIRE_E51
```

**定义位置（Location）**：[`soc/microchip/miv/polarfire/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/miv/polarfire/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_POLARFIRE`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_POLARFIRE)、[`CONFIG_SOC_POLARFIRE_U54`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_POLARFIRE_U54)、[`CONFIG_SOC_POLARFIRE_E51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_POLARFIRE_E51)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_POLARFIRE_U54`、`CONFIG_SOC_POLARFIRE_E51`。

<a id="CONFIG_SOC_SERIES_ATSAMD51"></a>

## 285.59 `CONFIG_SOC_SERIES_ATSAMD51`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMD51 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
```

**被选择（Selected by）**

```text
CONFIG_SOC_ATSAMD51G18A
CONFIG_SOC_ATSAMD51G19A
CONFIG_SOC_ATSAMD51J18A
CONFIG_SOC_ATSAMD51J19A
CONFIG_SOC_ATSAMD51J20A
CONFIG_SOC_ATSAMD51N19A
CONFIG_SOC_ATSAMD51N20A
CONFIG_SOC_ATSAMD51P19A
CONFIG_SOC_ATSAMD51P20A
```

**定义位置（Location）**：[`soc/microchip/sam/sam_d5x_e5x/atsamd51/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sam_d5x_e5x/atsamd51/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_SOC_ATSAMD51G18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAMD51G18A)、[`CONFIG_SOC_ATSAMD51G19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAMD51G19A)、[`CONFIG_SOC_ATSAMD51J18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAMD51J18A)、[`CONFIG_SOC_ATSAMD51J19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAMD51J19A)、[`CONFIG_SOC_ATSAMD51J20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAMD51J20A)、[`CONFIG_SOC_ATSAMD51N19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAMD51N19A)、[`CONFIG_SOC_ATSAMD51N20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAMD51N20A)、[`CONFIG_SOC_ATSAMD51P19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAMD51P19A)、[`CONFIG_SOC_ATSAMD51P20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAMD51P20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`CONFIG_SOC_ATSAMD51G18A`、`CONFIG_SOC_ATSAMD51G19A`、`CONFIG_SOC_ATSAMD51J18A`、`CONFIG_SOC_ATSAMD51J19A`、`CONFIG_SOC_ATSAMD51J20A`、`CONFIG_SOC_ATSAMD51N19A`、`CONFIG_SOC_ATSAMD51N20A`、`CONFIG_SOC_ATSAMD51P19A`、`CONFIG_SOC_ATSAMD51P20A`。

<a id="CONFIG_SOC_SERIES_ATSAME51"></a>

## 285.60 `CONFIG_SOC_SERIES_ATSAME51`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAME51 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
```

**被选择（Selected by）**

```text
CONFIG_SOC_ATSAME51G18A
CONFIG_SOC_ATSAME51G19A
CONFIG_SOC_ATSAME51J18A
CONFIG_SOC_ATSAME51J19A
CONFIG_SOC_ATSAME51J20A
CONFIG_SOC_ATSAME51N19A
CONFIG_SOC_ATSAME51N20A
```

**定义位置（Location）**：[`soc/microchip/sam/sam_d5x_e5x/atsame51/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sam_d5x_e5x/atsame51/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_SOC_ATSAME51G18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME51G18A)、[`CONFIG_SOC_ATSAME51G19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME51G19A)、[`CONFIG_SOC_ATSAME51J18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME51J18A)、[`CONFIG_SOC_ATSAME51J19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME51J19A)、[`CONFIG_SOC_ATSAME51J20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME51J20A)、[`CONFIG_SOC_ATSAME51N19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME51N19A)、[`CONFIG_SOC_ATSAME51N20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME51N20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`CONFIG_SOC_ATSAME51G18A`、`CONFIG_SOC_ATSAME51G19A`、`CONFIG_SOC_ATSAME51J18A`、`CONFIG_SOC_ATSAME51J19A`、`CONFIG_SOC_ATSAME51J20A`、`CONFIG_SOC_ATSAME51N19A`、`CONFIG_SOC_ATSAME51N20A`。

<a id="CONFIG_SOC_SERIES_ATSAME53"></a>

## 285.61 `CONFIG_SOC_SERIES_ATSAME53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAME53 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
```

**被选择（Selected by）**

```text
CONFIG_SOC_ATSAME53J18A
CONFIG_SOC_ATSAME53J19A
CONFIG_SOC_ATSAME53J20A
CONFIG_SOC_ATSAME53N19A
CONFIG_SOC_ATSAME53N20A
```

**定义位置（Location）**：[`soc/microchip/sam/sam_d5x_e5x/atsame53/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sam_d5x_e5x/atsame53/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_SOC_ATSAME53J18A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME53J18A)、[`CONFIG_SOC_ATSAME53J19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME53J19A)、[`CONFIG_SOC_ATSAME53J20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME53J20A)、[`CONFIG_SOC_ATSAME53N19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME53N19A)、[`CONFIG_SOC_ATSAME53N20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME53N20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`CONFIG_SOC_ATSAME53J18A`、`CONFIG_SOC_ATSAME53J19A`、`CONFIG_SOC_ATSAME53J20A`、`CONFIG_SOC_ATSAME53N19A`、`CONFIG_SOC_ATSAME53N20A`。

<a id="CONFIG_SOC_SERIES_ATSAME54"></a>

## 285.62 `CONFIG_SOC_SERIES_ATSAME54`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAME54 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
```

**被选择（Selected by）**

```text
CONFIG_SOC_ATSAME54N19A
CONFIG_SOC_ATSAME54N20A
CONFIG_SOC_ATSAME54P19A
CONFIG_SOC_ATSAME54P20A
```

**定义位置（Location）**：[`soc/microchip/sam/sam_d5x_e5x/atsame54/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sam_d5x_e5x/atsame54/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_SOC_ATSAME54N19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME54N19A)、[`CONFIG_SOC_ATSAME54N20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME54N20A)、[`CONFIG_SOC_ATSAME54P19A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME54P19A)、[`CONFIG_SOC_ATSAME54P20A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ATSAME54P20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`CONFIG_SOC_ATSAME54N19A`、`CONFIG_SOC_ATSAME54N20A`、`CONFIG_SOC_ATSAME54P19A`、`CONFIG_SOC_ATSAME54P20A`。

<a id="CONFIG_SOC_SERIES_MEC15XX"></a>

## 285.63 `CONFIG_SOC_SERIES_MEC15XX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip MEC Cortex-M4 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**被选择（Selected by）**

```text
CONFIG_SOC_MEC1501_HSZ
```

**定义位置（Location）**：[`soc/microchip/mec/mec15xx/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec15xx/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_SOC_MEC1501_HSZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MEC1501_HSZ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`、`CONFIG_SOC_MEC1501_HSZ`。

<a id="CONFIG_SOC_SERIES_MEC165XB"></a>

## 285.64 `CONFIG_SOC_SERIES_MEC165XB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip MEC Cortex-M4 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**被选择（Selected by）**

```text
CONFIG_SOC_MEC1653B_NSZ
```

**定义位置（Location）**：[`soc/microchip/mec/mec165xb/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec165xb/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_SOC_MEC1653B_NSZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MEC1653B_NSZ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`、`CONFIG_SOC_MEC1653B_NSZ`。

<a id="CONFIG_SOC_SERIES_MEC172X"></a>

## 285.65 `CONFIG_SOC_SERIES_MEC172X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip MEC Cortex-M4F 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**被选择（Selected by）**

```text
CONFIG_SOC_MEC172X_NSZ
CONFIG_SOC_MEC172X_NLJ
```

**定义位置（Location）**：[`soc/microchip/mec/mec172x/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec172x/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_SOC_MEC172X_NSZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MEC172X_NSZ)、[`CONFIG_SOC_MEC172X_NLJ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MEC172X_NLJ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`、`CONFIG_SOC_MEC172X_NSZ`、`CONFIG_SOC_MEC172X_NLJ`。

<a id="CONFIG_SOC_SERIES_MEC174X"></a>

## 285.66 `CONFIG_SOC_SERIES_MEC174X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip MEC Cortex-M4F 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**被选择（Selected by）**

```text
CONFIG_SOC_MEC1743_QLJ
CONFIG_SOC_MEC1743_QSZ
```

**定义位置（Location）**：[`soc/microchip/mec/mec174x/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec174x/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_SOC_MEC1743_QLJ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MEC1743_QLJ)、[`CONFIG_SOC_MEC1743_QSZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MEC1743_QSZ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`、`CONFIG_SOC_MEC1743_QLJ`、`CONFIG_SOC_MEC1743_QSZ`。

<a id="CONFIG_SOC_SERIES_MEC175X"></a>

## 285.67 `CONFIG_SOC_SERIES_MEC175X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip MEC Cortex-M4F 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_MEC
```

**被选择（Selected by）**

```text
CONFIG_SOC_MEC1753_QLJ
CONFIG_SOC_MEC1753_QSZ
```

**定义位置（Location）**：[`soc/microchip/mec/mec175x/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/mec/mec175x/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_SOC_MEC1753_QLJ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MEC1753_QLJ)、[`CONFIG_SOC_MEC1753_QSZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MEC1753_QSZ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`、`CONFIG_SOC_MEC1753_QLJ`、`CONFIG_SOC_MEC1753_QSZ`。

<a id="CONFIG_SOC_SERIES_MIV"></a>

## 285.68 `CONFIG_SOC_SERIES_MIV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip Mi-V 实现（implementation）#。译注：原始提示末尾带有 `#` 字符。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_MIV
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIV
```

**定义位置（Location）**：[`soc/microchip/miv/miv/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/miv/miv/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MIV)、[`CONFIG_SOC_MIV`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_MIV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MIV`。

<a id="CONFIG_SOC_SERIES_PIC32CK_GC00"></a>

## 285.69 `CONFIG_SOC_SERIES_PIC32CK_GC00`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CK GC00 Cortex-M33 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CK0512GC00064
CONFIG_SOC_PIC32CK0512GC00100
CONFIG_SOC_PIC32CK1012GC00048
CONFIG_SOC_PIC32CK1012GC00064
CONFIG_SOC_PIC32CK1012GC00100
CONFIG_SOC_PIC32CK1025GC00064
CONFIG_SOC_PIC32CK1025GC00100
CONFIG_SOC_PIC32CK2051GC00064
CONFIG_SOC_PIC32CK2051GC00100
CONFIG_SOC_PIC32CK2051GC00144
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_gc00/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_gc00/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_PIC32CK0512GC00064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK0512GC00064)、[`CONFIG_SOC_PIC32CK0512GC00100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK0512GC00100)、[`CONFIG_SOC_PIC32CK1012GC00048`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1012GC00048)、[`CONFIG_SOC_PIC32CK1012GC00064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1012GC00064)、[`CONFIG_SOC_PIC32CK1012GC00100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1012GC00100)、[`CONFIG_SOC_PIC32CK1025GC00064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1025GC00064)、[`CONFIG_SOC_PIC32CK1025GC00100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1025GC00100)、[`CONFIG_SOC_PIC32CK2051GC00064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK2051GC00064)、[`CONFIG_SOC_PIC32CK2051GC00100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK2051GC00100)、[`CONFIG_SOC_PIC32CK2051GC00144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK2051GC00144)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_PIC32CK0512GC00064`、`CONFIG_SOC_PIC32CK0512GC00100`、`CONFIG_SOC_PIC32CK1012GC00048`、`CONFIG_SOC_PIC32CK1012GC00064`、`CONFIG_SOC_PIC32CK1012GC00100`、`CONFIG_SOC_PIC32CK1025GC00064`、`CONFIG_SOC_PIC32CK1025GC00100`、`CONFIG_SOC_PIC32CK2051GC00064`、`CONFIG_SOC_PIC32CK2051GC00100`、`CONFIG_SOC_PIC32CK2051GC00144`。

<a id="CONFIG_SOC_SERIES_PIC32CK_GC01"></a>

## 285.70 `CONFIG_SOC_SERIES_PIC32CK_GC01`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CK GC01 Cortex-M33 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CK0512GC01064
CONFIG_SOC_PIC32CK0512GC01100
CONFIG_SOC_PIC32CK1012GC01048
CONFIG_SOC_PIC32CK1012GC01064
CONFIG_SOC_PIC32CK1012GC01100
CONFIG_SOC_PIC32CK1025GC01064
CONFIG_SOC_PIC32CK1025GC01100
CONFIG_SOC_PIC32CK2051GC01064
CONFIG_SOC_PIC32CK2051GC01100
CONFIG_SOC_PIC32CK2051GC01144
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_gc01/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_gc01/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_PIC32CK0512GC01064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK0512GC01064)、[`CONFIG_SOC_PIC32CK0512GC01100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK0512GC01100)、[`CONFIG_SOC_PIC32CK1012GC01048`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1012GC01048)、[`CONFIG_SOC_PIC32CK1012GC01064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1012GC01064)、[`CONFIG_SOC_PIC32CK1012GC01100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1012GC01100)、[`CONFIG_SOC_PIC32CK1025GC01064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1025GC01064)、[`CONFIG_SOC_PIC32CK1025GC01100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1025GC01100)、[`CONFIG_SOC_PIC32CK2051GC01064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK2051GC01064)、[`CONFIG_SOC_PIC32CK2051GC01100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK2051GC01100)、[`CONFIG_SOC_PIC32CK2051GC01144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK2051GC01144)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_PIC32CK0512GC01064`、`CONFIG_SOC_PIC32CK0512GC01100`、`CONFIG_SOC_PIC32CK1012GC01048`、`CONFIG_SOC_PIC32CK1012GC01064`、`CONFIG_SOC_PIC32CK1012GC01100`、`CONFIG_SOC_PIC32CK1025GC01064`、`CONFIG_SOC_PIC32CK1025GC01100`、`CONFIG_SOC_PIC32CK2051GC01064`、`CONFIG_SOC_PIC32CK2051GC01100`、`CONFIG_SOC_PIC32CK2051GC01144`。

<a id="CONFIG_SOC_SERIES_PIC32CK_SG00"></a>

## 285.71 `CONFIG_SOC_SERIES_PIC32CK_SG00`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CK SG00 Cortex-M33 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CK0512SG00064
CONFIG_SOC_PIC32CK0512SG00100
CONFIG_SOC_PIC32CK1012SG00048
CONFIG_SOC_PIC32CK1012SG00064
CONFIG_SOC_PIC32CK1012SG00100
CONFIG_SOC_PIC32CK1025SG00064
CONFIG_SOC_PIC32CK1025SG00100
CONFIG_SOC_PIC32CK1025SG00144
CONFIG_SOC_PIC32CK2051SG00064
CONFIG_SOC_PIC32CK2051SG00100
CONFIG_SOC_PIC32CK2051SG00144
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_sg00/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_sg00/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_PIC32CK0512SG00064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK0512SG00064)、[`CONFIG_SOC_PIC32CK0512SG00100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK0512SG00100)、[`CONFIG_SOC_PIC32CK1012SG00048`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1012SG00048)、[`CONFIG_SOC_PIC32CK1012SG00064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1012SG00064)、[`CONFIG_SOC_PIC32CK1012SG00100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1012SG00100)、[`CONFIG_SOC_PIC32CK1025SG00064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1025SG00064)、[`CONFIG_SOC_PIC32CK1025SG00100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1025SG00100)、[`CONFIG_SOC_PIC32CK1025SG00144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1025SG00144)、[`CONFIG_SOC_PIC32CK2051SG00064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK2051SG00064)、[`CONFIG_SOC_PIC32CK2051SG00100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK2051SG00100)、[`CONFIG_SOC_PIC32CK2051SG00144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK2051SG00144)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_PIC32CK0512SG00064`、`CONFIG_SOC_PIC32CK0512SG00100`、`CONFIG_SOC_PIC32CK1012SG00048`、`CONFIG_SOC_PIC32CK1012SG00064`、`CONFIG_SOC_PIC32CK1012SG00100`、`CONFIG_SOC_PIC32CK1025SG00064`、`CONFIG_SOC_PIC32CK1025SG00100`、`CONFIG_SOC_PIC32CK1025SG00144`、`CONFIG_SOC_PIC32CK2051SG00064`、`CONFIG_SOC_PIC32CK2051SG00100`、`CONFIG_SOC_PIC32CK2051SG00144`。

<a id="CONFIG_SOC_SERIES_PIC32CK_SG01"></a>

## 285.72 `CONFIG_SOC_SERIES_PIC32CK_SG01`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CK SG01 Cortex-M33 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CK0512SG01064
CONFIG_SOC_PIC32CK0512SG01100
CONFIG_SOC_PIC32CK1012SG01048
CONFIG_SOC_PIC32CK1012SG01064
CONFIG_SOC_PIC32CK1012SG01100
CONFIG_SOC_PIC32CK1025SG01064
CONFIG_SOC_PIC32CK1025SG01100
CONFIG_SOC_PIC32CK1025SG01144
CONFIG_SOC_PIC32CK2051SG01064
CONFIG_SOC_PIC32CK2051SG01100
CONFIG_SOC_PIC32CK2051SG01144
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_sg01/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32ck_sg_gc/pic32ck_sg01/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_PIC32CK0512SG01064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK0512SG01064)、[`CONFIG_SOC_PIC32CK0512SG01100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK0512SG01100)、[`CONFIG_SOC_PIC32CK1012SG01048`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1012SG01048)、[`CONFIG_SOC_PIC32CK1012SG01064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1012SG01064)、[`CONFIG_SOC_PIC32CK1012SG01100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1012SG01100)、[`CONFIG_SOC_PIC32CK1025SG01064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1025SG01064)、[`CONFIG_SOC_PIC32CK1025SG01100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1025SG01100)、[`CONFIG_SOC_PIC32CK1025SG01144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK1025SG01144)、[`CONFIG_SOC_PIC32CK2051SG01064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK2051SG01064)、[`CONFIG_SOC_PIC32CK2051SG01100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK2051SG01100)、[`CONFIG_SOC_PIC32CK2051SG01144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CK2051SG01144)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_PIC32CK0512SG01064`、`CONFIG_SOC_PIC32CK0512SG01100`、`CONFIG_SOC_PIC32CK1012SG01048`、`CONFIG_SOC_PIC32CK1012SG01064`、`CONFIG_SOC_PIC32CK1012SG01100`、`CONFIG_SOC_PIC32CK1025SG01064`、`CONFIG_SOC_PIC32CK1025SG01100`、`CONFIG_SOC_PIC32CK1025SG01144`、`CONFIG_SOC_PIC32CK2051SG01064`、`CONFIG_SOC_PIC32CK2051SG01100`、`CONFIG_SOC_PIC32CK2051SG01144`。

<a id="CONFIG_SOC_SERIES_PIC32CM_GC00"></a>

## 285.73 `CONFIG_SOC_SERIES_PIC32CM_GC00`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM GC00 Cortex-M23 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CM5112GC00048
CONFIG_SOC_PIC32CM5112GC00064
CONFIG_SOC_PIC32CM5112GC00100
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_sg_gc/pic32cm_gc00/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_sg_gc/pic32cm_gc00/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC)、[`CONFIG_SOC_PIC32CM5112GC00048`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5112GC00048)、[`CONFIG_SOC_PIC32CM5112GC00064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5112GC00064)、[`CONFIG_SOC_PIC32CM5112GC00100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5112GC00100)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`、`CONFIG_SOC_PIC32CM5112GC00048`、`CONFIG_SOC_PIC32CM5112GC00064`、`CONFIG_SOC_PIC32CM5112GC00100`。

<a id="CONFIG_SOC_SERIES_PIC32CM_JH00"></a>

## 285.74 `CONFIG_SOC_SERIES_PIC32CM_JH00`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM JH00 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CM2532JH00032
CONFIG_SOC_PIC32CM5164JH00032
CONFIG_SOC_PIC32CM2532JH00048
CONFIG_SOC_PIC32CM5164JH00048
CONFIG_SOC_PIC32CM2532JH00064
CONFIG_SOC_PIC32CM5164JH00064
CONFIG_SOC_PIC32CM2532JH00100
CONFIG_SOC_PIC32CM5164JH00100
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_jh/pic32cm_jh00/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_jh/pic32cm_jh00/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`CONFIG_SOC_PIC32CM2532JH00032`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM2532JH00032)、[`CONFIG_SOC_PIC32CM5164JH00032`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5164JH00032)、[`CONFIG_SOC_PIC32CM2532JH00048`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM2532JH00048)、[`CONFIG_SOC_PIC32CM5164JH00048`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5164JH00048)、[`CONFIG_SOC_PIC32CM2532JH00064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM2532JH00064)、[`CONFIG_SOC_PIC32CM5164JH00064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5164JH00064)、[`CONFIG_SOC_PIC32CM2532JH00100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM2532JH00100)、[`CONFIG_SOC_PIC32CM5164JH00100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5164JH00100)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`、`CONFIG_SOC_PIC32CM2532JH00032`、`CONFIG_SOC_PIC32CM5164JH00032`、`CONFIG_SOC_PIC32CM2532JH00048`、`CONFIG_SOC_PIC32CM5164JH00048`、`CONFIG_SOC_PIC32CM2532JH00064`、`CONFIG_SOC_PIC32CM5164JH00064`、`CONFIG_SOC_PIC32CM2532JH00100`、`CONFIG_SOC_PIC32CM5164JH00100`。

<a id="CONFIG_SOC_SERIES_PIC32CM_JH01"></a>

## 285.75 `CONFIG_SOC_SERIES_PIC32CM_JH01`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM JH01 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CM2532JH01032
CONFIG_SOC_PIC32CM5164JH01032
CONFIG_SOC_PIC32CM2532JH01048
CONFIG_SOC_PIC32CM5164JH01048
CONFIG_SOC_PIC32CM2532JH01064
CONFIG_SOC_PIC32CM5164JH01064
CONFIG_SOC_PIC32CM2532JH01100
CONFIG_SOC_PIC32CM5164JH01100
CONFIG_SOC_PIC32CM1216JH01032
CONFIG_SOC_PIC32CM1216JH01048
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_jh/pic32cm_jh01/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_jh/pic32cm_jh01/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`CONFIG_SOC_PIC32CM2532JH01032`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM2532JH01032)、[`CONFIG_SOC_PIC32CM5164JH01032`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5164JH01032)、[`CONFIG_SOC_PIC32CM2532JH01048`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM2532JH01048)、[`CONFIG_SOC_PIC32CM5164JH01048`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5164JH01048)、[`CONFIG_SOC_PIC32CM2532JH01064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM2532JH01064)、[`CONFIG_SOC_PIC32CM5164JH01064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5164JH01064)、[`CONFIG_SOC_PIC32CM2532JH01100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM2532JH01100)、[`CONFIG_SOC_PIC32CM5164JH01100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5164JH01100)、[`CONFIG_SOC_PIC32CM1216JH01032`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM1216JH01032)、[`CONFIG_SOC_PIC32CM1216JH01048`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM1216JH01048)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`、`CONFIG_SOC_PIC32CM2532JH01032`、`CONFIG_SOC_PIC32CM5164JH01032`、`CONFIG_SOC_PIC32CM2532JH01048`、`CONFIG_SOC_PIC32CM5164JH01048`、`CONFIG_SOC_PIC32CM2532JH01064`、`CONFIG_SOC_PIC32CM5164JH01064`、`CONFIG_SOC_PIC32CM2532JH01100`、`CONFIG_SOC_PIC32CM5164JH01100`、`CONFIG_SOC_PIC32CM1216JH01032`、`CONFIG_SOC_PIC32CM1216JH01048`。

<a id="CONFIG_SOC_SERIES_PIC32CM_PL10"></a>

## 285.76 `CONFIG_SOC_SERIES_PIC32CM_PL10`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM PL10 Cortex-M0+ 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CM6408PL10028
CONFIG_SOC_PIC32CM6408PL10032
CONFIG_SOC_PIC32CM6408PL10048
CONFIG_SOC_PIC32CM6408PL10064
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_pl/pic32cm_pl10/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_pl/pic32cm_pl10/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL)、[`CONFIG_SOC_PIC32CM6408PL10028`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM6408PL10028)、[`CONFIG_SOC_PIC32CM6408PL10032`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM6408PL10032)、[`CONFIG_SOC_PIC32CM6408PL10048`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM6408PL10048)、[`CONFIG_SOC_PIC32CM6408PL10064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM6408PL10064)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`、`CONFIG_SOC_PIC32CM6408PL10028`、`CONFIG_SOC_PIC32CM6408PL10032`、`CONFIG_SOC_PIC32CM6408PL10048`、`CONFIG_SOC_PIC32CM6408PL10064`。

<a id="CONFIG_SOC_SERIES_PIC32CM_SG00"></a>

## 285.77 `CONFIG_SOC_SERIES_PIC32CM_SG00`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CM SG00 Cortex-M23 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CM5112SG00048
CONFIG_SOC_PIC32CM5112SG00064
CONFIG_SOC_PIC32CM5112SG00100
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_sg_gc/pic32cm_sg00/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_sg_gc/pic32cm_sg00/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC)、[`CONFIG_SOC_PIC32CM5112SG00048`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5112SG00048)、[`CONFIG_SOC_PIC32CM5112SG00064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5112SG00064)、[`CONFIG_SOC_PIC32CM5112SG00100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CM5112SG00100)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`、`CONFIG_SOC_PIC32CM5112SG00048`、`CONFIG_SOC_PIC32CM5112SG00064`、`CONFIG_SOC_PIC32CM5112SG00100`。

<a id="CONFIG_SOC_SERIES_PIC32CX_SG41"></a>

## 285.78 `CONFIG_SOC_SERIES_PIC32CX_SG41`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CX SG41 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CX1025SG41064
CONFIG_SOC_PIC32CX1025SG41080
CONFIG_SOC_PIC32CX1025SG41100
CONFIG_SOC_PIC32CX1025SG41128
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cx_sg/pic32cx_sg41/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cx_sg/pic32cx_sg41/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`CONFIG_SOC_PIC32CX1025SG41064`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CX1025SG41064)、[`CONFIG_SOC_PIC32CX1025SG41080`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CX1025SG41080)、[`CONFIG_SOC_PIC32CX1025SG41100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CX1025SG41100)、[`CONFIG_SOC_PIC32CX1025SG41128`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CX1025SG41128)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`CONFIG_SOC_PIC32CX1025SG41064`、`CONFIG_SOC_PIC32CX1025SG41080`、`CONFIG_SOC_PIC32CX1025SG41100`、`CONFIG_SOC_PIC32CX1025SG41128`。

<a id="CONFIG_SOC_SERIES_PIC32CX_SG60"></a>

## 285.79 `CONFIG_SOC_SERIES_PIC32CX_SG60`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CX SG60 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CX1025SG60100
CONFIG_SOC_PIC32CX1025SG60128
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cx_sg/pic32cx_sg60/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cx_sg/pic32cx_sg60/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`CONFIG_SOC_PIC32CX1025SG60100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CX1025SG60100)、[`CONFIG_SOC_PIC32CX1025SG60128`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CX1025SG60128)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`CONFIG_SOC_PIC32CX1025SG60100`、`CONFIG_SOC_PIC32CX1025SG60128`。

<a id="CONFIG_SOC_SERIES_PIC32CX_SG61"></a>

## 285.80 `CONFIG_SOC_SERIES_PIC32CX_SG61`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CX SG61 Cortex-M4F 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CX1025SG61100
CONFIG_SOC_PIC32CX1025SG61128
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cx_sg/pic32cx_sg61/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cx_sg/pic32cx_sg61/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`CONFIG_SOC_PIC32CX1025SG61100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CX1025SG61100)、[`CONFIG_SOC_PIC32CX1025SG61128`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CX1025SG61128)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`CONFIG_SOC_PIC32CX1025SG61100`、`CONFIG_SOC_PIC32CX1025SG61128`。

<a id="CONFIG_SOC_SERIES_PIC32CZ_CA80"></a>

## 285.81 `CONFIG_SOC_SERIES_PIC32CZ_CA80`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CZ CA80 Cortex-M7 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CZ2051CA80100
CONFIG_SOC_PIC32CZ2051CA80144
CONFIG_SOC_PIC32CZ2051CA80176
CONFIG_SOC_PIC32CZ2051CA80208
CONFIG_SOC_PIC32CZ4010CA80100
CONFIG_SOC_PIC32CZ4010CA80144
CONFIG_SOC_PIC32CZ4010CA80176
CONFIG_SOC_PIC32CZ4010CA80208
CONFIG_SOC_PIC32CZ8110CA80100
CONFIG_SOC_PIC32CZ8110CA80144
CONFIG_SOC_PIC32CZ8110CA80176
CONFIG_SOC_PIC32CZ8110CA80208
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cz_ca/pic32cz_ca80/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cz_ca/pic32cz_ca80/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_PIC32CZ2051CA80100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ2051CA80100)、[`CONFIG_SOC_PIC32CZ2051CA80144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ2051CA80144)、[`CONFIG_SOC_PIC32CZ2051CA80176`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ2051CA80176)、[`CONFIG_SOC_PIC32CZ2051CA80208`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ2051CA80208)、[`CONFIG_SOC_PIC32CZ4010CA80100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ4010CA80100)、[`CONFIG_SOC_PIC32CZ4010CA80144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ4010CA80144)、[`CONFIG_SOC_PIC32CZ4010CA80176`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ4010CA80176)、[`CONFIG_SOC_PIC32CZ4010CA80208`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ4010CA80208)、[`CONFIG_SOC_PIC32CZ8110CA80100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ8110CA80100)、[`CONFIG_SOC_PIC32CZ8110CA80144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ8110CA80144)、[`CONFIG_SOC_PIC32CZ8110CA80176`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ8110CA80176)、[`CONFIG_SOC_PIC32CZ8110CA80208`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ8110CA80208)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_PIC32CZ2051CA80100`、`CONFIG_SOC_PIC32CZ2051CA80144`、`CONFIG_SOC_PIC32CZ2051CA80176`、`CONFIG_SOC_PIC32CZ2051CA80208`、`CONFIG_SOC_PIC32CZ4010CA80100`、`CONFIG_SOC_PIC32CZ4010CA80144`、`CONFIG_SOC_PIC32CZ4010CA80176`、`CONFIG_SOC_PIC32CZ4010CA80208`、`CONFIG_SOC_PIC32CZ8110CA80100`、`CONFIG_SOC_PIC32CZ8110CA80144`、`CONFIG_SOC_PIC32CZ8110CA80176`、`CONFIG_SOC_PIC32CZ8110CA80208`。

<a id="CONFIG_SOC_SERIES_PIC32CZ_CA90"></a>

## 285.82 `CONFIG_SOC_SERIES_PIC32CZ_CA90`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CZ CA90 Cortex-M7 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CZ2051CA90100
CONFIG_SOC_PIC32CZ2051CA90144
CONFIG_SOC_PIC32CZ2051CA90176
CONFIG_SOC_PIC32CZ2051CA90208
CONFIG_SOC_PIC32CZ4010CA90100
CONFIG_SOC_PIC32CZ4010CA90144
CONFIG_SOC_PIC32CZ4010CA90176
CONFIG_SOC_PIC32CZ4010CA90208
CONFIG_SOC_PIC32CZ8110CA90100
CONFIG_SOC_PIC32CZ8110CA90144
CONFIG_SOC_PIC32CZ8110CA90176
CONFIG_SOC_PIC32CZ8110CA90208
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cz_ca/pic32cz_ca90/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cz_ca/pic32cz_ca90/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_PIC32CZ2051CA90100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ2051CA90100)、[`CONFIG_SOC_PIC32CZ2051CA90144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ2051CA90144)、[`CONFIG_SOC_PIC32CZ2051CA90176`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ2051CA90176)、[`CONFIG_SOC_PIC32CZ2051CA90208`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ2051CA90208)、[`CONFIG_SOC_PIC32CZ4010CA90100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ4010CA90100)、[`CONFIG_SOC_PIC32CZ4010CA90144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ4010CA90144)、[`CONFIG_SOC_PIC32CZ4010CA90176`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ4010CA90176)、[`CONFIG_SOC_PIC32CZ4010CA90208`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ4010CA90208)、[`CONFIG_SOC_PIC32CZ8110CA90100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ8110CA90100)、[`CONFIG_SOC_PIC32CZ8110CA90144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ8110CA90144)、[`CONFIG_SOC_PIC32CZ8110CA90176`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ8110CA90176)、[`CONFIG_SOC_PIC32CZ8110CA90208`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ8110CA90208)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_PIC32CZ2051CA90100`、`CONFIG_SOC_PIC32CZ2051CA90144`、`CONFIG_SOC_PIC32CZ2051CA90176`、`CONFIG_SOC_PIC32CZ2051CA90208`、`CONFIG_SOC_PIC32CZ4010CA90100`、`CONFIG_SOC_PIC32CZ4010CA90144`、`CONFIG_SOC_PIC32CZ4010CA90176`、`CONFIG_SOC_PIC32CZ4010CA90208`、`CONFIG_SOC_PIC32CZ8110CA90100`、`CONFIG_SOC_PIC32CZ8110CA90144`、`CONFIG_SOC_PIC32CZ8110CA90176`、`CONFIG_SOC_PIC32CZ8110CA90208`。

<a id="CONFIG_SOC_SERIES_PIC32CZ_CA91"></a>

## 285.83 `CONFIG_SOC_SERIES_PIC32CZ_CA91`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC32CZ CA91 Cortex-M7 微控制器（microcontroller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC32CZ2051CA91100
CONFIG_SOC_PIC32CZ2051CA91144
CONFIG_SOC_PIC32CZ2051CA91176
CONFIG_SOC_PIC32CZ4010CA91100
CONFIG_SOC_PIC32CZ4010CA91144
CONFIG_SOC_PIC32CZ4010CA91176
CONFIG_SOC_PIC32CZ4010CA91208
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cz_ca/pic32cz_ca91/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cz_ca/pic32cz_ca91/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA)、[`CONFIG_SOC_PIC32CZ2051CA91100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ2051CA91100)、[`CONFIG_SOC_PIC32CZ2051CA91144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ2051CA91144)、[`CONFIG_SOC_PIC32CZ2051CA91176`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ2051CA91176)、[`CONFIG_SOC_PIC32CZ4010CA91100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ4010CA91100)、[`CONFIG_SOC_PIC32CZ4010CA91144`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ4010CA91144)、[`CONFIG_SOC_PIC32CZ4010CA91176`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ4010CA91176)、[`CONFIG_SOC_PIC32CZ4010CA91208`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC32CZ4010CA91208)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CZ_CA`、`CONFIG_SOC_PIC32CZ2051CA91100`、`CONFIG_SOC_PIC32CZ2051CA91144`、`CONFIG_SOC_PIC32CZ2051CA91176`、`CONFIG_SOC_PIC32CZ4010CA91100`、`CONFIG_SOC_PIC32CZ4010CA91144`、`CONFIG_SOC_PIC32CZ4010CA91176`、`CONFIG_SOC_PIC32CZ4010CA91208`。

<a id="CONFIG_SOC_SERIES_PIC64GX"></a>

## 285.84 `CONFIG_SOC_SERIES_PIC64GX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip PIC64GX 片上系统（SoC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC64
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC64GX1000
```

**定义位置（Location）**：[`soc/microchip/pic64/pic64gx/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic64/pic64gx/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC64)、[`CONFIG_SOC_PIC64GX1000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC64GX1000)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC64`、`CONFIG_SOC_PIC64GX1000`。

<a id="CONFIG_SOC_SERIES_POLARFIRE"></a>

## 285.85 `CONFIG_SOC_SERIES_POLARFIRE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip RV64 实现（implementation）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_MIV
```

**被选择（Selected by）**

```text
CONFIG_SOC_POLARFIRE
```

**定义位置（Location）**：[`soc/microchip/miv/polarfire/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/miv/polarfire/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MIV)、[`CONFIG_SOC_POLARFIRE`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_POLARFIRE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MIV`。

<a id="CONFIG_SOC_SERIES_SAMA5D2"></a>

## 285.86 `CONFIG_SOC_SERIES_SAMA5D2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA5D2 Cortex-A 微处理器（Microprocessor）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAMA5
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_SAMA5D27SOM
CONFIG_SOC_SERIES_SAMA5D29
CONFIG_SOC_SAMA5D21
CONFIG_SOC_SAMA5D22
CONFIG_SOC_SAMA5D225CD1M
CONFIG_SOC_SAMA5D23
CONFIG_SOC_SAMA5D24
CONFIG_SOC_SAMA5D26
CONFIG_SOC_SAMA5D27
CONFIG_SOC_SAMA5D27CD1G
CONFIG_SOC_SAMA5D27CD5M
CONFIG_SOC_SAMA5D27CLD1G
CONFIG_SOC_SAMA5D27CLD2G
CONFIG_SOC_SAMA5D28
CONFIG_SOC_SAMA5D28CD1G
CONFIG_SOC_SAMA5D28CLD1G
CONFIG_SOC_SAMA5D28CLD2G
```

**定义位置（Location）**：[`soc/microchip/sam/sama5/sama5d2/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama5/sama5d2/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA5`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_FAMILY_MICROCHIP_SAMA5)、[`CONFIG_SOC_SERIES_SAMA5D27SOM`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_SAMA5D27SOM)、[`CONFIG_SOC_SERIES_SAMA5D29`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_SAMA5D29)、[`CONFIG_SOC_SAMA5D21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D21)、[`CONFIG_SOC_SAMA5D22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D22)、[`CONFIG_SOC_SAMA5D225CD1M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D225CD1M)、[`CONFIG_SOC_SAMA5D23`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D23)、[`CONFIG_SOC_SAMA5D24`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D24)、[`CONFIG_SOC_SAMA5D26`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D26)、[`CONFIG_SOC_SAMA5D27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D27)、[`CONFIG_SOC_SAMA5D27CD1G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D27CD1G)、[`CONFIG_SOC_SAMA5D27CD5M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D27CD5M)、[`CONFIG_SOC_SAMA5D27CLD1G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D27CLD1G)、[`CONFIG_SOC_SAMA5D27CLD2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D27CLD2G)、[`CONFIG_SOC_SAMA5D28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D28)、[`CONFIG_SOC_SAMA5D28CD1G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D28CD1G)、[`CONFIG_SOC_SAMA5D28CLD1G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D28CLD1G)、[`CONFIG_SOC_SAMA5D28CLD2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D28CLD2G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SAMA5D21`、`CONFIG_SOC_SAMA5D22`、`CONFIG_SOC_SAMA5D225CD1M`、`CONFIG_SOC_SAMA5D23`、`CONFIG_SOC_SAMA5D24`、`CONFIG_SOC_SAMA5D26`、`CONFIG_SOC_SAMA5D27`、`CONFIG_SOC_SAMA5D27CD1G`、`CONFIG_SOC_SAMA5D27CD5M`、`CONFIG_SOC_SAMA5D27CLD1G`、`CONFIG_SOC_SAMA5D27CLD2G`、`CONFIG_SOC_SAMA5D28`、`CONFIG_SOC_SAMA5D28CD1G`、`CONFIG_SOC_SAMA5D28CLD1G`、`CONFIG_SOC_SAMA5D28CLD2G`。

<a id="CONFIG_SOC_SERIES_SAMA5D27SOM"></a>

## 285.87 `CONFIG_SOC_SERIES_SAMA5D27SOM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA5D2 系统模组（System-On-Module，SOM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_SAMA5D2
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAMA5D27SOM1
CONFIG_SOC_SAMA5D27WLSOM1
```

**定义位置（Location）**：[`soc/microchip/sam/sama5/sama5d2/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama5/sama5d2/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMA5D2`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_SAMA5D2)、[`CONFIG_SOC_SAMA5D27SOM1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D27SOM1)、[`CONFIG_SOC_SAMA5D27WLSOM1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D27WLSOM1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SAMA5D27SOM1`、`CONFIG_SOC_SAMA5D27WLSOM1`。

<a id="CONFIG_SOC_SERIES_SAMA5D29"></a>

## 285.88 `CONFIG_SOC_SERIES_SAMA5D29`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA5D29 Cortex-A 微处理器（Microprocessor）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_SAMA5D2
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAMA5D29
CONFIG_SOC_SAMA5D29TA100
```

**定义位置（Location）**：[`soc/microchip/sam/sama5/sama5d2/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama5/sama5d2/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_SAMA5D2`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_SERIES_SAMA5D2)、[`CONFIG_SOC_SAMA5D29`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D29)、[`CONFIG_SOC_SAMA5D29TA100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA5D29TA100)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SAMA5D29`、`CONFIG_SOC_SAMA5D29TA100`。

<a id="CONFIG_SOC_SERIES_SAMA7D6"></a>

## 285.89 `CONFIG_SOC_SERIES_SAMA7D6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA7D6 Cortex-A 微处理器（Microprocessor）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAMA7
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAMA7D65
CONFIG_SOC_SAMA7D65D1G
CONFIG_SOC_SAMA7D65D1GN2
CONFIG_SOC_SAMA7D65D2G
CONFIG_SOC_SAMA7D65D2GN8
CONFIG_SOC_SAMA7D65D5M
```

**定义位置（Location）**：[`soc/microchip/sam/sama7/sama7d6/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama7/sama7d6/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA7`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_FAMILY_MICROCHIP_SAMA7)、[`CONFIG_SOC_SAMA7D65`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7D65)、[`CONFIG_SOC_SAMA7D65D1G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7D65D1G)、[`CONFIG_SOC_SAMA7D65D1GN2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7D65D1GN2)、[`CONFIG_SOC_SAMA7D65D2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7D65D2G)、[`CONFIG_SOC_SAMA7D65D2GN8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7D65D2GN8)、[`CONFIG_SOC_SAMA7D65D5M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7D65D5M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SAMA7D65`、`CONFIG_SOC_SAMA7D65D1G`、`CONFIG_SOC_SAMA7D65D1GN2`、`CONFIG_SOC_SAMA7D65D2G`、`CONFIG_SOC_SAMA7D65D2GN8`、`CONFIG_SOC_SAMA7D65D5M`。

<a id="CONFIG_SOC_SERIES_SAMA7G5"></a>

## 285.90 `CONFIG_SOC_SERIES_SAMA7G5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA7G5 Cortex-A 微处理器（Microprocessor）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAMA7
```

**被选择（Selected by）**

```text
CONFIG_SOC_SAMA7G54
CONFIG_SOC_SAMA7G54D1G
CONFIG_SOC_SAMA7G54D1GN0
CONFIG_SOC_SAMA7G54D1GN2
CONFIG_SOC_SAMA7G54D2G
CONFIG_SOC_SAMA7G54D2GN4
CONFIG_SOC_SAMA7G54D4G
```

**定义位置（Location）**：[`soc/microchip/sam/sama7/sama7g5/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama7/sama7g5/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAMA7`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_FAMILY_MICROCHIP_SAMA7)、[`CONFIG_SOC_SAMA7G54`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7G54)、[`CONFIG_SOC_SAMA7G54D1G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7G54D1G)、[`CONFIG_SOC_SAMA7G54D1GN0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7G54D1GN0)、[`CONFIG_SOC_SAMA7G54D1GN2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7G54D1GN2)、[`CONFIG_SOC_SAMA7G54D2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7G54D2G)、[`CONFIG_SOC_SAMA7G54D2GN4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7G54D2GN4)、[`CONFIG_SOC_SAMA7G54D4G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SAMA7G54D4G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SAMA7G54`、`CONFIG_SOC_SAMA7G54D1G`、`CONFIG_SOC_SAMA7G54D1GN0`、`CONFIG_SOC_SAMA7G54D1GN2`、`CONFIG_SOC_SAMA7G54D2G`、`CONFIG_SOC_SAMA7G54D2GN4`、`CONFIG_SOC_SAMA7G54D4G`。

<a id="CONFIG_SOC_SERIES_SMARTFUSION2"></a>

## 285.91 `CONFIG_SOC_SERIES_SMARTFUSION2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip SmartFusion2 系列（series）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_MICROCHIP
```

**被选择（Selected by）**

```text
CONFIG_SOC_M2S010
```

**定义位置（Location）**：[`soc/microchip/smartfusion2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/smartfusion2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP)、[`CONFIG_SOC_M2S010`](P285_soc_microchip_配置项参考_1.md#CONFIG_SOC_M2S010)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP`。

<a id="CONFIG_UART_MCHP_SERCOM_U2201_5_0_0"></a>

## 285.92 `CONFIG_UART_MCHP_SERCOM_U2201_5_0_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用串行通信 UART 外设 IP（SERCOM UART peripheral IP）版本 5.0.0，标识为 U2201。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/microchip/sam/sam_d5x_e5x/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sam_d5x_e5x/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`。

<a id="SB_CONFIG_GPIO_MCHP_PORT_U2210_3_1_0"></a>

## 285.93 `SB_CONFIG_GPIO_MCHP_PORT_U2210_3_1_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 PORT GPIO 外设 IP，标识为 `U2210`，版本为 `3.1.0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_jh/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_jh/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`。

<a id="SB_CONFIG_PINCTRL_MCHP_PORT_U2210_2_2_0"></a>

## 285.94 `SB_CONFIG_PINCTRL_MCHP_PORT_U2210_2_2_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 PORT 引脚控制外设 IP（pinctrl peripheral IP）版本 2.2.0，标识为 U2210。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/microchip/sam/sam_d5x_e5x/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sam_d5x_e5x/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`。

<a id="SB_CONFIG_PINCTRL_MCHP_PORT_U2210_3_1_0"></a>

## 285.95 `SB_CONFIG_PINCTRL_MCHP_PORT_U2210_3_1_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 PORT 引脚控制外设 IP（pinctrl peripheral IP）版本 3.1.0，标识为 U2210。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/microchip/pic32c/pic32cm_jh/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/pic32c/pic32cm_jh/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`。

<a id="SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA5"></a>

## 285.96 `SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA5 Cortex-A 微处理器（Microprocessors）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_SAMA5D2
```

**定义位置（Location）**：[`soc/microchip/sam/sama5/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama5/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_SAMA5D2`](P286_soc_microchip_配置项参考_2.md#SB_CONFIG_SOC_SERIES_SAMA5D2)。

<a id="SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA7"></a>

## 285.97 `SB_CONFIG_SOC_FAMILY_MICROCHIP_SAMA7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Microchip SAMA7 Cortex-A 微处理器（Microprocessors）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_SAMA7D6
SB_CONFIG_SOC_SERIES_SAMA7G5
```

**定义位置（Location）**：[`soc/microchip/sam/sama7/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/sam/sama7/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_SAMA7D6`](P286_soc_microchip_配置项参考_2.md#SB_CONFIG_SOC_SERIES_SAMA7D6)、[`SB_CONFIG_SOC_SERIES_SAMA7G5`](P286_soc_microchip_配置项参考_2.md#SB_CONFIG_SOC_SERIES_SAMA7G5)。

<a id="SB_CONFIG_SOC_M2S010"></a>

## 285.98 `SB_CONFIG_SOC_M2S010`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip SmartFusion2 M2S010 片上系统（SoC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_SMARTFUSION2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_M2S_HELLO_FPGA_KIT
SB_CONFIG_BOARD_M2S010_MKR_KIT
```

**定义位置（Location）**：[`soc/microchip/smartfusion2/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/smartfusion2/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_SMARTFUSION2`](P286_soc_microchip_配置项参考_2.md#SB_CONFIG_SOC_SERIES_SMARTFUSION2)、[`SB_CONFIG_BOARD_M2S_HELLO_FPGA_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M2S_HELLO_FPGA_KIT)、[`SB_CONFIG_BOARD_M2S010_MKR_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M2S010_MKR_KIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_M2S_HELLO_FPGA_KIT`、`SB_CONFIG_BOARD_M2S010_MKR_KIT`。

<a id="SB_CONFIG_SOC_MIV"></a>

## 285.99 `SB_CONFIG_SOC_MIV`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip Mi-V 系统实现（system implementation）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_MIV
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_M2GL025_MIV
SB_CONFIG_BOARD_SCOBC_V1
```

**定义位置（Location）**：[`soc/microchip/miv/miv/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/miv/miv/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_MIV`](P286_soc_microchip_配置项参考_2.md#SB_CONFIG_SOC_SERIES_MIV)、[`SB_CONFIG_BOARD_M2GL025_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M2GL025_MIV)、[`SB_CONFIG_BOARD_SCOBC_V1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_SCOBC_V1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_M2GL025_MIV`、`SB_CONFIG_BOARD_SCOBC_V1`。

<a id="SB_CONFIG_SOC_POLARFIRE"></a>

## 285.100 `SB_CONFIG_SOC_POLARFIRE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Microchip MPFS 系统实现（system implementation）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_POLARFIRE
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_POLARFIRE_U54
SB_CONFIG_SOC_POLARFIRE_E51
```

**定义位置（Location）**：[`soc/microchip/miv/polarfire/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/microchip/miv/polarfire/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_POLARFIRE`](P286_soc_microchip_配置项参考_2.md#SB_CONFIG_SOC_SERIES_POLARFIRE)、[`SB_CONFIG_SOC_POLARFIRE_U54`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_POLARFIRE_U54)、[`SB_CONFIG_SOC_POLARFIRE_E51`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_POLARFIRE_E51)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_POLARFIRE_U54`、`SB_CONFIG_SOC_POLARFIRE_E51`。

<!-- kconfig-navigation -->

[上一章](P284_soc_mediatek_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P286_soc_microchip_配置项参考_2.md)
