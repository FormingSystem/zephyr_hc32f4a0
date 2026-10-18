---
id: learning.zephyr-docs.kconfig-reference.page-420
title: "`subsys/sd`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第420章\_`subsys/sd`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/sd` 的 14 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MMC_RCA"></a>

## 420.1 `CONFIG_MMC_RCA`

**提示（Prompt）**：MMC 相对卡地址（Relative Card Address）

**说明（Help）**

向多媒体卡（MMC）公布的相对卡地址（Relative Card Address）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SD_STACK
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/sd/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_SD_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SD_STACK)。

<a id="CONFIG_MMC_STACK"></a>

## 420.2 `CONFIG_MMC_STACK`

**提示（Prompt）**：多媒体卡（MMC）协议支持

**说明（Help）**

启用多媒体卡（MMC）协议支持，这是嵌入式多媒体卡（eMMC）正常工作所必需的。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_MMC_SUBSYS
```

**定义位置（Location）**：[`subsys/sd/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_MMC_SUBSYS`](P076_drivers_disk_配置项参考.md#CONFIG_MMC_SUBSYS)。

<a id="CONFIG_SDIO_STACK"></a>

## 420.3 `CONFIG_SDIO_STACK`

**提示（Prompt）**：安全数字输入输出（SDIO）协议支持

**说明（Help）**

启用安全数字输入输出（SDIO）协议支持，这是 SD I/O 卡正常工作所必需的。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_WIFI_NXP
```

**定义位置（Location）**：[`subsys/sd/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)。

<a id="CONFIG_SDMMC_STACK"></a>

## 420.4 `CONFIG_SDMMC_STACK`

**提示（Prompt）**：SDMMC 协议支持

**说明（Help）**

启用 SDMMC 协议支持，这是 SD 存储卡（SD memory card）正常工作所必需的。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SDMMC_SUBSYS
```

**定义位置（Location）**：[`subsys/sd/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_SDMMC_SUBSYS`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_SUBSYS)。

<a id="CONFIG_SD_BUFFER_SIZE"></a>

## 420.5 `CONFIG_SD_BUFFER_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SD 卡内部缓冲区大小，单位为字节；用于未对齐读取（Unaligned read），以及初始化期间的内部数据读取。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SD_STACK
```

**默认值（Defaults）**

```text
512 if CONFIG_SDHC_BUFFER_ALIGNMENT != 1
512 if CONFIG_MMC_STACK
512 if CONFIG_SDIO_STACK
64
```

**定义位置（Location）**：[`subsys/sd/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_SD_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SD_STACK)、[`CONFIG_SDHC_BUFFER_ALIGNMENT`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_BUFFER_ALIGNMENT)、[`CONFIG_MMC_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_MMC_STACK)、[`CONFIG_SDIO_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SDIO_STACK)。

<a id="CONFIG_SD_CMD_RETRIES"></a>

## 420.6 `CONFIG_SD_CMD_RETRIES`

**提示（Prompt）**：向卡发送命令的重试次数

**说明（Help）**

向 SD 卡发送命令失败时的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SD_STACK
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/sd/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_SD_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SD_STACK)。

<a id="CONFIG_SD_CMD_TIMEOUT"></a>

## 420.7 `CONFIG_SD_CMD_TIMEOUT`

**提示（Prompt）**：SD 命令超时，单位为毫秒

**说明（Help）**

SD 命令的默认超时时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SD_STACK
```

**默认值（Defaults）**

```text
200
```

**定义位置（Location）**：[`subsys/sd/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_SD_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SD_STACK)。

<a id="CONFIG_SD_DATA_RETRIES"></a>

## 420.8 `CONFIG_SD_DATA_RETRIES`

**提示（Prompt）**：向卡发送数据的重试次数（Retries）

**说明（Help）**

向 SD 卡发送数据失败时的重试次数（Retries）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SD_STACK
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/sd/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_SD_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SD_STACK)。

<a id="CONFIG_SD_DATA_TIMEOUT"></a>

## 420.9 `CONFIG_SD_DATA_TIMEOUT`

**提示（Prompt）**：SD 数据传输超时（Data transfer timeout，毫秒）

**说明（Help）**

SD 数据传输命令（Data transfer command）的默认超时，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SD_STACK
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`subsys/sd/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_SD_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SD_STACK)。

<a id="CONFIG_SD_INIT_TIMEOUT"></a>

## 420.10 `CONFIG_SD_INIT_TIMEOUT`

**提示（Prompt）**：SD 卡初始化超时（Initialization timeout）

**说明（Help）**

等待 SD 卡初始化完成的最长时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SD_STACK
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`subsys/sd/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_SD_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SD_STACK)。

<a id="CONFIG_SD_OCR_RETRY_COUNT"></a>

## 420.11 `CONFIG_SD_OCR_RETRY_COUNT`

**提示（Prompt）**：SD 操作条件寄存器（OCR）读取的重试次数

**说明（Help）**

读取 SD 操作条件寄存器（Operating Conditions Register，OCR）命令的重试次数。OCR 读取通常比一般 SD 命令需要更多重试。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SD_STACK
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`subsys/sd/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_SD_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SD_STACK)。

<a id="CONFIG_SD_RETRY_COUNT"></a>

## 420.12 `CONFIG_SD_RETRY_COUNT`

**提示（Prompt）**：初始化命令（Initialization command）的重试次数

**说明（Help）**

初始化命令（Initialization command）失败时的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SD_STACK
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/sd/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_SD_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SD_STACK)。

<a id="CONFIG_SD_STACK"></a>

## 420.13 `CONFIG_SD_STACK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 SD 卡支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if CONFIG_MMC_STACK || CONFIG_SDMMC_STACK || CONFIG_SDIO_STACK
```

**主动选择（Selects）**

```text
CONFIG_SDHC
```

**定义位置（Location）**：[`subsys/sd/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_MMC_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_MMC_STACK)、[`CONFIG_SDMMC_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SDMMC_STACK)、[`CONFIG_SDIO_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SDIO_STACK)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_SD_UHS_PROTOCOL"></a>

## 420.14 `CONFIG_SD_UHS_PROTOCOL`

**提示（Prompt）**：超高速 SD 卡协议（Ultra High Speed SD card protocol）支持

**说明（Help）**

启用超高速 SD 卡（Ultra High Speed SD card）支持。可禁用以减少代码大小，但会牺牲数据传输速度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SD_STACK
```

**默认值（Defaults）**

```text
y if CONFIG_SDHC_SUPPORTS_UHS
```

**定义位置（Location）**：[`subsys/sd/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sd/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 安全数字存储卡（SD）

**配置项引用（Symbol References）**：[`CONFIG_SD_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SD_STACK)、[`CONFIG_SDHC_SUPPORTS_UHS`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_UHS)。

<!-- kconfig-navigation -->

[上一章](P419_subsys_rtio_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P421_subsys_secure_storage_配置项参考.md)
