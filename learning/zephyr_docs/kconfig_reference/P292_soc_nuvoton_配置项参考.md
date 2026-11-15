---
id: learning.zephyr-docs.kconfig-reference.page-292
title: "`soc/nuvoton`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第292章\_`soc/nuvoton`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/nuvoton` 的 75 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NPCX_HEADER"></a>

## 292.1 `CONFIG_NPCX_HEADER`

**提示（Prompt）**：带 NPCX 二进制头部的输出文件（output binary with NPCX binary header）

**说明（Help）**

在 NPCX 系列芯片上，NPCX ROM 代码根据固件二进制头部（firmware binary header）的设置，将固件镜像从 Flash 加载到 RAM。启用此项会调用 `ecst`，生成 NPCX 固件头部。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NPCX
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`。

<a id="CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_1"></a>

## 292.2 `CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_1`

**提示（Prompt）**：NPCX SPI 时钟比为 1（SPI clock ratio）

**说明（Help）**

SPI Flash 时钟与内核时钟（core clock）频率相同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → 内核时钟与 SPI Flash 时钟的比值（Core clock to SPI flash clock ratio）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_CHOICE)。

<a id="CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_2"></a>

## 292.3 `CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_2`

**提示（Prompt）**：NPCX SPI 时钟比为 2（SPI clock ratio）

**说明（Help）**

内核时钟频率（core clock frequency）是 Flash 时钟频率的两倍。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → 内核时钟与 SPI Flash 时钟的比值（Core clock to SPI flash clock ratio）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_CHOICE)。

<a id="CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_CHOICE"></a>

## 292.4 `CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_CHOICE`

**提示（Prompt）**：内核时钟与 SPI Flash 时钟的比值（Core clock to SPI flash clock ratio）

**说明（Help）**

设置时钟比（clock ratio），即内核时钟／SPI 时钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NPCX_HEADER && CONFIG_SOC_FAMILY_NPCX
```

**默认值（Defaults）**

```text
CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_1
```

**可选项（Choices）**

```text
CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_1
CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_2
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER)、[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)、[`CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_1`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_1)、[`CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_2`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_CORE_CLOCK_SPI_CLOCK_RATIO_2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`。

<a id="CONFIG_NPCX_HEADER_ENABLE_FIRMWARE_CRC"></a>

## 292.5 `CONFIG_NPCX_HEADER_ENABLE_FIRMWARE_CRC`

**提示（Prompt）**：固件镜像循环冗余校验（Firmware image CRC check）

**说明（Help）**

启用后，启动时使用循环冗余校验和（CRC checksum）验证固件镜像。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NPCX_HEADER && CONFIG_SOC_FAMILY_NPCX
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER)、[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`。

<a id="CONFIG_NPCX_HEADER_ENABLE_HEADER_CRC"></a>

## 292.6 `CONFIG_NPCX_HEADER_ENABLE_HEADER_CRC`

**提示（Prompt）**：头部循环冗余校验（Header CRC check）

**说明（Help）**

启用后，启动时使用循环冗余校验和（CRC checksum）验证头部。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NPCX_HEADER && CONFIG_SOC_FAMILY_NPCX
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER)、[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`。

<a id="CONFIG_NPCX_HEADER_FLASH_SIZE_0P5M_1M"></a>

## 292.7 `CONFIG_NPCX_HEADER_FLASH_SIZE_0P5M_1M`

**提示（Prompt）**：SPI Flash 大小为 0.5M 或 1M 字节（Bytes）

**说明（Help）**

SPI Flash 大小为 0.5M 或 1M 字节（Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE)。

<a id="CONFIG_NPCX_HEADER_FLASH_SIZE_16M"></a>

## 292.8 `CONFIG_NPCX_HEADER_FLASH_SIZE_16M`

**提示（Prompt）**：SPI Flash 大小为 16M 字节（16M Bytes）

**说明（Help）**

SPI Flash 大小为 16M 字节（16M Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE)。

<a id="CONFIG_NPCX_HEADER_FLASH_SIZE_2M"></a>

## 292.9 `CONFIG_NPCX_HEADER_FLASH_SIZE_2M`

**提示（Prompt）**：SPI Flash 大小为 2M 字节（2M Bytes）

**说明（Help）**

SPI Flash 大小为 2M 字节（2M Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE)。

<a id="CONFIG_NPCX_HEADER_FLASH_SIZE_4M"></a>

## 292.10 `CONFIG_NPCX_HEADER_FLASH_SIZE_4M`

**提示（Prompt）**：SPI Flash 大小为 4M 字节（4M Bytes）

**说明（Help）**

SPI Flash 大小为 4M 字节（4M Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L156)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE)。

