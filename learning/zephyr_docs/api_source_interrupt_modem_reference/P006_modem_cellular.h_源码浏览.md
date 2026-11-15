---
id: learning.zephyr-docs.api-source-interrupt-modem-reference.page-6
title: modem_cellular.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modem__cellular_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_modem\_cellular.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/modem__cellular_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/modem__cellular_8h.html)。

## 6.1\_原始可见代码（Source Code）

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
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00040"></a>
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
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
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
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
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
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
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
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="foldopen00254"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="foldopen00277"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00292"></a>
<a id="l00299"></a>
<a id="l00301"></a>
<a id="l00303"></a>
<a id="l00308"></a>
<a id="l00310"></a>
<a id="l00312"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
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
<a id="l00392"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00418"></a>
<a id="foldopen00427"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
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
<a id="l00469"></a>
<a id="l00471"></a>
<a id="foldopen00482"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="foldopen00501"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="foldopen00513"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
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
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="foldopen00559"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="foldopen00580"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
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
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="foldopen00625"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00642"></a>
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
<a id="l00655"></a>
<a id="l00657"></a>
<a id="l00662"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="aatomic_8h_html"></a>
<a id="acellular_8h_html"></a>
<a id="achat_8h_html"></a>
<a id="acmux_8h_html"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="adrivers_2uart_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__cellular__interface_html_ga168002533ce39996e68bda2c2e92428e"></a>
<a id="agroup__cellular__interface_html_ga27c0b71128c782a7f42832b82eb94411"></a>
<a id="agroup__cellular__interface_html_ga2ae42cd17e07ca8e24aa75352c07e5fe"></a>
<a id="agroup__cellular__interface_html_ga5dc375b9ab33b2468846b8ca77a2106b"></a>
<a id="agroup__cellular__interface_html_ga7309390ed507748fdb72cf078b8e08a4"></a>
<a id="agroup__cellular__interface_html_ga84efd3405e5233358514c7d634710042"></a>
<a id="agroup__cellular__interface_html_gac9d02d18ed6e0af07e480cde678afdc1"></a>
<a id="agroup__modem__cellular__backend_html_ga02b8a8d17bca3f6a5bf361fdd6362b33"></a>
<a id="agroup__modem__chat_html_ga4035be227ddec8424311575305647d3e"></a>
<a id="agroup__subsys__pm__device_html_gaee5546eacb9be7caa9d59ab63926cc4c"></a>
<a id="amodem_2backend_2uart_8h_html"></a>
<a id="amodem_2ppp_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="apipe_8h_html"></a>
<a id="apipelink_8h_html"></a>
<a id="apm_2device_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructcellular__driver__api_html"></a>
<a id="astructcellular__evt__network__status_html"></a>
<a id="astructcellular__stats_html"></a>
<a id="astructdevice_html"></a>
<a id="astructgpio__callback_html"></a>
<a id="astructgpio__dt__spec_html"></a>
<a id="astructk__msgq_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructk__work_html"></a>
<a id="astructmodem__backend__uart_html"></a>
<a id="astructmodem__cellular__board__init_html"></a>
<a id="astructmodem__cellular__board__init_html_a4e1bb0a376530c370edf8e0d993b0e28"></a>
<a id="astructmodem__cellular__board__init_html_a9cb679dd7826435256334e55c163c9fc"></a>
<a id="astructmodem__cellular__config__scripts_html"></a>
<a id="astructmodem__cellular__config__scripts_html_a10d764e69608d3cf70178eaa9f82cb86"></a>
<a id="astructmodem__cellular__config__scripts_html_a1a7cd1d3932f81ef30714d4d9d50e2ee"></a>
<a id="astructmodem__cellular__config__scripts_html_a1d1e340cef1848413eb9269094d4502d"></a>
<a id="astructmodem__cellular__config__scripts_html_a3f9a561d25bbabe27e0dc5920eb9eed5"></a>
<a id="astructmodem__cellular__config__scripts_html_a900207cd3ef0a6003fad53a7d47773ee"></a>
<a id="astructmodem__cellular__config__scripts_html_ae52b436497e5250c7df4ed18d4819436"></a>
<a id="astructmodem__cellular__config__scripts_html_ae92a8fb7e262369c1110d9a47a54a6ca"></a>
<a id="astructmodem__cellular__data_html"></a>
<a id="astructmodem__cellular__vendor__config_html"></a>
<a id="astructmodem__cellular__vendor__config_html_a2f6a9b8f14ddf2650562b3348cedabfd"></a>
<a id="astructmodem__cellular__vendor__config_html_a3b4fb8542f1a4903b54b49c667e2378c"></a>
<a id="astructmodem__cellular__vendor__config_html_a52e33fceac79378e370675d567de2b5e"></a>
<a id="astructmodem__cellular__vendor__config_html_a5b19228e384856ac3a57af617b4afcf0"></a>
<a id="astructmodem__cellular__vendor__config_html_a7dee75ad296954cc33932aa98186f0a6"></a>
<a id="astructmodem__cellular__vendor__config_html_a84e1ccc5a311240a4c7d356ec7d90f5f"></a>
<a id="astructmodem__cellular__vendor__config_html_a8d14f4c96be18fb575beffd5768bc16c"></a>
<a id="astructmodem__cellular__vendor__config_html_a90b312d50b585d13a3d56f9974e17251"></a>
<a id="astructmodem__cellular__vendor__config_html_a95eca8f1f380a97f64f46e0a80b58922"></a>
<a id="astructmodem__cellular__vendor__config_html_a967f56a3ec4e1c331db02e71ebf2fdeb"></a>
<a id="astructmodem__cellular__vendor__config_html_af37df7d8e6ef21cffc52fd4bc0b3dec2"></a>
<a id="astructmodem__cellular__vendor__config_html_affae7b69107c6f63f59bb6c64e844cdb"></a>
<a id="astructmodem__chat__match_html"></a>
<a id="astructmodem__chat__script__chat_html"></a>
<a id="astructmodem__chat__script__completion__info_html"></a>
<a id="astructmodem__chat__script_html"></a>
<a id="astructmodem__chat_html"></a>
<a id="astructnet__mgmt__event__callback_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CELLULAR_INTERNAL_H_
#define ZEPHYR_INCLUDE_DRIVERS_CELLULAR_INTERNAL_H_

