---
id: learning.zephyr-docs.kconfig-reference.page-308
title: "`soc/silabs`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第308章\_`soc/silabs`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `soc/silabs` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CRYPTO_ACC_GECKO_TRNG"></a>

## 308.1 `CONFIG_CRYPTO_ACC_GECKO_TRNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 Silicon Labs Gecko 芯片启用基于 CRYPTO_ACC 模块的熵驱动（Entropy driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
CONFIG_ENTROPY_GECKO_TRNG
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_ENTROPY_GECKO_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GECKO_TRNG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_SILABS_GECKO_EMU_DCDC"></a>

## 308.2 `CONFIG_SILABS_GECKO_EMU_DCDC`

**提示（Prompt）**：片上系统直流－直流稳压器（SoC DC/DC regulator）

**说明（Help）**

启用片上直流－直流稳压器（on-chip DC/DC regulator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_S0 || CONFIG_SOC_FAMILY_SILABS_S1
```

**主动选择（Selects）**

```text
CONFIG_SILABS_GECKO_EMU
```

**定义位置（Location）**：[`soc/silabs/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SILABS_GECKO_EMU`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_GECKO_EMU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_FAMILY_SILABS_S1`。

<a id="CONFIG_SILABS_GECKO_EMU_DCDC_MODE"></a>

## 308.3 `CONFIG_SILABS_GECKO_EMU_DCDC_MODE`

**提示（Prompt）**：直流－直流转换模式（DC/DC mode）

**说明（Help）**

选择片上直流－直流转换器（DC/DC converter）的电源配置模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SILABS_GECKO_EMU_DCDC && (CONFIG_SOC_FAMILY_SILABS_S0 || CONFIG_SOC_FAMILY_SILABS_S1)
```

**可选项（Choices）**

```text
CONFIG_SILABS_GECKO_EMU_DCDC_MODE_UNCONFIGURED
CONFIG_SILABS_GECKO_EMU_DCDC_MODE_ON
CONFIG_SILABS_GECKO_EMU_DCDC_MODE_OFF
CONFIG_SILABS_GECKO_EMU_DCDC_MODE_BYPASS
```

**定义位置（Location）**：[`soc/silabs/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 片上系统直流－直流稳压器（SoC DC/DC regulator）

