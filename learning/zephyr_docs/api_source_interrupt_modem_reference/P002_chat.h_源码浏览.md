---
id: learning.zephyr-docs.api-source-interrupt-modem-reference.page-2
title: chat.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/chat_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_chat.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h.html)。

## 2.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
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
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
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
<a id="foldopen00095"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="foldopen00125"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="foldopen00148"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="foldopen00163"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="foldopen00178"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="foldopen00211"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="foldopen00228"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="foldopen00244"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="foldopen00250"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="foldopen00259"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="foldopen00287"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="foldopen00304"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="foldopen00315"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="foldopen00319"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="foldopen00322"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="foldopen00333"></a>
<a id="l00333"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
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
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
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
<a id="l00381"></a>
<a id="l00382"></a>
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
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="foldopen00413"></a>
<a id="l00413"></a>
<a id="l00415"></a>
<a id="l00417"></a>
<a id="l00419"></a>
<a id="l00421"></a>
<a id="l00423"></a>
<a id="l00425"></a>
<a id="l00427"></a>
<a id="l00429"></a>
<a id="l00431"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="foldopen00498"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__modem__chat_html_ga19cd30454fb4eb9293e87b24a8cf0655"></a>
<a id="agroup__modem__chat_html_ga1a0680c65972b58ea065b98a78095540"></a>
<a id="agroup__modem__chat_html_ga1f41fc90f5026dc688a90567278ac175"></a>
<a id="agroup__modem__chat_html_ga2aec485e298ebde8af0372deb9c4784f"></a>
<a id="agroup__modem__chat_html_ga3274b7ffcce059c4d0a5d2ccb3e0bcc6"></a>
<a id="agroup__modem__chat_html_ga35c1a4f9ed2677fb747025f859eeae56"></a>
<a id="agroup__modem__chat_html_ga372f3ffe3960a1bd3aa59a377656c262"></a>
<a id="agroup__modem__chat_html_ga397d399703449498171ac898776fe791"></a>
<a id="agroup__modem__chat_html_ga4035be227ddec8424311575305647d3e"></a>
<a id="agroup__modem__chat_html_ga4389d813db136c199c872f20a125eba2"></a>
<a id="agroup__modem__chat_html_ga53cb148e665095d036edc266e778a8ce"></a>
<a id="agroup__modem__chat_html_ga5ec3918a4beb6b30deecedbd6f6382ee"></a>
<a id="agroup__modem__chat_html_ga62fa275cb9ce387b0bf5b384c9448c41"></a>
<a id="agroup__modem__chat_html_ga734cb1bcbbbf5c87551b20038e0608ae"></a>
<a id="agroup__modem__chat_html_ga9180fa670c3b6e88fa6011fdce5fd909"></a>
<a id="agroup__modem__chat_html_ga959b05c06c113cd8107dbc71d06b0f81"></a>
<a id="agroup__modem__chat_html_ga9ab3fa018ee0b2ebaacb3d74ee7ce29a"></a>
<a id="agroup__modem__chat_html_ga9bff858315a05324ff9690bdbce7398f"></a>
<a id="agroup__modem__chat_html_gaa92ffb91bab15c882cff7b13fca7eeb5"></a>
<a id="agroup__modem__chat_html_gac94a45b118b155ca7de1a45d12297ae4"></a>
<a id="agroup__modem__chat_html_gac9ed985688aeaee96adcb2b6c4285099"></a>
<a id="agroup__modem__chat_html_gad6b669708d24a3d3d91d1c40c2c504c8"></a>
<a id="agroup__modem__chat_html_gada2cd7e12d9a37af6f13ecfb6c182176"></a>
<a id="agroup__modem__chat_html_gadaed8cb3a0933fd15a46344ca0df9930"></a>
<a id="agroup__modem__chat_html_gae52a949df85cbcb7729c88917f46ef8d"></a>
<a id="agroup__modem__chat_html_gae64d151a5f65bde1dd1973393acf3ff1"></a>
<a id="agroup__modem__chat_html_gae689e92c91d414f968267e290e5246bd"></a>
<a id="agroup__modem__chat_html_gaf12d45cf404e85c94fc13252294c76ca"></a>
<a id="agroup__modem__chat_html_gaf79f3b0e67b5777876137b9e3e16d985"></a>
<a id="agroup__modem__chat_html_gaf91ae4e64113188e7049a7568a086556"></a>
<a id="agroup__modem__chat_html_gafdca5529d3ae3c982f3577560216e309"></a>
<a id="agroup__modem__chat_html_gafea28e13817e1daa6bb5c42514542e4e"></a>
<a id="agroup__modem__chat_html_gga4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e"></a>
<a id="agroup__modem__chat_html_gga4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee"></a>
<a id="agroup__modem__chat_html_gga4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b"></a>
<a id="agroup__modem__chat_html_gga734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd"></a>
<a id="agroup__modem__chat_html_gga734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amodem_2stats_8h_html"></a>
<a id="apipe_8h_html"></a>
<a id="aring__buffer_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructk__work_html"></a>
<a id="astructmodem__chat__config_html"></a>
<a id="astructmodem__chat__config_html_a00f0dc42251980cd51a8f2fd70b82e4f"></a>
<a id="astructmodem__chat__config_html_a295de98c2e8866059e7194c57d0502b7"></a>
<a id="astructmodem__chat__config_html_a2cf551a0946459b2825595026ebc7490"></a>
<a id="astructmodem__chat__config_html_a38e1eb6fb1e5a452f999bf8b3090141c"></a>
<a id="astructmodem__chat__config_html_a661d96b8a7031b17e6f660c6e0e4be11"></a>
<a id="astructmodem__chat__config_html_a76f85951f5750f0d07b1253af118ec6f"></a>
<a id="astructmodem__chat__config_html_aa30ccfd372c47c64e2a7b7c840405499"></a>
<a id="astructmodem__chat__config_html_ac002d9f43309db8c3c35826127d94194"></a>
<a id="astructmodem__chat__config_html_addfa7cacc676190d9e29c451d47ea3bd"></a>
<a id="astructmodem__chat__config_html_ae2afa6465bfad9c83dd57498165888b4"></a>
<a id="astructmodem__chat__config_html_af762b783d33e192ef45647e0b2e2d70b"></a>
<a id="astructmodem__chat__match_html"></a>
<a id="astructmodem__chat__match_html_a11f6e35cd2fd2166ac95adace6ec5c54"></a>
<a id="astructmodem__chat__match_html_a7c80555e1bf33504cef7be6c0f9db383"></a>
<a id="astructmodem__chat__match_html_a7fd423890bea11c65f326ace831233fc"></a>
<a id="astructmodem__chat__match_html_aa7f414d867fdcb2f34a9e4bd3c9b0eeb"></a>
<a id="astructmodem__chat__match_html_ad1bed20d70285a465663d9babc3fb3e2"></a>
<a id="astructmodem__chat__match_html_adb8c0ee17d317192432198949d116259"></a>
<a id="astructmodem__chat__match_html_afe00a3c87a68d9f7f889f7a0d3cc4150"></a>
<a id="astructmodem__chat__script__chat_html"></a>
<a id="astructmodem__chat__script__chat_html_a21647c746e9b2da52b7093afccf08268"></a>
<a id="astructmodem__chat__script__chat_html_a27be66d0a39b1956e7ca5a00e2be17f6"></a>
<a id="astructmodem__chat__script__chat_html_a5cab9c3a31624c8ffb490b70285f86ee"></a>
<a id="astructmodem__chat__script__chat_html_a92c038d56623b4f4b26c64b537e7ce8a"></a>
<a id="astructmodem__chat__script__chat_html_ad87948ff4e6441c118ee269bf6458aa0"></a>
<a id="astructmodem__chat__script__chat_html_afaaa9a7bc1842dfb65156fff2d91cfa0"></a>
<a id="astructmodem__chat__script__completion__info_html"></a>
<a id="astructmodem__chat__script__completion__info_html_a2e6ec071adec5565d4248e9ba1232c3b"></a>
<a id="astructmodem__chat__script__completion__info_html_a96294f87215db5d14432d208d1bad960"></a>
<a id="astructmodem__chat__script_html"></a>
<a id="astructmodem__chat__script_html_a0b9a9d3d44a8624728e16922cbdfd662"></a>
<a id="astructmodem__chat__script_html_a2b586e1ff80c22d8ff45829f3e2e7b17"></a>
<a id="astructmodem__chat__script_html_a3ac30e3ba1842cf53747721592f16cd4"></a>
<a id="astructmodem__chat__script_html_a5f329ecadd721d88e423074f00005114"></a>
<a id="astructmodem__chat__script_html_a73f4c3892052f827c10ea466c9a75954"></a>
<a id="astructmodem__chat__script_html_aa56bdf520b0f385bc6410b2c6aa2e8d4"></a>
<a id="astructmodem__chat__script_html_aca3b75a494273d8c06cf943153dd7dc8"></a>
<a id="astructmodem__chat_html"></a>

