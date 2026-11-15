---
id: learning.zephyr-docs.api-source-supplement-reference.page-234
title: usb_audio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__audio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第234章\_usb\_audio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usb__audio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../usb/P142_旧版USB音频头文件接口.md)。

## 234.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="foldopen00102"></a>
<a id="l00102"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="foldopen00179"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="foldopen00190"></a>
<a id="l00190"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="foldopen00262"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="adevice_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_a1522d81a002804223e25300a6961f527"></a>
<a id="astructusb__audio__fu__evt_html"></a>
<a id="astructusb__audio__fu__evt_html_a1cb4849aae8b9a4e667ed126e9bce26b"></a>
<a id="astructusb__audio__fu__evt_html_a47c6c7c00fac32a04bffd251d715dc39"></a>
<a id="astructusb__audio__fu__evt_html_a5baf5d4e2a39337dc9c21c4465d5ad8e"></a>
<a id="astructusb__audio__fu__evt_html_a6ef19bf7d37c3d636edba243dac8ecb2"></a>
<a id="astructusb__audio__fu__evt_html_a9313b39f178c8a86d680a950ce505713"></a>
<a id="astructusb__audio__ops_html"></a>
<a id="astructusb__audio__ops_html_a2752018597ba5bd4e9a80d1ae650bf8b"></a>
<a id="astructusb__audio__ops_html_a483af21f54537bef1a6ae3be2cd3717d"></a>
<a id="astructusb__audio__ops_html_a6ee19a7aef47561f14981b7e7ebd8ac7"></a>
<a id="astructusb__audio__ops_html_a861823185efb5c9a06b900799adb9efb"></a>
<a id="asys_2util_8h_html"></a>
<a id="ausb__audio_8h_html_a4885d280ebe68e42cf068524038ec582"></a>
<a id="ausb__audio_8h_html_a4885d280ebe68e42cf068524038ec582a589d9e4883f109f787517a017d6187b2"></a>
<a id="ausb__audio_8h_html_a4885d280ebe68e42cf068524038ec582a8f451ebdab0c5a1d930ce5808b6f0892"></a>
<a id="ausb__audio_8h_html_a4885d280ebe68e42cf068524038ec582aabd72d1d6016fbe1e37788f37c1c8cac"></a>
<a id="ausb__audio_8h_html_a4885d280ebe68e42cf068524038ec582aba82b7b28c0ad0ecf125695bd1f35db2"></a>
<a id="ausb__audio_8h_html_a4d49f239cc36daf8bd0cfa36c5fb75d2"></a>
<a id="ausb__audio_8h_html_a4d49f239cc36daf8bd0cfa36c5fb75d2a08d27821af6c7d875351ec8f58082794"></a>
<a id="ausb__audio_8h_html_a4d49f239cc36daf8bd0cfa36c5fb75d2a1c23bc45ef27b6acf87da3c68281d2a3"></a>
<a id="ausb__audio_8h_html_a4d49f239cc36daf8bd0cfa36c5fb75d2a26c439798671f4efe7b6469f3dcd37c5"></a>
<a id="ausb__audio_8h_html_a4d49f239cc36daf8bd0cfa36c5fb75d2a2b14e19e39d96c31764f89128b393efc"></a>
<a id="ausb__audio_8h_html_a4d49f239cc36daf8bd0cfa36c5fb75d2a657b1e5689be60c2f1ce6d3d2cb68f89"></a>
<a id="ausb__audio_8h_html_a4d49f239cc36daf8bd0cfa36c5fb75d2a6d258289b44ddeb1153168fafb92c0d8"></a>
<a id="ausb__audio_8h_html_a4d49f239cc36daf8bd0cfa36c5fb75d2a9e9d8f03326339a9a5e212aad42f984f"></a>
<a id="ausb__audio_8h_html_a4d49f239cc36daf8bd0cfa36c5fb75d2acfcc2072d11863eaedb68f87a93eb601"></a>
<a id="ausb__audio_8h_html_a4d49f239cc36daf8bd0cfa36c5fb75d2adae061d51c1df5d03cc47b7b2c412f1d"></a>
<a id="ausb__audio_8h_html_a4d49f239cc36daf8bd0cfa36c5fb75d2adb4f2720ad78a26d22279a45df56b43d"></a>
<a id="ausb__audio_8h_html_a4d49f239cc36daf8bd0cfa36c5fb75d2aef98729fa59119eb0e0cbed2e6a992da"></a>
<a id="ausb__audio_8h_html_a57bc8c499f03323db38f5604f8ebcda2"></a>
<a id="ausb__audio_8h_html_a692362e834622532b7be71d5e0bdc219"></a>
<a id="ausb__audio_8h_html_a6a69824dadab0c36bb6a6ce378da8ba5"></a>
<a id="ausb__audio_8h_html_a8f289f2b4d0a7d3accdc6308cb5661e8"></a>
<a id="ausb__audio_8h_html_ab5e6c883af53c089c7fcdee4d2249d9a"></a>
<a id="ausb__audio_8h_html_ab5e6c883af53c089c7fcdee4d2249d9aa10f58b16088a3218eb4ed8c31ffd9dfe"></a>
<a id="ausb__audio_8h_html_ab5e6c883af53c089c7fcdee4d2249d9aa2eee02b3652783891eb878bd0a02227d"></a>
<a id="ausb__audio_8h_html_ab5e6c883af53c089c7fcdee4d2249d9aa357c88ef81ee69875f4cbbf5610fd48f"></a>
<a id="ausb__audio_8h_html_ab5e6c883af53c089c7fcdee4d2249d9aa533df0f1df0cd0ba91f05922780c3f51"></a>
<a id="ausb__audio_8h_html_ab5e6c883af53c089c7fcdee4d2249d9aa80b350d862e1fe02fb04572481ae6343"></a>
<a id="ausb__audio_8h_html_ab5e6c883af53c089c7fcdee4d2249d9aab01072ed5bad284a34cf9a2e8b2098e5"></a>
<a id="ausb__audio_8h_html_ab5e6c883af53c089c7fcdee4d2249d9aad06ebbc1c9c35ec35dca8c7bb95c52c7"></a>
<a id="ausb__audio_8h_html_ab5e6c883af53c089c7fcdee4d2249d9aad1f55fd97d0217453704ba61a7357ca1"></a>
<a id="ausb__audio_8h_html_ab5e6c883af53c089c7fcdee4d2249d9aae5e4af543ede652cda987db1ca5b10ab"></a>
<a id="ausb__audio_8h_html_acbdc8b284d108983fb204cbd679043bb"></a>
<a id="ausb__audio_8h_html_acbdc8b284d108983fb204cbd679043bba0f0e91f9580d03853432259d74f108ba"></a>
<a id="ausb__audio_8h_html_acbdc8b284d108983fb204cbd679043bbab2ce7b1140be0d960ab2754bc8e262dd"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6ad"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6ada1088106727c5c6d850dd2ab98a7b454d"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6ada1945ba97faeff43f68bd4918be76a4e7"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6ada229701fae8fdc58a530ffcdd1cdea109"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6ada2e921e391ec9f89345e6b63ad1fd5da6"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6ada4ce3135409f73b58295898087e9ff485"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6ada6e3db81f03ab284c82c254952c3f7259"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6ada6e5e1dd7fd6292ba8bcc4564223b8220"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6ada6f5faa411e92cdeacdc521bd05b4bfab"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6ada8d2d8fdf1663f9691f566245062b2cf6"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6ada96ac36a0735d03e3addf0fe540903707"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6adac027c9e016ad88a9c135a0c1050921bb"></a>
<a id="ausb__audio_8h_html_ad6eb1c3ec75aef329ea973d1cb4dc6adae89a907671d2940da6bb4c58cf9a7fd0"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79e"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79ea232edf193a4f755d8821c51001d11f1d"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79ea24f6c5657c301871089dc8eac3b5d207"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79ea2eaf530492705b7e493e5d746752c262"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79ea3140dd357e3093db21f581226a6b000a"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79ea319eef3f2a59242b0c8dd5ca50212e14"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79ea349881bce5285d61f886aec8fc2bf84c"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79ea3cace6841265454e604513ebba78f749"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79ea456a90d55e1b271698516d89e8ba7f5b"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79ea64205001486011d22c1ec0abd382a486"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79ea64f43c7efb785a88f72302d2ad8d00f0"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79ea699cefac29e9d9c60f53562c7ad7050d"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79ea8b48c4993389b7f5a08d55b68b924480"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79eaa0fbe557eba975cb5e368e199ea4f6d4"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79eaad81dbd6f39554f52c3912755643d661"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79eab7f8515fb0154f5b0e038f485bdadaf6"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79eac551e3ea3e21ddf057062fe7d05b3ec9"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79eac565b3d090c71949c1e1423bb8529c86"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79eac740f1b3cfcfba8c4def54e1ca81a3d8"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79eacf6fe169bd54e6178dc74bd7c504f795"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79eae6581df62f5da9ab88149ec8049d7213"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79eaed594545b8a4e2c0e0703b4b9d3ebb73"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79eaf75bca3db10d28611a9ffa8637a4488e"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79eaf85af15795d80c07cdff711ac172be57"></a>
<a id="ausb__audio_8h_html_ad73e9e9b72475496b6c483f78605e79eaff9805f63bd75e000dd08652c6dc913b"></a>
<a id="ausb__audio_8h_html_ade80a3c7e04049fd27e4e39269baaeeb"></a>
<a id="ausb__audio_8h_html_ade80a3c7e04049fd27e4e39269baaeeba6ac0131cbfcbe01e06cde15e6fdb4e5e"></a>
<a id="ausb__audio_8h_html_ade80a3c7e04049fd27e4e39269baaeeba8cefa4d87a243d6ee01b0c72bc39fe84"></a>
<a id="ausb__audio_8h_html_ade80a3c7e04049fd27e4e39269baaeebab7df49ec3cb5b7a7f19c7f0ec9161de4"></a>
<a id="ausb__audio_8h_html_ade80a3c7e04049fd27e4e39269baaeebada7521b50fd74ef8bfb77485976e0e0a"></a>
<a id="ausb__audio_8h_html_af1874c929638325e9e2a44da0e613041"></a>
<a id="ausb__audio_8h_html_af314d5beb1d16377855313d46148a86c"></a>
<a id="ausb__ch9_8h_html"></a>