**配置项引用（Symbol References）**：[`CONFIG_SILABS_GECKO_EMU_DCDC`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_GECKO_EMU_DCDC)、[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SILABS_GECKO_EMU_DCDC_MODE_UNCONFIGURED`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_GECKO_EMU_DCDC_MODE_UNCONFIGURED)、[`CONFIG_SILABS_GECKO_EMU_DCDC_MODE_ON`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_GECKO_EMU_DCDC_MODE_ON)、[`CONFIG_SILABS_GECKO_EMU_DCDC_MODE_OFF`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_GECKO_EMU_DCDC_MODE_OFF)、[`CONFIG_SILABS_GECKO_EMU_DCDC_MODE_BYPASS`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_GECKO_EMU_DCDC_MODE_BYPASS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_FAMILY_SILABS_S1`。

<a id="CONFIG_SILABS_GECKO_EMU_DCDC_MODE_BYPASS"></a>

## 308.4 `CONFIG_SILABS_GECKO_EMU_DCDC_MODE_BYPASS`

**提示（Prompt）**：旁路（Bypass）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SILABS_GECKO_EMU_DCDC_MODE>
```

**定义位置（Location）**：[`soc/silabs/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 片上系统直流－直流稳压器（SoC DC/DC regulator） → 直流－直流转换模式（DC/DC mode）

**配置项引用（Symbol References）**：[`CONFIG_SILABS_GECKO_EMU_DCDC_MODE`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_GECKO_EMU_DCDC_MODE)。

<a id="CONFIG_SILABS_GECKO_EMU_DCDC_MODE_OFF"></a>

## 308.5 `CONFIG_SILABS_GECKO_EMU_DCDC_MODE_OFF`

**提示（Prompt）**：关闭直流－直流转换器（DC/DC Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SILABS_GECKO_EMU_DCDC_MODE>
```

**定义位置（Location）**：[`soc/silabs/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 片上系统直流－直流稳压器（SoC DC/DC regulator） → 直流－直流转换模式（DC/DC mode）

**配置项引用（Symbol References）**：[`CONFIG_SILABS_GECKO_EMU_DCDC_MODE`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_GECKO_EMU_DCDC_MODE)。

<a id="CONFIG_SILABS_GECKO_EMU_DCDC_MODE_ON"></a>

## 308.6 `CONFIG_SILABS_GECKO_EMU_DCDC_MODE_ON`

**提示（Prompt）**：开启直流－直流转换器（DC/DC On）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SILABS_GECKO_EMU_DCDC_MODE>
```

**定义位置（Location）**：[`soc/silabs/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 片上系统直流－直流稳压器（SoC DC/DC regulator） → 直流－直流转换模式（DC/DC mode）

**配置项引用（Symbol References）**：[`CONFIG_SILABS_GECKO_EMU_DCDC_MODE`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_GECKO_EMU_DCDC_MODE)。

<a id="CONFIG_SILABS_GECKO_EMU_DCDC_MODE_UNCONFIGURED"></a>

## 308.7 `CONFIG_SILABS_GECKO_EMU_DCDC_MODE_UNCONFIGURED`

**提示（Prompt）**：初始／未配置（Initial / Unconfigured）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SILABS_GECKO_EMU_DCDC_MODE>
```

**定义位置（Location）**：[`soc/silabs/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 片上系统直流－直流稳压器（SoC DC/DC regulator） → 直流－直流转换模式（DC/DC mode）

**配置项引用（Symbol References）**：[`CONFIG_SILABS_GECKO_EMU_DCDC_MODE`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_GECKO_EMU_DCDC_MODE)。

<a id="CONFIG_SILABS_SHELL"></a>

## 308.8 `CONFIG_SILABS_SHELL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 `silabs` shell 命令命名空间（command namespace）的隐藏选项。任何注册子命令的 Silicon Labs SoC 功能都会选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**被选择（Selected by）**

```text
CONFIG_SIWX91X_FIRMWARE_UPGRADE_SHELL
CONFIG_SIWX91X_VERSION_SHELL
CONFIG_SIWX91X_CLOCK_SHELL
```

**定义位置（Location）**：[`soc/silabs/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SIWX91X_FIRMWARE_UPGRADE_SHELL`](P308_soc_silabs_配置项参考_1.md#CONFIG_SIWX91X_FIRMWARE_UPGRADE_SHELL)、[`CONFIG_SIWX91X_VERSION_SHELL`](P308_soc_silabs_配置项参考_1.md#CONFIG_SIWX91X_VERSION_SHELL)、[`CONFIG_SIWX91X_CLOCK_SHELL`](P308_soc_silabs_配置项参考_1.md#CONFIG_SIWX91X_CLOCK_SHELL)。

<a id="CONFIG_SILABS_SIWX91X_NWP"></a>

## 308.9 `CONFIG_SILABS_SIWX91X_NWP`

**提示（Prompt）**：Silicon Labs 网络协处理器（Network Coprocessor）

**说明（Help）**

添加对 SiWx91x 器件中网络协处理器（Network Coprocessor，也称 NWP）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_NWP_ENABLED && CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**主动选择（Selects）**

```text
CONFIG_CODE_DATA_RELOCATION_SRAM
CONFIG_CMSIS_RTOS_V2
CONFIG_POLL
CONFIG_DYNAMIC_THREAD
CONFIG_THREAD_NAME
CONFIG_THREAD_STACK_INFO
CONFIG_THREAD_MONITOR
CONFIG_INIT_STACKS
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_SILABS_SIWX91X
CONFIG_SIWX91X_FIRMWARE_UPGRADE
CONFIG_BT_SILABS_SIWX91X
CONFIG_SOC_FLASH_SILABS_SIWX91X
CONFIG_WIFI_SILABS_SIWX91X
```

**定义位置（Location）**：[`soc/silabs/silabs_siwx91x/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_siwx91x/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_CODE_DATA_RELOCATION_SRAM`](P029_arch_arm_配置项参考_1.md#CONFIG_CODE_DATA_RELOCATION_SRAM)、[`CONFIG_CMSIS_RTOS_V2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CMSIS_RTOS_V2)、[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)、[`CONFIG_DYNAMIC_THREAD`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD)、[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_INIT_STACKS`](P001_kernel_配置项参考_1.md#CONFIG_INIT_STACKS)、[`CONFIG_SIWX91X_FIRMWARE_UPGRADE`](P308_soc_silabs_配置项参考_1.md#CONFIG_SIWX91X_FIRMWARE_UPGRADE)、[`CONFIG_BT_SILABS_SIWX91X`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_SIWX91X)、[`CONFIG_SOC_FLASH_SILABS_SIWX91X`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_SILABS_SIWX91X)、[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`。

<a id="CONFIG_SILABS_SIWX91X_SLOW_FLASH_DATA"></a>

## 308.10 `CONFIG_SILABS_SIWX91X_SLOW_FLASH_DATA`

**提示（Prompt）**：限制访问 Flash 中的数据（Limit access to data in flash）［实验性，EXPERIMENTAL］

**说明（Help）**

SiWx91x 的主 Flash 没有数据缓存（data cache）。使用此项可要求编译器限制对 Flash 中数据的访问。收益取决于工作负载：某些内核基准测试（`tests/benchmarks/app_kernel/`）运行速度最高可提升 300%，通常提升约 10%～50%。此选项会引入 `CONFIG_SLOW_FLASH_DATA` 中描述的限制，用户必须了解这些限制。译注：性能数字来自本次官方文档快照，不代表本仓库的实测结果。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**主动选择（Selects）**

```text
CONFIG_SLOW_FLASH_DATA
```

**定义位置（Location）**：[`soc/silabs/silabs_siwx91x/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_siwx91x/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SLOW_FLASH_DATA`](P030_arch_arm_配置项参考_2.md#CONFIG_SLOW_FLASH_DATA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`。

<a id="CONFIG_SIWX91X_CLOCK_SHELL"></a>

## 308.11 `CONFIG_SIWX91X_CLOCK_SHELL`

**提示（Prompt）**：列出 SiWx91x 时钟的 shell 命令（Shell command）

**说明（Help）**

添加 `silabs clocks` shell 命令，打印全部 SiWx91x 时钟域（clock domain）的开启／关闭状态，以及可获取的频率。若要在构建时生成设备树连接图（devicetree wiring diagram），运行：

```sh
west build -t siwx91x_clock_tree
```

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_SILABS_SIWX91X && CONFIG_SHELL && CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SHELL
```

**定义位置（Location）**：[`soc/silabs/silabs_siwx91x/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_siwx91x/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_SILABS_SIWX91X`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_SILABS_SIWX91X)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SILABS_SHELL`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_SHELL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`。

<a id="CONFIG_SIWX91X_ENCRYPT"></a>

## 308.12 `CONFIG_SIWX91X_ENCRYPT`

**提示（Prompt）**：同时加密固件（Also encrypt the firmware）

**说明（Help）**

使用 AES 电子密码本模式（ECB）加密应用镜像。密钥取自 `CONFIG_SIWX91X_MIC_KEY`，其值原样传给 `commander rps convert` 命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SIWX91X_MIC_KEY != "" && CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**定义位置（Location）**：[`soc/silabs/silabs_siwx91x/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_siwx91x/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SIWX91X_MIC_KEY`](P308_soc_silabs_配置项参考_1.md#CONFIG_SIWX91X_MIC_KEY)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`。

<a id="CONFIG_SIWX91X_FIRMWARE_UPGRADE"></a>

## 308.13 `CONFIG_SIWX91X_FIRMWARE_UPGRADE`

**提示（Prompt）**：固件升级支持（Support for firmware upgrade）

**说明（Help）**

SiWx91x 器件的固件升级流程需要同时与网络协处理器（Network Co-Processor，NCP）和 ROM 引导加载程序（ROM bootloader）协同通信。NCP 负责将固件镜像写入 Flash；ROM 引导加载程序负责 A／B 升级逻辑，以确保可靠切换固件。

此选项提供执行这些升级任务所需的 API，与底层传输协议无关。它不直接获取固件；应用层负责通过 HTTP 客户端等方式取得固件镜像，并调用相应 API 启动和完成升级过程。更多信息请参阅 [Si91x 从主机更新固件的 API](https://docs.silabs.com/wiseconnect/latest/wiseconnect-api-reference-guide-si91x-driver/si91-x-firmware-update-from-host-functions#sl-si91x-fwup-load)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SIWX91X_NWP
```

**定义位置（Location）**：[`soc/silabs/silabs_siwx91x/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_siwx91x/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SILABS_SIWX91X_NWP`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_SIWX91X_NWP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`。

<a id="CONFIG_SIWX91X_FIRMWARE_UPGRADE_SHELL"></a>

## 308.14 `CONFIG_SIWX91X_FIRMWARE_UPGRADE_SHELL`

**提示（Prompt）**：固件升级 shell 命令（Shell command for firmware upgrade）

**说明（Help）**

添加 `silabs fota <URL>` shell 命令，通过 HTTP 或 HTTPS 下载固件镜像并烧录。执行命令前必须已经连接 Wi-Fi。升级完成后设备会自动重启。要支持 HTTPS，用户必须启用传输层安全（TLS）支持；通常可使用 HTTP 客户端示例提供的覆盖文件 `samples/net/sockets/http_client/overlay-tls.conf`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_NET_TCP && CONFIG_SIWX91X_FIRMWARE_UPGRADE && CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SHELL
CONFIG_HTTP_CLIENT
CONFIG_NET_SOCKETS
CONFIG_REBOOT
```

**定义位置（Location）**：[`soc/silabs/silabs_siwx91x/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_siwx91x/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 固件升级支持（Support for firmware upgrade）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_SIWX91X_FIRMWARE_UPGRADE`](P308_soc_silabs_配置项参考_1.md#CONFIG_SIWX91X_FIRMWARE_UPGRADE)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SILABS_SHELL`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_SHELL)、[`CONFIG_HTTP_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_CLIENT)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`。

<a id="CONFIG_SIWX91X_MIC_KEY"></a>

## 308.15 `CONFIG_SIWX91X_MIC_KEY`

**提示（Prompt）**：消息完整性码密钥（Integrity Code，MIC）

**说明（Help）**

使用基于消息完整性码（MIC，AES CBC-MAC）的完整性检查代替基于循环冗余校验（CRC）的检查，以验证固件完整性。此值原样传给 `commander rps convert` 命令。原文称，该值通常是表示 AES-256 密钥的 32 个十六进制数字组成的字符串。译注：32 个十六进制数字表示 128 位，与 AES-256 的 256 位不一致；这里保留原文说法，不将其视为已核实的密钥长度要求。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**定义位置（Location）**：[`soc/silabs/silabs_siwx91x/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_siwx91x/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`。

<a id="CONFIG_SIWX91X_NWP_INIT_PRIORITY"></a>

## 308.16 `CONFIG_SIWX91X_NWP_INIT_PRIORITY`

**提示（Prompt）**：SiWx91x 网络处理器初始化优先级（Network Processor init priority）

**说明（Help）**

SiWx91x 网络处理器（Network Processor）的初始化优先级。NWP 必须先于依赖它的服务初始化，例如蓝牙、Wi-Fi 和加密服务。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**默认值（Defaults）**

```text
39
```

**定义位置（Location）**：[`soc/silabs/silabs_siwx91x/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_siwx91x/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`。

<a id="CONFIG_SIWX91X_SIGN_KEY"></a>

## 308.17 `CONFIG_SIWX91X_SIGN_KEY`

**提示（Prompt）**：签名密钥（Signing key）

**说明（Help）**

使用此私钥签署固件。此值原样传给 `commander rps convert` 命令，通常为 PEM 格式文件的路径。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**定义位置（Location）**：[`soc/silabs/silabs_siwx91x/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_siwx91x/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`。

<a id="CONFIG_SIWX91X_VERSION_SHELL"></a>

## 308.18 `CONFIG_SIWX91X_VERSION_SHELL`

**提示（Prompt）**：查询网络处理器固件版本的 shell 命令（NWP firmware version）

**说明（Help）**

添加 `silabs nwp_version [-c]` shell 命令，打印网络处理器（NWP）固件版本。带 `-c` 时，会验证其是否与预期版本匹配，不匹配则返回错误。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SILABS_SIWX91X_NWP && CONFIG_SHELL && CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SHELL
```

**定义位置（Location）**：[`soc/silabs/silabs_siwx91x/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_siwx91x/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SILABS_SIWX91X_NWP`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_SIWX91X_NWP)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SILABS_SHELL`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_SHELL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`。

<a id="CONFIG_SOC_FAMILY_SILABS_S2_XG21"></a>

## 308.19 `CONFIG_SOC_FAMILY_SILABS_S2_XG21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG21 通用家族片上系统与模组（Generic Family SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFR32BG21
CONFIG_SOC_SERIES_EFR32MG21
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg21/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg21/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_SERIES_EFR32BG21`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG21)、[`CONFIG_SOC_SERIES_EFR32MG21`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG21)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_SOC_FAMILY_SILABS_S2_XG22"></a>

## 308.20 `CONFIG_SOC_FAMILY_SILABS_S2_XG22`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG22 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFR32BG22
CONFIG_SOC_SERIES_EFR32MG22
CONFIG_SOC_SERIES_BGM22
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg22/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg22/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_SERIES_EFR32BG22`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG22)、[`CONFIG_SOC_SERIES_EFR32MG22`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG22)、[`CONFIG_SOC_SERIES_BGM22`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_BGM22)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_SOC_FAMILY_SILABS_S2_XG23"></a>

## 308.21 `CONFIG_SOC_FAMILY_SILABS_S2_XG23`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG23 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFR32ZG23
CONFIG_SOC_SERIES_EFM32PG23
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg23/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg23/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_SERIES_EFR32ZG23`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32ZG23)、[`CONFIG_SOC_SERIES_EFM32PG23`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32PG23)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_SOC_FAMILY_SILABS_S2_XG24"></a>

## 308.22 `CONFIG_SOC_FAMILY_SILABS_S2_XG24`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG24 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFR32BG24
CONFIG_SOC_SERIES_EFR32MG24
CONFIG_SOC_SERIES_MGM24
CONFIG_SOC_SERIES_BGM24
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg24/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg24/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_SERIES_EFR32BG24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG24)、[`CONFIG_SOC_SERIES_EFR32MG24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG24)、[`CONFIG_SOC_SERIES_MGM24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_MGM24)、[`CONFIG_SOC_SERIES_BGM24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_BGM24)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_SOC_FAMILY_SILABS_S2_XG26"></a>

## 308.23 `CONFIG_SOC_FAMILY_SILABS_S2_XG26`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG26 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFM32PG26
CONFIG_SOC_SERIES_EFR32BG26
CONFIG_SOC_SERIES_BGM26
CONFIG_SOC_SERIES_EFR32MG26
CONFIG_SOC_SERIES_MGM26
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg26/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg26/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_SERIES_EFM32PG26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32PG26)、[`CONFIG_SOC_SERIES_EFR32BG26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG26)、[`CONFIG_SOC_SERIES_BGM26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_BGM26)、[`CONFIG_SOC_SERIES_EFR32MG26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG26)、[`CONFIG_SOC_SERIES_MGM26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_MGM26)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_SOC_FAMILY_SILABS_S2_XG27"></a>

## 308.24 `CONFIG_SOC_FAMILY_SILABS_S2_XG27`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG27 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFR32BG27
CONFIG_SOC_SERIES_EFR32MG27
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg27/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg27/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_SERIES_EFR32BG27`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG27)、[`CONFIG_SOC_SERIES_EFR32MG27`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG27)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_SOC_FAMILY_SILABS_S2_XG28"></a>

## 308.25 `CONFIG_SOC_FAMILY_SILABS_S2_XG28`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG28 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFM32PG28
CONFIG_SOC_SERIES_EFR32FG28
CONFIG_SOC_SERIES_EFR32ZG28
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg28/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg28/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_SERIES_EFM32PG28`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32PG28)、[`CONFIG_SOC_SERIES_EFR32FG28`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32FG28)、[`CONFIG_SOC_SERIES_EFR32ZG28`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32ZG28)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_SOC_FAMILY_SILABS_S2_XG29"></a>

## 308.26 `CONFIG_SOC_FAMILY_SILABS_S2_XG29`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG29 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFR32BG29
CONFIG_SOC_SERIES_EFR32MG29
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg29/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg29/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_SERIES_EFR32BG29`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG29)、[`CONFIG_SOC_SERIES_EFR32MG29`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG29)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_SOC_FAMILY_SILABS_S3_SIX301"></a>

## 308.27 `CONFIG_SOC_FAMILY_SILABS_S3_SIX301`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs Six301 片上系统与模组（SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S3
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_SIBG301
CONFIG_SOC_SERIES_SIMG301
```

**定义位置（Location）**：[`soc/silabs/silabs_s3/six301/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s3/six301/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_SOC_SERIES_SIBG301`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_SIBG301)、[`CONFIG_SOC_SERIES_SIMG301`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_SIMG301)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S3`。

<a id="CONFIG_SOC_GECKO_CUSTOM_RADIO_PHY"></a>

## 308.28 `CONFIG_SOC_GECKO_CUSTOM_RADIO_PHY`

**提示（Prompt）**：使用无线电抽象接口层进行自定义物理层数据包收发（RAIL）

**说明（Help）**

启用后，可使用无线电抽象接口层（RAIL）管理用户生成的自定义无线电物理层（radio PHY），并在该物理层上发送和接收数据包。用户必须提供该 PHY 的 `radio_config.c` 和 `radio_config.h` 文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_VENDOR_SILABS_HAS_RADIO && (CONFIG_SOC_FAMILY_SILABS_S1 || CONFIG_SOC_FAMILY_SILABS_S2 || CONFIG_SOC_FAMILY_SILABS_S3)
```

**主动选择（Selects）**

```text
CONFIG_SOC_GECKO_USE_RAIL
```

**定义位置（Location）**：[`soc/silabs/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_VENDOR_SILABS_HAS_RADIO)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_SOC_GECKO_USE_RAIL`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_GECKO_USE_RAIL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_FAMILY_SILABS_S2`、`CONFIG_SOC_FAMILY_SILABS_S3`。

<a id="CONFIG_SOC_GECKO_HAS_ERRATA_RTCC_E201"></a>

## 308.29 `CONFIG_SOC_GECKO_HAS_ERRATA_RTCC_E201`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 SoC 受勘误 RTCC_E201（errata）影响，则设置此项。勘误内容：“当 RTCC 配置了预分频器，并通过设置 `RTCC_CTRL` 中的 `CCV1TOP` 启用 CCV1 顶值功能时，在 `RTCC_CNT` 等于 `RTCC_CC1_CCV` 时，计数器无法按预期回绕（wrap）。”

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_S0 || CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFR32FG13P
CONFIG_SOC_SERIES_EFR32FG1P
```

**定义位置（Location）**：[`soc/silabs/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_SERIES_EFR32FG13P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32FG13P)、[`CONFIG_SOC_SERIES_EFR32FG1P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32FG1P)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_FAMILY_SILABS_S1`。

<a id="CONFIG_SOC_GECKO_HAS_INDIVIDUAL_PIN_LOCATION"></a>

## 308.30 `CONFIG_SOC_GECKO_HAS_INDIVIDUAL_PIN_LOCATION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用后，表示 SoC 允许分别配置单个引脚位置（individual pin locations），例如 efr32fg1p、efr32mg12p 系列支持此方式。禁用时，表示引脚位置按组配置，例如 efm32hg、efm32wg 系列支持此方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_S0 || CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFM32GG11B
CONFIG_SOC_SERIES_EFM32GG12B
CONFIG_SOC_SERIES_EFM32JG12B
CONFIG_SOC_SERIES_EFM32PG12B
CONFIG_SOC_SERIES_EFM32PG1B
CONFIG_SOC_SERIES_EFR32BG13P
CONFIG_SOC_SERIES_EFR32FG13P
CONFIG_SOC_SERIES_EFR32FG1P
CONFIG_SOC_SERIES_EFR32MG12P
CONFIG_SOC_SERIES_EFR32MG13P
```

**定义位置（Location）**：[`soc/silabs/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_SERIES_EFM32GG11B`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32GG11B)、[`CONFIG_SOC_SERIES_EFM32GG12B`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32GG12B)、[`CONFIG_SOC_SERIES_EFM32JG12B`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32JG12B)、[`CONFIG_SOC_SERIES_EFM32PG12B`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32PG12B)、[`CONFIG_SOC_SERIES_EFM32PG1B`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFM32PG1B)、[`CONFIG_SOC_SERIES_EFR32BG13P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG13P)、[`CONFIG_SOC_SERIES_EFR32FG13P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32FG13P)、[`CONFIG_SOC_SERIES_EFR32FG1P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32FG1P)、[`CONFIG_SOC_SERIES_EFR32MG12P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG13P)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_FAMILY_SILABS_S1`。

<a id="CONFIG_SOC_GECKO_USE_RAIL"></a>

## 308.31 `CONFIG_SOC_GECKO_USE_RAIL`

**提示（Prompt）**：使用无线电抽象接口层（Radio Abstraction Interface Layer，RAIL）

**说明（Help）**

无线电抽象接口层（Radio Abstraction Interface Layer，RAIL）是使用 EFR 无线电硬件所需的库。此选项启用适当的功能集，使其能够与 RAIL 二进制组件（blob）正确编译。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_VENDOR_SILABS_HAS_RADIO && (CONFIG_SOC_FAMILY_SILABS_S1 || CONFIG_SOC_FAMILY_SILABS_S2 || CONFIG_SOC_FAMILY_SILABS_S3)
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_LDMA
CONFIG_SILABS_SISDK_TIMER if CONFIG_BT_CHANNEL_SOUNDING
```

**被选择（Selected by）**

```text
CONFIG_SOC_GECKO_CUSTOM_RADIO_PHY
CONFIG_BT_SILABS_EFR32
CONFIG_IEEE802154_SILABS_EFR32
```

**定义位置（Location）**：[`soc/silabs/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_VENDOR_SILABS_HAS_RADIO)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_SILABS_SISDK_LDMA`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_LDMA)、[`CONFIG_SILABS_SISDK_TIMER`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_TIMER)、[`CONFIG_BT_CHANNEL_SOUNDING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CHANNEL_SOUNDING)、[`CONFIG_SOC_GECKO_CUSTOM_RADIO_PHY`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_GECKO_CUSTOM_RADIO_PHY)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_IEEE802154_SILABS_EFR32`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_SILABS_EFR32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_FAMILY_SILABS_S2`、`CONFIG_SOC_FAMILY_SILABS_S3`。

<a id="CONFIG_SOC_SERIES_BGM22"></a>

## 308.32 `CONFIG_SOC_SERIES_BGM22`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs BGM220 系列微控制器模组（Series MCU modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG22
```

**被选择（Selected by）**

```text
CONFIG_SOC_BGM220PC22HNA
CONFIG_SOC_BGM220PC22WGA
CONFIG_SOC_BGM220SC22HNA
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg22/Kconfig.soc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg22/Kconfig.soc#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_BGM220PC22HNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM220PC22HNA)、[`CONFIG_SOC_BGM220PC22WGA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM220PC22WGA)、[`CONFIG_SOC_BGM220SC22HNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM220SC22HNA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_BGM220PC22HNA`、`CONFIG_SOC_BGM220PC22WGA`、`CONFIG_SOC_BGM220SC22HNA`。

<a id="CONFIG_SOC_SERIES_BGM24"></a>

## 308.33 `CONFIG_SOC_SERIES_BGM24`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs BGM240 系列微控制器模组（Series MCU modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG24
```

**被选择（Selected by）**

```text
CONFIG_SOC_BGM240PA22VNA
CONFIG_SOC_BGM240PA32VNA
CONFIG_SOC_BGM240PA32VNN
CONFIG_SOC_BGM240PB22VNA
CONFIG_SOC_BGM240PB32VNA
CONFIG_SOC_BGM240PB32VNN
CONFIG_SOC_BGM240SA22VNA
CONFIG_SOC_BGM240SB22VNA
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg24/Kconfig.soc:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg24/Kconfig.soc#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_BGM240PA22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM240PA22VNA)、[`CONFIG_SOC_BGM240PA32VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM240PA32VNA)、[`CONFIG_SOC_BGM240PA32VNN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM240PA32VNN)、[`CONFIG_SOC_BGM240PB22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM240PB22VNA)、[`CONFIG_SOC_BGM240PB32VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM240PB32VNA)、[`CONFIG_SOC_BGM240PB32VNN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM240PB32VNN)、[`CONFIG_SOC_BGM240SA22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM240SA22VNA)、[`CONFIG_SOC_BGM240SB22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM240SB22VNA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_BGM240PA22VNA`、`CONFIG_SOC_BGM240PA32VNA`、`CONFIG_SOC_BGM240PA32VNN`、`CONFIG_SOC_BGM240PB22VNA`、`CONFIG_SOC_BGM240PB32VNA`、`CONFIG_SOC_BGM240PB32VNN`、`CONFIG_SOC_BGM240SA22VNA`、`CONFIG_SOC_BGM240SB22VNA`。

<a id="CONFIG_SOC_SERIES_BGM26"></a>

## 308.34 `CONFIG_SOC_SERIES_BGM26`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs BGM260（Blue Gecko）系列微控制器模组（Series MCU modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG26
```

**被选择（Selected by）**

```text
CONFIG_SOC_BGM260PB22VNA
CONFIG_SOC_BGM260PB32VNA
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg26/Kconfig.soc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg26/Kconfig.soc#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_BGM260PB22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM260PB22VNA)、[`CONFIG_SOC_BGM260PB32VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BGM260PB32VNA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_BGM260PB22VNA`、`CONFIG_SOC_BGM260PB32VNA`。

<a id="CONFIG_SOC_SERIES_EFM32GG11B"></a>

## 308.35 `CONFIG_SOC_SERIES_EFM32GG11B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32GG11B（Giant Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFM32GG11B820F2048GL192
CONFIG_SOC_EFM32GG11B820F2048GM64
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efm32gg11b/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efm32gg11b/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_EFM32GG11B820F2048GL192`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32GG11B820F2048GL192)、[`CONFIG_SOC_EFM32GG11B820F2048GM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32GG11B820F2048GM64)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_EFM32GG11B820F2048GL192`、`CONFIG_SOC_EFM32GG11B820F2048GM64`。

<a id="CONFIG_SOC_SERIES_EFM32GG12B"></a>

## 308.36 `CONFIG_SOC_SERIES_EFM32GG12B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32GG12（Giant Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFM32GG12B810F1024GM64
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efm32gg12b/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efm32gg12b/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_EFM32GG12B810F1024GM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32GG12B810F1024GM64)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_EFM32GG12B810F1024GM64`。

<a id="CONFIG_SOC_SERIES_EFM32HG"></a>

## 308.37 `CONFIG_SOC_SERIES_EFM32HG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32HG（Happy Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S0
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFM32HG309F64
CONFIG_SOC_EFM32HG322F64
```

**定义位置（Location）**：[`soc/silabs/silabs_s0/efm32hg/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s0/efm32hg/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_EFM32HG309F64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32HG309F64)、[`CONFIG_SOC_EFM32HG322F64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32HG322F64)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_EFM32HG309F64`、`CONFIG_SOC_EFM32HG322F64`。

<a id="CONFIG_SOC_SERIES_EFM32JG12B"></a>

## 308.38 `CONFIG_SOC_SERIES_EFM32JG12B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32JG12B（Jade Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFM32JG12B500F1024GL125
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efm32jg12b/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efm32jg12b/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_EFM32JG12B500F1024GL125`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32JG12B500F1024GL125)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_EFM32JG12B500F1024GL125`。

<a id="CONFIG_SOC_SERIES_EFM32PG12B"></a>

## 308.39 `CONFIG_SOC_SERIES_EFM32PG12B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32PG12B（Pearl Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFM32PG12B500F1024GL125
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efm32pg12b/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efm32pg12b/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_EFM32PG12B500F1024GL125`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG12B500F1024GL125)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_EFM32PG12B500F1024GL125`。

<a id="CONFIG_SOC_SERIES_EFM32PG1B"></a>

## 308.40 `CONFIG_SOC_SERIES_EFM32PG1B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32PG1B（Pearl Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFM32PG1B200F256GM48
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efm32pg1b/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efm32pg1b/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_EFM32PG1B200F256GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG1B200F256GM48)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_EFM32PG1B200F256GM48`。

<a id="CONFIG_SOC_SERIES_EFM32PG23"></a>

## 308.41 `CONFIG_SOC_SERIES_EFM32PG23`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32PG23 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG23
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFM32PG23B310F512IM48
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg23/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg23/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_EFM32PG23B310F512IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG23B310F512IM48)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFM32PG23B310F512IM48`。

