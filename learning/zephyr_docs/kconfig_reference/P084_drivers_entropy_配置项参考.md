---
id: learning.zephyr-docs.kconfig-reference.page-84
title: "`drivers/entropy`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第84章\_`drivers/entropy`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/entropy` 的 88 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ARCH_HAS_ENTROPY"></a>

## 84.1 `CONFIG_ARCH_HAS_ENTROPY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

这是一个隐藏选项（Hidden Option），用于指示该架构无需专用设备即可提供熵（Entropy）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_GENERATOR
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_ENTROPY_ARM64_RNG
CONFIG_ENTROPY_RISCV_ZKR
```

**定义位置（Location）**：[`drivers/entropy/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_ENTROPY_ARM64_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_ARM64_RNG)、[`CONFIG_ENTROPY_RISCV_ZKR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_RISCV_ZKR)。

<a id="CONFIG_ENTROPY_AMBIQ_PUF_TRNG"></a>

## 84.2 `CONFIG_ENTROPY_AMBIQ_PUF_TRNG`

**提示（Prompt）**：Ambiq 真随机数发生器（TRNG）驱动

**说明（Help）**

此选项启用基于 OTP/PUF TRNG 的真随机数发生器（True Random Number Generator）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_AMBIQ_HAS_PUF && DT_HAS_AMBIQ_PUF_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.ambiq:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.ambiq#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AMBIQ_HAS_PUF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMBIQ_HAS_PUF)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_AMEBA_TRNG"></a>

## 84.3 `CONFIG_ENTROPY_AMEBA_TRNG`

**提示（Prompt）**：Ameba 熵数发生器驱动（Entropy Number Generator Driver）

**说明（Help）**

为 AMEBA 系列处理器启用熵数发生器（Entropy Number Generator）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.ameba:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.ameba#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_ARM64_RNG"></a>

## 84.4 `CONFIG_ENTROPY_ARM64_RNG`

**提示（Prompt）**：使用 ARM64 熵源驱动（Entropy Driver）

**说明（Help）**

启用基于 ARM 扩展 `FEAT_RNG` 中 `RNDRRS` 指令的架构熵源驱动（Architectural Entropy Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_ENTROPY
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.arm64:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.arm64#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_RNG`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ARCH_HAS_ENTROPY`](P084_drivers_entropy_配置项参考.md#CONFIG_ARCH_HAS_ENTROPY)。

<a id="CONFIG_ENTROPY_ARM64_RNG_MAX_RETRIES"></a>

## 84.5 `CONFIG_ENTROPY_ARM64_RNG_MAX_RETRIES`

**提示（Prompt）**：ARM64 熵源驱动的最大重试次数（Maximum Retries）

**说明（Help）**

`RNDRRS` 指令允许连续失败的最大次数，达到此次数后驱动应返回错误。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_ARM64_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.arm64:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.arm64#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → 使用 ARM64 熵源驱动（Entropy Driver）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_ARM64_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_ARM64_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_ARM64_RNG_RETRY_WAIT_USEC"></a>

## 84.6 `CONFIG_ENTROPY_ARM64_RNG_RETRY_WAIT_USEC`

**提示（Prompt）**：ARM64 熵源驱动的重试等待时间（Retry Wait Time）

**说明（Help）**

`RNDRRS` 指令失败后，驱动重试前应等待的微秒数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_ARM64_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.arm64:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.arm64#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → 使用 ARM64 熵源驱动（Entropy Driver）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_ARM64_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_ARM64_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_BEE_TRNG"></a>

## 84.7 `CONFIG_ENTROPY_BEE_TRNG`

**提示（Prompt）**：Realtek Bee 系列 TRNG 驱动

**说明（Help）**

启用瑞昱（Realtek）Bee 系列 SoC 的真随机数发生器（TRNG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_BFLB_SEC_ENG"></a>

## 84.8 `CONFIG_ENTROPY_BFLB_SEC_ENG`

**提示（Prompt）**：博流（Bouffalo Lab）SEC 引擎 TRNG 驱动

**说明（Help）**

启用博流（Bouffalo Lab）SEC 引擎的 TRNG 熵源驱动（Entropy Driver）。通过 `SEC_ENG` TRNG 外设提供硬件真随机数生成（Hardware True Random Number Generation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_SEC_ENG_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_BRCM_BCM2835_RNG"></a>

## 84.9 `CONFIG_ENTROPY_BRCM_BCM2835_RNG`

**提示（Prompt）**：Broadcom BCM2835 简单 RNG 驱动（Simple RNG Driver）

**说明（Help）**

启用 Broadcom BCM2835 简单硬件随机数发生器（RNG）模块的驱动，适用于 BCM2835 / BCM2836 / BCM2837 / BCM2710 SoC，即树莓派（Raspberry Pi）1/2/3/Zero 系列。它与 BCM2711（Pi 4）上的 iProc RNG200 不同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_BCM2835_RNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.bcm2835:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.bcm2835#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_BRCM_IPROC_RNG200"></a>

## 84.10 `CONFIG_ENTROPY_BRCM_IPROC_RNG200`

**提示（Prompt）**：Broadcom iProc RNG200 驱动

**说明（Help）**

启用 Broadcom iProc RNG200 随机数发生器（Random Number Generator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_IPROC_RNG200_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.iproc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.iproc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_BT_HCI"></a>

## 84.11 `CONFIG_ENTROPY_BT_HCI`

**提示（Prompt）**：蓝牙 HCI 随机数发生器驱动（Bluetooth HCI RNG Driver）

**说明（Help）**

启用蓝牙主机控制器接口（Bluetooth HCI）设备提供的随机数发生器（Random Number Generator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_BT_HCI_ENTROPY_ENABLED && CONFIG_BT_HCI_HOST && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.bt_hci:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.bt_hci#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_ENTROPY_CC13XX_CC26XX_ALARM_THRESHOLD"></a>

## 84.12 `CONFIG_ENTROPY_CC13XX_CC26XX_ALARM_THRESHOLD`

**提示（Prompt）**：检测到重复模式的阈值（Repeated Pattern Threshold）

**说明（Help）**

触发报警事件（Alarm Event）之前，检测到具有重复模式（Repeating Pattern）的样本数量。相应的 FRO 会自动关闭。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_CC13XX_CC26XX_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.cc13xx_cc26xx:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.cc13xx_cc26xx#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → TI SimpleLink CC13xx / CC26xx 真随机数发生器（True Random Number Generator，TRNG）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_CC13XX_CC26XX_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_CC13XX_CC26XX_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_CC13XX_CC26XX_POOL_SIZE"></a>

## 84.13 `CONFIG_ENTROPY_CC13XX_CC26XX_POOL_SIZE`

**提示（Prompt）**：熵池（Entropy Pool）中的字节数

**说明（Help）**

用于存储硬件生成的熵（Entropy）的缓冲区大小，以字节为单位。为获得较高性能，应取 2 的幂。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_CC13XX_CC26XX_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.cc13xx_cc26xx:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.cc13xx_cc26xx#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → TI SimpleLink CC13xx / CC26xx 真随机数发生器（True Random Number Generator，TRNG）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_CC13XX_CC26XX_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_CC13XX_CC26XX_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_CC13XX_CC26XX_RNG"></a>

## 84.14 `CONFIG_ENTROPY_CC13XX_CC26XX_RNG`

**提示（Prompt）**：TI SimpleLink CC13xx / CC26xx 真随机数发生器（True Random Number Generator，TRNG）

**说明（Help）**

此选项启用 TI SimpleLink CC13xx / CC26xx SoC 的真随机数发生器（True Random Number Generator，TRNG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC13XX_CC26XX_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.cc13xx_cc26xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.cc13xx_cc26xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_CC13XX_CC26XX_SAMPLES_PER_CYCLE"></a>

## 84.15 `CONFIG_ENTROPY_CC13XX_CC26XX_SAMPLES_PER_CYCLE`

**提示（Prompt）**：用于生成熵的样本数量（Sample Count）

**说明（Help）**

用于生成熵（Entropy）的样本数量。生成 64 位熵所需的时间，取决于启用的 FRO 数量、采样（系统）时钟频率以及此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_CC13XX_CC26XX_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
240000
```

**取值范围（Ranges）**

```text
[256, 16777216]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.cc13xx_cc26xx:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.cc13xx_cc26xx#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → TI SimpleLink CC13xx / CC26xx 真随机数发生器（True Random Number Generator，TRNG）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_CC13XX_CC26XX_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_CC13XX_CC26XX_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_CC13XX_CC26XX_SHUTDOWN_THRESHOLD"></a>

## 84.16 `CONFIG_ENTROPY_CC13XX_CC26XX_SHUTDOWN_THRESHOLD`

**提示（Prompt）**：自动关闭的 FRO 数量阈值（Threshold）

**说明（Help）**

驱动尝试采取纠正措施（Corrective Action）之前，允许关闭的 FRO 数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_CC13XX_CC26XX_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 24]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.cc13xx_cc26xx:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.cc13xx_cc26xx#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → TI SimpleLink CC13xx / CC26xx 真随机数发生器（True Random Number Generator，TRNG）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_CC13XX_CC26XX_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_CC13XX_CC26XX_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_ESP32_RNG"></a>

## 84.17 `CONFIG_ENTROPY_ESP32_RNG`

**提示（Prompt）**：ESP32 熵数发生器驱动（Entropy Number Generator Driver）

**说明（Help）**

此选项启用 ESP32 SoC 的熵数发生器（Entropy Number Generator）。禁用 Wi-Fi 和蓝牙（Bluetooth）时，它会生成伪熵数（Pseudo-Entropy Numbers），因为该发生器利用这些无线电模块的噪声补充熵。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.esp32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.esp32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_GD32_TRNG"></a>

## 84.18 `CONFIG_ENTROPY_GD32_TRNG`

**提示（Prompt）**：兆易创新（GigaDevice）GD32F4xx TRNG 驱动

**说明（Help）**

为兆易创新（GigaDevice）GD32F4xx 系列启用真随机数发生器（True Random Number Generator，TRNG）驱动。此驱动使用 GD32 硬件抽象层（HAL），并以轮询模式（Polling Mode）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
CONFIG_USE_GD32_TRNG
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.gd32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.gd32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_USE_GD32_TRNG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_GD32_TRNG)。

<a id="CONFIG_ENTROPY_GECKO_SE"></a>

## 84.19 `CONFIG_ENTROPY_GECKO_SE`

**提示（Prompt）**：GECKO 安全元件（SE）驱动

**说明（Help）**

此选项启用基于安全元件（Secure Element，SE）模块的真随机数发生器（True Random Number Generator）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GECKO_SEMAILBOX_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
CONFIG_SILABS_SISDK_SE
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.gecko:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.gecko#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_SILABS_SISDK_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_SE)。

<a id="CONFIG_ENTROPY_GECKO_TRNG"></a>

## 84.20 `CONFIG_ENTROPY_GECKO_TRNG`

**提示（Prompt）**：GECKO TRNG 驱动

**说明（Help）**

此选项启用基于 TRNG 的真随机数发生器（True Random Number Generator）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GECKO_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
CONFIG_CRYPTO_ACC_GECKO_TRNG if CONFIG_SOC_FAMILY_SILABS_S2_XG22 || CONFIG_SOC_FAMILY_SILABS_S2_XG27
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.gecko:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.gecko#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_CRYPTO_ACC_GECKO_TRNG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRYPTO_ACC_GECKO_TRNG)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG22`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG22)、[`CONFIG_SOC_FAMILY_SILABS_S2_XG27`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2_XG27)。

