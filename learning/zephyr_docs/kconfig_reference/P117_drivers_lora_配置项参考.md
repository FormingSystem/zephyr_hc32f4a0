---
id: learning.zephyr-docs.kconfig-reference.page-117
title: "`drivers/lora`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第117章\_`drivers/lora`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/lora` 的 31 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LORA"></a>

## 117.1 `CONFIG_LORA`

**提示（Prompt）**：LoRa 驱动

**说明（Help）**

在系统配置中纳入 LoRa 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_POLL
```

**定义位置（Location）**：[`drivers/lora/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)。

<a id="CONFIG_LORA_BASICS_MODEM_ASYNC_RX_MAX_PAYLOAD"></a>

## 117.2 `CONFIG_LORA_BASICS_MODEM_ASYNC_RX_MAX_PAYLOAD`

**提示（Prompt）**：异步接收（Async RX）可接收的最大有效载荷大小

**说明（Help）**

运行异步接收处理程序时，在系统工作队列（System Workqueue）的栈上分配此大小的缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM && CONFIG_LORA
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/lora/lora-basics-modem/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/lora-basics-modem/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_BASICS_MODEM_DEFERRED_INIT"></a>

## 117.3 `CONFIG_LORA_BASICS_MODEM_DEFERRED_INIT`

**提示（Prompt）**：将无线电初始化推迟至首次使用（Defer Initialization）

**说明（Help）**

启用后，无线电硬件初始化（复位、中断配置）会推迟到首次调用 `lora_config()` 时进行，使应用能够在无线电初始化之前完成准备。禁用时，无线电在启动时完成全部初始化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM && CONFIG_LORA
```

**定义位置（Location）**：[`drivers/lora/lora-basics-modem/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/lora-basics-modem/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE"></a>

## 117.4 `CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE`

**提示（Prompt）**：向应用层报告的接收信号强度指示（RSSI）类型

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM && CONFIG_LORA
```

**默认值（Defaults）**

```text
CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE_SIGNAL
```

**可选项（Choices）**

```text
CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE_PACKET
CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE_SIGNAL
```

**定义位置（Location）**：[`drivers/lora/lora-basics-modem/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/lora-basics-modem/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)、[`CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE_SIGNAL`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE_SIGNAL)、[`CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE_PACKET`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE_PACKET)。

<a id="CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE_PACKET"></a>

## 117.5 `CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE_PACKET`

**提示（Prompt）**：报告数据包 RSSI（`rssi_pkt_in_dbm`）

**说明（Help）**

数据包 RSSI 表示配置频段内的信号强度。一旦 LoRa 信号降到噪声底（Noise Floor）以下，此值将停留在噪声底的信号强度水平。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE>
```

**定义位置（Location）**：[`drivers/lora/lora-basics-modem/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/lora-basics-modem/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → 向应用层报告的接收信号强度指示（RSSI）类型

