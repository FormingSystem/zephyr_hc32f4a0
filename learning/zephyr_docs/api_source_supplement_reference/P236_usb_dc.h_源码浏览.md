---
id: learning.zephyr-docs.api-source-supplement-reference.page-236
title: usb_dc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__dc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第236章\_usb\_dc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usb__dc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../usb/P154_旧版USB控制器头文件接口.md)。

## 236.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00029"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00095"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="adevice_8h_html"></a>
<a id="agroup____usb__device__controller__api_html_ga012fb4d99870e1e30e0ecd4ac2b22312"></a>
<a id="agroup____usb__device__controller__api_html_ga0154d6b5d462fa2a9db174a985259429"></a>
<a id="agroup____usb__device__controller__api_html_ga062b4c8b618f2e964984786baf635a93"></a>
<a id="agroup____usb__device__controller__api_html_ga199aaf51e878cadc0e4ad65007a5a622"></a>
<a id="agroup____usb__device__controller__api_html_ga2ddb0b059b4e1e76473ed7f56d0cf2ee"></a>
<a id="agroup____usb__device__controller__api_html_ga459110125c2a52da95b5b2c3c6fff096"></a>
<a id="agroup____usb__device__controller__api_html_ga478eb2e57635ea816fd6acc8cb9a9424"></a>
<a id="agroup____usb__device__controller__api_html_ga54a8280e4b011eff3640f6d21af1c292"></a>
<a id="agroup____usb__device__controller__api_html_ga68fcfcfe36a36cef202586686c5d30e3"></a>
<a id="agroup____usb__device__controller__api_html_ga6e97104269bfe6dd08f5d0bbb791390e"></a>
<a id="agroup____usb__device__controller__api_html_ga821d65d9872ebb62bfaee79afbb80004"></a>
<a id="agroup____usb__device__controller__api_html_ga858a4e1bf2c35f5a0ec333801e75b718"></a>
<a id="agroup____usb__device__controller__api_html_ga8a72b00cfa90dcde41daa228791b61da"></a>
<a id="agroup____usb__device__controller__api_html_ga8b51a93295c7f9d3b15f4bfe8a09bb11"></a>
<a id="agroup____usb__device__controller__api_html_ga8f702709dd2ed8257d61a8593c4c3b0d"></a>
<a id="agroup____usb__device__controller__api_html_ga9694ad0cc1ee84a4ed9de4f2860d4ae6"></a>
<a id="agroup____usb__device__controller__api_html_gab6b9ca74059ff2285bd301e9264df45b"></a>
<a id="agroup____usb__device__controller__api_html_gab89ebb3049f7fd7a1e764ffef16b1b64"></a>
<a id="agroup____usb__device__controller__api_html_gaba2134e2a7b8d870860903aead03b418"></a>
<a id="agroup____usb__device__controller__api_html_gac09e3e0af1a2b41a5bfbad91f900baf7"></a>
<a id="agroup____usb__device__controller__api_html_gaca68e4a7c3c0a984d1df23794cfa7d87"></a>
<a id="agroup____usb__device__controller__api_html_gad0b822f08c4a29a46aaa8fa8b30d58ef"></a>
<a id="agroup____usb__device__controller__api_html_gad75ee35cdfb5dc4f1fad0e615067cb70"></a>
<a id="agroup____usb__device__controller__api_html_gae247c1ce7213e35d7ce74598225fa428"></a>
<a id="agroup____usb__device__controller__api_html_gaf78984e6103185c6ebadee2fcbdf62f7"></a>
<a id="agroup____usb__device__controller__api_html_gaf7f083f61e1406e7d41513113dccd3bd"></a>
<a id="agroup____usb__device__controller__api_html_gaff2d98b0b6d4ae409b9961a7a123b326"></a>
<a id="agroup____usb__device__controller__api_html_ggac09e3e0af1a2b41a5bfbad91f900baf7a25d070f91c1e3ff0382b360f5ac2d501"></a>
<a id="agroup____usb__device__controller__api_html_ggac09e3e0af1a2b41a5bfbad91f900baf7a306cbcf313be2111434f3e29b787de1d"></a>
<a id="agroup____usb__device__controller__api_html_ggac09e3e0af1a2b41a5bfbad91f900baf7a3584740de2622bf915e67fee6104da4c"></a>
<a id="agroup____usb__device__controller__api_html_ggac09e3e0af1a2b41a5bfbad91f900baf7a426477e3ab4378cb0783523346e5ff23"></a>
<a id="agroup____usb__device__controller__api_html_ggac09e3e0af1a2b41a5bfbad91f900baf7a63372b97af29a434d58a970439afc23f"></a>
<a id="agroup____usb__device__controller__api_html_ggac09e3e0af1a2b41a5bfbad91f900baf7a643918c145a481a36bda37ae5b36599f"></a>
<a id="agroup____usb__device__controller__api_html_ggac09e3e0af1a2b41a5bfbad91f900baf7a6486b0e1a9f4c68fd3bc3b6b3354daa6"></a>
<a id="agroup____usb__device__controller__api_html_ggac09e3e0af1a2b41a5bfbad91f900baf7a65828d350f0cd42be7f8406624eb3828"></a>
<a id="agroup____usb__device__controller__api_html_ggac09e3e0af1a2b41a5bfbad91f900baf7a8a0f6af1f3625530c9ecdfb2409205d9"></a>
<a id="agroup____usb__device__controller__api_html_ggac09e3e0af1a2b41a5bfbad91f900baf7a8c34e2279a64268809170d6b7f08ed14"></a>
<a id="agroup____usb__device__controller__api_html_ggac09e3e0af1a2b41a5bfbad91f900baf7abe89e0ffc160ffd1d8ae88d3771fcbc0"></a>
<a id="agroup____usb__device__controller__api_html_ggac09e3e0af1a2b41a5bfbad91f900baf7afb40fc53f01c4e947a7d4c85a1a21c87"></a>
<a id="agroup____usb__device__controller__api_html_ggaca68e4a7c3c0a984d1df23794cfa7d87a10c7e329a8eceb8cc693b77743f43681"></a>
<a id="agroup____usb__device__controller__api_html_ggaca68e4a7c3c0a984d1df23794cfa7d87a75c49ff44a9729723af190640a710ab6"></a>
<a id="agroup____usb__device__controller__api_html_ggaca68e4a7c3c0a984d1df23794cfa7d87aa0ecbc47a337243efd86155cb4ca54fe"></a>
<a id="agroup____usb__device__controller__api_html_ggaca68e4a7c3c0a984d1df23794cfa7d87aa70b161209601f1d7a43c5ebcc197b73"></a>
<a id="agroup____usb__device__controller__api_html_ggae247c1ce7213e35d7ce74598225fa428a13e7d8970d0723b36a17ae8a29dc9151"></a>
<a id="agroup____usb__device__controller__api_html_ggae247c1ce7213e35d7ce74598225fa428a70976afffbf9a9ef89eb51453c4307c5"></a>
<a id="agroup____usb__device__controller__api_html_ggae247c1ce7213e35d7ce74598225fa428a8cb40e0f2b85da1adfc005fbd5f9f45d"></a>
<a id="agroup____usb__device__controller__api_html_ggae247c1ce7213e35d7ce74598225fa428a98061a0e90201b01c7b9b04b51eb0da8"></a>
<a id="agroup____usb__device__controller__api_html_ggaf7f083f61e1406e7d41513113dccd3bda1801d1ba252ed6a0e573c46e76ae1f78"></a>
<a id="agroup____usb__device__controller__api_html_ggaf7f083f61e1406e7d41513113dccd3bdabeb0ca69354218c5efc14c4ddbdf1c27"></a>
<a id="agroup____usb__device__controller__api_html_ggaf7f083f61e1406e7d41513113dccd3bdae2f497d34e18d6431ab886d120bd124c"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructusb__dc__ep__cfg__data_html"></a>
<a id="astructusb__dc__ep__cfg__data_html_a497bc16439e98415f383a680a0c4d008"></a>
<a id="astructusb__dc__ep__cfg__data_html_a689682e1df951fd2fd492dda5e03cf08"></a>
<a id="astructusb__dc__ep__cfg__data_html_aba57a59450c93db5935e2ca08c94aa8b"></a>