<a id="CONFIG_ENTROPY_GENERATOR"></a>

## 84.21 `CONFIG_ENTROPY_GENERATOR`

**提示（Prompt）**：熵源驱动（Entropy Drivers）

**说明（Help）**

将熵源驱动（Entropy Drivers）纳入系统配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_NRF_802154_RADIO_DRIVER
CONFIG_OPENTHREAD
CONFIG_NRF_802154_RADIO_DRIVER
CONFIG_OPENTHREAD
CONFIG_BT_SILABS_SIWX91X
CONFIG_BT_CTLR_ENTROPY
CONFIG_CPU_FREQ_POLICY_TIMING_NOISE
CONFIG_LORAWAN_SERVICES
CONFIG_NETWORKING
CONFIG_MCP_TRANSPORT_HTTP
CONFIG_CSPRNG_NEEDED
CONFIG_TEST_BUSY_SIM
```

**定义位置（Location）**：[`drivers/entropy/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_RADIO_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD)、[`CONFIG_BT_SILABS_SIWX91X`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_SIWX91X)、[`CONFIG_BT_CTLR_ENTROPY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ENTROPY)、[`CONFIG_CPU_FREQ_POLICY_TIMING_NOISE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_FREQ_POLICY_TIMING_NOISE)、[`CONFIG_LORAWAN_SERVICES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_SERVICES)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_MCP_TRANSPORT_HTTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_CSPRNG_NEEDED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CSPRNG_NEEDED)、[`CONFIG_TEST_BUSY_SIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_BUSY_SIM)。

<a id="CONFIG_ENTROPY_HAS_DRIVER"></a>

