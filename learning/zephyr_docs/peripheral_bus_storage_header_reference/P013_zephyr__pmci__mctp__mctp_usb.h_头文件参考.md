---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-13
title: zephyr__pmci__mctp__mctp_usb.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__usb_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_pmci\_\_mctp\_\_mctp\_usb.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mctp__usb_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于Zephyr USB设备协议栈的MCTP总线绑定（Bus Binding）。

<a id="details"></a>

```c
#include <zephyr/sys/iterable_sections.h>
#include <libmctp.h>
```

查看此文件的源码。

基于Zephyr USB设备协议栈的MCTP总线绑定（Bus Binding）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.1\_数据结构（Data Structures）

<a id="r_mctp_5Fbinding_5Fusb"></a>

```c
struct mctp_binding_usb
```

相关声明：[mctp_binding_usb](../peripheral_bus_storage_model_reference/P031_mctp_binding_usb_结构体.md)。

内部隐藏标记（INTERNAL_HIDDEN）。

<a id="r_mctp_5Fusb_5Fclass_5Finst"></a>

```c
struct mctp_usb_class_inst
```

相关声明：[mctp_usb_class_inst](../peripheral_bus_storage_model_reference/P032_mctp_usb_class_inst_结构体.md)。

管理组件传输协议（MCTP）的USB类实例配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.2\_宏定义（Macros）

<a id="r_a6bbe1dbce33e8e4a47b2d6a604bfa364"></a>

```c
#define MCTP_USB_DEFINE(_name, _subclass, _protocol)
```

