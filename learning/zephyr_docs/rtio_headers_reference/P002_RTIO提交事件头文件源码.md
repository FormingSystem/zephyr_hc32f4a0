---
id: learning.zephyr-docs.rtio-headers-reference.page-2
title: RTIO提交事件头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sqe_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_RTIO提交事件头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sqe_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_RTIO提交事件头文件参考.md)和[公共API](../rtio_core_reference/P001_RTIO公共接口.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00251"></a>
<a id="foldopen00257"></a>
<a id="foldopen00268"></a>
<a id="foldopen00274"></a>
<a id="foldopen00310"></a>
<a id="foldopen00403"></a>
<a id="foldopen00427"></a>
<a id="foldopen00462"></a>
<a id="foldopen00479"></a>
<a id="foldopen00494"></a>
<a id="foldopen00505"></a>
<a id="foldopen00533"></a>
<a id="foldopen00560"></a>
<a id="foldopen00584"></a>
<a id="foldopen00596"></a>
<a id="foldopen00630"></a>
<a id="foldopen00653"></a>
<a id="foldopen00670"></a>
<a id="foldopen00707"></a>
<a id="foldopen00712"></a>
<a id="foldopen00727"></a>
<a id="foldopen00747"></a>
<a id="foldopen00768"></a>
<a id="foldopen00788"></a>
<a id="foldopen00803"></a>
<a id="aatomic_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__atomic__apis_html_gab879da5aa1ffcc317adc664c016586f7"></a>
<a id="agroup__mpsc__lockfree_html_ga403add133841ef88e10d74141e782b37"></a>
<a id="agroup__mpsc__lockfree_html_ga823ec37b84ac43e46167aac954bce9d7"></a>
<a id="agroup__rtio__ops_html_ga18e0ff7d44e4c33900106aefad0a8508"></a>
<a id="agroup__rtio__ops_html_ga3b4f9b1ee1612290323161ecc16e0859"></a>
<a id="agroup__rtio__ops_html_ga6f95c0a5fbcc020a0d1102d3b08934bd"></a>
<a id="agroup__rtio__ops_html_ga8dcaef0cda159e16520a95543ff62827"></a>
<a id="agroup__rtio__ops_html_ga9f0e70f5a28be65a8ed67c0257a72692"></a>
<a id="agroup__rtio__ops_html_gad5f073978f641413989d1c6b405d6c36"></a>
<a id="agroup__rtio__ops_html_gad74290935595b83040676b426cd07161"></a>
<a id="agroup__rtio__ops_html_gad987be3acfe406b11419c7e8cd068cf5"></a>
<a id="agroup__rtio__ops_html_gae8da4da54f32963190f52c7533d4c951"></a>
<a id="agroup__rtio__ops_html_gafeb05c351207cd1638fa78f6607e1a4a"></a>
<a id="agroup__rtio__sqe__flags_html_ga00f8ead8f043fe40d49d0bc3325fb299"></a>
<a id="agroup__rtio__sqe__flags_html_ga07f09cc0c95be6cfdddb23f8acacb1ea"></a>
<a id="agroup__rtio__sqe__flags_html_ga2802b46584220afffa0e959e149d5a4d"></a>
<a id="agroup__rtio__sqe__flags_html_ga8578ffdb8f53a51b94fa86a6f02d4a11"></a>
<a id="agroup__rtio__sqe__flags_html_gae9191d521d4ab602b53fefb74020d06b"></a>
<a id="agroup__rtio_html_ga15c1f623658d27d300d1a31a6f3d6b9d"></a>
<a id="agroup__rtio_html_ga274cb5490582b38682f255cac4703143"></a>
<a id="agroup__rtio_html_ga31be14ece09e061a8d42ca8f2395286a"></a>
<a id="agroup__rtio_html_ga599ee43fdf35e1cf895cbbe9272e4c50"></a>
<a id="agroup__rtio_html_ga5d5b7d440eab064918424b0261455a9f"></a>
<a id="agroup__rtio_html_ga5e55583901cd13d24f60744747c5c72b"></a>
<a id="agroup__rtio_html_ga7d2e5673582f32b630e2294dfbf0fe44"></a>
<a id="agroup__rtio_html_ga7f7856d1f4fd1d8c4f6eebcccfe77701"></a>
<a id="agroup__rtio_html_ga89c7cc2494e3dda50737f78f1a1376cf"></a>
<a id="agroup__rtio_html_ga9803aa829f8c0eeee746ea7d872c20cc"></a>
<a id="agroup__rtio_html_ga9d0dd7d0e2e3d281092f2350d6e1713e"></a>
<a id="agroup__rtio_html_gaa2f35d2909f4a19003199a3fd759fc41"></a>
<a id="agroup__rtio_html_gab254ffa4d10bfb670bacd1c47c1f8711"></a>
<a id="agroup__rtio_html_gab9b605dcbb01d21c88f9ae70588ea3b5"></a>
<a id="agroup__rtio_html_gabcb356e1df7b39bbb6f732d6fa6cc97d"></a>
<a id="agroup__rtio_html_gad45b80544e4e894cf170fe44fb752930"></a>
<a id="agroup__rtio_html_gada1e3abf92a46e376138435debc8baf4"></a>
<a id="agroup__rtio_html_gae690e3dc0fc40dda57257b2eed432719"></a>
<a id="agroup__rtio_html_gae87be354087d038953dae07c7f9cd3b0"></a>
<a id="agroup__rtio_html_gaef904eb6a8810d8c3ea537c4d6edbee5"></a>
<a id="agroup__rtio_html_gafd97c145b8525895494a31a87610f65d"></a>
<a id="agroup__subsys__tracing__macros_html_ga445bcac4cec53d560ddca757de17e1e3"></a>
<a id="agroup__subsys__tracing__macros_html_gab0350eef3ed26733e57505ee2d0487cb"></a>
<a id="agroup__sys-util_html_gac5bc561d1bfd1bf68877fe577779bd2f"></a>
<a id="akernel_8h_html"></a>
<a id="ampsc__lockfree_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astring_8h_html"></a>
<a id="astring_8h_html_a4137694174d4ca2fad886a1db355015c"></a>
<a id="astring_8h_html_af0f01bffcd16daa9143f6014d10a25ad"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructk__timepoint__t_html"></a>
<a id="astructmpsc__node_html"></a>
<a id="astructrtio__iodev__sqe_html"></a>
<a id="astructrtio__iodev__sqe_html_a2afb82e550e614f87db7cd1bf2c3a352"></a>
<a id="astructrtio__iodev__sqe_html_a2bd98599678909c0ddb22f879affa12b"></a>
<a id="astructrtio__iodev__sqe_html_a3c3a050793589258eab5ff5ac30f24c8"></a>
<a id="astructrtio__iodev__sqe_html_a9cfdd004b65a5e2bc111bc2fb333498c"></a>
<a id="astructrtio__iodev_html"></a>
<a id="astructrtio__sqe_html"></a>
<a id="astructrtio__sqe_html_a07bf344b1b1063b8bea80cf5ba1c1cc5"></a>
<a id="astructrtio__sqe_html_a0ed519ee0b5867ff73bdaf37f983c971"></a>
<a id="astructrtio__sqe_html_a18bfa63542954f4bb8b924c92c48e931"></a>
<a id="astructrtio__sqe_html_a1d8d3e3426e47a2c7f54d98f51acd953"></a>
<a id="astructrtio__sqe_html_a29e0c1b06b6f7b604af147a231b46319"></a>
<a id="astructrtio__sqe_html_a2b73e59283f6dc79cef3c804ed973160"></a>
<a id="astructrtio__sqe_html_a438d2156a61aef9ca840af9c01d5dfa4"></a>
<a id="astructrtio__sqe_html_a4d2090fc11b897724a883ad1087d9f73"></a>
<a id="astructrtio__sqe_html_a528eb9b721be7b8a8898ab16a7e2d9a7"></a>
<a id="astructrtio__sqe_html_a64f5db04d58882832f86477628c25be3"></a>
<a id="astructrtio__sqe_html_a67376f40a13960b152a23da250275722"></a>
<a id="astructrtio__sqe_html_a6c784702f011592c84feacd57915bbfc"></a>
<a id="astructrtio__sqe_html_a8bebe5d55aa8549d749466e444fadf91"></a>
<a id="astructrtio__sqe_html_a8d78973983abca8b97cfc5bcdc2dd2f1"></a>
<a id="astructrtio__sqe_html_a927a43f86f65484179c8113caa775c9c"></a>
<a id="astructrtio__sqe_html_aa09a0c93a6e8cfc73278a87942e4af33"></a>
<a id="astructrtio__sqe_html_aad2ff8524df0e24b812e77e2393bf5b0"></a>
<a id="astructrtio__sqe_html_ab71176c084e8b8eb65dfeb3018ae2a49"></a>
<a id="astructrtio__sqe_html_ac07a16c50a067acc90bd4ab08aae4184"></a>
<a id="astructrtio__sqe_html_af1bd1edaaf32a58fb0461c989ac2a456"></a>
<a id="astructrtio__sqe_html_af8c31c33e9fedebe55cac73595d0f696"></a>
<a id="astructrtio_html"></a>
<a id="asys_2util_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * SPDX-FileCopyrightText: Copyright (c) 2022 Intel Corporation
<a id="l00003"></a> * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
<a id="l00004"></a> * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
<a id="l00005"></a> *
<a id="l00006"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00007"></a> */
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>#ifndef ZEPHYR_INCLUDE_RTIO_SQE_H_
<a id="l00017"></a>#define ZEPHYR_INCLUDE_RTIO_SQE_H_
<a id="l00018"></a>
<a id="l00019"></a>#include &lt;stdint.h&gt;
<a id="l00020"></a>#include &lt;string.h&gt;
<a id="l00021"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00022"></a>#include &lt;zephyr/sys/atomic.h&gt;
<a id="l00023"></a>#include &lt;zephyr/sys/mpsc_lockfree.h&gt;
<a id="l00024"></a>#include &lt;zephyr/sys/util.h&gt;
<a id="l00025"></a>
<a id="l00026"></a>#ifdef __cplusplus
<a id="l00027"></a>extern "C" {
<a id="l00028"></a>#endif
<a id="l00029"></a>
<a id="l00034"></a>
<a id="l00047"></a>
<a id="l00051"></a>#define RTIO_PRIO_LOW 0U
<a id="l00052"></a>
<a id="l00056"></a>#define RTIO_PRIO_NORM 127U
<a id="l00057"></a>
<a id="l00061"></a>#define RTIO_PRIO_HIGH 255U
<a id="l00062"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00074"></a>
<a id="l00082"></a>#define RTIO_SQE_CHAINED BIT(0)
<a id="l00083"></a>
<a id="l00094"></a>#define RTIO_SQE_TRANSACTION BIT(1)
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00106"></a>#define RTIO_SQE_MEMPOOL_BUFFER BIT(2)
<a id="l00107"></a>
<a id="l00114"></a>#define RTIO_SQE_CANCELED BIT(3)
<a id="l00115"></a>
<a id="l00122"></a>#define RTIO_SQE_MULTISHOT BIT(4)
<a id="l00123"></a>
<a id="l00127"></a>#define RTIO_SQE_NO_RESPONSE BIT(5)
<a id="l00128"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00140"></a>
<a id="l00142"></a>#define RTIO_OP_NOP 0
<a id="l00143"></a>
<a id="l00145"></a>#define RTIO_OP_RX (RTIO_OP_NOP+1)
<a id="l00146"></a>
<a id="l00148"></a>#define RTIO_OP_TX (RTIO_OP_RX+1)
<a id="l00149"></a>
<a id="l00151"></a>#define RTIO_OP_TINY_TX (RTIO_OP_TX+1)
<a id="l00152"></a>
<a id="l00154"></a>#define RTIO_OP_CALLBACK (RTIO_OP_TINY_TX+1)
<a id="l00155"></a>
<a id="l00157"></a>#define RTIO_OP_TXRX (RTIO_OP_CALLBACK+1)
<a id="l00158"></a>
<a id="l00160"></a>#define RTIO_OP_DELAY (RTIO_OP_TXRX+1)
<a id="l00161"></a>
<a id="l00163"></a>#define RTIO_OP_I2C_RECOVER (RTIO_OP_DELAY+1)
<a id="l00164"></a>
<a id="l00166"></a>#define RTIO_OP_I2C_CONFIGURE (RTIO_OP_I2C_RECOVER+1)
<a id="l00167"></a>
<a id="l00169"></a>#define RTIO_OP_I3C_RECOVER (RTIO_OP_I2C_CONFIGURE+1)
<a id="l00170"></a>
<a id="l00172"></a>#define RTIO_OP_I3C_CONFIGURE (RTIO_OP_I3C_RECOVER+1)
<a id="l00173"></a>
<a id="l00175"></a>#define RTIO_OP_I3C_CCC (RTIO_OP_I3C_CONFIGURE+1)
<a id="l00176"></a>
<a id="l00178"></a>#define RTIO_OP_AWAIT (RTIO_OP_I3C_CCC+1)
<a id="l00179"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00191"></a>
<a id="l00195"></a>#define RTIO_IODEV_I2C_STOP BIT(1)
<a id="l00196"></a>
<a id="l00200"></a>#define RTIO_IODEV_I2C_RESTART BIT(2)
<a id="l00201"></a>
<a id="l00205"></a>#define RTIO_IODEV_I2C_10_BITS BIT(3)
<a id="l00206"></a>
<a id="l00210"></a>
<a id="l00217"></a>
<a id="l00221"></a>#define RTIO_IODEV_I3C_STOP BIT(1)
<a id="l00222"></a>
<a id="l00226"></a>#define RTIO_IODEV_I3C_RESTART BIT(2)
<a id="l00227"></a>
<a id="l00231"></a>#define RTIO_IODEV_I3C_HDR BIT(3)
<a id="l00232"></a>
<a id="l00236"></a>#define RTIO_IODEV_I3C_NBCH BIT(4)
<a id="l00237"></a>
<a id="l00241"></a>#define RTIO_IODEV_I3C_NOACK_EXPECTED BIT(5)
<a id="l00242"></a>
<a id="l00246"></a>#define RTIO_IODEV_I3C_HDR_MODE_MASK GENMASK(15, 8)
<a id="l00247"></a>
<a id="l00251"></a>#define RTIO_IODEV_I3C_HDR_MODE_SET(flags) \
<a id="l00252"></a>        FIELD_PREP(RTIO_IODEV_I3C_HDR_MODE_MASK, flags)
<a id="l00253"></a>
<a id="l00257"></a>#define RTIO_IODEV_I3C_HDR_MODE_GET(flags) \
<a id="l00258"></a>        FIELD_GET(RTIO_IODEV_I3C_HDR_MODE_MASK, flags)
<a id="l00259"></a>
<a id="l00263"></a>#define RTIO_IODEV_I3C_HDR_CMD_CODE_MASK GENMASK(22, 16)
<a id="l00264"></a>
<a id="l00268"></a>#define RTIO_IODEV_I3C_HDR_CMD_CODE_SET(flags) \
<a id="l00269"></a>        FIELD_PREP(RTIO_IODEV_I3C_HDR_CMD_CODE_MASK, flags)
<a id="l00270"></a>
<a id="l00274"></a>#define RTIO_IODEV_I3C_HDR_CMD_CODE_GET(flags) \
<a id="l00275"></a>        FIELD_GET(RTIO_IODEV_I3C_HDR_CMD_CODE_MASK, flags)
<a id="l00276"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00283"></a>struct rtio_sqe;
<a id="l00284"></a>struct rtio_iodev_sqe;
<a id="l00285"></a>struct rtio_iodev;
<a id="l00286"></a>struct rtio;
<a id="l00288"></a>
<a id="l00297"></a>typedef void (*rtio_callback_t)(struct rtio *r, const struct rtio_sqe *sqe, int res, void *arg0);
<a id="l00298"></a>
<a id="l00305"></a>typedef void (*rtio_signaled_t)(struct rtio_iodev_sqe *iodev_sqe, void *userdata);
<a id="l00306"></a>
<a id="l00310"></a>struct rtio_sqe {
<a id="l00311"></a>        uint8_t op;
<a id="l00312"></a>
<a id="l00313"></a>        uint8_t prio;
<a id="l00314"></a>
<a id="l00315"></a>        uint16_t flags;
<a id="l00316"></a>
<a id="l00317"></a>        uint32_t iodev_flags;
<a id="l00318"></a>
<a id="l00319"></a>        const struct rtio_iodev *iodev;
<a id="l00320"></a>
<a id="l00328"></a>        void *userdata;
<a id="l00329"></a>
<a id="l00331"></a>        union {
<a id="l00332"></a>
<a id="l00334"></a>                struct {
<a id="l00335"></a>                        uint32_t buf_len;
<a id="l00336"></a>                        const uint8_t *buf;
<a id="l00337"></a>                } tx;
<a id="l00338"></a>
<a id="l00340"></a>                struct {
<a id="l00341"></a>                        uint32_t buf_len;
<a id="l00342"></a>                        uint8_t *buf;
<a id="l00343"></a>                } rx;
<a id="l00344"></a>
<a id="l00346"></a>                struct {
<a id="l00347"></a>                        uint8_t buf_len;
<a id="l00348"></a>                        uint8_t buf[7];
<a id="l00349"></a>                } tiny_tx;
<a id="l00350"></a>
<a id="l00352"></a>                struct {
<a id="l00353"></a>                        rtio_callback_t callback;
<a id="l00354"></a>                        void *arg0;
<a id="l00355"></a>                } callback;
<a id="l00356"></a>
<a id="l00358"></a>                struct {
<a id="l00359"></a>                        uint32_t buf_len;
<a id="l00360"></a>                        const uint8_t *tx_buf;
<a id="l00361"></a>                        uint8_t *rx_buf;
<a id="l00362"></a>                } txrx;
<a id="l00363"></a>
<a id="l00364"></a>#ifdef CONFIG_RTIO_OP_DELAY
<a id="l00366"></a>                struct {
<a id="l00367"></a>                        k_timeout_t timeout;
<a id="l00368"></a>                        k_timepoint_t expiry;
<a id="l00369"></a>                } delay;
<a id="l00370"></a>#endif
<a id="l00371"></a>
<a id="l00373"></a>                uint32_t i2c_config;
<a id="l00374"></a>
<a id="l00376"></a>                struct {
<a id="l00377"></a>                        /* enum i3c_config_type type; */
<a id="l00378"></a>                        int type;
<a id="l00379"></a>                        void *config;
<a id="l00380"></a>                } i3c_config;
<a id="l00381"></a>
<a id="l00383"></a>                /* struct i3c_ccc_payload *ccc_payload; */
<a id="l00384"></a>                void *ccc_payload;
<a id="l00385"></a>
<a id="l00387"></a>                struct {
<a id="l00389"></a>                        atomic_t ok;
<a id="l00391"></a>                        rtio_signaled_t callback;
<a id="l00392"></a>                        void *userdata;
<a id="l00393"></a>                } await;
<a id="l00394"></a>        };
<a id="l00395"></a>};
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00403"></a>struct rtio_iodev_sqe {
<a id="l00404"></a>        struct rtio_sqe sqe;
<a id="l00405"></a>        struct mpsc_node q;
<a id="l00406"></a>        struct rtio_iodev_sqe *next;
<a id="l00407"></a>        struct rtio *r;
<a id="l00408"></a>};
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00412"></a>/* Ensure the rtio_iodev_sqe never grows beyond a common cacheline size of 64 bytes */
<a id="l00413"></a>#if CONFIG_RTIO_SQE_CACHELINE_CHECK
<a id="l00414"></a>#ifdef CONFIG_DCACHE_LINE_SIZE
<a id="l00415"></a>#define RTIO_CACHE_LINE_SIZE CONFIG_DCACHE_LINE_SIZE
<a id="l00416"></a>#else
<a id="l00417"></a>#define RTIO_CACHE_LINE_SIZE 64
<a id="l00418"></a>#endif
<a id="l00419"></a>BUILD_ASSERT(sizeof(struct rtio_iodev_sqe) &lt;= RTIO_CACHE_LINE_SIZE,
<a id="l00420"></a>        "RTIO performs best when the submissions queue entries are less than a cache line");
<a id="l00421"></a>#endif
<a id="l00423"></a>
<a id="l00427"></a>static inline void rtio_sqe_prep_nop(struct rtio_sqe *sqe,
<a id="l00428"></a>                                const struct rtio_iodev *iodev,
<a id="l00429"></a>                                void *userdata)
<a id="l00430"></a>{
<a id="l00431"></a>        memset(sqe, 0, sizeof(struct rtio_sqe));
<a id="l00432"></a>        sqe-&gt;op = RTIO_OP_NOP;
<a id="l00433"></a>        sqe-&gt;iodev = iodev;
<a id="l00434"></a>        sqe-&gt;userdata = userdata;
<a id="l00435"></a>}
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00442"></a>static inline void _rtio_sqe_prep_read(struct rtio_sqe *sqe,
<a id="l00443"></a>                                      const struct rtio_iodev *iodev,
<a id="l00444"></a>                                      int8_t prio,
<a id="l00445"></a>                                      uint8_t *buf,
<a id="l00446"></a>                                      uint32_t len,
<a id="l00447"></a>                                      void *userdata)
<a id="l00448"></a>{
<a id="l00449"></a>        memset(sqe, 0, sizeof(struct rtio_sqe));
<a id="l00450"></a>        sqe-&gt;op = RTIO_OP_RX;
<a id="l00451"></a>        sqe-&gt;prio = prio;
<a id="l00452"></a>        sqe-&gt;iodev = iodev;
<a id="l00453"></a>        sqe-&gt;rx.buf_len = len;
<a id="l00454"></a>        sqe-&gt;rx.buf = buf;
<a id="l00455"></a>        sqe-&gt;userdata = userdata;
<a id="l00456"></a>}
<a id="l00458"></a>
<a id="l00462"></a>static inline void rtio_sqe_prep_read(struct rtio_sqe *sqe,
<a id="l00463"></a>                                      const struct rtio_iodev *iodev,
<a id="l00464"></a>                                      int8_t prio,
<a id="l00465"></a>                                      uint8_t *buf,
<a id="l00466"></a>                                      uint32_t len,
<a id="l00467"></a>                                      void *userdata)
<a id="l00468"></a>{
<a id="l00469"></a>        __ASSERT_NO_MSG(len &gt; 0 &amp;&amp; buf != NULL);
<a id="l00470"></a>
<a id="l00471"></a>        _rtio_sqe_prep_read(sqe, iodev, prio, buf, len, userdata);
<a id="l00472"></a>}
<a id="l00473"></a>
<a id="l00479"></a>static inline void rtio_sqe_prep_read_with_pool(struct rtio_sqe *sqe,
<a id="l00480"></a>                                                const struct rtio_iodev *iodev, int8_t prio,
<a id="l00481"></a>                                                void *userdata)
<a id="l00482"></a>{
<a id="l00483"></a>        _rtio_sqe_prep_read(sqe, iodev, prio, NULL, 0, userdata);
<a id="l00484"></a>        sqe-&gt;flags = RTIO_SQE_MEMPOOL_BUFFER;
<a id="l00485"></a>}
<a id="l00486"></a>
<a id="l00494"></a>static inline void rtio_sqe_prep_read_multishot(struct rtio_sqe *sqe,
<a id="l00495"></a>                                                const struct rtio_iodev *iodev, int8_t prio,
<a id="l00496"></a>                                                void *userdata)
<a id="l00497"></a>{
<a id="l00498"></a>        rtio_sqe_prep_read_with_pool(sqe, iodev, prio, userdata);
<a id="l00499"></a>        sqe-&gt;flags |= RTIO_SQE_MULTISHOT;
<a id="l00500"></a>}
<a id="l00501"></a>
<a id="l00505"></a>static inline void rtio_sqe_prep_write(struct rtio_sqe *sqe,
<a id="l00506"></a>                                       const struct rtio_iodev *iodev,
<a id="l00507"></a>                                       int8_t prio,
<a id="l00508"></a>                                       const uint8_t *buf,
<a id="l00509"></a>                                       uint32_t len,
<a id="l00510"></a>                                       void *userdata)
<a id="l00511"></a>{
<a id="l00512"></a>        __ASSERT_NO_MSG(len &gt; 0 &amp;&amp; buf != NULL);
<a id="l00513"></a>
<a id="l00514"></a>        memset(sqe, 0, sizeof(struct rtio_sqe));
<a id="l00515"></a>        sqe-&gt;op = RTIO_OP_TX;
<a id="l00516"></a>        sqe-&gt;prio = prio;
<a id="l00517"></a>        sqe-&gt;iodev = iodev;
<a id="l00518"></a>        sqe-&gt;tx.buf_len = len;
<a id="l00519"></a>        sqe-&gt;tx.buf = buf;
<a id="l00520"></a>        sqe-&gt;userdata = userdata;
<a id="l00521"></a>}
<a id="l00522"></a>
<a id="l00533"></a>static inline void rtio_sqe_prep_tiny_write(struct rtio_sqe *sqe,
<a id="l00534"></a>                                            const struct rtio_iodev *iodev,
<a id="l00535"></a>                                            int8_t prio,
<a id="l00536"></a>                                            const uint8_t *tiny_write_data,
<a id="l00537"></a>                                            uint8_t tiny_write_len,
<a id="l00538"></a>                                            void *userdata)
<a id="l00539"></a>{
<a id="l00540"></a>        __ASSERT_NO_MSG(tiny_write_len &lt;= sizeof(sqe-&gt;tiny_tx.buf));
<a id="l00541"></a>        __ASSERT_NO_MSG(tiny_write_len &gt; 0 &amp;&amp; tiny_write_data != NULL);
<a id="l00542"></a>
<a id="l00543"></a>        memset(sqe, 0, sizeof(struct rtio_sqe));
<a id="l00544"></a>        sqe-&gt;op = RTIO_OP_TINY_TX;
<a id="l00545"></a>        sqe-&gt;prio = prio;
<a id="l00546"></a>        sqe-&gt;iodev = iodev;
<a id="l00547"></a>        sqe-&gt;tiny_tx.buf_len = tiny_write_len;
<a id="l00548"></a>        memcpy(sqe-&gt;tiny_tx.buf, tiny_write_data, tiny_write_len);
<a id="l00549"></a>        sqe-&gt;userdata = userdata;
<a id="l00550"></a>}
<a id="l00551"></a>
<a id="l00560"></a>static inline void rtio_sqe_prep_callback(struct rtio_sqe *sqe,
<a id="l00561"></a>                                          rtio_callback_t callback,
<a id="l00562"></a>                                          void *arg0,
<a id="l00563"></a>                                          void *userdata)
<a id="l00564"></a>{
<a id="l00565"></a>        memset(sqe, 0, sizeof(struct rtio_sqe));
<a id="l00566"></a>        sqe-&gt;op = RTIO_OP_CALLBACK;
<a id="l00567"></a>        sqe-&gt;prio = 0;
<a id="l00568"></a>        sqe-&gt;iodev = NULL;
<a id="l00569"></a>        sqe-&gt;callback.callback = callback;
<a id="l00570"></a>        sqe-&gt;callback.arg0 = arg0;
<a id="l00571"></a>        sqe-&gt;userdata = userdata;
<a id="l00572"></a>}
<a id="l00573"></a>
<a id="l00584"></a>static inline void rtio_sqe_prep_callback_no_cqe(struct rtio_sqe *sqe,
<a id="l00585"></a>                                                 rtio_callback_t callback,
<a id="l00586"></a>                                                 void *arg0,
<a id="l00587"></a>                                                 void *userdata)
<a id="l00588"></a>{
<a id="l00589"></a>        rtio_sqe_prep_callback(sqe, callback, arg0, userdata);
<a id="l00590"></a>        sqe-&gt;flags |= RTIO_SQE_NO_RESPONSE;
<a id="l00591"></a>}
<a id="l00592"></a>
<a id="l00596"></a>static inline void rtio_sqe_prep_transceive(struct rtio_sqe *sqe,
<a id="l00597"></a>                                            const struct rtio_iodev *iodev,
<a id="l00598"></a>                                            int8_t prio,
<a id="l00599"></a>                                            const uint8_t *tx_buf,
<a id="l00600"></a>                                            uint8_t *rx_buf,
<a id="l00601"></a>                                            uint32_t buf_len,
<a id="l00602"></a>                                            void *userdata)
<a id="l00603"></a>{
<a id="l00604"></a>        __ASSERT_NO_MSG(buf_len &gt; 0 &amp;&amp; tx_buf != NULL &amp;&amp; rx_buf != NULL);
<a id="l00605"></a>
<a id="l00606"></a>        memset(sqe, 0, sizeof(struct rtio_sqe));
<a id="l00607"></a>        sqe-&gt;op = RTIO_OP_TXRX;
<a id="l00608"></a>        sqe-&gt;prio = prio;
<a id="l00609"></a>        sqe-&gt;iodev = iodev;
<a id="l00610"></a>        sqe-&gt;txrx.buf_len = buf_len;
<a id="l00611"></a>        sqe-&gt;txrx.tx_buf = tx_buf;
<a id="l00612"></a>        sqe-&gt;txrx.rx_buf = rx_buf;
<a id="l00613"></a>        sqe-&gt;userdata = userdata;
<a id="l00614"></a>}
<a id="l00615"></a>
<a id="l00630"></a>static inline void rtio_sqe_prep_await(struct rtio_sqe *sqe,
<a id="l00631"></a>                                       const struct rtio_iodev *iodev,
<a id="l00632"></a>                                       int8_t prio,
<a id="l00633"></a>                                       void *userdata)
<a id="l00634"></a>{
<a id="l00635"></a>        memset(sqe, 0, sizeof(struct rtio_sqe));
<a id="l00636"></a>        sqe-&gt;op = RTIO_OP_AWAIT;
<a id="l00637"></a>        sqe-&gt;prio = prio;
<a id="l00638"></a>        sqe-&gt;iodev = iodev;
<a id="l00639"></a>        sqe-&gt;userdata = userdata;
<a id="l00640"></a>}
<a id="l00641"></a>
<a id="l00653"></a>static inline void rtio_sqe_prep_await_iodev(struct rtio_sqe *sqe, const struct rtio_iodev *iodev,
<a id="l00654"></a>                                             int8_t prio, void *userdata)
<a id="l00655"></a>{
<a id="l00656"></a>        __ASSERT_NO_MSG(iodev != NULL);
<a id="l00657"></a>        rtio_sqe_prep_await(sqe, iodev, prio, userdata);
<a id="l00658"></a>}
<a id="l00659"></a>
<a id="l00670"></a>static inline void rtio_sqe_prep_await_executor(struct rtio_sqe *sqe, int8_t prio, void *userdata)
<a id="l00671"></a>{
<a id="l00672"></a>        rtio_sqe_prep_await(sqe, NULL, prio, userdata);
<a id="l00673"></a>}
<a id="l00674"></a>
<a id="l00686"></a>#ifdef CONFIG_RTIO_OP_DELAY
<a id="l00693"></a>extern struct rtio_iodev rtio_timeout_iodev;
<a id="l00694"></a>
<a id="l00695"></a>static inline void rtio_sqe_prep_delay(struct rtio_sqe *sqe,
<a id="l00696"></a>                                       k_timeout_t timeout,
<a id="l00697"></a>                                       void *userdata)
<a id="l00698"></a>{
<a id="l00699"></a>        memset(sqe, 0, sizeof(struct rtio_sqe));
<a id="l00700"></a>        sqe-&gt;op = RTIO_OP_DELAY;
<a id="l00701"></a>        sqe-&gt;prio = 0;
<a id="l00702"></a>        sqe-&gt;iodev = &amp;rtio_timeout_iodev;
<a id="l00703"></a>        sqe-&gt;delay.timeout = timeout;
<a id="l00704"></a>        sqe-&gt;userdata = userdata;
<a id="l00705"></a>}
<a id="l00706"></a>#else
<a id="l00707"></a>#define rtio_sqe_prep_delay(sqe, timeout, userdata) \
<a id="l00708"></a>        BUILD_ASSERT(false, "CONFIG_RTIO_OP_DELAY not enabled")
<a id="l00709"></a>#endif
<a id="l00710"></a>
<a id="l00712"></a>static inline void rtio_sqe_prep_i2c_configure(struct rtio_sqe *sqe,
<a id="l00713"></a>                                               const struct rtio_iodev *iodev,
<a id="l00714"></a>                                               int8_t prio,
<a id="l00715"></a>                                               uint32_t dev_config,
<a id="l00716"></a>                                               void *userdata)
<a id="l00717"></a>{
<a id="l00718"></a>        memset(sqe, 0, sizeof(struct rtio_sqe));
<a id="l00719"></a>        sqe-&gt;op = RTIO_OP_I2C_CONFIGURE;
<a id="l00720"></a>        sqe-&gt;prio = prio;
<a id="l00721"></a>        sqe-&gt;iodev = iodev;
<a id="l00722"></a>        sqe-&gt;i2c_config = dev_config;
<a id="l00723"></a>        sqe-&gt;userdata = userdata;
<a id="l00724"></a>}
<a id="l00725"></a>
<a id="l00727"></a>static inline void rtio_sqe_prep_i2c_recover(struct rtio_sqe *sqe,
<a id="l00728"></a>                                             const struct rtio_iodev *iodev,
<a id="l00729"></a>                                             int8_t prio,
<a id="l00730"></a>                                             void *userdata)
<a id="l00731"></a>{
<a id="l00732"></a>        memset(sqe, 0, sizeof(struct rtio_sqe));
<a id="l00733"></a>        sqe-&gt;op = RTIO_OP_I2C_RECOVER;
<a id="l00734"></a>        sqe-&gt;prio = prio;
<a id="l00735"></a>        sqe-&gt;iodev = iodev;
<a id="l00736"></a>        sqe-&gt;userdata = userdata;
<a id="l00737"></a>}
<a id="l00738"></a>
<a id="l00747"></a>static inline struct rtio_iodev_sqe *rtio_txn_next(const struct rtio_iodev_sqe *iodev_sqe)
<a id="l00748"></a>{
<a id="l00749"></a>        struct rtio_iodev_sqe *next = NULL;
<a id="l00750"></a>
<a id="l00751"></a>        SYS_PORT_TRACING_FUNC_ENTER(rtio, txn_next, iodev_sqe-&gt;r, iodev_sqe);
<a id="l00752"></a>        if (iodev_sqe-&gt;sqe.flags &amp; RTIO_SQE_TRANSACTION) {
<a id="l00753"></a>                next = iodev_sqe-&gt;next;
<a id="l00754"></a>        }
<a id="l00755"></a>        SYS_PORT_TRACING_FUNC_EXIT(rtio, txn_next, iodev_sqe-&gt;r, next);
<a id="l00756"></a>        return next;
<a id="l00757"></a>}
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00768"></a>static inline struct rtio_iodev_sqe *rtio_chain_next(const struct rtio_iodev_sqe *iodev_sqe)
<a id="l00769"></a>{
<a id="l00770"></a>        struct rtio_iodev_sqe *next = NULL;
<a id="l00771"></a>
<a id="l00772"></a>        SYS_PORT_TRACING_FUNC_ENTER(rtio, txn_next, iodev_sqe-&gt;r, iodev_sqe);
<a id="l00773"></a>        if (iodev_sqe-&gt;sqe.flags &amp; RTIO_SQE_CHAINED) {
<a id="l00774"></a>                next = iodev_sqe-&gt;next;
<a id="l00775"></a>        }
<a id="l00776"></a>        SYS_PORT_TRACING_FUNC_EXIT(rtio, txn_next, iodev_sqe-&gt;r, next);
<a id="l00777"></a>        return next;
<a id="l00778"></a>}
<a id="l00779"></a>
<a id="l00788"></a>static inline struct rtio_iodev_sqe *rtio_iodev_sqe_next(const struct rtio_iodev_sqe *iodev_sqe)
<a id="l00789"></a>{
<a id="l00790"></a>        return iodev_sqe-&gt;next;
<a id="l00791"></a>}
<a id="l00792"></a>
<a id="l00803"></a>static inline void rtio_iodev_sqe_await_signal(struct rtio_iodev_sqe *iodev_sqe,
<a id="l00804"></a>                                               rtio_signaled_t callback,
<a id="l00805"></a>                                               void *userdata)
<a id="l00806"></a>{
<a id="l00807"></a>        iodev_sqe-&gt;sqe.await.callback = callback;
<a id="l00808"></a>        iodev_sqe-&gt;sqe.await.userdata = userdata;
<a id="l00809"></a>
<a id="l00810"></a>        if (!atomic_cas(&amp;iodev_sqe-&gt;sqe.await.ok, 0, 1)) {
<a id="l00811"></a>                callback(iodev_sqe, userdata);
<a id="l00812"></a>        }
<a id="l00813"></a>}
<a id="l00814"></a>
<a id="l00815"></a>/* Private structures and functions used for the pool of sqe structures */
<a id="l00817"></a>
<a id="l00818"></a>struct rtio_sqe_pool {
<a id="l00819"></a>        struct mpsc free_q;
<a id="l00820"></a>        const uint16_t pool_size;
<a id="l00821"></a>        uint16_t pool_free;
<a id="l00822"></a>        struct rtio_iodev_sqe *pool;
<a id="l00823"></a>};
<a id="l00824"></a>
<a id="l00825"></a>static inline struct rtio_iodev_sqe *rtio_sqe_pool_alloc(struct rtio_sqe_pool *pool)
<a id="l00826"></a>{
<a id="l00827"></a>        struct mpsc_node *node = mpsc_pop(&amp;pool-&gt;free_q);
<a id="l00828"></a>
<a id="l00829"></a>        if (node == NULL) {
<a id="l00830"></a>                return NULL;
<a id="l00831"></a>        }
<a id="l00832"></a>
<a id="l00833"></a>        struct rtio_iodev_sqe *iodev_sqe = CONTAINER_OF(node, struct rtio_iodev_sqe, q);
<a id="l00834"></a>
<a id="l00835"></a>        pool-&gt;pool_free--;
<a id="l00836"></a>
<a id="l00837"></a>        return iodev_sqe;
<a id="l00838"></a>}
<a id="l00839"></a>
<a id="l00840"></a>static inline void rtio_sqe_pool_free(struct rtio_sqe_pool *pool, struct rtio_iodev_sqe *iodev_sqe)
<a id="l00841"></a>{
<a id="l00842"></a>        mpsc_push(&amp;pool-&gt;free_q, &amp;iodev_sqe-&gt;q);
<a id="l00843"></a>
<a id="l00844"></a>        pool-&gt;pool_free++;
<a id="l00845"></a>}
<a id="l00846"></a>
<a id="l00847"></a>#if CONFIG_RTIO_SQE_PLACEMENT_DTCM
<a id="l00848"></a>#define RTIO_SQE_MEM Z_GENERIC_SECTION(".dtcm_bss") static
<a id="l00849"></a>#elif defined(CONFIG_RTIO_SQE_PLACEMENT_NOCACHE)
<a id="l00850"></a>#define RTIO_SQE_MEM __nocache static
<a id="l00851"></a>#else
<a id="l00852"></a>#define RTIO_SQE_MEM static
<a id="l00853"></a>#endif
<a id="l00854"></a>
<a id="l00855"></a>/* Do not try and reformat the macros */
<a id="l00856"></a>/* clang-format off */
<a id="l00857"></a>
<a id="l00858"></a>#define Z_RTIO_SQE_POOL_DEFINE(name, sz)                        \
<a id="l00859"></a>        RTIO_SQE_MEM struct rtio_iodev_sqe CONCAT(_sqe_pool_, name)[sz];        \
<a id="l00860"></a>        STRUCT_SECTION_ITERABLE(rtio_sqe_pool, name) = {        \
<a id="l00861"></a>                .free_q = MPSC_INIT((name.free_q)),     \
<a id="l00862"></a>                .pool_size = sz,                                \
<a id="l00863"></a>                .pool_free = sz,                                \
<a id="l00864"></a>                .pool = CONCAT(_sqe_pool_, name),               \
<a id="l00865"></a>        }
<a id="l00866"></a>
<a id="l00867"></a>/* clang-format on */
<a id="l00869"></a>
<a id="l00873"></a>
<a id="l00874"></a>#ifdef __cplusplus
<a id="l00875"></a>}
<a id="l00876"></a>#endif
<a id="l00877"></a>
<a id="l00878"></a>#endif /* ZEPHYR_INCLUDE_RTIO_SQE_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权属于Intel Corporation（2022年）以及Infineon Technologies AG或其关联公司（2026年）；保留全部权利，许可证为Apache-2.0。原始SPDX记录完整保留。