```c
/*
 * Copyright (c) 2022 Trackunit Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/sys/ring_buffer.h>

#include <zephyr/modem/pipe.h>
#include <zephyr/modem/stats.h>

#ifndef ZEPHYR_INCLUDE_MODEM_CHAT_H_
#define ZEPHYR_INCLUDE_MODEM_CHAT_H_

#ifdef __cplusplus
extern "C" {
#endif


struct modem_chat;
struct modem_chat_script;

typedef bool (*modem_chat_run_check)(void *user_data);

typedef void (*modem_chat_match_callback)(struct modem_chat *chat, char **argv, uint16_t argc,
                                          void *user_data);

struct modem_chat_match {
        const uint8_t *match;
        const uint8_t *separators;
        modem_chat_match_callback callback;
        uint8_t match_size;
        uint8_t separators_size;
        bool wildcards;
        bool partial;
};

#define MODEM_CHAT_MATCH(_match, _separators, _callback)                                           \
        {                                                                                          \
                .match = (uint8_t *)(_match),                                                      \
                .separators = (uint8_t *)(_separators),                                            \
                .match_size = (uint8_t)(sizeof(_match) - 1),                                       \
                .separators_size = (uint8_t)(sizeof(_separators) - 1),                             \
                .wildcards = false,                                                                \
                .callback = _callback,                                                             \
        }

#define MODEM_CHAT_MATCH_WILDCARD(_match, _separators, _callback)                                  \
        {                                                                                          \
                .match = (uint8_t *)(_match),                                                      \
                .separators = (uint8_t *)(_separators),                                            \
                .match_size = (uint8_t)(sizeof(_match) - 1),                                       \
                .separators_size = (uint8_t)(sizeof(_separators) - 1),                             \
                .wildcards = true,                                                                 \
                .callback = _callback,                                                             \
        }

#define MODEM_CHAT_MATCH_INITIALIZER(_match, _separators, _callback, _wildcards, _partial)         \
        {                                                                                          \
                .match = (uint8_t *)(_match),                                                      \
                .separators = (uint8_t *)(_separators),                                            \
                .match_size = (uint8_t)(sizeof(_match) - 1),                                       \
                .separators_size = (uint8_t)(sizeof(_separators) - 1),                             \
                .wildcards = _wildcards,                                                           \
                .partial = _partial,                                                               \
                .callback = _callback,                                                             \
        }

#define MODEM_CHAT_MATCH_DEFINE(_sym, _match, _separators, _callback)                              \
        const static struct modem_chat_match _sym = MODEM_CHAT_MATCH(_match, _separators, _callback)

#define MODEM_CHAT_MATCH_WILDCARD_DEFINE(_sym, _match, _separators, _callback)                     \
        const static struct modem_chat_match _sym =                                                \
                MODEM_CHAT_MATCH_WILDCARD(_match, _separators, _callback)

/* Helper struct to match any response without callback. */
extern const struct modem_chat_match modem_chat_any_match;

#define MODEM_CHAT_MATCHES_DEFINE(_sym, ...)                                                       \
        const static struct modem_chat_match _sym[] = {__VA_ARGS__}

/* Helper struct to match nothing. */
extern const struct modem_chat_match modem_chat_empty_matches[0];

struct modem_chat_script_chat {
        const uint8_t *request;
        uint16_t request_size;
        const struct modem_chat_match *response_matches;
        uint16_t response_matches_size;
        uint16_t timeout;
#if defined(CONFIG_MODEM_CHAT_COMMANDS_CONDITIONAL) || defined(__DOXYGEN__)
        modem_chat_run_check run_check;
#endif
};

#define MODEM_CHAT_SCRIPT_CMD_RESP(_request, _response_match)                                      \
        {                                                                                          \
                .request = (uint8_t *)(_request),                                                  \
                .request_size = (uint16_t)(sizeof(_request) - 1),                                  \
                .response_matches = &_response_match,                                              \
                .response_matches_size = 1,                                                        \
                .timeout = 0,                                                                      \
        }

#define MODEM_CHAT_SCRIPT_CMD_RESP_MULT(_request, _response_matches)                               \
        {                                                                                          \
                .request = (uint8_t *)(_request),                                                  \
                .request_size = (uint16_t)(sizeof(_request) - 1),                                  \
                .response_matches = _response_matches,                                             \
                .response_matches_size = ARRAY_SIZE(_response_matches),                            \
                .timeout = 0,                                                                      \
        }

#define MODEM_CHAT_SCRIPT_CMD_RESP_NONE(_request, _timeout_ms)                                     \
        {                                                                                          \
                .request = (uint8_t *)(_request),                                                  \
                .request_size = (uint16_t)(sizeof(_request) - 1),                                  \
                .response_matches = NULL,                                                          \
                .response_matches_size = 0,                                                        \
                .timeout = _timeout_ms,                                                            \
        }

#define MODEM_CHAT_SCRIPT_CMD_RESP_COND(_request, _response_match, _run_check)                     \
        {                                                                                          \
                .request = (uint8_t *)(_request),                                                  \
                .request_size = (uint16_t)(sizeof(_request) - 1),                                  \
                .response_matches = &_response_match,                                              \
                .response_matches_size = 1,                                                        \
                .timeout = 0,                                                                      \
                .run_check = _run_check                                                            \
        }

#define MODEM_CHAT_SCRIPT_CMD_RESP_MULT_COND(_request, _response_matches, _run_check)              \
        {                                                                                          \
                .request = (uint8_t *)(_request),                                                  \
                .request_size = (uint16_t)(sizeof(_request) - 1),                                  \
                .response_matches = _response_matches,                                             \
                .response_matches_size = ARRAY_SIZE(_response_matches),                            \
                .timeout = 0,                                                                      \
                .run_check = _run_check                                                            \
        }

#define MODEM_CHAT_SCRIPT_CMD_RESP_NONE_COND(_request, _timeout_ms, _run_check)                    \
        {                                                                                          \
                .request = (uint8_t *)(_request),                                                  \
                .request_size = (uint16_t)(sizeof(_request) - 1),                                  \
                .response_matches = NULL,                                                          \
                .response_matches_size = 0,                                                        \
                .timeout = _timeout_ms,                                                            \
                .run_check = _run_check                                                            \
        }

#define MODEM_CHAT_SCRIPT_CMDS_DEFINE(_sym, ...)                                                   \
        const static struct modem_chat_script_chat _sym[] = {__VA_ARGS__}

/* Helper struct to have no chat script command. */
extern const struct modem_chat_script_chat modem_chat_empty_script_chats[0];

enum modem_chat_script_result {
        MODEM_CHAT_SCRIPT_RESULT_SUCCESS,
        MODEM_CHAT_SCRIPT_RESULT_ABORT,
        MODEM_CHAT_SCRIPT_RESULT_TIMEOUT
};

struct modem_chat_script_completion_info {
        const struct modem_chat_script *script;
        const struct modem_chat_script_chat *script_chat;
};

typedef void (*modem_chat_script_callback)(struct modem_chat *chat,
                                           enum modem_chat_script_result result,
                                           const struct modem_chat_script_completion_info *info,
                                           void *user_data);

struct modem_chat_script {
        const char *name;
        const struct modem_chat_script_chat *script_chats;
        uint16_t script_chats_size;
        const struct modem_chat_match *abort_matches;
        uint16_t abort_matches_size;
        modem_chat_script_callback callback;
        uint32_t timeout;
};

#define MODEM_CHAT_SCRIPT_DEFINE(_sym, _script_chats, _abort_matches, _callback, _timeout_s)       \
        const static struct modem_chat_script _sym = {                                             \
                .name = #_sym,                                                                     \
                .script_chats = _script_chats,                                                     \
                .script_chats_size = ARRAY_SIZE(_script_chats),                                    \
                .abort_matches = _abort_matches,                                                   \
                .abort_matches_size = ARRAY_SIZE(_abort_matches),                                  \
                .callback = _callback,                                                             \
                .timeout = _timeout_s,                                                             \
        }

#define MODEM_CHAT_SCRIPT_NO_ABORT_DEFINE(_sym, _script_chats, _callback, _timeout_s)              \
        MODEM_CHAT_SCRIPT_DEFINE(_sym, _script_chats, modem_chat_empty_matches,                    \
                                 _callback, _timeout_s)

#define MODEM_CHAT_SCRIPT_EMPTY_DEFINE(_sym)                                                       \
        MODEM_CHAT_SCRIPT_NO_ABORT_DEFINE(_sym, modem_chat_empty_script_chats, NULL, 0)

enum modem_chat_script_send_state {
        /* No data to send */
        MODEM_CHAT_SCRIPT_SEND_STATE_IDLE,
        /* Sending request */
        MODEM_CHAT_SCRIPT_SEND_STATE_REQUEST,
};

struct modem_chat {
        /* Pipe used to send and receive data */
        struct modem_pipe *pipe;

        /* User data passed with match callbacks */
        void *user_data;

        /* Receive buffer */
        uint8_t *receive_buf;
        uint16_t receive_buf_size;
        uint16_t receive_buf_len;

        /* Work buffer */
        uint8_t work_buf[CONFIG_MODEM_CHAT_WORK_BUFFER_SIZE];
        uint16_t work_buf_len;

        /* Chat delimiter */
        const uint8_t *delimiter;
        uint16_t delimiter_size;
        uint16_t delimiter_match_len;

        /* Array of bytes which are discarded out by parser */
        const uint8_t *filter;
        uint16_t filter_size;

        /* Parsed arguments */
        uint8_t **argv;
        uint16_t argv_size;
        uint16_t argc;

        /* Matches
         * Index 0 -> Response matches
         * Index 1 -> Abort matches
         * Index 2 -> Unsolicited matches
         */
        const struct modem_chat_match *matches[3];
        uint16_t matches_size[3];

        /* Script execution */
        const struct modem_chat_script *script;
        const struct modem_chat_script *pending_script;
        struct k_work script_run_work;
        struct k_work_delayable script_timeout_work;
        struct k_work script_abort_work;
        uint16_t script_chat_it;
        atomic_t script_state;
        enum modem_chat_script_result script_result;
        struct k_sem script_stopped_sem;

        /* Script sending */
        enum modem_chat_script_send_state script_send_state;
        uint16_t script_send_pos;
        struct k_work script_send_work;
        struct k_work_delayable script_send_timeout_work;

        /* Match parsing */
        const struct modem_chat_match *parse_match;
        uint16_t parse_match_len;
        uint16_t parse_arg_len;
        uint16_t parse_match_type;
#if defined(CONFIG_MODEM_CHAT_LOG_RAW_RX)
        uint8_t raw_log_separators[CONFIG_MODEM_CHAT_LOG_BUFFER_SIZE];
        uint16_t raw_log_separators_len;
#endif

        /* Process received data */
        struct k_work receive_work;

        /* Statistics */
#if CONFIG_MODEM_STATS
        struct modem_stats_buffer receive_buf_stats;
        struct modem_stats_buffer work_buf_stats;
#endif
};

struct modem_chat_config {
        void *user_data;
        uint8_t *receive_buf;
        uint16_t receive_buf_size;
        const uint8_t *delimiter;
        uint8_t delimiter_size;
        const uint8_t *filter;
        uint8_t filter_size;
        uint8_t **argv;
        uint16_t argv_size;
        const struct modem_chat_match *unsol_matches;
        uint16_t unsol_matches_size;
};

int modem_chat_init(struct modem_chat *chat, const struct modem_chat_config *config);

int modem_chat_attach(struct modem_chat *chat, struct modem_pipe *pipe);

bool modem_chat_is_running(struct modem_chat *chat);

int modem_chat_run_script_async(struct modem_chat *chat, const struct modem_chat_script *script);

int modem_chat_run_script(struct modem_chat *chat, const struct modem_chat_script *script);

static inline int modem_chat_script_run(struct modem_chat *chat,
                                        const struct modem_chat_script *script)
{
        return modem_chat_run_script_async(chat, script);
}

void modem_chat_script_abort(struct modem_chat *chat);

void modem_chat_release(struct modem_chat *chat);

void modem_chat_match_init(struct modem_chat_match *chat_match);

int modem_chat_match_set_match(struct modem_chat_match *chat_match, const char *match);

int modem_chat_match_set_separators(struct modem_chat_match *chat_match, const char *separators);

void modem_chat_match_set_callback(struct modem_chat_match *chat_match,
                                   modem_chat_match_callback callback);

void modem_chat_match_set_partial(struct modem_chat_match *chat_match, bool partial);

void modem_chat_match_enable_wildcards(struct modem_chat_match *chat_match, bool enable);

void modem_chat_script_chat_init(struct modem_chat_script_chat *script_chat);

int modem_chat_script_chat_set_request(struct modem_chat_script_chat *script_chat,
                                       const char *request);

int modem_chat_script_chat_set_response_matches(struct modem_chat_script_chat *script_chat,
                                                const struct modem_chat_match *response_matches,
                                                uint16_t response_matches_size);

void modem_chat_script_chat_set_timeout(struct modem_chat_script_chat *script_chat,
                                        uint16_t timeout_ms);

void modem_chat_script_init(struct modem_chat_script *script);

void modem_chat_script_set_name(struct modem_chat_script *script, const char *name);

int modem_chat_script_set_script_chats(struct modem_chat_script *script,
                                       const struct modem_chat_script_chat *script_chats,
                                       uint16_t script_chats_size);

int modem_chat_script_set_abort_matches(struct modem_chat_script *script,
                                        const struct modem_chat_match *abort_matches,
                                        uint16_t abort_matches_size);

void modem_chat_script_set_callback(struct modem_chat_script *script,
                                    modem_chat_script_callback callback);

void modem_chat_script_set_timeout(struct modem_chat_script *script, uint32_t timeout_s);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MODEM_CHAT_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Trackunit Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 113 行

用于匹配任意响应且不执行回调的辅助结构体（helper struct）。

### 注释 3：原第 119 行

不匹配任何内容的辅助结构体。

### 注释 4：原第 247 行

用于表示没有交互脚本命令（chat script command）的辅助结构体。

### 注释 5：原第 323 行

没有待发送数据。

### 注释 6：原第 325 行

正在发送请求（sending request）。

### 注释 7：原第 335 行

用于发送和接收数据的管道（pipe）。

### 注释 8：原第 338 行

传给匹配回调（match callbacks）的用户数据。

### 注释 9：原第 341 行

接收缓冲区。

### 注释 10：原第 346 行

工作缓冲区（work buffer）。

### 注释 11：原第 350 行

交互分隔符（chat delimiter）。

### 注释 12：原第 355 行

解析器（parser）会丢弃的字节数组。

### 注释 13：原第 359 行

已解析的参数（parsed arguments）。

### 注释 14：原第 364 行

匹配项（matches）：索引 0 为响应匹配（Response matches）；索引 1 为中止匹配（Abort matches）；索引 2 为非请求消息匹配（Unsolicited matches）。

### 注释 15：原第 372 行

脚本执行（script execution）。

### 注释 16：原第 383 行

脚本发送（script sending）。

### 注释 17：原第 389 行

匹配解析（match parsing）。

### 注释 18：原第 399 行

处理已接收的数据。

### 注释 19：原第 402 行

统计信息（Statistics）。

### 注释 20：原第 668 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MODEM_CHAT_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)
- [zephyr/modem/pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [zephyr/modem/stats.h](../api_file_management_reference/P035_zephyr__modem__stats.h_文件参考.md)
- [modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)
- [modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [modem_chat_run_check](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga372f3ffe3960a1bd3aa59a377656c262)
- [modem_chat_match_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae689e92c91d414f968267e290e5246bd)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#ad1bed20d70285a465663d9babc3fb3e2)
- [separators](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#a7fd423890bea11c65f326ace831233fc)
- [callback](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#a11f6e35cd2fd2166ac95adace6ec5c54)
- [match_size](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#afe00a3c87a68d9f7f889f7a0d3cc4150)
- [separators_size](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#a7c80555e1bf33504cef7be6c0f9db383)
- [wildcards](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#adb8c0ee17d317192432198949d116259)
- [partial](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#aa7f414d867fdcb2f34a9e4bd3c9b0eeb)
- [modem_chat_any_match](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gada2cd7e12d9a37af6f13ecfb6c182176)
- [modem_chat_empty_matches](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gac94a45b118b155ca7de1a45d12297ae4)
- [modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)
- [request](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#a92c038d56623b4f4b26c64b537e7ce8a)
- [request_size](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#ad87948ff4e6441c118ee269bf6458aa0)
- [response_matches](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#a5cab9c3a31624c8ffb490b70285f86ee)
- [response_matches_size](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#afaaa9a7bc1842dfb65156fff2d91cfa0)
- [timeout](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#a21647c746e9b2da52b7093afccf08268)
- [run_check](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#a27be66d0a39b1956e7ca5a00e2be17f6)
- [modem_chat_empty_script_chats](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga19cd30454fb4eb9293e87b24a8cf0655)
- [modem_chat_script_result](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga4035be227ddec8424311575305647d3e)
- [MODEM_CHAT_SCRIPT_RESULT_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee)
- [MODEM_CHAT_SCRIPT_RESULT_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b)
- [MODEM_CHAT_SCRIPT_RESULT_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e)
- [modem_chat_script_completion_info](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md)
- [script](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md#a2e6ec071adec5565d4248e9ba1232c3b)
- [script_chat](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md#a96294f87215db5d14432d208d1bad960)
- [modem_chat_script_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga1a0680c65972b58ea065b98a78095540)
- [name](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#aca3b75a494273d8c06cf943153dd7dc8)
- [script_chats](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#a5f329ecadd721d88e423074f00005114)
- [script_chats_size](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#a3ac30e3ba1842cf53747721592f16cd4)
- [abort_matches](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#a2b586e1ff80c22d8ff45829f3e2e7b17)
- [abort_matches_size](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#aa56bdf520b0f385bc6410b2c6aa2e8d4)
- [callback](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#a73f4c3892052f827c10ea466c9a75954)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [timeout](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#a0b9a9d3d44a8624728e16922cbdfd662)
- [modem_chat_script_send_state](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga734cb1bcbbbf5c87551b20038e0608ae)
- [MODEM_CHAT_SCRIPT_SEND_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974)
- [MODEM_CHAT_SCRIPT_SEND_STATE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gga734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [modem_chat_config](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md)
- [user_data](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#ac002d9f43309db8c3c35826127d94194)
- [receive_buf](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#a295de98c2e8866059e7194c57d0502b7)
- [receive_buf_size](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#a76f85951f5750f0d07b1253af118ec6f)
- [delimiter](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#a38e1eb6fb1e5a452f999bf8b3090141c)
- [delimiter_size](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#aa30ccfd372c47c64e2a7b7c840405499)
- [filter](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#a00f0dc42251980cd51a8f2fd70b82e4f)
- [filter_size](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#af762b783d33e192ef45647e0b2e2d70b)
- [argv](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#ae2afa6465bfad9c83dd57498165888b4)
- [argv_size](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#a2cf551a0946459b2825595026ebc7490)
- [unsol_matches](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#a661d96b8a7031b17e6f660c6e0e4be11)
- [unsol_matches_size](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#addfa7cacc676190d9e29c451d47ea3bd)
- [modem_chat_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaf79f3b0e67b5777876137b9e3e16d985)
- [modem_chat_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaf91ae4e64113188e7049a7568a086556)
- [modem_chat_is_running](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga959b05c06c113cd8107dbc71d06b0f81)
- [modem_chat_run_script_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga397d399703449498171ac898776fe791)
- [modem_chat_run_script](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae64d151a5f65bde1dd1973393acf3ff1)
- [modem_chat_script_run](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaa92ffb91bab15c882cff7b13fca7eeb5)
- [modem_chat_script_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga5ec3918a4beb6b30deecedbd6f6382ee)
- [modem_chat_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga62fa275cb9ce387b0bf5b384c9448c41)
- [modem_chat_match_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga1f41fc90f5026dc688a90567278ac175)
- [modem_chat_match_set_match](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gac9ed985688aeaee96adcb2b6c4285099)
- [modem_chat_match_set_separators](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga35c1a4f9ed2677fb747025f859eeae56)
- [modem_chat_match_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gafea28e13817e1daa6bb5c42514542e4e)
- [modem_chat_match_set_partial](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga53cb148e665095d036edc266e778a8ce)
- [modem_chat_match_enable_wildcards](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga3274b7ffcce059c4d0a5d2ccb3e0bcc6)
- [modem_chat_script_chat_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gaf12d45cf404e85c94fc13252294c76ca)
- [modem_chat_script_chat_set_request](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gadaed8cb3a0933fd15a46344ca0df9930)
- [modem_chat_script_chat_set_response_matches](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga2aec485e298ebde8af0372deb9c4784f)
- [modem_chat_script_chat_set_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae52a949df85cbcb7729c88917f46ef8d)
- [modem_chat_script_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gafdca5529d3ae3c982f3577560216e309)
- [modem_chat_script_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga9ab3fa018ee0b2ebaacb3d74ee7ce29a)
- [modem_chat_script_set_script_chats](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gad6b669708d24a3d3d91d1c40c2c504c8)
- [modem_chat_script_set_abort_matches](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga9bff858315a05324ff9690bdbce7398f)
- [modem_chat_script_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga4389d813db136c199c872f20a125eba2)
- [modem_chat_script_set_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga9180fa670c3b6e88fa6011fdce5fd909)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [stats.h](../api_file_management_reference/P035_zephyr__modem__stats.h_文件参考.md)
- [pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)
- [modem_chat_config::filter](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#a00f0dc42251980cd51a8f2fd70b82e4f)
- [modem_chat_config::receive_buf](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#a295de98c2e8866059e7194c57d0502b7)
- [modem_chat_config::argv_size](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#a2cf551a0946459b2825595026ebc7490)
- [modem_chat_config::delimiter](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#a38e1eb6fb1e5a452f999bf8b3090141c)
- [modem_chat_config::unsol_matches](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#a661d96b8a7031b17e6f660c6e0e4be11)
- [modem_chat_config::receive_buf_size](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#a76f85951f5750f0d07b1253af118ec6f)
- [modem_chat_config::delimiter_size](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#aa30ccfd372c47c64e2a7b7c840405499)
- [modem_chat_config::user_data](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#ac002d9f43309db8c3c35826127d94194)
- [modem_chat_config::unsol_matches_size](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#addfa7cacc676190d9e29c451d47ea3bd)
- [modem_chat_config::argv](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#ae2afa6465bfad9c83dd57498165888b4)
- [modem_chat_config::filter_size](../modem_wireless_model_reference/P053_modem_chat_config_结构体.md#af762b783d33e192ef45647e0b2e2d70b)
- [modem_chat_match::callback](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#a11f6e35cd2fd2166ac95adace6ec5c54)
- [modem_chat_match::separators_size](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#a7c80555e1bf33504cef7be6c0f9db383)
- [modem_chat_match::separators](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#a7fd423890bea11c65f326ace831233fc)
- [modem_chat_match::partial](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#aa7f414d867fdcb2f34a9e4bd3c9b0eeb)
- [modem_chat_match::match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#ad1bed20d70285a465663d9babc3fb3e2)
- [modem_chat_match::wildcards](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#adb8c0ee17d317192432198949d116259)
- [modem_chat_match::match_size](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md#afe00a3c87a68d9f7f889f7a0d3cc4150)
- [modem_chat_script_chat::timeout](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#a21647c746e9b2da52b7093afccf08268)
- [modem_chat_script_chat::run_check](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#a27be66d0a39b1956e7ca5a00e2be17f6)
- [modem_chat_script_chat::response_matches](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#a5cab9c3a31624c8ffb490b70285f86ee)
- [modem_chat_script_chat::request](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#a92c038d56623b4f4b26c64b537e7ce8a)
- [modem_chat_script_chat::request_size](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#ad87948ff4e6441c118ee269bf6458aa0)
- [modem_chat_script_chat::response_matches_size](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md#afaaa9a7bc1842dfb65156fff2d91cfa0)
- [modem_chat_script_completion_info::script](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md#a2e6ec071adec5565d4248e9ba1232c3b)
- [modem_chat_script_completion_info::script_chat](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md#a96294f87215db5d14432d208d1bad960)
- [modem_chat_script::timeout](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#a0b9a9d3d44a8624728e16922cbdfd662)
- [modem_chat_script::abort_matches](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#a2b586e1ff80c22d8ff45829f3e2e7b17)
- [modem_chat_script::script_chats_size](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#a3ac30e3ba1842cf53747721592f16cd4)
- [modem_chat_script::script_chats](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#a5f329ecadd721d88e423074f00005114)
- [modem_chat_script::callback](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#a73f4c3892052f827c10ea466c9a75954)
- [modem_chat_script::abort_matches_size](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#aa56bdf520b0f385bc6410b2c6aa2e8d4)
- [modem_chat_script::name](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md#aca3b75a494273d8c06cf943153dd7dc8)

---

[上一章](P001_bcm2835-armctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_dma_stm32.h_源码浏览.md)
