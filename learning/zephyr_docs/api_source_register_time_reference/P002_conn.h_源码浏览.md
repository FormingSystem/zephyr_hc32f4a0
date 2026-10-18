---
id: learning.zephyr-docs.api-source-register-time-reference.page-2
title: conn.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_conn.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)。

## 2.1\_原始可见代码（Source Code）

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
<a id="l00013"></a>
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
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="foldopen00140"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="foldopen00148"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="foldopen00152"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="foldopen00160"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="foldopen00172"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="foldopen00184"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="foldopen00195"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="foldopen00201"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="foldopen00206"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="foldopen00211"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00222"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="foldopen00231"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="foldopen00242"></a>
<a id="l00242"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="foldopen00277"></a>
<a id="l00277"></a>
<a id="l00284"></a>
<a id="l00291"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="foldopen00302"></a>
<a id="l00302"></a>
<a id="l00309"></a>
<a id="l00316"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="foldopen00325"></a>
<a id="l00325"></a>
<a id="l00332"></a>
<a id="l00339"></a>
<a id="l00344"></a>
<a id="l00349"></a>
<a id="l00356"></a>
<a id="l00363"></a>
<a id="l00370"></a>
<a id="l00377"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="foldopen00388"></a>
<a id="l00388"></a>
<a id="l00395"></a>
<a id="l00400"></a>
<a id="l00407"></a>
<a id="l00414"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="foldopen00425"></a>
<a id="l00425"></a>
<a id="l00430"></a>
<a id="l00432"></a>
<a id="l00434"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="foldopen00445"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="foldopen00449"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="foldopen00454"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="foldopen00464"></a>
<a id="l00464"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="foldopen00477"></a>
<a id="l00477"></a>
<a id="l00481"></a>
<a id="l00486"></a>
<a id="l00493"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="foldopen00504"></a>
<a id="l00504"></a>
<a id="l00509"></a>
<a id="l00511"></a>
<a id="l00513"></a>
<a id="l00517"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="foldopen00526"></a>
<a id="l00526"></a>
<a id="l00528"></a>
<a id="l00530"></a>
<a id="l00532"></a>
<a id="l00534"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="foldopen00541"></a>
<a id="l00541"></a>
<a id="l00543"></a>
<a id="l00545"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="foldopen00551"></a>
<a id="l00551"></a>
<a id="l00553"></a>
<a id="l00555"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="foldopen00561"></a>
<a id="l00561"></a>
<a id="l00563"></a>
<a id="l00565"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="foldopen00571"></a>
<a id="l00571"></a>
<a id="l00573"></a>
<a id="l00579"></a>
<a id="l00581"></a>
<a id="l00583"></a>
<a id="l00585"></a>
<a id="l00587"></a>
<a id="l00589"></a>
<a id="l00591"></a>
<a id="l00593"></a>
<a id="l00595"></a>
<a id="l00601"></a>
<a id="l00607"></a>
<a id="l00613"></a>
<a id="l00617"></a>
<a id="l00621"></a>
<a id="l00623"></a>
<a id="l00625"></a>
<a id="l00627"></a>
<a id="l00629"></a>
<a id="l00631"></a>
<a id="l00633"></a>
<a id="l00644"></a>
<a id="l00655"></a>
<a id="l00668"></a>
<a id="l00674"></a>
<a id="l00676"></a>
<a id="l00685"></a>
<a id="l00696"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="foldopen00707"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="foldopen00751"></a>
<a id="l00751"></a>
<a id="l00753"></a>
<a id="l00755"></a>
<a id="l00757"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="foldopen00770"></a>
<a id="l00770"></a>
<a id="l00772"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="foldopen00778"></a>
<a id="l00778"></a>
<a id="l00780"></a>
<a id="l00782"></a>
<a id="l00784"></a>
<a id="l00786"></a>
<a id="l00788"></a>
<a id="l00790"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="foldopen00796"></a>
<a id="l00796"></a>
<a id="l00798"></a>
<a id="l00800"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="foldopen00806"></a>
<a id="l00806"></a>
<a id="l00808"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="foldopen00814"></a>
<a id="l00814"></a>
<a id="l00816"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="foldopen00822"></a>
<a id="l00822"></a>
<a id="l00824"></a>
<a id="l00826"></a>
<a id="l00828"></a>
<a id="l00830"></a>
<a id="l00835"></a>
<a id="l00837"></a>
<a id="l00839"></a>
<a id="l00841"></a>
<a id="l00843"></a>
<a id="l00847"></a>
<a id="l00849"></a>
<a id="l00851"></a>
<a id="l00853"></a>
<a id="l00858"></a>
<a id="l00860"></a>
<a id="l00862"></a>
<a id="l00864"></a>
<a id="l00866"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="foldopen00876"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00879"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="foldopen00883"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="foldopen00889"></a>
<a id="l00889"></a>
<a id="l00890"></a>
<a id="l00891"></a>
<a id="l00892"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="l00899"></a>
<a id="foldopen00901"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="foldopen00913"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00922"></a>
<a id="l00928"></a>
<a id="l00934"></a>
<a id="l00943"></a>
<a id="l00951"></a>
<a id="l00953"></a>
<a id="l00967"></a>
<a id="l00974"></a>
<a id="l00981"></a>
<a id="l00984"></a>
<a id="l00987"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00997"></a>
<a id="l00998"></a>
<a id="l00999"></a>
<a id="l01011"></a>
<a id="l01012"></a>
<a id="l01021"></a>
<a id="l01022"></a>
<a id="foldopen01036"></a>
<a id="l01036"></a>
<a id="l01037"></a>
<a id="l01038"></a>
<a id="l01039"></a>
<a id="l01040"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="l01070"></a>
<a id="l01083"></a>
<a id="l01084"></a>
<a id="l01091"></a>
<a id="l01092"></a>
<a id="l01103"></a>
<a id="l01104"></a>
<a id="foldopen01106"></a>
<a id="l01106"></a>
<a id="l01108"></a>
<a id="l01112"></a>
<a id="l01114"></a>
<a id="l01116"></a>
<a id="l01118"></a>
<a id="l01119"></a>
<a id="l01120"></a>
<a id="l01125"></a>
<a id="l01128"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01132"></a>
<a id="l01133"></a>
<a id="l01134"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01141"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="l01146"></a>
<a id="l01148"></a>
<a id="l01149"></a>
<a id="l01150"></a>
<a id="l01151"></a>
<a id="l01159"></a>
<a id="l01160"></a>
<a id="l01165"></a>
<a id="l01166"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="foldopen01174"></a>
<a id="l01174"></a>
<a id="l01175"></a>
<a id="l01176"></a>
<a id="l01177"></a>
<a id="foldopen01179"></a>
<a id="l01179"></a>
<a id="l01180"></a>
<a id="l01181"></a>
<a id="l01182"></a>
<a id="l01183"></a>
<a id="l01184"></a>
<a id="l01185"></a>
<a id="l01186"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="foldopen01189"></a>
<a id="l01189"></a>
<a id="l01191"></a>
<a id="l01193"></a>
<a id="l01195"></a>
<a id="l01197"></a>
<a id="l01198"></a>
<a id="l01199"></a>
<a id="foldopen01201"></a>
<a id="l01201"></a>
<a id="l01203"></a>
<a id="l01205"></a>
<a id="l01207"></a>
<a id="l01209"></a>
<a id="l01211"></a>
<a id="l01215"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="foldopen01219"></a>
<a id="l01219"></a>
<a id="l01221"></a>
<a id="l01223"></a>
<a id="l01224"></a>
<a id="l01225"></a>
<a id="foldopen01227"></a>
<a id="l01227"></a>
<a id="l01229"></a>
<a id="l01231"></a>
<a id="l01233"></a>
<a id="l01234"></a>
<a id="l01235"></a>
<a id="foldopen01237"></a>
<a id="l01237"></a>
<a id="l01239"></a>
<a id="l01241"></a>
<a id="l01243"></a>
<a id="l01245"></a>
<a id="l01247"></a>
<a id="l01249"></a>
<a id="l01251"></a>
<a id="l01252"></a>
<a id="l01254"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01258"></a>
<a id="foldopen01260"></a>
<a id="l01260"></a>
<a id="l01261"></a>
<a id="l01263"></a>
<a id="l01264"></a>
<a id="l01265"></a>
<a id="foldopen01267"></a>
<a id="l01267"></a>
<a id="l01268"></a>
<a id="l01270"></a>
<a id="l01271"></a>
<a id="l01273"></a>
<a id="l01274"></a>
<a id="l01275"></a>
<a id="foldopen01281"></a>
<a id="l01281"></a>
<a id="l01283"></a>
<a id="l01284"></a>
<a id="l01286"></a>
<a id="l01287"></a>
<a id="l01289"></a>
<a id="l01290"></a>
<a id="l01292"></a>
<a id="l01293"></a>
<a id="l01294"></a>
<a id="l01296"></a>
<a id="l01297"></a>
<a id="l01299"></a>
<a id="l01300"></a>
<a id="l01301"></a>
<a id="l01302"></a>
<a id="foldopen01303"></a>
<a id="l01303"></a>
<a id="l01305"></a>
<a id="l01307"></a>
<a id="l01309"></a>
<a id="l01311"></a>
<a id="l01313"></a>
<a id="l01314"></a>
<a id="l01315"></a>
<a id="foldopen01317"></a>
<a id="l01317"></a>
<a id="l01318"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="l01328"></a>
<a id="l01329"></a>
<a id="l01336"></a>
<a id="l01337"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="foldopen01341"></a>
<a id="l01341"></a>
<a id="l01342"></a>
<a id="l01346"></a>
<a id="l01347"></a>
<a id="l01349"></a>
<a id="l01350"></a>
<a id="l01359"></a>
<a id="l01360"></a>
<a id="l01364"></a>
<a id="l01365"></a>
<a id="l01372"></a>
<a id="l01373"></a>
<a id="l01374"></a>
<a id="foldopen01383"></a>
<a id="l01383"></a>
<a id="l01385"></a>
<a id="l01387"></a>
<a id="l01389"></a>
<a id="l01391"></a>
<a id="l01392"></a>
<a id="l01393"></a>
<a id="l01394"></a>
<a id="l01395"></a>
<a id="l01396"></a>
<a id="l01397"></a>
<a id="foldopen01399"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01402"></a>
<a id="l01403"></a>
<a id="l01405"></a>
<a id="l01406"></a>
<a id="l01407"></a>
<a id="foldopen01411"></a>
<a id="l01411"></a>
<a id="l01413"></a>
<a id="l01415"></a>
<a id="l01417"></a>
<a id="l01419"></a>
<a id="l01423"></a>
<a id="l01424"></a>
<a id="l01425"></a>
<a id="foldopen01431"></a>
<a id="l01431"></a>
<a id="l01432"></a>
<a id="l01433"></a>
<a id="l01434"></a>
<a id="l01435"></a>
<a id="l01436"></a>
<a id="l01437"></a>
<a id="l01438"></a>
<a id="l01446"></a>
<a id="l01447"></a>
<a id="l01449"></a>
<a id="l01450"></a>
<a id="l01451"></a>
<a id="l01452"></a>
<a id="l01453"></a>
<a id="l01454"></a>
<a id="l01456"></a>
<a id="l01467"></a>
<a id="l01468"></a>
<a id="l01478"></a>
<a id="l01479"></a>
<a id="l01496"></a>
<a id="l01497"></a>
<a id="l01507"></a>
<a id="l01508"></a>
<a id="l01509"></a>
<a id="l01519"></a>
<a id="l01520"></a>
<a id="l01521"></a>
<a id="l01531"></a>
<a id="l01532"></a>
<a id="l01533"></a>
<a id="l01544"></a>
<a id="l01545"></a>
<a id="l01546"></a>
<a id="l01547"></a>
<a id="l01560"></a>
<a id="l01561"></a>
<a id="l01562"></a>
<a id="l01576"></a>
<a id="l01577"></a>
<a id="l01592"></a>
<a id="l01593"></a>
<a id="l01606"></a>
<a id="l01607"></a>
<a id="l01608"></a>
<a id="l01626"></a>
<a id="l01627"></a>
<a id="l01641"></a>
<a id="l01642"></a>
<a id="l01659"></a>
<a id="l01660"></a>
<a id="l01678"></a>
<a id="l01679"></a>
<a id="l01680"></a>
<a id="l01697"></a>
<a id="l01698"></a>
<a id="l01713"></a>
<a id="l01714"></a>
<a id="l01715"></a>
<a id="l01728"></a>
<a id="l01729"></a>
<a id="l01730"></a>
<a id="l01739"></a>
<a id="l01740"></a>
<a id="l01741"></a>
<a id="l01753"></a>
<a id="l01754"></a>
<a id="l01755"></a>
<a id="l01768"></a>
<a id="l01769"></a>
<a id="l01792"></a>
<a id="l01793"></a>
<a id="l01794"></a>
<a id="l01796"></a>
<a id="l01797"></a>
<a id="l01802"></a>
<a id="l01803"></a>
<a id="l01810"></a>
<a id="l01811"></a>
<a id="l01812"></a>
<a id="foldopen01813"></a>
<a id="l01813"></a>
<a id="l01814"></a>
<a id="l01816"></a>
<a id="l01817"></a>
<a id="l01826"></a>
<a id="l01827"></a>
<a id="l01836"></a>
<a id="l01837"></a>
<a id="l01842"></a>
<a id="l01843"></a>
<a id="l01848"></a>
<a id="l01849"></a>
<a id="l01857"></a>
<a id="l01858"></a>
<a id="l01859"></a>
<a id="foldopen01866"></a>
<a id="l01866"></a>
<a id="l01867"></a>
<a id="l01868"></a>
<a id="l01869"></a>
<a id="l01870"></a>
<a id="l01871"></a>
<a id="l01872"></a>
<a id="l01873"></a>
<a id="l01874"></a>
<a id="l01875"></a>
<a id="foldopen01882"></a>
<a id="l01882"></a>
<a id="l01883"></a>
<a id="l01884"></a>
<a id="l01885"></a>
<a id="l01886"></a>
<a id="foldopen01890"></a>
<a id="l01890"></a>
<a id="l01891"></a>
<a id="l01892"></a>
<a id="l01893"></a>
<a id="l01894"></a>
<a id="foldopen01899"></a>
<a id="l01899"></a>
<a id="l01900"></a>
<a id="l01901"></a>
<a id="l01902"></a>
<a id="l01903"></a>
<a id="l01926"></a>
<a id="l01927"></a>
<a id="l01928"></a>
<a id="l01929"></a>
<a id="l01930"></a>
<a id="foldopen01931"></a>
<a id="l01931"></a>
<a id="l01932"></a>
<a id="l01938"></a>
<a id="l01939"></a>
<a id="l01941"></a>
<a id="l01942"></a>
<a id="l01943"></a>
<a id="l01963"></a>
<a id="l01964"></a>
<a id="l01965"></a>
<a id="l01966"></a>
<a id="l01982"></a>
<a id="l01983"></a>
<a id="l01984"></a>
<a id="l01989"></a>
<a id="l01990"></a>
<a id="l02031"></a>
<a id="l02032"></a>
<a id="l02042"></a>
<a id="l02043"></a>
<a id="l02054"></a>
<a id="l02055"></a>
<a id="foldopen02056"></a>
<a id="l02056"></a>
<a id="l02058"></a>
<a id="l02059"></a>
<a id="l02061"></a>
<a id="l02062"></a>
<a id="l02064"></a>
<a id="l02065"></a>
<a id="l02067"></a>
<a id="l02068"></a>
<a id="l02070"></a>
<a id="l02071"></a>
<a id="l02073"></a>
<a id="l02074"></a>
<a id="l02076"></a>
<a id="l02077"></a>
<a id="l02079"></a>
<a id="l02080"></a>
<a id="l02082"></a>
<a id="l02083"></a>
<a id="l02085"></a>
<a id="l02086"></a>
<a id="l02087"></a>
<a id="foldopen02088"></a>
<a id="l02088"></a>
<a id="l02089"></a>
<a id="l02090"></a>
<a id="l02091"></a>
<a id="l02092"></a>
<a id="foldopen02123"></a>
<a id="l02123"></a>
<a id="l02125"></a>
<a id="l02127"></a>
<a id="l02129"></a>
<a id="l02131"></a>
<a id="l02133"></a>
<a id="l02135"></a>
<a id="l02137"></a>
<a id="l02139"></a>
<a id="l02140"></a>
<a id="l02141"></a>
<a id="foldopen02142"></a>
<a id="l02142"></a>
<a id="l02143"></a>
<a id="l02144"></a>
<a id="l02145"></a>
<a id="l02146"></a>
<a id="l02147"></a>
<a id="l02148"></a>
<a id="l02149"></a>
<a id="l02150"></a>
<a id="l02151"></a>
<a id="l02152"></a>
<a id="l02153"></a>
<a id="l02154"></a>
<a id="l02155"></a>
<a id="l02156"></a>
<a id="l02157"></a>
<a id="l02158"></a>
<a id="l02159"></a>
<a id="l02160"></a>
<a id="l02161"></a>
<a id="l02162"></a>
<a id="l02163"></a>
<a id="l02164"></a>
<a id="l02165"></a>
<a id="l02166"></a>
<a id="l02167"></a>
<a id="l02168"></a>
<a id="l02169"></a>
<a id="l02170"></a>
<a id="l02171"></a>
<a id="l02172"></a>
<a id="l02173"></a>
<a id="l02174"></a>
<a id="l02175"></a>
<a id="l02176"></a>
<a id="l02177"></a>
<a id="l02178"></a>
<a id="foldopen02180"></a>
<a id="l02180"></a>
<a id="l02181"></a>
<a id="l02190"></a>
<a id="l02191"></a>
<a id="l02192"></a>
<a id="l02201"></a>
<a id="l02202"></a>
<a id="l02212"></a>
<a id="l02213"></a>
<a id="l02214"></a>
<a id="l02223"></a>
<a id="l02224"></a>
<a id="foldopen02243"></a>
<a id="l02243"></a>
<a id="l02268"></a>
<a id="l02269"></a>
<a id="l02286"></a>
<a id="l02287"></a>
<a id="l02303"></a>
<a id="l02304"></a>
<a id="l02329"></a>
<a id="l02330"></a>
<a id="l02331"></a>
<a id="l02342"></a>
<a id="l02343"></a>
<a id="l02344"></a>
<a id="l02345"></a>
<a id="l02364"></a>
<a id="l02365"></a>
<a id="l02366"></a>
<a id="l02367"></a>
<a id="l02377"></a>
<a id="l02378"></a>
<a id="l02379"></a>
<a id="l02380"></a>
<a id="l02381"></a>
<a id="l02398"></a>
<a id="l02399"></a>
<a id="l02400"></a>
<a id="l02401"></a>
<a id="l02402"></a>
<a id="l02411"></a>
<a id="l02412"></a>
<a id="l02413"></a>
<a id="l02414"></a>
<a id="l02415"></a>
<a id="l02417"></a>
<a id="l02418"></a>
<a id="l02419"></a>
<a id="l02420"></a>
<a id="l02429"></a>
<a id="l02430"></a>
<a id="l02431"></a>
<a id="l02432"></a>
<a id="l02433"></a>
<a id="l02442"></a>
<a id="l02443"></a>
<a id="l02444"></a>
<a id="l02445"></a>
<a id="l02446"></a>
<a id="l02453"></a>
<a id="l02454"></a>
<a id="l02455"></a>
<a id="l02456"></a>
<a id="l02457"></a>
<a id="l02469"></a>
<a id="l02470"></a>
<a id="l02471"></a>
<a id="l02472"></a>
<a id="l02473"></a>
<a id="l02483"></a>
<a id="l02484"></a>
<a id="l02485"></a>
<a id="l02486"></a>
<a id="l02487"></a>
<a id="l02498"></a>
<a id="l02499"></a>
<a id="l02500"></a>
<a id="l02501"></a>
<a id="l02502"></a>
<a id="l02523"></a>
<a id="l02524"></a>
<a id="l02525"></a>
<a id="l02526"></a>
<a id="l02527"></a>
<a id="l02541"></a>
<a id="l02542"></a>
<a id="l02543"></a>
<a id="l02544"></a>
<a id="l02545"></a>
<a id="l02546"></a>
<a id="l02561"></a>
<a id="l02562"></a>
<a id="l02563"></a>
<a id="l02564"></a>
<a id="l02565"></a>
<a id="l02566"></a>
<a id="l02579"></a>
<a id="l02580"></a>
<a id="l02581"></a>
<a id="l02582"></a>
<a id="l02595"></a>
<a id="l02596"></a>
<a id="l02597"></a>
<a id="l02598"></a>
<a id="l02610"></a>
<a id="l02611"></a>
<a id="l02612"></a>
<a id="l02613"></a>
<a id="l02622"></a>
<a id="l02623"></a>
<a id="l02632"></a>
<a id="l02633"></a>
<a id="l02634"></a>
<a id="l02645"></a>
<a id="l02646"></a>
<a id="l02658"></a>
<a id="l02659"></a>
<a id="l02660"></a>
<a id="l02661"></a>
<a id="l02662"></a>
<a id="l02663"></a>
<a id="l02664"></a>
<a id="l02666"></a>
<a id="l02667"></a>
<a id="l02668"></a>
<a id="l02669"></a>
<a id="l02679"></a>
<a id="l02680"></a>
<a id="l02692"></a>
<a id="l02693"></a>
<a id="foldopen02699"></a>
<a id="l02699"></a>
<a id="l02700"></a>
<a id="l02701"></a>
<a id="l02702"></a>
<a id="l02703"></a>
<a id="l02710"></a>
<a id="l02711"></a>
<a id="l02712"></a>
<a id="foldopen02713"></a>
<a id="l02713"></a>
<a id="l02714"></a>
<a id="l02715"></a>
<a id="l02716"></a>
<a id="l02717"></a>
<a id="l02718"></a>
<a id="l02719"></a>
<a id="l02720"></a>
<a id="l02731"></a>
<a id="l02732"></a>
<a id="l02742"></a>
<a id="l02743"></a>
<a id="l02767"></a>
<a id="l02768"></a>
<a id="l02775"></a>
<a id="l02776"></a>
<a id="l02783"></a>
<a id="l02784"></a>
<a id="l02799"></a>
<a id="l02800"></a>
<a id="l02820"></a>
<a id="l02821"></a>
<a id="l02822"></a>
<a id="l02823"></a>
<a id="l02840"></a>
<a id="l02841"></a>
<a id="l02842"></a>
<a id="l02843"></a>
<a id="foldopen02845"></a>
<a id="l02845"></a>
<a id="l02847"></a>
<a id="l02849"></a>
<a id="l02850"></a>
<a id="l02852"></a>
<a id="l02853"></a>
<a id="l02854"></a>
<a id="l02855"></a>
<a id="l02857"></a>
<a id="l02859"></a>
<a id="l02861"></a>
<a id="l02862"></a>
<a id="l02864"></a>
<a id="l02865"></a>
<a id="l02867"></a>
<a id="l02868"></a>
<a id="l02870"></a>
<a id="l02871"></a>
<a id="l02872"></a>
<a id="l02873"></a>
<a id="l02874"></a>
<a id="l02875"></a>
<a id="foldopen02882"></a>
<a id="l02882"></a>
<a id="l02884"></a>
<a id="l02885"></a>
<a id="l02887"></a>
<a id="l02888"></a>
<a id="l02890"></a>
<a id="l02891"></a>
<a id="l02893"></a>
<a id="l02894"></a>
<a id="l02898"></a>
<a id="l02899"></a>
<a id="l02903"></a>
<a id="l02904"></a>
<a id="l02905"></a>
<a id="l02911"></a>
<a id="l02912"></a>
<a id="foldopen02923"></a>
<a id="l02923"></a>
<a id="l02924"></a>
<a id="l02954"></a>
<a id="l02955"></a>
<a id="l02956"></a>
<a id="l02957"></a>
<a id="l02976"></a>
<a id="l02977"></a>
<a id="l02978"></a>
<a id="l03000"></a>
<a id="l03001"></a>
<a id="l03002"></a>
<a id="l03003"></a>
<a id="l03022"></a>
<a id="l03023"></a>
<a id="l03045"></a>
<a id="l03046"></a>
<a id="l03063"></a>
<a id="l03064"></a>
<a id="l03065"></a>
<a id="l03078"></a>
<a id="l03079"></a>
<a id="l03098"></a>
<a id="l03099"></a>
<a id="l03100"></a>
<a id="l03119"></a>
<a id="l03120"></a>
<a id="l03121"></a>
<a id="l03122"></a>
<a id="l03143"></a>
<a id="l03144"></a>
<a id="l03145"></a>
<a id="l03146"></a>
<a id="foldopen03157"></a>
<a id="l03157"></a>
<a id="l03167"></a>
<a id="l03168"></a>
<a id="l03174"></a>
<a id="l03175"></a>
<a id="l03176"></a>
<a id="l03185"></a>
<a id="l03186"></a>
<a id="l03199"></a>
<a id="l03200"></a>
<a id="l03201"></a>
<a id="l03202"></a>
<a id="l03210"></a>
<a id="l03211"></a>
<a id="l03212"></a>
<a id="l03214"></a>
<a id="l03215"></a>
<a id="l03216"></a>
<a id="l03226"></a>
<a id="l03227"></a>
<a id="l03243"></a>
<a id="l03244"></a>
<a id="l03254"></a>
<a id="l03255"></a>
<a id="l03264"></a>
<a id="l03265"></a>
<a id="l03277"></a>
<a id="l03278"></a>
<a id="l03295"></a>
<a id="l03296"></a>
<a id="l03306"></a>
<a id="l03307"></a>
<a id="l03318"></a>
<a id="l03319"></a>
<a id="l03330"></a>
<a id="l03331"></a>
<a id="l03343"></a>
<a id="l03344"></a>
<a id="foldopen03346"></a>
<a id="l03346"></a>
<a id="l03347"></a>
<a id="l03348"></a>
<a id="l03349"></a>
<a id="foldopen03354"></a>
<a id="l03354"></a>
<a id="l03355"></a>
<a id="l03356"></a>
<a id="l03357"></a>
<a id="l03358"></a>
<a id="foldopen03363"></a>
<a id="l03363"></a>
<a id="l03364"></a>
<a id="l03365"></a>
<a id="l03366"></a>
<a id="l03367"></a>
<a id="l03371"></a>
<a id="l03372"></a>
<a id="l03373"></a>
<a id="l03386"></a>
<a id="l03387"></a>
<a id="l03388"></a>
<a id="l03400"></a>
<a id="l03401"></a>
<a id="l03408"></a>
<a id="l03409"></a>
<a id="l03420"></a>
<a id="l03421"></a>
<a id="l03431"></a>
<a id="l03432"></a>
<a id="l03446"></a>
<a id="l03447"></a>
<a id="l03448"></a>
<a id="l03457"></a>
<a id="l03458"></a>
<a id="l03480"></a>
<a id="l03481"></a>
<a id="l03482"></a>
<a id="l03483"></a>
<a id="l03493"></a>
<a id="l03494"></a>
<a id="l03508"></a>
<a id="l03509"></a>
<a id="l03527"></a>
<a id="l03528"></a>
<a id="l03529"></a>
<a id="l03530"></a>
<a id="l03531"></a>
<a id="l03532"></a>
<a id="l03536"></a>
<a id="l03537"></a>
<a id="aaddr_8h_html"></a>
<a id="aatomic_8h_html"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="adirection_8h_html"></a>
<a id="agap_8h_html"></a>
<a id="agroup__atomic__apis_html_ga587e3134cd8176e7b1c00361711ee2df"></a>
<a id="agroup__atomic__apis_html_gacad6866fa4c844026cd9f8c3fb60ecd7"></a>
<a id="agroup__bt__addr_html_gae0df0067c55eb4388625bb62f3d7e235"></a>
<a id="agroup__bt__conn_html_ga014db594b17a3b5d7d954e64ad8de759"></a>
<a id="agroup__bt__conn_html_ga060d51eb2208de6f805b1fc0672d2d0c"></a>
<a id="agroup__bt__conn_html_ga0843a2e0b6f16ebd132a3a512cfd27a4"></a>
<a id="agroup__bt__conn_html_ga096552403b5bcd0107f69eded772b1ee"></a>
<a id="agroup__bt__conn_html_ga0c84d5597a71fe38788a88063fd19a2d"></a>
<a id="agroup__bt__conn_html_ga0e6f6d4fdbdfc3ed75fef4a95136076f"></a>
<a id="agroup__bt__conn_html_ga0f889983cfabafe826b4feb6899b95ba"></a>
<a id="agroup__bt__conn_html_ga11ae1b656683cebe9db6a53e5166ad7a"></a>
<a id="agroup__bt__conn_html_ga14e7c852b0271781594e742ae509c5d3"></a>
<a id="agroup__bt__conn_html_ga1892ec23ca3b1818287a9d7dafc16433"></a>
<a id="agroup__bt__conn_html_ga1b02a1ce8e48ad483d73d1efd803618c"></a>
<a id="agroup__bt__conn_html_ga1bf13d2dfdbdf0a72f9b1c759ef23f60"></a>
<a id="agroup__bt__conn_html_ga1bfe349efd8a7de31e9457fe439d746a"></a>
<a id="agroup__bt__conn_html_ga2987a902da4f5cfe3671c60d154ced7e"></a>
<a id="agroup__bt__conn_html_ga2de54f2ac83f0d8dca2a85a9fbfadcaa"></a>
<a id="agroup__bt__conn_html_ga2e4188482deeda71f8e5d42a07538f31"></a>
<a id="agroup__bt__conn_html_ga2e7e836d94a5330ae01e14dbd3e29f14"></a>
<a id="agroup__bt__conn_html_ga2f757b15d1d5006ce2fa6a7a78082156"></a>
<a id="agroup__bt__conn_html_ga2f8712bbf3410de5cbe6ce489fe30e5e"></a>
<a id="agroup__bt__conn_html_ga3196a0eb1c7497e93d7c646713d2fc79"></a>
<a id="agroup__bt__conn_html_ga327444a6987b8e0b573fe758d2f75886"></a>
<a id="agroup__bt__conn_html_ga34e4837a77c7afd6999095985ddad4f0"></a>
<a id="agroup__bt__conn_html_ga3906d8d3d192e8a6ad1bf6b7acc32ff0"></a>
<a id="agroup__bt__conn_html_ga3a7741f1e884168168a09e9ec5f28c49"></a>
<a id="agroup__bt__conn_html_ga3e15b9deb6787d3e415bbea35c9aa91d"></a>
<a id="agroup__bt__conn_html_ga4002a1b092832807218afa8ad279ab98"></a>
<a id="agroup__bt__conn_html_ga4165819d12dd96e00dfa2fd6f4b95669"></a>
<a id="agroup__bt__conn_html_ga4b18c6b22a9f02be0d7d078b2ce51ff6"></a>
<a id="agroup__bt__conn_html_ga4b43ef0f30146808e560991a302e88ad"></a>
<a id="agroup__bt__conn_html_ga5568443825fc1ce9534753d8918aa813"></a>
<a id="agroup__bt__conn_html_ga57465d3a61214531ddaffc2c30939043"></a>
<a id="agroup__bt__conn_html_ga5bdf8e8efc85138d3631dc1efffc3916"></a>
<a id="agroup__bt__conn_html_ga62dc2663b4fa39a33adb76dc9a136aa4"></a>
<a id="agroup__bt__conn_html_ga6394906c6da40c9bebfaeb05de9fd5be"></a>
<a id="agroup__bt__conn_html_ga641f7f4ce7fe0641948a798881ecedcb"></a>
<a id="agroup__bt__conn_html_ga6be5f3bf064ba03dc2307fdd2b634637"></a>
<a id="agroup__bt__conn_html_ga737d8118f8aba8985292d92d0604b190"></a>
<a id="agroup__bt__conn_html_ga754ed218fe9577f2d0ef6d508cfc5a0b"></a>
<a id="agroup__bt__conn_html_ga76f872637f9b34c701c80d71ce7e585c"></a>
<a id="agroup__bt__conn_html_ga77108581b8f61485ca840e4bf7a17087"></a>
<a id="agroup__bt__conn_html_ga7c8e7a7616e7b56f97da7ff4bc0fc7ba"></a>
<a id="agroup__bt__conn_html_ga81077385583d71c248a1eb6aab9ee86e"></a>
<a id="agroup__bt__conn_html_ga8516a5304ec78362ab66a9f18968d20d"></a>
<a id="agroup__bt__conn_html_ga89e5fc4bcab3f5598d20a9cd8ace5f59"></a>
<a id="agroup__bt__conn_html_ga8a2006f6e34b20c7e8ef65a73f431a57"></a>
<a id="agroup__bt__conn_html_ga8d66f3e0262a51279e9fa8b3139252e6"></a>
<a id="agroup__bt__conn_html_ga8e54a191b889b1d5ed3e1fbb648d9bc7"></a>
<a id="agroup__bt__conn_html_ga90ae27bcc6f71f32be56efe8ecbc165d"></a>
<a id="agroup__bt__conn_html_ga910157e30fad972e8c606d1e1645603e"></a>
<a id="agroup__bt__conn_html_ga9442c1479db60e2db40a2ea6de565282"></a>
<a id="agroup__bt__conn_html_ga978770d46d7c8af854a61261c14cb892"></a>
<a id="agroup__bt__conn_html_ga98f99c893e444d1ad1ecd9139803c0b1"></a>
<a id="agroup__bt__conn_html_ga9a1dc2010c5237466de87160944630d3"></a>
<a id="agroup__bt__conn_html_ga9af26600acdf5b3a8b8ea0a32e14b497"></a>
<a id="agroup__bt__conn_html_gaa1f38911acee0534a8a6e414018c6fb6"></a>
<a id="agroup__bt__conn_html_gaa5289154bc508444f68df7abcef18aca"></a>
<a id="agroup__bt__conn_html_gaa79eada87d698f4998af876d03d7e92b"></a>
<a id="agroup__bt__conn_html_gaa9420ff489fd5857ff076406442679ff"></a>
<a id="agroup__bt__conn_html_gaa9b79cd44734c1e560d6f30509be4d0b"></a>
<a id="agroup__bt__conn_html_gaadbf6a4dba28aec90ea07b7da634e1bb"></a>
<a id="agroup__bt__conn_html_gab1aedad7da2eecc6c30acbfcdf9fbfec"></a>
<a id="agroup__bt__conn_html_gab44a964725f54ed2d37de17c6e2fd3eb"></a>
<a id="agroup__bt__conn_html_gab6c2073091d1d08032c51aadb904ea3f"></a>
<a id="agroup__bt__conn_html_gab734fbc307eff3c5bddf7c5e6ddd341b"></a>
<a id="agroup__bt__conn_html_gab7acdbdf273fc760799cf0d8cf71591c"></a>
<a id="agroup__bt__conn_html_gab8c3ecf2a3d68e54379917844a29d995"></a>
<a id="agroup__bt__conn_html_gab8dde20ae75b51f1e28dbeed06001f20"></a>
<a id="agroup__bt__conn_html_gac0dbbdb95ef868f35006622932dc8901"></a>
<a id="agroup__bt__conn_html_gac365f9748ad0737f09142ee1de982503"></a>
<a id="agroup__bt__conn_html_gac4e0bd799fc87b65367129685f57c2bd"></a>
<a id="agroup__bt__conn_html_gac6684a8089ebd495b539d661cf9fd13f"></a>
<a id="agroup__bt__conn_html_gac73a60b8b6b569b84fe17f707fa33f37"></a>
<a id="agroup__bt__conn_html_gac7bb456c530c7e08b4fa9f4d478fdaf9"></a>
<a id="agroup__bt__conn_html_gac9b111639f9b982cd97e13f313e51461"></a>
<a id="agroup__bt__conn_html_gad02f8fe587efd543c0c81cace3f63d63"></a>
<a id="agroup__bt__conn_html_gad2f90b34390e3c3697fd455ae4ef5f31"></a>
<a id="agroup__bt__conn_html_gad4aed76b80cc815f748ad0e84ae3d87c"></a>
<a id="agroup__bt__conn_html_gadcb74ad947485dd81dfd59a82d3b0db6"></a>
<a id="agroup__bt__conn_html_gae001f1268e1ff42c3c974c95dcb6735d"></a>
<a id="agroup__bt__conn_html_gae13ed81b1e7928f44b8fdf85995b3e58"></a>
<a id="agroup__bt__conn_html_gae5073b3666aff788f6f389d010a918a6"></a>
<a id="agroup__bt__conn_html_gae60f156d2aa01814ad485786e00c4ca7"></a>
<a id="agroup__bt__conn_html_gaecfaf2cb44772511dbb585de8f76f09b"></a>
<a id="agroup__bt__conn_html_gaf073384538a67c242b00150904176f66"></a>
<a id="agroup__bt__conn_html_gaf0c56cd26c4147f6c9f0faa11fa01783"></a>
<a id="agroup__bt__conn_html_gaf1aeec9b9893450423cf066a6f471824"></a>
<a id="agroup__bt__conn_html_gaf2331ec1f1222de51fc4f30566e1c52b"></a>
<a id="agroup__bt__conn_html_gaf3653de72793f775e33fd9eb04c3e7a2"></a>
<a id="agroup__bt__conn_html_gaf3d55f1f8efc630b495389ced3ee3fa5"></a>
<a id="agroup__bt__conn_html_gaf43d7aa3ad1c8d2bde8b04e650fe7b7e"></a>
<a id="agroup__bt__conn_html_gaf7849f332386f8903d35d6904f6c82b9"></a>
<a id="agroup__bt__conn_html_gafe14d64a64383b097760764697b035e2"></a>
<a id="agroup__bt__conn_html_gaff3e6aa16b68e5da7dab53289295545e"></a>
<a id="agroup__bt__conn_html_gaffd6abf9b92cc8d8463797a73b840f51"></a>
<a id="agroup__bt__conn_html_gga08eb37185a763212e65c47ab4c886ecaa42e6ff627268b9eef111375d591f9f34"></a>
<a id="agroup__bt__conn_html_gga08eb37185a763212e65c47ab4c886ecaad1d46128ba2516810af7383e850929e0"></a>
<a id="agroup__bt__conn_html_gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98"></a>
<a id="agroup__bt__conn_html_gga0e6f6d4fdbdfc3ed75fef4a95136076fa5fbcf5ba6c42da7deca9f92d6b92c968"></a>
<a id="agroup__bt__conn_html_gga0e6f6d4fdbdfc3ed75fef4a95136076fad3172d9c6319a579ee9923f3d28279f4"></a>
<a id="agroup__bt__conn_html_gga1892ec23ca3b1818287a9d7dafc16433a529c39021229684361aeb33251b2c584"></a>
<a id="agroup__bt__conn_html_gga1892ec23ca3b1818287a9d7dafc16433a9d4f71899fb3ad7212fe3f544bd55d14"></a>
<a id="agroup__bt__conn_html_gga1892ec23ca3b1818287a9d7dafc16433aaafb75f1fab71f3f1daee1db96fc44bb"></a>
<a id="agroup__bt__conn_html_gga2f757b15d1d5006ce2fa6a7a78082156a35b1c587320f31ec1c1bcfe6913c57ac"></a>
<a id="agroup__bt__conn_html_gga2f757b15d1d5006ce2fa6a7a78082156a43e2dea6e52df54423bb7a6aaabcbdbf"></a>
<a id="agroup__bt__conn_html_gga2f757b15d1d5006ce2fa6a7a78082156a78b56a5342bf31a57de235dddf5e499a"></a>
<a id="agroup__bt__conn_html_gga2f757b15d1d5006ce2fa6a7a78082156a8f5842c33912ea291388ae380e54565a"></a>
<a id="agroup__bt__conn_html_gga2f757b15d1d5006ce2fa6a7a78082156ac4f05c5aea07cfc19a606caebd7201f7"></a>
<a id="agroup__bt__conn_html_gga2f757b15d1d5006ce2fa6a7a78082156ad6df550b1f4908268752841224bbab26"></a>
<a id="agroup__bt__conn_html_gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198"></a>
<a id="agroup__bt__conn_html_gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6"></a>
<a id="agroup__bt__conn_html_gga3196a0eb1c7497e93d7c646713d2fc79a0a5f18ca51c837f9621d0212997b2ce0"></a>
<a id="agroup__bt__conn_html_gga3196a0eb1c7497e93d7c646713d2fc79a9aa1742041d4958399bb411982c3bc02"></a>
<a id="agroup__bt__conn_html_gga3196a0eb1c7497e93d7c646713d2fc79ac1ef74618cb45abd9161cd4d9141570d"></a>
<a id="agroup__bt__conn_html_gga3196a0eb1c7497e93d7c646713d2fc79ade9e8345ff7946844ba7df3e7379a886"></a>
<a id="agroup__bt__conn_html_gga3196a0eb1c7497e93d7c646713d2fc79af817bbbc221a3615da50e14c14086744"></a>
<a id="agroup__bt__conn_html_gga34e4837a77c7afd6999095985ddad4f0ab2dde3a39fba7129203fc9afc23a5bd6"></a>
<a id="agroup__bt__conn_html_gga34e4837a77c7afd6999095985ddad4f0ac0d5b6a9d1a0c02fce0472b07ec6b0f1"></a>
<a id="agroup__bt__conn_html_gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9"></a>
<a id="agroup__bt__conn_html_gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9"></a>
<a id="agroup__bt__conn_html_gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b"></a>
<a id="agroup__bt__conn_html_gga5568443825fc1ce9534753d8918aa813ab79f96814227514fe5aeeee21a219741"></a>
<a id="agroup__bt__conn_html_gga5568443825fc1ce9534753d8918aa813acd51ea3eb01cb91c9fda392af42bcd2d"></a>
<a id="agroup__bt__conn_html_gga5568443825fc1ce9534753d8918aa813af50e6d16f23f5b12e41a9c6fce8716db"></a>
<a id="agroup__bt__conn_html_gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529"></a>
<a id="agroup__bt__conn_html_gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1"></a>
<a id="agroup__bt__conn_html_gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da"></a>
<a id="agroup__bt__conn_html_gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6"></a>
<a id="agroup__bt__conn_html_gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8"></a>
<a id="agroup__bt__conn_html_gga6394906c6da40c9bebfaeb05de9fd5bea30b6d4dc4a32556cedd61ed1bbfbf12c"></a>
<a id="agroup__bt__conn_html_gga6394906c6da40c9bebfaeb05de9fd5bea30c5743ef2b358390fd93bd775f72bc3"></a>
<a id="agroup__bt__conn_html_gga6394906c6da40c9bebfaeb05de9fd5bea938fcb8be6a45efce064c881bc668f8d"></a>
<a id="agroup__bt__conn_html_gga6394906c6da40c9bebfaeb05de9fd5beabaafdce9a596454fe4f23c50afba2ddd"></a>
<a id="agroup__bt__conn_html_gga6394906c6da40c9bebfaeb05de9fd5beabacfa9f390d61d7471c81669bcc0243d"></a>
<a id="agroup__bt__conn_html_gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a"></a>
<a id="agroup__bt__conn_html_gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296"></a>
<a id="agroup__bt__conn_html_gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2"></a>
<a id="agroup__bt__conn_html_gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046"></a>
<a id="agroup__bt__conn_html_gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800"></a>
<a id="agroup__bt__conn_html_gga8e54a191b889b1d5ed3e1fbb648d9bc7a5943689e3233bc87054dbd9f54042202"></a>
<a id="agroup__bt__conn_html_gga8e54a191b889b1d5ed3e1fbb648d9bc7a900282c089ca30323171da1a0e0e0146"></a>
<a id="agroup__bt__conn_html_gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd"></a>
<a id="agroup__bt__conn_html_gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f"></a>
<a id="agroup__bt__conn_html_gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587"></a>
<a id="agroup__bt__conn_html_gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f"></a>
<a id="agroup__bt__conn_html_gga9a1dc2010c5237466de87160944630d3a0ff236987e96f368c09944a9074f8f7b"></a>
<a id="agroup__bt__conn_html_gga9a1dc2010c5237466de87160944630d3a17689e9502318b16c35a4792ecc6e73f"></a>
<a id="agroup__bt__conn_html_gga9a1dc2010c5237466de87160944630d3a295b2e0d0fff2ea730a00e7916065b82"></a>
<a id="agroup__bt__conn_html_gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0"></a>
<a id="agroup__bt__conn_html_gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30"></a>
<a id="agroup__bt__conn_html_ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7"></a>
<a id="agroup__bt__conn_html_ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae"></a>
<a id="agroup__bt__conn_html_ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216"></a>
<a id="agroup__bt__conn_html_ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242"></a>
<a id="agroup__bt__conn_html_ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5"></a>
<a id="agroup__bt__conn_html_ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6"></a>
<a id="agroup__bt__conn_html_ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7"></a>
<a id="agroup__bt__conn_html_ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171"></a>
<a id="agroup__bt__conn_html_ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05"></a>
<a id="agroup__bt__conn_html_ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f"></a>
<a id="agroup__bt__conn_html_ggaadbf6a4dba28aec90ea07b7da634e1bba4ff9aa9e9c41dbdc288360d354775e95"></a>
<a id="agroup__bt__conn_html_ggaadbf6a4dba28aec90ea07b7da634e1bbaa0fc3809d1d71f4fdfe632ffe0a57cd6"></a>
<a id="agroup__bt__conn_html_ggaadbf6a4dba28aec90ea07b7da634e1bbaba211d71eb3eccecb93b8e5b4e956e7b"></a>
<a id="agroup__bt__conn_html_ggab7acdbdf273fc760799cf0d8cf71591ca3bdbab03ae31a6340a10066476e9edac"></a>
<a id="agroup__bt__conn_html_ggab7acdbdf273fc760799cf0d8cf71591ca5745021b56f9da077db312f104e855b2"></a>
<a id="agroup__bt__conn_html_ggab7acdbdf273fc760799cf0d8cf71591ca6908e64a2774e0ddeca4b510ee56de33"></a>
<a id="agroup__bt__conn_html_ggab7acdbdf273fc760799cf0d8cf71591ca9253d001290986ae07a262260a01fafb"></a>
<a id="agroup__bt__conn_html_ggab7acdbdf273fc760799cf0d8cf71591ca92ac9a31531c26a23bd1b268e68815ba"></a>
<a id="agroup__bt__conn_html_ggab7acdbdf273fc760799cf0d8cf71591ca957116fdc29742ec8e75284bbaa726b7"></a>
<a id="agroup__bt__conn_html_ggab7acdbdf273fc760799cf0d8cf71591cabc273bf65c87ff09f72f85e8f0160bb7"></a>
<a id="agroup__bt__conn_html_ggab7acdbdf273fc760799cf0d8cf71591caeb8a8776c0e54eada45de6a45f6ee1ea"></a>
<a id="agroup__bt__conn_html_ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2"></a>
<a id="agroup__bt__conn_html_ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836"></a>
<a id="agroup__bt__conn_html_ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6"></a>
<a id="agroup__bt__conn_html_ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee"></a>
<a id="agroup__bt__conn_html_ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953"></a>
<a id="agroup__bt__conn_html_ggae60f156d2aa01814ad485786e00c4ca7a8ce5e76ef31654408105b5505f63a4c4"></a>
<a id="agroup__bt__conn_html_ggae60f156d2aa01814ad485786e00c4ca7a9fae7a5909e7c6974361ab71be717495"></a>
<a id="agroup__bt__conn_html_ggae60f156d2aa01814ad485786e00c4ca7aabb0edb792a8fbfe91f8a8847672b67c"></a>
<a id="agroup__bt__conn_html_ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81"></a>
<a id="agroup__bt__conn_html_ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e"></a>
<a id="agroup__bt__conn_html_ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631"></a>
<a id="agroup__bt__conn_html_ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae"></a>
<a id="agroup__bt__conn_html_ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b"></a>
<a id="agroup__bt__conn_html_ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a"></a>
<a id="agroup__bt__conn_html_ggaf2331ec1f1222de51fc4f30566e1c52ba1235210de336af7cac9777d2f91408ea"></a>
<a id="agroup__bt__conn_html_ggaf2331ec1f1222de51fc4f30566e1c52ba5ddc8d83fa6f143b985bd2f891018622"></a>
<a id="agroup__bt__conn_html_ggaf3653de72793f775e33fd9eb04c3e7a2a35ab078fac9e0ef608ca87c2a3db63ac"></a>
<a id="agroup__bt__conn_html_ggaf3653de72793f775e33fd9eb04c3e7a2aa24f08ba114af2ac928087527d514c83"></a>
<a id="agroup__bt__conn_html_ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea06bd101d7cc98d39403ed16719542dec"></a>
<a id="agroup__bt__conn_html_ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea17765999979bb1bac00769ea742d53d8"></a>
<a id="agroup__bt__conn_html_ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea19fd0c4702ca5e08c8cbfb51b34bb705"></a>
<a id="agroup__bt__conn_html_ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea684ce653c5fffe9d49316d22904d3942"></a>
<a id="agroup__bt__conn_html_ggafe14d64a64383b097760764697b035e2a288abc3e9a886eb3ab2b8f32c7913d94"></a>
<a id="agroup__bt__conn_html_ggafe14d64a64383b097760764697b035e2a788566d99b00e42f48aceb7d7c0229e6"></a>
<a id="agroup__bt__conn_html_ggafe14d64a64383b097760764697b035e2af81e06eb920435cc68ccfa3ee6cee34a"></a>
<a id="agroup__bt__conn_html_ggaffd6abf9b92cc8d8463797a73b840f51a243bb67b834cda207b61cc7ea65bdab2"></a>
<a id="agroup__bt__conn_html_ggaffd6abf9b92cc8d8463797a73b840f51a6350cf2f1d91e496ec49ddd09f7044fc"></a>
<a id="agroup__bt__conn_html_ggaffd6abf9b92cc8d8463797a73b840f51a8edae9d98c26da94ec152fa1f1f690f5"></a>
<a id="agroup__bt__conn_html_ggaffd6abf9b92cc8d8463797a73b840f51aa9b85139381d29cdfb6adb756544e088"></a>
<a id="agroup__bt__conn_html_ggaffd6abf9b92cc8d8463797a73b840f51ab0d60b2e7e26ab862df16d926fc2198f"></a>
<a id="agroup__bt__conn_html_ggaffd6abf9b92cc8d8463797a73b840f51ac05977c1622cc7383a1035a63b33ecad"></a>
<a id="agroup__bt__conn_html_ggaffd6abf9b92cc8d8463797a73b840f51ae14f994d1c3329695d0257caffd20f91"></a>
<a id="agroup__bt__gap_html_gaad0039d4b524a0eef31158dc9b24a497"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="ahci__types_8h_html"></a>
<a id="ahci__types_8h_html_a056a67d663cfdc2189b480fc79946c74"></a>
<a id="ahci__types_8h_html_a076869aba2dc8593b2263c642cdaa148"></a>
<a id="ahci__types_8h_html_a095b6061c31229b951b6b96e5d02381f"></a>
<a id="ahci__types_8h_html_a1e92177f7be3c6a6be00f97fbfc17dcf"></a>
<a id="ahci__types_8h_html_a1fe5e94fbd1156c8196c8e1ab9816bac"></a>
<a id="ahci__types_8h_html_a219243d501bbcb6d62668398cde79fca"></a>
<a id="ahci__types_8h_html_a21eb191c5d99f902c7a244cad685995f"></a>
<a id="ahci__types_8h_html_a31cb520a05fe31313bacf8b021da468c"></a>
<a id="ahci__types_8h_html_a3e01bbe3a72c946015a288ee49d3cbdd"></a>
<a id="ahci__types_8h_html_a41bbe08db99fb0a2ef77f4f3103f9b6c"></a>
<a id="ahci__types_8h_html_a45ff3a04cd0179ed02576136114ed8c0"></a>
<a id="ahci__types_8h_html_a4a88120ae7e83fd791012c913315d14f"></a>
<a id="ahci__types_8h_html_a4b48c199b6b75e9dd62ec36883b40aa4"></a>
<a id="ahci__types_8h_html_a4c7ff3c949023f4544bf50353a0f082b"></a>
<a id="ahci__types_8h_html_a5b082fa5b8ba11a651468cc516d067fe"></a>
<a id="ahci__types_8h_html_a5d2af0ed5e0cc5cf7d9f0baae512ff68"></a>
<a id="ahci__types_8h_html_a6dc3f766ce40bbd0ddb7af3cf85677b1"></a>
<a id="ahci__types_8h_html_a714152a085bbc317b539d6e973ccffc6"></a>
<a id="ahci__types_8h_html_a73cbfe2a942b684ac0b5b50d900fb83f"></a>
<a id="ahci__types_8h_html_a759eb7a8e43ee7cf1ea88ddd3e69feb5"></a>
<a id="ahci__types_8h_html_a76d1452003c0bd3b688765aa2d25047f"></a>
<a id="ahci__types_8h_html_a77d27762b9faa7743a55d822a1839eac"></a>
<a id="ahci__types_8h_html_a77e56fd5302673f6ef295c0cceabdc9f"></a>
<a id="ahci__types_8h_html_a7baf90f5bf691ce6b650677e6c2a9600"></a>
<a id="ahci__types_8h_html_a821a29dacea9867e4e576f916cf7be3d"></a>
<a id="ahci__types_8h_html_a92e1ec21014999f40172fa1812c36575"></a>
<a id="ahci__types_8h_html_aa2ae18252a20ef3481d2402f8924cdda"></a>
<a id="ahci__types_8h_html_aa60f64ff7259fd79fb1da2c063530348"></a>
<a id="ahci__types_8h_html_ab30a4e55002080394c39fb885eba36e4"></a>
<a id="ahci__types_8h_html_ab88f3d713f6862c08b73752436ca8b1b"></a>
<a id="ahci__types_8h_html_abe4efee7cf9371129f4b5bd650b0d64a"></a>
<a id="ahci__types_8h_html_abfdca3ae615e19c8e24c098ba8349618"></a>
<a id="ahci__types_8h_html_ac34716156b071e06eb454f091a63216c"></a>
<a id="ahci__types_8h_html_ac4817c265c50019d8f74146f7477bf58"></a>
<a id="ahci__types_8h_html_acabccf9f5893324dcb6acc0769ab8417"></a>
<a id="ahci__types_8h_html_acb1d2b1b3e2e1802b81dbeb82bcc9f12"></a>
<a id="ahci__types_8h_html_acd33fc2eb3f5ebe10cbe4c5060f8336b"></a>
<a id="ahci__types_8h_html_ace872d54fba6d94d62b59a2373c7d0d5"></a>
<a id="ahci__types_8h_html_ad09c735ab352d7a546cade296e915e85"></a>
<a id="ahci__types_8h_html_ad980d8f134d940b80dc9b0e3a570ac06"></a>
<a id="ahci__types_8h_html_ada09c787fca0a1d54bb754635489b51e"></a>
<a id="ahci__types_8h_html_ae49d35db87532e06ea685a63eb89177a"></a>
<a id="ahci__types_8h_html_ae8446a2638bd4009b7dee725bb54c883"></a>
<a id="ahci__types_8h_html_aee251ce3c46dc0404d880be7d4550fa6"></a>
<a id="ahci__types_8h_html_af057e8492e52d0c8763d4a2e969d949d"></a>
<a id="ahci__types_8h_html_af16c4c79e602e6da833b8aa3e0c4bf64"></a>
<a id="ahci__types_8h_html_af17f867204bc7cf99e5d530c39302be0"></a>
<a id="ahci__types_8h_html_af1907f8ae481a08c674d86e689826f49"></a>
<a id="ahci__types_8h_html_af1b7924e50ba017e59d697fd8814d491"></a>
<a id="ahci__types_8h_html_af7cc15be8165315ee0358ebb517b5e33"></a>
<a id="ahci__types_8h_html_aff1538e314a97aa4910d4f7066dc4d55"></a>
<a id="anet__buf_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructbt__addr__le__t_html"></a>
<a id="astructbt__addr__t_html"></a>
<a id="astructbt__br__conn__param_html"></a>
<a id="astructbt__br__conn__param_html_a95454a74932a14b4137c3fe82821be49"></a>
<a id="astructbt__conn__auth__cb_html"></a>
<a id="astructbt__conn__auth__cb_html_a10f9d22c89c95a6f3ffe0016f92445c0"></a>
<a id="astructbt__conn__auth__cb_html_a14074ca97fad6af4c58c43a00c503104"></a>
<a id="astructbt__conn__auth__cb_html_a1be006307d1c9b6b13b4d35024f130e5"></a>
<a id="astructbt__conn__auth__cb_html_a2bb6c10666d111f675fd6de5ff51410a"></a>
<a id="astructbt__conn__auth__cb_html_a92391a172e158a42966f410d732424a7"></a>
<a id="astructbt__conn__auth__cb_html_ab6df1b1505dc22dd8dae0e946546c8bb"></a>
<a id="astructbt__conn__auth__cb_html_aec9f6256607ea2cd1ce1b4cdb3052b42"></a>
<a id="astructbt__conn__auth__cb_html_af4f7d3ee570b3472ee79b014be01f76e"></a>
<a id="astructbt__conn__auth__cb_html_af6eb01c252ba3e32ff8bf583aa6ca0a4"></a>
<a id="astructbt__conn__auth__cb_html_af736a8808504fce22b95131818bad450"></a>
<a id="astructbt__conn__auth__info__cb_html"></a>
<a id="astructbt__conn__auth__info__cb_html_a44896258f0221d4f0a55cc1fb785b06c"></a>
<a id="astructbt__conn__auth__info__cb_html_ae7228bb82889eacebf67e1d4b3b23375"></a>
<a id="astructbt__conn__auth__info__cb_html_aea737700f2760de1ed26a721b5e860d2"></a>
<a id="astructbt__conn__auth__info__cb_html_af20b0d7fc5fd8399ad9368b3ef7067f8"></a>
<a id="astructbt__conn__auth__info__cb_html_afcb8dae77f7b4df3ed0741de65f7f5d0"></a>
<a id="astructbt__conn__auth__info__cb_html_afde62f2cdfb40b4154208f3c1c3dadc1"></a>
<a id="astructbt__conn__br__cb_html"></a>
<a id="astructbt__conn__br__cb_html_a37af27d6d6d0e767dd439f24ff999c28"></a>
<a id="astructbt__conn__br__cb_html_a93be2950207ea20c02b66647f5335273"></a>
<a id="astructbt__conn__br__cb_html_aa278e529ac45aab63586b2566e857057"></a>
<a id="astructbt__conn__br__info_html"></a>
<a id="astructbt__conn__br__info_html_aeef49f711872ccfec5dd558c4552b71e"></a>
<a id="astructbt__conn__br__remote__info_html"></a>
<a id="astructbt__conn__br__remote__info_html_a798c179c803e709182a1b0c3594f4a0a"></a>
<a id="astructbt__conn__br__remote__info_html_afa19f7db400bb0de234e8cda61f3deaf"></a>
<a id="astructbt__conn__cb_html"></a>
<a id="astructbt__conn__cb_html_a01582ed3e3801e10c665534eaa991454"></a>
<a id="astructbt__conn__cb_html_a016b5f28c5d7187991905abc71d09656"></a>
<a id="astructbt__conn__cb_html_a0dd4f406a0807014794470b2f33a0cea"></a>
<a id="astructbt__conn__cb_html_a1142d1861cc0b0058f68ecf537d0cec3"></a>
<a id="astructbt__conn__cb_html_a11b357037d6e3bdf99be7d3649a876d4"></a>
<a id="astructbt__conn__cb_html_a1818aa00a45e807872e732e1fdfddc2c"></a>
<a id="astructbt__conn__cb_html_a1bd8d99988ad0ae3f79aad3d03fcbd8b"></a>
<a id="astructbt__conn__cb_html_a2179943b5f64302e38c64f075a5b6a9e"></a>
<a id="astructbt__conn__cb_html_a274d375b999d46854a691990fb58d90b"></a>
<a id="astructbt__conn__cb_html_a2c52c2e2798062708c373fae9610fadd"></a>
<a id="astructbt__conn__cb_html_a32949bf4b5d8cc44f0887c3022df0023"></a>
<a id="astructbt__conn__cb_html_a39d8ed2cf68be3b029bd269be71b448a"></a>
<a id="astructbt__conn__cb_html_a73d18565f1510a0adaa2b1f4d2278f2f"></a>
<a id="astructbt__conn__cb_html_a8b8983b5b5b05c9e2dae242485b6c914"></a>
<a id="astructbt__conn__cb_html_a8bde5cae151fa9ba79a7bf91c8901f5f"></a>
<a id="astructbt__conn__cb_html_a95af0f47a531b9ec02bb2ec4a26a2017"></a>
<a id="astructbt__conn__cb_html_a9cbc0e6b91fc2742c59815b676875235"></a>
<a id="astructbt__conn__cb_html_ab3618150bfeea9492095ba27ce978c69"></a>
<a id="astructbt__conn__cb_html_abc6a0c4846d52d040b671b4f9f505755"></a>
<a id="astructbt__conn__cb_html_ac20a741bc56068addc9fad442281a493"></a>
<a id="astructbt__conn__cb_html_ae02a23d823954a747f8f474fb19276d7"></a>
<a id="astructbt__conn__cb_html_ae454d5bc2664e90ba2b1e0c867db374e"></a>
<a id="astructbt__conn__cb_html_ae79d3b27e75e4c49575d70ff1a860589"></a>
<a id="astructbt__conn__cb_html_aea9b62ab1a1469be97a207a8e07d2f14"></a>
<a id="astructbt__conn__cb_html_af726f004c06b86f770ece263ed6c9ca4"></a>
<a id="astructbt__conn__cb_html_aff02fd2cc1fd90640d0b9ce2e7440202"></a>
<a id="astructbt__conn__info_html"></a>
<a id="astructbt__conn__info_html_a3a4e24519b5d3ba547423e53c4d92a5c"></a>
<a id="astructbt__conn__info_html_a6b536e7732dcf7b77a7bc05116dca548"></a>
<a id="astructbt__conn__info_html_a7995e1291be494b5bdf860eceea0cad1"></a>
<a id="astructbt__conn__info_html_a799e59d3a85625799a32ac3f0b3d67d1"></a>
<a id="astructbt__conn__info_html_a8237b8c1bb9a97a174d04cbe13dca7c7"></a>
<a id="astructbt__conn__info_html_ad622c69f262ee53ec94918857250a2a0"></a>
<a id="astructbt__conn__info_html_ae4405f1b4f3fe2ff6253453964860931"></a>
<a id="astructbt__conn__info_html_ae566e2382b69ff27314dc1dd632dbdbc"></a>
<a id="astructbt__conn__le__conn__rate__changed_html"></a>
<a id="astructbt__conn__le__conn__rate__changed_html_a348cc25c2f19bab8c5e140b712b3034a"></a>
<a id="astructbt__conn__le__conn__rate__changed_html_a47d662c1e00e8c4e1a553d9a4909f6df"></a>
<a id="astructbt__conn__le__conn__rate__changed_html_a768af259e8d37f463278946bd660ce58"></a>
<a id="astructbt__conn__le__conn__rate__changed_html_aa6dfef1425c47823897b8b84de17ecf9"></a>
<a id="astructbt__conn__le__conn__rate__changed_html_ab2b60e61438b0d814c9a8a8adcae35fc"></a>
<a id="astructbt__conn__le__conn__rate__param_html"></a>
<a id="astructbt__conn__le__conn__rate__param_html_a264baeb210c9cbd559f0cd3ed2cd78b1"></a>
<a id="astructbt__conn__le__conn__rate__param_html_a50a3c9eca10ed5c11773aaf07e1fbc12"></a>
<a id="astructbt__conn__le__conn__rate__param_html_a751042149cb8ff1ec28de10fe1e4c8bd"></a>
<a id="astructbt__conn__le__conn__rate__param_html_a9afcc899991204f17c1390b9362ec54b"></a>
<a id="astructbt__conn__le__conn__rate__param_html_aa764837e74aac1feba2025cf01a87d85"></a>
<a id="astructbt__conn__le__conn__rate__param_html_adf4c1069b5aa3b8afb09ea8b59d93eca"></a>
<a id="astructbt__conn__le__conn__rate__param_html_ae4734b6d8f0f4903624e47e975828482"></a>
<a id="astructbt__conn__le__conn__rate__param_html_aed9238960e4be8ddbeff53afab74ef6f"></a>
<a id="astructbt__conn__le__conn__rate__param_html_afb3fa1a4202c39a9551dd41396595771"></a>
<a id="astructbt__conn__le__create__param_html"></a>
<a id="astructbt__conn__le__create__param_html_a2bc978ac97435fe5f87c6e01692f2910"></a>
<a id="astructbt__conn__le__create__param_html_a339b99f65c5029ada6cdf453ab1f258e"></a>
<a id="astructbt__conn__le__create__param_html_a4b1e26c0976d9c900b831c886c77b055"></a>
<a id="astructbt__conn__le__create__param_html_a59f05bfb9468779d02f8d0beeb7a35c1"></a>
<a id="astructbt__conn__le__create__param_html_a5cfae677f924534dc5bc7b38c457a7af"></a>
<a id="astructbt__conn__le__create__param_html_ae62491837d35d95e32016b793edf8c96"></a>
<a id="astructbt__conn__le__create__synced__param_html"></a>
<a id="astructbt__conn__le__create__synced__param_html_ac5872dda4042e3ba6c161dce60784b70"></a>
<a id="astructbt__conn__le__create__synced__param_html_ac7b4e4144aaf914bdef1dc305b5e297f"></a>
<a id="astructbt__conn__le__cs__capabilities_html"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a090f869cfe7e39a70cea94afbd5ac376"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a1a0076a0c97317803976f4aca86afc0d"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a1ff1d7d769e3ba915f91bf672a6f8a61"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a21262b0e588a75146f2d0c325d0b5cc1"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a22604c052da2f8ccf77c81a0a5c628b7"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a345d9e43222d77024a8f4283b274b48f"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a3fd09db5fae9c5e307994a78131199c6"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a46c9168328d3fbc98a2625799c733818"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a4e4c56c5066d02b2a0cd59c067f1e4b9"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a5a86629a5ad4203b5efe3802cd8b6ae7"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a6513d8ffe7d168441205f6dd656dcbbc"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a6530d2a3fb66d498711856b723acecb7"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a694119619d359d0b7e298edf6201ee20"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a6e92391b21d4acaebba8a171643f572f"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a77aacfd02b354e04d4cc29cc1bf4b779"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a7f35343a1572800850e791ba3ff5ffb1"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a94fd00a7a9b22d649f75c7fdd17590a9"></a>
<a id="astructbt__conn__le__cs__capabilities_html_a97b42928bcba43a6d90e8139efce0870"></a>
<a id="astructbt__conn__le__cs__capabilities_html_aa1616417e6183cf283cf96efc9a92b8e"></a>
<a id="astructbt__conn__le__cs__capabilities_html_aba0db15183d4fa4ae0e3f1333202e55e"></a>
<a id="astructbt__conn__le__cs__capabilities_html_abbefdc0268a775712c7abd664adcb6b2"></a>
<a id="astructbt__conn__le__cs__capabilities_html_abe3c611316bb5f710f355846ee9ec437"></a>
<a id="astructbt__conn__le__cs__capabilities_html_ac842e123166008ad1ad663f827937a3b"></a>
<a id="astructbt__conn__le__cs__capabilities_html_acef0d65ed55ae304fea47006bfb0076f"></a>
<a id="astructbt__conn__le__cs__capabilities_html_ad57f15b4dda88e2b747f30451601c923"></a>
<a id="astructbt__conn__le__cs__capabilities_html_ad58deea7a825bb5f0bc2ca0034183948"></a>
<a id="astructbt__conn__le__cs__capabilities_html_adfac38e7771604971a82ece149c1d337"></a>
<a id="astructbt__conn__le__cs__capabilities_html_ae76fbc0f88525e83717e1d8ef5acae59"></a>
<a id="astructbt__conn__le__cs__capabilities_html_ae93594f360430e9c0c80cf3edcf570f6"></a>
<a id="astructbt__conn__le__cs__config_html"></a>
<a id="astructbt__conn__le__cs__config_html_a194e3844373c57e714917d03ac82666d"></a>
<a id="astructbt__conn__le__cs__config_html_a2051f559b41085c4b41743aaaaecf3a1"></a>
<a id="astructbt__conn__le__cs__config_html_a29912bd291fa4da09bb5b196d747ca6b"></a>
<a id="astructbt__conn__le__cs__config_html_a2e59fb17cd932b7670b3e915684c2107"></a>
<a id="astructbt__conn__le__cs__config_html_a2e904438c579870ed96b5dccff239c18"></a>
<a id="astructbt__conn__le__cs__config_html_a60f9d21629554d47556d0fe8d63dcae3"></a>
<a id="astructbt__conn__le__cs__config_html_a63b7027929a5c3ec7fd68f35343262ee"></a>
<a id="astructbt__conn__le__cs__config_html_a8e650b50400a45040c02a88dfb30683c"></a>
<a id="astructbt__conn__le__cs__config_html_a8eea68bffef759b4532b68a1ecbdd4f1"></a>
<a id="astructbt__conn__le__cs__config_html_a971ff7ba734dd71512af7f3850de364d"></a>
<a id="astructbt__conn__le__cs__config_html_a9b64ecb0986e7e9995c29feaf105eeaa"></a>
<a id="astructbt__conn__le__cs__config_html_aab9a1d8d09d7a439f1c4dd28b9dd05c4"></a>
<a id="astructbt__conn__le__cs__config_html_aaf8f1ce04fd22b4ca4728bdcfce8bd4a"></a>
<a id="astructbt__conn__le__cs__config_html_ab59b31730b91f843e5b8a156d98da42d"></a>
<a id="astructbt__conn__le__cs__config_html_acfccd404abced1c5f5490130f2f77f23"></a>
<a id="astructbt__conn__le__cs__config_html_ad11f8bee028ad3eb59008d46dce2d5bd"></a>
<a id="astructbt__conn__le__cs__config_html_ae7f1cc232df00b4543fdb2b2596b9bbf"></a>
<a id="astructbt__conn__le__cs__config_html_afa2846689f1a9d5b9e124b1c9095154f"></a>
<a id="astructbt__conn__le__cs__config_html_aff70b37fac8a3bd94acb25d7bd06989b"></a>
<a id="astructbt__conn__le__cs__fae__table_html"></a>
<a id="astructbt__conn__le__cs__fae__table_html_a9d4a2fe09edc897143b6e479f30b7f65"></a>
<a id="astructbt__conn__le__cs__procedure__enable__complete_html"></a>
<a id="astructbt__conn__le__cs__procedure__enable__complete_html_a2e290c25ec5af8b0259d45f04d6c543d"></a>
<a id="astructbt__conn__le__cs__procedure__enable__complete_html_a3fa8ad4dd264eb4e2489dea9c1048d22"></a>
<a id="astructbt__conn__le__cs__procedure__enable__complete_html_a40b03220932852b6b51d65f557c21f17"></a>
<a id="astructbt__conn__le__cs__procedure__enable__complete_html_a4129ab9519ba140ffb198aa9a5cde6ac"></a>
<a id="astructbt__conn__le__cs__procedure__enable__complete_html_a77a2bd8ee384c4567321a09f6b64782c"></a>
<a id="astructbt__conn__le__cs__procedure__enable__complete_html_a8511deef97f19c53ddaa4dec8492658f"></a>
<a id="astructbt__conn__le__cs__procedure__enable__complete_html_ab83778fe2d1274e5658fd5f5f867314f"></a>
<a id="astructbt__conn__le__cs__procedure__enable__complete_html_acc1d12d347e1b02b2eea562ea064a40b"></a>
<a id="astructbt__conn__le__cs__procedure__enable__complete_html_ad71825d71ab89baea138e41f9a3ff57e"></a>
<a id="astructbt__conn__le__cs__procedure__enable__complete_html_ae990a10c468ec62fbaf9325c94733c7c"></a>
<a id="astructbt__conn__le__cs__procedure__enable__complete_html_aeb918e438cd02296c7f693757268f6bf"></a>
<a id="astructbt__conn__le__cs__subevent__result_html"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_a0f8fc918f8eb31c47acf51885c7add08"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_a1a90563a8c93f9b309e88fd771a7cec4"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_a3597697ae4acdd8f7c009bececab6a65"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_a3bffc0935a5410d75d0050337e4fad27"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_a45b22c6c2252e2afa28ee8b1bfed3ecf"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_a6948c4a8c5882cb1d1b04a2b390fda8c"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_a7706d0dfd7246d4cf193a8a9e7b6305d"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_a778c89f57ef50f612654243ba673ba3f"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_a967d37f37d0e1596984fdda34609a3b3"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_a9bfcc6dcaa191c7f56958ef88926b51e"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_aa4c770ab2db8d4ab665ad50f7edd5bfa"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_acbfc5e80a2fb82072d9376e996f7969f"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_adf60893d9229003d1eefc552a4957b65"></a>
<a id="astructbt__conn__le__cs__subevent__result_html_aef5ba53497c4d1576c9ecec1b5dea289"></a>
<a id="astructbt__conn__le__data__len__info_html"></a>
<a id="astructbt__conn__le__data__len__info_html_a14288429cbbcce2ef34580a581815eb7"></a>
<a id="astructbt__conn__le__data__len__info_html_a18ddc603e922586e331187c9b29f2908"></a>
<a id="astructbt__conn__le__data__len__info_html_a48d175f3c4b03dbdee129feae3edab23"></a>
<a id="astructbt__conn__le__data__len__info_html_af2316cdc921e9ec19491501e15248f73"></a>
<a id="astructbt__conn__le__data__len__param_html"></a>
<a id="astructbt__conn__le__data__len__param_html_a8b279a0dc72c70aaf5205558fd4b4c4a"></a>
<a id="astructbt__conn__le__data__len__param_html_a9046542952fa822b944602b398562e6e"></a>
<a id="astructbt__conn__le__frame__space__update__param_html"></a>
<a id="astructbt__conn__le__frame__space__update__param_html_a1e5bd6b331c1c7c4881e2875b1adfd3d"></a>
<a id="astructbt__conn__le__frame__space__update__param_html_a67adb4f731d9a1822b400af9f30bcf43"></a>
<a id="astructbt__conn__le__frame__space__update__param_html_a7d3f1ee0c43797ab100b24c3919f304f"></a>
<a id="astructbt__conn__le__frame__space__update__param_html_a90e83dca82b557ef1476d5e4919fb170"></a>
<a id="astructbt__conn__le__frame__space__updated_html"></a>
<a id="astructbt__conn__le__frame__space__updated_html_a126026dba0cb84ceaf10324212bbf3e0"></a>
<a id="astructbt__conn__le__frame__space__updated_html_a332a93e2d05750bd241e137381186f8b"></a>
<a id="astructbt__conn__le__frame__space__updated_html_a7cb3366670e07d06a466c3c7eb885b09"></a>
<a id="astructbt__conn__le__frame__space__updated_html_af1918fb7b4abc7f7b3eb11c33a3190f6"></a>
<a id="astructbt__conn__le__frame__space__updated_html_af6b88c108be375ea80466ece72257f2e"></a>
<a id="astructbt__conn__le__info_html"></a>
<a id="astructbt__conn__le__info_html_a1f78e1c0ed3482ce6eec9ce6eeda4769"></a>
<a id="astructbt__conn__le__info_html_a215d39c6cd7da1ac033529b5541cbfc1"></a>
<a id="astructbt__conn__le__info_html_a236d1c97c735c7cfaead0b1a3672d512"></a>
<a id="astructbt__conn__le__info_html_a3be5df0deb0af08f84843eb3c6a5e5ae"></a>
<a id="astructbt__conn__le__info_html_a3bede29a6a5df282bde6a26f50ea9aee"></a>
<a id="astructbt__conn__le__info_html_a5d97a2eb4aa880abe857f19adeea425d"></a>
<a id="astructbt__conn__le__info_html_a5f1eacec82f31182460d6d5359a8b295"></a>
<a id="astructbt__conn__le__info_html_a95a1f635e53f16d5839cdd58f4bda962"></a>
<a id="astructbt__conn__le__info_html_acd83835fe5ec0878fd653b87cb570a49"></a>
<a id="astructbt__conn__le__info_html_ae309f390c8d7b33a4de55791af235ab0"></a>
<a id="astructbt__conn__le__info_html_afb4dc594d063fbbad2bcd4acf047f716"></a>
<a id="astructbt__conn__le__min__conn__interval__group_html"></a>
<a id="astructbt__conn__le__min__conn__interval__group_html_a3d48e4889d3e039fc19da55c40efc911"></a>
<a id="astructbt__conn__le__min__conn__interval__group_html_a44c7e6e9983d607fdde9cafe8cb595e1"></a>
<a id="astructbt__conn__le__min__conn__interval__group_html_aed08c6c6bbe9f4bfae0a5e0c8ad6e9f3"></a>
<a id="astructbt__conn__le__min__conn__interval__info_html"></a>
<a id="astructbt__conn__le__min__conn__interval__info_html_aa39299ca32657e9f684e88875e7517dc"></a>
<a id="astructbt__conn__le__min__conn__interval__info_html_ac0d63f57518324d81509fea51fcefa60"></a>
<a id="astructbt__conn__le__min__conn__interval__info_html_ad9e6ae7c5632e4cc2a5e5eda52d2e0e8"></a>
<a id="astructbt__conn__le__path__loss__reporting__param_html"></a>
<a id="astructbt__conn__le__path__loss__reporting__param_html_a5cc7a17efee69d61b8f8d0c242321054"></a>
<a id="astructbt__conn__le__path__loss__reporting__param_html_a634c08e573cffd97a94ad681bed9239e"></a>
<a id="astructbt__conn__le__path__loss__reporting__param_html_a6fec4497c6fd95fa6f265bd859976c9d"></a>
<a id="astructbt__conn__le__path__loss__reporting__param_html_aec49adc896604d878060b03bd40ab0f4"></a>
<a id="astructbt__conn__le__path__loss__reporting__param_html_af8e70508a39ee73b75a4769769aa303f"></a>
<a id="astructbt__conn__le__path__loss__threshold__report_html"></a>
<a id="astructbt__conn__le__path__loss__threshold__report_html_ab2b71b7ddccc40ced56657a548b98e77"></a>
<a id="astructbt__conn__le__path__loss__threshold__report_html_abe631b07816d6c18bacba64bfbd1e844"></a>
<a id="astructbt__conn__le__phy__info_html"></a>
<a id="astructbt__conn__le__phy__info_html_abf029b63958d86eef7bf15218238783b"></a>
<a id="astructbt__conn__le__phy__info_html_ac65912cc2a7997c0f886886783ea5b11"></a>
<a id="astructbt__conn__le__phy__param_html"></a>
<a id="astructbt__conn__le__phy__param_html_a889dae2cdc2fba43f9f1194d26c4b737"></a>
<a id="astructbt__conn__le__phy__param_html_a8d576bed5d9dfe9ca9a694d6d295afbc"></a>
<a id="astructbt__conn__le__phy__param_html_ace64d2181ecc25ecdfa374f7f4bcf664"></a>
<a id="astructbt__conn__le__read__all__remote__feat__complete_html"></a>
<a id="astructbt__conn__le__read__all__remote__feat__complete_html_a0dbbd0144cc6990b45d662896862cce7"></a>
<a id="astructbt__conn__le__read__all__remote__feat__complete_html_a1554bd9035619cc4dbdb2d04fd9105ad"></a>
<a id="astructbt__conn__le__read__all__remote__feat__complete_html_a7a8db1d0c0656e8953da8b8aa4bec2c7"></a>
<a id="astructbt__conn__le__read__all__remote__feat__complete_html_a996e2600fd41bf1b6d95b6ee5873f6ce"></a>
<a id="astructbt__conn__le__remote__info_html"></a>
<a id="astructbt__conn__le__remote__info_html_a4ff434f6c501dc60db5c4b776be46b3b"></a>
<a id="astructbt__conn__le__subrate__changed_html"></a>
<a id="astructbt__conn__le__subrate__changed_html_a0c3e3dc41ca4dec92740c920e959060b"></a>
<a id="astructbt__conn__le__subrate__changed_html_a2420a0a3145471c6a1a618bea8d1d7c6"></a>
<a id="astructbt__conn__le__subrate__changed_html_aa0bab070bc43972dfb3a5259934b4931"></a>
<a id="astructbt__conn__le__subrate__changed_html_aab0cb08a7549401684bcab3c291dc192"></a>
<a id="astructbt__conn__le__subrate__changed_html_afc5a577dadf41819e89bc3af016ce258"></a>
<a id="astructbt__conn__le__subrate__param_html"></a>
<a id="astructbt__conn__le__subrate__param_html_a15d05324708ddeea8d2f3515eea396bb"></a>
<a id="astructbt__conn__le__subrate__param_html_a59d2d244e3568b8f97ce936121d41b1a"></a>
<a id="astructbt__conn__le__subrate__param_html_a978cef5f2f14a5a7fe7ded09c6fdf2d9"></a>
<a id="astructbt__conn__le__subrate__param_html_aca0897d00a1dd1735dbbaf5bfde711ed"></a>
<a id="astructbt__conn__le__subrate__param_html_aef75fec8ba8c9987d55e81aa2539b96e"></a>
<a id="astructbt__conn__le__subrating__info_html"></a>
<a id="astructbt__conn__le__subrating__info_html_a0a6d1eae73f76382f1a9415c01761c19"></a>
<a id="astructbt__conn__le__subrating__info_html_a23736535309f38695a2e432c5c80bbe1"></a>
<a id="astructbt__conn__le__tx__power__report_html"></a>
<a id="astructbt__conn__le__tx__power__report_html_a5b1f67537fbe945f2f258b47082723b4"></a>
<a id="astructbt__conn__le__tx__power__report_html_a7c681c7b9f77d994b2de1febea7c5dc9"></a>
<a id="astructbt__conn__le__tx__power__report_html_aa5606925229784af8ae90542432cf200"></a>
<a id="astructbt__conn__le__tx__power__report_html_ace830ddb7ae662c9759babed87f1b6f3"></a>
<a id="astructbt__conn__le__tx__power__report_html_ae7a4f77c6f7af1a459896d25cf661eb8"></a>
<a id="astructbt__conn__le__tx__power_html"></a>
<a id="astructbt__conn__le__tx__power_html_a1674247c511906fa6f0193653ed0b71a"></a>
<a id="astructbt__conn__le__tx__power_html_a6d2e5a5215fa5d60630e74928a67fc04"></a>
<a id="astructbt__conn__le__tx__power_html_a8702c4ff5082b8f90decdfabfb8253fe"></a>
<a id="astructbt__conn__oob__info_html"></a>
<a id="astructbt__conn__oob__info_html_a2117d76f495304753bc028afc66fc6b0"></a>
<a id="astructbt__conn__oob__info_html_a49c2473beac84e2ea21b1299352beee6"></a>
<a id="astructbt__conn__oob__info_html_a71bf295d82fbc647b3816bfba6fa0ae7"></a>
<a id="astructbt__conn__oob__info_html_a72a749120c0a55a8dc9bd078921277e5"></a>
<a id="astructbt__conn__oob__info_html_a7506049b35ac63602452b087d1d60fa2"></a>
<a id="astructbt__conn__oob__info_html_a99685ad84ac991e0540855cab5546ff8"></a>
<a id="astructbt__conn__oob__info_html_a9c71633c3fc8c0a16edde7e6f1a832db"></a>
<a id="astructbt__conn__oob__info_html_aaec69b732a4bd8baf10c8b66bc73db89a4c33ea839306256a198c29ea783c659b"></a>
<a id="astructbt__conn__oob__info_html_aaec69b732a4bd8baf10c8b66bc73db89acd02773beb42df3fb6cbaa2fa2abda1e"></a>
<a id="astructbt__conn__pairing__feat_html"></a>
<a id="astructbt__conn__pairing__feat_html_a49f9f02e232e91f7f7a530aa7f226cba"></a>
<a id="astructbt__conn__pairing__feat_html_a68005cea273c8e76c086502001b258b0"></a>
<a id="astructbt__conn__pairing__feat_html_a70adc125b875348ec8d273dea3b470d8"></a>
<a id="astructbt__conn__pairing__feat_html_abe1d7d4bd9f4b551a2d0c69adc75bd40"></a>
<a id="astructbt__conn__pairing__feat_html_af9a977b1e0f9d4eada26a82d92eaec54"></a>
<a id="astructbt__conn__pairing__feat_html_afb03164960db62b4b4cf70d3f0134099"></a>
<a id="astructbt__conn__remote__info_html"></a>
<a id="astructbt__conn__remote__info_html_a2664f6ed3bd22f9a011126daf5d81376"></a>
<a id="astructbt__conn__remote__info_html_a360979a15c958706157fc630fd55cbca"></a>
<a id="astructbt__conn__remote__info_html_a47cc5a4b8888a0b8faaf6880c37418b8"></a>
<a id="astructbt__conn__remote__info_html_a8bb514196bde5df561dbf76b68060729"></a>
<a id="astructbt__conn__remote__info_html_ab73365f09cdb5ce870272546543bcfeb"></a>
<a id="astructbt__conn__remote__info_html_ae75530b09c6dea416630a4a19a1d64cc"></a>
<a id="astructbt__conn__sco__info_html"></a>
<a id="astructbt__conn__sco__info_html_aad5fc309d1ffccda38c07b40ac028dd1"></a>
<a id="astructbt__conn__sco__info_html_ae4474ebfe0129eb6214987a31430d4f7"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__df__conn__iq__samples__report_html"></a>
<a id="astructbt__le__conn__param_html"></a>
<a id="astructbt__le__conn__param_html_a3d21bd8363fa77dab83468ea319fef7d"></a>
<a id="astructbt__le__conn__param_html_a6d5a2662a5f22ccc26c992829d21f22d"></a>
<a id="astructbt__le__conn__param_html_ac06c16eb02e7a9d8b414db07e829178a"></a>
<a id="astructbt__le__conn__param_html_acd3b0a74402ca45402bab9ff54763e8d"></a>
<a id="astructbt__le__ext__adv_html"></a>
<a id="astructbt__le__oob__sc__data_html"></a>
<a id="astructbt__security__info_html"></a>
<a id="astructbt__security__info_html_a6567ffb82b7fa8093cc57ef4662873ba"></a>
<a id="astructbt__security__info_html_a7b18849fad25b3f2da6b8c85a56d86e1"></a>
<a id="astructbt__security__info_html_a99cb4af08bfa1dab182821d956368526"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="atoolchain_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2015-2016 Intel Corporation
 * Copyright (c) 2025 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CONN_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CONN_H_


