---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-13
title: zephyr__pmci__mctp__mctp_usb.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__usb_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr__pmci__mctp__mctp_usb.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mctp__usb_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P013_zephyr__pmci__mctp__mctp_usb.h_头文件参考.md)。

## 13.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
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
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="foldopen00103"></a>
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
<a id="l00113"></a>
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
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__sem_html"></a>
<a id="astructmctp__binding__usb_html"></a>
<a id="astructmctp__usb__class__inst_html"></a>
<a id="astructmctp__usb__class__inst_html_a72a792cb05ef8d7ebdf0c97a6f371828"></a>
<a id="astructmctp__usb__class__inst_html_a8c93e48357b67467b729f111d7dc484d"></a>
<a id="astructmctp__usb__class__inst_html_aa436a766a2d3c4a29b64bed4fc86a099"></a>
<a id="astructusbd__class__data_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Intel Corporation
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */


#ifndef ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_USB_H_
#define ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_USB_H_

#include <zephyr/sys/iterable_sections.h>
#include <libmctp.h>

#define USBD_MCTP_SUBCLASS_MANAGEMENT_CONTROLLER   0
#define USBD_MCTP_SUBCLASS_MANAGED_DEVICE_ENDPOINT 0
#define USBD_MCTP_SUBCLASS_HOST_INTERFACE_ENDPOINT 1

#define USBD_MCTP_PROTOCOL_1_X 1
#define USBD_MCTP_PROTOCOL_2_X 2

/* Binding-specific defines, internal use */
#define MCTP_USB_HEADER_SIZE       4
#define MCTP_USB_MAX_PACKET_LENGTH 255

struct mctp_binding_usb {
        struct mctp_binding binding;
        struct usbd_class_data *usb_class_data;
        uint8_t tx_buf[MCTP_USB_HEADER_SIZE + MCTP_USB_MAX_PACKET_LENGTH];
        struct k_sem tx_lock;
        struct mctp_pktbuf *rx_pkt;
        uint8_t rx_data_idx;
        enum {
                STATE_WAIT_HDR_DMTF0,
                STATE_WAIT_HDR_DMTF1,
                STATE_WAIT_HDR_RSVD0,
                STATE_WAIT_HDR_LEN,
                STATE_DATA
        } rx_state;
        uint8_t tx_storage[MCTP_PKTBUF_SIZE(MCTP_PACKET_SIZE(MCTP_USB_MAX_PACKET_LENGTH))]
                PKTBUF_STORAGE_ALIGN;
};

struct mctp_usb_class_inst {
        uint8_t subclass;
        uint8_t mctp_protocol;
        struct mctp_binding_usb *mctp_binding;
};

int mctp_usb_start(struct mctp_binding *binding);
int mctp_usb_tx(struct mctp_binding *binding, struct mctp_pktbuf *pkt);

#define MCTP_USB_DEFINE(_name, _subclass, _protocol)                                            \
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

#endif /* ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_USB_H_ */
```

## 13.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Intel Corporation。

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 48 行

绑定专用的定义，仅供内部使用。

### 注释 3：原第 127 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_USB_H_`。

## 13.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P013_zephyr__pmci__mctp__mctp_usb.h_头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [mctp_binding_usb](../peripheral_bus_storage_model_reference/P031_mctp_binding_usb_结构体.md)
- [usbd_class_data](../usb/P028_USB类数据结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [mctp_usb_class_inst](../peripheral_bus_storage_model_reference/P032_mctp_usb_class_inst_结构体.md)
- [subclass](../peripheral_bus_storage_model_reference/P032_mctp_usb_class_inst_结构体.md#a72a792cb05ef8d7ebdf0c97a6f371828)
- [mctp_protocol](../peripheral_bus_storage_model_reference/P032_mctp_usb_class_inst_结构体.md#a8c93e48357b67467b729f111d7dc484d)
- [mctp_binding](../peripheral_bus_storage_model_reference/P032_mctp_usb_class_inst_结构体.md#aa436a766a2d3c4a29b64bed4fc86a099)
- [mctp_usb_class_inst::subclass](../peripheral_bus_storage_model_reference/P032_mctp_usb_class_inst_结构体.md#a72a792cb05ef8d7ebdf0c97a6f371828)
- [mctp_usb_class_inst::mctp_protocol](../peripheral_bus_storage_model_reference/P032_mctp_usb_class_inst_结构体.md#a8c93e48357b67467b729f111d7dc484d)
- [mctp_usb_class_inst::mctp_binding](../peripheral_bus_storage_model_reference/P032_mctp_usb_class_inst_结构体.md#aa436a766a2d3c4a29b64bed4fc86a099)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P012_zephyr__pmci__mctp__mctp_uart.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__drivers__memc.h_头文件源码.md)
