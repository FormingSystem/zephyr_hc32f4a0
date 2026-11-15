---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-7
title: zephyr__drivers__lin.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lin_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr__drivers__lin.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lin_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P007_zephyr__drivers__lin.h_头文件参考.md)。

## 7.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
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
<a id="l00042"></a>
<a id="l00047"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00159"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="foldopen00177"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="foldopen00220"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="foldopen00303"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="foldopen00321"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="foldopen00337"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="foldopen00346"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="foldopen00360"></a>
<a id="l00360"></a>
<a id="l00364"></a>
<a id="l00368"></a>
<a id="l00372"></a>
<a id="l00376"></a>
<a id="l00380"></a>
<a id="l00384"></a>
<a id="l00388"></a>
<a id="l00392"></a>
<a id="l00396"></a>
<a id="l00400"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="foldopen00413"></a>
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
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="foldopen00442"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="foldopen00676"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="aclock_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__lin__controller_html_ga07ec84c466d94f6057d7852998b2fbb2"></a>
<a id="agroup__lin__controller_html_ga0fe3631c3f9b7100162b5f48e83bd6e3"></a>
<a id="agroup__lin__controller_html_ga136329dfada85698d56308d6157abea0"></a>
<a id="agroup__lin__controller_html_ga13e0a57996ba2f010bcda6561298b658"></a>
<a id="agroup__lin__controller_html_ga149ca3972fc800c4fd2bbb0b5d8a85e3"></a>
<a id="agroup__lin__controller_html_ga16889d5f804b14ef80a608f6b8a86193"></a>
<a id="agroup__lin__controller_html_ga2a2afff5c7524504f24860673c24a217"></a>
<a id="agroup__lin__controller_html_ga305d83d265245ed657a9974c0bab1962"></a>
<a id="agroup__lin__controller_html_ga344a6eade12faa423b8bd2718009b0c5"></a>
<a id="agroup__lin__controller_html_ga39766c7605a50fcb600e9d72bfcf07d5"></a>
<a id="agroup__lin__controller_html_ga42976918cdbcec388095d77e398e7633"></a>
<a id="agroup__lin__controller_html_ga4d80ed442a8a83985c6ba3658f96fd16"></a>
<a id="agroup__lin__controller_html_ga560c00e1f3b7990836a06c83ab0eca43"></a>
<a id="agroup__lin__controller_html_ga58c5052899f49601a91d6da614ea8c82"></a>
<a id="agroup__lin__controller_html_ga727b0f7fe4949e3fd17a303e239586bb"></a>
<a id="agroup__lin__controller_html_ga752004d89d50932711c3aa6189874478"></a>
<a id="agroup__lin__controller_html_ga7594e89b4fc3a018c1cd0010bd4a6ac1"></a>
<a id="agroup__lin__controller_html_ga8091d2d225709439f9afb2eddeb73792"></a>
<a id="agroup__lin__controller_html_ga880b0c5dd454342160bcf454de5105e9"></a>
<a id="agroup__lin__controller_html_ga9410aa6989aea2cc173e7f36dcaf6be7"></a>
<a id="agroup__lin__controller_html_ga97468832dddf9e21b33e93a36c60102a"></a>
<a id="agroup__lin__controller_html_gab0f27d3ad3637f9040920b3088c1e239"></a>
<a id="agroup__lin__controller_html_gab7aca457453e6e6409c02903bcdf9bab"></a>
<a id="agroup__lin__controller_html_gabcad96f6950ec45b71adfd14e4c0c363"></a>
<a id="agroup__lin__controller_html_gac3d1d8680c88765a49ca9c6d04763158"></a>
<a id="agroup__lin__controller_html_gad1df29d89982f09a9652db231e36c0c4"></a>
<a id="agroup__lin__controller_html_gad37ddea1dbcc29151c7a504813eebfac"></a>
<a id="agroup__lin__controller_html_gad77d365c000a2f9c7f2558ec24d0f455"></a>
<a id="agroup__lin__controller_html_gae69d33055fe07087a19b33dbe7a7252f"></a>
<a id="agroup__lin__controller_html_gaefe6f3853ea2f70d8ba4d6ab86f62b57"></a>
<a id="agroup__lin__controller_html_gaf8bd57bf6e9306a30fa025c1f9fe09e8"></a>
<a id="agroup__lin__controller_html_gaf97478fd971b8b6913386a225078a24f"></a>
<a id="agroup__lin__controller_html_gafae0fa8e806c2856f61642ef80368ec8"></a>
<a id="agroup__lin__controller_html_gga4d80ed442a8a83985c6ba3658f96fd16a71650e86f1cd26ae46011a2cdce767b8"></a>
<a id="agroup__lin__controller_html_gga4d80ed442a8a83985c6ba3658f96fd16aab1c3507ec82321e02c98f4878e6475d"></a>
<a id="agroup__lin__controller_html_ggab7aca457453e6e6409c02903bcdf9baba3d1c9ec13a13ce51893bf4c59f22cc2e"></a>
<a id="agroup__lin__controller_html_ggab7aca457453e6e6409c02903bcdf9baba3e30d82061bbcf51d89b63e94d362301"></a>
<a id="agroup__lin__controller_html_ggab7aca457453e6e6409c02903bcdf9baba9ee3a39dbc2ff9448a5cf443db5c1625"></a>
<a id="agroup__lin__controller_html_ggab7aca457453e6e6409c02903bcdf9babaa0770ae0419aadfc97ded5e9a524a6eb"></a>
<a id="agroup__lin__controller_html_ggab7aca457453e6e6409c02903bcdf9babab70beb6e355ef5c01fe3f8f285e8dd45"></a>
<a id="agroup__lin__controller_html_ggab7aca457453e6e6409c02903bcdf9babac57f7922e1bc6328afa742e8efa22211"></a>
<a id="agroup__lin__controller_html_ggab7aca457453e6e6409c02903bcdf9babadd5da0e9a1ceb2536f11991702784508"></a>
<a id="agroup__lin__controller_html_ggaf97478fd971b8b6913386a225078a24fa6b6c53f36bcccb2f099e63977bd2391a"></a>
<a id="agroup__lin__controller_html_ggaf97478fd971b8b6913386a225078a24fa9a93132138ea30a19f03d6bd52c8de5e"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys-util_html_gae664e7492e37d324831caf2321ddda37"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa49a456f06f7bdbedfcf3517e461947e"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_aca2d801eb15996cf1c74dc65cfa651fc"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructlin__config_html"></a>
<a id="astructlin__config_html_a1ea39425c06334cab01e224eba5e6aea"></a>
<a id="astructlin__config_html_a54077348c405316ba557ef0068a5a245"></a>
<a id="astructlin__config_html_a8474d3f259ecb76b0f10ace0f78ae360"></a>
<a id="astructlin__config_html_aa61435f08c254683bced69fade50b775"></a>
<a id="astructlin__config_html_ad8c36401d16e91a9f15a93733e42c8b9"></a>
<a id="astructlin__driver__api_html"></a>
<a id="astructlin__driver__api_html_a42abd5bd44fa028a4b2244131e5f17f4"></a>
<a id="astructlin__driver__api_html_a4704606967b3eb5d7ed103e1cccfb2fd"></a>
<a id="astructlin__driver__api_html_a4740986a33d152d9b57505334ed0df6b"></a>
<a id="astructlin__driver__api_html_a538f1329573a0919ed908e58ec60c24e"></a>
<a id="astructlin__driver__api_html_a6dbb848a229b52e1d0c005a142d1d2ac"></a>
<a id="astructlin__driver__api_html_a72c15ca01a63897758fab966be5f71fe"></a>
<a id="astructlin__driver__api_html_a91891ea072a84183ee95f7038a728ded"></a>
<a id="astructlin__driver__api_html_acf01655ffd47f72425ef385745700569"></a>
<a id="astructlin__driver__api_html_ada6d4e2661d5b9352d218757a69c7b10"></a>
<a id="astructlin__driver__api_html_adda8aa06d38c6f788eaff9e00978f9a7"></a>
<a id="astructlin__driver__api_html_af3321e6ce2a598a4bd123b968a608633"></a>
<a id="astructlin__driver__config_html"></a>
<a id="astructlin__driver__config_html_a561b88e59156f48fb5694cf4f00ed2ea"></a>
<a id="astructlin__driver__config_html_a6affbea0028b2c0876f74ff9397b41df"></a>
<a id="astructlin__driver__config_html_ae26b0452f7aa43f8f710647a6f00ea67"></a>
<a id="astructlin__driver__config_html_af62ec3ddcc7c42281e0d6cf9758645f7"></a>
<a id="astructlin__driver__data_html"></a>
<a id="astructlin__driver__data_html_a227dd7bb9dd4778a4dcfe13d5cc29751"></a>
<a id="astructlin__driver__data_html_a5c8c75a944077f3c84d80826dbcb76a5"></a>
<a id="astructlin__driver__data_html_aa83a634b8726bf5f2ff8552aedc9ca36"></a>
<a id="astructlin__driver__data_html_acfe00a4ae3aeaff0d43d51c9b8aeeec1"></a>
<a id="astructlin__event_html"></a>
<a id="astructlin__event_html_a17b7f0acfe393d09e58c2548e4f22212"></a>
<a id="astructlin__event_html_a1e82bfb19eddb23a27fcff1bee7e0667"></a>
<a id="astructlin__event_html_a1ff71b532d8e117247465d6d330e32bb"></a>
<a id="astructlin__event_html_a3b9f0adfcc43c3fed83ea23c10b7e67b"></a>
<a id="astructlin__event_html_aa9a3195610f167381e89b28d054ebd10"></a>
<a id="astructlin__event_html_ac5b4c13e4f9cfa2bdf327269013900a8"></a>
<a id="astructlin__event_html_ad47886103edb3c8709ec51bfec4905e7"></a>
<a id="astructlin__event_html_af401a550032c87c4b1a1e1d1941baee0"></a>
<a id="astructlin__filter_html"></a>
<a id="astructlin__filter_html_a20028b04b390f8c8dc95dbc5355fdde1"></a>
<a id="astructlin__filter_html_a36ac597c28bcc8f66c0369be41b6868e"></a>
<a id="astructlin__filter_html_a4b7c5a4d4aea3b15fa248957071b34a8"></a>
<a id="astructlin__msg_html"></a>
<a id="astructlin__msg_html_a0bbd5b4c8d50c298372d6227674843df"></a>
<a id="astructlin__msg_html_a3f139b75c8cd61fe2085b7eac4eb828b"></a>
<a id="astructlin__msg_html_a785c43cefa7fd940bf45f7729a51fb95"></a>
<a id="astructlin__msg_html_a8f9f0346d4f9f9a128150fbee2d2e3e6"></a>
<a id="astructlin__msg_html_ae0a650e8bbd278259f59bec5337ff955"></a>
<a id="astructlin__msg_html_aecea8811d33cfeb2c2d50a2d0cf92cbd"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_LIN_H
#define ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_LIN_H