## 84.22 `CONFIG_ENTROPY_HAS_DRIVER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项由各个熵源驱动（Entropy Driver）启用，用于表明存在真正的熵源驱动（True Entropy Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_GENERATOR
```

**被选择（Selected by）**

```text
CONFIG_ENTROPY_AMBIQ_PUF_TRNG
CONFIG_ENTROPY_AMEBA_TRNG
CONFIG_ENTROPY_TELINK_B91_TRNG
CONFIG_ENTROPY_BRCM_BCM2835_RNG
CONFIG_ENTROPY_BEE_TRNG
CONFIG_ENTROPY_BFLB_SEC_ENG
CONFIG_ENTROPY_BT_HCI
CONFIG_ENTROPY_CC13XX_CC26XX_RNG
CONFIG_ENTROPY_ESP32_RNG
CONFIG_ENTROPY_GD32_TRNG
CONFIG_ENTROPY_GECKO_TRNG
CONFIG_ENTROPY_GECKO_SE
CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG
CONFIG_ENTROPY_INFINEON_MXCRYPTOLITE_TRNG
CONFIG_ENTROPY_BRCM_IPROC_RNG200
CONFIG_ENTROPY_LITEX_RNG
CONFIG_ENTROPY_MAX32_TRNG
CONFIG_ENTROPY_MAXQ10XX_RNG
CONFIG_ENTROPY_MCHP_TRNG_G1
CONFIG_ENTROPY_MCHP_TRNG_G2
CONFIG_ENTROPY_MCUX_RNGA
CONFIG_ENTROPY_MCUX_TRNG
CONFIG_ENTROPY_MCUX_RNG
CONFIG_ENTROPY_MCUX_CAAM
CONFIG_ENTROPY_MSPM0_TRNG
CONFIG_FAKE_ENTROPY_NATIVE_SIM
CONFIG_ENTROPY_NEORV32_TRNG
CONFIG_ENTROPY_NPCX_DRBG
CONFIG_ENTROPY_NRF5_RNG
CONFIG_ENTROPY_NRF_CRACEN_CTR_DRBG
CONFIG_ENTROPY_NXP_ELE_TRNG
CONFIG_ENTROPY_NXP_ELS_TRNG
CONFIG_ENTROPY_PSA_CRYPTO_RNG
CONFIG_ENTROPY_RENESAS_RA
CONFIG_ENTROPY_RPI_PICO_RNG
CONFIG_ENTROPY_RV32M1_TRNG
CONFIG_ENTROPY_SAM_RNG
CONFIG_ENTROPY_SF32LB
CONFIG_ENTROPY_SILABS_SIWX91X
CONFIG_ENTROPY_SMARTBOND_TRNG
CONFIG_ENTROPY_STM32_RNG
CONFIG_ENTROPY_SY1XX_TRNG
CONFIG_ENTROPY_VIRTIO
CONFIG_ENTROPY_WCH_RNG
CONFIG_ARCH_HAS_ENTROPY
```

**定义位置（Location）**：[`drivers/entropy/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_AMBIQ_PUF_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_AMBIQ_PUF_TRNG)、[`CONFIG_ENTROPY_AMEBA_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_AMEBA_TRNG)、[`CONFIG_ENTROPY_TELINK_B91_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_TELINK_B91_TRNG)、[`CONFIG_ENTROPY_BRCM_BCM2835_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_BRCM_BCM2835_RNG)、[`CONFIG_ENTROPY_BEE_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_BEE_TRNG)、[`CONFIG_ENTROPY_BFLB_SEC_ENG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_BFLB_SEC_ENG)、[`CONFIG_ENTROPY_BT_HCI`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_BT_HCI)、[`CONFIG_ENTROPY_CC13XX_CC26XX_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_CC13XX_CC26XX_RNG)、[`CONFIG_ENTROPY_ESP32_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_ESP32_RNG)、[`CONFIG_ENTROPY_GD32_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GD32_TRNG)、[`CONFIG_ENTROPY_GECKO_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GECKO_TRNG)、[`CONFIG_ENTROPY_GECKO_SE`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GECKO_SE)、[`CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG)、[`CONFIG_ENTROPY_INFINEON_MXCRYPTOLITE_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_INFINEON_MXCRYPTOLITE_TRNG)、[`CONFIG_ENTROPY_BRCM_IPROC_RNG200`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_BRCM_IPROC_RNG200)、[`CONFIG_ENTROPY_LITEX_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_LITEX_RNG)、[`CONFIG_ENTROPY_MAX32_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MAX32_TRNG)、[`CONFIG_ENTROPY_MAXQ10XX_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MAXQ10XX_RNG)、[`CONFIG_ENTROPY_MCHP_TRNG_G1`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MCHP_TRNG_G1)、[`CONFIG_ENTROPY_MCHP_TRNG_G2`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MCHP_TRNG_G2)、[`CONFIG_ENTROPY_MCUX_RNGA`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MCUX_RNGA)、[`CONFIG_ENTROPY_MCUX_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MCUX_TRNG)、[`CONFIG_ENTROPY_MCUX_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MCUX_RNG)、[`CONFIG_ENTROPY_MCUX_CAAM`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MCUX_CAAM)、[`CONFIG_ENTROPY_MSPM0_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MSPM0_TRNG)、[`CONFIG_FAKE_ENTROPY_NATIVE_SIM`](P084_drivers_entropy_配置项参考.md#CONFIG_FAKE_ENTROPY_NATIVE_SIM)、[`CONFIG_ENTROPY_NEORV32_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NEORV32_TRNG)、[`CONFIG_ENTROPY_NPCX_DRBG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NPCX_DRBG)、[`CONFIG_ENTROPY_NRF5_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF5_RNG)、[`CONFIG_ENTROPY_NRF_CRACEN_CTR_DRBG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF_CRACEN_CTR_DRBG)、[`CONFIG_ENTROPY_NXP_ELE_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NXP_ELE_TRNG)、[`CONFIG_ENTROPY_NXP_ELS_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NXP_ELS_TRNG)、[`CONFIG_ENTROPY_PSA_CRYPTO_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_PSA_CRYPTO_RNG)、[`CONFIG_ENTROPY_RENESAS_RA`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_RENESAS_RA)、[`CONFIG_ENTROPY_RPI_PICO_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_RPI_PICO_RNG)、[`CONFIG_ENTROPY_RV32M1_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_RV32M1_TRNG)、[`CONFIG_ENTROPY_SAM_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_SAM_RNG)、[`CONFIG_ENTROPY_SF32LB`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_SF32LB)、[`CONFIG_ENTROPY_SILABS_SIWX91X`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_SILABS_SIWX91X)、[`CONFIG_ENTROPY_SMARTBOND_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_SMARTBOND_TRNG)、[`CONFIG_ENTROPY_STM32_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_RNG)、[`CONFIG_ENTROPY_SY1XX_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_SY1XX_TRNG)、[`CONFIG_ENTROPY_VIRTIO`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_VIRTIO)、[`CONFIG_ENTROPY_WCH_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_WCH_RNG)、[`CONFIG_ARCH_HAS_ENTROPY`](P084_drivers_entropy_配置项参考.md#CONFIG_ARCH_HAS_ENTROPY)。

<a id="CONFIG_ENTROPY_INFINEON_MXCRYPTOLITE_TRNG"></a>

## 84.23 `CONFIG_ENTROPY_INFINEON_MXCRYPTOLITE_TRNG`

**提示（Prompt）**：Infineon MXCRYPTOLITE TRNG 熵源驱动（Entropy Driver）

**说明（Help）**

为包含 MXCRYPTOLITE IP 的英飞凌（Infineon）器件启用真随机数发生器（True Random Number Generator）熵源驱动。

> 译注：官方帮助正文将该 IP 拼作 `MXRYPTOLITE`，提示文本则为 `MXCRYPTOLITE`；两处原文拼写不同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_MXCRYPTOLITE_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
CONFIG_ENTROPY_HAS_DRIVER
CONFIG_USE_INFINEON_MXCRYPTOLITE_TRNG
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.infineon_mxcryptolite:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.infineon_mxcryptolite#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_USE_INFINEON_MXCRYPTOLITE_TRNG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_MXCRYPTOLITE_TRNG)。

<a id="CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG"></a>

## 84.24 `CONFIG_ENTROPY_INFINEON_MXCRYPTO_TRNG`

**提示（Prompt）**：Infineon MXCRYPTO TRNG 熵源驱动（Entropy Driver）

**说明（Help）**

为包含 MXCRYPTO IP 的英飞凌（Infineon）器件启用真随机数发生器（True Random Number Generator）熵源驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_MXCRYPTO_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
CONFIG_ENTROPY_HAS_DRIVER
CONFIG_USE_INFINEON_MXCRYPTO_TRNG
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.infineon_mxcrypto:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.infineon_mxcrypto#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_USE_INFINEON_MXCRYPTO_TRNG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_MXCRYPTO_TRNG)。

<a id="CONFIG_ENTROPY_INIT_PRIORITY"></a>

## 84.25 `CONFIG_ENTROPY_INIT_PRIORITY`

**提示（Prompt）**：熵源驱动初始化优先级（Entropy Driver Init Priority）

**说明（Help）**

熵源驱动设备的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/entropy/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_ENTROPY_LITEX_RNG"></a>

## 84.26 `CONFIG_ENTROPY_LITEX_RNG`

**提示（Prompt）**：伪随机二进制序列（PRBS）RNG 驱动

**说明（Help）**

此选项启用随机数发生器（RNG）模块；它是用于 LiteX SoC 构建器（SoC Builder）、基于伪随机二进制序列（Pseudo-Random Binary Sequences，PRBS）的熵数发生器（Entropy Number Generator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_PRBS_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.litex:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.litex#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_MAX32_TRNG"></a>

## 84.27 `CONFIG_ENTROPY_MAX32_TRNG`

**提示（Prompt）**：ADI MAX32XXX 微控制器系列真随机数发生器（True Random Number Generator，TRNG）驱动

**说明（Help）**

为 ADI MAX32XXX 微控制器（MCU）启用真随机数发生器（True Random Number Generator，TRNG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_MAXQ10XX_RNG"></a>

## 84.28 `CONFIG_ENTROPY_MAXQ10XX_RNG`

**提示（Prompt）**：MAXQ10xx 熵数发生器驱动（Entropy Number Generator Driver）

**说明（Help）**

此选项启用 MAXQ10xx 密码芯片（Crypto Chip）的熵数发生器驱动（Entropy Number Generator Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAXQ10XX_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
CONFIG_SPI
CONFIG_MFD
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.maxq10xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.maxq10xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_ENTROPY_MCHP_TRNG_G1"></a>

## 84.29 `CONFIG_ENTROPY_MCHP_TRNG_G1`

**提示（Prompt）**：Microchip MCHP G1 熵源驱动（Entropy Driver）

**说明（Help）**

此选项启用 G1 组（Group）的熵源驱动（Entropy Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_TRNG_G1_ENTROPY_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_MCHP_TRNG_G2"></a>

## 84.30 `CONFIG_ENTROPY_MCHP_TRNG_G2`

**提示（Prompt）**：Microchip MCHP G2 熵源驱动（Entropy Driver）

**说明（Help）**

此选项启用 G2 组（Group）的熵源驱动（Entropy Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_TRNG_G2_ENTROPY_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.mchp:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.mchp#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_MCUX_CAAM"></a>

## 84.31 `CONFIG_ENTROPY_MCUX_CAAM`

**提示（Prompt）**：MCUX CAAM 驱动

**说明（Help）**

此选项启用基于 MCUX CAAM 驱动的 CAAM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_CAAM_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.mcux:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.mcux#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ENTROPY_MCUX_RNG"></a>

## 84.32 `CONFIG_ENTROPY_MCUX_RNG`

**提示（Prompt）**：MCUX RNG 驱动

**说明（Help）**

此选项启用 LPC 系列中基于 MCUX RNG 驱动的真随机数发生器（True Random Number Generator，TRNG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_RNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.mcux:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.mcux#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_MCUX_RNGA"></a>

## 84.33 `CONFIG_ENTROPY_MCUX_RNGA`

**提示（Prompt）**：MCUX RNGA 驱动

**说明（Help）**

此选项启用基于 MCUX RNGA 驱动的随机数发生器加速器（Random Number Generator Accelerator，RNGA）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_RNGA_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.mcux:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.mcux#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_MCUX_TRNG"></a>

## 84.34 `CONFIG_ENTROPY_MCUX_TRNG`

**提示（Prompt）**：MCUX TRNG 驱动

**说明（Help）**

此选项启用基于 MCUX TRNG 驱动的真随机数发生器（True Random Number Generator，TRNG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
CONFIG_ENTROPY_NEEDS_PRNG
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.mcux:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.mcux#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_ENTROPY_NEEDS_PRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NEEDS_PRNG)。

<a id="CONFIG_ENTROPY_MSPM0_TRNG"></a>

## 84.35 `CONFIG_ENTROPY_MSPM0_TRNG`

**提示（Prompt）**：TI MSPM0 真随机数发生器（True Random Number Generator，TRNG）

**说明（Help）**

此选项启用 TI MSPM0 SoC 的真随机数发生器（True Random Number Generator，TRNG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.mspm0_trng:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.mspm0_trng#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_MSPM0_TRNG_DECIMATION_RATE"></a>

## 84.36 `CONFIG_ENTROPY_MSPM0_TRNG_DECIMATION_RATE`

**提示（Prompt）**：TRNG 抽取率（Decimation Rate），取值 1–8

**说明（Help）**

抽取率（Decimation Rate）控制 TRNG 的采样率（Sampling Rate）。值越大，熵质量（Entropy Quality）越好。根据技术参考手册（TRM）的建议，抽取率应为 `4` 或更大。有效值为 `1` 至 `8`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_MSPM0_TRNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.mspm0_trng:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.mspm0_trng#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → TI MSPM0 真随机数发生器（True Random Number Generator，TRNG）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_MSPM0_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MSPM0_TRNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_MSPM0_TRNG_POOL_SIZE"></a>

## 84.37 `CONFIG_ENTROPY_MSPM0_TRNG_POOL_SIZE`

**提示（Prompt）**：熵池缓冲区大小（Entropy Pool Buffer Size），以字节为单位

**说明（Help）**

用于存储 TRNG 硬件生成的熵（Entropy）的环形缓冲区（Ring Buffer）大小，以字节为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_MSPM0_TRNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.mspm0_trng:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.mspm0_trng#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → TI MSPM0 真随机数发生器（True Random Number Generator，TRNG）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_MSPM0_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MSPM0_TRNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_NEEDS_PRNG"></a>

## 84.38 `CONFIG_ENTROPY_NEEDS_PRNG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

无提示选项（Promptless Option），用于表明熵源驱动（Entropy Driver）无法在较短时间内提供大量数据。因此，使用 `CTR_DRBG` 或 `HMAC_DRBG` 等密码算法（Crypto Algorithm）来解决此限制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_GENERATOR
```

**被选择（Selected by）**

```text
CONFIG_ENTROPY_MCUX_TRNG
```

**定义位置（Location）**：[`drivers/entropy/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_MCUX_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MCUX_TRNG)。

