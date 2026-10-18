---
id: learning.zephyr-docs.api-source-supplement-reference.page-18
title: avdtp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_avdtp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html)。

## 18.1\_原始可见代码（Source Code）

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
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="foldopen00108"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00128"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="foldopen00170"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="aavdtp_8h_html_a28b828df32df5a40e8487dc4dee78757"></a>
<a id="aavdtp_8h_html_a28b828df32df5a40e8487dc4dee78757a29ddb8e6ac9f3a5e15dcac7cafa0c8d9"></a>
<a id="aavdtp_8h_html_a28b828df32df5a40e8487dc4dee78757a8652b3d997c0daec5b90be2aa046ae0f"></a>
<a id="aavdtp_8h_html_a4cf69d936236918ec0fc7adecb6080e3"></a>
<a id="aavdtp_8h_html_a4cf69d936236918ec0fc7adecb6080e3a9c31ee783c40c6f9ce82975915b2bf7d"></a>
<a id="aavdtp_8h_html_a4cf69d936236918ec0fc7adecb6080e3adbf6d71be0000eb3fec4a4d27dc73ce0"></a>
<a id="aavdtp_8h_html_a6e9f13217ede2687e206b6a8cbd9137f"></a>
<a id="aavdtp_8h_html_a6e9f13217ede2687e206b6a8cbd9137fa383f8313252215e91846309eaebb96ee"></a>
<a id="aavdtp_8h_html_a6e9f13217ede2687e206b6a8cbd9137fa6ecbf2cc869da3ca5cab0dac88718cf4"></a>
<a id="aavdtp_8h_html_a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58"></a>
<a id="aavdtp_8h_html_a8427dfa4dcd3fe8ac6eaf2471bad7e51"></a>
<a id="aavdtp_8h_html_a8427dfa4dcd3fe8ac6eaf2471bad7e51a071e2e6d18ed90fb1ec2df84449c1902"></a>
<a id="aavdtp_8h_html_a8427dfa4dcd3fe8ac6eaf2471bad7e51a2eaaefe841558fdcb6218d28e59a0b73"></a>
<a id="aavdtp_8h_html_a8427dfa4dcd3fe8ac6eaf2471bad7e51a53110f0946f0b8f1dde7c0913ae4d642"></a>
<a id="aavdtp_8h_html_a8427dfa4dcd3fe8ac6eaf2471bad7e51a84ae7f392441dead9cd57b3098fc6a5e"></a>
<a id="aavdtp_8h_html_a8427dfa4dcd3fe8ac6eaf2471bad7e51aa26e4aaa9a62ee539d6001f7af5c3b37"></a>
<a id="aavdtp_8h_html_a8427dfa4dcd3fe8ac6eaf2471bad7e51ab1f6623b4d8205e0ca7119e2b4c1c40c"></a>
<a id="aavdtp_8h_html_a8427dfa4dcd3fe8ac6eaf2471bad7e51ab639cf078a6fa9012ee5ee5320203439"></a>
<a id="aavdtp_8h_html_a8427dfa4dcd3fe8ac6eaf2471bad7e51ad2a426bce39bfc9cf5451243ed26c6c0"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a10e3d79ef76dcfefd5ac648e1fdf2818"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a14ec5c7a6ab35e9b946395765a911099"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a15256eb00e75a0f4075a7bb93f3419af"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a203030bcba53de65a3cee79a10f8e24a"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a260b2bc259678f0d813e7b1a20c477e6"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a3599e6793991735508735f644a502e75"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a4c85c064ea60c5d13000494f0f2abd20"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a57665911c0fa0f58660407c05a523320"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a60cf8824a9c3a5b38bfb6b300d0e01d7"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a751370153f9c3f55ddce10b6353db49f"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a7a25b50bff50fff150a3bfb69a7d2aa8"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a851fd25830e88e90706c2e3a8db45ba0"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21a90f79a8847a33d5ad76a1ca339a33b14"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21ac1c1575a5479fc41dba1534b03d21e35"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21acb07c6cd131aa3bc77eb1cf32050c7e9"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21accb4c206f63e8ef78265bd83b25f52da"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21accd5a3a315e7ebcb0da1364665494064"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21ad3c7ef84765610f59dea092aa1504eee"></a>
<a id="aavdtp_8h_html_affc7226c1b7795a3d2f51cb4ffaf6d21aecefed33942c46624cdd26209a791445"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__avdtp__sep__info_html"></a>
<a id="astructbt__avdtp__sep__info_html_a03bf1e8c29eaff7ef3b48f21dff7aa49"></a>
<a id="astructbt__avdtp__sep__info_html_a3d6c6832a40cdb31976a447459576e0f"></a>
<a id="astructbt__avdtp__sep__info_html_a8cd4323a80ad4138095d5aceb08a64b6"></a>
<a id="astructbt__avdtp__sep__info_html_ab644a59a54d943e3d4729a198bda59cd"></a>
<a id="astructbt__avdtp__sep__info_html_add86d89b0e062f034aa85bf7121313ee"></a>
<a id="astructbt__avdtp__sep__ops_html"></a>
<a id="astructbt__avdtp__sep__ops_html_a62cffe9d43241f5314ae04fd993d4943"></a>
<a id="astructbt__avdtp__sep__ops_html_a97a6ac5f821579e2ab04ee22e738f173"></a>
<a id="astructbt__avdtp__sep__ops_html_add289f4fed823f55e80fbf29b6e87e1c"></a>
<a id="astructbt__avdtp__sep_html"></a>
<a id="astructbt__avdtp__sep_html_a0258b35f0834479a2dccdcad9b3854b9"></a>
<a id="astructbt__avdtp__sep_html_a1d9cb5bedeae1fdea1ee63e656d06503"></a>
<a id="astructbt__avdtp__sep_html_a2405b59cc7ed23c9cb221a9a684dc386"></a>
<a id="astructbt__avdtp__sep_html_a33e4959b5d7c5f53469ed59af4cae022"></a>
<a id="astructbt__avdtp__sep_html_a5c1afb8231c42d39156023939583681a"></a>
<a id="astructbt__avdtp__sep_html_acff70f1a2d29b987f57af88ac75afc3e"></a>
<a id="astructbt__l2cap__br__chan_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructnet__buf_html"></a>

