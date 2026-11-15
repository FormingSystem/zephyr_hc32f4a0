---
id: learning.zephyr-docs.api-source-configuration-reference.page-72
title: pulse_io.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_pulse\_io.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h.html)。

## 72.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
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
<a id="l00053"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="foldopen00112"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="foldopen00236"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="foldopen00253"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="foldopen00272"></a>
<a id="l00272"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00301"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00434"></a>
<a id="foldopen00440"></a>
<a id="l00440"></a>
<a id="l00442"></a>
<a id="l00444"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00467"></a>
<a id="l00478"></a>
<a id="foldopen00482"></a>
<a id="l00482"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="foldopen00495"></a>
<a id="l00495"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00573"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__pulse__io__interface_html_ga05add5c7dc934ad84ddafbfe4c08d2a6"></a>
<a id="agroup__pulse__io__interface_html_ga0a0eb57e852853da9c3ba1e262991091"></a>
<a id="agroup__pulse__io__interface_html_ga1188071d39a4018b719f18d019ba6f89"></a>
<a id="agroup__pulse__io__interface_html_ga1d122c085430f9d4408564b76dee0944"></a>
<a id="agroup__pulse__io__interface_html_ga382adc1d7095dba8dd087c47c551436c"></a>
<a id="agroup__pulse__io__interface_html_ga3d92ae937058d0675dd56b009aa1138f"></a>
<a id="agroup__pulse__io__interface_html_ga3e03e72bb73c8949c222d48f28c03612"></a>
<a id="agroup__pulse__io__interface_html_ga8810dd66d863919cf3ea03ae27da4cf7"></a>
<a id="agroup__pulse__io__interface_html_ga8a69608ee00587642aca6e0d69878b07"></a>
<a id="agroup__pulse__io__interface_html_gaa3a5b31cb44647823aa60af4416e6d3f"></a>
<a id="agroup__pulse__io__interface_html_gaca42826a8404d4e5e1eacefc5f17debf"></a>
<a id="agroup__pulse__io__interface_html_gaf925af6fa08b119550e51024c5ebc408"></a>
<a id="agroup__pulse__io__interface_html_gafcce0615be70ca39c346df4c260f09d2"></a>
<a id="agroup__pulse__io__interface_html_gga1188071d39a4018b719f18d019ba6f89ab41397616fbd4b428db60bc6d665186a"></a>
<a id="agroup__pulse__io__interface_html_gga1188071d39a4018b719f18d019ba6f89ad4c6756a1f8972376620492ab1943ee3"></a>
<a id="agroup__pulse__io__interface_html_gga8a69608ee00587642aca6e0d69878b07a72babf2ca6b039635cb177be4f2e5e19"></a>
<a id="agroup__pulse__io__interface_html_gga8a69608ee00587642aca6e0d69878b07ae89d6f0f750e30719501cf32fbe2b220"></a>
<a id="agroup__rtio_html_gaada07aa6acefa548743b525225fa482f"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="akernel_8h_html"></a>
<a id="artio_2rtio_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructpulse__cell_html"></a>
<a id="astructpulse__cell_html_a884c5d0305517a2b4914351cb371b231"></a>
<a id="astructpulse__cell_html_ac205607e071a653d65aed9d7beba2606"></a>
<a id="astructpulse__cell_html_adae24acc734855ddfdb7c0ed340f8ebb"></a>
<a id="astructpulse__io__bit__template_html"></a>
<a id="astructpulse__io__bit__template_html_a32b1f8e31bc606180dac02beee6b3c74"></a>
<a id="astructpulse__io__bit__template_html_ab57882bf17ca354573f2e0bab95009fc"></a>
<a id="astructpulse__io__bit__template_html_af5cf7de078f5a298afe49a64680ee0d0"></a>
<a id="astructpulse__io__caps_html"></a>
<a id="astructpulse__io__caps_html_a16fa91b3ccba69c11ebc826eeb29245d"></a>
<a id="astructpulse__io__caps_html_a173fa1c857ed24a2ecb5f9de8527136b"></a>
<a id="astructpulse__io__caps_html_a1de73e3e72e07bc99d09808402d17b61"></a>
<a id="astructpulse__io__caps_html_a2084a3bd36ed5c131d898edfbcdfba0a"></a>
<a id="astructpulse__io__caps_html_a219331ae467da4a2583d4d905bbac05b"></a>
<a id="astructpulse__io__caps_html_a2ee6e5254c8f3bf474c9c49745d8c377"></a>
<a id="astructpulse__io__caps_html_a3b0e9052d24dbc55e53b2f0d9ceda0cf"></a>
<a id="astructpulse__io__caps_html_a4da263bc4a355448249400ad364f87b9"></a>
<a id="astructpulse__io__caps_html_a5da774fe623fd1f35cbf2e54671399d6"></a>
<a id="astructpulse__io__caps_html_a6300be8f6722fd166d33849df9c031aa"></a>
<a id="astructpulse__io__caps_html_a64cf12b881eab0f538536c34d3273c14"></a>
<a id="astructpulse__io__caps_html_a92a922e8a11823ad0ba733a2ee88cf0d"></a>
<a id="astructpulse__io__caps_html_a986f4a6419df94ce618b0d05ee876276"></a>
<a id="astructpulse__io__caps_html_aa91e3a0fe7e1fd95c89a2436558467eb"></a>
<a id="astructpulse__io__caps_html_aad176fbf3bf21edc3b45a89be128002d"></a>
<a id="astructpulse__io__caps_html_ab8b1aa9fea93cd697bcc760214f12760"></a>
<a id="astructpulse__io__caps_html_acb4396add794dda4933f9c176d1766be"></a>
<a id="astructpulse__io__caps_html_ad85c4a8652bbf80da429c87bbcb680c6"></a>
<a id="astructpulse__io__caps_html_adfa8d33306657b2870d3b5df8a4dce04"></a>
<a id="astructpulse__io__caps_html_aead2efb6f8fe2955d2d9b188cd9264eb"></a>
<a id="astructpulse__io__caps_html_af6dee58bfc47780ccc77092777080ce8"></a>
<a id="astructpulse__io__caps_html_afc8e349e152b2a271b51a2810eab2586"></a>
<a id="astructpulse__io__config_html"></a>
<a id="astructpulse__io__config_html_a09ab3fcf00e4bab33f290695d045d9ce"></a>
<a id="astructpulse__io__config_html_a0c10cf29df1143a842fdde9cf1d49a42"></a>
<a id="astructpulse__io__config_html_a0d74c4cf0960039675f3806870c68a2c"></a>
<a id="astructpulse__io__config_html_a106d88a37daf50fd704a33e6fc49054a"></a>
<a id="astructpulse__io__config_html_a3f378f0c755b40de97c9c601f413b91f"></a>
<a id="astructpulse__io__config_html_a65c6a04405648635c9fea5ac47cf5063"></a>
<a id="astructpulse__io__config_html_a7466b1968e22a84f4542d0be6ee65304"></a>
<a id="astructpulse__io__config_html_aa0f9d3365b77ff5d80c6f9ec222ff5ff"></a>
<a id="astructpulse__io__config_html_adeee7ddbc94ba628916ac3a6b029d337"></a>
<a id="astructpulse__io__config_html_ae767da3eb5f3d4d516262c84972d261f"></a>
<a id="astructpulse__io__config_html_aef4876ae134c3aa2b1634ac6892f7c5e"></a>
<a id="astructpulse__io__decoder__api_html"></a>
<a id="astructpulse__io__decoder__api_html_a3898c1fec9586b45606c9071ddba21a5"></a>
<a id="astructpulse__io__driver__api_html"></a>
<a id="astructpulse__io__driver__api_html_a1e5d2a7e7aa0a44d4b8cc106c22242e9"></a>
<a id="astructpulse__io__driver__api_html_a27dab2f1794e29d51ff613af6d85b0ee"></a>
<a id="astructpulse__io__driver__api_html_a42d3e7109cab1333e12ba4da57eac80c"></a>
<a id="astructpulse__io__driver__api_html_a5c621cc969cddc1af5698616a3809994"></a>
<a id="astructpulse__io__driver__api_html_a6a3d4ba7f6da3ffdc79f9bc30cbc4429"></a>
<a id="astructpulse__io__driver__api_html_a9aa7510ea5c1aab6b490dd3b6b1a4bbc"></a>
<a id="astructpulse__io__driver__api_html_a9aeb9a2a707d8a3c2fe81d064e59c320"></a>
<a id="astructpulse__io__driver__api_html_adbfd779fcbcecce8af577256c38cf941"></a>
<a id="astructpulse__io__driver__api_html_aee848f0d513e8fe1573cf1e8f5c480a4"></a>
<a id="astructpulse__io__driver__api_html_afba3d4238934be36aa5a27c20160df5f"></a>
<a id="astructpulse__io__encoder__api_html"></a>
<a id="astructpulse__io__encoder__api_html_ab5d90fd2dc5832a0f9d48078b1d1193c"></a>
<a id="astructpulse__io__rx__req_html"></a>
<a id="astructpulse__io__rx__req_html_a3412f6080ba7eaecaf1d4b532b77451a"></a>
<a id="astructpulse__io__rx__req_html_a5847bb48236f6d665b176daf72cdee6e"></a>
<a id="astructpulse__io__rx__req_html_a70ae274b716278583e655e2457577f58"></a>
<a id="astructpulse__io__tx__req_html"></a>
<a id="astructpulse__io__tx__req_html_a21426e72b2eaab937e86d50e46177505"></a>
<a id="astructpulse__io__tx__req_html_a33af6b148afa43e93d1b8826d78198d7"></a>
<a id="astructpulse__io__tx__req_html_a39ba9d615f8b40f117bd3efc97bdacd7"></a>
<a id="astructpulse__io__tx__req_html_a39ecb966484761d419c10cd41ae15512"></a>
<a id="astructpulse__symbol_html"></a>
<a id="astructpulse__symbol_html_aa164a0e6915c09bf376739ea724bf3e5"></a>
<a id="astructpulse__symbol_html_abcebf0eaf2ca01ab0144b23153b024fc"></a>
<a id="astructrtio__iodev__sqe_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_PULSE_IO_H_
#define ZEPHYR_INCLUDE_DRIVERS_PULSE_IO_H_


