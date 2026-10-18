---
id: learning.zephyr-docs.kconfig-reference.page-293
title: "`soc/nxp`配置项参考（1/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第293章\_`soc/nxp`配置项参考（1/3）

本章翻译官方 Kconfig 数据库中 `soc/nxp` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ADJUST_DCDC"></a>

## 293.1 `CONFIG_ADJUST_DCDC`

**提示（Prompt）**：调整内部直流－直流转换器输出（DCDC output）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_IMXRT10XX || CONFIG_SOC_SERIES_IMXRT11XX || CONFIG_SOC_SERIES_IMXRT118X) && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_ADJUST_LDO"></a>

## 293.2 `CONFIG_ADJUST_LDO`

**提示（Prompt）**：调整低压差稳压器设置（LDO setting）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT11XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt11xx/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_ADVC_DRIVER_USED"></a>

## 293.3 `CONFIG_ADVC_DRIVER_USED`

**提示（Prompt）**：NXP 自适应电压控制驱动支持（Adaptive Voltage Control，ADVC）

**说明（Help）**

链接通过 `west blobs` 获取的预编译 NXP 自适应电压控制库（ADVC library），并在 NXP 电源／时钟驱动中启用相应代码路径。禁用后，这些驱动改用根据目标频率选择固定电压的方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_MCXL255_CPU0 || CONFIG_SOC_MCXL255_CPU1
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxl/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxl/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MCXL255_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255_CPU0)、[`CONFIG_SOC_MCXL255_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255_CPU1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MCXL255_CPU0`、`CONFIG_SOC_MCXL255_CPU1`。

<a id="CONFIG_BOOT_DEVICE"></a>

## 293.4 `CONFIG_BOOT_DEVICE`

**提示（Prompt）**：启动设备（Boot device）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_IMXRT_BOOT_HEADER && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
CONFIG_BOOT_XSPI_NOR if DT_HAS_NXP_XSPI_ENABLED
CONFIG_BOOT_FLEXSPI_NOR
```

**可选项（Choices）**

```text
CONFIG_BOOT_XSPI_NOR
CONFIG_BOOT_FLEXSPI_NOR
CONFIG_BOOT_FLEXSPI_NAND
CONFIG_BOOT_SEMC_NOR
CONFIG_BOOT_SEMC_NAND
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header）

**配置项引用（Symbol References）**：[`CONFIG_NXP_IMXRT_BOOT_HEADER`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_IMXRT_BOOT_HEADER)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_BOOT_XSPI_NOR`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_XSPI_NOR)、[`CONFIG_BOOT_FLEXSPI_NOR`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_FLEXSPI_NOR)、[`CONFIG_BOOT_FLEXSPI_NAND`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_FLEXSPI_NAND)、[`CONFIG_BOOT_SEMC_NOR`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_SEMC_NOR)、[`CONFIG_BOOT_SEMC_NAND`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_SEMC_NAND)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_BOOT_FLEXSPI_NAND"></a>

## 293.5 `CONFIG_BOOT_FLEXSPI_NAND`

**提示（Prompt）**：FlexSPI 串行 NAND（serial NAND）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header） → 启动设备（Boot device）

<a id="CONFIG_BOOT_FLEXSPI_NOR"></a>

## 293.6 `CONFIG_BOOT_FLEXSPI_NOR`

**提示（Prompt）**：FlexSPI 串行 NOR（serial NOR）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header） → 启动设备（Boot device）

<a id="CONFIG_BOOT_HEADER_OFFSET"></a>

## 293.7 `CONFIG_BOOT_HEADER_OFFSET`

**提示（Prompt）**：Flash 配置数据偏移（Flash config data offset）

**说明（Help）**

Flash 配置偏移（flash config offset）用于向启动 ROM（boot ROM）提供板载 Flash 类型和参数。对于 FlexSPI 设备，启动 ROM 要求 Flash 配置位于固定偏移处。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NXP_MCXE31X_BOOT_HEADER && CONFIG_SOC_SERIES_MCXE31X && CONFIG_SOC_FAMILY_MCXE
```

**默认值（Defaults）**

```text
0x0
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxe/mcxe31x/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxe/mcxe31x/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NXP_MCXE31X_BOOT_HEADER`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_NXP_MCXE31X_BOOT_HEADER)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_FAMILY_MCXE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_FAMILY_MCXE`。

<a id="CONFIG_BOOT_SEMC_NAND"></a>

## 293.8 `CONFIG_BOOT_SEMC_NAND`

**提示（Prompt）**：SEMC 并行 NAND（parallel NAND）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header） → 启动设备（Boot device）

<a id="CONFIG_BOOT_SEMC_NOR"></a>

## 293.9 `CONFIG_BOOT_SEMC_NOR`

**提示（Prompt）**：SEMC 并行 NOR（parallel NOR）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header） → 启动设备（Boot device）

<a id="CONFIG_BOOT_XSPI_NOR"></a>

## 293.10 `CONFIG_BOOT_XSPI_NOR`

**提示（Prompt）**：XSPI 串行 NOR（serial NOR）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_XSPI_ENABLED && <choice CONFIG_BOOT_DEVICE>
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header） → 启动设备（Boot device）

**配置项引用（Symbol References）**：[`CONFIG_BOOT_DEVICE`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_DEVICE)。

<a id="CONFIG_BYPASS_LDO_LPSR"></a>

## 293.11 `CONFIG_BYPASS_LDO_LPSR`

**提示（Prompt）**：旁路 lpsr 低压差稳压器（Bypass LDO lpsr）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT11XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt11xx/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_CODE_DDR"></a>

## 293.12 `CONFIG_CODE_DDR`

**提示（Prompt）**：将代码链接到双倍数据速率内存（DDR memory）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CODE_LOCATION>
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 代码位置选择（Code location selection）

**配置项引用（Symbol References）**：[`CONFIG_CODE_LOCATION`](P293_soc_nxp_配置项参考_1.md#CONFIG_CODE_LOCATION)。

<a id="CONFIG_CODE_ITCM"></a>

## 293.13 `CONFIG_CODE_ITCM`

**提示（Prompt）**：将代码链接到内部指令紧耦合内存（Instruction Tightly Coupled Memory，ITCM）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CODE_LOCATION>
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 代码位置选择（Code location selection）

**配置项引用（Symbol References）**：[`CONFIG_CODE_LOCATION`](P293_soc_nxp_配置项参考_1.md#CONFIG_CODE_LOCATION)。

<a id="CONFIG_CODE_LOCATION"></a>

## 293.14 `CONFIG_CODE_LOCATION`

**提示（Prompt）**：代码位置选择（Code location selection）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_MIMX8ML8_M7 && CONFIG_SOC_FAMILY_NXP_IMX
```

**可选项（Choices）**

```text
CONFIG_CODE_ITCM
CONFIG_CODE_DDR
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX8ML8_M7`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX8ML8_M7)、[`CONFIG_SOC_FAMILY_NXP_IMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMX)、[`CONFIG_CODE_ITCM`](P293_soc_nxp_配置项参考_1.md#CONFIG_CODE_ITCM)、[`CONFIG_CODE_DDR`](P293_soc_nxp_配置项参考_1.md#CONFIG_CODE_DDR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMX`。

<a id="CONFIG_CONTAINER_USER_IMAGE_OFFSET"></a>

## 293.15 `CONFIG_CONTAINER_USER_IMAGE_OFFSET`

**提示（Prompt）**：容器头部与用户镜像之间的偏移（container header to user image offset）

**说明（Help）**

容器（container）与用户镜像（user image）之间的偏移。如果更改用户镜像起始地址，请务必修改 `CONTAINER_USER_IMAGE_OFFSET`，使 ROM 能够获取用户镜像起始地址。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT118X && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
0xA000
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt118x/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt118x/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_DCDC_TARGET_LOW_POWER_VOLTAGE"></a>

## 293.16 `CONFIG_DCDC_TARGET_LOW_POWER_VOLTAGE`

**提示（Prompt）**：低功耗模式的 DCDC 目标电压，单位为 mV（target DCDC voltage）

**说明（Help）**

进入挂起到空闲模式（suspend-to-idle）时，将 SoC 电压降到此目标值。如果低功耗模式的稳定性出现问题，可尝试提高此值。以 25 mV 为步长增加或减小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && CONFIG_SOC_SERIES_IMXRT10XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
1075
```

**取值范围（Ranges）**

```text
[925, 1300]
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt10xx/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt10xx/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_DCDC_TARGET_NORMAL_VOLTAGE"></a>

## 293.17 `CONFIG_DCDC_TARGET_NORMAL_VOLTAGE`

**提示（Prompt）**：正常模式的 DCDC 目标电压，单位为 mV（target DCDC voltage）

**说明（Help）**

退出挂起到空闲模式（suspend-to-idle）时，将 SoC 电压升到此值。以 25 mV 为步长增加或减小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && CONFIG_SOC_SERIES_IMXRT10XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
1275
```

**取值范围（Ranges）**

```text
[925, 1300]
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt10xx/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt10xx/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_DCDC_VALUE"></a>

## 293.18 `CONFIG_DCDC_VALUE`

**提示（Prompt）**：VDD_SOC 的直流－直流转换器设置值（DCDC value）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_IMXRT10XX || CONFIG_SOC_SERIES_IMXRT11XX || CONFIG_SOC_SERIES_IMXRT118X) && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L191)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_DEVICE_CONFIGURATION_DATA"></a>