#include <errno.h>

#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/clock.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif



#define LIN_ID_MASK 0x3FU

#define LIN_MAX_DLEN 8U



#define LIN_BUS_CONFLICT_DETECTION BIT(0)
#define LIN_BUS_AUTO_SYNC          BIT(1)


typedef uint32_t lin_config_flags_t;

enum lin_checksum_type {
        LIN_CHECKSUM_CLASSIC = 0,
        LIN_CHECKSUM_ENHANCED,
};

enum lin_event_type {
        LIN_EVT_RX_HEADER = 0,
        LIN_EVT_TX_HEADER,
        LIN_EVT_RX_DATA,
        LIN_EVT_TX_DATA,
        LIN_EVT_TX_WAKEUP,
        LIN_EVT_RX_WAKEUP,
        LIN_EVT_ERR,
};

#define LIN_ERR_BUS_COLLISION    BIT(0)
#define LIN_ERR_INVALID_CHECKSUM BIT(1)
#define LIN_ERR_COUNTER_OVERFLOW BIT(2)
#define LIN_ERR_OVERRUN          BIT(3)
#define LIN_ERR_PARITY           BIT(4)
#define LIN_ERR_FRAMING          BIT(5)

typedef uint32_t lin_error_flags_t;

enum lin_mode {
        LIN_MODE_COMMANDER = 0,
        LIN_MODE_RESPONDER,
};