#include <zephyr/drivers/cellular.h>
#include <zephyr/modem/backend/uart.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/pm/device.h>
#include <zephyr/modem/chat.h>
#include <zephyr/modem/cmux.h>
#include <zephyr/modem/pipe.h>
#include <zephyr/modem/pipelink.h>
#include <zephyr/modem/ppp.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/atomic.h>

#ifdef __cplusplus
extern "C" {
#endif



#define MODEM_CELLULAR_DATA_IMEI_LEN         (16)
#define MODEM_CELLULAR_DATA_SN_LEN           (CONFIG_MODEM_CELLULAR_SERIAL_NUMBER_MAX_SIZE + 1)
#define MODEM_CELLULAR_DATA_MODEL_ID_LEN     (65)
#define MODEM_CELLULAR_DATA_IMSI_LEN         (23)
#define MODEM_CELLULAR_DATA_ICCID_LEN        (22)
#define MODEM_CELLULAR_DATA_MANUFACTURER_LEN (65)
#define MODEM_CELLULAR_DATA_FW_VERSION_LEN   (65)
#define MODEM_CELLULAR_DATA_APN_LEN          (32)
#define MODEM_CELLULAR_MAX_APN_CMDS          (2)
#define MODEM_CELLULAR_APN_BUF_SIZE          (64)

/* Zephyr networking interface states:
 *    NET_IF_LOWER_UP: Carrier is on in AWAIT_REGISTERED and REGISTERED
 *     NET_IF_DORMANT: Interface is dormant in every state except REGISTERED
 */
enum modem_cellular_state {
        MODEM_CELLULAR_STATE_IDLE = 0,
        MODEM_CELLULAR_STATE_RECOVERY,
        MODEM_CELLULAR_STATE_RESET_PULSE,
        MODEM_CELLULAR_STATE_AWAIT_RESET,
        MODEM_CELLULAR_STATE_POWER_ON_PULSE,
        MODEM_CELLULAR_STATE_AWAIT_POWER_ON,
        MODEM_CELLULAR_STATE_SET_BAUDRATE,
        MODEM_CELLULAR_STATE_RUN_INIT_SCRIPT,
        MODEM_CELLULAR_STATE_CONNECT_CMUX,
        MODEM_CELLULAR_STATE_OPEN_DLCI1,
        MODEM_CELLULAR_STATE_OPEN_DLCI2,
        MODEM_CELLULAR_STATE_RUN_BOARD_INIT_SCRIPT,
        MODEM_CELLULAR_STATE_WAIT_FOR_APN,
        MODEM_CELLULAR_STATE_RUN_APN_SCRIPT,
        MODEM_CELLULAR_STATE_RUN_NETWORK_SCRIPT,
        MODEM_CELLULAR_STATE_RUN_DIAL_SCRIPT,
        MODEM_CELLULAR_STATE_AWAIT_REGISTERED,
        MODEM_CELLULAR_STATE_REGISTERED,
        MODEM_CELLULAR_STATE_AWAIT_PPP_DEAD,
        MODEM_CELLULAR_STATE_INIT_POWER_OFF,
        MODEM_CELLULAR_STATE_RUN_SHUTDOWN_SCRIPT,
        MODEM_CELLULAR_STATE_POWER_OFF_PULSE,
        MODEM_CELLULAR_STATE_AWAIT_POWER_OFF,
        MODEM_CELLULAR_STATE_AWAIT_DIAL,
};

enum modem_cellular_event {
        MODEM_CELLULAR_EVENT_RESUME = 0,
        MODEM_CELLULAR_EVENT_SUSPEND,
        MODEM_CELLULAR_EVENT_SCRIPT_SUCCESS,
        MODEM_CELLULAR_EVENT_SCRIPT_FAILED,
        MODEM_CELLULAR_EVENT_CMUX_CONNECTED,
        MODEM_CELLULAR_EVENT_CMUX_DISCONNECTED,
        MODEM_CELLULAR_EVENT_DLCI1_OPENED,
        MODEM_CELLULAR_EVENT_DLCI2_OPENED,
        MODEM_CELLULAR_EVENT_TIMEOUT,
        MODEM_CELLULAR_EVENT_REGISTERED,
        MODEM_CELLULAR_EVENT_DEREGISTERED,
        MODEM_CELLULAR_EVENT_BUS_OPENED,
        MODEM_CELLULAR_EVENT_BUS_CLOSED,
        MODEM_CELLULAR_EVENT_PPP_DEAD,
        MODEM_CELLULAR_EVENT_MODEM_READY,
        MODEM_CELLULAR_EVENT_APN_SET,
        MODEM_CELLULAR_EVENT_RING,
        MODEM_CELLULAR_EVENT_PERIODIC_KICK,
        MODEM_CELLULAR_EVENT_DIAL,
        MODEM_CELLULAR_EVENT_HANGUP,
} __packed;

struct modem_cellular_event_cb {
        cellular_event_mask_t mask;
        cellular_event_cb_t fn;
        void *user_data;
};

struct modem_cellular_event_pkg {
        uint8_t event;
        const void *ptr;
};


struct modem_cellular_data {
        /* UART backend */
        struct modem_pipe *uart_pipe;
        struct modem_backend_uart uart_backend;
        uint8_t uart_backend_receive_buf[CONFIG_MODEM_CELLULAR_UART_BUFFER_SIZES];
        uint8_t uart_backend_transmit_buf[CONFIG_MODEM_CELLULAR_UART_BUFFER_SIZES];
        uint32_t original_baudrate;

        /* CMUX */
        struct modem_cmux cmux;
        uint8_t cmux_receive_buf[MODEM_CMUX_WORK_BUFFER_SIZE];
        uint8_t cmux_transmit_buf[MODEM_CMUX_WORK_BUFFER_SIZE];

        struct modem_cmux_dlci dlci1;
        struct modem_cmux_dlci dlci2;
        struct modem_pipe *dlci1_pipe;
        struct modem_pipe *dlci2_pipe;
        /* Points to dlci1_pipe or NULL. Used for shutdown script if not NULL */
        struct modem_pipe *cmd_pipe;
        uint8_t dlci1_receive_buf[MODEM_CMUX_WORK_BUFFER_SIZE];
        /* DLCI 2 is only used for chat scripts. */
        uint8_t dlci2_receive_buf[MODEM_CMUX_WORK_BUFFER_SIZE];

        /* Modem chat */
        struct modem_chat chat;
        uint8_t chat_receive_buf[CONFIG_MODEM_CELLULAR_CHAT_BUFFER_SIZE];
        uint8_t *chat_argv[32];
        uint8_t script_failure_counter;
        uint8_t recovery_count;

        /* Status */
        enum cellular_registration_status registration_status_gsm;
        enum cellular_registration_status registration_status_gprs;
        enum cellular_registration_status registration_status_lte;
        enum cellular_registration_status registration_status_5g;
        enum cellular_access_technology access_tech;
        uint8_t rssi;
        uint8_t rsrp;
        uint8_t rsrq;
        struct cellular_evt_network_status network_status;
        bool network_status_valid;
        uint8_t imei[MODEM_CELLULAR_DATA_IMEI_LEN];
        uint8_t sn[MODEM_CELLULAR_DATA_SN_LEN];
        uint8_t model_id[MODEM_CELLULAR_DATA_MODEL_ID_LEN];
        uint8_t imsi[MODEM_CELLULAR_DATA_IMSI_LEN];
        uint8_t iccid[MODEM_CELLULAR_DATA_ICCID_LEN];
        uint8_t manufacturer[MODEM_CELLULAR_DATA_MANUFACTURER_LEN];
        uint8_t fw_version[MODEM_CELLULAR_DATA_FW_VERSION_LEN];
        uint8_t apn[MODEM_CELLULAR_DATA_APN_LEN];

        struct modem_chat_script_chat apn_chats[MODEM_CELLULAR_MAX_APN_CMDS];
        struct modem_chat_script apn_script;
        char apn_buf[MODEM_CELLULAR_MAX_APN_CMDS][MODEM_CELLULAR_APN_BUF_SIZE];

        struct modem_chat_script board_init_script;

        struct net_mgmt_event_callback net_mgmt_event_callback;
#if defined(CONFIG_MODEM_CELLULAR_ON_DEMAND_CONNECT)
        struct net_mgmt_event_callback if_event_callback;
#endif

        enum modem_cellular_state state;
        const struct device *dev;
        struct k_work_delayable timeout_work;

        /* Power management */
        struct k_sem suspended_sem;

        /* Event dispatcher */
        struct k_work event_dispatch_work;
        struct k_msgq event_queue;
        struct modem_cellular_event_pkg event_buf[8];
        const void *event_ptr;

        struct k_mutex api_lock;
        struct modem_cellular_event_cb cb;

        /* Ring interrupt */
        struct gpio_callback ring_gpio_cb;

        atomic_t periodic_paused;
        bool periodic_timeout_skipped;
        bool power_on_skipped;

#if defined(CONFIG_MODEM_CELLULAR_STATS)
        struct cellular_stats stats;
        uint32_t stats_outage_start_ms;
#endif
};


struct modem_cellular_user_pipe {
        struct modem_cmux_dlci dlci;
        uint8_t dlci_address;
        uint8_t *dlci_receive_buf;
        uint16_t dlci_receive_buf_size;
        struct modem_pipe *pipe;
        struct modem_pipelink *pipelink;
};


struct modem_cellular_config_scripts {
        const struct modem_chat_script *set_baudrate;
        const struct modem_chat_script *init;
        const struct modem_chat_script *network;
        const struct modem_chat_script *dial;
        const struct modem_chat_script *periodic;
        const struct modem_chat_script *shutdown;
        const struct modem_chat_script *dlci_setup;
};

struct modem_cellular_vendor_config {
        struct modem_cellular_config_scripts scripts;
        struct {
                const struct modem_chat_match *matches;
                uint16_t size;
        } unsol_matches;
        const char *chat_delimiter;
        const char *chat_filter;
        uint16_t power_pulse_duration_ms;
        uint16_t reset_pulse_duration_ms;
        uint16_t cmux_disconnect_timeout_ms;
        uint16_t startup_time_ms;
        uint16_t shutdown_time_ms;
        bool force_autostart;
};


struct modem_cellular_config {
        const struct device *uart;
        const struct modem_cellular_vendor_config *vendor;
        const void *vendor_specific;
        struct modem_ppp *ppp;
        struct gpio_dt_spec power_gpio;
        struct gpio_dt_spec reset_gpio;
        struct gpio_dt_spec wake_gpio;
        struct gpio_dt_spec ring_gpio;
        struct gpio_dt_spec dtr_gpio;
        struct gpio_dt_spec status_gpio;
        bool autostarts;
        bool hold_reset_on_suspend;
        bool reset_on_resume;
        bool reset_on_recovery;
        bool cmux_enable_runtime_power_save;
        bool cmux_close_pipe_on_power_save;
        bool cmux_no_powersave_handshake;
        bool use_default_pdp_context;
        bool use_default_apn;
        k_timeout_t cmux_idle_timeout;
        struct modem_cellular_user_pipe *user_pipes;
        uint8_t user_pipes_size;
};

int modem_cellular_init(const struct device *dev);

int modem_cellular_pm_action(const struct device *dev, enum pm_device_action action);

extern const struct cellular_driver_api modem_cellular_api;

void modem_cellular_emit_event(struct modem_cellular_data *data, enum cellular_event evt,
                               const void *payload);

/*
 * Store the latest serving-cell status and emit CELLULAR_EVENT_NETWORK_STATUS_CHANGED
 * only when it changed, ignoring signal quality (rsrp/rsrq) so periodic polls do not
 * re-fire the event on signal fluctuation.
 */
void modem_cellular_emit_network_status(struct modem_cellular_data *data,
                                        const struct cellular_evt_network_status *status);

void modem_cellular_chat_on_imei(struct modem_chat *chat, char **argv, uint16_t argc,
                                 void *user_data);
void modem_cellular_chat_on_cgsn_sn(struct modem_chat *chat, char **argv, uint16_t argc,
                                    void *user_data);
void modem_cellular_chat_on_cgsn_imei(struct modem_chat *chat, char **argv, uint16_t argc,
                                      void *user_data);
void modem_cellular_chat_on_cgmm(struct modem_chat *chat, char **argv, uint16_t argc,
                                 void *user_data);
void modem_cellular_chat_on_csq(struct modem_chat *chat, char **argv, uint16_t argc,
                                void *user_data);
void modem_cellular_chat_on_cesq(struct modem_chat *chat, char **argv, uint16_t argc,
                                 void *user_data);
void modem_cellular_chat_on_iccid(struct modem_chat *chat, char **argv, uint16_t argc,
                                  void *user_data);
void modem_cellular_chat_on_imsi(struct modem_chat *chat, char **argv, uint16_t argc,
                                 void *user_data);
void modem_cellular_chat_on_cgmi(struct modem_chat *chat, char **argv, uint16_t argc,
                                 void *user_data);
void modem_cellular_chat_on_cgmr(struct modem_chat *chat, char **argv, uint16_t argc,
                                 void *user_data);
void modem_cellular_chat_on_cxreg(struct modem_chat *chat, char **argv, uint16_t argc,
                                  void *user_data);
void modem_cellular_chat_on_cgev(struct modem_chat *chat, char **argv, uint16_t argc,
                                 void *user_data);
void modem_cellular_chat_on_modem_ready(struct modem_chat *chat, char **argv, uint16_t argc,
                                        void *user_data);


void modem_cellular_chat_callback_handler(struct modem_chat *chat,
                                          enum modem_chat_script_result result,
                                          const struct modem_chat_script_completion_info *info,
                                          void *user_data);


#define MODEM_CELLULAR_INST_NAME(name, inst) \
        CONCAT(name, _, DT_DRV_COMPAT, inst)


#define MODEM_CELLULAR_DEFINE_USER_PIPE_DATA(inst, name, size)                                     \
        MODEM_PIPELINK_DT_INST_DEFINE(inst, name);                                                 \
        static uint8_t MODEM_CELLULAR_INST_NAME(name, inst)[size]                                  \

#define MODEM_CELLULAR_INIT_USER_PIPE(_inst, _name, _dlci_address)                                 \
        {                                                                                          \
                .dlci_address = _dlci_address,                                                     \
                .dlci_receive_buf = MODEM_CELLULAR_INST_NAME(_name, _inst),                        \
                .dlci_receive_buf_size = sizeof(MODEM_CELLULAR_INST_NAME(_name, _inst)),           \
                .pipelink = MODEM_PIPELINK_DT_INST_GET(_inst, _name),                              \
        }

#define MODEM_CELLULAR_DEFINE_USER_PIPES(inst, ...)                                                \
        static struct modem_cellular_user_pipe MODEM_CELLULAR_INST_NAME(user_pipes, inst)[] = {    \
                __VA_ARGS__                                                                        \
        }

#define MODEM_CELLULAR_GET_USER_PIPES(inst) \
        MODEM_CELLULAR_INST_NAME(user_pipes, inst)

/* Extract the first argument (pipe name) from a pair */
#define MODEM_CELLULAR_GET_PIPE_NAME_ARG(arg1, ...) arg1

/* Extract the second argument (DLCI address) from a pair */
#define MODEM_CELLULAR_GET_DLCI_ADDRESS_ARG(arg1, arg2, ...) arg2

/* Define user pipe data using instance and extracted pipe name */
#define MODEM_CELLULAR_DEFINE_USER_PIPE_DATA_HELPER(_args, inst)                                   \
        MODEM_CELLULAR_DEFINE_USER_PIPE_DATA(inst,                                                 \
                                             MODEM_CELLULAR_GET_PIPE_NAME_ARG _args,               \
                                             CONFIG_MODEM_CELLULAR_USER_PIPE_BUFFER_SIZES)

/* Initialize user pipe using instance, extracted pipe name, and DLCI address */
#define MODEM_CELLULAR_INIT_USER_PIPE_HELPER(_args, inst)                                          \
        MODEM_CELLULAR_INIT_USER_PIPE(inst,                                                        \
                                      MODEM_CELLULAR_GET_PIPE_NAME_ARG _args,                      \
                                      MODEM_CELLULAR_GET_DLCI_ADDRESS_ARG _args)


#define MODEM_CELLULAR_DEFINE_AND_INIT_USER_PIPES(inst, ...)                                       \
        FOR_EACH_FIXED_ARG(MODEM_CELLULAR_DEFINE_USER_PIPE_DATA_HELPER,                            \
                           (;), inst, __VA_ARGS__);                                                \
        MODEM_CELLULAR_DEFINE_USER_PIPES(                                                          \
                inst,                                                                              \
                FOR_EACH_FIXED_ARG(MODEM_CELLULAR_INIT_USER_PIPE_HELPER,                           \
                                   (,), inst, __VA_ARGS__)                                         \
        );

#define MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(_sym, _match, _separators, _callback)                  \
        MODEM_CHAT_MATCHES_DEFINE(_sym,                                                            \
                MODEM_CHAT_MATCH_INITIALIZER(_match, _separators, _callback, false, true),         \
                MODEM_CHAT_MATCH("OK", "", NULL))

#define MODEM_CELLULAR_COMMON_CHAT_MATCHES()                                                       \
        MODEM_CHAT_MATCH_DEFINE(ok_match, "OK", "", NULL);                                         \
        MODEM_CHAT_MATCHES_DEFINE(__maybe_unused allow_match,                                      \
                                  MODEM_CHAT_MATCH("OK", "", NULL),                                \
                                  MODEM_CHAT_MATCH("ERROR", "", NULL));                            \
        MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused imei_match,                             \
                                "", "", modem_cellular_chat_on_imei);                              \
        MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cgsn_sn_match,                          \
                                "", "", modem_cellular_chat_on_cgsn_sn);                           \
        MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cgsn_imei_match,                        \
                                "+CGSN: ", "", modem_cellular_chat_on_cgsn_imei);                  \
        MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cgmm_match,                             \
                                "", "", modem_cellular_chat_on_cgmm);                              \
        MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused csq_match,                              \
                                "+CSQ: ", ",", modem_cellular_chat_on_csq);                        \
        MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cesq_match,                             \
                                "+CESQ: ", ",", modem_cellular_chat_on_cesq);                      \
        MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused qccid_match,                            \
                                "+QCCID: ", "", modem_cellular_chat_on_iccid);                     \
        MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused iccid_match,                            \
                                "+ICCID: ", "", modem_cellular_chat_on_iccid);                     \
        MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused ccid_match,                             \
                                "+CCID: ", "", modem_cellular_chat_on_iccid);                      \
        MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cimi_match,                             \
                                "", "", modem_cellular_chat_on_imsi);                              \
        MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cgmi_match,                             \
                                "", "", modem_cellular_chat_on_cgmi);                              \
        MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(__maybe_unused cgmr_match,                             \
                                "", "", modem_cellular_chat_on_cgmr);                              \
        MODEM_CHAT_MATCH_DEFINE(connect_match __maybe_unused,                                      \
                                "CONNECT", "", NULL);                                              \
        MODEM_CHAT_MATCHES_DEFINE(__maybe_unused abort_matches,                                    \
                                  MODEM_CHAT_MATCH("ERROR", "", NULL));                            \
        MODEM_CHAT_MATCHES_DEFINE(__maybe_unused dial_abort_matches,                               \
                                  MODEM_CHAT_MATCH("ERROR", "", NULL),                             \
                                  MODEM_CHAT_MATCH("BUSY", "", NULL),                              \
                                  MODEM_CHAT_MATCH("NO ANSWER", "", NULL),                         \
                                  MODEM_CHAT_MATCH("NO CARRIER", "", NULL),                        \
                                  MODEM_CHAT_MATCH("NO DIALTONE", "", NULL))

