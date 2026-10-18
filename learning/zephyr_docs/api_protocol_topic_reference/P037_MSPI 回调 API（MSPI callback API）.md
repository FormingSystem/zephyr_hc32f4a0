---
id: learning.zephyr-docs.api-protocol-topic-reference.page-37
title: MSPI 回调 API（MSPI callback API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_MSPI 回调 API（MSPI callback API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI 回调 API（MSPI callback API）

<a id="details"></a>

MSPI 回调 API（MSPI callback API）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 37.1\_数据结构（Data Structures）

<a id="r_mspi_5Fevent_5Fdata"></a>

```c
struct mspi_event_data
```

相关声明：[mspi_event_data](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md)。

MSPI事件数据（Event Data）。

<a id="r_mspi_5Fevent"></a>

```c
struct mspi_event
```

相关声明：[mspi_event](../peripheral_bus_storage_model_reference/P045_mspi_event_结构体.md)。

MSPI事件（Event）。

<a id="r_mspi_5Fcallback_5Fcontext"></a>

```c
struct mspi_callback_context
```

相关声明：[mspi_callback_context](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md)。

MSPI回调上下文（Callback Context）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 37.2\_类型定义（Typedefs）

<a id="r_ga29421f748fdb89c823e1a48ff69cf0f4"></a>

```c
typedef void(* mspi_callback_handler_t) (struct mspi_callback_context *mspi_cb_ctx,...)
```

相关声明：[mspi_callback_handler_t](#ga29421f748fdb89c823e1a48ff69cf0f4)、[mspi_callback_context](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md)。

定义应用程序回调处理函数的签名（Function Signature）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 37.3\_函数（Functions）

<a id="r_ga967f5fed63f08ac2d5a88625b030cd14"></a>

```c
static int mspi_register_callback (const struct device *controller, const struct mspi_dev_id *dev_id, const enum mspi_bus_event evt_type, mspi_callback_handler_t cb, struct mspi_callback_context *ctx)
```

相关声明：[mspi_register_callback](#ga967f5fed63f08ac2d5a88625b030cd14)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5)、[mspi_callback_handler_t](#ga29421f748fdb89c823e1a48ff69cf0f4)、[mspi_callback_context](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md)。

注册 MSPI 回调函数。

## 37.4\_详细说明（Detailed Documentation）

<a id="ga29421f748fdb89c823e1a48ff69cf0f4"></a>

### `mspi_callback_handler_t`

```c
typedef void(* mspi_callback_handler_t) (struct mspi_callback_context *mspi_cb_ctx,...)
```

```c
#include <zephyr/drivers/mspi.h>
```

定义应用程序回调处理函数的签名（Function Signature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mspi_cb_ctx` | 指向多位 SPI（MSPI）回调上下文的指针。 |

<a id="ga967f5fed63f08ac2d5a88625b030cd14"></a>

### `mspi_register_callback()`

```c
int mspi_register_callback ( const struct device * controller, const struct mspi_dev_id * dev_id, const enum mspi_bus_event evt_type, mspi_callback_handler_t cb, struct mspi_callback_context * ctx )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/mspi.h>
```

注册 MSPI 回调函数。

此例程提供注册 MSPI 回调函数的通用接口。通常应在 `mspi_transceive` 之前调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `controller` | 指向驱动实例的设备结构（Device Structure）。 |
| `dev_id` | 指向设备的设备 ID 结构体的指针。 |
| `evt_type` | 与该回调关联的事件类型（event type）。 |
| `cb` | 指向用户实现的回调函数的指针。 |
| `ctx` | 指向回调上下文（callback context）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOTSUP` |  |


## 37.5\_原页交叉引用（Cross References）

- [mspi_event_data](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md)
- [mspi_event](../peripheral_bus_storage_model_reference/P045_mspi_event_结构体.md)
- [mspi_callback_context](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)
- [mspi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5)
- [zephyr/drivers/mspi.h](../peripheral_bus_storage_header_reference/P017_zephyr__drivers__mspi.h_头文件参考.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P036_分流器（Tee）.md) · [返回大纲](大纲.md) · [下一章](P038_IPv4 网络地址转换（Network Address Translation）.md)