## 293.19 `CONFIG_DEVICE_CONFIGURATION_DATA`

**提示（Prompt）**：设备配置数据（Device configuration data）

**说明（Help）**

设备配置数据（Device Configuration Data，DCD）向启动 ROM（boot ROM）提供一系列命令，用于初始化 SDRAM 等组件。如果应用希望在启动时完成 SDRAM 等组件的初始化，此功能会很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_IMXRT_BOOT_HEADER && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header）

**配置项引用（Symbol References）**：[`CONFIG_NXP_IMXRT_BOOT_HEADER`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_IMXRT_BOOT_HEADER)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_EXTERNAL_MEM_CONFIG_DATA"></a>

## 293.20 `CONFIG_EXTERNAL_MEM_CONFIG_DATA`

**提示（Prompt）**：外部存储器配置数据（External Memory Configuration Data）

**说明（Help）**

外部存储器配置数据（External Memory Configuration Data，XMDC）提供另一套配置序列，可在启动时初始化外部存储器。这套序列允许使用更高级的选项配置 SDRAM 等外部存储器。与 DCD 相比，这是一种新的替代启动头部（boot header）；必须禁用 DCD 才能选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_DEVICE_CONFIGURATION_DATA && CONFIG_NXP_IMXRT_BOOT_HEADER && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header）

