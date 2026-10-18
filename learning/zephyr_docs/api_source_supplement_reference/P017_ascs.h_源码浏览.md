---
id: learning.zephyr-docs.api-source-supplement-reference.page-17
title: ascs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ascs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_ascs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ascs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ascs_8h.html)。

## 17.1\_原始可见代码（Source Code）

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
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="foldopen00090"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00137"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="foldopen00174"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="foldopen00279"></a>
<a id="l00279"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="foldopen00424"></a>
<a id="l00424"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="aassigned__numbers_8h_html"></a>
<a id="abluetooth_2audio_2audio_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__ascs_html_ga04eddf75bc1f2deafee5d6b234dd5b07"></a>
<a id="agroup__bt__ascs_html_ga2a87430dd2b2a04985c2faffb0b033a3"></a>
<a id="agroup__bt__ascs_html_ga9ca1630544a336b15af8a8e8934c5a45"></a>
<a id="agroup__bt__ascs_html_ga9f7efa749c75edd32dc50503397ab9d1"></a>
<a id="agroup__bt__ascs_html_gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd"></a>
<a id="agroup__bt__ascs_html_gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557"></a>
<a id="agroup__bt__ascs_html_gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539"></a>
<a id="agroup__bt__ascs_html_gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0"></a>
<a id="agroup__bt__ascs_html_gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b"></a>
<a id="agroup__bt__ascs_html_gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea"></a>
<a id="agroup__bt__ascs_html_gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8"></a>
<a id="agroup__bt__ascs_html_gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942"></a>
<a id="agroup__bt__ascs_html_gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c"></a>
<a id="agroup__bt__ascs_html_gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf"></a>
<a id="agroup__bt__ascs_html_gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd"></a>
<a id="agroup__bt__ascs_html_gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gab53d0dd62bceff97cf8eed7d8cf80354"></a>
<a id="agroup__bt__audio_html_ga5bd899fb5e4d844058184913866e462f"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__ascs__cb_html"></a>
<a id="astructbt__ascs__cb_html_a319395d4c1dbbfe31d6f67366edd6125"></a>
<a id="astructbt__ascs__cb_html_a6c10e167b53d555e2762596bc8b28088"></a>
<a id="astructbt__ascs__cb_html_a6eb6e4e35f9373cbcceb6e93e29b5ef6"></a>
<a id="astructbt__ascs__cb_html_a99a5b250d4944c218c432df6bce5130d"></a>
<a id="astructbt__ascs__cb_html_aa259b32e5a731a20e23659d88143ec6e"></a>
<a id="astructbt__ascs__cb_html_ab303fa3d23738b85d55b6b88a5827f43"></a>
<a id="astructbt__ascs__cb_html_ab9e8bc649765905b1db1b62e5a2a0f09"></a>
<a id="astructbt__ascs__cb_html_adcecb25b3c30808d38109eaa414bbf97"></a>
<a id="astructbt__ascs__cb_html_af2934cbca5f9700adb01f6035f0c329a"></a>
<a id="astructbt__ascs__register__param_html"></a>
<a id="astructbt__ascs__register__param_html_a04839e2149a25e801905fff837b7ab59"></a>
<a id="astructbt__ascs__register__param_html_a9607646e7f44a39fa589b13d2bcaa9bb"></a>
<a id="astructbt__ascs__register__param_html_ad830e2991175f5e86fd8be34692e7af5"></a>
<a id="astructbt__audio__codec__cfg_html"></a>
<a id="astructbt__bap__ascs__rsp_html"></a>
<a id="astructbt__bap__ascs__rsp_html_a138532bc40f60547c56d8b108ad44d1e"></a>
<a id="astructbt__bap__ascs__rsp_html_a736f44864015244a8b48a859eff6b902"></a>
<a id="astructbt__bap__ascs__rsp_html_a8ea364298f7e3e784b7878215db63d91"></a>
<a id="astructbt__bap__ep_html"></a>
<a id="astructbt__bap__qos__cfg__pref_html"></a>
<a id="astructbt__bap__qos__cfg__pref_html_a1df8cd4ed27e9099b8b2a069855010aa"></a>
<a id="astructbt__bap__qos__cfg__pref_html_a286bfb02d35ca148f263f1fa1ca9e061"></a>
<a id="astructbt__bap__qos__cfg__pref_html_a2a2de382f04a50d26d174dcc7c7a12c1"></a>
<a id="astructbt__bap__qos__cfg__pref_html_a3f643768de9d8b0a7a62e403703e0033"></a>
<a id="astructbt__bap__qos__cfg__pref_html_a666be60856b5b4688d21d7a36b956c29"></a>
<a id="astructbt__bap__qos__cfg__pref_html_a697a67e623d758b76be342a125a369a6"></a>
<a id="astructbt__bap__qos__cfg__pref_html_ab6475a80b33a9cea69edeaa3093c9070"></a>
<a id="astructbt__bap__qos__cfg__pref_html_ac5871b4f58be038eeda483e8d07b9b53"></a>
<a id="astructbt__bap__qos__cfg_html"></a>
<a id="astructbt__bap__stream_html"></a>
<a id="astructbt__conn_html"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_ASCS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_ASCS_H_


