---
id: learning.zephyr-docs.api-source-reference.page-66
title: biometrics.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/biometrics_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_biometrics.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/biometrics_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/biometrics_8h.html)。

## 66.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
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
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00088"></a>
<a id="l00093"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00133"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00146"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="foldopen00243"></a>
<a id="l00243"></a>
<a id="l00247"></a>
<a id="l00251"></a>
<a id="l00255"></a>
<a id="l00259"></a>
<a id="l00263"></a>
<a id="l00267"></a>
<a id="l00271"></a>
<a id="l00275"></a>
<a id="l00279"></a>
<a id="l00283"></a>
<a id="l00287"></a>
<a id="l00291"></a>
<a id="l00295"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00305"></a>
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
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00364"></a>
<a id="l00365"></a>
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
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__biometrics__interface__backend_html_ga182b3b06e09416ba826a46ec346b57d1"></a>
<a id="agroup__biometrics__interface__backend_html_ga2515c347864644dea3906fc3a25c155e"></a>
<a id="agroup__biometrics__interface__backend_html_ga36b3ac91aceeca57ccaaa78619ab603f"></a>
<a id="agroup__biometrics__interface__backend_html_ga38a8a21a46a8e252792951ce8312294a"></a>
<a id="agroup__biometrics__interface__backend_html_ga5db0eae1ba88eef3d2fcb99f4a75ff50"></a>
<a id="agroup__biometrics__interface__backend_html_ga5f49256b2d8abf90fdedb33dcd84a95e"></a>
<a id="agroup__biometrics__interface__backend_html_ga70253fb65673c4c95c22896ca1bb0641"></a>
<a id="agroup__biometrics__interface__backend_html_ga8196c59e50e8f093383c7a354ceaf694"></a>
<a id="agroup__biometrics__interface__backend_html_gaa379e427029685e4c73a9dd9ccd3f6c4"></a>
<a id="agroup__biometrics__interface__backend_html_gaa86339893ac58e9a1480d013605c2718"></a>
<a id="agroup__biometrics__interface__backend_html_gab69ee26aff13e80183e5a929d4f20277"></a>
<a id="agroup__biometrics__interface__backend_html_gad0aa92ba1e326e98f5963206d548cda3"></a>
<a id="agroup__biometrics__interface__backend_html_gad7f71482bb3407bcedf37a7b4b5633be"></a>
<a id="agroup__biometrics__interface__backend_html_gaf70dbdc914f9a6b89574f1947d821424"></a>
<a id="agroup__biometrics__interface_html_ga1fa103e8d4a55ffba82f1b0f65634c16"></a>
<a id="agroup__biometrics__interface_html_ga243ad98c425edb68b425be8639b6fcac"></a>
<a id="agroup__biometrics__interface_html_ga2a5c36eca939da337f38b54b44ef16eb"></a>
<a id="agroup__biometrics__interface_html_ga330af9905835af25b41e2e9b7fff11e6"></a>
<a id="agroup__biometrics__interface_html_ga4ca9b34414ff86b2a5271bbc4c2563df"></a>
<a id="agroup__biometrics__interface_html_ga51d358b76f65d2776dfe4fed79e4afcd"></a>
<a id="agroup__biometrics__interface_html_ga65bdfd912acf5e9503d0f91d5842cf8c"></a>
<a id="agroup__biometrics__interface_html_ga83c3fbd41de6c4f3739880fceadea96f"></a>
<a id="agroup__biometrics__interface_html_ga8be2ec31d1848891327a44cda198b86e"></a>
<a id="agroup__biometrics__interface_html_ga96ebb7910e37418080a121d043a18bab"></a>
<a id="agroup__biometrics__interface_html_ga9de5325164b6ed98427275662a7bb07e"></a>
<a id="agroup__biometrics__interface_html_gaa335d1d790f5ce609b6de57eaeb1399c"></a>
<a id="agroup__biometrics__interface_html_gab5c9975eff4a737f75710e2f43df39b2"></a>
<a id="agroup__biometrics__interface_html_gaca4596921ea8f1554215d4994da5537e"></a>
<a id="agroup__biometrics__interface_html_gad84df8a20c10cfacd4b7e547f1b4ca24"></a>
<a id="agroup__biometrics__interface_html_gae323da0884660fba5b7bcb9b210aec00"></a>
<a id="agroup__biometrics__interface_html_gaf2d6cf698d301c58dbcfb782af96d205"></a>
<a id="agroup__biometrics__interface_html_gafe560b9baea81cbad071ead5015721d0"></a>
<a id="agroup__biometrics__interface_html_gga83c3fbd41de6c4f3739880fceadea96fa49d40e2d9ade1192b968fba235449da7"></a>
<a id="agroup__biometrics__interface_html_gga83c3fbd41de6c4f3739880fceadea96fa54de3799271229142ffa8e099fbf9ae2"></a>
<a id="agroup__biometrics__interface_html_gga83c3fbd41de6c4f3739880fceadea96faa59be78efbd9b2d4c8a7b8720b04967e"></a>
<a id="agroup__biometrics__interface_html_gga83c3fbd41de6c4f3739880fceadea96fab2c1b886bd5c42fa10c488e492bf571a"></a>
<a id="agroup__biometrics__interface_html_gga96ebb7910e37418080a121d043a18baba06b785aa0f5a09c137c9f5b35d28ff59"></a>
<a id="agroup__biometrics__interface_html_gga96ebb7910e37418080a121d043a18baba2b78962d7f87642eccdd98176fa705da"></a>
<a id="agroup__biometrics__interface_html_gga96ebb7910e37418080a121d043a18baba30138a67266a6765908016f70a14336e"></a>
<a id="agroup__biometrics__interface_html_gga96ebb7910e37418080a121d043a18baba946f0e361f258e007fdc003946b21291"></a>
<a id="agroup__biometrics__interface_html_ggad84df8a20c10cfacd4b7e547f1b4ca24a677c053cb520e1b07da0cc884c3053ef"></a>
<a id="agroup__biometrics__interface_html_ggad84df8a20c10cfacd4b7e547f1b4ca24aae262097565b0a8420b1658f362d8e81"></a>
<a id="agroup__biometrics__interface_html_ggafe560b9baea81cbad071ead5015721d0a29e1b51dfbda37a58642630b44a59ece"></a>
<a id="agroup__biometrics__interface_html_ggafe560b9baea81cbad071ead5015721d0a3770042eafa778b907f7598d762f8ca3"></a>
<a id="agroup__biometrics__interface_html_ggafe560b9baea81cbad071ead5015721d0a8af3a6b4fb231c8991543f357a318eec"></a>
<a id="agroup__biometrics__interface_html_ggafe560b9baea81cbad071ead5015721d0aa0b5c4fb004ee442265819f1ad1f888f"></a>
<a id="agroup__biometrics__interface_html_ggafe560b9baea81cbad071ead5015721d0ac7cc9f7e2420227e96d33b526665cda0"></a>
<a id="agroup__biometrics__interface_html_ggafe560b9baea81cbad071ead5015721d0aceaac5e1b094da0b92a927f9d0379071"></a>
<a id="agroup__biometrics__interface_html_ggafe560b9baea81cbad071ead5015721d0aef92b844ead708b1337fa983278e4499"></a>
<a id="agroup__biometrics__interface_html_ggafe560b9baea81cbad071ead5015721d0af4ebcb6c0c73f05f6f6279d71d76a3d5"></a>
<a id="agroup__biometrics__interface_html_ggafe560b9baea81cbad071ead5015721d0afa83aa1fd1d91ba0753e46d9cf8e098d"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac58f2c111cc9989c86db2a7dc4fd84ca"></a>
<a id="astructbiometric__capabilities_html"></a>
<a id="astructbiometric__capabilities_html_a05bdbadc7e38bc72503a556804ed04a5"></a>
<a id="astructbiometric__capabilities_html_a2bc185c7fb7623f7fe65ee4c9b30cc62"></a>
<a id="astructbiometric__capabilities_html_a6e6afaa6381f27e2635f60af531da094"></a>
<a id="astructbiometric__capabilities_html_a9b7fd2768df210ac02f3a104ec1db6c9"></a>
<a id="astructbiometric__capabilities_html_ad8c0934aec564a9e472ab75fb7e6163f"></a>
<a id="astructbiometric__capture__result_html"></a>
<a id="astructbiometric__capture__result_html_a97b590dec9a83f835c5c71e64834b8f6"></a>
<a id="astructbiometric__capture__result_html_adf436e8f4aca8d86df613beb5fd3f821"></a>
<a id="astructbiometric__capture__result_html_ae2b9f021e8becd7a5339248f6b39162d"></a>
<a id="astructbiometric__driver__api_html"></a>
<a id="astructbiometric__driver__api_html_a0b03da9661ffbd2980230f7cdcd63440"></a>
<a id="astructbiometric__driver__api_html_a1312d877f54c4a58fca34e657d4ed76e"></a>
<a id="astructbiometric__driver__api_html_a18b95022f52d21655ffc4f8d38d60ab8"></a>
<a id="astructbiometric__driver__api_html_a267615faeb182198f3af7d5328baf29e"></a>
<a id="astructbiometric__driver__api_html_a87e0be3ddc66a4b8d2bd5c28f16be49c"></a>
<a id="astructbiometric__driver__api_html_a8e3ce1b03251fd828b5df85e4c573080"></a>
<a id="astructbiometric__driver__api_html_a94f6375942786ee4798ea55d961398a4"></a>
<a id="astructbiometric__driver__api_html_aa9e731ce70feadf0bb9ee2a6c76c19ee"></a>
<a id="astructbiometric__driver__api_html_ab2b7f89b60294aa916be9d4bc016f986"></a>
<a id="astructbiometric__driver__api_html_acc200c2bb820d4114e9ae282c31d5dbf"></a>
<a id="astructbiometric__driver__api_html_ade705f56f4dc7d95e0b296a4bb4d4163"></a>
<a id="astructbiometric__driver__api_html_ade76db1b6d6bd505b295daa44c61ddca"></a>
<a id="astructbiometric__driver__api_html_ae546cb778af0bbbfa48d9704eb658be8"></a>
<a id="astructbiometric__driver__api_html_ae89d8eaf26b0563be483d87488d690a4"></a>
<a id="astructbiometric__match__result_html"></a>
<a id="astructbiometric__match__result_html_ada317052641352f1f7d8871bc025c1d0"></a>
<a id="astructbiometric__match__result_html_adb749246db9d80a7f00813633e497894"></a>
<a id="astructbiometric__match__result_html_adfaeb77884875c6339a93e5b152a333d"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructk__timeout__t_html"></a>