<a id="CONFIG_SOC_SERIES_EFM32PG26"></a>

## 308.42 `CONFIG_SOC_SERIES_EFM32PG26`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32PG26（Pearl Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG26
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFM32PG26B101F512IL136
CONFIG_SOC_EFM32PG26B101F512IM68
CONFIG_SOC_EFM32PG26B301F1024IL136
CONFIG_SOC_EFM32PG26B301F1024IM68
CONFIG_SOC_EFM32PG26B301F2048IL136
CONFIG_SOC_EFM32PG26B301F2048IM68
CONFIG_SOC_EFM32PG26B500F3200IL136
CONFIG_SOC_EFM32PG26B500F3200IM48
CONFIG_SOC_EFM32PG26B500F3200IM68
CONFIG_SOC_EFM32PG26B501F3200IL136
CONFIG_SOC_EFM32PG26B501F3200IM48
CONFIG_SOC_EFM32PG26B501F3200IM68
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg26/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg26/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_EFM32PG26B101F512IL136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG26B101F512IL136)、[`CONFIG_SOC_EFM32PG26B101F512IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG26B101F512IM68)、[`CONFIG_SOC_EFM32PG26B301F1024IL136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG26B301F1024IL136)、[`CONFIG_SOC_EFM32PG26B301F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG26B301F1024IM68)、[`CONFIG_SOC_EFM32PG26B301F2048IL136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG26B301F2048IL136)、[`CONFIG_SOC_EFM32PG26B301F2048IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG26B301F2048IM68)、[`CONFIG_SOC_EFM32PG26B500F3200IL136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG26B500F3200IL136)、[`CONFIG_SOC_EFM32PG26B500F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG26B500F3200IM48)、[`CONFIG_SOC_EFM32PG26B500F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG26B500F3200IM68)、[`CONFIG_SOC_EFM32PG26B501F3200IL136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG26B501F3200IL136)、[`CONFIG_SOC_EFM32PG26B501F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG26B501F3200IM48)、[`CONFIG_SOC_EFM32PG26B501F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG26B501F3200IM68)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFM32PG26B101F512IL136`、`CONFIG_SOC_EFM32PG26B101F512IM68`、`CONFIG_SOC_EFM32PG26B301F1024IL136`、`CONFIG_SOC_EFM32PG26B301F1024IM68`、`CONFIG_SOC_EFM32PG26B301F2048IL136`、`CONFIG_SOC_EFM32PG26B301F2048IM68`、`CONFIG_SOC_EFM32PG26B500F3200IL136`、`CONFIG_SOC_EFM32PG26B500F3200IM48`、`CONFIG_SOC_EFM32PG26B500F3200IM68`、`CONFIG_SOC_EFM32PG26B501F3200IL136`、`CONFIG_SOC_EFM32PG26B501F3200IM48`、`CONFIG_SOC_EFM32PG26B501F3200IM68`。

<a id="CONFIG_SOC_SERIES_EFM32PG28"></a>

## 308.43 `CONFIG_SOC_SERIES_EFM32PG28`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32PG28 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG28
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFM32PG28B200F512IM68
CONFIG_SOC_EFM32PG28B210F1024IM68
CONFIG_SOC_EFM32PG28B300F512IM68
CONFIG_SOC_EFM32PG28B310F1024IM68
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg28/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg28/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_EFM32PG28B200F512IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG28B200F512IM68)、[`CONFIG_SOC_EFM32PG28B210F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG28B210F1024IM68)、[`CONFIG_SOC_EFM32PG28B300F512IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG28B300F512IM68)、[`CONFIG_SOC_EFM32PG28B310F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32PG28B310F1024IM68)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFM32PG28B200F512IM68`、`CONFIG_SOC_EFM32PG28B210F1024IM68`、`CONFIG_SOC_EFM32PG28B300F512IM68`、`CONFIG_SOC_EFM32PG28B310F1024IM68`。

<a id="CONFIG_SOC_SERIES_EFM32TG"></a>

## 308.44 `CONFIG_SOC_SERIES_EFM32TG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32TG（Tiny Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S0
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFM32TG840F32
```

**定义位置（Location）**：[`soc/silabs/silabs_s0/efm32tg/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s0/efm32tg/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_EFM32TG840F32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32TG840F32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_EFM32TG840F32`。

<a id="CONFIG_SOC_SERIES_EFM32WG"></a>

## 308.45 `CONFIG_SOC_SERIES_EFM32WG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32WG（Wonder Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S0
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFM32WG990F256
```

**定义位置（Location）**：[`soc/silabs/silabs_s0/efm32wg/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s0/efm32wg/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_EFM32WG990F256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFM32WG990F256)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_EFM32WG990F256`。

<a id="CONFIG_SOC_SERIES_EFR32BG13P"></a>

## 308.46 `CONFIG_SOC_SERIES_EFR32BG13P`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32BG13P（Blue Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32BG13P632F512GM48
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efr32bg13p/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efr32bg13p/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_EFR32BG13P632F512GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG13P632F512GM48)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_EFR32BG13P632F512GM48`。

<a id="CONFIG_SOC_SERIES_EFR32BG21"></a>

