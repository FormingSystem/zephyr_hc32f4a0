---
id: learning.zephyr-docs.api-source-architecture-reference.page-23
title: usb_device.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__device_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_usb\_device.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usb__device_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../usb/P158_旧版USB设备栈头文件接口.md)。

## 23.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00096"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="foldopen00128"></a>
<a id="l00128"></a>
<a id="l00134"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00149"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="foldopen00174"></a>
<a id="l00174"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="foldopen00488"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="agroup____usb__device__controller__api_html_ga2ddb0b059b4e1e76473ed7f56d0cf2ee"></a>
<a id="agroup____usb__device__controller__api_html_gac09e3e0af1a2b41a5bfbad91f900baf7"></a>
<a id="agroup____usb__device__controller__api_html_gaf7f083f61e1406e7d41513113dccd3bd"></a>
<a id="agroup____usb__device__core__api_html_ga1060e3a473a7f0bc71763a413e91ab56"></a>
<a id="agroup____usb__device__core__api_html_ga1bf8ec88cf752e98234d9f8bb57f976a"></a>
<a id="agroup____usb__device__core__api_html_ga27c3040dca474b5b45e6bea63a500cce"></a>
<a id="agroup____usb__device__core__api_html_ga28783e727e35db1a651309a7f9f5444a"></a>
<a id="agroup____usb__device__core__api_html_ga2d485c77055dd975f3170fbaea7f2bdf"></a>
<a id="agroup____usb__device__core__api_html_ga2e599eb20f647d9bb2369d76a7dc51db"></a>
<a id="agroup____usb__device__core__api_html_ga3439af9464471b3acdc21f4359efb53a"></a>
<a id="agroup____usb__device__core__api_html_ga4c919f7e993f80150bdde2d7fab254ee"></a>
<a id="agroup____usb__device__core__api_html_ga577018c415eec38ef5038cdb2f45ed2f"></a>
<a id="agroup____usb__device__core__api_html_ga6292a473cffc1f8683da902c2a85d653"></a>
<a id="agroup____usb__device__core__api_html_ga65723c9469a12c87e5554169396f8e76"></a>
<a id="agroup____usb__device__core__api_html_ga6d4b568f2f3aac4f099c35393fb601b3"></a>
<a id="agroup____usb__device__core__api_html_ga758a63b22c48d2ae9d025adb92ed5925"></a>
<a id="agroup____usb__device__core__api_html_ga7d67c8d49b52fb33818d654ca647c1e5"></a>
<a id="agroup____usb__device__core__api_html_ga9a45db26a9be295640ed122533427725"></a>
<a id="agroup____usb__device__core__api_html_gaab17b8c523ac211ff308c8dc774ba092"></a>
<a id="agroup____usb__device__core__api_html_gaaf206afaf32bde1b8d77d04bc6ec091f"></a>
<a id="agroup____usb__device__core__api_html_gab2c21738baa839b483654d1d5baf2981"></a>
<a id="agroup____usb__device__core__api_html_gab399dc4a43a99c927ee7588a57c49211"></a>
<a id="agroup____usb__device__core__api_html_gad1fa5e491d93c2bd1fe7967c12148902"></a>
<a id="agroup____usb__device__core__api_html_gaddacbff094a41c885c3041af72fa6804"></a>
<a id="agroup____usb__device__core__api_html_gae07256f6b4c1df494025a87bb6dbfd51"></a>
<a id="agroup____usb__device__core__api_html_gae7bc410d0db8a6d2142992153bb1424d"></a>
<a id="alog_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructusb__cfg__data_html"></a>
<a id="astructusb__cfg__data_html_a3ea73c7ea8759d3637852ff2d02ee96b"></a>
<a id="astructusb__cfg__data_html_a5e58af56af22ecdf0e2222afc408a33b"></a>
<a id="astructusb__cfg__data_html_a842d4d8a08dd619dd8ee5ccf62ae1e2a"></a>
<a id="astructusb__cfg__data_html_a84b41f3ddabab946ed165c03e3812e10"></a>
<a id="astructusb__cfg__data_html_aaf33be8983eb59105beb2d6e551ff195"></a>
<a id="astructusb__cfg__data_html_adbd7a747db040b54d047c48bed2f50c3"></a>
<a id="astructusb__cfg__data_html_ade7cc5e164a82a86d7c57d7a2a4ef306"></a>
<a id="astructusb__desc__header_html"></a>
<a id="astructusb__ep__cfg__data_html"></a>
<a id="astructusb__ep__cfg__data_html_a5d03244508b6a58d9d0bfb896c2537d1"></a>
<a id="astructusb__ep__cfg__data_html_aa87f676a577a8c1605bb9a8fa04f411c"></a>
<a id="astructusb__interface__cfg__data_html"></a>
<a id="astructusb__interface__cfg__data_html_a117a1a88c02048ee43994d3e5a4ce922"></a>
<a id="astructusb__interface__cfg__data_html_a144ed5ba67d1adb8dbb1d936ac440272"></a>
<a id="astructusb__interface__cfg__data_html_a2d5d65d41cef609173287161797318d2"></a>
<a id="astructusb__setup__packet_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="ausb__ch9_8h_html"></a>
<a id="ausb__dc_8h_html"></a>