<a id="CONFIG_NPCX_HEADER_FLASH_SIZE_8M"></a>

## 292.11 `CONFIG_NPCX_HEADER_FLASH_SIZE_8M`

**提示（Prompt）**：SPI Flash 大小为 8M 字节（8M Bytes）

**说明（Help）**

SPI Flash 大小为 8M 字节（8M Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE)。

<a id="CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE"></a>

## 292.12 `CONFIG_NPCX_HEADER_FLASH_SIZE_CHOICE`

**提示（Prompt）**：Flash 大小（Flash size）

**说明（Help）**

设置 SPI Flash 的大小（size）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NPCX_HEADER && CONFIG_SOC_FAMILY_NPCX
```

**默认值（Defaults）**

```text
CONFIG_NPCX_HEADER_FLASH_SIZE_0P5M_1M if CONFIG_SOC_SERIES_NPCX7 || CONFIG_SOC_SERIES_NPCX9 || CONFIG_SOC_SERIES_NPCK3
CONFIG_NPCX_HEADER_FLASH_SIZE_16M
```

**可选项（Choices）**

```text
CONFIG_NPCX_HEADER_FLASH_SIZE_0P5M_1M
CONFIG_NPCX_HEADER_FLASH_SIZE_2M
CONFIG_NPCX_HEADER_FLASH_SIZE_4M
CONFIG_NPCX_HEADER_FLASH_SIZE_8M
CONFIG_NPCX_HEADER_FLASH_SIZE_16M
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER)、[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)、[`CONFIG_NPCX_HEADER_FLASH_SIZE_0P5M_1M`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_FLASH_SIZE_0P5M_1M)、[`CONFIG_SOC_SERIES_NPCX7`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX7)、[`CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX9)、[`CONFIG_SOC_SERIES_NPCK3`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCK3)、[`CONFIG_NPCX_HEADER_FLASH_SIZE_16M`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_FLASH_SIZE_16M)、[`CONFIG_NPCX_HEADER_FLASH_SIZE_2M`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_FLASH_SIZE_2M)、[`CONFIG_NPCX_HEADER_FLASH_SIZE_4M`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_FLASH_SIZE_4M)、[`CONFIG_NPCX_HEADER_FLASH_SIZE_8M`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_FLASH_SIZE_8M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`。

<a id="CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_20"></a>

## 292.13 `CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_20`

**提示（Prompt）**：SPI Flash 最大时钟速率为 20 MHz（max clock rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → SPI Flash 使用的时钟速率（Clock rate）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE)。

<a id="CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_25"></a>

## 292.14 `CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_25`

**提示（Prompt）**：SPI Flash 最大时钟速率为 25 MHz（max clock rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → SPI Flash 使用的时钟速率（Clock rate）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE)。

<a id="CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_33"></a>

## 292.15 `CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_33`