#include <errno.h>
#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/rtio/rtio.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif


enum pulse_io_mode {
        PULSE_IO_MODE_SYMBOL = BIT(0),
        PULSE_IO_MODE_CELL = BIT(1),
};

enum pulse_io_dir {
        PULSE_IO_DIR_TX,
        PULSE_IO_DIR_RX,
};

struct pulse_symbol {
        uint32_t duration: 31;
        uint32_t level: 1;
};

struct pulse_cell {
        uint16_t duty;
        uint16_t level: 1;
        uint16_t rsvd: 15;
};

struct pulse_io_caps {
        /* Fields are ordered widest-first to pack without padding holes. */

        size_t tx_min_chunk_symbols;
        size_t tx_max_streaming;

        uint32_t modes;
        uint32_t min_tick_ns;
        uint32_t max_tick_ns;
        uint32_t max_duration_ticks;
        uint32_t tx_loop_max;
        uint32_t rx_idle_threshold_max;
        uint32_t rx_filter_max_ticks;

        uint32_t tx_channel_mask;
        uint32_t rx_channel_mask;

        uint8_t cell_duty_bits;
        uint8_t num_channels;

        bool supports_tx;
        bool supports_rx;
        bool tx_carrier;
        bool tx_loop_auto_stop;
        bool tx_sync_multi_channel;
        bool rx_carrier_demod;
        bool rx_dma_buffered;
        bool rx_streaming;
        bool cell_period_per_chunk;
};