**配置项引用（Symbol References）**：[`CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE)。

<a id="CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE_SIGNAL"></a>

## 117.6 `CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE_SIGNAL`

**提示（Prompt）**：报告信号 RSSI（`signal_rssi_pkt_in_dbm`）

**说明（Help）**

信号 RSSI 是对接收到的 LoRa 信号强度的估算。与数据包 RSSI 不同，当信号接近接收器灵敏度极限时，此值会继续下降到噪声底（Noise Floor）以下。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE>
```

**定义位置（Location）**：[`drivers/lora/lora-basics-modem/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/lora-basics-modem/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → 向应用层报告的接收信号强度指示（RSSI）类型

**配置项引用（Symbol References）**：[`CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_BASICS_MODEM_RSSI_REPORT_TYPE)。

<a id="CONFIG_LORA_ENERGY_DETECT_SAMPLE_INTERVAL_US"></a>

## 117.7 `CONFIG_LORA_ENERGY_DETECT_SAMPLE_INTERVAL_US`

**提示（Prompt）**：能量检测采样间隔（Energy Detection Sample Interval），单位为微秒

**说明（Help）**

侦听信道时，两次 RSSI 采样之间的睡眠时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/lora/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_FAKE"></a>

## 117.8 `CONFIG_LORA_FAKE`

**提示（Prompt）**：模拟 LoRa 驱动程序。

**说明（Help）**

启用基于伪函数框架（FFF）的模拟 LoRa 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_NATIVE && DT_HAS_ZEPHYR_FAKE_LORA_ENABLED && CONFIG_LORA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/lora/native/Kconfig.fake:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/native/Kconfig.fake#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_FAKE_OPTIONAL_API"></a>

## 117.9 `CONFIG_LORA_FAKE_OPTIONAL_API`

**提示（Prompt）**：模拟 LoRa 驱动的可选 API 支持

**说明（Help）**

在模拟驱动中编译所有可选 LoRa 驱动 API 函数的支持。禁用后，可测试 LoRa 驱动仅实现必需 API 时应用的行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_FAKE && CONFIG_LORA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/lora/native/Kconfig.fake:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/native/Kconfig.fake#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → 模拟 LoRa 驱动程序。

**配置项引用（Symbol References）**：[`CONFIG_LORA_FAKE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_FAKE)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_GFSK"></a>

## 117.10 `CONFIG_LORA_GFSK`

**提示（Prompt）**：高斯频移键控（GFSK）调制

**说明（Help）**

除 LoRa 外，还提供高斯频移键控（GFSK）调制的软件支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA
```

**定义位置（Location）**：[`drivers/lora/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_INIT_PRIORITY"></a>

## 117.11 `CONFIG_LORA_INIT_PRIORITY`

**提示（Prompt）**：LoRa 初始化优先级（Initialization Priority）

**说明（Help）**

LoRa 驱动的系统初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/lora/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_LR11XX_NATIVE"></a>

## 117.12 `CONFIG_LORA_LR11XX_NATIVE`

**提示（Prompt）**：Semtech LR11XX 原生驱动（Native Driver，实验性）

**说明（Help）**

启用 Semtech LR11xx LoRa 收发器的原生驱动。此实验性驱动不依赖 `loramac-node` 或 `lora-basics-modem` 外部模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_NATIVE && DT_HAS_SEMTECH_LR1121_ENABLED && CONFIG_LORA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/lora/native/lr11xx/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/native/lr11xx/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_LORA_LR11XX_NATIVE_SLEEP"></a>

## 117.13 `CONFIG_LORA_LR11XX_NATIVE_SLEEP`

**提示（Prompt）**：睡眠模式电源管理（Sleep Mode Power Management）

**说明（Help）**

空闲时使 LR11xx 无线电进入睡眠模式以降低功耗，电流约为 1.6 μA，而待机模式约为 1.25 mA。禁用后，无线电保持待机，以获得更快响应。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_LR11XX_NATIVE && CONFIG_LORA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/lora/native/lr11xx/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/native/lr11xx/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → Semtech LR11XX 原生驱动（Native Driver，实验性）

**配置项引用（Symbol References）**：[`CONFIG_LORA_LR11XX_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_LR11XX_NATIVE)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_MODULE_BACKEND"></a>

## 117.14 `CONFIG_LORA_MODULE_BACKEND`

**提示（Prompt）**：要使用的底层 LoRa 调制解调器集成（Low-level Modem Integration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA
```

**默认值（Defaults）**

```text
CONFIG_LORA_MODULE_BACKEND_NATIVE if DT_HAS_ZEPHYR_FAKE_LORA_ENABLED
CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM if DT_HAS_SEMTECH_SX1268_ENABLED || DT_HAS_SEMTECH_LLCC68_ENABLED || DT_HAS_SEMTECH_SX1278_ENABLED
```

**可选项（Choices）**

```text
CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE
CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM
CONFIG_LORA_MODULE_BACKEND_NATIVE
```

**定义位置（Location）**：[`drivers/lora/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)、[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM)、[`CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE)。

<a id="CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE"></a>

## 117.15 `CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE`

**提示（Prompt）**：loramac-node 后端（Backend）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_LORAMAC_NODE_MODULE && <choice CONFIG_LORA_MODULE_BACKEND>
```

**定义位置（Location）**：[`drivers/lora/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → 要使用的底层 LoRa 调制解调器集成（Low-level Modem Integration）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_LORAMAC_NODE_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_LORAMAC_NODE_MODULE)、[`CONFIG_LORA_MODULE_BACKEND`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_LORAMAC_NODE_MODULE`。

<a id="CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM"></a>

## 117.16 `CONFIG_LORA_MODULE_BACKEND_LORA_BASICS_MODEM`

**提示（Prompt）**：LoRa Basic Modem 后端（Backend）

**说明（Help）**

使用 LoRa Basics Modem 模块提供 LoRa API 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_LORA_BASICS_MODEM_MODULE && (DT_HAS_SEMTECH_SX1262_ENABLED || DT_HAS_SEMTECH_SX1261_ENABLED || DT_HAS_SEMTECH_SX1272_ENABLED || DT_HAS_SEMTECH_SX1276_ENABLED || DT_HAS_SEMTECH_SX1268_ENABLED || DT_HAS_SEMTECH_LLCC68_ENABLED || DT_HAS_SEMTECH_SX1278_ENABLED) && <choice CONFIG_LORA_MODULE_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_USE_LORA_BASICS_MODEM_DRIVERS
```

**定义位置（Location）**：[`drivers/lora/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → 要使用的底层 LoRa 调制解调器集成（Low-level Modem Integration）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_LORA_BASICS_MODEM_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_LORA_BASICS_MODEM_MODULE)、[`CONFIG_LORA_MODULE_BACKEND`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND)、[`CONFIG_USE_LORA_BASICS_MODEM_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_LORA_BASICS_MODEM_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_LORA_BASICS_MODEM_MODULE`、`CONFIG_USE_LORA_BASICS_MODEM_DRIVERS`。

<a id="CONFIG_LORA_MODULE_BACKEND_NATIVE"></a>

## 117.17 `CONFIG_LORA_MODULE_BACKEND_NATIVE`

**提示（Prompt）**：Zephyr 原生后端（Native Backend）

**说明（Help）**

使用 Zephyr 内置 LoRa 驱动，无需外部模块。所用快照中支持 SX1261/SX1262、STM32WL、LR1121 和模拟无线电。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_SEMTECH_SX1261_ENABLED || DT_HAS_SEMTECH_SX1262_ENABLED || DT_HAS_ST_STM32WL_SUBGHZ_RADIO_ENABLED || DT_HAS_SEMTECH_LR1121_ENABLED || DT_HAS_ZEPHYR_FAKE_LORA_ENABLED) && <choice CONFIG_LORA_MODULE_BACKEND>
```

**定义位置（Location）**：[`drivers/lora/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → 要使用的底层 LoRa 调制解调器集成（Low-level Modem Integration）

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND)。

<a id="CONFIG_LORA_RSSI_SETTLE_US"></a>

## 117.18 `CONFIG_LORA_RSSI_SETTLE_US`

**提示（Prompt）**：RSSI 稳定时间（Settling Time），单位为微秒

**说明（Help）**

进入接收模式后、读取 RSSI 之前等待的时间，用于让接收器稳定。无线电所需时长取决于驱动：访问之间进入睡眠的驱动会将其中一部分时间用于唤醒校准，读取过早会得到噪声底值。默认值来自 SX1262：`loramac-node` 和原生驱动在 0.5 ms 后就绪，Basics Modem 适配层需要 7 ms。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA
```

**默认值（Defaults）**

```text
500 if CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE
500 if CONFIG_LORA_MODULE_BACKEND_NATIVE
10000
```

**定义位置（Location）**：[`drivers/lora/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)、[`CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE)、[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)。

<a id="CONFIG_LORA_RYLRXXX"></a>

## 117.19 `CONFIG_LORA_RYLRXXX`

**提示（Prompt）**：Reyax LYLR 驱动

**说明（Help）**

启用 Reyax LYLR 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REYAX_RYLRXXX_ENABLED && CONFIG_LORA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MODEM_MODULES
CONFIG_MODEM_CHAT
CONFIG_MODEM_PIPE
CONFIG_MODEM_BACKEND_UART
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/lora/Kconfig.rylrxxx:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig.rylrxxx#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_CHAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CHAT)、[`CONFIG_MODEM_PIPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_PIPE)、[`CONFIG_MODEM_BACKEND_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_LORA_RYLRXX_CMD_BUF_SIZE"></a>

## 117.20 `CONFIG_LORA_RYLRXX_CMD_BUF_SIZE`

**提示（Prompt）**：命令缓冲区大小（Command Buffer Size）

**说明（Help）**

配置命令缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_RYLRXXX && CONFIG_LORA
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/lora/Kconfig.rylrxxx:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig.rylrxxx#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → Reyax LYLR 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA_RYLRXXX`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_RYLRXXX)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_SHELL"></a>

