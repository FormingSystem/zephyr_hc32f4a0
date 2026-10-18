---
id: learning.zephyr-docs.api-source-supplement-reference.page-80
title: gmap_lc3_preset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gmap__lc3__preset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第80章\_gmap\_lc3\_preset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gmap__lc3__preset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gmap__lc3__preset_8h.html)。

## 80.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
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
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="foldopen00107"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00143"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="foldopen00155"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="foldopen00167"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="foldopen00179"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="foldopen00193"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="foldopen00205"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="foldopen00217"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="foldopen00229"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="abap_8h_html"></a>
<a id="abap__lc3__preset_8h_html"></a>
<a id="abluetooth_2audio_2audio_8h_html"></a>
<a id="alc3_8h_html"></a>

```c


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_GMAP_LC3_PRESET_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_GMAP_LC3_PRESET_H_


#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/audio/bap.h>
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
#include <zephyr/bluetooth/audio/lc3.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_GMAP_LC3_PRESET_32_1_GR(_loc, _stream_context)                                          \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 60U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 60U, 1U, 15U, 10000U))

#define BT_GMAP_LC3_PRESET_32_2_GR(_loc, _stream_context)                                          \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 80U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 80U, 1U, 20U, 10000U))

#define BT_GMAP_LC3_PRESET_48_1_GR(_loc, _stream_context)                                          \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 75U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 75U, 1U, 15U, 10000U))

#define BT_GMAP_LC3_PRESET_48_2_GR(_loc, _stream_context)                                          \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 100U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 100U, 1U, 20U, 10000U))

#define BT_GMAP_LC3_PRESET_48_3_GR(_loc, _stream_context)                                          \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 90U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 90U, 1U, 15U, 10000U))

#define BT_GMAP_LC3_PRESET_48_4_GR(_loc, _stream_context)                                          \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 120u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 120U, 1U, 20U, 10000U))

#define BT_GMAP_LC3_PRESET_16_1_GS(_loc, _stream_context)                                          \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 30U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 30U, 1U, 15U, 60000U))

#define BT_GMAP_LC3_PRESET_16_2_GS(_loc, _stream_context)                                          \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 40U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 40U, 1U, 20U, 60000U))

#define BT_GMAP_LC3_PRESET_32_1_GS(_loc, _stream_context)                                          \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 60U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 60U, 1U, 15U, 60000U))

#define BT_GMAP_LC3_PRESET_32_2_GS(_loc, _stream_context)                                          \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 80U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 80U, 1U, 20U, 60000U))

#define BT_GMAP_LC3_PRESET_48_1_GS(_loc, _stream_context)                                          \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 75U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 75U, 1U, 15U, 60000U))

#define BT_GMAP_LC3_PRESET_48_2_GS(_loc, _stream_context)                                          \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 100U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 100U, 1U, 20U, 60000U))

/* GMAP LC3 broadcast presets defined by table 3.22 in the GMAP v1.0 specification */

#define BT_GMAP_LC3_PRESET_48_1_G(_loc, _stream_context)                                           \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 75U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 75U, 1U, 8U, 10000U))

#define BT_GMAP_LC3_PRESET_48_2_G(_loc, _stream_context)                                           \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 100U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 100U, 1U, 10U, 10000U))

#define BT_GMAP_LC3_PRESET_48_3_G(_loc, _stream_context)                                           \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 90U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 90U, 1U, 8U, 10000U))

#define BT_GMAP_LC3_PRESET_48_4_G(_loc, _stream_context)                                           \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 120u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 120U, 1U, 10U, 10000U))

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_GMAP_LC3_PRESET_H_ */
```

## 80.2\_可见注释译文（Comments）

### 注释 1：原第 185 行

GMAP v1.0 规范表 3.22 定义的 GMAP LC3 广播预设（Broadcast presets）。

### 注释 2：原第 240 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_GMAP_LC3_PRESET_H_`。

## 80.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gmap__lc3__preset_8h.html)
- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)
- [zephyr/bluetooth/audio/bap_lc3_preset.h](https://docs.zephyrproject.org/latest/doxygen/html/bap__lc3__preset_8h.html)
- [zephyr/bluetooth/audio/lc3.h](https://docs.zephyrproject.org/latest/doxygen/html/lc3_8h.html)
- [bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)
- [bap_lc3_preset.h](https://docs.zephyrproject.org/latest/doxygen/html/bap__lc3__preset_8h.html)
- [audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [lc3.h](https://docs.zephyrproject.org/latest/doxygen/html/lc3_8h.html)

---

[上一章](P079_gmap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P081_goep.h_源码浏览.md)