#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

enum bt_bap_ascs_rsp_code {
        BT_BAP_ASCS_RSP_CODE_SUCCESS = 0x00U,
        BT_BAP_ASCS_RSP_CODE_NOT_SUPPORTED = 0x01U,
        BT_BAP_ASCS_RSP_CODE_INVALID_LENGTH = 0x02U,
        BT_BAP_ASCS_RSP_CODE_INVALID_ASE = 0x03U,
        BT_BAP_ASCS_RSP_CODE_INVALID_ASE_STATE = 0x04U,
        BT_BAP_ASCS_RSP_CODE_INVALID_DIR = 0x05U,
        BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED = 0x06U,
        BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED = 0x07U,
        BT_BAP_ASCS_RSP_CODE_CONF_REJECTED = 0x08U,
        BT_BAP_ASCS_RSP_CODE_CONF_INVALID = 0x09U,
        BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED = 0x0AU,
        BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED = 0x0BU,
        BT_BAP_ASCS_RSP_CODE_METADATA_INVALID = 0x0CU,
        BT_BAP_ASCS_RSP_CODE_NO_MEM = 0x0DU,
        BT_BAP_ASCS_RSP_CODE_UNSPECIFIED = 0x0EU,
};

enum bt_bap_ascs_reason {
        BT_BAP_ASCS_REASON_NONE = 0x00U,
        BT_BAP_ASCS_REASON_CODEC = 0x01U,
        BT_BAP_ASCS_REASON_CODEC_DATA = 0x02U,
        BT_BAP_ASCS_REASON_INTERVAL = 0x03U,
        BT_BAP_ASCS_REASON_FRAMING = 0x04U,
        BT_BAP_ASCS_REASON_PHY = 0x05U,
        BT_BAP_ASCS_REASON_SDU = 0x06U,
        BT_BAP_ASCS_REASON_RTN = 0x07U,
        BT_BAP_ASCS_REASON_LATENCY = 0x08U,
        BT_BAP_ASCS_REASON_PD = 0x09U,
        BT_BAP_ASCS_REASON_CIS = 0x0AU,
};

struct bt_bap_ascs_rsp {
        enum bt_bap_ascs_rsp_code code;

        union {
                enum bt_bap_ascs_reason reason;

                enum bt_audio_metadata_type metadata_type;
        };
};

#define BT_BAP_ASCS_RSP(c, r)                                                                      \
        (struct bt_bap_ascs_rsp)                                                                   \
        {                                                                                          \
                .code = c, .reason = r                                                             \
        }

struct bt_bap_qos_cfg_pref {
        bool unframed_supported;

        uint8_t phy;

        uint8_t rtn;

        uint16_t latency;

        uint32_t pd_min;

        uint32_t pd_max;

        uint32_t pref_pd_min;

        uint32_t pref_pd_max;
};

#define BT_BAP_QOS_CFG_PREF(_unframed_supported, _phy, _rtn, _latency, _pd_min, _pd_max,           \
                            _pref_pd_min, _pref_pd_max)                                            \
        {                                                                                          \
                .unframed_supported = _unframed_supported,                                         \
                .phy = _phy,                                                                       \
                .rtn = _rtn,                                                                       \
                .latency = _latency,                                                               \
                .pd_min = _pd_min,                                                                 \
                .pd_max = _pd_max,                                                                 \
                .pref_pd_min = _pref_pd_min,                                                       \
                .pref_pd_max = _pref_pd_max,                                                       \
        }

/* Temporary solution to handle circular dependencies between ascs.h and bap.h */
struct bt_bap_stream;
struct bt_bap_ep;
struct bt_bap_qos_cfg;

struct bt_ascs_cb {
        int (*config)(struct bt_conn *conn, const struct bt_bap_ep *ep, enum bt_audio_dir dir,
                      const struct bt_audio_codec_cfg *codec_cfg, struct bt_bap_stream **stream,
                      struct bt_bap_qos_cfg_pref *const pref, struct bt_bap_ascs_rsp *rsp);