#define MODEM_CELLULAR_COMMON_UNSOL_MATCHES                                                        \
        MODEM_CHAT_MATCH("+CREG: ", ",", modem_cellular_chat_on_cxreg),                            \
        MODEM_CHAT_MATCH("+CEREG: ", ",", modem_cellular_chat_on_cxreg),                           \
        MODEM_CHAT_MATCH("+CGREG: ", ",", modem_cellular_chat_on_cxreg),                           \
        MODEM_CHAT_MATCH("+CGEV: ", ",", modem_cellular_chat_on_cgev),                             \
        MODEM_CHAT_MATCH("APP RDY", "", modem_cellular_chat_on_modem_ready),                       \
        MODEM_CHAT_MATCH("Ready", "", modem_cellular_chat_on_modem_ready)

#define MODEM_CELLULAR_DEFINE_INSTANCE(inst, vendor_config, _vendor_specific)                      \
        BUILD_ASSERT(vendor_config != NULL, "vendor_config must be non-NULL");                     \
        static const struct modem_cellular_config MODEM_CELLULAR_INST_NAME(config, inst) = {       \
                .uart = DEVICE_DT_GET(DT_INST_BUS(inst)),                                          \
                .vendor = vendor_config,                                                           \
                .vendor_specific = _vendor_specific,                                               \
                .ppp = &MODEM_CELLULAR_INST_NAME(ppp, inst),                                       \
                .power_gpio = GPIO_DT_SPEC_INST_GET_OR(inst, mdm_power_gpios, {}),                 \
                .reset_gpio = GPIO_DT_SPEC_INST_GET_OR(inst, mdm_reset_gpios, {}),                 \
                .wake_gpio = GPIO_DT_SPEC_INST_GET_OR(inst, mdm_wake_gpios, {}),                   \
                .ring_gpio = GPIO_DT_SPEC_INST_GET_OR(inst, mdm_ring_gpios, {}),                   \
                .dtr_gpio = GPIO_DT_SPEC_INST_GET_OR(inst, mdm_dtr_gpios, {}),                     \
                .status_gpio = GPIO_DT_SPEC_INST_GET_OR(inst, mdm_status_gpios, {}),               \
                .autostarts = DT_INST_PROP(inst, autostarts),                                      \
                .hold_reset_on_suspend =                                                           \
                        DT_INST_ENUM_HAS_VALUE(inst, zephyr_mdm_reset_behavior, hold_on_suspend),  \
                .reset_on_resume = DT_INST_ENUM_HAS_VALUE(inst, zephyr_mdm_reset_behavior,         \
                                                            toggle_on_resume),                     \
                .reset_on_recovery = DT_INST_ENUM_HAS_VALUE(inst, zephyr_mdm_reset_behavior,       \
                                                            toggle_on_recovery),                   \
                .cmux_enable_runtime_power_save =                                                  \
                        DT_INST_PROP_OR(inst, cmux_enable_runtime_power_save, 0),                  \
                .cmux_close_pipe_on_power_save =                                                   \
                        DT_INST_PROP_OR(inst, cmux_close_pipe_on_power_save, 0),                   \
                .cmux_no_powersave_handshake =                                                     \
                        DT_INST_PROP_OR(inst, cmux_no_powersave_handshake, 0),                     \
                .use_default_pdp_context = DT_INST_PROP_OR(inst, zephyr_use_default_pdp_ctx, 0),   \
                .use_default_apn = DT_INST_PROP_OR(inst, zephyr_use_default_apn, 0),               \
                .cmux_idle_timeout = K_MSEC(DT_INST_PROP_OR(inst, cmux_idle_timeout_ms, 0)),       \
                .user_pipes = MODEM_CELLULAR_GET_USER_PIPES(inst),                                 \
                .user_pipes_size = ARRAY_SIZE(MODEM_CELLULAR_GET_USER_PIPES(inst)),                \
        };                                                                                         \
                                                                                                   \
        PM_DEVICE_DT_INST_DEFINE(inst, modem_cellular_pm_action);                                  \
                                                                                                   \
        DEVICE_DT_INST_DEFINE(inst, modem_cellular_init, PM_DEVICE_DT_INST_GET(inst),              \
                              &MODEM_CELLULAR_INST_NAME(data, inst),                               \
                              &MODEM_CELLULAR_INST_NAME(config, inst), POST_KERNEL,                \
                              CONFIG_MODEM_CELLULAR_INIT_PRIORITY, &modem_cellular_api);