## 308.47 `CONFIG_SOC_SERIES_EFR32BG21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32BG21（Blue Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG21
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32BG21B010F1024IM32
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg21/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg21/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_EFR32BG21B010F1024IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG21B010F1024IM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32BG21B010F1024IM32`。

<a id="CONFIG_SOC_SERIES_EFR32BG22"></a>

## 308.48 `CONFIG_SOC_SERIES_EFR32BG22`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32BG22（Blue Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG22
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32BG22C224F512IM40
CONFIG_SOC_EFR32BG22C224F512IM32
CONFIG_SOC_EFR32BG22C224F512GN32
CONFIG_SOC_EFR32BG22C224F512GM40
CONFIG_SOC_EFR32BG22C224F512GM32
CONFIG_SOC_EFR32BG22C222F352GN32
CONFIG_SOC_EFR32BG22C222F352GM40
CONFIG_SOC_EFR32BG22C222F352GM32
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg22/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg22/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_EFR32BG22C224F512IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG22C224F512IM40)、[`CONFIG_SOC_EFR32BG22C224F512IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG22C224F512IM32)、[`CONFIG_SOC_EFR32BG22C224F512GN32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG22C224F512GN32)、[`CONFIG_SOC_EFR32BG22C224F512GM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG22C224F512GM40)、[`CONFIG_SOC_EFR32BG22C224F512GM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG22C224F512GM32)、[`CONFIG_SOC_EFR32BG22C222F352GN32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG22C222F352GN32)、[`CONFIG_SOC_EFR32BG22C222F352GM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG22C222F352GM40)、[`CONFIG_SOC_EFR32BG22C222F352GM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG22C222F352GM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32BG22C224F512IM40`、`CONFIG_SOC_EFR32BG22C224F512IM32`、`CONFIG_SOC_EFR32BG22C224F512GN32`、`CONFIG_SOC_EFR32BG22C224F512GM40`、`CONFIG_SOC_EFR32BG22C224F512GM32`、`CONFIG_SOC_EFR32BG22C222F352GN32`、`CONFIG_SOC_EFR32BG22C222F352GM40`、`CONFIG_SOC_EFR32BG22C222F352GM32`。

<a id="CONFIG_SOC_SERIES_EFR32BG24"></a>

## 308.49 `CONFIG_SOC_SERIES_EFR32BG24`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32BG24（Blue Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG24
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32BG24A010F1024IM40
CONFIG_SOC_EFR32BG24A010F1024IM48
CONFIG_SOC_EFR32BG24A020F1024IM40
CONFIG_SOC_EFR32BG24A020F1024IM48
CONFIG_SOC_EFR32BG24B110F1536IM48
CONFIG_SOC_EFR32BG24B210F1024IM48
CONFIG_SOC_EFR32BG24B220F1024IM48
CONFIG_SOC_EFR32BG24L010F768IM40
CONFIG_SOC_EFR32BG24L210F768IM40
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg24/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg24/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_EFR32BG24A010F1024IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG24A010F1024IM40)、[`CONFIG_SOC_EFR32BG24A010F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG24A010F1024IM48)、[`CONFIG_SOC_EFR32BG24A020F1024IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG24A020F1024IM40)、[`CONFIG_SOC_EFR32BG24A020F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG24A020F1024IM48)、[`CONFIG_SOC_EFR32BG24B110F1536IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG24B110F1536IM48)、[`CONFIG_SOC_EFR32BG24B210F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG24B210F1024IM48)、[`CONFIG_SOC_EFR32BG24B220F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG24B220F1024IM48)、[`CONFIG_SOC_EFR32BG24L010F768IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG24L010F768IM40)、[`CONFIG_SOC_EFR32BG24L210F768IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG24L210F768IM40)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32BG24A010F1024IM40`、`CONFIG_SOC_EFR32BG24A010F1024IM48`、`CONFIG_SOC_EFR32BG24A020F1024IM40`、`CONFIG_SOC_EFR32BG24A020F1024IM48`、`CONFIG_SOC_EFR32BG24B110F1536IM48`、`CONFIG_SOC_EFR32BG24B210F1024IM48`、`CONFIG_SOC_EFR32BG24B220F1024IM48`、`CONFIG_SOC_EFR32BG24L010F768IM40`、`CONFIG_SOC_EFR32BG24L210F768IM40`。

<a id="CONFIG_SOC_SERIES_EFR32BG26"></a>

## 308.50 `CONFIG_SOC_SERIES_EFR32BG26`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32BG26（Blue Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG26
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32BG26B311F1024IL136
CONFIG_SOC_EFR32BG26B311F1024IM68
CONFIG_SOC_EFR32BG26B311F2048IL136
CONFIG_SOC_EFR32BG26B311F2048IM48
CONFIG_SOC_EFR32BG26B311F2048IM68
CONFIG_SOC_EFR32BG26B321F1024IM68
CONFIG_SOC_EFR32BG26B321F2048IM48
CONFIG_SOC_EFR32BG26B321F2048IM68
CONFIG_SOC_EFR32BG26B410F3200IM48
CONFIG_SOC_EFR32BG26B411F3200IM48
CONFIG_SOC_EFR32BG26B420F3200IM48
CONFIG_SOC_EFR32BG26B421F3200IM48
CONFIG_SOC_EFR32BG26B510F3200IL136
CONFIG_SOC_EFR32BG26B510F3200IM48
CONFIG_SOC_EFR32BG26B510F3200IM68
CONFIG_SOC_EFR32BG26B511F3200IL136
CONFIG_SOC_EFR32BG26B511F3200IM48
CONFIG_SOC_EFR32BG26B511F3200IM68
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg26/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg26/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_EFR32BG26B311F1024IL136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B311F1024IL136)、[`CONFIG_SOC_EFR32BG26B311F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B311F1024IM68)、[`CONFIG_SOC_EFR32BG26B311F2048IL136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B311F2048IL136)、[`CONFIG_SOC_EFR32BG26B311F2048IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B311F2048IM48)、[`CONFIG_SOC_EFR32BG26B311F2048IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B311F2048IM68)、[`CONFIG_SOC_EFR32BG26B321F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B321F1024IM68)、[`CONFIG_SOC_EFR32BG26B321F2048IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B321F2048IM48)、[`CONFIG_SOC_EFR32BG26B321F2048IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B321F2048IM68)、[`CONFIG_SOC_EFR32BG26B410F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B410F3200IM48)、[`CONFIG_SOC_EFR32BG26B411F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B411F3200IM48)、[`CONFIG_SOC_EFR32BG26B420F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B420F3200IM48)、[`CONFIG_SOC_EFR32BG26B421F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B421F3200IM48)、[`CONFIG_SOC_EFR32BG26B510F3200IL136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B510F3200IL136)、[`CONFIG_SOC_EFR32BG26B510F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B510F3200IM48)、[`CONFIG_SOC_EFR32BG26B510F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B510F3200IM68)、[`CONFIG_SOC_EFR32BG26B511F3200IL136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B511F3200IL136)、[`CONFIG_SOC_EFR32BG26B511F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B511F3200IM48)、[`CONFIG_SOC_EFR32BG26B511F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG26B511F3200IM68)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32BG26B311F1024IL136`、`CONFIG_SOC_EFR32BG26B311F1024IM68`、`CONFIG_SOC_EFR32BG26B311F2048IL136`、`CONFIG_SOC_EFR32BG26B311F2048IM48`、`CONFIG_SOC_EFR32BG26B311F2048IM68`、`CONFIG_SOC_EFR32BG26B321F1024IM68`、`CONFIG_SOC_EFR32BG26B321F2048IM48`、`CONFIG_SOC_EFR32BG26B321F2048IM68`、`CONFIG_SOC_EFR32BG26B410F3200IM48`、`CONFIG_SOC_EFR32BG26B411F3200IM48`、`CONFIG_SOC_EFR32BG26B420F3200IM48`、`CONFIG_SOC_EFR32BG26B421F3200IM48`、`CONFIG_SOC_EFR32BG26B510F3200IL136`、`CONFIG_SOC_EFR32BG26B510F3200IM48`、`CONFIG_SOC_EFR32BG26B510F3200IM68`、`CONFIG_SOC_EFR32BG26B511F3200IL136`、`CONFIG_SOC_EFR32BG26B511F3200IM48`、`CONFIG_SOC_EFR32BG26B511F3200IM68`。

<a id="CONFIG_SOC_SERIES_EFR32BG27"></a>

## 308.51 `CONFIG_SOC_SERIES_EFR32BG27`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32BG27（Blue Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG27
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32BG27C140F768IM32
CONFIG_SOC_EFR32BG27C140F768IM40
CONFIG_SOC_EFR32BG27C230F768IM32
CONFIG_SOC_EFR32BG27C230F768IM40
CONFIG_SOC_EFR32BG27C320F768GJ39
CONFIG_SOC_EFR32BG27C320F768IJ39
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg27/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg27/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_EFR32BG27C140F768IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG27C140F768IM32)、[`CONFIG_SOC_EFR32BG27C140F768IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG27C140F768IM40)、[`CONFIG_SOC_EFR32BG27C230F768IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG27C230F768IM32)、[`CONFIG_SOC_EFR32BG27C230F768IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG27C230F768IM40)、[`CONFIG_SOC_EFR32BG27C320F768GJ39`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG27C320F768GJ39)、[`CONFIG_SOC_EFR32BG27C320F768IJ39`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG27C320F768IJ39)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32BG27C140F768IM32`、`CONFIG_SOC_EFR32BG27C140F768IM40`、`CONFIG_SOC_EFR32BG27C230F768IM32`、`CONFIG_SOC_EFR32BG27C230F768IM40`、`CONFIG_SOC_EFR32BG27C320F768GJ39`、`CONFIG_SOC_EFR32BG27C320F768IJ39`。

<a id="CONFIG_SOC_SERIES_EFR32BG29"></a>

## 308.52 `CONFIG_SOC_SERIES_EFR32BG29`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32BG29（Blue Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG29
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32BG29B140F1024IM40
CONFIG_SOC_EFR32BG29B220F1024CJ45
CONFIG_SOC_EFR32BG29B221F1024CJ45
CONFIG_SOC_EFR32BG29B230F1024CM40
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg29/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg29/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_EFR32BG29B140F1024IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG29B140F1024IM40)、[`CONFIG_SOC_EFR32BG29B220F1024CJ45`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG29B220F1024CJ45)、[`CONFIG_SOC_EFR32BG29B221F1024CJ45`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG29B221F1024CJ45)、[`CONFIG_SOC_EFR32BG29B230F1024CM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32BG29B230F1024CM40)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32BG29B140F1024IM40`、`CONFIG_SOC_EFR32BG29B220F1024CJ45`、`CONFIG_SOC_EFR32BG29B221F1024CJ45`、`CONFIG_SOC_EFR32BG29B230F1024CM40`。

<a id="CONFIG_SOC_SERIES_EFR32FG13P"></a>

## 308.53 `CONFIG_SOC_SERIES_EFR32FG13P`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32FG13P（Flex Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32FG13P233F512GM48
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efr32fg13p/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efr32fg13p/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_EFR32FG13P233F512GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG13P233F512GM48)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_EFR32FG13P233F512GM48`。

<a id="CONFIG_SOC_SERIES_EFR32FG1P"></a>

## 308.54 `CONFIG_SOC_SERIES_EFR32FG1P`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32FG1P（Flex Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32FG1P133F256GM48
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efr32fg1p/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efr32fg1p/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_EFR32FG1P133F256GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG1P133F256GM48)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_EFR32FG1P133F256GM48`。

<a id="CONFIG_SOC_SERIES_EFR32FG28"></a>

## 308.55 `CONFIG_SOC_SERIES_EFR32FG28`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32FG28 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG28
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32FG28A010F1024GM48
CONFIG_SOC_EFR32FG28A010F1024GM68
CONFIG_SOC_EFR32FG28A110F1024GM48
CONFIG_SOC_EFR32FG28A110F1024GM68
CONFIG_SOC_EFR32FG28A112F1024GM48
CONFIG_SOC_EFR32FG28A112F1024GM68
CONFIG_SOC_EFR32FG28A120F1024GM48
CONFIG_SOC_EFR32FG28A120F1024GM68
CONFIG_SOC_EFR32FG28A122F1024GM48
CONFIG_SOC_EFR32FG28A122F1024GM68
CONFIG_SOC_EFR32FG28B310F1024IM48
CONFIG_SOC_EFR32FG28B310F1024IM68
CONFIG_SOC_EFR32FG28B312F1024IM48
CONFIG_SOC_EFR32FG28B312F1024IM68
CONFIG_SOC_EFR32FG28B320F1024IM48
CONFIG_SOC_EFR32FG28B320F1024IM68
CONFIG_SOC_EFR32FG28B322F1024IM48
CONFIG_SOC_EFR32FG28B322F1024IM68
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg28/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg28/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_EFR32FG28A010F1024GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28A010F1024GM48)、[`CONFIG_SOC_EFR32FG28A010F1024GM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28A010F1024GM68)、[`CONFIG_SOC_EFR32FG28A110F1024GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28A110F1024GM48)、[`CONFIG_SOC_EFR32FG28A110F1024GM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28A110F1024GM68)、[`CONFIG_SOC_EFR32FG28A112F1024GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28A112F1024GM48)、[`CONFIG_SOC_EFR32FG28A112F1024GM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28A112F1024GM68)、[`CONFIG_SOC_EFR32FG28A120F1024GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28A120F1024GM48)、[`CONFIG_SOC_EFR32FG28A120F1024GM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28A120F1024GM68)、[`CONFIG_SOC_EFR32FG28A122F1024GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28A122F1024GM48)、[`CONFIG_SOC_EFR32FG28A122F1024GM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28A122F1024GM68)、[`CONFIG_SOC_EFR32FG28B310F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28B310F1024IM48)、[`CONFIG_SOC_EFR32FG28B310F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28B310F1024IM68)、[`CONFIG_SOC_EFR32FG28B312F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28B312F1024IM48)、[`CONFIG_SOC_EFR32FG28B312F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28B312F1024IM68)、[`CONFIG_SOC_EFR32FG28B320F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28B320F1024IM48)、[`CONFIG_SOC_EFR32FG28B320F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28B320F1024IM68)、[`CONFIG_SOC_EFR32FG28B322F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28B322F1024IM48)、[`CONFIG_SOC_EFR32FG28B322F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32FG28B322F1024IM68)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32FG28A010F1024GM48`、`CONFIG_SOC_EFR32FG28A010F1024GM68`、`CONFIG_SOC_EFR32FG28A110F1024GM48`、`CONFIG_SOC_EFR32FG28A110F1024GM68`、`CONFIG_SOC_EFR32FG28A112F1024GM48`、`CONFIG_SOC_EFR32FG28A112F1024GM68`、`CONFIG_SOC_EFR32FG28A120F1024GM48`、`CONFIG_SOC_EFR32FG28A120F1024GM68`、`CONFIG_SOC_EFR32FG28A122F1024GM48`、`CONFIG_SOC_EFR32FG28A122F1024GM68`、`CONFIG_SOC_EFR32FG28B310F1024IM48`、`CONFIG_SOC_EFR32FG28B310F1024IM68`、`CONFIG_SOC_EFR32FG28B312F1024IM48`、`CONFIG_SOC_EFR32FG28B312F1024IM68`、`CONFIG_SOC_EFR32FG28B320F1024IM48`、`CONFIG_SOC_EFR32FG28B320F1024IM68`、`CONFIG_SOC_EFR32FG28B322F1024IM48`、`CONFIG_SOC_EFR32FG28B322F1024IM68`。

<a id="CONFIG_SOC_SERIES_EFR32MG12P"></a>

## 308.56 `CONFIG_SOC_SERIES_EFR32MG12P`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32MG12P（Mighty Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32MG12P332F1024GL125
CONFIG_SOC_EFR32MG12P433F1024GM68
CONFIG_SOC_EFR32MG12P432F1024GL125
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efr32mg12p/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efr32mg12p/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_EFR32MG12P332F1024GL125`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG12P332F1024GL125)、[`CONFIG_SOC_EFR32MG12P433F1024GM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG12P433F1024GM68)、[`CONFIG_SOC_EFR32MG12P432F1024GL125`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG12P432F1024GL125)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_EFR32MG12P332F1024GL125`、`CONFIG_SOC_EFR32MG12P433F1024GM68`、`CONFIG_SOC_EFR32MG12P432F1024GL125`。

<a id="CONFIG_SOC_SERIES_EFR32MG13P"></a>

## 308.57 `CONFIG_SOC_SERIES_EFR32MG13P`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32MG13P（Mighty Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32MG13P732F512GM48
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efr32mg13p/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efr32mg13p/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_EFR32MG13P732F512GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG13P732F512GM48)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_EFR32MG13P732F512GM48`。