```c
/* SPDX-License-Identifier: BSD-3-Clause */

/*
 *  LPCUSB, an USB device driver for LPC microcontrollers
 *  Copyright (C) 2006 Bertrik Sikken (bertrik@sikken.nl)
 *  Copyright (c) 2016 Intel Corporation
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions are met:
 *
 *  1. Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *  2. Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *  3. The name of the author may not be used to endorse or promote products
 *     derived from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 *  IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 *  OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 *  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 *  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 *  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 *  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 *  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */


#ifndef ZEPHYR_INCLUDE_USB_USB_DEVICE_H_
#define ZEPHYR_INCLUDE_USB_USB_DEVICE_H_

#include <zephyr/drivers/usb/usb_dc.h>
#include <zephyr/usb/usb_ch9.h>
#include <zephyr/logging/log.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif

/*
 * These macros should be used to place the USB descriptors
 * in predetermined order in the RAM.
 */
#define USBD_DEVICE_DESCR_DEFINE(p) \
        static __in_section(usb, descriptor_##p, 0) __used __aligned(1) __DEPRECATED_MACRO
#define USBD_CLASS_DESCR_DEFINE(p, instance) \
        static __in_section(usb, descriptor_##p.1, instance) __used __aligned(1) __DEPRECATED_MACRO
#define USBD_MISC_DESCR_DEFINE(p) \
        static __in_section(usb, descriptor_##p, 2) __used __aligned(1) __DEPRECATED_MACRO
#define USBD_USER_DESCR_DEFINE(p) \
        static __in_section(usb, descriptor_##p, 3) __used __aligned(1) __DEPRECATED_MACRO
#define USBD_STRING_DESCR_DEFINE(p) \
        static __in_section(usb, descriptor_##p, 4) __used __aligned(1) __DEPRECATED_MACRO
#define USBD_STRING_DESCR_USER_DEFINE(p) \
        static __in_section(usb, descriptor_##p, 5) __used __aligned(1) __DEPRECATED_MACRO
#define USBD_TERM_DESCR_DEFINE(p) \
        static __in_section(usb, descriptor_##p, 6) __used __aligned(1) __DEPRECATED_MACRO

/*
 * This macro should be used to place the struct usb_cfg_data
 * inside usb data section in the RAM.
 */
#define USBD_DEFINE_CFG_DATA(name) \
        static STRUCT_SECTION_ITERABLE(usb_cfg_data, name) __DEPRECATED_MACRO

/*************************************************************************
 *  USB configuration
 **************************************************************************/

#define USB_MAX_CTRL_MPS        64  __DEPRECATED_MACRO
#define USB_MAX_FS_BULK_MPS     64  __DEPRECATED_MACRO
#define USB_MAX_FS_INT_MPS      64  __DEPRECATED_MACRO
#define USB_MAX_FS_ISO_MPS      1023 __DEPRECATED_MACRO

/*************************************************************************
 *  USB application interface
 **************************************************************************/


typedef void (*usb_ep_callback)(uint8_t ep,
                                enum usb_dc_ep_cb_status_code cb_status);

typedef int (*usb_request_handler)(struct usb_setup_packet *setup,
                                   int32_t *transfer_len, uint8_t **payload_data);

typedef void (*usb_interface_config)(struct usb_desc_header *head,
                                     uint8_t bInterfaceNumber);

struct usb_ep_cfg_data {
        usb_ep_callback ep_cb;
        uint8_t ep_addr;
};

struct usb_interface_cfg_data {
        usb_request_handler class_handler;
        usb_request_handler vendor_handler;
        usb_request_handler custom_handler;
};

struct usb_cfg_data {
        const uint8_t *usb_device_description;
        void *interface_descriptor;
        usb_interface_config interface_config;
        void (*cb_usb_status)(struct usb_cfg_data *cfg,
                              enum usb_dc_status_code cb_status,
                              const uint8_t *param);
        struct usb_interface_cfg_data interface;
        uint8_t num_endpoints;
        struct usb_ep_cfg_data *endpoint;
};

__deprecated int usb_set_config(const uint8_t *usb_descriptor);

__deprecated int usb_deconfig(void);

__deprecated int usb_enable(usb_dc_status_callback status_cb);

__deprecated int usb_disable(void);

__deprecated int usb_write(uint8_t ep, const uint8_t *data, uint32_t data_len, uint32_t *bytes_ret);

__deprecated int usb_read(uint8_t ep, uint8_t *data, uint32_t max_data_len, uint32_t *ret_bytes);

__deprecated int usb_ep_set_stall(uint8_t ep);

__deprecated int usb_ep_clear_stall(uint8_t ep);

__deprecated int usb_ep_read_wait(uint8_t ep, uint8_t *data, uint32_t max_data_len,
                     uint32_t *read_bytes);


__deprecated int usb_ep_read_continue(uint8_t ep);

typedef void (*usb_transfer_callback)(uint8_t ep, int tsize, void *priv);

/* USB transfer flags */
#define USB_TRANS_READ       BIT(0) __DEPRECATED_MACRO
#define USB_TRANS_WRITE      BIT(1) __DEPRECATED_MACRO
#define USB_TRANS_NO_ZLP     BIT(2) __DEPRECATED_MACRO

__deprecated void usb_transfer_ep_callback(uint8_t ep, enum usb_dc_ep_cb_status_code status);

__deprecated int usb_transfer(uint8_t ep, uint8_t *data, size_t dlen, unsigned int flags,
                 usb_transfer_callback cb, void *priv);

__deprecated int usb_transfer_sync(uint8_t ep, uint8_t *data, size_t dlen, unsigned int flags);

__deprecated void usb_cancel_transfer(uint8_t ep);

__deprecated void usb_cancel_transfers(void);

__deprecated bool usb_transfer_is_busy(uint8_t ep);

__deprecated int usb_wakeup_request(void);

__deprecated bool usb_get_remote_wakeup_status(void);

#define USB_DEVICE_BOS_DESC_DEFINE_CAP \
        static __in_section(usb, bos_desc_area, 1) __aligned(1) __used __DEPRECATED_MACRO

__deprecated void usb_bos_register_cap(void *hdr);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_USB_USB_DEVICE_H_ */
```

