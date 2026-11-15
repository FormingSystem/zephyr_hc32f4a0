---
id: learning.zephyr-docs.usb.api-186
title: DFU公共头文件源码
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__dfu_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2015,2016 Intel Corporation. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第186章\_DFU公共头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb__dfu_8h_source.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 186.1\_阅读说明与来源

译注：本组补齐设备固件升级（Device Firmware Upgrade，DFU）的头文件参考、协议状态和功能描述符，分别标明旧版设备栈与新版设备栈。镜像定义宏及回调说明见[设备固件升级 API](P062_USB设备固件升级API.md)和[镜像结构](P063_USB固件升级镜像结构.md)；本页不会仅凭描述符字段推定目标板已具备升级能力。

下方完整保留官方 Doxygen 源码浏览页中的代码及许可注释；仅移除网页行号、还原显示空格并清理行尾空白。浏览页省略的 API 文档注释由对应头文件参考和[DFU API 译文](P062_USB设备固件升级API.md)承接。此页展示不冒充包含全部注释的原始头文件。

## 186.2\_原始源码展示

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
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="foldopen00084"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="foldopen00094"></a>
<a id="l00094"></a>
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
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="foldopen00114"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="aclock_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdfu__runtime__descriptor_html"></a>
<a id="astructdfu__runtime__descriptor_html_a0eeecced453c285febca7a9d867c7241"></a>
<a id="astructdfu__runtime__descriptor_html_a3dca4dc35930794eaa0ac03522949048"></a>
<a id="astructdfu__runtime__descriptor_html_a5464341cf3c706af93de58c6db5edfb9"></a>
<a id="astructdfu__runtime__descriptor_html_a86312a99ed7c89eb027ca3e35b7b32e5"></a>
<a id="astructdfu__runtime__descriptor_html_aa8d5f353530adf846b14e88c97095a50"></a>
<a id="astructdfu__runtime__descriptor_html_adaf32d218daf9fc74a6639845355cd9b"></a>
<a id="astructk__timeout__t_html"></a>
<a id="ausb__dfu_8h_html_a3f025bde53c777c5e0493ef54bbeb143"></a>
<a id="ausb__dfu_8h_html_a3f025bde53c777c5e0493ef54bbeb143a002e3cc408cf56d51c6cd2b0d90f1b7c"></a>
<a id="ausb__dfu_8h_html_a3f025bde53c777c5e0493ef54bbeb143a15ff004b2336c3e5b88e3edd276b32fd"></a>
<a id="ausb__dfu_8h_html_a3f025bde53c777c5e0493ef54bbeb143a541f6e1c465d547c1265ba6bde6c59c2"></a>
<a id="ausb__dfu_8h_html_a3f025bde53c777c5e0493ef54bbeb143a64a13d4b1b2cc0b0a40069d8c28fe74c"></a>
<a id="ausb__dfu_8h_html_a3f025bde53c777c5e0493ef54bbeb143a68f32e308ff090838040f69ddcab8fff"></a>
<a id="ausb__dfu_8h_html_a3f025bde53c777c5e0493ef54bbeb143a71f82402de0db9a8f3263f045f87bcc1"></a>
<a id="ausb__dfu_8h_html_a3f025bde53c777c5e0493ef54bbeb143aa6e5b30fd65a5485046759f438be29d8"></a>
<a id="ausb__dfu_8h_html_a3f025bde53c777c5e0493ef54bbeb143aadb4993cd9183666f3ef9fd82a4519fa"></a>
<a id="ausb__dfu_8h_html_a3f025bde53c777c5e0493ef54bbeb143aaffa9156a82ef21608e730325d8bb2c6"></a>
<a id="ausb__dfu_8h_html_a3f025bde53c777c5e0493ef54bbeb143ad5eb9bbb1f4eb27a0ac7e60c0bf5341f"></a>
<a id="ausb__dfu_8h_html_a3f025bde53c777c5e0493ef54bbeb143afd398c862995dfe599a9f182fa1e902e"></a>
<a id="ausb__dfu_8h_html_a892959f521c403e4ec295c252e75e5dc"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31a0123f1a634c8d384393557aedecb0788"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31a08770dc5628ca360ef8a5ecfdf3d2210"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31a251a276fd7bfe2744888dc97fe956aff"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31a4f6d9b9397bdaf8c52b1a3b21814795d"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31a56c7583a5956d85dc99cf250f8c7771e"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31a5816bb25bcc32867630963dba649cc54"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31a62181eec68b16d43c1aee03174f9bba1"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31a65c1f54049798ea81c7d1719f166a1be"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31a7006bd30ea4310800fa059ddc8d30947"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31a7465c34dd18ad03c8cbe13e3d395c902"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31a770d6396237b7deac15001165ef9c9bb"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31a992b1de144265596023b92aa21094ecb"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31aa69cd762eb2bcefece21d4601c51f471"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31aacb4bde78f2c57c18dc2dc3d5249f2c8"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31acf11a7eb0a529adca2b399a6b81c8d19"></a>
<a id="ausb__dfu_8h_html_abcf2757cf1c6281a06a8a6f25ff2aa31af30286bf44938bdea942a7f3c513d998"></a>