<a id="CONFIG_SOC_SERIES_EFR32MG21"></a>

## 308.58 `CONFIG_SOC_SERIES_EFR32MG21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32MG21（Mighty Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG21
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32MG21A020F1024IM32
CONFIG_SOC_EFR32MG21B010F512IM32
CONFIG_SOC_EFR32MG21B010F768IM32
CONFIG_SOC_EFR32MG21B010F1024IM32
CONFIG_SOC_EFR32MG21B020F512IM32
CONFIG_SOC_EFR32MG21B020F768IM32
CONFIG_SOC_EFR32MG21B020F1024IM32
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg21/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg21/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG21`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`CONFIG_SOC_EFR32MG21A020F1024IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG21A020F1024IM32)、[`CONFIG_SOC_EFR32MG21B010F512IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG21B010F512IM32)、[`CONFIG_SOC_EFR32MG21B010F768IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG21B010F768IM32)、[`CONFIG_SOC_EFR32MG21B010F1024IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG21B010F1024IM32)、[`CONFIG_SOC_EFR32MG21B020F512IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG21B020F512IM32)、[`CONFIG_SOC_EFR32MG21B020F768IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG21B020F768IM32)、[`CONFIG_SOC_EFR32MG21B020F1024IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG21B020F1024IM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32MG21A020F1024IM32`、`CONFIG_SOC_EFR32MG21B010F512IM32`、`CONFIG_SOC_EFR32MG21B010F768IM32`、`CONFIG_SOC_EFR32MG21B010F1024IM32`、`CONFIG_SOC_EFR32MG21B020F512IM32`、`CONFIG_SOC_EFR32MG21B020F768IM32`、`CONFIG_SOC_EFR32MG21B020F1024IM32`。

<a id="CONFIG_SOC_SERIES_EFR32MG22"></a>

## 308.59 `CONFIG_SOC_SERIES_EFR32MG22`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32MG22（Mighty Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG22
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32MG22C224F512IM40
CONFIG_SOC_EFR32MG22C224F512IM32
CONFIG_SOC_EFR32MG22C224F512GN32
CONFIG_SOC_EFR32MG22E224F512IM40
CONFIG_SOC_EFR32MG22E224F512IM32
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg22/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg22/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_EFR32MG22C224F512IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG22C224F512IM40)、[`CONFIG_SOC_EFR32MG22C224F512IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG22C224F512IM32)、[`CONFIG_SOC_EFR32MG22C224F512GN32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG22C224F512GN32)、[`CONFIG_SOC_EFR32MG22E224F512IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG22E224F512IM40)、[`CONFIG_SOC_EFR32MG22E224F512IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG22E224F512IM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32MG22C224F512IM40`、`CONFIG_SOC_EFR32MG22C224F512IM32`、`CONFIG_SOC_EFR32MG22C224F512GN32`、`CONFIG_SOC_EFR32MG22E224F512IM40`、`CONFIG_SOC_EFR32MG22E224F512IM32`。

<a id="CONFIG_SOC_SERIES_EFR32MG24"></a>

## 308.60 `CONFIG_SOC_SERIES_EFR32MG24`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32MG24（Mighty Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG24
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32MG24B010F1024IM48
CONFIG_SOC_EFR32MG24B010F1536IM40
CONFIG_SOC_EFR32MG24B010F1536IM48
CONFIG_SOC_EFR32MG24B020F1024IM48
CONFIG_SOC_EFR32MG24B020F1536IM40
CONFIG_SOC_EFR32MG24B020F1536IM48
CONFIG_SOC_EFR32MG24B110F1536IM48
CONFIG_SOC_EFR32MG24B120F1536IM48
CONFIG_SOC_EFR32MG24B210F1536IM48
CONFIG_SOC_EFR32MG24B220F1536IM48
CONFIG_SOC_EFR32MG24B310F1536IM48
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg24/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg24/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_EFR32MG24B010F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG24B010F1024IM48)、[`CONFIG_SOC_EFR32MG24B010F1536IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG24B010F1536IM40)、[`CONFIG_SOC_EFR32MG24B010F1536IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG24B010F1536IM48)、[`CONFIG_SOC_EFR32MG24B020F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG24B020F1024IM48)、[`CONFIG_SOC_EFR32MG24B020F1536IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG24B020F1536IM40)、[`CONFIG_SOC_EFR32MG24B020F1536IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG24B020F1536IM48)、[`CONFIG_SOC_EFR32MG24B110F1536IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG24B110F1536IM48)、[`CONFIG_SOC_EFR32MG24B120F1536IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG24B120F1536IM48)、[`CONFIG_SOC_EFR32MG24B210F1536IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG24B210F1536IM48)、[`CONFIG_SOC_EFR32MG24B220F1536IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG24B220F1536IM48)、[`CONFIG_SOC_EFR32MG24B310F1536IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG24B310F1536IM48)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32MG24B010F1024IM48`、`CONFIG_SOC_EFR32MG24B010F1536IM40`、`CONFIG_SOC_EFR32MG24B010F1536IM48`、`CONFIG_SOC_EFR32MG24B020F1024IM48`、`CONFIG_SOC_EFR32MG24B020F1536IM40`、`CONFIG_SOC_EFR32MG24B020F1536IM48`、`CONFIG_SOC_EFR32MG24B110F1536IM48`、`CONFIG_SOC_EFR32MG24B120F1536IM48`、`CONFIG_SOC_EFR32MG24B210F1536IM48`、`CONFIG_SOC_EFR32MG24B220F1536IM48`、`CONFIG_SOC_EFR32MG24B310F1536IM48`。

<a id="CONFIG_SOC_SERIES_EFR32MG26"></a>

## 308.61 `CONFIG_SOC_SERIES_EFR32MG26`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32MG26（Mighty Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG26
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32MG26B521F3200IM68
CONFIG_SOC_EFR32MG26B521F3200IM48
CONFIG_SOC_EFR32MG26B520F3200IM68
CONFIG_SOC_EFR32MG26B520F3200IM48
CONFIG_SOC_EFR32MG26B511F3200IM68
CONFIG_SOC_EFR32MG26B511F3200IM48
CONFIG_SOC_EFR32MG26B511F3200IL136
CONFIG_SOC_EFR32MG26B510F3200IM68
CONFIG_SOC_EFR32MG26B510F3200IM48
CONFIG_SOC_EFR32MG26B510F3200IL136
CONFIG_SOC_EFR32MG26B421F3200IM68
CONFIG_SOC_EFR32MG26B421F3200IM48
CONFIG_SOC_EFR32MG26B420F3200IM68
CONFIG_SOC_EFR32MG26B420F3200IM48
CONFIG_SOC_EFR32MG26B411F3200IM68
CONFIG_SOC_EFR32MG26B411F3200IM48
CONFIG_SOC_EFR32MG26B410F3200IM68
CONFIG_SOC_EFR32MG26B410F3200IM48
CONFIG_SOC_EFR32MG26B311F3200IL136
CONFIG_SOC_EFR32MG26B221F3200IM48
CONFIG_SOC_EFR32MG26B221F2048IM68
CONFIG_SOC_EFR32MG26B211F3200IM48
CONFIG_SOC_EFR32MG26B211F2048IM68
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg26/Kconfig.soc:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg26/Kconfig.soc#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_EFR32MG26B521F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B521F3200IM68)、[`CONFIG_SOC_EFR32MG26B521F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B521F3200IM48)、[`CONFIG_SOC_EFR32MG26B520F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B520F3200IM68)、[`CONFIG_SOC_EFR32MG26B520F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B520F3200IM48)、[`CONFIG_SOC_EFR32MG26B511F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B511F3200IM68)、[`CONFIG_SOC_EFR32MG26B511F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B511F3200IM48)、[`CONFIG_SOC_EFR32MG26B511F3200IL136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B511F3200IL136)、[`CONFIG_SOC_EFR32MG26B510F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B510F3200IM68)、[`CONFIG_SOC_EFR32MG26B510F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B510F3200IM48)、[`CONFIG_SOC_EFR32MG26B510F3200IL136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B510F3200IL136)、[`CONFIG_SOC_EFR32MG26B421F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B421F3200IM68)、[`CONFIG_SOC_EFR32MG26B421F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B421F3200IM48)、[`CONFIG_SOC_EFR32MG26B420F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B420F3200IM68)、[`CONFIG_SOC_EFR32MG26B420F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B420F3200IM48)、[`CONFIG_SOC_EFR32MG26B411F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B411F3200IM68)、[`CONFIG_SOC_EFR32MG26B411F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B411F3200IM48)、[`CONFIG_SOC_EFR32MG26B410F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B410F3200IM68)、[`CONFIG_SOC_EFR32MG26B410F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B410F3200IM48)、[`CONFIG_SOC_EFR32MG26B311F3200IL136`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B311F3200IL136)、[`CONFIG_SOC_EFR32MG26B221F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B221F3200IM48)、[`CONFIG_SOC_EFR32MG26B221F2048IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B221F2048IM68)、[`CONFIG_SOC_EFR32MG26B211F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B211F3200IM48)、[`CONFIG_SOC_EFR32MG26B211F2048IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG26B211F2048IM68)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32MG26B521F3200IM68`、`CONFIG_SOC_EFR32MG26B521F3200IM48`、`CONFIG_SOC_EFR32MG26B520F3200IM68`、`CONFIG_SOC_EFR32MG26B520F3200IM48`、`CONFIG_SOC_EFR32MG26B511F3200IM68`、`CONFIG_SOC_EFR32MG26B511F3200IM48`、`CONFIG_SOC_EFR32MG26B511F3200IL136`、`CONFIG_SOC_EFR32MG26B510F3200IM68`、`CONFIG_SOC_EFR32MG26B510F3200IM48`、`CONFIG_SOC_EFR32MG26B510F3200IL136`、`CONFIG_SOC_EFR32MG26B421F3200IM68`、`CONFIG_SOC_EFR32MG26B421F3200IM48`、`CONFIG_SOC_EFR32MG26B420F3200IM68`、`CONFIG_SOC_EFR32MG26B420F3200IM48`、`CONFIG_SOC_EFR32MG26B411F3200IM68`、`CONFIG_SOC_EFR32MG26B411F3200IM48`、`CONFIG_SOC_EFR32MG26B410F3200IM68`、`CONFIG_SOC_EFR32MG26B410F3200IM48`、`CONFIG_SOC_EFR32MG26B311F3200IL136`、`CONFIG_SOC_EFR32MG26B221F3200IM48`、`CONFIG_SOC_EFR32MG26B221F2048IM68`、`CONFIG_SOC_EFR32MG26B211F3200IM48`、`CONFIG_SOC_EFR32MG26B211F2048IM68`。

<a id="CONFIG_SOC_SERIES_EFR32MG27"></a>

## 308.62 `CONFIG_SOC_SERIES_EFR32MG27`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32MG27（Mighty Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG27
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32MG27C140F768IM32
CONFIG_SOC_EFR32MG27C140F768IM40
CONFIG_SOC_EFR32MG27C230F768IM32
CONFIG_SOC_EFR32MG27C230F768IM40
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg27/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg27/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG27)、[`CONFIG_SOC_EFR32MG27C140F768IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG27C140F768IM32)、[`CONFIG_SOC_EFR32MG27C140F768IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG27C140F768IM40)、[`CONFIG_SOC_EFR32MG27C230F768IM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG27C230F768IM32)、[`CONFIG_SOC_EFR32MG27C230F768IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG27C230F768IM40)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32MG27C140F768IM32`、`CONFIG_SOC_EFR32MG27C140F768IM40`、`CONFIG_SOC_EFR32MG27C230F768IM32`、`CONFIG_SOC_EFR32MG27C230F768IM40`。

<a id="CONFIG_SOC_SERIES_EFR32MG29"></a>

## 308.63 `CONFIG_SOC_SERIES_EFR32MG29`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32MG29（Mighty Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG29
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32MG29B140F1024IM40
CONFIG_SOC_EFR32MG29B230F1024CM40
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg29/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg29/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG29`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG29)、[`CONFIG_SOC_EFR32MG29B140F1024IM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG29B140F1024IM40)、[`CONFIG_SOC_EFR32MG29B230F1024CM40`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32MG29B230F1024CM40)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32MG29B140F1024IM40`、`CONFIG_SOC_EFR32MG29B230F1024CM40`。

<a id="CONFIG_SOC_SERIES_EFR32ZG23"></a>

## 308.64 `CONFIG_SOC_SERIES_EFR32ZG23`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32ZG23 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG23
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32ZG23B020F512IM48
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg23/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg23/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG23`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`CONFIG_SOC_EFR32ZG23B020F512IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG23B020F512IM48)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32ZG23B020F512IM48`。

<a id="CONFIG_SOC_SERIES_EFR32ZG28"></a>