**配置项引用（Symbol References）**：[`CONFIG_DEVICE_CONFIGURATION_DATA`](P293_soc_nxp_配置项参考_1.md#CONFIG_DEVICE_CONFIGURATION_DATA)、[`CONFIG_NXP_IMXRT_BOOT_HEADER`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_IMXRT_BOOT_HEADER)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_EXTERNAL_MEM_CONFIG_OFFSET"></a>

## 293.21 `CONFIG_EXTERNAL_MEM_CONFIG_OFFSET`

**提示（Prompt）**：外部存储器配置偏移（External memory configuration offset）

**说明（Help）**

按照启动 ROM（boot ROM）的规定，外部存储器配置数据（External Memory configuration data）必须放在特定地址位置，以便启动 ROM 指向它。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_EXTERNAL_MEM_CONFIG_DATA && CONFIG_NXP_IMXRT_BOOT_HEADER && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
0x800 if CONFIG_SOC_SERIES_IMXRT118X
0x1040 if CONFIG_BOOT_FLEXSPI_NOR || CONFIG_BOOT_SEMC_NOR
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header） → 外部存储器配置数据（External Memory Configuration Data）

**配置项引用（Symbol References）**：[`CONFIG_EXTERNAL_MEM_CONFIG_DATA`](P293_soc_nxp_配置项参考_1.md#CONFIG_EXTERNAL_MEM_CONFIG_DATA)、[`CONFIG_NXP_IMXRT_BOOT_HEADER`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_IMXRT_BOOT_HEADER)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_BOOT_FLEXSPI_NOR`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_FLEXSPI_NOR)、[`CONFIG_BOOT_SEMC_NOR`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_SEMC_NOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`、`CONFIG_SOC_SERIES_IMXRT118X`。

<a id="CONFIG_FLASH_CONFIG_OFFSET"></a>

## 293.22 `CONFIG_FLASH_CONFIG_OFFSET`

**提示（Prompt）**：Flash 配置数据偏移（Flash config data offset）

**说明（Help）**

Flash 配置偏移（flash config offset）用于向启动 ROM（boot ROM）提供板载 Flash 类型和参数。对于 FlexSPI 设备，启动 ROM 要求 Flash 配置位于固定偏移处。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_RW6XX_BOOT_HEADER && CONFIG_SOC_SERIES_RW6XX
```

**默认值（Defaults）**

```text
0x400
```

**定义位置（Location）**：[`soc/nxp/rw/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/rw/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建启动头部（Create boot header）

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW6XX_BOOT_HEADER`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_RW6XX_BOOT_HEADER)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_FLASH_DISABLE_CACHE64"></a>

## 293.23 `CONFIG_FLASH_DISABLE_CACHE64`

**提示（Prompt）**：禁用 FlexSPI Flash 访问的 CACHE64 缓存（cache）

**说明（Help）**

禁用 cache64 缓存（cache）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_MCXN947 || CONFIG_SOC_MCXN547) && CONFIG_SOC_FAMILY_MCXN
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxn/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxn/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MCXN947`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947)、[`CONFIG_SOC_MCXN547`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MCXN947`、`CONFIG_SOC_MCXN547`、`CONFIG_SOC_FAMILY_MCXN`。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_XIP"></a>

## 293.24 `CONFIG_FLASH_MCUX_FLEXSPI_XIP`

原库同名定义共 3 条；本项为数据库第 6525 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

计划从 FlexSPI 内存执行代码时，使 SoC 能够安全初始化 FlexSPI 时钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!(CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD || CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT) && CONFIG_SOC_FAMILY_MCXN
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_XIP
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxn/../../common/Kconfig.flexspi_xip:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxn/../../common/Kconfig.flexspi_xip#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MCXN`。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_XIP--record-6526"></a>

## 293.25 `CONFIG_FLASH_MCUX_FLEXSPI_XIP`

原库同名定义共 3 条；本项为数据库第 6526 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

计划从 FlexSPI 内存执行代码时，使 SoC 能够安全初始化 FlexSPI 时钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!(CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD || CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT) && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_XIP
```

**定义位置（Location）**：[`soc/nxp/imxrt/../common/Kconfig.flexspi_xip:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/../common/Kconfig.flexspi_xip#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_XIP--record-6527"></a>

## 293.26 `CONFIG_FLASH_MCUX_FLEXSPI_XIP`

原库同名定义共 3 条；本项为数据库第 6527 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

计划从 FlexSPI 内存执行代码时，使 SoC 能够安全初始化 FlexSPI 时钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!(CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD || CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT) && CONFIG_SOC_SERIES_RW6XX
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_XIP
```

**定义位置（Location）**：[`soc/nxp/rw/../common/Kconfig.flexspi_xip:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/rw/../common/Kconfig.flexspi_xip#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_XIP_MEM"></a>

## 293.27 `CONFIG_FLASH_MCUX_FLEXSPI_XIP_MEM`

原库同名定义共 3 条；本项为数据库第 6528 条记录，各定义分别保留。

**提示（Prompt）**：FlexSPI 驱动的内存位置（drivers memory location）

**说明（Help）**

选择使用 Flash API 时 FlexSPI 驱动的运行位置（location）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MCUX_FLEXSPI_XIP && CONFIG_MEMC_MCUX_FLEXSPI && CONFIG_SOC_FAMILY_MCXN
```

**默认值（Defaults）**

```text
"RAM"
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxn/../../common/Kconfig.flexspi_xip:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxn/../../common/Kconfig.flexspi_xip#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_FLEXSPI_XIP`](P293_soc_nxp_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_XIP)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`、`CONFIG_SOC_FAMILY_MCXN`。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_XIP_MEM--record-6529"></a>

## 293.28 `CONFIG_FLASH_MCUX_FLEXSPI_XIP_MEM`

原库同名定义共 3 条；本项为数据库第 6529 条记录，各定义分别保留。

**提示（Prompt）**：FlexSPI 驱动的内存位置（drivers memory location）

**说明（Help）**

选择使用 Flash API 时 FlexSPI 驱动的运行位置（location）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MCUX_FLEXSPI_XIP && CONFIG_MEMC_MCUX_FLEXSPI && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
"RAM"
```

**定义位置（Location）**：[`soc/nxp/imxrt/../common/Kconfig.flexspi_xip:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/../common/Kconfig.flexspi_xip#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_FLEXSPI_XIP`](P293_soc_nxp_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_XIP)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_XIP_MEM--record-6530"></a>

## 293.29 `CONFIG_FLASH_MCUX_FLEXSPI_XIP_MEM`

原库同名定义共 3 条；本项为数据库第 6530 条记录，各定义分别保留。

**提示（Prompt）**：FlexSPI 驱动的内存位置（drivers memory location）

**说明（Help）**

选择使用 Flash API 时 FlexSPI 驱动的运行位置（location）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MCUX_FLEXSPI_XIP && CONFIG_MEMC_MCUX_FLEXSPI && CONFIG_SOC_SERIES_RW6XX
```

**默认值（Defaults）**

```text
"RAM"
```

**定义位置（Location）**：[`soc/nxp/rw/../common/Kconfig.flexspi_xip:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/rw/../common/Kconfig.flexspi_xip#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_FLEXSPI_XIP`](P293_soc_nxp_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_XIP)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`、`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_FLASH_MCUX_XSPI_XIP"></a>

## 293.30 `CONFIG_FLASH_MCUX_XSPI_XIP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

计划从 XSPI 内存执行代码时，使 SoC 能够安全初始化 XSPI 时钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_XSPI_ENABLED && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_XIP
```

**定义位置（Location）**：[`soc/nxp/imxrt/../common/Kconfig.xspi_xip:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/../common/Kconfig.xspi_xip#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_FLASH_MCUX_XSPI_XIP_MEM"></a>

## 293.31 `CONFIG_FLASH_MCUX_XSPI_XIP_MEM`

**提示（Prompt）**：XSPI 驱动的内存位置（drivers memory location）

**说明（Help）**

选择使用 Flash API 时 XSPI 驱动的运行位置（location）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MCUX_XSPI_XIP && DT_HAS_NXP_XSPI_ENABLED && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
"RAM"
```

**定义位置（Location）**：[`soc/nxp/imxrt/../common/Kconfig.xspi_xip:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/../common/Kconfig.xspi_xip#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_XSPI_XIP`](P293_soc_nxp_配置项参考_1.md#CONFIG_FLASH_MCUX_XSPI_XIP)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_FLEXCOMM0_CLK_SRC"></a>

## 293.32 `CONFIG_FLEXCOMM0_CLK_SRC`

**提示（Prompt）**：Flexcomm0 时钟源（Clock source）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT5XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
CONFIG_FLEXCOMM0_CLK_SRC_FRG
```

**可选项（Choices）**

```text
CONFIG_FLEXCOMM0_CLK_SRC_FRG
CONFIG_FLEXCOMM0_CLK_SRC_FRO
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt5xx/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt5xx/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT5XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT5XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_FLEXCOMM0_CLK_SRC_FRG`](P293_soc_nxp_配置项参考_1.md#CONFIG_FLEXCOMM0_CLK_SRC_FRG)、[`CONFIG_FLEXCOMM0_CLK_SRC_FRO`](P293_soc_nxp_配置项参考_1.md#CONFIG_FLEXCOMM0_CLK_SRC_FRO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT5XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_FLEXCOMM0_CLK_SRC_FRG"></a>

## 293.33 `CONFIG_FLEXCOMM0_CLK_SRC_FRG`

**提示（Prompt）**：Flexcomm0 时钟源为分数波特率发生器（FRG）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLEXCOMM0_CLK_SRC>
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt5xx/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt5xx/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flexcomm0 时钟源（Clock source）

**配置项引用（Symbol References）**：[`CONFIG_FLEXCOMM0_CLK_SRC`](P293_soc_nxp_配置项参考_1.md#CONFIG_FLEXCOMM0_CLK_SRC)。

<a id="CONFIG_FLEXCOMM0_CLK_SRC_FRO"></a>

## 293.34 `CONFIG_FLEXCOMM0_CLK_SRC_FRO`

**提示（Prompt）**：Flexcomm0 时钟源为 FRO_DIV4

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLEXCOMM0_CLK_SRC>
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt5xx/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt5xx/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flexcomm0 时钟源（Clock source）

**配置项引用（Symbol References）**：[`CONFIG_FLEXCOMM0_CLK_SRC`](P293_soc_nxp_配置项参考_1.md#CONFIG_FLEXCOMM0_CLK_SRC)。

<a id="CONFIG_FLEXSPI_CONFIG_BLOCK_OFFSET"></a>

## 293.35 `CONFIG_FLEXSPI_CONFIG_BLOCK_OFFSET`

原库同名定义共 2 条；本项为数据库第 6624 条记录，各定义分别保留。

**提示（Prompt）**：FlexSPI 配置块偏移（config block offset）

**说明（Help）**

FlexSPI 配置块（configuration block）由特定 Flash 器件的参数组成，包括读取命令序列、可选的四线模式启用序列（quad mode enablement sequence）等。启动 ROM（boot ROM）要求 FlexSPI 配置参数位于串行 NOR Flash 中。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_FLEXSPI_BOOT_HEADER && CONFIG_SOC_FAMILY_MCXN
```

**默认值（Defaults）**

```text
0x400
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxn/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxn/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header）

**配置项引用（Symbol References）**：[`CONFIG_NXP_FLEXSPI_BOOT_HEADER`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_FLEXSPI_BOOT_HEADER)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MCXN`。

<a id="CONFIG_FLEXSPI_CONFIG_BLOCK_OFFSET--record-6625"></a>

## 293.36 `CONFIG_FLEXSPI_CONFIG_BLOCK_OFFSET`

原库同名定义共 2 条；本项为数据库第 6625 条记录，各定义分别保留。

**提示（Prompt）**：FlexSPI 配置块偏移（config block offset）

**说明（Help）**

FlexSPI 配置块（configuration block）由特定 Flash 器件的参数组成，包括读取命令序列、可选的四线模式启用序列（quad mode enablement sequence）等。启动 ROM（boot ROM）要求 FlexSPI 配置参数位于串行 NOR Flash 中。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOT_FLEXSPI_NOR && CONFIG_NXP_IMXRT_BOOT_HEADER && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
0x0 if CONFIG_BOOT_FLEXSPI_NOR
0x400
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header）

**配置项引用（Symbol References）**：[`CONFIG_BOOT_FLEXSPI_NOR`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_FLEXSPI_NOR)、[`CONFIG_NXP_IMXRT_BOOT_HEADER`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_IMXRT_BOOT_HEADER)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_GLIKEY_MCUX_GLIKEY"></a>

## 293.37 `CONFIG_GLIKEY_MCUX_GLIKEY`

**提示（Prompt）**：使用 MCUX 的 glikey 驱动（glikey MCUX Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT7XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT7XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT7XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT7XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_HAS_MCG"></a>

## 293.38 `CONFIG_HAS_MCG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 SoC 包含多用途时钟发生器模块（Multipurpose Clock Generator，MCG），则设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_KINETIS
```

**被选择（Selected by）**

```text
CONFIG_SOC_MK22F51212
CONFIG_SOC_MK22F12
CONFIG_SOC_MK64F12
CONFIG_SOC_MK66F18
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_MKL25Z4
CONFIG_SOC_SERIES_KV5X
CONFIG_SOC_MKW22D5
CONFIG_SOC_MKW24D5
CONFIG_SOC_MKW40Z4
CONFIG_SOC_MKW41Z4
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)、[`CONFIG_SOC_MK22F51212`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK22F51212)、[`CONFIG_SOC_MK22F12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK22F12)、[`CONFIG_SOC_MK64F12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK64F12)、[`CONFIG_SOC_MK66F18`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK66F18)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_MKL25Z4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKL25Z4)、[`CONFIG_SOC_SERIES_KV5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KV5X)、[`CONFIG_SOC_MKW22D5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW22D5)、[`CONFIG_SOC_MKW24D5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW24D5)、[`CONFIG_SOC_MKW40Z4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW40Z4)、[`CONFIG_SOC_MKW41Z4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW41Z4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`、`CONFIG_SOC_MK22F51212`、`CONFIG_SOC_MK22F12`、`CONFIG_SOC_MK64F12`、`CONFIG_SOC_MK66F18`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_MKL25Z4`、`CONFIG_SOC_SERIES_KV5X`、`CONFIG_SOC_MKW22D5`、`CONFIG_SOC_MKW24D5`、`CONFIG_SOC_MKW40Z4`、`CONFIG_SOC_MKW41Z4`。

<a id="CONFIG_HAS_OSC"></a>

## 293.39 `CONFIG_HAS_OSC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 SoC 包含振荡器模块（Oscillator，OSC），则设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_KINETIS
```

**被选择（Selected by）**

```text
CONFIG_SOC_MK22F51212
CONFIG_SOC_MK22F12
CONFIG_SOC_MK64F12
CONFIG_SOC_MK66F18
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_MKL25Z4
CONFIG_SOC_SERIES_KV5X
CONFIG_SOC_MKW22D5
CONFIG_SOC_MKW24D5
CONFIG_SOC_MKW40Z4
CONFIG_SOC_MKW41Z4
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)、[`CONFIG_SOC_MK22F51212`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK22F51212)、[`CONFIG_SOC_MK22F12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK22F12)、[`CONFIG_SOC_MK64F12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK64F12)、[`CONFIG_SOC_MK66F18`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK66F18)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_MKL25Z4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKL25Z4)、[`CONFIG_SOC_SERIES_KV5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KV5X)、[`CONFIG_SOC_MKW22D5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW22D5)、[`CONFIG_SOC_MKW24D5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW24D5)、[`CONFIG_SOC_MKW40Z4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW40Z4)、[`CONFIG_SOC_MKW41Z4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MKW41Z4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`、`CONFIG_SOC_MK22F51212`、`CONFIG_SOC_MK22F12`、`CONFIG_SOC_MK64F12`、`CONFIG_SOC_MK66F18`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_MKL25Z4`、`CONFIG_SOC_SERIES_KV5X`、`CONFIG_SOC_MKW22D5`、`CONFIG_SOC_MKW24D5`、`CONFIG_SOC_MKW40Z4`、`CONFIG_SOC_MKW41Z4`。

<a id="CONFIG_IMAGE_CONTAINER_OFFSET"></a>

## 293.40 `CONFIG_IMAGE_CONTAINER_OFFSET`

**提示（Prompt）**：镜像容器（Image container）

**说明（Help）**

镜像容器（image container）是 ROM 使用的一种启动镜像格式，由容器头部（container header）、镜像数组条目（image array entry）、签名块（signature block）、用户程序镜像和数据组成。启动 ROM（boot ROM）要求容器数据保存在外部存储器中。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT118X && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
0x1000
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt118x/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt118x/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_IMAGE_VECTOR_TABLE_OFFSET"></a>

## 293.41 `CONFIG_IMAGE_VECTOR_TABLE_OFFSET`

原库同名定义共 3 条；本项为数据库第 8285 条记录，各定义分别保留。

**提示（Prompt）**：镜像向量表偏移（Image vector table offset）

**说明（Help）**

镜像向量表（Image Vector Table，IVT）向启动 ROM（boot ROM）提供应用入口点和设备配置数据的指针。对于每种启动设备，启动 ROM 都要求固定的 IVT 偏移。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NXP_MCXE31X_BOOT_HEADER && CONFIG_SOC_SERIES_MCXE31X && CONFIG_SOC_FAMILY_MCXE
```

**默认值（Defaults）**

```text
0x1000
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxe/mcxe31x/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxe/mcxe31x/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NXP_MCXE31X_BOOT_HEADER`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_NXP_MCXE31X_BOOT_HEADER)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_FAMILY_MCXE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_FAMILY_MCXE`。

<a id="CONFIG_IMAGE_VECTOR_TABLE_OFFSET--record-8286"></a>

## 293.42 `CONFIG_IMAGE_VECTOR_TABLE_OFFSET`

原库同名定义共 3 条；本项为数据库第 8286 条记录，各定义分别保留。

**提示（Prompt）**：镜像向量表偏移（Image vector table offset）

**说明（Help）**

镜像向量表（Image Vector Table，IVT）向启动 ROM（boot ROM）提供应用入口点和设备配置数据的指针。对于每种启动设备，启动 ROM 都要求固定的 IVT 偏移。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_IMXRT_BOOT_HEADER && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
0x1000 if CONFIG_BOOT_FLEXSPI_NOR || CONFIG_BOOT_SEMC_NOR
0x400 if CONFIG_BOOT_FLEXSPI_NAND || CONFIG_BOOT_SEMC_NAND
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header）

**配置项引用（Symbol References）**：[`CONFIG_NXP_IMXRT_BOOT_HEADER`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_IMXRT_BOOT_HEADER)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_BOOT_FLEXSPI_NOR`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_FLEXSPI_NOR)、[`CONFIG_BOOT_SEMC_NOR`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_SEMC_NOR)、[`CONFIG_BOOT_FLEXSPI_NAND`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_FLEXSPI_NAND)、[`CONFIG_BOOT_SEMC_NAND`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_SEMC_NAND)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_IMAGE_VECTOR_TABLE_OFFSET--record-8287"></a>