struct modem_cellular_board_init {
        const struct device *dev;
        const struct modem_chat_script *script;
};

#if defined(CONFIG_MODEM_CELLULAR)
#define MODEM_CELLULAR_BOARD_INIT_DEFINE(node_id, _script)                                         \
        static const STRUCT_SECTION_ITERABLE(                                                      \
                modem_cellular_board_init,                                                         \
                CONCAT(modem_cellular_board_init_, DT_DEP_ORD(node_id))) = {                       \
                .dev = DEVICE_DT_GET(node_id),                                                     \
                .script = (_script),                                                               \
        }
#else
#define MODEM_CELLULAR_BOARD_INIT_DEFINE(node_id, _script)
#endif




int cellular_modem_pause_periodic_script(const struct device *dev);

int cellular_modem_resume_periodic_script(const struct device *dev);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_CELLULAR_INTERNAL_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 54 行

Zephyr 网络接口状态（networking interface states）：`NET_IF_LOWER_UP` 表示载波有效，在 `AWAIT_REGISTERED` 和 `REGISTERED` 状态下置位；`NET_IF_DORMANT` 表示接口休眠，除 `REGISTERED` 之外的所有状态下均如此。

### 注释 3：原第 131 行

UART 后端（backend）。

### 注释 4：原第 138 行