#include <stdbool.h>
#include <stdint.h>

#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/direction.h>
#include <zephyr/bluetooth/gap.h>
#include <zephyr/bluetooth/hci_types.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_conn;

struct bt_le_conn_param {
        uint16_t interval_min;
        uint16_t interval_max;
        uint16_t latency;
        uint16_t timeout;
};

#define BT_LE_CONN_PARAM_INIT(int_min, int_max, lat, to) \
{ \
        .interval_min = (int_min), \
        .interval_max = (int_max), \
        .latency = (lat), \
        .timeout = (to), \
}

#define BT_LE_CONN_PARAM(int_min, int_max, lat, to) \
        ((struct bt_le_conn_param[]) { \
                BT_LE_CONN_PARAM_INIT(int_min, int_max, lat, to) \
         })

#define BT_LE_CONN_PARAM_DEFAULT                                                                   \
        BT_LE_CONN_PARAM(BT_GAP_INIT_CONN_INT_MIN, BT_GAP_INIT_CONN_INT_MAX, 0,                    \
                         BT_GAP_MS_TO_CONN_TIMEOUT(4000))

struct bt_conn_le_phy_info {
        uint8_t tx_phy;
        uint8_t rx_phy;
};

enum {
        BT_CONN_LE_PHY_OPT_NONE = 0,

