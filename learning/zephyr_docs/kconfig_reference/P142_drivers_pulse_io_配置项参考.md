---
id: learning.zephyr-docs.kconfig-reference.page-142
title: "`drivers/pulse_io`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第142章\_`drivers/pulse_io`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/pulse_io` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PULSE_IO"></a>

## 142.1 `CONFIG_PULSE_IO`

**提示（Prompt）**：脉冲 I/O（Pulse IO）驱动

**说明（Help）**

启用 Pulse IO 子系统支持。该子系统为在 GPIO 线上生成和捕获定时数字边沿（Timed Digital Edge）的硬件提供与厂商无关的抽象。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_WS2812_STRIP_PULSE_IO
```

**定义位置（Location）**：[`drivers/pulse_io/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pulse_io/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WS2812_STRIP_PULSE_IO`](P115_drivers_led_strip_配置项参考.md#CONFIG_WS2812_STRIP_PULSE_IO)。

<a id="CONFIG_PULSE_IO_ESP32_RMT"></a>

## 142.2 `CONFIG_PULSE_IO_ESP32_RMT`

**提示（Prompt）**：Espressif RMT Pulse IO 后端（Backend）

**说明（Help）**

启用 Espressif 遥控收发器（Remote Control Transceiver，RMT）Pulse IO 后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_RMT_ENABLED && CONFIG_PULSE_IO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pulse_io/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pulse_io/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉冲 I/O（Pulse IO）驱动

**配置项引用（Symbol References）**：[`CONFIG_PULSE_IO`](P142_drivers_pulse_io_配置项参考.md#CONFIG_PULSE_IO)。

<a id="CONFIG_PULSE_IO_ESP32_RMT_DMA"></a>

## 142.3 `CONFIG_PULSE_IO_ESP32_RMT_DMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在后端支持其 RMT DMA 代际的 SoC 上编译 RMT DMA 路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PULSE_IO_ESP32_RMT && CONFIG_PULSE_IO
```

**默认值（Defaults）**

```text
CONFIG_SOC_SERIES_ESP32S3
```

**主动选择（Selects）**

```text
CONFIG_DMA if DT_HAS_ESPRESSIF_ESP32_GDMA_ENABLED
```

**定义位置（Location）**：[`drivers/pulse_io/Kconfig.esp32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pulse_io/Kconfig.esp32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉冲 I/O（Pulse IO）驱动 → Espressif RMT Pulse IO 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_PULSE_IO_ESP32_RMT`](P142_drivers_pulse_io_配置项参考.md#CONFIG_PULSE_IO_ESP32_RMT)、[`CONFIG_PULSE_IO`](P142_drivers_pulse_io_配置项参考.md#CONFIG_PULSE_IO)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_PULSE_IO_ESP32_RMT_DMA_WORDS"></a>

## 142.4 `CONFIG_PULSE_IO_ESP32_RMT_DMA_WORDS`

**提示（Prompt）**：RMT DMA 缓冲区大小，以 RMT 字（Word）计

**说明（Help）**

静态发送和接收 DMA 中转缓冲区（Bounce Buffer）大小，以 RMT 符号字计，每字 4 字节。仅在通过设备树 `dmas` 属性启用 DMA 时，由最后一个发送通道和最后一个接收通道使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PULSE_IO_ESP32_RMT_DMA && CONFIG_PULSE_IO_ESP32_RMT && CONFIG_PULSE_IO
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/pulse_io/Kconfig.esp32:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pulse_io/Kconfig.esp32#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉冲 I/O（Pulse IO）驱动 → Espressif RMT Pulse IO 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_PULSE_IO_ESP32_RMT_DMA`](P142_drivers_pulse_io_配置项参考.md#CONFIG_PULSE_IO_ESP32_RMT_DMA)、[`CONFIG_PULSE_IO_ESP32_RMT`](P142_drivers_pulse_io_配置项参考.md#CONFIG_PULSE_IO_ESP32_RMT)、[`CONFIG_PULSE_IO`](P142_drivers_pulse_io_配置项参考.md#CONFIG_PULSE_IO)。

<a id="CONFIG_PULSE_IO_INIT_PRIORITY"></a>

## 142.5 `CONFIG_PULSE_IO_INIT_PRIORITY`

**提示（Prompt）**：Pulse IO 初始化优先级

**说明（Help）**

Pulse IO 设备的设备驱动初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PULSE_IO
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/pulse_io/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pulse_io/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉冲 I/O（Pulse IO）驱动

**配置项引用（Symbol References）**：[`CONFIG_PULSE_IO`](P142_drivers_pulse_io_配置项参考.md#CONFIG_PULSE_IO)。

<a id="CONFIG_PULSE_IO_LOOPBACK"></a>

## 142.6 `CONFIG_PULSE_IO_LOOPBACK`

**提示（Prompt）**：软件回环（Software Loopback）Pulse IO 后端

**说明（Help）**

启用软件回环 Pulse IO 后端。它将发送的符号回送到接收端，使子系统 API 无需硬件即可测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_PULSE_IO_LOOPBACK_ENABLED && CONFIG_PULSE_IO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pulse_io/Kconfig.loopback:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pulse_io/Kconfig.loopback#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉冲 I/O（Pulse IO）驱动

**配置项引用（Symbol References）**：[`CONFIG_PULSE_IO`](P142_drivers_pulse_io_配置项参考.md#CONFIG_PULSE_IO)。

<!-- kconfig-navigation -->

[上一章](P141_drivers_ptp_clock_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P143_drivers_pwm_配置项参考.md)
