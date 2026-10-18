---
id: learning.zephyr-docs.api-source-supplement-reference.page-81
title: goep.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/goep_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_goep.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h.html)。

## 81.1\_原始可见代码（Source Code）

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
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="foldopen00114"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="foldopen00183"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="foldopen00208"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00223"></a>
<a id="foldopen00225"></a>
<a id="l00225"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00337"></a>
<a id="l00343"></a>
<a id="foldopen00345"></a>
<a id="l00345"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00463"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__bt__goep__transport__l2cap_html_ga4730911b9e0ddb5c66575d0529128aee"></a>
<a id="agroup__bt__goep__transport__l2cap_html_ga48b039f1f5fa1a8c15449a061396c668"></a>
<a id="agroup__bt__goep__transport__l2cap_html_ga5f7a699eb8c857c6b6b99c506953f176"></a>
<a id="agroup__bt__goep__transport__rfcomm_html_ga22f4502e4eb56dab71ca478dee474e55"></a>
<a id="agroup__bt__goep__transport__rfcomm_html_ga781dc33ffa086753319c84f59b8e977f"></a>
<a id="agroup__bt__goep__transport__rfcomm_html_ga924d103e3556e274a4cb7ba16d0589c7"></a>
<a id="agroup__bt__goep_html_ga75294425d3da6d10ec5e591508be211c"></a>
<a id="agroup__bt__goep_html_ga7d751335e777b84a319626e50f43ffe9"></a>
<a id="agroup__bt__goep_html_gga75294425d3da6d10ec5e591508be211ca10d39d8b2b808a47998b05baeaf03cfe"></a>
<a id="agroup__bt__goep_html_gga75294425d3da6d10ec5e591508be211ca8f060690ba88c7e944d2f4a0e6a7db79"></a>
<a id="agroup__bt__goep_html_gga75294425d3da6d10ec5e591508be211cab221e071b255925006edba23221dd060"></a>
<a id="agroup__bt__goep_html_gga75294425d3da6d10ec5e591508be211cabe00a5c73a264c014b7e25983aed9a43"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="akernel_8h_html"></a>
<a id="al2cap_8h_html"></a>
<a id="aobex_8h_html"></a>
<a id="arfcomm_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astring_8h_html"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__goep__transport__l2cap__server_html"></a>
<a id="astructbt__goep__transport__l2cap__server_html_a514125628a8d90cb8c50982c2f2c133d"></a>
<a id="astructbt__goep__transport__l2cap__server_html_a7441985cb5ce8e2f961dcd5c5175f9c8"></a>
<a id="astructbt__goep__transport__l2cap__server_html_a8003824bb36da572b290fcb3a55b6c59"></a>
<a id="astructbt__goep__transport__ops_html"></a>
<a id="astructbt__goep__transport__ops_html_a46068be01ea341e1b74163bea0003e2e"></a>
<a id="astructbt__goep__transport__ops_html_a5f8ce2be1a4c87f4e36d47dcc3aa6f3c"></a>
<a id="astructbt__goep__transport__rfcomm__server_html"></a>
<a id="astructbt__goep__transport__rfcomm__server_html_a4d1df6a46e76d2f9e37a2d791d79bb84"></a>
<a id="astructbt__goep__transport__rfcomm__server_html_a66c433a47c20018f9f0a018b4fbc8048"></a>
<a id="astructbt__goep__transport__rfcomm__server_html_adaa1fb6c58cdb28560e3b4be272ae94d"></a>
<a id="astructbt__goep__transport__v1_html"></a>
<a id="astructbt__goep__transport__v1_html_a5e3a3cfd380d2001a156949177e1ca38"></a>
<a id="astructbt__goep__transport__v1_html_a82ed6f11432432f051c705bddfd7a53b"></a>
<a id="astructbt__goep__transport__v2_html"></a>
<a id="astructbt__goep__transport__v2_html_a5d3086e35bd244810e87d4bd0023e7bc"></a>
<a id="astructbt__goep__transport__v2_html_a8a273966650ed88693c9de1213f2088d"></a>
<a id="astructbt__goep__transport_html"></a>
<a id="astructbt__goep__transport_html_a607ceb28a77f1cb74cfa5188c9cc8ce4"></a>
<a id="astructbt__goep__transport_html_adcf88fd5c75b25f9b43fc6432f4ed41e"></a>
<a id="astructbt__goep_html"></a>
<a id="astructbt__goep_html_a6d341f018f6e7dc9187eab11cea9bc53"></a>
<a id="astructbt__goep_html_a8ff09a1652dca4c9d10c6bbef7c73c5f"></a>
<a id="astructbt__goep_html_a9820cd834fb77847110b0c0f490b637e"></a>
<a id="astructbt__goep_html_abca52709a4b2535eccecb632a1a6f29d"></a>
<a id="astructbt__l2cap__br__chan_html"></a>
<a id="astructbt__l2cap__server_html"></a>
<a id="astructbt__obex_html"></a>
<a id="astructbt__rfcomm__dlc_html"></a>
<a id="astructbt__rfcomm__server_html"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf_html"></a>