struct pulse_io_config {
        /* Fields are ordered widest-first to pack without padding holes. */

        uint32_t resolution_hz;
        uint32_t cell_period_ticks;
        uint32_t carrier_hz;
        uint32_t rx_idle_threshold_ticks;
        uint32_t rx_filter_ticks;

        enum pulse_io_mode mode;
        enum pulse_io_dir dir;

        uint8_t carrier_duty_pct;

        bool idle_high;
        bool carrier_en;
        bool rx_carrier_demod;
};

struct pulse_io_channel;

/* Forward declarations for the RTIO codec vtables (defined below). */
struct pulse_io_encoder_api;
struct pulse_io_decoder_api;

struct pulse_io_tx_req {
        union {
                const struct pulse_symbol *symbols;
                const struct pulse_cell *cells;
        };
        size_t count;
        uint32_t loop_count;
};

struct pulse_io_rx_req {
        union {
                struct pulse_symbol *symbols;
                struct pulse_cell *cells;
        };
        size_t capacity;
};

__subsystem struct pulse_io_driver_api {
        int (*get_capabilities)(const struct device *dev, struct pulse_io_caps *caps);

        int (*channel_get)(const struct device *dev, uint8_t channel_idx,
                           struct pulse_io_channel **chan);

        int (*channel_release)(const struct device *dev, struct pulse_io_channel *chan);

        int (*channel_configure)(const struct device *dev, struct pulse_io_channel *chan,
                                 const struct pulse_io_config *cfg);

        int (*transmit_sync)(const struct device *dev, struct pulse_io_channel *chan,
                             const struct pulse_io_tx_req *req, k_timeout_t timeout);

        int (*receive_sync)(const struct device *dev, struct pulse_io_channel *chan,
                            const struct pulse_io_rx_req *req, size_t *count, k_timeout_t timeout);

        int (*stop)(const struct device *dev, struct pulse_io_channel *chan);

        void (*submit)(const struct device *dev, struct rtio_iodev_sqe *iodev_sqe);
        int (*get_encoder)(const struct device *dev, const struct pulse_io_encoder_api **api);
        int (*get_decoder)(const struct device *dev, const struct pulse_io_decoder_api **api);
};