```c
/*
 * USB audio class core header
 *
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USB_CLASS_AUDIO_H_
#define ZEPHYR_INCLUDE_USB_CLASS_AUDIO_H_

#include <zephyr/usb/usb_ch9.h>
#include <zephyr/device.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/util.h>

enum usb_audio_int_subclass_codes {
        USB_AUDIO_SUBCLASS_UNDEFINED    = 0x00,
        USB_AUDIO_AUDIOCONTROL          = 0x01,
        USB_AUDIO_AUDIOSTREAMING        = 0x02,
        USB_AUDIO_MIDISTREAMING         = 0x03
};

enum usb_audio_cs_ac_int_desc_subtypes {
        USB_AUDIO_AC_DESCRIPTOR_UNDEFINED       = 0x00,
        USB_AUDIO_HEADER                        = 0x01,
        USB_AUDIO_INPUT_TERMINAL                = 0x02,
        USB_AUDIO_OUTPUT_TERMINAL               = 0x03,
        USB_AUDIO_MIXER_UNIT                    = 0x04,
        USB_AUDIO_SELECTOR_UNIT                 = 0x05,
        USB_AUDIO_FEATURE_UNIT                  = 0x06,
        USB_AUDIO_PROCESSING_UNIT               = 0x07,
        USB_AUDIO_EXTENSION_UNIT                = 0x08
};

enum usb_audio_cs_as_int_desc_subtypes {
        USB_AUDIO_AS_DESCRIPTOR_UNDEFINED       = 0x00,
        USB_AUDIO_AS_GENERAL                    = 0x01,
        USB_AUDIO_FORMAT_TYPE                   = 0x02,
        USB_AUDIO_FORMAT_SPECIFIC               = 0x03
};

enum usb_audio_cs_req_codes {
        USB_AUDIO_REQUEST_CODE_UNDEFINED        = 0x00,
        USB_AUDIO_SET_CUR                       = 0x01,
        USB_AUDIO_GET_CUR                       = 0x81,
        USB_AUDIO_SET_MIN                       = 0x02,
        USB_AUDIO_GET_MIN                       = 0x82,
        USB_AUDIO_SET_MAX                       = 0x03,
        USB_AUDIO_GET_MAX                       = 0x83,
        USB_AUDIO_SET_RES                       = 0x04,
        USB_AUDIO_GET_RES                       = 0x84,
        USB_AUDIO_SET_MEM                       = 0x05,
        USB_AUDIO_GET_MEM                       = 0x85,
        USB_AUDIO_GET_STAT                      = 0xFF
};

enum usb_audio_fucs {
        USB_AUDIO_FU_CONTROL_UNDEFINED          = 0x00,
        USB_AUDIO_FU_MUTE_CONTROL               = 0x01,
        USB_AUDIO_FU_VOLUME_CONTROL             = 0x02,
        USB_AUDIO_FU_BASS_CONTROL               = 0x03,
        USB_AUDIO_FU_MID_CONTROL                = 0x04,
        USB_AUDIO_FU_TREBLE_CONTROL             = 0x05,
        USB_AUDIO_FU_GRAPHIC_EQUALIZER_CONTROL  = 0x06,
        USB_AUDIO_FU_AUTOMATIC_GAIN_CONTROL     = 0x07,
        USB_AUDIO_FU_DELAY_CONTROL              = 0x08,
        USB_AUDIO_FU_BASS_BOOST_CONTROL         = 0x09,
        USB_AUDIO_FU_LOUDNESS_CONTROL           = 0x0A
};

enum usb_audio_terminal_types {
        USB_AUDIO_USB_UNDEFINED   = 0x0100,
        USB_AUDIO_USB_STREAMING   = 0x0101,
        USB_AUDIO_USB_VENDOR_SPEC = 0x01FF,

        USB_AUDIO_IN_UNDEFINED      = 0x0200,
        USB_AUDIO_IN_MICROPHONE     = 0x0201,
        USB_AUDIO_IN_DESKTOP_MIC    = 0x0202,
        USB_AUDIO_IN_PERSONAL_MIC   = 0x0203,
        USB_AUDIO_IN_OM_DIR_MIC     = 0x0204,
        USB_AUDIO_IN_MIC_ARRAY      = 0x0205,
        USB_AUDIO_IN_PROC_MIC_ARRAY = 0x0205,

        USB_AUDIO_OUT_UNDEFINED         = 0x0300,
        USB_AUDIO_OUT_SPEAKER           = 0x0301,
        USB_AUDIO_OUT_HEADPHONES        = 0x0302,
        USB_AUDIO_OUT_HEAD_AUDIO        = 0x0303,
        USB_AUDIO_OUT_DESKTOP_SPEAKER   = 0x0304,
        USB_AUDIO_OUT_ROOM_SPEAKER      = 0x0305,
        USB_AUDIO_OUT_COMM_SPEAKER      = 0x0306,
        USB_AUDIO_OUT_LOW_FREQ_SPEAKER  = 0x0307,

        USB_AUDIO_IO_UNDEFINED                  = 0x0400,
        USB_AUDIO_IO_HANDSET                    = 0x0401,
        USB_AUDIO_IO_HEADSET                    = 0x0402,
        USB_AUDIO_IO_SPEAKERPHONE_ECHO_NONE     = 0x0403,
        USB_AUDIO_IO_SPEAKERPHONE_ECHO_SUP      = 0x0404,
        USB_AUDIO_IO_SPEAKERPHONE_ECHO_CAN      = 0x0405,
};

enum usb_audio_direction {
        USB_AUDIO_IN = 0x00,
        USB_AUDIO_OUT = 0x01
};

struct usb_audio_fu_evt {
        enum usb_audio_direction dir;
        enum usb_audio_fucs cs;
        uint8_t channel;
        uint8_t val_len;
        const void *val;
};

typedef void (*usb_audio_data_request_cb_t)(const struct device *dev);

typedef void (*usb_audio_data_completion_cb_t)(const struct device *dev,
                                               struct net_buf *buffer,
                                               size_t size);

typedef void (*usb_audio_feature_updated_cb_t)(const struct device *dev,
                                               const struct usb_audio_fu_evt *evt);

struct usb_audio_ops {
        usb_audio_data_request_cb_t data_request_cb;

        usb_audio_data_completion_cb_t data_written_cb;

        usb_audio_data_completion_cb_t data_received_cb;

        usb_audio_feature_updated_cb_t feature_update_cb;
};

__deprecated size_t usb_audio_get_in_frame_size(const struct device *dev);

__deprecated void usb_audio_register(const struct device *dev,
                        const struct usb_audio_ops *ops);

__deprecated int usb_audio_send(const struct device *dev, struct net_buf *buffer,
                   size_t len);

#endif /* ZEPHYR_INCLUDE_USB_CLASS_AUDIO_H_ */
```

