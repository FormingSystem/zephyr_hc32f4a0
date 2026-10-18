---
id: learning.zephyr-docs.kconfig-reference.page-123
title: "`drivers/misc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第123章\_`drivers/misc`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/misc` 的 54 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DEVMUX"></a>

## 123.1 `CONFIG_DEVMUX`

**提示（Prompt）**：设备多路复用器（Device Multiplexer，devmux）【实验性】

**说明（Help）**

Devmux 是充当设备切换器的伪设备（Pseudo-device）。它允许软件从多个关联设备中选择数据（Data）、配置（Config）和 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_DEVMUX_ENABLED && CONFIG_DEVICE_MUTABLE
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/misc/devmux/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/devmux/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DEVICE_MUTABLE`](P001_kernel_配置项参考_1.md#CONFIG_DEVICE_MUTABLE)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_DEVMUX_INIT_PRIORITY"></a>

## 123.2 `CONFIG_DEVMUX_INIT_PRIORITY`

**提示（Prompt）**：Devmux 初始化优先级（Initialization Priority）

**说明（Help）**

Devmux 驱动的初始化优先级，必须大于初始选中的被复用设备的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DEVMUX
```

**默认值（Defaults）**

```text
51
```

**定义位置（Location）**：[`drivers/misc/devmux/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/devmux/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → 设备多路复用器（Device Multiplexer，devmux）【实验性】

**配置项引用（Symbol References）**：[`CONFIG_DEVMUX`](P123_drivers_misc_配置项参考.md#CONFIG_DEVMUX)。

<a id="CONFIG_ESP_HOSTED_MCU"></a>

## 123.3 `CONFIG_ESP_HOSTED_MCU`

**提示（Prompt）**：esp-hosted-mcu 传输核心（Transport Core）

**说明（Help）**

通用主机侧传输层，用于与运行 esp-hosted-mcu 协处理器固件的外部 Espressif 协处理器通信。它管理 SPI 或 SDIO 链路、帧解复用（Demultiplexing）及远程过程调用（RPC）往返机制。Wi-Fi 网络接口（Netif）驱动或蓝牙 HCI 驱动等协议使用方在其上构建。此项不直接选择，而由使用方选中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP_HOSTED_MCU_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_NANOPB
CONFIG_NANOPB_ENABLE_MALLOC
```

**被选择（Selected by）**

```text
CONFIG_BT_HCI_ESP_HOSTED_MCU
CONFIG_WIFI_ESP_HOSTED_MCU
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_NANOPB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NANOPB)、[`CONFIG_NANOPB_ENABLE_MALLOC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NANOPB_ENABLE_MALLOC)、[`CONFIG_BT_HCI_ESP_HOSTED_MCU`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_ESP_HOSTED_MCU)、[`CONFIG_WIFI_ESP_HOSTED_MCU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP_HOSTED_MCU)。

<a id="CONFIG_ESP_HOSTED_MCU_EVENT_TASK_POLL_MS"></a>

## 123.4 `CONFIG_ESP_HOSTED_MCU_EVENT_TASK_POLL_MS`

**提示（Prompt）**：事件任务轮询周期（Poll Rate），单位为毫秒

**说明（Help）**

限制接收线程等待协处理器数据就绪信号的时长；达到上限后，即使没有信号也检查一次。在 SPI 上，数据就绪 GPIO 是正常唤醒源，此值仅限制等待时间，因此采样该引脚不会占用总线。在 SDIO 上，协处理器在状态寄存器中标记待处理帧，但不驱动 DAT1，因此不会触发卡中断，真正发现输入数据的是此轮询。每次检查只读取一个四字节寄存器，所以该间隔决定最坏接收延迟：每个请求和响应最多各等待一个轮询周期。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_HOSTED_MCU
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)。

<a id="CONFIG_ESP_HOSTED_MCU_EVENT_TASK_PRIORITY"></a>

## 123.5 `CONFIG_ESP_HOSTED_MCU_EVENT_TASK_PRIORITY`

**提示（Prompt）**：事件任务优先级（Task Priority）

**说明（Help）**

接收／事件线程的优先级。必须始终高于其供给数据的使用方线程，即数值更小，避免繁忙的使用方阻塞帧接收。默认采用可抢占线程（Preemptible）；负值会使线程成为协作式（Cooperative）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_HOSTED_MCU
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)。

<a id="CONFIG_ESP_HOSTED_MCU_EVENT_TASK_STACK_SIZE"></a>

## 123.6 `CONFIG_ESP_HOSTED_MCU_EVENT_TASK_STACK_SIZE`

**提示（Prompt）**：事件任务栈大小（Stack Size）

**说明（Help）**

接收／事件线程的栈大小。RPC 帧会解码为驻留栈上的 `Rpc` 消息，因此必须容纳驱动处理的最大响应。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_HOSTED_MCU
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)。

<a id="CONFIG_ESP_HOSTED_MCU_FW_VERSION_MAJOR"></a>

## 123.7 `CONFIG_ESP_HOSTED_MCU_FW_VERSION_MAJOR`

**提示（Prompt）**：预期协处理器固件主版本（Major Version）

**说明（Help）**

此主机针对其构建的 esp-hosted-mcu 协处理器固件主版本。固件在独立芯片上运行，并单独烧录，因此无法在构建时强制检查；驱动会查询运行中的固件，并在主版本不同时给出警告。此配置不会改变主机使用的协议。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_HOSTED_MCU
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)。

<a id="CONFIG_ESP_HOSTED_MCU_FW_VERSION_MINOR"></a>

## 123.8 `CONFIG_ESP_HOSTED_MCU_FW_VERSION_MINOR`

**提示（Prompt）**：预期协处理器固件次版本（Minor Version）

**说明（Help）**

预期协处理器固件的次版本。会在版本日志行中报告，但不同也不会发出警告。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_HOSTED_MCU
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)。

<a id="CONFIG_ESP_HOSTED_MCU_FW_VERSION_PATCH"></a>

## 123.9 `CONFIG_ESP_HOSTED_MCU_FW_VERSION_PATCH`

**提示（Prompt）**：预期协处理器固件补丁版本（Patch Version）

**说明（Help）**

预期协处理器固件的补丁版本。会在版本日志行中报告，但不同也不会发出警告。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_HOSTED_MCU
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)。

<a id="CONFIG_ESP_HOSTED_MCU_INIT_PRIORITY"></a>

## 123.10 `CONFIG_ESP_HOSTED_MCU_INIT_PRIORITY`

**提示（Prompt）**：esp-hosted-mcu 核心初始化优先级（Initialization Priority）

**说明（Help）**

核心设备在 `POST_KERNEL` 级别的初始化优先级。它由所用总线的优先级推导，所以开发板调整总线优先级时，核心优先级也会随之变化。使用方驱动的优先级，例如 `CONFIG_WIFI_INIT_PRIORITY`，数值必须保持更大，保证使用方注册处理程序并操作协处理器之前，链路和接收线程已存在。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_HOSTED_MCU
```

**默认值（Defaults）**

```text
CONFIG_SDHC_INIT_PRIORITY if CONFIG_ESP_HOSTED_MCU_SDIO
CONFIG_SPI_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)、[`CONFIG_SDHC_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC_INIT_PRIORITY)、[`CONFIG_ESP_HOSTED_MCU_SDIO`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU_SDIO)、[`CONFIG_SPI_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_INIT_PRIORITY)。

<a id="CONFIG_ESP_HOSTED_MCU_RESET_PULSE_MS"></a>

## 123.11 `CONFIG_ESP_HOSTED_MCU_RESET_PULSE_MS`

**提示（Prompt）**：复位脉冲宽度（Reset Pulse Width，毫秒）

**说明（Help）**

为重启协处理器，复位线保持有效状态（Asserted）的时长。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_HOSTED_MCU
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[1, 1000]
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)。

<a id="CONFIG_ESP_HOSTED_MCU_SDIO"></a>

## 123.12 `CONFIG_ESP_HOSTED_MCU_SDIO`

**提示（Prompt）**：SDIO 传输（Transport）

**说明（Help）**

通过 SDIO 总线与协处理器通信，使用 SLC 寄存器窗口和复位 GPIO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SDHC
CONFIG_SDIO_STACK
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core） → esp-hosted-mcu 传输方式（Transport）

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC)、[`CONFIG_SDIO_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDIO_STACK)。