__syscall int pulse_io_get_capabilities(const struct device *dev, struct pulse_io_caps *caps);

static inline int z_impl_pulse_io_get_capabilities(const struct device *dev,
                                                   struct pulse_io_caps *caps)
{
        const struct pulse_io_driver_api *api = DEVICE_API_GET(pulse_io, dev);

        if (api->get_capabilities == NULL) {
                return -ENOSYS;
        }
        return api->get_capabilities(dev, caps);
}

__syscall int pulse_io_channel_get(const struct device *dev, uint8_t channel_idx,
                                   struct pulse_io_channel **chan);

static inline int z_impl_pulse_io_channel_get(const struct device *dev, uint8_t channel_idx,
                                              struct pulse_io_channel **chan)
{
        return DEVICE_API_GET(pulse_io, dev)->channel_get(dev, channel_idx, chan);
}

__syscall int pulse_io_channel_release(const struct device *dev, struct pulse_io_channel *chan);

static inline int z_impl_pulse_io_channel_release(const struct device *dev,
                                                  struct pulse_io_channel *chan)
{
        return DEVICE_API_GET(pulse_io, dev)->channel_release(dev, chan);
}

__syscall int pulse_io_channel_configure(const struct device *dev, struct pulse_io_channel *chan,
                                         const struct pulse_io_config *cfg);

static inline int z_impl_pulse_io_channel_configure(const struct device *dev,
                                                    struct pulse_io_channel *chan,
                                                    const struct pulse_io_config *cfg)
{
        return DEVICE_API_GET(pulse_io, dev)->channel_configure(dev, chan, cfg);
}

__syscall int pulse_io_transmit_sync(const struct device *dev, struct pulse_io_channel *chan,
                                     const struct pulse_io_tx_req *req, k_timeout_t timeout);

static inline int z_impl_pulse_io_transmit_sync(const struct device *dev,
                                                struct pulse_io_channel *chan,
                                                const struct pulse_io_tx_req *req,
                                                k_timeout_t timeout)
{
        return DEVICE_API_GET(pulse_io, dev)->transmit_sync(dev, chan, req, timeout);
}

__syscall int pulse_io_receive_sync(const struct device *dev, struct pulse_io_channel *chan,
                                    const struct pulse_io_rx_req *req, size_t *count,
                                    k_timeout_t timeout);

static inline int z_impl_pulse_io_receive_sync(const struct device *dev,
                                               struct pulse_io_channel *chan,
                                               const struct pulse_io_rx_req *req, size_t *count,
                                               k_timeout_t timeout)
{
        return DEVICE_API_GET(pulse_io, dev)->receive_sync(dev, chan, req, count, timeout);
}

__syscall int pulse_io_stop(const struct device *dev, struct pulse_io_channel *chan);

static inline int z_impl_pulse_io_stop(const struct device *dev, struct pulse_io_channel *chan)
{
        return DEVICE_API_GET(pulse_io, dev)->stop(dev, chan);
}


struct pulse_io_bit_template {
        struct pulse_symbol zero[2];
        struct pulse_symbol one[2];
        bool msb_first;
};

int pulse_io_encode_bytes(const struct pulse_io_bit_template *tmpl, const uint8_t *bytes,
                          size_t nbytes, struct pulse_symbol *out, size_t out_cap,
                          size_t *produced);



struct pulse_io_encoder_api {
        int (*encode)(const struct pulse_io_bit_template *tmpl, const uint8_t *bytes, size_t nbytes,
                      struct pulse_symbol *out, size_t out_cap, size_t *produced);
};

struct pulse_io_decoder_api {
        int (*decode)(const struct pulse_io_bit_template *tmpl, uint32_t tolerance_ticks,
                      const struct pulse_symbol *in, size_t nsyms, uint8_t *out, size_t out_cap,
                      size_t *produced);
};

__syscall int pulse_io_get_encoder(const struct device *dev,
                                   const struct pulse_io_encoder_api **api);

static inline int z_impl_pulse_io_get_encoder(const struct device *dev,
                                              const struct pulse_io_encoder_api **api)
{
        const struct pulse_io_driver_api *drv = DEVICE_API_GET(pulse_io, dev);

        if (drv->get_encoder == NULL) {
                return -ENOSYS;
        }
        return drv->get_encoder(dev, api);
}