串口多路复用（CMUX）。

### 注释 5：原第 147 行

指向 `dlci1_pipe` 或为 `NULL`。不为 `NULL` 时供关闭脚本（shutdown script）使用。

### 注释 6：原第 150 行

DLCI 2 仅用于交互脚本（chat scripts）。

### 注释 7：原第 153 行

调制解调器交互（modem chat）。

### 注释 8：原第 160 行

状态（Status）。

### 注释 9：原第 195 行

电源管理（power management）。

### 注释 10：原第 198 行

事件分发器（event dispatcher）。

### 注释 11：原第 207 行

振铃中断（ring interrupt）。

### 注释 12：原第 356 行

保存最新的服务小区状态（serving-cell status），仅在该状态变化时发出 `CELLULAR_EVENT_NETWORK_STATUS_CHANGED`。忽略信号质量（RSRP/RSRQ），以免周期性轮询因信号波动反复触发事件。

### 注释 13：原第 452 行

从一对参数中提取第一个参数，即管道名称（pipe name）。

### 注释 14：原第 455 行

从一对参数中提取第二个参数，即 DLCI 地址。

### 注释 15：原第 458 行

使用实例及提取的管道名称定义用户管道数据。

### 注释 16：原第 464 行

使用实例、提取的管道名称和 DLCI 地址初始化用户管道。