<a id="CONFIG_ESP_HOSTED_MCU_SPI"></a>

## 123.13 `CONFIG_ESP_HOSTED_MCU_SPI`

**提示（Prompt）**：SPI 传输（Transport）

**说明（Help）**

通过 SPI 与协处理器通信，并使用复位、握手（Handshake）和数据就绪（Data-ready）GPIO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core） → esp-hosted-mcu 传输方式（Transport）

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ESP_HOSTED_MCU_SPI_RESET_SETTLE_MS"></a>

## 123.14 `CONFIG_ESP_HOSTED_MCU_SPI_RESET_SETTLE_MS`

**提示（Prompt）**：复位后延迟（Delay after Reset，毫秒）

**说明（Help）**

释放复位后、使用总线前的等待时长。协处理器会在能够响应之前很早就置起握手和数据就绪信号，因此两者都不能标志启动结束，只有此延迟覆盖这段启动时间。如果协处理器在冷启动（Cold Boot）后漏掉最初的请求，应增大此值。SDIO 无需同类延迟，因为它会反复尝试枚举，直到协处理器响应。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_HOSTED_MCU_SPI && CONFIG_ESP_HOSTED_MCU
```

**默认值（Defaults）**

```text
500
```

**取值范围（Ranges）**

```text
[0, 5000]
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU_SPI`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU_SPI)、[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)。

<a id="CONFIG_ESP_HOSTED_MCU_TRANSPORT"></a>

## 123.15 `CONFIG_ESP_HOSTED_MCU_TRANSPORT`

**提示（Prompt）**：esp-hosted-mcu 传输方式（Transport）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_HOSTED_MCU
```

