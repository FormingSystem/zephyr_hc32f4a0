---
id: learning.zephyr-docs.platform-security-model-reference.page-52
title: scmi_transport_api_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__transport__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_scmi\_transport\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__transport__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）的传输驱动操作。

```c
#include <zephyr/drivers/firmware/scmi/transport.h>
```

<a id="details"></a>

SCMI 传输驱动操作（Transport driver operations）。此结构体包含所有传输驱动都应实现的一组操作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_a2d90efd745ef78a07482c51a5748fef4"></a>

```c
int(* init )(const struct device *transport)
```

相关声明：[init](#a2d90efd745ef78a07482c51a5748fef4)、[device](../device_reference/P002_设备对象结构.md)。

初始化传输驱动。

<a id="r_ac5eb66a8b0d25c17ef6bf36da23c06ae"></a>

```c
int(* send_message )(const struct device *transport, struct scmi_channel *chan, struct scmi_message *msg, bool use_polling)
```

相关声明：[send_message](#ac5eb66a8b0d25c17ef6bf36da23c06ae)、[device](../device_reference/P002_设备对象结构.md)、[scmi_channel](P033_scmi_channel_结构体.md)、[scmi_message](P037_scmi_message_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

向平台发送消息。

<a id="r_a452deceb4eb343b19adf720eae7fb602"></a>

```c
int(* setup_chan )(const struct device *transport, struct scmi_channel *chan, bool tx)
```

相关声明：[setup_chan](#a452deceb4eb343b19adf720eae7fb602)、[device](../device_reference/P002_设备对象结构.md)、[scmi_channel](P033_scmi_channel_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

准备通道以进行通信。

<a id="r_a8cc80f631a74b7cf253140fa1a7707d9"></a>

```c
int(* read_message )(const struct device *transport, struct scmi_channel *chan, struct scmi_message *msg)
```

相关声明：[read_message](#a8cc80f631a74b7cf253140fa1a7707d9)、[device](../device_reference/P002_设备对象结构.md)、[scmi_channel](P033_scmi_channel_结构体.md)、[scmi_message](P037_scmi_message_结构体.md)。

从平台读取消息。

<a id="r_a52c33e80eda1ac892d2e04e3692ced58"></a>

```c
bool(* channel_is_free )(const struct device *transport, struct scmi_channel *chan)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[channel_is_free](#a52c33e80eda1ac892d2e04e3692ced58)、[device](../device_reference/P002_设备对象结构.md)、[scmi_channel](P033_scmi_channel_结构体.md)。

检查发送通道（TX channel）是否空闲。

<a id="r_a517cb99fc369eec024d4a4acf66865e3"></a>

```c
struct scmi_channel *(* request_channel )(const struct device *transport, uint32_t proto, bool tx)
```

相关声明：[scmi_channel](P033_scmi_channel_结构体.md)、[request_channel](#a517cb99fc369eec024d4a4acf66865e3)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

动态请求通道。

## 52.2\_详细说明（Detailed Documentation）

<a id="a52c33e80eda1ac892d2e04e3692ced58"></a>

### `channel_is_free`

```c
bool(* scmi_transport_api::channel_is_free) (const struct device *transport, struct scmi_channel *chan)
```

检查发送通道（TX channel）是否空闲。

用于检查发送通道是否允许向平台发送数据。如果此前已向平台发送消息，则假定此函数会指示该消息的回复是否可用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 设备（Device）。 |
| `chan` | 要查询的发送通道。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="a2d90efd745ef78a07482c51a5748fef4"></a>

### `init`

```c
int(* scmi_transport_api::init) (const struct device *transport)
```

初始化传输驱动。

如果驱动无需初始化，可以不实现此操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 传输设备（Transport device）。 |

**说明（Note）**：注意：此操作为可选操作。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="a8cc80f631a74b7cf253140fa1a7707d9"></a>

### `read_message`

```c
int(* scmi_transport_api::read_message) (const struct device *transport, struct scmi_channel *chan, struct scmi_message *msg)
```

从平台读取消息。

用于通过给定的接收通道（RX channel）从平台读取或接收消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 传输设备（Transport device）。 |
| `chan` | 用于接收消息的通道。 |
| `msg` | 要接收的消息。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="a517cb99fc369eec024d4a4acf66865e3"></a>

### `request_channel`

```c
struct scmi_channel *(* scmi_transport_api::request_channel) (const struct device *transport, uint32_t proto, bool tx)
```

动态请求通道。

若启用了 `CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS`，则使用此操作动态请求通道，并将其绑定到给定协议。否则，可以不实现此操作。

译注：原文使用上述配置条件并描述为“动态请求”，此处保留原文的条件与行为说明。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 传输设备（Transport device）。 |
| `proto` | 所请求通道对应的协议 ID。 |
| `tx` | 通道为发送通道时取 `true`，为接收通道时取 `false`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `pointer` | 成功时，指向已绑定到给定协议的通道。 |
| `NULL` | 失败时。 |

**说明（Note）**：注意：此操作为可选操作。

<a id="ac5eb66a8b0d25c17ef6bf36da23c06ae"></a>

### `send_message`

```c
int(* scmi_transport_api::send_message) (const struct device *transport, struct scmi_channel *chan, struct scmi_message *msg, bool use_polling)
```

向平台发送消息。

用于通过给定的发送通道向平台发送消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 传输设备（Transport device）。 |
| `chan` | 用于发送消息的通道。 |
| `msg` | 要发送的消息。 |
| `use_polling` | 应启用轮询时为 `true`，否则为 `false`。 |

**说明（Note）**：注意：传输驱动在任何情况下都不得覆盖 `use_polling` 参数的值，必须遵循此参数。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="a452deceb4eb343b19adf720eae7fb602"></a>

### `setup_chan`

```c
int(* scmi_transport_api::setup_chan) (const struct device *transport, struct scmi_channel *chan, bool tx)
```

准备通道以进行通信。

执行通道收发数据所需的各种初始化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 传输设备（Transport device）。 |
| `chan` | 要准备的通道。 |
| `tx` | 通道为发送通道时取 `true`，为接收通道时取 `false`。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/transport.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/transport.h](https://docs.zephyrproject.org/latest/doxygen/html/transport_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [scmi_channel](P033_scmi_channel_结构体.md)
- [scmi_message](P037_scmi_message_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_scmi_system_power_state_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_secure_storage_its_uid_t_结构体.md)
