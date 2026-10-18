---
id: learning.zephyr-docs.api-source-supplement-reference.page-20
title: uuid.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_uuid.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)。

## 20.1\_原始可见代码（Source Code）

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
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="foldopen00118"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="foldopen00139"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="foldopen00195"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00248"></a>
<a id="foldopen00252"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00257"></a>
<a id="foldopen00261"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00266"></a>
<a id="foldopen00270"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00275"></a>
<a id="foldopen00279"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00284"></a>
<a id="foldopen00288"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00293"></a>
<a id="foldopen00297"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00302"></a>
<a id="foldopen00306"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00311"></a>
<a id="foldopen00315"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00320"></a>
<a id="foldopen00324"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00329"></a>
<a id="foldopen00333"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00338"></a>
<a id="foldopen00342"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00347"></a>
<a id="foldopen00351"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00356"></a>
<a id="foldopen00360"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00365"></a>
<a id="foldopen00369"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00374"></a>
<a id="foldopen00378"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00383"></a>
<a id="foldopen00387"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00392"></a>
<a id="foldopen00396"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00401"></a>
<a id="foldopen00405"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00410"></a>
<a id="foldopen00414"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00419"></a>
<a id="foldopen00423"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00428"></a>
<a id="foldopen00432"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00437"></a>
<a id="foldopen00441"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00446"></a>
<a id="foldopen00450"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00455"></a>
<a id="foldopen00459"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00464"></a>
<a id="foldopen00468"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00473"></a>
<a id="foldopen00477"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00482"></a>
<a id="foldopen00486"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00491"></a>
<a id="foldopen00495"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00500"></a>
<a id="foldopen00504"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00509"></a>
<a id="foldopen00513"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00518"></a>
<a id="foldopen00522"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00527"></a>
<a id="foldopen00531"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00536"></a>
<a id="foldopen00540"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00545"></a>
<a id="foldopen00549"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00554"></a>
<a id="foldopen00558"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00563"></a>
<a id="foldopen00567"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00572"></a>
<a id="foldopen00576"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00581"></a>
<a id="foldopen00585"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00590"></a>
<a id="foldopen00594"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00599"></a>
<a id="foldopen00603"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00608"></a>
<a id="l00612"></a>
<a id="foldopen00616"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00621"></a>
<a id="foldopen00625"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00630"></a>
<a id="foldopen00634"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00639"></a>
<a id="foldopen00643"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00648"></a>
<a id="foldopen00652"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00657"></a>
<a id="foldopen00661"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00666"></a>
<a id="foldopen00670"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00675"></a>
<a id="foldopen00679"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00684"></a>
<a id="foldopen00688"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00693"></a>
<a id="foldopen00697"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00702"></a>
<a id="foldopen00706"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00711"></a>
<a id="foldopen00715"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00720"></a>
<a id="foldopen00724"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00729"></a>
<a id="foldopen00733"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00738"></a>
<a id="foldopen00742"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00747"></a>
<a id="foldopen00751"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00756"></a>
<a id="foldopen00760"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00765"></a>
<a id="foldopen00769"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00774"></a>
<a id="foldopen00778"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00783"></a>
<a id="foldopen00787"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00792"></a>
<a id="foldopen00796"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00801"></a>
<a id="foldopen00805"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00810"></a>
<a id="foldopen00814"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00819"></a>
<a id="foldopen00823"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00828"></a>
<a id="foldopen00832"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00837"></a>
<a id="foldopen00841"></a>
<a id="l00841"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00846"></a>
<a id="foldopen00850"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00852"></a>
<a id="l00855"></a>
<a id="foldopen00859"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="l00864"></a>
<a id="foldopen00868"></a>
<a id="l00868"></a>
<a id="l00869"></a>
<a id="l00870"></a>
<a id="l00873"></a>
<a id="foldopen00877"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00879"></a>
<a id="l00882"></a>
<a id="foldopen00886"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00888"></a>
<a id="l00891"></a>
<a id="foldopen00895"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00900"></a>
<a id="foldopen00904"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00909"></a>
<a id="foldopen00913"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00918"></a>
<a id="foldopen00922"></a>
<a id="l00922"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00927"></a>
<a id="foldopen00931"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="l00933"></a>
<a id="l00936"></a>
<a id="foldopen00940"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00945"></a>
<a id="foldopen00949"></a>
<a id="l00949"></a>
<a id="l00950"></a>
<a id="l00951"></a>
<a id="l00954"></a>
<a id="foldopen00958"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00963"></a>
<a id="foldopen00967"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="l00972"></a>
<a id="foldopen00976"></a>
<a id="l00976"></a>
<a id="l00977"></a>
<a id="l00978"></a>
<a id="l00981"></a>
<a id="foldopen00985"></a>
<a id="l00985"></a>
<a id="l00986"></a>
<a id="l00987"></a>
<a id="l00990"></a>
<a id="foldopen00994"></a>
<a id="l00994"></a>
<a id="l00995"></a>
<a id="l00996"></a>
<a id="l00999"></a>
<a id="foldopen01003"></a>
<a id="l01003"></a>
<a id="l01004"></a>
<a id="l01005"></a>
<a id="l01008"></a>
<a id="foldopen01012"></a>
<a id="l01012"></a>
<a id="l01013"></a>
<a id="l01014"></a>
<a id="l01017"></a>
<a id="foldopen01021"></a>
<a id="l01021"></a>
<a id="l01022"></a>
<a id="l01023"></a>
<a id="l01026"></a>
<a id="foldopen01030"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="l01032"></a>
<a id="l01035"></a>
<a id="foldopen01039"></a>
<a id="l01039"></a>
<a id="l01040"></a>
<a id="l01041"></a>
<a id="l01044"></a>
<a id="foldopen01048"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01054"></a>
<a id="foldopen01058"></a>
<a id="l01058"></a>
<a id="l01059"></a>
<a id="l01060"></a>
<a id="l01063"></a>
<a id="foldopen01067"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="l01072"></a>
<a id="foldopen01076"></a>
<a id="l01076"></a>
<a id="l01077"></a>
<a id="l01078"></a>
<a id="l01081"></a>
<a id="foldopen01085"></a>
<a id="l01085"></a>
<a id="l01086"></a>
<a id="l01087"></a>
<a id="l01090"></a>
<a id="foldopen01094"></a>
<a id="l01094"></a>
<a id="l01095"></a>
<a id="l01096"></a>
<a id="l01099"></a>
<a id="foldopen01103"></a>
<a id="l01103"></a>
<a id="l01104"></a>
<a id="l01105"></a>
<a id="l01108"></a>
<a id="foldopen01112"></a>
<a id="l01112"></a>
<a id="l01113"></a>
<a id="l01114"></a>
<a id="l01117"></a>
<a id="foldopen01121"></a>
<a id="l01121"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01126"></a>
<a id="foldopen01130"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01132"></a>
<a id="l01135"></a>
<a id="foldopen01139"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01141"></a>
<a id="l01144"></a>
<a id="foldopen01148"></a>
<a id="l01148"></a>
<a id="l01149"></a>
<a id="l01150"></a>
<a id="l01153"></a>
<a id="foldopen01157"></a>
<a id="l01157"></a>
<a id="l01158"></a>
<a id="l01159"></a>
<a id="l01162"></a>
<a id="foldopen01166"></a>
<a id="l01166"></a>
<a id="l01167"></a>
<a id="l01168"></a>
<a id="l01171"></a>
<a id="foldopen01175"></a>
<a id="l01175"></a>
<a id="l01176"></a>
<a id="l01177"></a>
<a id="l01180"></a>
<a id="foldopen01184"></a>
<a id="l01184"></a>
<a id="l01185"></a>
<a id="l01186"></a>
<a id="l01189"></a>
<a id="foldopen01193"></a>
<a id="l01193"></a>
<a id="l01194"></a>
<a id="l01195"></a>
<a id="l01198"></a>
<a id="foldopen01202"></a>
<a id="l01202"></a>
<a id="l01203"></a>
<a id="l01204"></a>
<a id="l01207"></a>
<a id="foldopen01211"></a>
<a id="l01211"></a>
<a id="l01212"></a>
<a id="l01213"></a>
<a id="l01216"></a>
<a id="foldopen01220"></a>
<a id="l01220"></a>
<a id="l01221"></a>
<a id="l01222"></a>
<a id="l01225"></a>
<a id="foldopen01229"></a>
<a id="l01229"></a>
<a id="l01230"></a>
<a id="l01231"></a>
<a id="l01234"></a>
<a id="foldopen01238"></a>
<a id="l01238"></a>
<a id="l01239"></a>
<a id="l01240"></a>
<a id="l01243"></a>
<a id="foldopen01247"></a>
<a id="l01247"></a>
<a id="l01248"></a>
<a id="l01249"></a>
<a id="l01252"></a>
<a id="foldopen01256"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01258"></a>
<a id="l01261"></a>
<a id="foldopen01265"></a>
<a id="l01265"></a>
<a id="l01266"></a>
<a id="l01267"></a>
<a id="l01270"></a>
<a id="foldopen01274"></a>
<a id="l01274"></a>
<a id="l01275"></a>
<a id="l01276"></a>
<a id="l01279"></a>
<a id="foldopen01283"></a>
<a id="l01283"></a>
<a id="l01284"></a>
<a id="l01285"></a>
<a id="l01288"></a>
<a id="foldopen01292"></a>
<a id="l01292"></a>
<a id="l01293"></a>
<a id="l01294"></a>
<a id="l01297"></a>
<a id="foldopen01301"></a>
<a id="l01301"></a>
<a id="l01302"></a>
<a id="l01303"></a>
<a id="l01306"></a>
<a id="foldopen01310"></a>
<a id="l01310"></a>
<a id="l01311"></a>
<a id="l01312"></a>
<a id="l01315"></a>
<a id="foldopen01319"></a>
<a id="l01319"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="l01324"></a>
<a id="foldopen01328"></a>
<a id="l01328"></a>
<a id="l01329"></a>
<a id="l01330"></a>
<a id="l01333"></a>
<a id="foldopen01337"></a>
<a id="l01337"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="l01342"></a>
<a id="foldopen01346"></a>
<a id="l01346"></a>
<a id="l01347"></a>
<a id="l01348"></a>
<a id="l01351"></a>
<a id="foldopen01355"></a>
<a id="l01355"></a>
<a id="l01356"></a>
<a id="l01357"></a>
<a id="l01360"></a>
<a id="foldopen01364"></a>
<a id="l01364"></a>
<a id="l01365"></a>
<a id="l01366"></a>
<a id="l01369"></a>
<a id="foldopen01373"></a>
<a id="l01373"></a>
<a id="l01374"></a>
<a id="l01375"></a>
<a id="l01378"></a>
<a id="foldopen01382"></a>
<a id="l01382"></a>
<a id="l01383"></a>
<a id="l01384"></a>
<a id="l01387"></a>
<a id="foldopen01391"></a>
<a id="l01391"></a>
<a id="l01392"></a>
<a id="l01393"></a>
<a id="l01396"></a>
<a id="foldopen01400"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01402"></a>
<a id="l01405"></a>
<a id="foldopen01409"></a>
<a id="l01409"></a>
<a id="l01410"></a>
<a id="l01411"></a>
<a id="l01414"></a>
<a id="foldopen01418"></a>
<a id="l01418"></a>
<a id="l01419"></a>
<a id="l01420"></a>
<a id="l01423"></a>
<a id="foldopen01427"></a>
<a id="l01427"></a>
<a id="l01428"></a>
<a id="l01429"></a>
<a id="l01432"></a>
<a id="foldopen01436"></a>
<a id="l01436"></a>
<a id="l01437"></a>
<a id="l01438"></a>
<a id="l01441"></a>
<a id="foldopen01445"></a>
<a id="l01445"></a>
<a id="l01446"></a>
<a id="l01447"></a>
<a id="l01450"></a>
<a id="foldopen01454"></a>
<a id="l01454"></a>
<a id="l01455"></a>
<a id="l01456"></a>
<a id="l01459"></a>
<a id="foldopen01463"></a>
<a id="l01463"></a>
<a id="l01464"></a>
<a id="l01465"></a>
<a id="l01468"></a>
<a id="foldopen01472"></a>
<a id="l01472"></a>
<a id="l01473"></a>
<a id="l01474"></a>
<a id="l01477"></a>
<a id="foldopen01481"></a>
<a id="l01481"></a>
<a id="l01482"></a>
<a id="l01483"></a>
<a id="l01486"></a>
<a id="foldopen01490"></a>
<a id="l01490"></a>
<a id="l01491"></a>
<a id="l01492"></a>
<a id="l01495"></a>
<a id="foldopen01499"></a>
<a id="l01499"></a>
<a id="l01500"></a>
<a id="l01501"></a>
<a id="l01504"></a>
<a id="foldopen01508"></a>
<a id="l01508"></a>
<a id="l01509"></a>
<a id="l01510"></a>
<a id="l01513"></a>
<a id="foldopen01517"></a>
<a id="l01517"></a>
<a id="l01518"></a>
<a id="l01519"></a>
<a id="l01522"></a>
<a id="foldopen01526"></a>
<a id="l01526"></a>
<a id="l01527"></a>
<a id="l01528"></a>
<a id="l01531"></a>
<a id="foldopen01535"></a>
<a id="l01535"></a>
<a id="l01536"></a>
<a id="l01537"></a>
<a id="l01540"></a>
<a id="foldopen01544"></a>
<a id="l01544"></a>
<a id="l01545"></a>
<a id="l01546"></a>
<a id="l01549"></a>
<a id="foldopen01553"></a>
<a id="l01553"></a>
<a id="l01554"></a>
<a id="l01555"></a>
<a id="l01558"></a>
<a id="foldopen01562"></a>
<a id="l01562"></a>
<a id="l01563"></a>
<a id="l01564"></a>
<a id="l01567"></a>
<a id="foldopen01571"></a>
<a id="l01571"></a>
<a id="l01572"></a>
<a id="l01573"></a>
<a id="l01576"></a>
<a id="foldopen01580"></a>
<a id="l01580"></a>
<a id="l01581"></a>
<a id="l01582"></a>
<a id="l01585"></a>
<a id="foldopen01589"></a>
<a id="l01589"></a>
<a id="l01590"></a>
<a id="l01591"></a>
<a id="l01594"></a>
<a id="foldopen01598"></a>
<a id="l01598"></a>
<a id="l01599"></a>
<a id="l01600"></a>
<a id="l01603"></a>
<a id="foldopen01607"></a>
<a id="l01607"></a>
<a id="l01608"></a>
<a id="l01609"></a>
<a id="l01612"></a>
<a id="foldopen01616"></a>
<a id="l01616"></a>
<a id="l01617"></a>
<a id="l01618"></a>
<a id="l01621"></a>
<a id="foldopen01625"></a>
<a id="l01625"></a>
<a id="l01626"></a>
<a id="l01627"></a>
<a id="l01630"></a>
<a id="foldopen01634"></a>
<a id="l01634"></a>
<a id="l01635"></a>
<a id="l01636"></a>
<a id="l01639"></a>
<a id="foldopen01643"></a>
<a id="l01643"></a>
<a id="l01644"></a>
<a id="l01645"></a>
<a id="l01648"></a>
<a id="foldopen01652"></a>
<a id="l01652"></a>
<a id="l01653"></a>
<a id="l01654"></a>
<a id="l01657"></a>
<a id="foldopen01661"></a>
<a id="l01661"></a>
<a id="l01662"></a>
<a id="l01663"></a>
<a id="l01666"></a>
<a id="foldopen01670"></a>
<a id="l01670"></a>
<a id="l01671"></a>
<a id="l01672"></a>
<a id="l01675"></a>
<a id="foldopen01679"></a>
<a id="l01679"></a>
<a id="l01680"></a>
<a id="l01681"></a>
<a id="l01684"></a>
<a id="foldopen01688"></a>
<a id="l01688"></a>
<a id="l01689"></a>
<a id="l01690"></a>
<a id="l01693"></a>
<a id="foldopen01697"></a>
<a id="l01697"></a>
<a id="l01698"></a>
<a id="l01699"></a>
<a id="l01702"></a>
<a id="foldopen01706"></a>
<a id="l01706"></a>
<a id="l01707"></a>
<a id="l01708"></a>
<a id="l01711"></a>
<a id="foldopen01715"></a>
<a id="l01715"></a>
<a id="l01716"></a>
<a id="l01717"></a>
<a id="l01720"></a>
<a id="foldopen01724"></a>
<a id="l01724"></a>
<a id="l01725"></a>
<a id="l01726"></a>
<a id="l01729"></a>
<a id="foldopen01733"></a>
<a id="l01733"></a>
<a id="l01734"></a>
<a id="l01735"></a>
<a id="l01738"></a>
<a id="foldopen01742"></a>
<a id="l01742"></a>
<a id="l01743"></a>
<a id="l01744"></a>
<a id="l01747"></a>
<a id="foldopen01751"></a>
<a id="l01751"></a>
<a id="l01752"></a>
<a id="l01753"></a>
<a id="l01756"></a>
<a id="foldopen01760"></a>
<a id="l01760"></a>
<a id="l01761"></a>
<a id="l01762"></a>
<a id="l01765"></a>
<a id="foldopen01769"></a>
<a id="l01769"></a>
<a id="l01770"></a>
<a id="l01771"></a>
<a id="l01774"></a>
<a id="foldopen01778"></a>
<a id="l01778"></a>
<a id="l01779"></a>
<a id="l01780"></a>
<a id="l01783"></a>
<a id="foldopen01787"></a>
<a id="l01787"></a>
<a id="l01788"></a>
<a id="l01789"></a>
<a id="l01792"></a>
<a id="foldopen01796"></a>
<a id="l01796"></a>
<a id="l01797"></a>
<a id="l01798"></a>
<a id="l01801"></a>
<a id="foldopen01805"></a>
<a id="l01805"></a>
<a id="l01806"></a>
<a id="l01807"></a>
<a id="l01810"></a>
<a id="foldopen01814"></a>
<a id="l01814"></a>
<a id="l01815"></a>
<a id="l01816"></a>
<a id="l01819"></a>
<a id="foldopen01823"></a>
<a id="l01823"></a>
<a id="l01824"></a>
<a id="l01825"></a>
<a id="l01828"></a>
<a id="foldopen01832"></a>
<a id="l01832"></a>
<a id="l01833"></a>
<a id="l01834"></a>
<a id="l01837"></a>
<a id="foldopen01841"></a>
<a id="l01841"></a>
<a id="l01842"></a>
<a id="l01843"></a>
<a id="l01846"></a>
<a id="foldopen01850"></a>
<a id="l01850"></a>
<a id="l01851"></a>
<a id="l01852"></a>
<a id="l01855"></a>
<a id="foldopen01859"></a>
<a id="l01859"></a>
<a id="l01860"></a>
<a id="l01861"></a>
<a id="l01864"></a>
<a id="foldopen01868"></a>
<a id="l01868"></a>
<a id="l01869"></a>
<a id="l01870"></a>
<a id="l01873"></a>
<a id="foldopen01877"></a>
<a id="l01877"></a>
<a id="l01878"></a>
<a id="l01879"></a>
<a id="l01882"></a>
<a id="foldopen01886"></a>
<a id="l01886"></a>
<a id="l01887"></a>
<a id="l01888"></a>
<a id="l01891"></a>
<a id="foldopen01895"></a>
<a id="l01895"></a>
<a id="l01896"></a>
<a id="l01897"></a>
<a id="l01900"></a>
<a id="foldopen01904"></a>
<a id="l01904"></a>
<a id="l01905"></a>
<a id="l01906"></a>
<a id="l01909"></a>
<a id="foldopen01913"></a>
<a id="l01913"></a>
<a id="l01914"></a>
<a id="l01915"></a>
<a id="l01918"></a>
<a id="foldopen01922"></a>
<a id="l01922"></a>
<a id="l01923"></a>
<a id="l01924"></a>
<a id="l01927"></a>
<a id="foldopen01931"></a>
<a id="l01931"></a>
<a id="l01932"></a>
<a id="l01933"></a>
<a id="l01936"></a>
<a id="foldopen01940"></a>
<a id="l01940"></a>
<a id="l01941"></a>
<a id="l01942"></a>
<a id="l01945"></a>
<a id="foldopen01949"></a>
<a id="l01949"></a>
<a id="l01950"></a>
<a id="l01951"></a>
<a id="l01954"></a>
<a id="foldopen01958"></a>
<a id="l01958"></a>
<a id="l01959"></a>
<a id="l01960"></a>
<a id="l01963"></a>
<a id="foldopen01967"></a>
<a id="l01967"></a>
<a id="l01968"></a>
<a id="l01969"></a>
<a id="l01972"></a>
<a id="foldopen01976"></a>
<a id="l01976"></a>
<a id="l01977"></a>
<a id="l01978"></a>
<a id="l01981"></a>
<a id="foldopen01985"></a>
<a id="l01985"></a>
<a id="l01986"></a>
<a id="l01987"></a>
<a id="l01990"></a>
<a id="foldopen01994"></a>
<a id="l01994"></a>
<a id="l01995"></a>
<a id="l01996"></a>
<a id="l01999"></a>
<a id="foldopen02003"></a>
<a id="l02003"></a>
<a id="l02004"></a>
<a id="l02005"></a>
<a id="l02008"></a>
<a id="foldopen02012"></a>
<a id="l02012"></a>
<a id="l02013"></a>
<a id="l02014"></a>
<a id="l02017"></a>
<a id="foldopen02021"></a>
<a id="l02021"></a>
<a id="l02022"></a>
<a id="l02023"></a>
<a id="l02026"></a>
<a id="foldopen02030"></a>
<a id="l02030"></a>
<a id="l02031"></a>
<a id="l02032"></a>
<a id="l02035"></a>
<a id="foldopen02039"></a>
<a id="l02039"></a>
<a id="l02040"></a>
<a id="l02041"></a>
<a id="l02044"></a>
<a id="foldopen02048"></a>
<a id="l02048"></a>
<a id="l02049"></a>
<a id="l02050"></a>
<a id="l02053"></a>
<a id="foldopen02057"></a>
<a id="l02057"></a>
<a id="l02058"></a>
<a id="l02059"></a>
<a id="l02062"></a>
<a id="foldopen02066"></a>
<a id="l02066"></a>
<a id="l02067"></a>
<a id="l02068"></a>
<a id="l02071"></a>
<a id="foldopen02075"></a>
<a id="l02075"></a>
<a id="l02076"></a>
<a id="l02077"></a>
<a id="l02080"></a>
<a id="foldopen02084"></a>
<a id="l02084"></a>
<a id="l02085"></a>
<a id="l02086"></a>
<a id="l02089"></a>
<a id="foldopen02093"></a>
<a id="l02093"></a>
<a id="l02094"></a>
<a id="l02095"></a>
<a id="l02098"></a>
<a id="foldopen02102"></a>
<a id="l02102"></a>
<a id="l02103"></a>
<a id="l02104"></a>
<a id="l02107"></a>
<a id="foldopen02111"></a>
<a id="l02111"></a>
<a id="l02112"></a>
<a id="l02113"></a>
<a id="l02116"></a>
<a id="foldopen02120"></a>
<a id="l02120"></a>
<a id="l02121"></a>
<a id="l02122"></a>
<a id="l02125"></a>
<a id="foldopen02129"></a>
<a id="l02129"></a>
<a id="l02130"></a>
<a id="l02131"></a>
<a id="l02134"></a>
<a id="foldopen02138"></a>
<a id="l02138"></a>
<a id="l02139"></a>
<a id="l02140"></a>
<a id="l02143"></a>
<a id="foldopen02147"></a>
<a id="l02147"></a>
<a id="l02148"></a>
<a id="l02149"></a>
<a id="l02152"></a>
<a id="foldopen02156"></a>
<a id="l02156"></a>
<a id="l02157"></a>
<a id="l02158"></a>
<a id="l02161"></a>
<a id="foldopen02165"></a>
<a id="l02165"></a>
<a id="l02166"></a>
<a id="l02167"></a>
<a id="l02170"></a>
<a id="foldopen02174"></a>
<a id="l02174"></a>
<a id="l02175"></a>
<a id="l02176"></a>
<a id="l02179"></a>
<a id="foldopen02183"></a>
<a id="l02183"></a>
<a id="l02184"></a>
<a id="l02185"></a>
<a id="l02188"></a>
<a id="foldopen02192"></a>
<a id="l02192"></a>
<a id="l02193"></a>
<a id="l02194"></a>
<a id="l02197"></a>
<a id="foldopen02201"></a>
<a id="l02201"></a>
<a id="l02202"></a>
<a id="l02203"></a>
<a id="l02206"></a>
<a id="foldopen02210"></a>
<a id="l02210"></a>
<a id="l02211"></a>
<a id="l02212"></a>
<a id="l02215"></a>
<a id="foldopen02219"></a>
<a id="l02219"></a>
<a id="l02220"></a>
<a id="l02221"></a>
<a id="l02224"></a>
<a id="foldopen02228"></a>
<a id="l02228"></a>
<a id="l02229"></a>
<a id="l02230"></a>
<a id="l02233"></a>
<a id="foldopen02237"></a>
<a id="l02237"></a>
<a id="l02238"></a>
<a id="l02239"></a>
<a id="l02242"></a>
<a id="foldopen02246"></a>
<a id="l02246"></a>
<a id="l02247"></a>
<a id="l02248"></a>
<a id="l02251"></a>
<a id="foldopen02255"></a>
<a id="l02255"></a>
<a id="l02256"></a>
<a id="l02257"></a>
<a id="l02260"></a>
<a id="foldopen02264"></a>
<a id="l02264"></a>
<a id="l02265"></a>
<a id="l02266"></a>
<a id="l02269"></a>
<a id="foldopen02273"></a>
<a id="l02273"></a>
<a id="l02274"></a>
<a id="l02275"></a>
<a id="l02278"></a>
<a id="foldopen02282"></a>
<a id="l02282"></a>
<a id="l02283"></a>
<a id="l02284"></a>
<a id="l02287"></a>
<a id="foldopen02291"></a>
<a id="l02291"></a>
<a id="l02292"></a>
<a id="l02293"></a>
<a id="l02296"></a>
<a id="foldopen02300"></a>
<a id="l02300"></a>
<a id="l02301"></a>
<a id="l02302"></a>
<a id="l02305"></a>
<a id="foldopen02309"></a>
<a id="l02309"></a>
<a id="l02310"></a>
<a id="l02311"></a>
<a id="l02314"></a>
<a id="foldopen02318"></a>
<a id="l02318"></a>
<a id="l02319"></a>
<a id="l02320"></a>
<a id="l02323"></a>
<a id="foldopen02327"></a>
<a id="l02327"></a>
<a id="l02328"></a>
<a id="l02329"></a>
<a id="l02332"></a>
<a id="foldopen02336"></a>
<a id="l02336"></a>
<a id="l02337"></a>
<a id="l02338"></a>
<a id="l02341"></a>
<a id="foldopen02345"></a>
<a id="l02345"></a>
<a id="l02346"></a>
<a id="l02347"></a>
<a id="l02350"></a>
<a id="foldopen02354"></a>
<a id="l02354"></a>
<a id="l02355"></a>
<a id="l02356"></a>
<a id="l02359"></a>
<a id="foldopen02363"></a>
<a id="l02363"></a>
<a id="l02364"></a>
<a id="l02365"></a>
<a id="l02368"></a>
<a id="foldopen02372"></a>
<a id="l02372"></a>
<a id="l02373"></a>
<a id="l02374"></a>
<a id="l02377"></a>
<a id="foldopen02381"></a>
<a id="l02381"></a>
<a id="l02382"></a>
<a id="l02383"></a>
<a id="l02386"></a>
<a id="foldopen02390"></a>
<a id="l02390"></a>
<a id="l02391"></a>
<a id="l02392"></a>
<a id="l02395"></a>
<a id="foldopen02399"></a>
<a id="l02399"></a>
<a id="l02400"></a>
<a id="l02401"></a>
<a id="l02404"></a>
<a id="foldopen02408"></a>
<a id="l02408"></a>
<a id="l02409"></a>
<a id="l02410"></a>
<a id="l02413"></a>
<a id="foldopen02417"></a>
<a id="l02417"></a>
<a id="l02418"></a>
<a id="l02419"></a>
<a id="l02422"></a>
<a id="foldopen02426"></a>
<a id="l02426"></a>
<a id="l02427"></a>
<a id="l02428"></a>
<a id="l02431"></a>
<a id="foldopen02435"></a>
<a id="l02435"></a>
<a id="l02436"></a>
<a id="l02437"></a>
<a id="l02440"></a>
<a id="foldopen02444"></a>
<a id="l02444"></a>
<a id="l02445"></a>
<a id="l02446"></a>
<a id="l02449"></a>
<a id="foldopen02453"></a>
<a id="l02453"></a>
<a id="l02454"></a>
<a id="l02455"></a>
<a id="l02458"></a>
<a id="foldopen02462"></a>
<a id="l02462"></a>
<a id="l02463"></a>
<a id="l02464"></a>
<a id="l02467"></a>
<a id="foldopen02471"></a>
<a id="l02471"></a>
<a id="l02472"></a>
<a id="l02473"></a>
<a id="l02476"></a>
<a id="foldopen02480"></a>
<a id="l02480"></a>
<a id="l02481"></a>
<a id="l02482"></a>
<a id="l02485"></a>
<a id="foldopen02489"></a>
<a id="l02489"></a>
<a id="l02490"></a>
<a id="l02491"></a>
<a id="l02494"></a>
<a id="foldopen02498"></a>
<a id="l02498"></a>
<a id="l02499"></a>
<a id="l02500"></a>
<a id="l02503"></a>
<a id="foldopen02507"></a>
<a id="l02507"></a>
<a id="l02508"></a>
<a id="l02509"></a>
<a id="l02512"></a>
<a id="foldopen02516"></a>
<a id="l02516"></a>
<a id="l02517"></a>
<a id="l02518"></a>
<a id="l02521"></a>
<a id="foldopen02525"></a>
<a id="l02525"></a>
<a id="l02526"></a>
<a id="l02527"></a>
<a id="l02530"></a>
<a id="foldopen02534"></a>
<a id="l02534"></a>
<a id="l02535"></a>
<a id="l02536"></a>
<a id="l02539"></a>
<a id="foldopen02543"></a>
<a id="l02543"></a>
<a id="l02544"></a>
<a id="l02545"></a>
<a id="l02548"></a>
<a id="foldopen02552"></a>
<a id="l02552"></a>
<a id="l02553"></a>
<a id="l02554"></a>
<a id="l02557"></a>
<a id="foldopen02561"></a>
<a id="l02561"></a>
<a id="l02562"></a>
<a id="l02563"></a>
<a id="l02566"></a>
<a id="foldopen02570"></a>
<a id="l02570"></a>
<a id="l02571"></a>
<a id="l02572"></a>
<a id="l02575"></a>
<a id="foldopen02579"></a>
<a id="l02579"></a>
<a id="l02580"></a>
<a id="l02581"></a>
<a id="l02584"></a>
<a id="foldopen02588"></a>
<a id="l02588"></a>
<a id="l02589"></a>
<a id="l02590"></a>
<a id="l02593"></a>
<a id="foldopen02597"></a>
<a id="l02597"></a>
<a id="l02598"></a>
<a id="l02599"></a>
<a id="l02602"></a>
<a id="foldopen02606"></a>
<a id="l02606"></a>
<a id="l02607"></a>
<a id="l02608"></a>
<a id="l02611"></a>
<a id="foldopen02615"></a>
<a id="l02615"></a>
<a id="l02616"></a>
<a id="l02617"></a>
<a id="l02620"></a>
<a id="foldopen02624"></a>
<a id="l02624"></a>
<a id="l02625"></a>
<a id="l02626"></a>
<a id="l02629"></a>
<a id="foldopen02633"></a>
<a id="l02633"></a>
<a id="l02634"></a>
<a id="l02635"></a>
<a id="l02638"></a>
<a id="foldopen02642"></a>
<a id="l02642"></a>
<a id="l02643"></a>
<a id="l02644"></a>
<a id="l02647"></a>
<a id="foldopen02651"></a>
<a id="l02651"></a>
<a id="l02652"></a>
<a id="l02653"></a>
<a id="l02656"></a>
<a id="foldopen02660"></a>
<a id="l02660"></a>
<a id="l02661"></a>
<a id="l02662"></a>
<a id="l02665"></a>
<a id="foldopen02669"></a>
<a id="l02669"></a>
<a id="l02670"></a>
<a id="l02671"></a>
<a id="l02674"></a>
<a id="foldopen02678"></a>
<a id="l02678"></a>
<a id="l02679"></a>
<a id="l02680"></a>
<a id="l02683"></a>
<a id="foldopen02687"></a>
<a id="l02687"></a>
<a id="l02688"></a>
<a id="l02689"></a>
<a id="l02692"></a>
<a id="foldopen02696"></a>
<a id="l02696"></a>
<a id="l02697"></a>
<a id="l02698"></a>
<a id="l02701"></a>
<a id="foldopen02705"></a>
<a id="l02705"></a>
<a id="l02706"></a>
<a id="l02707"></a>
<a id="l02710"></a>
<a id="foldopen02714"></a>
<a id="l02714"></a>
<a id="l02715"></a>
<a id="l02716"></a>
<a id="l02719"></a>
<a id="foldopen02723"></a>
<a id="l02723"></a>
<a id="l02724"></a>
<a id="l02725"></a>
<a id="l02728"></a>
<a id="foldopen02732"></a>
<a id="l02732"></a>
<a id="l02733"></a>
<a id="l02734"></a>
<a id="l02737"></a>
<a id="foldopen02741"></a>
<a id="l02741"></a>
<a id="l02742"></a>
<a id="l02743"></a>
<a id="l02746"></a>
<a id="foldopen02750"></a>
<a id="l02750"></a>
<a id="l02751"></a>
<a id="l02752"></a>
<a id="l02755"></a>
<a id="foldopen02759"></a>
<a id="l02759"></a>
<a id="l02760"></a>
<a id="l02761"></a>
<a id="l02764"></a>
<a id="foldopen02768"></a>
<a id="l02768"></a>
<a id="l02769"></a>
<a id="l02770"></a>
<a id="l02773"></a>
<a id="foldopen02777"></a>
<a id="l02777"></a>
<a id="l02778"></a>
<a id="l02779"></a>
<a id="l02782"></a>
<a id="foldopen02786"></a>
<a id="l02786"></a>
<a id="l02787"></a>
<a id="l02788"></a>
<a id="l02791"></a>
<a id="foldopen02795"></a>
<a id="l02795"></a>
<a id="l02796"></a>
<a id="l02797"></a>
<a id="l02800"></a>
<a id="foldopen02804"></a>
<a id="l02804"></a>
<a id="l02805"></a>
<a id="l02806"></a>
<a id="l02809"></a>
<a id="foldopen02813"></a>
<a id="l02813"></a>
<a id="l02814"></a>
<a id="l02815"></a>
<a id="l02818"></a>
<a id="foldopen02822"></a>
<a id="l02822"></a>
<a id="l02823"></a>
<a id="l02824"></a>
<a id="l02827"></a>
<a id="foldopen02831"></a>
<a id="l02831"></a>
<a id="l02832"></a>
<a id="l02833"></a>
<a id="l02836"></a>
<a id="foldopen02840"></a>
<a id="l02840"></a>
<a id="l02841"></a>
<a id="l02842"></a>
<a id="l02845"></a>
<a id="foldopen02849"></a>
<a id="l02849"></a>
<a id="l02850"></a>
<a id="l02851"></a>
<a id="l02854"></a>
<a id="foldopen02858"></a>
<a id="l02858"></a>
<a id="l02859"></a>
<a id="l02860"></a>
<a id="l02863"></a>
<a id="foldopen02867"></a>
<a id="l02867"></a>
<a id="l02868"></a>
<a id="l02869"></a>
<a id="l02872"></a>
<a id="foldopen02876"></a>
<a id="l02876"></a>
<a id="l02877"></a>
<a id="l02878"></a>
<a id="l02881"></a>
<a id="foldopen02885"></a>
<a id="l02885"></a>
<a id="l02886"></a>
<a id="l02887"></a>
<a id="l02890"></a>
<a id="foldopen02894"></a>
<a id="l02894"></a>
<a id="l02895"></a>
<a id="l02896"></a>
<a id="l02899"></a>
<a id="foldopen02903"></a>
<a id="l02903"></a>
<a id="l02904"></a>
<a id="l02905"></a>
<a id="l02908"></a>
<a id="foldopen02912"></a>
<a id="l02912"></a>
<a id="l02913"></a>
<a id="l02914"></a>
<a id="l02917"></a>
<a id="foldopen02921"></a>
<a id="l02921"></a>
<a id="l02922"></a>
<a id="l02923"></a>
<a id="l02926"></a>
<a id="foldopen02930"></a>
<a id="l02930"></a>
<a id="l02931"></a>
<a id="l02932"></a>
<a id="l02935"></a>
<a id="foldopen02939"></a>
<a id="l02939"></a>
<a id="l02940"></a>
<a id="l02941"></a>
<a id="l02944"></a>
<a id="foldopen02948"></a>
<a id="l02948"></a>
<a id="l02949"></a>
<a id="l02950"></a>
<a id="l02953"></a>
<a id="foldopen02957"></a>
<a id="l02957"></a>
<a id="l02958"></a>
<a id="l02959"></a>
<a id="l02962"></a>
<a id="foldopen02966"></a>
<a id="l02966"></a>
<a id="l02967"></a>
<a id="l02968"></a>
<a id="l02971"></a>
<a id="foldopen02975"></a>
<a id="l02975"></a>
<a id="l02976"></a>
<a id="l02977"></a>
<a id="l02980"></a>
<a id="foldopen02984"></a>
<a id="l02984"></a>
<a id="l02985"></a>
<a id="l02986"></a>
<a id="l02989"></a>
<a id="foldopen02993"></a>
<a id="l02993"></a>
<a id="l02994"></a>
<a id="l02995"></a>
<a id="l02998"></a>
<a id="foldopen03002"></a>
<a id="l03002"></a>
<a id="l03003"></a>
<a id="l03004"></a>
<a id="l03007"></a>
<a id="foldopen03011"></a>
<a id="l03011"></a>
<a id="l03012"></a>
<a id="l03013"></a>
<a id="l03016"></a>
<a id="foldopen03020"></a>
<a id="l03020"></a>
<a id="l03021"></a>
<a id="l03022"></a>
<a id="l03025"></a>
<a id="foldopen03029"></a>
<a id="l03029"></a>
<a id="l03030"></a>
<a id="l03031"></a>
<a id="l03034"></a>
<a id="foldopen03038"></a>
<a id="l03038"></a>
<a id="l03039"></a>
<a id="l03040"></a>
<a id="l03043"></a>
<a id="foldopen03047"></a>
<a id="l03047"></a>
<a id="l03048"></a>
<a id="l03049"></a>
<a id="l03052"></a>
<a id="foldopen03056"></a>
<a id="l03056"></a>
<a id="l03057"></a>
<a id="l03058"></a>
<a id="l03061"></a>
<a id="foldopen03065"></a>
<a id="l03065"></a>
<a id="l03066"></a>
<a id="l03067"></a>
<a id="l03070"></a>
<a id="foldopen03074"></a>
<a id="l03074"></a>
<a id="l03075"></a>
<a id="l03076"></a>
<a id="l03079"></a>
<a id="foldopen03083"></a>
<a id="l03083"></a>
<a id="l03084"></a>
<a id="l03085"></a>
<a id="l03088"></a>
<a id="foldopen03092"></a>
<a id="l03092"></a>
<a id="l03093"></a>
<a id="l03094"></a>
<a id="l03097"></a>
<a id="foldopen03101"></a>
<a id="l03101"></a>
<a id="l03102"></a>
<a id="l03103"></a>
<a id="l03106"></a>
<a id="foldopen03110"></a>
<a id="l03110"></a>
<a id="l03111"></a>
<a id="l03112"></a>
<a id="l03115"></a>
<a id="foldopen03119"></a>
<a id="l03119"></a>
<a id="l03120"></a>
<a id="l03121"></a>
<a id="l03124"></a>
<a id="foldopen03128"></a>
<a id="l03128"></a>
<a id="l03129"></a>
<a id="l03130"></a>
<a id="l03133"></a>
<a id="foldopen03137"></a>
<a id="l03137"></a>
<a id="l03138"></a>
<a id="l03139"></a>
<a id="l03142"></a>
<a id="foldopen03146"></a>
<a id="l03146"></a>
<a id="l03147"></a>
<a id="l03148"></a>
<a id="l03151"></a>
<a id="foldopen03155"></a>
<a id="l03155"></a>
<a id="l03156"></a>
<a id="l03157"></a>
<a id="l03160"></a>
<a id="foldopen03164"></a>
<a id="l03164"></a>
<a id="l03165"></a>
<a id="l03166"></a>
<a id="l03169"></a>
<a id="foldopen03173"></a>
<a id="l03173"></a>
<a id="l03174"></a>
<a id="l03175"></a>
<a id="l03178"></a>
<a id="foldopen03182"></a>
<a id="l03182"></a>
<a id="l03183"></a>
<a id="l03184"></a>
<a id="l03187"></a>
<a id="foldopen03191"></a>
<a id="l03191"></a>
<a id="l03192"></a>
<a id="l03193"></a>
<a id="l03196"></a>
<a id="foldopen03200"></a>
<a id="l03200"></a>
<a id="l03201"></a>
<a id="l03202"></a>
<a id="l03205"></a>
<a id="foldopen03209"></a>
<a id="l03209"></a>
<a id="l03210"></a>
<a id="l03211"></a>
<a id="l03214"></a>
<a id="foldopen03218"></a>
<a id="l03218"></a>
<a id="l03219"></a>
<a id="l03220"></a>
<a id="l03223"></a>
<a id="foldopen03227"></a>
<a id="l03227"></a>
<a id="l03228"></a>
<a id="l03229"></a>
<a id="l03232"></a>
<a id="foldopen03236"></a>
<a id="l03236"></a>
<a id="l03237"></a>
<a id="l03238"></a>
<a id="l03241"></a>
<a id="foldopen03245"></a>
<a id="l03245"></a>
<a id="l03246"></a>
<a id="l03247"></a>
<a id="l03250"></a>
<a id="foldopen03254"></a>
<a id="l03254"></a>
<a id="l03255"></a>
<a id="l03256"></a>
<a id="l03259"></a>
<a id="foldopen03263"></a>
<a id="l03263"></a>
<a id="l03264"></a>
<a id="l03265"></a>
<a id="l03268"></a>
<a id="foldopen03272"></a>
<a id="l03272"></a>
<a id="l03273"></a>
<a id="l03274"></a>
<a id="l03277"></a>
<a id="foldopen03281"></a>
<a id="l03281"></a>
<a id="l03282"></a>
<a id="l03283"></a>
<a id="l03286"></a>
<a id="foldopen03290"></a>
<a id="l03290"></a>
<a id="l03291"></a>
<a id="l03292"></a>
<a id="l03295"></a>
<a id="foldopen03299"></a>
<a id="l03299"></a>
<a id="l03300"></a>
<a id="l03301"></a>
<a id="l03304"></a>
<a id="foldopen03308"></a>
<a id="l03308"></a>
<a id="l03309"></a>
<a id="l03310"></a>
<a id="l03313"></a>
<a id="foldopen03317"></a>
<a id="l03317"></a>
<a id="l03318"></a>
<a id="l03319"></a>
<a id="l03322"></a>
<a id="foldopen03326"></a>
<a id="l03326"></a>
<a id="l03327"></a>
<a id="l03328"></a>
<a id="l03331"></a>
<a id="foldopen03335"></a>
<a id="l03335"></a>
<a id="l03336"></a>
<a id="l03337"></a>
<a id="l03340"></a>
<a id="foldopen03344"></a>
<a id="l03344"></a>
<a id="l03345"></a>
<a id="l03346"></a>
<a id="l03349"></a>
<a id="foldopen03353"></a>
<a id="l03353"></a>
<a id="l03354"></a>
<a id="l03355"></a>
<a id="l03358"></a>
<a id="foldopen03362"></a>
<a id="l03362"></a>
<a id="l03363"></a>
<a id="l03364"></a>
<a id="l03367"></a>
<a id="foldopen03371"></a>
<a id="l03371"></a>
<a id="l03372"></a>
<a id="l03373"></a>
<a id="l03376"></a>
<a id="foldopen03380"></a>
<a id="l03380"></a>
<a id="l03381"></a>
<a id="l03382"></a>
<a id="l03385"></a>
<a id="foldopen03389"></a>
<a id="l03389"></a>
<a id="l03390"></a>
<a id="l03391"></a>
<a id="l03394"></a>
<a id="foldopen03398"></a>
<a id="l03398"></a>
<a id="l03399"></a>
<a id="l03400"></a>
<a id="l03403"></a>
<a id="foldopen03407"></a>
<a id="l03407"></a>
<a id="l03408"></a>
<a id="l03409"></a>
<a id="l03412"></a>
<a id="foldopen03416"></a>
<a id="l03416"></a>
<a id="l03417"></a>
<a id="l03418"></a>
<a id="l03421"></a>
<a id="foldopen03425"></a>
<a id="l03425"></a>
<a id="l03426"></a>
<a id="l03427"></a>
<a id="l03430"></a>
<a id="foldopen03434"></a>
<a id="l03434"></a>
<a id="l03435"></a>
<a id="l03436"></a>
<a id="l03439"></a>
<a id="foldopen03443"></a>
<a id="l03443"></a>
<a id="l03444"></a>
<a id="l03445"></a>
<a id="l03448"></a>
<a id="foldopen03452"></a>
<a id="l03452"></a>
<a id="l03453"></a>
<a id="l03454"></a>
<a id="l03457"></a>
<a id="foldopen03461"></a>
<a id="l03461"></a>
<a id="l03462"></a>
<a id="l03463"></a>
<a id="l03466"></a>
<a id="foldopen03470"></a>
<a id="l03470"></a>
<a id="l03471"></a>
<a id="l03472"></a>
<a id="l03475"></a>
<a id="foldopen03479"></a>
<a id="l03479"></a>
<a id="l03480"></a>
<a id="l03481"></a>
<a id="l03484"></a>
<a id="foldopen03488"></a>
<a id="l03488"></a>
<a id="l03489"></a>
<a id="l03490"></a>
<a id="l03493"></a>
<a id="foldopen03497"></a>
<a id="l03497"></a>
<a id="l03498"></a>
<a id="l03499"></a>
<a id="l03502"></a>
<a id="foldopen03506"></a>
<a id="l03506"></a>
<a id="l03507"></a>
<a id="l03508"></a>
<a id="l03511"></a>
<a id="foldopen03515"></a>
<a id="l03515"></a>
<a id="l03516"></a>
<a id="l03517"></a>
<a id="l03520"></a>
<a id="foldopen03524"></a>
<a id="l03524"></a>
<a id="l03525"></a>
<a id="l03526"></a>
<a id="l03529"></a>
<a id="foldopen03533"></a>
<a id="l03533"></a>
<a id="l03534"></a>
<a id="l03535"></a>
<a id="l03538"></a>
<a id="foldopen03542"></a>
<a id="l03542"></a>
<a id="l03543"></a>
<a id="l03544"></a>
<a id="l03547"></a>
<a id="foldopen03551"></a>
<a id="l03551"></a>
<a id="l03552"></a>
<a id="l03553"></a>
<a id="l03556"></a>
<a id="foldopen03560"></a>
<a id="l03560"></a>
<a id="l03561"></a>
<a id="l03562"></a>
<a id="l03565"></a>
<a id="foldopen03569"></a>
<a id="l03569"></a>
<a id="l03570"></a>
<a id="l03571"></a>
<a id="l03574"></a>
<a id="foldopen03578"></a>
<a id="l03578"></a>
<a id="l03579"></a>
<a id="l03580"></a>
<a id="l03583"></a>
<a id="foldopen03587"></a>
<a id="l03587"></a>
<a id="l03588"></a>
<a id="l03589"></a>
<a id="l03592"></a>
<a id="foldopen03596"></a>
<a id="l03596"></a>
<a id="l03597"></a>
<a id="l03598"></a>
<a id="l03601"></a>
<a id="foldopen03605"></a>
<a id="l03605"></a>
<a id="l03606"></a>
<a id="l03607"></a>
<a id="l03610"></a>
<a id="foldopen03614"></a>
<a id="l03614"></a>
<a id="l03615"></a>
<a id="l03616"></a>
<a id="l03619"></a>
<a id="foldopen03623"></a>
<a id="l03623"></a>
<a id="l03624"></a>
<a id="l03625"></a>
<a id="l03628"></a>
<a id="foldopen03632"></a>
<a id="l03632"></a>
<a id="l03633"></a>
<a id="l03634"></a>
<a id="l03637"></a>
<a id="foldopen03641"></a>
<a id="l03641"></a>
<a id="l03642"></a>
<a id="l03643"></a>
<a id="l03646"></a>
<a id="foldopen03650"></a>
<a id="l03650"></a>
<a id="l03651"></a>
<a id="l03652"></a>
<a id="l03655"></a>
<a id="foldopen03659"></a>
<a id="l03659"></a>
<a id="l03660"></a>
<a id="l03661"></a>
<a id="l03664"></a>
<a id="foldopen03668"></a>
<a id="l03668"></a>
<a id="l03669"></a>
<a id="l03670"></a>
<a id="l03673"></a>
<a id="foldopen03677"></a>
<a id="l03677"></a>
<a id="l03678"></a>
<a id="l03679"></a>
<a id="l03682"></a>
<a id="foldopen03686"></a>
<a id="l03686"></a>
<a id="l03687"></a>
<a id="l03688"></a>
<a id="l03691"></a>
<a id="foldopen03695"></a>
<a id="l03695"></a>
<a id="l03696"></a>
<a id="l03697"></a>
<a id="l03700"></a>
<a id="foldopen03704"></a>
<a id="l03704"></a>
<a id="l03705"></a>
<a id="l03706"></a>
<a id="l03709"></a>
<a id="foldopen03713"></a>
<a id="l03713"></a>
<a id="l03714"></a>
<a id="l03715"></a>
<a id="l03718"></a>
<a id="foldopen03722"></a>
<a id="l03722"></a>
<a id="l03723"></a>
<a id="l03724"></a>
<a id="l03727"></a>
<a id="foldopen03731"></a>
<a id="l03731"></a>
<a id="l03732"></a>
<a id="l03733"></a>
<a id="l03736"></a>
<a id="foldopen03740"></a>
<a id="l03740"></a>
<a id="l03741"></a>
<a id="l03742"></a>
<a id="l03745"></a>
<a id="foldopen03749"></a>
<a id="l03749"></a>
<a id="l03750"></a>
<a id="l03751"></a>
<a id="l03754"></a>
<a id="foldopen03758"></a>
<a id="l03758"></a>
<a id="l03759"></a>
<a id="l03760"></a>
<a id="l03763"></a>
<a id="foldopen03767"></a>
<a id="l03767"></a>
<a id="l03768"></a>
<a id="l03769"></a>
<a id="l03772"></a>
<a id="foldopen03776"></a>
<a id="l03776"></a>
<a id="l03777"></a>
<a id="l03778"></a>
<a id="l03781"></a>
<a id="foldopen03785"></a>
<a id="l03785"></a>
<a id="l03786"></a>
<a id="l03787"></a>
<a id="l03790"></a>
<a id="foldopen03794"></a>
<a id="l03794"></a>
<a id="l03795"></a>
<a id="l03796"></a>
<a id="l03799"></a>
<a id="foldopen03803"></a>
<a id="l03803"></a>
<a id="l03804"></a>
<a id="l03805"></a>
<a id="l03808"></a>
<a id="foldopen03812"></a>
<a id="l03812"></a>
<a id="l03813"></a>
<a id="l03814"></a>
<a id="l03817"></a>
<a id="foldopen03821"></a>
<a id="l03821"></a>
<a id="l03822"></a>
<a id="l03823"></a>
<a id="l03826"></a>
<a id="foldopen03830"></a>
<a id="l03830"></a>
<a id="l03831"></a>
<a id="l03832"></a>
<a id="l03835"></a>
<a id="foldopen03839"></a>
<a id="l03839"></a>
<a id="l03840"></a>
<a id="l03841"></a>
<a id="l03844"></a>
<a id="foldopen03848"></a>
<a id="l03848"></a>
<a id="l03849"></a>
<a id="l03850"></a>
<a id="l03853"></a>
<a id="foldopen03857"></a>
<a id="l03857"></a>
<a id="l03858"></a>
<a id="l03859"></a>
<a id="l03862"></a>
<a id="foldopen03866"></a>
<a id="l03866"></a>
<a id="l03867"></a>
<a id="l03868"></a>
<a id="l03871"></a>
<a id="foldopen03875"></a>
<a id="l03875"></a>
<a id="l03876"></a>
<a id="l03877"></a>
<a id="l03880"></a>
<a id="foldopen03884"></a>
<a id="l03884"></a>
<a id="l03885"></a>
<a id="l03886"></a>
<a id="l03889"></a>
<a id="foldopen03893"></a>
<a id="l03893"></a>
<a id="l03894"></a>
<a id="l03895"></a>
<a id="l03898"></a>
<a id="foldopen03902"></a>
<a id="l03902"></a>
<a id="l03903"></a>
<a id="l03904"></a>
<a id="l03907"></a>
<a id="foldopen03911"></a>
<a id="l03911"></a>
<a id="l03912"></a>
<a id="l03913"></a>
<a id="l03916"></a>
<a id="foldopen03920"></a>
<a id="l03920"></a>
<a id="l03921"></a>
<a id="l03922"></a>
<a id="l03925"></a>
<a id="foldopen03929"></a>
<a id="l03929"></a>
<a id="l03930"></a>
<a id="l03931"></a>
<a id="l03934"></a>
<a id="foldopen03938"></a>
<a id="l03938"></a>
<a id="l03939"></a>
<a id="l03940"></a>
<a id="l03943"></a>
<a id="foldopen03947"></a>
<a id="l03947"></a>
<a id="l03948"></a>
<a id="l03949"></a>
<a id="l03952"></a>
<a id="foldopen03956"></a>
<a id="l03956"></a>
<a id="l03957"></a>
<a id="l03958"></a>
<a id="l03961"></a>
<a id="foldopen03965"></a>
<a id="l03965"></a>
<a id="l03966"></a>
<a id="l03967"></a>
<a id="l03970"></a>
<a id="foldopen03974"></a>
<a id="l03974"></a>
<a id="l03975"></a>
<a id="l03976"></a>
<a id="l03979"></a>
<a id="foldopen03983"></a>
<a id="l03983"></a>
<a id="l03984"></a>
<a id="l03985"></a>
<a id="l03988"></a>
<a id="foldopen03992"></a>
<a id="l03992"></a>
<a id="l03993"></a>
<a id="l03994"></a>
<a id="l03997"></a>
<a id="foldopen04001"></a>
<a id="l04001"></a>
<a id="l04002"></a>
<a id="l04003"></a>
<a id="l04006"></a>
<a id="foldopen04010"></a>
<a id="l04010"></a>
<a id="l04011"></a>
<a id="l04012"></a>
<a id="l04015"></a>
<a id="foldopen04019"></a>
<a id="l04019"></a>
<a id="l04020"></a>
<a id="l04021"></a>
<a id="l04024"></a>
<a id="foldopen04028"></a>
<a id="l04028"></a>
<a id="l04029"></a>
<a id="l04030"></a>
<a id="l04033"></a>
<a id="foldopen04037"></a>
<a id="l04037"></a>
<a id="l04038"></a>
<a id="l04039"></a>
<a id="l04042"></a>
<a id="foldopen04046"></a>
<a id="l04046"></a>
<a id="l04047"></a>
<a id="l04048"></a>
<a id="l04051"></a>
<a id="foldopen04055"></a>
<a id="l04055"></a>
<a id="l04056"></a>
<a id="l04057"></a>
<a id="l04060"></a>
<a id="foldopen04064"></a>
<a id="l04064"></a>
<a id="l04065"></a>
<a id="l04066"></a>
<a id="l04069"></a>
<a id="foldopen04073"></a>
<a id="l04073"></a>
<a id="l04074"></a>
<a id="l04075"></a>
<a id="l04078"></a>
<a id="foldopen04082"></a>
<a id="l04082"></a>
<a id="l04083"></a>
<a id="l04084"></a>
<a id="l04087"></a>
<a id="foldopen04091"></a>
<a id="l04091"></a>
<a id="l04092"></a>
<a id="l04093"></a>
<a id="l04096"></a>
<a id="foldopen04100"></a>
<a id="l04100"></a>
<a id="l04101"></a>
<a id="l04102"></a>
<a id="l04105"></a>
<a id="foldopen04109"></a>
<a id="l04109"></a>
<a id="l04110"></a>
<a id="l04111"></a>
<a id="l04114"></a>
<a id="foldopen04118"></a>
<a id="l04118"></a>
<a id="l04119"></a>
<a id="l04120"></a>
<a id="l04123"></a>
<a id="foldopen04127"></a>
<a id="l04127"></a>
<a id="l04128"></a>
<a id="l04129"></a>
<a id="l04132"></a>
<a id="foldopen04136"></a>
<a id="l04136"></a>
<a id="l04137"></a>
<a id="l04138"></a>
<a id="l04141"></a>
<a id="foldopen04145"></a>
<a id="l04145"></a>
<a id="l04146"></a>
<a id="l04147"></a>
<a id="l04150"></a>
<a id="l04154"></a>
<a id="l04158"></a>
<a id="foldopen04162"></a>
<a id="l04162"></a>
<a id="l04163"></a>
<a id="l04164"></a>
<a id="l04167"></a>
<a id="foldopen04171"></a>
<a id="l04171"></a>
<a id="l04172"></a>
<a id="l04173"></a>
<a id="l04176"></a>
<a id="foldopen04180"></a>
<a id="l04180"></a>
<a id="l04181"></a>
<a id="l04182"></a>
<a id="l04185"></a>
<a id="foldopen04189"></a>
<a id="l04189"></a>
<a id="l04190"></a>
<a id="l04191"></a>
<a id="l04194"></a>
<a id="foldopen04198"></a>
<a id="l04198"></a>
<a id="l04199"></a>
<a id="l04200"></a>
<a id="l04203"></a>
<a id="foldopen04207"></a>
<a id="l04207"></a>
<a id="l04208"></a>
<a id="l04209"></a>
<a id="l04212"></a>
<a id="foldopen04216"></a>
<a id="l04216"></a>
<a id="l04217"></a>
<a id="l04218"></a>
<a id="l04221"></a>
<a id="foldopen04225"></a>
<a id="l04225"></a>
<a id="l04226"></a>
<a id="l04227"></a>
<a id="l04230"></a>
<a id="foldopen04234"></a>
<a id="l04234"></a>
<a id="l04235"></a>
<a id="l04236"></a>
<a id="l04239"></a>
<a id="foldopen04243"></a>
<a id="l04243"></a>
<a id="l04244"></a>
<a id="l04245"></a>
<a id="l04248"></a>
<a id="foldopen04252"></a>
<a id="l04252"></a>
<a id="l04253"></a>
<a id="l04254"></a>
<a id="l04257"></a>
<a id="foldopen04261"></a>
<a id="l04261"></a>
<a id="l04262"></a>
<a id="l04263"></a>
<a id="l04266"></a>
<a id="foldopen04270"></a>
<a id="l04270"></a>
<a id="l04271"></a>
<a id="l04272"></a>
<a id="l04275"></a>
<a id="foldopen04279"></a>
<a id="l04279"></a>
<a id="l04280"></a>
<a id="l04281"></a>
<a id="l04284"></a>
<a id="foldopen04288"></a>
<a id="l04288"></a>
<a id="l04289"></a>
<a id="l04290"></a>
<a id="l04293"></a>
<a id="foldopen04297"></a>
<a id="l04297"></a>
<a id="l04298"></a>
<a id="l04299"></a>
<a id="l04302"></a>
<a id="foldopen04306"></a>
<a id="l04306"></a>
<a id="l04307"></a>
<a id="l04308"></a>
<a id="l04311"></a>
<a id="foldopen04315"></a>
<a id="l04315"></a>
<a id="l04316"></a>
<a id="l04317"></a>
<a id="l04320"></a>
<a id="foldopen04324"></a>
<a id="l04324"></a>
<a id="l04325"></a>
<a id="l04326"></a>
<a id="l04329"></a>
<a id="foldopen04333"></a>
<a id="l04333"></a>
<a id="l04334"></a>
<a id="l04335"></a>
<a id="l04338"></a>
<a id="foldopen04342"></a>
<a id="l04342"></a>
<a id="l04343"></a>
<a id="l04344"></a>
<a id="l04347"></a>
<a id="foldopen04351"></a>
<a id="l04351"></a>
<a id="l04352"></a>
<a id="l04353"></a>
<a id="l04356"></a>
<a id="foldopen04360"></a>
<a id="l04360"></a>
<a id="l04361"></a>
<a id="l04362"></a>
<a id="l04365"></a>
<a id="foldopen04369"></a>
<a id="l04369"></a>
<a id="l04370"></a>
<a id="l04371"></a>
<a id="l04374"></a>
<a id="foldopen04378"></a>
<a id="l04378"></a>
<a id="l04379"></a>
<a id="l04380"></a>
<a id="l04383"></a>
<a id="foldopen04387"></a>
<a id="l04387"></a>
<a id="l04388"></a>
<a id="l04389"></a>
<a id="l04392"></a>
<a id="foldopen04396"></a>
<a id="l04396"></a>
<a id="l04397"></a>
<a id="l04398"></a>
<a id="l04401"></a>
<a id="foldopen04405"></a>
<a id="l04405"></a>
<a id="l04406"></a>
<a id="l04407"></a>
<a id="l04410"></a>
<a id="foldopen04414"></a>
<a id="l04414"></a>
<a id="l04415"></a>
<a id="l04416"></a>
<a id="l04419"></a>
<a id="foldopen04423"></a>
<a id="l04423"></a>
<a id="l04424"></a>
<a id="l04425"></a>
<a id="l04428"></a>
<a id="foldopen04432"></a>
<a id="l04432"></a>
<a id="l04433"></a>
<a id="l04434"></a>
<a id="l04437"></a>
<a id="foldopen04441"></a>
<a id="l04441"></a>
<a id="l04442"></a>
<a id="l04443"></a>
<a id="l04446"></a>
<a id="foldopen04450"></a>
<a id="l04450"></a>
<a id="l04451"></a>
<a id="l04452"></a>
<a id="l04455"></a>
<a id="foldopen04459"></a>
<a id="l04459"></a>
<a id="l04460"></a>
<a id="l04461"></a>
<a id="l04464"></a>
<a id="foldopen04468"></a>
<a id="l04468"></a>
<a id="l04469"></a>
<a id="l04470"></a>
<a id="l04474"></a>
<a id="foldopen04478"></a>
<a id="l04478"></a>
<a id="l04479"></a>
<a id="l04480"></a>
<a id="l04483"></a>
<a id="foldopen04487"></a>
<a id="l04487"></a>
<a id="l04488"></a>
<a id="l04489"></a>
<a id="l04492"></a>
<a id="foldopen04496"></a>
<a id="l04496"></a>
<a id="l04497"></a>
<a id="l04498"></a>
<a id="l04501"></a>
<a id="foldopen04505"></a>
<a id="l04505"></a>
<a id="l04506"></a>
<a id="l04507"></a>
<a id="l04510"></a>
<a id="foldopen04514"></a>
<a id="l04514"></a>
<a id="l04515"></a>
<a id="l04516"></a>
<a id="l04519"></a>
<a id="foldopen04523"></a>
<a id="l04523"></a>
<a id="l04524"></a>
<a id="l04525"></a>
<a id="l04528"></a>
<a id="foldopen04532"></a>
<a id="l04532"></a>
<a id="l04533"></a>
<a id="l04534"></a>
<a id="l04537"></a>
<a id="foldopen04541"></a>
<a id="l04541"></a>
<a id="l04542"></a>
<a id="l04543"></a>
<a id="l04546"></a>
<a id="foldopen04550"></a>
<a id="l04550"></a>
<a id="l04551"></a>
<a id="l04552"></a>
<a id="l04555"></a>
<a id="foldopen04559"></a>
<a id="l04559"></a>
<a id="l04560"></a>
<a id="l04561"></a>
<a id="l04564"></a>
<a id="foldopen04568"></a>
<a id="l04568"></a>
<a id="l04569"></a>
<a id="l04570"></a>
<a id="l04573"></a>
<a id="foldopen04577"></a>
<a id="l04577"></a>
<a id="l04578"></a>
<a id="l04579"></a>
<a id="l04582"></a>
<a id="foldopen04586"></a>
<a id="l04586"></a>
<a id="l04587"></a>
<a id="l04588"></a>
<a id="l04591"></a>
<a id="foldopen04595"></a>
<a id="l04595"></a>
<a id="l04596"></a>
<a id="l04597"></a>
<a id="l04600"></a>
<a id="foldopen04604"></a>
<a id="l04604"></a>
<a id="l04605"></a>
<a id="l04606"></a>
<a id="l04609"></a>
<a id="foldopen04613"></a>
<a id="l04613"></a>
<a id="l04614"></a>
<a id="l04615"></a>
<a id="l04618"></a>
<a id="foldopen04622"></a>
<a id="l04622"></a>
<a id="l04623"></a>
<a id="l04624"></a>
<a id="l04627"></a>
<a id="foldopen04631"></a>
<a id="l04631"></a>
<a id="l04632"></a>
<a id="l04633"></a>
<a id="l04636"></a>
<a id="foldopen04640"></a>
<a id="l04640"></a>
<a id="l04641"></a>
<a id="l04642"></a>
<a id="l04645"></a>
<a id="foldopen04649"></a>
<a id="l04649"></a>
<a id="l04650"></a>
<a id="l04651"></a>
<a id="l04654"></a>
<a id="foldopen04658"></a>
<a id="l04658"></a>
<a id="l04659"></a>
<a id="l04660"></a>
<a id="l04663"></a>
<a id="foldopen04667"></a>
<a id="l04667"></a>
<a id="l04668"></a>
<a id="l04669"></a>
<a id="l04672"></a>
<a id="foldopen04676"></a>
<a id="l04676"></a>
<a id="l04677"></a>
<a id="l04678"></a>
<a id="l04681"></a>
<a id="foldopen04685"></a>
<a id="l04685"></a>
<a id="l04686"></a>
<a id="l04687"></a>
<a id="l04690"></a>
<a id="foldopen04694"></a>
<a id="l04694"></a>
<a id="l04695"></a>
<a id="l04696"></a>
<a id="l04699"></a>
<a id="foldopen04703"></a>
<a id="l04703"></a>
<a id="l04704"></a>
<a id="l04705"></a>
<a id="l04708"></a>
<a id="foldopen04712"></a>
<a id="l04712"></a>
<a id="l04713"></a>
<a id="l04714"></a>
<a id="l04717"></a>
<a id="foldopen04721"></a>
<a id="l04721"></a>
<a id="l04722"></a>
<a id="l04723"></a>
<a id="l04726"></a>
<a id="foldopen04730"></a>
<a id="l04730"></a>
<a id="l04731"></a>
<a id="l04732"></a>
<a id="l04735"></a>
<a id="foldopen04739"></a>
<a id="l04739"></a>
<a id="l04740"></a>
<a id="l04741"></a>
<a id="l04744"></a>
<a id="foldopen04748"></a>
<a id="l04748"></a>
<a id="l04749"></a>
<a id="l04750"></a>
<a id="l04753"></a>
<a id="foldopen04757"></a>
<a id="l04757"></a>
<a id="l04758"></a>
<a id="l04759"></a>
<a id="l04762"></a>
<a id="foldopen04766"></a>
<a id="l04766"></a>
<a id="l04767"></a>
<a id="l04768"></a>
<a id="l04771"></a>
<a id="foldopen04775"></a>
<a id="l04775"></a>
<a id="l04776"></a>
<a id="l04777"></a>
<a id="l04780"></a>
<a id="foldopen04784"></a>
<a id="l04784"></a>
<a id="l04785"></a>
<a id="l04786"></a>
<a id="l04789"></a>
<a id="foldopen04793"></a>
<a id="l04793"></a>
<a id="l04794"></a>
<a id="l04795"></a>
<a id="l04798"></a>
<a id="foldopen04802"></a>
<a id="l04802"></a>
<a id="l04803"></a>
<a id="l04804"></a>
<a id="l04807"></a>
<a id="foldopen04811"></a>
<a id="l04811"></a>
<a id="l04812"></a>
<a id="l04813"></a>
<a id="l04816"></a>
<a id="foldopen04820"></a>
<a id="l04820"></a>
<a id="l04821"></a>
<a id="l04822"></a>
<a id="l04825"></a>
<a id="foldopen04829"></a>
<a id="l04829"></a>
<a id="l04830"></a>
<a id="l04831"></a>
<a id="l04834"></a>
<a id="foldopen04838"></a>
<a id="l04838"></a>
<a id="l04839"></a>
<a id="l04840"></a>
<a id="l04843"></a>
<a id="foldopen04847"></a>
<a id="l04847"></a>
<a id="l04848"></a>
<a id="l04849"></a>
<a id="l04852"></a>
<a id="foldopen04856"></a>
<a id="l04856"></a>
<a id="l04857"></a>
<a id="l04858"></a>
<a id="l04861"></a>
<a id="foldopen04865"></a>
<a id="l04865"></a>
<a id="l04866"></a>
<a id="l04867"></a>
<a id="l04870"></a>
<a id="foldopen04874"></a>
<a id="l04874"></a>
<a id="l04875"></a>
<a id="l04876"></a>
<a id="l04879"></a>
<a id="foldopen04883"></a>
<a id="l04883"></a>
<a id="l04884"></a>
<a id="l04885"></a>
<a id="l04888"></a>
<a id="foldopen04892"></a>
<a id="l04892"></a>
<a id="l04893"></a>
<a id="l04894"></a>
<a id="l04897"></a>
<a id="foldopen04901"></a>
<a id="l04901"></a>
<a id="l04902"></a>
<a id="l04903"></a>
<a id="l04906"></a>
<a id="foldopen04910"></a>
<a id="l04910"></a>
<a id="l04911"></a>
<a id="l04912"></a>
<a id="l04915"></a>
<a id="foldopen04919"></a>
<a id="l04919"></a>
<a id="l04920"></a>
<a id="l04921"></a>
<a id="l04924"></a>
<a id="foldopen04928"></a>
<a id="l04928"></a>
<a id="l04929"></a>
<a id="l04930"></a>
<a id="l04933"></a>
<a id="foldopen04937"></a>
<a id="l04937"></a>
<a id="l04938"></a>
<a id="l04939"></a>
<a id="l04942"></a>
<a id="foldopen04946"></a>
<a id="l04946"></a>
<a id="l04947"></a>
<a id="l04948"></a>
<a id="l04951"></a>
<a id="foldopen04955"></a>
<a id="l04955"></a>
<a id="l04956"></a>
<a id="l04957"></a>
<a id="l04960"></a>
<a id="foldopen04964"></a>
<a id="l04964"></a>
<a id="l04965"></a>
<a id="l04966"></a>
<a id="l04969"></a>
<a id="foldopen04973"></a>
<a id="l04973"></a>
<a id="l04974"></a>
<a id="l04975"></a>
<a id="l04978"></a>
<a id="foldopen04982"></a>
<a id="l04982"></a>
<a id="l04983"></a>
<a id="l04984"></a>
<a id="l04987"></a>
<a id="foldopen04991"></a>
<a id="l04991"></a>
<a id="l04992"></a>
<a id="l04993"></a>
<a id="l04996"></a>
<a id="foldopen05000"></a>
<a id="l05000"></a>
<a id="l05001"></a>
<a id="l05002"></a>
<a id="l05005"></a>
<a id="foldopen05009"></a>
<a id="l05009"></a>
<a id="l05010"></a>
<a id="l05011"></a>
<a id="l05014"></a>
<a id="foldopen05018"></a>
<a id="l05018"></a>
<a id="l05019"></a>
<a id="l05020"></a>
<a id="l05023"></a>
<a id="foldopen05027"></a>
<a id="l05027"></a>
<a id="l05028"></a>
<a id="l05029"></a>
<a id="l05032"></a>
<a id="foldopen05036"></a>
<a id="l05036"></a>
<a id="l05037"></a>
<a id="l05038"></a>
<a id="l05041"></a>
<a id="foldopen05045"></a>
<a id="l05045"></a>
<a id="l05046"></a>
<a id="l05047"></a>
<a id="l05050"></a>
<a id="foldopen05054"></a>
<a id="l05054"></a>
<a id="l05055"></a>
<a id="l05056"></a>
<a id="l05059"></a>
<a id="foldopen05063"></a>
<a id="l05063"></a>
<a id="l05064"></a>
<a id="l05065"></a>
<a id="l05068"></a>
<a id="foldopen05072"></a>
<a id="l05072"></a>
<a id="l05073"></a>
<a id="l05074"></a>
<a id="l05077"></a>
<a id="foldopen05081"></a>
<a id="l05081"></a>
<a id="l05082"></a>
<a id="l05083"></a>
<a id="l05086"></a>
<a id="foldopen05090"></a>
<a id="l05090"></a>
<a id="l05091"></a>
<a id="l05092"></a>
<a id="l05095"></a>
<a id="foldopen05099"></a>
<a id="l05099"></a>
<a id="l05100"></a>
<a id="l05101"></a>
<a id="l05104"></a>
<a id="foldopen05108"></a>
<a id="l05108"></a>
<a id="l05109"></a>
<a id="l05110"></a>
<a id="l05113"></a>
<a id="foldopen05117"></a>
<a id="l05117"></a>
<a id="l05118"></a>
<a id="l05119"></a>
<a id="l05122"></a>
<a id="foldopen05126"></a>
<a id="l05126"></a>
<a id="l05127"></a>
<a id="l05128"></a>
<a id="l05132"></a>
<a id="foldopen05136"></a>
<a id="l05136"></a>
<a id="l05137"></a>
<a id="l05138"></a>
<a id="l05142"></a>
<a id="l05146"></a>
<a id="l05147"></a>
<a id="l05151"></a>
<a id="l05155"></a>
<a id="l05156"></a>
<a id="l05160"></a>
<a id="l05164"></a>
<a id="l05165"></a>
<a id="l05169"></a>
<a id="l05173"></a>
<a id="l05174"></a>
<a id="l05178"></a>
<a id="l05182"></a>
<a id="l05183"></a>
<a id="l05187"></a>
<a id="l05191"></a>
<a id="l05192"></a>
<a id="l05196"></a>
<a id="l05200"></a>
<a id="l05201"></a>
<a id="l05205"></a>
<a id="l05209"></a>
<a id="l05210"></a>
<a id="l05211"></a>
<a id="l05212"></a>
<a id="l05213"></a>
<a id="l05214"></a>
<a id="l05215"></a>
<a id="l05216"></a>
<a id="l05217"></a>
<a id="l05218"></a>
<a id="l05219"></a>
<a id="l05220"></a>
<a id="l05221"></a>
<a id="l05222"></a>
<a id="l05223"></a>
<a id="l05224"></a>
<a id="l05225"></a>
<a id="l05226"></a>
<a id="l05227"></a>
<a id="l05228"></a>
<a id="l05229"></a>
<a id="l05230"></a>
<a id="l05231"></a>
<a id="l05232"></a>
<a id="l05233"></a>
<a id="l05234"></a>
<a id="l05235"></a>
<a id="l05236"></a>
<a id="l05237"></a>
<a id="l05238"></a>
<a id="l05239"></a>
<a id="l05240"></a>
<a id="l05241"></a>
<a id="l05242"></a>
<a id="l05243"></a>
<a id="l05244"></a>
<a id="l05245"></a>
<a id="l05246"></a>
<a id="l05247"></a>
<a id="l05248"></a>
<a id="l05249"></a>
<a id="l05250"></a>
<a id="l05251"></a>
<a id="l05252"></a>
<a id="l05253"></a>
<a id="l05254"></a>
<a id="l05255"></a>
<a id="l05256"></a>
<a id="l05257"></a>
<a id="l05258"></a>
<a id="l05259"></a>
<a id="l05260"></a>
<a id="l05261"></a>
<a id="l05262"></a>
<a id="l05263"></a>
<a id="l05264"></a>
<a id="l05265"></a>
<a id="l05266"></a>
<a id="l05267"></a>
<a id="l05278"></a>
<a id="l05279"></a>
<a id="l05292"></a>
<a id="l05293"></a>
<a id="l05303"></a>
<a id="l05304"></a>
<a id="l05332"></a>
<a id="l05333"></a>
<a id="l05350"></a>
<a id="l05351"></a>
<a id="l05352"></a>
<a id="l05353"></a>
<a id="l05354"></a>
<a id="l05355"></a>
<a id="l05359"></a>
<a id="l05360"></a>
<a id="abluetooth_2byteorder_8h_html"></a>
<a id="agroup__bt__uuid_html_ga4dec477f7827ece43b91d42d75b1244b"></a>
<a id="agroup__bt__uuid_html_ga72cd2ea0cc6fedded3d1eb8f617f4c07"></a>
<a id="agroup__bt__uuid_html_ga86fdce8e63c0f8208bea6b0f2584eb67"></a>
<a id="agroup__bt__uuid_html_ga9e260584efcc111eb3ee02bf78f01881"></a>
<a id="agroup__bt__uuid_html_gab5ef78dd2263f08de16a0f1e764df657"></a>
<a id="agroup__bt__uuid_html_gafe17513c1f91cb3f3e61648b71620c6b"></a>
<a id="agroup__bt__uuid_html_ggabec48a57ba2d88c9e6006d9996a0fb43a27382df27b8098bf6144021c1b23c4c8"></a>
<a id="agroup__bt__uuid_html_ggabec48a57ba2d88c9e6006d9996a0fb43a786cbb74a1d74c77cb31ff3c4da45517"></a>
<a id="agroup__bt__uuid_html_ggabec48a57ba2d88c9e6006d9996a0fb43a8a5a0c5b6310aff10b182daec0e452ba"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__uuid__128_html"></a>
<a id="astructbt__uuid__128_html_a0918addaa7afaf1eeb864d5ec40bd59a"></a>
<a id="astructbt__uuid__128_html_a3b8fd8a362ed8fd9eabcfa5bffa9eeee"></a>
<a id="astructbt__uuid__16_html"></a>
<a id="astructbt__uuid__16_html_a08f8a5e0eadf1ef2c4c917a5dd3db191"></a>
<a id="astructbt__uuid__16_html_a13ee02ec58cf5fdede249aa8b20a1a9a"></a>
<a id="astructbt__uuid__32_html"></a>
<a id="astructbt__uuid__32_html_a56e991966643c9a1ca689986e57e6bfc"></a>
<a id="astructbt__uuid__32_html_ae37fff06890b200895d559ef42d454e2"></a>
<a id="astructbt__uuid__any_html"></a>
<a id="astructbt__uuid__any_html_a08fab9ce3f49d00dcb7af0cc7a7ad3af"></a>
<a id="astructbt__uuid__any_html_a504aec6e7e793c3de13242aef56fb833"></a>
<a id="astructbt__uuid__any_html_adc9711e614e3839f6af9dd4db315dc66"></a>
<a id="astructbt__uuid__any_html_aea87835ffd5ee2e01bbc6674a0bc83e1"></a>
<a id="astructbt__uuid_html"></a>
<a id="astructbt__uuid_html_abac3a8b54416cbd89ff55f8f82902dcb"></a>
<a id="astructuuid_html"></a>
<a id="asys_2util_8h_html"></a>

