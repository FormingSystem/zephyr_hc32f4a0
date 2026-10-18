---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-4
title: zephyr__drivers__espi.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/espi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_drivers\_\_espi.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/espi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/sys/slist.h>
#include <zephyr/syscalls/espi.h>
```

查看此文件的源码。

增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_espi_5Fevt_5Fdata_5Fkbc"></a>

```c
struct espi_evt_data_kbc
```

相关声明：[espi_evt_data_kbc](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md)。

键盘控制器（KBC）事件的数据格式。

<a id="r_espi_5Fevt_5Fdata_5Facpi"></a>

```c
struct espi_evt_data_acpi
```

相关声明：[espi_evt_data_acpi](../peripheral_bus_storage_model_reference/P009_espi_evt_data_acpi_结构体.md)。

高级配置与电源接口（ACPI）事件的数据格式。

<a id="r_espi_5Fevt_5Fdata_5Fpvt"></a>

```c
struct espi_evt_data_pvt
```

相关声明：[espi_evt_data_pvt](../peripheral_bus_storage_model_reference/P011_espi_evt_data_pvt_结构体.md)。

私有通道（Private Channel，PVT）事件的数据格式。

<a id="r_espi_5Fevent"></a>

```c
struct espi_event
```

相关声明：[espi_event](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md)。

增强型串行外设接口（eSPI）事件。

<a id="r_espi_5Fcfg"></a>

```c
struct espi_cfg
```

相关声明：[espi_cfg](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md)。

增强型串行外设接口（eSPI）的总线配置参数。

<a id="r_espi_5Frequest_5Fpacket"></a>

```c
struct espi_request_packet
```

相关声明：[espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)。

eSPI外设请求（Peripheral Request）数据包。

<a id="r_espi_5Foob_5Fpacket"></a>

```c
struct espi_oob_packet
```

相关声明：[espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)。

eSPI带外事务（Out-of-Band Transaction）的数据包格式。

<a id="r_espi_5Fflash_5Fpacket"></a>

```c
struct espi_flash_packet
```

相关声明：[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

eSPI闪存事务（Flash Transaction）的数据包格式。

<a id="r_espi_5Fdriver_5Fapi"></a>

```c
struct espi_driver_api
```

相关声明：[espi_driver_api](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md)。

驱动操作（Driver Operations）：eSPI驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga8da8ac3b45044323fdb24f1361adaac7"></a>

```c
#define ESPI_INT_ALL_MASK
```

相关声明：[ESPI_INT_ALL_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga8da8ac3b45044323fdb24f1361adaac7)。

选择所有 eSPI 通用中断。

<a id="r_gadeb45b8838f4d1fbf05095c36ca3faba"></a>

```c
#define ESPI_INT_BUS_ONLY_MASK
```

相关声明：[ESPI_INT_BUS_ONLY_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gadeb45b8838f4d1fbf05095c36ca3faba)。

仅选择 eSPI 总线硬件中断。

<a id="r_ga24b468de0013cd9cf9d814faff13b94e"></a>

```c
#define ESPI_INT_NONE_MASK 0U
```

相关声明：[ESPI_INT_NONE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga24b468de0013cd9cf9d814faff13b94e)。

禁用所有 eSPI 硬件事件。

<a id="r_gaa0807c908666cdcbb3a85f310bfbfccc"></a>

```c
#define HOST_KBC_EVT_IBF BIT(0)
```

相关声明：[HOST_KBC_EVT_IBF](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaa0807c908666cdcbb3a85f310bfbfccc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

KBC 8042 事件：输入缓冲区满（Input Buffer Full）。

<a id="r_ga807bb75027f24e040cd28eba4bc1002c"></a>

```c
#define HOST_KBC_EVT_OBE BIT(1)
```

相关声明：[HOST_KBC_EVT_OBE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga807bb75027f24e040cd28eba4bc1002c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

KBC 8042 事件：输出缓冲区空（Output Buffer Empty）。

<a id="r_gaa45ee9beafbda94f8f9ad799e78089cd"></a>

```c
#define ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_DATA 0
```

相关声明：[ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaa45ee9beafbda94f8f9ad799e78089cd)。

ACPI 事件：输入缓冲区满。

<a id="r_ga01e61256f8be5e24d131c68d81ed8916"></a>

```c
#define ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_CMD 1U
```

相关声明：[ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga01e61256f8be5e24d131c68d81ed8916)。

ACPI 事件：输入缓冲区满。

<a id="r_ga6807d29b11134b76b14c8887053cbce1"></a>

```c
#define ESPI_EVENT_DATA_ACPI_TYPE_HOST_RD_EC_TO_HOST 2U
```

相关声明：[ESPI_EVENT_DATA_ACPI_TYPE_HOST_RD_EC_TO_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga6807d29b11134b76b14c8887053cbce1)。

ACPI 事件：输出缓冲区空。主机已读取嵌入式控制器（EC）写入 EC-to-Host 寄存器的数据。

<a id="define-members-0"></a>

### USB-C 端口过流信号别名（Over current signal aliases）

<a id="r_gae4855b6cf8049de8aa6d67763f1be8c3"></a>

```c
#define ESPI_VWIRE_SIGNAL_OCB_0 ESPI_VWIRE_SIGNAL_TARGET_GPIO_0
```

相关声明：[ESPI_VWIRE_SIGNAL_OCB_0](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gae4855b6cf8049de8aa6d67763f1be8c3)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_0](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2)。

USB-C 端口 0 的过流信号（Over current signal）。

<a id="r_ga2ed490939e0249ff8196f77a74967727"></a>

```c
#define ESPI_VWIRE_SIGNAL_OCB_1 ESPI_VWIRE_SIGNAL_TARGET_GPIO_1
```

相关声明：[ESPI_VWIRE_SIGNAL_OCB_1](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga2ed490939e0249ff8196f77a74967727)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_1](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de)。

USB-C 端口 1 的过流信号。

<a id="r_gaf35d03bc041dc6baefe35b74c163d73b"></a>

```c
#define ESPI_VWIRE_SIGNAL_OCB_2 ESPI_VWIRE_SIGNAL_TARGET_GPIO_2
```

相关声明：[ESPI_VWIRE_SIGNAL_OCB_2](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaf35d03bc041dc6baefe35b74c163d73b)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_2](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b)。

USB-C 端口 2 的过流信号。

<a id="r_gaeae1765d801cd298c27404c173a94707"></a>

```c
#define ESPI_VWIRE_SIGNAL_OCB_3 ESPI_VWIRE_SIGNAL_TARGET_GPIO_3
```

相关声明：[ESPI_VWIRE_SIGNAL_OCB_3](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaeae1765d801cd298c27404c173a94707)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_3](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a)。

USB-C 端口 3 的过流信号。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.3\_类型定义（Typedefs）

<a id="r_ga9d848c7e367cf277230f365f73c15c46"></a>

```c
typedef void(* espi_callback_handler_t) (const struct device *dev, struct espi_callback *cb, struct espi_event espi_evt)
```

相关声明：[espi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga9d848c7e367cf277230f365f73c15c46)、[device](../device_reference/P002_设备对象结构.md)、[espi_event](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md)。

定义应用程序回调处理函数的签名（Function Signature）。

<a id="r_ga97336083a3ed3f561301fcf5762dc73c"></a>

```c
typedef int(* espi_api_config) (const struct device *dev, struct espi_cfg *cfg)
```

相关声明：[espi_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga97336083a3ed3f561301fcf5762dc73c)、[device](../device_reference/P002_设备对象结构.md)、[espi_cfg](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md)。

配置 eSPI 设备的运行方式。

<a id="r_ga4712365e3a38d859fefbf0e9a6f32b07"></a>

```c
typedef bool(* espi_api_get_channel_status) (const struct device *dev, enum espi_channel ch)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[espi_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga4712365e3a38d859fefbf0e9a6f32b07)、[device](../device_reference/P002_设备对象结构.md)、[espi_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gafaa3f7d54503c901ab23bd79a7f8a755)。