        int (*reconfig)(struct bt_bap_stream *stream, enum bt_audio_dir dir,
                        const struct bt_audio_codec_cfg *codec_cfg,
                        struct bt_bap_qos_cfg_pref *const pref, struct bt_bap_ascs_rsp *rsp);

        int (*qos)(struct bt_bap_stream *stream, const struct bt_bap_qos_cfg *qos,
                   struct bt_bap_ascs_rsp *rsp);

        int (*enable)(struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len,
                      struct bt_bap_ascs_rsp *rsp);

        int (*start)(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp);

        int (*metadata)(struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len,
                        struct bt_bap_ascs_rsp *rsp);

        int (*disable)(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp);

        int (*stop)(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp);

        int (*release)(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp);
};

struct bt_ascs_register_param {
        uint8_t snk_cnt;

        uint8_t src_cnt;

        const struct bt_ascs_cb *cb;
};

int bt_ascs_register(const struct bt_ascs_register_param *param);

int bt_ascs_unregister(void);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_ASCS_H_ */
```

## 17.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 273 行

处理 `ascs.h` 与 `bap.h` 之间循环依赖（Circular dependencies）的临时解决方案。

### 注释 3：原第 481 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_ASCS_H_`。

## 17.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ascs_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)
- [BT_BAP_ASCS_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd)
- [BT_BAP_ASCS_RSP_CODE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d)
- [BT_BAP_ASCS_RSP_CODE_INVALID_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9)
- [BT_BAP_ASCS_RSP_CODE_INVALID_ASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa)
- [BT_BAP_ASCS_RSP_CODE_INVALID_ASE_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5)
- [BT_BAP_ASCS_RSP_CODE_INVALID_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146)
- [BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a)
- [BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62)
- [BT_BAP_ASCS_RSP_CODE_CONF_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21)
- [BT_BAP_ASCS_RSP_CODE_CONF_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219)
- [BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7)
- [BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06)
- [BT_BAP_ASCS_RSP_CODE_METADATA_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06)
- [BT_BAP_ASCS_RSP_CODE_NO_MEM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb)
- [BT_BAP_ASCS_RSP_CODE_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a)
- [bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)
- [BT_BAP_ASCS_REASON_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd)
- [BT_BAP_ASCS_REASON_CODEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea)
- [BT_BAP_ASCS_REASON_CODEC_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0)
- [BT_BAP_ASCS_REASON_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c)
- [BT_BAP_ASCS_REASON_FRAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539)
- [BT_BAP_ASCS_REASON_PHY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8)
- [BT_BAP_ASCS_REASON_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b)
- [BT_BAP_ASCS_REASON_RTN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf)
- [BT_BAP_ASCS_REASON_LATENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942)
- [BT_BAP_ASCS_REASON_PD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557)
- [BT_BAP_ASCS_REASON_CIS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c)
- [bt_bap_ascs_rsp](../bluetooth_le_audio_model_reference/P010_bt_bap_ascs_rsp_结构体.md)
- [code](../bluetooth_le_audio_model_reference/P010_bt_bap_ascs_rsp_结构体.md#a8ea364298f7e3e784b7878215db63d91)
- [reason](../bluetooth_le_audio_model_reference/P010_bt_bap_ascs_rsp_结构体.md#a138532bc40f60547c56d8b108ad44d1e)
- [bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)
- [metadata_type](../bluetooth_le_audio_model_reference/P010_bt_bap_ascs_rsp_结构体.md#a736f44864015244a8b48a859eff6b902)
- [bt_bap_qos_cfg_pref](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md)
- [unframed_supported](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#a2a2de382f04a50d26d174dcc7c7a12c1)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [phy](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#a697a67e623d758b76be342a125a369a6)
- [rtn](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#a286bfb02d35ca148f263f1fa1ca9e061)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [latency](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#ac5871b4f58be038eeda483e8d07b9b53)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pd_min](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#a3f643768de9d8b0a7a62e403703e0033)
- [pd_max](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#a666be60856b5b4688d21d7a36b956c29)
- [pref_pd_min](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#a1df8cd4ed27e9099b8b2a069855010aa)
- [pref_pd_max](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#ab6475a80b33a9cea69edeaa3093c9070)
- [bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)
- [bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)
- [bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)
- [bt_ascs_cb](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md)
- [config](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#aa259b32e5a731a20e23659d88143ec6e)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [reconfig](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#a6eb6e4e35f9373cbcceb6e93e29b5ef6)
- [qos](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#a319395d4c1dbbfe31d6f67366edd6125)
- [enable](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#adcecb25b3c30808d38109eaa414bbf97)
- [start](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#ab303fa3d23738b85d55b6b88a5827f43)
- [metadata](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#af2934cbca5f9700adb01f6035f0c329a)
- [disable](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#a6c10e167b53d555e2762596bc8b28088)
- [stop](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#a99a5b250d4944c218c432df6bce5130d)
- [release](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#ab9e8bc649765905b1db1b62e5a2a0f09)
- [bt_ascs_register_param](../bluetooth_le_audio_model_reference/P006_bt_ascs_register_param_结构体.md)
- [snk_cnt](../bluetooth_le_audio_model_reference/P006_bt_ascs_register_param_结构体.md#a04839e2149a25e801905fff837b7ab59)
- [src_cnt](../bluetooth_le_audio_model_reference/P006_bt_ascs_register_param_结构体.md#ad830e2991175f5e86fd8be34692e7af5)
- [cb](../bluetooth_le_audio_model_reference/P006_bt_ascs_register_param_结构体.md#a9607646e7f44a39fa589b13d2bcaa9bb)
- [bt_ascs_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga04eddf75bc1f2deafee5d6b234dd5b07)
- [bt_ascs_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga2a87430dd2b2a04985c2faffb0b033a3)
- [assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [bt_ascs_cb::qos](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#a319395d4c1dbbfe31d6f67366edd6125)
- [bt_ascs_cb::disable](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#a6c10e167b53d555e2762596bc8b28088)
- [bt_ascs_cb::reconfig](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#a6eb6e4e35f9373cbcceb6e93e29b5ef6)
- [bt_ascs_cb::stop](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#a99a5b250d4944c218c432df6bce5130d)
- [bt_ascs_cb::config](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#aa259b32e5a731a20e23659d88143ec6e)
- [bt_ascs_cb::start](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#ab303fa3d23738b85d55b6b88a5827f43)
- [bt_ascs_cb::release](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#ab9e8bc649765905b1db1b62e5a2a0f09)
- [bt_ascs_cb::enable](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#adcecb25b3c30808d38109eaa414bbf97)
- [bt_ascs_cb::metadata](../bluetooth_le_audio_model_reference/P005_bt_ascs_cb_结构体.md#af2934cbca5f9700adb01f6035f0c329a)
- [bt_ascs_register_param::snk_cnt](../bluetooth_le_audio_model_reference/P006_bt_ascs_register_param_结构体.md#a04839e2149a25e801905fff837b7ab59)
- [bt_ascs_register_param::cb](../bluetooth_le_audio_model_reference/P006_bt_ascs_register_param_结构体.md#a9607646e7f44a39fa589b13d2bcaa9bb)
- [bt_ascs_register_param::src_cnt](../bluetooth_le_audio_model_reference/P006_bt_ascs_register_param_结构体.md#ad830e2991175f5e86fd8be34692e7af5)
- [bt_bap_ascs_rsp::reason](../bluetooth_le_audio_model_reference/P010_bt_bap_ascs_rsp_结构体.md#a138532bc40f60547c56d8b108ad44d1e)
- [bt_bap_ascs_rsp::metadata_type](../bluetooth_le_audio_model_reference/P010_bt_bap_ascs_rsp_结构体.md#a736f44864015244a8b48a859eff6b902)
- [bt_bap_ascs_rsp::code](../bluetooth_le_audio_model_reference/P010_bt_bap_ascs_rsp_结构体.md#a8ea364298f7e3e784b7878215db63d91)
- [bt_bap_qos_cfg_pref::pref_pd_min](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#a1df8cd4ed27e9099b8b2a069855010aa)
- [bt_bap_qos_cfg_pref::rtn](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#a286bfb02d35ca148f263f1fa1ca9e061)
- [bt_bap_qos_cfg_pref::unframed_supported](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#a2a2de382f04a50d26d174dcc7c7a12c1)
- [bt_bap_qos_cfg_pref::pd_min](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#a3f643768de9d8b0a7a62e403703e0033)
- [bt_bap_qos_cfg_pref::pd_max](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#a666be60856b5b4688d21d7a36b956c29)
- [bt_bap_qos_cfg_pref::phy](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#a697a67e623d758b76be342a125a369a6)
- [bt_bap_qos_cfg_pref::pref_pd_max](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#ab6475a80b33a9cea69edeaa3093c9070)
- [bt_bap_qos_cfg_pref::latency](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md#ac5871b4f58be038eeda483e8d07b9b53)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P016_arm-gic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P018_avdtp.h_源码浏览.md)