struct lin_config {
        enum lin_mode mode;
        uint32_t baudrate;
        size_t break_len;
        size_t break_delimiter_len;
        lin_config_flags_t flags;
};

struct lin_msg {
        uint8_t id;
        uint8_t flags;
        uint8_t data_len;
        uint8_t reserved;
        union {
                uint8_t data[LIN_MAX_DLEN];
                uint32_t data_32[DIV_ROUND_UP(LIN_MAX_DLEN, sizeof(uint32_t))];
        };
        enum lin_checksum_type checksum_type;
};

struct lin_event {
        enum lin_event_type type;
        int status;
        union {
                struct {
                        uint8_t pid;
                } header;
                struct {
                        uint8_t pid;
                        uint8_t bytes_received;
                        uint8_t checksum;
                } data;
                lin_error_flags_t error_flags;
        };
};

typedef void (*lin_event_callback_t)(const struct device *dev, const struct lin_event *event,
                                     void *user_data);

struct lin_filter {
        uint8_t primary_pid;
        uint8_t secondary_pid;
        uint8_t mask;
};

typedef int (*lin_start_t)(const struct device *dev);

typedef int (*lin_stop_t)(const struct device *dev);

typedef int (*lin_configure_t)(const struct device *dev, const struct lin_config *config);

typedef int (*lin_get_config_t)(const struct device *dev, struct lin_config *config);

