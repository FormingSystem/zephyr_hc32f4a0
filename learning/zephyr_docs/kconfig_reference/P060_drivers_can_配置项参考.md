---
id: learning.zephyr-docs.kconfig-reference.page-60
title: "`drivers/can`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第60章\_`drivers/can`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/can` 的 87 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CAN"></a>

## 60.1 `CONFIG_CAN`

**提示（Prompt）**：控制器局域网驱动（Controller Area Network，CAN）

**说明（Help）**

启用控制器局域网（CAN）驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/can/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_CAN_ACCEPT_RTR"></a>

## 60.2 `CONFIG_CAN_ACCEPT_RTR`

**提示（Prompt）**：接受远程传输请求帧（Remote Transmission Request，RTR）

**说明（Help）**

接受与 CAN 接收过滤器（RX Filter）匹配的传入远程传输请求（RTR）帧。如果未启用，则驱动层拒绝所有传入 RTR 帧。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN
```

**定义位置（Location）**：[`drivers/can/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_BFLB_BL61X"></a>

## 60.3 `CONFIG_CAN_BFLB_BL61X`

**提示（Prompt）**：博流 BL61x CAN 驱动（Bouffalo Lab CAN Driver）

**说明（Help）**

启用博流（Bouffalo Lab）BL61x ISO11898 传统 CAN 2.0 控制器支持，该控制器兼容 SJA1000。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BL61X_CAN_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAN_SJA1000
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_SJA1000`](P060_drivers_can_配置项参考.md#CONFIG_CAN_SJA1000)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_DEFAULT_BITRATE"></a>

## 60.4 `CONFIG_CAN_DEFAULT_BITRATE`

**提示（Prompt）**：默认 CAN 比特率（Default CAN Bitrate）

**说明（Help）**

默认初始 CAN 比特率（Bitrate），单位为 bit/s。可以通过设备树（Devicetree）的 `bitrate` 属性为各 CAN 控制器分别覆盖此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN
```

**默认值（Defaults）**

```text
125000
```

