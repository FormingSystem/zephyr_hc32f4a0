---
id: learning.zephyr-docs.usb.api-188
title: DFU设备类头文件源码
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__dfu_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2024 Nordic Semiconductor ASA -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第188章\_DFU设备类头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbd__dfu_8h_source.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 188.1\_阅读说明与来源

译注：本组补齐设备固件升级（Device Firmware Upgrade，DFU）的头文件参考、协议状态和功能描述符，分别标明旧版设备栈与新版设备栈。镜像定义宏及回调说明见[设备固件升级 API](P062_USB设备固件升级API.md)和[镜像结构](P063_USB固件升级镜像结构.md)；本页不会仅凭描述符字段推定目标板已具备升级能力。

下方完整保留官方 Doxygen 源码浏览页中的代码及许可注释；仅移除网页行号、还原显示空格并清理行尾空白。浏览页省略的 API 文档注释由对应头文件参考和[DFU API 译文](P062_USB设备固件升级API.md)承接。此页展示不冒充包含全部注释的原始头文件。

## 188.2\_原始源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00038"></a>
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
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="foldopen00095"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00118"></a>
<a id="foldopen00155"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00173"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructusb__dfu__descriptor_html"></a>
<a id="astructusb__dfu__descriptor_html_a545d551fdf9612abab9679ad9092fe21"></a>
<a id="astructusb__dfu__descriptor_html_a6eda776c2fa8ad9e92da5a9c0771c017"></a>
<a id="astructusb__dfu__descriptor_html_a6f28ae6870039d8ba994a2aed1d6b8b9"></a>
<a id="astructusb__dfu__descriptor_html_aaae3ed6f5fc202453e5a295b25c391e0"></a>
<a id="astructusb__dfu__descriptor_html_ab37985af3ea9985ebe57d04eb7b004b6"></a>
<a id="astructusb__dfu__descriptor_html_ac917f4ae3b4cda852e7e23a1378cc584"></a>
<a id="astructusb__if__descriptor_html"></a>
<a id="astructusbd__desc__node_html"></a>
<a id="astructusbd__dfu__image_html"></a>
<a id="astructusbd__dfu__image_html_a03ee7685c90ac7ec8c2c4d87a6389e62"></a>
<a id="astructusbd__dfu__image_html_a2202146c73e3b2300200f04eff05c888"></a>
<a id="astructusbd__dfu__image_html_a2aade79d72faef1fe8a6fe846189daf0"></a>
<a id="astructusbd__dfu__image_html_a3e2d6339752919988f3c113ca87a543e"></a>
<a id="astructusbd__dfu__image_html_a4df9017274c5094ed49fd8e6964b4379"></a>
<a id="astructusbd__dfu__image_html_aad9a4efbf3649373328b6b6b12fa1922"></a>
<a id="astructusbd__dfu__image_html_aff741ab9145292e9b7a30fe3a93a4615"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a1a945da4703d6f5953ea81519dcaaaad"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a1d02e2949a0d4e292140efe5742c79a6"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a4f5e97d0bc125828f2c779c11426367c"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a5c708decdcbd7d8c9fddd8d9e75828a1"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a614b66b2b507a2c6343462f94582cecb"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a6532abde77d62a3154cb1ee22a5bce0b"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a7b2c2fd2edcf9479181e72ee6ef6fffc"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a7b3dcb9b918d6e5af83b68d4fb767274"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a7f528dddca00563b477800a95163a347"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a86a37904a04f8a7ddc9831e85d826a5a"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a8c7d94233447f239b74aeea63cb8e09d"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a97067bf5865840561ec9eba092838e9a"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62a98b47a7a9e4e6f1442d76fa668a6ff49"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62aa26c163b80b1f6786ca81dadc14b00fb"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62aaaefe7b6fd4399eb00ed391833956103"></a>
<a id="ausbd__dfu_8h_html_a3c39293bedc430e245f3f0919cb36e62add41639f9db3a8cc4c0183c039c2b6ed"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01e"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01ea1b6cb3fe0a26dce8a6fce9f179aa23ef"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01ea24195d3c70ed2d81039d3a0e306b3c94"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01ea5c827ad80eccc0249ee7ada76f36a8ac"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01ea6750bb1bc3aa5e183a24e5f1eebbc134"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01ea6c7e0d5ef61f350a4719b0d637dae263"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01ea7b90825d89b39d39d150336fe251982c"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01eab7ba8c8ed2c179fec88a9b6aafc663f0"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01eac112f5ac931419fca913cc4791c768cc"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01eadf68d3fd97017e0caba53637e530fc1d"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01eaf56d835eb6704702c3ddf5134402f82a"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01eaf6596caed39e4fc9a86c86fc48fb04ea"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01eafc200a88839dcdee3b90417f52b35657"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USB_CLASS_USBD_DFU_H
#define ZEPHYR_INCLUDE_USB_CLASS_USBD_DFU_H