## 308.65 `CONFIG_SOC_SERIES_EFR32ZG28`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32ZG28 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG28
```

**被选择（Selected by）**

```text
CONFIG_SOC_EFR32ZG28A110F1024GM48
CONFIG_SOC_EFR32ZG28A110F1024GM68
CONFIG_SOC_EFR32ZG28A112F1024GM48
CONFIG_SOC_EFR32ZG28A112F1024GM68
CONFIG_SOC_EFR32ZG28A120F1024GM48
CONFIG_SOC_EFR32ZG28A120F1024GM68
CONFIG_SOC_EFR32ZG28A122F1024GM48
CONFIG_SOC_EFR32ZG28A122F1024GM68
CONFIG_SOC_EFR32ZG28B310F1024IM48
CONFIG_SOC_EFR32ZG28B310F1024IM68
CONFIG_SOC_EFR32ZG28B312F1024IM48
CONFIG_SOC_EFR32ZG28B312F1024IM68
CONFIG_SOC_EFR32ZG28B320F1024IM48
CONFIG_SOC_EFR32ZG28B320F1024IM68
CONFIG_SOC_EFR32ZG28B322F1024IM48
CONFIG_SOC_EFR32ZG28B322F1024IM68
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg28/Kconfig.soc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg28/Kconfig.soc#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG28`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`CONFIG_SOC_EFR32ZG28A110F1024GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28A110F1024GM48)、[`CONFIG_SOC_EFR32ZG28A110F1024GM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28A110F1024GM68)、[`CONFIG_SOC_EFR32ZG28A112F1024GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28A112F1024GM48)、[`CONFIG_SOC_EFR32ZG28A112F1024GM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28A112F1024GM68)、[`CONFIG_SOC_EFR32ZG28A120F1024GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28A120F1024GM48)、[`CONFIG_SOC_EFR32ZG28A120F1024GM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28A120F1024GM68)、[`CONFIG_SOC_EFR32ZG28A122F1024GM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28A122F1024GM48)、[`CONFIG_SOC_EFR32ZG28A122F1024GM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28A122F1024GM68)、[`CONFIG_SOC_EFR32ZG28B310F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28B310F1024IM48)、[`CONFIG_SOC_EFR32ZG28B310F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28B310F1024IM68)、[`CONFIG_SOC_EFR32ZG28B312F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28B312F1024IM48)、[`CONFIG_SOC_EFR32ZG28B312F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28B312F1024IM68)、[`CONFIG_SOC_EFR32ZG28B320F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28B320F1024IM48)、[`CONFIG_SOC_EFR32ZG28B320F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28B320F1024IM68)、[`CONFIG_SOC_EFR32ZG28B322F1024IM48`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28B322F1024IM48)、[`CONFIG_SOC_EFR32ZG28B322F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EFR32ZG28B322F1024IM68)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_EFR32ZG28A110F1024GM48`、`CONFIG_SOC_EFR32ZG28A110F1024GM68`、`CONFIG_SOC_EFR32ZG28A112F1024GM48`、`CONFIG_SOC_EFR32ZG28A112F1024GM68`、`CONFIG_SOC_EFR32ZG28A120F1024GM48`、`CONFIG_SOC_EFR32ZG28A120F1024GM68`、`CONFIG_SOC_EFR32ZG28A122F1024GM48`、`CONFIG_SOC_EFR32ZG28A122F1024GM68`、`CONFIG_SOC_EFR32ZG28B310F1024IM48`、`CONFIG_SOC_EFR32ZG28B310F1024IM68`、`CONFIG_SOC_EFR32ZG28B312F1024IM48`、`CONFIG_SOC_EFR32ZG28B312F1024IM68`、`CONFIG_SOC_EFR32ZG28B320F1024IM48`、`CONFIG_SOC_EFR32ZG28B320F1024IM68`、`CONFIG_SOC_EFR32ZG28B322F1024IM48`、`CONFIG_SOC_EFR32ZG28B322F1024IM68`。

<a id="CONFIG_SOC_SERIES_MGM24"></a>

## 308.66 `CONFIG_SOC_SERIES_MGM24`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs MGM240（Mighty Gecko）系列微控制器模组（Series MCU modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG24
```

**被选择（Selected by）**

```text
CONFIG_SOC_MGM240PA22VNA
CONFIG_SOC_MGM240PA32VNA
CONFIG_SOC_MGM240PA32VNN
CONFIG_SOC_MGM240PB22VNA
CONFIG_SOC_MGM240PB32VNA
CONFIG_SOC_MGM240PB32VNN
CONFIG_SOC_MGM240SA22VNA
CONFIG_SOC_MGM240SD22VNA
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg24/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg24/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`CONFIG_SOC_MGM240PA22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM240PA22VNA)、[`CONFIG_SOC_MGM240PA32VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM240PA32VNA)、[`CONFIG_SOC_MGM240PA32VNN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM240PA32VNN)、[`CONFIG_SOC_MGM240PB22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM240PB22VNA)、[`CONFIG_SOC_MGM240PB32VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM240PB32VNA)、[`CONFIG_SOC_MGM240PB32VNN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM240PB32VNN)、[`CONFIG_SOC_MGM240SA22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM240SA22VNA)、[`CONFIG_SOC_MGM240SD22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM240SD22VNA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MGM240PA22VNA`、`CONFIG_SOC_MGM240PA32VNA`、`CONFIG_SOC_MGM240PA32VNN`、`CONFIG_SOC_MGM240PB22VNA`、`CONFIG_SOC_MGM240PB32VNA`、`CONFIG_SOC_MGM240PB32VNN`、`CONFIG_SOC_MGM240SA22VNA`、`CONFIG_SOC_MGM240SD22VNA`。

<a id="CONFIG_SOC_SERIES_MGM26"></a>

## 308.67 `CONFIG_SOC_SERIES_MGM26`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs MGM260（Mighty Gecko）系列微控制器模组（Series MCU modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S2_XG26
```

**被选择（Selected by）**

```text
CONFIG_SOC_MGM260PB22VNA
CONFIG_SOC_MGM260PB32VNA
CONFIG_SOC_MGM260PB32VNN
CONFIG_SOC_MGM260PD22VNA
CONFIG_SOC_MGM260PD32VNA
CONFIG_SOC_MGM260PD32VNN
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg26/Kconfig.soc:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg26/Kconfig.soc#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2_XG26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`CONFIG_SOC_MGM260PB22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM260PB22VNA)、[`CONFIG_SOC_MGM260PB32VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM260PB32VNA)、[`CONFIG_SOC_MGM260PB32VNN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM260PB32VNN)、[`CONFIG_SOC_MGM260PD22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM260PD22VNA)、[`CONFIG_SOC_MGM260PD32VNA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM260PD32VNA)、[`CONFIG_SOC_MGM260PD32VNN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MGM260PD32VNN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MGM260PB22VNA`、`CONFIG_SOC_MGM260PB32VNA`、`CONFIG_SOC_MGM260PB32VNN`、`CONFIG_SOC_MGM260PD22VNA`、`CONFIG_SOC_MGM260PD32VNA`、`CONFIG_SOC_MGM260PD32VNN`。

<a id="CONFIG_SOC_SERIES_SIBG301"></a>

## 308.68 `CONFIG_SOC_SERIES_SIBG301`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs SiBG301 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
```

**被选择（Selected by）**

```text
CONFIG_SOC_SIBG301M104LGH
CONFIG_SOC_SIBG301M104LGL
CONFIG_SOC_SIBG301M104LIH
CONFIG_SOC_SIBG301M104LIL
CONFIG_SOC_SIBG301M104XIL
CONFIG_SOC_SIBG301M114KGH
CONFIG_SOC_SIBG301M114KIH
```

**定义位置（Location）**：[`soc/silabs/silabs_s3/six301/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s3/six301/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_SOC_SIBG301M104LGH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIBG301M104LGH)、[`CONFIG_SOC_SIBG301M104LGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIBG301M104LGL)、[`CONFIG_SOC_SIBG301M104LIH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIBG301M104LIH)、[`CONFIG_SOC_SIBG301M104LIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIBG301M104LIL)、[`CONFIG_SOC_SIBG301M104XIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIBG301M104XIL)、[`CONFIG_SOC_SIBG301M114KGH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIBG301M114KGH)、[`CONFIG_SOC_SIBG301M114KIH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIBG301M114KIH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SIBG301M104LGH`、`CONFIG_SOC_SIBG301M104LGL`、`CONFIG_SOC_SIBG301M104LIH`、`CONFIG_SOC_SIBG301M104LIL`、`CONFIG_SOC_SIBG301M104XIL`、`CONFIG_SOC_SIBG301M114KGH`、`CONFIG_SOC_SIBG301M114KIH`。

<a id="CONFIG_SOC_SERIES_SIM3U"></a>

## 308.69 `CONFIG_SOC_SERIES_SIM3U`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 SiM3U 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_SIM3
```

**被选择（Selected by）**

```text
CONFIG_SOC_SIM3U167BGM
CONFIG_SOC_SIM3U167AGQ
```

**定义位置（Location）**：[`soc/silabs/silabs_sim3/sim3u/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_sim3/sim3u/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_SIM3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIM3)、[`CONFIG_SOC_SIM3U167BGM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIM3U167BGM)、[`CONFIG_SOC_SIM3U167AGQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIM3U167AGQ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIM3`、`CONFIG_SOC_SIM3U167BGM`、`CONFIG_SOC_SIM3U167AGQ`。

<a id="CONFIG_SOC_SERIES_SIMG301"></a>

## 308.70 `CONFIG_SOC_SERIES_SIMG301`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs SiMG301 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_S3_SIX301
```

**被选择（Selected by）**

```text
CONFIG_SOC_SIMG301M103LIH
CONFIG_SOC_SIMG301M103WIH
CONFIG_SOC_SIMG301M104LGH
CONFIG_SOC_SIMG301M104LGL
CONFIG_SOC_SIMG301M104LIH
CONFIG_SOC_SIMG301M104LIL
CONFIG_SOC_SIMG301M104XIL
CONFIG_SOC_SIMG301M113WIH
CONFIG_SOC_SIMG301M114KGH
CONFIG_SOC_SIMG301M114KIH
CONFIG_SOC_SIMG301M114LGH
CONFIG_SOC_SIMG301M114LIH
```

**定义位置（Location）**：[`soc/silabs/silabs_s3/six301/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s3/six301/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S3_SIX301`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_FAMILY_SILABS_S3_SIX301)、[`CONFIG_SOC_SIMG301M103LIH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIMG301M103LIH)、[`CONFIG_SOC_SIMG301M103WIH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIMG301M103WIH)、[`CONFIG_SOC_SIMG301M104LGH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIMG301M104LGH)、[`CONFIG_SOC_SIMG301M104LGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIMG301M104LGL)、[`CONFIG_SOC_SIMG301M104LIH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIMG301M104LIH)、[`CONFIG_SOC_SIMG301M104LIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIMG301M104LIL)、[`CONFIG_SOC_SIMG301M104XIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIMG301M104XIL)、[`CONFIG_SOC_SIMG301M113WIH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIMG301M113WIH)、[`CONFIG_SOC_SIMG301M114KGH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIMG301M114KGH)、[`CONFIG_SOC_SIMG301M114KIH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIMG301M114KIH)、[`CONFIG_SOC_SIMG301M114LGH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIMG301M114LGH)、[`CONFIG_SOC_SIMG301M114LIH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIMG301M114LIH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SIMG301M103LIH`、`CONFIG_SOC_SIMG301M103WIH`、`CONFIG_SOC_SIMG301M104LGH`、`CONFIG_SOC_SIMG301M104LGL`、`CONFIG_SOC_SIMG301M104LIH`、`CONFIG_SOC_SIMG301M104LIL`、`CONFIG_SOC_SIMG301M104XIL`、`CONFIG_SOC_SIMG301M113WIH`、`CONFIG_SOC_SIMG301M114KGH`、`CONFIG_SOC_SIMG301M114KIH`、`CONFIG_SOC_SIMG301M114LGH`、`CONFIG_SOC_SIMG301M114LIH`。

<a id="CONFIG_SOC_SERIES_SIWG917"></a>

## 308.71 `CONFIG_SOC_SERIES_SIWG917`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SiWG917 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**被选择（Selected by）**

```text
CONFIG_SOC_SIWG917M111MGTBA
CONFIG_SOC_SIWG917Y111MGABA
```

**定义位置（Location）**：[`soc/silabs/silabs_siwx91x/siwg917/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_siwx91x/siwg917/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SOC_SIWG917M111MGTBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIWG917M111MGTBA)、[`CONFIG_SOC_SIWG917Y111MGABA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SIWG917Y111MGABA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_SOC_SIWG917M111MGTBA`、`CONFIG_SOC_SIWG917Y111MGABA`。

<a id="CONFIG_SOC_VENDOR_SILABS_HAS_RADIO"></a>

## 308.72 `CONFIG_SOC_VENDOR_SILABS_HAS_RADIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用后，表示 SoC 具有无线电物理层（Radio PHY）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_S1 || CONFIG_SOC_FAMILY_SILABS_S2 || CONFIG_SOC_FAMILY_SILABS_S3
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_EFR32BG13P
CONFIG_SOC_SERIES_EFR32FG13P
CONFIG_SOC_SERIES_EFR32FG1P
CONFIG_SOC_SERIES_EFR32MG12P
CONFIG_SOC_SERIES_EFR32MG13P
CONFIG_SOC_SERIES_EFR32BG21
CONFIG_SOC_SERIES_EFR32MG21
CONFIG_SOC_SERIES_EFR32BG22
CONFIG_SOC_SERIES_EFR32MG22
CONFIG_SOC_SERIES_BGM22
CONFIG_SOC_SERIES_EFR32ZG23
CONFIG_SOC_SERIES_EFR32BG24
CONFIG_SOC_SERIES_EFR32MG24
CONFIG_SOC_SERIES_MGM24
CONFIG_SOC_SERIES_BGM24
CONFIG_SOC_SERIES_EFR32BG26
CONFIG_SOC_SERIES_EFR32MG26
CONFIG_SOC_SERIES_BGM26
CONFIG_SOC_SERIES_MGM26
CONFIG_SOC_SERIES_EFR32BG27
CONFIG_SOC_SERIES_EFR32MG27
CONFIG_SOC_SERIES_EFR32ZG28
CONFIG_SOC_SERIES_EFR32BG29
CONFIG_SOC_SERIES_EFR32MG29
CONFIG_SOC_SERIES_SIBG301
CONFIG_SOC_SERIES_SIMG301
```

**定义位置（Location）**：[`soc/silabs/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_SOC_SERIES_EFR32BG13P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG13P)、[`CONFIG_SOC_SERIES_EFR32FG13P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32FG13P)、[`CONFIG_SOC_SERIES_EFR32FG1P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32FG1P)、[`CONFIG_SOC_SERIES_EFR32MG12P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG12P)、[`CONFIG_SOC_SERIES_EFR32MG13P`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG13P)、[`CONFIG_SOC_SERIES_EFR32BG21`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG21)、[`CONFIG_SOC_SERIES_EFR32MG21`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG21)、[`CONFIG_SOC_SERIES_EFR32BG22`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG22)、[`CONFIG_SOC_SERIES_EFR32MG22`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG22)、[`CONFIG_SOC_SERIES_BGM22`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_BGM22)、[`CONFIG_SOC_SERIES_EFR32ZG23`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32ZG23)、[`CONFIG_SOC_SERIES_EFR32BG24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG24)、[`CONFIG_SOC_SERIES_EFR32MG24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG24)、[`CONFIG_SOC_SERIES_MGM24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_MGM24)、[`CONFIG_SOC_SERIES_BGM24`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_BGM24)、[`CONFIG_SOC_SERIES_EFR32BG26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG26)、[`CONFIG_SOC_SERIES_EFR32MG26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG26)、[`CONFIG_SOC_SERIES_BGM26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_BGM26)、[`CONFIG_SOC_SERIES_MGM26`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_MGM26)、[`CONFIG_SOC_SERIES_EFR32BG27`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG27)、[`CONFIG_SOC_SERIES_EFR32MG27`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG27)、[`CONFIG_SOC_SERIES_EFR32ZG28`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32ZG28)、[`CONFIG_SOC_SERIES_EFR32BG29`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32BG29)、[`CONFIG_SOC_SERIES_EFR32MG29`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_EFR32MG29)、[`CONFIG_SOC_SERIES_SIBG301`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_SIBG301)、[`CONFIG_SOC_SERIES_SIMG301`](P308_soc_silabs_配置项参考_1.md#CONFIG_SOC_SERIES_SIMG301)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_FAMILY_SILABS_S2`、`CONFIG_SOC_FAMILY_SILABS_S3`。

<a id="CONFIG_SOC_VENDOR_SILABS_IMAGE_PROPERTIES"></a>

## 308.73 `CONFIG_SOC_VENDOR_SILABS_IMAGE_PROPERTIES`

**提示（Prompt）**：在镜像中包含应用属性数据结构（application properties data structure）

**说明（Help）**

在固件镜像中包含 Silicon Labs 应用属性数据结构（application properties data structure），使安全引擎（SE）和 Gecko 引导加载程序能够访问镜像版本、能力等信息。如果使用 MCUboot，只有 MCUboot 镜像自身需要该属性数据结构，以便 SE 对引导加载程序执行安全启动验证；MCUboot 使用自己的类型－长度－值格式（TLV）验证应用。如果使用 Gecko 引导加载程序，Zephyr 应用镜像也需要该数据结构。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_S1 || CONFIG_SOC_FAMILY_SILABS_S2 || CONFIG_SOC_FAMILY_SILABS_S3
```

**默认值（Defaults）**

```text
y if CONFIG_MCUBOOT
```

**定义位置（Location）**：[`soc/silabs/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_FAMILY_SILABS_S2`、`CONFIG_SOC_FAMILY_SILABS_S3`。

<a id="CONFIG_SOC_VENDOR_SILABS_PM_LOW_INTERRUPT_LATENCY"></a>

## 308.74 `CONFIG_SOC_VENDOR_SILABS_PM_LOW_INTERRUPT_LATENCY`

**提示（Prompt）**：低中断延迟模式（Low interrupt latency mode）

**说明（Help）**

启用低中断延迟（low interrupt latency）后，睡眠唤醒时可在高频时钟恢复之前执行中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && (CONFIG_SOC_FAMILY_SILABS_S1 || CONFIG_SOC_FAMILY_SILABS_S2 || CONFIG_SOC_FAMILY_SILABS_S3)
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/silabs/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_FAMILY_SILABS_S2`、`CONFIG_SOC_FAMILY_SILABS_S3`。

<a id="SB_CONFIG_SOC_FAMILY_SILABS_S2_XG21"></a>

## 308.75 `SB_CONFIG_SOC_FAMILY_SILABS_S2_XG21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG21 通用家族片上系统与模组（Generic Family SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_EFR32BG21
SB_CONFIG_SOC_SERIES_EFR32MG21
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg21/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg21/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S2)、[`SB_CONFIG_SOC_SERIES_EFR32BG21`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_SERIES_EFR32BG21)、[`SB_CONFIG_SOC_SERIES_EFR32MG21`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32MG21)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="SB_CONFIG_SOC_FAMILY_SILABS_S2_XG22"></a>

## 308.76 `SB_CONFIG_SOC_FAMILY_SILABS_S2_XG22`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG22 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_EFR32BG22
SB_CONFIG_SOC_SERIES_EFR32MG22
SB_CONFIG_SOC_SERIES_BGM22
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg22/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg22/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S2)、[`SB_CONFIG_SOC_SERIES_EFR32BG22`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_SERIES_EFR32BG22)、[`SB_CONFIG_SOC_SERIES_EFR32MG22`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32MG22)、[`SB_CONFIG_SOC_SERIES_BGM22`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_SERIES_BGM22)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="SB_CONFIG_SOC_FAMILY_SILABS_S2_XG23"></a>

## 308.77 `SB_CONFIG_SOC_FAMILY_SILABS_S2_XG23`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG23 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_EFR32ZG23
SB_CONFIG_SOC_SERIES_EFM32PG23
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg23/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg23/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S2)、[`SB_CONFIG_SOC_SERIES_EFR32ZG23`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32ZG23)、[`SB_CONFIG_SOC_SERIES_EFM32PG23`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_SERIES_EFM32PG23)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="SB_CONFIG_SOC_FAMILY_SILABS_S2_XG24"></a>