typedef int (*lin_send_t)(const struct device *dev, const struct lin_msg *msg, k_timeout_t timeout);

typedef int (*lin_receive_t)(const struct device *dev, struct lin_msg *msg, k_timeout_t timeout);

typedef int (*lin_response_t)(const struct device *dev, const struct lin_msg *msg,
                              k_timeout_t timeout);

typedef int (*lin_read_t)(const struct device *dev, struct lin_msg *msg, k_timeout_t timeout);

typedef int (*lin_wakeup_send_t)(const struct device *dev);

typedef int (*lin_set_event_callback_t)(const struct device *dev, lin_event_callback_t callback,
                                        void *user_data);

typedef int (*lin_set_rx_filter_t)(const struct device *dev, const struct lin_filter *filter);

struct lin_driver_config {
        const struct device *phy;
        uint32_t min_bitrate;
        uint32_t max_bitrate;
        uint32_t bitrate;
};

#define LIN_DT_DRIVER_CONFIG_GET(node_id, _min_bitrate, _max_bitrate)                              \
        {                                                                                          \
                .phy = DEVICE_DT_GET_OR_NULL(DT_PHANDLE(node_id, phys)),                           \
                .min_bitrate = DT_PROP_OR(node_id, min_bitrate, _min_bitrate),                     \
                .max_bitrate = DT_PROP_OR(node_id, max_bitrate, _max_bitrate),                     \
                .bitrate = DT_PROP_OR(node_id, bitrate, 0),                                        \
        }

#define LIN_DT_DRIVER_CONFIG_INST_GET(inst, _min_bitrate, _max_bitrate)                            \
        LIN_DT_DRIVER_CONFIG_GET(DT_DRV_INST(inst), _min_bitrate, _max_bitrate)

struct lin_driver_data {
        struct lin_config config;
        bool started;
        lin_event_callback_t callback;
        void *callback_data;
};

__subsystem struct lin_driver_api {
        lin_start_t start;
        lin_stop_t stop;
        lin_configure_t configure;
        lin_get_config_t get_config;
        lin_set_rx_filter_t set_rx_filter;
        lin_send_t send;
        lin_receive_t receive;
        lin_response_t response;
        lin_read_t read;
        lin_wakeup_send_t wakeup_send;
        lin_set_event_callback_t set_event_callback;
};

static inline uint8_t lin_get_frame_id(uint8_t pid)
{
        return pid & LIN_ID_MASK;
}

static inline uint8_t lin_compute_pid(uint8_t id)
{
        uint8_t p0 = (FIELD_GET(BIT(0), id) ^ FIELD_GET(BIT(1), id) ^ FIELD_GET(BIT(2), id) ^
                      FIELD_GET(BIT(4), id)) &
                     0x1U;
        uint8_t p1 = ~(FIELD_GET(BIT(1), id) ^ FIELD_GET(BIT(3), id) ^ FIELD_GET(BIT(4), id) ^
                       FIELD_GET(BIT(5), id)) &
                     0x1U;

        return (id & LIN_ID_MASK) | (p0 << 6) | (p1 << 7);
}

static inline bool lin_verify_pid(uint8_t pid)
{
        uint8_t id = lin_get_frame_id(pid);

        return lin_compute_pid(id) == pid;
}

__syscall const struct device *lin_get_transceiver(const struct device *dev);

static const struct device *z_impl_lin_get_transceiver(const struct device *dev)
{
        const struct lin_driver_config *config = dev->config;

        return config->phy;
}

