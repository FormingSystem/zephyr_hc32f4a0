---
id: learning.zephyr-docs.api-source-device-reference.page-1
title: bap_lc3_preset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bap__lc3__preset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_bap\_lc3\_preset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bap__lc3__preset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bap__lc3__preset_8h.html)。

## 1.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="foldopen00123"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="foldopen00135"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="foldopen00147"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="foldopen00159"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="foldopen00183"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="foldopen00195"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="foldopen00207"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="foldopen00219"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="foldopen00231"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="foldopen00243"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00255"></a>
<a id="foldopen00256"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="foldopen00268"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="foldopen00280"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="foldopen00292"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="foldopen00304"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="foldopen00316"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="foldopen00328"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="foldopen00340"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="foldopen00352"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="foldopen00364"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="foldopen00376"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="foldopen00388"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="foldopen00400"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="foldopen00412"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="foldopen00424"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="foldopen00436"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00448"></a>
<a id="foldopen00449"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="foldopen00461"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="foldopen00473"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="foldopen00487"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="foldopen00499"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="foldopen00513"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="foldopen00525"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="foldopen00537"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="foldopen00549"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="foldopen00561"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="foldopen00573"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="foldopen00585"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="foldopen00597"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="foldopen00609"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="foldopen00621"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="foldopen00633"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00645"></a>
<a id="foldopen00646"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="foldopen00658"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="foldopen00670"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="foldopen00684"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="foldopen00696"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="foldopen00710"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="foldopen00722"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="foldopen00734"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="foldopen00746"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="foldopen00758"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="foldopen00770"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="foldopen00782"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00787"></a>
<a id="foldopen00794"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="foldopen00806"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="foldopen00818"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="foldopen00830"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="abap_8h_html"></a>
<a id="abluetooth_2audio_2audio_8h_html"></a>
<a id="alc3_8h_html"></a>
<a id="astructbt__audio__codec__cfg_html"></a>
<a id="astructbt__bap__lc3__preset_html"></a>
<a id="astructbt__bap__lc3__preset_html_a2615416828c62842a076749796beb6da"></a>
<a id="astructbt__bap__lc3__preset_html_a8f5954471875861bfd387446060e9565"></a>
<a id="astructbt__bap__qos__cfg_html"></a>