2. 原注释中的类型写法为`enum i3c_config_type type;`，可见实际成员声明使用`int`。

3. 原注释中的类型写法为`struct i3c_ccc_payload *ccc_payload;`，可见实际成员声明使用`void *`。

4. 确保`rtio_iodev_sqe`不会增长到超过常见的64字节缓存行（Cache Line）大小。

5. 供SQE结构体池使用的内部结构与函数。

6. 不要尝试重新格式化这些宏。

7. 关闭clang-format自动格式化。

8. 恢复clang-format自动格式化。

9. 头文件保护宏`ZEPHYR_INCLUDE_RTIO_SQE_H_`结束。

## 2.3\_原页符号提示（Symbol Descriptions）

### `atomic.h`

原子操作（Atomic Operations）API头文件。

符号定位：[atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)。

### `atomic_t`

```c
long atomic_t
```

原子整数变量（Atomic Integer Variable）。

定义位置（Definition）：atomic_types.h:34。

符号定位：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)。

### `atomic_cas`

```c
bool atomic_cas(atomic_t *target, atomic_val_t old_value, atomic_val_t new_value)
```

原子比较并设置（Atomic Compare-and-Set）。

符号定位：[atomic_cas](../atomic_reference/P001_原子操作公共接口.md#gab879da5aa1ffcc317adc664c016586f7)。

### `mpsc_push`

```c
static ALWAYS_INLINE void mpsc_push(struct mpsc *q, struct mpsc_node *n)
```

压入一个节点（Node）。

定义位置（Definition）：mpsc_lockfree.h:126。

符号定位：[mpsc_push](../intercore_reference/P158_MPSC无锁队列接口.md#ga403add133841ef88e10d74141e782b37)。

### `mpsc_pop`

```c
static struct mpsc_node * mpsc_pop(struct mpsc *q)
```

从链表中弹出一个节点。

定义位置（Definition）：mpsc_lockfree.h:145。

符号定位：[mpsc_pop](../intercore_reference/P158_MPSC无锁队列接口.md#ga823ec37b84ac43e46167aac954bce9d7)。

### `RTIO_OP_CALLBACK`

```c
#define RTIO_OP_CALLBACK
```

调用给定函数，即回调（Callback）的操作。

定义位置（Definition）：sqe.h:154。

符号定位：[RTIO_OP_CALLBACK](../rtio_model_reference/P009_RTIO操作码.md#ga18e0ff7d44e4c33900106aefad0a8508)。

### `RTIO_OP_I2C_RECOVER`

```c
#define RTIO_OP_I2C_RECOVER
```

恢复I2C总线的操作。

定义位置（Definition）：sqe.h:163。

符号定位：[RTIO_OP_I2C_RECOVER](../rtio_model_reference/P009_RTIO操作码.md#ga3b4f9b1ee1612290323161ecc16e0859)。

### `RTIO_OP_TINY_TX`

```c
#define RTIO_OP_TINY_TX
```

通过复制待写数据执行微量写入（Tiny Write）的发送操作。

定义位置（Definition）：sqe.h:151。

符号定位：[RTIO_OP_TINY_TX](../rtio_model_reference/P009_RTIO操作码.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)。

### `RTIO_OP_TX`

```c
#define RTIO_OP_TX
```

执行发送（写入）的操作。

定义位置（Definition）：sqe.h:148。

符号定位：[RTIO_OP_TX](../rtio_model_reference/P009_RTIO操作码.md#ga8dcaef0cda159e16520a95543ff62827)。

### `RTIO_OP_TXRX`

```c
#define RTIO_OP_TXRX
```

执行收发（Transceive），即同时读取和写入的操作。

定义位置（Definition）：sqe.h:157。

符号定位：[RTIO_OP_TXRX](../rtio_model_reference/P009_RTIO操作码.md#ga9f0e70f5a28be65a8ed67c0257a72692)。

### `RTIO_OP_NOP`

```c
#define RTIO_OP_NOP
```

不执行任何动作并立即完成的操作。

定义位置（Definition）：sqe.h:142。

符号定位：[RTIO_OP_NOP](../rtio_model_reference/P009_RTIO操作码.md#gad5f073978f641413989d1c6b405d6c36)。

### `RTIO_OP_AWAIT`

```c
#define RTIO_OP_AWAIT
```

等待信号的操作；如果提供了IODEV，则在等待期间阻塞该IODEV。

定义位置（Definition）：sqe.h:178。

符号定位：[RTIO_OP_AWAIT](../rtio_model_reference/P009_RTIO操作码.md#gad74290935595b83040676b426cd07161)。

### `RTIO_OP_I2C_CONFIGURE`

```c
#define RTIO_OP_I2C_CONFIGURE
```

配置I2C总线的操作。

定义位置（Definition）：sqe.h:166。

符号定位：[RTIO_OP_I2C_CONFIGURE](../rtio_model_reference/P009_RTIO操作码.md#gad987be3acfe406b11419c7e8cd068cf5)。

### `RTIO_OP_DELAY`

```c
#define RTIO_OP_DELAY
```

异步等待指定时长后才完成的操作。

定义位置（Definition）：sqe.h:160。

符号定位：[RTIO_OP_DELAY](../rtio_model_reference/P009_RTIO操作码.md#gae8da4da54f32963190f52c7533d4c951)。

### `RTIO_OP_RX`

```c
#define RTIO_OP_RX
```

执行接收（读取）的操作。

定义位置（Definition）：sqe.h:145。

符号定位：[RTIO_OP_RX](../rtio_model_reference/P009_RTIO操作码.md#gafeb05c351207cd1638fa78f6607e1a4a)。

### `RTIO_SQE_MULTISHOT`

```c
#define RTIO_SQE_MULTISHOT
```

该SQE应持续产生CQE，直到被取消。

定义位置（Definition）：sqe.h:122。

符号定位：[RTIO_SQE_MULTISHOT](../rtio_model_reference/P010_RTIO提交事件标志.md#ga00f8ead8f043fe40d49d0bc3325fb299)。

### `RTIO_SQE_TRANSACTION`

```c
#define RTIO_SQE_TRANSACTION
```

队列中的下一个请求属于同一事务（Transaction）。

定义位置（Definition）：sqe.h:94。

符号定位：[RTIO_SQE_TRANSACTION](../rtio_model_reference/P010_RTIO提交事件标志.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)。

### `RTIO_SQE_MEMPOOL_BUFFER`

```c
#define RTIO_SQE_MEMPOOL_BUFFER
```

缓冲区应由RTIO内存池分配。

定义位置（Definition）：sqe.h:106。

符号定位：[RTIO_SQE_MEMPOOL_BUFFER](../rtio_model_reference/P010_RTIO提交事件标志.md#ga2802b46584220afffa0e959e149d5a4d)。

### `RTIO_SQE_NO_RESPONSE`

```c
#define RTIO_SQE_NO_RESPONSE
```

该SQE不产生CQE。

定义位置（Definition）：sqe.h:127。

符号定位：[RTIO_SQE_NO_RESPONSE](../rtio_model_reference/P010_RTIO提交事件标志.md#ga8578ffdb8f53a51b94fa86a6f02d4a11)。

### `RTIO_SQE_CHAINED`

```c
#define RTIO_SQE_CHAINED
```

队列中的下一个请求应等待此请求。

定义位置（Definition）：sqe.h:82。

符号定位：[RTIO_SQE_CHAINED](../rtio_model_reference/P010_RTIO提交事件标志.md#gae9191d521d4ab602b53fefb74020d06b)。

### `rtio_sqe_prep_read_with_pool`

```c
static void rtio_sqe_prep_read_with_pool(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

准备一个使用上下文内存池的读操作提交。

定义位置（Definition）：sqe.h:479。

符号定位：[rtio_sqe_prep_read_with_pool](../rtio_core_reference/P001_RTIO公共接口.md#ga15c1f623658d27d300d1a31a6f3d6b9d)。

### `rtio_sqe_prep_i2c_recover`

```c
static void rtio_sqe_prep_i2c_recover(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

准备一个I2C总线恢复操作（Recover Operation）提交。

定义位置（Definition）：sqe.h:727。

符号定位：[rtio_sqe_prep_i2c_recover](../rtio_core_reference/P001_RTIO公共接口.md#ga274cb5490582b38682f255cac4703143)。

### `rtio_sqe_prep_tiny_write`

```c
static void rtio_sqe_prep_tiny_write(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, const uint8_t *tiny_write_data, uint8_t tiny_write_len, void *userdata)
```

准备一个微量写操作（Tiny Write）提交。

定义位置（Definition）：sqe.h:533。

符号定位：[rtio_sqe_prep_tiny_write](../rtio_core_reference/P001_RTIO公共接口.md#ga31be14ece09e061a8d42ca8f2395286a)。

### `rtio_sqe_prep_nop`

```c
static void rtio_sqe_prep_nop(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, void *userdata)
```

准备一个空操作（No Operation，NOP）提交。

定义位置（Definition）：sqe.h:427。

符号定位：[rtio_sqe_prep_nop](../rtio_core_reference/P001_RTIO公共接口.md#ga599ee43fdf35e1cf895cbbe9272e4c50)。

### `rtio_callback_t`

```c
void(* rtio_callback_t)(struct rtio *r, const struct rtio_sqe *sqe, int res, void *arg0)
```

`RTIO_OP_CALLBACK`的回调函数签名（Callback Signature）。

定义位置（Definition）：sqe.h:297。

符号定位：[rtio_callback_t](../rtio_core_reference/P001_RTIO公共接口.md#ga5d5b7d440eab064918424b0261455a9f)。

### `rtio_sqe_prep_await_iodev`

```c
static void rtio_sqe_prep_await_iodev(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

准备一个等待操作提交，该操作会阻塞`rtio_iodev`直至完成。

定义位置（Definition）：sqe.h:653。

符号定位：[rtio_sqe_prep_await_iodev](../rtio_core_reference/P001_RTIO公共接口.md#ga5e55583901cd13d24f60744747c5c72b)。

### `rtio_iodev_sqe_await_signal`

```c
static void rtio_iodev_sqe_await_signal(struct rtio_iodev_sqe *iodev_sqe, rtio_signaled_t callback, void *userdata)
```

从RTIO IODEV等待一个AWAIT SQE信号。

定义位置（Definition）：sqe.h:803。

符号定位：[rtio_iodev_sqe_await_signal](../rtio_core_reference/P001_RTIO公共接口.md#ga7d2e5673582f32b630e2294dfbf0fe44)。

### `rtio_sqe_prep_write`

```c
static void rtio_sqe_prep_write(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, const uint8_t *buf, uint32_t len, void *userdata)
```

准备一个写操作（Write Operation）提交。

定义位置（Definition）：sqe.h:505。

符号定位：[rtio_sqe_prep_write](../rtio_core_reference/P001_RTIO公共接口.md#ga7f7856d1f4fd1d8c4f6eebcccfe77701)。

### `rtio_sqe_prep_read`

```c
static void rtio_sqe_prep_read(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, uint8_t *buf, uint32_t len, void *userdata)
```

准备一个读操作（Read Operation）提交。

定义位置（Definition）：sqe.h:462。

符号定位：[rtio_sqe_prep_read](../rtio_core_reference/P001_RTIO公共接口.md#ga89c7cc2494e3dda50737f78f1a1376cf)。

### `rtio_sqe_prep_read_multishot`

```c
static void rtio_sqe_prep_read_multishot(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

准备一个使用上下文内存池的多次完成读操作（Multishot Read）提交。

定义位置（Definition）：sqe.h:494。

符号定位：[rtio_sqe_prep_read_multishot](../rtio_core_reference/P001_RTIO公共接口.md#ga9803aa829f8c0eeee746ea7d872c20cc)。

### `rtio_sqe_prep_callback`

```c
static void rtio_sqe_prep_callback(struct rtio_sqe *sqe, rtio_callback_t callback, void *arg0, void *userdata)
```

准备一个回调操作（Callback Operation）提交。

定义位置（Definition）：sqe.h:560。

符号定位：[rtio_sqe_prep_callback](../rtio_core_reference/P001_RTIO公共接口.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)。

### `rtio_sqe_prep_await_executor`

```c
static void rtio_sqe_prep_await_executor(struct rtio_sqe *sqe, int8_t prio, void *userdata)
```

准备一个等待操作提交，该操作在收到信号后完成SQE。

定义位置（Definition）：sqe.h:670。

符号定位：[rtio_sqe_prep_await_executor](../rtio_core_reference/P001_RTIO公共接口.md#gaa2f35d2909f4a19003199a3fd759fc41)。

### `rtio_signaled_t`

```c
void(* rtio_signaled_t)(struct rtio_iodev_sqe *iodev_sqe, void *userdata)
```

`RTIO_OP_AWAIT`收到信号时的回调函数签名（Callback Signature）。

定义位置（Definition）：sqe.h:305。

符号定位：[rtio_signaled_t](../rtio_core_reference/P001_RTIO公共接口.md#gab254ffa4d10bfb670bacd1c47c1f8711)。

### `rtio_sqe_prep_transceive`

```c
static void rtio_sqe_prep_transceive(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, const uint8_t *tx_buf, uint8_t *rx_buf, uint32_t buf_len, void *userdata)
```

准备一个收发操作（Transceive Operation）提交。

定义位置（Definition）：sqe.h:596。

符号定位：[rtio_sqe_prep_transceive](../rtio_core_reference/P001_RTIO公共接口.md#gab9b605dcbb01d21c88f9ae70588ea3b5)。

### `rtio_sqe_prep_i2c_configure`

```c
static void rtio_sqe_prep_i2c_configure(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, uint32_t dev_config, void *userdata)
```

准备一个I2C配置操作（Configure Operation）提交。

定义位置（Definition）：sqe.h:712。

符号定位：[rtio_sqe_prep_i2c_configure](../rtio_core_reference/P001_RTIO公共接口.md#gabcb356e1df7b39bbb6f732d6fa6cc97d)。

### `rtio_sqe_prep_delay`

```c
#define rtio_sqe_prep_delay(sqe, timeout, userdata)
```

准备一个延时操作（Delay Operation）提交，在指定超时后完成。

定义位置（Definition）：sqe.h:707。

符号定位：[rtio_sqe_prep_delay](../rtio_core_reference/P001_RTIO公共接口.md#gad45b80544e4e894cf170fe44fb752930)。

### `rtio_chain_next`

```c
static struct rtio_iodev_sqe * rtio_chain_next(const struct rtio_iodev_sqe *iodev_sqe)
```

获取链（Chain）中的下一个SQE。

定义位置（Definition）：sqe.h:768。

符号定位：[rtio_chain_next](../rtio_core_reference/P001_RTIO公共接口.md#gada1e3abf92a46e376138435debc8baf4)。

### `rtio_iodev_sqe_next`

```c
static struct rtio_iodev_sqe * rtio_iodev_sqe_next(const struct rtio_iodev_sqe *iodev_sqe)
```

获取链或事务中的下一个SQE。

定义位置（Definition）：sqe.h:788。

符号定位：[rtio_iodev_sqe_next](../rtio_core_reference/P001_RTIO公共接口.md#gae690e3dc0fc40dda57257b2eed432719)。

### `rtio_sqe_prep_callback_no_cqe`

```c
static void rtio_sqe_prep_callback_no_cqe(struct rtio_sqe *sqe, rtio_callback_t callback, void *arg0, void *userdata)
```

准备一个不产生CQE的回调操作提交。

定义位置（Definition）：sqe.h:584。

符号定位：[rtio_sqe_prep_callback_no_cqe](../rtio_core_reference/P001_RTIO公共接口.md#gae87be354087d038953dae07c7f9cd3b0)。

### `rtio_txn_next`

```c
static struct rtio_iodev_sqe * rtio_txn_next(const struct rtio_iodev_sqe *iodev_sqe)
```

获取事务（Transaction）中的下一个SQE。

定义位置（Definition）：sqe.h:747。

符号定位：[rtio_txn_next](../rtio_core_reference/P001_RTIO公共接口.md#gaef904eb6a8810d8c3ea537c4d6edbee5)。

### `rtio_sqe_prep_await`

```c
static void rtio_sqe_prep_await(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

准备一个等待操作（Await Operation）提交。

定义位置（Definition）：sqe.h:630。

符号定位：[rtio_sqe_prep_await](../rtio_core_reference/P001_RTIO公共接口.md#gafd97c145b8525895494a31a87610f65d)。

### `SYS_PORT_TRACING_FUNC_ENTER`

```c
#define SYS_PORT_TRACING_FUNC_ENTER(type, func,...)
```

用于记录可能返回值或不返回值的函数入口的跟踪宏（Tracing Macro）。

定义位置（Definition）：tracing_macros.h:246。

符号定位：[SYS_PORT_TRACING_FUNC_ENTER](../tracing_core_reference/P004_跟踪包装宏接口.md#ga445bcac4cec53d560ddca757de17e1e3)。

### `SYS_PORT_TRACING_FUNC_EXIT`

```c
#define SYS_PORT_TRACING_FUNC_EXIT(type, func,...)
```

用于记录函数执行结束的跟踪宏。

定义位置（Definition）：tracing_macros.h:272。

符号定位：[SYS_PORT_TRACING_FUNC_EXIT](../tracing_core_reference/P004_跟踪包装宏接口.md#gab0350eef3ed26733e57505ee2d0487cb)。

### `CONTAINER_OF`

```c
#define CONTAINER_OF(ptr, type, field)
```

取得包含指定成员的结构体指针。

定义位置（Definition）：util.h:281。

符号定位：[CONTAINER_OF](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f)。

### `kernel.h`

公共内核API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `mpsc_lockfree.h`

使用单向链表（Singly Linked List）的无等待（Wait-free）侵入式多生产者单消费者队列（Multi-Producer Single-Consumer Queue，MPSC）。

符号定位：[mpsc_lockfree.h](../intercore_reference/P161_MPSC无锁队列头文件参考.md)。

### `stdint.h`

符号定位：[stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `int8_t`

```c
__INT8_TYPE__ int8_t
```

定义位置（Definition）：stdint.h:72。

符号定位：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

### `string.h`

符号定位：[string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)。

### `memset`

```c
void * memset(void *buf, int c, size_t n)
```

符号定位：[memset](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a4137694174d4ca2fad886a1db355015c)。

### `memcpy`

```c
void * memcpy(void *ZRESTRICT d, const void *ZRESTRICT s, size_t n)
```

符号定位：[memcpy](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#af0f01bffcd16daa9143f6014d10a25ad)。

### `k_timeout_t`

内核超时类型（Kernel Timeout Type）。

定义位置（Definition）：clock.h:65。

符号定位：[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

### `k_timepoint_t`

内核时间点类型（Kernel Timepoint Type）。

定义位置（Definition）：clock.h:289。

符号定位：[k_timepoint_t](../timer_reference/P088_内核时间点类型.md)。

### `mpsc_node`

队列成员（Queue Member）。

定义位置（Definition）：mpsc_lockfree.h:79。

符号定位：[mpsc_node](../intercore_reference/P160_MPSC无锁队列节点.md)。

### `rtio_iodev_sqe`

输入输出设备提交队列条目（I/O Device Submission Queue Entry）。

定义位置（Definition）：sqe.h:403。

符号定位：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

### `rtio_iodev_sqe::next`

```c
struct rtio_iodev_sqe * next
```

链（Chain）或事务（Transaction）中的下一个条目；如果当前是最后一个条目，则为`NULL`。

定义位置（Definition）：sqe.h:406。

符号定位：[rtio_iodev_sqe::next](../rtio_model_reference/P005_RTIO设备提交条目.md#a2afb82e550e614f87db7cd1bf2c3a352)。

### `rtio_iodev_sqe::sqe`

```c
struct rtio_sqe sqe
```

此条目携带的提交。

定义位置（Definition）：sqe.h:404。

符号定位：[rtio_iodev_sqe::sqe](../rtio_model_reference/P005_RTIO设备提交条目.md#a2bd98599678909c0ddb22f879affa12b)。

### `rtio_iodev_sqe::r`

```c
struct rtio * r
```

该提交所属的RTIO上下文。

定义位置（Definition）：sqe.h:407。

符号定位：[rtio_iodev_sqe::r](../rtio_model_reference/P005_RTIO设备提交条目.md#a3c3a050793589258eab5ff5ac30f24c8)。

### `rtio_iodev_sqe::q`

```c
struct mpsc_node q
```

用于将此条目入队的链接。

定义位置（Definition）：sqe.h:405。

符号定位：[rtio_iodev_sqe::q](../rtio_model_reference/P005_RTIO设备提交条目.md#a9cfdd004b65a5e2bc111bc2fb333498c)。

### `rtio_iodev`

具有请求提交函数表（Function Table）的输入输出设备（I/O Device）。

定义位置（Definition）：iodev.h:49。

符号定位：[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)。

### `rtio_sqe`

一个提交队列事件（Submission Queue Event，SQE）。

定义位置（Definition）：sqe.h:310。

符号定位：[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

### `rtio_sqe::i2c_config`

```c
uint32_t i2c_config
```

`OP_I2C_CONFIGURE`，即I2C配置操作。

定义位置（Definition）：sqe.h:373。

符号定位：[rtio_sqe::i2c_config](../rtio_model_reference/P007_RTIO提交事件.md#a07bf344b1b1063b8bea80cf5ba1c1cc5)。

### `rtio_sqe::userdata`

```c
void * userdata
```

用户提供的数据，在操作完成时返回。

定义位置（Definition）：sqe.h:328。

符号定位：[rtio_sqe::userdata](../rtio_model_reference/P007_RTIO提交事件.md#a0ed519ee0b5867ff73bdaf37f983c971)。

### `rtio_sqe::tx_buf`

```c
const uint8_t * tx_buf
```

写操作的数据来源缓冲区。

定义位置（Definition）：sqe.h:360。

符号定位：[rtio_sqe::tx_buf](../rtio_model_reference/P007_RTIO提交事件.md#a18bfa63542954f4bb8b924c92c48e931)。

### `rtio_sqe::op`

```c
uint8_t op
```

操作码（Operation Code）。

定义位置（Definition）：sqe.h:311。

符号定位：[rtio_sqe::op](../rtio_model_reference/P007_RTIO提交事件.md#a1d8d3e3426e47a2c7f54d98f51acd953)。

### `rtio_sqe::rx`

```c
struct rtio_sqe::@126267262255374054123217063150244034155174062054::@222067021034074304061254367152327164076222165070 rx
```

`OP_RX`接收操作。

符号定位：[rtio_sqe::rx](../rtio_model_reference/P007_RTIO提交事件.md#a29e0c1b06b6f7b604af147a231b46319)。

### `rtio_sqe::tiny_tx`

```c
struct rtio_sqe::@126267262255374054123217063150244034155174062054::@036347012270137154075057170156115300365157200061 tiny_tx
```

`OP_TINY_TX`微量发送操作。

符号定位：[rtio_sqe::tiny_tx](../rtio_model_reference/P007_RTIO提交事件.md#a2b73e59283f6dc79cef3c804ed973160)。

### `rtio_sqe::arg0`

```c
void * arg0
```

传给回调的最后一个参数。

定义位置（Definition）：sqe.h:354。

符号定位：[rtio_sqe::arg0](../rtio_model_reference/P007_RTIO提交事件.md#a438d2156a61aef9ca840af9c01d5dfa4)。

### `rtio_sqe::rx_buf`

```c
uint8_t * rx_buf
```

读操作的数据目标缓冲区。

定义位置（Definition）：sqe.h:361。

符号定位：[rtio_sqe::rx_buf](../rtio_model_reference/P007_RTIO提交事件.md#a4d2090fc11b897724a883ad1087d9f73)。

### `rtio_sqe::prio`

```c
uint8_t prio
```

操作优先级（Operation Priority）。

定义位置（Definition）：sqe.h:313。

符号定位：[rtio_sqe::prio](../rtio_model_reference/P007_RTIO提交事件.md#a528eb9b721be7b8a8898ab16a7e2d9a7)。

### `rtio_sqe::await`

```c
struct rtio_sqe::@126267262255374054123217063150244034155174062054::@236333123355174166163204241333175337261032350217 await
```

`OP_AWAIT`等待操作。

符号定位：[rtio_sqe::await](../rtio_model_reference/P007_RTIO提交事件.md#a64f5db04d58882832f86477628c25be3)。

### `rtio_sqe::buf_len`

```c
uint32_t buf_len
```

缓冲区长度。

定义位置（Definition）：sqe.h:335。

符号定位：[rtio_sqe::buf_len](../rtio_model_reference/P007_RTIO提交事件.md#a67376f40a13960b152a23da250275722)。

### `rtio_sqe::iodev`

```c
const struct rtio_iodev * iodev
```

要在其上执行操作的设备。

定义位置（Definition）：sqe.h:319。

符号定位：[rtio_sqe::iodev](../rtio_model_reference/P007_RTIO提交事件.md#a6c784702f011592c84feacd57915bbfc)。

### `rtio_sqe::iodev_flags`

```c
uint32_t iodev_flags
```

操作的IODEV标志。

定义位置（Definition）：sqe.h:317。

符号定位：[rtio_sqe::iodev_flags](../rtio_model_reference/P007_RTIO提交事件.md#a8bebe5d55aa8549d749466e444fadf91)。

### `rtio_sqe::ccc_payload`

```c
void * ccc_payload
```

`OP_I3C_CCC`，即I3C公共命令码（Common Command Code，CCC）操作。

定义位置（Definition）：sqe.h:384。

符号定位：[rtio_sqe::ccc_payload](../rtio_model_reference/P007_RTIO提交事件.md#a8d78973983abca8b97cfc5bcdc2dd2f1)。

### `rtio_sqe::txrx`

```c
struct rtio_sqe::@126267262255374054123217063150244034155174062054::@366052340324346171254040100167341103343101366005 txrx
```

`OP_TXRX`收发操作。

符号定位：[rtio_sqe::txrx](../rtio_model_reference/P007_RTIO提交事件.md#a927a43f86f65484179c8113caa775c9c)。

### `rtio_sqe::type`

```c
int type
```

配置类型，为`enum i3c_config_type`中的一个值。

定义位置（Definition）：sqe.h:378。

符号定位：[rtio_sqe::type](../rtio_model_reference/P007_RTIO提交事件.md#aa09a0c93a6e8cfc73278a87942e4af33)。

### `rtio_sqe::flags`

```c
uint16_t flags
```

操作标志（Operation Flags）。

定义位置（Definition）：sqe.h:315。

符号定位：[rtio_sqe::flags](../rtio_model_reference/P007_RTIO提交事件.md#aad2ff8524df0e24b812e77e2393bf5b0)。

### `rtio_sqe::buf`

```c
const uint8_t * buf
```

写操作的数据来源缓冲区。

定义位置（Definition）：sqe.h:336。

符号定位：[rtio_sqe::buf](../rtio_model_reference/P007_RTIO提交事件.md#ab71176c084e8b8eb65dfeb3018ae2a49)。

### `rtio_sqe::config`

```c
void * config
```

要应用的配置。

定义位置（Definition）：sqe.h:379。

符号定位：[rtio_sqe::config](../rtio_model_reference/P007_RTIO提交事件.md#ac07a16c50a067acc90bd4ab08aae4184)。

### `rtio_sqe::tx`

```c
struct rtio_sqe::@126267262255374054123217063150244034155174062054::@344335000264002157174077227357232142206143107046 tx
```

`OP_TX`发送操作。

符号定位：[rtio_sqe::tx](../rtio_model_reference/P007_RTIO提交事件.md#af1bd1edaaf32a58fb0461c989ac2a456)。

### `rtio_sqe::callback`

```c
rtio_callback_t callback
```

要运行的函数。

定义位置（Definition）：sqe.h:353。

符号定位：[rtio_sqe::callback](../rtio_model_reference/P007_RTIO提交事件.md#af8c31c33e9fedebe55cac73595d0f696)。

### `rtio`

一个RTIO上下文（Context），其内容可以视为一对队列。

定义位置（Definition）：rtio.h:83。

符号定位：[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

### `util.h`

杂项工具（Miscellaneous Utilities）。

符号定位：[util.h](../util_reference/P002_通用工具头文件参考.md)。

## 2.4\_源码跟踪译注

> 译注——准备（Prepare）与提交（Submit）分开：prep函数只设置SQE，不启动硬件。多数准备函数直接或通过共同辅助函数先memset清零整个公开SQE，再写操作字段；因此CHAINED、TRANSACTION和总线iodev_flags等附加标志应在准备之后按需要设置，不能先设置再假定prep会保留。参考[核心接口](../rtio_core_reference/P001_RTIO公共接口.md)和[SQE结构](../rtio_model_reference/P007_RTIO提交事件.md)。

> 译注——普通读写及收发准备函数只保存缓冲区指针，内存必须在异步使用期间有效。微量写（Tiny Write）通过memcpy复制到本次为7字节的内嵌数组中；长度和非空检查使用断言，不是返回错误码的运行时校验。不能因为关闭断言就传入越界长度或无效指针。

> 译注——内存池读准备函数先保存NULL缓冲区和0长度，再设置MEMPOOL_BUFFER；并非准备完成就已经取得内存块。多次完成读（Multishot Read）另外设置MULTISHOT，后续分配、重提与错误清理由驱动、核心辅助函数和执行器完成。

> 译注——回调（Callback）准备函数把iodev设为NULL，交给执行器执行。no_cqe变体额外设置NO_RESPONSE，避免完成回调本身再产生一个CQE；此标志也影响提交等待时能收到的完成事件数量。用户模式支持范围另由系统调用校验限制，不能把任意内核回调地址提交为用户操作。

> 译注——AWAIT准备函数清零状态；注册等待回调与发送信号分别尝试0→1的原子比较并交换（CAS），后到的一方调用回调。它不是累计任意多次通知的计数器，重复发信号或在SQE回收后继续使用句柄不在此前提内。提供IODEV时是否正确保持总线阻塞仍由该设备驱动负责。

> 译注——DELAY启用时，同名准备函数保存timeout并指向共享rtio_timeout_iodev；禁用时宏分支触发BUILD_ASSERT。共享超时实现从IODEV接收提交时计算到期点，不能把准备时刻当作延时起点。

> 译注——`rtio_txn_next()`和`rtio_chain_next()`先检查当前SQE对应标志再返回next；`rtio_iodev_sqe_next()`直接返回next。原接口说明中前两者的返回类型写作rtio_sqe*，当前声明实际为rtio_iodev_sqe*。链与事务链接由执行器建立，不能对尚未链接的孤立SQE假定next有效。

> 译注——SQE对象池分配只取出空闲节点并减少pool_free，不在这个内部函数中清零整个对象；公开prep函数负责设置操作字段。对象回收后旧指针不可继续代表原请求。对象池宏仅建立存储及元数据，启动时的rtio_init()把各节点加入空闲队列。

> 译注——缓存行注释提到常见64字节，但当前检查由CONFIG_RTIO_SQE_CACHELINE_CHECK控制，比较的是sizeof(struct rtio_iodev_sqe)；若定义CONFIG_DCACHE_LINE_SIZE则使用该值，否则回退到64。断言条件为小于等于，并不证明所有构建中条目恰为64字节。SQE内存放置选项也不等同于任意数据缓冲区自动满足DMA或缓存一致性要求。

> 译注——源码中的操作优先级字段是uint8_t，而部分准备函数参数使用int8_t，本页原样保留声明；不要擅自改成另一套接口。操作优先级是否用于仲裁由驱动决定，不能与线程优先级混同。I2C／I3C设备标志位于iodev_flags，不能与SQE的链、事务或内存池标志相互替代。

头文件相对定位：[include/zephyr/rtio/sqe.h](../../../include/zephyr/rtio/sqe.h)，关联实现／接口：[subsys/rtio/rtio_executor.c](../../../subsys/rtio/rtio_executor.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/rtio/sqe.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/rtio/rtio_executor.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_RTIO提交事件头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/mpsc_lockfree.h](../intercore_reference/P161_MPSC无锁队列头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [rtio_callback_t](../rtio_core_reference/P001_RTIO公共接口.md#ga5d5b7d440eab064918424b0261455a9f)
- [arg0](../rtio_model_reference/P007_RTIO提交事件.md#a438d2156a61aef9ca840af9c01d5dfa4)
- [rtio_signaled_t](../rtio_core_reference/P001_RTIO公共接口.md#gab254ffa4d10bfb670bacd1c47c1f8711)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [op](../rtio_model_reference/P007_RTIO提交事件.md#a1d8d3e3426e47a2c7f54d98f51acd953)
- [prio](../rtio_model_reference/P007_RTIO提交事件.md#a528eb9b721be7b8a8898ab16a7e2d9a7)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [flags](../rtio_model_reference/P007_RTIO提交事件.md#aad2ff8524df0e24b812e77e2393bf5b0)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [iodev_flags](../rtio_model_reference/P007_RTIO提交事件.md#a8bebe5d55aa8549d749466e444fadf91)
- [iodev](../rtio_model_reference/P007_RTIO提交事件.md#a6c784702f011592c84feacd57915bbfc)
- [userdata](../rtio_model_reference/P007_RTIO提交事件.md#a0ed519ee0b5867ff73bdaf37f983c971)
- [buf_len](../rtio_model_reference/P007_RTIO提交事件.md#a67376f40a13960b152a23da250275722)
- [buf](../rtio_model_reference/P007_RTIO提交事件.md#ab71176c084e8b8eb65dfeb3018ae2a49)
- [callback](../rtio_model_reference/P007_RTIO提交事件.md#af8c31c33e9fedebe55cac73595d0f696)
- [tx_buf](../rtio_model_reference/P007_RTIO提交事件.md#a18bfa63542954f4bb8b924c92c48e931)
- [rx_buf](../rtio_model_reference/P007_RTIO提交事件.md#a4d2090fc11b897724a883ad1087d9f73)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [k_timepoint_t](../timer_reference/P088_内核时间点类型.md)
- [i2c_config](../rtio_model_reference/P007_RTIO提交事件.md#a07bf344b1b1063b8bea80cf5ba1c1cc5)
- [type](../rtio_model_reference/P007_RTIO提交事件.md#aa09a0c93a6e8cfc73278a87942e4af33)
- [config](../rtio_model_reference/P007_RTIO提交事件.md#ac07a16c50a067acc90bd4ab08aae4184)
- [ccc_payload](../rtio_model_reference/P007_RTIO提交事件.md#a8d78973983abca8b97cfc5bcdc2dd2f1)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [sqe](../rtio_model_reference/P005_RTIO设备提交条目.md#a2bd98599678909c0ddb22f879affa12b)
- [mpsc_node](../intercore_reference/P160_MPSC无锁队列节点.md)
- [q](../rtio_model_reference/P005_RTIO设备提交条目.md#a9cfdd004b65a5e2bc111bc2fb333498c)
- [next](../rtio_model_reference/P005_RTIO设备提交条目.md#a2afb82e550e614f87db7cd1bf2c3a352)
- [r](../rtio_model_reference/P005_RTIO设备提交条目.md#a3c3a050793589258eab5ff5ac30f24c8)
- [rtio_sqe_prep_nop](../rtio_core_reference/P001_RTIO公共接口.md#ga599ee43fdf35e1cf895cbbe9272e4c50)
- [memset](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a4137694174d4ca2fad886a1db355015c)
- [RTIO_OP_NOP](../rtio_model_reference/P009_RTIO操作码.md#gad5f073978f641413989d1c6b405d6c36)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [RTIO_OP_RX](../rtio_model_reference/P009_RTIO操作码.md#gafeb05c351207cd1638fa78f6607e1a4a)
- [rx](../rtio_model_reference/P007_RTIO提交事件.md#a29e0c1b06b6f7b604af147a231b46319)
- [rtio_sqe_prep_read](../rtio_core_reference/P001_RTIO公共接口.md#ga89c7cc2494e3dda50737f78f1a1376cf)
- [rtio_sqe_prep_read_with_pool](../rtio_core_reference/P001_RTIO公共接口.md#ga15c1f623658d27d300d1a31a6f3d6b9d)
- [RTIO_SQE_MEMPOOL_BUFFER](../rtio_model_reference/P010_RTIO提交事件标志.md#ga2802b46584220afffa0e959e149d5a4d)
- [rtio_sqe_prep_read_multishot](../rtio_core_reference/P001_RTIO公共接口.md#ga9803aa829f8c0eeee746ea7d872c20cc)
- [RTIO_SQE_MULTISHOT](../rtio_model_reference/P010_RTIO提交事件标志.md#ga00f8ead8f043fe40d49d0bc3325fb299)
- [rtio_sqe_prep_write](../rtio_core_reference/P001_RTIO公共接口.md#ga7f7856d1f4fd1d8c4f6eebcccfe77701)
- [RTIO_OP_TX](../rtio_model_reference/P009_RTIO操作码.md#ga8dcaef0cda159e16520a95543ff62827)
- [tx](../rtio_model_reference/P007_RTIO提交事件.md#af1bd1edaaf32a58fb0461c989ac2a456)
- [rtio_sqe_prep_tiny_write](../rtio_core_reference/P001_RTIO公共接口.md#ga31be14ece09e061a8d42ca8f2395286a)
- [tiny_tx](../rtio_model_reference/P007_RTIO提交事件.md#a2b73e59283f6dc79cef3c804ed973160)
- [RTIO_OP_TINY_TX](../rtio_model_reference/P009_RTIO操作码.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)
- [memcpy](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#af0f01bffcd16daa9143f6014d10a25ad)
- [rtio_sqe_prep_callback](../rtio_core_reference/P001_RTIO公共接口.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)
- [RTIO_OP_CALLBACK](../rtio_model_reference/P009_RTIO操作码.md#ga18e0ff7d44e4c33900106aefad0a8508)
- [rtio_sqe_prep_callback_no_cqe](../rtio_core_reference/P001_RTIO公共接口.md#gae87be354087d038953dae07c7f9cd3b0)
- [RTIO_SQE_NO_RESPONSE](../rtio_model_reference/P010_RTIO提交事件标志.md#ga8578ffdb8f53a51b94fa86a6f02d4a11)
- [rtio_sqe_prep_transceive](../rtio_core_reference/P001_RTIO公共接口.md#gab9b605dcbb01d21c88f9ae70588ea3b5)
- [RTIO_OP_TXRX](../rtio_model_reference/P009_RTIO操作码.md#ga9f0e70f5a28be65a8ed67c0257a72692)
- [txrx](../rtio_model_reference/P007_RTIO提交事件.md#a927a43f86f65484179c8113caa775c9c)
- [rtio_sqe_prep_await](../rtio_core_reference/P001_RTIO公共接口.md#gafd97c145b8525895494a31a87610f65d)
- [RTIO_OP_AWAIT](../rtio_model_reference/P009_RTIO操作码.md#gad74290935595b83040676b426cd07161)
- [rtio_sqe_prep_await_iodev](../rtio_core_reference/P001_RTIO公共接口.md#ga5e55583901cd13d24f60744747c5c72b)
- [rtio_sqe_prep_await_executor](../rtio_core_reference/P001_RTIO公共接口.md#gaa2f35d2909f4a19003199a3fd759fc41)
- [rtio_sqe_prep_delay](../rtio_core_reference/P001_RTIO公共接口.md#gad45b80544e4e894cf170fe44fb752930)
- [RTIO_OP_DELAY](../rtio_model_reference/P009_RTIO操作码.md#gae8da4da54f32963190f52c7533d4c951)
- [rtio_sqe_prep_i2c_configure](../rtio_core_reference/P001_RTIO公共接口.md#gabcb356e1df7b39bbb6f732d6fa6cc97d)
- [RTIO_OP_I2C_CONFIGURE](../rtio_model_reference/P009_RTIO操作码.md#gad987be3acfe406b11419c7e8cd068cf5)
- [rtio_sqe_prep_i2c_recover](../rtio_core_reference/P001_RTIO公共接口.md#ga274cb5490582b38682f255cac4703143)
- [RTIO_OP_I2C_RECOVER](../rtio_model_reference/P009_RTIO操作码.md#ga3b4f9b1ee1612290323161ecc16e0859)
- [rtio_txn_next](../rtio_core_reference/P001_RTIO公共接口.md#gaef904eb6a8810d8c3ea537c4d6edbee5)
- [SYS_PORT_TRACING_FUNC_ENTER](../tracing_core_reference/P004_跟踪包装宏接口.md#ga445bcac4cec53d560ddca757de17e1e3)
- [RTIO_SQE_TRANSACTION](../rtio_model_reference/P010_RTIO提交事件标志.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)
- [SYS_PORT_TRACING_FUNC_EXIT](../tracing_core_reference/P004_跟踪包装宏接口.md#gab0350eef3ed26733e57505ee2d0487cb)
- [rtio_chain_next](../rtio_core_reference/P001_RTIO公共接口.md#gada1e3abf92a46e376138435debc8baf4)
- [RTIO_SQE_CHAINED](../rtio_model_reference/P010_RTIO提交事件标志.md#gae9191d521d4ab602b53fefb74020d06b)
- [rtio_iodev_sqe_next](../rtio_core_reference/P001_RTIO公共接口.md#gae690e3dc0fc40dda57257b2eed432719)
- [rtio_iodev_sqe_await_signal](../rtio_core_reference/P001_RTIO公共接口.md#ga7d2e5673582f32b630e2294dfbf0fe44)
- [await](../rtio_model_reference/P007_RTIO提交事件.md#a64f5db04d58882832f86477628c25be3)
- [atomic_cas](../atomic_reference/P001_原子操作公共接口.md#gab879da5aa1ffcc317adc664c016586f7)
- [mpsc_pop](../intercore_reference/P158_MPSC无锁队列接口.md#ga823ec37b84ac43e46167aac954bce9d7)
- [CONTAINER_OF](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f)
- [mpsc_push](../intercore_reference/P158_MPSC无锁队列接口.md#ga403add133841ef88e10d74141e782b37)

---

[上一章](P001_RTIO提交事件头文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_RTIO完成事件头文件参考.md)