```c
/* usb_dc.h - USB device controller driver interface */

/*
 * Copyright (c) 2016 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_USB_USB_DC_H_
#define ZEPHYR_INCLUDE_DRIVERS_USB_USB_DC_H_

#include <zephyr/device.h>


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
};

enum usb_dc_ep_cb_status_code {
        USB_DC_EP_SETUP,
        USB_DC_EP_DATA_OUT,
        USB_DC_EP_DATA_IN
};

enum usb_dc_ep_transfer_type {
        USB_DC_EP_CONTROL = 0,
        USB_DC_EP_ISOCHRONOUS,
        USB_DC_EP_BULK,
        USB_DC_EP_INTERRUPT
};

enum usb_dc_ep_synchronozation_type {
        USB_DC_EP_NO_SYNCHRONIZATION = (0U << 2U),
        USB_DC_EP_ASYNCHRONOUS = (1U << 2U),
        USB_DC_EP_ADAPTIVE = (2U << 2U),
        USB_DC_EP_SYNCHRONOUS = (3U << 2U)
};

struct usb_dc_ep_cfg_data {
        uint8_t ep_addr;
        uint16_t ep_mps;
        enum usb_dc_ep_transfer_type ep_type;
};

typedef void (*usb_dc_ep_callback)(uint8_t ep,
                                   enum usb_dc_ep_cb_status_code cb_status);

typedef void (*usb_dc_status_callback)(enum usb_dc_status_code cb_status,
                                       const uint8_t *param);

__deprecated int usb_dc_attach(void);

__deprecated int usb_dc_detach(void);

__deprecated int usb_dc_reset(void);

__deprecated int usb_dc_set_address(const uint8_t addr);

__deprecated void usb_dc_set_status_callback(const usb_dc_status_callback cb);

__deprecated int usb_dc_ep_check_cap(const struct usb_dc_ep_cfg_data * const cfg);

__deprecated int usb_dc_ep_configure(const struct usb_dc_ep_cfg_data * const cfg);

__deprecated int usb_dc_ep_set_stall(const uint8_t ep);

__deprecated int usb_dc_ep_clear_stall(const uint8_t ep);

__deprecated int usb_dc_ep_is_stalled(const uint8_t ep, uint8_t *const stalled);

__deprecated int usb_dc_ep_halt(const uint8_t ep);

__deprecated int usb_dc_ep_enable(const uint8_t ep);

__deprecated int usb_dc_ep_disable(const uint8_t ep);

__deprecated int usb_dc_ep_flush(const uint8_t ep);

__deprecated int usb_dc_ep_write(const uint8_t ep, const uint8_t *const data,
                    const uint32_t data_len, uint32_t * const ret_bytes);

__deprecated int usb_dc_ep_read(const uint8_t ep, uint8_t *const data,
                   const uint32_t max_data_len, uint32_t *const read_bytes);

__deprecated int usb_dc_ep_set_callback(const uint8_t ep, const usb_dc_ep_callback cb);

__deprecated int usb_dc_ep_read_wait(uint8_t ep, uint8_t *data, uint32_t max_data_len,
                        uint32_t *read_bytes);

__deprecated int usb_dc_ep_read_continue(uint8_t ep);

__deprecated int usb_dc_ep_mps(uint8_t ep);

__deprecated int usb_dc_wakeup_request(void);


#endif /* ZEPHYR_INCLUDE_DRIVERS_USB_USB_DC_H_ */
```