## 23.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`BSD-3-Clause`。

### 注释 2：原第 3 行

LPCUSB：用于 LPC 微控制器（Microcontrollers）的 USB 设备驱动（Device Driver）。
版权所有（Copyright）2006 Bertrik Sikken（`bertrik@sikken.nl`）。
版权所有（Copyright）2016 Intel Corporation。

在满足下列条件时，允许以源码或二进制形式再分发和使用本软件，无论是否经过修改：

1. 再分发源码时，必须保留上述版权声明、本条件列表及下述免责声明。
2. 再分发二进制形式时，必须在随分发提供的文档和／或其他材料中重现上述版权声明、本条件列表及下述免责声明。
3. 未经事先明确的书面许可，不得使用作者姓名为本软件衍生产品背书或推广。

本软件由作者按“原样”（AS IS）提供，不提供任何明示或默示保证，包括但不限于适销性及适用于特定用途的默示保证。在任何情况下，作者均不对因使用本软件以任何方式产生的直接、间接、附带、特殊、惩罚性或后果性损害承担责任，包括但不限于采购替代商品或服务、使用机会或数据或利润的损失、业务中断。无论这些损害如何造成，亦无论依据何种责任理论，包括合同责任、严格责任或侵权责任（包括过失或其他情形），即使作者事先已被告知可能发生此类损害，也不承担责任。

### 注释 3：原第 50 行

应使用这些宏（Macros），将 USB 描述符（Descriptors）按预定顺序放置到 RAM 中。

### 注释 4：原第 69 行

应使用本宏，将 `struct usb_cfg_data` 放入 RAM 的 USB 数据区段（USB Data Section）。

