---
id: learning.zephyr-docs.usb.api-152
title: 旧版USB控制器驱动API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group____usb__device__controller__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第152章\_旧版USB控制器驱动API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group____usb__device__controller__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 152.1\_阅读说明与来源

译注：本页说明旧版USB设备控制器驱动API（usb_dc）。它与新版USB设备控制器（USB Device Controller，UDC）API不同；原文的弃用标记与完整接口声明均保留。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 设备控制器（USB Device Controller）API。

USB 设备控制器（USB Device Controller）API。

引入版本（Since）：1.5。

接口版本（Version）：1.0.0。

## 152.2\_数据结构（Data Structures）

<a id="r_usb_5Fdc_5Fep_5Fcfg_5Fdata"></a>

```c
struct usb_dc_ep_cfg_data
```

USB 端点配置（Endpoint Configuration）。

相关声明：[usb_dc_ep_cfg_data](P153_旧版USB端点配置结构.md)。

## 152.3\_类型定义（Typedefs）

<a id="r_gad75ee35cdfb5dc4f1fad0e615067cb70"></a>

```c
typedef void(* usb_dc_ep_callback) (uint8_t ep, enum usb_dc_ep_cb_status_code cb_status)
```

USB 端点状态回调的函数签名。

相关声明：[usb_dc_ep_callback](P152_旧版USB控制器驱动API.md#gad75ee35cdfb5dc4f1fad0e615067cb70)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[usb_dc_ep_cb_status_code](P152_旧版USB控制器驱动API.md#gaf7f083f61e1406e7d41513113dccd3bd)。

<a id="r_ga2ddb0b059b4e1e76473ed7f56d0cf2ee"></a>

```c
typedef void(* usb_dc_status_callback) (enum usb_dc_status_code cb_status, const uint8_t *param)
```

设备回调的函数签名。

相关声明：[usb_dc_status_callback](P152_旧版USB控制器驱动API.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee)、[usb_dc_status_code](P152_旧版USB控制器驱动API.md#gac09e3e0af1a2b41a5bfbad91f900baf7)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

## 152.4\_枚举（Enumerations）

<a id="r_gac09e3e0af1a2b41a5bfbad91f900baf7"></a>

```c
enum usb_dc_status_code {
    USB_DC_ERROR,
    USB_DC_RESET,
    USB_DC_CONNECTED,
    USB_DC_CONFIGURED,
    USB_DC_DISCONNECTED,
    USB_DC_SUSPEND,
    USB_DC_RESUME,
    USB_DC_INTERFACE,
    USB_DC_SET_HALT,
    USB_DC_CLEAR_HALT,
    USB_DC_SOF,
    USB_DC_UNKNOWN
}
```

USB 驱动状态码（Driver Status Codes）。

相关声明：[usb_dc_status_code](P152_旧版USB控制器驱动API.md#gac09e3e0af1a2b41a5bfbad91f900baf7)、[USB_DC_ERROR](P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a8c34e2279a64268809170d6b7f08ed14)、[USB_DC_RESET](P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a6486b0e1a9f4c68fd3bc3b6b3354daa6)、[USB_DC_CONNECTED](P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a643918c145a481a36bda37ae5b36599f)、[USB_DC_CONFIGURED](P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a63372b97af29a434d58a970439afc23f)、[USB_DC_DISCONNECTED](P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a3584740de2622bf915e67fee6104da4c)、[USB_DC_SUSPEND](P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7afb40fc53f01c4e947a7d4c85a1a21c87)、[USB_DC_RESUME](P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a306cbcf313be2111434f3e29b787de1d)、[USB_DC_INTERFACE](P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a65828d350f0cd42be7f8406624eb3828)、[USB_DC_SET_HALT](P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a426477e3ab4378cb0783523346e5ff23)、[USB_DC_CLEAR_HALT](P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a25d070f91c1e3ff0382b360f5ac2d501)、[USB_DC_SOF](P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7abe89e0ffc160ffd1d8ae88d3771fcbc0)、[USB_DC_UNKNOWN](P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a8a0f6af1f3625530c9ecdfb2409205d9)。

<a id="r_gaf7f083f61e1406e7d41513113dccd3bd"></a>

```c
enum usb_dc_ep_cb_status_code {
    USB_DC_EP_SETUP,
    USB_DC_EP_DATA_OUT,
    USB_DC_EP_DATA_IN
}
```

USB 端点回调状态码（Endpoint Callback Status Codes）。

相关声明：[usb_dc_ep_cb_status_code](P152_旧版USB控制器驱动API.md#gaf7f083f61e1406e7d41513113dccd3bd)、[USB_DC_EP_SETUP](P152_旧版USB控制器驱动API.md#ggaf7f083f61e1406e7d41513113dccd3bdabeb0ca69354218c5efc14c4ddbdf1c27)、[USB_DC_EP_DATA_OUT](P152_旧版USB控制器驱动API.md#ggaf7f083f61e1406e7d41513113dccd3bda1801d1ba252ed6a0e573c46e76ae1f78)、[USB_DC_EP_DATA_IN](P152_旧版USB控制器驱动API.md#ggaf7f083f61e1406e7d41513113dccd3bdae2f497d34e18d6431ab886d120bd124c)。

<a id="r_gaca68e4a7c3c0a984d1df23794cfa7d87"></a>

```c
enum usb_dc_ep_transfer_type {
    USB_DC_EP_CONTROL = 0,
    USB_DC_EP_ISOCHRONOUS,
    USB_DC_EP_BULK,
    USB_DC_EP_INTERRUPT
}
```

USB 端点传输类型（Endpoint Transfer Type）。

相关声明：[usb_dc_ep_transfer_type](P152_旧版USB控制器驱动API.md#gaca68e4a7c3c0a984d1df23794cfa7d87)、[USB_DC_EP_CONTROL](P152_旧版USB控制器驱动API.md#ggaca68e4a7c3c0a984d1df23794cfa7d87a10c7e329a8eceb8cc693b77743f43681)、[USB_DC_EP_ISOCHRONOUS](P152_旧版USB控制器驱动API.md#ggaca68e4a7c3c0a984d1df23794cfa7d87a75c49ff44a9729723af190640a710ab6)、[USB_DC_EP_BULK](P152_旧版USB控制器驱动API.md#ggaca68e4a7c3c0a984d1df23794cfa7d87aa0ecbc47a337243efd86155cb4ca54fe)、[USB_DC_EP_INTERRUPT](P152_旧版USB控制器驱动API.md#ggaca68e4a7c3c0a984d1df23794cfa7d87aa70b161209601f1d7a43c5ebcc197b73)。

<a id="r_gae247c1ce7213e35d7ce74598225fa428"></a>

```c
enum usb_dc_ep_synchronozation_type {
    USB_DC_EP_NO_SYNCHRONIZATION = (0U << 2U),
    USB_DC_EP_ASYNCHRONOUS = (1U << 2U),
    USB_DC_EP_ADAPTIVE = (2U << 2U),
    USB_DC_EP_SYNCHRONOUS = (3U << 2U)
}
```

USB 端点同步类型（Endpoint Synchronization Type）。

相关声明：[usb_dc_ep_synchronozation_type](P152_旧版USB控制器驱动API.md#gae247c1ce7213e35d7ce74598225fa428)、[USB_DC_EP_NO_SYNCHRONIZATION](P152_旧版USB控制器驱动API.md#ggae247c1ce7213e35d7ce74598225fa428a98061a0e90201b01c7b9b04b51eb0da8)、[USB_DC_EP_ASYNCHRONOUS](P152_旧版USB控制器驱动API.md#ggae247c1ce7213e35d7ce74598225fa428a8cb40e0f2b85da1adfc005fbd5f9f45d)、[USB_DC_EP_ADAPTIVE](P152_旧版USB控制器驱动API.md#ggae247c1ce7213e35d7ce74598225fa428a13e7d8970d0723b36a17ae8a29dc9151)、[USB_DC_EP_SYNCHRONOUS](P152_旧版USB控制器驱动API.md#ggae247c1ce7213e35d7ce74598225fa428a70976afffbf9a9ef89eb51453c4307c5)。

## 152.5\_函数（Functions）

<a id="r_gaf78984e6103185c6ebadee2fcbdf62f7"></a>

```c
int usb_dc_attach (void)
```

连接 USB，以建立设备连接。

相关声明：[usb_dc_attach](P152_旧版USB控制器驱动API.md#gaf78984e6103185c6ebadee2fcbdf62f7)。

<a id="r_ga062b4c8b618f2e964984786baf635a93"></a>

```c
int usb_dc_detach (void)
```

断开 USB 设备。

相关声明：[usb_dc_detach](P152_旧版USB控制器驱动API.md#ga062b4c8b618f2e964984786baf635a93)。

<a id="r_ga8a72b00cfa90dcde41daa228791b61da"></a>

```c
int usb_dc_reset (void)
```

复位 USB 设备。

相关声明：[usb_dc_reset](P152_旧版USB控制器驱动API.md#ga8a72b00cfa90dcde41daa228791b61da)。

<a id="r_ga54a8280e4b011eff3640f6d21af1c292"></a>

```c
int usb_dc_set_address (const uint8_t addr)
```

设置 USB 设备地址。

相关声明：[usb_dc_set_address](P152_旧版USB控制器驱动API.md#ga54a8280e4b011eff3640f6d21af1c292)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga478eb2e57635ea816fd6acc8cb9a9424"></a>

```c
void usb_dc_set_status_callback (const usb_dc_status_callback cb)
```

设置 USB 设备控制器状态回调。

相关声明：[usb_dc_set_status_callback](P152_旧版USB控制器驱动API.md#ga478eb2e57635ea816fd6acc8cb9a9424)、[usb_dc_status_callback](P152_旧版USB控制器驱动API.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee)。

<a id="r_gab6b9ca74059ff2285bd301e9264df45b"></a>

```c
int usb_dc_ep_check_cap (const struct usb_dc_ep_cfg_data *const cfg)
```

检查端点能力。

相关声明：[usb_dc_ep_check_cap](P152_旧版USB控制器驱动API.md#gab6b9ca74059ff2285bd301e9264df45b)、[usb_dc_ep_cfg_data](P153_旧版USB端点配置结构.md)。

<a id="r_ga858a4e1bf2c35f5a0ec333801e75b718"></a>

```c
int usb_dc_ep_configure (const struct usb_dc_ep_cfg_data *const cfg)
```

配置端点。

相关声明：[usb_dc_ep_configure](P152_旧版USB控制器驱动API.md#ga858a4e1bf2c35f5a0ec333801e75b718)、[usb_dc_ep_cfg_data](P153_旧版USB端点配置结构.md)。

<a id="r_ga68fcfcfe36a36cef202586686c5d30e3"></a>

```c
int usb_dc_ep_set_stall (const uint8_t ep)
```

为选定端点设置停滞状态（Stall）。

相关声明：[usb_dc_ep_set_stall](P152_旧版USB控制器驱动API.md#ga68fcfcfe36a36cef202586686c5d30e3)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gab89ebb3049f7fd7a1e764ffef16b1b64"></a>

```c
int usb_dc_ep_clear_stall (const uint8_t ep)
```

清除选定端点的停滞状态（Stall）。

相关声明：[usb_dc_ep_clear_stall](P152_旧版USB控制器驱动API.md#gab89ebb3049f7fd7a1e764ffef16b1b64)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gaff2d98b0b6d4ae409b9961a7a123b326"></a>

```c
int usb_dc_ep_is_stalled (const uint8_t ep, uint8_t *const stalled)
```

检查选定端点是否处于停滞状态（Stalled）。

相关声明：[usb_dc_ep_is_stalled](P152_旧版USB控制器驱动API.md#gaff2d98b0b6d4ae409b9961a7a123b326)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga821d65d9872ebb62bfaee79afbb80004"></a>

```c
int usb_dc_ep_halt (const uint8_t ep)
```

停止选定端点（Halt）。

相关声明：[usb_dc_ep_halt](P152_旧版USB控制器驱动API.md#ga821d65d9872ebb62bfaee79afbb80004)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga199aaf51e878cadc0e4ad65007a5a622"></a>

```c
int usb_dc_ep_enable (const uint8_t ep)
```

启用选定端点。

相关声明：[usb_dc_ep_enable](P152_旧版USB控制器驱动API.md#ga199aaf51e878cadc0e4ad65007a5a622)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga0154d6b5d462fa2a9db174a985259429"></a>

```c
int usb_dc_ep_disable (const uint8_t ep)
```

禁用选定端点。

相关声明：[usb_dc_ep_disable](P152_旧版USB控制器驱动API.md#ga0154d6b5d462fa2a9db174a985259429)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga8f702709dd2ed8257d61a8593c4c3b0d"></a>

```c
int usb_dc_ep_flush (const uint8_t ep)
```

清空选定端点。

相关声明：[usb_dc_ep_flush](P152_旧版USB控制器驱动API.md#ga8f702709dd2ed8257d61a8593c4c3b0d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gad0b822f08c4a29a46aaa8fa8b30d58ef"></a>

```c
int usb_dc_ep_write (const uint8_t ep, const uint8_t *const data, const uint32_t data_len, uint32_t *const ret_bytes)
```

向指定端点写入数据。

相关声明：[usb_dc_ep_write](P152_旧版USB控制器驱动API.md#gad0b822f08c4a29a46aaa8fa8b30d58ef)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_ga8b51a93295c7f9d3b15f4bfe8a09bb11"></a>

```c
int usb_dc_ep_read (const uint8_t ep, uint8_t *const data, const uint32_t max_data_len, uint32_t *const read_bytes)
```

从指定端点读取数据。

相关声明：[usb_dc_ep_read](P152_旧版USB控制器驱动API.md#ga8b51a93295c7f9d3b15f4bfe8a09bb11)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_gaba2134e2a7b8d870860903aead03b418"></a>

```c
int usb_dc_ep_set_callback (const uint8_t ep, const usb_dc_ep_callback cb)
```

设置指定端点的回调函数。

相关声明：[usb_dc_ep_set_callback](P152_旧版USB控制器驱动API.md#gaba2134e2a7b8d870860903aead03b418)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[usb_dc_ep_callback](P152_旧版USB控制器驱动API.md#gad75ee35cdfb5dc4f1fad0e615067cb70)。

<a id="r_ga012fb4d99870e1e30e0ecd4ac2b22312"></a>

```c
int usb_dc_ep_read_wait (uint8_t ep, uint8_t *data, uint32_t max_data_len, uint32_t *read_bytes)
```

从指定端点读取数据。

相关声明：[usb_dc_ep_read_wait](P152_旧版USB控制器驱动API.md#ga012fb4d99870e1e30e0ecd4ac2b22312)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_ga9694ad0cc1ee84a4ed9de4f2860d4ae6"></a>

```c
int usb_dc_ep_read_continue (uint8_t ep)
```

继续从端点读取数据。

相关声明：[usb_dc_ep_read_continue](P152_旧版USB控制器驱动API.md#ga9694ad0cc1ee84a4ed9de4f2860d4ae6)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga6e97104269bfe6dd08f5d0bbb791390e"></a>

```c
int usb_dc_ep_mps (uint8_t ep)
```

取得端点最大包大小（Maximum Packet Size，MPS）。

相关声明：[usb_dc_ep_mps](P152_旧版USB控制器驱动API.md#ga6e97104269bfe6dd08f5d0bbb791390e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga459110125c2a52da95b5b2c3c6fff096"></a>

```c
int usb_dc_wakeup_request (void)
```

启动唤醒主机的过程。

相关声明：[usb_dc_wakeup_request](P152_旧版USB控制器驱动API.md#ga459110125c2a52da95b5b2c3c6fff096)。

## 152.6\_详细说明（Detailed Documentation）

<a id="gad75ee35cdfb5dc4f1fad0e615067cb70"></a>

### 152.6.1\_`usb_dc_ep_callback`

```c
typedef void(* usb_dc_ep_callback) (uint8_t ep, enum usb_dc_ep_cb_status_code cb_status)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

USB 端点状态回调的函数签名。

<a id="ga2ddb0b059b4e1e76473ed7f56d0cf2ee"></a>

### 152.6.2\_`usb_dc_status_callback`

```c
typedef void(* usb_dc_status_callback) (enum usb_dc_status_code cb_status, const uint8_t *param)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

设备回调的函数签名。

<a id="gaf7f083f61e1406e7d41513113dccd3bd"></a>

### 152.6.3\_`usb_dc_ep_cb_status_code`

```c
enum usb_dc_ep_cb_status_code
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

USB 端点回调状态码（Endpoint Callback Status Codes）。

由已注册的端点回调报告的状态码。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_DC_EP_SETUP` | 收到 SETUP 事务。 |
| `USB_DC_EP_DATA_OUT` | 此端点发生 OUT 事务，有数据可供读取。 |
| `USB_DC_EP_DATA_IN` | 此端点的 IN 事务已完成。 |

<a id="gae247c1ce7213e35d7ce74598225fa428"></a>

### 152.6.4\_`usb_dc_ep_synchronozation_type`

```c
enum usb_dc_ep_synchronozation_type
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

USB 端点同步类型（Endpoint Synchronization Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_DC_EP_NO_SYNCHRONIZATION` | 无同步（No Synchronization）。 |
| `USB_DC_EP_ASYNCHRONOUS` | 异步（Asynchronous）。 |
| `USB_DC_EP_ADAPTIVE` | 自适应（Adaptive）。 |
| `USB_DC_EP_SYNCHRONOUS` | 同步（Synchronous）。 |

**注意（Note）**：仅对等时端点（Isochronous Endpoint）有效。

> 译注（源码核对）：synchronozation是原API标识符的拼写，代码中保持不变。同步方式枚举值已左移2位，对应等时端点属性；它与控制／等时／批量／中断的传输类型枚举不是同一概念，不能直接把同步位当作ep_type传入。

<a id="gaca68e4a7c3c0a984d1df23794cfa7d87"></a>

### 152.6.5\_`usb_dc_ep_transfer_type`

```c
enum usb_dc_ep_transfer_type
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

USB 端点传输类型（Endpoint Transfer Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_DC_EP_CONTROL` | 控制类型端点（Control）。 |
| `USB_DC_EP_ISOCHRONOUS` | 等时类型端点（Isochronous）。 |
| `USB_DC_EP_BULK` | 批量类型端点（Bulk）。 |
| `USB_DC_EP_INTERRUPT` | 中断类型端点（Interrupt）。 |

<a id="gac09e3e0af1a2b41a5bfbad91f900baf7"></a>

### 152.6.6\_`usb_dc_status_code`

```c
enum usb_dc_status_code
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

USB 驱动状态码（Driver Status Codes）。

由已注册的设备状态回调报告的状态码。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_DC_ERROR` | 控制器报告 USB 错误。 |
| `USB_DC_RESET` | USB 复位（Reset）。 |
| `USB_DC_CONNECTED` | USB 连接已建立，硬件枚举（Hardware Enumeration）完成。 |
| `USB_DC_CONFIGURED` | USB 配置完成。 |
| `USB_DC_DISCONNECTED` | USB 连接丢失。 |
| `USB_DC_SUSPEND` | 主机（Host）挂起 USB 连接。 |
| `USB_DC_RESUME` | 主机恢复 USB 连接。 |
| `USB_DC_INTERFACE` | 已选择 USB 接口。 |
| `USB_DC_SET_HALT` | 收到针对 ENDPOINT_HALT 的 Set Feature 请求。 |
| `USB_DC_CLEAR_HALT` | 收到针对 ENDPOINT_HALT 的 Clear Feature 请求。 |
| `USB_DC_SOF` | 收到帧起始（Start of Frame，SOF）。 |
| `USB_DC_UNKNOWN` | 初始 USB 连接状态。 |

> 译注（源码核对）：CONNECTED与CONFIGURED是两个不同事件。原注释对CONNECTED使用了“硬件枚举完成”的措辞，但旧版设备栈还在选择配置后独立报告USB_DC_CONFIGURED；不能仅凭连接事件认定应用端点已全部配置可用。

<a id="gaf78984e6103185c6ebadee2fcbdf62f7"></a>

### 152.6.7\_`usb_dc_attach()`

```c
int usb_dc_attach ( void )
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

连接 USB，以建立设备连接。

此函数连接 USB 以建立设备连接。成功后，USB 锁相环（Phase-Locked Loop，PLL）启用，USB 设备能够在总线上发送和接收数据，并产生中断。

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

> 译注（源码核对）：上方PLL和中断行为是原API的描述，实际时钟、引脚及供电操作由具体控制器驱动实现。这里的“连接”指控制器连接到USB总线，不等于主机已经选择设备配置。

<a id="ga062b4c8b618f2e964984786baf635a93"></a>

### 152.6.8\_`usb_dc_detach()`

```c
int usb_dc_detach ( void )
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

断开 USB 设备。

此函数断开 USB 设备。成功后，USB 硬件 PLL 断电，USB 通信被禁用。

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="gab6b9ca74059ff2285bd301e9264df45b"></a>

### 152.6.9\_`usb_dc_ep_check_cap()`

```c
int usb_dc_ep_check_cap ( const struct usb_dc_ep_cfg_data *const cfg)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

检查端点能力。

此函数检查端点能力。usb_dc_ep_cfg_data 结构提供端点地址、端点最大包大小及端点类型等配置参数。驱动应检查端点能力；如果能够采用该端点配置，则返回 0。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cfg` | 端点配置。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

> 译注（源码核对）：这是检查配置是否可行的接口，不代替usb_dc_ep_configure()及后续端点启用。驱动仍需按具体硬件核对端点方向、类型和最大包大小。

<a id="gab89ebb3049f7fd7a1e764ffef16b1b64"></a>

### 152.6.10\_`usb_dc_ep_clear_stall()`

```c
int usb_dc_ep_clear_stall ( const uint8_t ep)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

清除选定端点的停滞状态（Stall）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="ga858a4e1bf2c35f5a0ec333801e75b718"></a>

### 152.6.11\_`usb_dc_ep_configure()`

```c
int usb_dc_ep_configure ( const struct usb_dc_ep_cfg_data *const cfg)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

配置端点。

此函数配置端点。usb_dc_ep_cfg_data 结构提供端点地址、端点最大包大小和端点类型等配置参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cfg` | 端点配置。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="ga0154d6b5d462fa2a9db174a985259429"></a>

### 152.6.12\_`usb_dc_ep_disable()`

```c
int usb_dc_ep_disable ( const uint8_t ep)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

禁用选定端点。

此函数禁用选定端点。成功后，相应端点的中断被禁用，该端点不再能够发送或接收数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="ga199aaf51e878cadc0e4ad65007a5a622"></a>

### 152.6.13\_`usb_dc_ep_enable()`

```c
int usb_dc_ep_enable ( const uint8_t ep)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

启用选定端点。

此函数启用选定端点。成功后，相应端点的中断被启用，该端点已准备好发送或接收数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="ga8f702709dd2ed8257d61a8593c4c3b0d"></a>

### 152.6.14\_`usb_dc_ep_flush()`

```c
int usb_dc_ep_flush ( const uint8_t ep)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

清空选定端点。

此函数清空选定端点的先进先出缓冲区（First-In, First-Out，FIFO）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="ga821d65d9872ebb62bfaee79afbb80004"></a>

### 152.6.15\_`usb_dc_ep_halt()`

```c
int usb_dc_ep_halt ( const uint8_t ep)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

停止选定端点（Halt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="gaff2d98b0b6d4ae409b9961a7a123b326"></a>

### 152.6.16\_`usb_dc_ep_is_stalled()`

```c
int usb_dc_ep_is_stalled ( const uint8_t ep, uint8_t *const stalled )
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

检查选定端点是否处于停滞状态（Stalled）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |
| `[out] stalled` | 端点停滞状态。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="ga6e97104269bfe6dd08f5d0bbb791390e"></a>

### 152.6.17\_`usb_dc_ep_mps()`

```c
int usb_dc_ep_mps ( uint8_t ep)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

取得端点最大包大小（Maximum Packet Size，MPS）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：端点最大包大小（MPS）。

> 译注（源码核对）：此接口的正常返回值是最大包大小，不是其他许多接口采用的成功码0。原页没有逐项列出各驱动的失败返回；使用时仍应核对目标实现。

<a id="ga8b51a93295c7f9d3b15f4bfe8a09bb11"></a>

### 152.6.18\_`usb_dc_ep_read()`

```c
int usb_dc_ep_read ( const uint8_t ep, uint8_t *const data, const uint32_t max_data_len, uint32_t *const read_bytes )
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

从指定端点读取数据。

端点收到 OUT 中断后，由端点处理函数调用此函数。应用必须仅通过提供的 usb_ep_callback 函数调用它。如果端点 FIFO 中的全部数据已读完，此函数会清除端点的 NAK 状态，以便接收主机发送的更多数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |
| `[in] data` | 指向用于写入所读数据的缓冲区。 |
| `[in] max_data_len` | 最多读取的数据长度。 |
| `[out] read_bytes` | 已读取的字节数。如果 data 为 NULL 且 max_data_len 为 0，则应返回当前可读取的字节数。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

> 译注（源码核对）：data为NULL且max_data_len为0的组合用于查询可读长度，不表示将数据写到空指针。参数表中的[in]描述的是传入的缓冲区指针；被指向的存储空间会接收读出的字节。

<a id="ga9694ad0cc1ee84a4ed9de4f2860d4ae6"></a>

### 152.6.19\_`usb_dc_ep_read_continue()`

```c
int usb_dc_ep_read_continue ( uint8_t ep)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

继续从端点读取数据。

清除端点 NAK，使端点能够接收主机发送的更多数据。通常在调用 usb_dc_ep_read_wait() 后、消费者准备好接收更多数据时调用。因此这两个调用共同形成流量控制机制（Flow Control）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="ga012fb4d99870e1e30e0ecd4ac2b22312"></a>

### 152.6.20\_`usb_dc_ep_read_wait()`

```c
int usb_dc_ep_read_wait ( uint8_t ep, uint8_t * data, uint32_t max_data_len, uint32_t * read_bytes )
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

从指定端点读取数据。

此函数类似 usb_dc_ep_read，但不会清除端点 NAK，使消费者完成数据处理前不会被更多向上回调淹没。调用者随后应调用 usb_dc_ep_read_continue() 重新启用端点接收。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |
| `[in] data` | 指向用于写入所读数据的缓冲区。 |
| `[in] max_data_len` | 最多读取的数据长度。 |
| `[out] read_bytes` | 已读取的字节数。如果 data 为 NULL 且 max_data_len 为 0，则应返回当前可读取的字节数。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

> 译注（源码核对）：此处wait表示读后保留NAK以控制后续接收，不能据函数名推断它会阻塞到有数据。重新允许接收由usb_dc_ep_read_continue()负责；普通read在全部读完后的处理不同。NAK是暂时不接收事务的否定应答（Negative Acknowledgment），与表示端点停滞的STALL含义不同。

<a id="gaba2134e2a7b8d870860903aead03b418"></a>

### 152.6.21\_`usb_dc_ep_set_callback()`

```c
int usb_dc_ep_set_callback ( const uint8_t ep, const usb_dc_ep_callback cb )
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

设置指定端点的回调函数。

此函数设置选定端点的回调，用于通知应用有接收数据可用或发送已经完成。如果应用代码不需要回调，可设置为 NULL。回调状态码由 usb_dc_ep_cb_status_code 描述。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |
| `[in] cb` | 回调函数。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="ga68fcfcfe36a36cef202586686c5d30e3"></a>

### 152.6.22\_`usb_dc_ep_set_stall()`

```c
int usb_dc_ep_set_stall ( const uint8_t ep)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

为选定端点设置停滞状态（Stall）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="gad0b822f08c4a29a46aaa8fa8b30d58ef"></a>

### 152.6.23\_`usb_dc_ep_write()`

```c
int usb_dc_ep_write ( const uint8_t ep, const uint8_t *const data, const uint32_t data_len, uint32_t *const ret_bytes )
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

向指定端点写入数据。

此函数向指定端点写入数据。数据发送出去后，会调用提供的 usb_ep_callback 函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |
| `[in] data` | 指向待写入数据。 |
| `[in] data_len` | 请求写入的数据长度。发送零长度状态包（Zero-Length Status Packet）时，此值可以为零。 |
| `[out] ret_bytes` | 已安排发送的字节数。如果应用预期全部字节都会写入，此指针可以为 NULL。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

> 译注（源码核对）：ret_bytes描述安排发送的字节数，不等于主机应用已经消费的字节数。应按端点完成回调区分提交和完成；希望处理部分写入的调用者需要保留并检查ret_bytes。

<a id="ga8a72b00cfa90dcde41daa228791b61da"></a>

### 152.6.24\_`usb_dc_reset()`

```c
int usb_dc_reset ( void )
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

复位 USB 设备。

此函数使 USB 设备及固件回到初始状态。注意：USB PLL 由 usb_detach 函数处理。

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

> 译注（源码核对）：原文写作usb_detach；本头文件实际声明的断开接口名为usb_dc_detach()。这里保留原说明并明确接口名称，不能把USB控制器复位误解为整个SoC重启。

<a id="ga54a8280e4b011eff3640f6d21af1c292"></a>

### 152.6.25\_`usb_dc_set_address()`

```c
int usb_dc_set_address ( const uint8_t addr)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

设置 USB 设备地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] addr` | 设备地址。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="ga478eb2e57635ea816fd6acc8cb9a9424"></a>

### 152.6.26\_`usb_dc_set_status_callback()`

```c
void usb_dc_set_status_callback ( const usb_dc_status_callback cb)
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

设置 USB 设备控制器状态回调。

此函数设置 USB 设备控制器状态回调。已注册的回调用于报告设备控制器状态变化，状态码由 usb_dc_status_code 枚举描述。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cb` | 回调函数。 |

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

<a id="ga459110125c2a52da95b5b2c3c6fff096"></a>

### 152.6.27\_`usb_dc_wakeup_request()`

```c
int usb_dc_wakeup_request ( void )
```

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

启动唤醒主机的过程。

当主机当前处于休眠模式时，此函数用于唤醒主机。

**已弃用（Deprecated）**：请改用[USB设备控制器API（UDC）](P030_USB设备控制器API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

> 译注（源码核对）：该接口是控制器层的唤醒请求。旧版设备栈的usb_wakeup_request()还检查CONFIG_USB_DEVICE_REMOTE_WAKEUP及主机是否启用远程唤醒；不要把底层接口说明理解为设备可无条件唤醒任意休眠主机。

## 152.7\_源码跟踪与使用边界

译注依据保存的[官方usb_dc头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/usb_dc.h)、[旧版设备栈核心](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_device.c)及[传输实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_transfer.c)，摘要见[来源记录](../SOURCES.md)。本仓库[控制器头文件](../../../include/zephyr/drivers/usb/usb_dc.h)与[设备栈实现](../../../subsys/usb/device/usb_device.c)可用于相对路径源码跟踪，版本可能与网页不同。新版接口见[UDC说明](P029_USB设备控制器API说明.md)，旧版入口见[usb_dc说明](P128_旧版USB设备控制器API.md)。本批未构建、烧录、执行总线收发或唤醒测试。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaf7f083f61e1406e7d41513113dccd3bdabeb0ca69354218c5efc14c4ddbdf1c27"></a>
<a id="ggaf7f083f61e1406e7d41513113dccd3bda1801d1ba252ed6a0e573c46e76ae1f78"></a>
<a id="ggaf7f083f61e1406e7d41513113dccd3bdae2f497d34e18d6431ab886d120bd124c"></a>
<a id="ggae247c1ce7213e35d7ce74598225fa428a98061a0e90201b01c7b9b04b51eb0da8"></a>
<a id="ggae247c1ce7213e35d7ce74598225fa428a8cb40e0f2b85da1adfc005fbd5f9f45d"></a>
<a id="ggae247c1ce7213e35d7ce74598225fa428a13e7d8970d0723b36a17ae8a29dc9151"></a>
<a id="ggae247c1ce7213e35d7ce74598225fa428a70976afffbf9a9ef89eb51453c4307c5"></a>
<a id="ggaca68e4a7c3c0a984d1df23794cfa7d87a10c7e329a8eceb8cc693b77743f43681"></a>
<a id="ggaca68e4a7c3c0a984d1df23794cfa7d87a75c49ff44a9729723af190640a710ab6"></a>
<a id="ggaca68e4a7c3c0a984d1df23794cfa7d87aa0ecbc47a337243efd86155cb4ca54fe"></a>
<a id="ggaca68e4a7c3c0a984d1df23794cfa7d87aa70b161209601f1d7a43c5ebcc197b73"></a>
<a id="ggac09e3e0af1a2b41a5bfbad91f900baf7a8c34e2279a64268809170d6b7f08ed14"></a>
<a id="ggac09e3e0af1a2b41a5bfbad91f900baf7a6486b0e1a9f4c68fd3bc3b6b3354daa6"></a>
<a id="ggac09e3e0af1a2b41a5bfbad91f900baf7a643918c145a481a36bda37ae5b36599f"></a>
<a id="ggac09e3e0af1a2b41a5bfbad91f900baf7a63372b97af29a434d58a970439afc23f"></a>
<a id="ggac09e3e0af1a2b41a5bfbad91f900baf7a3584740de2622bf915e67fee6104da4c"></a>
<a id="ggac09e3e0af1a2b41a5bfbad91f900baf7afb40fc53f01c4e947a7d4c85a1a21c87"></a>
<a id="ggac09e3e0af1a2b41a5bfbad91f900baf7a306cbcf313be2111434f3e29b787de1d"></a>
<a id="ggac09e3e0af1a2b41a5bfbad91f900baf7a65828d350f0cd42be7f8406624eb3828"></a>
<a id="ggac09e3e0af1a2b41a5bfbad91f900baf7a426477e3ab4378cb0783523346e5ff23"></a>
<a id="ggac09e3e0af1a2b41a5bfbad91f900baf7a25d070f91c1e3ff0382b360f5ac2d501"></a>
<a id="ggac09e3e0af1a2b41a5bfbad91f900baf7abe89e0ffc160ffd1d8ae88d3771fcbc0"></a>
<a id="ggac09e3e0af1a2b41a5bfbad91f900baf7a8a0f6af1f3625530c9ecdfb2409205d9"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P151_USBBOS公共头文件.md) · [返回大纲](大纲.md) · [下一章](P153_旧版USB端点配置结构.md)
