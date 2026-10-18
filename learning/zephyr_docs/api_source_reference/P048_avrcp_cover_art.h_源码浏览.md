---
id: learning.zephyr-docs.api-source-reference.page-48
title: avrcp_cover_art.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/avrcp__cover__art_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_avrcp\_cover\_art.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/avrcp__cover__art_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/avrcp__cover__art_8h.html)。

## 48.1\_原始可见代码（Source Code）

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
<a id="l00036"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="aavrcp_8h_html"></a>
<a id="abip_8h_html"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="agroup__bt__avrcp__cover__art_html_ga0b724c5eff89386663781a2d55048b60"></a>
<a id="agroup__bt__avrcp__cover__art_html_ga12c27e417b4c16ed6f9c31f018bdce65"></a>
<a id="agroup__bt__avrcp__cover__art_html_ga2fa73ceca47131564f2c16d00e88eda1"></a>
<a id="agroup__bt__avrcp__cover__art_html_ga301c1475df0c136220548d9979e4eec1"></a>
<a id="agroup__bt__avrcp__cover__art_html_ga47c4b70799634de73e7adb812dc439fd"></a>
<a id="agroup__bt__avrcp__cover__art_html_ga4ee3725ebf771ca6afa93ec0ab9b0096"></a>
<a id="agroup__bt__avrcp__cover__art_html_ga5fedcfbbe99925fa8b61272ba40ebe05"></a>
<a id="agroup__bt__avrcp__cover__art_html_ga6456a9ceae773b3490a3a065674e7770"></a>
<a id="agroup__bt__avrcp__cover__art_html_ga8e035c3c1d6fce40aac194ca556307d7"></a>
<a id="agroup__bt__avrcp__cover__art_html_ga9a87234df456d8005ac1b160242f8be6"></a>
<a id="agroup__bt__avrcp__cover__art_html_gab10e1b0b9ba4ebe2a41372b5e4cedbc0"></a>
<a id="agroup__bt__avrcp__cover__art_html_gabcce60bdcce46b8e1b7de69152b93273"></a>
<a id="agroup__bt__avrcp__cover__art_html_gac9982c9227d5ced224aa3f13065128d2"></a>
<a id="agroup__bt__avrcp__cover__art_html_gacb58f20f3b7aa8993d9fae851bad8b15"></a>
<a id="agroup__bt__avrcp__cover__art_html_gad7a0efe86750b95e94e7f18ab8720bcb"></a>
<a id="agroup__bt__avrcp__cover__art_html_gad7a25376e1d6c6910dee15b758b3970d"></a>
<a id="agroup__bt__avrcp__cover__art_html_gadeeb8f39a8a8f6e44eb51f6487309e97"></a>
<a id="agroup__bt__avrcp__cover__art_html_gae822bb08fca3ae8e8c7e1d946490922e"></a>
<a id="agroup__bt__avrcp__cover__art_html_gaf60f588b44b2f94f5af562c2f0408fa2"></a>
<a id="al2cap_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__avrcp__cover__art__ct__cb_html"></a>
<a id="astructbt__avrcp__cover__art__ct__cb_html_a4cd7e7b24297bf1b65756b628470be7f"></a>
<a id="astructbt__avrcp__cover__art__ct__cb_html_a5ff5e206b4ace7e9a1c95a7f77a82591"></a>
<a id="astructbt__avrcp__cover__art__ct__cb_html_a763a5bae17a8273b2c472315cdbed153"></a>
<a id="astructbt__avrcp__cover__art__ct__cb_html_a856c77a333c623e42203c62bafd0cb01"></a>
<a id="astructbt__avrcp__cover__art__ct__cb_html_a875ccc914eefb93e0e30228fb7ca6f9a"></a>
<a id="astructbt__avrcp__cover__art__ct__cb_html_a9e3c5f78b0b187ac7a4d14a7af7f8b9d"></a>
<a id="astructbt__avrcp__cover__art__ct__cb_html_ac6230b6880b55db094f486d246b0ea8f"></a>
<a id="astructbt__avrcp__cover__art__ct__cb_html_ae931386c504da5182f7d58a785058296"></a>
<a id="astructbt__avrcp__cover__art__ct_html"></a>
<a id="astructbt__avrcp__cover__art__ct_html_a128f10710dfb12aa80a6d95354b532da"></a>
<a id="astructbt__avrcp__cover__art__ct_html_a4634dc499f02165e48c59c2bb87b0b81"></a>
<a id="astructbt__avrcp__cover__art__ct_html_a69843b53b4398f82fae0e05c087680a1"></a>
<a id="astructbt__avrcp__cover__art__ct_html_af44481b36c5b0ff98519e01ad0c4f61f"></a>
<a id="astructbt__avrcp__cover__art__tg__cb_html"></a>
<a id="astructbt__avrcp__cover__art__tg__cb_html_a07845b015a7c47b4236d9320f71026cc"></a>
<a id="astructbt__avrcp__cover__art__tg__cb_html_a33cf7ee28952df116b8410bd1b7c737d"></a>
<a id="astructbt__avrcp__cover__art__tg__cb_html_a49ab3dbbfae6ae0ee86ac9646357cd4b"></a>
<a id="astructbt__avrcp__cover__art__tg__cb_html_a5debda6bf20c68cb713527777d09e89c"></a>
<a id="astructbt__avrcp__cover__art__tg__cb_html_a8d9c712c2cfc8ff106f57b406558b2e8"></a>
<a id="astructbt__avrcp__cover__art__tg__cb_html_aad5cd595a1616b2ae2370c328d83cb2e"></a>
<a id="astructbt__avrcp__cover__art__tg__cb_html_ae4f3a363e0808807753dcb878916cd8b"></a>
<a id="astructbt__avrcp__cover__art__tg__cb_html_afe707ed6123c7cb78f94c6669bdfdcd4"></a>
<a id="astructbt__avrcp__cover__art__tg_html"></a>
<a id="astructbt__avrcp__cover__art__tg_html_a08644473b1f4c425e7dfb5e8dc64bc0a"></a>
<a id="astructbt__avrcp__cover__art__tg_html_a41e8025b600c057b1fe47c5e74f0a658"></a>
<a id="astructbt__avrcp__cover__art__tg_html_acdd5b50f1f5f8f21738e5723441b4b8c"></a>
<a id="astructbt__avrcp__cover__art__tg_html_aedc07dd496bebcfef110c1e2c2bacb93"></a>
<a id="astructbt__avrcp__ct_html"></a>
<a id="astructbt__avrcp__tg_html"></a>
<a id="astructbt__bip__client_html"></a>
<a id="astructbt__bip__server_html"></a>
<a id="astructbt__bip_html"></a>
<a id="astructbt__conn_html"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf_html"></a>