### 注释 5：原第 76 行

USB 配置（USB Configuration），原注释以分隔线标示此段。

### 注释 6：原第 85 行

USB 应用程序接口（USB Application Interface），原注释以分隔线标示此段。

### 注释 7：原第 375 行

USB 传输标志（Transfer Flags）。

### 注释 8：原第 511 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USB_USB_DEVICE_H_`。

## 23.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../usb/P158_旧版USB设备栈头文件接口.md)
- [zephyr/drivers/usb/usb_dc.h](../usb/P154_旧版USB控制器头文件接口.md)
- [zephyr/usb/usb_ch9.h](../usb/P172_USB标准请求与描述符常量.md)
- [zephyr/logging/log.h](../log_core_reference/P003_日志公共头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [usb_ep_callback](../usb/P155_旧版USB设备栈核心API.md#ga9a45db26a9be295640ed122533427725)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [usb_dc_ep_cb_status_code](../usb/P152_旧版USB控制器驱动API.md#gaf7f083f61e1406e7d41513113dccd3bd)
- [usb_request_handler](../usb/P155_旧版USB设备栈核心API.md#gaddacbff094a41c885c3041af72fa6804)
- [usb_setup_packet](../usb/P160_USB控制请求包.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [usb_interface_config](../usb/P155_旧版USB设备栈核心API.md#ga3439af9464471b3acdc21f4359efb53a)
- [usb_desc_header](../usb/P161_USB通用描述符头.md)
- [usb_ep_cfg_data](../usb/P157_旧版USB端点回调配置.md)
- [ep_cb](../usb/P157_旧版USB端点回调配置.md#a5d03244508b6a58d9d0bfb896c2537d1)
- [ep_addr](../usb/P157_旧版USB端点回调配置.md#aa87f676a577a8c1605bb9a8fa04f411c)
- [usb_interface_cfg_data](../usb/P159_旧版USB接口请求配置.md)
- [class_handler](../usb/P159_旧版USB接口请求配置.md#a144ed5ba67d1adb8dbb1d936ac440272)
- [vendor_handler](../usb/P159_旧版USB接口请求配置.md#a2d5d65d41cef609173287161797318d2)
- [custom_handler](../usb/P159_旧版USB接口请求配置.md#a117a1a88c02048ee43994d3e5a4ce922)
- [usb_cfg_data](../usb/P156_旧版USB功能配置结构.md)
- [usb_device_description](../usb/P156_旧版USB功能配置结构.md#a842d4d8a08dd619dd8ee5ccf62ae1e2a)
- [interface_descriptor](../usb/P156_旧版USB功能配置结构.md#ade7cc5e164a82a86d7c57d7a2a4ef306)
- [interface_config](../usb/P156_旧版USB功能配置结构.md#a3ea73c7ea8759d3637852ff2d02ee96b)
- [cb_usb_status](../usb/P156_旧版USB功能配置结构.md#aaf33be8983eb59105beb2d6e551ff195)
- [usb_dc_status_code](../usb/P152_旧版USB控制器驱动API.md#gac09e3e0af1a2b41a5bfbad91f900baf7)
- [interface](../usb/P156_旧版USB功能配置结构.md#a84b41f3ddabab946ed165c03e3812e10)
- [num_endpoints](../usb/P156_旧版USB功能配置结构.md#a5e58af56af22ecdf0e2222afc408a33b)
- [endpoint](../usb/P156_旧版USB功能配置结构.md#adbd7a747db040b54d047c48bed2f50c3)
- [usb_set_config](../usb/P155_旧版USB设备栈核心API.md#ga28783e727e35db1a651309a7f9f5444a)
- [usb_deconfig](../usb/P155_旧版USB设备栈核心API.md#ga2d485c77055dd975f3170fbaea7f2bdf)
- [usb_enable](../usb/P155_旧版USB设备栈核心API.md#gad1fa5e491d93c2bd1fe7967c12148902)
- [usb_dc_status_callback](../usb/P152_旧版USB控制器驱动API.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee)
- [usb_disable](../usb/P155_旧版USB设备栈核心API.md#ga65723c9469a12c87e5554169396f8e76)
- [usb_write](../usb/P155_旧版USB设备栈核心API.md#ga6d4b568f2f3aac4f099c35393fb601b3)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [usb_read](../usb/P155_旧版USB设备栈核心API.md#gab2c21738baa839b483654d1d5baf2981)
- [usb_ep_set_stall](../usb/P155_旧版USB设备栈核心API.md#gaaf206afaf32bde1b8d77d04bc6ec091f)
- [usb_ep_clear_stall](../usb/P155_旧版USB设备栈核心API.md#gae7bc410d0db8a6d2142992153bb1424d)
- [usb_ep_read_wait](../usb/P155_旧版USB设备栈核心API.md#ga4c919f7e993f80150bdde2d7fab254ee)
- [usb_ep_read_continue](../usb/P155_旧版USB设备栈核心API.md#gaab17b8c523ac211ff308c8dc774ba092)
- [usb_transfer_callback](../usb/P155_旧版USB设备栈核心API.md#ga2e599eb20f647d9bb2369d76a7dc51db)
- [usb_transfer_ep_callback](../usb/P155_旧版USB设备栈核心API.md#gae07256f6b4c1df494025a87bb6dbfd51)
- [usb_transfer](../usb/P155_旧版USB设备栈核心API.md#ga27c3040dca474b5b45e6bea63a500cce)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [usb_transfer_sync](../usb/P155_旧版USB设备栈核心API.md#ga1060e3a473a7f0bc71763a413e91ab56)
- [usb_cancel_transfer](../usb/P155_旧版USB设备栈核心API.md#gab399dc4a43a99c927ee7588a57c49211)
- [usb_cancel_transfers](../usb/P155_旧版USB设备栈核心API.md#ga758a63b22c48d2ae9d025adb92ed5925)
- [usb_transfer_is_busy](../usb/P155_旧版USB设备栈核心API.md#ga6292a473cffc1f8683da902c2a85d653)
- [usb_wakeup_request](../usb/P155_旧版USB设备栈核心API.md#ga7d67c8d49b52fb33818d654ca647c1e5)
- [usb_get_remote_wakeup_status](../usb/P155_旧版USB设备栈核心API.md#ga577018c415eec38ef5038cdb2f45ed2f)
- [usb_bos_register_cap](../usb/P155_旧版USB设备栈核心API.md#ga1bf8ec88cf752e98234d9f8bb57f976a)
- [log.h](../log_core_reference/P003_日志公共头文件参考.md)
- [usb_cfg_data::interface_config](../usb/P156_旧版USB功能配置结构.md#a3ea73c7ea8759d3637852ff2d02ee96b)
- [usb_cfg_data::num_endpoints](../usb/P156_旧版USB功能配置结构.md#a5e58af56af22ecdf0e2222afc408a33b)
- [usb_cfg_data::usb_device_description](../usb/P156_旧版USB功能配置结构.md#a842d4d8a08dd619dd8ee5ccf62ae1e2a)
- [usb_cfg_data::interface](../usb/P156_旧版USB功能配置结构.md#a84b41f3ddabab946ed165c03e3812e10)
- [usb_cfg_data::cb_usb_status](../usb/P156_旧版USB功能配置结构.md#aaf33be8983eb59105beb2d6e551ff195)
- [usb_cfg_data::endpoint](../usb/P156_旧版USB功能配置结构.md#adbd7a747db040b54d047c48bed2f50c3)
- [usb_cfg_data::interface_descriptor](../usb/P156_旧版USB功能配置结构.md#ade7cc5e164a82a86d7c57d7a2a4ef306)
- [usb_ep_cfg_data::ep_cb](../usb/P157_旧版USB端点回调配置.md#a5d03244508b6a58d9d0bfb896c2537d1)
- [usb_ep_cfg_data::ep_addr](../usb/P157_旧版USB端点回调配置.md#aa87f676a577a8c1605bb9a8fa04f411c)
- [usb_interface_cfg_data::custom_handler](../usb/P159_旧版USB接口请求配置.md#a117a1a88c02048ee43994d3e5a4ce922)
- [usb_interface_cfg_data::class_handler](../usb/P159_旧版USB接口请求配置.md#a144ed5ba67d1adb8dbb1d936ac440272)
- [usb_interface_cfg_data::vendor_handler](../usb/P159_旧版USB接口请求配置.md#a2d5d65d41cef609173287161797318d2)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [usb_ch9.h](../usb/P172_USB标准请求与描述符常量.md)
- [usb_dc.h](../usb/P154_旧版USB控制器头文件接口.md)

---

[上一章](P022_uart_ifx_cat1.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P024_zassert.h_源码浏览.md)
