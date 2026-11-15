---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-26
title: zephyr__drivers__sent__sent.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sent_2sent_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_zephyr\_\_drivers\_\_sent\_\_sent.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sent_2sent_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单边沿半字节传输（Single Edge Nibble Transmission，SENT）的驱动API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/sent.h>
```

查看此文件的源码。

单边沿半字节传输（Single Edge Nibble Transmission，SENT）的驱动API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 26.1\_数据结构（Data Structures）

<a id="r_sent_5Fframe"></a>

```c
struct sent_frame
```

相关声明：[sent_frame](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md)。

单边沿半字节传输（SENT）的帧结构。

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 26.2\_宏定义（Macros）

<a id="r_ga19bb6e9149dfb7af97ca90289e33bdac"></a>

```c
#define SENT_MAX_DATA_NIBBLES 8
```

相关声明：[SENT_MAX_DATA_NIBBLES](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga19bb6e9149dfb7af97ca90289e33bdac)。

数据半字节（Nibble）的最大数量。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 26.3\_类型定义（Typedefs）

<a id="r_ga47d05656177dae0a388e1155be82494f"></a>

```c
typedef void(* sent_rx_frame_callback_t) (const struct device *dev, uint8_t channel, uint32_t num_frame, void *user_data)
```

相关声明：[sent_rx_frame_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga47d05656177dae0a388e1155be82494f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

定义用于接收帧的应用程序回调处理函数签名。

<a id="r_ga4d4cc8870210e37bdac56d15f5979a32"></a>

```c
typedef int(* sent_start_listening_t) (const struct device *dev, uint8_t channel)
```

相关声明：[sent_start_listening_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#ga4d4cc8870210e37bdac56d15f5979a32)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

开始接收帧时的回调 API，参数说明见 `sent_start_listening()`。

<a id="r_gad13f1bbd1eb6b6300780596b94bff6ac"></a>

```c
typedef int(* sent_stop_listening_t) (const struct device *dev, uint8_t channel)
```

相关声明：[sent_stop_listening_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#gad13f1bbd1eb6b6300780596b94bff6ac)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

停止接收帧时的回调 API，参数说明见 `sent_stop_listening()`。

<a id="r_ga3b72c0fafbb177264d20df089ff5c38c"></a>

```c
typedef int(* sent_register_callback_t) (const struct device *dev, uint8_t channel, struct sent_rx_callback_configs callback_configs)
```

相关声明：[sent_register_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#ga3b72c0fafbb177264d20df089ff5c38c)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sent_rx_callback_configs](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md)。

添加接收回调时的回调 API，参数说明见 `sent_register_callback()`。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 26.4\_枚举（Enumerations）

<a id="r_ga069232b79943be845df411539ef04993"></a>

```c
enum sent_frame_type { SENT_SHORT_SERIAL_FRAME , SENT_ENHANCED_SERIAL_FRAME_4_BIT_ID , SENT_ENHANCED_SERIAL_FRAME_8_BIT_ID , SENT_FAST_FRAME }
```

相关声明：[sent_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga069232b79943be845df411539ef04993)、[SENT_SHORT_SERIAL_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gga069232b79943be845df411539ef04993adbbb93e3efeeb6d2330bc4c9cb0ae4d5)、[SENT_ENHANCED_SERIAL_FRAME_4_BIT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gga069232b79943be845df411539ef04993a44b400409bb8a00ba23022490a6e6e73)、[SENT_ENHANCED_SERIAL_FRAME_8_BIT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gga069232b79943be845df411539ef04993aeef9ade678a8b59d7a8e0d0154f9b137)、[SENT_FAST_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gga069232b79943be845df411539ef04993afb15bcda86b0faef89c8dc1662f060a1)。

SENT 帧类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 26.5\_函数（Functions）

<a id="r_ga227aafdbe8f93dbdb97f3969517e6c63"></a>

```c
int sent_start_listening (const struct device *dev, uint8_t channel)
```

相关声明：[sent_start_listening](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga227aafdbe8f93dbdb97f3969517e6c63)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启用指定通道，使其开始从总线接收。

<a id="r_gae1eacde97297c97e27b67a7ae7e121cb"></a>

```c
int sent_stop_listening (const struct device *dev, uint8_t channel)
```

相关声明：[sent_stop_listening](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gae1eacde97297c97e27b67a7ae7e121cb)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

禁用指定通道，使其停止从总线接收。

<a id="r_ga9deb810297f7d42159187bbb8dddb8d2"></a>

```c
int sent_register_callback (const struct device *dev, uint8_t channel, struct sent_rx_callback_configs callback_configs)
```

相关声明：[sent_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga9deb810297f7d42159187bbb8dddb8d2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sent_rx_callback_configs](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md)。

添加回调函数，以处理指定通道接收到的消息。


## 26.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sent_2sent_8h_source.html)
- [sent_frame](../peripheral_bus_storage_model_reference/P088_sent_frame_结构体.md)
- [sent_rx_callback_config](../peripheral_bus_storage_model_reference/P089_sent_rx_callback_config_结构体.md)
- [sent_rx_callback_configs](../peripheral_bus_storage_model_reference/P090_sent_rx_callback_configs_结构体.md)
- [sent_driver_api](../peripheral_bus_storage_model_reference/P087_sent_driver_api_结构体.md)
- [SENT_MAX_DATA_NIBBLES](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga19bb6e9149dfb7af97ca90289e33bdac)
- [sent_rx_frame_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga47d05656177dae0a388e1155be82494f)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sent_start_listening_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#ga4d4cc8870210e37bdac56d15f5979a32)
- [sent_start_listening()](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga227aafdbe8f93dbdb97f3969517e6c63)
- [sent_stop_listening_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#gad13f1bbd1eb6b6300780596b94bff6ac)
- [sent_stop_listening()](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gae1eacde97297c97e27b67a7ae7e121cb)
- [sent_register_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#ga3b72c0fafbb177264d20df089ff5c38c)
- [sent_register_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga9deb810297f7d42159187bbb8dddb8d2)
- [sent_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga069232b79943be845df411539ef04993)
- [SENT_SHORT_SERIAL_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gga069232b79943be845df411539ef04993adbbb93e3efeeb6d2330bc4c9cb0ae4d5)
- [SENT_ENHANCED_SERIAL_FRAME_4_BIT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gga069232b79943be845df411539ef04993a44b400409bb8a00ba23022490a6e6e73)
- [SENT_ENHANCED_SERIAL_FRAME_8_BIT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gga069232b79943be845df411539ef04993aeef9ade678a8b59d7a8e0d0154f9b137)
- [SENT_FAST_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#gga069232b79943be845df411539ef04993afb15bcda86b0faef89c8dc1662f060a1)

<a id="header-details"></a>

---

[上一章](P025_zephyr__drivers__sdhc.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P027_zephyr__drivers__smbus.h_头文件参考.md)