```c


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_BAP_LC3_PRESET_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_BAP_LC3_PRESET_H_


#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/audio/bap.h>
#include <zephyr/bluetooth/audio/lc3.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_bap_lc3_preset {
        struct bt_audio_codec_cfg codec_cfg;
        struct bt_bap_qos_cfg qos;
};

#define BT_BAP_LC3_PRESET(_codec, _qos)                                                            \
        {                                                                                          \
                .codec_cfg = _codec, .qos = _qos,                                                  \
        }

/* LC3 Unicast presets defined by table 5.2 in the BAP v1.0 specification */

#define BT_BAP_LC3_UNICAST_PRESET_8_1_1(_loc, _stream_context)                                     \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 26u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 26u, 2u, 8u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_8_2_1(_loc, _stream_context)                                     \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 30U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 30u, 2u, 10u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_16_1_1(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 30U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 30u, 2u, 8u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_16_2_1(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 40U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 40u, 2u, 10u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_24_1_1(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 45U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 45u, 2u, 8u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_24_2_1(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 60U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 60u, 2u, 10u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_32_1_1(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 60U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 60u, 2u, 8u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_32_2_1(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 80U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 80u, 2u, 10u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_441_1_1(_loc, _stream_context)                                   \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 97U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_FRAMED(8163u, 97u, 5u, 24u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_441_2_1(_loc, _stream_context)                                   \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 130U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_FRAMED(10884u, 130u, 5u, 31u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_48_1_1(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 75U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 75u, 5u, 15u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_48_2_1(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 100U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 100u, 5u, 20u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_48_3_1(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 90U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 90u, 5u, 15u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_48_4_1(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 120u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 120u, 5u, 20u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_48_5_1(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 117u,   \
                                                    1, _stream_context),                           \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 117u, 5u, 15u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_48_6_1(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 155u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 155u, 5u, 20u, 40000u))

/* Following presets are for unicast high reliability audio data */
#define BT_BAP_LC3_UNICAST_PRESET_8_1_2(_loc, _stream_context)                                     \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 26u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 26u, 13u, 75u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_8_2_2(_loc, _stream_context)                                     \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 30U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 30u, 13u, 95u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_16_1_2(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 30U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 30u, 13u, 75u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_16_2_2(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 40U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 40u, 13u, 95u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_24_1_2(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 45U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 45u, 13u, 75u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_24_2_2(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 60U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 60u, 13u, 95u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_32_1_2(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 60U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 60u, 13u, 75u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_32_2_2(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 80U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 80u, 13u, 95u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_441_1_2(_loc, _stream_context)                                   \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 97U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_FRAMED(8163u, 97u, 13u, 80u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_441_2_2(_loc, _stream_context)                                   \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 130U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_FRAMED(10884u, 130u, 13u, 85u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_48_1_2(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 75U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 75u, 13u, 75u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_48_2_2(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 100U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 100u, 13u, 95u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_48_3_2(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 90U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 90u, 13u, 75u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_48_4_2(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 120u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 120u, 13u, 100u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_48_5_2(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 117u,   \
                                                    1, _stream_context),                           \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 117u, 13u, 75u, 40000u))

#define BT_BAP_LC3_UNICAST_PRESET_48_6_2(_loc, _stream_context)                                    \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 155u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 155u, 13u, 100u, 40000u))

/* LC3 Broadcast presets defined by table 6.4 in the BAP v1.0 specification */
#define BT_BAP_LC3_BROADCAST_PRESET_8_1_1(_loc, _stream_context)                                   \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 26u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 26u, 2u, 8u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_8_2_1(_loc, _stream_context)                                   \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 30U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 30u, 2u, 10u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_16_1_1(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 30U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 30u, 2u, 8u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_16_2_1(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 40U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 40u, 2u, 10u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_24_1_1(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 45U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 45u, 2u, 8u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_24_2_1(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 60U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 60u, 2u, 10u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_32_1_1(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 60U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 60u, 2u, 8u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_32_2_1(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 80U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 80u, 2u, 10u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_441_1_1(_loc, _stream_context)                                 \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 97U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_FRAMED(8163u, 97u, 4u, 24u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_441_2_1(_loc, _stream_context)                                 \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 130U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_FRAMED(10884u, 130u, 4u, 31u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_48_1_1(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 75U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 75u, 4u, 15u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_48_2_1(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 100U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 100u, 4u, 20u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_48_3_1(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 90U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 90u, 4u, 15u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_48_4_1(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 120u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 120u, 4u, 20u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_48_5_1(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 117u,   \
                                                    1, _stream_context),                           \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 117u, 4u, 15u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_48_6_1(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 155u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 155u, 4u, 20u, 40000u))

/* Following presets are for broadcast high reliability audio data */
#define BT_BAP_LC3_BROADCAST_PRESET_8_1_2(_loc, _stream_context)                                   \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 26u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 26u, 4u, 45u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_8_2_2(_loc, _stream_context)                                   \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 30U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 30u, 4u, 60u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_16_1_2(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 30U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 30u, 4u, 45u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_16_2_2(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 40U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 40u, 4u, 60u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_24_1_2(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 45U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 45u, 4u, 45u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_24_2_2(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 60U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 60u, 4u, 60u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_32_1_2(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 60U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 60u, 4u, 45u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_32_2_2(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 80U, 1,  \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 80u, 4u, 60u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_441_1_2(_loc, _stream_context)                                 \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 97U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_FRAMED(8163u, 97u, 4u, 54u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_441_2_2(_loc, _stream_context)                                 \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 130U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_FRAMED(10884u, 130u, 4u, 60u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_48_1_2(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 75U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 75u, 4u, 50u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_48_2_2(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 100U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 100u, 4u, 65u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_48_3_2(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 90U, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 90u, 4u, 50u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_48_4_2(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 120u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 120u, 4u, 65u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_48_5_2(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 117u,   \
                                                    1, _stream_context),                           \
                          BT_BAP_QOS_CFG_UNFRAMED(7500u, 117u, 4u, 50u, 40000u))

#define BT_BAP_LC3_BROADCAST_PRESET_48_6_2(_loc, _stream_context)                                  \
        BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                                    BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 155u, 1, \
                                                    _stream_context),                              \
                          BT_BAP_QOS_CFG_UNFRAMED(10000u, 155u, 4u, 65u, 40000u))

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_BAP_LC3_PRESET_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 51 行

BAP v1.0 规范表 5.2 定义的低复杂度通信编解码器单播预设（LC3 Unicast Presets）。

### 注释 2：原第 255 行

以下预设（Presets）用于高可靠性单播音频数据（Unicast High Reliability Audio Data）。

### 注释 3：原第 448 行

BAP v1.0 规范表 6.4 定义的低复杂度通信编解码器广播预设（LC3 Broadcast Presets）。

### 注释 4：原第 645 行

以下预设（Presets）用于高可靠性广播音频数据（Broadcast High Reliability Audio Data）。

### 注释 5：原第 841 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_BAP_LC3_PRESET_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bap__lc3__preset_8h.html)
- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)
- [zephyr/bluetooth/audio/lc3.h](https://docs.zephyrproject.org/latest/doxygen/html/lc3_8h.html)
- [bt_bap_lc3_preset](../bluetooth_le_audio_model_reference/P026_bt_bap_lc3_preset_结构体.md)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [codec_cfg](../bluetooth_le_audio_model_reference/P026_bt_bap_lc3_preset_结构体.md#a2615416828c62842a076749796beb6da)
- [bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)
- [qos](../bluetooth_le_audio_model_reference/P026_bt_bap_lc3_preset_结构体.md#a8f5954471875861bfd387446060e9565)
- [bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)
- [audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [lc3.h](https://docs.zephyrproject.org/latest/doxygen/html/lc3_8h.html)
- [bt_bap_lc3_preset::codec_cfg](../bluetooth_le_audio_model_reference/P026_bt_bap_lc3_preset_结构体.md#a2615416828c62842a076749796beb6da)
- [bt_bap_lc3_preset::qos](../bluetooth_le_audio_model_reference/P026_bt_bap_lc3_preset_结构体.md#a8f5954471875861bfd387446060e9565)

---

[返回大纲](大纲.md) · [下一章](P002_map.h_源码浏览.md)
