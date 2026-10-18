---
id: learning.zephyr-docs.api-source-reference.page-770
title: serial.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/serial_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第770章\_serial.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/serial_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/serial_8h.html)。

## 770.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="agroup__mcumgr__transport__serial_html_ga49006881d527ebba84948a913a83c17e"></a>
<a id="agroup__mcumgr__transport__serial_html_gaa510a98df8b01ccf5bae8eacc9c59078"></a>
<a id="agroup__mcumgr__transport__serial_html_gaca191e14700f0c2da9643e7daa582867"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructmcumgr__serial__rx__ctxt_html"></a>
<a id="astructmcumgr__serial__rx__ctxt_html_a4ded2b7748334b0f3166f4c18cd1d6b0"></a>
<a id="astructmcumgr__serial__rx__ctxt_html_a5fdf2dd95185a49806c1900184c7bdfc"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_ac6eef59915e7ce167442fdacbbfb5e56"></a>
<a id="astructnet__buf_html_ae75b7ca728fb7440ea483be8bf88bc38"></a>

```c
/*
 * Copyright Runtime.io 2018. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SERIAL_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SERIAL_H_


#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MCUMGR_SERIAL_HDR_PKT       0x0609
#define MCUMGR_SERIAL_HDR_FRAG      0x0414
#define MCUMGR_SERIAL_MAX_FRAME     127

#define MCUMGR_SERIAL_HDR_PKT_1     (MCUMGR_SERIAL_HDR_PKT >> 8)
#define MCUMGR_SERIAL_HDR_PKT_2     (MCUMGR_SERIAL_HDR_PKT & 0xff)
#define MCUMGR_SERIAL_HDR_FRAG_1    (MCUMGR_SERIAL_HDR_FRAG >> 8)
#define MCUMGR_SERIAL_HDR_FRAG_2    (MCUMGR_SERIAL_HDR_FRAG & 0xff)

struct mcumgr_serial_rx_ctxt {
        struct net_buf *nb;

        uint16_t pkt_len;

#if defined(CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_SMP_OVER_CONSOLE) && \
        defined(CONFIG_MCUMGR_TRANSPORT_SERIAL_HAS_RAW_BINARY_NON_SMP_OVER_CONSOLE)
        const bool raw_transport;
#endif
};

typedef int (*mcumgr_serial_tx_cb)(const void *data, int len);

struct net_buf *mcumgr_serial_process_frag(
        struct mcumgr_serial_rx_ctxt *rx_ctxt,
        const uint8_t *frag, int frag_len);

int mcumgr_serial_tx_pkt(const uint8_t *data, int len, mcumgr_serial_tx_cb cb);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SERIAL_H_ */
```

## 770.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：Runtime.io 2018. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 119 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SERIAL_H_`。

## 770.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/serial_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [mcumgr_serial_rx_ctxt](../system_service_model_reference/P065_mcumgr_serial_rx_ctxt_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [nb](../system_service_model_reference/P065_mcumgr_serial_rx_ctxt_结构体.md#a5fdf2dd95185a49806c1900184c7bdfc)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [pkt_len](../system_service_model_reference/P065_mcumgr_serial_rx_ctxt_结构体.md#a4ded2b7748334b0f3166f4c18cd1d6b0)
- [mcumgr_serial_tx_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga49006881d527ebba84948a913a83c17e)
- [data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [mcumgr_serial_process_frag](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#gaa510a98df8b01ccf5bae8eacc9c59078)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mcumgr_serial_tx_pkt](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#gaca191e14700f0c2da9643e7daa582867)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [mcumgr_serial_rx_ctxt::pkt_len](../system_service_model_reference/P065_mcumgr_serial_rx_ctxt_结构体.md#a4ded2b7748334b0f3166f4c18cd1d6b0)
- [mcumgr_serial_rx_ctxt::nb](../system_service_model_reference/P065_mcumgr_serial_rx_ctxt_结构体.md#a5fdf2dd95185a49806c1900184c7bdfc)
- [net_buf::data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [net_buf::len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)

---

[上一章](P769_uart_emul.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P771_settings_mgmt.h_源码浏览.md)