```c
/* goep.h - Bluetooth Generic Object Exchange Profile handling */

/*
 * Copyright 2024-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_GOEP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_GOEP_H_


#include <zephyr/kernel.h>
#include <string.h>
#include <errno.h>
#include <stdbool.h>

#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/l2cap.h>
#include <zephyr/bluetooth/classic/rfcomm.h>
#include <zephyr/bluetooth/classic/obex.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_goep;

struct bt_goep_transport_ops {
        void (*connected)(struct bt_conn *conn, struct bt_goep *goep);

        void (*disconnected)(struct bt_goep *goep);
};

struct bt_goep_transport_v1 {
        struct bt_rfcomm_dlc dlc;

        struct bt_goep *goep;
};

struct bt_goep_transport_v2 {
        struct bt_l2cap_br_chan chan;

        struct bt_goep *goep;
};

struct bt_goep_transport {
        struct bt_goep_transport_v1 v1;
        struct bt_goep_transport_v2 v2;
};

enum __packed bt_goep_transport_state {
        BT_GOEP_TRANSPORT_DISCONNECTED,
        BT_GOEP_TRANSPORT_CONNECTING,
        BT_GOEP_TRANSPORT_CONNECTED,
        BT_GOEP_TRANSPORT_DISCONNECTING,
};

struct bt_goep {
        struct bt_goep_transport_v1 *v1;

        struct bt_goep_transport_v2 *v2;

        struct bt_conn *_acl;

        atomic_t _state;

        const struct bt_goep_transport_ops *transport_ops;

        struct bt_obex obex;
};

#define BT_GOEP_INIT_V1(_goep, _v1) \
        do { \
                BUILD_ASSERT(SAME_TYPE(*(_goep), struct bt_goep) && \
                             SAME_TYPE(*(_v1), struct bt_goep_transport_v1), \
                             "pointer type mismatch in BT_GOEP_INIT_V1"); \
                (_v1)->goep = (_goep); \
                (_goep)->v1 = (_v1); \
                (_goep)->v2 = NULL; \
        } while (0)

#define BT_GOEP_INIT_V2(_goep, _v2) \
        do { \
                BUILD_ASSERT(SAME_TYPE(*(_goep), struct bt_goep) && \
                             SAME_TYPE(*(_v2), struct bt_goep_transport_v2), \
                             "pointer type mismatch in BT_GOEP_INIT_V2"); \
                (_v2)->goep = (_goep); \
                (_goep)->v2 = (_v2); \
                (_goep)->v1 = NULL; \
        } while (0)


struct bt_goep_transport_rfcomm_server {
        struct bt_rfcomm_server rfcomm;

        int (*accept)(struct bt_conn *conn, struct bt_goep_transport_rfcomm_server *server,
                      struct bt_goep **goep);

        sys_snode_t node;
};

int bt_goep_transport_rfcomm_server_register(struct bt_goep_transport_rfcomm_server *server);

int bt_goep_transport_rfcomm_connect(struct bt_conn *conn, struct bt_goep *goep, uint8_t channel);

int bt_goep_transport_rfcomm_disconnect(struct bt_goep *goep);



struct bt_goep_transport_l2cap_server {
        struct bt_l2cap_server l2cap;

        int (*accept)(struct bt_conn *conn, struct bt_goep_transport_l2cap_server *server,
                      struct bt_goep **goep);

        sys_snode_t node;
};

int bt_goep_transport_l2cap_server_register(struct bt_goep_transport_l2cap_server *server);

int bt_goep_transport_l2cap_connect(struct bt_conn *conn, struct bt_goep *goep, uint16_t psm);

int bt_goep_transport_l2cap_disconnect(struct bt_goep *goep);


struct net_buf *bt_goep_create_pdu(struct bt_goep *goep, struct net_buf_pool *pool);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_GOEP_H_ */
```