#include <stdint.h>

/* DFU Class Subclass */
#define USB_DFU_SUBCLASS                0x01

/* DFU Class runtime Protocol */
#define USB_DFU_PROTOCOL_RUNTIME        0x01

/* DFU Class DFU mode Protocol */
#define USB_DFU_PROTOCOL_DFU            0x02

/* DFU Class Specific Requests */
#define USB_DFU_REQ_DETACH                      0x00
#define USB_DFU_REQ_DNLOAD                      0x01
#define USB_DFU_REQ_UPLOAD                      0x02
#define USB_DFU_REQ_GETSTATUS                   0x03
#define USB_DFU_REQ_CLRSTATUS                   0x04
#define USB_DFU_REQ_GETSTATE                    0x05
#define USB_DFU_REQ_ABORT                       0x06

/* Run-Time DFU Functional Descriptor */
struct usb_dfu_descriptor {
        uint8_t bLength;
        uint8_t bDescriptorType;
        uint8_t bmAttributes;
        uint16_t wDetachTimeOut;
        uint16_t wTransferSize;
        uint16_t bcdDFUVersion;
} __packed;

/* DFU Functional Descriptor Type */
#define USB_DESC_DFU_FUNCTIONAL                 0x21

/* DFU attributes DFU Functional Descriptor */
#define USB_DFU_ATTR_WILL_DETACH                BIT(3)
#define USB_DFU_ATTR_MANIFESTATION_TOLERANT     BIT(2)
#define USB_DFU_ATTR_CAN_UPLOAD                 BIT(1)
#define USB_DFU_ATTR_CAN_DNLOAD                 BIT(0)

/* DFU Specification release */
#define USB_DFU_VERSION                         0x0110

/* DFU device status */
enum usb_dfu_status {
        ERR_OK                  = 0x00,
        ERR_TARGET              = 0x01,
        ERR_FILE                = 0x02,
        ERR_WRITE               = 0x03,
        ERR_ERASE               = 0x04,
        ERR_CHECK_ERASED        = 0x05,
        ERR_PROG                = 0x06,
        ERR_VERIFY              = 0x07,
        ERR_ADDRESS             = 0x08,
        ERR_NOTDONE             = 0x09,
        ERR_FIRMWARE            = 0x0A,
        ERR_VENDOR              = 0x0B,
        ERR_USBR                = 0x0C,
        ERR_POR                 = 0x0D,
        ERR_UNKNOWN             = 0x0E,
        ERR_STALLEDPKT          = 0x0F,
};

/* DFU device states */
enum usb_dfu_state {
        APP_IDLE                = 0,
        APP_DETACH              = 1,
        DFU_IDLE                = 2,
        DFU_DNLOAD_SYNC         = 3,
        DFU_DNBUSY              = 4,
        DFU_DNLOAD_IDLE         = 5,
        DFU_MANIFEST_SYNC       = 6,
        DFU_MANIFEST            = 7,
        DFU_MANIFEST_WAIT_RST   = 8,
        DFU_UPLOAD_IDLE         = 9,
        DFU_ERROR               = 10,
        DFU_STATE_MAX           = 11,
};