<a id="CONFIG_ENTROPY_NEORV32_TRNG"></a>

## 84.39 `CONFIG_ENTROPY_NEORV32_TRNG`

**提示（Prompt）**：NEORV32 真随机数发生器（TRNG）

**说明（Help）**

此选项启用 NEORV32 的真随机数发生器（True Random Number Generator，TRNG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NEORV32_TRNG_ENABLED && CONFIG_SYSCON && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.neorv32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.neorv32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_NPCX_DRBG"></a>

## 84.40 `CONFIG_ENTROPY_NPCX_DRBG`

**提示（Prompt）**：NPCX 确定性随机比特发生器（DRBG）驱动

**说明（Help）**

此选项启用 NPCX 系列处理器的确定性随机比特发生器（Deterministic Random Bit Generator，DRBG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_DRBG_ENABLED && CONFIG_SOC_NPCX9MFP && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NPCX9MFP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NPCX9MFP)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_NPCX_DRBG_RESEED_INTERVAL"></a>

## 84.41 `CONFIG_ENTROPY_NPCX_DRBG_RESEED_INTERVAL`

**提示（Prompt）**：DRBG 重新播种间隔（Reseed Interval）

**说明（Help）**

下一次重新播种（Reseeding）之前允许执行的生成次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_NPCX_DRBG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.npcx:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.npcx#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → NPCX 确定性随机比特发生器（DRBG）驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_NPCX_DRBG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NPCX_DRBG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_NPCX_DRBG_SECURITY_STRENGTH_112B"></a>