```c


/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_AVRCP_COVER_ART_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_AVRCP_COVER_ART_H_


#include <stdint.h>

#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/l2cap.h>
#include <zephyr/bluetooth/classic/avrcp.h>
#include <zephyr/bluetooth/classic/bip.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_avrcp_ct;
struct bt_avrcp_tg;

struct bt_avrcp_cover_art_ct {
        struct bt_bip bip;
        struct bt_bip_client client;
        struct bt_avrcp_ct *ct;
        struct bt_conn *conn;
};

struct bt_avrcp_cover_art_tg {
        struct bt_bip bip;
        struct bt_bip_server server;
        struct bt_avrcp_tg *tg;
        struct bt_conn *conn;
};

struct bt_avrcp_cover_art_ct_cb {
        void (*l2cap_connected)(struct bt_avrcp_ct *ct, struct bt_avrcp_cover_art_ct *cover_art_ct);

        void (*l2cap_disconnected)(struct bt_avrcp_cover_art_ct *ct);

        void (*connect)(struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, uint8_t version,
                        uint16_t mopl, struct net_buf *buf);

        void (*disconnect)(struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf);

        void (*abort)(struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf);

        void (*get_image_properties)(struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code,
                                     struct net_buf *buf);

        void (*get_image)(struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf);

        void (*get_linked_thumbnail)(struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code,
                                     struct net_buf *buf);
};

struct bt_avrcp_cover_art_tg_cb {
        void (*l2cap_connected)(struct bt_avrcp_tg *tg, struct bt_avrcp_cover_art_tg *cover_art_tg);

        void (*l2cap_disconnected)(struct bt_avrcp_cover_art_tg *tg);

        void (*connect)(struct bt_avrcp_cover_art_tg *tg, uint8_t version, uint16_t mopl,
                        struct net_buf *buf);

        void (*disconnect)(struct bt_avrcp_cover_art_tg *tg, struct net_buf *buf);

        void (*abort)(struct bt_avrcp_cover_art_tg *tg, struct net_buf *buf);

        void (*get_image_properties)(struct bt_avrcp_cover_art_tg *tg, bool final,
                                     struct net_buf *buf);

        void (*get_image)(struct bt_avrcp_cover_art_tg *tg, bool final, struct net_buf *buf);

        void (*get_linked_thumbnail)(struct bt_avrcp_cover_art_tg *tg, bool final,
                                     struct net_buf *buf);
};

int bt_avrcp_cover_art_ct_cb_register(struct bt_avrcp_cover_art_ct_cb *cb);

int bt_avrcp_cover_art_tg_cb_register(struct bt_avrcp_cover_art_tg_cb *cb);

int bt_avrcp_cover_art_ct_l2cap_connect(struct bt_avrcp_ct *ct,
                                        struct bt_avrcp_cover_art_ct **cover_art_ct, uint16_t psm);

int bt_avrcp_cover_art_ct_l2cap_disconnect(struct bt_avrcp_cover_art_ct *ct);

int bt_avrcp_cover_art_tg_l2cap_disconnect(struct bt_avrcp_cover_art_tg *tg);

struct net_buf *bt_avrcp_cover_art_ct_create_pdu(struct bt_avrcp_cover_art_ct *ct,
                                                 struct net_buf_pool *pool);

struct net_buf *bt_avrcp_cover_art_tg_create_pdu(struct bt_avrcp_cover_art_tg *tg,
                                                 struct net_buf_pool *pool);

int bt_avrcp_cover_art_ct_connect(struct bt_avrcp_cover_art_ct *ct);

int bt_avrcp_cover_art_tg_connect(struct bt_avrcp_cover_art_tg *tg, uint8_t rsp_code);

int bt_avrcp_cover_art_ct_disconnect(struct bt_avrcp_cover_art_ct *ct);

int bt_avrcp_cover_art_tg_disconnect(struct bt_avrcp_cover_art_tg *tg, uint8_t rsp_code);

int bt_avrcp_cover_art_ct_abort(struct bt_avrcp_cover_art_ct *ct, struct net_buf *buf);

int bt_avrcp_cover_art_tg_abort(struct bt_avrcp_cover_art_tg *tg, uint8_t rsp_code,
                                struct net_buf *buf);

int bt_avrcp_cover_art_ct_get_image_properties(struct bt_avrcp_cover_art_ct *ct, bool final,
                                               struct net_buf *buf);

int bt_avrcp_cover_art_tg_get_image_properties(struct bt_avrcp_cover_art_tg *tg, uint8_t rsp_code,
                                               struct net_buf *buf);

int bt_avrcp_cover_art_ct_get_image(struct bt_avrcp_cover_art_ct *ct, bool final,
                                    struct net_buf *buf);

int bt_avrcp_cover_art_tg_get_image(struct bt_avrcp_cover_art_tg *tg, uint8_t rsp_code,
                                    struct net_buf *buf);

int bt_avrcp_cover_art_ct_get_linked_thumbnail(struct bt_avrcp_cover_art_ct *ct, bool final,
                                               struct net_buf *buf);

int bt_avrcp_cover_art_tg_get_linked_thumbnail(struct bt_avrcp_cover_art_tg *tg, uint8_t rsp_code,
                                               struct net_buf *buf);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_AVRCP_COVER_ART_H_ */
```