查询逻辑通道（Logical channel）是否就绪。

<a id="r_ga3c3e6a70a04c14ec50fa0dcef4055f73"></a>

```c
typedef int(* espi_api_read_request) (const struct device *dev, struct espi_request_packet *req)
```

相关声明：[espi_api_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga3c3e6a70a04c14ec50fa0dcef4055f73)、[device](../device_reference/P002_设备对象结构.md)、[espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)。

通过 eSPI 发送内存、I/O 或消息读取请求。

<a id="r_ga47ea19517406b64f074b4eee7a9d1923"></a>

```c
typedef int(* espi_api_write_request) (const struct device *dev, struct espi_request_packet *req)
```

相关声明：[espi_api_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga47ea19517406b64f074b4eee7a9d1923)、[device](../device_reference/P002_设备对象结构.md)、[espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)。

通过 eSPI 发送内存、I/O 或消息写入请求。

<a id="r_ga04547d61ee4ed5d34fca3fb11ec0370f"></a>

```c
typedef int(* espi_api_lpc_read_request) (const struct device *dev, enum lpc_peripheral_opcode op, uint32_t *data)
```

相关声明：[espi_api_lpc_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga04547d61ee4ed5d34fca3fb11ec0370f)、[device](../device_reference/P002_设备对象结构.md)、[lpc_peripheral_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gad00b6a22843e5df9c6d6945d0d82310e)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

读取 LPC 外设寄存器。

<a id="r_gac7e3730c214b877772b24c4055ab997a"></a>

```c
typedef int(* espi_api_lpc_write_request) (const struct device *dev, enum lpc_peripheral_opcode op, uint32_t *data)
```

相关声明：[espi_api_lpc_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gac7e3730c214b877772b24c4055ab997a)、[device](../device_reference/P002_设备对象结构.md)、[lpc_peripheral_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gad00b6a22843e5df9c6d6945d0d82310e)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

写入 LPC 外设寄存器。

<a id="r_ga838aefb5fbe399f6492803ceb391fa8c"></a>

```c
typedef int(* espi_api_send_vwire) (const struct device *dev, enum espi_vwire_signal vw, uint8_t level)
```