### 注释 17：原第 704 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CELLULAR_INTERNAL_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/modem__cellular_8h.html)
- [zephyr/drivers/cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h.html)
- [zephyr/modem/backend/uart.h](../api_file_reference/P229_zephyr__modem__backend__uart.h_文件参考.md)
- [zephyr/drivers/uart.h](../uart_driver_reference/P001_UART驱动头文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [zephyr/pm/device.h](../power/P069_设备电源管理头文件.md)
- [zephyr/modem/chat.h](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h.html)
- [zephyr/modem/cmux.h](https://docs.zephyrproject.org/latest/doxygen/html/cmux_8h.html)
- [zephyr/modem/pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [zephyr/modem/pipelink.h](https://docs.zephyrproject.org/latest/doxygen/html/pipelink_8h.html)
- [zephyr/modem/ppp.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ppp_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [cellular_event_mask_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga84efd3405e5233358514c7d634710042)
- [cellular_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gac9d02d18ed6e0af07e480cde678afdc1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [modem_cellular_data](../modem_wireless_model_reference/P050_modem_cellular_data_结构体.md)
- [modem_backend_uart](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)
- [cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)
- [cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)
- [cellular_evt_network_status](../modem_wireless_model_reference/P005_cellular_evt_network_status_结构体.md)
- [modem_chat_script_chat](../modem_wireless_model_reference/P056_modem_chat_script_chat_结构体.md)
- [modem_chat_script](../modem_wireless_model_reference/P055_modem_chat_script_结构体.md)
- [net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [device](../device_reference/P002_设备对象结构.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [gpio_callback](../hardware/P270_GPIO回调结构.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [cellular_stats](../modem_wireless_model_reference/P008_cellular_stats_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [modem_cellular_config_scripts](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md)
- [set_baudrate](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#a3f9a561d25bbabe27e0dc5920eb9eed5)
- [init](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#ae52b436497e5250c7df4ed18d4819436)
- [network](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#a1d1e340cef1848413eb9269094d4502d)
- [dial](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#a1a7cd1d3932f81ef30714d4d9d50e2ee)
- [periodic](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#a10d764e69608d3cf70178eaa9f82cb86)
- [shutdown](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#a900207cd3ef0a6003fad53a7d47773ee)
- [dlci_setup](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#ae92a8fb7e262369c1110d9a47a54a6ca)
- [modem_cellular_vendor_config](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md)
- [scripts](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a7dee75ad296954cc33932aa98186f0a6)
- [modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)
- [matches](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a84e1ccc5a311240a4c7d356ec7d90f5f)
- [size](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a8d14f4c96be18fb575beffd5768bc16c)
- [unsol_matches](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#affae7b69107c6f63f59bb6c64e844cdb)
- [chat_delimiter](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a5b19228e384856ac3a57af617b4afcf0)
- [chat_filter](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a95eca8f1f380a97f64f46e0a80b58922)
- [power_pulse_duration_ms](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a90b312d50b585d13a3d56f9974e17251)
- [reset_pulse_duration_ms](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a3b4fb8542f1a4903b54b49c667e2378c)
- [cmux_disconnect_timeout_ms](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a967f56a3ec4e1c331db02e71ebf2fdeb)
- [startup_time_ms](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#af37df7d8e6ef21cffc52fd4bc0b3dec2)
- [shutdown_time_ms](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a2f6a9b8f14ddf2650562b3348cedabfd)
- [force_autostart](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a52e33fceac79378e370675d567de2b5e)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [pm_device_action](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gaee5546eacb9be7caa9d59ab63926cc4c)
- [cellular_driver_api](../modem_wireless_model_reference/P002_cellular_driver_api_结构体.md)
- [cellular_event](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga27c0b71128c782a7f42832b82eb94411)
- [modem_cellular_chat_callback_handler](../api_protocol_topic_reference/P033_蜂窝调制解调器辅助功能（Cellular modem helpers）.md#ga02b8a8d17bca3f6a5bf361fdd6362b33)
- [modem_chat_script_result](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga4035be227ddec8424311575305647d3e)
- [modem_chat_script_completion_info](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md)
- [modem_cellular_board_init](../modem_wireless_model_reference/P048_modem_cellular_board_init_结构体.md)
- [dev](../modem_wireless_model_reference/P048_modem_cellular_board_init_结构体.md#a9cb679dd7826435256334e55c163c9fc)
- [script](../modem_wireless_model_reference/P048_modem_cellular_board_init_结构体.md#a4e1bb0a376530c370edf8e0d993b0e28)
- [cellular_modem_pause_periodic_script](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga2ae42cd17e07ca8e24aa75352c07e5fe)
- [cellular_modem_resume_periodic_script](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga5dc375b9ab33b2468846b8ca77a2106b)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h.html)
- [chat.h](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h.html)
- [cmux.h](https://docs.zephyrproject.org/latest/doxygen/html/cmux_8h.html)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [uart.h](../uart_driver_reference/P001_UART驱动头文件参考.md)
- [uart.h](../api_file_reference/P229_zephyr__modem__backend__uart.h_文件参考.md)
- [ppp.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ppp_8h.html)
- [pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [pipelink.h](https://docs.zephyrproject.org/latest/doxygen/html/pipelink_8h.html)
- [device.h](../power/P069_设备电源管理头文件.md)
- [modem_cellular_board_init::script](../modem_wireless_model_reference/P048_modem_cellular_board_init_结构体.md#a4e1bb0a376530c370edf8e0d993b0e28)
- [modem_cellular_board_init::dev](../modem_wireless_model_reference/P048_modem_cellular_board_init_结构体.md#a9cb679dd7826435256334e55c163c9fc)
- [modem_cellular_config_scripts::periodic](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#a10d764e69608d3cf70178eaa9f82cb86)
- [modem_cellular_config_scripts::dial](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#a1a7cd1d3932f81ef30714d4d9d50e2ee)
- [modem_cellular_config_scripts::network](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#a1d1e340cef1848413eb9269094d4502d)
- [modem_cellular_config_scripts::set_baudrate](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#a3f9a561d25bbabe27e0dc5920eb9eed5)
- [modem_cellular_config_scripts::shutdown](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#a900207cd3ef0a6003fad53a7d47773ee)
- [modem_cellular_config_scripts::init](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#ae52b436497e5250c7df4ed18d4819436)
- [modem_cellular_config_scripts::dlci_setup](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md#ae92a8fb7e262369c1110d9a47a54a6ca)
- [modem_cellular_vendor_config::shutdown_time_ms](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a2f6a9b8f14ddf2650562b3348cedabfd)
- [modem_cellular_vendor_config::reset_pulse_duration_ms](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a3b4fb8542f1a4903b54b49c667e2378c)
- [modem_cellular_vendor_config::force_autostart](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a52e33fceac79378e370675d567de2b5e)
- [modem_cellular_vendor_config::chat_delimiter](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a5b19228e384856ac3a57af617b4afcf0)
- [modem_cellular_vendor_config::scripts](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a7dee75ad296954cc33932aa98186f0a6)
- [modem_cellular_vendor_config::matches](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a84e1ccc5a311240a4c7d356ec7d90f5f)
- [modem_cellular_vendor_config::size](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a8d14f4c96be18fb575beffd5768bc16c)
- [modem_cellular_vendor_config::power_pulse_duration_ms](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a90b312d50b585d13a3d56f9974e17251)
- [modem_cellular_vendor_config::chat_filter](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a95eca8f1f380a97f64f46e0a80b58922)
- [modem_cellular_vendor_config::cmux_disconnect_timeout_ms](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#a967f56a3ec4e1c331db02e71ebf2fdeb)
- [modem_cellular_vendor_config::startup_time_ms](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#af37df7d8e6ef21cffc52fd4bc0b3dec2)
- [modem_cellular_vendor_config::unsol_matches](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md#affae7b69107c6f63f59bb6c64e844cdb)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P005_ppp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_net_stats.h_源码浏览.md)