        BT_CONN_LE_PHY_OPT_CODED_S2  = BIT(0),

        BT_CONN_LE_PHY_OPT_CODED_S8  = BIT(1),
};

struct bt_conn_le_phy_param {
        uint16_t options;
        uint8_t  pref_tx_phy;
        uint8_t  pref_rx_phy;
};

#define BT_CONN_LE_PHY_PARAM_INIT(_pref_tx_phy, _pref_rx_phy) \
{ \
        .options = BT_CONN_LE_PHY_OPT_NONE, \
        .pref_tx_phy = (_pref_tx_phy), \
        .pref_rx_phy = (_pref_rx_phy), \
}

#define BT_CONN_LE_PHY_PARAM(_pref_tx_phy, _pref_rx_phy) \
        ((struct bt_conn_le_phy_param []) { \
                BT_CONN_LE_PHY_PARAM_INIT(_pref_tx_phy, _pref_rx_phy) \
         })

#define BT_CONN_LE_PHY_PARAM_1M BT_CONN_LE_PHY_PARAM(BT_GAP_LE_PHY_1M, \
                                                     BT_GAP_LE_PHY_1M)

#define BT_CONN_LE_PHY_PARAM_2M BT_CONN_LE_PHY_PARAM(BT_GAP_LE_PHY_2M, \
                                                     BT_GAP_LE_PHY_2M)

