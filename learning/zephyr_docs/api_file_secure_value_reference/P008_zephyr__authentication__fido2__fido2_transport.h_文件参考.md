---
id: learning.zephyr-docs.api-file-secure-value-reference.page-8
title: zephyr__authentication__fido2__fido2_transport.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_authentication\_\_fido2\_\_fido2\_transport.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FIDO2传输抽象（Transport Abstraction）的API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/authentication/fido2/fido2_types.h>
#include <stddef.h>
#include <stdint.h>
```

查看此文件的源码。

FIDO2传输抽象（Transport Abstraction）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_fido2_5Ftransport_5Fapi"></a>

```c
struct fido2_transport_api
```

相关声明：[fido2_transport_api](../platform_security_model_reference/P011_fido2_transport_api_结构体.md)。

传输驱动（Transport Driver）的API回调。

<a id="r_fido2_5Ftransport"></a>

```c
struct fido2_transport
```

相关声明：[fido2_transport](../platform_security_model_reference/P010_fido2_transport_结构体.md)。

已注册的FIDO2传输（Transport）。

<a id="r_aaca1dbd2854544f0c691d7eba104a065"></a>

```c
#define FIDO2_BLE_SERVICE_UUID_VAL 0xFFFDU
```

相关声明：[FIDO2_BLE_SERVICE_UUID_VAL](#aaca1dbd2854544f0c691d7eba104a065)。

快速身份认证低功耗蓝牙服务（FIDO BLE Service）的 UUID 值。

<a id="r_a5e293d6509138c129b1f8c78b27cec45"></a>

```c
#define FIDO2_BLE_SERVICE_DATA_PAIRING_MODE BIT(7)
```

相关声明：[FIDO2_BLE_SERVICE_DATA_PAIRING_MODE](#a5e293d6509138c129b1f8c78b27cec45)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

FIDO 配对模式（Pairing Mode）的位位置。

<a id="r_a146a5108012a6b5092458cc1e14340c8"></a>

```c
#define FIDO2_TRANSPORT_DEFINE(_name, _label, _api)
```

相关声明：[FIDO2_TRANSPORT_DEFINE](#a146a5108012a6b5092458cc1e14340c8)。

注册 FIDO2 传输（Transport）。

<a id="r_a7d65ad137d8ce67f9af03a6f37d1720b"></a>

```c
enum fido2_wire_status { FIDO2_WIRE_STATUS_UP_NEEDED , FIDO2_WIRE_STATUS_PROCESSING , FIDO2_WIRE_STATUS_DONE }
```

相关声明：[fido2_wire_status](#a7d65ad137d8ce67f9af03a6f37d1720b)、[FIDO2_WIRE_STATUS_UP_NEEDED](#a7d65ad137d8ce67f9af03a6f37d1720baaa077f7facef9bf040cd0173f3e3cc61)、[FIDO2_WIRE_STATUS_PROCESSING](#a7d65ad137d8ce67f9af03a6f37d1720ba5106b64cfc0b02d2beeae5e2d84d0049)、[FIDO2_WIRE_STATUS_DONE](#a7d65ad137d8ce67f9af03a6f37d1720bab4d2bd4f1f2c898cf706afbb12c43b8a)。

传输进度状态码（Transport Progress Status Codes）。

<a id="r_af8365317181d301d3f44fd3eb9416475"></a>

```c
typedef int(* fido2_transport_recv_cb_t) (const struct fido2_transport *transport, uint32_t cid, const uint8_t *buf, size_t len)
```

相关声明：[fido2_transport_recv_cb_t](#af8365317181d301d3f44fd3eb9416475)、[fido2_transport](../platform_security_model_reference/P010_fido2_transport_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

传输从主机收到数据时调用的回调（Callback）。

<a id="r_a081a49ee568a0939254bc640b509c3f8"></a>

```c
typedef void(* fido2_transport_cancel_cb_t) (const struct fido2_transport *transport)
```

相关声明：[fido2_transport_cancel_cb_t](#a081a49ee568a0939254bc640b509c3f8)、[fido2_transport](../platform_security_model_reference/P010_fido2_transport_结构体.md)。

传输收到取消命令（Cancel Command）时调用的回调。

## 8.2\_详细说明（Detailed Documentation）

<a id="a5e293d6509138c129b1f8c78b27cec45"></a>

### `FIDO2_BLE_SERVICE_DATA_PAIRING_MODE`

```c
#define FIDO2_BLE_SERVICE_DATA_PAIRING_MODE BIT(7)
```

FIDO 配对模式（Pairing Mode）的位位置。

<a id="aaca1dbd2854544f0c691d7eba104a065"></a>

### `FIDO2_BLE_SERVICE_UUID_VAL`

```c
#define FIDO2_BLE_SERVICE_UUID_VAL 0xFFFDU
```

快速身份认证低功耗蓝牙服务（FIDO BLE Service）的 UUID 值。

<a id="a146a5108012a6b5092458cc1e14340c8"></a>

### `FIDO2_TRANSPORT_DEFINE`

```c
#define FIDO2_TRANSPORT_DEFINE ( _name, _label, _api )
```

展开值（Value）：

```c
STRUCT_SECTION_ITERABLE(fido2_transport, _name) = {                                        \
        .name = _label,                                                                    \
        .api = _api,                                                                       \
}
```

注册 FIDO2 传输（Transport）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 此传输实例的 C 标识符（C Identifier）。 |
| `_label` | 可读的名称字符串（Human-readable Name String），例如 `"USB_HID"`。 |
| `_api` | 指向该传输的 `fido2_transport_api` 的指针。 |

<a id="a081a49ee568a0939254bc640b509c3f8"></a>

### `fido2_transport_cancel_cb_t`

```c
typedef void(* fido2_transport_cancel_cb_t) (const struct fido2_transport *transport)
```

传输收到取消命令（Cancel Command）时调用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 收到取消命令的传输实例（Transport Instance）。 |

<a id="af8365317181d301d3f44fd3eb9416475"></a>

### `fido2_transport_recv_cb_t`

```c
typedef int(* fido2_transport_recv_cb_t) (const struct fido2_transport *transport, uint32_t cid, const uint8_t *buf, size_t len)
```

传输从主机收到数据时调用的回调（Callback）。

在传输内部工作队列线程（Work Queue Thread）中执行，而非 FIDO2 核心线程。不得阻塞；实现应将工作入队并立即返回。不能从用户空间（Userspace）调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 收到数据的传输实例（Transport Instance）。 |
| `cid` | 与已接收消息关联的传输通道 ID（Transport Channel ID）。 |
| `buf` | 收到的数据有效载荷（Data Payload）。 |
| `len` | 收到的数据长度，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EMSGSIZE` | 消息大于消息队列（Message Queue）允许大小时。 |
| `-ENOBUFS` | 消息队列已满，或另一个传输上已有活动操作时。 |