## 293.43 `CONFIG_IMAGE_VECTOR_TABLE_OFFSET`

原库同名定义共 3 条；本项为数据库第 8287 条记录，各定义分别保留。

**提示（Prompt）**：镜像向量表偏移（Image vector table offset）

**说明（Help）**

镜像向量表（Image Vector Table，IVT）向启动 ROM（boot ROM）提供应用入口点和设备配置数据的指针。对于每种启动设备，启动 ROM 都要求固定的 IVT 偏移。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_RW6XX_BOOT_HEADER && CONFIG_SOC_SERIES_RW6XX
```

**默认值（Defaults）**

```text
0x1000
```

**定义位置（Location）**：[`soc/nxp/rw/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/rw/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建启动头部（Create boot header）

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW6XX_BOOT_HEADER`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_RW6XX_BOOT_HEADER)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_IMXRT5XX_CODE_CACHE"></a>

## 293.44 `CONFIG_IMXRT5XX_CODE_CACHE`

**提示（Prompt）**：代码缓存（Code cache）

**说明（Help）**

启动时为 FlexSPI 区域启用代码缓存（code cache）。如果关闭此 Kconfig 项，则在 SoC 初始化期间禁用 CACHE64 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT5XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt5xx/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt5xx/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT5XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT5XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT5XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_IMXRT6XX_CODE_CACHE"></a>

## 293.45 `CONFIG_IMXRT6XX_CODE_CACHE`

**提示（Prompt）**：代码缓存（Code cache）

**说明（Help）**

启动时为 FlexSPI 区域启用代码缓存（code cache）。如果关闭此 Kconfig 项，则在 SoC 初始化期间禁用 CACHE64 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_MIMXRT685S_CM33 && CONFIG_SOC_SERIES_IMXRT6XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt6xx/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt6xx/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_SERIES_IMXRT6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT6XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_SERIES_IMXRT6XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_INIT_ARM_PLL"></a>

## 293.46 `CONFIG_INIT_ARM_PLL`

**提示（Prompt）**：初始化 ARM 锁相环（ARM PLL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_MIMXRT1011 && !CONFIG_SOC_MIMXRT1015 && !CONFIG_SOC_MIMXRT1021 && !CONFIG_SOC_MIMXRT1024 && (CONFIG_SOC_SERIES_IMXRT10XX || CONFIG_SOC_SERIES_IMXRT11XX || CONFIG_SOC_SERIES_IMXRT118X) && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT1011`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1011)、[`CONFIG_SOC_MIMXRT1015`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1015)、[`CONFIG_SOC_MIMXRT1021`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1021)、[`CONFIG_SOC_MIMXRT1024`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1024)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT1011`、`CONFIG_SOC_MIMXRT1015`、`CONFIG_SOC_MIMXRT1021`、`CONFIG_SOC_MIMXRT1024`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_INIT_AUDIO_PLL"></a>

## 293.47 `CONFIG_INIT_AUDIO_PLL`

**提示（Prompt）**：初始化音频锁相环（Audio PLL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_MIMXRT685S_CM33 && CONFIG_SOC_SERIES_IMXRT6XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt6xx/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt6xx/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_SERIES_IMXRT6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT6XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_SERIES_IMXRT6XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_INIT_ENET_PLL"></a>

## 293.48 `CONFIG_INIT_ENET_PLL`

**提示（Prompt）**：初始化以太网锁相环（ENET PLL）

**说明（Help）**

启用后，会调用 SDK 函数初始化以太网锁相环（enet pll）。SDK 所称“enet pll”在硬件上的确切含义随平台变化，API 签名也随之不同。此配置还假定每个 SoC 采用某种默认时钟方案。要进一步理解，请查看该平台的 `soc.c` 和 HAL 中的 `fsl_clock.c`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT10XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y if CONFIG_ETH_NXP_ENET
```

**被选择（Selected by）**