```c


/*
 * Copyright (c) 2015-2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_UUID_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_UUID_H_


#include <stddef.h>
#include <stdint.h>

#include <zephyr/sys/util.h>
#include <zephyr/bluetooth/byteorder.h>

#ifdef __cplusplus
extern "C" {
#endif

enum {
        BT_UUID_TYPE_16,
        BT_UUID_TYPE_32,
        BT_UUID_TYPE_128,
};

#define BT_UUID_SIZE_16                  2

#define BT_UUID_SIZE_32                  4

#define BT_UUID_SIZE_128                 16

struct bt_uuid {
        uint8_t type;
};

struct bt_uuid_16 {
        struct bt_uuid uuid;
        uint16_t val;
};

struct bt_uuid_32 {
        struct bt_uuid uuid;
        uint32_t val;
};

struct bt_uuid_128 {
        struct bt_uuid uuid;
        uint8_t val[BT_UUID_SIZE_128];
};

struct bt_uuid_any {
        union {
                struct bt_uuid uuid;
                struct bt_uuid_16 u16;
                struct bt_uuid_32 u32;
                struct bt_uuid_128 u128;
        };
};

#define BT_UUID_INIT_16(value)          \
{                                       \
        .uuid = { BT_UUID_TYPE_16 },    \
        .val = (value),                 \
}

#define BT_UUID_INIT_32(value)          \
{                                       \
        .uuid = { BT_UUID_TYPE_32 },    \
        .val = (value),                 \
}

#define BT_UUID_INIT_128(value...)      \
{                                       \
        .uuid = { BT_UUID_TYPE_128 },   \
        .val = { value },               \
}

#define BT_UUID_DECLARE_16(value) \
        ((const struct bt_uuid *) ((const struct bt_uuid_16[]) {BT_UUID_INIT_16(value)}))

#define BT_UUID_DECLARE_32(value) \
        ((const struct bt_uuid *) ((const struct bt_uuid_32[]) {BT_UUID_INIT_32(value)}))

#define BT_UUID_DECLARE_128(value...) \
        ((const struct bt_uuid *) ((const struct bt_uuid_128[]) {BT_UUID_INIT_128(value)}))

#define BT_UUID_16(__u) CONTAINER_OF(__u, struct bt_uuid_16, uuid)

#define BT_UUID_32(__u) CONTAINER_OF(__u, struct bt_uuid_32, uuid)

#define BT_UUID_128(__u) CONTAINER_OF(__u, struct bt_uuid_128, uuid)

#define BT_UUID_128_ENCODE(w32, w1, w2, w3, w48) \
        BT_BYTES_LIST_LE48(w48),\
        BT_BYTES_LIST_LE16(w3), \
        BT_BYTES_LIST_LE16(w2), \
        BT_BYTES_LIST_LE16(w1), \
        BT_BYTES_LIST_LE32(w32)

#define BT_UUID_16_ENCODE(w16) BT_BYTES_LIST_LE16(w16)

#define BT_UUID_32_ENCODE(w32) BT_BYTES_LIST_LE32(w32)

#define BT_UUID_STR_LEN 37

#define BT_UUID_GAP_VAL 0x1800
#define BT_UUID_GAP \
        BT_UUID_DECLARE_16(BT_UUID_GAP_VAL)

#define BT_UUID_GATT_VAL 0x1801
#define BT_UUID_GATT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_VAL)

#define BT_UUID_IAS_VAL 0x1802
#define BT_UUID_IAS \
        BT_UUID_DECLARE_16(BT_UUID_IAS_VAL)

#define BT_UUID_LLS_VAL 0x1803
#define BT_UUID_LLS \
        BT_UUID_DECLARE_16(BT_UUID_LLS_VAL)

#define BT_UUID_TPS_VAL 0x1804
#define BT_UUID_TPS \
        BT_UUID_DECLARE_16(BT_UUID_TPS_VAL)

#define BT_UUID_CTS_VAL 0x1805
#define BT_UUID_CTS \
        BT_UUID_DECLARE_16(BT_UUID_CTS_VAL)

#define BT_UUID_RTUS_VAL 0x1806
#define BT_UUID_RTUS \
        BT_UUID_DECLARE_16(BT_UUID_RTUS_VAL)

#define BT_UUID_NDSTS_VAL 0x1807
#define BT_UUID_NDSTS \
        BT_UUID_DECLARE_16(BT_UUID_NDSTS_VAL)

#define BT_UUID_GS_VAL 0x1808
#define BT_UUID_GS \
        BT_UUID_DECLARE_16(BT_UUID_GS_VAL)

#define BT_UUID_HTS_VAL 0x1809
#define BT_UUID_HTS \
        BT_UUID_DECLARE_16(BT_UUID_HTS_VAL)

#define BT_UUID_DIS_VAL 0x180a
#define BT_UUID_DIS \
        BT_UUID_DECLARE_16(BT_UUID_DIS_VAL)

#define BT_UUID_NAS_VAL 0x180b
#define BT_UUID_NAS \
        BT_UUID_DECLARE_16(BT_UUID_NAS_VAL)

#define BT_UUID_WDS_VAL 0x180c
#define BT_UUID_WDS \
        BT_UUID_DECLARE_16(BT_UUID_WDS_VAL)

#define BT_UUID_HRS_VAL 0x180d
#define BT_UUID_HRS \
        BT_UUID_DECLARE_16(BT_UUID_HRS_VAL)

#define BT_UUID_PAS_VAL 0x180e
#define BT_UUID_PAS \
        BT_UUID_DECLARE_16(BT_UUID_PAS_VAL)

#define BT_UUID_BAS_VAL 0x180f
#define BT_UUID_BAS \
        BT_UUID_DECLARE_16(BT_UUID_BAS_VAL)

#define BT_UUID_BPS_VAL 0x1810
#define BT_UUID_BPS \
        BT_UUID_DECLARE_16(BT_UUID_BPS_VAL)

#define BT_UUID_ANS_VAL 0x1811
#define BT_UUID_ANS \
        BT_UUID_DECLARE_16(BT_UUID_ANS_VAL)

#define BT_UUID_HIDS_VAL 0x1812
#define BT_UUID_HIDS \
        BT_UUID_DECLARE_16(BT_UUID_HIDS_VAL)

#define BT_UUID_SPS_VAL 0x1813
#define BT_UUID_SPS \
        BT_UUID_DECLARE_16(BT_UUID_SPS_VAL)

#define BT_UUID_RSCS_VAL 0x1814
#define BT_UUID_RSCS \
        BT_UUID_DECLARE_16(BT_UUID_RSCS_VAL)

#define BT_UUID_AIOS_VAL 0x1815
#define BT_UUID_AIOS \
        BT_UUID_DECLARE_16(BT_UUID_AIOS_VAL)

#define BT_UUID_CSC_VAL 0x1816
#define BT_UUID_CSC \
        BT_UUID_DECLARE_16(BT_UUID_CSC_VAL)

#define BT_UUID_CPS_VAL 0x1818
#define BT_UUID_CPS \
        BT_UUID_DECLARE_16(BT_UUID_CPS_VAL)

#define BT_UUID_LNS_VAL 0x1819
#define BT_UUID_LNS \
        BT_UUID_DECLARE_16(BT_UUID_LNS_VAL)

#define BT_UUID_ESS_VAL 0x181a
#define BT_UUID_ESS \
        BT_UUID_DECLARE_16(BT_UUID_ESS_VAL)

#define BT_UUID_BCS_VAL 0x181b
#define BT_UUID_BCS \
        BT_UUID_DECLARE_16(BT_UUID_BCS_VAL)

#define BT_UUID_UDS_VAL 0x181c
#define BT_UUID_UDS \
        BT_UUID_DECLARE_16(BT_UUID_UDS_VAL)

#define BT_UUID_WSS_VAL 0x181d
#define BT_UUID_WSS \
        BT_UUID_DECLARE_16(BT_UUID_WSS_VAL)

#define BT_UUID_BMS_VAL 0x181e
#define BT_UUID_BMS \
        BT_UUID_DECLARE_16(BT_UUID_BMS_VAL)

#define BT_UUID_CGMS_VAL 0x181f
#define BT_UUID_CGMS \
        BT_UUID_DECLARE_16(BT_UUID_CGMS_VAL)

#define BT_UUID_IPSS_VAL 0x1820
#define BT_UUID_IPSS \
        BT_UUID_DECLARE_16(BT_UUID_IPSS_VAL)

#define BT_UUID_IPS_VAL 0x1821
#define BT_UUID_IPS \
        BT_UUID_DECLARE_16(BT_UUID_IPS_VAL)

#define BT_UUID_POS_VAL 0x1822
#define BT_UUID_POS \
        BT_UUID_DECLARE_16(BT_UUID_POS_VAL)

#define BT_UUID_HPS_VAL 0x1823
#define BT_UUID_HPS \
        BT_UUID_DECLARE_16(BT_UUID_HPS_VAL)

#define BT_UUID_TDS_VAL 0x1824
#define BT_UUID_TDS \
        BT_UUID_DECLARE_16(BT_UUID_TDS_VAL)

#define BT_UUID_OTS_VAL 0x1825
#define BT_UUID_OTS \
        BT_UUID_DECLARE_16(BT_UUID_OTS_VAL)

#define BT_UUID_FMS_VAL 0x1826
#define BT_UUID_FMS \
        BT_UUID_DECLARE_16(BT_UUID_FMS_VAL)

#define BT_UUID_MESH_PROV_VAL 0x1827
#define BT_UUID_MESH_PROV \
        BT_UUID_DECLARE_16(BT_UUID_MESH_PROV_VAL)

#define BT_UUID_MESH_PROXY_VAL 0x1828
#define BT_UUID_MESH_PROXY \
        BT_UUID_DECLARE_16(BT_UUID_MESH_PROXY_VAL)

#define BT_UUID_MESH_PROXY_SOLICITATION_VAL 0x1859
#define BT_UUID_RCSRV_VAL 0x1829
#define BT_UUID_RCSRV \
        BT_UUID_DECLARE_16(BT_UUID_RCSRV_VAL)

#define BT_UUID_IDS_VAL 0x183a
#define BT_UUID_IDS \
        BT_UUID_DECLARE_16(BT_UUID_IDS_VAL)

#define BT_UUID_BSS_VAL 0x183b
#define BT_UUID_BSS \
        BT_UUID_DECLARE_16(BT_UUID_BSS_VAL)

#define BT_UUID_ECS_VAL 0x183c
#define BT_UUID_ECS \
        BT_UUID_DECLARE_16(BT_UUID_ECS_VAL)

#define BT_UUID_ACLS_VAL 0x183d
#define BT_UUID_ACLS \
        BT_UUID_DECLARE_16(BT_UUID_ACLS_VAL)

#define BT_UUID_PAMS_VAL 0x183e
#define BT_UUID_PAMS \
        BT_UUID_DECLARE_16(BT_UUID_PAMS_VAL)

#define BT_UUID_ETS_VAL 0x183f
#define BT_UUID_ETS \
        BT_UUID_DECLARE_16(BT_UUID_ETS_VAL)

#define BT_UUID_AICS_VAL 0x1843
#define BT_UUID_AICS \
        BT_UUID_DECLARE_16(BT_UUID_AICS_VAL)

#define BT_UUID_VCS_VAL 0x1844
#define BT_UUID_VCS \
        BT_UUID_DECLARE_16(BT_UUID_VCS_VAL)

#define BT_UUID_VOCS_VAL 0x1845
#define BT_UUID_VOCS \
        BT_UUID_DECLARE_16(BT_UUID_VOCS_VAL)

#define BT_UUID_CSIS_VAL 0x1846
#define BT_UUID_CSIS \
        BT_UUID_DECLARE_16(BT_UUID_CSIS_VAL)

#define BT_UUID_DTS_VAL 0x1847
#define BT_UUID_DTS \
        BT_UUID_DECLARE_16(BT_UUID_DTS_VAL)

#define BT_UUID_MCS_VAL 0x1848
#define BT_UUID_MCS \
        BT_UUID_DECLARE_16(BT_UUID_MCS_VAL)

#define BT_UUID_GMCS_VAL 0x1849
#define BT_UUID_GMCS \
        BT_UUID_DECLARE_16(BT_UUID_GMCS_VAL)

#define BT_UUID_CTES_VAL 0x184a
#define BT_UUID_CTES \
        BT_UUID_DECLARE_16(BT_UUID_CTES_VAL)

#define BT_UUID_TBS_VAL 0x184b
#define BT_UUID_TBS \
        BT_UUID_DECLARE_16(BT_UUID_TBS_VAL)

#define BT_UUID_GTBS_VAL 0x184c
#define BT_UUID_GTBS \
        BT_UUID_DECLARE_16(BT_UUID_GTBS_VAL)

#define BT_UUID_MICS_VAL 0x184d
#define BT_UUID_MICS \
        BT_UUID_DECLARE_16(BT_UUID_MICS_VAL)

#define BT_UUID_ASCS_VAL 0x184e
#define BT_UUID_ASCS \
        BT_UUID_DECLARE_16(BT_UUID_ASCS_VAL)

#define BT_UUID_BASS_VAL 0x184f
#define BT_UUID_BASS \
        BT_UUID_DECLARE_16(BT_UUID_BASS_VAL)

#define BT_UUID_PACS_VAL 0x1850
#define BT_UUID_PACS \
        BT_UUID_DECLARE_16(BT_UUID_PACS_VAL)

#define BT_UUID_BASIC_AUDIO_VAL 0x1851
#define BT_UUID_BASIC_AUDIO \
        BT_UUID_DECLARE_16(BT_UUID_BASIC_AUDIO_VAL)

#define BT_UUID_BROADCAST_AUDIO_VAL 0x1852
#define BT_UUID_BROADCAST_AUDIO \
        BT_UUID_DECLARE_16(BT_UUID_BROADCAST_AUDIO_VAL)

#define BT_UUID_CAS_VAL 0x1853
#define BT_UUID_CAS \
        BT_UUID_DECLARE_16(BT_UUID_CAS_VAL)

#define BT_UUID_HAS_VAL 0x1854
#define BT_UUID_HAS \
        BT_UUID_DECLARE_16(BT_UUID_HAS_VAL)

#define BT_UUID_TMAS_VAL 0x1855
#define BT_UUID_TMAS \
        BT_UUID_DECLARE_16(BT_UUID_TMAS_VAL)

#define BT_UUID_PBA_VAL 0x1856
#define BT_UUID_PBA \
        BT_UUID_DECLARE_16(BT_UUID_PBA_VAL)

#define BT_UUID_GATT_PRIMARY_VAL 0x2800
#define BT_UUID_GATT_PRIMARY \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PRIMARY_VAL)

#define BT_UUID_GATT_SECONDARY_VAL 0x2801
#define BT_UUID_GATT_SECONDARY \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SECONDARY_VAL)

#define BT_UUID_GATT_INCLUDE_VAL 0x2802
#define BT_UUID_GATT_INCLUDE \
        BT_UUID_DECLARE_16(BT_UUID_GATT_INCLUDE_VAL)

#define BT_UUID_GATT_CHRC_VAL 0x2803
#define BT_UUID_GATT_CHRC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CHRC_VAL)

#define BT_UUID_GATT_CEP_VAL 0x2900
#define BT_UUID_GATT_CEP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CEP_VAL)

#define BT_UUID_GATT_CUD_VAL 0x2901
#define BT_UUID_GATT_CUD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CUD_VAL)

#define BT_UUID_GATT_CCC_VAL 0x2902
#define BT_UUID_GATT_CCC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CCC_VAL)

#define BT_UUID_GATT_SCC_VAL 0x2903
#define BT_UUID_GATT_SCC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SCC_VAL)

#define BT_UUID_GATT_CPF_VAL 0x2904
#define BT_UUID_GATT_CPF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CPF_VAL)

#define BT_UUID_GATT_CAF_VAL 0x2905
#define BT_UUID_GATT_CAF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CAF_VAL)

#define BT_UUID_VALID_RANGE_VAL 0x2906
#define BT_UUID_VALID_RANGE \
        BT_UUID_DECLARE_16(BT_UUID_VALID_RANGE_VAL)

#define BT_UUID_HIDS_EXT_REPORT_VAL 0x2907
#define BT_UUID_HIDS_EXT_REPORT \
        BT_UUID_DECLARE_16(BT_UUID_HIDS_EXT_REPORT_VAL)

#define BT_UUID_HIDS_REPORT_REF_VAL 0x2908
#define BT_UUID_HIDS_REPORT_REF \
        BT_UUID_DECLARE_16(BT_UUID_HIDS_REPORT_REF_VAL)

#define BT_UUID_VAL_TRIGGER_SETTING_VAL 0x290a
#define BT_UUID_VAL_TRIGGER_SETTING \
        BT_UUID_DECLARE_16(BT_UUID_VAL_TRIGGER_SETTING_VAL)

#define BT_UUID_ES_CONFIGURATION_VAL 0x290b
#define BT_UUID_ES_CONFIGURATION \
        BT_UUID_DECLARE_16(BT_UUID_ES_CONFIGURATION_VAL)

#define BT_UUID_ES_MEASUREMENT_VAL 0x290c
#define BT_UUID_ES_MEASUREMENT \
        BT_UUID_DECLARE_16(BT_UUID_ES_MEASUREMENT_VAL)

#define BT_UUID_ES_TRIGGER_SETTING_VAL 0x290d
#define BT_UUID_ES_TRIGGER_SETTING \
        BT_UUID_DECLARE_16(BT_UUID_ES_TRIGGER_SETTING_VAL)

#define BT_UUID_TM_TRIGGER_SETTING_VAL 0x290e
#define BT_UUID_TM_TRIGGER_SETTING \
        BT_UUID_DECLARE_16(BT_UUID_TM_TRIGGER_SETTING_VAL)

#define BT_UUID_GAP_DEVICE_NAME_VAL 0x2a00
#define BT_UUID_GAP_DEVICE_NAME \
        BT_UUID_DECLARE_16(BT_UUID_GAP_DEVICE_NAME_VAL)

#define BT_UUID_GAP_APPEARANCE_VAL 0x2a01
#define BT_UUID_GAP_APPEARANCE \
        BT_UUID_DECLARE_16(BT_UUID_GAP_APPEARANCE_VAL)

#define BT_UUID_GAP_PPF_VAL 0x2a02
#define BT_UUID_GAP_PPF \
        BT_UUID_DECLARE_16(BT_UUID_GAP_PPF_VAL)

#define BT_UUID_GAP_RA_VAL 0x2a03
#define BT_UUID_GAP_RA \
        BT_UUID_DECLARE_16(BT_UUID_GAP_RA_VAL)

#define BT_UUID_GAP_PPCP_VAL 0x2a04
#define BT_UUID_GAP_PPCP \
        BT_UUID_DECLARE_16(BT_UUID_GAP_PPCP_VAL)

#define BT_UUID_GATT_SC_VAL 0x2a05
#define BT_UUID_GATT_SC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SC_VAL)

#define BT_UUID_ALERT_LEVEL_VAL  0x2a06
#define BT_UUID_ALERT_LEVEL \
        BT_UUID_DECLARE_16(BT_UUID_ALERT_LEVEL_VAL)

#define BT_UUID_TPS_TX_POWER_LEVEL_VAL 0x2a07
#define BT_UUID_TPS_TX_POWER_LEVEL \
        BT_UUID_DECLARE_16(BT_UUID_TPS_TX_POWER_LEVEL_VAL)

#define BT_UUID_GATT_DT_VAL 0x2a08
#define BT_UUID_GATT_DT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DT_VAL)

#define BT_UUID_GATT_DW_VAL 0x2a09
#define BT_UUID_GATT_DW \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DW_VAL)

#define BT_UUID_GATT_DDT_VAL 0x2a0a
#define BT_UUID_GATT_DDT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DDT_VAL)

#define BT_UUID_GATT_ET256_VAL 0x2a0c
#define BT_UUID_GATT_ET256 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ET256_VAL)

#define BT_UUID_GATT_DST_VAL 0x2a0d
#define BT_UUID_GATT_DST \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DST_VAL)

#define BT_UUID_GATT_TZ_VAL 0x2a0e
#define BT_UUID_GATT_TZ \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TZ_VAL)

#define BT_UUID_GATT_LTI_VAL 0x2a0f
#define BT_UUID_GATT_LTI \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LTI_VAL)

#define BT_UUID_GATT_TDST_VAL 0x2a11
#define BT_UUID_GATT_TDST \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TDST_VAL)

#define BT_UUID_GATT_TA_VAL 0x2a12
#define BT_UUID_GATT_TA \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TA_VAL)

#define BT_UUID_GATT_TS_VAL 0x2a13
#define BT_UUID_GATT_TS \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TS_VAL)

#define BT_UUID_GATT_RTI_VAL 0x2a14
#define BT_UUID_GATT_RTI \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RTI_VAL)

#define BT_UUID_GATT_TUCP_VAL 0x2a16
#define BT_UUID_GATT_TUCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TUCP_VAL)

#define BT_UUID_GATT_TUS_VAL 0x2a17
#define BT_UUID_GATT_TUS \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TUS_VAL)

#define BT_UUID_GATT_GM_VAL 0x2a18
#define BT_UUID_GATT_GM \
        BT_UUID_DECLARE_16(BT_UUID_GATT_GM_VAL)

#define BT_UUID_BAS_BATTERY_LEVEL_VAL 0x2a19
#define BT_UUID_BAS_BATTERY_LEVEL \
        BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_LEVEL_VAL)

#define BT_UUID_BAS_BATTERY_POWER_STATE_VAL 0x2a1a
#define BT_UUID_BAS_BATTERY_POWER_STATE \
        BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_POWER_STATE_VAL)

#define BT_UUID_BAS_BATTERY_LEVEL_STATE_VAL 0x2a1b
#define BT_UUID_BAS_BATTERY_LEVEL_STATE \
        BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_LEVEL_STATE_VAL)

#define BT_UUID_HTS_MEASUREMENT_VAL 0x2a1c
#define BT_UUID_HTS_MEASUREMENT \
        BT_UUID_DECLARE_16(BT_UUID_HTS_MEASUREMENT_VAL)

#define BT_UUID_HTS_TEMP_TYP_VAL 0x2a1d
#define BT_UUID_HTS_TEMP_TYP \
        BT_UUID_DECLARE_16(BT_UUID_HTS_TEMP_TYP_VAL)

#define BT_UUID_HTS_TEMP_INT_VAL 0x2a1e
#define BT_UUID_HTS_TEMP_INT \
        BT_UUID_DECLARE_16(BT_UUID_HTS_TEMP_INT_VAL)

#define BT_UUID_HTS_TEMP_C_VAL 0x2a1f
#define BT_UUID_HTS_TEMP_C \
        BT_UUID_DECLARE_16(BT_UUID_HTS_TEMP_C_VAL)

#define BT_UUID_HTS_TEMP_F_VAL 0x2a20
#define BT_UUID_HTS_TEMP_F \
        BT_UUID_DECLARE_16(BT_UUID_HTS_TEMP_F_VAL)

#define BT_UUID_HTS_INTERVAL_VAL 0x2a21
#define BT_UUID_HTS_INTERVAL \
        BT_UUID_DECLARE_16(BT_UUID_HTS_INTERVAL_VAL)

#define BT_UUID_HIDS_BOOT_KB_IN_REPORT_VAL 0x2a22
#define BT_UUID_HIDS_BOOT_KB_IN_REPORT \
        BT_UUID_DECLARE_16(BT_UUID_HIDS_BOOT_KB_IN_REPORT_VAL)

#define BT_UUID_DIS_SYSTEM_ID_VAL 0x2a23
#define BT_UUID_DIS_SYSTEM_ID \
        BT_UUID_DECLARE_16(BT_UUID_DIS_SYSTEM_ID_VAL)

#define BT_UUID_DIS_MODEL_NUMBER_VAL 0x2a24
#define BT_UUID_DIS_MODEL_NUMBER \
        BT_UUID_DECLARE_16(BT_UUID_DIS_MODEL_NUMBER_VAL)

#define BT_UUID_DIS_SERIAL_NUMBER_VAL 0x2a25
#define BT_UUID_DIS_SERIAL_NUMBER \
        BT_UUID_DECLARE_16(BT_UUID_DIS_SERIAL_NUMBER_VAL)

#define BT_UUID_DIS_FIRMWARE_REVISION_VAL 0x2a26
#define BT_UUID_DIS_FIRMWARE_REVISION \
        BT_UUID_DECLARE_16(BT_UUID_DIS_FIRMWARE_REVISION_VAL)

#define BT_UUID_DIS_HARDWARE_REVISION_VAL 0x2a27
#define BT_UUID_DIS_HARDWARE_REVISION \
        BT_UUID_DECLARE_16(BT_UUID_DIS_HARDWARE_REVISION_VAL)

#define BT_UUID_DIS_SOFTWARE_REVISION_VAL 0x2a28
#define BT_UUID_DIS_SOFTWARE_REVISION \
        BT_UUID_DECLARE_16(BT_UUID_DIS_SOFTWARE_REVISION_VAL)

#define BT_UUID_DIS_MANUFACTURER_NAME_VAL 0x2a29
#define BT_UUID_DIS_MANUFACTURER_NAME \
        BT_UUID_DECLARE_16(BT_UUID_DIS_MANUFACTURER_NAME_VAL)

#define BT_UUID_GATT_IEEE_RCDL_VAL 0x2a2a
#define BT_UUID_GATT_IEEE_RCDL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_IEEE_RCDL_VAL)

#define BT_UUID_CTS_CURRENT_TIME_VAL 0x2a2b
#define BT_UUID_CTS_CURRENT_TIME \
        BT_UUID_DECLARE_16(BT_UUID_CTS_CURRENT_TIME_VAL)

#define BT_UUID_MAGN_DECLINATION_VAL 0x2a2c
#define BT_UUID_MAGN_DECLINATION \
        BT_UUID_DECLARE_16(BT_UUID_MAGN_DECLINATION_VAL)

#define BT_UUID_GATT_LLAT_VAL 0x2a2d
#define BT_UUID_GATT_LLAT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LLAT_VAL)

#define BT_UUID_GATT_LLON_VAL 0x2a2e
#define BT_UUID_GATT_LLON \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LLON_VAL)

#define BT_UUID_GATT_POS_2D_VAL 0x2a2f
#define BT_UUID_GATT_POS_2D \
        BT_UUID_DECLARE_16(BT_UUID_GATT_POS_2D_VAL)

#define BT_UUID_GATT_POS_3D_VAL 0x2a30
#define BT_UUID_GATT_POS_3D \
        BT_UUID_DECLARE_16(BT_UUID_GATT_POS_3D_VAL)

#define BT_UUID_GATT_SR_VAL 0x2a31
#define BT_UUID_GATT_SR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SR_VAL)

#define BT_UUID_HIDS_BOOT_KB_OUT_REPORT_VAL 0x2a32
#define BT_UUID_HIDS_BOOT_KB_OUT_REPORT \
        BT_UUID_DECLARE_16(BT_UUID_HIDS_BOOT_KB_OUT_REPORT_VAL)

#define BT_UUID_HIDS_BOOT_MOUSE_IN_REPORT_VAL 0x2a33
#define BT_UUID_HIDS_BOOT_MOUSE_IN_REPORT \
        BT_UUID_DECLARE_16(BT_UUID_HIDS_BOOT_MOUSE_IN_REPORT_VAL)

#define BT_UUID_GATT_GMC_VAL 0x2a34
#define BT_UUID_GATT_GMC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_GMC_VAL)

#define BT_UUID_GATT_BPM_VAL 0x2a35
#define BT_UUID_GATT_BPM \
        BT_UUID_DECLARE_16(BT_UUID_GATT_BPM_VAL)

#define BT_UUID_GATT_ICP_VAL 0x2a36
#define BT_UUID_GATT_ICP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ICP_VAL)

#define BT_UUID_HRS_MEASUREMENT_VAL 0x2a37
#define BT_UUID_HRS_MEASUREMENT \
        BT_UUID_DECLARE_16(BT_UUID_HRS_MEASUREMENT_VAL)

#define BT_UUID_HRS_BODY_SENSOR_VAL 0x2a38
#define BT_UUID_HRS_BODY_SENSOR \
        BT_UUID_DECLARE_16(BT_UUID_HRS_BODY_SENSOR_VAL)

#define BT_UUID_HRS_CONTROL_POINT_VAL 0x2a39
#define BT_UUID_HRS_CONTROL_POINT \
        BT_UUID_DECLARE_16(BT_UUID_HRS_CONTROL_POINT_VAL)

#define BT_UUID_GATT_REM_VAL 0x2a3a
#define BT_UUID_GATT_REM \
        BT_UUID_DECLARE_16(BT_UUID_GATT_REM_VAL)

#define BT_UUID_GATT_SRVREQ_VAL 0x2a3b
#define BT_UUID_GATT_SRVREQ \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SRVREQ_VAL)

#define BT_UUID_GATT_SC_TEMP_C_VAL 0x2a3c
#define BT_UUID_GATT_SC_TEMP_C \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SC_TEMP_C_VAL)

#define BT_UUID_GATT_STRING_VAL 0x2a3d
#define BT_UUID_GATT_STRING \
        BT_UUID_DECLARE_16(BT_UUID_GATT_STRING_VAL)

#define BT_UUID_GATT_NETA_VAL 0x2a3e
#define BT_UUID_GATT_NETA \
        BT_UUID_DECLARE_16(BT_UUID_GATT_NETA_VAL)

#define BT_UUID_GATT_ALRTS_VAL 0x2a3f
#define BT_UUID_GATT_ALRTS \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ALRTS_VAL)

#define BT_UUID_GATT_RCP_VAL 0x2a40
#define BT_UUID_GATT_RCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RCP_VAL)

#define BT_UUID_GATT_RS_VAL 0x2a41
#define BT_UUID_GATT_RS \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RS_VAL)

#define BT_UUID_GATT_ALRTCID_MASK_VAL 0x2a42
#define BT_UUID_GATT_ALRTCID_MASK \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ALRTCID_MASK_VAL)

#define BT_UUID_GATT_ALRTCID_VAL 0x2a43
#define BT_UUID_GATT_ALRTCID \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ALRTCID_VAL)

#define BT_UUID_GATT_ALRTNCP_VAL 0x2a44
#define BT_UUID_GATT_ALRTNCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ALRTNCP_VAL)

#define BT_UUID_GATT_UALRTS_VAL 0x2a45
#define BT_UUID_GATT_UALRTS \
        BT_UUID_DECLARE_16(BT_UUID_GATT_UALRTS_VAL)

#define BT_UUID_GATT_NALRT_VAL 0x2a46
#define BT_UUID_GATT_NALRT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_NALRT_VAL)

#define BT_UUID_GATT_SNALRTC_VAL 0x2a47
#define BT_UUID_GATT_SNALRTC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SNALRTC_VAL)

#define BT_UUID_GATT_SUALRTC_VAL 0x2a48
#define BT_UUID_GATT_SUALRTC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SUALRTC_VAL)

#define BT_UUID_GATT_BPF_VAL 0x2a49
#define BT_UUID_GATT_BPF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_BPF_VAL)

#define BT_UUID_HIDS_INFO_VAL 0x2a4a
#define BT_UUID_HIDS_INFO \
        BT_UUID_DECLARE_16(BT_UUID_HIDS_INFO_VAL)

#define BT_UUID_HIDS_REPORT_MAP_VAL 0x2a4b
#define BT_UUID_HIDS_REPORT_MAP \
        BT_UUID_DECLARE_16(BT_UUID_HIDS_REPORT_MAP_VAL)

#define BT_UUID_HIDS_CTRL_POINT_VAL 0x2a4c
#define BT_UUID_HIDS_CTRL_POINT \
        BT_UUID_DECLARE_16(BT_UUID_HIDS_CTRL_POINT_VAL)

#define BT_UUID_HIDS_REPORT_VAL 0x2a4d
#define BT_UUID_HIDS_REPORT \
        BT_UUID_DECLARE_16(BT_UUID_HIDS_REPORT_VAL)

#define BT_UUID_HIDS_PROTOCOL_MODE_VAL 0x2a4e
#define BT_UUID_HIDS_PROTOCOL_MODE \
        BT_UUID_DECLARE_16(BT_UUID_HIDS_PROTOCOL_MODE_VAL)

#define BT_UUID_GATT_SIW_VAL 0x2a4f
#define BT_UUID_GATT_SIW \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SIW_VAL)

#define BT_UUID_DIS_PNP_ID_VAL 0x2a50
#define BT_UUID_DIS_PNP_ID \
        BT_UUID_DECLARE_16(BT_UUID_DIS_PNP_ID_VAL)

#define BT_UUID_GATT_GF_VAL 0x2a51
#define BT_UUID_GATT_GF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_GF_VAL)

#define BT_UUID_RECORD_ACCESS_CONTROL_POINT_VAL 0x2a52
#define BT_UUID_RECORD_ACCESS_CONTROL_POINT \
        BT_UUID_DECLARE_16(BT_UUID_RECORD_ACCESS_CONTROL_POINT_VAL)

#define BT_UUID_RSC_MEASUREMENT_VAL 0x2a53
#define BT_UUID_RSC_MEASUREMENT \
        BT_UUID_DECLARE_16(BT_UUID_RSC_MEASUREMENT_VAL)

#define BT_UUID_RSC_FEATURE_VAL 0x2a54
#define BT_UUID_RSC_FEATURE \
        BT_UUID_DECLARE_16(BT_UUID_RSC_FEATURE_VAL)

#define BT_UUID_SC_CONTROL_POINT_VAL 0x2a55
#define BT_UUID_SC_CONTROL_POINT \
        BT_UUID_DECLARE_16(BT_UUID_SC_CONTROL_POINT_VAL)

#define BT_UUID_GATT_DI_VAL 0x2a56
#define BT_UUID_GATT_DI \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DI_VAL)

#define BT_UUID_GATT_DO_VAL 0x2a57
#define BT_UUID_GATT_DO \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DO_VAL)

#define BT_UUID_GATT_AI_VAL 0x2a58
#define BT_UUID_GATT_AI \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AI_VAL)

#define BT_UUID_GATT_AO_VAL 0x2a59
#define BT_UUID_GATT_AO \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AO_VAL)

#define BT_UUID_GATT_AGGR_VAL 0x2a5a
#define BT_UUID_GATT_AGGR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AGGR_VAL)

#define BT_UUID_CSC_MEASUREMENT_VAL 0x2a5b
#define BT_UUID_CSC_MEASUREMENT \
        BT_UUID_DECLARE_16(BT_UUID_CSC_MEASUREMENT_VAL)

#define BT_UUID_CSC_FEATURE_VAL 0x2a5c
#define BT_UUID_CSC_FEATURE \
        BT_UUID_DECLARE_16(BT_UUID_CSC_FEATURE_VAL)

#define BT_UUID_SENSOR_LOCATION_VAL 0x2a5d
#define BT_UUID_SENSOR_LOCATION \
        BT_UUID_DECLARE_16(BT_UUID_SENSOR_LOCATION_VAL)

#define BT_UUID_GATT_PLX_SCM_VAL 0x2a5e
#define BT_UUID_GATT_PLX_SCM \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PLX_SCM_VAL)

#define BT_UUID_GATT_PLX_CM_VAL 0x2a5f
#define BT_UUID_GATT_PLX_CM \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PLX_CM_VAL)

#define BT_UUID_GATT_PLX_F_VAL 0x2a60
#define BT_UUID_GATT_PLX_F \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PLX_F_VAL)

#define BT_UUID_GATT_POPE_VAL 0x2a61
#define BT_UUID_GATT_POPE \
        BT_UUID_DECLARE_16(BT_UUID_GATT_POPE_VAL)

#define BT_UUID_GATT_POCP_VAL 0x2a62
#define BT_UUID_GATT_POCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_POCP_VAL)

#define BT_UUID_GATT_CPS_CPM_VAL 0x2a63
#define BT_UUID_GATT_CPS_CPM \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CPS_CPM_VAL)

#define BT_UUID_GATT_CPS_CPV_VAL 0x2a64
#define BT_UUID_GATT_CPS_CPV \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CPS_CPV_VAL)

#define BT_UUID_GATT_CPS_CPF_VAL 0x2a65
#define BT_UUID_GATT_CPS_CPF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CPS_CPF_VAL)

#define BT_UUID_GATT_CPS_CPCP_VAL 0x2a66
#define BT_UUID_GATT_CPS_CPCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CPS_CPCP_VAL)

#define BT_UUID_GATT_LOC_SPD_VAL 0x2a67
#define BT_UUID_GATT_LOC_SPD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LOC_SPD_VAL)

#define BT_UUID_GATT_NAV_VAL 0x2a68
#define BT_UUID_GATT_NAV \
        BT_UUID_DECLARE_16(BT_UUID_GATT_NAV_VAL)

#define BT_UUID_GATT_PQ_VAL 0x2a69
#define BT_UUID_GATT_PQ \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PQ_VAL)

#define BT_UUID_GATT_LNF_VAL 0x2a6a
#define BT_UUID_GATT_LNF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LNF_VAL)

#define BT_UUID_GATT_LNCP_VAL 0x2a6b
#define BT_UUID_GATT_LNCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LNCP_VAL)

#define BT_UUID_ELEVATION_VAL 0x2a6c
#define BT_UUID_ELEVATION \
        BT_UUID_DECLARE_16(BT_UUID_ELEVATION_VAL)

#define BT_UUID_PRESSURE_VAL 0x2a6d
#define BT_UUID_PRESSURE \
        BT_UUID_DECLARE_16(BT_UUID_PRESSURE_VAL)

#define BT_UUID_TEMPERATURE_VAL 0x2a6e
#define BT_UUID_TEMPERATURE \
        BT_UUID_DECLARE_16(BT_UUID_TEMPERATURE_VAL)

#define BT_UUID_HUMIDITY_VAL 0x2a6f
#define BT_UUID_HUMIDITY \
        BT_UUID_DECLARE_16(BT_UUID_HUMIDITY_VAL)

#define BT_UUID_TRUE_WIND_SPEED_VAL 0x2a70
#define BT_UUID_TRUE_WIND_SPEED \
        BT_UUID_DECLARE_16(BT_UUID_TRUE_WIND_SPEED_VAL)

#define BT_UUID_TRUE_WIND_DIR_VAL 0x2a71
#define BT_UUID_TRUE_WIND_DIR \
        BT_UUID_DECLARE_16(BT_UUID_TRUE_WIND_DIR_VAL)

#define BT_UUID_APPARENT_WIND_SPEED_VAL 0x2a72
#define BT_UUID_APPARENT_WIND_SPEED \
        BT_UUID_DECLARE_16(BT_UUID_APPARENT_WIND_SPEED_VAL)

#define BT_UUID_APPARENT_WIND_DIR_VAL 0x2a73
#define BT_UUID_APPARENT_WIND_DIR \
        BT_UUID_DECLARE_16(BT_UUID_APPARENT_WIND_DIR_VAL)

#define BT_UUID_GUST_FACTOR_VAL 0x2a74
#define BT_UUID_GUST_FACTOR \
        BT_UUID_DECLARE_16(BT_UUID_GUST_FACTOR_VAL)

#define BT_UUID_POLLEN_CONCENTRATION_VAL 0x2a75
#define BT_UUID_POLLEN_CONCENTRATION \
        BT_UUID_DECLARE_16(BT_UUID_POLLEN_CONCENTRATION_VAL)

#define BT_UUID_UV_INDEX_VAL 0x2a76
#define BT_UUID_UV_INDEX \
        BT_UUID_DECLARE_16(BT_UUID_UV_INDEX_VAL)

#define BT_UUID_IRRADIANCE_VAL 0x2a77
#define BT_UUID_IRRADIANCE \
        BT_UUID_DECLARE_16(BT_UUID_IRRADIANCE_VAL)

#define BT_UUID_RAINFALL_VAL 0x2a78
#define BT_UUID_RAINFALL \
        BT_UUID_DECLARE_16(BT_UUID_RAINFALL_VAL)

#define BT_UUID_WIND_CHILL_VAL 0x2a79
#define BT_UUID_WIND_CHILL \
        BT_UUID_DECLARE_16(BT_UUID_WIND_CHILL_VAL)

#define BT_UUID_HEAT_INDEX_VAL 0x2a7a
#define BT_UUID_HEAT_INDEX \
        BT_UUID_DECLARE_16(BT_UUID_HEAT_INDEX_VAL)

#define BT_UUID_DEW_POINT_VAL 0x2a7b
#define BT_UUID_DEW_POINT \
        BT_UUID_DECLARE_16(BT_UUID_DEW_POINT_VAL)

#define BT_UUID_GATT_TREND_VAL 0x2a7c
#define BT_UUID_GATT_TREND \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TREND_VAL)

#define BT_UUID_DESC_VALUE_CHANGED_VAL 0x2a7d
#define BT_UUID_DESC_VALUE_CHANGED \
        BT_UUID_DECLARE_16(BT_UUID_DESC_VALUE_CHANGED_VAL)

#define BT_UUID_GATT_AEHRLL_VAL 0x2a7e
#define BT_UUID_GATT_AEHRLL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AEHRLL_VAL)

#define BT_UUID_GATT_AETHR_VAL 0x2a7f
#define BT_UUID_GATT_AETHR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AETHR_VAL)

#define BT_UUID_GATT_AGE_VAL 0x2a80
#define BT_UUID_GATT_AGE \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AGE_VAL)

#define BT_UUID_GATT_ANHRLL_VAL 0x2a81
#define BT_UUID_GATT_ANHRLL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ANHRLL_VAL)

#define BT_UUID_GATT_ANHRUL_VAL 0x2a82
#define BT_UUID_GATT_ANHRUL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ANHRUL_VAL)

#define BT_UUID_GATT_ANTHR_VAL 0x2a83
#define BT_UUID_GATT_ANTHR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ANTHR_VAL)

#define BT_UUID_GATT_AEHRUL_VAL 0x2a84
#define BT_UUID_GATT_AEHRUL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AEHRUL_VAL)

#define BT_UUID_GATT_DATE_BIRTH_VAL 0x2a85
#define BT_UUID_GATT_DATE_BIRTH \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DATE_BIRTH_VAL)

#define BT_UUID_GATT_DATE_THRASS_VAL 0x2a86
#define BT_UUID_GATT_DATE_THRASS \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DATE_THRASS_VAL)

#define BT_UUID_GATT_EMAIL_VAL 0x2a87
#define BT_UUID_GATT_EMAIL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_EMAIL_VAL)

#define BT_UUID_GATT_FBHRLL_VAL 0x2a88
#define BT_UUID_GATT_FBHRLL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_FBHRLL_VAL)

#define BT_UUID_GATT_FBHRUL_VAL 0x2a89
#define BT_UUID_GATT_FBHRUL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_FBHRUL_VAL)

#define BT_UUID_GATT_FIRST_NAME_VAL 0x2a8a
#define BT_UUID_GATT_FIRST_NAME \
        BT_UUID_DECLARE_16(BT_UUID_GATT_FIRST_NAME_VAL)

#define BT_UUID_GATT_5ZHRL_VAL 0x2a8b
#define BT_UUID_GATT_5ZHRL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_5ZHRL_VAL)

#define BT_UUID_GATT_GENDER_VAL 0x2a8c
#define BT_UUID_GATT_GENDER \
        BT_UUID_DECLARE_16(BT_UUID_GATT_GENDER_VAL)

#define BT_UUID_GATT_HR_MAX_VAL 0x2a8d
#define BT_UUID_GATT_HR_MAX \
        BT_UUID_DECLARE_16(BT_UUID_GATT_HR_MAX_VAL)

#define BT_UUID_GATT_HEIGHT_VAL 0x2a8e
#define BT_UUID_GATT_HEIGHT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_HEIGHT_VAL)

#define BT_UUID_GATT_HC_VAL 0x2a8f
#define BT_UUID_GATT_HC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_HC_VAL)

#define BT_UUID_GATT_LAST_NAME_VAL 0x2a90
#define BT_UUID_GATT_LAST_NAME \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LAST_NAME_VAL)

#define BT_UUID_GATT_MRHR_VAL 0x2a91
#define BT_UUID_GATT_MRHR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_MRHR_VAL)

#define BT_UUID_GATT_RHR_VAL 0x2a92
#define BT_UUID_GATT_RHR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RHR_VAL)

#define BT_UUID_GATT_AEANTHR_VAL 0x2a93
#define BT_UUID_GATT_AEANTHR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AEANTHR_VAL)

#define BT_UUID_GATT_3ZHRL_VAL 0x2a94
#define BT_UUID_GATT_3ZHRL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_3ZHRL_VAL)

#define BT_UUID_GATT_2ZHRL_VAL 0x2a95
#define BT_UUID_GATT_2ZHRL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_2ZHRL_VAL)

#define BT_UUID_GATT_VO2_MAX_VAL 0x2a96
#define BT_UUID_GATT_VO2_MAX \
        BT_UUID_DECLARE_16(BT_UUID_GATT_VO2_MAX_VAL)

#define BT_UUID_GATT_WC_VAL 0x2a97
#define BT_UUID_GATT_WC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_WC_VAL)

#define BT_UUID_GATT_WEIGHT_VAL 0x2a98
#define BT_UUID_GATT_WEIGHT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_WEIGHT_VAL)

#define BT_UUID_GATT_DBCHINC_VAL 0x2a99
#define BT_UUID_GATT_DBCHINC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DBCHINC_VAL)

#define BT_UUID_GATT_USRIDX_VAL 0x2a9a
#define BT_UUID_GATT_USRIDX \
        BT_UUID_DECLARE_16(BT_UUID_GATT_USRIDX_VAL)

#define BT_UUID_GATT_BCF_VAL 0x2a9b
#define BT_UUID_GATT_BCF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_BCF_VAL)

#define BT_UUID_GATT_BCM_VAL 0x2a9c
#define BT_UUID_GATT_BCM \
        BT_UUID_DECLARE_16(BT_UUID_GATT_BCM_VAL)

#define BT_UUID_GATT_WM_VAL 0x2a9d
#define BT_UUID_GATT_WM \
        BT_UUID_DECLARE_16(BT_UUID_GATT_WM_VAL)

#define BT_UUID_GATT_WSF_VAL 0x2a9e
#define BT_UUID_GATT_WSF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_WSF_VAL)

#define BT_UUID_GATT_USRCP_VAL 0x2a9f
#define BT_UUID_GATT_USRCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_USRCP_VAL)

#define BT_UUID_MAGN_FLUX_DENSITY_2D_VAL 0x2aa0
#define BT_UUID_MAGN_FLUX_DENSITY_2D \
        BT_UUID_DECLARE_16(BT_UUID_MAGN_FLUX_DENSITY_2D_VAL)

#define BT_UUID_MAGN_FLUX_DENSITY_3D_VAL 0x2aa1
#define BT_UUID_MAGN_FLUX_DENSITY_3D \
        BT_UUID_DECLARE_16(BT_UUID_MAGN_FLUX_DENSITY_3D_VAL)

#define BT_UUID_GATT_LANG_VAL 0x2aa2
#define BT_UUID_GATT_LANG \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LANG_VAL)

#define BT_UUID_BAR_PRESSURE_TREND_VAL 0x2aa3
#define BT_UUID_BAR_PRESSURE_TREND \
        BT_UUID_DECLARE_16(BT_UUID_BAR_PRESSURE_TREND_VAL)

#define BT_UUID_BMS_CONTROL_POINT_VAL 0x2aa4
#define BT_UUID_BMS_CONTROL_POINT \
        BT_UUID_DECLARE_16(BT_UUID_BMS_CONTROL_POINT_VAL)

#define BT_UUID_BMS_FEATURE_VAL 0x2aa5
#define BT_UUID_BMS_FEATURE \
        BT_UUID_DECLARE_16(BT_UUID_BMS_FEATURE_VAL)

#define BT_UUID_CENTRAL_ADDR_RES_VAL 0x2aa6
#define BT_UUID_CENTRAL_ADDR_RES \
        BT_UUID_DECLARE_16(BT_UUID_CENTRAL_ADDR_RES_VAL)

#define BT_UUID_CGM_MEASUREMENT_VAL 0x2aa7
#define BT_UUID_CGM_MEASUREMENT \
        BT_UUID_DECLARE_16(BT_UUID_CGM_MEASUREMENT_VAL)

#define BT_UUID_CGM_FEATURE_VAL 0x2aa8
#define BT_UUID_CGM_FEATURE \
        BT_UUID_DECLARE_16(BT_UUID_CGM_FEATURE_VAL)

#define BT_UUID_CGM_STATUS_VAL 0x2aa9
#define BT_UUID_CGM_STATUS \
        BT_UUID_DECLARE_16(BT_UUID_CGM_STATUS_VAL)

#define BT_UUID_CGM_SESSION_START_TIME_VAL 0x2aaa
#define BT_UUID_CGM_SESSION_START_TIME \
        BT_UUID_DECLARE_16(BT_UUID_CGM_SESSION_START_TIME_VAL)

#define BT_UUID_CGM_SESSION_RUN_TIME_VAL 0x2aab
#define BT_UUID_CGM_SESSION_RUN_TIME \
        BT_UUID_DECLARE_16(BT_UUID_CGM_SESSION_RUN_TIME_VAL)

#define BT_UUID_CGM_SPECIFIC_OPS_CONTROL_POINT_VAL 0x2aac
#define BT_UUID_CGM_SPECIFIC_OPS_CONTROL_POINT \
        BT_UUID_DECLARE_16(BT_UUID_CGM_SPECIFIC_OPS_CONTROL_POINT_VAL)

#define BT_UUID_GATT_IPC_VAL 0x2aad
#define BT_UUID_GATT_IPC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_IPC_VAL)

#define BT_UUID_GATT_LAT_VAL 0x2aae
#define BT_UUID_GATT_LAT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LAT_VAL)

#define BT_UUID_GATT_LON_VAL 0x2aaf
#define BT_UUID_GATT_LON \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LON_VAL)

#define BT_UUID_GATT_LNCOORD_VAL 0x2ab0
#define BT_UUID_GATT_LNCOORD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LNCOORD_VAL)

#define BT_UUID_GATT_LECOORD_VAL 0x2ab1
#define BT_UUID_GATT_LECOORD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LECOORD_VAL)

#define BT_UUID_GATT_FN_VAL 0x2ab2
#define BT_UUID_GATT_FN \
        BT_UUID_DECLARE_16(BT_UUID_GATT_FN_VAL)

#define BT_UUID_GATT_ALT_VAL 0x2ab3
#define BT_UUID_GATT_ALT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ALT_VAL)

#define BT_UUID_GATT_UNCERTAINTY_VAL 0x2ab4
#define BT_UUID_GATT_UNCERTAINTY \
        BT_UUID_DECLARE_16(BT_UUID_GATT_UNCERTAINTY_VAL)

#define BT_UUID_GATT_LOC_NAME_VAL 0x2ab5
#define BT_UUID_GATT_LOC_NAME \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LOC_NAME_VAL)

#define BT_UUID_URI_VAL 0x2ab6
#define BT_UUID_URI \
        BT_UUID_DECLARE_16(BT_UUID_URI_VAL)

#define BT_UUID_HTTP_HEADERS_VAL 0x2ab7
#define BT_UUID_HTTP_HEADERS \
        BT_UUID_DECLARE_16(BT_UUID_HTTP_HEADERS_VAL)

#define BT_UUID_HTTP_STATUS_CODE_VAL 0x2ab8
#define BT_UUID_HTTP_STATUS_CODE \
        BT_UUID_DECLARE_16(BT_UUID_HTTP_STATUS_CODE_VAL)

#define BT_UUID_HTTP_ENTITY_BODY_VAL 0x2ab9
#define BT_UUID_HTTP_ENTITY_BODY \
        BT_UUID_DECLARE_16(BT_UUID_HTTP_ENTITY_BODY_VAL)

#define BT_UUID_HTTP_CONTROL_POINT_VAL 0x2aba
#define BT_UUID_HTTP_CONTROL_POINT \
        BT_UUID_DECLARE_16(BT_UUID_HTTP_CONTROL_POINT_VAL)

#define BT_UUID_HTTPS_SECURITY_VAL 0x2abb
#define BT_UUID_HTTPS_SECURITY \
        BT_UUID_DECLARE_16(BT_UUID_HTTPS_SECURITY_VAL)

#define BT_UUID_GATT_TDS_CP_VAL 0x2abc
#define BT_UUID_GATT_TDS_CP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TDS_CP_VAL)

#define BT_UUID_OTS_FEATURE_VAL 0x2abd
#define BT_UUID_OTS_FEATURE \
        BT_UUID_DECLARE_16(BT_UUID_OTS_FEATURE_VAL)

#define BT_UUID_OTS_NAME_VAL 0x2abe
#define BT_UUID_OTS_NAME \
        BT_UUID_DECLARE_16(BT_UUID_OTS_NAME_VAL)

#define BT_UUID_OTS_TYPE_VAL 0x2abf
#define BT_UUID_OTS_TYPE \
        BT_UUID_DECLARE_16(BT_UUID_OTS_TYPE_VAL)

#define BT_UUID_OTS_SIZE_VAL 0x2ac0
#define BT_UUID_OTS_SIZE \
        BT_UUID_DECLARE_16(BT_UUID_OTS_SIZE_VAL)

#define BT_UUID_OTS_FIRST_CREATED_VAL 0x2ac1
#define BT_UUID_OTS_FIRST_CREATED \
        BT_UUID_DECLARE_16(BT_UUID_OTS_FIRST_CREATED_VAL)

#define BT_UUID_OTS_LAST_MODIFIED_VAL 0x2ac2
#define BT_UUID_OTS_LAST_MODIFIED \
        BT_UUID_DECLARE_16(BT_UUID_OTS_LAST_MODIFIED_VAL)

#define BT_UUID_OTS_ID_VAL 0x2ac3
#define BT_UUID_OTS_ID \
        BT_UUID_DECLARE_16(BT_UUID_OTS_ID_VAL)

#define BT_UUID_OTS_PROPERTIES_VAL 0x2ac4
#define BT_UUID_OTS_PROPERTIES \
        BT_UUID_DECLARE_16(BT_UUID_OTS_PROPERTIES_VAL)

#define BT_UUID_OTS_ACTION_CP_VAL 0x2ac5
#define BT_UUID_OTS_ACTION_CP \
        BT_UUID_DECLARE_16(BT_UUID_OTS_ACTION_CP_VAL)

#define BT_UUID_OTS_LIST_CP_VAL 0x2ac6
#define BT_UUID_OTS_LIST_CP \
        BT_UUID_DECLARE_16(BT_UUID_OTS_LIST_CP_VAL)

#define BT_UUID_OTS_LIST_FILTER_VAL 0x2ac7
#define BT_UUID_OTS_LIST_FILTER \
        BT_UUID_DECLARE_16(BT_UUID_OTS_LIST_FILTER_VAL)

#define BT_UUID_OTS_CHANGED_VAL 0x2ac8
#define BT_UUID_OTS_CHANGED \
        BT_UUID_DECLARE_16(BT_UUID_OTS_CHANGED_VAL)

#define BT_UUID_GATT_RPAO_VAL 0x2ac9
#define BT_UUID_GATT_RPAO \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RPAO_VAL)

#define BT_UUID_OTS_TYPE_UNSPECIFIED_VAL 0x2aca
#define BT_UUID_OTS_TYPE_UNSPECIFIED \
        BT_UUID_DECLARE_16(BT_UUID_OTS_TYPE_UNSPECIFIED_VAL)

#define BT_UUID_OTS_DIRECTORY_LISTING_VAL 0x2acb
#define BT_UUID_OTS_DIRECTORY_LISTING \
        BT_UUID_DECLARE_16(BT_UUID_OTS_DIRECTORY_LISTING_VAL)

#define BT_UUID_GATT_FMF_VAL 0x2acc
#define BT_UUID_GATT_FMF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_FMF_VAL)

#define BT_UUID_GATT_TD_VAL 0x2acd
#define BT_UUID_GATT_TD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TD_VAL)

#define BT_UUID_GATT_CTD_VAL 0x2ace
#define BT_UUID_GATT_CTD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CTD_VAL)

#define BT_UUID_GATT_STPCD_VAL 0x2acf
#define BT_UUID_GATT_STPCD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_STPCD_VAL)

#define BT_UUID_GATT_STRCD_VAL 0x2ad0
#define BT_UUID_GATT_STRCD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_STRCD_VAL)

#define BT_UUID_GATT_RD_VAL 0x2ad1
#define BT_UUID_GATT_RD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RD_VAL)

#define BT_UUID_GATT_IBD_VAL 0x2ad2
#define BT_UUID_GATT_IBD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_IBD_VAL)

#define BT_UUID_GATT_TRSTAT_VAL 0x2ad3
#define BT_UUID_GATT_TRSTAT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TRSTAT_VAL)

#define BT_UUID_GATT_SSR_VAL 0x2ad4
#define BT_UUID_GATT_SSR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SSR_VAL)

#define BT_UUID_GATT_SIR_VAL 0x2ad5
#define BT_UUID_GATT_SIR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SIR_VAL)

#define BT_UUID_GATT_SRLR_VAL 0x2ad6
#define BT_UUID_GATT_SRLR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SRLR_VAL)

#define BT_UUID_GATT_SHRR_VAL 0x2ad7
#define BT_UUID_GATT_SHRR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SHRR_VAL)

#define BT_UUID_GATT_SPR_VAL 0x2ad8
#define BT_UUID_GATT_SPR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SPR_VAL)

#define BT_UUID_GATT_FMCP_VAL 0x2ad9
#define BT_UUID_GATT_FMCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_FMCP_VAL)

#define BT_UUID_GATT_FMS_VAL 0x2ada
#define BT_UUID_GATT_FMS \
        BT_UUID_DECLARE_16(BT_UUID_GATT_FMS_VAL)

#define BT_UUID_MESH_PROV_DATA_IN_VAL 0x2adb
#define BT_UUID_MESH_PROV_DATA_IN \
        BT_UUID_DECLARE_16(BT_UUID_MESH_PROV_DATA_IN_VAL)

#define BT_UUID_MESH_PROV_DATA_OUT_VAL 0x2adc
#define BT_UUID_MESH_PROV_DATA_OUT \
        BT_UUID_DECLARE_16(BT_UUID_MESH_PROV_DATA_OUT_VAL)

#define BT_UUID_MESH_PROXY_DATA_IN_VAL 0x2add
#define BT_UUID_MESH_PROXY_DATA_IN \
        BT_UUID_DECLARE_16(BT_UUID_MESH_PROXY_DATA_IN_VAL)

#define BT_UUID_MESH_PROXY_DATA_OUT_VAL 0x2ade
#define BT_UUID_MESH_PROXY_DATA_OUT \
        BT_UUID_DECLARE_16(BT_UUID_MESH_PROXY_DATA_OUT_VAL)

#define BT_UUID_GATT_NNN_VAL 0x2adf
#define BT_UUID_GATT_NNN \
        BT_UUID_DECLARE_16(BT_UUID_GATT_NNN_VAL)

#define BT_UUID_GATT_AC_VAL 0x2ae0
#define BT_UUID_GATT_AC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AC_VAL)

#define BT_UUID_GATT_AV_VAL 0x2ae1
#define BT_UUID_GATT_AV \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AV_VAL)

#define BT_UUID_GATT_BOOLEAN_VAL 0x2ae2
#define BT_UUID_GATT_BOOLEAN \
        BT_UUID_DECLARE_16(BT_UUID_GATT_BOOLEAN_VAL)

#define BT_UUID_GATT_CRDFP_VAL 0x2ae3
#define BT_UUID_GATT_CRDFP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CRDFP_VAL)

#define BT_UUID_GATT_CRCOORDS_VAL 0x2ae4
#define BT_UUID_GATT_CRCOORDS \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CRCOORDS_VAL)

#define BT_UUID_GATT_CRCCT_VAL 0x2ae5
#define BT_UUID_GATT_CRCCT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CRCCT_VAL)

#define BT_UUID_GATT_CRT_VAL 0x2ae6
#define BT_UUID_GATT_CRT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CRT_VAL)

#define BT_UUID_GATT_CIEIDX_VAL 0x2ae7
#define BT_UUID_GATT_CIEIDX \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CIEIDX_VAL)

#define BT_UUID_GATT_COEFFICIENT_VAL 0x2ae8
#define BT_UUID_GATT_COEFFICIENT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_COEFFICIENT_VAL)

#define BT_UUID_GATT_CCTEMP_VAL 0x2ae9
#define BT_UUID_GATT_CCTEMP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CCTEMP_VAL)

#define BT_UUID_GATT_COUNT16_VAL 0x2aea
#define BT_UUID_GATT_COUNT16 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_COUNT16_VAL)

#define BT_UUID_GATT_COUNT24_VAL 0x2aeb
#define BT_UUID_GATT_COUNT24 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_COUNT24_VAL)

#define BT_UUID_GATT_CNTRCODE_VAL 0x2aec
#define BT_UUID_GATT_CNTRCODE \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CNTRCODE_VAL)

#define BT_UUID_GATT_DATEUTC_VAL 0x2aed
#define BT_UUID_GATT_DATEUTC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DATEUTC_VAL)

#define BT_UUID_GATT_EC_VAL 0x2aee
#define BT_UUID_GATT_EC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_EC_VAL)

#define BT_UUID_GATT_ECR_VAL 0x2aef
#define BT_UUID_GATT_ECR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ECR_VAL)

#define BT_UUID_GATT_ECSPEC_VAL 0x2af0
#define BT_UUID_GATT_ECSPEC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ECSPEC_VAL)

#define BT_UUID_GATT_ECSTAT_VAL 0x2af1
#define BT_UUID_GATT_ECSTAT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ECSTAT_VAL)

#define BT_UUID_GATT_ENERGY_VAL 0x2af2
#define BT_UUID_GATT_ENERGY \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ENERGY_VAL)

#define BT_UUID_GATT_EPOD_VAL 0x2af3
#define BT_UUID_GATT_EPOD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_EPOD_VAL)

#define BT_UUID_GATT_EVTSTAT_VAL 0x2af4
#define BT_UUID_GATT_EVTSTAT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_EVTSTAT_VAL)

#define BT_UUID_GATT_FSTR16_VAL 0x2af5
#define BT_UUID_GATT_FSTR16 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_FSTR16_VAL)

#define BT_UUID_GATT_FSTR24_VAL 0x2af6
#define BT_UUID_GATT_FSTR24 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_FSTR24_VAL)

#define BT_UUID_GATT_FSTR36_VAL 0x2af7
#define BT_UUID_GATT_FSTR36 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_FSTR36_VAL)

#define BT_UUID_GATT_FSTR8_VAL 0x2af8
#define BT_UUID_GATT_FSTR8 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_FSTR8_VAL)

#define BT_UUID_GATT_GENLVL_VAL 0x2af9
#define BT_UUID_GATT_GENLVL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_GENLVL_VAL)

#define BT_UUID_GATT_GTIN_VAL 0x2afa
#define BT_UUID_GATT_GTIN \
        BT_UUID_DECLARE_16(BT_UUID_GATT_GTIN_VAL)

#define BT_UUID_GATT_ILLUM_VAL 0x2afb
#define BT_UUID_GATT_ILLUM \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ILLUM_VAL)

#define BT_UUID_GATT_LUMEFF_VAL 0x2afc
#define BT_UUID_GATT_LUMEFF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LUMEFF_VAL)

#define BT_UUID_GATT_LUMNRG_VAL 0x2afd
#define BT_UUID_GATT_LUMNRG \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LUMNRG_VAL)

#define BT_UUID_GATT_LUMEXP_VAL 0x2afe
#define BT_UUID_GATT_LUMEXP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LUMEXP_VAL)

#define BT_UUID_GATT_LUMFLX_VAL 0x2aff
#define BT_UUID_GATT_LUMFLX \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LUMFLX_VAL)

#define BT_UUID_GATT_LUMFLXR_VAL 0x2b00
#define BT_UUID_GATT_LUMFLXR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LUMFLXR_VAL)

#define BT_UUID_GATT_LUMINT_VAL 0x2b01
#define BT_UUID_GATT_LUMINT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LUMINT_VAL)

#define BT_UUID_GATT_MASSFLOW_VAL 0x2b02
#define BT_UUID_GATT_MASSFLOW \
        BT_UUID_DECLARE_16(BT_UUID_GATT_MASSFLOW_VAL)

#define BT_UUID_GATT_PERLGHT_VAL 0x2b03
#define BT_UUID_GATT_PERLGHT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PERLGHT_VAL)

#define BT_UUID_GATT_PER8_VAL 0x2b04
#define BT_UUID_GATT_PER8 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PER8_VAL)

#define BT_UUID_GATT_PWR_VAL 0x2b05
#define BT_UUID_GATT_PWR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PWR_VAL)

#define BT_UUID_GATT_PWRSPEC_VAL 0x2b06
#define BT_UUID_GATT_PWRSPEC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PWRSPEC_VAL)

#define BT_UUID_GATT_RRICR_VAL 0x2b07
#define BT_UUID_GATT_RRICR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RRICR_VAL)

#define BT_UUID_GATT_RRIGLR_VAL 0x2b08
#define BT_UUID_GATT_RRIGLR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RRIGLR_VAL)

#define BT_UUID_GATT_RVIVR_VAL 0x2b09
#define BT_UUID_GATT_RVIVR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RVIVR_VAL)

#define BT_UUID_GATT_RVIIR_VAL 0x2b0a
#define BT_UUID_GATT_RVIIR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RVIIR_VAL)

#define BT_UUID_GATT_RVIPOD_VAL 0x2b0b
#define BT_UUID_GATT_RVIPOD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RVIPOD_VAL)

#define BT_UUID_GATT_RVITR_VAL 0x2b0c
#define BT_UUID_GATT_RVITR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RVITR_VAL)

#define BT_UUID_GATT_TEMP8_VAL 0x2b0d
#define BT_UUID_GATT_TEMP8 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TEMP8_VAL)

#define BT_UUID_GATT_TEMP8_IPOD_VAL 0x2b0e
#define BT_UUID_GATT_TEMP8_IPOD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TEMP8_IPOD_VAL)

#define BT_UUID_GATT_TEMP8_STAT_VAL 0x2b0f
#define BT_UUID_GATT_TEMP8_STAT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TEMP8_STAT_VAL)

#define BT_UUID_GATT_TEMP_RNG_VAL 0x2b10
#define BT_UUID_GATT_TEMP_RNG \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TEMP_RNG_VAL)

#define BT_UUID_GATT_TEMP_STAT_VAL 0x2b11
#define BT_UUID_GATT_TEMP_STAT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TEMP_STAT_VAL)

#define BT_UUID_GATT_TIM_DC8_VAL 0x2b12
#define BT_UUID_GATT_TIM_DC8 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_DC8_VAL)

#define BT_UUID_GATT_TIM_EXP8_VAL 0x2b13
#define BT_UUID_GATT_TIM_EXP8 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_EXP8_VAL)

#define BT_UUID_GATT_TIM_H24_VAL 0x2b14
#define BT_UUID_GATT_TIM_H24 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_H24_VAL)

#define BT_UUID_GATT_TIM_MS24_VAL 0x2b15
#define BT_UUID_GATT_TIM_MS24 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_MS24_VAL)

#define BT_UUID_GATT_TIM_S16_VAL 0x2b16
#define BT_UUID_GATT_TIM_S16 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_S16_VAL)

#define BT_UUID_GATT_TIM_S8_VAL 0x2b17
#define BT_UUID_GATT_TIM_S8 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_S8_VAL)

#define BT_UUID_GATT_V_VAL 0x2b18
#define BT_UUID_GATT_V \
        BT_UUID_DECLARE_16(BT_UUID_GATT_V_VAL)

#define BT_UUID_GATT_V_SPEC_VAL 0x2b19
#define BT_UUID_GATT_V_SPEC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_V_SPEC_VAL)

#define BT_UUID_GATT_V_STAT_VAL 0x2b1a
#define BT_UUID_GATT_V_STAT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_V_STAT_VAL)

#define BT_UUID_GATT_VOLF_VAL 0x2b1b
#define BT_UUID_GATT_VOLF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_VOLF_VAL)

#define BT_UUID_GATT_CRCOORD_VAL 0x2b1c
#define BT_UUID_GATT_CRCOORD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CRCOORD_VAL)

#define BT_UUID_GATT_RCF_VAL 0x2b1d
#define BT_UUID_GATT_RCF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RCF_VAL)

#define BT_UUID_GATT_RCSET_VAL 0x2b1e
#define BT_UUID_GATT_RCSET \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RCSET_VAL)

#define BT_UUID_GATT_RCCP_VAL 0x2b1f
#define BT_UUID_GATT_RCCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RCCP_VAL)

#define BT_UUID_GATT_IDD_SC_VAL 0x2b20
#define BT_UUID_GATT_IDD_SC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_SC_VAL)

#define BT_UUID_GATT_IDD_S_VAL 0x2b21
#define BT_UUID_GATT_IDD_S \
        BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_S_VAL)

#define BT_UUID_GATT_IDD_AS_VAL 0x2b22
#define BT_UUID_GATT_IDD_AS \
        BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_AS_VAL)

#define BT_UUID_GATT_IDD_F_VAL 0x2b23
#define BT_UUID_GATT_IDD_F \
        BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_F_VAL)

#define BT_UUID_GATT_IDD_SRCP_VAL 0x2b24
#define BT_UUID_GATT_IDD_SRCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_SRCP_VAL)

#define BT_UUID_GATT_IDD_CCP_VAL 0x2b25
#define BT_UUID_GATT_IDD_CCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_CCP_VAL)

#define BT_UUID_GATT_IDD_CD_VAL 0x2b26
#define BT_UUID_GATT_IDD_CD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_CD_VAL)

#define BT_UUID_GATT_IDD_RACP_VAL 0x2b27
#define BT_UUID_GATT_IDD_RACP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_RACP_VAL)

#define BT_UUID_GATT_IDD_HD_VAL 0x2b28
#define BT_UUID_GATT_IDD_HD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_IDD_HD_VAL)

#define BT_UUID_GATT_CLIENT_FEATURES_VAL 0x2b29
#define BT_UUID_GATT_CLIENT_FEATURES \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CLIENT_FEATURES_VAL)

#define BT_UUID_GATT_DB_HASH_VAL 0x2b2a
#define BT_UUID_GATT_DB_HASH \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DB_HASH_VAL)

#define BT_UUID_GATT_BSS_CP_VAL 0x2b2b
#define BT_UUID_GATT_BSS_CP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_BSS_CP_VAL)

#define BT_UUID_GATT_BSS_R_VAL 0x2b2c
#define BT_UUID_GATT_BSS_R \
        BT_UUID_DECLARE_16(BT_UUID_GATT_BSS_R_VAL)

#define BT_UUID_GATT_EMG_ID_VAL 0x2b2d
#define BT_UUID_GATT_EMG_ID \
        BT_UUID_DECLARE_16(BT_UUID_GATT_EMG_ID_VAL)

#define BT_UUID_GATT_EMG_TXT_VAL 0x2b2e
#define BT_UUID_GATT_EMG_TXT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_EMG_TXT_VAL)

#define BT_UUID_GATT_ACS_S_VAL 0x2b2f
#define BT_UUID_GATT_ACS_S \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ACS_S_VAL)

#define BT_UUID_GATT_ACS_DI_VAL 0x2b30
#define BT_UUID_GATT_ACS_DI \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ACS_DI_VAL)

#define BT_UUID_GATT_ACS_DON_VAL 0x2b31
#define BT_UUID_GATT_ACS_DON \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ACS_DON_VAL)

#define BT_UUID_GATT_ACS_DOI_VAL 0x2b32
#define BT_UUID_GATT_ACS_DOI \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ACS_DOI_VAL)

#define BT_UUID_GATT_ACS_CP_VAL 0x2b33
#define BT_UUID_GATT_ACS_CP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ACS_CP_VAL)

#define BT_UUID_GATT_EBPM_VAL 0x2b34
#define BT_UUID_GATT_EBPM \
        BT_UUID_DECLARE_16(BT_UUID_GATT_EBPM_VAL)

#define BT_UUID_GATT_EICP_VAL 0x2b35
#define BT_UUID_GATT_EICP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_EICP_VAL)

#define BT_UUID_GATT_BPR_VAL 0x2b36
#define BT_UUID_GATT_BPR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_BPR_VAL)

#define BT_UUID_GATT_RU_VAL 0x2b37
#define BT_UUID_GATT_RU \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RU_VAL)

#define BT_UUID_GATT_BR_EDR_HD_VAL 0x2b38
#define BT_UUID_GATT_BR_EDR_HD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_BR_EDR_HD_VAL)

#define BT_UUID_GATT_BT_SIG_D_VAL 0x2b39
#define BT_UUID_GATT_BT_SIG_D \
        BT_UUID_DECLARE_16(BT_UUID_GATT_BT_SIG_D_VAL)

#define BT_UUID_GATT_SERVER_FEATURES_VAL  0x2b3a
#define BT_UUID_GATT_SERVER_FEATURES      \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SERVER_FEATURES_VAL)

#define BT_UUID_GATT_PHY_AMF_VAL 0x2b3b
#define BT_UUID_GATT_PHY_AMF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PHY_AMF_VAL)

#define BT_UUID_GATT_GEN_AID_VAL 0x2b3c
#define BT_UUID_GATT_GEN_AID \
        BT_UUID_DECLARE_16(BT_UUID_GATT_GEN_AID_VAL)

#define BT_UUID_GATT_GEN_ASD_VAL 0x2b3d
#define BT_UUID_GATT_GEN_ASD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_GEN_ASD_VAL)

#define BT_UUID_GATT_CR_AID_VAL 0x2b3e
#define BT_UUID_GATT_CR_AID \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CR_AID_VAL)

#define BT_UUID_GATT_CR_ASD_VAL 0x2b3f
#define BT_UUID_GATT_CR_ASD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CR_ASD_VAL)

#define BT_UUID_GATT_SC_ASD_VAL 0x2b40
#define BT_UUID_GATT_SC_ASD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SC_ASD_VAL)

#define BT_UUID_GATT_SLP_AID_VAL 0x2b41
#define BT_UUID_GATT_SLP_AID \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SLP_AID_VAL)

#define BT_UUID_GATT_SLP_ASD_VAL 0x2b42
#define BT_UUID_GATT_SLP_ASD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SLP_ASD_VAL)

#define BT_UUID_GATT_PHY_AMCP_VAL 0x2b43
#define BT_UUID_GATT_PHY_AMCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PHY_AMCP_VAL)

#define BT_UUID_GATT_ACS_VAL 0x2b44
#define BT_UUID_GATT_ACS \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ACS_VAL)

#define BT_UUID_GATT_PHY_ASDESC_VAL 0x2b45
#define BT_UUID_GATT_PHY_ASDESC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PHY_ASDESC_VAL)

#define BT_UUID_GATT_PREF_U_VAL 0x2b46
#define BT_UUID_GATT_PREF_U \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PREF_U_VAL)

#define BT_UUID_GATT_HRES_H_VAL 0x2b47
#define BT_UUID_GATT_HRES_H \
        BT_UUID_DECLARE_16(BT_UUID_GATT_HRES_H_VAL)

#define BT_UUID_GATT_MID_NAME_VAL 0x2b48
#define BT_UUID_GATT_MID_NAME \
        BT_UUID_DECLARE_16(BT_UUID_GATT_MID_NAME_VAL)

#define BT_UUID_GATT_STRDLEN_VAL 0x2b49
#define BT_UUID_GATT_STRDLEN \
        BT_UUID_DECLARE_16(BT_UUID_GATT_STRDLEN_VAL)

#define BT_UUID_GATT_HANDEDNESS_VAL 0x2b4a
#define BT_UUID_GATT_HANDEDNESS \
        BT_UUID_DECLARE_16(BT_UUID_GATT_HANDEDNESS_VAL)

#define BT_UUID_GATT_DEVICE_WP_VAL 0x2b4b
#define BT_UUID_GATT_DEVICE_WP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DEVICE_WP_VAL)

#define BT_UUID_GATT_4ZHRL_VAL 0x2b4c
#define BT_UUID_GATT_4ZHRL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_4ZHRL_VAL)

#define BT_UUID_GATT_HIET_VAL 0x2b4d
#define BT_UUID_GATT_HIET \
        BT_UUID_DECLARE_16(BT_UUID_GATT_HIET_VAL)

#define BT_UUID_GATT_AG_VAL 0x2b4e
#define BT_UUID_GATT_AG \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AG_VAL)

#define BT_UUID_GATT_SIN_VAL 0x2b4f
#define BT_UUID_GATT_SIN \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SIN_VAL)

#define BT_UUID_GATT_CI_VAL 0x2b50
#define BT_UUID_GATT_CI \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CI_VAL)

#define BT_UUID_GATT_TMAPR_VAL 0x2b51
#define BT_UUID_GATT_TMAPR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TMAPR_VAL)

#define BT_UUID_AICS_STATE_VAL 0x2b77
#define BT_UUID_AICS_STATE \
        BT_UUID_DECLARE_16(BT_UUID_AICS_STATE_VAL)

#define BT_UUID_AICS_GAIN_SETTINGS_VAL 0x2b78
#define BT_UUID_AICS_GAIN_SETTINGS \
        BT_UUID_DECLARE_16(BT_UUID_AICS_GAIN_SETTINGS_VAL)

#define BT_UUID_AICS_INPUT_TYPE_VAL 0x2b79
#define BT_UUID_AICS_INPUT_TYPE \
        BT_UUID_DECLARE_16(BT_UUID_AICS_INPUT_TYPE_VAL)

#define BT_UUID_AICS_INPUT_STATUS_VAL 0x2b7a
#define BT_UUID_AICS_INPUT_STATUS \
        BT_UUID_DECLARE_16(BT_UUID_AICS_INPUT_STATUS_VAL)

#define BT_UUID_AICS_CONTROL_VAL 0x2b7b
#define BT_UUID_AICS_CONTROL \
        BT_UUID_DECLARE_16(BT_UUID_AICS_CONTROL_VAL)

#define BT_UUID_AICS_DESCRIPTION_VAL 0x2b7c
#define BT_UUID_AICS_DESCRIPTION \
        BT_UUID_DECLARE_16(BT_UUID_AICS_DESCRIPTION_VAL)

#define BT_UUID_VCS_STATE_VAL 0x2b7d
#define BT_UUID_VCS_STATE \
        BT_UUID_DECLARE_16(BT_UUID_VCS_STATE_VAL)

#define BT_UUID_VCS_CONTROL_VAL 0x2b7e
#define BT_UUID_VCS_CONTROL \
        BT_UUID_DECLARE_16(BT_UUID_VCS_CONTROL_VAL)

#define BT_UUID_VCS_FLAGS_VAL 0x2b7f
#define BT_UUID_VCS_FLAGS \
        BT_UUID_DECLARE_16(BT_UUID_VCS_FLAGS_VAL)

#define BT_UUID_VOCS_STATE_VAL 0x2b80
#define BT_UUID_VOCS_STATE \
        BT_UUID_DECLARE_16(BT_UUID_VOCS_STATE_VAL)

#define BT_UUID_VOCS_LOCATION_VAL 0x2b81
#define BT_UUID_VOCS_LOCATION \
        BT_UUID_DECLARE_16(BT_UUID_VOCS_LOCATION_VAL)

#define BT_UUID_VOCS_CONTROL_VAL 0x2b82
#define BT_UUID_VOCS_CONTROL \
        BT_UUID_DECLARE_16(BT_UUID_VOCS_CONTROL_VAL)

#define BT_UUID_VOCS_DESCRIPTION_VAL 0x2b83
#define BT_UUID_VOCS_DESCRIPTION \
        BT_UUID_DECLARE_16(BT_UUID_VOCS_DESCRIPTION_VAL)

#define BT_UUID_CSIS_SIRK_VAL 0x2b84
#define BT_UUID_CSIS_SIRK         BT_UUID_DECLARE_16(BT_UUID_CSIS_SIRK_VAL)
#define BT_UUID_CSIS_SET_SIZE_VAL 0x2b85
#define BT_UUID_CSIS_SET_SIZE \
        BT_UUID_DECLARE_16(BT_UUID_CSIS_SET_SIZE_VAL)

#define BT_UUID_CSIS_SET_LOCK_VAL 0x2b86
#define BT_UUID_CSIS_SET_LOCK \
        BT_UUID_DECLARE_16(BT_UUID_CSIS_SET_LOCK_VAL)

#define BT_UUID_CSIS_RANK_VAL 0x2b87
#define BT_UUID_CSIS_RANK \
        BT_UUID_DECLARE_16(BT_UUID_CSIS_RANK_VAL)

#define BT_UUID_GATT_EDKM_VAL 0x2b88
#define BT_UUID_GATT_EDKM \
        BT_UUID_DECLARE_16(BT_UUID_GATT_EDKM_VAL)

#define BT_UUID_GATT_AE32_VAL 0x2b89
#define BT_UUID_GATT_AE32 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AE32_VAL)

#define BT_UUID_GATT_AP_VAL 0x2b8a
#define BT_UUID_GATT_AP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_AP_VAL)

#define BT_UUID_GATT_CO2CONC_VAL 0x2b8c
#define BT_UUID_GATT_CO2CONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CO2CONC_VAL)

#define BT_UUID_GATT_COS_VAL 0x2b8d
#define BT_UUID_GATT_COS \
        BT_UUID_DECLARE_16(BT_UUID_GATT_COS_VAL)

#define BT_UUID_GATT_DEVTF_VAL 0x2b8e
#define BT_UUID_GATT_DEVTF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DEVTF_VAL)

#define BT_UUID_GATT_DEVTP_VAL 0x2b8f
#define BT_UUID_GATT_DEVTP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DEVTP_VAL)

#define BT_UUID_GATT_DEVT_VAL 0x2b90
#define BT_UUID_GATT_DEVT \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DEVT_VAL)

#define BT_UUID_GATT_DEVTCP_VAL 0x2b91
#define BT_UUID_GATT_DEVTCP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_DEVTCP_VAL)

#define BT_UUID_GATT_TCLD_VAL 0x2b92
#define BT_UUID_GATT_TCLD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TCLD_VAL)

#define BT_UUID_MCS_PLAYER_NAME_VAL 0x2b93
#define BT_UUID_MCS_PLAYER_NAME \
        BT_UUID_DECLARE_16(BT_UUID_MCS_PLAYER_NAME_VAL)

#define BT_UUID_MCS_ICON_OBJ_ID_VAL 0x2b94
#define BT_UUID_MCS_ICON_OBJ_ID \
        BT_UUID_DECLARE_16(BT_UUID_MCS_ICON_OBJ_ID_VAL)

#define BT_UUID_MCS_ICON_URL_VAL 0x2b95
#define BT_UUID_MCS_ICON_URL \
        BT_UUID_DECLARE_16(BT_UUID_MCS_ICON_URL_VAL)

#define BT_UUID_MCS_TRACK_CHANGED_VAL 0x2b96
#define BT_UUID_MCS_TRACK_CHANGED \
        BT_UUID_DECLARE_16(BT_UUID_MCS_TRACK_CHANGED_VAL)

#define BT_UUID_MCS_TRACK_TITLE_VAL 0x2b97
#define BT_UUID_MCS_TRACK_TITLE \
        BT_UUID_DECLARE_16(BT_UUID_MCS_TRACK_TITLE_VAL)

#define BT_UUID_MCS_TRACK_DURATION_VAL 0x2b98
#define BT_UUID_MCS_TRACK_DURATION \
        BT_UUID_DECLARE_16(BT_UUID_MCS_TRACK_DURATION_VAL)

#define BT_UUID_MCS_TRACK_POSITION_VAL 0x2b99
#define BT_UUID_MCS_TRACK_POSITION \
        BT_UUID_DECLARE_16(BT_UUID_MCS_TRACK_POSITION_VAL)

#define BT_UUID_MCS_PLAYBACK_SPEED_VAL 0x2b9a
#define BT_UUID_MCS_PLAYBACK_SPEED \
        BT_UUID_DECLARE_16(BT_UUID_MCS_PLAYBACK_SPEED_VAL)

#define BT_UUID_MCS_SEEKING_SPEED_VAL 0x2b9b
#define BT_UUID_MCS_SEEKING_SPEED \
        BT_UUID_DECLARE_16(BT_UUID_MCS_SEEKING_SPEED_VAL)

#define BT_UUID_MCS_TRACK_SEGMENTS_OBJ_ID_VAL 0x2b9c
#define BT_UUID_MCS_TRACK_SEGMENTS_OBJ_ID \
        BT_UUID_DECLARE_16(BT_UUID_MCS_TRACK_SEGMENTS_OBJ_ID_VAL)

#define BT_UUID_MCS_CURRENT_TRACK_OBJ_ID_VAL 0x2b9d
#define BT_UUID_MCS_CURRENT_TRACK_OBJ_ID \
        BT_UUID_DECLARE_16(BT_UUID_MCS_CURRENT_TRACK_OBJ_ID_VAL)

#define BT_UUID_MCS_NEXT_TRACK_OBJ_ID_VAL 0x2b9e
#define BT_UUID_MCS_NEXT_TRACK_OBJ_ID \
        BT_UUID_DECLARE_16(BT_UUID_MCS_NEXT_TRACK_OBJ_ID_VAL)

#define BT_UUID_MCS_PARENT_GROUP_OBJ_ID_VAL 0x2b9f
#define BT_UUID_MCS_PARENT_GROUP_OBJ_ID \
        BT_UUID_DECLARE_16(BT_UUID_MCS_PARENT_GROUP_OBJ_ID_VAL)

#define BT_UUID_MCS_CURRENT_GROUP_OBJ_ID_VAL 0x2ba0
#define BT_UUID_MCS_CURRENT_GROUP_OBJ_ID \
        BT_UUID_DECLARE_16(BT_UUID_MCS_CURRENT_GROUP_OBJ_ID_VAL)

#define BT_UUID_MCS_PLAYING_ORDER_VAL 0x2ba1
#define BT_UUID_MCS_PLAYING_ORDER \
        BT_UUID_DECLARE_16(BT_UUID_MCS_PLAYING_ORDER_VAL)

#define BT_UUID_MCS_PLAYING_ORDERS_VAL 0x2ba2
#define BT_UUID_MCS_PLAYING_ORDERS \
        BT_UUID_DECLARE_16(BT_UUID_MCS_PLAYING_ORDERS_VAL)

#define BT_UUID_MCS_MEDIA_STATE_VAL 0x2ba3
#define BT_UUID_MCS_MEDIA_STATE \
        BT_UUID_DECLARE_16(BT_UUID_MCS_MEDIA_STATE_VAL)

#define BT_UUID_MCS_MEDIA_CONTROL_POINT_VAL 0x2ba4
#define BT_UUID_MCS_MEDIA_CONTROL_POINT \
        BT_UUID_DECLARE_16(BT_UUID_MCS_MEDIA_CONTROL_POINT_VAL)

#define BT_UUID_MCS_MEDIA_CONTROL_OPCODES_VAL 0x2ba5
#define BT_UUID_MCS_MEDIA_CONTROL_OPCODES \
        BT_UUID_DECLARE_16(BT_UUID_MCS_MEDIA_CONTROL_OPCODES_VAL)

#define BT_UUID_MCS_SEARCH_RESULTS_OBJ_ID_VAL 0x2ba6
#define BT_UUID_MCS_SEARCH_RESULTS_OBJ_ID \
        BT_UUID_DECLARE_16(BT_UUID_MCS_SEARCH_RESULTS_OBJ_ID_VAL)

#define BT_UUID_MCS_SEARCH_CONTROL_POINT_VAL 0x2ba7
#define BT_UUID_MCS_SEARCH_CONTROL_POINT \
        BT_UUID_DECLARE_16(BT_UUID_MCS_SEARCH_CONTROL_POINT_VAL)

#define BT_UUID_GATT_E32_VAL 0x2ba8
#define BT_UUID_GATT_E32 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_E32_VAL)

#define BT_UUID_OTS_TYPE_MPL_ICON_VAL 0x2ba9
#define BT_UUID_OTS_TYPE_MPL_ICON \
        BT_UUID_DECLARE_16(BT_UUID_OTS_TYPE_MPL_ICON_VAL)

#define BT_UUID_OTS_TYPE_TRACK_SEGMENT_VAL 0x2baa
#define BT_UUID_OTS_TYPE_TRACK_SEGMENT \
        BT_UUID_DECLARE_16(BT_UUID_OTS_TYPE_TRACK_SEGMENT_VAL)

#define BT_UUID_OTS_TYPE_TRACK_VAL 0x2bab
#define BT_UUID_OTS_TYPE_TRACK \
        BT_UUID_DECLARE_16(BT_UUID_OTS_TYPE_TRACK_VAL)

#define BT_UUID_OTS_TYPE_GROUP_VAL 0x2bac
#define BT_UUID_OTS_TYPE_GROUP \
        BT_UUID_DECLARE_16(BT_UUID_OTS_TYPE_GROUP_VAL)

#define BT_UUID_GATT_CTEE_VAL 0x2bad
#define BT_UUID_GATT_CTEE \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CTEE_VAL)

#define BT_UUID_GATT_ACTEML_VAL 0x2bae
#define BT_UUID_GATT_ACTEML \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ACTEML_VAL)

#define BT_UUID_GATT_ACTEMTC_VAL 0x2baf
#define BT_UUID_GATT_ACTEMTC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ACTEMTC_VAL)

#define BT_UUID_GATT_ACTETD_VAL 0x2bb0
#define BT_UUID_GATT_ACTETD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ACTETD_VAL)

#define BT_UUID_GATT_ACTEI_VAL 0x2bb1
#define BT_UUID_GATT_ACTEI \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ACTEI_VAL)

#define BT_UUID_GATT_ACTEP_VAL 0x2bb2
#define BT_UUID_GATT_ACTEP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ACTEP_VAL)

#define BT_UUID_TBS_PROVIDER_NAME_VAL 0x2bb3
#define BT_UUID_TBS_PROVIDER_NAME \
        BT_UUID_DECLARE_16(BT_UUID_TBS_PROVIDER_NAME_VAL)

#define BT_UUID_TBS_UCI_VAL 0x2bb4
#define BT_UUID_TBS_UCI \
        BT_UUID_DECLARE_16(BT_UUID_TBS_UCI_VAL)

#define BT_UUID_TBS_TECHNOLOGY_VAL 0x2bb5
#define BT_UUID_TBS_TECHNOLOGY \
        BT_UUID_DECLARE_16(BT_UUID_TBS_TECHNOLOGY_VAL)

#define BT_UUID_TBS_URI_LIST_VAL 0x2bb6
#define BT_UUID_TBS_URI_LIST \
        BT_UUID_DECLARE_16(BT_UUID_TBS_URI_LIST_VAL)

#define BT_UUID_TBS_SIGNAL_STRENGTH_VAL 0x2bb7
#define BT_UUID_TBS_SIGNAL_STRENGTH \
        BT_UUID_DECLARE_16(BT_UUID_TBS_SIGNAL_STRENGTH_VAL)

#define BT_UUID_TBS_SIGNAL_INTERVAL_VAL 0x2bb8
#define BT_UUID_TBS_SIGNAL_INTERVAL \
        BT_UUID_DECLARE_16(BT_UUID_TBS_SIGNAL_INTERVAL_VAL)

#define BT_UUID_TBS_LIST_CURRENT_CALLS_VAL 0x2bb9
#define BT_UUID_TBS_LIST_CURRENT_CALLS \
        BT_UUID_DECLARE_16(BT_UUID_TBS_LIST_CURRENT_CALLS_VAL)

#define BT_UUID_CCID_VAL 0x2bba
#define BT_UUID_CCID \
        BT_UUID_DECLARE_16(BT_UUID_CCID_VAL)

#define BT_UUID_TBS_STATUS_FLAGS_VAL 0x2bbb
#define BT_UUID_TBS_STATUS_FLAGS \
        BT_UUID_DECLARE_16(BT_UUID_TBS_STATUS_FLAGS_VAL)

#define BT_UUID_TBS_INCOMING_URI_VAL 0x2bbc
#define BT_UUID_TBS_INCOMING_URI \
        BT_UUID_DECLARE_16(BT_UUID_TBS_INCOMING_URI_VAL)

#define BT_UUID_TBS_CALL_STATE_VAL 0x2bbd
#define BT_UUID_TBS_CALL_STATE \
        BT_UUID_DECLARE_16(BT_UUID_TBS_CALL_STATE_VAL)

#define BT_UUID_TBS_CALL_CONTROL_POINT_VAL 0x2bbe
#define BT_UUID_TBS_CALL_CONTROL_POINT \
        BT_UUID_DECLARE_16(BT_UUID_TBS_CALL_CONTROL_POINT_VAL)

#define BT_UUID_TBS_OPTIONAL_OPCODES_VAL 0x2bbf
#define BT_UUID_TBS_OPTIONAL_OPCODES \
        BT_UUID_DECLARE_16(BT_UUID_TBS_OPTIONAL_OPCODES_VAL)

#define BT_UUID_TBS_TERMINATE_REASON_VAL 0x2bc0
#define BT_UUID_TBS_TERMINATE_REASON \
        BT_UUID_DECLARE_16(BT_UUID_TBS_TERMINATE_REASON_VAL)

#define BT_UUID_TBS_INCOMING_CALL_VAL 0x2bc1
#define BT_UUID_TBS_INCOMING_CALL \
        BT_UUID_DECLARE_16(BT_UUID_TBS_INCOMING_CALL_VAL)

#define BT_UUID_TBS_FRIENDLY_NAME_VAL 0x2bc2
#define BT_UUID_TBS_FRIENDLY_NAME \
        BT_UUID_DECLARE_16(BT_UUID_TBS_FRIENDLY_NAME_VAL)

#define BT_UUID_MICS_MUTE_VAL 0x2bc3
#define BT_UUID_MICS_MUTE \
        BT_UUID_DECLARE_16(BT_UUID_MICS_MUTE_VAL)

#define BT_UUID_ASCS_ASE_SNK_VAL 0x2bc4
#define BT_UUID_ASCS_ASE_SNK \
        BT_UUID_DECLARE_16(BT_UUID_ASCS_ASE_SNK_VAL)

#define BT_UUID_ASCS_ASE_SRC_VAL 0x2bc5
#define BT_UUID_ASCS_ASE_SRC \
        BT_UUID_DECLARE_16(BT_UUID_ASCS_ASE_SRC_VAL)

#define BT_UUID_ASCS_ASE_CP_VAL 0x2bc6
#define BT_UUID_ASCS_ASE_CP \
        BT_UUID_DECLARE_16(BT_UUID_ASCS_ASE_CP_VAL)

#define BT_UUID_BASS_CONTROL_POINT_VAL 0x2bc7
#define BT_UUID_BASS_CONTROL_POINT \
        BT_UUID_DECLARE_16(BT_UUID_BASS_CONTROL_POINT_VAL)

#define BT_UUID_BASS_RECV_STATE_VAL 0x2bc8
#define BT_UUID_BASS_RECV_STATE \
        BT_UUID_DECLARE_16(BT_UUID_BASS_RECV_STATE_VAL)

#define BT_UUID_PACS_SNK_VAL 0x2bc9
#define BT_UUID_PACS_SNK \
        BT_UUID_DECLARE_16(BT_UUID_PACS_SNK_VAL)

#define BT_UUID_PACS_SNK_LOC_VAL 0x2bca
#define BT_UUID_PACS_SNK_LOC \
        BT_UUID_DECLARE_16(BT_UUID_PACS_SNK_LOC_VAL)

#define BT_UUID_PACS_SRC_VAL 0x2bcb
#define BT_UUID_PACS_SRC \
        BT_UUID_DECLARE_16(BT_UUID_PACS_SRC_VAL)

#define BT_UUID_PACS_SRC_LOC_VAL 0x2bcc
#define BT_UUID_PACS_SRC_LOC \
        BT_UUID_DECLARE_16(BT_UUID_PACS_SRC_LOC_VAL)

#define BT_UUID_PACS_AVAILABLE_CONTEXT_VAL 0x2bcd
#define BT_UUID_PACS_AVAILABLE_CONTEXT \
        BT_UUID_DECLARE_16(BT_UUID_PACS_AVAILABLE_CONTEXT_VAL)

#define BT_UUID_PACS_SUPPORTED_CONTEXT_VAL 0x2bce
#define BT_UUID_PACS_SUPPORTED_CONTEXT \
        BT_UUID_DECLARE_16(BT_UUID_PACS_SUPPORTED_CONTEXT_VAL)

#define BT_UUID_GATT_NH4CONC_VAL 0x2bcf
#define BT_UUID_GATT_NH4CONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_NH4CONC_VAL)

#define BT_UUID_GATT_COCONC_VAL 0x2bd0
#define BT_UUID_GATT_COCONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_COCONC_VAL)

#define BT_UUID_GATT_CH4CONC_VAL 0x2bd1
#define BT_UUID_GATT_CH4CONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_CH4CONC_VAL)

#define BT_UUID_GATT_NO2CONC_VAL 0x2bd2
#define BT_UUID_GATT_NO2CONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_NO2CONC_VAL)

#define BT_UUID_GATT_NONCH4CONC_VAL 0x2bd3
#define BT_UUID_GATT_NONCH4CONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_NONCH4CONC_VAL)

#define BT_UUID_GATT_O3CONC_VAL 0x2bd4
#define BT_UUID_GATT_O3CONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_O3CONC_VAL)

#define BT_UUID_GATT_PM1CONC_VAL 0x2bd5
#define BT_UUID_GATT_PM1CONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PM1CONC_VAL)

#define BT_UUID_GATT_PM25CONC_VAL 0x2bd6
#define BT_UUID_GATT_PM25CONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PM25CONC_VAL)

#define BT_UUID_GATT_PM10CONC_VAL 0x2bd7
#define BT_UUID_GATT_PM10CONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_PM10CONC_VAL)

#define BT_UUID_GATT_SO2CONC_VAL 0x2bd8
#define BT_UUID_GATT_SO2CONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SO2CONC_VAL)

#define BT_UUID_GATT_SF6CONC_VAL 0x2bd9
#define BT_UUID_GATT_SF6CONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SF6CONC_VAL)

#define BT_UUID_HAS_HEARING_AID_FEATURES_VAL 0x2bda
#define BT_UUID_HAS_HEARING_AID_FEATURES \
        BT_UUID_DECLARE_16(BT_UUID_HAS_HEARING_AID_FEATURES_VAL)

#define BT_UUID_HAS_PRESET_CONTROL_POINT_VAL 0x2bdb
#define BT_UUID_HAS_PRESET_CONTROL_POINT \
        BT_UUID_DECLARE_16(BT_UUID_HAS_PRESET_CONTROL_POINT_VAL)

#define BT_UUID_HAS_ACTIVE_PRESET_INDEX_VAL 0x2bdc
#define BT_UUID_HAS_ACTIVE_PRESET_INDEX \
        BT_UUID_DECLARE_16(BT_UUID_HAS_ACTIVE_PRESET_INDEX_VAL)

#define BT_UUID_GATT_FSTR64_VAL 0x2bde
#define BT_UUID_GATT_FSTR64 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_FSTR64_VAL)

#define BT_UUID_GATT_HITEMP_VAL 0x2bdf
#define BT_UUID_GATT_HITEMP \
        BT_UUID_DECLARE_16(BT_UUID_GATT_HITEMP_VAL)

#define BT_UUID_GATT_HV_VAL 0x2be0
#define BT_UUID_GATT_HV \
        BT_UUID_DECLARE_16(BT_UUID_GATT_HV_VAL)

#define BT_UUID_GATT_LD_VAL 0x2be1
#define BT_UUID_GATT_LD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LD_VAL)

#define BT_UUID_GATT_LO_VAL 0x2be2
#define BT_UUID_GATT_LO \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LO_VAL)

#define BT_UUID_GATT_LST_VAL 0x2be3
#define BT_UUID_GATT_LST \
        BT_UUID_DECLARE_16(BT_UUID_GATT_LST_VAL)

#define BT_UUID_GATT_NOISE_VAL 0x2be4
#define BT_UUID_GATT_NOISE \
        BT_UUID_DECLARE_16(BT_UUID_GATT_NOISE_VAL)

#define BT_UUID_GATT_RRCCTP_VAL 0x2be5
#define BT_UUID_GATT_RRCCTR \
        BT_UUID_DECLARE_16(BT_UUID_GATT_RRCCTR_VAL)

#define BT_UUID_GATT_TIM_S32_VAL 0x2be6
#define BT_UUID_GATT_TIM_S32 \
        BT_UUID_DECLARE_16(BT_UUID_GATT_TIM_S32_VAL)

#define BT_UUID_GATT_VOCCONC_VAL 0x2be7
#define BT_UUID_GATT_VOCCONC \
        BT_UUID_DECLARE_16(BT_UUID_GATT_VOCCONC_VAL)

#define BT_UUID_GATT_VF_VAL 0x2be8
#define BT_UUID_GATT_VF \
        BT_UUID_DECLARE_16(BT_UUID_GATT_VF_VAL)

#define BT_UUID_BAS_BATTERY_CRIT_STATUS_VAL 0x2be9
#define BT_UUID_BAS_BATTERY_CRIT_STATUS \
        BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_CRIT_STATUS_VAL)

#define BT_UUID_BAS_BATTERY_HEALTH_STATUS_VAL 0x2bea
#define BT_UUID_BAS_BATTERY_HEALTH_STATUS \
        BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_HEALTH_STATUS_VAL)

#define BT_UUID_BAS_BATTERY_HEALTH_INF_VAL 0x2beb
#define BT_UUID_BAS_BATTERY_HEALTH_INF \
        BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_HEALTH_INF_VAL)

#define BT_UUID_BAS_BATTERY_INF_VAL 0x2bec
#define BT_UUID_BAS_BATTERY_INF \
        BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_INF_VAL)

#define BT_UUID_BAS_BATTERY_LEVEL_STATUS_VAL 0x2bed
#define BT_UUID_BAS_BATTERY_LEVEL_STATUS \
        BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_LEVEL_STATUS_VAL)

#define BT_UUID_BAS_BATTERY_TIME_STATUS_VAL 0x2bee
#define BT_UUID_BAS_BATTERY_TIME_STATUS \
        BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_TIME_STATUS_VAL)

#define BT_UUID_GATT_ESD_VAL 0x2bef
#define BT_UUID_GATT_ESD \
        BT_UUID_DECLARE_16(BT_UUID_GATT_ESD_VAL)

#define BT_UUID_BAS_BATTERY_ENERGY_STATUS_VAL 0x2bf0
#define BT_UUID_BAS_BATTERY_ENERGY_STATUS \
        BT_UUID_DECLARE_16(BT_UUID_BAS_BATTERY_ENERGY_STATUS_VAL)

#define BT_UUID_ETS_CURRENT_ELAPSED_TIME_VAL 0x2bf2
#define BT_UUID_ETS_CURRENT_ELAPSED_TIME \
        BT_UUID_DECLARE_16(BT_UUID_ETS_CURRENT_ELAPSED_TIME_VAL)

#define BT_UUID_GATT_SL_VAL 0x2bf5
#define BT_UUID_GATT_SL \
        BT_UUID_DECLARE_16(BT_UUID_GATT_SL_VAL)

#define BT_UUID_UDI_FOR_MEDICAL_DEVICES_VAL 0x2bff
#define BT_UUID_UDI_FOR_MEDICAL_DEVICES \
        BT_UUID_DECLARE_16(BT_UUID_UDI_FOR_MEDICAL_DEVICES_VAL)

#define BT_UUID_GMAS_VAL 0x1858
#define BT_UUID_GMAS     BT_UUID_DECLARE_16(BT_UUID_GMAS_VAL)

#define BT_UUID_GMAP_ROLE_VAL 0x2C00
#define BT_UUID_GMAP_ROLE     BT_UUID_DECLARE_16(BT_UUID_GMAP_ROLE_VAL)

#define BT_UUID_GMAP_UGG_FEAT_VAL 0x2C01
#define BT_UUID_GMAP_UGG_FEAT     BT_UUID_DECLARE_16(BT_UUID_GMAP_UGG_FEAT_VAL)

#define BT_UUID_GMAP_UGT_FEAT_VAL 0x2C02
#define BT_UUID_GMAP_UGT_FEAT     BT_UUID_DECLARE_16(BT_UUID_GMAP_UGT_FEAT_VAL)

#define BT_UUID_GMAP_BGS_FEAT_VAL 0x2C03
#define BT_UUID_GMAP_BGS_FEAT     BT_UUID_DECLARE_16(BT_UUID_GMAP_BGS_FEAT_VAL)

#define BT_UUID_GMAP_BGR_FEAT_VAL 0x2C04
#define BT_UUID_GMAP_BGR_FEAT     BT_UUID_DECLARE_16(BT_UUID_GMAP_BGR_FEAT_VAL)

#define BT_UUID_HIDS_SCI_MODE_VAL 0x2C39
#define BT_UUID_HIDS_SCI_MODE BT_UUID_DECLARE_16(BT_UUID_HIDS_SCI_MODE_VAL)

#define BT_UUID_HIDS_SCI_INFO_VAL 0x2C3A
#define BT_UUID_HIDS_SCI_INFO BT_UUID_DECLARE_16(BT_UUID_HIDS_SCI_INFO_VAL)

/*
 * Protocol UUIDs
 */
#define BT_UUID_SDP_VAL               0x0001
#define BT_UUID_SDP                   BT_UUID_DECLARE_16(BT_UUID_SDP_VAL)
#define BT_UUID_UDP_VAL               0x0002
#define BT_UUID_UDP                   BT_UUID_DECLARE_16(BT_UUID_UDP_VAL)
#define BT_UUID_RFCOMM_VAL            0x0003
#define BT_UUID_RFCOMM                BT_UUID_DECLARE_16(BT_UUID_RFCOMM_VAL)
#define BT_UUID_TCP_VAL               0x0004
#define BT_UUID_TCP                   BT_UUID_DECLARE_16(BT_UUID_TCP_VAL)
#define BT_UUID_TCS_BIN_VAL           0x0005
#define BT_UUID_TCS_BIN               BT_UUID_DECLARE_16(BT_UUID_TCS_BIN_VAL)
#define BT_UUID_TCS_AT_VAL            0x0006
#define BT_UUID_TCS_AT                BT_UUID_DECLARE_16(BT_UUID_TCS_AT_VAL)
#define BT_UUID_ATT_VAL               0x0007
#define BT_UUID_ATT                   BT_UUID_DECLARE_16(BT_UUID_ATT_VAL)
#define BT_UUID_OBEX_VAL              0x0008
#define BT_UUID_OBEX                  BT_UUID_DECLARE_16(BT_UUID_OBEX_VAL)
#define BT_UUID_IP_VAL                0x0009
#define BT_UUID_IP                    BT_UUID_DECLARE_16(BT_UUID_IP_VAL)
#define BT_UUID_FTP_VAL               0x000a
#define BT_UUID_FTP                   BT_UUID_DECLARE_16(BT_UUID_FTP_VAL)
#define BT_UUID_HTTP_VAL              0x000c
#define BT_UUID_HTTP                  BT_UUID_DECLARE_16(BT_UUID_HTTP_VAL)
#define BT_UUID_WSP_VAL               0x000e
#define BT_UUID_WSP                   BT_UUID_DECLARE_16(BT_UUID_WSP_VAL)
#define BT_UUID_BNEP_VAL              0x000f
#define BT_UUID_BNEP                  BT_UUID_DECLARE_16(BT_UUID_BNEP_VAL)
#define BT_UUID_UPNP_VAL              0x0010
#define BT_UUID_UPNP                  BT_UUID_DECLARE_16(BT_UUID_UPNP_VAL)
#define BT_UUID_HIDP_VAL              0x0011
#define BT_UUID_HIDP                  BT_UUID_DECLARE_16(BT_UUID_HIDP_VAL)
#define BT_UUID_HCRP_CTRL_VAL         0x0012
#define BT_UUID_HCRP_CTRL             BT_UUID_DECLARE_16(BT_UUID_HCRP_CTRL_VAL)
#define BT_UUID_HCRP_DATA_VAL         0x0014
#define BT_UUID_HCRP_DATA             BT_UUID_DECLARE_16(BT_UUID_HCRP_DATA_VAL)
#define BT_UUID_HCRP_NOTE_VAL         0x0016
#define BT_UUID_HCRP_NOTE             BT_UUID_DECLARE_16(BT_UUID_HCRP_NOTE_VAL)
#define BT_UUID_AVCTP_VAL             0x0017
#define BT_UUID_AVCTP                 BT_UUID_DECLARE_16(BT_UUID_AVCTP_VAL)
#define BT_UUID_AVCTP_BROWSING_VAL    0x0018
#define BT_UUID_AVCTP_BROWSING        BT_UUID_DECLARE_16(BT_UUID_AVCTP_BROWSING_VAL)
#define BT_UUID_AVDTP_VAL             0x0019
#define BT_UUID_AVDTP                 BT_UUID_DECLARE_16(BT_UUID_AVDTP_VAL)
#define BT_UUID_CMTP_VAL              0x001b
#define BT_UUID_CMTP                  BT_UUID_DECLARE_16(BT_UUID_CMTP_VAL)
#define BT_UUID_UDI_VAL               0x001d
#define BT_UUID_UDI                   BT_UUID_DECLARE_16(BT_UUID_UDI_VAL)
#define BT_UUID_MCAP_CTRL_VAL         0x001e
#define BT_UUID_MCAP_CTRL             BT_UUID_DECLARE_16(BT_UUID_MCAP_CTRL_VAL)
#define BT_UUID_MCAP_DATA_VAL         0x001f
#define BT_UUID_MCAP_DATA             BT_UUID_DECLARE_16(BT_UUID_MCAP_DATA_VAL)
#define BT_UUID_L2CAP_VAL             0x0100
#define BT_UUID_L2CAP                 BT_UUID_DECLARE_16(BT_UUID_L2CAP_VAL)


int bt_uuid_cmp(const struct bt_uuid *u1, const struct bt_uuid *u2);

bool bt_uuid_create(struct bt_uuid *uuid, const uint8_t *data, uint8_t data_len);

void bt_uuid_to_str(const struct bt_uuid *uuid, char *str, size_t len);

int bt_uuid_from_str(const char *str, struct bt_uuid_any *uuid);

int bt_uuid_compress(const struct bt_uuid *src, struct bt_uuid_any *dst);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_UUID_H_ */
```