```c


/*
 * Copyright (c) 2015-2016 Intel Corporation
 * Copyright 2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_AVDTP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_AVDTP_H_

#ifdef __cplusplus
extern "C" {
#endif

#define AVDTP_VERSION_1_3 0x0103

#define AVDTP_VERSION AVDTP_VERSION_1_3

enum bt_avdtp_err_code {
        BT_AVDTP_SUCCESS = 0x00,
        BT_AVDTP_TIME_OUT = 0xFF,
        BT_AVDTP_BAD_HEADER_FORMAT = 0x01,
        BT_AVDTP_BAD_LENGTH = 0x11,
        BT_AVDTP_BAD_ACP_SEID = 0x12,
        BT_AVDTP_SEP_IN_USE = 0x13,
        BT_AVDTP_SEP_NOT_IN_USE = 0x14,
        BT_AVDTP_BAD_SERV_CATEGORY = 0x17,
        BT_AVDTP_BAD_PAYLOAD_FORMAT = 0x18,
        BT_AVDTP_NOT_SUPPORTED_COMMAND = 0x19,
        BT_AVDTP_INVALID_CAPABILITIES = 0x1A,
        BT_AVDTP_BAD_RECOVERY_TYPE = 0x22,
        BT_AVDTP_BAD_MEDIA_TRANSPORT_FORMAT = 0x23,
        BT_AVDTP_BAD_RECOVERY_FORMAT = 0x25,
        BT_AVDTP_BAD_ROHC_FORMAT = 0x26,
        BT_AVDTP_BAD_CP_FORMAT = 0x27,
        BT_AVDTP_BAD_MULTIPLEXING_FORMAT = 0x28,
        BT_AVDTP_UNSUPPORTED_CONFIGURATION = 0x29,
        BT_AVDTP_BAD_STATE = 0x31,
};

enum bt_avdtp_sep_type {
        BT_AVDTP_SOURCE = 0,
        BT_AVDTP_SINK = 1
};

enum bt_avdtp_media_type {
        BT_AVDTP_AUDIO = 0x00,
        BT_AVDTP_VIDEO = 0x01,
        BT_AVDTP_MULTIMEDIA = 0x02
};

struct bt_avdtp_sep_info {
        uint8_t inuse: 1;
        uint8_t id: 6;
        uint8_t reserved: 1;
        enum bt_avdtp_sep_type tsep;
        enum bt_avdtp_media_type media_type;
};

enum bt_avdtp_service_category {
        BT_AVDTP_SERVICE_MEDIA_TRANSPORT = 0x01,
        BT_AVDTP_SERVICE_REPORTING = 0x02,
        BT_AVDTP_SERVICE_MEDIA_RECOVERY = 0x03,
        BT_AVDTP_SERVICE_CONTENT_PROTECTION = 0x04,
        BT_AVDTP_SERVICE_HEADER_COMPRESSION = 0x05,
        BT_AVDTP_SERVICE_MULTIPLEXING = 0x06,
        BT_AVDTP_SERVICE_MEDIA_CODEC = 0x07,
        BT_AVDTP_SERVICE_DELAY_REPORTING = 0x08,
};

enum bt_avdtp_recovery_type {
        BT_AVDTP_RECOVERY_TYPE_FORBIDDEN = 0x00,
        BT_ADVTP_RECOVERY_TYPE_RFC2733 = 0x01,
};

struct bt_avdtp_sep;

struct bt_avdtp_sep_ops {
        void (*connected)(struct bt_avdtp_sep *sep);

        void (*disconnected)(struct bt_avdtp_sep *sep);

        void (*media_data_cb)(struct bt_avdtp_sep *sep, struct net_buf *buf);
};

struct bt_avdtp_sep {
        struct bt_avdtp_sep_info sep_info;
        struct bt_l2cap_br_chan chan;
        /* semaphore for lock/unlock */
        struct k_sem sem_lock;
        struct bt_avdtp *session;
        const struct bt_avdtp_sep_ops *ops;
        struct k_work_delayable _delay_work;
        uint8_t _delay_work_state;
        uint8_t state;
        /* Internally used list node */
        sys_snode_t _node;
};

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_AVDTP_H_ */
```