#define BT_CONN_LE_PHY_PARAM_CODED BT_CONN_LE_PHY_PARAM(BT_GAP_LE_PHY_CODED, \
                                                        BT_GAP_LE_PHY_CODED)

#define BT_CONN_LE_PHY_PARAM_ALL BT_CONN_LE_PHY_PARAM(BT_GAP_LE_PHY_1M |   \
                                                      BT_GAP_LE_PHY_2M |   \
                                                      BT_GAP_LE_PHY_CODED, \
                                                      BT_GAP_LE_PHY_1M |   \
                                                      BT_GAP_LE_PHY_2M |   \
                                                      BT_GAP_LE_PHY_CODED)

struct bt_conn_le_data_len_info {
        uint16_t tx_max_len;
        uint16_t tx_max_time;
        uint16_t rx_max_len;
        uint16_t rx_max_time;
};

struct bt_conn_le_data_len_param {
        uint16_t tx_max_len;
        uint16_t tx_max_time;
};

#define BT_CONN_LE_DATA_LEN_PARAM_INIT(_tx_max_len, _tx_max_time) \
{ \
        .tx_max_len = (_tx_max_len), \
        .tx_max_time = (_tx_max_time), \
}

#define BT_CONN_LE_DATA_LEN_PARAM(_tx_max_len, _tx_max_time) \
        ((struct bt_conn_le_data_len_param[]) { \
                BT_CONN_LE_DATA_LEN_PARAM_INIT(_tx_max_len, _tx_max_time) \
         })

#define BT_LE_DATA_LEN_PARAM_DEFAULT \
        BT_CONN_LE_DATA_LEN_PARAM(BT_GAP_DATA_LEN_DEFAULT, \
                                  BT_GAP_DATA_TIME_DEFAULT)

#define BT_LE_DATA_LEN_PARAM_MAX \
        BT_CONN_LE_DATA_LEN_PARAM(BT_GAP_DATA_LEN_MAX, \
                                  BT_GAP_DATA_TIME_MAX)

struct bt_conn_le_subrate_param {
        uint16_t subrate_min;
        uint16_t subrate_max;
        uint16_t max_latency;
        uint16_t continuation_number;
        uint16_t supervision_timeout;
};

struct bt_conn_le_subrating_info {
        uint16_t factor;
        uint16_t continuation_number;
};

struct bt_conn_le_subrate_changed {
        uint8_t status;
        uint16_t factor;
        uint16_t continuation_number;
        uint16_t peripheral_latency;
        uint16_t supervision_timeout;
};

#define BT_CONN_LE_MAX_CONN_INTERVAL_GROUPS 41

struct bt_conn_le_min_conn_interval_group {
        uint16_t min_125us;
        uint16_t max_125us;
        uint16_t stride_125us;
};

struct bt_conn_le_min_conn_interval_info {
        uint16_t min_supported_conn_interval_us;
        uint8_t num_groups;
        struct bt_conn_le_min_conn_interval_group groups[BT_CONN_LE_MAX_CONN_INTERVAL_GROUPS];
};

struct bt_conn_le_conn_rate_param {
        uint16_t interval_min_125us;
        uint16_t interval_max_125us;
        uint16_t subrate_min;
        uint16_t subrate_max;
        uint16_t max_latency;
        uint16_t continuation_number;
        uint16_t supervision_timeout_10ms;
        uint16_t min_ce_len_125us;
        uint16_t max_ce_len_125us;
};

struct bt_conn_le_conn_rate_changed {
        uint32_t interval_us;
        uint16_t subrate_factor;
        uint16_t peripheral_latency;
        uint16_t continuation_number;
        uint16_t supervision_timeout_10ms;
};

struct bt_conn_le_read_all_remote_feat_complete {
        uint8_t status;
        uint8_t max_remote_page;
        uint8_t max_valid_page;
        const uint8_t *features;
};

#define BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL_IFS                    \
        (BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_CP_MASK | \
         BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_PC_MASK)

#define BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL                        \
        (BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_CP_MASK | \
         BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_PC_MASK | \
         BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MCES_MASK)

#define BT_CONN_LE_FRAME_SPACE_TYPES_MASK_CIS                     \
        (BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_CIS_MASK | \
         BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MSS_CIS_MASK)

#define BT_CONN_LE_FRAME_SPACE_MAX (10000U)

enum bt_conn_le_frame_space_update_initiator {
        BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST =
                BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST,
        BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER =
                BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER,
        BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER =
                BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER
};

struct bt_conn_le_frame_space_update_param {
        uint8_t phys;
        uint16_t spacing_types;
        uint16_t frame_space_min;
        uint16_t frame_space_max;
};

struct bt_conn_le_frame_space_updated {
        uint8_t status;
        enum bt_conn_le_frame_space_update_initiator initiator;
        uint16_t frame_space;
        uint8_t phys;
        uint16_t spacing_types;
};

enum __packed bt_conn_type {
        BT_CONN_TYPE_LE = BIT(0),
        BT_CONN_TYPE_BR = BIT(1),
        BT_CONN_TYPE_SCO = BIT(2),
        BT_CONN_TYPE_ISO = BIT(3),
        BT_CONN_TYPE_ALL = BT_CONN_TYPE_LE | BT_CONN_TYPE_BR |
                           BT_CONN_TYPE_SCO | BT_CONN_TYPE_ISO,
};

enum bt_conn_le_cs_capability_rtt_aa_only {
        BT_CONN_LE_CS_RTT_AA_ONLY_NOT_SUPP = 0,
        BT_CONN_LE_CS_RTT_AA_ONLY_10NS,
        BT_CONN_LE_CS_RTT_AA_ONLY_150NS,
};

enum bt_conn_le_cs_capability_rtt_sounding {
        BT_CONN_LE_CS_RTT_SOUNDING_NOT_SUPP = 0,
        BT_CONN_LE_CS_RTT_SOUNDING_10NS,
        BT_CONN_LE_CS_RTT_SOUNDING_150NS,
};

enum bt_conn_le_cs_capability_rtt_random_payload {
        BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_NOT_SUPP = 0,
        BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_10NS,
        BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_150NS,
};

struct bt_conn_le_cs_capabilities {
        uint8_t num_config_supported;
        uint16_t max_consecutive_procedures_supported;
        uint8_t num_antennas_supported;
        uint8_t max_antenna_paths_supported;
        bool initiator_supported;
        bool reflector_supported;
        bool mode_3_supported;
        enum bt_conn_le_cs_capability_rtt_aa_only rtt_aa_only_precision;
        enum bt_conn_le_cs_capability_rtt_sounding rtt_sounding_precision;
        enum bt_conn_le_cs_capability_rtt_random_payload rtt_random_payload_precision;
        uint8_t rtt_aa_only_n;
        uint8_t rtt_sounding_n;
        uint8_t rtt_random_payload_n;
        bool phase_based_nadm_sounding_supported;
        bool phase_based_nadm_random_supported;
        bool cs_sync_2m_phy_supported;
        bool cs_sync_2m_2bt_phy_supported;
        bool cs_without_fae_supported;
        bool chsel_alg_3c_supported;
        bool pbr_from_rtt_sounding_seq_supported;
        bool cs_ipt_reflector;
        uint16_t t_ip1_times_supported;
        uint16_t t_ip2_times_supported;
        uint16_t t_fcs_times_supported;
        uint16_t t_pm_times_supported;
        uint8_t t_sw_time;
        uint8_t tx_snr_capability;
        uint16_t t_ip2_ipt_times_supported;
        uint8_t t_sw_ipt_time_supported;
};

struct bt_conn_le_cs_fae_table {
        int8_t *remote_fae_table;
};

#define BT_CONN_LE_CS_MODE_MAIN_MODE_PART(x) ((x) & 0x3)

#define BT_CONN_LE_CS_MODE_SUB_MODE_PART(x)  (((x) >> 4) & 0x3)

enum bt_conn_le_cs_mode {
        BT_CONN_LE_CS_MAIN_MODE_1_NO_SUB_MODE = BT_HCI_OP_LE_CS_MAIN_MODE_1,
        BT_CONN_LE_CS_MAIN_MODE_2_NO_SUB_MODE = BT_HCI_OP_LE_CS_MAIN_MODE_2,
        BT_CONN_LE_CS_MAIN_MODE_3_NO_SUB_MODE = BT_HCI_OP_LE_CS_MAIN_MODE_3,
        BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_1 = BT_HCI_OP_LE_CS_MAIN_MODE_2 |
                                              (BT_HCI_OP_LE_CS_SUB_MODE_1 << 4),
        BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_3 = BT_HCI_OP_LE_CS_MAIN_MODE_2 |
                                              (BT_HCI_OP_LE_CS_SUB_MODE_3 << 4),
        BT_CONN_LE_CS_MAIN_MODE_3_SUB_MODE_2 = BT_HCI_OP_LE_CS_MAIN_MODE_3 |
                                              (BT_HCI_OP_LE_CS_SUB_MODE_2 << 4),
};

enum bt_conn_le_cs_role {
        BT_CONN_LE_CS_ROLE_INITIATOR,
        BT_CONN_LE_CS_ROLE_REFLECTOR,
};

enum bt_conn_le_cs_rtt_type {
        BT_CONN_LE_CS_RTT_TYPE_AA_ONLY = BT_HCI_OP_LE_CS_RTT_TYPE_AA_ONLY,
        BT_CONN_LE_CS_RTT_TYPE_32_BIT_SOUNDING = BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_SOUND,
        BT_CONN_LE_CS_RTT_TYPE_96_BIT_SOUNDING = BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_SOUND,
        BT_CONN_LE_CS_RTT_TYPE_32_BIT_RANDOM = BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_RAND,
        BT_CONN_LE_CS_RTT_TYPE_64_BIT_RANDOM = BT_HCI_OP_LE_CS_RTT_TYPE_64BIT_RAND,
        BT_CONN_LE_CS_RTT_TYPE_96_BIT_RANDOM = BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_RAND,
        BT_CONN_LE_CS_RTT_TYPE_128_BIT_RANDOM = BT_HCI_OP_LE_CS_RTT_TYPE_128BIT_RAND,
};

enum bt_conn_le_cs_sync_phy {
        BT_CONN_LE_CS_SYNC_1M_PHY = BT_HCI_OP_LE_CS_CS_SYNC_1M,
        BT_CONN_LE_CS_SYNC_2M_PHY = BT_HCI_OP_LE_CS_CS_SYNC_2M,
        BT_CONN_LE_CS_SYNC_2M_2BT_PHY = BT_HCI_OP_LE_CS_CS_SYNC_2M_2BT,
};

enum bt_conn_le_cs_chsel_type {
        BT_CONN_LE_CS_CHSEL_TYPE_3B = BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3B,
        BT_CONN_LE_CS_CHSEL_TYPE_3C = BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3C,
};

enum bt_conn_le_cs_ch3c_shape {
        BT_CONN_LE_CS_CH3C_SHAPE_HAT = BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_HAT,
        BT_CONN_LE_CS_CH3C_SHAPE_X = BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_X,
};

struct bt_conn_le_cs_config {
        uint8_t id;
        enum bt_conn_le_cs_mode mode;
        uint8_t min_main_mode_steps;
        uint8_t max_main_mode_steps;
        uint8_t main_mode_repetition;
        uint8_t mode_0_steps;
        enum bt_conn_le_cs_role role;
        enum bt_conn_le_cs_rtt_type rtt_type;
        enum bt_conn_le_cs_sync_phy cs_sync_phy;
        uint8_t channel_map_repetition;
        enum bt_conn_le_cs_chsel_type channel_selection_type;
        enum bt_conn_le_cs_ch3c_shape ch3c_shape;
        uint8_t ch3c_jump;
        uint8_t cs_enhancements_1;
        uint8_t t_ip1_time_us;
        uint8_t t_ip2_time_us;
        uint8_t t_fcs_time_us;
        uint8_t t_pm_time_us;
        uint8_t channel_map[10];
};

enum bt_conn_le_cs_procedure_done_status {
        BT_CONN_LE_CS_PROCEDURE_COMPLETE = BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_COMPLETE,
        BT_CONN_LE_CS_PROCEDURE_INCOMPLETE = BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_PARTIAL,
        BT_CONN_LE_CS_PROCEDURE_ABORTED = BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_ABORTED,
};

enum bt_conn_le_cs_subevent_done_status {
        BT_CONN_LE_CS_SUBEVENT_COMPLETE = BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_COMPLETE,
        BT_CONN_LE_CS_SUBEVENT_ABORTED = BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_ABORTED,
};

enum bt_conn_le_cs_procedure_abort_reason {
        BT_CONN_LE_CS_PROCEDURE_NOT_ABORTED = BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_NO_ABORT,
        BT_CONN_LE_CS_PROCEDURE_ABORT_REQUESTED =
                BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST,
        BT_CONN_LE_CS_PROCEDURE_ABORT_TOO_FEW_CHANNELS =
                BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_TOO_FEW_CHANNELS,
        BT_CONN_LE_CS_PROCEDURE_ABORT_CHMAP_INSTANT_PASSED =
                BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_CHMAP_INSTANT_PASSED,
        BT_CONN_LE_CS_PROCEDURE_ABORT_UNSPECIFIED = BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_UNSPECIFIED,
};

enum bt_conn_le_cs_subevent_abort_reason {
        BT_CONN_LE_CS_SUBEVENT_NOT_ABORTED = BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_ABORT,
        BT_CONN_LE_CS_SUBEVENT_ABORT_REQUESTED =
                BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST,
        BT_CONN_LE_CS_SUBEVENT_ABORT_NO_CS_SYNC =
                BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_CS_SYNC_RECEIVED,
        BT_CONN_LE_CS_SUBEVENT_ABORT_SCHED_CONFLICT =
                BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_SCHED_CONFLICT,
        BT_CONN_LE_CS_SUBEVENT_ABORT_UNSPECIFIED = BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_UNSPECIFIED,
};

struct bt_conn_le_cs_subevent_result {
        struct {
                uint8_t config_id;
                uint16_t start_acl_conn_event;
                uint16_t procedure_counter;
                uint16_t frequency_compensation;
                int8_t reference_power_level;
                enum bt_conn_le_cs_procedure_done_status procedure_done_status;
                enum bt_conn_le_cs_subevent_done_status subevent_done_status;
                enum bt_conn_le_cs_procedure_abort_reason procedure_abort_reason;
                enum bt_conn_le_cs_subevent_abort_reason subevent_abort_reason;
                uint8_t num_antenna_paths;
                uint8_t num_steps_reported;
                uint8_t abort_step;
        } header;
        struct net_buf_simple *step_data_buf;
};

struct bt_conn *bt_conn_ref(struct bt_conn *conn);

void bt_conn_unref(struct bt_conn *conn);

static inline struct bt_conn *__must_check bt_conn_take(struct bt_conn **orig)
{
        return (struct bt_conn *)atomic_ptr_clear((atomic_ptr_t *)orig);
}

void bt_conn_drop(struct bt_conn **orig);

void bt_conn_foreach(enum bt_conn_type type,
                     void (*func)(struct bt_conn *conn, void *data),
                     void *data);

struct bt_conn *bt_conn_lookup_addr_le(uint8_t id, const bt_addr_le_t *peer);

const bt_addr_le_t *bt_conn_get_dst(const struct bt_conn *conn);

uint8_t bt_conn_index(const struct bt_conn *conn);

struct bt_conn_le_info {
        const bt_addr_le_t *src;
        const bt_addr_le_t *dst;
        const bt_addr_le_t *local;
        const bt_addr_le_t *remote;
        uint32_t interval_us;
#if !defined(CONFIG_BT_SHORTER_CONNECTION_INTERVALS) || defined(__DOXYGEN__)
        union {
                __deprecated uint16_t interval;
                uint16_t _interval;
        };
#endif /* !CONFIG_BT_SHORTER_CONNECTION_INTERVALS */

        uint16_t latency;
        uint16_t timeout;

#if defined(CONFIG_BT_USER_PHY_UPDATE) || defined(__DOXYGEN__)
        const struct bt_conn_le_phy_info      *phy;
#endif /* defined(CONFIG_BT_USER_PHY_UPDATE) */

#if defined(CONFIG_BT_USER_DATA_LEN_UPDATE) || defined(__DOXYGEN__)
        const struct bt_conn_le_data_len_info *data_len;
#endif /* defined(CONFIG_BT_USER_DATA_LEN_UPDATE) */

#if defined(CONFIG_BT_SUBRATING) || defined(__DOXYGEN__)
        const struct bt_conn_le_subrating_info *subrate;
#endif /* defined(CONFIG_BT_SUBRATING) */
};

#define BT_CONN_INTERVAL_TO_MS(interval) ((interval) * 5U / 4U)

#define BT_CONN_INTERVAL_TO_US(interval) ((interval) * 1250U)

#define BT_CONN_SCI_INTERVAL_TO_US(_interval) ((_interval) * BT_HCI_LE_SCI_INTERVAL_UNIT_US)

struct bt_conn_br_info {
        const bt_addr_t *dst;
};

struct bt_conn_sco_info {
        uint8_t link_type;
        uint8_t air_mode;
};

enum {
        BT_CONN_ROLE_CENTRAL = 0,
        BT_CONN_ROLE_PERIPHERAL = 1,
};

enum bt_conn_state {
        BT_CONN_STATE_DISCONNECTED,
        BT_CONN_STATE_CONNECTING,
        BT_CONN_STATE_CONNECTED,
        BT_CONN_STATE_DISCONNECTING,
};

typedef enum __packed {
        BT_SECURITY_L0,
        BT_SECURITY_L1,
        BT_SECURITY_L2,
        BT_SECURITY_L3,
        BT_SECURITY_L4,
        BT_SECURITY_FORCE_PAIR = BIT(7),
} bt_security_t;

enum bt_security_flag {
        BT_SECURITY_FLAG_SC = BIT(0),
        BT_SECURITY_FLAG_OOB = BIT(1),
};

struct bt_security_info {
        bt_security_t level;
        uint8_t enc_key_size;
        enum bt_security_flag flags;
};

struct bt_conn_info {
        enum bt_conn_type type;
        uint8_t role;
        uint8_t id;
        union {
                struct bt_conn_le_info le;
                struct bt_conn_br_info br;
                struct bt_conn_sco_info sco;
        };
        enum bt_conn_state state;
        struct bt_security_info security;
};

struct bt_conn_le_remote_info {

        const uint8_t *features;
};

struct bt_conn_br_remote_info {

        const uint8_t *features;

        uint8_t num_pages;
};

struct bt_conn_remote_info {
        uint8_t  type;

        uint8_t  version;

        uint16_t manufacturer;

        uint16_t subversion;

        union {
                struct bt_conn_le_remote_info le;

                struct bt_conn_br_remote_info br;
        };
};

enum bt_conn_le_tx_power_phy {
        BT_CONN_LE_TX_POWER_PHY_NONE,
        BT_CONN_LE_TX_POWER_PHY_1M,
        BT_CONN_LE_TX_POWER_PHY_2M,
        BT_CONN_LE_TX_POWER_PHY_CODED_S8,
        BT_CONN_LE_TX_POWER_PHY_CODED_S2,
};

struct bt_conn_le_tx_power {

        uint8_t phy;

        int8_t current_level;

        int8_t max_level;
};


struct bt_conn_le_tx_power_report {

        uint8_t reason;

        enum bt_conn_le_tx_power_phy phy;

        int8_t tx_power_level;

        uint8_t tx_power_level_flag;

        int8_t delta;
};

enum bt_conn_le_path_loss_zone {
        BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_LOW,
        BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_MIDDLE,
        BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_HIGH,
        BT_CONN_LE_PATH_LOSS_ZONE_UNAVAILABLE,
};

BUILD_ASSERT(BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_LOW == BT_HCI_LE_ZONE_ENTERED_LOW);
BUILD_ASSERT(BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_MIDDLE == BT_HCI_LE_ZONE_ENTERED_MIDDLE);
BUILD_ASSERT(BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_HIGH == BT_HCI_LE_ZONE_ENTERED_HIGH);

struct bt_conn_le_path_loss_threshold_report {

        enum bt_conn_le_path_loss_zone zone;

        uint8_t path_loss;
};

struct bt_conn_le_path_loss_reporting_param {
        uint8_t high_threshold;
        uint8_t high_hysteresis;
        uint8_t low_threshold;
        uint8_t low_hysteresis;
        uint16_t min_time_spent;
};

enum bt_conn_auth_keypress {
        BT_CONN_AUTH_KEYPRESS_ENTRY_STARTED = 0x00,
        BT_CONN_AUTH_KEYPRESS_DIGIT_ENTERED = 0x01,
        BT_CONN_AUTH_KEYPRESS_DIGIT_ERASED = 0x02,
        BT_CONN_AUTH_KEYPRESS_CLEARED = 0x03,
        BT_CONN_AUTH_KEYPRESS_ENTRY_COMPLETED = 0x04,
};

int bt_conn_get_info(const struct bt_conn *conn, struct bt_conn_info *info);

struct bt_conn_tmp_str {
        /* BT_ADDR_LE_STR_LEN covers both BR/EDR and LE string lengths */
        char str[BT_ADDR_LE_STR_LEN];
};

struct bt_conn_tmp_str bt_conn_dst_tmp_str(const struct bt_conn *conn);

#define bt_conn_dst_str(_conn) bt_conn_dst_tmp_str(_conn).str

bool bt_conn_is_type(const struct bt_conn *conn, enum bt_conn_type type);

int bt_conn_get_remote_info(const struct bt_conn *conn, struct bt_conn_remote_info *remote_info);

int bt_conn_le_get_tx_power_level(struct bt_conn *conn,
                                  struct bt_conn_le_tx_power *tx_power_level);

int bt_conn_le_enhanced_get_tx_power_level(struct bt_conn *conn,
                                           struct bt_conn_le_tx_power *tx_power);

int bt_conn_le_get_remote_tx_power_level(struct bt_conn *conn,
                                         enum bt_conn_le_tx_power_phy phy);

int bt_conn_le_set_tx_power_report_enable(struct bt_conn *conn,
                                          bool local_enable,
                                          bool remote_enable);

int bt_conn_le_set_path_loss_mon_param(struct bt_conn *conn,
                                       const struct bt_conn_le_path_loss_reporting_param *param);

int bt_conn_le_set_path_loss_mon_enable(struct bt_conn *conn, bool enable);

int bt_conn_le_subrate_set_defaults(const struct bt_conn_le_subrate_param *params);

int bt_conn_le_subrate_request(struct bt_conn *conn,
                               const struct bt_conn_le_subrate_param *params);

int bt_conn_le_read_min_conn_interval_groups(struct bt_conn_le_min_conn_interval_info *info);

int bt_conn_le_read_min_conn_interval(uint16_t *min_interval_us);

int bt_conn_le_conn_rate_set_defaults(const struct bt_conn_le_conn_rate_param *params);

int bt_conn_le_conn_rate_request(struct bt_conn *conn,
                                 const struct bt_conn_le_conn_rate_param *params);

int bt_conn_le_read_all_remote_features(struct bt_conn *conn, uint8_t pages_requested);

int bt_conn_le_frame_space_update(struct bt_conn *conn,
                                  const struct bt_conn_le_frame_space_update_param *params);

int bt_conn_le_param_update(struct bt_conn *conn,
                            const struct bt_le_conn_param *param);

int bt_conn_le_data_len_update(struct bt_conn *conn,
                               const struct bt_conn_le_data_len_param *param);

int bt_conn_le_phy_update(struct bt_conn *conn,
                          const struct bt_conn_le_phy_param *param);

int bt_conn_le_set_default_phy(uint8_t pref_tx_phy, uint8_t pref_rx_phy);