## 308.78 `SB_CONFIG_SOC_FAMILY_SILABS_S2_XG24`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG24 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_EFR32BG24
SB_CONFIG_SOC_SERIES_EFR32MG24
SB_CONFIG_SOC_SERIES_MGM24
SB_CONFIG_SOC_SERIES_BGM24
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg24/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg24/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S2)、[`SB_CONFIG_SOC_SERIES_EFR32BG24`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32BG24)、[`SB_CONFIG_SOC_SERIES_EFR32MG24`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32MG24)、[`SB_CONFIG_SOC_SERIES_MGM24`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_MGM24)、[`SB_CONFIG_SOC_SERIES_BGM24`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_SERIES_BGM24)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="SB_CONFIG_SOC_FAMILY_SILABS_S2_XG26"></a>

## 308.79 `SB_CONFIG_SOC_FAMILY_SILABS_S2_XG26`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG26 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_EFM32PG26
SB_CONFIG_SOC_SERIES_EFR32BG26
SB_CONFIG_SOC_SERIES_BGM26
SB_CONFIG_SOC_SERIES_EFR32MG26
SB_CONFIG_SOC_SERIES_MGM26
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg26/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg26/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S2)、[`SB_CONFIG_SOC_SERIES_EFM32PG26`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_SERIES_EFM32PG26)、[`SB_CONFIG_SOC_SERIES_EFR32BG26`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32BG26)、[`SB_CONFIG_SOC_SERIES_BGM26`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_SERIES_BGM26)、[`SB_CONFIG_SOC_SERIES_EFR32MG26`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32MG26)、[`SB_CONFIG_SOC_SERIES_MGM26`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_MGM26)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="SB_CONFIG_SOC_FAMILY_SILABS_S2_XG27"></a>

## 308.80 `SB_CONFIG_SOC_FAMILY_SILABS_S2_XG27`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG27 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_EFR32BG27
SB_CONFIG_SOC_SERIES_EFR32MG27
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg27/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg27/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S2)、[`SB_CONFIG_SOC_SERIES_EFR32BG27`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32BG27)、[`SB_CONFIG_SOC_SERIES_EFR32MG27`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32MG27)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="SB_CONFIG_SOC_FAMILY_SILABS_S2_XG28"></a>

## 308.81 `SB_CONFIG_SOC_FAMILY_SILABS_S2_XG28`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG28 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_EFM32PG28
SB_CONFIG_SOC_SERIES_EFR32FG28
SB_CONFIG_SOC_SERIES_EFR32ZG28
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg28/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg28/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S2)、[`SB_CONFIG_SOC_SERIES_EFM32PG28`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_SERIES_EFM32PG28)、[`SB_CONFIG_SOC_SERIES_EFR32FG28`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32FG28)、[`SB_CONFIG_SOC_SERIES_EFR32ZG28`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32ZG28)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="SB_CONFIG_SOC_FAMILY_SILABS_S2_XG29"></a>

## 308.82 `SB_CONFIG_SOC_FAMILY_SILABS_S2_XG29`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs XG29 系列片上系统与模组（Series SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_EFR32BG29
SB_CONFIG_SOC_SERIES_EFR32MG29
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg29/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg29/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S2)、[`SB_CONFIG_SOC_SERIES_EFR32BG29`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32BG29)、[`SB_CONFIG_SOC_SERIES_EFR32MG29`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_EFR32MG29)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="SB_CONFIG_SOC_FAMILY_SILABS_S3_SIX301"></a>