<a id="a7d65ad137d8ce67f9af03a6f37d1720b"></a>

### `fido2_wire_status`

```c
enum fido2_wire_status
```

传输进度状态码（Transport Progress Status Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FIDO2_WIRE_STATUS_UP_NEEDED` | 认证器（Authenticator）正在等待证明用户在场的操作（User Presence Gesture）。 |
| `FIDO2_WIRE_STATUS_PROCESSING` | 长时间运行的操作（Long-running Operation）已开始，例如密码运算或存储。 |
| `FIDO2_WIRE_STATUS_DONE` | 操作已完成（Complete）。 |


## 8.3\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/authentication/fido2/fido2_types.h](../api_source_reference/P262_fido2_types.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P261_fido2_transport.h_源码浏览.md)
- [fido2_transport_api](../platform_security_model_reference/P011_fido2_transport_api_结构体.md)
- [fido2_transport](../platform_security_model_reference/P010_fido2_transport_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructfido2__transport_html"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a7d65ad137d8ce67f9af03a6f37d1720baaa077f7facef9bf040cd0173f3e3cc61"></a>
<a id="a7d65ad137d8ce67f9af03a6f37d1720ba5106b64cfc0b02d2beeae5e2d84d0049"></a>
<a id="a7d65ad137d8ce67f9af03a6f37d1720bab4d2bd4f1f2c898cf706afbb12c43b8a"></a>

---

[上一章](P007_zephyr__drivers__sensor__adxl355.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__mpipe__mpipe_value.h_文件参考.md)