相关声明：[espi_api_send_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga838aefb5fbe399f6492803ceb391fa8c)、[device](../device_reference/P002_设备对象结构.md)、[espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过 eSPI 发送虚拟线（Virtual wire）数据包。

<a id="r_ga806a0b3f3f4e629c5556f1399c4e29e2"></a>

```c
typedef int(* espi_api_receive_vwire) (const struct device *dev, enum espi_vwire_signal vw, uint8_t *level)
```

相关声明：[espi_api_receive_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga806a0b3f3f4e629c5556f1399c4e29e2)、[device](../device_reference/P002_设备对象结构.md)、[espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取虚拟线信号的电平。

<a id="r_gae7497b9629a9444f94dae125fdf46005"></a>

```c
typedef int(* espi_api_send_oob) (const struct device *dev, struct espi_oob_packet *pckt)
```

相关声明：[espi_api_send_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gae7497b9629a9444f94dae125fdf46005)、[device](../device_reference/P002_设备对象结构.md)、[espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)。

通过 eSPI 发送 SMBus 事务的带外（Out-of-band，OOB）数据包。

<a id="r_ga79255a516e48256d8381d0b32e5ae345"></a>

```c
typedef int(* espi_api_receive_oob) (const struct device *dev, struct espi_oob_packet *pckt)
```

相关声明：[espi_api_receive_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga79255a516e48256d8381d0b32e5ae345)、[device](../device_reference/P002_设备对象结构.md)、[espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)。

从 eSPI 接收 SMBus 事务的带外数据包。

<a id="r_ga6bb1bb8af96c58dc0d9ad041d95cd397"></a>

```c
typedef int(* espi_api_flash_read) (const struct device *dev, struct espi_flash_packet *pckt)
```

相关声明：[espi_api_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga6bb1bb8af96c58dc0d9ad041d95cd397)、[device](../device_reference/P002_设备对象结构.md)、[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

发送对经 eSPI 共享的 Flash 区域的读取请求。

<a id="r_ga1a8715b387a037dddacc92424fe0ba6f"></a>

```c
typedef int(* espi_api_flash_write) (const struct device *dev, struct espi_flash_packet *pckt)
```

相关声明：[espi_api_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga1a8715b387a037dddacc92424fe0ba6f)、[device](../device_reference/P002_设备对象结构.md)、[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

发送对经 eSPI 共享的 Flash 区域的写入请求。

<a id="r_ga422abe38a4d2cce441d5165192adc982"></a>

```c
typedef int(* espi_api_flash_erase) (const struct device *dev, struct espi_flash_packet *pckt)
```

相关声明：[espi_api_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga422abe38a4d2cce441d5165192adc982)、[device](../device_reference/P002_设备对象结构.md)、[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

发送对经 eSPI 共享的 Flash 区域的擦除请求。

<a id="r_gab0313b00d884426800395ec5a907f744"></a>

```c
typedef int(* espi_api_manage_callback) (const struct device *dev, struct espi_callback *callback, bool set)
```

相关声明：[espi_api_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gab0313b00d884426800395ec5a907f744)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

添加或移除应用程序回调。

<a id="r_ga7d497e1f4573f54f49202b67cb5cbe5c"></a>

```c
typedef int(* espi_api_interrupt_configure) (const struct device *dev, uint32_t espi_interrupt_flags, uint32_t espi_interrupt_vendor)
```

相关声明：[espi_api_interrupt_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga7d497e1f4573f54f49202b67cb5cbe5c)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[espi_interrupt_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga4e35c754c720f262805689a94985272c)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

控制 eSPI 中断。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.4\_枚举（Enumerations）

<a id="r_ga0d7c61f1f4ec611d0c8a67ba73e2b4f0"></a>

```c
enum espi_io_mode { ESPI_IO_MODE_SINGLE_LINE = BIT(0) , ESPI_IO_MODE_DUAL_LINES = BIT(1) , ESPI_IO_MODE_QUAD_LINES = BIT(2) }
```

相关声明：[espi_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0)、[ESPI_IO_MODE_SINGLE_LINE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a9f47188ebd9bb4cb6e426d0bc0b6595c)、[ESPI_IO_MODE_DUAL_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0af766582d28d16af7c5aff6372e4ee243)、[ESPI_IO_MODE_QUAD_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a87e70bb0f5c4f6a3a21ca1bcfa4540fc)。

eSPI I/O 模式能力（Capabilities）。

<a id="r_gafaa3f7d54503c901ab23bd79a7f8a755"></a>

```c
enum espi_channel { ESPI_CHANNEL_PERIPHERAL = BIT(0) , ESPI_CHANNEL_VWIRE = BIT(1) , ESPI_CHANNEL_OOB = BIT(2) , ESPI_CHANNEL_FLASH = BIT(3) }
```

相关声明：[espi_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gafaa3f7d54503c901ab23bd79a7f8a755)、[ESPI_CHANNEL_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggafaa3f7d54503c901ab23bd79a7f8a755a32f636bbad2618a6b1554656d3b53206)、[ESPI_CHANNEL_VWIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggafaa3f7d54503c901ab23bd79a7f8a755ac2e84a127870ff50359cf96528c9a7c6)、[ESPI_CHANNEL_OOB](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggafaa3f7d54503c901ab23bd79a7f8a755a0ccb80544cbda501cc90ea0c3b868e54)、[ESPI_CHANNEL_FLASH](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggafaa3f7d54503c901ab23bd79a7f8a755a5616bf2bf49a8c457fcc2f27d9fe0518)。

eSPI 通道（Channel）。

<a id="r_ga36ac3fbf9813f78bad90f047e1eb1128"></a>

```c
enum espi_bus_event { ESPI_BUS_RESET = BIT(0) , ESPI_BUS_EVENT_CHANNEL_READY = BIT(1) , ESPI_BUS_EVENT_VWIRE_RECEIVED = BIT(2) , ESPI_BUS_EVENT_OOB_RECEIVED = BIT(3) , ESPI_BUS_PERIPHERAL_NOTIFICATION = BIT(4) , ESPI_BUS_TAF_NOTIFICATION = BIT(5) }
```

相关声明：[espi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga36ac3fbf9813f78bad90f047e1eb1128)、[ESPI_BUS_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128ae6d4d43eded0d8a368c90ea653a60956)、[ESPI_BUS_EVENT_CHANNEL_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128a996aee0a8f8ba0cead11cea0d39d2973)、[ESPI_BUS_EVENT_VWIRE_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128aa09f7dcd4b2d3addfaddbad5b8f2e5a2)、[ESPI_BUS_EVENT_OOB_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128a3b5e529d1d0ba11c59172ab01c30e203)、[ESPI_BUS_PERIPHERAL_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128a9ac837699f302bd10332814c7014adea)、[ESPI_BUS_TAF_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128a9f2a9cfda3b803687a0992a9d41f0014)。

eSPI 总线事件。

<a id="r_gac55098842dd9d181144ac4b4122a610e"></a>

```c
enum espi_pc_event { ESPI_PC_EVT_BUS_CHANNEL_READY = BIT(0) , ESPI_PC_EVT_BUS_MASTER_ENABLE = BIT(1) }
```

相关声明：[espi_pc_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gac55098842dd9d181144ac4b4122a610e)、[ESPI_PC_EVT_BUS_CHANNEL_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggac55098842dd9d181144ac4b4122a610ea68ecb52b04ffddcc93fbcc77d3643687)、[ESPI_PC_EVT_BUS_MASTER_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggac55098842dd9d181144ac4b4122a610ea0e245cbeef479218d4e6c9bec57e40d1)。

eSPI 外设通道事件（Peripheral channel events）。

<a id="r_ga2629a5518a94f031419eeccd05f07373"></a>

```c
enum espi_virtual_peripheral { ESPI_PERIPHERAL_UART , ESPI_PERIPHERAL_8042_KBC , ESPI_PERIPHERAL_HOST_IO , ESPI_PERIPHERAL_DEBUG_PORT80 , ESPI_PERIPHERAL_HOST_IO_PVT , ESPI_PERIPHERAL_HOST_IO_PVT2 , ESPI_PERIPHERAL_HOST_IO_PVT3 , ESPI_PERIPHERAL_EC_HOST_CMD }
```

相关声明：[espi_virtual_peripheral](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga2629a5518a94f031419eeccd05f07373)、[ESPI_PERIPHERAL_UART](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373a24478711945fd5258d8ca86bbb79b867)、[ESPI_PERIPHERAL_8042_KBC](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373aaea75bb5ab8a5ff31dd6b8787f44df30)、[ESPI_PERIPHERAL_HOST_IO](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373a8948a6f18bfbe87859a529d5f6e669b8)、[ESPI_PERIPHERAL_DEBUG_PORT80](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373af51b7171cf6085fa7946333ff32fe2f0)、[ESPI_PERIPHERAL_HOST_IO_PVT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373aa217b4786d7b8bacbaa4ec740550e71e)、[ESPI_PERIPHERAL_HOST_IO_PVT2](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373a0e6e9dc1a7975cd80991090a78ea6231)、[ESPI_PERIPHERAL_HOST_IO_PVT3](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373a8d8c64c49e8c7a75cb3a665e63a6f5ce)、[ESPI_PERIPHERAL_EC_HOST_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373ace2e4ef0298e7c67a82dbfcab43769ad)。

eSPI 外设通知类型（Notification type）。

<a id="r_ga4e35c754c720f262805689a94985272c"></a>

```c
enum espi_interrupt_flags { ESPI_BUS_EVENTS = BIT(0) , ESPI_VIRTUAL_WIRE_CHANNEL_EVENTS = BIT(1) , ESPI_OOB_CHANNEL_EVENTS = BIT(2) , ESPI_FLASH_CHANNEL_EVENTS = BIT(3) , ESPI_PERIPHERAL_UART_EVENTS = BIT(4) , ESPI_PERIPHERAL_DEBUG_PORT80_EVENTS = BIT(5) , ESPI_PERIPHERAL_8042_KBC_EVENTS = BIT(6) , ESPI_PERIPHERAL_HOST_IO_EVENTS = BIT(7) , ESPI_PERIPHERAL_SHARED_MEMORY_EVENTS = BIT(8) }
```

相关声明：[espi_interrupt_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga4e35c754c720f262805689a94985272c)、[ESPI_BUS_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca21fadb75fbf1f2131e6b44b318a955a5)、[ESPI_VIRTUAL_WIRE_CHANNEL_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca6be11dd62eb439a30d95013f2b3ebcee)、[ESPI_OOB_CHANNEL_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca4b760583473994661ef490a64201b2ac)、[ESPI_FLASH_CHANNEL_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca3040bdf3cbb3888f3972202091fc5592)、[ESPI_PERIPHERAL_UART_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca07591a29b44dea00b0218680644c180b)、[ESPI_PERIPHERAL_DEBUG_PORT80_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca2f59f8c02560181d98b2d3b29de8f800)、[ESPI_PERIPHERAL_8042_KBC_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca0d877c057f5f32c02e55e89afc0a562b)、[ESPI_PERIPHERAL_HOST_IO_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272cafb7c66ad4601fcd17e4a1c040491c1a3)、[ESPI_PERIPHERAL_SHARED_MEMORY_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272cab402f4c4e5ebe41bd4e7927ab24806dd)。

eSPI 中断标志。

<a id="r_ga3e52615f244d7fa8ccda495ab8ec8a5b"></a>

```c
enum espi_cycle_type { ESPI_CYCLE_MEMORY_READ32 , ESPI_CYCLE_MEMORY_READ64 , ESPI_CYCLE_MEMORY_WRITE32 , ESPI_CYCLE_MEMORY_WRITE64 , ESPI_CYCLE_MESSAGE_NODATA , ESPI_CYCLE_MESSAGE_DATA , ESPI_CYCLE_OK_COMPLETION_NODATA , ESPI_CYCLE_OKCOMPLETION_DATA , ESPI_CYCLE_NOK_COMPLETION_NODATA }
```

相关声明：[espi_cycle_type](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga3e52615f244d7fa8ccda495ab8ec8a5b)、[ESPI_CYCLE_MEMORY_READ32](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba5b480e093a58849d4181bba22d5868a5)、[ESPI_CYCLE_MEMORY_READ64](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5bac8ec7673b4466b278dfb5e468f7a4d79)、[ESPI_CYCLE_MEMORY_WRITE32](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba2e5a736cf8a63491ee13d51ae4f8f073)、[ESPI_CYCLE_MEMORY_WRITE64](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba54c11e63fcfe3f859af57e65af3f31f7)、[ESPI_CYCLE_MESSAGE_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba5f2ae0575ca4e9b61c0acd7d4f08ee82)、[ESPI_CYCLE_MESSAGE_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba380e3d4e6b5579c8bb94e792fcb7d71f)、[ESPI_CYCLE_OK_COMPLETION_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba0335f2d34fab46960939e2d2c1c12e3f)、[ESPI_CYCLE_OKCOMPLETION_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5baf3dbc2bcc0ed883bc4d4160c21e6934f)、[ESPI_CYCLE_NOK_COMPLETION_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba0edb306e5fabcbf8b009375cde6a8a2b)。

eSPI 外设通道支持的 eSPI 周期类型（Cycle types）。

<a id="r_gab65a0951a8912d9de398cfec0aef7d35"></a>

```c
enum espi_vwire_signal { ESPI_VWIRE_SIGNAL_SLP_S3 , ESPI_VWIRE_SIGNAL_SLP_S4 , ESPI_VWIRE_SIGNAL_SLP_S5 , ESPI_VWIRE_SIGNAL_OOB_RST_WARN , ESPI_VWIRE_SIGNAL_PLTRST , ESPI_VWIRE_SIGNAL_SUS_STAT , ESPI_VWIRE_SIGNAL_NMIOUT , ESPI_VWIRE_SIGNAL_SMIOUT , ESPI_VWIRE_SIGNAL_HOST_RST_WARN , ESPI_VWIRE_SIGNAL_SLP_A , ESPI_VWIRE_SIGNAL_SUS_PWRDN_ACK , ESPI_VWIRE_SIGNAL_SUS_WARN , ESPI_VWIRE_SIGNAL_SLP_WLAN , ESPI_VWIRE_SIGNAL_SLP_LAN , ESPI_VWIRE_SIGNAL_HOST_C10 , ESPI_VWIRE_SIGNAL_DNX_WARN , ESPI_VWIRE_SIGNAL_PME , ESPI_VWIRE_SIGNAL_WAKE , ESPI_VWIRE_SIGNAL_OOB_RST_ACK , ESPI_VWIRE_SIGNAL_TARGET_BOOT_STS , ESPI_VWIRE_SIGNAL_ERR_NON_FATAL , ESPI_VWIRE_SIGNAL_ERR_FATAL , ESPI_VWIRE_SIGNAL_TARGET_BOOT_DONE , ESPI_VWIRE_SIGNAL_HOST_RST_ACK , ESPI_VWIRE_SIGNAL_RST_CPU_INIT , ESPI_VWIRE_SIGNAL_SMI , ESPI_VWIRE_SIGNAL_SCI , ESPI_VWIRE_SIGNAL_DNX_ACK , ESPI_VWIRE_SIGNAL_SUS_ACK , ESPI_VWIRE_SIGNAL_TARGET_GPIO_0 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_1 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_2 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_3 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_4 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_5 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_6 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_7 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_8 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_9 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_10 , ESPI_VWIRE_SIGNAL_TARGET_GPIO_11 , ESPI_VWIRE_SIGNAL_COUNT }
```

相关声明：[espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)、[ESPI_VWIRE_SIGNAL_SLP_S3](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab880a7156e489d5f7b8f78550e72b166)、[ESPI_VWIRE_SIGNAL_SLP_S4](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a4ef1fe12bd09be0875864d6c32164f73)、[ESPI_VWIRE_SIGNAL_SLP_S5](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ac4b4e30c097a4ef49f21549a799e1e13)、[ESPI_VWIRE_SIGNAL_OOB_RST_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a2f3f97b51b750050cd98e887e39431d1)、[ESPI_VWIRE_SIGNAL_PLTRST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a0bafcd0bb7f592f0e308dcfce39bcd08)、[ESPI_VWIRE_SIGNAL_SUS_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a0e13f250ba0c5a37451c7f3b0e98e663)、[ESPI_VWIRE_SIGNAL_NMIOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ad14b4b7a25141346bfefc507c588a238)、[ESPI_VWIRE_SIGNAL_SMIOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a1d54a71c6d2e52cb66cfaa0b55b61152)、[ESPI_VWIRE_SIGNAL_HOST_RST_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35af44250de6f60eabf9b0d85b8860ac56e)、[ESPI_VWIRE_SIGNAL_SLP_A](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aa4c8c69475b48d88302066823d2f3592)、[ESPI_VWIRE_SIGNAL_SUS_PWRDN_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab4f0bedd5717660cc8cac2d85c6c3d18)、[ESPI_VWIRE_SIGNAL_SUS_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a9e32eee077aaa1668c356fe1d4ab1cc5)、[ESPI_VWIRE_SIGNAL_SLP_WLAN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a3d95f095ae41bba9ef916fc68ddd4779)、[ESPI_VWIRE_SIGNAL_SLP_LAN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aba8b891a643ca567966d091963be4615)、[ESPI_VWIRE_SIGNAL_HOST_C10](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab9deb0dd6d4e878eff6413ddc34bb36c)、[ESPI_VWIRE_SIGNAL_DNX_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a923f3e602d9f8ac821ece2a625183146)、[ESPI_VWIRE_SIGNAL_PME](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aa87af5b5de184238e5f371851aaee692)、[ESPI_VWIRE_SIGNAL_WAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a736724f8229aebc356c2720a34a0143f)、[ESPI_VWIRE_SIGNAL_OOB_RST_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a8e15df6f8159b4c275dc4b20aaec352e)、[ESPI_VWIRE_SIGNAL_TARGET_BOOT_STS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a231caf3d46cde2eaf7305bf3f694838c)、[ESPI_VWIRE_SIGNAL_ERR_NON_FATAL](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a504ae332b89262f70a0bf1a9c8b6f527)、[ESPI_VWIRE_SIGNAL_ERR_FATAL](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aae0a3fd882c5765db33a4e7bd05e1ab1)、[ESPI_VWIRE_SIGNAL_TARGET_BOOT_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ad99ea62f91b40c8926cda944928e3631)、[ESPI_VWIRE_SIGNAL_HOST_RST_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a89420628ae26df4c45ef7fba04a3a85e)、[ESPI_VWIRE_SIGNAL_RST_CPU_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a19c40230e0bb4cee7b6ee42580c28a8d)、[ESPI_VWIRE_SIGNAL_SMI](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a2d9b2eef499d1bfd13bec1d2caa0e2f3)、[ESPI_VWIRE_SIGNAL_SCI](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35afa1f99a7e45b306c6736888e280f527c)、[ESPI_VWIRE_SIGNAL_DNX_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a58280c68c980476aabefa16e0509dd1c)、[ESPI_VWIRE_SIGNAL_SUS_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35abe28432b566619d8c6cce5e5034e5333)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_0](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_1](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_2](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_3](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_4](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ad9b6bb998bea0bc983ab8a6c452d52a1)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_5](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35af10e9e5b320301b2fe923e6793adbeaf)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_6](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aee0a1576a6e07708e1cde59597b49662)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_7](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ae34962d6db346e02f175894843ce0e1e)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_8](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a8a7b50f0aa53a2c80bae7747d628d219)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_9](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a9410475f349afcf44ddb25ebbd454978)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_10](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a637b5c00aaca05e5daa6969a680cbbb1)、[ESPI_VWIRE_SIGNAL_TARGET_GPIO_11](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a07a6b00a4b1cfad2137dc43d7232fc9f)、[ESPI_VWIRE_SIGNAL_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ad3319083735295454bc59b742988cfca)。