__syscall int pulse_io_get_decoder(const struct device *dev,
                                   const struct pulse_io_decoder_api **api);

static inline int z_impl_pulse_io_get_decoder(const struct device *dev,
                                              const struct pulse_io_decoder_api **api)
{
        const struct pulse_io_driver_api *drv = DEVICE_API_GET(pulse_io, dev);

        if (drv->get_decoder == NULL) {
                return -ENOSYS;
        }
        return drv->get_decoder(dev, api);
}

#ifdef CONFIG_RTIO
static inline void pulse_io_iodev_submit(const struct device *dev, struct rtio_iodev_sqe *iodev_sqe)
{
        const struct pulse_io_driver_api *drv = DEVICE_API_GET(pulse_io, dev);

        if (drv->submit == NULL) {
                rtio_iodev_sqe_err(iodev_sqe, -ENOSYS);
                return;
        }
        drv->submit(dev, iodev_sqe);
}
#endif /* CONFIG_RTIO */

int pulse_io_decode_bytes(const struct pulse_io_bit_template *tmpl, uint32_t tolerance_ticks,
                          const struct pulse_symbol *in, size_t nsyms, uint8_t *out, size_t out_cap,
                          size_t *produced);



#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/pulse_io.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_PULSE_IO_H_ */
```

## 72.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 113 行

字段按宽度从大到小排列，以紧凑存放并避免填充空洞（Padding holes）。

### 注释 3：原第 182 行

字段按宽度从大到小排列，以紧凑存放并避免填充空洞（Padding holes）。

### 注释 4：原第 226 行

RTIO 编解码器虚函数表（Codec vtables）的前向声明，定义见下文。

### 注释 5：原第 559 行

条件编译配置（Configuration）标记：`CONFIG_RTIO`。

### 注释 6：原第 582 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PULSE_IO_H_`。

