---
id: learning.zephyr-docs.api-source-reference.page-902
title: vcp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/vcp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第902章\_vcp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/vcp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/vcp_8h.html)。

## 902.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00118"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00413"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="aaics_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__vcp_html_ga03e073e29920f4a530d2f8851b4b8df4"></a>
<a id="agroup__bt__vcp_html_ga0c6d0b6b015f069a9adc1332a32c79f9"></a>
<a id="agroup__bt__vcp_html_ga0c8faa95cc36950c70ff572c931eedee"></a>
<a id="agroup__bt__vcp_html_ga106b7f826adec665b4f0ac3d5e82b867"></a>
<a id="agroup__bt__vcp_html_ga1761d6618c48983e034cee5574c9c34f"></a>
<a id="agroup__bt__vcp_html_ga1e6c9cfa0d012a4b701c99d8e6b5985d"></a>
<a id="agroup__bt__vcp_html_ga20348b220988c700cabf356f7165d4d6"></a>
<a id="agroup__bt__vcp_html_ga2defdeee7486eee22a3416db8aa7c251"></a>
<a id="agroup__bt__vcp_html_ga303d4b6b77987ab41cb1753ef861dd6c"></a>
<a id="agroup__bt__vcp_html_ga3e6236a8679f95ba512181284a05923d"></a>
<a id="agroup__bt__vcp_html_ga4e95c3fb071cb94fbe75f88e96d34b36"></a>
<a id="agroup__bt__vcp_html_ga56e0f99d2688fb6f9e0e4d9103de706c"></a>
<a id="agroup__bt__vcp_html_ga571d7ff5a6a507fcd7cbdfa32a04643b"></a>
<a id="agroup__bt__vcp_html_ga61279baeba11152625cd3a87c5d973c9"></a>
<a id="agroup__bt__vcp_html_ga68cab2f59c63542b6a7da33d555da0ab"></a>
<a id="agroup__bt__vcp_html_ga6c10dd5a029b524994739f0b37a82c84"></a>
<a id="agroup__bt__vcp_html_ga752d8ff54a4b8c8c854a9c693617e64d"></a>
<a id="agroup__bt__vcp_html_ga7861d0c3426870c015106e8e170004a3"></a>
<a id="agroup__bt__vcp_html_ga908eb20727e1d68ed569badfd13ff896"></a>
<a id="agroup__bt__vcp_html_ga9d1ac028abc88549ea18b6a0c585c781"></a>
<a id="agroup__bt__vcp_html_gaaa5b5cd9a11c0e1fcdabce690ba20616"></a>
<a id="agroup__bt__vcp_html_gaaa748c49e103ff161f67df9663ea6330"></a>
<a id="agroup__bt__vcp_html_gab287197243191e3dbf162c6d16b6d726"></a>
<a id="agroup__bt__vcp_html_gac18d43a0785155c1131249f95554f2de"></a>
<a id="agroup__bt__vcp_html_gadf77729fee34f6605101c278fd2b7c46"></a>
<a id="agroup__bt__vcp_html_gae69e4730df4341bbb9bbbba1bea14005"></a>
<a id="agroup__bt__vcp_html_gae7195f4556ad2442bc45d8d43cdeedd0"></a>
<a id="agroup__bt__vcp_html_gaefc226a5abb6bb1540d4b44ac4ddc236"></a>
<a id="agroup__bt__vcp_html_gaf3c622f151a21d1dd617e97917c5ff5e"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__aics__cb_html"></a>
<a id="astructbt__aics__register__param_html"></a>
<a id="astructbt__aics_html"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__vcp__included_html"></a>
<a id="astructbt__vcp__included_html_a1f04068dd88d2fecef5fd78a3c7d4429"></a>
<a id="astructbt__vcp__included_html_aa6c87b8c9b4b2be6ec6429fd2ee68398"></a>
<a id="astructbt__vcp__included_html_acb0c8e853808adfd9c3b92b45e874103"></a>
<a id="astructbt__vcp__included_html_af521bb12ebef4c5f60609040140474c0"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html_a430b1ee27c9bf7d6c7f8498748d91b21"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html_a4df90987abe0e53894e4064b3487c2bb"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html_a6a217e0d8cbcc56e5128d5b7acdaac6d"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html_a770e300127b8357f1e76f0cca21b74e5"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html_aa2cd77992831eef7e59d3e4a01a0e542"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html_abe7cf51858428db6b953a21a6ba40f83"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html_ac3b89f35b79d35384f9ead31cf15ac4e"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html_ac986e0c5cb49395fe8581f5b1dae1a88"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html_ada8fe8d838d6d2c983d746e7e7ed1171"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html_ae1beaa5d0a61c630fa90b4a5236ce743"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html_af4ca636d19c83694f9b86102404b0538"></a>
<a id="astructbt__vcp__vol__ctlr__cb_html_af6407bb0652539608f0100f02cfaadd1"></a>
<a id="astructbt__vcp__vol__ctlr_html"></a>
<a id="astructbt__vcp__vol__rend__cb_html"></a>
<a id="astructbt__vcp__vol__rend__cb_html_a05f84d8a2deedbc426ef22b89c87bd40"></a>
<a id="astructbt__vcp__vol__rend__cb_html_a3413d33fa8c3362ded6ec81533c27c86"></a>
<a id="astructbt__vcp__vol__rend__register__param_html"></a>
<a id="astructbt__vcp__vol__rend__register__param_html_a098e6c6921813b3f0dc7512cd483c829"></a>
<a id="astructbt__vcp__vol__rend__register__param_html_a69257b668dc52429c64daa7af5161805"></a>
<a id="astructbt__vcp__vol__rend__register__param_html_a6b5096f174425659c7fbc71df0da8e67"></a>
<a id="astructbt__vcp__vol__rend__register__param_html_a6cf1343a2b3033c3f4676d66017cfda7"></a>
<a id="astructbt__vcp__vol__rend__register__param_html_a93f2b246ac4241db468a46a64909866e"></a>
<a id="astructbt__vcp__vol__rend__register__param_html_af9a09c453394fd4a28d6415e2775c3f5"></a>
<a id="astructbt__vocs__cb_html"></a>
<a id="astructbt__vocs__register__param_html"></a>
<a id="astructbt__vocs_html"></a>
<a id="avocs_8h_html"></a>