**提示（Prompt）**：SPI Flash 最大时钟速率为 33 MHz（max clock rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_NPCX9 && <choice CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → SPI Flash 使用的时钟速率（Clock rate）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX9)、[`CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE)。

<a id="CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_40"></a>

## 292.16 `CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_40`

**提示（Prompt）**：SPI Flash 最大时钟速率为 40 MHz（max clock rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → SPI Flash 使用的时钟速率（Clock rate）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE)。

<a id="CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_50"></a>

## 292.17 `CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_50`

**提示（Prompt）**：SPI Flash 最大时钟速率为 50 MHz（max clock rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → SPI Flash 使用的时钟速率（Clock rate）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE)。

<a id="CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE"></a>

## 292.18 `CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_CHOICE`

**提示（Prompt）**：SPI Flash 使用的时钟速率（Clock rate）

**说明（Help）**

选择将固件二进制文件从 Flash 加载到 RAM 时使用的最大时钟速率（max clock rate）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NPCX_HEADER && CONFIG_SOC_FAMILY_NPCX
```

**默认值（Defaults）**

```text
CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_20
```

**可选项（Choices）**

```text
CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_20
CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_25
CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_33
CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_40
CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_50
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER)、[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)、[`CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_20`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_20)、[`CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_25`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_25)、[`CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_33`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_33)、[`CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_40`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_40)、[`CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_50`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_MAX_CLOCK_50)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`。

<a id="CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE"></a>

## 292.19 `CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE`

**提示（Prompt）**：SPI Flash 使用的读取模式（Reading mode）

**说明（Help）**

设置 SPI Flash 可使用的读取模式（reading mode）。支持普通（normal）、快速（fast）、双线（dual）和四线（quad）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NPCX_HEADER && CONFIG_SOC_FAMILY_NPCX
```

**默认值（Defaults）**

```text
CONFIG_NPCX_HEADER_SPI_READ_MODE_NORMAL
```

**可选项（Choices）**

```text
CONFIG_NPCX_HEADER_SPI_READ_MODE_NORMAL
CONFIG_NPCX_HEADER_SPI_READ_MODE_FAST
CONFIG_NPCX_HEADER_SPI_READ_MODE_DUAL
CONFIG_NPCX_HEADER_SPI_READ_MODE_QUAD
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER)、[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)、[`CONFIG_NPCX_HEADER_SPI_READ_MODE_NORMAL`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_READ_MODE_NORMAL)、[`CONFIG_NPCX_HEADER_SPI_READ_MODE_FAST`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_READ_MODE_FAST)、[`CONFIG_NPCX_HEADER_SPI_READ_MODE_DUAL`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_READ_MODE_DUAL)、[`CONFIG_NPCX_HEADER_SPI_READ_MODE_QUAD`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_READ_MODE_QUAD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`。

<a id="CONFIG_NPCX_HEADER_SPI_READ_MODE_DUAL"></a>

## 292.20 `CONFIG_NPCX_HEADER_SPI_READ_MODE_DUAL`

**提示（Prompt）**：SPI Flash 使用双线读取模式（dual reading mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → SPI Flash 使用的读取模式（Reading mode）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE)。

<a id="CONFIG_NPCX_HEADER_SPI_READ_MODE_FAST"></a>

## 292.21 `CONFIG_NPCX_HEADER_SPI_READ_MODE_FAST`

**提示（Prompt）**：SPI Flash 使用快速读取模式（fast reading mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → SPI Flash 使用的读取模式（Reading mode）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE)。

<a id="CONFIG_NPCX_HEADER_SPI_READ_MODE_NORMAL"></a>

## 292.22 `CONFIG_NPCX_HEADER_SPI_READ_MODE_NORMAL`

**提示（Prompt）**：SPI Flash 使用普通读取模式（normal reading mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → SPI Flash 使用的读取模式（Reading mode）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE)。

<a id="CONFIG_NPCX_HEADER_SPI_READ_MODE_QUAD"></a>

## 292.23 `CONFIG_NPCX_HEADER_SPI_READ_MODE_QUAD`

**提示（Prompt）**：SPI Flash 使用四线读取模式（quad reading mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE>
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → SPI Flash 使用的读取模式（Reading mode）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER_SPI_READ_MODE_CHOICE)。

<a id="CONFIG_NPCX_IMAGE_OUTPUT_BIN"></a>

## 292.24 `CONFIG_NPCX_IMAGE_OUTPUT_BIN`

**提示（Prompt）**：以 BIN 格式构建 NPCX 二进制文件（BIN format）

**说明（Help）**

在构建目录中生成原始二进制文件（raw binary）`zephyr/zephyr.npcx.bin`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NPCX_HEADER && CONFIG_SOC_FAMILY_NPCX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_HEADER`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER)、[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`。

<a id="CONFIG_NPCX_IMAGE_OUTPUT_HEX"></a>

## 292.25 `CONFIG_NPCX_IMAGE_OUTPUT_HEX`

**提示（Prompt）**：以 HEX 格式构建 NPCX 二进制文件（HEX format）

**说明（Help）**

在构建目录中生成 HEX 文件 `zephyr/zephyr.npcx.hex`，由 NPCX BIN 镜像转换而来。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NPCX_IMAGE_OUTPUT_BIN && CONFIG_NPCX_HEADER && CONFIG_SOC_FAMILY_NPCX
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 带 NPCX 二进制头部的输出文件（output binary with NPCX binary header） → 以 BIN 格式构建 NPCX 二进制文件（BIN format）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_IMAGE_OUTPUT_BIN`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_IMAGE_OUTPUT_BIN)、[`CONFIG_NPCX_HEADER`](P292_soc_nuvoton_配置项参考.md#CONFIG_NPCX_HEADER)、[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`。

<a id="CONFIG_NPCX_PM_TRACE"></a>

## 292.26 `CONFIG_NPCX_PM_TRACE`

**提示（Prompt）**：跟踪 NPCX 家族的系统电源管理（Trace System Power Management）

**说明（Help）**

启用运行时电源管理跟踪（runtime power management traces）的内部配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && CONFIG_SOC_FAMILY_NPCX
```

**定义位置（Location）**：[`soc/nuvoton/npcx/Kconfig:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/Kconfig#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`。

<a id="CONFIG_NPCX_VCC1_RST_HANG_WORKAROUND"></a>

## 292.27 `CONFIG_NPCX_VCC1_RST_HANG_WORKAROUND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

规避 npcx9m7fb SoC 勘误中的“VCC1_RST 复位后可能挂起”问题（Possible Hang-Up After VCC1_RST Reset）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NPCX9M7FB
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NPCX9M7FB`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCX9M7FB)。

<a id="CONFIG_SOC_NPCK3M8K"></a>

## 292.28 `CONFIG_SOC_NPCK3M8K`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCK3M8K 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NPCK3
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NPCK3M8K_EVB
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npck3/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npck3/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCK3`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCK3)、[`CONFIG_BOARD_NPCK3M8K_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NPCK3M8K_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NPCK3M8K_EVB`。

<a id="CONFIG_SOC_NPCK_DEBUG_DISABLE"></a>

## 292.29 `CONFIG_SOC_NPCK_DEBUG_DISABLE`

**提示（Prompt）**：禁用全部 K3 调试接口（debug interfaces）

**说明（Help）**

初始化期间禁用全部 K3 调试接口（debug interfaces）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NPCK3
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npck3/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npck3/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCK3`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCK3)。

<a id="CONFIG_SOC_NPCK_EPURST_DISABLE"></a>

## 292.30 `CONFIG_SOC_NPCK_EPURST_DISABLE`

**提示（Prompt）**：禁用全部外部上电复位输入（External Power-Up Reset Inputs）

**说明（Help）**

初始化期间禁用全部外部上电复位输入（External Power-Up Reset Inputs）。EXT_PURST# 等所有信号默认禁用，用户可按需要启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NPCK3
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npck3/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npck3/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCK3`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCK3)。