相关声明：[MCTP_USB_DEFINE](#a6bbe1dbce33e8e4a47b2d6a604bfa364)。

内部隐藏标记（INTERNAL_HIDDEN）。

<a id="define-members-0"></a>

### MCTP 类的子类选项（Class subclass options）

`MCTP_USB_DEFINE()` 的 `subclass` 参数接受的值。

<a id="r_ad4bfc1fda8e8f9a17d0ff1aabc8dd907"></a>

```c
#define USBD_MCTP_SUBCLASS_MANAGEMENT_CONTROLLER 0
```

相关声明：[USBD_MCTP_SUBCLASS_MANAGEMENT_CONTROLLER](#ad4bfc1fda8e8f9a17d0ff1aabc8dd907)。

管理控制器（Management controller）。

<a id="r_a0dc7e1a0bb8477ee95d8d9a2228d7b5c"></a>

```c
#define USBD_MCTP_SUBCLASS_MANAGED_DEVICE_ENDPOINT 0
```

相关声明：[USBD_MCTP_SUBCLASS_MANAGED_DEVICE_ENDPOINT](#a0dc7e1a0bb8477ee95d8d9a2228d7b5c)。

受管设备端点（Managed device endpoint）。

<a id="r_aeba3f4f4bdb975ed0ea6cf6c1b4218c4"></a>

```c
#define USBD_MCTP_SUBCLASS_HOST_INTERFACE_ENDPOINT 1
```

相关声明：[USBD_MCTP_SUBCLASS_HOST_INTERFACE_ENDPOINT](#aeba3f4f4bdb975ed0ea6cf6c1b4218c4)。

主机接口端点（Host interface endpoint）。

<a id="define-members-1"></a>

### MCTP 类协议选项（Class protocol options）

`MCTP_USB_DEFINE()` 的 `protocol` 参数接受的值。

<a id="r_a5fa986e3261302dea383144234a8de09"></a>

```c
#define USBD_MCTP_PROTOCOL_1_X 1
```

相关声明：[USBD_MCTP_PROTOCOL_1_X](#a5fa986e3261302dea383144234a8de09)。

MCTP 协议版本 1.x。

<a id="r_ae23a15b09b00958e49a065eeda96254a"></a>

```c
#define USBD_MCTP_PROTOCOL_2_X 2
```

相关声明：[USBD_MCTP_PROTOCOL_2_X](#ae23a15b09b00958e49a065eeda96254a)。

MCTP 协议版本 2.x。

## 13.3\_详细说明（Detailed Documentation）

<a id="a6bbe1dbce33e8e4a47b2d6a604bfa364"></a>

### `MCTP_USB_DEFINE`

```c
#define MCTP_USB_DEFINE ( _name, _subclass, _protocol )
```

展开值（Value）：

```c
struct mctp_binding_usb _name = {                                                       \
        .binding = {                                                                    \
                .name = STRINGIFY(_name),                                               \
                .version = 1,                                                           \
                .pkt_size = MCTP_PACKET_SIZE(MCTP_USB_MAX_PACKET_LENGTH),               \
                .pkt_header = 0,                                                        \
                .pkt_trailer = 0,                                                       \
                .tx_storage = _name.tx_storage,                                         \
                .start = mctp_usb_start,                                                \
                .tx = mctp_usb_tx                                                       \
        },                                                                              \
        .usb_class_data = NULL,                                                         \
        .rx_pkt = NULL,                                                                 \
        .rx_data_idx = 0,                                                               \
        .rx_state = STATE_WAIT_HDR_DMTF0                                                \
};                                                                                      \
                                                                                        \
const STRUCT_SECTION_ITERABLE(mctp_usb_class_inst, mctp_usb_class_inst_##_name) = {     \
        .subclass = _subclass,                                                          \
        .mctp_protocol = _protocol,                                                     \
        .mctp_binding = &_name,                                                         \
};
```

内部隐藏标记（INTERNAL_HIDDEN）。

定义 USB 的 MCTP 总线绑定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 总线绑定变量的符号名称（Symbolic name）。 |
| `_subclass` | USB 接口描述符中使用的 MCTP 子类（Subclass）。 |
| `_protocol` | USB 接口描述符中使用的 MCTP 协议。 |

<a id="a5fa986e3261302dea383144234a8de09"></a>

### `USBD_MCTP_PROTOCOL_1_X`

```c
#define USBD_MCTP_PROTOCOL_1_X 1
```

MCTP 协议版本 1.x。

<a id="ae23a15b09b00958e49a065eeda96254a"></a>

### `USBD_MCTP_PROTOCOL_2_X`

```c
#define USBD_MCTP_PROTOCOL_2_X 2
```

MCTP 协议版本 2.x。

<a id="aeba3f4f4bdb975ed0ea6cf6c1b4218c4"></a>

### `USBD_MCTP_SUBCLASS_HOST_INTERFACE_ENDPOINT`

```c
#define USBD_MCTP_SUBCLASS_HOST_INTERFACE_ENDPOINT 1
```

主机接口端点（Host interface endpoint）。

<a id="a0dc7e1a0bb8477ee95d8d9a2228d7b5c"></a>

### `USBD_MCTP_SUBCLASS_MANAGED_DEVICE_ENDPOINT`

```c
#define USBD_MCTP_SUBCLASS_MANAGED_DEVICE_ENDPOINT 0
```

受管设备端点（Managed device endpoint）。

<a id="ad4bfc1fda8e8f9a17d0ff1aabc8dd907"></a>

### `USBD_MCTP_SUBCLASS_MANAGEMENT_CONTROLLER`

```c
#define USBD_MCTP_SUBCLASS_MANAGEMENT_CONTROLLER 0
```

管理控制器（Management controller）。


## 13.4\_原页交叉引用（Cross References）

- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/mctp__usb_8h_source.html)
- [mctp_binding_usb](../peripheral_bus_storage_model_reference/P031_mctp_binding_usb_结构体.md)
- [mctp_usb_class_inst](../peripheral_bus_storage_model_reference/P032_mctp_usb_class_inst_结构体.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructmctp__binding__usb_html"></a>

---

[上一章](P012_zephyr__pmci__mctp__mctp_uart.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__drivers__memc.h_头文件参考.md)
