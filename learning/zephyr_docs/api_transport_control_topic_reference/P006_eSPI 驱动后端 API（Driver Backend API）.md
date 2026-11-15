---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-6
title: eSPI 驱动后端 API（Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_eSPI 驱动后端 API（Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现 eSPI 驱动所需的 API 类型定义、回调签名（Callback Signatures）及其他辅助接口（Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_espi_5Fdriver_5Fapi"></a>

```c
struct espi_driver_api
```

相关声明：[espi_driver_api](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md)。

驱动操作（Driver Operations）：eSPI驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.2\_类型定义（Typedefs）

<a id="r_ga97336083a3ed3f561301fcf5762dc73c"></a>

```c
typedef int(* espi_api_config) (const struct device *dev, struct espi_cfg *cfg)
```

相关声明：[espi_api_config](#ga97336083a3ed3f561301fcf5762dc73c)、[device](../device_reference/P002_设备对象结构.md)、[espi_cfg](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md)。

配置 eSPI 设备的运行方式。

<a id="r_ga4712365e3a38d859fefbf0e9a6f32b07"></a>

```c
typedef bool(* espi_api_get_channel_status) (const struct device *dev, enum espi_channel ch)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[espi_api_get_channel_status](#ga4712365e3a38d859fefbf0e9a6f32b07)、[device](../device_reference/P002_设备对象结构.md)、[espi_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gafaa3f7d54503c901ab23bd79a7f8a755)。

查询逻辑通道（Logical channel）是否就绪。

<a id="r_ga3c3e6a70a04c14ec50fa0dcef4055f73"></a>

```c
typedef int(* espi_api_read_request) (const struct device *dev, struct espi_request_packet *req)
```

相关声明：[espi_api_read_request](#ga3c3e6a70a04c14ec50fa0dcef4055f73)、[device](../device_reference/P002_设备对象结构.md)、[espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)。

通过 eSPI 发送内存、I/O 或消息读取请求。

<a id="r_ga47ea19517406b64f074b4eee7a9d1923"></a>

```c
typedef int(* espi_api_write_request) (const struct device *dev, struct espi_request_packet *req)
```

相关声明：[espi_api_write_request](#ga47ea19517406b64f074b4eee7a9d1923)、[device](../device_reference/P002_设备对象结构.md)、[espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)。

通过 eSPI 发送内存、I/O 或消息写入请求。

<a id="r_ga04547d61ee4ed5d34fca3fb11ec0370f"></a>

```c
typedef int(* espi_api_lpc_read_request) (const struct device *dev, enum lpc_peripheral_opcode op, uint32_t *data)
```

相关声明：[espi_api_lpc_read_request](#ga04547d61ee4ed5d34fca3fb11ec0370f)、[device](../device_reference/P002_设备对象结构.md)、[lpc_peripheral_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gad00b6a22843e5df9c6d6945d0d82310e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取 LPC 外设寄存器。

<a id="r_gac7e3730c214b877772b24c4055ab997a"></a>

```c
typedef int(* espi_api_lpc_write_request) (const struct device *dev, enum lpc_peripheral_opcode op, uint32_t *data)
```

相关声明：[espi_api_lpc_write_request](#gac7e3730c214b877772b24c4055ab997a)、[device](../device_reference/P002_设备对象结构.md)、[lpc_peripheral_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gad00b6a22843e5df9c6d6945d0d82310e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

写入 LPC 外设寄存器。

<a id="r_ga838aefb5fbe399f6492803ceb391fa8c"></a>

```c
typedef int(* espi_api_send_vwire) (const struct device *dev, enum espi_vwire_signal vw, uint8_t level)
```

相关声明：[espi_api_send_vwire](#ga838aefb5fbe399f6492803ceb391fa8c)、[device](../device_reference/P002_设备对象结构.md)、[espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过 eSPI 发送虚拟线（Virtual wire）数据包。

<a id="r_ga806a0b3f3f4e629c5556f1399c4e29e2"></a>

```c
typedef int(* espi_api_receive_vwire) (const struct device *dev, enum espi_vwire_signal vw, uint8_t *level)
```

相关声明：[espi_api_receive_vwire](#ga806a0b3f3f4e629c5556f1399c4e29e2)、[device](../device_reference/P002_设备对象结构.md)、[espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取虚拟线信号的电平。

<a id="r_gae7497b9629a9444f94dae125fdf46005"></a>

```c
typedef int(* espi_api_send_oob) (const struct device *dev, struct espi_oob_packet *pckt)
```

相关声明：[espi_api_send_oob](#gae7497b9629a9444f94dae125fdf46005)、[device](../device_reference/P002_设备对象结构.md)、[espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)。

通过 eSPI 发送 SMBus 事务的带外（Out-of-band，OOB）数据包。

<a id="r_ga79255a516e48256d8381d0b32e5ae345"></a>

```c
typedef int(* espi_api_receive_oob) (const struct device *dev, struct espi_oob_packet *pckt)
```

相关声明：[espi_api_receive_oob](#ga79255a516e48256d8381d0b32e5ae345)、[device](../device_reference/P002_设备对象结构.md)、[espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)。

从 eSPI 接收 SMBus 事务的带外数据包。

<a id="r_ga6bb1bb8af96c58dc0d9ad041d95cd397"></a>

```c
typedef int(* espi_api_flash_read) (const struct device *dev, struct espi_flash_packet *pckt)
```

相关声明：[espi_api_flash_read](#ga6bb1bb8af96c58dc0d9ad041d95cd397)、[device](../device_reference/P002_设备对象结构.md)、[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

发送对经 eSPI 共享的 Flash 区域的读取请求。

<a id="r_ga1a8715b387a037dddacc92424fe0ba6f"></a>

```c
typedef int(* espi_api_flash_write) (const struct device *dev, struct espi_flash_packet *pckt)
```

相关声明：[espi_api_flash_write](#ga1a8715b387a037dddacc92424fe0ba6f)、[device](../device_reference/P002_设备对象结构.md)、[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

发送对经 eSPI 共享的 Flash 区域的写入请求。

<a id="r_ga422abe38a4d2cce441d5165192adc982"></a>

```c
typedef int(* espi_api_flash_erase) (const struct device *dev, struct espi_flash_packet *pckt)
```

相关声明：[espi_api_flash_erase](#ga422abe38a4d2cce441d5165192adc982)、[device](../device_reference/P002_设备对象结构.md)、[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

发送对经 eSPI 共享的 Flash 区域的擦除请求。

<a id="r_gab0313b00d884426800395ec5a907f744"></a>

```c
typedef int(* espi_api_manage_callback) (const struct device *dev, struct espi_callback *callback, bool set)
```

相关声明：[espi_api_manage_callback](#gab0313b00d884426800395ec5a907f744)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

添加或移除应用程序回调。

<a id="r_ga7d497e1f4573f54f49202b67cb5cbe5c"></a>

```c
typedef int(* espi_api_interrupt_configure) (const struct device *dev, uint32_t espi_interrupt_flags, uint32_t espi_interrupt_vendor)
```

相关声明：[espi_api_interrupt_configure](#ga7d497e1f4573f54f49202b67cb5cbe5c)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[espi_interrupt_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga4e35c754c720f262805689a94985272c)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

控制 eSPI 中断。

## 6.3\_详细说明（Detailed Documentation）

<a id="ga97336083a3ed3f561301fcf5762dc73c"></a>

### `espi_api_config`

```c
typedef int(* espi_api_config) (const struct device *dev, struct espi_cfg *cfg)
```

```c
#include <zephyr/drivers/espi.h>
```

配置 eSPI 设备的运行方式。

参数说明（Argument Description）参见 `espi_config()`。

<a id="ga422abe38a4d2cce441d5165192adc982"></a>

### `espi_api_flash_erase`

```c
typedef int(* espi_api_flash_erase) (const struct device *dev, struct espi_flash_packet *pckt)
```

```c
#include <zephyr/drivers/espi.h>
```

发送对经 eSPI 共享的 Flash 区域的擦除请求。

参数说明（Argument Description）参见 `espi_flash_erase()`。

<a id="ga6bb1bb8af96c58dc0d9ad041d95cd397"></a>

### `espi_api_flash_read`

```c
typedef int(* espi_api_flash_read) (const struct device *dev, struct espi_flash_packet *pckt)
```

```c
#include <zephyr/drivers/espi.h>
```

发送对经 eSPI 共享的 Flash 区域的读取请求。

参数说明（Argument Description）参见 `espi_read_flash()`。

<a id="ga1a8715b387a037dddacc92424fe0ba6f"></a>

### `espi_api_flash_write`

```c
typedef int(* espi_api_flash_write) (const struct device *dev, struct espi_flash_packet *pckt)
```

```c
#include <zephyr/drivers/espi.h>
```

发送对经 eSPI 共享的 Flash 区域的写入请求。

参数说明（Argument Description）参见 `espi_write_flash()`。

<a id="ga4712365e3a38d859fefbf0e9a6f32b07"></a>

### `espi_api_get_channel_status`

```c
typedef bool(* espi_api_get_channel_status) (const struct device *dev, enum espi_channel ch)
```

```c
#include <zephyr/drivers/espi.h>
```

查询逻辑通道（Logical channel）是否就绪。

参数说明（Argument Description）参见 `espi_get_channel_status()`。

<a id="ga7d497e1f4573f54f49202b67cb5cbe5c"></a>

### `espi_api_interrupt_configure`

```c
typedef int(* espi_api_interrupt_configure) (const struct device *dev, uint32_t espi_interrupt_flags, uint32_t espi_interrupt_vendor)
```

```c
#include <zephyr/drivers/espi.h>
```

控制 eSPI 中断。

参数说明（Argument Description）参见 `espi_interrupt_config()`。

<a id="ga04547d61ee4ed5d34fca3fb11ec0370f"></a>

### `espi_api_lpc_read_request`

```c
typedef int(* espi_api_lpc_read_request) (const struct device *dev, enum lpc_peripheral_opcode op, uint32_t *data)
```

```c
#include <zephyr/drivers/espi.h>
```

读取 LPC 外设寄存器。

参数说明（Argument Description）参见 `espi_read_lpc_request()`。

<a id="gac7e3730c214b877772b24c4055ab997a"></a>

### `espi_api_lpc_write_request`

```c
typedef int(* espi_api_lpc_write_request) (const struct device *dev, enum lpc_peripheral_opcode op, uint32_t *data)
```

```c
#include <zephyr/drivers/espi.h>
```

写入 LPC 外设寄存器。

参数说明（Argument Description）参见 `espi_write_lpc_request()`。

<a id="gab0313b00d884426800395ec5a907f744"></a>

### `espi_api_manage_callback`

```c
typedef int(* espi_api_manage_callback) (const struct device *dev, struct espi_callback *callback, bool set)
```

```c
#include <zephyr/drivers/espi.h>
```

添加或移除应用程序回调。

参数说明（Argument Description）参见 `espi_add_callback()` 和  `espi_remove_callback()`。

<a id="ga3c3e6a70a04c14ec50fa0dcef4055f73"></a>

### `espi_api_read_request`

```c
typedef int(* espi_api_read_request) (const struct device *dev, struct espi_request_packet *req)
```

```c
#include <zephyr/drivers/espi.h>
```

通过 eSPI 发送内存、I/O 或消息读取请求。

参数说明（Argument Description）参见 `espi_read_request()`。

<a id="ga79255a516e48256d8381d0b32e5ae345"></a>

### `espi_api_receive_oob`

```c
typedef int(* espi_api_receive_oob) (const struct device *dev, struct espi_oob_packet *pckt)
```

```c
#include <zephyr/drivers/espi.h>
```

从 eSPI 接收 SMBus 事务的带外数据包。

参数说明（Argument Description）参见 `espi_receive_oob()`。

<a id="ga806a0b3f3f4e629c5556f1399c4e29e2"></a>

### `espi_api_receive_vwire`

```c
typedef int(* espi_api_receive_vwire) (const struct device *dev, enum espi_vwire_signal vw, uint8_t *level)
```

```c
#include <zephyr/drivers/espi.h>
```

获取虚拟线信号的电平。

参数说明（Argument Description）参见 `espi_receive_vwire()`。

<a id="gae7497b9629a9444f94dae125fdf46005"></a>

### `espi_api_send_oob`

```c
typedef int(* espi_api_send_oob) (const struct device *dev, struct espi_oob_packet *pckt)
```

```c
#include <zephyr/drivers/espi.h>
```

通过 eSPI 发送 SMBus 事务的带外（Out-of-band，OOB）数据包。

参数说明（Argument Description）参见 `espi_send_oob()`。

<a id="ga838aefb5fbe399f6492803ceb391fa8c"></a>

### `espi_api_send_vwire`

```c
typedef int(* espi_api_send_vwire) (const struct device *dev, enum espi_vwire_signal vw, uint8_t level)
```

```c
#include <zephyr/drivers/espi.h>
```

通过 eSPI 发送虚拟线（Virtual wire）数据包。

参数说明（Argument Description）参见 `espi_send_vwire()`。

<a id="ga47ea19517406b64f074b4eee7a9d1923"></a>

### `espi_api_write_request`

```c
typedef int(* espi_api_write_request) (const struct device *dev, struct espi_request_packet *req)
```

```c
#include <zephyr/drivers/espi.h>
```

通过 eSPI 发送内存、I/O 或消息写入请求。

参数说明（Argument Description）参见 `espi_write_request()`。


## 6.4\_原页交叉引用（Cross References）

- [espi_driver_api](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [espi_cfg](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [espi_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gafaa3f7d54503c901ab23bd79a7f8a755)
- [espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)
- [lpc_peripheral_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gad00b6a22843e5df9c6d6945d0d82310e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)
- [espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)
- [espi_interrupt_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga4e35c754c720f262805689a94985272c)
- [zephyr/drivers/espi.h](../peripheral_bus_storage_header_reference/P004_zephyr__drivers__espi.h_头文件参考.md)
- [espi_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga7227c53d384eb0dc666361261f069f68)
- [espi_flash_erase()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab42be7c76c4523cea96365aa77fd18be)
- [espi_read_flash()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga0a97d11167367342283bfe6b6d66726e)
- [espi_write_flash()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab02d46fd690e33875cc1b2433c976891)
- [espi_get_channel_status()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga869551e20fc2c3be4311c21c3c53999d)
- [espi_interrupt_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga1cd0afc52d533414b5bbc684cef8b9af)
- [espi_read_lpc_request()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaeaae20afa90d9d825d80997369f31465)
- [espi_write_lpc_request()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga880b6b04824f9f0deea10e8018573b88)
- [espi_add_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gabf5f0ea01ec8ed5345b2e119181c2313)
- [espi_remove_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga7f04f98ea6a4671b821cf6ddf6bbf2a6)
- [espi_read_request()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga112f7554ba614c8e5f239b1319b4a763)
- [espi_receive_oob()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga4b8f4fbf66a2b2ae394e00b16500f70d)
- [espi_receive_vwire()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaa8bb48b5592c4b49d27c9b8a42432410)
- [espi_send_oob()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga2557cfc7a38f669d14e9826e3fb0fdee)
- [espi_send_vwire()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gacab2b3bff7d940e71ee1c2a9fdedf782)
- [espi_write_request()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga143ed88b1f220f9582c809165fd983fd)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P005_DMA的SF32LB专用功能（SF32LB Specifics）。.md) · [返回大纲](大纲.md) · [下一章](P007_MULTIRSTCR 复位控制（Reset Control）.md)