__syscall int lin_start(const struct device *dev);

static inline int z_impl_lin_start(const struct device *dev)
{
        return DEVICE_API_GET(lin, dev)->start(dev);
}

__syscall int lin_stop(const struct device *dev);

static inline int z_impl_lin_stop(const struct device *dev)
{
        return DEVICE_API_GET(lin, dev)->stop(dev);
}

__syscall int lin_configure(const struct device *dev, const struct lin_config *config);

static inline int z_impl_lin_configure(const struct device *dev, const struct lin_config *config)
{
        return DEVICE_API_GET(lin, dev)->configure(dev, config);
}

__syscall int lin_get_config(const struct device *dev, struct lin_config *config);

static inline int z_impl_lin_get_config(const struct device *dev, struct lin_config *config)
{
        return DEVICE_API_GET(lin, dev)->get_config(dev, config);
}

__syscall int lin_send(const struct device *dev, const struct lin_msg *msg, k_timeout_t timeout);

static inline int z_impl_lin_send(const struct device *dev, const struct lin_msg *msg,
                                  k_timeout_t timeout)
{
        return DEVICE_API_GET(lin, dev)->send(dev, msg, timeout);
}

__syscall int lin_receive(const struct device *dev, struct lin_msg *msg, k_timeout_t timeout);

static inline int z_impl_lin_receive(const struct device *dev, struct lin_msg *msg,
                                     k_timeout_t timeout)
{
        return DEVICE_API_GET(lin, dev)->receive(dev, msg, timeout);
}

__syscall int lin_response(const struct device *dev, const struct lin_msg *msg,
                           k_timeout_t timeout);

static inline int z_impl_lin_response(const struct device *dev, const struct lin_msg *msg,
                                      k_timeout_t timeout)
{
        const struct lin_driver_api *api = DEVICE_API_GET(lin, dev);

        if (api->response == NULL) {
                return -ENOSYS;
        }

        return api->response(dev, msg, timeout);
}

__syscall int lin_read(const struct device *dev, struct lin_msg *msg, k_timeout_t timeout);

static inline int z_impl_lin_read(const struct device *dev, struct lin_msg *msg,
                                  k_timeout_t timeout)
{
        const struct lin_driver_api *api = DEVICE_API_GET(lin, dev);

        if (api->read == NULL) {
                return -ENOSYS;
        }

        return api->read(dev, msg, timeout);
}

__syscall int lin_wakeup_send(const struct device *dev);

static inline int z_impl_lin_wakeup_send(const struct device *dev)
{
        const struct lin_driver_api *api = DEVICE_API_GET(lin, dev);

        if (api->wakeup_send == NULL) {
                return -ENOSYS;
        }

        return api->wakeup_send(dev);
}

static inline int lin_set_event_callback(const struct device *dev, lin_event_callback_t callback,
                                         void *user_data)
{
        return DEVICE_API_GET(lin, dev)->set_event_callback(dev, callback, user_data);
}

__syscall int lin_set_rx_filter(const struct device *dev, const struct lin_filter *filter);