## 117.21 `CONFIG_LORA_SHELL`

**提示（Prompt）**：LoRa 命令行（Shell）

**说明（Help）**

启用用于测试的 LoRa Shell。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_LORA
```

**定义位置（Location）**：[`drivers/lora/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_STM32WL_SUBGHZ_RADIO"></a>

## 117.22 `CONFIG_LORA_STM32WL_SUBGHZ_RADIO`

**提示（Prompt）**：STM32WL SUBGHZ 无线电驱动

**说明（Help）**

启用 STM32WL SUBGHZ 无线电的 LoRa 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32WL_SUBGHZ_RADIO_ENABLED && CONFIG_LORA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_SEMTECH_SX126X
CONFIG_SPI
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/lora/Kconfig.sx12xx:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig.sx12xx#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)、[`CONFIG_HAS_SEMTECH_SX126X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SEMTECH_SX126X)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SEMTECH_SX126X`。

<a id="CONFIG_LORA_SX126X"></a>

## 117.23 `CONFIG_LORA_SX126X`

**提示（Prompt）**：Semtech SX126x 驱动

**说明（Help）**

启用 Semtech SX1261、SX1262/SX1268 和 LLCC68 的 LoRa 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_SEMTECH_SX1261_ENABLED || DT_HAS_SEMTECH_SX1262_ENABLED || DT_HAS_SEMTECH_SX1268_ENABLED || DT_HAS_SEMTECH_LLCC68_ENABLED) && CONFIG_LORA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_SEMTECH_SX126X
CONFIG_SPI
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/lora/Kconfig.sx12xx:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig.sx12xx#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)、[`CONFIG_HAS_SEMTECH_SX126X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SEMTECH_SX126X)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SEMTECH_SX126X`。

