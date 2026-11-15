---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-12
title: zephyr__pmci__mctp__mctp_uart.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__uart_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr__pmci__mctp__mctp_uart.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mctp__uart_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P012_zephyr__pmci__mctp__mctp_uart.h_头文件参考.md)。

## 12.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="foldopen00025"></a>
<a id="l00025"></a>
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
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="foldopen00098"></a>
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
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="akernel_8h_html"></a>
<a id="amctp__uart_8h_html_ad4c5c12a116c6b1ed671887c5bd7ff94"></a>
<a id="amctp__uart_8h_html_aee9f5132cc9cfbc3c5223a89e59dc667"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructmctp__binding__uart_html"></a>

```c
/*
 * Copyright (c) 2024 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */


#ifndef ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_UART_H_
#define ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_UART_H_

#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <libmctp.h>

struct mctp_binding_uart {
        struct mctp_binding binding;
        const struct device *dev;

        /* receive buffers and state */
        struct k_sem rx_disabled;
        uint8_t rx_buf[2][256];
        bool rx_buf_used[2];
        struct mctp_pktbuf *rx_pkt;
        uint8_t rx_exp_len;
        uint16_t rx_fcs;
        uint16_t rx_fcs_calc;
        enum {
                STATE_WAIT_SYNC_START,
                STATE_WAIT_REVISION,
                STATE_WAIT_LEN,
                STATE_DATA,
                STATE_DATA_ESCAPED,
                STATE_WAIT_FCS1,
                STATE_WAIT_FCS2,
                STATE_WAIT_SYNC_END,
        } rx_state;
        int rx_res;

        /* staging buffer for tx */
        struct k_sem tx_done;
        uint8_t tx_buf[256];
        int tx_res;
        bool waiting;

        /* Keep track of all UART bindings */
        sys_snode_t node;

        uint8_t tx_storage[MCTP_PKTBUF_SIZE(MCTP_PACKET_SIZE(MCTP_BTU))] PKTBUF_STORAGE_ALIGN;

};

void mctp_uart_start_rx(struct mctp_binding_uart *uart);

int mctp_uart_stop_rx(struct mctp_binding_uart *uart);

int mctp_uart_start(struct mctp_binding *binding);
int mctp_uart_tx(struct mctp_binding *binding, struct mctp_pktbuf *pkt);

#define MCTP_UART_DT_DEFINE(_name, _dev)                                                           \
        struct mctp_binding_uart _name = {                                                         \
                .binding =                                                                         \
                        {                                                                          \
                                .name = STRINGIFY(_name), .version = 1,                            \
                                                  .pkt_size = MCTP_PACKET_SIZE(MCTP_BTU),          \
                                                  .pkt_header = 0, .pkt_trailer = 0,               \
                                                  .tx_storage = _name.tx_storage,          \
                                                  .start = mctp_uart_start, .tx = mctp_uart_tx,    \
                                },                                                                 \
                                .dev = _dev,                                                       \
                                .rx_state = STATE_WAIT_SYNC_START,                                 \
                                .rx_pkt = NULL,                                                    \
                                .rx_res = 0,                                                       \
                                .tx_res = 0,                                                       \
        };

#endif /* ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_UART_H_ */
```

## 12.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 30 行

接收缓冲区与状态。

### 注释 3：原第 50 行

用于发送（TX）的暂存缓冲区（Staging buffer）。

### 注释 4：原第 56 行

跟踪所有 UART 绑定（Bindings）。

### 注释 5：原第 115 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PMCI_MCTP_MCTP_UART_H_`。

## 12.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P012_zephyr__pmci__mctp__mctp_uart.h_头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [mctp_binding_uart](../peripheral_bus_storage_model_reference/P030_mctp_binding_uart_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [mctp_uart_start_rx](../peripheral_bus_storage_header_reference/P012_zephyr__pmci__mctp__mctp_uart.h_头文件参考.md#ad4c5c12a116c6b1ed671887c5bd7ff94)
- [mctp_uart_stop_rx](../peripheral_bus_storage_header_reference/P012_zephyr__pmci__mctp__mctp_uart.h_头文件参考.md#aee9f5132cc9cfbc3c5223a89e59dc667)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P011_zephyr__pmci__mctp__mctp_i3c_target.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__pmci__mctp__mctp_usb.h_头文件源码.md)