## 234.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

USB 音频类核心头文件（USB audio class core header）。

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 339 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USB_CLASS_AUDIO_H_`。

## 234.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../usb/P142_旧版USB音频头文件接口.md)
- [zephyr/usb/usb_ch9.h](../usb/P172_USB标准请求与描述符常量.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [usb_audio_int_subclass_codes](../usb/P142_旧版USB音频头文件接口.md#a4885d280ebe68e42cf068524038ec582)
- [USB_AUDIO_SUBCLASS_UNDEFINED](../usb/P142_旧版USB音频头文件接口.md#a4885d280ebe68e42cf068524038ec582aba82b7b28c0ad0ecf125695bd1f35db2)
- [USB_AUDIO_AUDIOCONTROL](../usb/P142_旧版USB音频头文件接口.md#a4885d280ebe68e42cf068524038ec582aabd72d1d6016fbe1e37788f37c1c8cac)
- [USB_AUDIO_AUDIOSTREAMING](../usb/P142_旧版USB音频头文件接口.md#a4885d280ebe68e42cf068524038ec582a8f451ebdab0c5a1d930ce5808b6f0892)
- [USB_AUDIO_MIDISTREAMING](../usb/P142_旧版USB音频头文件接口.md#a4885d280ebe68e42cf068524038ec582a589d9e4883f109f787517a017d6187b2)
- [usb_audio_cs_ac_int_desc_subtypes](../usb/P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9a)
- [USB_AUDIO_AC_DESCRIPTOR_UNDEFINED](../usb/P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aa2eee02b3652783891eb878bd0a02227d)
- [USB_AUDIO_HEADER](../usb/P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aa533df0f1df0cd0ba91f05922780c3f51)
- [USB_AUDIO_INPUT_TERMINAL](../usb/P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aa80b350d862e1fe02fb04572481ae6343)
- [USB_AUDIO_OUTPUT_TERMINAL](../usb/P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aa357c88ef81ee69875f4cbbf5610fd48f)
- [USB_AUDIO_MIXER_UNIT](../usb/P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aa10f58b16088a3218eb4ed8c31ffd9dfe)
- [USB_AUDIO_SELECTOR_UNIT](../usb/P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aab01072ed5bad284a34cf9a2e8b2098e5)
- [USB_AUDIO_FEATURE_UNIT](../usb/P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aad06ebbc1c9c35ec35dca8c7bb95c52c7)
- [USB_AUDIO_PROCESSING_UNIT](../usb/P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aae5e4af543ede652cda987db1ca5b10ab)
- [USB_AUDIO_EXTENSION_UNIT](../usb/P142_旧版USB音频头文件接口.md#ab5e6c883af53c089c7fcdee4d2249d9aad1f55fd97d0217453704ba61a7357ca1)
- [usb_audio_cs_as_int_desc_subtypes](../usb/P142_旧版USB音频头文件接口.md#ade80a3c7e04049fd27e4e39269baaeeb)
- [USB_AUDIO_AS_DESCRIPTOR_UNDEFINED](../usb/P142_旧版USB音频头文件接口.md#ade80a3c7e04049fd27e4e39269baaeeba6ac0131cbfcbe01e06cde15e6fdb4e5e)
- [USB_AUDIO_AS_GENERAL](../usb/P142_旧版USB音频头文件接口.md#ade80a3c7e04049fd27e4e39269baaeeba8cefa4d87a243d6ee01b0c72bc39fe84)
- [USB_AUDIO_FORMAT_TYPE](../usb/P142_旧版USB音频头文件接口.md#ade80a3c7e04049fd27e4e39269baaeebab7df49ec3cb5b7a7f19c7f0ec9161de4)
- [USB_AUDIO_FORMAT_SPECIFIC](../usb/P142_旧版USB音频头文件接口.md#ade80a3c7e04049fd27e4e39269baaeebada7521b50fd74ef8bfb77485976e0e0a)
- [usb_audio_cs_req_codes](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ad)
- [USB_AUDIO_REQUEST_CODE_UNDEFINED](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6e5e1dd7fd6292ba8bcc4564223b8220)
- [USB_AUDIO_SET_CUR](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada1088106727c5c6d850dd2ab98a7b454d)
- [USB_AUDIO_GET_CUR](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada8d2d8fdf1663f9691f566245062b2cf6)
- [USB_AUDIO_SET_MIN](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6f5faa411e92cdeacdc521bd05b4bfab)
- [USB_AUDIO_GET_MIN](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada2e921e391ec9f89345e6b63ad1fd5da6)
- [USB_AUDIO_SET_MAX](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada96ac36a0735d03e3addf0fe540903707)
- [USB_AUDIO_GET_MAX](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6adac027c9e016ad88a9c135a0c1050921bb)
- [USB_AUDIO_SET_RES](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada1945ba97faeff43f68bd4918be76a4e7)
- [USB_AUDIO_GET_RES](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada4ce3135409f73b58295898087e9ff485)
- [USB_AUDIO_SET_MEM](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6adae89a907671d2940da6bb4c58cf9a7fd0)
- [USB_AUDIO_GET_MEM](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada6e3db81f03ab284c82c254952c3f7259)
- [USB_AUDIO_GET_STAT](../usb/P142_旧版USB音频头文件接口.md#ad6eb1c3ec75aef329ea973d1cb4dc6ada229701fae8fdc58a530ffcdd1cdea109)
- [usb_audio_fucs](../usb/P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2)
- [USB_AUDIO_FU_CONTROL_UNDEFINED](../usb/P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a08d27821af6c7d875351ec8f58082794)
- [USB_AUDIO_FU_MUTE_CONTROL](../usb/P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2adb4f2720ad78a26d22279a45df56b43d)
- [USB_AUDIO_FU_VOLUME_CONTROL](../usb/P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a6d258289b44ddeb1153168fafb92c0d8)
- [USB_AUDIO_FU_BASS_CONTROL](../usb/P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a2b14e19e39d96c31764f89128b393efc)
- [USB_AUDIO_FU_MID_CONTROL](../usb/P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2acfcc2072d11863eaedb68f87a93eb601)
- [USB_AUDIO_FU_TREBLE_CONTROL](../usb/P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a657b1e5689be60c2f1ce6d3d2cb68f89)
- [USB_AUDIO_FU_GRAPHIC_EQUALIZER_CONTROL](../usb/P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a26c439798671f4efe7b6469f3dcd37c5)
- [USB_AUDIO_FU_AUTOMATIC_GAIN_CONTROL](../usb/P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a9e9d8f03326339a9a5e212aad42f984f)
- [USB_AUDIO_FU_DELAY_CONTROL](../usb/P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2aef98729fa59119eb0e0cbed2e6a992da)
- [USB_AUDIO_FU_BASS_BOOST_CONTROL](../usb/P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2a1c23bc45ef27b6acf87da3c68281d2a3)
- [USB_AUDIO_FU_LOUDNESS_CONTROL](../usb/P142_旧版USB音频头文件接口.md#a4d49f239cc36daf8bd0cfa36c5fb75d2adae061d51c1df5d03cc47b7b2c412f1d)
- [usb_audio_terminal_types](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79e)
- [USB_AUDIO_USB_UNDEFINED](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eaa0fbe557eba975cb5e368e199ea4f6d4)
- [USB_AUDIO_USB_STREAMING](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eaad81dbd6f39554f52c3912755643d661)
- [USB_AUDIO_USB_VENDOR_SPEC](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea64205001486011d22c1ec0abd382a486)
- [USB_AUDIO_IN_UNDEFINED](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eaf85af15795d80c07cdff711ac172be57)
- [USB_AUDIO_IN_MICROPHONE](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea699cefac29e9d9c60f53562c7ad7050d)
- [USB_AUDIO_IN_DESKTOP_MIC](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea3140dd357e3093db21f581226a6b000a)
- [USB_AUDIO_IN_PERSONAL_MIC](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea3cace6841265454e604513ebba78f749)
- [USB_AUDIO_IN_OM_DIR_MIC](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea456a90d55e1b271698516d89e8ba7f5b)
- [USB_AUDIO_IN_MIC_ARRAY](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea2eaf530492705b7e493e5d746752c262)
- [USB_AUDIO_IN_PROC_MIC_ARRAY](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eac565b3d090c71949c1e1423bb8529c86)
- [USB_AUDIO_OUT_UNDEFINED](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea64f43c7efb785a88f72302d2ad8d00f0)
- [USB_AUDIO_OUT_SPEAKER](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea349881bce5285d61f886aec8fc2bf84c)
- [USB_AUDIO_OUT_HEADPHONES](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eac551e3ea3e21ddf057062fe7d05b3ec9)
- [USB_AUDIO_OUT_HEAD_AUDIO](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eaed594545b8a4e2c0e0703b4b9d3ebb73)
- [USB_AUDIO_OUT_DESKTOP_SPEAKER](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eacf6fe169bd54e6178dc74bd7c504f795)
- [USB_AUDIO_OUT_ROOM_SPEAKER](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eae6581df62f5da9ab88149ec8049d7213)
- [USB_AUDIO_OUT_COMM_SPEAKER](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eaff9805f63bd75e000dd08652c6dc913b)
- [USB_AUDIO_OUT_LOW_FREQ_SPEAKER](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea8b48c4993389b7f5a08d55b68b924480)
- [USB_AUDIO_IO_UNDEFINED](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eac740f1b3cfcfba8c4def54e1ca81a3d8)
- [USB_AUDIO_IO_HANDSET](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea24f6c5657c301871089dc8eac3b5d207)
- [USB_AUDIO_IO_HEADSET](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eaf75bca3db10d28611a9ffa8637a4488e)
- [USB_AUDIO_IO_SPEAKERPHONE_ECHO_NONE](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea232edf193a4f755d8821c51001d11f1d)
- [USB_AUDIO_IO_SPEAKERPHONE_ECHO_SUP](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79eab7f8515fb0154f5b0e038f485bdadaf6)
- [USB_AUDIO_IO_SPEAKERPHONE_ECHO_CAN](../usb/P142_旧版USB音频头文件接口.md#ad73e9e9b72475496b6c483f78605e79ea319eef3f2a59242b0c8dd5ca50212e14)
- [usb_audio_direction](../usb/P142_旧版USB音频头文件接口.md#acbdc8b284d108983fb204cbd679043bb)
- [USB_AUDIO_IN](../usb/P142_旧版USB音频头文件接口.md#acbdc8b284d108983fb204cbd679043bbab2ce7b1140be0d960ab2754bc8e262dd)
- [USB_AUDIO_OUT](../usb/P142_旧版USB音频头文件接口.md#acbdc8b284d108983fb204cbd679043bba0f0e91f9580d03853432259d74f108ba)
- [usb_audio_fu_evt](../usb/P143_旧版USB音频功能单元事件.md)
- [dir](../usb/P143_旧版USB音频功能单元事件.md#a5baf5d4e2a39337dc9c21c4465d5ad8e)
- [cs](../usb/P143_旧版USB音频功能单元事件.md#a1cb4849aae8b9a4e667ed126e9bce26b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [channel](../usb/P143_旧版USB音频功能单元事件.md#a9313b39f178c8a86d680a950ce505713)
- [val_len](../usb/P143_旧版USB音频功能单元事件.md#a6ef19bf7d37c3d636edba243dac8ecb2)
- [val](../usb/P143_旧版USB音频功能单元事件.md#a47c6c7c00fac32a04bffd251d715dc39)
- [usb_audio_data_request_cb_t](../usb/P142_旧版USB音频头文件接口.md#a8f289f2b4d0a7d3accdc6308cb5661e8)
- [device](../device_reference/P002_设备对象结构.md)
- [usb_audio_data_completion_cb_t](../usb/P142_旧版USB音频头文件接口.md#a57bc8c499f03323db38f5604f8ebcda2)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [size](../network_core_model_reference/P046_net_buf_结构体.md#a1522d81a002804223e25300a6961f527)
- [usb_audio_feature_updated_cb_t](../usb/P142_旧版USB音频头文件接口.md#a692362e834622532b7be71d5e0bdc219)
- [usb_audio_ops](../usb/P144_旧版USB音频回调接口.md)
- [data_request_cb](../usb/P144_旧版USB音频回调接口.md#a6ee19a7aef47561f14981b7e7ebd8ac7)
- [data_written_cb](../usb/P144_旧版USB音频回调接口.md#a2752018597ba5bd4e9a80d1ae650bf8b)
- [data_received_cb](../usb/P144_旧版USB音频回调接口.md#a483af21f54537bef1a6ae3be2cd3717d)
- [feature_update_cb](../usb/P144_旧版USB音频回调接口.md#a861823185efb5c9a06b900799adb9efb)
- [usb_audio_get_in_frame_size](../usb/P142_旧版USB音频头文件接口.md#af314d5beb1d16377855313d46148a86c)
- [usb_audio_register](../usb/P142_旧版USB音频头文件接口.md#a6a69824dadab0c36bb6a6ce378da8ba5)
- [usb_audio_send](../usb/P142_旧版USB音频头文件接口.md#af1874c929638325e9e2a44da0e613041)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [net_buf::size](../network_core_model_reference/P046_net_buf_结构体.md#a1522d81a002804223e25300a6961f527)
- [usb_audio_fu_evt::cs](../usb/P143_旧版USB音频功能单元事件.md#a1cb4849aae8b9a4e667ed126e9bce26b)
- [usb_audio_fu_evt::val](../usb/P143_旧版USB音频功能单元事件.md#a47c6c7c00fac32a04bffd251d715dc39)
- [usb_audio_fu_evt::dir](../usb/P143_旧版USB音频功能单元事件.md#a5baf5d4e2a39337dc9c21c4465d5ad8e)
- [usb_audio_fu_evt::val_len](../usb/P143_旧版USB音频功能单元事件.md#a6ef19bf7d37c3d636edba243dac8ecb2)
- [usb_audio_fu_evt::channel](../usb/P143_旧版USB音频功能单元事件.md#a9313b39f178c8a86d680a950ce505713)
- [usb_audio_ops::data_written_cb](../usb/P144_旧版USB音频回调接口.md#a2752018597ba5bd4e9a80d1ae650bf8b)
- [usb_audio_ops::data_received_cb](../usb/P144_旧版USB音频回调接口.md#a483af21f54537bef1a6ae3be2cd3717d)
- [usb_audio_ops::data_request_cb](../usb/P144_旧版USB音频回调接口.md#a6ee19a7aef47561f14981b7e7ebd8ac7)
- [usb_audio_ops::feature_update_cb](../usb/P144_旧版USB音频回调接口.md#a861823185efb5c9a06b900799adb9efb)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [usb_ch9.h](../usb/P172_USB标准请求与描述符常量.md)

---

[上一章](P233_udp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P235_usb_bc12.h_源码浏览.md)