**定义位置（Location）**：[`drivers/can/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_DEFAULT_BITRATE_DATA"></a>

## 60.5 `CONFIG_CAN_DEFAULT_BITRATE_DATA`

**提示（Prompt）**：默认 CAN 数据阶段比特率（Data Phase Bitrate）

**说明（Help）**

默认初始 CAN 数据阶段比特率（Data Phase Bitrate），单位为 bit/s。可以通过设备树（Devicetree）的 `bitrate-data` 属性为各 CAN 控制器分别覆盖此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_FD_MODE && CONFIG_CAN
```

**默认值（Defaults）**

```text
1000000
```

**定义位置（Location）**：[`drivers/can/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN_FD_MODE`](P060_drivers_can_配置项参考.md#CONFIG_CAN_FD_MODE)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_ESP32_TWAI"></a>

## 60.6 `CONFIG_CAN_ESP32_TWAI`

**提示（Prompt）**：乐鑫 TWAI CAN 驱动（Espressif Driver）

**说明（Help）**

启用乐鑫（Espressif）双线汽车接口（Two-Wire Automotive Interface，TWAI）CAN 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_TWAI_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAN_SJA1000
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.esp32:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.esp32#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_SJA1000`](P060_drivers_can_配置项参考.md#CONFIG_CAN_SJA1000)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_ESP32_TWAIFD"></a>

## 60.7 `CONFIG_CAN_ESP32_TWAIFD`

**提示（Prompt）**：乐鑫 TWAI-FD CAN 驱动（Espressif Driver）

**说明（Help）**

启用乐鑫（Espressif）TWAI-FD 控制器驱动，即具备 CAN FD 能力的双线汽车接口（Two-Wire Automotive Interface）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_TWAIFD_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.esp32:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.esp32#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_ESP32_TWAIFD_MAX_FILTERS"></a>

## 60.8 `CONFIG_CAN_ESP32_TWAIFD_MAX_FILTERS`

**提示（Prompt）**：每个 TWAI-FD 控制器的最大接收过滤器数量（RX Filters）

**说明（Help）**

可以通过 `can_add_rx_filter()` 在一个 TWAI-FD 控制器实例上同时安装的最大接收过滤器（RX Filter）数量。过滤在软件中完成，每个槽位占用几个字（Word）的 RAM；如果需要的过滤器较少，可以减小此值以节省 RAM。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_ESP32_TWAIFD && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/can/Kconfig.esp32:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.esp32#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 乐鑫 TWAI-FD CAN 驱动（Espressif Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_ESP32_TWAIFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_ESP32_TWAIFD)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_FAKE"></a>

## 60.9 `CONFIG_CAN_FAKE`

**提示（Prompt）**：模拟 CAN 驱动（Fake CAN Driver）

**说明（Help）**

启用基于伪函数框架（FFF）的模拟 CAN 驱动（Fake CAN Driver）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_FAKE_CAN_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/can/Kconfig.fake:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.fake#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_FD_MODE"></a>

## 60.10 `CONFIG_CAN_FD_MODE`

**提示（Prompt）**：CAN 灵活数据速率支持（CAN FD Support）

**说明（Help）**

启用 CAN 灵活数据速率（CAN FD）支持。并非所有 CAN 控制器都支持 CAN FD。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN
```

**定义位置（Location）**：[`drivers/can/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_INFINEON_MCAN"></a>

## 60.11 `CONFIG_CAN_INFINEON_MCAN`

**提示（Prompt）**：英飞凌 MCAN 驱动（Infineon Driver）

**说明（Help）**

启用英飞凌（Infineon）CAN 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_CAN_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAN_MCAN
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.infineon:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.infineon#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_INIT_PRIORITY"></a>

## 60.12 `CONFIG_CAN_INIT_PRIORITY`

**提示（Prompt）**：CAN 驱动初始化优先级（Init Priority）

**说明（Help）**

CAN 驱动设备的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/can/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_KVASER_PCI"></a>

## 60.13 `CONFIG_CAN_KVASER_PCI`

**提示（Prompt）**：Kvaser PCIcan 驱动（Driver）

**说明（Help）**

启用 Kvaser PCIcan 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_KVASER_PCICAN_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PCIE
CONFIG_CAN_SJA1000
```

**定义位置（Location）**：[`drivers/can/Kconfig.kvaser:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.kvaser#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_PCIE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE)、[`CONFIG_CAN_SJA1000`](P060_drivers_can_配置项参考.md#CONFIG_CAN_SJA1000)。

<a id="CONFIG_CAN_LOOPBACK"></a>

## 60.14 `CONFIG_CAN_LOOPBACK`

**提示（Prompt）**：仿真 CAN 回环驱动（Emulated CAN Loopback Driver）

**说明（Help）**

这是一个只能回环消息（Loopback Messages）的仿真驱动（Emulated Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_CAN_LOOPBACK_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/can/Kconfig.loopback:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.loopback#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_LOOPBACK_MAX_FILTERS"></a>

## 60.15 `CONFIG_CAN_LOOPBACK_MAX_FILTERS`

**提示（Prompt）**：最大并发活动过滤器数量（Concurrent Active Filters）

**说明（Help）**

定义过滤器数组（Filter Array）的大小，必须至少容纳并发读取的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_LOOPBACK && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`drivers/can/Kconfig.loopback:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.loopback#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 仿真 CAN 回环驱动（Emulated CAN Loopback Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_LOOPBACK`](P060_drivers_can_配置项参考.md#CONFIG_CAN_LOOPBACK)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_LOOPBACK_TX_MSGQ_SIZE"></a>

## 60.16 `CONFIG_CAN_LOOPBACK_TX_MSGQ_SIZE`

**提示（Prompt）**：发送消息队列大小（TX Message Queue Size）

**说明（Help）**

可以缓冲的发送帧（TX Frame）数量。发送函数将帧放入此队列，发送线程从消息队列（Message Queue）取出消息；如果过滤器匹配，则调用对应的接收方。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_LOOPBACK && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/can/Kconfig.loopback:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.loopback#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 仿真 CAN 回环驱动（Emulated CAN Loopback Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_LOOPBACK`](P060_drivers_can_配置项参考.md#CONFIG_CAN_LOOPBACK)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_LOOPBACK_TX_THREAD_PRIORITY"></a>

## 60.17 `CONFIG_CAN_LOOPBACK_TX_THREAD_PRIORITY`

**提示（Prompt）**：发送线程优先级（TX Thread Priority）

**说明（Help）**

发送线程（TX Thread）的优先级。过滤器匹配时，发送线程调用接收方的回调（Callback）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_LOOPBACK && CONFIG_CAN
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/can/Kconfig.loopback:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.loopback#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 仿真 CAN 回环驱动（Emulated CAN Loopback Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_LOOPBACK`](P060_drivers_can_配置项参考.md#CONFIG_CAN_LOOPBACK)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_LOOPBACK_TX_THREAD_STACK_SIZE"></a>

## 60.18 `CONFIG_CAN_LOOPBACK_TX_THREAD_STACK_SIZE`

**提示（Prompt）**：发送线程栈大小（TX Thread Stack Size）

**说明（Help）**

发送线程（TX Thread）的栈大小。过滤器匹配时，发送线程调用接收方的回调（Callback）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_LOOPBACK && CONFIG_CAN
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/can/Kconfig.loopback:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.loopback#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 仿真 CAN 回环驱动（Emulated CAN Loopback Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_LOOPBACK`](P060_drivers_can_配置项参考.md#CONFIG_CAN_LOOPBACK)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MANUAL_RECOVERY_MODE"></a>

## 60.19 `CONFIG_CAN_MANUAL_RECOVERY_MODE`

**提示（Prompt）**：手动总线关闭状态恢复支持（Manual Bus-Off Recovery）

**说明（Help）**

启用从总线关闭状态（Bus-Off State）手动、而非自动恢复的支持。并非所有 CAN 控制器都支持手动恢复模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN
```

**定义位置（Location）**：[`drivers/can/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MAX32"></a>

## 60.20 `CONFIG_CAN_MAX32`

**提示（Prompt）**：ADI MAX32 CAN 驱动（Driver）

**说明（Help）**

启用 ADI MAX32 CAN 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_CAN_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_MAX32_MAX_FILTERS"></a>

## 60.21 `CONFIG_CAN_MAX32_MAX_FILTERS`

**提示（Prompt）**：最大并发活动过滤器数量（Concurrent Active Filters）

**说明（Help）**

`can_add_rx_callback()` API 调用支持的最大过滤器（Filter）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_MAX32 && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/can/Kconfig.max32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.max32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → ADI MAX32 CAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_MAX32`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MAX32)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MCAN"></a>

## 60.22 `CONFIG_CAN_MCAN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Bosch M_CAN CAN IP 模块驱动后端（Driver Backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN
```

**被选择（Selected by）**

```text
CONFIG_CAN_INFINEON_MCAN
CONFIG_CAN_MSPM0_CANFD
CONFIG_CAN_NRF
CONFIG_CAN_NUMAKER
CONFIG_CAN_NXP_LPC_MCAN
CONFIG_CAN_SAM
CONFIG_CAN_SAM0
CONFIG_CAN_STM32_FDCAN
CONFIG_CAN_STM32H7_FDCAN
CONFIG_CAN_TCAN4X5X
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcan:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcan#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_INFINEON_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_INFINEON_MCAN)、[`CONFIG_CAN_MSPM0_CANFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MSPM0_CANFD)、[`CONFIG_CAN_NRF`](P060_drivers_can_配置项参考.md#CONFIG_CAN_NRF)、[`CONFIG_CAN_NUMAKER`](P060_drivers_can_配置项参考.md#CONFIG_CAN_NUMAKER)、[`CONFIG_CAN_NXP_LPC_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_NXP_LPC_MCAN)、[`CONFIG_CAN_SAM`](P060_drivers_can_配置项参考.md#CONFIG_CAN_SAM)、[`CONFIG_CAN_SAM0`](P060_drivers_can_配置项参考.md#CONFIG_CAN_SAM0)、[`CONFIG_CAN_STM32_FDCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_STM32_FDCAN)、[`CONFIG_CAN_STM32H7_FDCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_STM32H7_FDCAN)、[`CONFIG_CAN_TCAN4X5X`](P060_drivers_can_配置项参考.md#CONFIG_CAN_TCAN4X5X)。

<a id="CONFIG_CAN_MCAN_FIXED_MRAM_LAYOUT"></a>

## 60.23 `CONFIG_CAN_MCAN_FIXED_MRAM_LAYOUT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

无论是否启用 `CONFIG_CAN_FD_MODE`，接收／发送缓冲区元素（RX/TX Buffer Element）始终使用 64 字节深度。对于使用固定消息 RAM 布局（Fixed Message RAM Layout）、没有 `TXESC` / `RXESC` 寄存器的 Bosch M_CAN IP 实例，其驱动必须选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN
```

**被选择（Selected by）**

```text
CONFIG_CAN_STM32_FDCAN
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcan:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcan#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_STM32_FDCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_STM32_FDCAN)。

<a id="CONFIG_CAN_MCP2515"></a>

## 60.24 `CONFIG_CAN_MCP2515`

**提示（Prompt）**：MCP2515 CAN 驱动（Driver）

**说明（Help）**

启用 MCP2515 CAN 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MCP2515_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcp2515:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcp2515#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_CAN_MCP2515_INT_THREAD_PRIO"></a>

## 60.25 `CONFIG_CAN_MCP2515_INT_THREAD_PRIO`

**提示（Prompt）**：中断处理程序优先级（Interrupt Handler Priority）

**说明（Help）**

用于处理中断和传入数据包的内部线程（Internal Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_MCP2515 && CONFIG_CAN
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcp2515:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcp2515#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → MCP2515 CAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_MCP2515`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCP2515)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MCP2515_INT_THREAD_STACK_SIZE"></a>

## 60.26 `CONFIG_CAN_MCP2515_INT_THREAD_STACK_SIZE`

**提示（Prompt）**：中断处理程序栈大小（Interrupt Handler Stack Size）

**说明（Help）**

用于处理中断和传入数据包的内部线程（Internal Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_MCP2515 && CONFIG_CAN
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcp2515:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcp2515#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → MCP2515 CAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_MCP2515`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCP2515)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MCP2515_MAX_FILTERS"></a>

## 60.27 `CONFIG_CAN_MCP2515_MAX_FILTERS`

**提示（Prompt）**：最大并发活动过滤器数量（Concurrent Active Filters）

**说明（Help）**

定义回调／消息队列指针（Callback / msgq Pointer）数组大小，必须至少容纳并发读取的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_MCP2515 && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcp2515:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcp2515#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → MCP2515 CAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_MCP2515`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCP2515)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MCP251XFD"></a>

## 60.28 `CONFIG_CAN_MCP251XFD`

**提示（Prompt）**：MCP25XXFD CAN 驱动（Driver）

**说明（Help）**

启用 MCP25XXFD CAN 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MCP251XFD_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcp251xfd:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcp251xfd#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_CAN_MCP251XFD_INT_THREAD_PRIO"></a>

## 60.29 `CONFIG_CAN_MCP251XFD_INT_THREAD_PRIO`

**提示（Prompt）**：中断处理程序优先级（Interrupt Handler Priority）

**说明（Help）**

中断处理线程（Interrupt Handler Thread）的优先级。原文说明数字越大，优先级越高。该线程是协作式（Cooperative）线程，在主动让出执行权之前，不会被另一个线程打断。

译注：这里保留上游对数值方向的说明；实际使用应对照驱动的优先级换算，不应将此句视为所有 Zephyr 线程优先级的通用规则。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_MCP251XFD && CONFIG_CAN
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcp251xfd:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcp251xfd#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → MCP25XXFD CAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_MCP251XFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCP251XFD)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MCP251XFD_INT_THREAD_STACK_SIZE"></a>

## 60.30 `CONFIG_CAN_MCP251XFD_INT_THREAD_STACK_SIZE`

**提示（Prompt）**：中断处理程序栈大小（Interrupt Handler Stack Size）

**说明（Help）**

用于处理中断和传入数据包的内部线程（Internal Thread）使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_MCP251XFD && CONFIG_CAN
```

**默认值（Defaults）**

```text
768
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcp251xfd:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcp251xfd#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → MCP25XXFD CAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_MCP251XFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCP251XFD)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MCP251XFD_MAX_FILTERS"></a>

## 60.31 `CONFIG_CAN_MCP251XFD_MAX_FILTERS`

**提示（Prompt）**：最大并发活动过滤器数量（Concurrent Active Filters）

**说明（Help）**

`can_add_rx_callback()` API 调用支持的最大过滤器（Filter）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_MCP251XFD && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcp251xfd:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcp251xfd#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → MCP25XXFD CAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_MCP251XFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCP251XFD)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MCP251XFD_MAX_TX_QUEUE"></a>

## 60.32 `CONFIG_CAN_MCP251XFD_MAX_TX_QUEUE`

**提示（Prompt）**：最大排队消息数量（Maximum Queued Messages）

**说明（Help）**

定义发送回调指针（Transmit Callback Pointer）和信号量（Semaphore）数组的大小，以及发送队列（TX Queue）中的消息数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_MCP251XFD && CONFIG_CAN
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcp251xfd:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcp251xfd#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → MCP25XXFD CAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_MCP251XFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCP251XFD)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MCP251XFD_READ_CRC_RETRIES"></a>

## 60.33 `CONFIG_CAN_MCP251XFD_READ_CRC_RETRIES`

**提示（Prompt）**：SFR 寄存器读取重试次数（SFR Read Retries）

**说明（Help）**

读取特殊功能寄存器（SFR）时，如果循环冗余校验（CRC）失败，允许重试的次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_MCP251XFD && CONFIG_CAN
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcp251xfd:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcp251xfd#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → MCP25XXFD CAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_MCP251XFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCP251XFD)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MCP251XFD_RX_FIFO_ITEMS"></a>

## 60.34 `CONFIG_CAN_MCP251XFD_RX_FIFO_ITEMS`

**提示（Prompt）**：接收 FIFO 中的 CAN 消息数量（RX FIFO Messages）

**说明（Help）**

定义接收先进先出队列（RX FIFO）中的 CAN 消息数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_MCP251XFD && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcp251xfd:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcp251xfd#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → MCP25XXFD CAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_MCP251XFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCP251XFD)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MCUX_FLEXCAN"></a>

## 60.35 `CONFIG_CAN_MCUX_FLEXCAN`

**提示（Prompt）**：恩智浦 FlexCAN 驱动（NXP Driver）

**说明（Help）**

启用恩智浦（NXP）FlexCAN 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FLEXCAN_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcux:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcux#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_MCUX_FLEXCAN_FD"></a>

## 60.36 `CONFIG_CAN_MCUX_FLEXCAN_FD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用具备 CAN 灵活数据速率（CAN FD）能力的恩智浦（NXP）FlexCAN 器件支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FLEXCAN_FD_ENABLED && CONFIG_CAN_FD_MODE && CONFIG_CAN_MCUX_FLEXCAN && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcux:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcux#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 恩智浦 FlexCAN 驱动（NXP Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_FD_MODE`](P060_drivers_can_配置项参考.md#CONFIG_CAN_FD_MODE)、[`CONFIG_CAN_MCUX_FLEXCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCUX_FLEXCAN)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MCUX_FLEXCAN_MAX_FILTERS"></a>

## 60.37 `CONFIG_CAN_MCUX_FLEXCAN_MAX_FILTERS`

**提示（Prompt）**：最大并发活动接收过滤器数量（Concurrent Active RX Filters）

**说明（Help）**

默认的最大并发活动接收过滤器（RX Filter）数量。最大值取决于每个 FlexCAN 实例的可用消息缓冲区（Message Buffer）数量。可以通过设备树（Devicetree）的 `max-filters` 属性为每个实例分别覆盖默认值。CAN FD 模式使用更大的消息缓冲区，因此可用过滤器会更少。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_MCUX_FLEXCAN && CONFIG_CAN
```

**默认值（Defaults）**

```text
5 if CONFIG_CAN_MCUX_FLEXCAN_FD
13
```

**取值范围（Ranges）**

```text
[0, 128]
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcux:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcux#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 恩智浦 FlexCAN 驱动（NXP Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_MCUX_FLEXCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCUX_FLEXCAN)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_MCUX_FLEXCAN_FD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCUX_FLEXCAN_FD)。

<a id="CONFIG_CAN_MCUX_FLEXCAN_WAIT_TIMEOUT"></a>

## 60.38 `CONFIG_CAN_MCUX_FLEXCAN_WAIT_TIMEOUT`

**提示（Prompt）**：等待循环的最大迭代次数（Wait Loop Iterations）

**说明（Help）**

MCUX FlexCAN 硬件抽象层（HAL）进入／退出冻结模式（Freeze Mode）时，等待循环允许的最大迭代次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_MCUX_FLEXCAN && CONFIG_CAN
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`drivers/can/Kconfig.mcux:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mcux#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 恩智浦 FlexCAN 驱动（NXP Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_MCUX_FLEXCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCUX_FLEXCAN)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_MSPM0_CANFD"></a>

## 60.39 `CONFIG_CAN_MSPM0_CANFD`

**提示（Prompt）**：MSPM0 CAN FD 驱动（Driver）

**说明（Help）**

启用 TI MSPM0 系列的 CAN 灵活数据速率（CAN FD）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_CANFD_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAN_MCAN
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.mspm0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.mspm0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_NATIVE_LINUX"></a>

## 60.40 `CONFIG_CAN_NATIVE_LINUX`

**提示（Prompt）**：原生 Linux SocketCAN 驱动（Native Linux Driver）

**说明（Help）**

启用原生 Linux SocketCAN 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_LINUX_CAN_ENABLED && CONFIG_ARCH_POSIX && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/can/Kconfig.native_linux:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.native_linux#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_NATIVE_LINUX_MAX_FILTERS"></a>

## 60.41 `CONFIG_CAN_NATIVE_LINUX_MAX_FILTERS`

**提示（Prompt）**：最大并发活动过滤器数量（Concurrent Active Filters）

**说明（Help）**

定义回调／消息队列指针（Callback / msgq Pointer）数组大小，必须至少容纳并发读取的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_NATIVE_LINUX && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/can/Kconfig.native_linux:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.native_linux#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 原生 Linux SocketCAN 驱动（Native Linux Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_NATIVE_LINUX`](P060_drivers_can_配置项参考.md#CONFIG_CAN_NATIVE_LINUX)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_NATIVE_LINUX_RX_THREAD_PRIORITY"></a>

## 60.42 `CONFIG_CAN_NATIVE_LINUX_RX_THREAD_PRIORITY`

**提示（Prompt）**：内部接收线程优先级（Internal RX Thread Priority）

**说明（Help）**

用于处理传入数据包的内部线程（Internal Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_NATIVE_LINUX && CONFIG_CAN
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/can/Kconfig.native_linux:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.native_linux#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 原生 Linux SocketCAN 驱动（Native Linux Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_NATIVE_LINUX`](P060_drivers_can_配置项参考.md#CONFIG_CAN_NATIVE_LINUX)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_NRF"></a>

## 60.43 `CONFIG_CAN_NRF`

**提示（Prompt）**：nRF CAN 驱动（Driver）

**说明（Help）**

nRF CAN 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_CAN_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAN_MCAN
CONFIG_CLOCK_CONTROL
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.nrf:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.nrf#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCAN)、[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_NUMAKER"></a>

## 60.44 `CONFIG_CAN_NUMAKER`

**提示（Prompt）**：新唐 NuMaker CAN FD 驱动（Nuvoton Driver）

**说明（Help）**

启用使用 Bosch M_CAN 的新唐（Nuvoton）NuMaker CAN FD 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_CANFD_ENABLED && (CONFIG_SOC_SERIES_M46X || CONFIG_SOC_SERIES_M2L31X || CONFIG_SOC_SERIES_M55M1X || CONFIG_SOC_SERIES_M333X || CONFIG_SOC_SERIES_M335X) && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAN_MCAN
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_M46X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M46X)、[`CONFIG_SOC_SERIES_M2L31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M2L31X)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_SERIES_M333X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M333X)、[`CONFIG_SOC_SERIES_M335X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M335X)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_NXP_LPC_MCAN"></a>

## 60.45 `CONFIG_CAN_NXP_LPC_MCAN`

**提示（Prompt）**：恩智浦 LPC 系列 MCAN 驱动（NXP Driver）

**说明（Help）**

启用恩智浦（NXP）LPC 系列 MCAN 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_MCAN_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAN_MCAN
CONFIG_PINCTRL
CONFIG_RESET
```

**定义位置（Location）**：[`drivers/can/Kconfig.nxp_lpc_mcan:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.nxp_lpc_mcan#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)。

<a id="CONFIG_CAN_NXP_S32_CANXL"></a>

## 60.46 `CONFIG_CAN_NXP_S32_CANXL`

**提示（Prompt）**：恩智浦 S32 CANXL 驱动（NXP Driver）

**说明（Help）**

启用恩智浦（NXP）S32 CANXL 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_CANXL_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.nxp_s32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.nxp_s32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_NXP_S32_MAX_RX"></a>

## 60.47 `CONFIG_CAN_NXP_S32_MAX_RX`

**提示（Prompt）**：最大接收描述符数量（RX Descriptors）

**说明（Help）**

接收描述符（RX Descriptor）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_NXP_S32_CANXL && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 32] if CONFIG_CAN_NXP_S32_RX_FIFO
[1, 128] if !CONFIG_CAN_NXP_S32_RX_FIFO
```

**定义位置（Location）**：[`drivers/can/Kconfig.nxp_s32:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.nxp_s32#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 恩智浦 S32 CANXL 驱动（NXP Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_NXP_S32_CANXL`](P060_drivers_can_配置项参考.md#CONFIG_CAN_NXP_S32_CANXL)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_NXP_S32_RX_FIFO`](P060_drivers_can_配置项参考.md#CONFIG_CAN_NXP_S32_RX_FIFO)。