## 84.42 `CONFIG_ENTROPY_NPCX_DRBG_SECURITY_STRENGTH_112B`

**提示（Prompt）**：DRBG 112 位安全强度（Security Strength）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.npcx:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.npcx#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → NPCX 确定性随机比特发生器（DRBG）驱动 → DRBG 安全强度选择（Security Strength Selection）

<a id="CONFIG_ENTROPY_NPCX_DRBG_SECURITY_STRENGTH_128B"></a>

## 84.43 `CONFIG_ENTROPY_NPCX_DRBG_SECURITY_STRENGTH_128B`

**提示（Prompt）**：DRBG 128 位安全强度（Security Strength）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.npcx:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.npcx#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → NPCX 确定性随机比特发生器（DRBG）驱动 → DRBG 安全强度选择（Security Strength Selection）

<a id="CONFIG_ENTROPY_NPCX_DRBG_SECURITY_STRENGTH_128B_TEST"></a>

## 84.44 `CONFIG_ENTROPY_NPCX_DRBG_SECURITY_STRENGTH_128B_TEST`

**提示（Prompt）**：DRBG 12b 位安全强度测试（Security Strength Test，原文为 12b）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.npcx:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.npcx#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → NPCX 确定性随机比特发生器（DRBG）驱动 → DRBG 安全强度选择（Security Strength Selection）

<a id="CONFIG_ENTROPY_NPCX_DRBG_SECURITY_STRENGTH_192B"></a>

## 84.45 `CONFIG_ENTROPY_NPCX_DRBG_SECURITY_STRENGTH_192B`

**提示（Prompt）**：DRBG 192 位安全强度（Security Strength）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.npcx:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.npcx#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → NPCX 确定性随机比特发生器（DRBG）驱动 → DRBG 安全强度选择（Security Strength Selection）

<a id="CONFIG_ENTROPY_NPCX_DRBG_SECURITY_STRENGTH_256B"></a>

## 84.46 `CONFIG_ENTROPY_NPCX_DRBG_SECURITY_STRENGTH_256B`

**提示（Prompt）**：DRBG 256 位安全强度（Security Strength）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.npcx:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.npcx#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → NPCX 确定性随机比特发生器（DRBG）驱动 → DRBG 安全强度选择（Security Strength Selection）

<a id="CONFIG_ENTROPY_NPCX_DRBG_SECURITY_STRENGTH_256B_TEST"></a>

## 84.47 `CONFIG_ENTROPY_NPCX_DRBG_SECURITY_STRENGTH_256B_TEST`

**提示（Prompt）**：DRBG 256 位安全强度测试（Security Strength Test）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.npcx:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.npcx#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → NPCX 确定性随机比特发生器（DRBG）驱动 → DRBG 安全强度选择（Security Strength Selection）

<a id="CONFIG_ENTROPY_NRF5_BIAS_CORRECTION"></a>

## 84.48 `CONFIG_ENTROPY_NRF5_BIAS_CORRECTION`

**提示（Prompt）**：偏差校正（Bias Correction），均匀分布（Uniform Distribution）

**说明（Help）**

此选项启用 RNG 偏差校正（Bias Correction），保证 `0` 与 `1` 均匀分布（Uniform Distribution）。启用后，无法保证生成一个字节所需的时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_NRF5_RNG && CONFIG_ENTROPY_GENERATOR
```

**被选择（Selected by）**

```text
CONFIG_BT_LLL_VENDOR_NORDIC
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.nrf5:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.nrf5#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → nRF5 RNG 驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_NRF5_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF5_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_BT_LLL_VENDOR_NORDIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LLL_VENDOR_NORDIC)。

<a id="CONFIG_ENTROPY_NRF5_ISR_POOL_SIZE"></a>

## 84.49 `CONFIG_ENTROPY_NRF5_ISR_POOL_SIZE`

**提示（Prompt）**：中断模式随机数池大小（ISR-Mode Random Number Pool Size）

**说明（Help）**

用于存储硬件生成的熵字节（Entropy Bytes）的缓冲区长度，以字节为单位，以便中断服务程序（ISR）中的使用者获取。池大小必须是 2 的幂。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_NRF5_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[CONFIG_ENTROPY_NRF5_ISR_THRESHOLD, 256]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.nrf5:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.nrf5#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → nRF5 RNG 驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_NRF5_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF5_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_NRF5_ISR_THRESHOLD`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF5_ISR_THRESHOLD)。

<a id="CONFIG_ENTROPY_NRF5_ISR_THRESHOLD"></a>

## 84.50 `CONFIG_ENTROPY_NRF5_ISR_THRESHOLD`

**提示（Prompt）**：中断模式随机数池低水位阈值（ISR-Mode Pool Low-Water Threshold）

**说明（Help）**

为中断服务程序（ISR）中的使用者触发熵生成的低水位阈值（Low-Water Mark），以字节为单位。缓冲区中的可用字节数一旦低于此值，就启动硬件熵生成（Hardware Entropy Generation）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_NRF5_RNG && CONFIG_ENTROPY_GENERATOR
```

**取值范围（Ranges）**

```text
[12, 255]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.nrf5:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.nrf5#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → nRF5 RNG 驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_NRF5_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF5_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_NRF5_RNG"></a>

## 84.51 `CONFIG_ENTROPY_NRF5_RNG`

**提示（Prompt）**：nRF5 RNG 驱动

**说明（Help）**

此选项启用随机数发生器（RNG）外设。它基于内部热噪声（Thermal Noise）生成随机数，在主机读取时提供一个随机的 8 位值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ENTROPY_NRF_FORCE_ALT && DT_HAS_NORDIC_NRF_RNG_ENABLED && CONFIG_MULTITHREADING && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_BT_LLL_VENDOR_NORDIC
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.nrf5:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.nrf5#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_NRF_FORCE_ALT`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF_FORCE_ALT)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_BT_LLL_VENDOR_NORDIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LLL_VENDOR_NORDIC)。

<a id="CONFIG_ENTROPY_NRF5_THR_POOL_SIZE"></a>

## 84.52 `CONFIG_ENTROPY_NRF5_THR_POOL_SIZE`

**提示（Prompt）**：线程模式随机数池大小（Thread-Mode Random Number Pool Size）

**说明（Help）**

用于存储硬件生成的熵字节（Entropy Bytes）的缓冲区长度，以字节为单位，以便线程模式（Thread Mode）中的使用者获取。池大小必须是 2 的幂。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_NRF5_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[CONFIG_ENTROPY_NRF5_THR_THRESHOLD, 256]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.nrf5:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.nrf5#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → nRF5 RNG 驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_NRF5_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF5_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_NRF5_THR_THRESHOLD`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF5_THR_THRESHOLD)。

<a id="CONFIG_ENTROPY_NRF5_THR_THRESHOLD"></a>

## 84.53 `CONFIG_ENTROPY_NRF5_THR_THRESHOLD`

**提示（Prompt）**：线程模式随机数池低水位阈值（Thread-Mode Pool Low-Water Threshold）

**说明（Help）**

为线程模式（Thread Mode）中的使用者触发熵生成的低水位阈值（Low-Water Mark），以字节为单位。缓冲区中的可用字节数一旦低于此值，就启动硬件熵生成（Hardware Entropy Generation）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_NRF5_RNG && CONFIG_ENTROPY_GENERATOR
```

**取值范围（Ranges）**

```text
[4, 255]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.nrf5:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.nrf5#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → nRF5 RNG 驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_NRF5_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF5_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_NRF_CRACEN_CTR_DRBG"></a>

