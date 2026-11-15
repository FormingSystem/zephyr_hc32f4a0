---
id: learning.zephyr-docs.api-source-reference.page-433
title: l2cap_br.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/l2cap__br_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第433章\_l2cap\_br.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/l2cap__br_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/l2cap__br_8h.html)。

## 433.1\_原始可见代码（Source Code）

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
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="aatomic_8h_html"></a>
<a id="abuf_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__conn_html_gaf0c56cd26c4147f6c9f0faa11fa01783"></a>
<a id="agroup__bt__l2cap__br_html_ga00ef7d0a42d8e544b195172af44b88b2"></a>
<a id="agroup__bt__l2cap__br_html_ga3478f19778e657a2d047f68f26b89966"></a>
<a id="agroup__bt__l2cap__br_html_ga3c6ad17ba18f5c00e39a379ed735de21"></a>
<a id="agroup__bt__l2cap__br_html_ga62c0115185f5026c1a842848dc5336ce"></a>
<a id="agroup__bt__l2cap__br_html_ga8ebf537cc7e4c0a68a320f9c65c94b05"></a>
<a id="agroup__bt__l2cap__br_html_gaa83e03f5ea5d62de096e1ebabb530697"></a>
<a id="agroup__bt__l2cap__br_html_gad1b4d59a8849124518bb973233b3f362"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ahci_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__l2cap__br__connless__cb_html"></a>
<a id="astructbt__l2cap__br__connless__cb_html_a2fd9c68c6689c7748f72925cae1ab343"></a>
<a id="astructbt__l2cap__br__connless__cb_html_a57be5b79d581d1acb5b5c59091fad5fa"></a>
<a id="astructbt__l2cap__br__connless__cb_html_ab4deccfa24dd5ea61ac390d0dec0cdbf"></a>
<a id="astructbt__l2cap__br__echo__cb_html"></a>
<a id="astructbt__l2cap__br__echo__cb_html_abc56aa16213b05fb9d330e4b0147066b"></a>
<a id="astructbt__l2cap__br__echo__cb_html_aee34c139bbfb03796aa162bf31687d6c"></a>
<a id="astructnet__buf_html"></a>
<a id="asys_2util_8h_html"></a>

```c


/*
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_L2CAP_BR_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_L2CAP_BR_H_


#include <stddef.h>
#include <stdint.h>

#include <zephyr/bluetooth/buf.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/hci.h>
#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util.h>
#include <sys/types.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_l2cap_br_echo_cb {
        void (*req)(struct bt_conn *conn, uint8_t identifier, struct net_buf *buf);

        void (*rsp)(struct bt_conn *conn, struct net_buf *buf);

        sys_snode_t _node;
};

int bt_l2cap_br_echo_cb_register(struct bt_l2cap_br_echo_cb *cb);

int bt_l2cap_br_echo_cb_unregister(struct bt_l2cap_br_echo_cb *cb);

#define BT_L2CAP_BR_ECHO_REQ_RESERVE BT_L2CAP_BUF_SIZE(4)

#define BT_L2CAP_BR_ECHO_RSP_RESERVE BT_L2CAP_BUF_SIZE(4)

int bt_l2cap_br_echo_req(struct bt_conn *conn, struct net_buf *buf);

int bt_l2cap_br_echo_rsp(struct bt_conn *conn, uint8_t identifier, struct net_buf *buf);

struct bt_l2cap_br_connless_cb {
        uint16_t psm;

        bt_security_t sec_level;

        void (*recv)(struct bt_conn *conn, uint16_t psm, struct net_buf *buf);

        sys_snode_t _node;
};

int bt_l2cap_br_connless_register(struct bt_l2cap_br_connless_cb *cb);

int bt_l2cap_br_connless_unregister(struct bt_l2cap_br_connless_cb *cb);

#define BT_L2CAP_CONNLESS_SDU_HDR_SIZE 2

#define BT_L2CAP_CONNLESS_RESERVE BT_L2CAP_BUF_SIZE(BT_L2CAP_CONNLESS_SDU_HDR_SIZE)

int bt_l2cap_br_connless_send(struct bt_conn *conn, uint16_t psm, struct net_buf *buf);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_L2CAP_BR_H_ */
```

## 433.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 259 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_L2CAP_BR_H_`。

## 433.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/l2cap__br_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/buf.h](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [bt_l2cap_br_echo_cb](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md)
- [req](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md#abc56aa16213b05fb9d330e4b0147066b)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [rsp](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md#aee34c139bbfb03796aa162bf31687d6c)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_l2cap_br_echo_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga62c0115185f5026c1a842848dc5336ce)
- [bt_l2cap_br_echo_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga00ef7d0a42d8e544b195172af44b88b2)
- [bt_l2cap_br_echo_req](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga3c6ad17ba18f5c00e39a379ed735de21)
- [bt_l2cap_br_echo_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga8ebf537cc7e4c0a68a320f9c65c94b05)
- [bt_l2cap_br_connless_cb](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [psm](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md#a57be5b79d581d1acb5b5c59091fad5fa)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [sec_level](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md#ab4deccfa24dd5ea61ac390d0dec0cdbf)
- [recv](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md#a2fd9c68c6689c7748f72925cae1ab343)
- [bt_l2cap_br_connless_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gad1b4d59a8849124518bb973233b3f362)
- [bt_l2cap_br_connless_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gaa83e03f5ea5d62de096e1ebabb530697)
- [bt_l2cap_br_connless_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga3478f19778e657a2d047f68f26b89966)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [buf.h](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_l2cap_br_connless_cb::recv](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md#a2fd9c68c6689c7748f72925cae1ab343)
- [bt_l2cap_br_connless_cb::psm](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md#a57be5b79d581d1acb5b5c59091fad5fa)
- [bt_l2cap_br_connless_cb::sec_level](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md#ab4deccfa24dd5ea61ac390d0dec0cdbf)
- [bt_l2cap_br_echo_cb::req](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md#abc56aa16213b05fb9d330e4b0147066b)
- [bt_l2cap_br_echo_cb::rsp](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md#aee34c139bbfb03796aa162bf31687d6c)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P432_kinetis_mcg.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P434_label.h_源码浏览.md)
