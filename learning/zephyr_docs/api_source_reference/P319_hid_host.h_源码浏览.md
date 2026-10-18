---
id: learning.zephyr-docs.api-source-reference.page-319
title: hid_host.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hid__host_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第319章\_hid\_host.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hid__host_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hid__host_8h.html)。

## 319.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00039"></a>
<a id="l00040"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="abluetooth_2classic_2hid_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__hid__host_html_ga0415ec8597cb6ccc1016703438ac4f48"></a>
<a id="agroup__bt__hid__host_html_ga15db8aa5b2e56048a7e513730918ef50"></a>
<a id="agroup__bt__hid__host_html_ga2a7d73c8ad7faff0ece2217f35757576"></a>
<a id="agroup__bt__hid__host_html_ga45726162f45815aa9c2dc789e3b2beed"></a>
<a id="agroup__bt__hid__host_html_ga5061be29cffeb76c1be0c5f7912f4cc8"></a>
<a id="agroup__bt__hid__host_html_ga66ce643cbff7dbeb7dc4d4fe2b5476d7"></a>
<a id="agroup__bt__hid__host_html_ga6f7f967c1aa2cd15ba434fda1584b511"></a>
<a id="agroup__bt__hid__host_html_ga80472c16b68cfb7d1e8d9f73379e612a"></a>
<a id="agroup__bt__hid__host_html_ga86d49efef335609422f23b52717c9e1b"></a>
<a id="agroup__bt__hid__host_html_ga8911b406dff5b2a0dd21f9abe3a571d5"></a>
<a id="agroup__bt__hid__host_html_gac0101a4f54d50d6615fc7cce41044107"></a>
<a id="agroup__bt__hid__host_html_gae13a5ae2473c239b4b109cd8e5b9a210"></a>
<a id="agroup__bt__hid__host_html_gae52c3d2ed7dd2a6868f9dff584ac2da4"></a>
<a id="agroup__bt__hid__host_html_gaf1998a703fcf34e51e051a7a4c42937b"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__hid__host__cb_html"></a>
<a id="astructbt__hid__host__cb_html_a26bd138b7be11a6402845fbfb7fdfbb3"></a>
<a id="astructbt__hid__host__cb_html_a32df7ffd5ee0092297a146925d888dd8"></a>
<a id="astructbt__hid__host__cb_html_a412114fad2e0624f96803827be7cd54a"></a>
<a id="astructbt__hid__host__cb_html_a78389dc6d2b89f4c16b95268a0c524e7"></a>
<a id="astructbt__hid__host__cb_html_a8f5f6486fa37551922b18a62f8b75730"></a>
<a id="astructbt__hid__host__cb_html_a94cf9747616471c4ba2cec2057f714a9"></a>
<a id="astructbt__hid__host__cb_html_a973e729e0633f5fbecc2c6270ea15d6c"></a>
<a id="astructbt__hid__host__cb_html_aabeb2d9589813690eec77297113090cd"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf_html"></a>

```c


/*
 * Copyright 2026 Xiaomi Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_HID_HOST_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_HID_HOST_H_


#include <stdbool.h>
#include <stdint.h>

#include <zephyr/bluetooth/classic/hid.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/net_buf.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_hid_host;

struct bt_hid_host_cb {
        void (*connected)(struct bt_hid_host *hid);

        void (*disconnected)(struct bt_hid_host *hid);

        void (*input_report)(struct bt_hid_host *hid, struct net_buf *buf);

        void (*get_report)(struct bt_hid_host *hid, uint8_t result_code, uint8_t type,
                           struct net_buf *buf);

        void (*set_report)(struct bt_hid_host *hid, uint8_t result_code);

        void (*get_protocol)(struct bt_hid_host *hid, uint8_t result_code, uint8_t protocol);

        void (*set_protocol)(struct bt_hid_host *hid, uint8_t result_code);

        void (*vc_unplug)(struct bt_hid_host *hid);
};

int bt_hid_host_register(const struct bt_hid_host_cb *cb);

int bt_hid_host_unregister(void);

int bt_hid_host_connect(struct bt_conn *conn, struct bt_hid_host **hid);

struct bt_conn *bt_hid_host_get_conn(struct bt_hid_host *hid);

int bt_hid_host_disconnect(struct bt_hid_host *hid);

int bt_hid_host_get_report(struct bt_hid_host *hid, uint8_t type, uint8_t report_id,
                           uint16_t buffer_size);

int bt_hid_host_set_report(struct bt_hid_host *hid, uint8_t type,
                           struct net_buf *buf);

int bt_hid_host_get_protocol(struct bt_hid_host *hid);

int bt_hid_host_set_protocol(struct bt_hid_host *hid, uint8_t protocol);

int bt_hid_host_output_report(struct bt_hid_host *hid, struct net_buf *buf);

int bt_hid_host_suspend(struct bt_hid_host *hid);

int bt_hid_host_exit_suspend(struct bt_hid_host *hid);

int bt_hid_host_virtual_cable_unplug(struct bt_hid_host *hid);

struct net_buf *bt_hid_host_create_pdu(struct net_buf_pool *pool);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_HID_HOST_H_ */
```