<a id="CONFIG_CAN_NXP_S32_MAX_TX"></a>

## 60.48 `CONFIG_CAN_NXP_S32_MAX_TX`

**提示（Prompt）**：最大发送描述符数量（TX Descriptors）

**说明（Help）**

发送描述符（TX Descriptor）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_NXP_S32_CANXL && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 128]
```

**定义位置（Location）**：[`drivers/can/Kconfig.nxp_s32:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.nxp_s32#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 恩智浦 S32 CANXL 驱动（NXP Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_NXP_S32_CANXL`](P060_drivers_can_配置项参考.md#CONFIG_CAN_NXP_S32_CANXL)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_NXP_S32_RX_FIFO"></a>

## 60.49 `CONFIG_CAN_NXP_S32_RX_FIFO`

**提示（Prompt）**：NXP S32 CANXL 使用接收 FIFO（RX FIFO）

**说明（Help）**

启用后，恩智浦（NXP）S32 CANXL 使用接收先进先出队列（RX FIFO）；否则使用接收消息描述符（RX Message Descriptor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_S32ZE && CONFIG_CAN_NXP_S32_CANXL && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/can/Kconfig.nxp_s32:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.nxp_s32#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 恩智浦 S32 CANXL 驱动（NXP Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)、[`CONFIG_CAN_NXP_S32_CANXL`](P060_drivers_can_配置项参考.md#CONFIG_CAN_NXP_S32_CANXL)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32ZE`。

