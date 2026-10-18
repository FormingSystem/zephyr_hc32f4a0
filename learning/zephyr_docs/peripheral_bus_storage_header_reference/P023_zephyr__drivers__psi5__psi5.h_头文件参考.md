---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-23
title: zephyr__drivers__psi5__psi5.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/psi5_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_drivers\_\_psi5\_\_psi5.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/psi5_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

外设传感器接口（Peripheral Sensor Interface，PSI5）的驱动API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/psi5.h>
```

查看此文件的源码。

外设传感器接口（Peripheral Sensor Interface，PSI5）的驱动API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 23.1\_数据结构（Data Structures）

<a id="r_psi5_5Fframe"></a>

```c
struct psi5_frame
```

相关声明：[psi5_frame](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md)。

外设传感器接口5（PSI5）的帧结构。

<a id="r_psi5_5Frx_5Fcallback_5Fconfig"></a>

```c
struct psi5_rx_callback_config
```

相关声明：[psi5_rx_callback_config](../peripheral_bus_storage_model_reference/P072_psi5_rx_callback_config_结构体.md)。

接收回调（RX Callback）的配置结构。

<a id="r_psi5_5Frx_5Fcallback_5Fconfigs"></a>

```c
struct psi5_rx_callback_configs
```

相关声明：[psi5_rx_callback_configs](../peripheral_bus_storage_model_reference/P073_psi5_rx_callback_configs_结构体.md)。

接收回调（RX Callback）注册的组合配置结构。

<a id="r_psi5_5Fdriver_5Fapi"></a>

```c
struct psi5_driver_api
```

相关声明：[psi5_driver_api](../peripheral_bus_storage_model_reference/P070_psi5_driver_api_结构体.md)。

驱动操作（Driver Operations）：外设传感器接口5（PSI5）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 23.2\_类型定义（Typedefs）

<a id="r_gaac8c99036369b14d639cfb82f3b9cd32"></a>

```c
typedef void(* psi5_tx_callback_t) (const struct device *dev, uint8_t channel, int status, void *user_data)
```

相关声明：[psi5_tx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gaac8c99036369b14d639cfb82f3b9cd32)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

定义用于发送的应用程序回调处理函数签名。

<a id="r_ga5f43079d704d882ae014c7a15bde6406"></a>

```c
typedef void(* psi5_rx_frame_callback_t) (const struct device *dev, uint8_t channel, uint32_t num_frame, void *user_data)
```

相关声明：[psi5_rx_frame_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga5f43079d704d882ae014c7a15bde6406)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

定义用于接收帧的应用程序回调处理函数签名。

<a id="r_gaf86804dd3befe78878ed2d9b3bad9a49"></a>

```c
typedef int(* psi5_start_sync_t) (const struct device *dev, uint8_t channel)
```

相关声明：[psi5_start_sync_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#gaf86804dd3befe78878ed2d9b3bad9a49)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启动 PSI5 同步时的回调 API，参数说明见 `psi5_start_sync()`。

<a id="r_ga44a73fc30fb29d688d761b8d23eb0da6"></a>

```c
typedef int(* psi5_stop_sync_t) (const struct device *dev, uint8_t channel)
```

相关声明：[psi5_stop_sync_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#ga44a73fc30fb29d688d761b8d23eb0da6)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

停止 PSI5 同步时的回调 API，参数说明见 `psi5_stop_sync()`。

<a id="r_ga1ddcb06317f425a9d97defb1e4ccd677"></a>

```c
typedef int(* psi5_send_t) (const struct device *dev, uint8_t channel, const uint64_t data, k_timeout_t timeout, psi5_tx_callback_t callback, void *user_data)
```

相关声明：[psi5_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#ga1ddcb06317f425a9d97defb1e4ccd677)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[psi5_tx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gaac8c99036369b14d639cfb82f3b9cd32)。

发送 PSI5 帧时的回调 API，参数说明见 `psi5_send()`。

<a id="r_gae9b98f6b16ed1364364e1d63f18bb479"></a>

```c
typedef int(* psi5_register_callback_t) (const struct device *dev, uint8_t channel, struct psi5_rx_callback_configs callback_configs)
```

相关声明：[psi5_register_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#gae9b98f6b16ed1364364e1d63f18bb479)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[psi5_rx_callback_configs](../peripheral_bus_storage_model_reference/P073_psi5_rx_callback_configs_结构体.md)。

添加接收回调时的回调 API，参数说明见 `psi5_register_callback()`。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 23.3\_枚举（Enumerations）

<a id="r_ga5cb0ef3be35e9ff2d05c39cc17f2659f"></a>

```c
enum psi5_frame_type { PSI5_SERIAL_FRAME_4_BIT_ID , PSI5_SERIAL_FRAME_8_BIT_ID , PSI5_DATA_FRAME }
```

相关声明：[psi5_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga5cb0ef3be35e9ff2d05c39cc17f2659f)、[PSI5_SERIAL_FRAME_4_BIT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gga5cb0ef3be35e9ff2d05c39cc17f2659fa456be16421eb918370e6e50c8367d3ff)、[PSI5_SERIAL_FRAME_8_BIT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gga5cb0ef3be35e9ff2d05c39cc17f2659fad1bbb5de03efb0be1075766a396d009a)、[PSI5_DATA_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gga5cb0ef3be35e9ff2d05c39cc17f2659fa8d7f6f8699ded09880c3febd44375c8f)。

PSI5 帧类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.4\_函数（Functions）

<a id="r_gabbc2a744edf1ab01e7bd9321054cf32b"></a>

```c
int psi5_start_sync (const struct device *dev, uint8_t channel)
```

相关声明：[psi5_start_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gabbc2a744edf1ab01e7bd9321054cf32b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启动指定通道上的同步脉冲发生器（Sync pulse generator）。

<a id="r_gacebce085be1e554e3faa7b69fd8da61f"></a>

```c
int psi5_stop_sync (const struct device *dev, uint8_t channel)
```

相关声明：[psi5_stop_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gacebce085be1e554e3faa7b69fd8da61f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

停止指定通道上的同步脉冲发生器。

<a id="r_ga3a27606e2828206608a79ada7238466d"></a>

```c
int psi5_send (const struct device *dev, uint8_t channel, const uint64_t data, k_timeout_t timeout, psi5_tx_callback_t callback, void *user_data)
```

相关声明：[psi5_send](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga3a27606e2828206608a79ada7238466d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[psi5_tx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gaac8c99036369b14d639cfb82f3b9cd32)。

在指定通道上传输 PSI5 数据。

<a id="r_ga37b0fcdecd4629c5f2657b1cc2e227b4"></a>

```c
int psi5_register_callback (const struct device *dev, uint8_t channel, struct psi5_rx_callback_configs callback_configs)
```

相关声明：[psi5_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga37b0fcdecd4629c5f2657b1cc2e227b4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[psi5_rx_callback_configs](../peripheral_bus_storage_model_reference/P073_psi5_rx_callback_configs_结构体.md)。

添加回调函数，以处理指定通道接收到的消息。


## 23.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/psi5_8h_source.html)
- [psi5_frame](../peripheral_bus_storage_model_reference/P071_psi5_frame_结构体.md)
- [psi5_rx_callback_config](../peripheral_bus_storage_model_reference/P072_psi5_rx_callback_config_结构体.md)
- [psi5_rx_callback_configs](../peripheral_bus_storage_model_reference/P073_psi5_rx_callback_configs_结构体.md)
- [psi5_driver_api](../peripheral_bus_storage_model_reference/P070_psi5_driver_api_结构体.md)
- [psi5_tx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gaac8c99036369b14d639cfb82f3b9cd32)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [psi5_rx_frame_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga5f43079d704d882ae014c7a15bde6406)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [psi5_start_sync_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#gaf86804dd3befe78878ed2d9b3bad9a49)
- [psi5_start_sync()](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gabbc2a744edf1ab01e7bd9321054cf32b)
- [psi5_stop_sync_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#ga44a73fc30fb29d688d761b8d23eb0da6)
- [psi5_stop_sync()](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gacebce085be1e554e3faa7b69fd8da61f)
- [psi5_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#ga1ddcb06317f425a9d97defb1e4ccd677)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [psi5_send()](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga3a27606e2828206608a79ada7238466d)
- [psi5_register_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#gae9b98f6b16ed1364364e1d63f18bb479)
- [psi5_register_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga37b0fcdecd4629c5f2657b1cc2e227b4)
- [psi5_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga5cb0ef3be35e9ff2d05c39cc17f2659f)
- [PSI5_SERIAL_FRAME_4_BIT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gga5cb0ef3be35e9ff2d05c39cc17f2659fa456be16421eb918370e6e50c8367d3ff)
- [PSI5_SERIAL_FRAME_8_BIT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gga5cb0ef3be35e9ff2d05c39cc17f2659fad1bbb5de03efb0be1075766a396d009a)
- [PSI5_DATA_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gga5cb0ef3be35e9ff2d05c39cc17f2659fa8d7f6f8699ded09880c3febd44375c8f)

<a id="header-details"></a>

---

[上一章](P022_zephyr__drivers__ps2.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__sd__sd.h_头文件参考.md)