<a id="CONFIG_SOC_NPCX4M3F"></a>

## 292.31 `CONFIG_SOC_NPCX4M3F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX4M3F 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NPCX4
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx4/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx4/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCX4`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX4)。

<a id="CONFIG_SOC_NPCX4M8F"></a>

## 292.32 `CONFIG_SOC_NPCX4M8F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX4M8F 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NPCX4
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NPCX4M8F_EVB
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx4/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx4/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCX4`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX4)、[`CONFIG_BOARD_NPCX4M8F_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NPCX4M8F_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NPCX4M8F_EVB`。

<a id="CONFIG_SOC_NPCX7M6FB"></a>

## 292.33 `CONFIG_SOC_NPCX7M6FB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX7M6FB 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NPCX7
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NPCX7M6FB_EVB
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx7/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx7/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCX7`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX7)、[`CONFIG_BOARD_NPCX7M6FB_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NPCX7M6FB_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NPCX7M6FB_EVB`。

<a id="CONFIG_SOC_NPCX7M6FC"></a>

## 292.34 `CONFIG_SOC_NPCX7M6FC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX7M6FC 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NPCX7
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx7/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx7/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCX7`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX7)。

<a id="CONFIG_SOC_NPCX7M7FC"></a>

## 292.35 `CONFIG_SOC_NPCX7M7FC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX7M7FC 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NPCX7
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx7/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx7/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCX7`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX7)。

<a id="CONFIG_SOC_NPCX9M3F"></a>

## 292.36 `CONFIG_SOC_NPCX9M3F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX9M3F 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NPCX9
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX9)。

<a id="CONFIG_SOC_NPCX9M6F"></a>

## 292.37 `CONFIG_SOC_NPCX9M6F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX9M6F 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NPCX9
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NPCX9M6F_EVB
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX9)、[`CONFIG_BOARD_NPCX9M6F_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NPCX9M6F_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NPCX9M6F_EVB`。

<a id="CONFIG_SOC_NPCX9M7F"></a>

## 292.38 `CONFIG_SOC_NPCX9M7F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX9M7F 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NPCX9
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX9)。

<a id="CONFIG_SOC_NPCX9M7FB"></a>

## 292.39 `CONFIG_SOC_NPCX9M7FB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX9M7FB 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NPCX9
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig.soc:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig.soc#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX9)。

<a id="CONFIG_SOC_NPCX9MFP"></a>

## 292.40 `CONFIG_SOC_NPCX9MFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX9MFP 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NPCX9
```

**被选择（Selected by）**

```text
CONFIG_BOARD_GOOGLE_QUINCY
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig.soc:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig.soc#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_SERIES_NPCX9)、[`CONFIG_BOARD_GOOGLE_QUINCY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_GOOGLE_QUINCY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_GOOGLE_QUINCY`。

<a id="CONFIG_SOC_SERIES_M031X"></a>