## 72.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/rtio/rtio.h](../rtio_core_reference/P002_RTIO核心头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [pulse_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga8a69608ee00587642aca6e0d69878b07)
- [PULSE_IO_MODE_SYMBOL](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gga8a69608ee00587642aca6e0d69878b07a72babf2ca6b039635cb177be4f2e5e19)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [PULSE_IO_MODE_CELL](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gga8a69608ee00587642aca6e0d69878b07ae89d6f0f750e30719501cf32fbe2b220)
- [pulse_io_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga1188071d39a4018b719f18d019ba6f89)
- [PULSE_IO_DIR_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gga1188071d39a4018b719f18d019ba6f89ad4c6756a1f8972376620492ab1943ee3)
- [PULSE_IO_DIR_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gga1188071d39a4018b719f18d019ba6f89ab41397616fbd4b428db60bc6d665186a)
- [pulse_symbol](../device_power_control_model_reference/P070_pulse_symbol_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [duration](../device_power_control_model_reference/P070_pulse_symbol_结构体.md#aa164a0e6915c09bf376739ea724bf3e5)
- [level](../device_power_control_model_reference/P070_pulse_symbol_结构体.md#abcebf0eaf2ca01ab0144b23153b024fc)
- [pulse_cell](../device_power_control_model_reference/P061_pulse_cell_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [duty](../device_power_control_model_reference/P061_pulse_cell_结构体.md#a884c5d0305517a2b4914351cb371b231)
- [level](../device_power_control_model_reference/P061_pulse_cell_结构体.md#adae24acc734855ddfdb7c0ed340f8ebb)
- [rsvd](../device_power_control_model_reference/P061_pulse_cell_结构体.md#ac205607e071a653d65aed9d7beba2606)
- [pulse_io_caps](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md)
- [tx_min_chunk_symbols](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#af6dee58bfc47780ccc77092777080ce8)
- [tx_max_streaming](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#afc8e349e152b2a271b51a2810eab2586)
- [modes](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#acb4396add794dda4933f9c176d1766be)
- [min_tick_ns](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#aad176fbf3bf21edc3b45a89be128002d)
- [max_tick_ns](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a6300be8f6722fd166d33849df9c031aa)
- [max_duration_ticks](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a4da263bc4a355448249400ad364f87b9)
- [tx_loop_max](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a3b0e9052d24dbc55e53b2f0d9ceda0cf)
- [rx_idle_threshold_max](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a92a922e8a11823ad0ba733a2ee88cf0d)
- [rx_filter_max_ticks](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a986f4a6419df94ce618b0d05ee876276)
- [tx_channel_mask](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a219331ae467da4a2583d4d905bbac05b)
- [rx_channel_mask](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#aa91e3a0fe7e1fd95c89a2436558467eb)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cell_duty_bits](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a173fa1c857ed24a2ecb5f9de8527136b)
- [num_channels](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a16fa91b3ccba69c11ebc826eeb29245d)
- [supports_tx](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#ad85c4a8652bbf80da429c87bbcb680c6)
- [supports_rx](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a1de73e3e72e07bc99d09808402d17b61)
- [tx_carrier](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#aead2efb6f8fe2955d2d9b188cd9264eb)
- [tx_loop_auto_stop](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a2ee6e5254c8f3bf474c9c49745d8c377)
- [tx_sync_multi_channel](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#ab8b1aa9fea93cd697bcc760214f12760)
- [rx_carrier_demod](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#adfa8d33306657b2870d3b5df8a4dce04)
- [rx_dma_buffered](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a2084a3bd36ed5c131d898edfbcdfba0a)
- [rx_streaming](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a5da774fe623fd1f35cbf2e54671399d6)
- [cell_period_per_chunk](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a64cf12b881eab0f538536c34d3273c14)
- [pulse_io_config](../device_power_control_model_reference/P064_pulse_io_config_结构体.md)
- [resolution_hz](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a09ab3fcf00e4bab33f290695d045d9ce)
- [cell_period_ticks](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a0c10cf29df1143a842fdde9cf1d49a42)
- [carrier_hz](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a65c6a04405648635c9fea5ac47cf5063)
- [rx_idle_threshold_ticks](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#ae767da3eb5f3d4d516262c84972d261f)
- [rx_filter_ticks](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#aef4876ae134c3aa2b1634ac6892f7c5e)
- [mode](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a0d74c4cf0960039675f3806870c68a2c)
- [dir](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#aa0f9d3365b77ff5d80c6f9ec222ff5ff)
- [carrier_duty_pct](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a7466b1968e22a84f4542d0be6ee65304)
- [idle_high](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a3f378f0c755b40de97c9c601f413b91f)
- [carrier_en](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#adeee7ddbc94ba628916ac3a6b029d337)
- [rx_carrier_demod](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a106d88a37daf50fd704a33e6fc49054a)
- [pulse_io_encoder_api](../device_power_control_model_reference/P067_pulse_io_encoder_api_结构体.md)
- [pulse_io_decoder_api](../device_power_control_model_reference/P065_pulse_io_decoder_api_结构体.md)
- [pulse_io_tx_req](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md)
- [symbols](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md#a33af6b148afa43e93d1b8826d78198d7)
- [cells](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md#a21426e72b2eaab937e86d50e46177505)
- [count](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md#a39ecb966484761d419c10cd41ae15512)
- [loop_count](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md#a39ba9d615f8b40f117bd3efc97bdacd7)
- [pulse_io_rx_req](../device_power_control_model_reference/P068_pulse_io_rx_req_结构体.md)
- [symbols](../device_power_control_model_reference/P068_pulse_io_rx_req_结构体.md#a5847bb48236f6d665b176daf72cdee6e)
- [cells](../device_power_control_model_reference/P068_pulse_io_rx_req_结构体.md#a70ae274b716278583e655e2457577f58)
- [capacity](../device_power_control_model_reference/P068_pulse_io_rx_req_结构体.md#a3412f6080ba7eaecaf1d4b532b77451a)
- [pulse_io_driver_api](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md)
- [get_capabilities](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a9aa7510ea5c1aab6b490dd3b6b1a4bbc)
- [device](../device_reference/P002_设备对象结构.md)
- [channel_get](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#aee848f0d513e8fe1573cf1e8f5c480a4)
- [channel_release](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a27dab2f1794e29d51ff613af6d85b0ee)
- [channel_configure](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a6a3d4ba7f6da3ffdc79f9bc30cbc4429)
- [transmit_sync](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a5c621cc969cddc1af5698616a3809994)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [receive_sync](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a42d3e7109cab1333e12ba4da57eac80c)
- [stop](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a1e5d2a7e7aa0a44d4b8cc106c22242e9)
- [submit](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#afba3d4238934be36aa5a27c20160df5f)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [get_encoder](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a9aeb9a2a707d8a3c2fe81d064e59c320)
- [get_decoder](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#adbfd779fcbcecce8af577256c38cf941)
- [pulse_io_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga3d92ae937058d0675dd56b009aa1138f)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [pulse_io_channel_get](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga0a0eb57e852853da9c3ba1e262991091)
- [pulse_io_channel_release](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gafcce0615be70ca39c346df4c260f09d2)
- [pulse_io_channel_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gaa3a5b31cb44647823aa60af4416e6d3f)
- [pulse_io_transmit_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga3e03e72bb73c8949c222d48f28c03612)
- [pulse_io_receive_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga1d122c085430f9d4408564b76dee0944)
- [pulse_io_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga8810dd66d863919cf3ea03ae27da4cf7)
- [pulse_io_bit_template](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md)
- [zero](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md#ab57882bf17ca354573f2e0bab95009fc)
- [one](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md#af5cf7de078f5a298afe49a64680ee0d0)
- [msb_first](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md#a32b1f8e31bc606180dac02beee6b3c74)
- [pulse_io_encode_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gaca42826a8404d4e5e1eacefc5f17debf)
- [encode](../device_power_control_model_reference/P067_pulse_io_encoder_api_结构体.md#ab5d90fd2dc5832a0f9d48078b1d1193c)
- [decode](../device_power_control_model_reference/P065_pulse_io_decoder_api_结构体.md#a3898c1fec9586b45606c9071ddba21a5)
- [pulse_io_get_encoder](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gaf925af6fa08b119550e51024c5ebc408)
- [pulse_io_get_decoder](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga382adc1d7095dba8dd087c47c551436c)
- [rtio_iodev_sqe_err](../rtio_core_reference/P001_RTIO公共接口.md#gaada07aa6acefa548743b525225fa482f)
- [pulse_io_decode_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga05add5c7dc934ad84ddafbfe4c08d2a6)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [rtio.h](../rtio_core_reference/P002_RTIO核心头文件参考.md)
- [pulse_cell::duty](../device_power_control_model_reference/P061_pulse_cell_结构体.md#a884c5d0305517a2b4914351cb371b231)
- [pulse_cell::rsvd](../device_power_control_model_reference/P061_pulse_cell_结构体.md#ac205607e071a653d65aed9d7beba2606)
- [pulse_cell::level](../device_power_control_model_reference/P061_pulse_cell_结构体.md#adae24acc734855ddfdb7c0ed340f8ebb)
- [pulse_io_bit_template::msb_first](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md#a32b1f8e31bc606180dac02beee6b3c74)
- [pulse_io_bit_template::zero](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md#ab57882bf17ca354573f2e0bab95009fc)
- [pulse_io_bit_template::one](../device_power_control_model_reference/P062_pulse_io_bit_template_结构体.md#af5cf7de078f5a298afe49a64680ee0d0)
- [pulse_io_caps::num_channels](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a16fa91b3ccba69c11ebc826eeb29245d)
- [pulse_io_caps::cell_duty_bits](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a173fa1c857ed24a2ecb5f9de8527136b)
- [pulse_io_caps::supports_rx](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a1de73e3e72e07bc99d09808402d17b61)
- [pulse_io_caps::rx_dma_buffered](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a2084a3bd36ed5c131d898edfbcdfba0a)
- [pulse_io_caps::tx_channel_mask](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a219331ae467da4a2583d4d905bbac05b)
- [pulse_io_caps::tx_loop_auto_stop](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a2ee6e5254c8f3bf474c9c49745d8c377)
- [pulse_io_caps::tx_loop_max](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a3b0e9052d24dbc55e53b2f0d9ceda0cf)
- [pulse_io_caps::max_duration_ticks](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a4da263bc4a355448249400ad364f87b9)
- [pulse_io_caps::rx_streaming](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a5da774fe623fd1f35cbf2e54671399d6)
- [pulse_io_caps::max_tick_ns](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a6300be8f6722fd166d33849df9c031aa)
- [pulse_io_caps::cell_period_per_chunk](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a64cf12b881eab0f538536c34d3273c14)
- [pulse_io_caps::rx_idle_threshold_max](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a92a922e8a11823ad0ba733a2ee88cf0d)
- [pulse_io_caps::rx_filter_max_ticks](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#a986f4a6419df94ce618b0d05ee876276)
- [pulse_io_caps::rx_channel_mask](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#aa91e3a0fe7e1fd95c89a2436558467eb)
- [pulse_io_caps::min_tick_ns](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#aad176fbf3bf21edc3b45a89be128002d)
- [pulse_io_caps::tx_sync_multi_channel](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#ab8b1aa9fea93cd697bcc760214f12760)
- [pulse_io_caps::modes](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#acb4396add794dda4933f9c176d1766be)
- [pulse_io_caps::supports_tx](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#ad85c4a8652bbf80da429c87bbcb680c6)
- [pulse_io_caps::rx_carrier_demod](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#adfa8d33306657b2870d3b5df8a4dce04)
- [pulse_io_caps::tx_carrier](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#aead2efb6f8fe2955d2d9b188cd9264eb)
- [pulse_io_caps::tx_min_chunk_symbols](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#af6dee58bfc47780ccc77092777080ce8)
- [pulse_io_caps::tx_max_streaming](../device_power_control_model_reference/P063_pulse_io_caps_结构体.md#afc8e349e152b2a271b51a2810eab2586)
- [pulse_io_config::resolution_hz](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a09ab3fcf00e4bab33f290695d045d9ce)
- [pulse_io_config::cell_period_ticks](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a0c10cf29df1143a842fdde9cf1d49a42)
- [pulse_io_config::mode](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a0d74c4cf0960039675f3806870c68a2c)
- [pulse_io_config::rx_carrier_demod](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a106d88a37daf50fd704a33e6fc49054a)
- [pulse_io_config::idle_high](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a3f378f0c755b40de97c9c601f413b91f)
- [pulse_io_config::carrier_hz](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a65c6a04405648635c9fea5ac47cf5063)
- [pulse_io_config::carrier_duty_pct](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#a7466b1968e22a84f4542d0be6ee65304)
- [pulse_io_config::dir](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#aa0f9d3365b77ff5d80c6f9ec222ff5ff)
- [pulse_io_config::carrier_en](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#adeee7ddbc94ba628916ac3a6b029d337)
- [pulse_io_config::rx_idle_threshold_ticks](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#ae767da3eb5f3d4d516262c84972d261f)
- [pulse_io_config::rx_filter_ticks](../device_power_control_model_reference/P064_pulse_io_config_结构体.md#aef4876ae134c3aa2b1634ac6892f7c5e)
- [pulse_io_decoder_api::decode](../device_power_control_model_reference/P065_pulse_io_decoder_api_结构体.md#a3898c1fec9586b45606c9071ddba21a5)
- [pulse_io_driver_api::stop](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a1e5d2a7e7aa0a44d4b8cc106c22242e9)
- [pulse_io_driver_api::channel_release](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a27dab2f1794e29d51ff613af6d85b0ee)
- [pulse_io_driver_api::receive_sync](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a42d3e7109cab1333e12ba4da57eac80c)
- [pulse_io_driver_api::transmit_sync](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a5c621cc969cddc1af5698616a3809994)
- [pulse_io_driver_api::channel_configure](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a6a3d4ba7f6da3ffdc79f9bc30cbc4429)
- [pulse_io_driver_api::get_capabilities](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a9aa7510ea5c1aab6b490dd3b6b1a4bbc)
- [pulse_io_driver_api::get_encoder](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#a9aeb9a2a707d8a3c2fe81d064e59c320)
- [pulse_io_driver_api::get_decoder](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#adbfd779fcbcecce8af577256c38cf941)
- [pulse_io_driver_api::channel_get](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#aee848f0d513e8fe1573cf1e8f5c480a4)
- [pulse_io_driver_api::submit](../device_power_control_model_reference/P066_pulse_io_driver_api_结构体.md#afba3d4238934be36aa5a27c20160df5f)
- [pulse_io_encoder_api::encode](../device_power_control_model_reference/P067_pulse_io_encoder_api_结构体.md#ab5d90fd2dc5832a0f9d48078b1d1193c)
- [pulse_io_rx_req::capacity](../device_power_control_model_reference/P068_pulse_io_rx_req_结构体.md#a3412f6080ba7eaecaf1d4b532b77451a)
- [pulse_io_rx_req::symbols](../device_power_control_model_reference/P068_pulse_io_rx_req_结构体.md#a5847bb48236f6d665b176daf72cdee6e)
- [pulse_io_rx_req::cells](../device_power_control_model_reference/P068_pulse_io_rx_req_结构体.md#a70ae274b716278583e655e2457577f58)
- [pulse_io_tx_req::cells](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md#a21426e72b2eaab937e86d50e46177505)
- [pulse_io_tx_req::symbols](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md#a33af6b148afa43e93d1b8826d78198d7)
- [pulse_io_tx_req::loop_count](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md#a39ba9d615f8b40f117bd3efc97bdacd7)
- [pulse_io_tx_req::count](../device_power_control_model_reference/P069_pulse_io_tx_req_结构体.md#a39ecb966484761d419c10cd41ae15512)
- [pulse_symbol::duration](../device_power_control_model_reference/P070_pulse_symbol_结构体.md#aa164a0e6915c09bf376739ea724bf3e5)
- [pulse_symbol::level](../device_power_control_model_reference/P070_pulse_symbol_结构体.md#abcebf0eaf2ca01ab0144b23153b024fc)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P071_device.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P073_pwm_mchp_pwm_g1.h_源码浏览.md)