## 48.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 439 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_AVRCP_COVER_ART_H_`。

## 48.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/avrcp__cover__art_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)
- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h.html)
- [zephyr/bluetooth/classic/bip.h](https://docs.zephyrproject.org/latest/doxygen/html/bip_8h.html)
- [bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)
- [bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)
- [bt_avrcp_cover_art_ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md)
- [bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)
- [bip](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md#a69843b53b4398f82fae0e05c087680a1)
- [bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)
- [client](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md#af44481b36c5b0ff98519e01ad0c4f61f)
- [ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md#a128f10710dfb12aa80a6d95354b532da)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [conn](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md#a4634dc499f02165e48c59c2bb87b0b81)
- [bt_avrcp_cover_art_tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md)
- [bip](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md#acdd5b50f1f5f8f21738e5723441b4b8c)
- [bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)
- [server](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md#a08644473b1f4c425e7dfb5e8dc64bc0a)
- [tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md#aedc07dd496bebcfef110c1e2c2bacb93)
- [conn](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md#a41e8025b600c057b1fe47c5e74f0a658)
- [bt_avrcp_cover_art_ct_cb](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md)
- [l2cap_connected](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#a9e3c5f78b0b187ac7a4d14a7af7f8b9d)
- [l2cap_disconnected](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#a4cd7e7b24297bf1b65756b628470be7f)
- [connect](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#a856c77a333c623e42203c62bafd0cb01)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [disconnect](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#ae931386c504da5182f7d58a785058296)
- [abort](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#a763a5bae17a8273b2c472315cdbed153)
- [get_image_properties](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#a875ccc914eefb93e0e30228fb7ca6f9a)
- [get_image](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#ac6230b6880b55db094f486d246b0ea8f)
- [get_linked_thumbnail](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#a5ff5e206b4ace7e9a1c95a7f77a82591)
- [bt_avrcp_cover_art_tg_cb](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md)
- [l2cap_connected](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#a49ab3dbbfae6ae0ee86ac9646357cd4b)
- [l2cap_disconnected](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#ae4f3a363e0808807753dcb878916cd8b)
- [connect](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#a33cf7ee28952df116b8410bd1b7c737d)
- [disconnect](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#a5debda6bf20c68cb713527777d09e89c)
- [abort](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#aad5cd595a1616b2ae2370c328d83cb2e)
- [get_image_properties](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#a07845b015a7c47b4236d9320f71026cc)
- [get_image](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#afe707ed6123c7cb78f94c6669bdfdcd4)
- [get_linked_thumbnail](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#a8d9c712c2cfc8ff106f57b406558b2e8)
- [bt_avrcp_cover_art_ct_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#ga6456a9ceae773b3490a3a065674e7770)
- [bt_avrcp_cover_art_tg_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#ga12c27e417b4c16ed6f9c31f018bdce65)
- [bt_avrcp_cover_art_ct_l2cap_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#ga0b724c5eff89386663781a2d55048b60)
- [bt_avrcp_cover_art_ct_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#ga9a87234df456d8005ac1b160242f8be6)
- [bt_avrcp_cover_art_tg_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#ga2fa73ceca47131564f2c16d00e88eda1)
- [bt_avrcp_cover_art_ct_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#ga8e035c3c1d6fce40aac194ca556307d7)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bt_avrcp_cover_art_tg_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#gadeeb8f39a8a8f6e44eb51f6487309e97)
- [bt_avrcp_cover_art_ct_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#gabcce60bdcce46b8e1b7de69152b93273)
- [bt_avrcp_cover_art_tg_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#gae822bb08fca3ae8e8c7e1d946490922e)
- [bt_avrcp_cover_art_ct_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#gad7a0efe86750b95e94e7f18ab8720bcb)
- [bt_avrcp_cover_art_tg_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#ga5fedcfbbe99925fa8b61272ba40ebe05)
- [bt_avrcp_cover_art_ct_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#gac9982c9227d5ced224aa3f13065128d2)
- [bt_avrcp_cover_art_tg_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#ga301c1475df0c136220548d9979e4eec1)
- [bt_avrcp_cover_art_ct_get_image_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#ga4ee3725ebf771ca6afa93ec0ab9b0096)
- [bt_avrcp_cover_art_tg_get_image_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#gab10e1b0b9ba4ebe2a41372b5e4cedbc0)
- [bt_avrcp_cover_art_ct_get_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#gaf60f588b44b2f94f5af562c2f0408fa2)
- [bt_avrcp_cover_art_tg_get_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#gacb58f20f3b7aa8993d9fae851bad8b15)
- [bt_avrcp_cover_art_ct_get_linked_thumbnail](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#ga47c4b70799634de73e7adb812dc439fd)
- [bt_avrcp_cover_art_tg_get_linked_thumbnail](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html#gad7a25376e1d6c6910dee15b758b3970d)
- [avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h.html)
- [bip.h](https://docs.zephyrproject.org/latest/doxygen/html/bip_8h.html)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)
- [bt_avrcp_cover_art_ct_cb::l2cap_disconnected](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#a4cd7e7b24297bf1b65756b628470be7f)
- [bt_avrcp_cover_art_ct_cb::get_linked_thumbnail](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#a5ff5e206b4ace7e9a1c95a7f77a82591)
- [bt_avrcp_cover_art_ct_cb::abort](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#a763a5bae17a8273b2c472315cdbed153)
- [bt_avrcp_cover_art_ct_cb::connect](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#a856c77a333c623e42203c62bafd0cb01)
- [bt_avrcp_cover_art_ct_cb::get_image_properties](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#a875ccc914eefb93e0e30228fb7ca6f9a)
- [bt_avrcp_cover_art_ct_cb::l2cap_connected](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#a9e3c5f78b0b187ac7a4d14a7af7f8b9d)
- [bt_avrcp_cover_art_ct_cb::get_image](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#ac6230b6880b55db094f486d246b0ea8f)
- [bt_avrcp_cover_art_ct_cb::disconnect](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md#ae931386c504da5182f7d58a785058296)
- [bt_avrcp_cover_art_ct::ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md#a128f10710dfb12aa80a6d95354b532da)
- [bt_avrcp_cover_art_ct::conn](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md#a4634dc499f02165e48c59c2bb87b0b81)
- [bt_avrcp_cover_art_ct::bip](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md#a69843b53b4398f82fae0e05c087680a1)
- [bt_avrcp_cover_art_ct::client](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md#af44481b36c5b0ff98519e01ad0c4f61f)
- [bt_avrcp_cover_art_tg_cb::get_image_properties](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#a07845b015a7c47b4236d9320f71026cc)
- [bt_avrcp_cover_art_tg_cb::connect](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#a33cf7ee28952df116b8410bd1b7c737d)
- [bt_avrcp_cover_art_tg_cb::l2cap_connected](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#a49ab3dbbfae6ae0ee86ac9646357cd4b)
- [bt_avrcp_cover_art_tg_cb::disconnect](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#a5debda6bf20c68cb713527777d09e89c)
- [bt_avrcp_cover_art_tg_cb::get_linked_thumbnail](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#a8d9c712c2cfc8ff106f57b406558b2e8)
- [bt_avrcp_cover_art_tg_cb::abort](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#aad5cd595a1616b2ae2370c328d83cb2e)
- [bt_avrcp_cover_art_tg_cb::l2cap_disconnected](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#ae4f3a363e0808807753dcb878916cd8b)
- [bt_avrcp_cover_art_tg_cb::get_image](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md#afe707ed6123c7cb78f94c6669bdfdcd4)
- [bt_avrcp_cover_art_tg::server](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md#a08644473b1f4c425e7dfb5e8dc64bc0a)
- [bt_avrcp_cover_art_tg::conn](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md#a41e8025b600c057b1fe47c5e74f0a658)
- [bt_avrcp_cover_art_tg::bip](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md#acdd5b50f1f5f8f21738e5723441b4b8c)
- [bt_avrcp_cover_art_tg::tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md#aedc07dd496bebcfef110c1e2c2bacb93)

---

[上一章](P047_auxdisplay.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P049_aw9523b.h_源码浏览.md)