**默认值（Defaults）**

```text
CONFIG_ESP_HOSTED_MCU_SPI if n
CONFIG_ESP_HOSTED_MCU_SDIO
```

**可选项（Choices）**

```text
CONFIG_ESP_HOSTED_MCU_SPI
CONFIG_ESP_HOSTED_MCU_SDIO
```

**定义位置（Location）**：[`drivers/misc/esp_hosted_mcu/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/esp_hosted_mcu/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)、[`CONFIG_ESP_HOSTED_MCU_SPI`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU_SPI)、[`CONFIG_ESP_HOSTED_MCU_SDIO`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU_SDIO)。

<a id="CONFIG_ETHOS_U_ARM"></a>

## 123.16 `CONFIG_ETHOS_U_ARM`

**提示（Prompt）**：Arm Ethos-U 神经网络处理单元（NPU）驱动

**说明（Help）**

启用 Arm Ethos-U NPU 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/misc/ethos_u/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/ethos_u/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → 选择厂商 Ethos-U NPU 驱动

<a id="CONFIG_ETHOS_U_DCACHE"></a>

## 123.17 `CONFIG_ETHOS_U_DCACHE`

**提示（Prompt）**：覆盖 Ethos-U 驱动的数据缓存（DCache）函数

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETHOS_U
```

**默认值（Defaults）**

```text
y if CONFIG_CACHE_MANAGEMENT
```

**定义位置（Location）**：[`drivers/misc/ethos_u/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/ethos_u/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETHOS_U`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETHOS_U)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)。

<a id="CONFIG_ETHOS_U_INFINEON"></a>

## 123.18 `CONFIG_ETHOS_U_INFINEON`

**提示（Prompt）**：Infineon PSE84 Ethos-U NPU 驱动

**说明（Help）**

启用 Arm Ethos-U NPU 驱动的 Infineon PSE84 前端（Frontend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/misc/ethos_u/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/ethos_u/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → 选择厂商 Ethos-U NPU 驱动

<a id="CONFIG_ETHOS_U_NUMAKER"></a>

## 123.19 `CONFIG_ETHOS_U_NUMAKER`

**提示（Prompt）**：Nuvoton NuMaker Ethos-U NPU 驱动

**说明（Help）**

启用 Arm Ethos-U NPU 驱动的 Nuvoton NuMaker 前端（Frontend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/misc/ethos_u/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/ethos_u/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → 选择厂商 Ethos-U NPU 驱动

<a id="CONFIG_ETHOS_U_RENESAS"></a>

## 123.20 `CONFIG_ETHOS_U_RENESAS`

**提示（Prompt）**：Renesas RA Ethos-U NPU 驱动

**说明（Help）**

启用 Arm Ethos-U NPU 驱动的 Renesas RA 前端（Frontend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/misc/ethos_u/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/ethos_u/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → 选择厂商 Ethos-U NPU 驱动

<a id="CONFIG_FT800"></a>

## 123.21 `CONFIG_FT800`

**提示（Prompt）**：FT800 嵌入式视频引擎（Embedded Video Engine）驱动

