---
id: learning.zephyr-docs.api-source-reference.page-888
title: usb_hub.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__hub_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第888章\_usb\_hub.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usb__hub_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usb__hub_8h.html)。

## 888.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="foldopen00191"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="foldopen00197"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="foldopen00219"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="foldopen00229"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructusb__hub__descriptor_html"></a>
<a id="astructusb__hub__descriptor_html_a1023ff5e3940284d86cf50fa25790ffe"></a>
<a id="astructusb__hub__descriptor_html_a2e62093b8304fe73becf63e8aa782c07"></a>
<a id="astructusb__hub__descriptor_html_a59dc42682121858aaeafac01deccd4e2"></a>
<a id="astructusb__hub__descriptor_html_ac4ef3bbf42df2e2caf582b566181a6a3"></a>
<a id="astructusb__hub__descriptor_html_af3d2523eaa7a4bd827105d9b61dcc8f0"></a>
<a id="astructusb__hub__descriptor_html_afeed7baf0d900ac0bcaac30afe65ee40"></a>
<a id="astructusb__hub__port__status_html"></a>
<a id="astructusb__hub__port__status_html_a0ce3b5e431b2153e9253c952ad49cfa1"></a>
<a id="astructusb__hub__port__status_html_a4e6e6bb6a2cc13c88456a4b391da3368"></a>
<a id="astructusb__hub__status_html"></a>
<a id="astructusb__hub__status_html_a69a3d6303815aef12358eb1f7da3d710"></a>
<a id="astructusb__hub__status_html_a9207edfd7adca1ab7339b3169595c96a"></a>

```c
/*
 * Copyright (c) 2022 Emerson Electric Co.
 * SPDX-FileCopyrightText: Copyright 2026 NXP
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USB_CLASS_USB_HUB_H_
#define ZEPHYR_INCLUDE_USB_CLASS_USB_HUB_H_

#define USB_HUB_CLASS_CODE              0x09
#define USB_HUB_SUBCLASS_CODE           0x00
#define USB_HUB_PROTOCOL_FS             0x00
#define USB_HUB_PROTOCOL_HS_SINGLE_TT   0x01
#define USB_HUB_PROTOCOL_HS_MULTI_TT    0x02
#define USB_HUB_PROTOCOL_CODE           USB_HUB_PROTOCOL_HS_SINGLE_TT

#define USB_HUB_DESCRIPTOR_TYPE         0x29

#define USB_HCREQ_GET_STATUS            0x00
#define USB_HCREQ_CLEAR_FEATURE         0x01
#define USB_HCREQ_SET_FEATURE           0x03
#define USB_HCREQ_GET_DESCRIPTOR        0x06
#define USB_HCREQ_SET_DESCRIPTOR        0x07
#define USB_HCREQ_CLEAR_TT_BUFFER       0x08
#define USB_HCREQ_RESET_TT              0x09
#define USB_HCREQ_GET_TT_STATE          0x0A
#define USB_HCREQ_STOP_TT               0x0B

#define USB_HCFS_C_HUB_LOCAL_POWER      0x00
#define USB_HCFS_C_HUB_OVER_CURRENT     0x01
#define USB_HCFS_PORT_CONNECTION        0x00
#define USB_HCFS_PORT_ENABLE            0x01
#define USB_HCFS_PORT_SUSPEND           0x02
#define USB_HCFS_PORT_OVER_CURRENT      0x03
#define USB_HCFS_PORT_RESET             0x04
#define USB_HCFS_PORT_POWER             0x08
#define USB_HCFS_PORT_LOW_SPEED         0x09
#define USB_HCFS_C_PORT_CONNECTION      0x10
#define USB_HCFS_C_PORT_ENABLE          0x11
#define USB_HCFS_C_PORT_SUSPEND         0x12
#define USB_HCFS_C_PORT_OVER_CURRENT    0x13
#define USB_HCFS_C_PORT_RESET           0x14
#define USB_HCFS_PORT_TEST              0x15
#define USB_HCFS_PORT_INDICATOR         0x16

#define USB_HUB_STATUS_LOCAL_POWER      BIT(0)
#define USB_HUB_STATUS_OVER_CURRENT     BIT(1)

#define USB_HUB_CHANGE_LOCAL_POWER      BIT(0)
#define USB_HUB_CHANGE_OVER_CURRENT     BIT(1)

#define USB_HUB_PORT_STATUS_CONNECTION          BIT(0)
#define USB_HUB_PORT_STATUS_ENABLE              BIT(1)
#define USB_HUB_PORT_STATUS_SUSPEND             BIT(2)
#define USB_HUB_PORT_STATUS_OVER_CURRENT        BIT(3)
#define USB_HUB_PORT_STATUS_RESET               BIT(4)
#define USB_HUB_PORT_STATUS_POWER               BIT(8)
#define USB_HUB_PORT_STATUS_LOW_SPEED           BIT(9)
#define USB_HUB_PORT_STATUS_HIGH_SPEED          BIT(10)
#define USB_HUB_PORT_STATUS_TEST                BIT(11)
#define USB_HUB_PORT_STATUS_INDICATOR           BIT(12)

#define USB_HUB_PORT_CHANGE_CONNECTION          BIT(0)
#define USB_HUB_PORT_CHANGE_ENABLE              BIT(1)
#define USB_HUB_PORT_CHANGE_SUSPEND             BIT(2)
#define USB_HUB_PORT_CHANGE_OVER_CURRENT        BIT(3)
#define USB_HUB_PORT_CHANGE_RESET               BIT(4)

#define USB_HUB_DESC_BUF_SIZE 71

#define USB_HUB_GET_THINK_TIME(wHubCharacteristics) \
        (((((wHubCharacteristics) & 0x0060U) >> 5) + 1) << 3)

struct usb_hub_descriptor {
        uint8_t bDescLength;
        uint8_t bDescriptorType;
        uint8_t bNbrPorts;
        uint16_t wHubCharacteristics;
        uint8_t bPwrOn2PwrGood;
        uint8_t bHubContrCurrent;
} __packed;

struct usb_hub_status {
        uint16_t wHubStatus;
        uint16_t wHubChange;
} __packed;

struct usb_hub_port_status {
        uint16_t wPortStatus;
        uint16_t wPortChange;
} __packed;

#endif /* ZEPHYR_INCLUDE_USB_CLASS_USB_HUB_H_ */
```