## 81.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`goep.h`：蓝牙通用对象交换配置文件（Generic Object Exchange Profile）的处理。

### 注释 2：原第 3 行

版权（Copyright）：2024-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 485 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_GOEP_H_`。

## 81.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)
- [zephyr/bluetooth/classic/rfcomm.h](https://docs.zephyrproject.org/latest/doxygen/html/rfcomm_8h.html)
- [zephyr/bluetooth/classic/obex.h](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h.html)
- [bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)
- [bt_goep_transport_ops](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md)
- [connected](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md#a46068be01ea341e1b74163bea0003e2e)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [disconnected](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md#a5f8ce2be1a4c87f4e36d47dcc3aa6f3c)
- [bt_goep_transport_v1](../bluetooth_service_model_reference/P075_bt_goep_transport_v1_结构体.md)
- [bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)
- [dlc](../bluetooth_service_model_reference/P075_bt_goep_transport_v1_结构体.md#a5e3a3cfd380d2001a156949177e1ca38)
- [goep](../bluetooth_service_model_reference/P075_bt_goep_transport_v1_结构体.md#a82ed6f11432432f051c705bddfd7a53b)
- [bt_goep_transport_v2](../bluetooth_service_model_reference/P076_bt_goep_transport_v2_结构体.md)
- [bt_l2cap_br_chan](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md)
- [chan](../bluetooth_service_model_reference/P076_bt_goep_transport_v2_结构体.md#a8a273966650ed88693c9de1213f2088d)
- [goep](../bluetooth_service_model_reference/P076_bt_goep_transport_v2_结构体.md#a5d3086e35bd244810e87d4bd0023e7bc)
- [bt_goep_transport](../bluetooth_service_model_reference/P071_bt_goep_transport_结构体.md)
- [v1](../bluetooth_service_model_reference/P071_bt_goep_transport_结构体.md#adcf88fd5c75b25f9b43fc6432f4ed41e)
- [v2](../bluetooth_service_model_reference/P071_bt_goep_transport_结构体.md#a607ceb28a77f1cb74cfa5188c9cc8ce4)
- [bt_goep_transport_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#ga75294425d3da6d10ec5e591508be211c)
- [BT_GOEP_TRANSPORT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gga75294425d3da6d10ec5e591508be211cab221e071b255925006edba23221dd060)
- [BT_GOEP_TRANSPORT_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gga75294425d3da6d10ec5e591508be211ca10d39d8b2b808a47998b05baeaf03cfe)
- [BT_GOEP_TRANSPORT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gga75294425d3da6d10ec5e591508be211cabe00a5c73a264c014b7e25983aed9a43)
- [BT_GOEP_TRANSPORT_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gga75294425d3da6d10ec5e591508be211ca8f060690ba88c7e944d2f4a0e6a7db79)
- [v1](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#a9820cd834fb77847110b0c0f490b637e)
- [v2](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#a6d341f018f6e7dc9187eab11cea9bc53)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [transport_ops](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#abca52709a4b2535eccecb632a1a6f29d)
- [bt_obex](../bluetooth_service_model_reference/P127_bt_obex_结构体.md)
- [obex](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#a8ff09a1652dca4c9d10c6bbef7c73c5f)
- [bt_goep_transport_rfcomm_server](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md)
- [bt_rfcomm_server](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md)
- [rfcomm](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md#adaa1fb6c58cdb28560e3b4be272ae94d)
- [accept](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md#a66c433a47c20018f9f0a018b4fbc8048)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md#a4d1df6a46e76d2f9e37a2d791d79bb84)
- [bt_goep_transport_rfcomm_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__rfcomm.html#ga781dc33ffa086753319c84f59b8e977f)
- [bt_goep_transport_rfcomm_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__rfcomm.html#ga924d103e3556e274a4cb7ba16d0589c7)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_goep_transport_rfcomm_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__rfcomm.html#ga22f4502e4eb56dab71ca478dee474e55)
- [bt_goep_transport_l2cap_server](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md)
- [bt_l2cap_server](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md)
- [l2cap](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md#a514125628a8d90cb8c50982c2f2c133d)
- [accept](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md#a7441985cb5ce8e2f961dcd5c5175f9c8)
- [node](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md#a8003824bb36da572b290fcb3a55b6c59)
- [bt_goep_transport_l2cap_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__l2cap.html#ga5f7a699eb8c857c6b6b99c506953f176)
- [bt_goep_transport_l2cap_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__l2cap.html#ga4730911b9e0ddb5c66575d0529128aee)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_goep_transport_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__l2cap.html#ga48b039f1f5fa1a8c15449a061396c668)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_goep_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#ga7d751335e777b84a319626e50f43ffe9)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)
- [obex.h](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h.html)
- [rfcomm.h](https://docs.zephyrproject.org/latest/doxygen/html/rfcomm_8h.html)
- [bt_goep_transport_l2cap_server::l2cap](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md#a514125628a8d90cb8c50982c2f2c133d)
- [bt_goep_transport_l2cap_server::accept](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md#a7441985cb5ce8e2f961dcd5c5175f9c8)
- [bt_goep_transport_l2cap_server::node](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md#a8003824bb36da572b290fcb3a55b6c59)
- [bt_goep_transport_ops::connected](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md#a46068be01ea341e1b74163bea0003e2e)
- [bt_goep_transport_ops::disconnected](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md#a5f8ce2be1a4c87f4e36d47dcc3aa6f3c)
- [bt_goep_transport_rfcomm_server::node](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md#a4d1df6a46e76d2f9e37a2d791d79bb84)
- [bt_goep_transport_rfcomm_server::accept](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md#a66c433a47c20018f9f0a018b4fbc8048)
- [bt_goep_transport_rfcomm_server::rfcomm](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md#adaa1fb6c58cdb28560e3b4be272ae94d)
- [bt_goep_transport_v1::dlc](../bluetooth_service_model_reference/P075_bt_goep_transport_v1_结构体.md#a5e3a3cfd380d2001a156949177e1ca38)
- [bt_goep_transport_v1::goep](../bluetooth_service_model_reference/P075_bt_goep_transport_v1_结构体.md#a82ed6f11432432f051c705bddfd7a53b)
- [bt_goep_transport_v2::goep](../bluetooth_service_model_reference/P076_bt_goep_transport_v2_结构体.md#a5d3086e35bd244810e87d4bd0023e7bc)
- [bt_goep_transport_v2::chan](../bluetooth_service_model_reference/P076_bt_goep_transport_v2_结构体.md#a8a273966650ed88693c9de1213f2088d)
- [bt_goep_transport::v2](../bluetooth_service_model_reference/P071_bt_goep_transport_结构体.md#a607ceb28a77f1cb74cfa5188c9cc8ce4)
- [bt_goep_transport::v1](../bluetooth_service_model_reference/P071_bt_goep_transport_结构体.md#adcf88fd5c75b25f9b43fc6432f4ed41e)
- [bt_goep::v2](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#a6d341f018f6e7dc9187eab11cea9bc53)
- [bt_goep::obex](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#a8ff09a1652dca4c9d10c6bbef7c73c5f)
- [bt_goep::v1](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#a9820cd834fb77847110b0c0f490b637e)
- [bt_goep::transport_ops](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#abca52709a4b2535eccecb632a1a6f29d)

---

[上一章](P080_gmap_lc3_preset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P082_gpio_rts5912.h_源码浏览.md)
