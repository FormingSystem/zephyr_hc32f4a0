---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-7
title: espi_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structespi__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_espi\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structespi__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：eSPI驱动操作。

```c
#include <zephyr/drivers/espi.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：增强串行外设接口（eSPI）驱动操作。这是每个 eSPI 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_ae7f3be0766c35a75d611735f09e6b728"></a>

```c
espi_api_config config
```

相关声明：[espi_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga97336083a3ed3f561301fcf5762dc73c)、[config](#ae7f3be0766c35a75d611735f09e6b728)。

`REQ`：配置 eSPI 设备的运行方式。

<a id="r_ac27072d18c70f4b415467d01a37a2f75"></a>

```c
espi_api_get_channel_status get_channel_status
```

相关声明：[espi_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga4712365e3a38d859fefbf0e9a6f32b07)、[get_channel_status](#ac27072d18c70f4b415467d01a37a2f75)。

`REQ`：查询逻辑通道（Logical channel）是否就绪。

<a id="r_ac9033b4b59e0c99747e367ed283ab116"></a>

```c
espi_api_read_request read_request
```

相关声明：[espi_api_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga3c3e6a70a04c14ec50fa0dcef4055f73)、[read_request](#ac9033b4b59e0c99747e367ed283ab116)。

`OPT`：通过 eSPI 发送内存、I/O 或消息读取请求。

<a id="r_a5ff3310cd5db4a08c42284cc4ea48057"></a>

```c
espi_api_write_request write_request
```

相关声明：[espi_api_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga47ea19517406b64f074b4eee7a9d1923)、[write_request](#a5ff3310cd5db4a08c42284cc4ea48057)。

`OPT`：通过 eSPI 发送内存、I/O 或消息写入请求。

<a id="r_aea877fee89f0d346b009c053a3c0a09d"></a>

```c
espi_api_lpc_read_request read_lpc_request
```

相关声明：[espi_api_lpc_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga04547d61ee4ed5d34fca3fb11ec0370f)、[read_lpc_request](#aea877fee89f0d346b009c053a3c0a09d)。

`OPT`：从 LPC 外设读取 SoC 数据，其中的信息通过 eSPI 更新。

<a id="r_a049bff890414ce43f2323238a6ee3d15"></a>

```c
espi_api_lpc_write_request write_lpc_request
```

相关声明：[espi_api_lpc_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gac7e3730c214b877772b24c4055ab997a)、[write_lpc_request](#a049bff890414ce43f2323238a6ee3d15)。

`OPT`：向 LPC 外设写入数据，由此产生 eSPI 事务（Transaction）。

<a id="r_a2241bb06a85d6220417cee282e359021"></a>

```c
espi_api_send_vwire send_vwire
```

相关声明：[espi_api_send_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga838aefb5fbe399f6492803ceb391fa8c)、[send_vwire](#a2241bb06a85d6220417cee282e359021)。

`REQ`：将系统/平台信号作为虚拟线（Virtual wire）数据包发送。

<a id="r_a53b561bfa5dbc53dbf8cbb6af88c1b36"></a>

```c
espi_api_receive_vwire receive_vwire
```

相关声明：[espi_api_receive_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga806a0b3f3f4e629c5556f1399c4e29e2)、[receive_vwire](#a53b561bfa5dbc53dbf8cbb6af88c1b36)。

`REQ`：获取封装在虚拟线中的信号的电平状态。

<a id="r_a47041efc4fb0879b2812bb53533b8ab8"></a>

```c
espi_api_send_oob send_oob
```

相关声明：[espi_api_send_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gae7497b9629a9444f94dae125fdf46005)、[send_oob](#a47041efc4fb0879b2812bb53533b8ab8)。

`OPT`：通过 eSPI 总线发送 SMBus 事务的带外（Out-of-band，OOB）数据包。

<a id="r_a5c1be83cf9f3eac140b8ab7b37a86c1b"></a>

```c
espi_api_receive_oob receive_oob
```

相关声明：[espi_api_receive_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga79255a516e48256d8381d0b32e5ae345)、[receive_oob](#a5c1be83cf9f3eac140b8ab7b37a86c1b)。

`OPT`：从 eSPI 总线接收 SMBus 事务的带外数据包。

<a id="r_a2ae357ec0cf8f4ee548f50350bd4eaa4"></a>

```c
espi_api_flash_read flash_read
```

相关声明：[espi_api_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga6bb1bb8af96c58dc0d9ad041d95cd397)、[flash_read](#a2ae357ec0cf8f4ee548f50350bd4eaa4)。

`OPT`：发送共享 Flash 的读取请求包。

<a id="r_a74218772f99c24af2fe9ae5b1749039e"></a>

```c
espi_api_flash_write flash_write
```

相关声明：[espi_api_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga1a8715b387a037dddacc92424fe0ba6f)、[flash_write](#a74218772f99c24af2fe9ae5b1749039e)。

`OPT`：发送共享 Flash 的写入请求包。

<a id="r_abfd2310657421141737af0f8316825ef"></a>

```c
espi_api_flash_erase flash_erase
```

相关声明：[espi_api_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga422abe38a4d2cce441d5165192adc982)、[flash_erase](#abfd2310657421141737af0f8316825ef)。

`OPT`：发送共享 Flash 的擦除请求包。

<a id="r_adfcdf83461d94819c788dac869b09096"></a>

```c
espi_api_manage_callback manage_callback
```

相关声明：[espi_api_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gab0313b00d884426800395ec5a907f744)、[manage_callback](#adfcdf83461d94819c788dac869b09096)。

`OPT`：添加或移除应用程序回调。

<a id="r_a96ad30567d449161c7c30f86b9500808"></a>

```c
espi_api_interrupt_configure interrupt_config
```

相关声明：[espi_api_interrupt_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga7d497e1f4573f54f49202b67cb5cbe5c)、[interrupt_config](#a96ad30567d449161c7c30f86b9500808)。

`OPT`：控制 eSPI 中断。

## 7.2\_详细说明（Detailed Documentation）

<a id="ae7f3be0766c35a75d611735f09e6b728"></a>

### `config`

```c
espi_api_config espi_driver_api::config
```

`REQ`：配置 eSPI 设备的运行方式。

<a id="abfd2310657421141737af0f8316825ef"></a>

### `flash_erase`

```c
espi_api_flash_erase espi_driver_api::flash_erase
```

`OPT`：发送共享 Flash 的擦除请求包。

<a id="a2ae357ec0cf8f4ee548f50350bd4eaa4"></a>

### `flash_read`

```c
espi_api_flash_read espi_driver_api::flash_read
```

`OPT`：发送共享 Flash 的读取请求包。

<a id="a74218772f99c24af2fe9ae5b1749039e"></a>

### `flash_write`

```c
espi_api_flash_write espi_driver_api::flash_write
```

`OPT`：发送共享 Flash 的写入请求包。

<a id="ac27072d18c70f4b415467d01a37a2f75"></a>

### `get_channel_status`

```c
espi_api_get_channel_status espi_driver_api::get_channel_status
```

`REQ`：查询逻辑通道（Logical channel）是否就绪。

<a id="a96ad30567d449161c7c30f86b9500808"></a>

### `interrupt_config`

```c
espi_api_interrupt_configure espi_driver_api::interrupt_config
```

`OPT`：控制 eSPI 中断。

<a id="adfcdf83461d94819c788dac869b09096"></a>

### `manage_callback`

```c
espi_api_manage_callback espi_driver_api::manage_callback
```

`OPT`：添加或移除应用程序回调。

<a id="aea877fee89f0d346b009c053a3c0a09d"></a>

### `read_lpc_request`

```c
espi_api_lpc_read_request espi_driver_api::read_lpc_request
```

`OPT`：从 LPC 外设读取 SoC 数据，其中的信息通过 eSPI 更新。

<a id="ac9033b4b59e0c99747e367ed283ab116"></a>

### `read_request`

```c
espi_api_read_request espi_driver_api::read_request
```

`OPT`：通过 eSPI 发送内存、I/O 或消息读取请求。

<a id="a5c1be83cf9f3eac140b8ab7b37a86c1b"></a>

### `receive_oob`

```c
espi_api_receive_oob espi_driver_api::receive_oob
```

`OPT`：从 eSPI 总线接收 SMBus 事务的带外数据包。

<a id="a53b561bfa5dbc53dbf8cbb6af88c1b36"></a>

### `receive_vwire`

```c
espi_api_receive_vwire espi_driver_api::receive_vwire
```

`REQ`：获取封装在虚拟线中的信号的电平状态。

<a id="a47041efc4fb0879b2812bb53533b8ab8"></a>

### `send_oob`

```c
espi_api_send_oob espi_driver_api::send_oob
```

`OPT`：通过 eSPI 总线发送 SMBus 事务的带外（Out-of-band，OOB）数据包。

<a id="a2241bb06a85d6220417cee282e359021"></a>

### `send_vwire`

```c
espi_api_send_vwire espi_driver_api::send_vwire
```

`REQ`：将系统/平台信号作为虚拟线（Virtual wire）数据包发送。

<a id="a049bff890414ce43f2323238a6ee3d15"></a>

### `write_lpc_request`

```c
espi_api_lpc_write_request espi_driver_api::write_lpc_request
```

`OPT`：向 LPC 外设写入数据，由此产生 eSPI 事务（Transaction）。

<a id="a5ff3310cd5db4a08c42284cc4ea48057"></a>

### `write_request`

```c
espi_api_write_request espi_driver_api::write_request
```

`OPT`：通过 eSPI 发送内存、I/O 或消息写入请求。

本数据类型文档由以下文件生成：

- `zephyr/drivers/espi.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/drivers/espi.h](https://docs.zephyrproject.org/latest/doxygen/html/espi_8h_source.html)
- [espi_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga97336083a3ed3f561301fcf5762dc73c)
- [espi_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga4712365e3a38d859fefbf0e9a6f32b07)
- [espi_api_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga3c3e6a70a04c14ec50fa0dcef4055f73)
- [espi_api_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga47ea19517406b64f074b4eee7a9d1923)
- [espi_api_lpc_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga04547d61ee4ed5d34fca3fb11ec0370f)
- [espi_api_lpc_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gac7e3730c214b877772b24c4055ab997a)
- [espi_api_send_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga838aefb5fbe399f6492803ceb391fa8c)
- [espi_api_receive_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga806a0b3f3f4e629c5556f1399c4e29e2)
- [espi_api_send_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gae7497b9629a9444f94dae125fdf46005)
- [espi_api_receive_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga79255a516e48256d8381d0b32e5ae345)
- [espi_api_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga6bb1bb8af96c58dc0d9ad041d95cd397)
- [espi_api_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga1a8715b387a037dddacc92424fe0ba6f)
- [espi_api_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga422abe38a4d2cce441d5165192adc982)
- [espi_api_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gab0313b00d884426800395ec5a907f744)
- [espi_api_interrupt_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga7d497e1f4573f54f49202b67cb5cbe5c)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_espi_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_espi_event_结构体.md)
