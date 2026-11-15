---
id: learning.zephyr-docs.api-platform-topic-reference.page-98
title: PSI5 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第98章\_PSI5 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现外设传感器接口 5 驱动（PSI5 Driver）所需的 API 类型定义（Type Definitions）、回调签名（Callback Signatures）及其他辅助工具（Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 98.1\_数据结构（Data Structures）

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

## 98.2\_类型定义（Typedefs）

<a id="r_gaf86804dd3befe78878ed2d9b3bad9a49"></a>

```c
typedef int(* psi5_start_sync_t) (const struct device *dev, uint8_t channel)
```

相关声明：[psi5_start_sync_t](#gaf86804dd3befe78878ed2d9b3bad9a49)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启动 PSI5 同步时的回调 API，参数说明见 `psi5_start_sync()`。

<a id="r_ga44a73fc30fb29d688d761b8d23eb0da6"></a>

```c
typedef int(* psi5_stop_sync_t) (const struct device *dev, uint8_t channel)
```

相关声明：[psi5_stop_sync_t](#ga44a73fc30fb29d688d761b8d23eb0da6)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

停止 PSI5 同步时的回调 API，参数说明见 `psi5_stop_sync()`。

<a id="r_ga1ddcb06317f425a9d97defb1e4ccd677"></a>

```c
typedef int(* psi5_send_t) (const struct device *dev, uint8_t channel, const uint64_t data, k_timeout_t timeout, psi5_tx_callback_t callback, void *user_data)
```

相关声明：[psi5_send_t](#ga1ddcb06317f425a9d97defb1e4ccd677)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[psi5_tx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gaac8c99036369b14d639cfb82f3b9cd32)。

发送 PSI5 帧时的回调 API，参数说明见 `psi5_send()`。

<a id="r_gae9b98f6b16ed1364364e1d63f18bb479"></a>

```c
typedef int(* psi5_register_callback_t) (const struct device *dev, uint8_t channel, struct psi5_rx_callback_configs callback_configs)
```

相关声明：[psi5_register_callback_t](#gae9b98f6b16ed1364364e1d63f18bb479)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[psi5_rx_callback_configs](../peripheral_bus_storage_model_reference/P073_psi5_rx_callback_configs_结构体.md)。

添加接收回调时的回调 API，参数说明见 `psi5_register_callback()`。

## 98.3\_详细说明（Detailed Documentation）

<a id="gae9b98f6b16ed1364364e1d63f18bb479"></a>

### `psi5_register_callback_t`

```c
typedef int(* psi5_register_callback_t) (const struct device *dev, uint8_t channel, struct psi5_rx_callback_configs callback_configs)
```

```c
#include <zephyr/drivers/psi5/psi5.h>
```

添加接收回调时的回调 API，参数说明见 `psi5_register_callback()`。

<a id="ga1ddcb06317f425a9d97defb1e4ccd677"></a>

### `psi5_send_t`

```c
typedef int(* psi5_send_t) (const struct device *dev, uint8_t channel, const uint64_t data, k_timeout_t timeout, psi5_tx_callback_t callback, void *user_data)
```

```c
#include <zephyr/drivers/psi5/psi5.h>
```

发送 PSI5 帧时的回调 API，参数说明见 `psi5_send()`。

<a id="gaf86804dd3befe78878ed2d9b3bad9a49"></a>

### `psi5_start_sync_t`

```c
typedef int(* psi5_start_sync_t) (const struct device *dev, uint8_t channel)
```

```c
#include <zephyr/drivers/psi5/psi5.h>
```

启动 PSI5 同步时的回调 API，参数说明见 `psi5_start_sync()`。

<a id="ga44a73fc30fb29d688d761b8d23eb0da6"></a>

### `psi5_stop_sync_t`

```c
typedef int(* psi5_stop_sync_t) (const struct device *dev, uint8_t channel)
```

```c
#include <zephyr/drivers/psi5/psi5.h>
```

停止 PSI5 同步时的回调 API，参数说明见 `psi5_stop_sync()`。


## 98.4\_原页交叉引用（Cross References）

- [psi5_rx_callback_config](../peripheral_bus_storage_model_reference/P072_psi5_rx_callback_config_结构体.md)
- [psi5_rx_callback_configs](../peripheral_bus_storage_model_reference/P073_psi5_rx_callback_configs_结构体.md)
- [psi5_driver_api](../peripheral_bus_storage_model_reference/P070_psi5_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [psi5_start_sync()](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gabbc2a744edf1ab01e7bd9321054cf32b)
- [psi5_stop_sync()](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gacebce085be1e554e3faa7b69fd8da61f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [psi5_tx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#gaac8c99036369b14d639cfb82f3b9cd32)
- [psi5_send()](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga3a27606e2828206608a79ada7238466d)
- [psi5_register_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga37b0fcdecd4629c5f2657b1cc2e227b4)
- [zephyr/drivers/psi5/psi5.h](../peripheral_bus_storage_header_reference/P023_zephyr__drivers__psi5__psi5.h_头文件参考.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P097_Silicon Labs xG29 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P099_瑞萨（Renesas）RA.md)