## 319.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：2026 Xiaomi Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 362 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_HID_HOST_H_`。

## 319.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hid__host_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/classic/hid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2hid_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_hid_host_cb](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md)
- [connected](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a973e729e0633f5fbecc2c6270ea15d6c)
- [disconnected](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a8f5f6486fa37551922b18a62f8b75730)
- [input_report](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a78389dc6d2b89f4c16b95268a0c524e7)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [get_report](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#aabeb2d9589813690eec77297113090cd)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [set_report](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a32df7ffd5ee0092297a146925d888dd8)
- [get_protocol](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a94cf9747616471c4ba2cec2057f714a9)
- [set_protocol](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a412114fad2e0624f96803827be7cd54a)
- [vc_unplug](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a26bd138b7be11a6402845fbfb7fdfbb3)
- [bt_hid_host_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga86d49efef335609422f23b52717c9e1b)
- [bt_hid_host_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#gaf1998a703fcf34e51e051a7a4c42937b)
- [bt_hid_host_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga8911b406dff5b2a0dd21f9abe3a571d5)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_hid_host_get_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga5061be29cffeb76c1be0c5f7912f4cc8)
- [bt_hid_host_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#gac0101a4f54d50d6615fc7cce41044107)
- [bt_hid_host_get_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#gae52c3d2ed7dd2a6868f9dff584ac2da4)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_hid_host_set_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga2a7d73c8ad7faff0ece2217f35757576)
- [bt_hid_host_get_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga45726162f45815aa9c2dc789e3b2beed)
- [bt_hid_host_set_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#gae13a5ae2473c239b4b109cd8e5b9a210)
- [bt_hid_host_output_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga0415ec8597cb6ccc1016703438ac4f48)
- [bt_hid_host_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga15db8aa5b2e56048a7e513730918ef50)
- [bt_hid_host_exit_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga80472c16b68cfb7d1e8d9f73379e612a)
- [bt_hid_host_virtual_cable_unplug](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga6f7f967c1aa2cd15ba434fda1584b511)
- [bt_hid_host_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga66ce643cbff7dbeb7dc4d4fe2b5476d7)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [hid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2hid_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_hid_host_cb::vc_unplug](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a26bd138b7be11a6402845fbfb7fdfbb3)
- [bt_hid_host_cb::set_report](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a32df7ffd5ee0092297a146925d888dd8)
- [bt_hid_host_cb::set_protocol](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a412114fad2e0624f96803827be7cd54a)
- [bt_hid_host_cb::input_report](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a78389dc6d2b89f4c16b95268a0c524e7)
- [bt_hid_host_cb::disconnected](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a8f5f6486fa37551922b18a62f8b75730)
- [bt_hid_host_cb::get_protocol](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a94cf9747616471c4ba2cec2057f714a9)
- [bt_hid_host_cb::connected](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#a973e729e0633f5fbecc2c6270ea15d6c)
- [bt_hid_host_cb::get_report](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md#aabeb2d9589813690eec77297113090cd)

---

[上一章](P318_hid_device.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P320_histogram.h_源码浏览.md)