<a id="CONFIG_LORA_SX126X_NATIVE"></a>

## 117.24 `CONFIG_LORA_SX126X_NATIVE`

**提示（Prompt）**：Semtech SX126x 原生驱动（Native Driver，实验性）

**说明（Help）**

启用 Semtech SX1261/SX1262 LoRa 收发器的原生驱动，包括 STM32WL 集成的 Sub-GHz 无线电。此实验性驱动不依赖 `loramac-node` 或 `lora-basics-modem` 外部模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_NATIVE && (DT_HAS_SEMTECH_SX1262_ENABLED || DT_HAS_SEMTECH_SX1261_ENABLED || DT_HAS_ST_STM32WL_SUBGHZ_RADIO_ENABLED) && CONFIG_LORA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/lora/native/sx126x/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/native/sx126x/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_LORA_SX126X_NATIVE_SLEEP"></a>

## 117.25 `CONFIG_LORA_SX126X_NATIVE_SLEEP`

**提示（Prompt）**：睡眠模式电源管理（Sleep Mode Power Management）

**说明（Help）**

空闲时使 SX126x 无线电进入睡眠模式以降低功耗，电流约为 600 nA，而待机模式约为 1.6 mA。禁用后，无线电保持待机，以获得更快响应。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_SX126X_NATIVE && CONFIG_LORA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/lora/native/sx126x/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/native/sx126x/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → Semtech SX126x 原生驱动（Native Driver，实验性）