static inline int z_impl_lin_set_rx_filter(const struct device *dev,
                                           const struct lin_filter *filter)
{
        const struct lin_driver_api *api = DEVICE_API_GET(lin, dev);

        if (api->set_rx_filter == NULL) {
                return -ENOSYS;
        }

        return api->set_rx_filter(dev, filter);
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/lin.h>

#endif /* ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_LIN_H */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 720 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_LIN_H`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P007_zephyr__drivers__lin.h_头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [lin_config_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga560c00e1f3b7990836a06c83ab0eca43)
- [lin_checksum_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaf97478fd971b8b6913386a225078a24f)
- [LIN_CHECKSUM_CLASSIC](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggaf97478fd971b8b6913386a225078a24fa6b6c53f36bcccb2f099e63977bd2391a)
- [LIN_CHECKSUM_ENHANCED](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggaf97478fd971b8b6913386a225078a24fa9a93132138ea30a19f03d6bd52c8de5e)
- [lin_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gab7aca457453e6e6409c02903bcdf9bab)
- [LIN_EVT_RX_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9baba9ee3a39dbc2ff9448a5cf443db5c1625)
- [LIN_EVT_TX_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9babac57f7922e1bc6328afa742e8efa22211)
- [LIN_EVT_RX_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9baba3e30d82061bbcf51d89b63e94d362301)
- [LIN_EVT_TX_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9babaa0770ae0419aadfc97ded5e9a524a6eb)
- [LIN_EVT_TX_WAKEUP](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9babadd5da0e9a1ceb2536f11991702784508)
- [LIN_EVT_RX_WAKEUP](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9baba3d1c9ec13a13ce51893bf4c59f22cc2e)
- [LIN_EVT_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ggab7aca457453e6e6409c02903bcdf9babab70beb6e355ef5c01fe3f8f285e8dd45)
- [lin_error_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga344a6eade12faa423b8bd2718009b0c5)
- [lin_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga4d80ed442a8a83985c6ba3658f96fd16)
- [LIN_MODE_COMMANDER](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gga4d80ed442a8a83985c6ba3658f96fd16aab1c3507ec82321e02c98f4878e6475d)
- [LIN_MODE_RESPONDER](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gga4d80ed442a8a83985c6ba3658f96fd16a71650e86f1cd26ae46011a2cdce767b8)
- [lin_config](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md)
- [mode](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md#ad8c36401d16e91a9f15a93733e42c8b9)
- [baudrate](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md#aa61435f08c254683bced69fade50b775)
- [break_len](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md#a1ea39425c06334cab01e224eba5e6aea)
- [break_delimiter_len](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md#a8474d3f259ecb76b0f10ace0f78ae360)
- [flags](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md#a54077348c405316ba557ef0068a5a245)
- [lin_msg](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [id](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md#a0bbd5b4c8d50c298372d6227674843df)
- [flags](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md#a785c43cefa7fd940bf45f7729a51fb95)
- [data_len](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md#a8f9f0346d4f9f9a128150fbee2d2e3e6)
- [data](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md#ae0a650e8bbd278259f59bec5337ff955)
- [data_32](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md#aecea8811d33cfeb2c2d50a2d0cf92cbd)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [checksum_type](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md#a3f139b75c8cd61fe2085b7eac4eb828b)
- [lin_event](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md)
- [type](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#aa9a3195610f167381e89b28d054ebd10)
- [status](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#ac5b4c13e4f9cfa2bdf327269013900a8)
- [pid](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#a1ff71b532d8e117247465d6d330e32bb)
- [header](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#ad47886103edb3c8709ec51bfec4905e7)
- [bytes_received](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#a3b9f0adfcc43c3fed83ea23c10b7e67b)
- [checksum](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#af401a550032c87c4b1a1e1d1941baee0)
- [data](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#a17b7f0acfe393d09e58c2548e4f22212)
- [error_flags](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#a1e82bfb19eddb23a27fcff1bee7e0667)
- [lin_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gae69d33055fe07087a19b33dbe7a7252f)
- [device](../device_reference/P002_设备对象结构.md)
- [lin_filter](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md)
- [primary_pid](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md#a20028b04b390f8c8dc95dbc5355fdde1)
- [secondary_pid](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md#a36ac597c28bcc8f66c0369be41b6868e)
- [mask](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md#a4b7c5a4d4aea3b15fa248957071b34a8)
- [lin_start_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga149ca3972fc800c4fd2bbb0b5d8a85e3)
- [lin_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gab0f27d3ad3637f9040920b3088c1e239)
- [lin_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga39766c7605a50fcb600e9d72bfcf07d5)
- [lin_get_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga305d83d265245ed657a9974c0bab1962)
- [lin_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga8091d2d225709439f9afb2eddeb73792)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [lin_receive_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad77d365c000a2f9c7f2558ec24d0f455)
- [lin_response_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga42976918cdbcec388095d77e398e7633)
- [lin_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gabcad96f6950ec45b71adfd14e4c0c363)
- [lin_wakeup_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga16889d5f804b14ef80a608f6b8a86193)
- [lin_set_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad1df29d89982f09a9652db231e36c0c4)
- [lin_set_rx_filter_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga727b0f7fe4949e3fd17a303e239586bb)
- [lin_driver_config](../peripheral_bus_storage_model_reference/P021_lin_driver_config_结构体.md)
- [phy](../peripheral_bus_storage_model_reference/P021_lin_driver_config_结构体.md#af62ec3ddcc7c42281e0d6cf9758645f7)
- [min_bitrate](../peripheral_bus_storage_model_reference/P021_lin_driver_config_结构体.md#a561b88e59156f48fb5694cf4f00ed2ea)
- [max_bitrate](../peripheral_bus_storage_model_reference/P021_lin_driver_config_结构体.md#ae26b0452f7aa43f8f710647a6f00ea67)
- [bitrate](../peripheral_bus_storage_model_reference/P021_lin_driver_config_结构体.md#a6affbea0028b2c0876f74ff9397b41df)
- [lin_driver_data](../peripheral_bus_storage_model_reference/P022_lin_driver_data_结构体.md)
- [config](../peripheral_bus_storage_model_reference/P022_lin_driver_data_结构体.md#aa83a634b8726bf5f2ff8552aedc9ca36)
- [started](../peripheral_bus_storage_model_reference/P022_lin_driver_data_结构体.md#acfe00a4ae3aeaff0d43d51c9b8aeeec1)
- [callback](../peripheral_bus_storage_model_reference/P022_lin_driver_data_结构体.md#a5c8c75a944077f3c84d80826dbcb76a5)
- [callback_data](../peripheral_bus_storage_model_reference/P022_lin_driver_data_结构体.md#a227dd7bb9dd4778a4dcfe13d5cc29751)
- [lin_driver_api](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md)
- [start](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a538f1329573a0919ed908e58ec60c24e)
- [stop](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a72c15ca01a63897758fab966be5f71fe)
- [configure](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#acf01655ffd47f72425ef385745700569)
- [get_config](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#ada6d4e2661d5b9352d218757a69c7b10)
- [set_rx_filter](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a42abd5bd44fa028a4b2244131e5f17f4)
- [send](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#af3321e6ce2a598a4bd123b968a608633)
- [receive](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a4704606967b3eb5d7ed103e1cccfb2fd)
- [response](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a6dbb848a229b52e1d0c005a142d1d2ac)
- [read](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#adda8aa06d38c6f788eaff9e00978f9a7)
- [wakeup_send](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a4740986a33d152d9b57505334ed0df6b)
- [set_event_callback](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a91891ea072a84183ee95f7038a728ded)
- [lin_get_frame_id](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gac3d1d8680c88765a49ca9c6d04763158)
- [LIN_ID_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad37ddea1dbcc29151c7a504813eebfac)
- [lin_compute_pid](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga136329dfada85698d56308d6157abea0)
- [FIELD_GET](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html#aa49a456f06f7bdbedfcf3517e461947e)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [lin_verify_pid](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaf8bd57bf6e9306a30fa025c1f9fe09e8)
- [lin_get_transceiver](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga880b0c5dd454342160bcf454de5105e9)
- [config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)
- [lin_start](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga752004d89d50932711c3aa6189874478)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [lin_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaefe6f3853ea2f70d8ba4d6ab86f62b57)
- [lin_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga97468832dddf9e21b33e93a36c60102a)
- [lin_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga9410aa6989aea2cc173e7f36dcaf6be7)
- [lin_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga2a2afff5c7524504f24860673c24a217)
- [lin_receive](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga13e0a57996ba2f010bcda6561298b658)
- [lin_response](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gafae0fa8e806c2856f61642ef80368ec8)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [lin_read](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga58c5052899f49601a91d6da614ea8c82)
- [lin_wakeup_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga0fe3631c3f9b7100162b5f48e83bd6e3)
- [lin_set_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga07ec84c466d94f6057d7852998b2fbb2)
- [lin_set_rx_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga7594e89b4fc3a018c1cd0010bd4a6ac1)
- [clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [device::config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)
- [lin_config::break_len](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md#a1ea39425c06334cab01e224eba5e6aea)
- [lin_config::flags](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md#a54077348c405316ba557ef0068a5a245)
- [lin_config::break_delimiter_len](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md#a8474d3f259ecb76b0f10ace0f78ae360)
- [lin_config::baudrate](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md#aa61435f08c254683bced69fade50b775)
- [lin_config::mode](../peripheral_bus_storage_model_reference/P019_lin_config_结构体.md#ad8c36401d16e91a9f15a93733e42c8b9)
- [lin_driver_api::set_rx_filter](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a42abd5bd44fa028a4b2244131e5f17f4)
- [lin_driver_api::receive](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a4704606967b3eb5d7ed103e1cccfb2fd)
- [lin_driver_api::wakeup_send](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a4740986a33d152d9b57505334ed0df6b)
- [lin_driver_api::start](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a538f1329573a0919ed908e58ec60c24e)
- [lin_driver_api::response](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a6dbb848a229b52e1d0c005a142d1d2ac)
- [lin_driver_api::stop](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a72c15ca01a63897758fab966be5f71fe)
- [lin_driver_api::set_event_callback](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#a91891ea072a84183ee95f7038a728ded)
- [lin_driver_api::configure](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#acf01655ffd47f72425ef385745700569)
- [lin_driver_api::get_config](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#ada6d4e2661d5b9352d218757a69c7b10)
- [lin_driver_api::read](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#adda8aa06d38c6f788eaff9e00978f9a7)
- [lin_driver_api::send](../peripheral_bus_storage_model_reference/P020_lin_driver_api_结构体.md#af3321e6ce2a598a4bd123b968a608633)
- [lin_driver_config::min_bitrate](../peripheral_bus_storage_model_reference/P021_lin_driver_config_结构体.md#a561b88e59156f48fb5694cf4f00ed2ea)
- [lin_driver_config::bitrate](../peripheral_bus_storage_model_reference/P021_lin_driver_config_结构体.md#a6affbea0028b2c0876f74ff9397b41df)
- [lin_driver_config::max_bitrate](../peripheral_bus_storage_model_reference/P021_lin_driver_config_结构体.md#ae26b0452f7aa43f8f710647a6f00ea67)
- [lin_driver_config::phy](../peripheral_bus_storage_model_reference/P021_lin_driver_config_结构体.md#af62ec3ddcc7c42281e0d6cf9758645f7)
- [lin_driver_data::callback_data](../peripheral_bus_storage_model_reference/P022_lin_driver_data_结构体.md#a227dd7bb9dd4778a4dcfe13d5cc29751)
- [lin_driver_data::callback](../peripheral_bus_storage_model_reference/P022_lin_driver_data_结构体.md#a5c8c75a944077f3c84d80826dbcb76a5)
- [lin_driver_data::config](../peripheral_bus_storage_model_reference/P022_lin_driver_data_结构体.md#aa83a634b8726bf5f2ff8552aedc9ca36)
- [lin_driver_data::started](../peripheral_bus_storage_model_reference/P022_lin_driver_data_结构体.md#acfe00a4ae3aeaff0d43d51c9b8aeeec1)
- [lin_event::data](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#a17b7f0acfe393d09e58c2548e4f22212)
- [lin_event::error_flags](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#a1e82bfb19eddb23a27fcff1bee7e0667)
- [lin_event::pid](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#a1ff71b532d8e117247465d6d330e32bb)
- [lin_event::bytes_received](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#a3b9f0adfcc43c3fed83ea23c10b7e67b)
- [lin_event::type](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#aa9a3195610f167381e89b28d054ebd10)
- [lin_event::status](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#ac5b4c13e4f9cfa2bdf327269013900a8)
- [lin_event::header](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#ad47886103edb3c8709ec51bfec4905e7)
- [lin_event::checksum](../peripheral_bus_storage_model_reference/P023_lin_event_结构体.md#af401a550032c87c4b1a1e1d1941baee0)
- [lin_filter::primary_pid](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md#a20028b04b390f8c8dc95dbc5355fdde1)
- [lin_filter::secondary_pid](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md#a36ac597c28bcc8f66c0369be41b6868e)
- [lin_filter::mask](../peripheral_bus_storage_model_reference/P024_lin_filter_结构体.md#a4b7c5a4d4aea3b15fa248957071b34a8)
- [lin_msg::id](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md#a0bbd5b4c8d50c298372d6227674843df)
- [lin_msg::checksum_type](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md#a3f139b75c8cd61fe2085b7eac4eb828b)
- [lin_msg::flags](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md#a785c43cefa7fd940bf45f7729a51fb95)
- [lin_msg::data_len](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md#a8f9f0346d4f9f9a128150fbee2d2e3e6)
- [lin_msg::data](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md#ae0a650e8bbd278259f59bec5337ff955)
- [lin_msg::data_32](../peripheral_bus_storage_model_reference/P025_lin_msg_结构体.md#aecea8811d33cfeb2c2d50a2d0cf92cbd)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P006_zephyr__drivers__fpga.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__pmci__mctp__mctp_i2c_gpio_controller.h_头文件源码.md)