可通过虚拟线通道发送或接收的 eSPI 系统平台信号。

<a id="r_gad00b6a22843e5df9c6d6945d0d82310e"></a>

```c
enum lpc_peripheral_opcode { E8042_OBF_HAS_CHAR = 0x50 , E8042_IBF_HAS_CHAR , E8042_WRITE_KB_CHAR , E8042_WRITE_MB_CHAR , E8042_RESUME_IRQ , E8042_PAUSE_IRQ , E8042_CLEAR_OBF , E8042_READ_KB_STS , E8042_SET_FLAG , E8042_CLEAR_FLAG , EACPI_OBF_HAS_CHAR = EACPI_START_OPCODE , EACPI_IBF_HAS_CHAR , EACPI_WRITE_CHAR , EACPI_READ_STS , EACPI_WRITE_STS , EACPI_GET_SHARED_MEMORY , ECUSTOM_HOST_SUBS_INTERRUPT_EN = ECUSTOM_START_OPCODE , ECUSTOM_HOST_CMD_GET_PARAM_MEMORY , ECUSTOM_HOST_CMD_GET_PARAM_MEMORY_SIZE , ECUSTOM_HOST_CMD_SEND_RESULT }
```

相关声明：[lpc_peripheral_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gad00b6a22843e5df9c6d6945d0d82310e)、[E8042_OBF_HAS_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eac172afb38cb38970ef6242a4f45132f9)、[E8042_IBF_HAS_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eab70684413d736c8583f3dc53f14b7c7a)、[E8042_WRITE_KB_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eaa9135a5ea9a5ebd9d25660c37983c5d6)、[E8042_WRITE_MB_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eaaef0649f867424ec0c7889acb7354911)、[E8042_RESUME_IRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eac5b666b3319dc2ef0fc571684c2ea198)、[E8042_PAUSE_IRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea5e7205b5f1371f1a0f2eaed299389475)、[E8042_CLEAR_OBF](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eacdeb74a9534310f5dab3f1bfb5def534)、[E8042_READ_KB_STS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea8c62cd1266681c88aa0cb1af65ab551b)、[E8042_SET_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea83266d88740588d45be6667a4034c447)、[E8042_CLEAR_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea5c592b1cad381b296cde832c67264cd1)、[EACPI_OBF_HAS_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea3cce8bd0205691ecda53fc469606929d)、[EACPI_IBF_HAS_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea09f241a3f6ffcb5b7839c81c7fc4ea6e)、[EACPI_WRITE_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea689643f6feb724a303d3b790ff2899f7)、[EACPI_READ_STS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea02bf8538a66f633e3d2ec094f57c6173)、[EACPI_WRITE_STS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea02c7b1c69d803a5c45304260786afb6f)、[EACPI_GET_SHARED_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea530fb2a8690538e9659d6eb2c234fb91)、[ECUSTOM_HOST_SUBS_INTERRUPT_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea113a85c90924922dde04f3b5bf64046b)、[ECUSTOM_HOST_CMD_GET_PARAM_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea464db427cfd432b44874495ed7503db8)、[ECUSTOM_HOST_CMD_GET_PARAM_MEMORY_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eae1e018f0ecde965905752204e557ba40)、[ECUSTOM_HOST_CMD_SEND_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eaf97f7d0d3562dba07b826101bb805243)。

