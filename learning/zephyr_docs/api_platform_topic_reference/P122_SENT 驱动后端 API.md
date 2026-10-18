---
id: learning.zephyr-docs.api-platform-topic-reference.page-122
title: SENT 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第122章\_SENT 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现单边沿半字节传输驱动（SENT Driver）所需的 API 类型定义（Type Definitions）、回调签名（Callback Signatures）及其他辅助工具（Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 122.1\_数据结构（Data Structures）

<a id="r_sent_5Frx_5Fcallback_5Fconfig"></a>

```c
struct sent_rx_callback_config
```

相关声明：[sent_rx_callback_config](../peripheral_bus_storage_model_reference/P089_sent_rx_callback_config_结构体.md)。

接收回调（RX Callback）的配置结构。

<a id="r_sent_5Frx_5Fcallback_5Fconfigs"></a>

```c
struct sent_rx_callback_configs
```

相关声明：[sent_rx_callback_configs](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md)。

接收回调（RX Callback）注册的组合配置结构。

<a id="r_sent_5Fdriver_5Fapi"></a>

```c
struct sent_driver_api
```

相关声明：[sent_driver_api](../peripheral_bus_storage_model_reference/P087_sent_driver_api_结构体.md)。

驱动操作（Driver Operations）：单边沿半字节传输（SENT）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 122.2\_类型定义（Typedefs）

<a id="r_ga4d4cc8870210e37bdac56d15f5979a32"></a>

```c
typedef int(* sent_start_listening_t) (const struct device *dev, uint8_t channel)
```

相关声明：[sent_start_listening_t](#ga4d4cc8870210e37bdac56d15f5979a32)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

开始接收帧时的回调 API，参数说明见 `sent_start_listening()`。

<a id="r_gad13f1bbd1eb6b6300780596b94bff6ac"></a>

```c
typedef int(* sent_stop_listening_t) (const struct device *dev, uint8_t channel)
```

相关声明：[sent_stop_listening_t](#gad13f1bbd1eb6b6300780596b94bff6ac)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

停止接收帧时的回调 API，参数说明见 `sent_stop_listening()`。

<a id="r_ga3b72c0fafbb177264d20df089ff5c38c"></a>

```c
typedef int(* sent_register_callback_t) (const struct device *dev, uint8_t channel, struct sent_rx_callback_configs callback_configs)
```

相关声明：[sent_register_callback_t](#ga3b72c0fafbb177264d20df089ff5c38c)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sent_rx_callback_configs](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md)。

添加接收回调时的回调 API，参数说明见 `sent_register_callback()`。

## 122.3\_详细说明（Detailed Documentation）

<a id="ga3b72c0fafbb177264d20df089ff5c38c"></a>

### `sent_register_callback_t`

```c
typedef int(* sent_register_callback_t) (const struct device *dev, uint8_t channel, struct sent_rx_callback_configs callback_configs)
```

```c
#include <zephyr/drivers/sent/sent.h>
```

添加接收回调时的回调 API，参数说明见 `sent_register_callback()`。

<a id="ga4d4cc8870210e37bdac56d15f5979a32"></a>

### `sent_start_listening_t`

```c
typedef int(* sent_start_listening_t) (const struct device *dev, uint8_t channel)
```

```c
#include <zephyr/drivers/sent/sent.h>
```

开始接收帧时的回调 API，参数说明见 `sent_start_listening()`。

<a id="gad13f1bbd1eb6b6300780596b94bff6ac"></a>

### `sent_stop_listening_t`

```c
typedef int(* sent_stop_listening_t) (const struct device *dev, uint8_t channel)
```

```c
#include <zephyr/drivers/sent/sent.h>
```

停止接收帧时的回调 API，参数说明见 `sent_stop_listening()`。


## 122.4\_原页交叉引用（Cross References）

- [sent_rx_callback_config](../peripheral_bus_storage_model_reference/P089_sent_rx_callback_config_结构体.md)
- [sent_rx_callback_configs](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md)
- [sent_driver_api](../peripheral_bus_storage_model_reference/P087_sent_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sent_start_listening()](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga227aafdbe8f93dbdb97f3969517e6c63)
- [sent_stop_listening()](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gae1eacde97297c97e27b67a7ae7e121cb)
- [sent_register_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga9deb810297f7d42159187bbb8dddb8d2)
- [zephyr/drivers/sent/sent.h](../peripheral_bus_storage_header_reference/P026_zephyr__drivers__sent__sent.h_头文件参考.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P121_MCUX 正交解码器（QDEC MCUX）.md) · [返回大纲](大纲.md) · [下一章](P123_ST87Mxx 常量（Constants）.md)