```c
/*
 * Copyright (c) 2025 Siratul Islam <email@sirat.me>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_BIOMETRICS_H_
#define ZEPHYR_INCLUDE_DRIVERS_BIOMETRICS_H_


#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <errno.h>
#include <stddef.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

enum biometric_sensor_type {
        BIOMETRIC_TYPE_FINGERPRINT,
        BIOMETRIC_TYPE_IRIS,
        BIOMETRIC_TYPE_FACE,
        BIOMETRIC_TYPE_VOICE,
};

enum biometric_match_mode {
        BIOMETRIC_MATCH_VERIFY,
        BIOMETRIC_MATCH_IDENTIFY,
};

#define BIOMETRIC_STORAGE_DEVICE BIT(0)
#define BIOMETRIC_STORAGE_HOST   BIT(1)

enum biometric_led_state {
        BIOMETRIC_LED_OFF,
        BIOMETRIC_LED_ON,
        BIOMETRIC_LED_BLINK,
        BIOMETRIC_LED_BREATHE
};

enum biometric_attribute {
        BIOMETRIC_ATTR_MATCH_THRESHOLD,
        BIOMETRIC_ATTR_ENROLLMENT_QUALITY,
        BIOMETRIC_ATTR_SECURITY_LEVEL,
        BIOMETRIC_ATTR_TIMEOUT_MS,
        BIOMETRIC_ATTR_ANTI_SPOOF_LEVEL,
        BIOMETRIC_ATTR_IMAGE_QUALITY,
        BIOMETRIC_ATTR_COMMON_COUNT,
        BIOMETRIC_ATTR_PRIV_START = BIOMETRIC_ATTR_COMMON_COUNT,
        BIOMETRIC_ATTR_MAX = INT16_MAX,
};

struct biometric_capabilities {
        enum biometric_sensor_type type;
        uint16_t max_templates;
        uint16_t template_size;
        uint8_t storage_modes;
        uint8_t enrollment_samples_required;
};

struct biometric_match_result {
        int32_t confidence;
        uint16_t template_id;
        uint8_t image_quality;
};

struct biometric_capture_result {
        uint8_t samples_captured;
        uint8_t samples_required;
        uint8_t quality;
};


typedef int (*biometric_api_get_capabilities)(const struct device *dev,
                                              struct biometric_capabilities *caps);

typedef int (*biometric_api_attr_set)(const struct device *dev, enum biometric_attribute attr,
                                      int32_t val);

typedef int (*biometric_api_attr_get)(const struct device *dev, enum biometric_attribute attr,
                                      int32_t *val);

typedef int (*biometric_api_enroll_start)(const struct device *dev, uint16_t template_id);

typedef int (*biometric_api_enroll_capture)(const struct device *dev, k_timeout_t timeout,
                                            struct biometric_capture_result *result);

typedef int (*biometric_api_enroll_finalize)(const struct device *dev);

typedef int (*biometric_api_enroll_abort)(const struct device *dev);

typedef int (*biometric_api_template_store)(const struct device *dev, uint16_t id,
                                            const uint8_t *data, size_t size);

typedef int (*biometric_api_template_read)(const struct device *dev, uint16_t id, uint8_t *data,
                                           size_t size);

typedef int (*biometric_api_template_delete)(const struct device *dev, uint16_t id);

typedef int (*biometric_api_template_delete_all)(const struct device *dev);

typedef int (*biometric_api_template_list)(const struct device *dev, uint16_t *ids,
                                           size_t max_count, size_t *actual_count);

typedef int (*biometric_api_match)(const struct device *dev, enum biometric_match_mode mode,
                                   uint16_t template_id, k_timeout_t timeout,
                                   struct biometric_match_result *result);

typedef int (*biometric_api_led_control)(const struct device *dev, enum biometric_led_state state);

__subsystem struct biometric_driver_api {
        biometric_api_get_capabilities get_capabilities;
        biometric_api_attr_set attr_set;
        biometric_api_attr_get attr_get;
        biometric_api_enroll_start enroll_start;
        biometric_api_enroll_capture enroll_capture;
        biometric_api_enroll_finalize enroll_finalize;
        biometric_api_enroll_abort enroll_abort;
        biometric_api_template_store template_store;
        biometric_api_template_read template_read;
        biometric_api_template_delete template_delete;
        biometric_api_template_delete_all template_delete_all;
        biometric_api_template_list template_list;
        biometric_api_match match;
        biometric_api_led_control led_control;
};


__syscall int biometric_get_capabilities(const struct device *dev,
                                         struct biometric_capabilities *caps);

static inline int z_impl_biometric_get_capabilities(const struct device *dev,
                                                    struct biometric_capabilities *caps)
{
        const struct biometric_driver_api *api = DEVICE_API_GET(biometric, dev);

        __ASSERT_NO_MSG(caps != NULL);

        return api->get_capabilities(dev, caps);
}

__syscall int biometric_attr_set(const struct device *dev, enum biometric_attribute attr,
                                 int32_t val);

static inline int z_impl_biometric_attr_set(const struct device *dev, enum biometric_attribute attr,
                                            int32_t val)
{
        const struct biometric_driver_api *api = DEVICE_API_GET(biometric, dev);

        if (api->attr_set == NULL) {
                return -ENOSYS;
        }

        return api->attr_set(dev, attr, val);
}

__syscall int biometric_attr_get(const struct device *dev, enum biometric_attribute attr,
                                 int32_t *val);

static inline int z_impl_biometric_attr_get(const struct device *dev, enum biometric_attribute attr,
                                            int32_t *val)
{
        const struct biometric_driver_api *api = DEVICE_API_GET(biometric, dev);

        __ASSERT_NO_MSG(val != NULL);

        if (api->attr_get == NULL) {
                return -ENOSYS;
        }

        return api->attr_get(dev, attr, val);
}

__syscall int biometric_enroll_start(const struct device *dev, uint16_t template_id);

static inline int z_impl_biometric_enroll_start(const struct device *dev, uint16_t template_id)
{
        return DEVICE_API_GET(biometric, dev)->enroll_start(dev, template_id);
}

__syscall int biometric_enroll_capture(const struct device *dev, k_timeout_t timeout,
                                       struct biometric_capture_result *result);

static inline int z_impl_biometric_enroll_capture(const struct device *dev, k_timeout_t timeout,
                                                  struct biometric_capture_result *result)
{
        return DEVICE_API_GET(biometric, dev)->enroll_capture(dev, timeout, result);
}

__syscall int biometric_enroll_finalize(const struct device *dev);

static inline int z_impl_biometric_enroll_finalize(const struct device *dev)
{
        return DEVICE_API_GET(biometric, dev)->enroll_finalize(dev);
}

__syscall int biometric_enroll_abort(const struct device *dev);

static inline int z_impl_biometric_enroll_abort(const struct device *dev)
{
        const struct biometric_driver_api *api = DEVICE_API_GET(biometric, dev);

        if (api->enroll_abort == NULL) {
                return -ENOSYS;
        }

        return api->enroll_abort(dev);
}

__syscall int biometric_template_store(const struct device *dev, uint16_t id, const uint8_t *data,
                                       size_t size);

static inline int z_impl_biometric_template_store(const struct device *dev, uint16_t id,
                                                  const uint8_t *data, size_t size)
{
        const struct biometric_driver_api *api = DEVICE_API_GET(biometric, dev);

        __ASSERT_NO_MSG(data != NULL);

        if (api->template_store == NULL) {
                return -ENOSYS;
        }

        return api->template_store(dev, id, data, size);
}

__syscall int biometric_template_read(const struct device *dev, uint16_t id, uint8_t *data,
                                      size_t size);

static inline int z_impl_biometric_template_read(const struct device *dev, uint16_t id,
                                                 uint8_t *data, size_t size)
{
        const struct biometric_driver_api *api = DEVICE_API_GET(biometric, dev);

        __ASSERT_NO_MSG(data != NULL);

        if (api->template_read == NULL) {
                return -ENOSYS;
        }

        return api->template_read(dev, id, data, size);
}

__syscall int biometric_template_delete(const struct device *dev, uint16_t id);

static inline int z_impl_biometric_template_delete(const struct device *dev, uint16_t id)
{
        return DEVICE_API_GET(biometric, dev)->template_delete(dev, id);
}

__syscall int biometric_template_delete_all(const struct device *dev);

static inline int z_impl_biometric_template_delete_all(const struct device *dev)
{
        const struct biometric_driver_api *api = DEVICE_API_GET(biometric, dev);

        if (api->template_delete_all == NULL) {
                return -ENOSYS;
        }

        return api->template_delete_all(dev);
}

__syscall int biometric_template_list(const struct device *dev, uint16_t *ids, size_t max_count,
                                      size_t *actual_count);

static inline int z_impl_biometric_template_list(const struct device *dev, uint16_t *ids,
                                                 size_t max_count, size_t *actual_count)
{
        const struct biometric_driver_api *api = DEVICE_API_GET(biometric, dev);

        __ASSERT_NO_MSG(ids != NULL);
        __ASSERT_NO_MSG(actual_count != NULL);

        if (api->template_list == NULL) {
                return -ENOSYS;
        }

        return api->template_list(dev, ids, max_count, actual_count);
}

__syscall int biometric_match(const struct device *dev, enum biometric_match_mode mode,
                              uint16_t template_id, k_timeout_t timeout,
                              struct biometric_match_result *result);

static inline int z_impl_biometric_match(const struct device *dev, enum biometric_match_mode mode,
                                         uint16_t template_id, k_timeout_t timeout,
                                         struct biometric_match_result *result)
{
        return DEVICE_API_GET(biometric, dev)->match(dev, mode, template_id, timeout, result);
}

__syscall int biometric_led_control(const struct device *dev, enum biometric_led_state state);

static inline int z_impl_biometric_led_control(const struct device *dev,
                                               enum biometric_led_state state)
{
        const struct biometric_driver_api *api = DEVICE_API_GET(biometric, dev);

        if (api->led_control == NULL) {
                return -ENOSYS;
        }

        return api->led_control(dev, state);
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/biometrics.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_BIOMETRICS_H_ */
```