## 292.41 `CONFIG_SOC_SERIES_M031X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M031X 微控制器系列支持（Nuvoton MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NUMAKER
```

**被选择（Selected by）**

```text
CONFIG_SOC_M031XXX
```

**定义位置（Location）**：[`soc/nuvoton/numaker/m031x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numaker/m031x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NUMAKER)、[`CONFIG_SOC_M031XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_M031XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NUMAKER`、`CONFIG_SOC_M031XXX`。

<a id="CONFIG_SOC_SERIES_M2L31X"></a>

## 292.42 `CONFIG_SOC_SERIES_M2L31X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M2L31X 微控制器系列支持（Nuvoton MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NUMAKER
```

**被选择（Selected by）**

```text
CONFIG_SOC_M2L31XXX
```

**定义位置（Location）**：[`soc/nuvoton/numaker/m2l31x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numaker/m2l31x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NUMAKER)、[`CONFIG_SOC_M2L31XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_M2L31XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NUMAKER`、`CONFIG_SOC_M2L31XXX`。

<a id="CONFIG_SOC_SERIES_M333X"></a>

## 292.43 `CONFIG_SOC_SERIES_M333X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M333X 微控制器系列支持（Nuvoton MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NUMAKER
```

**被选择（Selected by）**

```text
CONFIG_SOC_M333XXX
```

**定义位置（Location）**：[`soc/nuvoton/numaker/m333x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numaker/m333x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NUMAKER)、[`CONFIG_SOC_M333XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_M333XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NUMAKER`、`CONFIG_SOC_M333XXX`。

<a id="CONFIG_SOC_SERIES_M335X"></a>

## 292.44 `CONFIG_SOC_SERIES_M335X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M335X 微控制器系列支持（Nuvoton MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NUMAKER
```

**被选择（Selected by）**

```text
CONFIG_SOC_M335XXX
```

**定义位置（Location）**：[`soc/nuvoton/numaker/m335x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numaker/m335x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NUMAKER)、[`CONFIG_SOC_M335XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_M335XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NUMAKER`、`CONFIG_SOC_M335XXX`。

<a id="CONFIG_SOC_SERIES_M46X"></a>

## 292.45 `CONFIG_SOC_SERIES_M46X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M46X 微控制器系列支持（Nuvoton MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NUMAKER
```

**被选择（Selected by）**

```text
CONFIG_SOC_M467
```

**定义位置（Location）**：[`soc/nuvoton/numaker/m46x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numaker/m46x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NUMAKER)、[`CONFIG_SOC_M467`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_M467)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NUMAKER`、`CONFIG_SOC_M467`。

<a id="CONFIG_SOC_SERIES_M48X"></a>

## 292.46 `CONFIG_SOC_SERIES_M48X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M48X 微控制器系列支持（NUVOTON MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NUMICRO
```

**被选择（Selected by）**

```text
CONFIG_SOC_M487
```

**定义位置（Location）**：[`soc/nuvoton/numicro/m48x/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numicro/m48x/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NUMICRO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NUMICRO)、[`CONFIG_SOC_M487`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_M487)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NUMICRO`、`CONFIG_SOC_M487`。

<a id="CONFIG_SOC_SERIES_M55M1X"></a>

## 292.47 `CONFIG_SOC_SERIES_M55M1X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M55M1X 微控制器系列支持（Nuvoton MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NUMAKER
```

**被选择（Selected by）**

```text
CONFIG_SOC_M55M1XXX
```

**定义位置（Location）**：[`soc/nuvoton/numaker/m55m1x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numaker/m55m1x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NUMAKER)、[`CONFIG_SOC_M55M1XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_M55M1XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NUMAKER`、`CONFIG_SOC_M55M1XXX`。

<a id="CONFIG_SOC_SERIES_NPCK3"></a>

## 292.48 `CONFIG_SOC_SERIES_NPCK3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 NPCK3 系列支持（Nuvoton series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_NPCX_SOC_VARIANT_NPCKN
```

**被选择（Selected by）**

```text
CONFIG_SOC_NPCK3M8K
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npck3/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npck3/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_SOC_VARIANT_NPCKN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NPCX_SOC_VARIANT_NPCKN)、[`CONFIG_SOC_NPCK3M8K`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCK3M8K)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NPCX_SOC_VARIANT_NPCKN`。

<a id="CONFIG_SOC_SERIES_NPCM4"></a>

## 292.49 `CONFIG_SOC_SERIES_NPCM4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 NPCM4 系列支持（Nuvoton series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NPCM
```

**被选择（Selected by）**

```text
CONFIG_SOC_NPCM400
```

**定义位置（Location）**：[`soc/nuvoton/npcm/npcm4/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcm/npcm4/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NPCM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCM)、[`CONFIG_SOC_NPCM400`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NPCM400)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCM`、`CONFIG_SOC_NPCM400`。

<a id="CONFIG_SOC_SERIES_NPCX4"></a>

## 292.50 `CONFIG_SOC_SERIES_NPCX4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 NPCX4 系列支持（Nuvoton series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_NPCX_SOC_VARIANT_NPCXN
```

**被选择（Selected by）**

```text
CONFIG_SOC_NPCX4M3F
CONFIG_SOC_NPCX4M8F
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx4/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx4/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_SOC_VARIANT_NPCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NPCX_SOC_VARIANT_NPCXN)、[`CONFIG_SOC_NPCX4M3F`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCX4M3F)、[`CONFIG_SOC_NPCX4M8F`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCX4M8F)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NPCX_SOC_VARIANT_NPCXN`。

<a id="CONFIG_SOC_SERIES_NPCX7"></a>

## 292.51 `CONFIG_SOC_SERIES_NPCX7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 NPCX7 系列支持（Nuvoton series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_NPCX_SOC_VARIANT_NPCXN
```

**被选择（Selected by）**

```text
CONFIG_SOC_NPCX7M6FB
CONFIG_SOC_NPCX7M6FC
CONFIG_SOC_NPCX7M7FC
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx7/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx7/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_SOC_VARIANT_NPCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NPCX_SOC_VARIANT_NPCXN)、[`CONFIG_SOC_NPCX7M6FB`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCX7M6FB)、[`CONFIG_SOC_NPCX7M6FC`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCX7M6FC)、[`CONFIG_SOC_NPCX7M7FC`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCX7M7FC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NPCX_SOC_VARIANT_NPCXN`。

<a id="CONFIG_SOC_SERIES_NPCX9"></a>

## 292.52 `CONFIG_SOC_SERIES_NPCX9`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 NPCX9 系列支持（Nuvoton series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_NPCX_SOC_VARIANT_NPCXN
```

**被选择（Selected by）**

```text
CONFIG_SOC_NPCX9M3F
CONFIG_SOC_NPCX9M6F
CONFIG_SOC_NPCX9M7F
CONFIG_SOC_NPCX9M7FB
CONFIG_SOC_NPCX9MFP
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_NPCX_SOC_VARIANT_NPCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NPCX_SOC_VARIANT_NPCXN)、[`CONFIG_SOC_NPCX9M3F`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCX9M3F)、[`CONFIG_SOC_NPCX9M6F`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCX9M6F)、[`CONFIG_SOC_NPCX9M7F`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCX9M7F)、[`CONFIG_SOC_NPCX9M7FB`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCX9M7FB)、[`CONFIG_SOC_NPCX9MFP`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCX9MFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NPCX_SOC_VARIANT_NPCXN`。

<a id="SB_CONFIG_SOC_NPCK3M8K"></a>

## 292.53 `SB_CONFIG_SOC_NPCK3M8K`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCK3M8K 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NPCK3
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NPCK3M8K_EVB
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npck3/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npck3/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NPCK3`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_SERIES_NPCK3)、[`SB_CONFIG_BOARD_NPCK3M8K_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NPCK3M8K_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NPCK3M8K_EVB`。

<a id="SB_CONFIG_SOC_NPCX4M3F"></a>

## 292.54 `SB_CONFIG_SOC_NPCX4M3F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX4M3F 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NPCX4
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx4/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx4/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NPCX4`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_SERIES_NPCX4)。

<a id="SB_CONFIG_SOC_NPCX4M8F"></a>

## 292.55 `SB_CONFIG_SOC_NPCX4M8F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX4M8F 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NPCX4
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NPCX4M8F_EVB
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx4/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx4/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NPCX4`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_SERIES_NPCX4)、[`SB_CONFIG_BOARD_NPCX4M8F_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NPCX4M8F_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NPCX4M8F_EVB`。

<a id="SB_CONFIG_SOC_NPCX7M6FB"></a>

## 292.56 `SB_CONFIG_SOC_NPCX7M6FB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX7M6FB 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NPCX7
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NPCX7M6FB_EVB
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx7/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx7/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NPCX7`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_SERIES_NPCX7)、[`SB_CONFIG_BOARD_NPCX7M6FB_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NPCX7M6FB_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NPCX7M6FB_EVB`。

<a id="SB_CONFIG_SOC_NPCX7M6FC"></a>

## 292.57 `SB_CONFIG_SOC_NPCX7M6FC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX7M6FC 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NPCX7
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx7/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx7/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NPCX7`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_SERIES_NPCX7)。

<a id="SB_CONFIG_SOC_NPCX7M7FC"></a>

## 292.58 `SB_CONFIG_SOC_NPCX7M7FC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX7M7FC 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NPCX7
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx7/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx7/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NPCX7`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_SERIES_NPCX7)。

<a id="SB_CONFIG_SOC_NPCX9M3F"></a>

## 292.59 `SB_CONFIG_SOC_NPCX9M3F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX9M3F 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NPCX9
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_SERIES_NPCX9)。