## 236.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`usb_dc.h`：USB 设备控制器驱动接口（USB device controller driver interface）。

### 注释 2：原第 3 行

版权（Copyright）：© 2016 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 458 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_USB_USB_DC_H_`。

## 236.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../usb/P154_旧版USB控制器头文件接口.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [usb_dc_status_code](../usb/P152_旧版USB控制器驱动API.md#gac09e3e0af1a2b41a5bfbad91f900baf7)
- [USB_DC_ERROR](../usb/P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a8c34e2279a64268809170d6b7f08ed14)
- [USB_DC_RESET](../usb/P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a6486b0e1a9f4c68fd3bc3b6b3354daa6)
- [USB_DC_CONNECTED](../usb/P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a643918c145a481a36bda37ae5b36599f)
- [USB_DC_CONFIGURED](../usb/P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a63372b97af29a434d58a970439afc23f)
- [USB_DC_DISCONNECTED](../usb/P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a3584740de2622bf915e67fee6104da4c)
- [USB_DC_SUSPEND](../usb/P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7afb40fc53f01c4e947a7d4c85a1a21c87)
- [USB_DC_RESUME](../usb/P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a306cbcf313be2111434f3e29b787de1d)
- [USB_DC_INTERFACE](../usb/P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a65828d350f0cd42be7f8406624eb3828)
- [USB_DC_SET_HALT](../usb/P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a426477e3ab4378cb0783523346e5ff23)
- [USB_DC_CLEAR_HALT](../usb/P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a25d070f91c1e3ff0382b360f5ac2d501)
- [USB_DC_SOF](../usb/P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7abe89e0ffc160ffd1d8ae88d3771fcbc0)
- [USB_DC_UNKNOWN](../usb/P152_旧版USB控制器驱动API.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a8a0f6af1f3625530c9ecdfb2409205d9)
- [usb_dc_ep_cb_status_code](../usb/P152_旧版USB控制器驱动API.md#gaf7f083f61e1406e7d41513113dccd3bd)
- [USB_DC_EP_SETUP](../usb/P152_旧版USB控制器驱动API.md#ggaf7f083f61e1406e7d41513113dccd3bdabeb0ca69354218c5efc14c4ddbdf1c27)
- [USB_DC_EP_DATA_OUT](../usb/P152_旧版USB控制器驱动API.md#ggaf7f083f61e1406e7d41513113dccd3bda1801d1ba252ed6a0e573c46e76ae1f78)
- [USB_DC_EP_DATA_IN](../usb/P152_旧版USB控制器驱动API.md#ggaf7f083f61e1406e7d41513113dccd3bdae2f497d34e18d6431ab886d120bd124c)
- [usb_dc_ep_transfer_type](../usb/P152_旧版USB控制器驱动API.md#gaca68e4a7c3c0a984d1df23794cfa7d87)
- [USB_DC_EP_CONTROL](../usb/P152_旧版USB控制器驱动API.md#ggaca68e4a7c3c0a984d1df23794cfa7d87a10c7e329a8eceb8cc693b77743f43681)
- [USB_DC_EP_ISOCHRONOUS](../usb/P152_旧版USB控制器驱动API.md#ggaca68e4a7c3c0a984d1df23794cfa7d87a75c49ff44a9729723af190640a710ab6)
- [USB_DC_EP_BULK](../usb/P152_旧版USB控制器驱动API.md#ggaca68e4a7c3c0a984d1df23794cfa7d87aa0ecbc47a337243efd86155cb4ca54fe)
- [USB_DC_EP_INTERRUPT](../usb/P152_旧版USB控制器驱动API.md#ggaca68e4a7c3c0a984d1df23794cfa7d87aa70b161209601f1d7a43c5ebcc197b73)
- [usb_dc_ep_synchronozation_type](../usb/P152_旧版USB控制器驱动API.md#gae247c1ce7213e35d7ce74598225fa428)
- [USB_DC_EP_NO_SYNCHRONIZATION](../usb/P152_旧版USB控制器驱动API.md#ggae247c1ce7213e35d7ce74598225fa428a98061a0e90201b01c7b9b04b51eb0da8)
- [USB_DC_EP_ASYNCHRONOUS](../usb/P152_旧版USB控制器驱动API.md#ggae247c1ce7213e35d7ce74598225fa428a8cb40e0f2b85da1adfc005fbd5f9f45d)
- [USB_DC_EP_ADAPTIVE](../usb/P152_旧版USB控制器驱动API.md#ggae247c1ce7213e35d7ce74598225fa428a13e7d8970d0723b36a17ae8a29dc9151)
- [USB_DC_EP_SYNCHRONOUS](../usb/P152_旧版USB控制器驱动API.md#ggae247c1ce7213e35d7ce74598225fa428a70976afffbf9a9ef89eb51453c4307c5)
- [usb_dc_ep_cfg_data](../usb/P153_旧版USB端点配置结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ep_addr](../usb/P153_旧版USB端点配置结构.md#aba57a59450c93db5935e2ca08c94aa8b)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [ep_mps](../usb/P153_旧版USB端点配置结构.md#a497bc16439e98415f383a680a0c4d008)
- [ep_type](../usb/P153_旧版USB端点配置结构.md#a689682e1df951fd2fd492dda5e03cf08)
- [usb_dc_ep_callback](../usb/P152_旧版USB控制器驱动API.md#gad75ee35cdfb5dc4f1fad0e615067cb70)
- [usb_dc_status_callback](../usb/P152_旧版USB控制器驱动API.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee)
- [usb_dc_attach](../usb/P152_旧版USB控制器驱动API.md#gaf78984e6103185c6ebadee2fcbdf62f7)
- [usb_dc_detach](../usb/P152_旧版USB控制器驱动API.md#ga062b4c8b618f2e964984786baf635a93)
- [usb_dc_reset](../usb/P152_旧版USB控制器驱动API.md#ga8a72b00cfa90dcde41daa228791b61da)
- [usb_dc_set_address](../usb/P152_旧版USB控制器驱动API.md#ga54a8280e4b011eff3640f6d21af1c292)
- [usb_dc_set_status_callback](../usb/P152_旧版USB控制器驱动API.md#ga478eb2e57635ea816fd6acc8cb9a9424)
- [usb_dc_ep_check_cap](../usb/P152_旧版USB控制器驱动API.md#gab6b9ca74059ff2285bd301e9264df45b)
- [usb_dc_ep_configure](../usb/P152_旧版USB控制器驱动API.md#ga858a4e1bf2c35f5a0ec333801e75b718)
- [usb_dc_ep_set_stall](../usb/P152_旧版USB控制器驱动API.md#ga68fcfcfe36a36cef202586686c5d30e3)
- [usb_dc_ep_clear_stall](../usb/P152_旧版USB控制器驱动API.md#gab89ebb3049f7fd7a1e764ffef16b1b64)
- [usb_dc_ep_is_stalled](../usb/P152_旧版USB控制器驱动API.md#gaff2d98b0b6d4ae409b9961a7a123b326)
- [usb_dc_ep_halt](../usb/P152_旧版USB控制器驱动API.md#ga821d65d9872ebb62bfaee79afbb80004)
- [usb_dc_ep_enable](../usb/P152_旧版USB控制器驱动API.md#ga199aaf51e878cadc0e4ad65007a5a622)
- [usb_dc_ep_disable](../usb/P152_旧版USB控制器驱动API.md#ga0154d6b5d462fa2a9db174a985259429)
- [usb_dc_ep_flush](../usb/P152_旧版USB控制器驱动API.md#ga8f702709dd2ed8257d61a8593c4c3b0d)
- [usb_dc_ep_write](../usb/P152_旧版USB控制器驱动API.md#gad0b822f08c4a29a46aaa8fa8b30d58ef)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [usb_dc_ep_read](../usb/P152_旧版USB控制器驱动API.md#ga8b51a93295c7f9d3b15f4bfe8a09bb11)
- [usb_dc_ep_set_callback](../usb/P152_旧版USB控制器驱动API.md#gaba2134e2a7b8d870860903aead03b418)
- [usb_dc_ep_read_wait](../usb/P152_旧版USB控制器驱动API.md#ga012fb4d99870e1e30e0ecd4ac2b22312)
- [usb_dc_ep_read_continue](../usb/P152_旧版USB控制器驱动API.md#ga9694ad0cc1ee84a4ed9de4f2860d4ae6)
- [usb_dc_ep_mps](../usb/P152_旧版USB控制器驱动API.md#ga6e97104269bfe6dd08f5d0bbb791390e)
- [usb_dc_wakeup_request](../usb/P152_旧版USB控制器驱动API.md#ga459110125c2a52da95b5b2c3c6fff096)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [usb_dc_ep_cfg_data::ep_mps](../usb/P153_旧版USB端点配置结构.md#a497bc16439e98415f383a680a0c4d008)
- [usb_dc_ep_cfg_data::ep_type](../usb/P153_旧版USB端点配置结构.md#a689682e1df951fd2fd492dda5e03cf08)
- [usb_dc_ep_cfg_data::ep_addr](../usb/P153_旧版USB端点配置结构.md#aba57a59450c93db5935e2ca08c94aa8b)

---

[上一章](P235_usb_bc12.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P237_usb_hid.h_源码浏览.md)