int bt_conn_disconnect(struct bt_conn *conn, uint8_t reason);

enum {
        BT_CONN_LE_OPT_NONE = 0,

        BT_CONN_LE_OPT_CODED = BIT(0),

        BT_CONN_LE_OPT_NO_1M = BIT(1),
};

struct bt_conn_le_create_param {

        uint32_t options;

        uint16_t interval;

        uint16_t window;

        uint16_t interval_coded;

        uint16_t window_coded;

        uint16_t timeout;
};

#define BT_CONN_LE_CREATE_PARAM_INIT(_options, _interval, _window) \
{ \
        .options = (_options), \
        .interval = (_interval), \
        .window = (_window), \
        .interval_coded = 0, \
        .window_coded = 0, \
        .timeout = 0, \
}

#define BT_CONN_LE_CREATE_PARAM(_options, _interval, _window) \
        ((struct bt_conn_le_create_param[]) { \
                BT_CONN_LE_CREATE_PARAM_INIT(_options, _interval, _window) \
         })

#define BT_CONN_LE_CREATE_CONN \
        BT_CONN_LE_CREATE_PARAM(BT_CONN_LE_OPT_NONE, \
                                BT_GAP_SCAN_FAST_INTERVAL, \
                                BT_GAP_SCAN_FAST_INTERVAL)

#define BT_CONN_LE_CREATE_CONN_AUTO \
        BT_CONN_LE_CREATE_PARAM(BT_CONN_LE_OPT_NONE, \
                                BT_GAP_SCAN_FAST_INTERVAL, \
                                BT_GAP_SCAN_FAST_WINDOW)

int bt_conn_le_create(const bt_addr_le_t *peer,
                      const struct bt_conn_le_create_param *create_param,
                      const struct bt_le_conn_param *conn_param,
                      struct bt_conn **conn);

struct bt_conn_le_create_synced_param {

        const bt_addr_le_t *peer;

        uint8_t subevent;
};

int bt_conn_le_create_synced(const struct bt_le_ext_adv *adv,
                             const struct bt_conn_le_create_synced_param *synced_param,
                             const struct bt_le_conn_param *conn_param, struct bt_conn **conn);

int bt_conn_le_create_auto(const struct bt_conn_le_create_param *create_param,
                           const struct bt_le_conn_param *conn_param);

int bt_conn_create_auto_stop(void);

int bt_conn_set_security(struct bt_conn *conn, bt_security_t sec);

bt_security_t bt_conn_get_security(const struct bt_conn *conn);

uint8_t bt_conn_enc_key_size(const struct bt_conn *conn);

enum bt_security_err {
        BT_SECURITY_ERR_SUCCESS,

        BT_SECURITY_ERR_AUTH_FAIL,

        BT_SECURITY_ERR_PIN_OR_KEY_MISSING,

        BT_SECURITY_ERR_OOB_NOT_AVAILABLE,

        BT_SECURITY_ERR_AUTH_REQUIREMENT,

        BT_SECURITY_ERR_PAIR_NOT_SUPPORTED,

        BT_SECURITY_ERR_PAIR_NOT_ALLOWED,

        BT_SECURITY_ERR_INVALID_PARAM,

        BT_SECURITY_ERR_KEY_REJECTED,

        BT_SECURITY_ERR_UNSPECIFIED,
};

enum bt_conn_le_cs_procedure_enable_state {
        BT_CONN_LE_CS_PROCEDURES_DISABLED = BT_HCI_OP_LE_CS_PROCEDURES_DISABLED,
        BT_CONN_LE_CS_PROCEDURES_ENABLED = BT_HCI_OP_LE_CS_PROCEDURES_ENABLED,
};

enum bt_conn_le_cs_tone_antenna_config_selection {
        BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B1 = BT_HCI_OP_LE_CS_ACI_0,
        BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B1 = BT_HCI_OP_LE_CS_ACI_1,
        BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A3_B1 = BT_HCI_OP_LE_CS_ACI_2,
        BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A4_B1 = BT_HCI_OP_LE_CS_ACI_3,
        BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B2 = BT_HCI_OP_LE_CS_ACI_4,
        BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B3 = BT_HCI_OP_LE_CS_ACI_5,
        BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B4 = BT_HCI_OP_LE_CS_ACI_6,
        BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B2 = BT_HCI_OP_LE_CS_ACI_7,
};

struct bt_conn_le_cs_procedure_enable_complete {
        /* The ID associated with the desired configuration (0 to 3) */
        uint8_t config_id;

        /* State of the CS procedure */
        enum bt_conn_le_cs_procedure_enable_state state;

        /* Antenna configuration index */
        enum bt_conn_le_cs_tone_antenna_config_selection tone_antenna_config_selection;

        /* Transmit power level used for CS procedures (-127 to 20 dB; 0x7F if unavailable) */
        int8_t selected_tx_power;

        /* Duration of each CS subevent in microseconds (1250 us to 4 s) */
        uint32_t subevent_len;

        /* Number of CS subevents anchored off the same ACL connection event (0x01 to 0x20) */
        uint8_t subevents_per_event;

        /* Time between consecutive CS subevents anchored off the same ACL connection event in
         * units of 0.625 ms
         */
        uint16_t subevent_interval;

        /* Number of ACL connection events between consecutive CS event anchor points */
        uint16_t event_interval;

        /* Number of ACL connection events between consecutive CS procedure anchor points */
        uint16_t procedure_interval;

        /* Number of CS procedures to be scheduled (0 if procedures to continue until disabled) */
        uint16_t procedure_count;

        /* Maximum duration for each procedure in units of 0.625 ms (0x0001 to 0xFFFF) */
        uint16_t max_procedure_len;
};

struct bt_conn_br_cb {
#if defined(CONFIG_BT_POWER_MODE_CONTROL) || defined(__DOXYGEN__)
        void (*mode_changed)(struct bt_conn *conn, uint8_t mode, uint16_t interval);
#endif /* CONFIG_BT_POWER_MODE_CONTROL */

        void (*role_changed)(struct bt_conn *conn, uint8_t status);

        void (*packet_type_changed)(struct bt_conn *conn, uint8_t status, uint16_t packet_type);
};

#define BT_CONN_PARAM_REJECT_ERR_L2CAP_CPUP 0xFF

struct bt_conn_cb {
        void (*connected)(struct bt_conn *conn, uint8_t err);

        void (*disconnected)(struct bt_conn *conn, uint8_t reason);

        void (*recycled)(void);

        bool (*le_param_req)(struct bt_conn *conn,
                             struct bt_le_conn_param *param);

        void (*le_param_updated)(struct bt_conn *conn, uint16_t interval,
                                 uint16_t latency, uint16_t timeout);

#if defined(CONFIG_BT_USER_CONN_PARAM_REJECTED) || defined(__DOXYGEN__)
        void (*le_param_update_rejected)(struct bt_conn *conn, uint8_t hci_err);
#endif /* defined(CONFIG_BT_USER_CONN_PARAM_REJECTED) || defined(__DOXYGEN__) */

#if defined(CONFIG_BT_SMP) || defined(__DOXYGEN__)
        void (*identity_resolved)(struct bt_conn *conn,
                                  const bt_addr_le_t *rpa,
                                  const bt_addr_le_t *identity);
#endif /* CONFIG_BT_SMP */
#if defined(CONFIG_BT_SMP) || defined(CONFIG_BT_CLASSIC)
        void (*security_changed)(struct bt_conn *conn, bt_security_t level,
                                 enum bt_security_err err);
#endif /* defined(CONFIG_BT_SMP) || defined(CONFIG_BT_CLASSIC) */

#if defined(CONFIG_BT_REMOTE_INFO) || defined(__DOXYGEN__)
        void (*remote_info_available)(struct bt_conn *conn,
                                      struct bt_conn_remote_info *remote_info);
#endif /* defined(CONFIG_BT_REMOTE_INFO) */

#if defined(CONFIG_BT_CLASSIC) || defined(__DOXYGEN__)
        struct bt_conn_br_cb br;
#endif /* CONFIG_BT_CLASSIC */

#if defined(CONFIG_BT_USER_PHY_UPDATE) || defined(__DOXYGEN__)
        void (*le_phy_updated)(struct bt_conn *conn,
                               struct bt_conn_le_phy_info *param);
#endif /* defined(CONFIG_BT_USER_PHY_UPDATE) */

#if defined(CONFIG_BT_USER_DATA_LEN_UPDATE) || defined(__DOXYGEN__)
        void (*le_data_len_updated)(struct bt_conn *conn,
                                    struct bt_conn_le_data_len_info *info);
#endif /* defined(CONFIG_BT_USER_DATA_LEN_UPDATE) */

#if defined(CONFIG_BT_DF_CONNECTION_CTE_RX) || defined(__DOXYGEN__)
        void (*cte_report_cb)(struct bt_conn *conn,
                              const struct bt_df_conn_iq_samples_report *iq_report);
#endif /* CONFIG_BT_DF_CONNECTION_CTE_RX */

#if defined(CONFIG_BT_TRANSMIT_POWER_CONTROL) || defined(__DOXYGEN__)
        void (*tx_power_report)(struct bt_conn *conn,
                                const struct bt_conn_le_tx_power_report *report);
#endif /* CONFIG_BT_TRANSMIT_POWER_CONTROL */

#if defined(CONFIG_BT_PATH_LOSS_MONITORING) || defined(__DOXYGEN__)
        void (*path_loss_threshold_report)(struct bt_conn *conn,
                                const struct bt_conn_le_path_loss_threshold_report *report);
#endif /* CONFIG_BT_PATH_LOSS_MONITORING */

#if defined(CONFIG_BT_SUBRATING) || defined(__DOXYGEN__)
        void (*subrate_changed)(struct bt_conn *conn,
                                const struct bt_conn_le_subrate_changed *params);
#endif /* CONFIG_BT_SUBRATING */

#if defined(CONFIG_BT_SHORTER_CONNECTION_INTERVALS) || defined(__DOXYGEN__)
        void (*conn_rate_changed)(struct bt_conn *conn, uint8_t status,
                                  const struct bt_conn_le_conn_rate_changed *params);
#endif /* CONFIG_BT_SHORTER_CONNECTION_INTERVALS */

#if defined(CONFIG_BT_LE_EXTENDED_FEAT_SET) || defined(__DOXYGEN__)
        void (*read_all_remote_feat_complete)(
                struct bt_conn *conn,
                const struct bt_conn_le_read_all_remote_feat_complete *params);
#endif /* CONFIG_BT_LE_EXTENDED_FEAT_SET */

#if defined(CONFIG_BT_FRAME_SPACE_UPDATE) || defined(__DOXYGEN__)
        void (*frame_space_updated)(
                struct bt_conn *conn,
                const struct bt_conn_le_frame_space_updated *params);
#endif /* CONFIG_BT_FRAME_SPACE_UPDATE */

#if defined(CONFIG_BT_CHANNEL_SOUNDING) || defined(__DOXYGEN__)
        void (*le_cs_read_remote_capabilities_complete)(struct bt_conn *conn,
                                                        uint8_t status,
                                                        struct bt_conn_le_cs_capabilities *params);

        void (*le_cs_read_remote_fae_table_complete)(struct bt_conn *conn,
                                                     uint8_t status,
                                                     struct bt_conn_le_cs_fae_table *params);

        void (*le_cs_config_complete)(struct bt_conn *conn,
                                      uint8_t status,
                                      struct bt_conn_le_cs_config *config);

        void (*le_cs_config_removed)(struct bt_conn *conn, uint8_t config_id);

        void (*le_cs_subevent_data_available)(struct bt_conn *conn,
                                              struct bt_conn_le_cs_subevent_result *result);

        void (*le_cs_security_enable_complete)(struct bt_conn *conn, uint8_t status);

        void (*le_cs_procedure_enable_complete)(
                struct bt_conn *conn, uint8_t status,
                struct bt_conn_le_cs_procedure_enable_complete *params);

#endif

#if defined(CONFIG_BT_CONN_DYNAMIC_CALLBACKS)
        sys_snode_t _node;
#endif
};

int bt_conn_cb_register(struct bt_conn_cb *cb);

int bt_conn_cb_unregister(struct bt_conn_cb *cb);

#define BT_CONN_CB_DEFINE(_name)                                        \
        static const STRUCT_SECTION_ITERABLE(bt_conn_cb,                \
                                                _CONCAT(bt_conn_cb_,    \
                                                        _name))

#if defined(CONFIG_BT_SECURITY_ERR_TO_STR)
const char *bt_security_err_to_str(enum bt_security_err err);
#else
static inline const char *bt_security_err_to_str(enum bt_security_err err)
{
        ARG_UNUSED(err);

        return "";
}
#endif

void bt_set_bondable(bool enable);

bool bt_get_bondable(void);

int bt_conn_set_bondable(struct bt_conn *conn, bool enable);

void bt_le_oob_set_sc_flag(bool enable);

void bt_le_oob_set_legacy_flag(bool enable);

int bt_le_oob_set_legacy_tk(struct bt_conn *conn, const uint8_t *tk);

int bt_le_oob_set_sc_data(struct bt_conn *conn,
                          const struct bt_le_oob_sc_data *oobd_local,
                          const struct bt_le_oob_sc_data *oobd_remote);

int bt_le_oob_get_sc_data(struct bt_conn *conn,
                          const struct bt_le_oob_sc_data **oobd_local,
                          const struct bt_le_oob_sc_data **oobd_remote);

struct bt_conn_oob_info {
        enum {
                BT_CONN_OOB_LE_LEGACY,

                BT_CONN_OOB_LE_SC,
        } type;

        union {
                struct {
                        enum {
                                BT_CONN_OOB_LOCAL_ONLY,

                                BT_CONN_OOB_REMOTE_ONLY,

                                BT_CONN_OOB_BOTH_PEERS,

                                BT_CONN_OOB_NO_DATA,
                        } oob_config;
                } lesc;
        };
};

struct bt_conn_pairing_feat {
        uint8_t io_capability;

        uint8_t oob_data_flag;

        uint8_t auth_req;

        uint8_t max_enc_key_size;

        uint8_t init_key_dist;

        uint8_t resp_key_dist;
};

#define BT_PASSKEY_RAND 0xffffffff

struct bt_conn_auth_cb {
#if defined(CONFIG_BT_SMP_APP_PAIRING_ACCEPT) || defined(__DOXYGEN__)
        enum bt_security_err (*pairing_accept)(struct bt_conn *conn,
                              const struct bt_conn_pairing_feat *const feat);
#endif /* CONFIG_BT_SMP_APP_PAIRING_ACCEPT */

        void (*passkey_display)(struct bt_conn *conn, unsigned int passkey);

#if defined(CONFIG_BT_PASSKEY_KEYPRESS) || defined(__DOXYGEN__)
        void (*passkey_display_keypress)(struct bt_conn *conn,
                                         enum bt_conn_auth_keypress type);
#endif /* CONFIG_BT_PASSKEY_KEYPRESS */

        void (*passkey_entry)(struct bt_conn *conn);

        void (*passkey_confirm)(struct bt_conn *conn, unsigned int passkey);

        void (*oob_data_request)(struct bt_conn *conn,
                                 struct bt_conn_oob_info *info);

        void (*cancel)(struct bt_conn *conn);

        void (*pairing_confirm)(struct bt_conn *conn);

#if defined(CONFIG_BT_CLASSIC) || defined(__DOXYGEN__)
        void (*pincode_entry)(struct bt_conn *conn, bool highsec);
#endif /* CONFIG_BT_CLASSIC */

#if defined(CONFIG_BT_APP_PASSKEY) || defined(__DOXYGEN__)
        uint32_t (*app_passkey)(struct bt_conn *conn);
#endif /* CONFIG_BT_APP_PASSKEY */
};

struct bt_conn_auth_info_cb {
        void (*pairing_complete)(struct bt_conn *conn, bool bonded);

        void (*pairing_failed)(struct bt_conn *conn,
                               enum bt_security_err reason);

        void (*bond_deleted)(uint8_t id, const bt_addr_le_t *peer);

        void (*addr_res_support_read)(struct bt_conn *conn,
                                      enum bt_le_addr_res_support support);

#if defined(CONFIG_BT_CLASSIC) || defined(__DOXYGEN__)
        void (*br_bond_deleted)(const bt_addr_t *peer);
#endif /* CONFIG_BT_CLASSIC */

        sys_snode_t node;
};

int bt_conn_auth_cb_register(const struct bt_conn_auth_cb *cb);

int bt_conn_auth_cb_overlay(struct bt_conn *conn, const struct bt_conn_auth_cb *cb);

int bt_conn_auth_info_cb_register(struct bt_conn_auth_info_cb *cb);

int bt_conn_auth_info_cb_unregister(struct bt_conn_auth_info_cb *cb);

int bt_conn_auth_passkey_entry(struct bt_conn *conn, unsigned int passkey);

int bt_conn_auth_keypress_notify(struct bt_conn *conn, enum bt_conn_auth_keypress type);

int bt_conn_auth_cancel(struct bt_conn *conn);

int bt_conn_auth_passkey_confirm(struct bt_conn *conn);

int bt_conn_auth_pairing_confirm(struct bt_conn *conn);

int bt_conn_auth_pincode_entry(struct bt_conn *conn, const char *pin);

struct bt_br_conn_param {
        bool allow_role_switch;
};

#define BT_BR_CONN_PARAM_INIT(role_switch) \
{ \
        .allow_role_switch = (role_switch), \
}

#define BT_BR_CONN_PARAM(role_switch) \
        ((struct bt_br_conn_param[]) { \
                BT_BR_CONN_PARAM_INIT(role_switch) \
         })

#define BT_BR_CONN_PARAM_DEFAULT BT_BR_CONN_PARAM(true)


struct bt_conn *bt_conn_create_br(const bt_addr_t *peer,
                                  const struct bt_br_conn_param *param);

struct bt_conn *bt_conn_lookup_addr_br(const bt_addr_t *peer);

const bt_addr_t *bt_conn_get_dst_br(const struct bt_conn *conn);

int bt_conn_br_switch_role(const struct bt_conn *conn, uint8_t role);

int bt_conn_br_set_role_switch_enable(const struct bt_conn *conn, bool enable);

int bt_conn_br_enter_sniff_mode(struct bt_conn *conn, uint16_t min_interval,
                                 uint16_t max_interval, uint16_t attempt, uint16_t timeout);

int bt_conn_br_exit_sniff_mode(struct bt_conn *conn);

int bt_conn_br_set_sniff_subrating(struct bt_conn *conn, uint16_t max_latency,
                                   uint16_t min_remote_timeout,
                                   uint16_t min_local_timeout);

int bt_conn_br_get_supervision_timeout(struct bt_conn *conn, uint16_t *timeout);

int bt_conn_br_set_supervision_timeout(struct bt_conn *conn, uint16_t timeout);

int bt_conn_br_change_packet_type(const struct bt_conn *conn, uint16_t packet_type);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CONN_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2015-2016 Intel Corporation。

版权（Copyright）：© 2025 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 1131 行

条件表达式：`!CONFIG_BT_SHORTER_CONNECTION_INTERVALS`。

### 注释 3：原第 1139 行

条件表达式：`defined(CONFIG_BT_USER_PHY_UPDATE)`。

### 注释 4：原第 1144 行

条件表达式：`defined(CONFIG_BT_USER_DATA_LEN_UPDATE)`。

### 注释 5：原第 1149 行

条件表达式：`defined(CONFIG_BT_SUBRATING)`。

### 注释 6：原第 1450 行

`BT_ADDR_LE_STR_LEN` 同时覆盖蓝牙基本速率／增强数据率（BR/EDR）和低功耗（LE）地址字符串的长度。

### 注释 7：原第 2143 行

与所需配置关联的标识符（ID），取值为 0–3。

### 注释 8：原第 2146 行

信道探测（CS）过程的状态。

### 注释 9：原第 2149 行

天线配置索引（antenna configuration index）。

### 注释 10：原第 2152 行

CS 过程使用的发射功率电平（transmit power level），范围为 −127 至 20 dB；不可用时为 `0x7F`。译注：原文单位为 dB，此处按原文保留。

### 注释 11：原第 2155 行

每个 CS 子事件（subevent）的持续时间，单位为微秒，范围为 1250 μs 至 4 s。

### 注释 12：原第 2158 行

以同一个异步无连接（ACL）连接事件为锚点的 CS 子事件数量，范围为 `0x01`–`0x20`。

### 注释 13：原第 2161 行

以同一个 ACL 连接事件为锚点的连续 CS 子事件之间的时间间隔，以 0.625 ms 为单位。

### 注释 14：原第 2166 行

连续 CS 事件锚点（anchor points）之间的 ACL 连接事件数量。

### 注释 15：原第 2169 行

连续 CS 过程锚点之间的 ACL 连接事件数量。

### 注释 16：原第 2172 行

要调度的 CS 过程数量；0 表示持续执行，直到被禁用。

### 注释 17：原第 2175 行

每次过程的最长持续时间，以 0.625 ms 为单位，范围为 `0x0001`–`0xFFFF`。

### 注释 18：原第 2191 行

条件编译配置（Configuration）标记：`CONFIG_BT_POWER_MODE_CONTROL`。

### 注释 19：原第 2365 行

条件表达式：`defined(CONFIG_BT_USER_CONN_PARAM_REJECTED) || defined(__DOXYGEN__)`。

### 注释 20：原第 2380 行

条件编译配置（Configuration）标记：`CONFIG_BT_SMP`。

### 注释 21：原第 2400 行

条件表达式：`defined(CONFIG_BT_SMP) || defined(CONFIG_BT_CLASSIC)`。

### 注释 22：原第 2413 行

条件表达式：`defined(CONFIG_BT_REMOTE_INFO)`。

### 注释 23：原第 2418 行

条件编译配置（Configuration）标记：`CONFIG_BT_CLASSIC`。

### 注释 24：原第 2431 行

条件表达式：`defined(CONFIG_BT_USER_PHY_UPDATE)`。

### 注释 25：原第 2444 行

条件表达式：`defined(CONFIG_BT_USER_DATA_LEN_UPDATE)`。

### 注释 26：原第 2455 行

条件编译配置（Configuration）标记：`CONFIG_BT_DF_CONNECTION_CTE_RX`。

### 注释 27：原第 2471 行

条件编译配置（Configuration）标记：`CONFIG_BT_TRANSMIT_POWER_CONTROL`。

### 注释 28：原第 2485 行

条件编译配置（Configuration）标记：`CONFIG_BT_PATH_LOSS_MONITORING`。

### 注释 29：原第 2500 行

条件编译配置（Configuration）标记：`CONFIG_BT_SUBRATING`。

### 注释 30：原第 2525 行

条件编译配置（Configuration）标记：`CONFIG_BT_SHORTER_CONNECTION_INTERVALS`。

### 注释 31：原第 2544 行

条件编译配置（Configuration）标记：`CONFIG_BT_LE_EXTENDED_FEAT_SET`。

### 注释 32：原第 2564 行

条件编译配置（Configuration）标记：`CONFIG_BT_FRAME_SPACE_UPDATE`。

### 注释 33：原第 2956 行

条件编译配置（Configuration）标记：`CONFIG_BT_SMP_APP_PAIRING_ACCEPT`。

### 注释 34：原第 3002 行

条件编译配置（Configuration）标记：`CONFIG_BT_PASSKEY_KEYPRESS`。

### 注释 35：原第 3120 行

条件编译配置（Configuration）标记：`CONFIG_BT_CLASSIC`。

### 注释 36：原第 3144 行

条件编译配置（Configuration）标记：`CONFIG_BT_APP_PASSKEY`。

### 注释 37：原第 3211 行

条件编译配置（Configuration）标记：`CONFIG_BT_CLASSIC`。