```c
/* SPDX-License-Identifier: BSD-3-Clause */

/***************************************************************************
 *
 * Copyright (c) 2015,2016 Intel Corporation.
 * Copyright (c) 2017 PHYTEC Messtechnik GmbH
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * * Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 * * Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in
 * the documentation and/or other materials provided with the
 * distribution.
 * * Neither the name of Intel Corporation nor the names of its
 * contributors may be used to endorse or promote products derived
 * from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 ***************************************************************************/


#ifndef ZEPHYR_INCLUDE_USB_CLASS_USB_DFU_H_
#define ZEPHYR_INCLUDE_USB_CLASS_USB_DFU_H_

#include <zephyr/sys/clock.h>

#define DFU_SUBCLASS                    0x01 __DEPRECATED_MACRO

#define DFU_RT_PROTOCOL                 0x01 __DEPRECATED_MACRO

#define DFU_MODE_PROTOCOL               0x02 __DEPRECATED_MACRO

#define DFU_DETACH                      0x00 __DEPRECATED_MACRO
#define DFU_DNLOAD                      0x01 __DEPRECATED_MACRO
#define DFU_UPLOAD                      0x02 __DEPRECATED_MACRO
#define DFU_GETSTATUS                   0x03 __DEPRECATED_MACRO
#define DFU_CLRSTATUS                   0x04 __DEPRECATED_MACRO
#define DFU_GETSTATE                    0x05 __DEPRECATED_MACRO
#define DFU_ABORT                       0x06 __DEPRECATED_MACRO

#define DFU_FUNC_DESC                   0x21 __DEPRECATED_MACRO

#define DFU_ATTR_WILL_DETACH            0x08 __DEPRECATED_MACRO
#define DFU_ATTR_MANIFESTATION_TOLERANT 0x04 __DEPRECATED_MACRO
#define DFU_ATTR_CAN_UPLOAD             0x02 __DEPRECATED_MACRO
#define DFU_ATTR_CAN_DNLOAD             0x01 __DEPRECATED_MACRO

#define DFU_VERSION                     0x0110 __DEPRECATED_MACRO

struct dfu_runtime_descriptor {
        uint8_t bLength;
        uint8_t bDescriptorType;
        uint8_t bmAttributes;
        uint16_t wDetachTimeOut;
        uint16_t wTransferSize;
        uint16_t bcdDFUVersion;
} __packed;

enum dfu_status {
        statusOK,
        errTARGET,
        errFILE,
        errWRITE,
        errERASE,
        errCHECK_ERASED,
        errPROG,
        errVERIFY,
        errADDRESS,
        errNOTDONE,
        errFIRMWARE,
        errVENDOR,
        errUSB,
        errPOR,
        errUNKNOWN,
        errSTALLEDPKT
};

enum dfu_state {
        appIDLE,
        appDETACH,
        dfuIDLE,
        dfuDNLOAD_SYNC,
        dfuDNBUSY,
        dfuDNLOAD_IDLE,
        dfuMANIFEST_SYNC,
        dfuMANIFEST,
        dfuMANIFEST_WAIT_RST,
        dfuUPLOAD_IDLE,
        dfuERROR,
};

__deprecated void wait_for_usb_dfu(k_timeout_t delay);

#endif /* ZEPHYR_INCLUDE_USB_CLASS_USB_DFU_H_ */
```

## 186.3\_源码注释与阅读说明

原始头文件采用 BSD-3-Clause，Intel Corporation（2015、2016）和 PHYTEC Messtechnik GmbH（2017）的署名、再分发条件与免责声明逐字保留。`__DEPRECATED_MACRO` 和 `__deprecated` 标记说明旧接口已弃用；头文件包含保护（Header Include Guard）为 `ZEPHYR_INCLUDE_USB_CLASS_USB_DFU_H_`。

## 186.4\_源码跟踪与使用边界

译注依据保存的[旧版 DFU 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_dfu.h)、[新版 DFU 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_dfu.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_dfu.c)及[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/dfu/usb_dfu.c)，摘要见[来源记录](../SOURCES.md)。仓库内[旧版头文件](../../../include/zephyr/usb/class/usb_dfu.h)、[新版头文件](../../../include/zephyr/usb/class/usbd_dfu.h)、[新版实现](../../../subsys/usb/device_next/class/usbd_dfu.c)与[旧版实现](../../../subsys/usb/device/class/dfu/usb_dfu.c)用于相对路径跟踪，版本可能与官网不同。

> 译注：本页属于已弃用的旧版 DFU 接口，保留用于阅读和迁移对照；新实现从[新版 DFU API](P062_USB设备固件升级API.md)阅读。

本批未构建固件、执行镜像下载、擦写 Flash 或验证重启后的镜像。

[上一章](P185_DFU功能描述符.md) · [返回大纲](大纲.md) · [下一章](P187_DFU设备类头文件接口.md)