struct usbd_dfu_image {
        const char *name;
        struct usb_if_descriptor *const if_desc;
        void *const priv;
        struct usbd_desc_node *const sd_nd;
        bool (*next_cb)(void *const priv,
                        const enum usb_dfu_state state, const enum usb_dfu_state next);
        int (*read_cb)(void *const priv,
                       const uint32_t block, const uint16_t size,
                       uint8_t buf[static CONFIG_USBD_DFU_TRANSFER_SIZE]);
        int (*write_cb)(void *const priv,
                        const uint32_t block, const uint16_t size,
                        const uint8_t buf[static CONFIG_USBD_DFU_TRANSFER_SIZE]);
};


#define USBD_DFU_DEFINE_IMG(id, iname, ipriv, iread, iwrite, inext)                     \
        static __noinit struct usb_if_descriptor usbd_dfu_iface_##id;                   \
                                                                                        \
        USBD_DESC_STRING_DEFINE(usbd_dfu_str_##id, iname, USBD_DUT_STRING_INTERFACE);   \
                                                                                        \
        static const STRUCT_SECTION_ITERABLE(usbd_dfu_image, usbd_dfu_image_##id) = {   \
                .name = iname,                                                          \
                .if_desc = &usbd_dfu_iface_##id,                                        \
                .priv = ipriv,                                                          \
                .sd_nd = &usbd_dfu_str_##id,                                            \
                .read_cb = iread,                                                       \
                .write_cb = iwrite,                                                     \
                .next_cb = inext,                                                       \
        }

#endif /* ZEPHYR_INCLUDE_USB_CLASS_USBD_DFU_H */
```

## 188.3\_源码注释与阅读说明

原始头文件署名为 Copyright (c) 2024 Nordic Semiconductor ASA，许可证为 Apache-2.0。包含保护（Header Include Guard）为 `ZEPHYR_INCLUDE_USB_CLASS_USBD_DFU_H`。源码中的普通英文注释对应下列含义，声明与标识符保持原样。

| 源码注释 | 中文含义 |
| --- | --- |
| DFU Class Subclass | DFU 类子类 |
| DFU Class runtime Protocol | DFU 类运行时协议 |
| DFU Class DFU mode Protocol | DFU 类的 DFU 模式协议 |
| DFU Class Specific Requests | DFU 类专用请求 |
| Run-Time DFU Functional Descriptor | 运行时 DFU 功能描述符 |
| DFU Functional Descriptor Type | DFU 功能描述符类型 |
| DFU attributes DFU Functional Descriptor | DFU 功能描述符的属性 |
| DFU Specification release | DFU 规范版本 |
| DFU device status | DFU 设备状态码 |
| DFU device states | DFU 设备状态 |

## 188.4\_源码跟踪与使用边界

译注依据保存的[旧版 DFU 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_dfu.h)、[新版 DFU 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_dfu.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_dfu.c)及[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/dfu/usb_dfu.c)，摘要见[来源记录](../SOURCES.md)。仓库内[旧版头文件](../../../include/zephyr/usb/class/usb_dfu.h)、[新版头文件](../../../include/zephyr/usb/class/usbd_dfu.h)、[新版实现](../../../subsys/usb/device_next/class/usbd_dfu.c)与[旧版实现](../../../subsys/usb/device/class/dfu/usb_dfu.c)用于相对路径跟踪，版本可能与官网不同。

本批未构建固件、执行镜像下载、擦写 Flash 或验证重启后的镜像。

[上一章](P187_DFU设备类头文件接口.md) · [返回大纲](大纲.md) · [下一章](P189_旧版DFU运行时描述符.md)