## 84.54 `CONFIG_ENTROPY_NRF_CRACEN_CTR_DRBG`

**提示（Prompt）**：基于 CRACEN CTR_DRBG 驱动的 nRF 熵源驱动（Entropy Driver）

**说明（Help）**

此选项启用基于 CRACEN 的熵源驱动（Entropy Driver），该驱动以 nrfx CRACEN CTR_DRBG 随机数驱动为基础。

注意：此驱动不兼容 54H 器件，而且只能由一个处理器核（Processor Core）使用。此驱动无法与 nRF Security PSA 方案同时使用，因为两者都会尝试独占 CRACEN 硬件；启用该方案时，应改选 PSA Crypto 熵源驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_CRACEN_CTRDRBG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
CONFIG_NRFX_CRACEN
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.nrf_cracen:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.nrf_cracen#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_NRFX_CRACEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CRACEN)。

<a id="CONFIG_ENTROPY_NRF_FORCE_ALT"></a>

## 84.55 `CONFIG_ENTROPY_NRF_FORCE_ALT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

可启用此选项，强制使用熵源驱动（Entropy Driver）的另一种实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_COMPATIBLE_NRF && CONFIG_ENTROPY_GENERATOR
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.nrf5:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.nrf5#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`。

<a id="CONFIG_ENTROPY_NXP_ELE_TRNG"></a>

## 84.56 `CONFIG_ENTROPY_NXP_ELE_TRNG`

**提示（Prompt）**：NXP ELE 真随机数发生器（TRNG）驱动

**说明（Help）**

此选项启用 ELE 真随机数发生器（True Random Number Generator，TRNG）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_ELE_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.nxp:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.nxp#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_NXP_ELS_TRNG"></a>

## 84.57 `CONFIG_ENTROPY_NXP_ELS_TRNG`

**提示（Prompt）**：NXP ELS 真随机数发生器（TRNG）驱动

**说明（Help）**

此选项启用 ELS 真随机数发生器（True Random Number Generator，TRNG）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_ELS_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.nxp:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.nxp#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_PSA_CRYPTO_RNG"></a>

## 84.58 `CONFIG_ENTROPY_PSA_CRYPTO_RNG`

**提示（Prompt）**：以 PSA Crypto 随机数源（Random Source）为基础的熵源驱动（Entropy Driver）

**说明（Help）**

启用以 PSA Crypto 为来源的熵源驱动（Entropy Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_PSA_CRYPTO_RNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.psa_crypto:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.psa_crypto#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_RENESAS_RA"></a>

## 84.59 `CONFIG_ENTROPY_RENESAS_RA`

**提示（Prompt）**：瑞萨（Renesas）RA TRNG 驱动

**说明（Help）**

此选项启用瑞萨（Renesas）RA 的熵源驱动（Entropy Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_RENESAS_RA_RSIP_E51A_TRNG_ENABLED || DT_HAS_RENESAS_RA_SCE9_RNG_ENABLED || DT_HAS_RENESAS_RA_SCE7_RNG_ENABLED || DT_HAS_RENESAS_RA_SCE5_RNG_ENABLED || DT_HAS_RENESAS_RA_TRNG_ENABLED || DT_HAS_RENESAS_RA_RSIP_E50D_TRNG_ENABLED) && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
CONFIG_USE_RA_FSP_SCE
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.renesas_ra:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.renesas_ra#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_USE_RA_FSP_SCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SCE)。

<a id="CONFIG_ENTROPY_RISCV_ZKR"></a>

## 84.60 `CONFIG_ENTROPY_RISCV_ZKR`

**提示（Prompt）**：RISC-V Zkr 熵源驱动（Entropy Driver）

**说明（Help）**

启用基于 RISC-V Zkr 扩展的 `seed` 控制与状态寄存器（CSR）的架构熵源驱动（Architectural Entropy Driver）。驱动直接返回 `seed` CSR 提供的熵比特（Entropy Bits），不进行调理（Conditioning）。此扩展保证每提供 16 位数据，至少具有 8 位最小熵（Min-Entropy）。内核运行在监督模式（S-Mode）时，机器模式（M-Mode）固件必须设置 `mseccfg.SSEED`，以授予对 `seed` CSR 的访问权限。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_ISA_EXT_ZKR && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_ENTROPY
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.riscv_zkr:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.riscv_zkr#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_ISA_EXT_ZKR`](P034_arch_riscv_配置项参考_1.md#CONFIG_RISCV_ISA_EXT_ZKR)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ARCH_HAS_ENTROPY`](P084_drivers_entropy_配置项参考.md#CONFIG_ARCH_HAS_ENTROPY)。

<a id="CONFIG_ENTROPY_RISCV_ZKR_MAX_RETRIES"></a>

## 84.61 `CONFIG_ENTROPY_RISCV_ZKR_MAX_RETRIES`

**提示（Prompt）**：RISC-V Zkr 熵源驱动的最大重试次数（Maximum Retries）

**说明（Help）**

连续访问 `seed` CSR 却未获得熵（Entropy）的最大允许次数，达到此次数后驱动放弃尝试。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_RISCV_ZKR && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.riscv_zkr:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.riscv_zkr#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → RISC-V Zkr 熵源驱动（Entropy Driver）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_RISCV_ZKR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_RISCV_ZKR)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_RISCV_ZKR_RETRY_WAIT_USEC"></a>

## 84.62 `CONFIG_ENTROPY_RISCV_ZKR_RETRY_WAIT_USEC`

**提示（Prompt）**：RISC-V Zkr 熵源驱动的重试等待时间（Retry Wait Time）

**说明（Help）**

一次访问未获得熵（Entropy）后，驱动再次访问 `seed` CSR 前等待的微秒数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_RISCV_ZKR && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.riscv_zkr:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.riscv_zkr#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → RISC-V Zkr 熵源驱动（Entropy Driver）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_RISCV_ZKR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_RISCV_ZKR)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_RPI_PICO_RNG"></a>

## 84.63 `CONFIG_ENTROPY_RPI_PICO_RNG`

**提示（Prompt）**：树莓派（Raspberry Pi）Pico 熵数发生器驱动（Entropy Number Generator Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_RNG_ENABLED && CONFIG_SOC_SERIES_RP2350 && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
CONFIG_PICOSDK_USE_CLAIM
CONFIG_PICOSDK_USE_RAND
CONFIG_PICOSDK_USE_TIMER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.rpi_pico:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.rpi_pico#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2350)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_PICOSDK_USE_CLAIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_CLAIM)、[`CONFIG_PICOSDK_USE_RAND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_RAND)、[`CONFIG_PICOSDK_USE_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_TIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RP2350`。

<a id="CONFIG_ENTROPY_RV32M1_TRNG"></a>

## 84.64 `CONFIG_ENTROPY_RV32M1_TRNG`

**提示（Prompt）**：RV32M1 真随机数发生器（TRNG）驱动

**说明（Help）**

此选项启用基于 RV32M1 TRNG 驱动的真随机数发生器（True Random Number Generator，TRNG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OPENISA_RV32M1_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.rv32m1:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.rv32m1#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_SAM_RNG"></a>

## 84.65 `CONFIG_ENTROPY_SAM_RNG`