<a id="SB_CONFIG_SOC_NPCX9M6F"></a>

## 292.60 `SB_CONFIG_SOC_NPCX9M6F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX9M6F 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NPCX9
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NPCX9M6F_EVB
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_SERIES_NPCX9)、[`SB_CONFIG_BOARD_NPCX9M6F_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NPCX9M6F_EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NPCX9M6F_EVB`。

<a id="SB_CONFIG_SOC_NPCX9M7F"></a>

## 292.61 `SB_CONFIG_SOC_NPCX9M7F`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX9M7F 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NPCX9
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_SERIES_NPCX9)。

<a id="SB_CONFIG_SOC_NPCX9M7FB"></a>

## 292.62 `SB_CONFIG_SOC_NPCX9M7FB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX9M7FB 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NPCX9
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig.soc:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig.soc#L30)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_SERIES_NPCX9)。

<a id="SB_CONFIG_SOC_NPCX9MFP"></a>

## 292.63 `SB_CONFIG_SOC_NPCX9MFP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NPCX9MFP 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NPCX9
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_GOOGLE_QUINCY
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig.soc:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig.soc#L36)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NPCX9`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_SERIES_NPCX9)、[`SB_CONFIG_BOARD_GOOGLE_QUINCY`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_GOOGLE_QUINCY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_GOOGLE_QUINCY`。