## 18.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2015-2016 Intel Corporation。

版权（Copyright）：2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 175 行

用于加锁/解锁的信号量（Semaphore）。

### 注释 3：原第 187 行

内部使用的链表节点。

### 注释 4：原第 195 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_AVDTP_H_`。

## 18.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html)
- [bt_avdtp_err_code](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21)
- [BT_AVDTP_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a15256eb00e75a0f4075a7bb93f3419af)
- [BT_AVDTP_TIME_OUT](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a203030bcba53de65a3cee79a10f8e24a)
- [BT_AVDTP_BAD_HEADER_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a751370153f9c3f55ddce10b6353db49f)
- [BT_AVDTP_BAD_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21acb07c6cd131aa3bc77eb1cf32050c7e9)
- [BT_AVDTP_BAD_ACP_SEID](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21accd5a3a315e7ebcb0da1364665494064)
- [BT_AVDTP_SEP_IN_USE](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a7a25b50bff50fff150a3bfb69a7d2aa8)
- [BT_AVDTP_SEP_NOT_IN_USE](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21aecefed33942c46624cdd26209a791445)
- [BT_AVDTP_BAD_SERV_CATEGORY](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a260b2bc259678f0d813e7b1a20c477e6)
- [BT_AVDTP_BAD_PAYLOAD_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a851fd25830e88e90706c2e3a8db45ba0)
- [BT_AVDTP_NOT_SUPPORTED_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a3599e6793991735508735f644a502e75)
- [BT_AVDTP_INVALID_CAPABILITIES](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a4c85c064ea60c5d13000494f0f2abd20)
- [BT_AVDTP_BAD_RECOVERY_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21ad3c7ef84765610f59dea092aa1504eee)
- [BT_AVDTP_BAD_MEDIA_TRANSPORT_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21ac1c1575a5479fc41dba1534b03d21e35)
- [BT_AVDTP_BAD_RECOVERY_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a14ec5c7a6ab35e9b946395765a911099)
- [BT_AVDTP_BAD_ROHC_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a60cf8824a9c3a5b38bfb6b300d0e01d7)
- [BT_AVDTP_BAD_CP_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21accb4c206f63e8ef78265bd83b25f52da)
- [BT_AVDTP_BAD_MULTIPLEXING_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a90f79a8847a33d5ad76a1ca339a33b14)
- [BT_AVDTP_UNSUPPORTED_CONFIGURATION](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a57665911c0fa0f58660407c05a523320)
- [BT_AVDTP_BAD_STATE](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21a10e3d79ef76dcfefd5ac648e1fdf2818)
- [bt_avdtp_sep_type](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a28b828df32df5a40e8487dc4dee78757)
- [BT_AVDTP_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a28b828df32df5a40e8487dc4dee78757a8652b3d997c0daec5b90be2aa046ae0f)
- [BT_AVDTP_SINK](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a28b828df32df5a40e8487dc4dee78757a29ddb8e6ac9f3a5e15dcac7cafa0c8d9)
- [bt_avdtp_media_type](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a6e9f13217ede2687e206b6a8cbd9137f)
- [BT_AVDTP_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58)
- [BT_AVDTP_VIDEO](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a6e9f13217ede2687e206b6a8cbd9137fa383f8313252215e91846309eaebb96ee)
- [BT_AVDTP_MULTIMEDIA](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a6e9f13217ede2687e206b6a8cbd9137fa6ecbf2cc869da3ca5cab0dac88718cf4)
- [bt_avdtp_sep_info](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [inuse](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md#ab644a59a54d943e3d4729a198bda59cd)
- [id](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md#a03bf1e8c29eaff7ef3b48f21dff7aa49)
- [reserved](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md#a3d6c6832a40cdb31976a447459576e0f)
- [tsep](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md#add86d89b0e062f034aa85bf7121313ee)
- [media_type](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md#a8cd4323a80ad4138095d5aceb08a64b6)
- [bt_avdtp_service_category](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a8427dfa4dcd3fe8ac6eaf2471bad7e51)
- [BT_AVDTP_SERVICE_MEDIA_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a8427dfa4dcd3fe8ac6eaf2471bad7e51ab1f6623b4d8205e0ca7119e2b4c1c40c)
- [BT_AVDTP_SERVICE_REPORTING](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a8427dfa4dcd3fe8ac6eaf2471bad7e51aa26e4aaa9a62ee539d6001f7af5c3b37)
- [BT_AVDTP_SERVICE_MEDIA_RECOVERY](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a8427dfa4dcd3fe8ac6eaf2471bad7e51a071e2e6d18ed90fb1ec2df84449c1902)
- [BT_AVDTP_SERVICE_CONTENT_PROTECTION](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a8427dfa4dcd3fe8ac6eaf2471bad7e51a53110f0946f0b8f1dde7c0913ae4d642)
- [BT_AVDTP_SERVICE_HEADER_COMPRESSION](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a8427dfa4dcd3fe8ac6eaf2471bad7e51a2eaaefe841558fdcb6218d28e59a0b73)
- [BT_AVDTP_SERVICE_MULTIPLEXING](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a8427dfa4dcd3fe8ac6eaf2471bad7e51ab639cf078a6fa9012ee5ee5320203439)
- [BT_AVDTP_SERVICE_MEDIA_CODEC](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a8427dfa4dcd3fe8ac6eaf2471bad7e51a84ae7f392441dead9cd57b3098fc6a5e)
- [BT_AVDTP_SERVICE_DELAY_REPORTING](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a8427dfa4dcd3fe8ac6eaf2471bad7e51ad2a426bce39bfc9cf5451243ed26c6c0)
- [bt_avdtp_recovery_type](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a4cf69d936236918ec0fc7adecb6080e3)
- [BT_AVDTP_RECOVERY_TYPE_FORBIDDEN](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a4cf69d936236918ec0fc7adecb6080e3a9c31ee783c40c6f9ce82975915b2bf7d)
- [BT_ADVTP_RECOVERY_TYPE_RFC2733](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a4cf69d936236918ec0fc7adecb6080e3adbf6d71be0000eb3fec4a4d27dc73ce0)
- [bt_avdtp_sep](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md)
- [bt_avdtp_sep_ops](../bluetooth_classic_model_reference/P015_bt_avdtp_sep_ops_结构体.md)
- [connected](../bluetooth_classic_model_reference/P015_bt_avdtp_sep_ops_结构体.md#a97a6ac5f821579e2ab04ee22e738f173)
- [disconnected](../bluetooth_classic_model_reference/P015_bt_avdtp_sep_ops_结构体.md#add289f4fed823f55e80fbf29b6e87e1c)
- [media_data_cb](../bluetooth_classic_model_reference/P015_bt_avdtp_sep_ops_结构体.md#a62cffe9d43241f5314ae04fd993d4943)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [sep_info](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md#a0258b35f0834479a2dccdcad9b3854b9)
- [bt_l2cap_br_chan](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md)
- [chan](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md#a33e4959b5d7c5f53469ed59af4cae022)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [sem_lock](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md#acff70f1a2d29b987f57af88ac75afc3e)
- [session](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md#a5c1afb8231c42d39156023939583681a)
- [ops](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md#a1d9cb5bedeae1fdea1ee63e656d06503)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [state](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md#a2405b59cc7ed23c9cb221a9a684dc386)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_avdtp_sep_info::id](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md#a03bf1e8c29eaff7ef3b48f21dff7aa49)
- [bt_avdtp_sep_info::reserved](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md#a3d6c6832a40cdb31976a447459576e0f)
- [bt_avdtp_sep_info::media_type](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md#a8cd4323a80ad4138095d5aceb08a64b6)
- [bt_avdtp_sep_info::inuse](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md#ab644a59a54d943e3d4729a198bda59cd)
- [bt_avdtp_sep_info::tsep](../bluetooth_classic_model_reference/P014_bt_avdtp_sep_info_结构体.md#add86d89b0e062f034aa85bf7121313ee)
- [bt_avdtp_sep_ops::media_data_cb](../bluetooth_classic_model_reference/P015_bt_avdtp_sep_ops_结构体.md#a62cffe9d43241f5314ae04fd993d4943)
- [bt_avdtp_sep_ops::connected](../bluetooth_classic_model_reference/P015_bt_avdtp_sep_ops_结构体.md#a97a6ac5f821579e2ab04ee22e738f173)
- [bt_avdtp_sep_ops::disconnected](../bluetooth_classic_model_reference/P015_bt_avdtp_sep_ops_结构体.md#add289f4fed823f55e80fbf29b6e87e1c)
- [bt_avdtp_sep::sep_info](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md#a0258b35f0834479a2dccdcad9b3854b9)
- [bt_avdtp_sep::ops](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md#a1d9cb5bedeae1fdea1ee63e656d06503)
- [bt_avdtp_sep::state](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md#a2405b59cc7ed23c9cb221a9a684dc386)
- [bt_avdtp_sep::chan](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md#a33e4959b5d7c5f53469ed59af4cae022)
- [bt_avdtp_sep::session](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md#a5c1afb8231c42d39156023939583681a)
- [bt_avdtp_sep::sem_lock](../bluetooth_classic_model_reference/P013_bt_avdtp_sep_结构体.md#acff70f1a2d29b987f57af88ac75afc3e)

---

[上一章](P017_ascs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P019_bip.h_源码浏览.md)