**提示（Prompt）**：Atmel SAM 微控制器系列真随机数发生器（True Random Number Generator，TRNG）驱动

**说明（Help）**

为 Atmel SAM 微控制器（MCU）启用真随机数发生器（True Random Number Generator，TRNG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.sam:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.sam#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_SF32LB"></a>

## 84.66 `CONFIG_ENTROPY_SF32LB`

**提示（Prompt）**：SF32LB 熵源驱动（Entropy Driver）

**说明（Help）**

启用 SF32LB 真随机数发生器（True Random Number Generator，TRNG）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_SILABS_SIWX91X"></a>

## 84.67 `CONFIG_ENTROPY_SILABS_SIWX91X`

**提示（Prompt）**：Silabs SiWx91x RNG 驱动

**说明（Help）**

启用 Silicon Labs SiWx91x 芯片内嵌的硬件随机数发生器（Hardware Random Number Generator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_RNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.siwx91x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.siwx91x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_SMARTBOND_ISR_POOL_SIZE"></a>

## 84.68 `CONFIG_ENTROPY_SMARTBOND_ISR_POOL_SIZE`

**提示（Prompt）**：中断模式随机数池大小（ISR-Mode Random Number Pool Size）

**说明（Help）**

用于存储硬件生成的熵字节（Entropy Bytes）的缓冲区长度，以字节为单位，以便中断服务程序（ISR）中的使用者获取。池大小必须是 2 的幂。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_SMARTBOND_TRNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[CONFIG_ENTROPY_SMARTBOND_ISR_THRESHOLD, 256]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.smartbond:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.smartbond#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → Renesas Smartbond 微控制器系列真随机数发生器（True Random Number Generator，TRNG）驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_SMARTBOND_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_SMARTBOND_TRNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_SMARTBOND_ISR_THRESHOLD`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_SMARTBOND_ISR_THRESHOLD)。

<a id="CONFIG_ENTROPY_SMARTBOND_ISR_THRESHOLD"></a>

## 84.69 `CONFIG_ENTROPY_SMARTBOND_ISR_THRESHOLD`

**提示（Prompt）**：中断模式随机数池低水位阈值（ISR-Mode Pool Low-Water Threshold）

**说明（Help）**

为中断服务程序（ISR）中的使用者触发熵生成的低水位阈值（Low-Water Mark），以字节为单位。缓冲区中的可用字节数一旦低于此值，就启动硬件熵生成（Hardware Entropy Generation）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_SMARTBOND_TRNG && CONFIG_ENTROPY_GENERATOR
```

**取值范围（Ranges）**

```text
[12, 255]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.smartbond:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.smartbond#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → Renesas Smartbond 微控制器系列真随机数发生器（True Random Number Generator，TRNG）驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_SMARTBOND_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_SMARTBOND_TRNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_SMARTBOND_THR_POOL_SIZE"></a>

## 84.70 `CONFIG_ENTROPY_SMARTBOND_THR_POOL_SIZE`

**提示（Prompt）**：线程模式随机数池大小（Thread-Mode Random Number Pool Size）

**说明（Help）**

用于存储硬件生成的熵字节（Entropy Bytes）的缓冲区长度，以字节为单位，以便线程模式（Thread Mode）中的使用者获取。池大小必须是 2 的幂。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_SMARTBOND_TRNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[CONFIG_ENTROPY_SMARTBOND_THR_THRESHOLD, 256]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.smartbond:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.smartbond#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → Renesas Smartbond 微控制器系列真随机数发生器（True Random Number Generator，TRNG）驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_SMARTBOND_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_SMARTBOND_TRNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_SMARTBOND_THR_THRESHOLD`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_SMARTBOND_THR_THRESHOLD)。

<a id="CONFIG_ENTROPY_SMARTBOND_THR_THRESHOLD"></a>

## 84.71 `CONFIG_ENTROPY_SMARTBOND_THR_THRESHOLD`

**提示（Prompt）**：线程模式随机数池低水位阈值（Thread-Mode Pool Low-Water Threshold）

**说明（Help）**

为线程模式（Thread Mode）中的使用者触发熵生成的低水位阈值（Low-Water Mark），以字节为单位。缓冲区中的可用字节数一旦低于此值，就启动硬件熵生成（Hardware Entropy Generation）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_SMARTBOND_TRNG && CONFIG_ENTROPY_GENERATOR
```

**取值范围（Ranges）**

```text
[4, 255]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.smartbond:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.smartbond#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → Renesas Smartbond 微控制器系列真随机数发生器（True Random Number Generator，TRNG）驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_SMARTBOND_TRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_SMARTBOND_TRNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_SMARTBOND_TRNG"></a>

## 84.72 `CONFIG_ENTROPY_SMARTBOND_TRNG`

**提示（Prompt）**：Renesas Smartbond 微控制器系列真随机数发生器（True Random Number Generator，TRNG）驱动

**说明（Help）**

为瑞萨（Renesas）Smartbond 微控制器（MCU）启用真随机数发生器（True Random Number Generator，TRNG）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.smartbond:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.smartbond#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_STM32_CLK_CHECK"></a>

## 84.73 `CONFIG_ENTROPY_STM32_CLK_CHECK`

**提示（Prompt）**：运行时时钟配置检查（Runtime Clock Configuration Check）

**说明（Help）**

启用对随机数发生器（RNG）时钟配置的检查。正确的时钟配置取决于具体 STM32 系列；如果报告错误，请查阅参考手册（Reference Manual）。此检查假定时钟错误检测（Clock Error Detected，CED）位已启用；当该位可用时，默认启用 CED。如果禁用了 CED，也应禁用此检查。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_STM32WB0X && CONFIG_ENTROPY_STM32_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.stm32:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.stm32#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → STM32 RNG 驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_ENTROPY_STM32_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WB0X`。

<a id="CONFIG_ENTROPY_STM32_ISR_POOL_SIZE"></a>

## 84.74 `CONFIG_ENTROPY_STM32_ISR_POOL_SIZE`

**提示（Prompt）**：中断模式随机数池大小（ISR-Mode Random Number Pool Size）

**说明（Help）**

用于存储硬件生成的熵字节（Entropy Bytes）的缓冲区长度，以字节为单位，以便中断服务程序（ISR）中的使用者获取。池大小必须是 2 的幂。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_STM32_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[CONFIG_ENTROPY_STM32_ISR_THRESHOLD, 256]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.stm32:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.stm32#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → STM32 RNG 驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_STM32_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_STM32_ISR_THRESHOLD`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_ISR_THRESHOLD)。

<a id="CONFIG_ENTROPY_STM32_ISR_THRESHOLD"></a>

## 84.75 `CONFIG_ENTROPY_STM32_ISR_THRESHOLD`

**提示（Prompt）**：中断模式随机数池低水位阈值（ISR-Mode Pool Low-Water Threshold）

**说明（Help）**

为中断服务程序（ISR）中的使用者触发熵生成的低水位阈值（Low-Water Mark），以字节为单位。缓冲区中的可用字节数一旦低于此值，就启动硬件熵生成（Hardware Entropy Generation）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_STM32_RNG && CONFIG_ENTROPY_GENERATOR
```

**取值范围（Ranges）**

```text
[12, 255]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.stm32:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.stm32#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → STM32 RNG 驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_STM32_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_STM32_RNG"></a>

## 84.76 `CONFIG_ENTROPY_STM32_RNG`

**提示（Prompt）**：STM32 RNG 驱动

**说明（Help）**

