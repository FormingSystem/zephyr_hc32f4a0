---
id: learning.zephyr-docs.api-source-reference.page-318
title: hid_device.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hid__device_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第318章\_hid\_device.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hid__device_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hid__device_8h.html)。

## 318.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="abluetooth_2classic_2hid_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__hid__device_html_ga1034935eec4ff6a466990ee5f0c1ba2c"></a>
<a id="agroup__bt__hid__device_html_ga296d1b9695091507438261035d067c02"></a>
<a id="agroup__bt__hid__device_html_ga35b0ec48658daa94010bef0c91503491"></a>
<a id="agroup__bt__hid__device_html_ga63608252095d8c0638c6c43809e42553"></a>
<a id="agroup__bt__hid__device_html_gab5b6b5f1047961ed5164f4e1059201ad"></a>
<a id="agroup__bt__hid__device_html_gad6bc5203aa9a2c8e4e217005f8f58b2e"></a>
<a id="agroup__bt__hid__device_html_gae2000b4d39ed956cb37298bfcab351ed"></a>
<a id="agroup__bt__hid__device_html_gaf30d808e9903988d72d831c3c4aab617"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__hid__device__cb_html"></a>
<a id="astructbt__hid__device__cb_html_a21ca7e5d28b575007fb12dbfe779d83a"></a>
<a id="astructbt__hid__device__cb_html_a42c35e661602bb1c8f5687ce04b055ef"></a>
<a id="astructbt__hid__device__cb_html_a59768788c42e4369146767b95f9a22df"></a>
<a id="astructbt__hid__device__cb_html_a6221aa4f32aaa913536cb1ae70173a8e"></a>
<a id="astructbt__hid__device__cb_html_a71ee8022e59c83e2b28318432355663d"></a>
<a id="astructbt__hid__device__cb_html_a9c6dc500625337da8ce7a5f692d73fa9"></a>
<a id="astructbt__hid__device__cb_html_aef0dda6b39282bc19f316ba364ae9420"></a>
<a id="astructbt__hid__device__cb_html_af8fa358139cf4bec7483234c90bdf655"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf_html"></a>

```c


/*
 * Copyright 2025 Xiaomi Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HID_DEVICE_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HID_DEVICE_H_


#include <stdbool.h>
#include <stdint.h>

#include <zephyr/bluetooth/classic/hid.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/net_buf.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_hid_device;

struct bt_hid_device_cb {
        void (*connected)(struct bt_hid_device *hid);

        void (*disconnected)(struct bt_hid_device *hid);

        int (*set_report)(struct bt_hid_device *hid, uint8_t type, struct net_buf *buf);

        int (*get_report)(struct bt_hid_device *hid, uint8_t type, bool size_present,
                          struct net_buf *req, struct net_buf *rsp);

        int (*set_protocol)(struct bt_hid_device *hid, uint8_t protocol);

        void (*output_report)(struct bt_hid_device *hid, struct net_buf *buf);

        void (*vc_unplug)(struct bt_hid_device *hid);

        void (*suspend)(struct bt_hid_device *hid, bool suspended);
};

int bt_hid_device_register(const struct bt_hid_device_cb *cb);

int bt_hid_device_unregister(void);

int bt_hid_device_connect(struct bt_conn *conn, struct bt_hid_device **hid);

int bt_hid_device_disconnect(struct bt_hid_device *hid);

struct net_buf *bt_hid_device_create_pdu(struct net_buf_pool *pool);

int bt_hid_device_input_report(struct bt_hid_device *hid, struct net_buf *buf);

int bt_hid_device_virtual_cable_unplug(struct bt_hid_device *hid);

struct bt_conn *bt_hid_device_get_conn(struct bt_hid_device *hid);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HID_DEVICE_H_ */
```

## 318.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：2025 Xiaomi Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 312 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HID_DEVICE_H_`。

## 318.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hid__device_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/classic/hid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2hid_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_hid_device_cb](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md)
- [connected](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a9c6dc500625337da8ce7a5f692d73fa9)
- [disconnected](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#aef0dda6b39282bc19f316ba364ae9420)
- [set_report](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a59768788c42e4369146767b95f9a22df)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [get_report](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a42c35e661602bb1c8f5687ce04b055ef)
- [set_protocol](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a21ca7e5d28b575007fb12dbfe779d83a)
- [output_report](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#af8fa358139cf4bec7483234c90bdf655)
- [vc_unplug](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a71ee8022e59c83e2b28318432355663d)
- [suspend](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a6221aa4f32aaa913536cb1ae70173a8e)
- [bt_hid_device_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga296d1b9695091507438261035d067c02)
- [bt_hid_device_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga35b0ec48658daa94010bef0c91503491)
- [bt_hid_device_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#gaf30d808e9903988d72d831c3c4aab617)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_hid_device_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#gae2000b4d39ed956cb37298bfcab351ed)
- [bt_hid_device_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#gad6bc5203aa9a2c8e4e217005f8f58b2e)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bt_hid_device_input_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga1034935eec4ff6a466990ee5f0c1ba2c)
- [bt_hid_device_virtual_cable_unplug](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#gab5b6b5f1047961ed5164f4e1059201ad)
- [bt_hid_device_get_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga63608252095d8c0638c6c43809e42553)
- [hid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2hid_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_hid_device_cb::set_protocol](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a21ca7e5d28b575007fb12dbfe779d83a)
- [bt_hid_device_cb::get_report](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a42c35e661602bb1c8f5687ce04b055ef)
- [bt_hid_device_cb::set_report](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a59768788c42e4369146767b95f9a22df)
- [bt_hid_device_cb::suspend](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a6221aa4f32aaa913536cb1ae70173a8e)
- [bt_hid_device_cb::vc_unplug](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a71ee8022e59c83e2b28318432355663d)
- [bt_hid_device_cb::connected](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#a9c6dc500625337da8ce7a5f692d73fa9)
- [bt_hid_device_cb::disconnected](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#aef0dda6b39282bc19f316ba364ae9420)
- [bt_hid_device_cb::output_report](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md#af8fa358139cf4bec7483234c90bdf655)

---

[上一章](P317_heartbeat.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P319_hid_host.h_源码浏览.md)