```text
CONFIG_INIT_PLL6_500M
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt10xx/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt10xx/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_ETH_NXP_ENET`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET)、[`CONFIG_INIT_PLL6_500M`](P293_soc_nxp_配置项参考_1.md#CONFIG_INIT_PLL6_500M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_INIT_PLL0"></a>

## 293.49 `CONFIG_INIT_PLL0`

**提示（Prompt）**：初始化锁相环 0（PLL0）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_LPC55XXX && CONFIG_SOC_FAMILY_LPC
```

**定义位置（Location）**：[`soc/nxp/lpc/lpc55xxx/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/lpc/lpc55xxx/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_LPC55XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC55XXX)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC55XXX`、`CONFIG_SOC_FAMILY_LPC`。

<a id="CONFIG_INIT_PLL1"></a>

## 293.50 `CONFIG_INIT_PLL1`

**提示（Prompt）**：初始化锁相环 1（PLL1）

**说明（Help）**

在 LPC55XXX 家族中，此项当前用于将内核时钟设为其最高频率 150MHz。注意，Flash 编程操作的频率上限为 100MHz，在这些情况下不应使用该锁相环（PLL）作为内核时钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!(CONFIG_SOC_LPC55S06 || CONFIG_FLASH || CONFIG_BUILD_WITH_TFM) && CONFIG_SOC_SERIES_LPC55XXX && CONFIG_SOC_FAMILY_LPC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/lpc/lpc55xxx/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/lpc/lpc55xxx/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_LPC55S06`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC55S06)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_SERIES_LPC55XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC55XXX)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_LPC55S06`、`CONFIG_SOC_SERIES_LPC55XXX`、`CONFIG_SOC_FAMILY_LPC`。

<a id="CONFIG_INIT_PLL6_500M"></a>

## 293.51 `CONFIG_INIT_PLL6_500M`

**提示（Prompt）**：启用 PLL6 的 500M 输出（output enable）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_MIMXRT1011 || CONFIG_SOC_MIMXRT1015 || CONFIG_SOC_MIMXRT1021 || CONFIG_SOC_MIMXRT1024) && CONFIG_SOC_SERIES_IMXRT10XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INIT_ENET_PLL
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt10xx/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt10xx/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT1011`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1011)、[`CONFIG_SOC_MIMXRT1015`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1015)、[`CONFIG_SOC_MIMXRT1021`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1021)、[`CONFIG_SOC_MIMXRT1024`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1024)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_INIT_ENET_PLL`](P293_soc_nxp_配置项参考_1.md#CONFIG_INIT_ENET_PLL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT1011`、`CONFIG_SOC_MIMXRT1015`、`CONFIG_SOC_MIMXRT1021`、`CONFIG_SOC_MIMXRT1024`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_INIT_SYS_PLL"></a>

## 293.52 `CONFIG_INIT_SYS_PLL`

原库同名定义共 3 条；本项为数据库第 8340 条记录，各定义分别保留。

**提示（Prompt）**：初始化系统锁相环（System PLL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT10XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_MIMXRT1042
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT685S_CM33
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt10xx/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt10xx/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_SOC_MIMXRT1042`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1042)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`、`CONFIG_SOC_MIMXRT1042`、`CONFIG_SOC_MIMXRT685S_CM33`。

<a id="CONFIG_INIT_SYS_PLL--record-8341"></a>

## 293.53 `CONFIG_INIT_SYS_PLL`

原库同名定义共 3 条；本项为数据库第 8341 条记录，各定义分别保留。

**提示（Prompt）**：初始化 SYS 锁相环（SYS PLL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_MIMXRT685S_CM33 && CONFIG_SOC_SERIES_IMXRT6XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT685S_CM33
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt6xx/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt6xx/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_SERIES_IMXRT6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT6XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_SERIES_IMXRT6XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_INIT_SYS_PLL--record-8342"></a>

## 293.54 `CONFIG_INIT_SYS_PLL`

原库同名定义共 3 条；本项为数据库第 8342 条记录，各定义分别保留。

**提示（Prompt）**：初始化系统锁相环（System PLL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_IMXRT10XX || CONFIG_SOC_SERIES_IMXRT11XX || CONFIG_SOC_SERIES_IMXRT118X) && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT685S_CM33
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`、`CONFIG_SOC_MIMXRT685S_CM33`。

<a id="CONFIG_INIT_VIDEO_PLL"></a>

## 293.55 `CONFIG_INIT_VIDEO_PLL`

原库同名定义共 2 条；本项为数据库第 8343 条记录，各定义分别保留。

**提示（Prompt）**：初始化视频锁相环（Video PLL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_IMXRT10XX || CONFIG_SOC_SERIES_IMXRT11XX || CONFIG_SOC_SERIES_IMXRT118X) && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMX8ML8_M7
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:200`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L200)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_SOC_MIMX8ML8_M7`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX8ML8_M7)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_INIT_VIDEO_PLL--record-8344"></a>

## 293.56 `CONFIG_INIT_VIDEO_PLL`

原库同名定义共 2 条；本项为数据库第 8344 条记录，各定义分别保留。

**提示（Prompt）**：初始化视频锁相环（Video PLL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_MIMX8ML8_M7 && CONFIG_SOC_FAMILY_NXP_IMX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMX8ML8_M7
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX8ML8_M7`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX8ML8_M7)、[`CONFIG_SOC_FAMILY_NXP_IMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMX`。

<a id="CONFIG_IVT_HEADER_OFFSET"></a>

## 293.57 `CONFIG_IVT_HEADER_OFFSET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

镜像向量表头部相对于 Flash 基地址的偏移（ivt header offset）

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_XIP && CONFIG_SOC_SERIES_S32K3 && CONFIG_SOC_FAMILY_NXP_S32
```

**默认值（Defaults）**

```text
0x0
```

**定义位置（Location）**：[`soc/nxp/s32/s32k3/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/s32/s32k3/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_FAMILY_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_S32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_FAMILY_NXP_S32`。

<a id="CONFIG_IVT_HEADER_SIZE"></a>

## 293.58 `CONFIG_IVT_HEADER_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

镜像向量表头部区域大小（ivt header region size）

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_XIP && CONFIG_SOC_SERIES_S32K3 && CONFIG_SOC_FAMILY_NXP_S32
```

**默认值（Defaults）**

```text
0x0
```

**定义位置（Location）**：[`soc/nxp/s32/s32k3/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/s32/s32k3/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_FAMILY_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_S32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_FAMILY_NXP_S32`。

<a id="CONFIG_K6X_HSRUN"></a>

## 293.59 `CONFIG_K6X_HSRUN`

**提示（Prompt）**：高速运行模式（High Speed RUN mode）

**说明（Help）**

此选项在 K66F SoC 上启用高速运行模式（High Speed RUN mode）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_MK66F18 && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/kinetis/k6x/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/k6x/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MK66F18`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MK66F18)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MK66F18`、`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_K8X_BUS_CLOCK_DIVIDER"></a>

## 293.60 `CONFIG_K8X_BUS_CLOCK_DIVIDER`

**提示（Prompt）**：Freescale K8x 总线时钟分频值（bus clock divider）

**说明（Help）**

此选项指定从系统时钟生成 K8x 总线时钟（bus clock）所用的分频值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_K8X && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`soc/nxp/kinetis/k8x/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/k8x/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_K8X_CORE_CLOCK_DIVIDER"></a>

## 293.61 `CONFIG_K8X_CORE_CLOCK_DIVIDER`

**提示（Prompt）**：Freescale K8x 内核时钟分频值（core clock divider）

**说明（Help）**

此选项指定从系统时钟生成 K8x 处理器内核时钟（processor core clock）所用的分频值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_K8X && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`soc/nxp/kinetis/k8x/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/k8x/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_K8X_FLASH_CLOCK_DIVIDER"></a>

## 293.62 `CONFIG_K8X_FLASH_CLOCK_DIVIDER`

**提示（Prompt）**：Freescale K8x Flash 时钟分频值（flash clock divider）

**说明（Help）**

此选项指定从系统时钟生成 K8x Flash 时钟所用的分频值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_K8X && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`soc/nxp/kinetis/k8x/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/k8x/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_K8X_FLEXBUS_CLOCK_DIVIDER"></a>

## 293.63 `CONFIG_K8X_FLEXBUS_CLOCK_DIVIDER`

**提示（Prompt）**：Freescale K8x FlexBus 时钟分频值（clock divider）

**说明（Help）**

此选项指定从系统时钟生成 K8x FlexBus 时钟所用的分频值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_K8X && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`soc/nxp/kinetis/k8x/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/k8x/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_KINETIS_FLASH_CONFIG"></a>

## 293.64 `CONFIG_KINETIS_FLASH_CONFIG`

**提示（Prompt）**：Kinetis Flash 配置字段（flash configuration field）

**说明（Help）**