<a id="SB_CONFIG_SOC_SERIES_M031X"></a>

## 292.64 `SB_CONFIG_SOC_SERIES_M031X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M031X 微控制器系列支持（Nuvoton MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NUMAKER
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_M031XXX
```

**定义位置（Location）**：[`soc/nuvoton/numaker/m031x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numaker/m031x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NUMAKER)、[`SB_CONFIG_SOC_M031XXX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_M031XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NUMAKER`、`SB_CONFIG_SOC_M031XXX`。

<a id="SB_CONFIG_SOC_SERIES_M2L31X"></a>

## 292.65 `SB_CONFIG_SOC_SERIES_M2L31X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M2L31X 微控制器系列支持（Nuvoton MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NUMAKER
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_M2L31XXX
```

**定义位置（Location）**：[`soc/nuvoton/numaker/m2l31x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numaker/m2l31x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NUMAKER)、[`SB_CONFIG_SOC_M2L31XXX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_M2L31XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NUMAKER`、`SB_CONFIG_SOC_M2L31XXX`。

<a id="SB_CONFIG_SOC_SERIES_M333X"></a>

## 292.66 `SB_CONFIG_SOC_SERIES_M333X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M333X 微控制器系列支持（Nuvoton MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NUMAKER
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_M333XXX
```

**定义位置（Location）**：[`soc/nuvoton/numaker/m333x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numaker/m333x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NUMAKER)、[`SB_CONFIG_SOC_M333XXX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_M333XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NUMAKER`、`SB_CONFIG_SOC_M333XXX`。

<a id="SB_CONFIG_SOC_SERIES_M335X"></a>

## 292.67 `SB_CONFIG_SOC_SERIES_M335X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M335X 微控制器系列支持（Nuvoton MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NUMAKER
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_M335XXX
```

**定义位置（Location）**：[`soc/nuvoton/numaker/m335x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numaker/m335x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NUMAKER)、[`SB_CONFIG_SOC_M335XXX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_M335XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NUMAKER`、`SB_CONFIG_SOC_M335XXX`。

<a id="SB_CONFIG_SOC_SERIES_M46X"></a>

## 292.68 `SB_CONFIG_SOC_SERIES_M46X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M46X 微控制器系列支持（Nuvoton MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NUMAKER
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_M467
```

**定义位置（Location）**：[`soc/nuvoton/numaker/m46x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numaker/m46x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NUMAKER)、[`SB_CONFIG_SOC_M467`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_M467)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NUMAKER`、`SB_CONFIG_SOC_M467`。

<a id="SB_CONFIG_SOC_SERIES_M48X"></a>

## 292.69 `SB_CONFIG_SOC_SERIES_M48X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M48X 微控制器系列支持（NUVOTON MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NUMICRO
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_M487
```

**定义位置（Location）**：[`soc/nuvoton/numicro/m48x/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numicro/m48x/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NUMICRO`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NUMICRO)、[`SB_CONFIG_SOC_M487`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_M487)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NUMICRO`、`SB_CONFIG_SOC_M487`。

<a id="SB_CONFIG_SOC_SERIES_M55M1X"></a>