## 20.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2015-2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 5211 行

协议通用唯一标识符（Protocol UUIDs）。

### 注释 3：原第 5360 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_UUID_H_`。

## 20.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/bluetooth/byteorder.h](../byteorder_reference/P004_蓝牙字节序头文件参考.md)
- [BT_UUID_TYPE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ggabec48a57ba2d88c9e6006d9996a0fb43a8a5a0c5b6310aff10b182daec0e452ba)
- [BT_UUID_TYPE_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ggabec48a57ba2d88c9e6006d9996a0fb43a27382df27b8098bf6144021c1b23c4c8)
- [BT_UUID_TYPE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ggabec48a57ba2d88c9e6006d9996a0fb43a786cbb74a1d74c77cb31ff3c4da45517)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [type](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md#abac3a8b54416cbd89ff55f8f82902dcb)
- [bt_uuid_16](../bluetooth_connection_model_reference/P133_bt_uuid_16_结构体.md)
- [uuid](../bluetooth_connection_model_reference/P133_bt_uuid_16_结构体.md#a08f8a5e0eadf1ef2c4c917a5dd3db191)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [val](../bluetooth_connection_model_reference/P133_bt_uuid_16_结构体.md#a13ee02ec58cf5fdede249aa8b20a1a9a)
- [bt_uuid_32](../bluetooth_connection_model_reference/P134_bt_uuid_32_结构体.md)
- [uuid](../bluetooth_connection_model_reference/P134_bt_uuid_32_结构体.md#ae37fff06890b200895d559ef42d454e2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [val](../bluetooth_connection_model_reference/P134_bt_uuid_32_结构体.md#a56e991966643c9a1ca689986e57e6bfc)
- [bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)
- [uuid](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md#a3b8fd8a362ed8fd9eabcfa5bffa9eeee)
- [val](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md#a0918addaa7afaf1eeb864d5ec40bd59a)
- [BT_UUID_SIZE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga86fdce8e63c0f8208bea6b0f2584eb67)
- [bt_uuid_any](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md)
- [uuid](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md#a08fab9ce3f49d00dcb7af0cc7a7ad3af)
- [u16](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md#aea87835ffd5ee2e01bbc6674a0bc83e1)
- [u32](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md#adc9711e614e3839f6af9dd4db315dc66)
- [u128](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md#a504aec6e7e793c3de13242aef56fb833)
- [bt_uuid_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gafe17513c1f91cb3f3e61648b71620c6b)
- [bt_uuid_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9e260584efcc111eb3ee02bf78f01881)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_uuid_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gab5ef78dd2263f08de16a0f1e764df657)
- [bt_uuid_from_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga4dec477f7827ece43b91d42d75b1244b)
- [bt_uuid_compress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga72cd2ea0cc6fedded3d1eb8f617f4c07)
- [byteorder.h](../byteorder_reference/P004_蓝牙字节序头文件参考.md)
- [bt_uuid_128::val](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md#a0918addaa7afaf1eeb864d5ec40bd59a)
- [bt_uuid_128::uuid](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md#a3b8fd8a362ed8fd9eabcfa5bffa9eeee)
- [bt_uuid_16::uuid](../bluetooth_connection_model_reference/P133_bt_uuid_16_结构体.md#a08f8a5e0eadf1ef2c4c917a5dd3db191)
- [bt_uuid_16::val](../bluetooth_connection_model_reference/P133_bt_uuid_16_结构体.md#a13ee02ec58cf5fdede249aa8b20a1a9a)
- [bt_uuid_32::val](../bluetooth_connection_model_reference/P134_bt_uuid_32_结构体.md#a56e991966643c9a1ca689986e57e6bfc)
- [bt_uuid_32::uuid](../bluetooth_connection_model_reference/P134_bt_uuid_32_结构体.md#ae37fff06890b200895d559ef42d454e2)
- [bt_uuid_any::uuid](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md#a08fab9ce3f49d00dcb7af0cc7a7ad3af)
- [bt_uuid_any::u128](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md#a504aec6e7e793c3de13242aef56fb833)
- [bt_uuid_any::u32](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md#adc9711e614e3839f6af9dd4db315dc66)
- [bt_uuid_any::u16](../bluetooth_connection_model_reference/P135_bt_uuid_any_结构体.md#aea87835ffd5ee2e01bbc6674a0bc83e1)
- [bt_uuid::type](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md#abac3a8b54416cbd89ff55f8f82902dcb)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P019_bip.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P021_bq274xx.h_源码浏览.md)