## 308.83 `SB_CONFIG_SOC_FAMILY_SILABS_S3_SIX301`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs Six301 片上系统与模组（SoC and modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S3
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_SIBG301
SB_CONFIG_SOC_SERIES_SIMG301
```

**定义位置（Location）**：[`soc/silabs/silabs_s3/six301/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s3/six301/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S3)、[`SB_CONFIG_SOC_SERIES_SIBG301`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_SIBG301)、[`SB_CONFIG_SOC_SERIES_SIMG301`](P309_soc_silabs_配置项参考_2.md#SB_CONFIG_SOC_SERIES_SIMG301)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S3`。

<a id="SB_CONFIG_SOC_SERIES_BGM22"></a>

## 308.84 `SB_CONFIG_SOC_SERIES_BGM22`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs BGM220 系列微控制器模组（Series MCU modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2_XG22
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_BGM220PC22HNA
SB_CONFIG_SOC_BGM220PC22WGA
SB_CONFIG_SOC_BGM220SC22HNA
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg22/Kconfig.soc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg22/Kconfig.soc#L23)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2_XG22`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`SB_CONFIG_SOC_BGM220PC22HNA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM220PC22HNA)、[`SB_CONFIG_SOC_BGM220PC22WGA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM220PC22WGA)、[`SB_CONFIG_SOC_BGM220SC22HNA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM220SC22HNA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_BGM220PC22HNA`、`SB_CONFIG_SOC_BGM220PC22WGA`、`SB_CONFIG_SOC_BGM220SC22HNA`。

<a id="SB_CONFIG_SOC_SERIES_BGM24"></a>

## 308.85 `SB_CONFIG_SOC_SERIES_BGM24`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs BGM240 系列微控制器模组（Series MCU modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2_XG24
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_BGM240PA22VNA
SB_CONFIG_SOC_BGM240PA32VNA
SB_CONFIG_SOC_BGM240PA32VNN
SB_CONFIG_SOC_BGM240PB22VNA
SB_CONFIG_SOC_BGM240PB32VNA
SB_CONFIG_SOC_BGM240PB32VNN
SB_CONFIG_SOC_BGM240SA22VNA
SB_CONFIG_SOC_BGM240SB22VNA
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg24/Kconfig.soc:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg24/Kconfig.soc#L30)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2_XG24`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_FAMILY_SILABS_S2_XG24)、[`SB_CONFIG_SOC_BGM240PA22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM240PA22VNA)、[`SB_CONFIG_SOC_BGM240PA32VNA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM240PA32VNA)、[`SB_CONFIG_SOC_BGM240PA32VNN`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM240PA32VNN)、[`SB_CONFIG_SOC_BGM240PB22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM240PB22VNA)、[`SB_CONFIG_SOC_BGM240PB32VNA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM240PB32VNA)、[`SB_CONFIG_SOC_BGM240PB32VNN`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM240PB32VNN)、[`SB_CONFIG_SOC_BGM240SA22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM240SA22VNA)、[`SB_CONFIG_SOC_BGM240SB22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM240SB22VNA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_BGM240PA22VNA`、`SB_CONFIG_SOC_BGM240PA32VNA`、`SB_CONFIG_SOC_BGM240PA32VNN`、`SB_CONFIG_SOC_BGM240PB22VNA`、`SB_CONFIG_SOC_BGM240PB32VNA`、`SB_CONFIG_SOC_BGM240PB32VNN`、`SB_CONFIG_SOC_BGM240SA22VNA`、`SB_CONFIG_SOC_BGM240SB22VNA`。

<a id="SB_CONFIG_SOC_SERIES_BGM26"></a>

## 308.86 `SB_CONFIG_SOC_SERIES_BGM26`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs BGM260（Blue Gecko）系列微控制器模组（Series MCU modules）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2_XG26
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_BGM260PB22VNA
SB_CONFIG_SOC_BGM260PB32VNA
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg26/Kconfig.soc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg26/Kconfig.soc#L22)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2_XG26`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`SB_CONFIG_SOC_BGM260PB22VNA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM260PB22VNA)、[`SB_CONFIG_SOC_BGM260PB32VNA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_BGM260PB32VNA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_BGM260PB22VNA`、`SB_CONFIG_SOC_BGM260PB32VNA`。

<a id="SB_CONFIG_SOC_SERIES_EFM32GG11B"></a>

## 308.87 `SB_CONFIG_SOC_SERIES_EFM32GG11B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32GG11B（Giant Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFM32GG11B820F2048GL192
SB_CONFIG_SOC_EFM32GG11B820F2048GM64
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efm32gg11b/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efm32gg11b/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S1)、[`SB_CONFIG_SOC_EFM32GG11B820F2048GL192`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32GG11B820F2048GL192)、[`SB_CONFIG_SOC_EFM32GG11B820F2048GM64`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32GG11B820F2048GM64)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S1`、`SB_CONFIG_SOC_EFM32GG11B820F2048GL192`、`SB_CONFIG_SOC_EFM32GG11B820F2048GM64`。

<a id="SB_CONFIG_SOC_SERIES_EFM32GG12B"></a>

## 308.88 `SB_CONFIG_SOC_SERIES_EFM32GG12B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32GG12（Giant Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFM32GG12B810F1024GM64
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efm32gg12b/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efm32gg12b/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S1)、[`SB_CONFIG_SOC_EFM32GG12B810F1024GM64`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32GG12B810F1024GM64)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S1`、`SB_CONFIG_SOC_EFM32GG12B810F1024GM64`。

<a id="SB_CONFIG_SOC_SERIES_EFM32HG"></a>

## 308.89 `SB_CONFIG_SOC_SERIES_EFM32HG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32HG（Happy Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFM32HG309F64
SB_CONFIG_SOC_EFM32HG322F64
```

**定义位置（Location）**：[`soc/silabs/silabs_s0/efm32hg/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s0/efm32hg/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S0)、[`SB_CONFIG_SOC_EFM32HG309F64`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32HG309F64)、[`SB_CONFIG_SOC_EFM32HG322F64`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32HG322F64)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S0`、`SB_CONFIG_SOC_EFM32HG309F64`、`SB_CONFIG_SOC_EFM32HG322F64`。

<a id="SB_CONFIG_SOC_SERIES_EFM32JG12B"></a>

## 308.90 `SB_CONFIG_SOC_SERIES_EFM32JG12B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32JG12B（Jade Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFM32JG12B500F1024GL125
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efm32jg12b/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efm32jg12b/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S1)、[`SB_CONFIG_SOC_EFM32JG12B500F1024GL125`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32JG12B500F1024GL125)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S1`、`SB_CONFIG_SOC_EFM32JG12B500F1024GL125`。

<a id="SB_CONFIG_SOC_SERIES_EFM32PG12B"></a>

## 308.91 `SB_CONFIG_SOC_SERIES_EFM32PG12B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32PG12B（Pearl Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFM32PG12B500F1024GL125
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efm32pg12b/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efm32pg12b/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S1)、[`SB_CONFIG_SOC_EFM32PG12B500F1024GL125`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG12B500F1024GL125)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S1`、`SB_CONFIG_SOC_EFM32PG12B500F1024GL125`。

<a id="SB_CONFIG_SOC_SERIES_EFM32PG1B"></a>

## 308.92 `SB_CONFIG_SOC_SERIES_EFM32PG1B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32PG1B（Pearl Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFM32PG1B200F256GM48
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efm32pg1b/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efm32pg1b/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S1)、[`SB_CONFIG_SOC_EFM32PG1B200F256GM48`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG1B200F256GM48)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S1`、`SB_CONFIG_SOC_EFM32PG1B200F256GM48`。

<a id="SB_CONFIG_SOC_SERIES_EFM32PG23"></a>

## 308.93 `SB_CONFIG_SOC_SERIES_EFM32PG23`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32PG23 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2_XG23
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFM32PG23B310F512IM48
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg23/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg23/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2_XG23`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_FAMILY_SILABS_S2_XG23)、[`SB_CONFIG_SOC_EFM32PG23B310F512IM48`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG23B310F512IM48)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_EFM32PG23B310F512IM48`。

<a id="SB_CONFIG_SOC_SERIES_EFM32PG26"></a>

## 308.94 `SB_CONFIG_SOC_SERIES_EFM32PG26`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32PG26（Pearl Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2_XG26
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFM32PG26B101F512IL136
SB_CONFIG_SOC_EFM32PG26B101F512IM68
SB_CONFIG_SOC_EFM32PG26B301F1024IL136
SB_CONFIG_SOC_EFM32PG26B301F1024IM68
SB_CONFIG_SOC_EFM32PG26B301F2048IL136
SB_CONFIG_SOC_EFM32PG26B301F2048IM68
SB_CONFIG_SOC_EFM32PG26B500F3200IL136
SB_CONFIG_SOC_EFM32PG26B500F3200IM48
SB_CONFIG_SOC_EFM32PG26B500F3200IM68
SB_CONFIG_SOC_EFM32PG26B501F3200IL136
SB_CONFIG_SOC_EFM32PG26B501F3200IM48
SB_CONFIG_SOC_EFM32PG26B501F3200IM68
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg26/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg26/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2_XG26`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_FAMILY_SILABS_S2_XG26)、[`SB_CONFIG_SOC_EFM32PG26B101F512IL136`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG26B101F512IL136)、[`SB_CONFIG_SOC_EFM32PG26B101F512IM68`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG26B101F512IM68)、[`SB_CONFIG_SOC_EFM32PG26B301F1024IL136`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG26B301F1024IL136)、[`SB_CONFIG_SOC_EFM32PG26B301F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG26B301F1024IM68)、[`SB_CONFIG_SOC_EFM32PG26B301F2048IL136`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG26B301F2048IL136)、[`SB_CONFIG_SOC_EFM32PG26B301F2048IM68`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG26B301F2048IM68)、[`SB_CONFIG_SOC_EFM32PG26B500F3200IL136`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG26B500F3200IL136)、[`SB_CONFIG_SOC_EFM32PG26B500F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG26B500F3200IM48)、[`SB_CONFIG_SOC_EFM32PG26B500F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG26B500F3200IM68)、[`SB_CONFIG_SOC_EFM32PG26B501F3200IL136`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG26B501F3200IL136)、[`SB_CONFIG_SOC_EFM32PG26B501F3200IM48`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG26B501F3200IM48)、[`SB_CONFIG_SOC_EFM32PG26B501F3200IM68`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG26B501F3200IM68)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_EFM32PG26B101F512IL136`、`SB_CONFIG_SOC_EFM32PG26B101F512IM68`、`SB_CONFIG_SOC_EFM32PG26B301F1024IL136`、`SB_CONFIG_SOC_EFM32PG26B301F1024IM68`、`SB_CONFIG_SOC_EFM32PG26B301F2048IL136`、`SB_CONFIG_SOC_EFM32PG26B301F2048IM68`、`SB_CONFIG_SOC_EFM32PG26B500F3200IL136`、`SB_CONFIG_SOC_EFM32PG26B500F3200IM48`、`SB_CONFIG_SOC_EFM32PG26B500F3200IM68`、`SB_CONFIG_SOC_EFM32PG26B501F3200IL136`、`SB_CONFIG_SOC_EFM32PG26B501F3200IM48`、`SB_CONFIG_SOC_EFM32PG26B501F3200IM68`。

<a id="SB_CONFIG_SOC_SERIES_EFM32PG28"></a>

## 308.95 `SB_CONFIG_SOC_SERIES_EFM32PG28`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32PG28 系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2_XG28
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFM32PG28B200F512IM68
SB_CONFIG_SOC_EFM32PG28B210F1024IM68
SB_CONFIG_SOC_EFM32PG28B300F512IM68
SB_CONFIG_SOC_EFM32PG28B310F1024IM68
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg28/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg28/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2_XG28`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_FAMILY_SILABS_S2_XG28)、[`SB_CONFIG_SOC_EFM32PG28B200F512IM68`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG28B200F512IM68)、[`SB_CONFIG_SOC_EFM32PG28B210F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG28B210F1024IM68)、[`SB_CONFIG_SOC_EFM32PG28B300F512IM68`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG28B300F512IM68)、[`SB_CONFIG_SOC_EFM32PG28B310F1024IM68`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32PG28B310F1024IM68)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_EFM32PG28B200F512IM68`、`SB_CONFIG_SOC_EFM32PG28B210F1024IM68`、`SB_CONFIG_SOC_EFM32PG28B300F512IM68`、`SB_CONFIG_SOC_EFM32PG28B310F1024IM68`。

<a id="SB_CONFIG_SOC_SERIES_EFM32TG"></a>

## 308.96 `SB_CONFIG_SOC_SERIES_EFM32TG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32TG（Tiny Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFM32TG840F32
```

**定义位置（Location）**：[`soc/silabs/silabs_s0/efm32tg/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s0/efm32tg/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S0)、[`SB_CONFIG_SOC_EFM32TG840F32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32TG840F32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S0`、`SB_CONFIG_SOC_EFM32TG840F32`。

<a id="SB_CONFIG_SOC_SERIES_EFM32WG"></a>

## 308.97 `SB_CONFIG_SOC_SERIES_EFM32WG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFM32WG（Wonder Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S0
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFM32WG990F256
```

**定义位置（Location）**：[`soc/silabs/silabs_s0/efm32wg/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s0/efm32wg/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S0)、[`SB_CONFIG_SOC_EFM32WG990F256`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFM32WG990F256)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S0`、`SB_CONFIG_SOC_EFM32WG990F256`。

<a id="SB_CONFIG_SOC_SERIES_EFR32BG13P"></a>

## 308.98 `SB_CONFIG_SOC_SERIES_EFR32BG13P`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32BG13P（Blue Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S1
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFR32BG13P632F512GM48
```

**定义位置（Location）**：[`soc/silabs/silabs_s1/efr32bg13p/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s1/efr32bg13p/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_SILABS_S1)、[`SB_CONFIG_SOC_EFR32BG13P632F512GM48`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFR32BG13P632F512GM48)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_SILABS_S1`、`SB_CONFIG_SOC_EFR32BG13P632F512GM48`。

<a id="SB_CONFIG_SOC_SERIES_EFR32BG21"></a>

## 308.99 `SB_CONFIG_SOC_SERIES_EFR32BG21`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32BG21（Blue Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2_XG21
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFR32BG21B010F1024IM32
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg21/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg21/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2_XG21`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_FAMILY_SILABS_S2_XG21)、[`SB_CONFIG_SOC_EFR32BG21B010F1024IM32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFR32BG21B010F1024IM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_EFR32BG21B010F1024IM32`。

<a id="SB_CONFIG_SOC_SERIES_EFR32BG22"></a>

## 308.100 `SB_CONFIG_SOC_SERIES_EFR32BG22`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Silicon Labs EFR32BG22（Blue Gecko）系列微控制器（Series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_SILABS_S2_XG22
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_EFR32BG22C224F512IM40
SB_CONFIG_SOC_EFR32BG22C224F512IM32
SB_CONFIG_SOC_EFR32BG22C224F512GN32
SB_CONFIG_SOC_EFR32BG22C224F512GM40
SB_CONFIG_SOC_EFR32BG22C224F512GM32
SB_CONFIG_SOC_EFR32BG22C222F352GN32
SB_CONFIG_SOC_EFR32BG22C222F352GM40
SB_CONFIG_SOC_EFR32BG22C222F352GM32
```

**定义位置（Location）**：[`soc/silabs/silabs_s2/xg22/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/silabs/silabs_s2/xg22/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_SILABS_S2_XG22`](P308_soc_silabs_配置项参考_1.md#SB_CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`SB_CONFIG_SOC_EFR32BG22C224F512IM40`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFR32BG22C224F512IM40)、[`SB_CONFIG_SOC_EFR32BG22C224F512IM32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFR32BG22C224F512IM32)、[`SB_CONFIG_SOC_EFR32BG22C224F512GN32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFR32BG22C224F512GN32)、[`SB_CONFIG_SOC_EFR32BG22C224F512GM40`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFR32BG22C224F512GM40)、[`SB_CONFIG_SOC_EFR32BG22C224F512GM32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFR32BG22C224F512GM32)、[`SB_CONFIG_SOC_EFR32BG22C222F352GN32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFR32BG22C222F352GN32)、[`SB_CONFIG_SOC_EFR32BG22C222F352GM40`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFR32BG22C222F352GM40)、[`SB_CONFIG_SOC_EFR32BG22C222F352GM32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_EFR32BG22C222F352GM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_EFR32BG22C224F512IM40`、`SB_CONFIG_SOC_EFR32BG22C224F512IM32`、`SB_CONFIG_SOC_EFR32BG22C224F512GN32`、`SB_CONFIG_SOC_EFR32BG22C224F512GM40`、`SB_CONFIG_SOC_EFR32BG22C224F512GM32`、`SB_CONFIG_SOC_EFR32BG22C222F352GN32`、`SB_CONFIG_SOC_EFR32BG22C222F352GM40`、`SB_CONFIG_SOC_EFR32BG22C222F352GM32`。

<!-- kconfig-navigation -->

[上一章](P307_soc_sifli_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P309_soc_silabs_配置项参考_2.md)