```c


/*
 * Copyright (c) 2020-2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_VCP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_VCP_H_


#include <stdint.h>

#include <zephyr/bluetooth/audio/aics.h>
#include <zephyr/bluetooth/audio/vocs.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_BT_VCP_VOL_REND)
#define BT_VCP_VOL_REND_VOCS_CNT CONFIG_BT_VCP_VOL_REND_VOCS_INSTANCE_COUNT
#else
#define BT_VCP_VOL_REND_VOCS_CNT 0U
#endif /* CONFIG_BT_VCP_VOL_REND */

#if defined(CONFIG_BT_VCP_VOL_REND)
#define BT_VCP_VOL_REND_AICS_CNT CONFIG_BT_VCP_VOL_REND_AICS_INSTANCE_COUNT
#else
#define BT_VCP_VOL_REND_AICS_CNT 0U
#endif /* CONFIG_BT_VCP_VOL_REND */

#define BT_VCP_ERR_INVALID_COUNTER             0x80U
#define BT_VCP_ERR_OP_NOT_SUPPORTED            0x81U

#define BT_VCP_STATE_UNMUTED                   0x00U
#define BT_VCP_STATE_MUTED                     0x01U

struct bt_vcp_vol_ctlr;

struct bt_vcp_vol_rend_register_param {
        uint8_t step;

        uint8_t mute;

        uint8_t volume;

        struct bt_vocs_register_param vocs_param[BT_VCP_VOL_REND_VOCS_CNT];

        struct bt_aics_register_param aics_param[BT_VCP_VOL_REND_AICS_CNT];

        struct bt_vcp_vol_rend_cb *cb;
};

struct bt_vcp_included {
        uint8_t vocs_cnt;
        struct bt_vocs **vocs;

        uint8_t aics_cnt;
        struct bt_aics **aics;
};

int bt_vcp_vol_rend_included_get(struct bt_vcp_included *included);

int bt_vcp_vol_rend_register(struct bt_vcp_vol_rend_register_param *param);

struct bt_vcp_vol_rend_cb {
        void (*state)(struct bt_conn *conn, int err, uint8_t volume, uint8_t mute);

        void (*flags)(struct bt_conn *conn, int err, uint8_t flags);
};

int bt_vcp_vol_rend_set_step(uint8_t volume_step);

int bt_vcp_vol_rend_get_state(void);

int bt_vcp_vol_rend_get_flags(void);

int bt_vcp_vol_rend_vol_down(void);

int bt_vcp_vol_rend_vol_up(void);

int bt_vcp_vol_rend_unmute_vol_down(void);

int bt_vcp_vol_rend_unmute_vol_up(void);

int bt_vcp_vol_rend_set_vol(uint8_t volume);

int bt_vcp_vol_rend_unmute(void);

int bt_vcp_vol_rend_mute(void);

struct bt_vcp_vol_ctlr_cb {
        void (*state)(struct bt_vcp_vol_ctlr *vol_ctlr, int err, uint8_t volume,
                      uint8_t mute);


        void (*flags)(struct bt_vcp_vol_ctlr *vol_ctlr, int err, uint8_t flags);

        void (*discover)(struct bt_vcp_vol_ctlr *vol_ctlr, int err, uint8_t vocs_count,
                         uint8_t aics_count);

        void (*vol_down)(struct bt_vcp_vol_ctlr *vol_ctlr, int err);

        void (*vol_up)(struct bt_vcp_vol_ctlr *vol_ctlr, int err);

        void (*mute)(struct bt_vcp_vol_ctlr *vol_ctlr, int err);

        void (*unmute)(struct bt_vcp_vol_ctlr *vol_ctlr, int err);

        void (*vol_down_unmute)(struct bt_vcp_vol_ctlr *vol_ctlr, int err);

        void (*vol_up_unmute)(struct bt_vcp_vol_ctlr *vol_ctlr, int err);

        void (*vol_set)(struct bt_vcp_vol_ctlr *vol_ctlr, int err);

        struct bt_vocs_cb             vocs_cb;

        struct bt_aics_cb             aics_cb;

        sys_snode_t _node;
};

int bt_vcp_vol_ctlr_cb_register(struct bt_vcp_vol_ctlr_cb *cb);

int bt_vcp_vol_ctlr_cb_unregister(struct bt_vcp_vol_ctlr_cb *cb);

int bt_vcp_vol_ctlr_discover(struct bt_conn *conn,
                             struct bt_vcp_vol_ctlr **vol_ctlr);

struct bt_vcp_vol_ctlr *bt_vcp_vol_ctlr_get_by_conn(const struct bt_conn *conn);

int bt_vcp_vol_ctlr_conn_get(const struct bt_vcp_vol_ctlr *vol_ctlr,
                             struct bt_conn **conn);

int bt_vcp_vol_ctlr_included_get(struct bt_vcp_vol_ctlr *vol_ctlr,
                                 struct bt_vcp_included *included);

int bt_vcp_vol_ctlr_read_state(struct bt_vcp_vol_ctlr *vol_ctlr);

int bt_vcp_vol_ctlr_read_flags(struct bt_vcp_vol_ctlr *vol_ctlr);

int bt_vcp_vol_ctlr_vol_down(struct bt_vcp_vol_ctlr *vol_ctlr);

int bt_vcp_vol_ctlr_vol_up(struct bt_vcp_vol_ctlr *vol_ctlr);

int bt_vcp_vol_ctlr_unmute_vol_down(struct bt_vcp_vol_ctlr *vol_ctlr);

int bt_vcp_vol_ctlr_unmute_vol_up(struct bt_vcp_vol_ctlr *vol_ctlr);

int bt_vcp_vol_ctlr_set_vol(struct bt_vcp_vol_ctlr *vol_ctlr, uint8_t volume);

int bt_vcp_vol_ctlr_unmute(struct bt_vcp_vol_ctlr *vol_ctlr);

int bt_vcp_vol_ctlr_mute(struct bt_vcp_vol_ctlr *vol_ctlr);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_VCP_H_ */
```