## 888.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Emerson Electric Co.。

SPDX 文件版权声明（FileCopyrightText）：Copyright 2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 236 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USB_CLASS_USB_HUB_H_`。

## 888.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usb__hub_8h.html)
- [usb_hub_descriptor](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bDescLength](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md#afeed7baf0d900ac0bcaac30afe65ee40)
- [bDescriptorType](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md#a2e62093b8304fe73becf63e8aa782c07)
- [bNbrPorts](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md#af3d2523eaa7a4bd827105d9b61dcc8f0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [wHubCharacteristics](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md#a1023ff5e3940284d86cf50fa25790ffe)
- [bPwrOn2PwrGood](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md#ac4ef3bbf42df2e2caf582b566181a6a3)
- [bHubContrCurrent](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md#a59dc42682121858aaeafac01deccd4e2)
- [usb_hub_status](../device_power_control_model_reference/P099_usb_hub_status_结构体.md)
- [wHubStatus](../device_power_control_model_reference/P099_usb_hub_status_结构体.md#a9207edfd7adca1ab7339b3169595c96a)
- [wHubChange](../device_power_control_model_reference/P099_usb_hub_status_结构体.md#a69a3d6303815aef12358eb1f7da3d710)
- [usb_hub_port_status](../device_power_control_model_reference/P098_usb_hub_port_status_结构体.md)
- [wPortStatus](../device_power_control_model_reference/P098_usb_hub_port_status_结构体.md#a4e6e6bb6a2cc13c88456a4b391da3368)
- [wPortChange](../device_power_control_model_reference/P098_usb_hub_port_status_结构体.md#a0ce3b5e431b2153e9253c952ad49cfa1)
- [usb_hub_descriptor::wHubCharacteristics](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md#a1023ff5e3940284d86cf50fa25790ffe)
- [usb_hub_descriptor::bDescriptorType](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md#a2e62093b8304fe73becf63e8aa782c07)
- [usb_hub_descriptor::bHubContrCurrent](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md#a59dc42682121858aaeafac01deccd4e2)
- [usb_hub_descriptor::bPwrOn2PwrGood](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md#ac4ef3bbf42df2e2caf582b566181a6a3)
- [usb_hub_descriptor::bNbrPorts](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md#af3d2523eaa7a4bd827105d9b61dcc8f0)
- [usb_hub_descriptor::bDescLength](../device_power_control_model_reference/P097_usb_hub_descriptor_结构体.md#afeed7baf0d900ac0bcaac30afe65ee40)
- [usb_hub_port_status::wPortChange](../device_power_control_model_reference/P098_usb_hub_port_status_结构体.md#a0ce3b5e431b2153e9253c952ad49cfa1)
- [usb_hub_port_status::wPortStatus](../device_power_control_model_reference/P098_usb_hub_port_status_结构体.md#a4e6e6bb6a2cc13c88456a4b391da3368)
- [usb_hub_status::wHubChange](../device_power_control_model_reference/P099_usb_hub_status_结构体.md#a69a3d6303815aef12358eb1f7da3d710)
- [usb_hub_status::wHubStatus](../device_power_control_model_reference/P099_usb_hub_status_结构体.md#a9207edfd7adca1ab7339b3169595c96a)

---

[上一章](P887_updatehub.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P889_usbc.h_源码浏览.md)