包含 16 字节的 Flash 配置字段（configuration field），用于存储复位时加载的默认保护设置，以及允许 MCU 限制 FTFx 模块访问的安全信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
y if CONFIG_XIP && !CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_KINETIS_FLASH_CONFIG_FDPROT"></a>

## 293.65 `CONFIG_KINETIS_FLASH_CONFIG_FDPROT`

**提示（Prompt）**：数据 Flash 保护字节（Data flash protection byte，FDPROT）

**说明（Help）**

为 FlexNVM 器件配置 FDPROT 寄存器的复位值。对于只有程序 Flash 的器件，此字节为保留字节（reserved）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_KINETIS_FLASH_CONFIG && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
0xff
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Kinetis Flash 配置字段（flash configuration field）

**配置项引用（Symbol References）**：[`CONFIG_KINETIS_FLASH_CONFIG`](P293_soc_nxp_配置项参考_1.md#CONFIG_KINETIS_FLASH_CONFIG)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_KINETIS_FLASH_CONFIG_FEPROT"></a>

## 293.66 `CONFIG_KINETIS_FLASH_CONFIG_FEPROT`

**提示（Prompt）**：电可擦可编程只读存储器保护字节（EEPROM protection byte，FEPROT）

**说明（Help）**

为 FlexNVM 器件配置 FEPROT 寄存器的复位值。对于只有程序 Flash 的器件，此字节为保留字节（reserved）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_KINETIS_FLASH_CONFIG && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
0xff
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Kinetis Flash 配置字段（flash configuration field）

**配置项引用（Symbol References）**：[`CONFIG_KINETIS_FLASH_CONFIG`](P293_soc_nxp_配置项参考_1.md#CONFIG_KINETIS_FLASH_CONFIG)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_KINETIS_FLASH_CONFIG_FOPT"></a>

## 293.67 `CONFIG_KINETIS_FLASH_CONFIG_FOPT`

**提示（Prompt）**：Flash 非易失选项字节（Flash nonvolatile option byte，FOPT）

**说明（Help）**

配置 FOPT 寄存器的复位值，其中包含启动（boot）、不可屏蔽中断（NMI）和 EzPort 选项。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_KINETIS_FLASH_CONFIG && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
0xff
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Kinetis Flash 配置字段（flash configuration field）

**配置项引用（Symbol References）**：[`CONFIG_KINETIS_FLASH_CONFIG`](P293_soc_nxp_配置项参考_1.md#CONFIG_KINETIS_FLASH_CONFIG)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_KINETIS_FLASH_CONFIG_FSEC"></a>

## 293.68 `CONFIG_KINETIS_FLASH_CONFIG_FSEC`

**提示（Prompt）**：Flash 安全字节（Flash security byte，FSEC）

**说明（Help）**

配置 FSEC 寄存器的复位值，其中包含后门密钥访问（backdoor key access）、批量擦除（mass erase）、工厂访问（factory access）和 Flash 安全选项。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_KINETIS_FLASH_CONFIG && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
0xfe
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Kinetis Flash 配置字段（flash configuration field）

**配置项引用（Symbol References）**：[`CONFIG_KINETIS_FLASH_CONFIG`](P293_soc_nxp_配置项参考_1.md#CONFIG_KINETIS_FLASH_CONFIG)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_KINETIS_FLASH_CONFIG_OFFSET"></a>

## 293.69 `CONFIG_KINETIS_FLASH_CONFIG_OFFSET`

**提示（Prompt）**：Kinetis Flash 配置字段偏移（configuration field offset）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_KINETIS_FLASH_CONFIG && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
0x400
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Kinetis Flash 配置字段（flash configuration field）

**配置项引用（Symbol References）**：[`CONFIG_KINETIS_FLASH_CONFIG`](P293_soc_nxp_配置项参考_1.md#CONFIG_KINETIS_FLASH_CONFIG)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_KINETIS_KE1XF_ENABLE_CODE_CACHE"></a>

## 293.70 `CONFIG_KINETIS_KE1XF_ENABLE_CODE_CACHE`

**提示（Prompt）**：代码缓存（Code cache）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_KE1XF && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/kinetis/ke1xf/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/ke1xf/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_LPC54XXX_USB_RAM"></a>

## 293.71 `CONFIG_LPC54XXX_USB_RAM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将 USB 设备栈的端点命令／状态列表（endpoint command/status list）及数据缓冲区链接到专用 USB SRAM。IP3511HS 高速设备控制器只能从此区域访问其数据结构。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_LPC54XXX && CONFIG_SOC_FAMILY_LPC
```

**定义位置（Location）**：[`soc/nxp/lpc/lpc54xxx/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/lpc/lpc54xxx/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_LPC54XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC54XXX)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC54XXX`、`CONFIG_SOC_FAMILY_LPC`。

<a id="CONFIG_LPC55XXX_SRAM_CLOCKS"></a>

## 293.72 `CONFIG_LPC55XXX_SRAM_CLOCKS`

**提示（Prompt）**：为 LPC SRAM 存储体供给时钟（CLock LPC SRAM banks）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_LPC55XXX && CONFIG_SOC_FAMILY_LPC
```

**定义位置（Location）**：[`soc/nxp/lpc/lpc55xxx/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/lpc/lpc55xxx/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_LPC55XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC55XXX)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC55XXX`、`CONFIG_SOC_FAMILY_LPC`。

<a id="CONFIG_MCG_FCRDIV"></a>

## 293.73 `CONFIG_MCG_FCRDIV`

**提示（Prompt）**：快速内部参考时钟分频值（Fast internal reference clock divider）

**说明（Help）**

选择快速内部参考时钟（fast internal reference clock）的分频值。分频后频率必须介于 31.25 kHz 和 4 MHz 之间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCG && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCG`](P293_soc_nxp_配置项参考_1.md#CONFIG_HAS_MCG)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_MCG_FRDIV"></a>

## 293.74 `CONFIG_MCG_FRDIV`

**提示（Prompt）**：锁频环外部参考分频值（FLL external reference divider）

**说明（Help）**

选择锁频环（FLL）外部参考时钟的分频值。分频后频率必须介于 31.25 kHz 和 39.0625 kHz 之间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCG && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCG`](P293_soc_nxp_配置项参考_1.md#CONFIG_HAS_MCG)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_MCG_PRDIV0"></a>

## 293.75 `CONFIG_MCG_PRDIV0`

**提示（Prompt）**：锁相环外部参考分频值（PLL external reference divider）

**说明（Help）**

选择锁相环（PLL）外部参考时钟的分频值。分频后频率必须介于 2 MHz 和 4 MHz 之间。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCG && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0x18]
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCG`](P293_soc_nxp_配置项参考_1.md#CONFIG_HAS_MCG)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_MCG_VDIV0"></a>

## 293.76 `CONFIG_MCG_VDIV0`

**提示（Prompt）**：压控振荡器 0 分频值（VCO 0 divider）

**说明（Help）**

选择 PLL 压控振荡器（VCO）输出的分频值。VDIV 0 位确定应用于参考时钟频率的倍频系数（multiplication factor，M）。译注：原文同时使用“分频”和“倍频系数”两种表述，此处保留，具体含义应结合对应寄存器定义。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCG && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0x1F]
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCG`](P293_soc_nxp_配置项参考_1.md#CONFIG_HAS_MCG)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_MCXC_FLASH_CONFIG"></a>

## 293.77 `CONFIG_MCXC_FLASH_CONFIG`

**提示（Prompt）**：MCXC Flash 配置字段（flash configuration field）

**说明（Help）**

包含 16 字节的 Flash 配置字段（configuration field），用于存储复位时加载的默认保护设置，以及允许 MCU 限制 FTFx 模块访问的安全信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MCXC
```

**默认值（Defaults）**

```text
y if CONFIG_XIP && !CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxc/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxc/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MCXC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXC)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MCXC`。

<a id="CONFIG_MCXE_FLASH_CONFIG"></a>

## 293.78 `CONFIG_MCXE_FLASH_CONFIG`

**提示（Prompt）**：MCXE Flash 配置字段（flash configuration field）

**说明（Help）**

包含 16 字节的 Flash 配置字段（configuration field），用于存储复位时加载的默认保护设置，以及允许 MCU 限制 FTFC 模块访问的安全信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_MCXE24X && CONFIG_SOC_FAMILY_MCXE
```

**默认值（Defaults）**

```text
y if CONFIG_XIP && !CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxe/mcxe24x/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxe/mcxe24x/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_FAMILY_MCXE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXE)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_FAMILY_MCXE`。

<a id="CONFIG_MIPI_DPHY_CLK_SRC"></a>

## 293.79 `CONFIG_MIPI_DPHY_CLK_SRC`

**提示（Prompt）**：MIPI D-PHY 时钟源（Clock source）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT5XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
CONFIG_MIPI_DPHY_CLK_SRC_AUX1_PLL
```

**可选项（Choices）**

```text
CONFIG_MIPI_DPHY_CLK_SRC_AUX1_PLL
CONFIG_MIPI_DPHY_CLK_SRC_FRO
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt5xx/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt5xx/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT5XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT5XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_MIPI_DPHY_CLK_SRC_AUX1_PLL`](P293_soc_nxp_配置项参考_1.md#CONFIG_MIPI_DPHY_CLK_SRC_AUX1_PLL)、[`CONFIG_MIPI_DPHY_CLK_SRC_FRO`](P293_soc_nxp_配置项参考_1.md#CONFIG_MIPI_DPHY_CLK_SRC_FRO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT5XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_MIPI_DPHY_CLK_SRC_AUX1_PLL"></a>

## 293.80 `CONFIG_MIPI_DPHY_CLK_SRC_AUX1_PLL`

**提示（Prompt）**：MIPI_DPHY 时钟源为辅助锁相环 1（AUX1_PLL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DPHY_CLK_SRC>
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt5xx/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt5xx/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MIPI D-PHY 时钟源（Clock source）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DPHY_CLK_SRC`](P293_soc_nxp_配置项参考_1.md#CONFIG_MIPI_DPHY_CLK_SRC)。

<a id="CONFIG_MIPI_DPHY_CLK_SRC_FRO"></a>

## 293.81 `CONFIG_MIPI_DPHY_CLK_SRC_FRO`

**提示（Prompt）**：MIPI_DPHY 时钟源为 FRO 192/96M

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DPHY_CLK_SRC>
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt5xx/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt5xx/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MIPI D-PHY 时钟源（Clock source）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DPHY_CLK_SRC`](P293_soc_nxp_配置项参考_1.md#CONFIG_MIPI_DPHY_CLK_SRC)。

<a id="CONFIG_NXP_FLEXSPI_BOOT_HEADER"></a>

## 293.82 `CONFIG_NXP_FLEXSPI_BOOT_HEADER`

**提示（Prompt）**：启动头部（Boot header）

**说明（Help）**

启用启动 ROM（boot ROM）从外部 Flash 设备启动应用所需的数据结构。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MCXN
```

**默认值（Defaults）**

```text
y if CONFIG_FLASH_MCUX_FLEXSPI_XIP && !CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxn/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxn/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)、[`CONFIG_FLASH_MCUX_FLEXSPI_XIP`](P293_soc_nxp_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_XIP)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MCXN`。

<a id="CONFIG_NXP_FLEXSPI_ROM_RAMLOADER"></a>

## 293.83 `CONFIG_NXP_FLEXSPI_ROM_RAMLOADER`

原库同名定义共 2 条；本项为数据库第 14100 条记录，各定义分别保留。

**提示（Prompt）**：创建 NXP ROM 可从 FlexSPI 加载到 RAM 的输出镜像（output image）

**说明（Help）**

构建一个输出镜像，使启动 ROM（BootROM）能够将其从 FlexSPI 启动设备加载到 RAM 区域。镜像从 FlexSPI 加载到 `zephyr,flash` 节点指定的区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_FLASH_MCUX_FLEXSPI_XIP && CONFIG_NXP_IMXRT_BOOT_HEADER && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**主动选择（Selects）**

```text
CONFIG_BUILD_OUTPUT_HEX
```

**定义位置（Location）**：[`soc/nxp/imxrt/../common/Kconfig.rom_loader:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/../common/Kconfig.rom_loader#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_FLEXSPI_XIP`](P293_soc_nxp_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_XIP)、[`CONFIG_NXP_IMXRT_BOOT_HEADER`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_IMXRT_BOOT_HEADER)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_BUILD_OUTPUT_HEX`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_HEX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_NXP_FLEXSPI_ROM_RAMLOADER--record-14101"></a>

## 293.84 `CONFIG_NXP_FLEXSPI_ROM_RAMLOADER`

原库同名定义共 2 条；本项为数据库第 14101 条记录，各定义分别保留。

**提示（Prompt）**：创建 NXP ROM 可从 FlexSPI 加载到 RAM 的输出镜像（output image）

**说明（Help）**

构建一个输出镜像，使启动 ROM（BootROM）能够将其从 FlexSPI 启动设备加载到 RAM 区域。镜像从 FlexSPI 加载到 `zephyr,flash` 节点指定的区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_FLASH_MCUX_FLEXSPI_XIP && CONFIG_NXP_RW6XX_BOOT_HEADER && CONFIG_SOC_SERIES_RW6XX
```

**主动选择（Selects）**

```text
CONFIG_BUILD_OUTPUT_HEX
```

**定义位置（Location）**：[`soc/nxp/rw/../common/Kconfig.rom_loader:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/rw/../common/Kconfig.rom_loader#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 创建启动头部（Create boot header）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_FLEXSPI_XIP`](P293_soc_nxp_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_XIP)、[`CONFIG_NXP_RW6XX_BOOT_HEADER`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_RW6XX_BOOT_HEADER)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_BUILD_OUTPUT_HEX`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_HEX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_NXP_IMXRT_BOOT_HEADER"></a>

## 293.85 `CONFIG_NXP_IMXRT_BOOT_HEADER`

**提示（Prompt）**：启动头部（Boot header）

**说明（Help）**

启用启动 ROM（boot ROM）从外部 Flash 设备启动应用所需的数据结构。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!(CONFIG_BOOTLOADER_MCUBOOT || CONFIG_SECOND_CORE_MCUX) && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_SECOND_CORE_MCUX`](P294_soc_nxp_配置项参考_2.md#CONFIG_SECOND_CORE_MCUX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_NXP_IMX_EXTERNAL_HYPERRAM"></a>

## 293.86 `CONFIG_NXP_IMX_EXTERNAL_HYPERRAM`

**提示（Prompt）**：允许访问外部 HyperRAM 区域（external HYPERRAM region）

**说明（Help）**

启用对 FlexSPI 管理的外部 HyperRAM 区域的访问。应用使用 HyperRAM 时应启用此设置；否则会定义一个内存保护单元区域（MPU region），禁用对 HyperRAM 地址空间的带缓存访问（cached access）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_NXP_IMX_EXTERNAL_SDRAM"></a>

## 293.87 `CONFIG_NXP_IMX_EXTERNAL_SDRAM`

**提示（Prompt）**：允许访问外部同步动态 RAM 区域（external SDRAM region）

**说明（Help）**

启用对 SEMC 管理的外部 SDRAM 区域的访问。应用使用 SDRAM 时应启用此设置；否则会定义一个内存保护单元区域（MPU region），禁用对 SDRAM 地址空间的带缓存访问（cached access）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_NXP_MCXW7XX_BOOT_HEADER"></a>

## 293.88 `CONFIG_NXP_MCXW7XX_BOOT_HEADER`

**提示（Prompt）**：创建启动头部（Create boot header）

**说明（Help）**

创建启动 ROM（boot ROM）从 Flash 启动应用所需的数据结构。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BOOTLOADER_MCUBOOT && !CONFIG_BUILD_WITH_TFM && CONFIG_SOC_FAMILY_MCXW
```

**被选择（Selected by）**

```text
CONFIG_SOC_MCXW70AC
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxw/mcxw7xx/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxw/mcxw7xx/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_MCXW70AC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW70AC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_MCXW70AC`。

<a id="CONFIG_NXP_NBU"></a>

## 293.89 `CONFIG_NXP_NBU`

原库同名定义共 2 条；本项为数据库第 14143 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP 窄带单元中断初始化（Narrow Band Unit interrupt initialization）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_NBU_ENABLED && CONFIG_SOC_FAMILY_MCXW
```

**默认值（Defaults）**

```text
y if CONFIG_BT || CONFIG_IEEE802154 || CONFIG_NXP_IEEE802154_MAC
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxw/mcxw7xx/../../../common/Kconfig.nbu:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxw/mcxw7xx/../../../common/Kconfig.nbu#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_NXP_IEEE802154_MAC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_NXP_IEEE802154_MAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MCXW`。

<a id="CONFIG_NXP_NBU--record-14144"></a>

## 293.90 `CONFIG_NXP_NBU`

原库同名定义共 2 条；本项为数据库第 14144 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP 窄带单元中断初始化（Narrow Band Unit interrupt initialization）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_NBU_ENABLED && CONFIG_SOC_SERIES_RW6XX
```

**默认值（Defaults）**

```text
y if CONFIG_BT || CONFIG_IEEE802154 || CONFIG_NXP_IEEE802154_MAC
```

**定义位置（Location）**：[`soc/nxp/rw/../common/Kconfig.nbu:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/rw/../common/Kconfig.nbu#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_NXP_IEEE802154_MAC`](P229_modules_hal_nxp_配置项参考.md#CONFIG_NXP_IEEE802154_MAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_NXP_RW6XX_BOOT_HEADER"></a>

## 293.91 `CONFIG_NXP_RW6XX_BOOT_HEADER`

**提示（Prompt）**：创建启动头部（Create boot header）

**说明（Help）**

创建启动 ROM（boot ROM）从外部 Flash 设备启动应用所需的数据结构。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RW6XX
```

**默认值（Defaults）**

```text
y if !CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`soc/nxp/rw/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/rw/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_NXP_S32_ENABLE_CODE_CACHE"></a>

## 293.92 `CONFIG_NXP_S32_ENABLE_CODE_CACHE`

**提示（Prompt）**：代码缓存（Code cache）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX_CACHE && CONFIG_SOC_SERIES_S32K1 && CONFIG_SOC_FAMILY_NXP_S32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/s32/s32k1/Kconfig:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/s32/s32k1/Kconfig#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX_CACHE`](P229_modules_hal_nxp_配置项参考.md#CONFIG_HAS_MCUX_CACHE)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_SOC_FAMILY_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_S32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K1`、`CONFIG_SOC_FAMILY_NXP_S32`。

<a id="CONFIG_NXP_S32_FLASH_CONFIG"></a>

## 293.93 `CONFIG_NXP_S32_FLASH_CONFIG`

**提示（Prompt）**：NXP S32 Flash 配置字段（flash configuration field）

**说明（Help）**

包含 16 字节的 Flash 配置字段（configuration field），用于存储复位时加载的默认保护设置，以及允许 MCU 限制 FTFx 模块访问的安全信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_S32K1 && CONFIG_SOC_FAMILY_NXP_S32
```

**默认值（Defaults）**

```text
y if CONFIG_XIP && !CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`soc/nxp/s32/s32k1/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/s32/s32k1/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_SOC_FAMILY_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_S32)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K1`、`CONFIG_SOC_FAMILY_NXP_S32`。

<a id="CONFIG_NXP_S32_FLASH_CONFIG_FDPROT"></a>

## 293.94 `CONFIG_NXP_S32_FLASH_CONFIG_FDPROT`

**提示（Prompt）**：数据 Flash 保护字节（Data flash protection byte，FDPROT）

**说明（Help）**

为 FlexNVM 器件配置 FDPROT 寄存器的复位值。对于只有程序 Flash 的器件，此字节为保留字节（reserved）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_S32_FLASH_CONFIG && CONFIG_SOC_SERIES_S32K1 && CONFIG_SOC_FAMILY_NXP_S32
```

**默认值（Defaults）**

```text
0xff
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`soc/nxp/s32/s32k1/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/s32/s32k1/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → NXP S32 Flash 配置字段（flash configuration field）

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_FLASH_CONFIG`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_S32_FLASH_CONFIG)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_SOC_FAMILY_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_S32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K1`、`CONFIG_SOC_FAMILY_NXP_S32`。

<a id="CONFIG_NXP_S32_FLASH_CONFIG_FEPROT"></a>

## 293.95 `CONFIG_NXP_S32_FLASH_CONFIG_FEPROT`

**提示（Prompt）**：电可擦可编程只读存储器保护字节（EEPROM protection byte，FEPROT）

**说明（Help）**

为 FlexNVM 器件配置 FEPROT 寄存器的复位值。对于只有程序 Flash 的器件，此字节为保留字节（reserved）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_S32_FLASH_CONFIG && CONFIG_SOC_SERIES_S32K1 && CONFIG_SOC_FAMILY_NXP_S32
```

**默认值（Defaults）**

```text
0xff
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`soc/nxp/s32/s32k1/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/s32/s32k1/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → NXP S32 Flash 配置字段（flash configuration field）

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_FLASH_CONFIG`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_S32_FLASH_CONFIG)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_SOC_FAMILY_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_S32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K1`、`CONFIG_SOC_FAMILY_NXP_S32`。

<a id="CONFIG_NXP_S32_FLASH_CONFIG_FOPT"></a>

## 293.96 `CONFIG_NXP_S32_FLASH_CONFIG_FOPT`

**提示（Prompt）**：Flash 非易失选项字节（Flash nonvolatile option byte，FOPT）

**说明（Help）**

配置 FOPT 寄存器的复位值，其中包含启动（boot）、不可屏蔽中断（NMI）和 EzPort 选项。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_S32_FLASH_CONFIG && CONFIG_SOC_SERIES_S32K1 && CONFIG_SOC_FAMILY_NXP_S32
```

**默认值（Defaults）**

```text
0xff
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`soc/nxp/s32/s32k1/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/s32/s32k1/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → NXP S32 Flash 配置字段（flash configuration field）

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_FLASH_CONFIG`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_S32_FLASH_CONFIG)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_SOC_FAMILY_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_S32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K1`、`CONFIG_SOC_FAMILY_NXP_S32`。

<a id="CONFIG_NXP_S32_FLASH_CONFIG_FSEC"></a>

## 293.97 `CONFIG_NXP_S32_FLASH_CONFIG_FSEC`

**提示（Prompt）**：Flash 安全字节（Flash security byte，FSEC）

**说明（Help）**

配置 FSEC 寄存器的复位值，其中包含后门密钥访问（backdoor key access）、批量擦除（mass erase）、工厂访问（factory access）和 Flash 安全选项。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_S32_FLASH_CONFIG && CONFIG_SOC_SERIES_S32K1 && CONFIG_SOC_FAMILY_NXP_S32
```

**默认值（Defaults）**

```text
0xfe
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`soc/nxp/s32/s32k1/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/s32/s32k1/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → NXP S32 Flash 配置字段（flash configuration field）

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_FLASH_CONFIG`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_S32_FLASH_CONFIG)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_SOC_FAMILY_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_S32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K1`、`CONFIG_SOC_FAMILY_NXP_S32`。

<a id="CONFIG_NXP_S32_FLASH_CONFIG_OFFSET"></a>

## 293.98 `CONFIG_NXP_S32_FLASH_CONFIG_OFFSET`

**提示（Prompt）**：NXP S32 Flash 配置字段偏移（configuration field offset）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_S32_FLASH_CONFIG && CONFIG_SOC_SERIES_S32K1 && CONFIG_SOC_FAMILY_NXP_S32
```

**默认值（Defaults）**

```text
0x400
```

**定义位置（Location）**：[`soc/nxp/s32/s32k1/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/s32/s32k1/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → NXP S32 Flash 配置字段（flash configuration field）

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_FLASH_CONFIG`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_S32_FLASH_CONFIG)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_SOC_FAMILY_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_S32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K1`、`CONFIG_SOC_FAMILY_NXP_S32`。

<a id="CONFIG_NXP_S32_RTU_INDEX"></a>

## 293.99 `CONFIG_NXP_S32_RTU_INDEX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项表示目标实时单元子系统（Real-Time Unit，RTU）的索引。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_S32ZE && CONFIG_SOC_FAMILY_NXP_S32
```

**默认值（Defaults）**

```text
0 if CONFIG_SOC_S32Z270_RTU0
1 if CONFIG_SOC_S32Z270_RTU1
```

**取值范围（Ranges）**

```text
[0, 1]
```

**定义位置（Location）**：[`soc/nxp/s32/s32ze/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/s32/s32ze/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)、[`CONFIG_SOC_FAMILY_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_S32)、[`CONFIG_SOC_S32Z270_RTU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32Z270_RTU0)、[`CONFIG_SOC_S32Z270_RTU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32Z270_RTU1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32ZE`、`CONFIG_SOC_FAMILY_NXP_S32`、`CONFIG_SOC_S32Z270_RTU0`、`CONFIG_SOC_S32Z270_RTU1`。

<a id="CONFIG_OSC_EXTERNAL"></a>

## 293.100 `CONFIG_OSC_EXTERNAL`

**提示（Prompt）**：外部参考时钟（External reference clock）

**说明（Help）**

设置此项以使用振荡器的外部参考时钟模式（external reference clock mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 振荡器模式选择（Oscillator Mode Selection）

<!-- kconfig-navigation -->

[上一章](P292_soc_nuvoton_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P294_soc_nxp_配置项参考_2.md)