此选项启用 RNG 处理单元（RNG Processor），它是基于连续模拟噪声（Continuous Analog Noise）的熵数发生器（Entropy Number Generator），读取时向主机提供一个 32 位熵值。它适用于 F4（STM32F401 和 STM32F411 除外）、L4、F7、H7 和 G4 系列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_RNG_ENABLED || DT_HAS_ST_STM32_RNG_NOIRQ_ENABLED) && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.stm32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.stm32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_STM32_THR_POOL_SIZE"></a>

## 84.77 `CONFIG_ENTROPY_STM32_THR_POOL_SIZE`

**提示（Prompt）**：线程模式随机数池大小（Thread-Mode Random Number Pool Size）

**说明（Help）**

用于存储硬件生成的熵字节（Entropy Bytes）的缓冲区长度，以字节为单位，以便线程模式（Thread Mode）中的使用者获取。池大小必须是 2 的幂。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_STM32_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[CONFIG_ENTROPY_STM32_THR_THRESHOLD, 256]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.stm32:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.stm32#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → STM32 RNG 驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_STM32_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_STM32_THR_THRESHOLD`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_THR_THRESHOLD)。

<a id="CONFIG_ENTROPY_STM32_THR_THRESHOLD"></a>

## 84.78 `CONFIG_ENTROPY_STM32_THR_THRESHOLD`

**提示（Prompt）**：线程模式随机数池低水位阈值（Thread-Mode Pool Low-Water Threshold）

**说明（Help）**

为线程模式（Thread Mode）中的使用者触发熵生成的低水位阈值（Low-Water Mark），以字节为单位。缓冲区中的可用字节数一旦低于此值，就启动硬件熵生成（Hardware Entropy Generation）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_STM32_RNG && CONFIG_ENTROPY_GENERATOR
```

**取值范围（Ranges）**

```text
[4, 255]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.stm32:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.stm32#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → STM32 RNG 驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_STM32_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_STM32_WORKQUEUE"></a>

## 84.79 `CONFIG_ENTROPY_STM32_WORKQUEUE`

**提示（Prompt）**：用于补充随机字节池的专用工作队列（Dedicated Workqueue）

**说明（Help）**

启用后，使用专用工作队列（Dedicated Workqueue）补充随机字节池（Random Bytes Pool）。禁用时，使用 Zephyr 的系统工作队列（System Workqueue），可减少 RAM 用量，但随机字节池的补充可能因系统工作队列中其他任务的行为而延迟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_STM32_RNG && CONFIG_ENTROPY_GENERATOR
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.stm32:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.stm32#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → STM32 RNG 驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_STM32_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_STM32_WQ_PRIO"></a>

## 84.80 `CONFIG_ENTROPY_STM32_WQ_PRIO`

**提示（Prompt）**：专用工作队列优先级（Dedicated Workqueue Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_STM32_WORKQUEUE && CONFIG_ENTROPY_STM32_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.stm32:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.stm32#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → STM32 RNG 驱动 → 用于补充随机字节池的专用工作队列（Dedicated Workqueue）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_STM32_WORKQUEUE`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_WORKQUEUE)、[`CONFIG_ENTROPY_STM32_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_STM32_WQ_STACK_SIZE"></a>

## 84.81 `CONFIG_ENTROPY_STM32_WQ_STACK_SIZE`

**提示（Prompt）**：专用工作队列栈大小（Dedicated Workqueue Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_STM32_WORKQUEUE && CONFIG_ENTROPY_STM32_RNG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
384
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.stm32:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.stm32#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → STM32 RNG 驱动 → 用于补充随机字节池的专用工作队列（Dedicated Workqueue）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_STM32_WORKQUEUE`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_WORKQUEUE)、[`CONFIG_ENTROPY_STM32_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_STM32_RNG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_ENTROPY_SY1XX_TRNG"></a>

## 84.82 `CONFIG_ENTROPY_SY1XX_TRNG`

**提示（Prompt）**：Sensry SY1xx SoC 系列真随机数发生器（True Random Number Generator，TRNG）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSRY_SY1XX_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.sy1xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.sy1xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_TELINK_B91_TRNG"></a>

## 84.83 `CONFIG_ENTROPY_TELINK_B91_TRNG`

**提示（Prompt）**：泰凌（Telink）B91 熵源驱动（Entropy Driver）

**说明（Help）**

启用 B91 熵源驱动（Entropy Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TELINK_B91_TRNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.b91:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.b91#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_VIRTIO"></a>

## 84.84 `CONFIG_ENTROPY_VIRTIO`

**提示（Prompt）**：VIRTIO 熵设备驱动（Entropy Device Driver）

**说明（Help）**

启用 VIRTIO 熵设备（Entropy Device）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VIRTIO_DEVICE4_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_VIRTIO
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.virtio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.virtio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_VIRTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIRTIO)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTROPY_WCH_RNG"></a>

## 84.85 `CONFIG_ENTROPY_WCH_RNG`

**提示（Prompt）**：WCH CH32 熵数发生器驱动（Entropy Number Generator Driver）

**说明（Help）**

此选项启用 CH32 SoC 的熵数发生器（Entropy Number Generator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_RNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.wch:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.wch#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_ENTRY_MCUX_CAAM_POOL_SIZE"></a>

## 84.86 `CONFIG_ENTRY_MCUX_CAAM_POOL_SIZE`

**提示（Prompt）**：CAAM 随机数池大小（Random Number Pool Size）

**说明（Help）**

用于存储 CAAM 硬件生成的随机字节（Random Bytes）的缓冲区长度，以字节为单位。池大小必须是 2 的幂。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_MCUX_CAAM && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[4, 1024]
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.mcux:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.mcux#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → MCUX CAAM 驱动

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_MCUX_CAAM`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MCUX_CAAM)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_FAKE_ENTROPY_NATIVE_SIM"></a>

## 84.87 `CONFIG_FAKE_ENTROPY_NATIVE_SIM`

**提示（Prompt）**：原生模拟器熵源驱动（Native Simulator Entropy Driver）

**说明（Help）**

此选项启用 `native_sim` 开发板（`ARCH_POSIX`）的测试随机数发生器（Test Random Number Generator），它基于主机的 `random()` API。此熵发生器仅用于测试，不生成真正的熵（Real Entropy）。实际上，只要以相同的种子（Seed）初始化，它就始终生成相同的随机数序列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_SIM_RNG_ENABLED && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.native_sim:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.native_sim#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_FAKE_ENTROPY_NATIVE_SIM_SEED_BY_DEFAULT"></a>

## 84.88 `CONFIG_FAKE_ENTROPY_NATIVE_SIM_SEED_BY_DEFAULT`

**提示（Prompt）**：默认对发生器播种（Seed by Default）

**说明（Help）**

即使用户未通过命令行（Command Line）请求，也默认应用一个种子（Seed）。禁用此功能后，其他组件可以为主机标准库的随机数发生器播种，而不会受到本组件默认初始化过程的干扰。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FAKE_ENTROPY_NATIVE_SIM && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/entropy/Kconfig.native_sim:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/Kconfig.native_sim#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → 原生模拟器熵源驱动（Native Simulator Entropy Driver）

**配置项引用（Symbol References）**：[`CONFIG_FAKE_ENTROPY_NATIVE_SIM`](P084_drivers_entropy_配置项参考.md#CONFIG_FAKE_ENTROPY_NATIVE_SIM)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<!-- kconfig-navigation -->

[上一章](P083_drivers_eeprom_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P085_drivers_espi_配置项参考_1.md)
