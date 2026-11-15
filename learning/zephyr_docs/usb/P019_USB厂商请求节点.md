---
id: learning.zephyr-docs.usb.api-19
title: USB厂商请求节点
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__vreq__node.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_USB厂商请求节点

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__vreq__node.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 19.1\_阅读说明与来源

译注：本页是[USB设备核心API](P015_USB设备核心API.md)的数据结构参考，说明描述符、配置、上下文与类实例的成员。字段声明和原注释按官方页面保留；内部类型或回调约定的补充明确标为源码译注。

[本册大纲](大纲.md)提供本组第18至28章的全部字段参考。

USBD 厂商请求节点（Vendor Request Node）。

```c
#include <zephyr/usb/usbd.h>
```

USBD 厂商请求节点（Vendor Request Node）。

厂商请求节点由厂商代码标识，用于注册处理以设备为接收方的厂商请求的回调。当设备栈收到类型为 Vendor、接收方为 Device，且 `bRequest` 等于该厂商请求代码的请求时，会根据请求方向调用对应厂商回调。

回调代码片段示例：

```c
static struct net_buf *foo_to_host_cb(const struct usbd_context *const ctx,
                                      const struct usb_setup_packet *const setup)
{
    if (setup->wIndex == WEBUSB_REQ_GET_URL) {
        struct net_buf *buf;
        uint16_t len;
        uint8_t index = USB_GET_DESCRIPTOR_INDEX(setup->wValue);

        if (index != SAMPLE_WEBUSB_LANDING_PAGE) {
            return NULL;
        }

        len = MIN(setup->wLength, sizeof(webusb_origin_url));
        buf = usbd_ep_ctrl_data_in_alloc(ctx, len);
        if (buf == NULL) {
            return NULL;
        }

        net_buf_add_mem(buf, &webusb_origin_url, len);

        return buf;
    }

    return NULL;
}
```

## 19.2\_数据成员（Data Fields）

<a id="r_a3c68346e2f871b22fb6c3b282ddfdccb"></a>

```c
sys_dnode_t node
```

双向链表（dlist）的节点信息。

相关声明：[sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)、[node](P019_USB厂商请求节点.md#a3c68346e2f871b22fb6c3b282ddfdccb)。

<a id="r_a91fe4c5cf5ccad89e81380a332a8f955"></a>

```c
const uint8_t code
```

厂商代码，即 `bRequest` 的值。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[code](P019_USB厂商请求节点.md#a91fe4c5cf5ccad89e81380a332a8f955)。

<a id="r_ab684d5065a5fcd762fcde4ceb4fb7a54"></a>

```c
struct net_buf *(* to_host )(const struct usbd_context *const ctx, const struct usb_setup_packet *const setup)
```

设备到主机方向的厂商请求回调。

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[to_host](P019_USB厂商请求节点.md#ab684d5065a5fcd762fcde4ceb4fb7a54)、[usbd_context](P025_USB设备上下文结构.md)、[usb_setup_packet](P160_USB控制请求包.md)。

<a id="r_ae69e3dd3b4cdc7deb1ccdd9d9ebe4ec3"></a>

```c
int(* to_dev )(const struct usbd_context *const ctx, const struct usb_setup_packet *const setup, const struct net_buf *const buf)
```

主机到设备方向的厂商请求回调。

相关声明：[to_dev](P019_USB厂商请求节点.md#ae69e3dd3b4cdc7deb1ccdd9d9ebe4ec3)、[usbd_context](P025_USB设备上下文结构.md)、[usb_setup_packet](P160_USB控制请求包.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

## 19.3\_详细说明（Detailed Documentation）

<a id="a91fe4c5cf5ccad89e81380a332a8f955"></a>

### `code`

```c
const uint8_t usbd_vreq_node::code
```

厂商代码，即 `bRequest` 的值。

<a id="a3c68346e2f871b22fb6c3b282ddfdccb"></a>

### `node`

```c
sys_dnode_t usbd_vreq_node::node
```

双向链表（dlist）的节点信息。

<a id="ae69e3dd3b4cdc7deb1ccdd9d9ebe4ec3"></a>

### `to_dev`

```c
int(* usbd_vreq_node::to_dev) (const struct usbd_context *const ctx, const struct usb_setup_packet *const setup, const struct net_buf *const buf)
```

主机到设备方向的厂商请求回调。

对于带有数据 OUT 阶段（Data OUT Stage，即 `wLength != 0`）的请求，在接收数据前会先以 `buf = NULL` 调用回调，检查是否应接收数据。数据接收完成后，回调会被再次调用，此时 `buf` 非空。

对于不含数据阶段（Data Stage，即 `wLength == 0`）的请求，只会以 `buf = NULL` 调用一次回调。

> 译注（源码核对）：带 OUT 数据的请求有“接收前检查”和“接收后处理”两次调用。第一次 buf 为 NULL 不代表请求失败，不能直接解引用；无数据阶段时则只有一次 NULL 调用。该约定按原文保留，不应把两个阶段当成两次独立请求。

<a id="ab684d5065a5fcd762fcde4ceb4fb7a54"></a>

### `to_host`

```c
struct net_buf *(* usbd_vreq_node::to_host) (const struct usbd_context *const ctx, const struct usb_setup_packet *const setup)
```

设备到主机方向的厂商请求回调。

> 译注（源码核对）：上方示例核对 wIndex 与 wValue 中的描述符索引，再用主机要求长度与实际 URL 描述符大小的较小值分配并填充缓冲区。WEBUSB_REQ_GET_URL、SAMPLE_WEBUSB_LANDING_PAGE 和 webusb_origin_url 由完整应用提供；代码片段本身不是可独立编译的程序。

## 19.4\_相关源码与使用边界

本页结构定义来自 `zephyr/usb/usbd.h`；本仓库的[对应头文件](../../../include/zephyr/usb/usbd.h)、[类回调包装接口](../../../subsys/usb/device_next/usbd_class_api.h)、[第9章控制请求处理](../../../subsys/usb/device_next/usbd_ch9.c)及[初始化实现](../../../subsys/usb/device_next/usbd_init.c)可用于源码跟踪，版本可能与官网 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[回调接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class_api.h)、[控制请求实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)、[描述符管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_desc.c)和[初始化实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_init.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="agroup__net__buf_html_gacf4e2eba52975ba6728c79274a769d0f"></a>
<a id="agroup__sys-util_html_ga3acffbd305ee72dcd4593c0d8af64a4f"></a>
<a id="agroup__usbd__api_html_ga1ce934ca354853ec9c7c295cca2d0e3d"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructnet__buf_html"></a>
<a id="astructusb__setup__packet_html"></a>
<a id="astructusb__setup__packet_html_a3421c921569bf3727534652c5f71da96"></a>
<a id="astructusb__setup__packet_html_a619fbc1b9b6452f4394da713bdbc6a89"></a>
<a id="astructusb__setup__packet_html_a953c058f0e31481a3d59b404037be009"></a>
<a id="astructusbd__context_html"></a>
<a id="ausb__ch9_8h_html_a653a141a5084536362396149e81b6b9a"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P018_USB字符串描述符数据.md) · [返回大纲](大纲.md) · [下一章](P020_USBBOS能力描述符数据.md)