### 注释 38：原第 3537 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CONN_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/bluetooth/direction.h](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html)
- [zephyr/bluetooth/gap.h](https://docs.zephyrproject.org/latest/doxygen/html/gap_8h.html)
- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_le_conn_param](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [interval_min](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md#acd3b0a74402ca45402bab9ff54763e8d)
- [interval_max](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md#a6d5a2662a5f22ccc26c992829d21f22d)
- [latency](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md#a3d21bd8363fa77dab83468ea319fef7d)
- [timeout](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md#ac06c16eb02e7a9d8b414db07e829178a)
- [bt_conn_le_phy_info](../bluetooth_connection_model_reference/P028_bt_conn_le_phy_info_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [tx_phy](../bluetooth_connection_model_reference/P028_bt_conn_le_phy_info_结构体.md#ac65912cc2a7997c0f886886783ea5b11)
- [rx_phy](../bluetooth_connection_model_reference/P028_bt_conn_le_phy_info_结构体.md#abf029b63958d86eef7bf15218238783b)
- [BT_CONN_LE_PHY_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98)
- [BT_CONN_LE_PHY_OPT_CODED_S2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga08eb37185a763212e65c47ab4c886ecaa42e6ff627268b9eef111375d591f9f34)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_CONN_LE_PHY_OPT_CODED_S8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga08eb37185a763212e65c47ab4c886ecaad1d46128ba2516810af7383e850929e0)
- [bt_conn_le_phy_param](../bluetooth_connection_model_reference/P029_bt_conn_le_phy_param_结构体.md)
- [options](../bluetooth_connection_model_reference/P029_bt_conn_le_phy_param_结构体.md#a889dae2cdc2fba43f9f1194d26c4b737)
- [pref_tx_phy](../bluetooth_connection_model_reference/P029_bt_conn_le_phy_param_结构体.md#ace64d2181ecc25ecdfa374f7f4bcf664)
- [pref_rx_phy](../bluetooth_connection_model_reference/P029_bt_conn_le_phy_param_结构体.md#a8d576bed5d9dfe9ca9a694d6d295afbc)
- [bt_conn_le_data_len_info](../bluetooth_connection_model_reference/P019_bt_conn_le_data_len_info_结构体.md)
- [tx_max_len](../bluetooth_connection_model_reference/P019_bt_conn_le_data_len_info_结构体.md#a48d175f3c4b03dbdee129feae3edab23)
- [tx_max_time](../bluetooth_connection_model_reference/P019_bt_conn_le_data_len_info_结构体.md#a14288429cbbcce2ef34580a581815eb7)
- [rx_max_len](../bluetooth_connection_model_reference/P019_bt_conn_le_data_len_info_结构体.md#a18ddc603e922586e331187c9b29f2908)
- [rx_max_time](../bluetooth_connection_model_reference/P019_bt_conn_le_data_len_info_结构体.md#af2316cdc921e9ec19491501e15248f73)
- [bt_conn_le_data_len_param](../bluetooth_connection_model_reference/P020_bt_conn_le_data_len_param_结构体.md)
- [tx_max_len](../bluetooth_connection_model_reference/P020_bt_conn_le_data_len_param_结构体.md#a8b279a0dc72c70aaf5205558fd4b4c4a)
- [tx_max_time](../bluetooth_connection_model_reference/P020_bt_conn_le_data_len_param_结构体.md#a9046542952fa822b944602b398562e6e)
- [bt_conn_le_subrate_param](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md)
- [subrate_min](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md#aef75fec8ba8c9987d55e81aa2539b96e)
- [subrate_max](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md#a59d2d244e3568b8f97ce936121d41b1a)
- [max_latency](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md#a15d05324708ddeea8d2f3515eea396bb)
- [continuation_number](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md#a978cef5f2f14a5a7fe7ded09c6fdf2d9)
- [supervision_timeout](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md#aca0897d00a1dd1735dbbaf5bfde711ed)
- [bt_conn_le_subrating_info](../bluetooth_connection_model_reference/P034_bt_conn_le_subrating_info_结构体.md)
- [factor](../bluetooth_connection_model_reference/P034_bt_conn_le_subrating_info_结构体.md#a23736535309f38695a2e432c5c80bbe1)
- [continuation_number](../bluetooth_connection_model_reference/P034_bt_conn_le_subrating_info_结构体.md#a0a6d1eae73f76382f1a9415c01761c19)
- [bt_conn_le_subrate_changed](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md)
- [status](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md#afc5a577dadf41819e89bc3af016ce258)
- [factor](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md#a0c3e3dc41ca4dec92740c920e959060b)
- [continuation_number](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md#a2420a0a3145471c6a1a618bea8d1d7c6)
- [peripheral_latency](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md#aa0bab070bc43972dfb3a5259934b4931)
- [supervision_timeout](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md#aab0cb08a7549401684bcab3c291dc192)
- [bt_conn_le_min_conn_interval_group](../bluetooth_connection_model_reference/P024_bt_conn_le_min_conn_interval_group_结构体.md)
- [min_125us](../bluetooth_connection_model_reference/P024_bt_conn_le_min_conn_interval_group_结构体.md#a44c7e6e9983d607fdde9cafe8cb595e1)
- [max_125us](../bluetooth_connection_model_reference/P024_bt_conn_le_min_conn_interval_group_结构体.md#a3d48e4889d3e039fc19da55c40efc911)
- [stride_125us](../bluetooth_connection_model_reference/P024_bt_conn_le_min_conn_interval_group_结构体.md#aed08c6c6bbe9f4bfae0a5e0c8ad6e9f3)
- [bt_conn_le_min_conn_interval_info](../bluetooth_connection_model_reference/P025_bt_conn_le_min_conn_interval_info_结构体.md)
- [min_supported_conn_interval_us](../bluetooth_connection_model_reference/P025_bt_conn_le_min_conn_interval_info_结构体.md#aa39299ca32657e9f684e88875e7517dc)
- [num_groups](../bluetooth_connection_model_reference/P025_bt_conn_le_min_conn_interval_info_结构体.md#ac0d63f57518324d81509fea51fcefa60)
- [groups](../bluetooth_connection_model_reference/P025_bt_conn_le_min_conn_interval_info_结构体.md#ad9e6ae7c5632e4cc2a5e5eda52d2e0e8)
- [BT_CONN_LE_MAX_CONN_INTERVAL_GROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gadcb74ad947485dd81dfd59a82d3b0db6)
- [bt_conn_le_conn_rate_param](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md)
- [interval_min_125us](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#a264baeb210c9cbd559f0cd3ed2cd78b1)
- [interval_max_125us](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#a9afcc899991204f17c1390b9362ec54b)
- [subrate_min](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#aed9238960e4be8ddbeff53afab74ef6f)
- [subrate_max](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#a751042149cb8ff1ec28de10fe1e4c8bd)
- [max_latency](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#afb3fa1a4202c39a9551dd41396595771)
- [continuation_number](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#adf4c1069b5aa3b8afb09ea8b59d93eca)
- [supervision_timeout_10ms](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#a50a3c9eca10ed5c11773aaf07e1fbc12)
- [min_ce_len_125us](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#ae4734b6d8f0f4903624e47e975828482)
- [max_ce_len_125us](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#aa764837e74aac1feba2025cf01a87d85)
- [bt_conn_le_conn_rate_changed](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [interval_us](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md#aa6dfef1425c47823897b8b84de17ecf9)
- [subrate_factor](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md#ab2b60e61438b0d814c9a8a8adcae35fc)
- [peripheral_latency](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md#a768af259e8d37f463278946bd660ce58)
- [continuation_number](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md#a348cc25c2f19bab8c5e140b712b3034a)
- [supervision_timeout_10ms](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md#a47d662c1e00e8c4e1a553d9a4909f6df)
- [bt_conn_le_read_all_remote_feat_complete](../bluetooth_connection_model_reference/P030_bt_conn_le_read_all_remote_feat_complete_结构体.md)
- [status](../bluetooth_connection_model_reference/P030_bt_conn_le_read_all_remote_feat_complete_结构体.md#a0dbbd0144cc6990b45d662896862cce7)
- [max_remote_page](../bluetooth_connection_model_reference/P030_bt_conn_le_read_all_remote_feat_complete_结构体.md#a1554bd9035619cc4dbdb2d04fd9105ad)
- [max_valid_page](../bluetooth_connection_model_reference/P030_bt_conn_le_read_all_remote_feat_complete_结构体.md#a996e2600fd41bf1b6d95b6ee5873f6ce)
- [features](../bluetooth_connection_model_reference/P030_bt_conn_le_read_all_remote_feat_complete_结构体.md#a7a8db1d0c0656e8953da8b8aa4bec2c7)
- [bt_conn_le_frame_space_update_initiator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae60f156d2aa01814ad485786e00c4ca7)
- [BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggae60f156d2aa01814ad485786e00c4ca7aabb0edb792a8fbfe91f8a8847672b67c)
- [BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a076869aba2dc8593b2263c642cdaa148)
- [BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggae60f156d2aa01814ad485786e00c4ca7a9fae7a5909e7c6974361ab71be717495)
- [BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a45ff3a04cd0179ed02576136114ed8c0)
- [BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggae60f156d2aa01814ad485786e00c4ca7a8ce5e76ef31654408105b5505f63a4c4)
- [BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#acb1d2b1b3e2e1802b81dbeb82bcc9f12)
- [bt_conn_le_frame_space_update_param](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md)
- [phys](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md#a67adb4f731d9a1822b400af9f30bcf43)
- [spacing_types](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md#a1e5bd6b331c1c7c4881e2875b1adfd3d)
- [frame_space_min](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md#a7d3f1ee0c43797ab100b24c3919f304f)
- [frame_space_max](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md#a90e83dca82b557ef1476d5e4919fb170)
- [bt_conn_le_frame_space_updated](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md)
- [status](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md#a126026dba0cb84ceaf10324212bbf3e0)
- [initiator](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md#af6b88c108be375ea80466ece72257f2e)
- [frame_space](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md#af1918fb7b4abc7f7b3eb11c33a3190f6)
- [phys](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md#a332a93e2d05750bd241e137381186f8b)
- [spacing_types](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md#a7cb3366670e07d06a466c3c7eb885b09)
- [bt_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab8dde20ae75b51f1e28dbeed06001f20)
- [BT_CONN_TYPE_LE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2)
- [BT_CONN_TYPE_BR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6)
- [BT_CONN_TYPE_SCO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953)
- [BT_CONN_TYPE_ISO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee)
- [BT_CONN_TYPE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836)
- [bt_conn_le_cs_capability_rtt_aa_only](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gafe14d64a64383b097760764697b035e2)
- [BT_CONN_LE_CS_RTT_AA_ONLY_NOT_SUPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggafe14d64a64383b097760764697b035e2a288abc3e9a886eb3ab2b8f32c7913d94)
- [BT_CONN_LE_CS_RTT_AA_ONLY_10NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggafe14d64a64383b097760764697b035e2af81e06eb920435cc68ccfa3ee6cee34a)
- [BT_CONN_LE_CS_RTT_AA_ONLY_150NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggafe14d64a64383b097760764697b035e2a788566d99b00e42f48aceb7d7c0229e6)
- [bt_conn_le_cs_capability_rtt_sounding](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1892ec23ca3b1818287a9d7dafc16433)
- [BT_CONN_LE_CS_RTT_SOUNDING_NOT_SUPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga1892ec23ca3b1818287a9d7dafc16433a9d4f71899fb3ad7212fe3f544bd55d14)
- [BT_CONN_LE_CS_RTT_SOUNDING_10NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga1892ec23ca3b1818287a9d7dafc16433aaafb75f1fab71f3f1daee1db96fc44bb)
- [BT_CONN_LE_CS_RTT_SOUNDING_150NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga1892ec23ca3b1818287a9d7dafc16433a529c39021229684361aeb33251b2c584)
- [bt_conn_le_cs_capability_rtt_random_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5568443825fc1ce9534753d8918aa813)
- [BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_NOT_SUPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga5568443825fc1ce9534753d8918aa813acd51ea3eb01cb91c9fda392af42bcd2d)
- [BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_10NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga5568443825fc1ce9534753d8918aa813ab79f96814227514fe5aeeee21a219741)
- [BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_150NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga5568443825fc1ce9534753d8918aa813af50e6d16f23f5b12e41a9c6fce8716db)
- [bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)
- [num_config_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a77aacfd02b354e04d4cc29cc1bf4b779)
- [max_consecutive_procedures_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#ae76fbc0f88525e83717e1d8ef5acae59)
- [num_antennas_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a4e4c56c5066d02b2a0cd59c067f1e4b9)
- [max_antenna_paths_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#ac842e123166008ad1ad663f827937a3b)
- [initiator_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a6530d2a3fb66d498711856b723acecb7)
- [reflector_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a694119619d359d0b7e298edf6201ee20)
- [mode_3_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#aa1616417e6183cf283cf96efc9a92b8e)
- [rtt_aa_only_precision](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a46c9168328d3fbc98a2625799c733818)
- [rtt_sounding_precision](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#acef0d65ed55ae304fea47006bfb0076f)
- [rtt_random_payload_precision](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#abbefdc0268a775712c7abd664adcb6b2)
- [rtt_aa_only_n](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#abe3c611316bb5f710f355846ee9ec437)
- [rtt_sounding_n](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a7f35343a1572800850e791ba3ff5ffb1)
- [rtt_random_payload_n](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a345d9e43222d77024a8f4283b274b48f)
- [phase_based_nadm_sounding_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a94fd00a7a9b22d649f75c7fdd17590a9)
- [phase_based_nadm_random_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a1a0076a0c97317803976f4aca86afc0d)
- [cs_sync_2m_phy_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a3fd09db5fae9c5e307994a78131199c6)
- [cs_sync_2m_2bt_phy_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a6513d8ffe7d168441205f6dd656dcbbc)
- [cs_without_fae_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a22604c052da2f8ccf77c81a0a5c628b7)
- [chsel_alg_3c_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#aba0db15183d4fa4ae0e3f1333202e55e)
- [pbr_from_rtt_sounding_seq_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#ad57f15b4dda88e2b747f30451601c923)
- [cs_ipt_reflector](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#adfac38e7771604971a82ece149c1d337)
- [t_ip1_times_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a090f869cfe7e39a70cea94afbd5ac376)
- [t_ip2_times_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#ae93594f360430e9c0c80cf3edcf570f6)
- [t_fcs_times_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a1ff1d7d769e3ba915f91bf672a6f8a61)
- [t_pm_times_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a6e92391b21d4acaebba8a171643f572f)
- [t_sw_time](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a5a86629a5ad4203b5efe3802cd8b6ae7)
- [tx_snr_capability](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#ad58deea7a825bb5f0bc2ca0034183948)
- [t_ip2_ipt_times_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a21262b0e588a75146f2d0c325d0b5cc1)
- [t_sw_ipt_time_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a97b42928bcba43a6d90e8139efce0870)
- [bt_conn_le_cs_fae_table](../bluetooth_connection_model_reference/P016_bt_conn_le_cs_fae_table_结构体.md)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [remote_fae_table](../bluetooth_connection_model_reference/P016_bt_conn_le_cs_fae_table_结构体.md#a9d4a2fe09edc897143b6e479f30b7f65)
- [bt_conn_le_cs_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f757b15d1d5006ce2fa6a7a78082156)
- [BT_CONN_LE_CS_MAIN_MODE_1_NO_SUB_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156a78b56a5342bf31a57de235dddf5e499a)
- [BT_HCI_OP_LE_CS_MAIN_MODE_1](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#af1b7924e50ba017e59d697fd8814d491)
- [BT_CONN_LE_CS_MAIN_MODE_2_NO_SUB_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156a8f5842c33912ea291388ae380e54565a)
- [BT_HCI_OP_LE_CS_MAIN_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a714152a085bbc317b539d6e973ccffc6)
- [BT_CONN_LE_CS_MAIN_MODE_3_NO_SUB_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156a43e2dea6e52df54423bb7a6aaabcbdbf)
- [BT_HCI_OP_LE_CS_MAIN_MODE_3](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a5d2af0ed5e0cc5cf7d9f0baae512ff68)
- [BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156ac4f05c5aea07cfc19a606caebd7201f7)
- [BT_HCI_OP_LE_CS_SUB_MODE_1](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a219243d501bbcb6d62668398cde79fca)
- [BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156ad6df550b1f4908268752841224bbab26)
- [BT_HCI_OP_LE_CS_SUB_MODE_3](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a4b48c199b6b75e9dd62ec36883b40aa4)
- [BT_CONN_LE_CS_MAIN_MODE_3_SUB_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156a35b1c587320f31ec1c1bcfe6913c57ac)
- [BT_HCI_OP_LE_CS_SUB_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ada09c787fca0a1d54bb754635489b51e)
- [bt_conn_le_cs_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0e6f6d4fdbdfc3ed75fef4a95136076f)
- [BT_CONN_LE_CS_ROLE_INITIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga0e6f6d4fdbdfc3ed75fef4a95136076fad3172d9c6319a579ee9923f3d28279f4)
- [BT_CONN_LE_CS_ROLE_REFLECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga0e6f6d4fdbdfc3ed75fef4a95136076fa5fbcf5ba6c42da7deca9f92d6b92c968)
- [bt_conn_le_cs_rtt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaffd6abf9b92cc8d8463797a73b840f51)
- [BT_CONN_LE_CS_RTT_TYPE_AA_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51aa9b85139381d29cdfb6adb756544e088)
- [BT_HCI_OP_LE_CS_RTT_TYPE_AA_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a759eb7a8e43ee7cf1ea88ddd3e69feb5)
- [BT_CONN_LE_CS_RTT_TYPE_32_BIT_SOUNDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51a6350cf2f1d91e496ec49ddd09f7044fc)
- [BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#aa2ae18252a20ef3481d2402f8924cdda)
- [BT_CONN_LE_CS_RTT_TYPE_96_BIT_SOUNDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51a243bb67b834cda207b61cc7ea65bdab2)
- [BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a73cbfe2a942b684ac0b5b50d900fb83f)
- [BT_CONN_LE_CS_RTT_TYPE_32_BIT_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51ac05977c1622cc7383a1035a63b33ecad)
- [BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_RAND](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#abe4efee7cf9371129f4b5bd650b0d64a)
- [BT_CONN_LE_CS_RTT_TYPE_64_BIT_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51ae14f994d1c3329695d0257caffd20f91)
- [BT_HCI_OP_LE_CS_RTT_TYPE_64BIT_RAND](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a77e56fd5302673f6ef295c0cceabdc9f)
- [BT_CONN_LE_CS_RTT_TYPE_96_BIT_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51ab0d60b2e7e26ab862df16d926fc2198f)
- [BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_RAND](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#aa60f64ff7259fd79fb1da2c063530348)
- [BT_CONN_LE_CS_RTT_TYPE_128_BIT_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51a8edae9d98c26da94ec152fa1f1f690f5)
- [BT_HCI_OP_LE_CS_RTT_TYPE_128BIT_RAND](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a1fe5e94fbd1156c8196c8e1ab9816bac)
- [bt_conn_le_cs_sync_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaadbf6a4dba28aec90ea07b7da634e1bb)
- [BT_CONN_LE_CS_SYNC_1M_PHY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaadbf6a4dba28aec90ea07b7da634e1bba4ff9aa9e9c41dbdc288360d354775e95)
- [BT_HCI_OP_LE_CS_CS_SYNC_1M](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7baf90f5bf691ce6b650677e6c2a9600)
- [BT_CONN_LE_CS_SYNC_2M_PHY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaadbf6a4dba28aec90ea07b7da634e1bbaa0fc3809d1d71f4fdfe632ffe0a57cd6)
- [BT_HCI_OP_LE_CS_CS_SYNC_2M](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ae49d35db87532e06ea685a63eb89177a)
- [BT_CONN_LE_CS_SYNC_2M_2BT_PHY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaadbf6a4dba28aec90ea07b7da634e1bbaba211d71eb3eccecb93b8e5b4e956e7b)
- [BT_HCI_OP_LE_CS_CS_SYNC_2M_2BT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ac34716156b071e06eb454f091a63216c)
- [bt_conn_le_cs_chsel_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga34e4837a77c7afd6999095985ddad4f0)
- [BT_CONN_LE_CS_CHSEL_TYPE_3B](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga34e4837a77c7afd6999095985ddad4f0ac0d5b6a9d1a0c02fce0472b07ec6b0f1)
- [BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3B](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a77d27762b9faa7743a55d822a1839eac)
- [BT_CONN_LE_CS_CHSEL_TYPE_3C](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga34e4837a77c7afd6999095985ddad4f0ab2dde3a39fba7129203fc9afc23a5bd6)
- [BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3C](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#af17f867204bc7cf99e5d530c39302be0)
- [bt_conn_le_cs_ch3c_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf2331ec1f1222de51fc4f30566e1c52b)
- [BT_CONN_LE_CS_CH3C_SHAPE_HAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf2331ec1f1222de51fc4f30566e1c52ba1235210de336af7cac9777d2f91408ea)
- [BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_HAT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#acd33fc2eb3f5ebe10cbe4c5060f8336b)
- [BT_CONN_LE_CS_CH3C_SHAPE_X](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf2331ec1f1222de51fc4f30566e1c52ba5ddc8d83fa6f143b985bd2f891018622)
- [BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_X](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ad09c735ab352d7a546cade296e915e85)
- [bt_conn_le_cs_config](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md)
- [id](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#aaf8f1ce04fd22b4ca4728bdcfce8bd4a)
- [mode](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#ab59b31730b91f843e5b8a156d98da42d)
- [min_main_mode_steps](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a2e59fb17cd932b7670b3e915684c2107)
- [max_main_mode_steps](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#aff70b37fac8a3bd94acb25d7bd06989b)
- [main_mode_repetition](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a2e904438c579870ed96b5dccff239c18)
- [mode_0_steps](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a8eea68bffef759b4532b68a1ecbdd4f1)
- [role](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#ad11f8bee028ad3eb59008d46dce2d5bd)
- [rtt_type](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a194e3844373c57e714917d03ac82666d)
- [cs_sync_phy](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a2051f559b41085c4b41743aaaaecf3a1)
- [channel_map_repetition](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a971ff7ba734dd71512af7f3850de364d)
- [channel_selection_type](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a63b7027929a5c3ec7fd68f35343262ee)
- [ch3c_shape](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a9b64ecb0986e7e9995c29feaf105eeaa)
- [ch3c_jump](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#afa2846689f1a9d5b9e124b1c9095154f)
- [cs_enhancements_1](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#acfccd404abced1c5f5490130f2f77f23)
- [t_ip1_time_us](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#aab9a1d8d09d7a439f1c4dd28b9dd05c4)
- [t_ip2_time_us](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a8e650b50400a45040c02a88dfb30683c)
- [t_fcs_time_us](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a29912bd291fa4da09bb5b196d747ca6b)
- [t_pm_time_us](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#ae7f1cc232df00b4543fdb2b2596b9bbf)
- [channel_map](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a60f9d21629554d47556d0fe8d63dcae3)
- [bt_conn_le_cs_procedure_done_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9a1dc2010c5237466de87160944630d3)
- [BT_CONN_LE_CS_PROCEDURE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9a1dc2010c5237466de87160944630d3a17689e9502318b16c35a4792ecc6e73f)
- [BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ace872d54fba6d94d62b59a2373c7d0d5)
- [BT_CONN_LE_CS_PROCEDURE_INCOMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9a1dc2010c5237466de87160944630d3a295b2e0d0fff2ea730a00e7916065b82)
- [BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_PARTIAL](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#af057e8492e52d0c8763d4a2e969d949d)
- [BT_CONN_LE_CS_PROCEDURE_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9a1dc2010c5237466de87160944630d3a0ff236987e96f368c09944a9074f8f7b)
- [BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a821a29dacea9867e4e576f916cf7be3d)
- [bt_conn_le_cs_subevent_done_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8e54a191b889b1d5ed3e1fbb648d9bc7)
- [BT_CONN_LE_CS_SUBEVENT_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga8e54a191b889b1d5ed3e1fbb648d9bc7a900282c089ca30323171da1a0e0e0146)
- [BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#aee251ce3c46dc0404d880be7d4550fa6)
- [BT_CONN_LE_CS_SUBEVENT_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga8e54a191b889b1d5ed3e1fbb648d9bc7a5943689e3233bc87054dbd9f54042202)
- [BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#af1907f8ae481a08c674d86e689826f49)
- [bt_conn_le_cs_procedure_abort_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3196a0eb1c7497e93d7c646713d2fc79)
- [BT_CONN_LE_CS_PROCEDURE_NOT_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79ac1ef74618cb45abd9161cd4d9141570d)
- [BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_NO_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a056a67d663cfdc2189b480fc79946c74)
- [BT_CONN_LE_CS_PROCEDURE_ABORT_REQUESTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79a0a5f18ca51c837f9621d0212997b2ce0)
- [BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a21eb191c5d99f902c7a244cad685995f)
- [BT_CONN_LE_CS_PROCEDURE_ABORT_TOO_FEW_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79a9aa1742041d4958399bb411982c3bc02)
- [BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_TOO_FEW_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6dc3f766ce40bbd0ddb7af3cf85677b1)
- [BT_CONN_LE_CS_PROCEDURE_ABORT_CHMAP_INSTANT_PASSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79af817bbbc221a3615da50e14c14086744)
- [BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_CHMAP_INSTANT_PASSED](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ae8446a2638bd4009b7dee725bb54c883)
- [BT_CONN_LE_CS_PROCEDURE_ABORT_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79ade9e8345ff7946844ba7df3e7379a886)
- [BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a1e92177f7be3c6a6be00f97fbfc17dcf)
- [bt_conn_le_cs_subevent_abort_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga6394906c6da40c9bebfaeb05de9fd5be)
- [BT_CONN_LE_CS_SUBEVENT_NOT_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5bea30b6d4dc4a32556cedd61ed1bbfbf12c)
- [BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a095b6061c31229b951b6b96e5d02381f)
- [BT_CONN_LE_CS_SUBEVENT_ABORT_REQUESTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5bea938fcb8be6a45efce064c881bc668f8d)
- [BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a41bbe08db99fb0a2ef77f4f3103f9b6c)
- [BT_CONN_LE_CS_SUBEVENT_ABORT_NO_CS_SYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5beabacfa9f390d61d7471c81669bcc0243d)
- [BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_CS_SYNC_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ac4817c265c50019d8f74146f7477bf58)
- [BT_CONN_LE_CS_SUBEVENT_ABORT_SCHED_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5beabaafdce9a596454fe4f23c50afba2ddd)
- [BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_SCHED_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a31cb520a05fe31313bacf8b021da468c)
- [BT_CONN_LE_CS_SUBEVENT_ABORT_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5bea30c5743ef2b358390fd93bd775f72bc3)
- [BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#abfdca3ae615e19c8e24c098ba8349618)
- [bt_conn_le_cs_subevent_result](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md)
- [config_id](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#aa4c770ab2db8d4ab665ad50f7edd5bfa)
- [start_acl_conn_event](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a7706d0dfd7246d4cf193a8a9e7b6305d)
- [procedure_counter](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a0f8fc918f8eb31c47acf51885c7add08)
- [frequency_compensation](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a967d37f37d0e1596984fdda34609a3b3)
- [reference_power_level](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#acbfc5e80a2fb82072d9376e996f7969f)
- [procedure_done_status](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#adf60893d9229003d1eefc552a4957b65)
- [subevent_done_status](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a45b22c6c2252e2afa28ee8b1bfed3ecf)
- [procedure_abort_reason](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a778c89f57ef50f612654243ba673ba3f)
- [subevent_abort_reason](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#aef5ba53497c4d1576c9ecec1b5dea289)
- [num_antenna_paths](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a3597697ae4acdd8f7c009bececab6a65)
- [num_steps_reported](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a3bffc0935a5410d75d0050337e4fad27)
- [abort_step](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a9bfcc6dcaa191c7f56958ef88926b51e)
- [header](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a1a90563a8c93f9b309e88fd771a7cec4)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [step_data_buf](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a6948c4a8c5882cb1d1b04a2b390fda8c)
- [bt_conn_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga060d51eb2208de6f805b1fc0672d2d0c)
- [bt_conn_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b18c6b22a9f02be0d7d078b2ce51ff6)
- [bt_conn_take](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf073384538a67c242b00150904176f66)
- [atomic_ptr_clear](../atomic_reference/P001_原子操作公共接口.md#ga587e3134cd8176e7b1c00361711ee2df)
- [atomic_ptr_t](../atomic_reference/P001_原子操作公共接口.md#gacad6866fa4c844026cd9f8c3fb60ecd7)
- [bt_conn_drop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf1aeec9b9893450423cf066a6f471824)
- [bt_conn_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5bdf8e8efc85138d3631dc1efffc3916)
- [bt_conn_lookup_addr_le](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1bfe349efd8a7de31e9457fe439d746a)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_conn_get_dst](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga77108581b8f61485ca840e4bf7a17087)
- [bt_conn_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gad4aed76b80cc815f748ad0e84ae3d87c)
- [bt_conn_le_info](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md)
- [src](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a5f1eacec82f31182460d6d5359a8b295)
- [dst](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a1f78e1c0ed3482ce6eec9ce6eeda4769)
- [local](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a3be5df0deb0af08f84843eb3c6a5e5ae)
- [remote](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a236d1c97c735c7cfaead0b1a3672d512)
- [interval_us](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a3bede29a6a5df282bde6a26f50ea9aee)
- [interval](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a95a1f635e53f16d5839cdd58f4bda962)
- [latency](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#acd83835fe5ec0878fd653b87cb570a49)
- [timeout](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#afb4dc594d063fbbad2bcd4acf047f716)
- [phy](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a215d39c6cd7da1ac033529b5541cbfc1)
- [data_len](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#ae309f390c8d7b33a4de55791af235ab0)
- [subrate](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a5d97a2eb4aa880abe857f19adeea425d)
- [bt_conn_br_info](../bluetooth_connection_model_reference/P006_bt_conn_br_info_结构体.md)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [dst](../bluetooth_connection_model_reference/P006_bt_conn_br_info_结构体.md#aeef49f711872ccfec5dd558c4552b71e)
- [bt_conn_sco_info](../bluetooth_connection_model_reference/P040_bt_conn_sco_info_结构体.md)
- [link_type](../bluetooth_connection_model_reference/P040_bt_conn_sco_info_结构体.md#aad5fc309d1ffccda38c07b40ac028dd1)
- [air_mode](../bluetooth_connection_model_reference/P040_bt_conn_sco_info_结构体.md#ae4474ebfe0129eb6214987a31430d4f7)
- [BT_CONN_ROLE_CENTRAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30)
- [BT_CONN_ROLE_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0)
- [bt_conn_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9442c1479db60e2db40a2ea6de565282)
- [BT_CONN_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587)
- [BT_CONN_STATE_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd)
- [BT_CONN_STATE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f)
- [BT_CONN_STATE_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f)
- [BT_SECURITY_L0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e)
- [BT_SECURITY_L1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b)
- [BT_SECURITY_L2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a)
- [BT_SECURITY_L3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631)
- [BT_SECURITY_L4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81)
- [BT_SECURITY_FORCE_PAIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [bt_security_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f8712bbf3410de5cbe6ce489fe30e5e)
- [BT_SECURITY_FLAG_SC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6)
- [BT_SECURITY_FLAG_OOB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198)
- [bt_security_info](../bluetooth_connection_model_reference/P130_bt_security_info_结构体.md)
- [level](../bluetooth_connection_model_reference/P130_bt_security_info_结构体.md#a7b18849fad25b3f2da6b8c85a56d86e1)
- [enc_key_size](../bluetooth_connection_model_reference/P130_bt_security_info_结构体.md#a6567ffb82b7fa8093cc57ef4662873ba)
- [flags](../bluetooth_connection_model_reference/P130_bt_security_info_结构体.md#a99cb4af08bfa1dab182821d956368526)
- [bt_conn_info](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md)
- [type](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#a7995e1291be494b5bdf860eceea0cad1)
- [role](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#a8237b8c1bb9a97a174d04cbe13dca7c7)
- [id](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#a3a4e24519b5d3ba547423e53c4d92a5c)
- [le](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#a6b536e7732dcf7b77a7bc05116dca548)
- [br](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#a799e59d3a85625799a32ac3f0b3d67d1)
- [sco](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#ad622c69f262ee53ec94918857250a2a0)
- [state](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#ae566e2382b69ff27314dc1dd632dbdbc)
- [security](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#ae4405f1b4f3fe2ff6253453964860931)
- [bt_conn_le_remote_info](../bluetooth_connection_model_reference/P031_bt_conn_le_remote_info_结构体.md)
- [features](../bluetooth_connection_model_reference/P031_bt_conn_le_remote_info_结构体.md#a4ff434f6c501dc60db5c4b776be46b3b)
- [bt_conn_br_remote_info](../bluetooth_connection_model_reference/P007_bt_conn_br_remote_info_结构体.md)
- [features](../bluetooth_connection_model_reference/P007_bt_conn_br_remote_info_结构体.md#afa19f7db400bb0de234e8cda61f3deaf)
- [num_pages](../bluetooth_connection_model_reference/P007_bt_conn_br_remote_info_结构体.md#a798c179c803e709182a1b0c3594f4a0a)
- [bt_conn_remote_info](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md)
- [type](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md#a8bb514196bde5df561dbf76b68060729)
- [version](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md#a2664f6ed3bd22f9a011126daf5d81376)
- [manufacturer](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md#a47cc5a4b8888a0b8faaf6880c37418b8)
- [subversion](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md#a360979a15c958706157fc630fd55cbca)
- [le](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md#ae75530b09c6dea416630a4a19a1d64cc)
- [br](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md#ab73365f09cdb5ce870272546543bcfeb)
- [bt_conn_le_tx_power_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga737d8118f8aba8985292d92d0604b190)
- [BT_CONN_LE_TX_POWER_PHY_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a)
- [BT_CONN_LE_TX_POWER_PHY_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046)
- [BT_CONN_LE_TX_POWER_PHY_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800)
- [BT_CONN_LE_TX_POWER_PHY_CODED_S8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2)
- [BT_CONN_LE_TX_POWER_PHY_CODED_S2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296)
- [bt_conn_le_tx_power](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md)
- [phy](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md#a8702c4ff5082b8f90decdfabfb8253fe)
- [current_level](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md#a6d2e5a5215fa5d60630e74928a67fc04)
- [max_level](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md#a1674247c511906fa6f0193653ed0b71a)
- [bt_conn_le_tx_power_report](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md)
- [reason](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md#aa5606925229784af8ae90542432cf200)
- [phy](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md#a5b1f67537fbe945f2f258b47082723b4)
- [tx_power_level](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md#ace830ddb7ae662c9759babed87f1b6f3)
- [tx_power_level_flag](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md#ae7a4f77c6f7af1a459896d25cf661eb8)
- [delta](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md#a7c681c7b9f77d994b2de1febea7c5dc9)
- [bt_conn_le_path_loss_zone](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e)
- [BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea17765999979bb1bac00769ea742d53d8)
- [BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_MIDDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea06bd101d7cc98d39403ed16719542dec)
- [BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea19fd0c4702ca5e08c8cbfb51b34bb705)
- [BT_CONN_LE_PATH_LOSS_ZONE_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea684ce653c5fffe9d49316d22904d3942)
- [BT_HCI_LE_ZONE_ENTERED_LOW](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#aff1538e314a97aa4910d4f7066dc4d55)
- [BT_HCI_LE_ZONE_ENTERED_MIDDLE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ab88f3d713f6862c08b73752436ca8b1b)
- [BT_HCI_LE_ZONE_ENTERED_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#af7cc15be8165315ee0358ebb517b5e33)
- [bt_conn_le_path_loss_threshold_report](../bluetooth_connection_model_reference/P027_bt_conn_le_path_loss_threshold_report_结构体.md)
- [zone](../bluetooth_connection_model_reference/P027_bt_conn_le_path_loss_threshold_report_结构体.md#ab2b71b7ddccc40ced56657a548b98e77)
- [path_loss](../bluetooth_connection_model_reference/P027_bt_conn_le_path_loss_threshold_report_结构体.md#abe631b07816d6c18bacba64bfbd1e844)
- [bt_conn_le_path_loss_reporting_param](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md)
- [high_threshold](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md#a5cc7a17efee69d61b8f8d0c242321054)
- [high_hysteresis](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md#aec49adc896604d878060b03bd40ab0f4)
- [low_threshold](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md#a634c08e573cffd97a94ad681bed9239e)
- [low_hysteresis](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md#af8e70508a39ee73b75a4769769aa303f)
- [min_time_spent](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md#a6fec4497c6fd95fa6f265bd859976c9d)
- [bt_conn_auth_keypress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga57465d3a61214531ddaffc2c30939043)
- [BT_CONN_AUTH_KEYPRESS_ENTRY_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6)
- [BT_CONN_AUTH_KEYPRESS_DIGIT_ENTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1)
- [BT_CONN_AUTH_KEYPRESS_DIGIT_ERASED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529)
- [BT_CONN_AUTH_KEYPRESS_CLEARED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da)
- [BT_CONN_AUTH_KEYPRESS_ENTRY_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8)
- [bt_conn_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2de54f2ac83f0d8dca2a85a9fbfadcaa)
- [BT_ADDR_LE_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gae0df0067c55eb4388625bb62f3d7e235)
- [bt_conn_is_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf3d55f1f8efc630b495389ced3ee3fa5)
- [bt_conn_get_remote_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac4e0bd799fc87b65367129685f57c2bd)
- [bt_conn_le_get_tx_power_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa5289154bc508444f68df7abcef18aca)
- [bt_conn_le_enhanced_get_tx_power_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa79eada87d698f4998af876d03d7e92b)
- [bt_conn_le_get_remote_tx_power_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0843a2e0b6f16ebd132a3a512cfd27a4)
- [bt_conn_le_set_tx_power_report_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa1f38911acee0534a8a6e414018c6fb6)
- [bt_conn_le_set_path_loss_mon_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga6be5f3bf064ba03dc2307fdd2b634637)
- [bt_conn_le_set_path_loss_mon_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga90ae27bcc6f71f32be56efe8ecbc165d)
- [bt_conn_le_subrate_set_defaults](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac7bb456c530c7e08b4fa9f4d478fdaf9)
- [bt_conn_le_subrate_request](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga754ed218fe9577f2d0ef6d508cfc5a0b)
- [bt_conn_le_read_min_conn_interval_groups](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2e7e836d94a5330ae01e14dbd3e29f14)
- [bt_conn_le_read_min_conn_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9af26600acdf5b3a8b8ea0a32e14b497)
- [bt_conn_le_conn_rate_set_defaults](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac9b111639f9b982cd97e13f313e51461)
- [bt_conn_le_conn_rate_request](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2e4188482deeda71f8e5d42a07538f31)
- [bt_conn_le_read_all_remote_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac0dbbdb95ef868f35006622932dc8901)
- [bt_conn_le_frame_space_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab734fbc307eff3c5bddf7c5e6ddd341b)
- [bt_conn_le_param_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab44a964725f54ed2d37de17c6e2fd3eb)
- [bt_conn_le_data_len_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8a2006f6e34b20c7e8ef65a73f431a57)
- [bt_conn_le_phy_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae13ed81b1e7928f44b8fdf85995b3e58)
- [bt_conn_le_set_default_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga7c8e7a7616e7b56f97da7ff4bc0fc7ba)
- [bt_conn_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga14e7c852b0271781594e742ae509c5d3)
- [BT_CONN_LE_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9)
- [BT_CONN_LE_OPT_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b)
- [BT_CONN_LE_OPT_NO_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9)
- [bt_conn_le_create_param](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md)
- [options](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md#a4b1e26c0976d9c900b831c886c77b055)
- [interval](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md#a5cfae677f924534dc5bc7b38c457a7af)
- [window](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md#a339b99f65c5029ada6cdf453ab1f258e)
- [interval_coded](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md#a2bc978ac97435fe5f87c6e01692f2910)
- [window_coded](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md#ae62491837d35d95e32016b793edf8c96)
- [timeout](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md#a59f05bfb9468779d02f8d0beeb7a35c1)
- [bt_conn_le_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8d66f3e0262a51279e9fa8b3139252e6)
- [bt_conn_le_create_synced_param](../bluetooth_connection_model_reference/P013_bt_conn_le_create_synced_param_结构体.md)
- [peer](../bluetooth_connection_model_reference/P013_bt_conn_le_create_synced_param_结构体.md#ac5872dda4042e3ba6c161dce60784b70)
- [subevent](../bluetooth_connection_model_reference/P013_bt_conn_le_create_synced_param_结构体.md#ac7b4e4144aaf914bdef1dc305b5e297f)
- [bt_conn_le_create_synced](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga98f99c893e444d1ad1ecd9139803c0b1)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_conn_le_create_auto](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaecfaf2cb44772511dbb585de8f76f09b)
- [bt_conn_create_auto_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga62dc2663b4fa39a33adb76dc9a136aa4)
- [bt_conn_set_security](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae001f1268e1ff42c3c974c95dcb6735d)
- [bt_conn_get_security](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b43ef0f30146808e560991a302e88ad)
- [bt_conn_enc_key_size](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaff3e6aa16b68e5da7dab53289295545e)
- [bt_security_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9420ff489fd5857ff076406442679ff)
- [BT_SECURITY_ERR_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05)
- [BT_SECURITY_ERR_AUTH_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7)
- [BT_SECURITY_ERR_PIN_OR_KEY_MISSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171)
- [BT_SECURITY_ERR_OOB_NOT_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7)
- [BT_SECURITY_ERR_AUTH_REQUIREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae)
- [BT_SECURITY_ERR_PAIR_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6)
- [BT_SECURITY_ERR_PAIR_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f)
- [BT_SECURITY_ERR_INVALID_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5)
- [BT_SECURITY_ERR_KEY_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216)
- [BT_SECURITY_ERR_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242)
- [bt_conn_le_cs_procedure_enable_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf3653de72793f775e33fd9eb04c3e7a2)
- [BT_CONN_LE_CS_PROCEDURES_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf3653de72793f775e33fd9eb04c3e7a2aa24f08ba114af2ac928087527d514c83)
- [BT_HCI_OP_LE_CS_PROCEDURES_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a3e01bbe3a72c946015a288ee49d3cbdd)
- [BT_CONN_LE_CS_PROCEDURES_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf3653de72793f775e33fd9eb04c3e7a2a35ab078fac9e0ef608ca87c2a3db63ac)
- [BT_HCI_OP_LE_CS_PROCEDURES_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a4a88120ae7e83fd791012c913315d14f)
- [bt_conn_le_cs_tone_antenna_config_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab7acdbdf273fc760799cf0d8cf71591c)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca3bdbab03ae31a6340a10066476e9edac)
- [BT_HCI_OP_LE_CS_ACI_0](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a92e1ec21014999f40172fa1812c36575)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591caeb8a8776c0e54eada45de6a45f6ee1ea)
- [BT_HCI_OP_LE_CS_ACI_1](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a5b082fa5b8ba11a651468cc516d067fe)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A3_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca957116fdc29742ec8e75284bbaa726b7)
- [BT_HCI_OP_LE_CS_ACI_2](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ab30a4e55002080394c39fb885eba36e4)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A4_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591cabc273bf65c87ff09f72f85e8f0160bb7)
- [BT_HCI_OP_LE_CS_ACI_3](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a76d1452003c0bd3b688765aa2d25047f)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca92ac9a31531c26a23bd1b268e68815ba)
- [BT_HCI_OP_LE_CS_ACI_4](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#af16c4c79e602e6da833b8aa3e0c4bf64)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca6908e64a2774e0ddeca4b510ee56de33)
- [BT_HCI_OP_LE_CS_ACI_5](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ad980d8f134d940b80dc9b0e3a570ac06)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca9253d001290986ae07a262260a01fafb)
- [BT_HCI_OP_LE_CS_ACI_6](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a4c7ff3c949023f4544bf50353a0f082b)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca5745021b56f9da077db312f104e855b2)
- [BT_HCI_OP_LE_CS_ACI_7](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#acabccf9f5893324dcb6acc0769ab8417)
- [bt_conn_le_cs_procedure_enable_complete](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md)
- [config_id](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#a2e290c25ec5af8b0259d45f04d6c543d)
- [state](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#acc1d12d347e1b02b2eea562ea064a40b)
- [tone_antenna_config_selection](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#a3fa8ad4dd264eb4e2489dea9c1048d22)
- [selected_tx_power](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#aeb918e438cd02296c7f693757268f6bf)
- [subevent_len](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#ae990a10c468ec62fbaf9325c94733c7c)
- [subevents_per_event](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#a40b03220932852b6b51d65f557c21f17)
- [subevent_interval](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#a77a2bd8ee384c4567321a09f6b64782c)
- [event_interval](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#a4129ab9519ba140ffb198aa9a5cde6ac)
- [procedure_interval](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#a8511deef97f19c53ddaa4dec8492658f)
- [procedure_count](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#ab83778fe2d1274e5658fd5f5f867314f)
- [max_procedure_len](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#ad71825d71ab89baea138e41f9a3ff57e)
- [bt_conn_br_cb](../bluetooth_connection_model_reference/P005_bt_conn_br_cb_结构体.md)
- [mode_changed](../bluetooth_connection_model_reference/P005_bt_conn_br_cb_结构体.md#aa278e529ac45aab63586b2566e857057)
- [role_changed](../bluetooth_connection_model_reference/P005_bt_conn_br_cb_结构体.md#a37af27d6d6d0e767dd439f24ff999c28)
- [packet_type_changed](../bluetooth_connection_model_reference/P005_bt_conn_br_cb_结构体.md#a93be2950207ea20c02b66647f5335273)
- [bt_conn_cb](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md)
- [connected](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#ab3618150bfeea9492095ba27ce978c69)
- [disconnected](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a8b8983b5b5b05c9e2dae242485b6c914)
- [recycled](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a1bd8d99988ad0ae3f79aad3d03fcbd8b)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [le_param_req](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a2c52c2e2798062708c373fae9610fadd)
- [le_param_updated](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a01582ed3e3801e10c665534eaa991454)
- [le_param_update_rejected](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a2179943b5f64302e38c64f075a5b6a9e)
- [identity_resolved](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#aea9b62ab1a1469be97a207a8e07d2f14)
- [security_changed](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#ae454d5bc2664e90ba2b1e0c867db374e)
- [remote_info_available](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#af726f004c06b86f770ece263ed6c9ca4)
- [br](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#abc6a0c4846d52d040b671b4f9f505755)
- [le_phy_updated](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#ae02a23d823954a747f8f474fb19276d7)
- [le_data_len_updated](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a1142d1861cc0b0058f68ecf537d0cec3)
- [cte_report_cb](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a8bde5cae151fa9ba79a7bf91c8901f5f)
- [bt_df_conn_iq_samples_report](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md)
- [tx_power_report](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a73d18565f1510a0adaa2b1f4d2278f2f)
- [path_loss_threshold_report](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a274d375b999d46854a691990fb58d90b)
- [subrate_changed](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a32949bf4b5d8cc44f0887c3022df0023)
- [conn_rate_changed](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a9cbc0e6b91fc2742c59815b676875235)
- [read_all_remote_feat_complete](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#aff02fd2cc1fd90640d0b9ce2e7440202)
- [frame_space_updated](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a1818aa00a45e807872e732e1fdfddc2c)
- [le_cs_read_remote_capabilities_complete](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a11b357037d6e3bdf99be7d3649a876d4)
- [le_cs_read_remote_fae_table_complete](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a016b5f28c5d7187991905abc71d09656)
- [le_cs_config_complete](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#ac20a741bc56068addc9fad442281a493)
- [le_cs_config_removed](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#ae79d3b27e75e4c49575d70ff1a860589)
- [le_cs_subevent_data_available](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a95af0f47a531b9ec02bb2ec4a26a2017)
- [le_cs_security_enable_complete](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a0dd4f406a0807014794470b2f33a0cea)
- [le_cs_procedure_enable_complete](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a39d8ed2cf68be3b029bd269be71b448a)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_conn_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9b79cd44734c1e560d6f30509be4d0b)
- [bt_conn_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gad2f90b34390e3c3697fd455ae4ef5f31)
- [bt_security_err_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga327444a6987b8e0b573fe758d2f75886)
- [bt_set_bondable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga014db594b17a3b5d7d954e64ad8de759)
- [bt_get_bondable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0c84d5597a71fe38788a88063fd19a2d)
- [bt_conn_set_bondable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4165819d12dd96e00dfa2fd6f4b95669)
- [bt_le_oob_set_sc_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gad02f8fe587efd543c0c81cace3f63d63)
- [bt_le_oob_set_legacy_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga978770d46d7c8af854a61261c14cb892)
- [bt_le_oob_set_legacy_tk](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0f889983cfabafe826b4feb6899b95ba)
- [bt_le_oob_set_sc_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac365f9748ad0737f09142ee1de982503)
- [bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)
- [bt_le_oob_get_sc_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga096552403b5bcd0107f69eded772b1ee)
- [bt_conn_oob_info](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md)
- [BT_CONN_OOB_LE_LEGACY](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md#aaec69b732a4bd8baf10c8b66bc73db89a4c33ea839306256a198c29ea783c659b)
- [BT_CONN_OOB_LE_SC](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md#aaec69b732a4bd8baf10c8b66bc73db89acd02773beb42df3fb6cbaa2fa2abda1e)
- [type](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md#a2117d76f495304753bc028afc66fc6b0)
- [BT_CONN_OOB_LOCAL_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__oob__info.html#a72a749120c0a55a8dc9bd078921277e5)
- [BT_CONN_OOB_REMOTE_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__oob__info.html#a7506049b35ac63602452b087d1d60fa2)
- [BT_CONN_OOB_BOTH_PEERS](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__oob__info.html#a99685ad84ac991e0540855cab5546ff8)
- [BT_CONN_OOB_NO_DATA](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__oob__info.html#a71bf295d82fbc647b3816bfba6fa0ae7)
- [oob_config](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md#a9c71633c3fc8c0a16edde7e6f1a832db)
- [lesc](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md#a49c2473beac84e2ea21b1299352beee6)
- [bt_conn_pairing_feat](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md)
- [io_capability](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md#a68005cea273c8e76c086502001b258b0)
- [oob_data_flag](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md#afb03164960db62b4b4cf70d3f0134099)
- [auth_req](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md#af9a977b1e0f9d4eada26a82d92eaec54)
- [max_enc_key_size](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md#abe1d7d4bd9f4b551a2d0c69adc75bd40)
- [init_key_dist](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md#a70adc125b875348ec8d273dea3b470d8)
- [resp_key_dist](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md#a49f9f02e232e91f7f7a530aa7f226cba)
- [bt_conn_auth_cb](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md)
- [pairing_accept](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#a92391a172e158a42966f410d732424a7)
- [passkey_display](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#a14074ca97fad6af4c58c43a00c503104)
- [passkey_display_keypress](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#af736a8808504fce22b95131818bad450)
- [passkey_entry](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#a10f9d22c89c95a6f3ffe0016f92445c0)
- [passkey_confirm](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#a2bb6c10666d111f675fd6de5ff51410a)
- [oob_data_request](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#aec9f6256607ea2cd1ce1b4cdb3052b42)
- [cancel](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#af6eb01c252ba3e32ff8bf583aa6ca0a4)
- [pairing_confirm](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#af4f7d3ee570b3472ee79b014be01f76e)
- [pincode_entry](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#ab6df1b1505dc22dd8dae0e946546c8bb)
- [app_passkey](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#a1be006307d1c9b6b13b4d35024f130e5)
- [bt_conn_auth_info_cb](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md)
- [pairing_complete](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#aea737700f2760de1ed26a721b5e860d2)
- [pairing_failed](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#ae7228bb82889eacebf67e1d4b3b23375)
- [bond_deleted](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#af20b0d7fc5fd8399ad9368b3ef7067f8)
- [addr_res_support_read](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#a44896258f0221d4f0a55cc1fb785b06c)
- [bt_le_addr_res_support](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad0039d4b524a0eef31158dc9b24a497)
- [br_bond_deleted](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#afcb8dae77f7b4df3ed0741de65f7f5d0)
- [node](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#afde62f2cdfb40b4154208f3c1c3dadc1)
- [bt_conn_auth_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1bf13d2dfdbdf0a72f9b1c759ef23f60)
- [bt_conn_auth_cb_overlay](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga81077385583d71c248a1eb6aab9ee86e)
- [bt_conn_auth_info_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac6684a8089ebd495b539d661cf9fd13f)
- [bt_conn_auth_info_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac73a60b8b6b569b84fe17f707fa33f37)
- [bt_conn_auth_passkey_entry](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3906d8d3d192e8a6ad1bf6b7acc32ff0)
- [bt_conn_auth_keypress_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2987a902da4f5cfe3671c60d154ced7e)
- [bt_conn_auth_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga89e5fc4bcab3f5598d20a9cd8ace5f59)
- [bt_conn_auth_passkey_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab8c3ecf2a3d68e54379917844a29d995)
- [bt_conn_auth_pairing_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3e15b9deb6787d3e415bbea35c9aa91d)
- [bt_conn_auth_pincode_entry](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4002a1b092832807218afa8ad279ab98)
- [bt_br_conn_param](../bluetooth_service_model_reference/P010_bt_br_conn_param_结构体.md)
- [allow_role_switch](../bluetooth_service_model_reference/P010_bt_br_conn_param_结构体.md#a95454a74932a14b4137c3fe82821be49)
- [bt_conn_create_br](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf7849f332386f8903d35d6904f6c82b9)
- [bt_conn_lookup_addr_br](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga11ae1b656683cebe9db6a53e5166ad7a)
- [bt_conn_get_dst_br](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1b02a1ce8e48ad483d73d1efd803618c)
- [bt_conn_br_switch_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3a7741f1e884168168a09e9ec5f28c49)
- [bt_conn_br_set_role_switch_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab6c2073091d1d08032c51aadb904ea3f)
- [bt_conn_br_enter_sniff_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga641f7f4ce7fe0641948a798881ecedcb)
- [bt_conn_br_exit_sniff_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab1aedad7da2eecc6c30acbfcdf9fbfec)
- [bt_conn_br_set_sniff_subrating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga910157e30fad972e8c606d1e1645603e)
- [bt_conn_br_get_supervision_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga76f872637f9b34c701c80d71ce7e585c)
- [bt_conn_br_set_supervision_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8516a5304ec78362ab66a9f18968d20d)
- [bt_conn_br_change_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae5073b3666aff788f6f389d010a918a6)
- [addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [direction.h](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html)
- [gap.h](https://docs.zephyrproject.org/latest/doxygen/html/gap_8h.html)
- [hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_br_conn_param::allow_role_switch](../bluetooth_service_model_reference/P010_bt_br_conn_param_结构体.md#a95454a74932a14b4137c3fe82821be49)
- [bt_conn_auth_cb::passkey_entry](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#a10f9d22c89c95a6f3ffe0016f92445c0)
- [bt_conn_auth_cb::passkey_display](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#a14074ca97fad6af4c58c43a00c503104)
- [bt_conn_auth_cb::app_passkey](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#a1be006307d1c9b6b13b4d35024f130e5)
- [bt_conn_auth_cb::passkey_confirm](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#a2bb6c10666d111f675fd6de5ff51410a)
- [bt_conn_auth_cb::pairing_accept](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#a92391a172e158a42966f410d732424a7)
- [bt_conn_auth_cb::pincode_entry](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#ab6df1b1505dc22dd8dae0e946546c8bb)
- [bt_conn_auth_cb::oob_data_request](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#aec9f6256607ea2cd1ce1b4cdb3052b42)
- [bt_conn_auth_cb::pairing_confirm](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#af4f7d3ee570b3472ee79b014be01f76e)
- [bt_conn_auth_cb::cancel](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#af6eb01c252ba3e32ff8bf583aa6ca0a4)
- [bt_conn_auth_cb::passkey_display_keypress](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md#af736a8808504fce22b95131818bad450)
- [bt_conn_auth_info_cb::addr_res_support_read](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#a44896258f0221d4f0a55cc1fb785b06c)
- [bt_conn_auth_info_cb::pairing_failed](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#ae7228bb82889eacebf67e1d4b3b23375)
- [bt_conn_auth_info_cb::pairing_complete](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#aea737700f2760de1ed26a721b5e860d2)
- [bt_conn_auth_info_cb::bond_deleted](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#af20b0d7fc5fd8399ad9368b3ef7067f8)
- [bt_conn_auth_info_cb::br_bond_deleted](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#afcb8dae77f7b4df3ed0741de65f7f5d0)
- [bt_conn_auth_info_cb::node](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#afde62f2cdfb40b4154208f3c1c3dadc1)
- [bt_conn_br_cb::role_changed](../bluetooth_connection_model_reference/P005_bt_conn_br_cb_结构体.md#a37af27d6d6d0e767dd439f24ff999c28)
- [bt_conn_br_cb::packet_type_changed](../bluetooth_connection_model_reference/P005_bt_conn_br_cb_结构体.md#a93be2950207ea20c02b66647f5335273)
- [bt_conn_br_cb::mode_changed](../bluetooth_connection_model_reference/P005_bt_conn_br_cb_结构体.md#aa278e529ac45aab63586b2566e857057)
- [bt_conn_br_info::dst](../bluetooth_connection_model_reference/P006_bt_conn_br_info_结构体.md#aeef49f711872ccfec5dd558c4552b71e)
- [bt_conn_br_remote_info::num_pages](../bluetooth_connection_model_reference/P007_bt_conn_br_remote_info_结构体.md#a798c179c803e709182a1b0c3594f4a0a)
- [bt_conn_br_remote_info::features](../bluetooth_connection_model_reference/P007_bt_conn_br_remote_info_结构体.md#afa19f7db400bb0de234e8cda61f3deaf)
- [bt_conn_cb::le_param_updated](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a01582ed3e3801e10c665534eaa991454)
- [bt_conn_cb::le_cs_read_remote_fae_table_complete](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a016b5f28c5d7187991905abc71d09656)
- [bt_conn_cb::le_cs_security_enable_complete](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a0dd4f406a0807014794470b2f33a0cea)
- [bt_conn_cb::le_data_len_updated](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a1142d1861cc0b0058f68ecf537d0cec3)
- [bt_conn_cb::le_cs_read_remote_capabilities_complete](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a11b357037d6e3bdf99be7d3649a876d4)
- [bt_conn_cb::frame_space_updated](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a1818aa00a45e807872e732e1fdfddc2c)
- [bt_conn_cb::recycled](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a1bd8d99988ad0ae3f79aad3d03fcbd8b)
- [bt_conn_cb::le_param_update_rejected](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a2179943b5f64302e38c64f075a5b6a9e)
- [bt_conn_cb::path_loss_threshold_report](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a274d375b999d46854a691990fb58d90b)
- [bt_conn_cb::le_param_req](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a2c52c2e2798062708c373fae9610fadd)
- [bt_conn_cb::subrate_changed](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a32949bf4b5d8cc44f0887c3022df0023)
- [bt_conn_cb::le_cs_procedure_enable_complete](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a39d8ed2cf68be3b029bd269be71b448a)
- [bt_conn_cb::tx_power_report](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a73d18565f1510a0adaa2b1f4d2278f2f)
- [bt_conn_cb::disconnected](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a8b8983b5b5b05c9e2dae242485b6c914)
- [bt_conn_cb::cte_report_cb](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a8bde5cae151fa9ba79a7bf91c8901f5f)
- [bt_conn_cb::le_cs_subevent_data_available](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a95af0f47a531b9ec02bb2ec4a26a2017)
- [bt_conn_cb::conn_rate_changed](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a9cbc0e6b91fc2742c59815b676875235)
- [bt_conn_cb::connected](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#ab3618150bfeea9492095ba27ce978c69)
- [bt_conn_cb::br](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#abc6a0c4846d52d040b671b4f9f505755)
- [bt_conn_cb::le_cs_config_complete](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#ac20a741bc56068addc9fad442281a493)
- [bt_conn_cb::le_phy_updated](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#ae02a23d823954a747f8f474fb19276d7)
- [bt_conn_cb::security_changed](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#ae454d5bc2664e90ba2b1e0c867db374e)
- [bt_conn_cb::le_cs_config_removed](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#ae79d3b27e75e4c49575d70ff1a860589)
- [bt_conn_cb::identity_resolved](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#aea9b62ab1a1469be97a207a8e07d2f14)
- [bt_conn_cb::remote_info_available](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#af726f004c06b86f770ece263ed6c9ca4)
- [bt_conn_cb::read_all_remote_feat_complete](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#aff02fd2cc1fd90640d0b9ce2e7440202)
- [bt_conn_info::id](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#a3a4e24519b5d3ba547423e53c4d92a5c)
- [bt_conn_info::le](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#a6b536e7732dcf7b77a7bc05116dca548)
- [bt_conn_info::type](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#a7995e1291be494b5bdf860eceea0cad1)
- [bt_conn_info::br](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#a799e59d3a85625799a32ac3f0b3d67d1)
- [bt_conn_info::role](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#a8237b8c1bb9a97a174d04cbe13dca7c7)
- [bt_conn_info::sco](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#ad622c69f262ee53ec94918857250a2a0)
- [bt_conn_info::security](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#ae4405f1b4f3fe2ff6253453964860931)
- [bt_conn_info::state](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#ae566e2382b69ff27314dc1dd632dbdbc)
- [bt_conn_le_conn_rate_changed::continuation_number](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md#a348cc25c2f19bab8c5e140b712b3034a)
- [bt_conn_le_conn_rate_changed::supervision_timeout_10ms](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md#a47d662c1e00e8c4e1a553d9a4909f6df)
- [bt_conn_le_conn_rate_changed::peripheral_latency](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md#a768af259e8d37f463278946bd660ce58)
- [bt_conn_le_conn_rate_changed::interval_us](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md#aa6dfef1425c47823897b8b84de17ecf9)
- [bt_conn_le_conn_rate_changed::subrate_factor](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md#ab2b60e61438b0d814c9a8a8adcae35fc)
- [bt_conn_le_conn_rate_param::interval_min_125us](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#a264baeb210c9cbd559f0cd3ed2cd78b1)
- [bt_conn_le_conn_rate_param::supervision_timeout_10ms](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#a50a3c9eca10ed5c11773aaf07e1fbc12)
- [bt_conn_le_conn_rate_param::subrate_max](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#a751042149cb8ff1ec28de10fe1e4c8bd)
- [bt_conn_le_conn_rate_param::interval_max_125us](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#a9afcc899991204f17c1390b9362ec54b)
- [bt_conn_le_conn_rate_param::max_ce_len_125us](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#aa764837e74aac1feba2025cf01a87d85)
- [bt_conn_le_conn_rate_param::continuation_number](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#adf4c1069b5aa3b8afb09ea8b59d93eca)
- [bt_conn_le_conn_rate_param::min_ce_len_125us](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#ae4734b6d8f0f4903624e47e975828482)
- [bt_conn_le_conn_rate_param::subrate_min](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#aed9238960e4be8ddbeff53afab74ef6f)
- [bt_conn_le_conn_rate_param::max_latency](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md#afb3fa1a4202c39a9551dd41396595771)
- [bt_conn_le_create_param::interval_coded](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md#a2bc978ac97435fe5f87c6e01692f2910)
- [bt_conn_le_create_param::window](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md#a339b99f65c5029ada6cdf453ab1f258e)
- [bt_conn_le_create_param::options](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md#a4b1e26c0976d9c900b831c886c77b055)
- [bt_conn_le_create_param::timeout](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md#a59f05bfb9468779d02f8d0beeb7a35c1)
- [bt_conn_le_create_param::interval](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md#a5cfae677f924534dc5bc7b38c457a7af)
- [bt_conn_le_create_param::window_coded](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md#ae62491837d35d95e32016b793edf8c96)
- [bt_conn_le_create_synced_param::peer](../bluetooth_connection_model_reference/P013_bt_conn_le_create_synced_param_结构体.md#ac5872dda4042e3ba6c161dce60784b70)
- [bt_conn_le_create_synced_param::subevent](../bluetooth_connection_model_reference/P013_bt_conn_le_create_synced_param_结构体.md#ac7b4e4144aaf914bdef1dc305b5e297f)
- [bt_conn_le_cs_capabilities::t_ip1_times_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a090f869cfe7e39a70cea94afbd5ac376)
- [bt_conn_le_cs_capabilities::phase_based_nadm_random_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a1a0076a0c97317803976f4aca86afc0d)
- [bt_conn_le_cs_capabilities::t_fcs_times_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a1ff1d7d769e3ba915f91bf672a6f8a61)
- [bt_conn_le_cs_capabilities::t_ip2_ipt_times_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a21262b0e588a75146f2d0c325d0b5cc1)
- [bt_conn_le_cs_capabilities::cs_without_fae_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a22604c052da2f8ccf77c81a0a5c628b7)
- [bt_conn_le_cs_capabilities::rtt_random_payload_n](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a345d9e43222d77024a8f4283b274b48f)
- [bt_conn_le_cs_capabilities::cs_sync_2m_phy_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a3fd09db5fae9c5e307994a78131199c6)
- [bt_conn_le_cs_capabilities::rtt_aa_only_precision](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a46c9168328d3fbc98a2625799c733818)
- [bt_conn_le_cs_capabilities::num_antennas_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a4e4c56c5066d02b2a0cd59c067f1e4b9)
- [bt_conn_le_cs_capabilities::t_sw_time](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a5a86629a5ad4203b5efe3802cd8b6ae7)
- [bt_conn_le_cs_capabilities::cs_sync_2m_2bt_phy_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a6513d8ffe7d168441205f6dd656dcbbc)
- [bt_conn_le_cs_capabilities::initiator_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a6530d2a3fb66d498711856b723acecb7)
- [bt_conn_le_cs_capabilities::reflector_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a694119619d359d0b7e298edf6201ee20)
- [bt_conn_le_cs_capabilities::t_pm_times_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a6e92391b21d4acaebba8a171643f572f)
- [bt_conn_le_cs_capabilities::num_config_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a77aacfd02b354e04d4cc29cc1bf4b779)
- [bt_conn_le_cs_capabilities::rtt_sounding_n](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a7f35343a1572800850e791ba3ff5ffb1)
- [bt_conn_le_cs_capabilities::phase_based_nadm_sounding_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a94fd00a7a9b22d649f75c7fdd17590a9)
- [bt_conn_le_cs_capabilities::t_sw_ipt_time_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a97b42928bcba43a6d90e8139efce0870)
- [bt_conn_le_cs_capabilities::mode_3_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#aa1616417e6183cf283cf96efc9a92b8e)
- [bt_conn_le_cs_capabilities::chsel_alg_3c_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#aba0db15183d4fa4ae0e3f1333202e55e)
- [bt_conn_le_cs_capabilities::rtt_random_payload_precision](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#abbefdc0268a775712c7abd664adcb6b2)
- [bt_conn_le_cs_capabilities::rtt_aa_only_n](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#abe3c611316bb5f710f355846ee9ec437)
- [bt_conn_le_cs_capabilities::max_antenna_paths_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#ac842e123166008ad1ad663f827937a3b)
- [bt_conn_le_cs_capabilities::rtt_sounding_precision](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#acef0d65ed55ae304fea47006bfb0076f)
- [bt_conn_le_cs_capabilities::pbr_from_rtt_sounding_seq_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#ad57f15b4dda88e2b747f30451601c923)
- [bt_conn_le_cs_capabilities::tx_snr_capability](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#ad58deea7a825bb5f0bc2ca0034183948)
- [bt_conn_le_cs_capabilities::cs_ipt_reflector](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#adfac38e7771604971a82ece149c1d337)
- [bt_conn_le_cs_capabilities::max_consecutive_procedures_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#ae76fbc0f88525e83717e1d8ef5acae59)
- [bt_conn_le_cs_capabilities::t_ip2_times_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#ae93594f360430e9c0c80cf3edcf570f6)
- [bt_conn_le_cs_config::rtt_type](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a194e3844373c57e714917d03ac82666d)
- [bt_conn_le_cs_config::cs_sync_phy](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a2051f559b41085c4b41743aaaaecf3a1)
- [bt_conn_le_cs_config::t_fcs_time_us](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a29912bd291fa4da09bb5b196d747ca6b)
- [bt_conn_le_cs_config::min_main_mode_steps](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a2e59fb17cd932b7670b3e915684c2107)
- [bt_conn_le_cs_config::main_mode_repetition](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a2e904438c579870ed96b5dccff239c18)
- [bt_conn_le_cs_config::channel_map](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a60f9d21629554d47556d0fe8d63dcae3)
- [bt_conn_le_cs_config::channel_selection_type](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a63b7027929a5c3ec7fd68f35343262ee)
- [bt_conn_le_cs_config::t_ip2_time_us](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a8e650b50400a45040c02a88dfb30683c)
- [bt_conn_le_cs_config::mode_0_steps](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a8eea68bffef759b4532b68a1ecbdd4f1)
- [bt_conn_le_cs_config::channel_map_repetition](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a971ff7ba734dd71512af7f3850de364d)
- [bt_conn_le_cs_config::ch3c_shape](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#a9b64ecb0986e7e9995c29feaf105eeaa)
- [bt_conn_le_cs_config::t_ip1_time_us](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#aab9a1d8d09d7a439f1c4dd28b9dd05c4)
- [bt_conn_le_cs_config::id](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#aaf8f1ce04fd22b4ca4728bdcfce8bd4a)
- [bt_conn_le_cs_config::mode](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#ab59b31730b91f843e5b8a156d98da42d)
- [bt_conn_le_cs_config::cs_enhancements_1](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#acfccd404abced1c5f5490130f2f77f23)
- [bt_conn_le_cs_config::role](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#ad11f8bee028ad3eb59008d46dce2d5bd)
- [bt_conn_le_cs_config::t_pm_time_us](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#ae7f1cc232df00b4543fdb2b2596b9bbf)
- [bt_conn_le_cs_config::ch3c_jump](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#afa2846689f1a9d5b9e124b1c9095154f)
- [bt_conn_le_cs_config::max_main_mode_steps](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md#aff70b37fac8a3bd94acb25d7bd06989b)
- [bt_conn_le_cs_fae_table::remote_fae_table](../bluetooth_connection_model_reference/P016_bt_conn_le_cs_fae_table_结构体.md#a9d4a2fe09edc897143b6e479f30b7f65)
- [bt_conn_le_cs_procedure_enable_complete::config_id](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#a2e290c25ec5af8b0259d45f04d6c543d)
- [bt_conn_le_cs_procedure_enable_complete::tone_antenna_config_selection](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#a3fa8ad4dd264eb4e2489dea9c1048d22)
- [bt_conn_le_cs_procedure_enable_complete::subevents_per_event](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#a40b03220932852b6b51d65f557c21f17)
- [bt_conn_le_cs_procedure_enable_complete::event_interval](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#a4129ab9519ba140ffb198aa9a5cde6ac)
- [bt_conn_le_cs_procedure_enable_complete::subevent_interval](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#a77a2bd8ee384c4567321a09f6b64782c)
- [bt_conn_le_cs_procedure_enable_complete::procedure_interval](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#a8511deef97f19c53ddaa4dec8492658f)
- [bt_conn_le_cs_procedure_enable_complete::procedure_count](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#ab83778fe2d1274e5658fd5f5f867314f)
- [bt_conn_le_cs_procedure_enable_complete::state](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#acc1d12d347e1b02b2eea562ea064a40b)
- [bt_conn_le_cs_procedure_enable_complete::max_procedure_len](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#ad71825d71ab89baea138e41f9a3ff57e)
- [bt_conn_le_cs_procedure_enable_complete::subevent_len](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#ae990a10c468ec62fbaf9325c94733c7c)
- [bt_conn_le_cs_procedure_enable_complete::selected_tx_power](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md#aeb918e438cd02296c7f693757268f6bf)
- [bt_conn_le_cs_subevent_result::procedure_counter](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a0f8fc918f8eb31c47acf51885c7add08)
- [bt_conn_le_cs_subevent_result::header](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a1a90563a8c93f9b309e88fd771a7cec4)
- [bt_conn_le_cs_subevent_result::num_antenna_paths](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a3597697ae4acdd8f7c009bececab6a65)
- [bt_conn_le_cs_subevent_result::num_steps_reported](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a3bffc0935a5410d75d0050337e4fad27)
- [bt_conn_le_cs_subevent_result::subevent_done_status](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a45b22c6c2252e2afa28ee8b1bfed3ecf)
- [bt_conn_le_cs_subevent_result::step_data_buf](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a6948c4a8c5882cb1d1b04a2b390fda8c)
- [bt_conn_le_cs_subevent_result::start_acl_conn_event](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a7706d0dfd7246d4cf193a8a9e7b6305d)
- [bt_conn_le_cs_subevent_result::procedure_abort_reason](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a778c89f57ef50f612654243ba673ba3f)
- [bt_conn_le_cs_subevent_result::frequency_compensation](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a967d37f37d0e1596984fdda34609a3b3)
- [bt_conn_le_cs_subevent_result::abort_step](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#a9bfcc6dcaa191c7f56958ef88926b51e)
- [bt_conn_le_cs_subevent_result::config_id](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#aa4c770ab2db8d4ab665ad50f7edd5bfa)
- [bt_conn_le_cs_subevent_result::reference_power_level](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#acbfc5e80a2fb82072d9376e996f7969f)
- [bt_conn_le_cs_subevent_result::procedure_done_status](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#adf60893d9229003d1eefc552a4957b65)
- [bt_conn_le_cs_subevent_result::subevent_abort_reason](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md#aef5ba53497c4d1576c9ecec1b5dea289)
- [bt_conn_le_data_len_info::tx_max_time](../bluetooth_connection_model_reference/P019_bt_conn_le_data_len_info_结构体.md#a14288429cbbcce2ef34580a581815eb7)
- [bt_conn_le_data_len_info::rx_max_len](../bluetooth_connection_model_reference/P019_bt_conn_le_data_len_info_结构体.md#a18ddc603e922586e331187c9b29f2908)
- [bt_conn_le_data_len_info::tx_max_len](../bluetooth_connection_model_reference/P019_bt_conn_le_data_len_info_结构体.md#a48d175f3c4b03dbdee129feae3edab23)
- [bt_conn_le_data_len_info::rx_max_time](../bluetooth_connection_model_reference/P019_bt_conn_le_data_len_info_结构体.md#af2316cdc921e9ec19491501e15248f73)
- [bt_conn_le_data_len_param::tx_max_len](../bluetooth_connection_model_reference/P020_bt_conn_le_data_len_param_结构体.md#a8b279a0dc72c70aaf5205558fd4b4c4a)
- [bt_conn_le_data_len_param::tx_max_time](../bluetooth_connection_model_reference/P020_bt_conn_le_data_len_param_结构体.md#a9046542952fa822b944602b398562e6e)
- [bt_conn_le_frame_space_update_param::spacing_types](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md#a1e5bd6b331c1c7c4881e2875b1adfd3d)
- [bt_conn_le_frame_space_update_param::phys](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md#a67adb4f731d9a1822b400af9f30bcf43)
- [bt_conn_le_frame_space_update_param::frame_space_min](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md#a7d3f1ee0c43797ab100b24c3919f304f)
- [bt_conn_le_frame_space_update_param::frame_space_max](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md#a90e83dca82b557ef1476d5e4919fb170)
- [bt_conn_le_frame_space_updated::status](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md#a126026dba0cb84ceaf10324212bbf3e0)
- [bt_conn_le_frame_space_updated::phys](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md#a332a93e2d05750bd241e137381186f8b)
- [bt_conn_le_frame_space_updated::spacing_types](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md#a7cb3366670e07d06a466c3c7eb885b09)
- [bt_conn_le_frame_space_updated::frame_space](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md#af1918fb7b4abc7f7b3eb11c33a3190f6)
- [bt_conn_le_frame_space_updated::initiator](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md#af6b88c108be375ea80466ece72257f2e)
- [bt_conn_le_info::dst](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a1f78e1c0ed3482ce6eec9ce6eeda4769)
- [bt_conn_le_info::phy](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a215d39c6cd7da1ac033529b5541cbfc1)
- [bt_conn_le_info::remote](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a236d1c97c735c7cfaead0b1a3672d512)
- [bt_conn_le_info::local](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a3be5df0deb0af08f84843eb3c6a5e5ae)
- [bt_conn_le_info::interval_us](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a3bede29a6a5df282bde6a26f50ea9aee)
- [bt_conn_le_info::subrate](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a5d97a2eb4aa880abe857f19adeea425d)
- [bt_conn_le_info::src](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a5f1eacec82f31182460d6d5359a8b295)
- [bt_conn_le_info::interval](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#a95a1f635e53f16d5839cdd58f4bda962)
- [bt_conn_le_info::latency](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#acd83835fe5ec0878fd653b87cb570a49)
- [bt_conn_le_info::data_len](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#ae309f390c8d7b33a4de55791af235ab0)
- [bt_conn_le_info::timeout](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md#afb4dc594d063fbbad2bcd4acf047f716)
- [bt_conn_le_min_conn_interval_group::max_125us](../bluetooth_connection_model_reference/P024_bt_conn_le_min_conn_interval_group_结构体.md#a3d48e4889d3e039fc19da55c40efc911)
- [bt_conn_le_min_conn_interval_group::min_125us](../bluetooth_connection_model_reference/P024_bt_conn_le_min_conn_interval_group_结构体.md#a44c7e6e9983d607fdde9cafe8cb595e1)
- [bt_conn_le_min_conn_interval_group::stride_125us](../bluetooth_connection_model_reference/P024_bt_conn_le_min_conn_interval_group_结构体.md#aed08c6c6bbe9f4bfae0a5e0c8ad6e9f3)
- [bt_conn_le_min_conn_interval_info::min_supported_conn_interval_us](../bluetooth_connection_model_reference/P025_bt_conn_le_min_conn_interval_info_结构体.md#aa39299ca32657e9f684e88875e7517dc)
- [bt_conn_le_min_conn_interval_info::num_groups](../bluetooth_connection_model_reference/P025_bt_conn_le_min_conn_interval_info_结构体.md#ac0d63f57518324d81509fea51fcefa60)
- [bt_conn_le_min_conn_interval_info::groups](../bluetooth_connection_model_reference/P025_bt_conn_le_min_conn_interval_info_结构体.md#ad9e6ae7c5632e4cc2a5e5eda52d2e0e8)
- [bt_conn_le_path_loss_reporting_param::high_threshold](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md#a5cc7a17efee69d61b8f8d0c242321054)
- [bt_conn_le_path_loss_reporting_param::low_threshold](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md#a634c08e573cffd97a94ad681bed9239e)
- [bt_conn_le_path_loss_reporting_param::min_time_spent](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md#a6fec4497c6fd95fa6f265bd859976c9d)
- [bt_conn_le_path_loss_reporting_param::high_hysteresis](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md#aec49adc896604d878060b03bd40ab0f4)
- [bt_conn_le_path_loss_reporting_param::low_hysteresis](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md#af8e70508a39ee73b75a4769769aa303f)
- [bt_conn_le_path_loss_threshold_report::zone](../bluetooth_connection_model_reference/P027_bt_conn_le_path_loss_threshold_report_结构体.md#ab2b71b7ddccc40ced56657a548b98e77)
- [bt_conn_le_path_loss_threshold_report::path_loss](../bluetooth_connection_model_reference/P027_bt_conn_le_path_loss_threshold_report_结构体.md#abe631b07816d6c18bacba64bfbd1e844)
- [bt_conn_le_phy_info::rx_phy](../bluetooth_connection_model_reference/P028_bt_conn_le_phy_info_结构体.md#abf029b63958d86eef7bf15218238783b)
- [bt_conn_le_phy_info::tx_phy](../bluetooth_connection_model_reference/P028_bt_conn_le_phy_info_结构体.md#ac65912cc2a7997c0f886886783ea5b11)
- [bt_conn_le_phy_param::options](../bluetooth_connection_model_reference/P029_bt_conn_le_phy_param_结构体.md#a889dae2cdc2fba43f9f1194d26c4b737)
- [bt_conn_le_phy_param::pref_rx_phy](../bluetooth_connection_model_reference/P029_bt_conn_le_phy_param_结构体.md#a8d576bed5d9dfe9ca9a694d6d295afbc)
- [bt_conn_le_phy_param::pref_tx_phy](../bluetooth_connection_model_reference/P029_bt_conn_le_phy_param_结构体.md#ace64d2181ecc25ecdfa374f7f4bcf664)
- [bt_conn_le_read_all_remote_feat_complete::status](../bluetooth_connection_model_reference/P030_bt_conn_le_read_all_remote_feat_complete_结构体.md#a0dbbd0144cc6990b45d662896862cce7)
- [bt_conn_le_read_all_remote_feat_complete::max_remote_page](../bluetooth_connection_model_reference/P030_bt_conn_le_read_all_remote_feat_complete_结构体.md#a1554bd9035619cc4dbdb2d04fd9105ad)
- [bt_conn_le_read_all_remote_feat_complete::features](../bluetooth_connection_model_reference/P030_bt_conn_le_read_all_remote_feat_complete_结构体.md#a7a8db1d0c0656e8953da8b8aa4bec2c7)
- [bt_conn_le_read_all_remote_feat_complete::max_valid_page](../bluetooth_connection_model_reference/P030_bt_conn_le_read_all_remote_feat_complete_结构体.md#a996e2600fd41bf1b6d95b6ee5873f6ce)
- [bt_conn_le_remote_info::features](../bluetooth_connection_model_reference/P031_bt_conn_le_remote_info_结构体.md#a4ff434f6c501dc60db5c4b776be46b3b)
- [bt_conn_le_subrate_changed::factor](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md#a0c3e3dc41ca4dec92740c920e959060b)
- [bt_conn_le_subrate_changed::continuation_number](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md#a2420a0a3145471c6a1a618bea8d1d7c6)
- [bt_conn_le_subrate_changed::peripheral_latency](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md#aa0bab070bc43972dfb3a5259934b4931)
- [bt_conn_le_subrate_changed::supervision_timeout](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md#aab0cb08a7549401684bcab3c291dc192)
- [bt_conn_le_subrate_changed::status](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md#afc5a577dadf41819e89bc3af016ce258)
- [bt_conn_le_subrate_param::max_latency](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md#a15d05324708ddeea8d2f3515eea396bb)
- [bt_conn_le_subrate_param::subrate_max](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md#a59d2d244e3568b8f97ce936121d41b1a)
- [bt_conn_le_subrate_param::continuation_number](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md#a978cef5f2f14a5a7fe7ded09c6fdf2d9)
- [bt_conn_le_subrate_param::supervision_timeout](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md#aca0897d00a1dd1735dbbaf5bfde711ed)
- [bt_conn_le_subrate_param::subrate_min](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md#aef75fec8ba8c9987d55e81aa2539b96e)
- [bt_conn_le_subrating_info::continuation_number](../bluetooth_connection_model_reference/P034_bt_conn_le_subrating_info_结构体.md#a0a6d1eae73f76382f1a9415c01761c19)
- [bt_conn_le_subrating_info::factor](../bluetooth_connection_model_reference/P034_bt_conn_le_subrating_info_结构体.md#a23736535309f38695a2e432c5c80bbe1)
- [bt_conn_le_tx_power_report::phy](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md#a5b1f67537fbe945f2f258b47082723b4)
- [bt_conn_le_tx_power_report::delta](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md#a7c681c7b9f77d994b2de1febea7c5dc9)
- [bt_conn_le_tx_power_report::reason](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md#aa5606925229784af8ae90542432cf200)
- [bt_conn_le_tx_power_report::tx_power_level](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md#ace830ddb7ae662c9759babed87f1b6f3)
- [bt_conn_le_tx_power_report::tx_power_level_flag](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md#ae7a4f77c6f7af1a459896d25cf661eb8)
- [bt_conn_le_tx_power::max_level](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md#a1674247c511906fa6f0193653ed0b71a)
- [bt_conn_le_tx_power::current_level](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md#a6d2e5a5215fa5d60630e74928a67fc04)
- [bt_conn_le_tx_power::phy](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md#a8702c4ff5082b8f90decdfabfb8253fe)
- [bt_conn_oob_info::type](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md#a2117d76f495304753bc028afc66fc6b0)
- [bt_conn_oob_info::lesc](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md#a49c2473beac84e2ea21b1299352beee6)
- [bt_conn_oob_info::BT_CONN_OOB_NO_DATA](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__oob__info.html#a71bf295d82fbc647b3816bfba6fa0ae7)
- [bt_conn_oob_info::BT_CONN_OOB_LOCAL_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__oob__info.html#a72a749120c0a55a8dc9bd078921277e5)
- [bt_conn_oob_info::BT_CONN_OOB_REMOTE_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__oob__info.html#a7506049b35ac63602452b087d1d60fa2)
- [bt_conn_oob_info::BT_CONN_OOB_BOTH_PEERS](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__oob__info.html#a99685ad84ac991e0540855cab5546ff8)
- [bt_conn_oob_info::oob_config](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md#a9c71633c3fc8c0a16edde7e6f1a832db)
- [bt_conn_oob_info::BT_CONN_OOB_LE_LEGACY](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md#aaec69b732a4bd8baf10c8b66bc73db89a4c33ea839306256a198c29ea783c659b)
- [bt_conn_oob_info::BT_CONN_OOB_LE_SC](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md#aaec69b732a4bd8baf10c8b66bc73db89acd02773beb42df3fb6cbaa2fa2abda1e)
- [bt_conn_pairing_feat::resp_key_dist](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md#a49f9f02e232e91f7f7a530aa7f226cba)
- [bt_conn_pairing_feat::io_capability](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md#a68005cea273c8e76c086502001b258b0)
- [bt_conn_pairing_feat::init_key_dist](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md#a70adc125b875348ec8d273dea3b470d8)
- [bt_conn_pairing_feat::max_enc_key_size](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md#abe1d7d4bd9f4b551a2d0c69adc75bd40)
- [bt_conn_pairing_feat::auth_req](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md#af9a977b1e0f9d4eada26a82d92eaec54)
- [bt_conn_pairing_feat::oob_data_flag](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md#afb03164960db62b4b4cf70d3f0134099)
- [bt_conn_remote_info::version](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md#a2664f6ed3bd22f9a011126daf5d81376)
- [bt_conn_remote_info::subversion](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md#a360979a15c958706157fc630fd55cbca)
- [bt_conn_remote_info::manufacturer](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md#a47cc5a4b8888a0b8faaf6880c37418b8)
- [bt_conn_remote_info::type](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md#a8bb514196bde5df561dbf76b68060729)
- [bt_conn_remote_info::br](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md#ab73365f09cdb5ce870272546543bcfeb)
- [bt_conn_remote_info::le](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md#ae75530b09c6dea416630a4a19a1d64cc)
- [bt_conn_sco_info::link_type](../bluetooth_connection_model_reference/P040_bt_conn_sco_info_结构体.md#aad5fc309d1ffccda38c07b40ac028dd1)
- [bt_conn_sco_info::air_mode](../bluetooth_connection_model_reference/P040_bt_conn_sco_info_结构体.md#ae4474ebfe0129eb6214987a31430d4f7)
- [bt_le_conn_param::latency](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md#a3d21bd8363fa77dab83468ea319fef7d)
- [bt_le_conn_param::interval_max](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md#a6d5a2662a5f22ccc26c992829d21f22d)
- [bt_le_conn_param::timeout](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md#ac06c16eb02e7a9d8b414db07e829178a)
- [bt_le_conn_param::interval_min](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md#acd3b0a74402ca45402bab9ff54763e8d)
- [bt_security_info::enc_key_size](../bluetooth_connection_model_reference/P130_bt_security_info_结构体.md#a6567ffb82b7fa8093cc57ef4662873ba)
- [bt_security_info::level](../bluetooth_connection_model_reference/P130_bt_security_info_结构体.md#a7b18849fad25b3f2da6b8c85a56d86e1)
- [bt_security_info::flags](../bluetooth_connection_model_reference/P130_bt_security_info_结构体.md#a99cb4af08bfa1dab182821d956368526)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P001_bcm2711-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_gpio_cmsdk_ahb.h_源码浏览.md)

## 原站枚举锚点译注（Upstream Enum Anchor Note）

原源码页的以下 4 个链接指向父结构体中不存在的锚点；官方结构体页给出的匿名嵌套结构体链接也返回 404。原链接已保留。以下补充入口直接指向经核对的枚举源码行，当前官方源码和本页均包含对应定义：

- `BT_CONN_OOB_LOCAL_ONLY`：[本页定义](#l02861)；[官方源码定义](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html#l02861)。
- `BT_CONN_OOB_REMOTE_ONLY`：[本页定义](#l02864)；[官方源码定义](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html#l02864)。
- `BT_CONN_OOB_BOTH_PEERS`：[本页定义](#l02867)；[官方源码定义](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html#l02867)。
- `BT_CONN_OOB_NO_DATA`：[本页定义](#l02870)；[官方源码定义](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html#l02870)。
