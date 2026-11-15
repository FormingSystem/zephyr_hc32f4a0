---
id: learning.zephyr-docs.usb.api-154
title: 旧版USB控制器头文件接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__dc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第154章\_旧版USB控制器头文件接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb__dc_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 154.1\_阅读说明与来源

译注：本页说明旧版USB设备控制器驱动API（usb_dc）。它与新版USB设备控制器（USB Device Controller，UDC）API不同；原文的弃用标记与完整接口声明均保留。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 设备控制器 API。

```c
#include <zephyr/device.h>
```

USB 设备控制器 API。

此文件包含 USB 设备控制器 API。所有设备控制器驱动都应实现本文件描述的 API。

## 154.2\_数据结构（Data Structures）

<a id="r_usb_5Fdc_5Fep_5Fcfg_5Fdata"></a>

```c
struct usb_dc_ep_cfg_data
```

USB 端点配置（Endpoint Configuration）。

相关声明：[usb_dc_ep_cfg_data](P153_旧版USB端点配置结构.md)。

## 154.3\_类型定义（Typedefs）

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

## 154.4\_枚举（Enumerations）

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

## 154.5\_函数（Functions）

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

## 154.6\_源码跟踪与使用边界

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

[上一章](P153_旧版USB端点配置结构.md) · [返回大纲](大纲.md) · [下一章](P155_旧版USB设备栈核心API.md)