## 292.70 `SB_CONFIG_SOC_SERIES_M55M1X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 M55M1X 微控制器系列支持（Nuvoton MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NUMAKER
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_M55M1XXX
```

**定义位置（Location）**：[`soc/nuvoton/numaker/m55m1x/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/numaker/m55m1x/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NUMAKER)、[`SB_CONFIG_SOC_M55M1XXX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_M55M1XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NUMAKER`、`SB_CONFIG_SOC_M55M1XXX`。

<a id="SB_CONFIG_SOC_SERIES_NPCK3"></a>

## 292.71 `SB_CONFIG_SOC_SERIES_NPCK3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 NPCK3 系列支持（Nuvoton series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_NPCX_SOC_VARIANT_NPCKN
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NPCK3M8K
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npck3/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npck3/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_NPCX_SOC_VARIANT_NPCKN`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_NPCX_SOC_VARIANT_NPCKN)、[`SB_CONFIG_SOC_NPCK3M8K`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_NPCK3M8K)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_NPCX_SOC_VARIANT_NPCKN`。

<a id="SB_CONFIG_SOC_SERIES_NPCM4"></a>

## 292.72 `SB_CONFIG_SOC_SERIES_NPCM4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 NPCM4 系列支持（Nuvoton series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NPCM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NPCM400
```

**定义位置（Location）**：[`soc/nuvoton/npcm/npcm4/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcm/npcm4/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NPCM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NPCM)、[`SB_CONFIG_SOC_NPCM400`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NPCM400)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NPCM`、`SB_CONFIG_SOC_NPCM400`。

<a id="SB_CONFIG_SOC_SERIES_NPCX4"></a>

## 292.73 `SB_CONFIG_SOC_SERIES_NPCX4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 NPCX4 系列支持（Nuvoton series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_NPCX_SOC_VARIANT_NPCXN
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NPCX4M3F
SB_CONFIG_SOC_NPCX4M8F
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx4/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx4/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_NPCX_SOC_VARIANT_NPCXN`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_NPCX_SOC_VARIANT_NPCXN)、[`SB_CONFIG_SOC_NPCX4M3F`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_NPCX4M3F)、[`SB_CONFIG_SOC_NPCX4M8F`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_NPCX4M8F)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_NPCX_SOC_VARIANT_NPCXN`。

<a id="SB_CONFIG_SOC_SERIES_NPCX7"></a>

## 292.74 `SB_CONFIG_SOC_SERIES_NPCX7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 NPCX7 系列支持（Nuvoton series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_NPCX_SOC_VARIANT_NPCXN
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NPCX7M6FB
SB_CONFIG_SOC_NPCX7M6FC
SB_CONFIG_SOC_NPCX7M7FC
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx7/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx7/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_NPCX_SOC_VARIANT_NPCXN`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_NPCX_SOC_VARIANT_NPCXN)、[`SB_CONFIG_SOC_NPCX7M6FB`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_NPCX7M6FB)、[`SB_CONFIG_SOC_NPCX7M6FC`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_NPCX7M6FC)、[`SB_CONFIG_SOC_NPCX7M7FC`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_NPCX7M7FC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_NPCX_SOC_VARIANT_NPCXN`。

<a id="SB_CONFIG_SOC_SERIES_NPCX9"></a>

## 292.75 `SB_CONFIG_SOC_SERIES_NPCX9`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用新唐 NPCX9 系列支持（Nuvoton series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_NPCX_SOC_VARIANT_NPCXN
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NPCX9M3F
SB_CONFIG_SOC_NPCX9M6F
SB_CONFIG_SOC_NPCX9M7F
SB_CONFIG_SOC_NPCX9M7FB
SB_CONFIG_SOC_NPCX9MFP
```

**定义位置（Location）**：[`soc/nuvoton/npcx/npcx9/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nuvoton/npcx/npcx9/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_NPCX_SOC_VARIANT_NPCXN`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_NPCX_SOC_VARIANT_NPCXN)、[`SB_CONFIG_SOC_NPCX9M3F`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_NPCX9M3F)、[`SB_CONFIG_SOC_NPCX9M6F`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_NPCX9M6F)、[`SB_CONFIG_SOC_NPCX9M7F`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_NPCX9M7F)、[`SB_CONFIG_SOC_NPCX9M7FB`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_NPCX9M7FB)、[`SB_CONFIG_SOC_NPCX9MFP`](P292_soc_nuvoton_配置项参考.md#SB_CONFIG_SOC_NPCX9MFP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_NPCX_SOC_VARIANT_NPCXN`。

<!-- kconfig-navigation -->

[上一章](P291_soc_nordic_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P293_soc_nxp_配置项参考_1.md)