## 902.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2020-2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 49 行

条件编译配置（Configuration）标记：`CONFIG_BT_VCP_VOL_REND`。

### 注释 3：原第 59 行

条件编译配置（Configuration）标记：`CONFIG_BT_VCP_VOL_REND`。

### 注释 4：原第 595 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_VCP_H_`。

## 902.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/vcp_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/audio/aics.h](https://docs.zephyrproject.org/latest/doxygen/html/aics_8h.html)
- [zephyr/bluetooth/audio/vocs.h](https://docs.zephyrproject.org/latest/doxygen/html/vocs_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)
- [bt_vcp_vol_rend_register_param](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [step](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md#a098e6c6921813b3f0dc7512cd483c829)
- [mute](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md#a93f2b246ac4241db468a46a64909866e)
- [volume](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md#a6cf1343a2b3033c3f4676d66017cfda7)
- [bt_vocs_register_param](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md)
- [vocs_param](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md#a6b5096f174425659c7fbc71df0da8e67)
- [BT_VCP_VOL_REND_VOCS_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gae7195f4556ad2442bc45d8d43cdeedd0)
- [bt_aics_register_param](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md)
- [aics_param](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md#a69257b668dc52429c64daa7af5161805)
- [BT_VCP_VOL_REND_AICS_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga571d7ff5a6a507fcd7cbdfa32a04643b)
- [bt_vcp_vol_rend_cb](../bluetooth_service_model_reference/P182_bt_vcp_vol_rend_cb_结构体.md)
- [cb](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md#af9a09c453394fd4a28d6415e2775c3f5)
- [bt_vcp_included](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md)
- [vocs_cnt](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md#acb0c8e853808adfd9c3b92b45e874103)
- [bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)
- [vocs](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md#a1f04068dd88d2fecef5fd78a3c7d4429)
- [aics_cnt](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md#af521bb12ebef4c5f60609040140474c0)
- [bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)
- [aics](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md#aa6c87b8c9b4b2be6ec6429fd2ee68398)
- [bt_vcp_vol_rend_included_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga1761d6618c48983e034cee5574c9c34f)
- [bt_vcp_vol_rend_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga752d8ff54a4b8c8c854a9c693617e64d)
- [state](../bluetooth_service_model_reference/P182_bt_vcp_vol_rend_cb_结构体.md#a05f84d8a2deedbc426ef22b89c87bd40)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [flags](../bluetooth_service_model_reference/P182_bt_vcp_vol_rend_cb_结构体.md#a3413d33fa8c3362ded6ec81533c27c86)
- [bt_vcp_vol_rend_set_step](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga56e0f99d2688fb6f9e0e4d9103de706c)
- [bt_vcp_vol_rend_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga9d1ac028abc88549ea18b6a0c585c781)
- [bt_vcp_vol_rend_get_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga1e6c9cfa0d012a4b701c99d8e6b5985d)
- [bt_vcp_vol_rend_vol_down](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gaf3c622f151a21d1dd617e97917c5ff5e)
- [bt_vcp_vol_rend_vol_up](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga6c10dd5a029b524994739f0b37a82c84)
- [bt_vcp_vol_rend_unmute_vol_down](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga3e6236a8679f95ba512181284a05923d)
- [bt_vcp_vol_rend_unmute_vol_up](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gadf77729fee34f6605101c278fd2b7c46)
- [bt_vcp_vol_rend_set_vol](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga61279baeba11152625cd3a87c5d973c9)
- [bt_vcp_vol_rend_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga303d4b6b77987ab41cb1753ef861dd6c)
- [bt_vcp_vol_rend_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga0c6d0b6b015f069a9adc1332a32c79f9)
- [bt_vcp_vol_ctlr_cb](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md)
- [state](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#ac3b89f35b79d35384f9ead31cf15ac4e)
- [mute](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#aa2cd77992831eef7e59d3e4a01a0e542)
- [flags](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#a4df90987abe0e53894e4064b3487c2bb)
- [discover](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#ada8fe8d838d6d2c983d746e7e7ed1171)
- [vol_down](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#ac986e0c5cb49395fe8581f5b1dae1a88)
- [vol_up](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#ae1beaa5d0a61c630fa90b4a5236ce743)
- [unmute](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#a6a217e0d8cbcc56e5128d5b7acdaac6d)
- [vol_down_unmute](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#a770e300127b8357f1e76f0cca21b74e5)
- [vol_up_unmute](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#af4ca636d19c83694f9b86102404b0538)
- [vol_set](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#abe7cf51858428db6b953a21a6ba40f83)
- [bt_vocs_cb](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md)
- [vocs_cb](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#af6407bb0652539608f0100f02cfaadd1)
- [bt_aics_cb](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md)
- [aics_cb](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#a430b1ee27c9bf7d6c7f8498748d91b21)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_vcp_vol_ctlr_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga7861d0c3426870c015106e8e170004a3)
- [bt_vcp_vol_ctlr_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gae69e4730df4341bbb9bbbba1bea14005)
- [bt_vcp_vol_ctlr_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gac18d43a0785155c1131249f95554f2de)
- [bt_vcp_vol_ctlr_get_by_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga0c8faa95cc36950c70ff572c931eedee)
- [bt_vcp_vol_ctlr_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gab287197243191e3dbf162c6d16b6d726)
- [bt_vcp_vol_ctlr_included_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gaaa748c49e103ff161f67df9663ea6330)
- [bt_vcp_vol_ctlr_read_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga68cab2f59c63542b6a7da33d555da0ab)
- [bt_vcp_vol_ctlr_read_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gaefc226a5abb6bb1540d4b44ac4ddc236)
- [bt_vcp_vol_ctlr_vol_down](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga03e073e29920f4a530d2f8851b4b8df4)
- [bt_vcp_vol_ctlr_vol_up](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga908eb20727e1d68ed569badfd13ff896)
- [bt_vcp_vol_ctlr_unmute_vol_down](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga20348b220988c700cabf356f7165d4d6)
- [bt_vcp_vol_ctlr_unmute_vol_up](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga2defdeee7486eee22a3416db8aa7c251)
- [bt_vcp_vol_ctlr_set_vol](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gaaa5b5cd9a11c0e1fcdabce690ba20616)
- [bt_vcp_vol_ctlr_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga4e95c3fb071cb94fbe75f88e96d34b36)
- [bt_vcp_vol_ctlr_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga106b7f826adec665b4f0ac3d5e82b867)
- [aics.h](https://docs.zephyrproject.org/latest/doxygen/html/aics_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_vcp_included::vocs](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md#a1f04068dd88d2fecef5fd78a3c7d4429)
- [bt_vcp_included::aics](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md#aa6c87b8c9b4b2be6ec6429fd2ee68398)
- [bt_vcp_included::vocs_cnt](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md#acb0c8e853808adfd9c3b92b45e874103)
- [bt_vcp_included::aics_cnt](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md#af521bb12ebef4c5f60609040140474c0)
- [bt_vcp_vol_ctlr_cb::aics_cb](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#a430b1ee27c9bf7d6c7f8498748d91b21)
- [bt_vcp_vol_ctlr_cb::flags](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#a4df90987abe0e53894e4064b3487c2bb)
- [bt_vcp_vol_ctlr_cb::unmute](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#a6a217e0d8cbcc56e5128d5b7acdaac6d)
- [bt_vcp_vol_ctlr_cb::vol_down_unmute](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#a770e300127b8357f1e76f0cca21b74e5)
- [bt_vcp_vol_ctlr_cb::mute](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#aa2cd77992831eef7e59d3e4a01a0e542)
- [bt_vcp_vol_ctlr_cb::vol_set](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#abe7cf51858428db6b953a21a6ba40f83)
- [bt_vcp_vol_ctlr_cb::state](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#ac3b89f35b79d35384f9ead31cf15ac4e)
- [bt_vcp_vol_ctlr_cb::vol_down](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#ac986e0c5cb49395fe8581f5b1dae1a88)
- [bt_vcp_vol_ctlr_cb::discover](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#ada8fe8d838d6d2c983d746e7e7ed1171)
- [bt_vcp_vol_ctlr_cb::vol_up](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#ae1beaa5d0a61c630fa90b4a5236ce743)
- [bt_vcp_vol_ctlr_cb::vol_up_unmute](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#af4ca636d19c83694f9b86102404b0538)
- [bt_vcp_vol_ctlr_cb::vocs_cb](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#af6407bb0652539608f0100f02cfaadd1)
- [bt_vcp_vol_rend_cb::state](../bluetooth_service_model_reference/P182_bt_vcp_vol_rend_cb_结构体.md#a05f84d8a2deedbc426ef22b89c87bd40)
- [bt_vcp_vol_rend_cb::flags](../bluetooth_service_model_reference/P182_bt_vcp_vol_rend_cb_结构体.md#a3413d33fa8c3362ded6ec81533c27c86)
- [bt_vcp_vol_rend_register_param::step](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md#a098e6c6921813b3f0dc7512cd483c829)
- [bt_vcp_vol_rend_register_param::aics_param](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md#a69257b668dc52429c64daa7af5161805)
- [bt_vcp_vol_rend_register_param::vocs_param](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md#a6b5096f174425659c7fbc71df0da8e67)
- [bt_vcp_vol_rend_register_param::volume](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md#a6cf1343a2b3033c3f4676d66017cfda7)
- [bt_vcp_vol_rend_register_param::mute](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md#a93f2b246ac4241db468a46a64909866e)
- [bt_vcp_vol_rend_register_param::cb](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md#af9a09c453394fd4a28d6415e2775c3f5)
- [vocs.h](https://docs.zephyrproject.org/latest/doxygen/html/vocs_8h.html)

---

[上一章](P901_vc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P903_veaa_x_3.h_源码浏览.md)