eSPI LPC 外设操作码（Opcodes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.5\_函数（Functions）

<a id="r_ga7227c53d384eb0dc666361261f069f68"></a>

```c
int espi_config (const struct device *dev, struct espi_cfg *cfg)
```

相关声明：[espi_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga7227c53d384eb0dc666361261f069f68)、[device](../device_reference/P002_设备对象结构.md)、[espi_cfg](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md)。

配置 eSPI 设备的运行方式。

<a id="r_ga869551e20fc2c3be4311c21c3c53999d"></a>

```c
bool espi_get_channel_status (const struct device *dev, enum espi_channel ch)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[espi_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga869551e20fc2c3be4311c21c3c53999d)、[device](../device_reference/P002_设备对象结构.md)、[espi_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gafaa3f7d54503c901ab23bd79a7f8a755)。

查询逻辑通道（Logical channel）是否就绪。

<a id="r_ga112f7554ba614c8e5f239b1319b4a763"></a>

```c
int espi_read_request (const struct device *dev, struct espi_request_packet *req)
```

相关声明：[espi_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga112f7554ba614c8e5f239b1319b4a763)、[device](../device_reference/P002_设备对象结构.md)、[espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)。

通过 eSPI 发送内存、I/O 或消息读取请求。

<a id="r_ga143ed88b1f220f9582c809165fd983fd"></a>

```c
int espi_write_request (const struct device *dev, struct espi_request_packet *req)
```

相关声明：[espi_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga143ed88b1f220f9582c809165fd983fd)、[device](../device_reference/P002_设备对象结构.md)、[espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)。

通过 eSPI 发送内存、I/O 或消息写入请求。

<a id="r_gaeaae20afa90d9d825d80997369f31465"></a>

```c
int espi_read_lpc_request (const struct device *dev, enum lpc_peripheral_opcode op, uint32_t *data)
```

相关声明：[espi_read_lpc_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaeaae20afa90d9d825d80997369f31465)、[device](../device_reference/P002_设备对象结构.md)、[lpc_peripheral_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gad00b6a22843e5df9c6d6945d0d82310e)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

从 LPC 外设读取 SoC 数据，其中的信息通过 eSPI 更新。

<a id="r_ga880b6b04824f9f0deea10e8018573b88"></a>

```c
int espi_write_lpc_request (const struct device *dev, enum lpc_peripheral_opcode op, uint32_t *data)
```

相关声明：[espi_write_lpc_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga880b6b04824f9f0deea10e8018573b88)、[device](../device_reference/P002_设备对象结构.md)、[lpc_peripheral_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gad00b6a22843e5df9c6d6945d0d82310e)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

向 LPC 外设写入数据，由此产生 eSPI 事务（Transaction）。

<a id="r_gacab2b3bff7d940e71ee1c2a9fdedf782"></a>

```c
int espi_send_vwire (const struct device *dev, enum espi_vwire_signal signal, uint8_t level)
```

相关声明：[espi_send_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gacab2b3bff7d940e71ee1c2a9fdedf782)、[device](../device_reference/P002_设备对象结构.md)、[espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)、[signal](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html#a5d326f119f87d0facaa662520f8c322a)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将系统/平台信号作为虚拟线（Virtual wire）数据包发送。

<a id="r_gaa8bb48b5592c4b49d27c9b8a42432410"></a>

```c
int espi_receive_vwire (const struct device *dev, enum espi_vwire_signal signal, uint8_t *level)
```

相关声明：[espi_receive_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaa8bb48b5592c4b49d27c9b8a42432410)、[device](../device_reference/P002_设备对象结构.md)、[espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)、[signal](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html#a5d326f119f87d0facaa662520f8c322a)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取封装在虚拟线中的信号的电平状态。

<a id="r_ga2557cfc7a38f669d14e9826e3fb0fdee"></a>

```c
int espi_send_oob (const struct device *dev, struct espi_oob_packet *pckt)
```

相关声明：[espi_send_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga2557cfc7a38f669d14e9826e3fb0fdee)、[device](../device_reference/P002_设备对象结构.md)、[espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)。

通过 eSPI 总线发送 SMBus 事务的带外（Out-of-band，OOB）数据包。

<a id="r_ga4b8f4fbf66a2b2ae394e00b16500f70d"></a>

```c
int espi_receive_oob (const struct device *dev, struct espi_oob_packet *pckt)
```

相关声明：[espi_receive_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga4b8f4fbf66a2b2ae394e00b16500f70d)、[device](../device_reference/P002_设备对象结构.md)、[espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)。

从 eSPI 总线接收 SMBus 事务的带外数据包。

<a id="r_ga0a97d11167367342283bfe6b6d66726e"></a>

```c
int espi_read_flash (const struct device *dev, struct espi_flash_packet *pckt)
```

相关声明：[espi_read_flash](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga0a97d11167367342283bfe6b6d66726e)、[device](../device_reference/P002_设备对象结构.md)、[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

发送共享 Flash 的读取请求包。

<a id="r_gab02d46fd690e33875cc1b2433c976891"></a>

```c
int espi_write_flash (const struct device *dev, struct espi_flash_packet *pckt)
```

相关声明：[espi_write_flash](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab02d46fd690e33875cc1b2433c976891)、[device](../device_reference/P002_设备对象结构.md)、[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

发送共享 Flash 的写入请求包。

<a id="r_gab42be7c76c4523cea96365aa77fd18be"></a>

```c
int espi_flash_erase (const struct device *dev, struct espi_flash_packet *pckt)
```

相关声明：[espi_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab42be7c76c4523cea96365aa77fd18be)、[device](../device_reference/P002_设备对象结构.md)、[espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)。

发送共享 Flash 的擦除请求包。

<a id="r_ga8d88e4e3893d610713195e5352ec2565"></a>

```c
static void espi_init_callback (struct espi_callback *callback, espi_callback_handler_t handler, enum espi_bus_event evt_type)
```

相关声明：[espi_init_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga8d88e4e3893d610713195e5352ec2565)、[espi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga9d848c7e367cf277230f365f73c15c46)、[espi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga36ac3fbf9813f78bad90f047e1eb1128)。

回调模型（Callback model）。

<a id="r_gabf5f0ea01ec8ed5345b2e119181c2313"></a>

```c
static int espi_add_callback (const struct device *dev, struct espi_callback *callback)
```

相关声明：[espi_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gabf5f0ea01ec8ed5345b2e119181c2313)、[device](../device_reference/P002_设备对象结构.md)。

添加应用回调。

<a id="r_ga7f04f98ea6a4671b821cf6ddf6bbf2a6"></a>

```c
static int espi_remove_callback (const struct device *dev, struct espi_callback *callback)
```

相关声明：[espi_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga7f04f98ea6a4671b821cf6ddf6bbf2a6)、[device](../device_reference/P002_设备对象结构.md)。

移除应用回调。

<a id="r_ga1cd0afc52d533414b5bbc684cef8b9af"></a>

```c
static int espi_interrupt_config (const struct device *dev, uint32_t espi_flags, uint32_t espi_vendor_flags)
```

相关声明：[espi_interrupt_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga1cd0afc52d533414b5bbc684cef8b9af)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

控制 eSPI 中断。


## 4.6\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/espi_8h_source.html)
- [espi_evt_data_kbc](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md)
- [espi_evt_data_acpi](../peripheral_bus_storage_model_reference/P009_espi_evt_data_acpi_结构体.md)
- [espi_evt_data_pvt](../peripheral_bus_storage_model_reference/P011_espi_evt_data_pvt_结构体.md)
- [espi_event](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md)
- [espi_cfg](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md)
- [espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)
- [espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)
- [espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)
- [espi_driver_api](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md)
- [ESPI_INT_ALL_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga8da8ac3b45044323fdb24f1361adaac7)
- [ESPI_INT_BUS_ONLY_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gadeb45b8838f4d1fbf05095c36ca3faba)
- [ESPI_INT_NONE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga24b468de0013cd9cf9d814faff13b94e)
- [HOST_KBC_EVT_IBF](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaa0807c908666cdcbb3a85f310bfbfccc)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [HOST_KBC_EVT_OBE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga807bb75027f24e040cd28eba4bc1002c)
- [ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaa45ee9beafbda94f8f9ad799e78089cd)
- [ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga01e61256f8be5e24d131c68d81ed8916)
- [ESPI_EVENT_DATA_ACPI_TYPE_HOST_RD_EC_TO_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga6807d29b11134b76b14c8887053cbce1)
- [ESPI_VWIRE_SIGNAL_OCB_0](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gae4855b6cf8049de8aa6d67763f1be8c3)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_0](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2)
- [ESPI_VWIRE_SIGNAL_OCB_1](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga2ed490939e0249ff8196f77a74967727)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_1](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de)
- [ESPI_VWIRE_SIGNAL_OCB_2](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaf35d03bc041dc6baefe35b74c163d73b)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_2](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b)
- [ESPI_VWIRE_SIGNAL_OCB_3](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaeae1765d801cd298c27404c173a94707)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_3](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a)
- [espi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga9d848c7e367cf277230f365f73c15c46)
- [device](../device_reference/P002_设备对象结构.md)
- [espi_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga97336083a3ed3f561301fcf5762dc73c)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [espi_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga4712365e3a38d859fefbf0e9a6f32b07)
- [espi_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gafaa3f7d54503c901ab23bd79a7f8a755)
- [espi_api_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga3c3e6a70a04c14ec50fa0dcef4055f73)
- [espi_api_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga47ea19517406b64f074b4eee7a9d1923)
- [espi_api_lpc_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga04547d61ee4ed5d34fca3fb11ec0370f)
- [lpc_peripheral_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gad00b6a22843e5df9c6d6945d0d82310e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [espi_api_lpc_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gac7e3730c214b877772b24c4055ab997a)
- [espi_api_send_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga838aefb5fbe399f6492803ceb391fa8c)
- [espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [espi_api_receive_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga806a0b3f3f4e629c5556f1399c4e29e2)
- [espi_api_send_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gae7497b9629a9444f94dae125fdf46005)
- [espi_api_receive_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga79255a516e48256d8381d0b32e5ae345)
- [espi_api_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga6bb1bb8af96c58dc0d9ad041d95cd397)
- [espi_api_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga1a8715b387a037dddacc92424fe0ba6f)
- [espi_api_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga422abe38a4d2cce441d5165192adc982)
- [espi_api_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gab0313b00d884426800395ec5a907f744)
- [espi_api_interrupt_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga7d497e1f4573f54f49202b67cb5cbe5c)
- [espi_interrupt_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga4e35c754c720f262805689a94985272c)
- [espi_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0)
- [ESPI_IO_MODE_SINGLE_LINE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a9f47188ebd9bb4cb6e426d0bc0b6595c)
- [ESPI_IO_MODE_DUAL_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0af766582d28d16af7c5aff6372e4ee243)
- [ESPI_IO_MODE_QUAD_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a87e70bb0f5c4f6a3a21ca1bcfa4540fc)
- [ESPI_CHANNEL_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggafaa3f7d54503c901ab23bd79a7f8a755a32f636bbad2618a6b1554656d3b53206)
- [ESPI_CHANNEL_VWIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggafaa3f7d54503c901ab23bd79a7f8a755ac2e84a127870ff50359cf96528c9a7c6)
- [ESPI_CHANNEL_OOB](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggafaa3f7d54503c901ab23bd79a7f8a755a0ccb80544cbda501cc90ea0c3b868e54)
- [ESPI_CHANNEL_FLASH](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggafaa3f7d54503c901ab23bd79a7f8a755a5616bf2bf49a8c457fcc2f27d9fe0518)
- [espi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga36ac3fbf9813f78bad90f047e1eb1128)
- [ESPI_BUS_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128ae6d4d43eded0d8a368c90ea653a60956)
- [ESPI_BUS_EVENT_CHANNEL_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128a996aee0a8f8ba0cead11cea0d39d2973)
- [ESPI_BUS_EVENT_VWIRE_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128aa09f7dcd4b2d3addfaddbad5b8f2e5a2)
- [ESPI_BUS_EVENT_OOB_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128a3b5e529d1d0ba11c59172ab01c30e203)
- [ESPI_BUS_PERIPHERAL_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128a9ac837699f302bd10332814c7014adea)
- [ESPI_BUS_TAF_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128a9f2a9cfda3b803687a0992a9d41f0014)
- [espi_pc_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gac55098842dd9d181144ac4b4122a610e)
- [ESPI_PC_EVT_BUS_CHANNEL_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggac55098842dd9d181144ac4b4122a610ea68ecb52b04ffddcc93fbcc77d3643687)
- [ESPI_PC_EVT_BUS_MASTER_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggac55098842dd9d181144ac4b4122a610ea0e245cbeef479218d4e6c9bec57e40d1)
- [espi_virtual_peripheral](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga2629a5518a94f031419eeccd05f07373)
- [ESPI_PERIPHERAL_UART](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373a24478711945fd5258d8ca86bbb79b867)
- [ESPI_PERIPHERAL_8042_KBC](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373aaea75bb5ab8a5ff31dd6b8787f44df30)
- [ESPI_PERIPHERAL_HOST_IO](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373a8948a6f18bfbe87859a529d5f6e669b8)
- [ESPI_PERIPHERAL_DEBUG_PORT80](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373af51b7171cf6085fa7946333ff32fe2f0)
- [ESPI_PERIPHERAL_HOST_IO_PVT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373aa217b4786d7b8bacbaa4ec740550e71e)
- [ESPI_PERIPHERAL_HOST_IO_PVT2](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373a0e6e9dc1a7975cd80991090a78ea6231)
- [ESPI_PERIPHERAL_HOST_IO_PVT3](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373a8d8c64c49e8c7a75cb3a665e63a6f5ce)
- [ESPI_PERIPHERAL_EC_HOST_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373ace2e4ef0298e7c67a82dbfcab43769ad)
- [ESPI_BUS_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca21fadb75fbf1f2131e6b44b318a955a5)
- [ESPI_VIRTUAL_WIRE_CHANNEL_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca6be11dd62eb439a30d95013f2b3ebcee)
- [ESPI_OOB_CHANNEL_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca4b760583473994661ef490a64201b2ac)
- [ESPI_FLASH_CHANNEL_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca3040bdf3cbb3888f3972202091fc5592)
- [ESPI_PERIPHERAL_UART_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca07591a29b44dea00b0218680644c180b)
- [ESPI_PERIPHERAL_DEBUG_PORT80_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca2f59f8c02560181d98b2d3b29de8f800)
- [ESPI_PERIPHERAL_8042_KBC_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca0d877c057f5f32c02e55e89afc0a562b)
- [ESPI_PERIPHERAL_HOST_IO_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272cafb7c66ad4601fcd17e4a1c040491c1a3)
- [ESPI_PERIPHERAL_SHARED_MEMORY_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272cab402f4c4e5ebe41bd4e7927ab24806dd)
- [espi_cycle_type](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga3e52615f244d7fa8ccda495ab8ec8a5b)
- [ESPI_CYCLE_MEMORY_READ32](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba5b480e093a58849d4181bba22d5868a5)
- [ESPI_CYCLE_MEMORY_READ64](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5bac8ec7673b4466b278dfb5e468f7a4d79)
- [ESPI_CYCLE_MEMORY_WRITE32](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba2e5a736cf8a63491ee13d51ae4f8f073)
- [ESPI_CYCLE_MEMORY_WRITE64](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba54c11e63fcfe3f859af57e65af3f31f7)
- [ESPI_CYCLE_MESSAGE_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba5f2ae0575ca4e9b61c0acd7d4f08ee82)
- [ESPI_CYCLE_MESSAGE_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba380e3d4e6b5579c8bb94e792fcb7d71f)
- [ESPI_CYCLE_OK_COMPLETION_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba0335f2d34fab46960939e2d2c1c12e3f)
- [ESPI_CYCLE_OKCOMPLETION_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5baf3dbc2bcc0ed883bc4d4160c21e6934f)
- [ESPI_CYCLE_NOK_COMPLETION_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba0edb306e5fabcbf8b009375cde6a8a2b)
- [ESPI_VWIRE_SIGNAL_SLP_S3](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab880a7156e489d5f7b8f78550e72b166)
- [ESPI_VWIRE_SIGNAL_SLP_S4](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a4ef1fe12bd09be0875864d6c32164f73)
- [ESPI_VWIRE_SIGNAL_SLP_S5](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ac4b4e30c097a4ef49f21549a799e1e13)
- [ESPI_VWIRE_SIGNAL_OOB_RST_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a2f3f97b51b750050cd98e887e39431d1)
- [ESPI_VWIRE_SIGNAL_PLTRST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a0bafcd0bb7f592f0e308dcfce39bcd08)
- [ESPI_VWIRE_SIGNAL_SUS_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a0e13f250ba0c5a37451c7f3b0e98e663)
- [ESPI_VWIRE_SIGNAL_NMIOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ad14b4b7a25141346bfefc507c588a238)
- [ESPI_VWIRE_SIGNAL_SMIOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a1d54a71c6d2e52cb66cfaa0b55b61152)
- [ESPI_VWIRE_SIGNAL_HOST_RST_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35af44250de6f60eabf9b0d85b8860ac56e)
- [ESPI_VWIRE_SIGNAL_SLP_A](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aa4c8c69475b48d88302066823d2f3592)
- [ESPI_VWIRE_SIGNAL_SUS_PWRDN_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab4f0bedd5717660cc8cac2d85c6c3d18)
- [ESPI_VWIRE_SIGNAL_SUS_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a9e32eee077aaa1668c356fe1d4ab1cc5)
- [ESPI_VWIRE_SIGNAL_SLP_WLAN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a3d95f095ae41bba9ef916fc68ddd4779)
- [ESPI_VWIRE_SIGNAL_SLP_LAN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aba8b891a643ca567966d091963be4615)
- [ESPI_VWIRE_SIGNAL_HOST_C10](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab9deb0dd6d4e878eff6413ddc34bb36c)
- [ESPI_VWIRE_SIGNAL_DNX_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a923f3e602d9f8ac821ece2a625183146)
- [ESPI_VWIRE_SIGNAL_PME](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aa87af5b5de184238e5f371851aaee692)
- [ESPI_VWIRE_SIGNAL_WAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a736724f8229aebc356c2720a34a0143f)
- [ESPI_VWIRE_SIGNAL_OOB_RST_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a8e15df6f8159b4c275dc4b20aaec352e)
- [ESPI_VWIRE_SIGNAL_TARGET_BOOT_STS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a231caf3d46cde2eaf7305bf3f694838c)
- [ESPI_VWIRE_SIGNAL_ERR_NON_FATAL](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a504ae332b89262f70a0bf1a9c8b6f527)
- [ESPI_VWIRE_SIGNAL_ERR_FATAL](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aae0a3fd882c5765db33a4e7bd05e1ab1)
- [ESPI_VWIRE_SIGNAL_TARGET_BOOT_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ad99ea62f91b40c8926cda944928e3631)
- [ESPI_VWIRE_SIGNAL_HOST_RST_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a89420628ae26df4c45ef7fba04a3a85e)
- [ESPI_VWIRE_SIGNAL_RST_CPU_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a19c40230e0bb4cee7b6ee42580c28a8d)
- [ESPI_VWIRE_SIGNAL_SMI](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a2d9b2eef499d1bfd13bec1d2caa0e2f3)
- [ESPI_VWIRE_SIGNAL_SCI](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35afa1f99a7e45b306c6736888e280f527c)
- [ESPI_VWIRE_SIGNAL_DNX_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a58280c68c980476aabefa16e0509dd1c)
- [ESPI_VWIRE_SIGNAL_SUS_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35abe28432b566619d8c6cce5e5034e5333)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_4](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ad9b6bb998bea0bc983ab8a6c452d52a1)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_5](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35af10e9e5b320301b2fe923e6793adbeaf)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_6](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aee0a1576a6e07708e1cde59597b49662)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_7](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ae34962d6db346e02f175894843ce0e1e)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_8](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a8a7b50f0aa53a2c80bae7747d628d219)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_9](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a9410475f349afcf44ddb25ebbd454978)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_10](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a637b5c00aaca05e5daa6969a680cbbb1)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_11](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a07a6b00a4b1cfad2137dc43d7232fc9f)
- [ESPI_VWIRE_SIGNAL_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ad3319083735295454bc59b742988cfca)
- [E8042_OBF_HAS_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eac172afb38cb38970ef6242a4f45132f9)
- [E8042_IBF_HAS_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eab70684413d736c8583f3dc53f14b7c7a)
- [E8042_WRITE_KB_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eaa9135a5ea9a5ebd9d25660c37983c5d6)
- [E8042_WRITE_MB_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eaaef0649f867424ec0c7889acb7354911)
- [E8042_RESUME_IRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eac5b666b3319dc2ef0fc571684c2ea198)
- [E8042_PAUSE_IRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea5e7205b5f1371f1a0f2eaed299389475)
- [E8042_CLEAR_OBF](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eacdeb74a9534310f5dab3f1bfb5def534)
- [E8042_READ_KB_STS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea8c62cd1266681c88aa0cb1af65ab551b)
- [E8042_SET_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea83266d88740588d45be6667a4034c447)
- [E8042_CLEAR_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea5c592b1cad381b296cde832c67264cd1)
- [EACPI_OBF_HAS_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea3cce8bd0205691ecda53fc469606929d)
- [EACPI_IBF_HAS_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea09f241a3f6ffcb5b7839c81c7fc4ea6e)
- [EACPI_WRITE_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea689643f6feb724a303d3b790ff2899f7)
- [EACPI_READ_STS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea02bf8538a66f633e3d2ec094f57c6173)
- [EACPI_WRITE_STS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea02c7b1c69d803a5c45304260786afb6f)
- [EACPI_GET_SHARED_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea530fb2a8690538e9659d6eb2c234fb91)
- [ECUSTOM_HOST_SUBS_INTERRUPT_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea113a85c90924922dde04f3b5bf64046b)
- [ECUSTOM_HOST_CMD_GET_PARAM_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea464db427cfd432b44874495ed7503db8)
- [ECUSTOM_HOST_CMD_GET_PARAM_MEMORY_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eae1e018f0ecde965905752204e557ba40)
- [ECUSTOM_HOST_CMD_SEND_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eaf97f7d0d3562dba07b826101bb805243)
- [espi_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga7227c53d384eb0dc666361261f069f68)
- [espi_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga869551e20fc2c3be4311c21c3c53999d)
- [espi_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga112f7554ba614c8e5f239b1319b4a763)
- [espi_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga143ed88b1f220f9582c809165fd983fd)
- [espi_read_lpc_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaeaae20afa90d9d825d80997369f31465)
- [espi_write_lpc_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga880b6b04824f9f0deea10e8018573b88)
- [espi_send_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gacab2b3bff7d940e71ee1c2a9fdedf782)
- [signal](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html#a5d326f119f87d0facaa662520f8c322a)
- [espi_receive_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaa8bb48b5592c4b49d27c9b8a42432410)
- [espi_send_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga2557cfc7a38f669d14e9826e3fb0fdee)
- [espi_receive_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga4b8f4fbf66a2b2ae394e00b16500f70d)
- [espi_read_flash](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga0a97d11167367342283bfe6b6d66726e)
- [espi_write_flash](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab02d46fd690e33875cc1b2433c976891)
- [espi_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab42be7c76c4523cea96365aa77fd18be)
- [espi_init_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga8d88e4e3893d610713195e5352ec2565)
- [espi_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gabf5f0ea01ec8ed5345b2e119181c2313)
- [espi_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga7f04f98ea6a4671b821cf6ddf6bbf2a6)
- [espi_interrupt_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga1cd0afc52d533414b5bbc684cef8b9af)

<a id="header-details"></a>

---

[上一章](P003_zephyr__drivers__disk.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__drivers__espi_saf.h_头文件参考.md)