**配置项引用（Symbol References）**：[`CONFIG_LORA_SX126X_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_SX126X_NATIVE)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_SX126X_NATIVE_STANDALONE"></a>

## 117.26 `CONFIG_LORA_SX126X_NATIVE_STANDALONE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

原生 SX126x 驱动对独立 SX1261/SX1262 的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_SX126X_NATIVE && (DT_HAS_SEMTECH_SX1262_ENABLED || DT_HAS_SEMTECH_SX1261_ENABLED) && CONFIG_LORA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/lora/native/sx126x/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/native/sx126x/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → Semtech SX126x 原生驱动（Native Driver，实验性）

**配置项引用（Symbol References）**：[`CONFIG_LORA_SX126X_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_SX126X_NATIVE)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_SX126X_NATIVE_STM32WL"></a>

## 117.27 `CONFIG_LORA_SX126X_NATIVE_STM32WL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

原生 SX126x 驱动对 STM32WL Sub-GHz 无线电的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_SX126X_NATIVE && DT_HAS_ST_STM32WL_SUBGHZ_RADIO_ENABLED && CONFIG_LORA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/lora/native/sx126x/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/native/sx126x/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → Semtech SX126x 原生驱动（Native Driver，实验性）

**配置项引用（Symbol References）**：[`CONFIG_LORA_SX126X_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_SX126X_NATIVE)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_LORA_SX127X"></a>

## 117.28 `CONFIG_LORA_SX127X`

**提示（Prompt）**：Semtech SX127x 驱动

**说明（Help）**

启用 Semtech SX1272 和 SX1276/SX1278 的 LoRa 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_SEMTECH_SX1272_ENABLED || DT_HAS_SEMTECH_SX1276_ENABLED || DT_HAS_SEMTECH_SX1278_ENABLED) && CONFIG_LORA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_SEMTECH_SX1272 if DT_HAS_SEMTECH_SX1272_ENABLED
CONFIG_HAS_SEMTECH_SX1276 if DT_HAS_SEMTECH_SX1276_ENABLED || DT_HAS_SEMTECH_SX1278_ENABLED
CONFIG_SPI
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/lora/Kconfig.sx12xx:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig.sx12xx#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)、[`CONFIG_HAS_SEMTECH_SX1272`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SEMTECH_SX1272)、[`CONFIG_HAS_SEMTECH_SX1276`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_SEMTECH_SX1276)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_SEMTECH_SX1272`、`CONFIG_HAS_SEMTECH_SX1276`。

<a id="CONFIG_RYLRXXX_MODEM_BUFFERS_SIZE"></a>

## 117.29 `CONFIG_RYLRXXX_MODEM_BUFFERS_SIZE`

**提示（Prompt）**：调制解调器库缓冲区大小（Modem Library Buffer Size）

**说明（Help）**

配置调制解调器库的缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_RYLRXXX && CONFIG_LORA
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/lora/Kconfig.rylrxxx:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig.rylrxxx#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → Reyax LYLR 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA_RYLRXXX`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_RYLRXXX)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_RYLRXXX_RADIO_CMD_RESPONSE_TIMEOUT_MS"></a>

## 117.30 `CONFIG_RYLRXXX_RADIO_CMD_RESPONSE_TIMEOUT_MS`

**提示（Prompt）**：发送命令后等待无线电串行接口响应的超时（Response Timeout）

**说明（Help）**

配置发送命令后等待无线电确认的超时时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_RYLRXXX && CONFIG_LORA
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/lora/Kconfig.rylrxxx:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig.rylrxxx#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → Reyax LYLR 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA_RYLRXXX`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_RYLRXXX)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<a id="CONFIG_RYLRXXX_UNSOLICITED_RX_MSGQ_SIZE"></a>

## 117.31 `CONFIG_RYLRXXX_UNSOLICITED_RX_MSGQ_SIZE`

**提示（Prompt）**：消息队列中保存的消息数量（Message Count）

**说明（Help）**

配置消息队列（Message Queue）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_RYLRXXX && CONFIG_LORA
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/lora/Kconfig.rylrxxx:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lora/Kconfig.rylrxxx#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → Reyax LYLR 驱动

**配置项引用（Symbol References）**：[`CONFIG_LORA_RYLRXXX`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_RYLRXXX)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)。

<!-- kconfig-navigation -->

[上一章](P116_drivers_lin_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P118_drivers_mbox_配置项参考.md)