<a id="CONFIG_CAN_QEMU_IFACE_NAME"></a>

## 60.50 `CONFIG_CAN_QEMU_IFACE_NAME`

**提示（Prompt）**：QEMU 的 SocketCAN 接口名称（Interface Name）

**说明（Help）**

QEMU 使用的 SocketCAN 接口名称。设置后，此值作为 `if` 参数传给 QEMU 命令行选项 `-object can-host-socketcan`。必须在启动 QEMU 之前配置好 CAN 接口。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_QEMU_TARGET && CONFIG_CAN
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`drivers/can/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_RCAR"></a>

## 60.51 `CONFIG_CAN_RCAR`

**提示（Prompt）**：瑞萨 R-Car CAN 驱动（Renesas Driver）

**说明（Help）**

启用瑞萨（Renesas）R-Car CAN 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RCAR_CAN_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.rcar:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.rcar#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_RCAR_MAX_FILTERS"></a>

## 60.52 `CONFIG_CAN_RCAR_MAX_FILTERS`

**提示（Prompt）**：最大并发活动过滤器数量（Concurrent Active Filters）

**说明（Help）**

定义回调／消息队列指针（Callback / msgq Pointer）数组大小，必须至少容纳并发读取的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_RCAR && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/can/Kconfig.rcar:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.rcar#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 瑞萨 R-Car CAN 驱动（Renesas Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_RCAR`](P060_drivers_can_配置项参考.md#CONFIG_CAN_RCAR)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_RCAR_RSCANFD"></a>

## 60.53 `CONFIG_CAN_RCAR_RSCANFD`

**提示（Prompt）**：瑞萨 R-Car RS-CANFD 驱动（Renesas Driver）

**说明（Help）**

为第 4 代（Gen 4）及更新平台上的 RS-CANFD 控制器，启用瑞萨（Renesas）R-Car CAN 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RCAR_RSCANFD_GLOBAL_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.rcar:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.rcar#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_RCAR_RSCANFD_MAX_FILTERS"></a>

## 60.54 `CONFIG_CAN_RCAR_RSCANFD_MAX_FILTERS`

**提示（Prompt）**：最大并发活动接收过滤器数量（Concurrent Active Reception Filters）

**说明（Help）**

定义回调／消息队列指针（Callback / msgq Pointer）数组大小，必须至少容纳并发读取的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_RCAR_RSCANFD && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/can/Kconfig.rcar:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.rcar#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 瑞萨 R-Car RS-CANFD 驱动（Renesas Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_RCAR_RSCANFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_RCAR_RSCANFD)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_REALTEK_BEE"></a>

## 60.55 `CONFIG_CAN_REALTEK_BEE`

**提示（Prompt）**：Realtek Bee 控制器局域网（CAN）驱动

**说明（Help）**

启用瑞昱（Realtek）Bee 片上系统（SoC）的 CAN 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_CAN_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_CAN
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.realtek_bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.realtek_bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_HAL_REALTEK_BEE_CAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_CAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_CAN`。

<a id="CONFIG_CAN_REALTEK_BEE_RX_MSG_BUF_NUM"></a>

## 60.56 `CONFIG_CAN_REALTEK_BEE_RX_MSG_BUF_NUM`

**提示（Prompt）**：用于接收的消息缓冲区数量（RX Message Buffers）

**说明（Help）**

定义应用用于接收（RX）的消息缓冲区（Message Buffer）数量。发送与接收共用总计 16 个消息缓冲区。每个接收消息缓冲区可过滤一个标准标识符（Standard ID）或扩展标识符（Extended ID）。发送与接收的总数量上限由下式确定：

```text
CAN_REALTEK_BEE_TX_MSG_BUF_NUM + CAN_REALTEK_BEE_RX_MSG_BUF_NUM <= 16
```

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_REALTEK_BEE && CONFIG_CAN
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`drivers/can/Kconfig.realtek_bee:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.realtek_bee#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → Realtek Bee 控制器局域网（CAN）驱动

**配置项引用（Symbol References）**：[`CONFIG_CAN_REALTEK_BEE`](P060_drivers_can_配置项参考.md#CONFIG_CAN_REALTEK_BEE)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_REALTEK_BEE_TX_MSG_BUF_NUM"></a>

## 60.57 `CONFIG_CAN_REALTEK_BEE_TX_MSG_BUF_NUM`

**提示（Prompt）**：用于发送的消息缓冲区数量（TX Message Buffers）

**说明（Help）**

定义应用用于发送（TX）的消息缓冲区（Message Buffer）数量。发送与接收共用总计 16 个消息缓冲区。每个接收消息缓冲区可过滤一个标准标识符（Standard ID）或扩展标识符（Extended ID）。发送与接收的总数量上限由下式确定：

```text
CAN_REALTEK_BEE_TX_MSG_BUF_NUM + CAN_REALTEK_BEE_RX_MSG_BUF_NUM <= 16
```

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_REALTEK_BEE && CONFIG_CAN
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`drivers/can/Kconfig.realtek_bee:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.realtek_bee#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → Realtek Bee 控制器局域网（CAN）驱动

**配置项引用（Symbol References）**：[`CONFIG_CAN_REALTEK_BEE`](P060_drivers_can_配置项参考.md#CONFIG_CAN_REALTEK_BEE)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_RENESAS_RA_CANFD"></a>

## 60.58 `CONFIG_CAN_RENESAS_RA_CANFD`

**提示（Prompt）**：瑞萨 RA CAN FD 驱动（Renesas Driver）

**说明（Help）**

启用瑞萨（Renesas）RA CAN FD 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_CANFD_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_CANFD
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_USE_RA_FSP_CANFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_CANFD)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_RENESAS_RZ_CANFD"></a>

## 60.59 `CONFIG_CAN_RENESAS_RZ_CANFD`

**提示（Prompt）**：瑞萨 RZ CAN FD 驱动（Renesas Driver）

**说明（Help）**

启用瑞萨（Renesas）RZ CAN FD 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_CANFD_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_CANFD
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/can/Kconfig.renesas_rz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.renesas_rz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_USE_RZ_FSP_CANFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_CANFD)、[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CAN_RX_TIMESTAMP"></a>

## 60.60 `CONFIG_CAN_RX_TIMESTAMP`

**提示（Prompt）**：接收时间戳（Receiving Timestamps）

**说明（Help）**

启用 CAN 自由运行定时器（Free-Running Timer）的时间戳（Timestamp）值。该值在控制器初始化时开始，每经过一个位时间（Bit Time）递增一次。并非所有 CAN 控制器都支持时间戳。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN
```

**定义位置（Location）**：[`drivers/can/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_SAM"></a>

## 60.61 `CONFIG_CAN_SAM`

**提示（Prompt）**：Atmel SAM CAN 驱动（Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_CAN_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAN_MCAN
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.sam:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.sam#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_SAM0"></a>

## 60.62 `CONFIG_CAN_SAM0`

**提示（Prompt）**：Atmel SAM0 CAN 驱动（Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_CAN_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAN_MCAN
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.sam0:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.sam0#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_SAMPLE_POINT_MARGIN"></a>

## 60.63 `CONFIG_CAN_SAMPLE_POINT_MARGIN`

**提示（Prompt）**：最大允许采样点位置偏差（Sample Point Location Deviation）

**说明（Help）**

采样点位置（Sample Point Location）允许的最大偏差，以千分之一（Permille）计。值为 50 表示允许正负 5 个百分点的误差。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`drivers/can/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_SHELL"></a>

## 60.64 `CONFIG_CAN_SHELL`

**提示（Prompt）**：CAN 命令行（CAN Shell）

**说明（Help）**

启用用于测试的 CAN 命令行（Shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_CAN
```

**主动选择（Selects）**

```text
CONFIG_POLL
```

**定义位置（Location）**：[`drivers/can/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)。

<a id="CONFIG_CAN_SHELL_RX_QUEUE_SIZE"></a>

## 60.65 `CONFIG_CAN_SHELL_RX_QUEUE_SIZE`

**提示（Prompt）**：CAN 命令行接收队列大小（Receive Queue Size）

**说明（Help）**

CAN 命令行（Shell）接收队列中的最大 CAN 帧数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_SHELL && CONFIG_CAN
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`drivers/can/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → CAN 命令行（CAN Shell）

**配置项引用（Symbol References）**：[`CONFIG_CAN_SHELL`](P060_drivers_can_配置项参考.md#CONFIG_CAN_SHELL)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_SHELL_SCRIPTING_FRIENDLY"></a>

## 60.66 `CONFIG_CAN_SHELL_SCRIPTING_FRIENDLY`

**提示（Prompt）**：生成便于脚本处理的输出（Scripting-Friendly Output）

**说明（Help）**

让 CAN 命令行（Shell）输出便于脚本处理、可由机器读取（Machine-Readable）的内容。启用后，打印某些输出时绕过 Shell，以确保内容不会与命令行提示符（Shell Prompt）交错。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_SHELL && CONFIG_CAN
```

**定义位置（Location）**：[`drivers/can/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → CAN 命令行（CAN Shell）

**配置项引用（Symbol References）**：[`CONFIG_CAN_SHELL`](P060_drivers_can_配置项参考.md#CONFIG_CAN_SHELL)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_SHELL_TX_QUEUE_SIZE"></a>

## 60.67 `CONFIG_CAN_SHELL_TX_QUEUE_SIZE`

**提示（Prompt）**：CAN 命令行发送队列大小（Transmit Queue Size）

**说明（Help）**

CAN 命令行（Shell）发送队列中的最大事件（Event）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_SHELL && CONFIG_CAN
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`drivers/can/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → CAN 命令行（CAN Shell）

**配置项引用（Symbol References）**：[`CONFIG_CAN_SHELL`](P060_drivers_can_配置项参考.md#CONFIG_CAN_SHELL)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_SJA1000"></a>

## 60.68 `CONFIG_CAN_SJA1000`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用共用的恩智浦（NXP）SJA1000 CAN 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN
```

**被选择（Selected by）**

```text
CONFIG_CAN_BFLB_BL61X
CONFIG_CAN_ESP32_TWAI
CONFIG_CAN_KVASER_PCI
```

**定义位置（Location）**：[`drivers/can/Kconfig.sja1000:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.sja1000#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_BFLB_BL61X`](P060_drivers_can_配置项参考.md#CONFIG_CAN_BFLB_BL61X)、[`CONFIG_CAN_ESP32_TWAI`](P060_drivers_can_配置项参考.md#CONFIG_CAN_ESP32_TWAI)、[`CONFIG_CAN_KVASER_PCI`](P060_drivers_can_配置项参考.md#CONFIG_CAN_KVASER_PCI)。

<a id="CONFIG_CAN_SJA1000_MAX_FILTERS"></a>

## 60.69 `CONFIG_CAN_SJA1000_MAX_FILTERS`

**提示（Prompt）**：最大并发活动接收过滤器数量（Concurrent Active RX Filters）

**说明（Help）**

恩智浦（NXP）SJA1000 仅支持一个全宽接收过滤器（Full-Width RX Filter），因此收到的 CAN 帧在软件中进行过滤。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_SJA1000 && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/can/Kconfig.sja1000:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.sja1000#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN_SJA1000`](P060_drivers_can_配置项参考.md#CONFIG_CAN_SJA1000)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_STATS"></a>

## 60.70 `CONFIG_CAN_STATS`

**提示（Prompt）**：CAN 控制器设备统计（Device Statistics）

**说明（Help）**

启用 CAN 控制器设备统计（Device Statistics）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STATS && CONFIG_CAN
```

**定义位置（Location）**：[`drivers/can/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_STM32H7_FDCAN"></a>

## 60.71 `CONFIG_CAN_STM32H7_FDCAN`

**提示（Prompt）**：STM32H7 FDCAN 驱动（Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32H7_FDCAN_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAN_MCAN
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.stm32:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.stm32#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_STM32_BXCAN"></a>

## 60.72 `CONFIG_CAN_STM32_BXCAN`

**提示（Prompt）**：STM32 bxCAN 驱动（Driver）

**说明（Help）**

启用 STM32 bxCAN 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_BXCAN_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.stm32:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.stm32#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_STM32_BXCAN_MAX_EXT_ID_FILTERS"></a>

## 60.73 `CONFIG_CAN_STM32_BXCAN_MAX_EXT_ID_FILTERS`

**提示（Prompt）**：扩展 29 位标识符过滤器的最大数量（Extended ID Filters）

**说明（Help）**

定义应用可以添加的扩展标识符（Extended ID，29 位）过滤器最大数量。一个带掩码（Mask）的扩展 ID 过滤器，会占用 14 个可用过滤器组（Filter Bank）中的 1 个。过滤器总数量上限由下式确定：

```text
CAN_STM32_BXCAN_MAX_STD_ID_FILTERS + CAN_STM32_BXCAN_MAX_EXT_ID_FILTERS * 2 <= 28
```

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_STM32_BXCAN && CONFIG_CAN
```

**默认值（Defaults）**

```text
7
```

**取值范围（Ranges）**

```text
[0, 14]
```

**定义位置（Location）**：[`drivers/can/Kconfig.stm32:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.stm32#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → STM32 bxCAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_STM32_BXCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_STM32_BXCAN)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_STM32_BXCAN_MAX_STD_ID_FILTERS"></a>

## 60.74 `CONFIG_CAN_STM32_BXCAN_MAX_STD_ID_FILTERS`

**提示（Prompt）**：标准 11 位标识符过滤器的最大数量（Standard ID Filters）

**说明（Help）**

定义应用可以添加的标准标识符（Standard ID，11 位）过滤器最大数量。一个带掩码（Mask）的标准 ID 过滤器，会占用 14 个可用过滤器组（Filter Bank）中某一组的一半。过滤器总数量上限由下式确定：

```text
CAN_STM32_BXCAN_MAX_STD_ID_FILTERS + CAN_STM32_BXCAN_MAX_EXT_ID_FILTERS * 2 <= 28
```

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_STM32_BXCAN && CONFIG_CAN
```

**默认值（Defaults）**

```text
14
```

**取值范围（Ranges）**

```text
[0, 28]
```

**定义位置（Location）**：[`drivers/can/Kconfig.stm32:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.stm32#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → STM32 bxCAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_STM32_BXCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_STM32_BXCAN)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_STM32_FDCAN"></a>

## 60.75 `CONFIG_CAN_STM32_FDCAN`

**提示（Prompt）**：STM32 FDCAN 驱动（Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_FDCAN_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAN_MCAN
CONFIG_CAN_MCAN_FIXED_MRAM_LAYOUT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.stm32:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.stm32#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCAN)、[`CONFIG_CAN_MCAN_FIXED_MRAM_LAYOUT`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCAN_FIXED_MRAM_LAYOUT)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_STM32_FDCAN_MAX_EXT_ID_FILTERS"></a>

## 60.76 `CONFIG_CAN_STM32_FDCAN_MAX_EXT_ID_FILTERS`

**提示（Prompt）**：扩展 29 位标识符过滤器的最大数量（Extended ID Filters）

**说明（Help）**

定义应用可以添加的扩展标识符（Extended ID，29 位）过滤器的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_STM32_FDCAN && CONFIG_CAN
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[0, 8]
```

**定义位置（Location）**：[`drivers/can/Kconfig.stm32:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.stm32#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → STM32 FDCAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_STM32_FDCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_STM32_FDCAN)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_STM32_FDCAN_MAX_STD_ID_FILTERS"></a>

## 60.77 `CONFIG_CAN_STM32_FDCAN_MAX_STD_ID_FILTERS`

**提示（Prompt）**：标准 11 位标识符过滤器的最大数量（Standard ID Filters）

**说明（Help）**

定义应用可以添加的标准标识符（Standard ID，11 位）过滤器的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_STM32_FDCAN && CONFIG_CAN
```

**默认值（Defaults）**

```text
28
```

**取值范围（Ranges）**

```text
[0, 28]
```

**定义位置（Location）**：[`drivers/can/Kconfig.stm32:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.stm32#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → STM32 FDCAN 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_STM32_FDCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_STM32_FDCAN)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_TCAN4X5X"></a>

## 60.78 `CONFIG_CAN_TCAN4X5X`

**提示（Prompt）**：TI TCAN4x5x 驱动（Driver）

**说明（Help）**

启用德州仪器（Texas Instruments）TCAN4x5x 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TCAN4X5X_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAN_MCAN
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/can/Kconfig.tcan4x5x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.tcan4x5x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_CAN_MCAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCAN)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_CAN_TCAN4X5X_THREAD_PRIO"></a>

## 60.79 `CONFIG_CAN_TCAN4X5X_THREAD_PRIO`

**提示（Prompt）**：TCAN4x5x 中断线程优先级（Interrupt Thread Priority）

**说明（Help）**

处理中断并分发回调（Callback）的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_TCAN4X5X && CONFIG_CAN
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/can/Kconfig.tcan4x5x:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.tcan4x5x#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → TI TCAN4x5x 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_TCAN4X5X`](P060_drivers_can_配置项参考.md#CONFIG_CAN_TCAN4X5X)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_TCAN4X5X_THREAD_STACK_SIZE"></a>

## 60.80 `CONFIG_CAN_TCAN4X5X_THREAD_STACK_SIZE`

**提示（Prompt）**：TCAN4x5x 中断线程栈大小（Interrupt Thread Stack Size）

**说明（Help）**

处理中断并分发回调（Callback）的线程所用栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_TCAN4X5X && CONFIG_CAN
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/can/Kconfig.tcan4x5x:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.tcan4x5x#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → TI TCAN4x5x 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_TCAN4X5X`](P060_drivers_can_配置项参考.md#CONFIG_CAN_TCAN4X5X)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_TRANSCEIVER_GPIO"></a>

## 60.81 `CONFIG_CAN_TRANSCEIVER_GPIO`

**提示（Prompt）**：GPIO 控制的 CAN 收发器（CAN Transceiver）

**说明（Help）**

启用 GPIO 控制的 CAN 收发器（CAN Transceiver）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CAN_TRANSCEIVER_GPIO_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/can/transceiver/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/transceiver/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → CAN 收发器驱动（Transceiver Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_CAN_TRANSCEIVER_INIT_PRIORITY"></a>

## 60.82 `CONFIG_CAN_TRANSCEIVER_INIT_PRIORITY`

**提示（Prompt）**：CAN 收发器驱动初始化优先级（Init Priority）

**说明（Help）**

CAN 收发器（Transceiver）设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN
```

**默认值（Defaults）**

```text
45
```

**定义位置（Location）**：[`drivers/can/transceiver/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/transceiver/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → CAN 收发器驱动（Transceiver Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_XMC4XXX"></a>

## 60.83 `CONFIG_CAN_XMC4XXX`

**提示（Prompt）**：英飞凌 XMC4xxx CAN 驱动（Infineon Driver）

**说明（Help）**

启用英飞凌（Infineon）XMC4xxx CAN 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_CAN_NODE_ENABLED && CONFIG_CAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.xmc4xxx:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.xmc4xxx#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_XMC4XXX_INTERNAL_BUS_MODE"></a>

## 60.84 `CONFIG_CAN_XMC4XXX_INTERNAL_BUS_MODE`

**提示（Prompt）**：内部总线模式（Internal Bus Mode）

**说明（Help）**

将所有 XMC4XXX CAN 设备连接到内部总线（Internal Bus），使微控制器（MCU）内的 CAN 设备无需任何外部连接器即可交换消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_XMC4XXX && CONFIG_CAN
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/can/Kconfig.xmc4xxx:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.xmc4xxx#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 英飞凌 XMC4xxx CAN 驱动（Infineon Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_XMC4XXX`](P060_drivers_can_配置项参考.md#CONFIG_CAN_XMC4XXX)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CAN_XMC4XXX_MAX_FILTERS"></a>

## 60.85 `CONFIG_CAN_XMC4XXX_MAX_FILTERS`

**提示（Prompt）**：最大并发活动过滤器数量（Concurrent Active Filters）

**说明（Help）**

`can_add_rx_callback()` API 调用支持的最大过滤器（Filter）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_XMC4XXX && CONFIG_CAN
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/can/Kconfig.xmc4xxx:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.xmc4xxx#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 英飞凌 XMC4xxx CAN 驱动（Infineon Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_XMC4XXX`](P060_drivers_can_配置项参考.md#CONFIG_CAN_XMC4XXX)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_XMC4XXX_MAX_TX_QUEUE"></a>

## 60.86 `CONFIG_CAN_XMC4XXX_MAX_TX_QUEUE`

**提示（Prompt）**：最大排队消息数量（Maximum Queued Messages）

**说明（Help）**

定义发送回调指针（Transmit Callback Pointer）和信号量（Semaphore）数组的大小，以及发送队列（TX Queue）中的消息数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_XMC4XXX && CONFIG_CAN
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/can/Kconfig.xmc4xxx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.xmc4xxx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 英飞凌 XMC4xxx CAN 驱动（Infineon Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_XMC4XXX`](P060_drivers_can_配置项参考.md#CONFIG_CAN_XMC4XXX)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<a id="CONFIG_CAN_XMC4XXX_RX_FIFO_ITEMS"></a>

## 60.87 `CONFIG_CAN_XMC4XXX_RX_FIFO_ITEMS`

**提示（Prompt）**：分配给每个接收 FIFO 的 CAN 消息数量（RX FIFO Messages）

**说明（Help）**

定义每个接收先进先出队列（RX FIFO）中的 CAN 消息数量。每个接收过滤器（RX Filter）都会创建一个独立的 RX FIFO。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN_XMC4XXX && CONFIG_CAN
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/can/Kconfig.xmc4xxx:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/Kconfig.xmc4xxx#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制器局域网驱动（Controller Area Network，CAN） → 英飞凌 XMC4xxx CAN 驱动（Infineon Driver）

**配置项引用（Symbol References）**：[`CONFIG_CAN_XMC4XXX`](P060_drivers_can_配置项参考.md#CONFIG_CAN_XMC4XXX)、[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)。

<!-- kconfig-navigation -->

[上一章](P059_drivers_cache_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P061_drivers_charger_配置项参考.md)