**说明（Help）**

启用 FT800 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FTDI_FT800_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/misc/ft8xx/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/ft8xx/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_FT800_INIT_PRIORITY"></a>

## 123.22 `CONFIG_FT800_INIT_PRIORITY`

**提示（Prompt）**：FT800 初始化优先级（Initialization Priority）

**说明（Help）**

FT800 驱动在 `POST_KERNEL` 级别的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FT800
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/misc/ft8xx/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/ft8xx/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → FT800 嵌入式视频引擎（Embedded Video Engine）驱动

**配置项引用（Symbol References）**：[`CONFIG_FT800`](P123_drivers_misc_配置项参考.md#CONFIG_FT800)。

<a id="CONFIG_GROVE_LCD_RGB"></a>

## 123.23 `CONFIG_GROVE_LCD_RGB`

**提示（Prompt）**：Seeed Grove LCD RGB 背光（Backlight）

**说明（Help）**

设置此值将启用 Grove-LCD RGB 背光驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SEEED_GROVE_LCD_RGB_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/misc/grove_lcd_rgb/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/grove_lcd_rgb/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

<a id="CONFIG_MCUX_FLEXIO"></a>

## 123.24 `CONFIG_MCUX_FLEXIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 FlexIO 控制器驱动。用户不能直接选择此驱动；应由其他 FlexIO 驱动启用，以便共享 FlexIO 设备资源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FLEXIO_ENABLED && CONFIG_CLOCK_CONTROL
```

**被选择（Selected by）**

```text
CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF
CONFIG_PWM_NXP_FLEXIO
CONFIG_SPI_MCUX_FLEXIO
CONFIG_VIDEO_MCUX_FLEXIO
```

**定义位置（Location）**：[`drivers/misc/mcux_flexio/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/mcux_flexio/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF)、[`CONFIG_PWM_NXP_FLEXIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_NXP_FLEXIO)、[`CONFIG_SPI_MCUX_FLEXIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_MCUX_FLEXIO)、[`CONFIG_VIDEO_MCUX_FLEXIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_MCUX_FLEXIO)。

<a id="CONFIG_MCUX_FLEXIO_INIT_PRIORITY"></a>

## 123.25 `CONFIG_MCUX_FLEXIO_INIT_PRIORITY`

**提示（Prompt）**：FlexIO 控制器驱动初始化优先级

**说明（Help）**

MCUX FlexIO 设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_FLEXIO
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/misc/mcux_flexio/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/mcux_flexio/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_FLEXIO`](P123_drivers_misc_配置项参考.md#CONFIG_MCUX_FLEXIO)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_MEDIAMIX_BLK_CTRL_INIT_PRIORITY"></a>

## 123.26 `CONFIG_MEDIAMIX_BLK_CTRL_INIT_PRIORITY`

**提示（Prompt）**：MEDIAMIX 初始化优先级（Initialization Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_MEDIAMIX_BLK_CTRL
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/misc/nxp_imx93_mediamix/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/nxp_imx93_mediamix/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP MEDIAMIX 模块控制（Block Control）驱动

**配置项引用（Symbol References）**：[`CONFIG_NXP_MEDIAMIX_BLK_CTRL`](P123_drivers_misc_配置项参考.md#CONFIG_NXP_MEDIAMIX_BLK_CTRL)。

<a id="CONFIG_MISC_MAX2221X"></a>

## 123.27 `CONFIG_MISC_MAX2221X`

**提示（Prompt）**：Analog Devices MAX22216/MAX22217 杂项（Misc）驱动

**说明（Help）**

启用 MAX2221X MISC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX2221X_MISC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/misc/max2221x/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/max2221x/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MISC_MAX2221X_INIT_PRIORITY"></a>

## 123.28 `CONFIG_MISC_MAX2221X_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

Analog Devices MAX22216/MAX22217 杂项驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MISC_MAX2221X
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/misc/max2221x/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/max2221x/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Analog Devices MAX22216/MAX22217 杂项（Misc）驱动

**配置项引用（Symbol References）**：[`CONFIG_MISC_MAX2221X`](P123_drivers_misc_配置项参考.md#CONFIG_MISC_MAX2221X)。

<a id="CONFIG_NORDIC_VPR_LAUNCHER"></a>

## 123.29 `CONFIG_NORDIC_VPR_LAUNCHER`

**提示（Prompt）**：Nordic VPR 协处理器启动器（Coprocessor Launcher）

**说明（Help）**

启用后，VPR 协处理器会在系统初始化期间自动启动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_VPR_COPROCESSOR_ENABLED && n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/misc/nordic_vpr_launcher/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/nordic_vpr_launcher/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

<a id="CONFIG_NORDIC_VPR_LAUNCHER_INIT_PRIORITY"></a>

## 123.30 `CONFIG_NORDIC_VPR_LAUNCHER_INIT_PRIORITY`

**提示（Prompt）**：Nordic VPR 协处理器启动器初始化优先级

**说明（Help）**

VPR 协处理器启动器的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NORDIC_VPR_LAUNCHER
```

**默认值（Defaults）**

```text
44 if DT_HAS_NORDIC_CORESIGHT_NRF_ENABLED
11 if CONFIG_MBOX_NRF_VEVIF_EVENT_USE_54L_ERRATA_16
0
```

**定义位置（Location）**：[`drivers/misc/nordic_vpr_launcher/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/nordic_vpr_launcher/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Nordic VPR 协处理器启动器（Coprocessor Launcher）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_VPR_LAUNCHER`](P123_drivers_misc_配置项参考.md#CONFIG_NORDIC_VPR_LAUNCHER)、[`CONFIG_MBOX_NRF_VEVIF_EVENT_USE_54L_ERRATA_16`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX_NRF_VEVIF_EVENT_USE_54L_ERRATA_16)。

<a id="CONFIG_NXP_FLEXRAM_ERROR_INTERRUPT"></a>

## 123.31 `CONFIG_NXP_FLEXRAM_ERROR_INTERRUPT`

**提示（Prompt）**：NXP FlexRAM 错误中断（Error Interrupt）

**说明（Help）**

允许 FlexRAM 产生错误中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_FLEXRAM
```

**定义位置（Location）**：[`drivers/misc/nxp_flexram/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/nxp_flexram/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NXP_FLEXRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_FLEXRAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NXP_FLEXRAM`。

<a id="CONFIG_NXP_FLEXRAM_MAGIC_ADDR_API"></a>

## 123.32 `CONFIG_NXP_FLEXRAM_MAGIC_ADDR_API`

**提示（Prompt）**：NXP FlexRAM 魔术地址（Magic Address）API

**说明（Help）**

启用用于 FlexRAM 魔术地址功能的 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT11XX && CONFIG_NXP_FLEXRAM
```

**定义位置（Location）**：[`drivers/misc/nxp_flexram/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/nxp_flexram/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_NXP_FLEXRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_FLEXRAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_NXP_FLEXRAM`。

<a id="CONFIG_NXP_INPUTMUX"></a>

## 123.33 `CONFIG_NXP_INPUTMUX`

**提示（Prompt）**：NXP INPUTMUX 驱动

**说明（Help）**

纳入部分 NXP 微控制器上 INPUTMUX 外设的硬件抽象层（HAL）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT685S_HIFI4
CONFIG_SOC_MIMXRT798S_HIFI4
CONFIG_DMA_MCUX_LPC
CONFIG_DMA_MCUX_SMARTDMA
CONFIG_NXP_PINT
CONFIG_MUX_NXP_INPUTMUX
```

**定义位置（Location）**：[`drivers/misc/nxp_inputmux/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/nxp_inputmux/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_MIMXRT685S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_HIFI4)、[`CONFIG_SOC_MIMXRT798S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI4)、[`CONFIG_DMA_MCUX_LPC`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_LPC)、[`CONFIG_DMA_MCUX_SMARTDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_SMARTDMA)、[`CONFIG_NXP_PINT`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_NXP_PINT)、[`CONFIG_MUX_NXP_INPUTMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MUX_NXP_INPUTMUX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_MIMXRT685S_HIFI4`。

<a id="CONFIG_NXP_MEDIAMIX_BLK_CTRL"></a>

## 123.34 `CONFIG_NXP_MEDIAMIX_BLK_CTRL`

**提示（Prompt）**：NXP MEDIAMIX 模块控制（Block Control）驱动

**说明（Help）**

启用 MEDIAMIX 模块控制（Block Control）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX93_MEDIAMIX_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/misc/nxp_imx93_mediamix/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/nxp_imx93_mediamix/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

<a id="CONFIG_NXP_RTXXX_DSP_CTRL"></a>

## 123.35 `CONFIG_NXP_RTXXX_DSP_CTRL`

**提示（Prompt）**：NXP i.MX RTxxx DSP 控制（Control）

**说明（Help）**

启用 NXP i.MX RTxxx 设备的数字信号处理器（DSP）控制驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_RT600_DSP_CTRL_ENABLED || DT_HAS_NXP_RT700_DSP_CTRL_HIFI4_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/misc/nxp_rtxxx_dsp_ctrl/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/nxp_rtxxx_dsp_ctrl/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

<a id="CONFIG_NXP_S32_EMIOS"></a>

## 123.36 `CONFIG_NXP_S32_EMIOS`

**提示（Prompt）**：NXP S32 eMIOS 驱动

**说明（Help）**

启用 NXP S32 eMIOS 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_EMIOS_ENABLED
```

**被选择（Selected by）**

```text
CONFIG_PWM_NXP_S32_EMIOS
CONFIG_QDEC_NXP_S32
```

**定义位置（Location）**：[`drivers/misc/nxp_s32_emios/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/nxp_s32_emios/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_PWM_NXP_S32_EMIOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_NXP_S32_EMIOS)、[`CONFIG_QDEC_NXP_S32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QDEC_NXP_S32)。

<a id="CONFIG_NXP_S32_EMIOS_INIT_PRIORITY"></a>

## 123.37 `CONFIG_NXP_S32_EMIOS_INIT_PRIORITY`

**提示（Prompt）**：NXP S32 eMIOS 初始化优先级

**说明（Help）**

NXP S32 eMIOS 驱动的系统初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_S32_EMIOS
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/misc/nxp_s32_emios/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/nxp_s32_emios/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → NXP S32 eMIOS 驱动

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_EMIOS`](P123_drivers_misc_配置项参考.md#CONFIG_NXP_S32_EMIOS)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_PIO_RPI_PICO"></a>

## 123.38 `CONFIG_PIO_RPI_PICO`

**提示（Prompt）**：Raspberry Pi Pico 可编程 I/O（PIO）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_PIO_ENABLED && CONFIG_RESET
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_PIO
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/misc/pio_rpi_pico/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/pio_rpi_pico/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_PICOSDK_USE_PIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_PIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_RENESAS_DAVE2D_RUNTIME_HEAP_SIZE"></a>

## 123.39 `CONFIG_RENESAS_DAVE2D_RUNTIME_HEAP_SIZE`

**提示（Prompt）**：Renesas DAVE2D 运行时堆大小（Runtime Heap Size）

**说明（Help）**

设置 DAVE2D 驱动运行时堆的大小。此堆用于运行期间的动态内存分配（Dynamic Memory Allocation）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RENESAS_RA_DRW && CONFIG_RENESAS_DRW
```

**默认值（Defaults）**

```text
32768
```

**定义位置（Location）**：[`drivers/misc/renesas_drw/Kconfig.renesas_ra_drw:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/renesas_drw/Kconfig.renesas_ra_drw#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Renesas DRW 驱动 → Renesas RA DRW 驱动

**配置项引用（Symbol References）**：[`CONFIG_RENESAS_RA_DRW`](P123_drivers_misc_配置项参考.md#CONFIG_RENESAS_RA_DRW)、[`CONFIG_RENESAS_DRW`](P123_drivers_misc_配置项参考.md#CONFIG_RENESAS_DRW)。

<a id="CONFIG_RENESAS_DRW"></a>

## 123.40 `CONFIG_RENESAS_DRW`

**提示（Prompt）**：Renesas DRW 驱动

**说明（Help）**

启用 Renesas DRW 驱动的配置选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**被弱选择（Implied by）**

```text
CONFIG_LV_Z_DRAW_DAVE2D
CONFIG_LV_Z_DRAW_DAVE2D
```

**定义位置（Location）**：[`drivers/misc/renesas_drw/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/renesas_drw/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_LV_Z_DRAW_DAVE2D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_DRAW_DAVE2D)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_DRW_INIT_PRIORITY"></a>

## 123.41 `CONFIG_RENESAS_DRW_INIT_PRIORITY`

**提示（Prompt）**：Renesas DRW 初始化优先级

**说明（Help）**

Renesas DRW 驱动的系统初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RENESAS_DRW
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/misc/renesas_drw/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/renesas_drw/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Renesas DRW 驱动

**配置项引用（Symbol References）**：[`CONFIG_RENESAS_DRW`](P123_drivers_misc_配置项参考.md#CONFIG_RENESAS_DRW)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_RENESAS_ELC"></a>

## 123.42 `CONFIG_RENESAS_ELC`

**提示（Prompt）**：Renesas 事件链接控制器（Event Link Controller）驱动

**说明（Help）**

启用 Renesas 事件链接控制器的配置选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
```

**定义位置（Location）**：[`drivers/misc/interconn/renesas_elc/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/interconn/renesas_elc/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → 互连驱动（Interconn Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`。

<a id="CONFIG_RENESAS_ELC_INIT_PRIORITY"></a>

## 123.43 `CONFIG_RENESAS_ELC_INIT_PRIORITY`

**提示（Prompt）**：Renesas 事件链接控制器初始化优先级

**说明（Help）**

Renesas 事件链接控制器驱动的系统初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RENESAS_ELC
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/misc/interconn/renesas_elc/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/interconn/renesas_elc/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → 互连驱动（Interconn Drivers） → Renesas 事件链接控制器（Event Link Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_RENESAS_ELC`](P123_drivers_misc_配置项参考.md#CONFIG_RENESAS_ELC)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_RENESAS_RA_DRW"></a>

## 123.44 `CONFIG_RENESAS_RA_DRW`

**提示（Prompt）**：Renesas RA DRW 驱动

**说明（Help）**

启用 Renesas DRW 驱动的配置选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_DRW_ENABLED && CONFIG_RENESAS_DRW
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DRW
```

**定义位置（Location）**：[`drivers/misc/renesas_drw/Kconfig.renesas_ra_drw:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/renesas_drw/Kconfig.renesas_ra_drw#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Renesas DRW 驱动

**配置项引用（Symbol References）**：[`CONFIG_RENESAS_DRW`](P123_drivers_misc_配置项参考.md#CONFIG_RENESAS_DRW)、[`CONFIG_USE_RA_FSP_DRW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DRW)。

<a id="CONFIG_RENESAS_RA_ELC"></a>

## 123.45 `CONFIG_RENESAS_RA_ELC`

**提示（Prompt）**：Renesas RA 事件链接控制器驱动

**说明（Help）**

启用 Renesas RA 事件链接控制器的配置选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_ELC_ENABLED && CONFIG_RENESAS_ELC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_ELC
```

**定义位置（Location）**：[`drivers/misc/interconn/renesas_elc/Kconfig.renesas_ra_elc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/interconn/renesas_elc/Kconfig.renesas_ra_elc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → 互连驱动（Interconn Drivers） → Renesas 事件链接控制器（Event Link Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_RENESAS_ELC`](P123_drivers_misc_配置项参考.md#CONFIG_RENESAS_ELC)、[`CONFIG_USE_RA_FSP_ELC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_ELC)。

<a id="CONFIG_RENESAS_RA_EXTERNAL_INTERRUPT"></a>

## 123.46 `CONFIG_RENESAS_RA_EXTERNAL_INTERRUPT`

**提示（Prompt）**：Renesas RA 外部中断（External Interrupt）驱动

**说明（Help）**

启用 Renesas RA 外部中断的配置选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_EXTERNAL_INTERRUPT_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/misc/renesas_ra_external_interrupt/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/renesas_ra_external_interrupt/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

<a id="CONFIG_RENESAS_RX_DTC"></a>

## 123.47 `CONFIG_RENESAS_RX_DTC`

**提示（Prompt）**：Renesas RX 数据传输控制器（Data Transfer Controller，DTC）驱动

**说明（Help）**

启用 Renesas RX 数据传输控制器的配置选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_DTC_ENABLED
```

**被选择（Selected by）**

```text
CONFIG_RENESAS_RX_I2C_DTC
CONFIG_UART_RENESAS_RX
CONFIG_SPI_RENESAS_RX_DTC
```

**定义位置（Location）**：[`drivers/misc/renesas_rx_dtc/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/renesas_rx_dtc/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RENESAS_RX_I2C_DTC`](P106_drivers_i2c_配置项参考_2.md#CONFIG_RENESAS_RX_I2C_DTC)、[`CONFIG_UART_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RX)、[`CONFIG_SPI_RENESAS_RX_DTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RENESAS_RX_DTC)。

<a id="CONFIG_RENESAS_RX_EXTERNAL_INTERRUPT"></a>

## 123.48 `CONFIG_RENESAS_RX_EXTERNAL_INTERRUPT`

**提示（Prompt）**：Renesas RX 外部中断驱动

**说明（Help）**

启用 Renesas RX 外部中断的配置选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_EXTERNAL_INTERRUPT_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/misc/renesas_rx_external_interrupt/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/renesas_rx_external_interrupt/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

<a id="CONFIG_TI_TDP2004"></a>

## 123.49 `CONFIG_TI_TDP2004`

**提示（Prompt）**：TDP2004 四通道 20 Gbps DisplayPort 2.1 和 12 Gbps HDMI 2.1 线性重驱动器（Linear Redriver）

**说明（Help）**

TDP2004 是四通道线性中继器／重驱动器（Linear Repeater / Redriver），设计用于支持最高 20 Gbps 的 DisplayPort 2.1，以及最高 12 Gbps 的交流耦合（AC-coupled）HDMI 2.1 信号源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TDP2004_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/misc/ti_tdp2004/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/ti_tdp2004/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TI_TDP2004_INIT_PRIORITY"></a>

## 123.50 `CONFIG_TI_TDP2004_INIT_PRIORITY`

**提示（Prompt）**：TI TDP2004 初始化优先级

**说明（Help）**

TI TDP2004 重驱动器的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TI_TDP2004
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/misc/ti_tdp2004/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/ti_tdp2004/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → TDP2004 四通道 20 Gbps DisplayPort 2.1 和 12 Gbps HDMI 2.1 线性重驱动器（Linear Redriver）

**配置项引用（Symbol References）**：[`CONFIG_TI_TDP2004`](P123_drivers_misc_配置项参考.md#CONFIG_TI_TDP2004)、[`CONFIG_I2C_INIT_PRIORITY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_TMC6460"></a>

## 123.51 `CONFIG_TMC6460`

**提示（Prompt）**：Trinamic TMC6460 磁场定向控制（FOC）电机控制器

**说明（Help）**

启用 Analog Devices / Trinamic TMC6460 磁场定向控制（Field Oriented Control，FOC）电机控制器支持。TMC6460 使用 48 位（6 字节）数据报（Datagram），具有 16 位地址空间，同时支持 SPI 和 UART 接口。它提供设备特定的寄存器访问与运动控制（Motion Control）API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_TMC6460_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/misc/tmc6460/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/tmc6460/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers）

<a id="CONFIG_TMC6460_INIT_PRIORITY"></a>

## 123.52 `CONFIG_TMC6460_INIT_PRIORITY`

**提示（Prompt）**：TMC6460 初始化优先级

**说明（Help）**

TMC6460 设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TMC6460
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/misc/tmc6460/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/tmc6460/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Trinamic TMC6460 磁场定向控制（FOC）电机控制器

**配置项引用（Symbol References）**：[`CONFIG_TMC6460`](P123_drivers_misc_配置项参考.md#CONFIG_TMC6460)。

<a id="CONFIG_TMC6460_SPI"></a>

## 123.53 `CONFIG_TMC6460_SPI`

**提示（Prompt）**：TMC6460 SPI 总线支持

**说明（Help）**

启用 TMC6460 的 SPI 总线支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TMC6460
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/misc/tmc6460/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/tmc6460/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Trinamic TMC6460 磁场定向控制（FOC）电机控制器

**配置项引用（Symbol References）**：[`CONFIG_TMC6460`](P123_drivers_misc_配置项参考.md#CONFIG_TMC6460)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_TMC6460_UART"></a>

## 123.54 `CONFIG_TMC6460_UART`

**提示（Prompt）**：TMC6460 UART 总线支持

**说明（Help）**

启用 TMC6460 的 UART 总线支持。TMC6460 UART 协议使用独特的 CRC8 多项式（原文写作 `0x100011011 reflected`，即反射形式），并支持 RTMI 流式传输。译注：多项式的前缀及数字按原文保留，未自行更改进制表示。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TMC6460
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/misc/tmc6460/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/tmc6460/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Trinamic TMC6460 磁场定向控制（FOC）电机控制器

**配置项引用（Symbol References）**：[`CONFIG_TMC6460`](P123_drivers_misc_配置项参考.md#CONFIG_TMC6460)、[`CONFIG_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL)。

<!-- kconfig-navigation -->

[上一章](P122_drivers_mipi_dsi_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P124_drivers_mm_配置项参考.md)