## 66.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Siratul Islam <email@sirat.me>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 667 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_BIOMETRICS_H_`。

## 66.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/biometrics_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [biometric_sensor_type](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga96ebb7910e37418080a121d043a18bab)
- [BIOMETRIC_TYPE_FINGERPRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga96ebb7910e37418080a121d043a18baba946f0e361f258e007fdc003946b21291)
- [BIOMETRIC_TYPE_IRIS](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga96ebb7910e37418080a121d043a18baba2b78962d7f87642eccdd98176fa705da)
- [BIOMETRIC_TYPE_FACE](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga96ebb7910e37418080a121d043a18baba06b785aa0f5a09c137c9f5b35d28ff59)
- [BIOMETRIC_TYPE_VOICE](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga96ebb7910e37418080a121d043a18baba30138a67266a6765908016f70a14336e)
- [biometric_match_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gad84df8a20c10cfacd4b7e547f1b4ca24)
- [BIOMETRIC_MATCH_VERIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggad84df8a20c10cfacd4b7e547f1b4ca24aae262097565b0a8420b1658f362d8e81)
- [BIOMETRIC_MATCH_IDENTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggad84df8a20c10cfacd4b7e547f1b4ca24a677c053cb520e1b07da0cc884c3053ef)
- [biometric_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga83c3fbd41de6c4f3739880fceadea96f)
- [BIOMETRIC_LED_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga83c3fbd41de6c4f3739880fceadea96fab2c1b886bd5c42fa10c488e492bf571a)
- [BIOMETRIC_LED_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga83c3fbd41de6c4f3739880fceadea96fa54de3799271229142ffa8e099fbf9ae2)
- [BIOMETRIC_LED_BLINK](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga83c3fbd41de6c4f3739880fceadea96faa59be78efbd9b2d4c8a7b8720b04967e)
- [BIOMETRIC_LED_BREATHE](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga83c3fbd41de6c4f3739880fceadea96fa49d40e2d9ade1192b968fba235449da7)
- [biometric_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gafe560b9baea81cbad071ead5015721d0)
- [BIOMETRIC_ATTR_MATCH_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0aa0b5c4fb004ee442265819f1ad1f888f)
- [BIOMETRIC_ATTR_ENROLLMENT_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0ac7cc9f7e2420227e96d33b526665cda0)
- [BIOMETRIC_ATTR_SECURITY_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0a8af3a6b4fb231c8991543f357a318eec)
- [BIOMETRIC_ATTR_TIMEOUT_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0af4ebcb6c0c73f05f6f6279d71d76a3d5)
- [BIOMETRIC_ATTR_ANTI_SPOOF_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0aef92b844ead708b1337fa983278e4499)
- [BIOMETRIC_ATTR_IMAGE_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0aceaac5e1b094da0b92a927f9d0379071)
- [BIOMETRIC_ATTR_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0a29e1b51dfbda37a58642630b44a59ece)
- [BIOMETRIC_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0afa83aa1fd1d91ba0753e46d9cf8e098d)
- [BIOMETRIC_ATTR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0a3770042eafa778b907f7598d762f8ca3)
- [INT16_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac58f2c111cc9989c86db2a7dc4fd84ca)
- [biometric_capabilities](../driver_model_reference/P027_生物识别能力.md)
- [type](../driver_model_reference/P027_生物识别能力.md#ad8c0934aec564a9e472ab75fb7e6163f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [max_templates](../driver_model_reference/P027_生物识别能力.md#a9b7fd2768df210ac02f3a104ec1db6c9)
- [template_size](../driver_model_reference/P027_生物识别能力.md#a2bc185c7fb7623f7fe65ee4c9b30cc62)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [storage_modes](../driver_model_reference/P027_生物识别能力.md#a6e6afaa6381f27e2635f60af531da094)
- [enrollment_samples_required](../driver_model_reference/P027_生物识别能力.md#a05bdbadc7e38bc72503a556804ed04a5)
- [biometric_match_result](../driver_model_reference/P030_生物识别匹配结果.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [confidence](../driver_model_reference/P030_生物识别匹配结果.md#ada317052641352f1f7d8871bc025c1d0)
- [template_id](../driver_model_reference/P030_生物识别匹配结果.md#adfaeb77884875c6339a93e5b152a333d)
- [image_quality](../driver_model_reference/P030_生物识别匹配结果.md#adb749246db9d80a7f00813633e497894)
- [biometric_capture_result](../driver_model_reference/P028_生物识别采集结果.md)
- [samples_captured](../driver_model_reference/P028_生物识别采集结果.md#ae2b9f021e8becd7a5339248f6b39162d)
- [samples_required](../driver_model_reference/P028_生物识别采集结果.md#a97b590dec9a83f835c5c71e64834b8f6)
- [quality](../driver_model_reference/P028_生物识别采集结果.md#adf436e8f4aca8d86df613beb5fd3f821)
- [biometric_api_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#ga38a8a21a46a8e252792951ce8312294a)
- [device](../device_reference/P002_设备对象结构.md)
- [biometric_api_attr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#gad7f71482bb3407bcedf37a7b4b5633be)
- [biometric_api_attr_get](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#ga5db0eae1ba88eef3d2fcb99f4a75ff50)
- [biometric_api_enroll_start](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#ga2515c347864644dea3906fc3a25c155e)
- [biometric_api_enroll_capture](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#ga70253fb65673c4c95c22896ca1bb0641)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [biometric_api_enroll_finalize](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#ga36b3ac91aceeca57ccaaa78619ab603f)
- [biometric_api_enroll_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#gad0aa92ba1e326e98f5963206d548cda3)
- [biometric_api_template_store](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#gaa86339893ac58e9a1480d013605c2718)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [biometric_api_template_read](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#gaf70dbdc914f9a6b89574f1947d821424)
- [biometric_api_template_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#ga182b3b06e09416ba826a46ec346b57d1)
- [biometric_api_template_delete_all](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#ga8196c59e50e8f093383c7a354ceaf694)
- [biometric_api_template_list](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#gab69ee26aff13e80183e5a929d4f20277)
- [biometric_api_match](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#ga5f49256b2d8abf90fdedb33dcd84a95e)
- [biometric_api_led_control](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html#gaa379e427029685e4c73a9dd9ccd3f6c4)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [biometric_driver_api](../driver_model_reference/P029_生物识别驱动接口.md)
- [get_capabilities](../driver_model_reference/P029_生物识别驱动接口.md#a0b03da9661ffbd2980230f7cdcd63440)
- [attr_set](../driver_model_reference/P029_生物识别驱动接口.md#aa9e731ce70feadf0bb9ee2a6c76c19ee)
- [attr_get](../driver_model_reference/P029_生物识别驱动接口.md#a267615faeb182198f3af7d5328baf29e)
- [enroll_start](../driver_model_reference/P029_生物识别驱动接口.md#ade76db1b6d6bd505b295daa44c61ddca)
- [enroll_capture](../driver_model_reference/P029_生物识别驱动接口.md#acc200c2bb820d4114e9ae282c31d5dbf)
- [enroll_finalize](../driver_model_reference/P029_生物识别驱动接口.md#ade705f56f4dc7d95e0b296a4bb4d4163)
- [enroll_abort](../driver_model_reference/P029_生物识别驱动接口.md#a94f6375942786ee4798ea55d961398a4)
- [template_store](../driver_model_reference/P029_生物识别驱动接口.md#a8e3ce1b03251fd828b5df85e4c573080)
- [template_read](../driver_model_reference/P029_生物识别驱动接口.md#ab2b7f89b60294aa916be9d4bc016f986)
- [template_delete](../driver_model_reference/P029_生物识别驱动接口.md#a18b95022f52d21655ffc4f8d38d60ab8)
- [template_delete_all](../driver_model_reference/P029_生物识别驱动接口.md#a87e0be3ddc66a4b8d2bd5c28f16be49c)
- [template_list](../driver_model_reference/P029_生物识别驱动接口.md#a1312d877f54c4a58fca34e657d4ed76e)
- [match](../driver_model_reference/P029_生物识别驱动接口.md#ae546cb778af0bbbfa48d9704eb658be8)
- [led_control](../driver_model_reference/P029_生物识别驱动接口.md#ae89d8eaf26b0563be483d87488d690a4)
- [biometric_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaa335d1d790f5ce609b6de57eaeb1399c)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [biometric_attr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga4ca9b34414ff86b2a5271bbc4c2563df)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [biometric_attr_get](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga243ad98c425edb68b425be8639b6fcac)
- [biometric_enroll_start](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga65bdfd912acf5e9503d0f91d5842cf8c)
- [biometric_enroll_capture](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga2a5c36eca939da337f38b54b44ef16eb)
- [biometric_enroll_finalize](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaf2d6cf698d301c58dbcfb782af96d205)
- [biometric_enroll_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga330af9905835af25b41e2e9b7fff11e6)
- [biometric_template_store](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gae323da0884660fba5b7bcb9b210aec00)
- [biometric_template_read](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga8be2ec31d1848891327a44cda198b86e)
- [biometric_template_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga1fa103e8d4a55ffba82f1b0f65634c16)
- [biometric_template_delete_all](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gab5c9975eff4a737f75710e2f43df39b2)
- [biometric_template_list](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga9de5325164b6ed98427275662a7bb07e)
- [biometric_match](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga51d358b76f65d2776dfe4fed79e4afcd)
- [biometric_led_control](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaca4596921ea8f1554215d4994da5537e)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [biometric_capabilities::enrollment_samples_required](../driver_model_reference/P027_生物识别能力.md#a05bdbadc7e38bc72503a556804ed04a5)
- [biometric_capabilities::template_size](../driver_model_reference/P027_生物识别能力.md#a2bc185c7fb7623f7fe65ee4c9b30cc62)
- [biometric_capabilities::storage_modes](../driver_model_reference/P027_生物识别能力.md#a6e6afaa6381f27e2635f60af531da094)
- [biometric_capabilities::max_templates](../driver_model_reference/P027_生物识别能力.md#a9b7fd2768df210ac02f3a104ec1db6c9)
- [biometric_capabilities::type](../driver_model_reference/P027_生物识别能力.md#ad8c0934aec564a9e472ab75fb7e6163f)
- [biometric_capture_result::samples_required](../driver_model_reference/P028_生物识别采集结果.md#a97b590dec9a83f835c5c71e64834b8f6)
- [biometric_capture_result::quality](../driver_model_reference/P028_生物识别采集结果.md#adf436e8f4aca8d86df613beb5fd3f821)
- [biometric_capture_result::samples_captured](../driver_model_reference/P028_生物识别采集结果.md#ae2b9f021e8becd7a5339248f6b39162d)
- [biometric_driver_api::get_capabilities](../driver_model_reference/P029_生物识别驱动接口.md#a0b03da9661ffbd2980230f7cdcd63440)
- [biometric_driver_api::template_list](../driver_model_reference/P029_生物识别驱动接口.md#a1312d877f54c4a58fca34e657d4ed76e)
- [biometric_driver_api::template_delete](../driver_model_reference/P029_生物识别驱动接口.md#a18b95022f52d21655ffc4f8d38d60ab8)
- [biometric_driver_api::attr_get](../driver_model_reference/P029_生物识别驱动接口.md#a267615faeb182198f3af7d5328baf29e)
- [biometric_driver_api::template_delete_all](../driver_model_reference/P029_生物识别驱动接口.md#a87e0be3ddc66a4b8d2bd5c28f16be49c)
- [biometric_driver_api::template_store](../driver_model_reference/P029_生物识别驱动接口.md#a8e3ce1b03251fd828b5df85e4c573080)
- [biometric_driver_api::enroll_abort](../driver_model_reference/P029_生物识别驱动接口.md#a94f6375942786ee4798ea55d961398a4)
- [biometric_driver_api::attr_set](../driver_model_reference/P029_生物识别驱动接口.md#aa9e731ce70feadf0bb9ee2a6c76c19ee)
- [biometric_driver_api::template_read](../driver_model_reference/P029_生物识别驱动接口.md#ab2b7f89b60294aa916be9d4bc016f986)
- [biometric_driver_api::enroll_capture](../driver_model_reference/P029_生物识别驱动接口.md#acc200c2bb820d4114e9ae282c31d5dbf)
- [biometric_driver_api::enroll_finalize](../driver_model_reference/P029_生物识别驱动接口.md#ade705f56f4dc7d95e0b296a4bb4d4163)
- [biometric_driver_api::enroll_start](../driver_model_reference/P029_生物识别驱动接口.md#ade76db1b6d6bd505b295daa44c61ddca)
- [biometric_driver_api::match](../driver_model_reference/P029_生物识别驱动接口.md#ae546cb778af0bbbfa48d9704eb658be8)
- [biometric_driver_api::led_control](../driver_model_reference/P029_生物识别驱动接口.md#ae89d8eaf26b0563be483d87488d690a4)
- [biometric_match_result::confidence](../driver_model_reference/P030_生物识别匹配结果.md#ada317052641352f1f7d8871bc025c1d0)
- [biometric_match_result::image_quality](../driver_model_reference/P030_生物识别匹配结果.md#adb749246db9d80a7f00813633e497894)
- [biometric_match_result::template_id](../driver_model_reference/P030_生物识别匹配结果.md#adfaeb77884875c6339a93e5b152a333d)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)

---

[上一章](P065_bflb_clock_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P067_blinfo.h_源码浏览.md)
