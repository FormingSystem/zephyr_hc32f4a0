---
id: learning.zephyr-docs.api-source-packet-gnss-reference.page-4
title: protocol.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_protocol.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md)。

## 4.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00047"></a>
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
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00077"></a>
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
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="foldopen00143"></a>
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
<a id="foldopen00155"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="foldopen00160"></a>
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
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="foldopen00176"></a>
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
<a id="foldopen00186"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="foldopen00191"></a>
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
<a id="foldopen00201"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="foldopen00212"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="foldopen00219"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="foldopen00226"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="foldopen00232"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="foldopen00247"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="foldopen00259"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="foldopen00272"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="foldopen00289"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="foldopen00311"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="foldopen00317"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="foldopen00324"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="foldopen00330"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="foldopen00339"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="foldopen00345"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="foldopen00350"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="foldopen00356"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="foldopen00362"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="foldopen00368"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="foldopen00374"></a>
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
<a id="foldopen00396"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="foldopen00404"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="foldopen00410"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="foldopen00415"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00422"></a>
<a id="l00423"></a>
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
<a id="foldopen00434"></a>
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
<a id="foldopen00459"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="foldopen00462"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="foldopen00465"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="foldopen00468"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="foldopen00471"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="foldopen00476"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="foldopen00482"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="foldopen00486"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="foldopen00493"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="foldopen00500"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="foldopen00508"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="foldopen00514"></a>
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
<a id="foldopen00533"></a>
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
<a id="achecksum_8h_html"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a99ef1cb2c789827dd5db3886dccf9067"></a>
<a id="amodem_2ubx_2protocol_8h_html_a0d969e434f941cf5af7143cca0cf0fe4"></a>
<a id="amodem_2ubx_2protocol_8h_html_a0d969e434f941cf5af7143cca0cf0fe4a43aa77232e6c2aed82ecf2033c0a06b0"></a>
<a id="amodem_2ubx_2protocol_8h_html_a0d969e434f941cf5af7143cca0cf0fe4a66c14a28074edc8631bd6b47f5c45888"></a>
<a id="amodem_2ubx_2protocol_8h_html_a1693f3584605a0197076cba71c79b0df"></a>
<a id="amodem_2ubx_2protocol_8h_html_a173b6c1016562da43b8131b8d8f04fef"></a>
<a id="amodem_2ubx_2protocol_8h_html_a173b6c1016562da43b8131b8d8f04fefa1f8c2845d6e8e41f62cc28b7f1681f43"></a>
<a id="amodem_2ubx_2protocol_8h_html_a173b6c1016562da43b8131b8d8f04fefa2c20469f6893f651ad14b8ed6a7c3845"></a>
<a id="amodem_2ubx_2protocol_8h_html_a173b6c1016562da43b8131b8d8f04fefa648f596240841758588749574998bd71"></a>
<a id="amodem_2ubx_2protocol_8h_html_a173b6c1016562da43b8131b8d8f04fefad351fdc11590580b88ba5b486113e498"></a>
<a id="amodem_2ubx_2protocol_8h_html_a173b6c1016562da43b8131b8d8f04fefae28182c06da19d2b498f92d09d74b33e"></a>
<a id="amodem_2ubx_2protocol_8h_html_a173b6c1016562da43b8131b8d8f04fefae47dad429327e6a0cc89e339729b2651"></a>
<a id="amodem_2ubx_2protocol_8h_html_a260c4adbe9524bd747127a4e3f14bbca"></a>
<a id="amodem_2ubx_2protocol_8h_html_a260c4adbe9524bd747127a4e3f14bbcaa88bba7f61485369188998bc1c18b2511"></a>
<a id="amodem_2ubx_2protocol_8h_html_a260c4adbe9524bd747127a4e3f14bbcaacd2316ff6386c7eb2da90de1f4466469"></a>
<a id="amodem_2ubx_2protocol_8h_html_a2c667ef9bb2d12effb251f4df6827c73"></a>
<a id="amodem_2ubx_2protocol_8h_html_a2e5de1479afbcf20caa3300282bb0d1a"></a>
<a id="amodem_2ubx_2protocol_8h_html_a2e5de1479afbcf20caa3300282bb0d1aa1ef24c67f4e90f7c6fb011ec433ebb68"></a>
<a id="amodem_2ubx_2protocol_8h_html_a2e5de1479afbcf20caa3300282bb0d1aa46b4ba80de7ca4c9d1ea403dd6efb385"></a>
<a id="amodem_2ubx_2protocol_8h_html_a2e5de1479afbcf20caa3300282bb0d1aa5db544370f64f19224e9243eae0942ac"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3384ec6c907acb911c4a9c32bcd473ca"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3384ec6c907acb911c4a9c32bcd473caa521219142a95c322e501497ab6262798"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3384ec6c907acb911c4a9c32bcd473caaec46850a66dfd2d6bfcb18849a737fdc"></a>
<a id="amodem_2ubx_2protocol_8h_html_a342c0d62cf874ccb8b657ce85d91efe0"></a>
<a id="amodem_2ubx_2protocol_8h_html_a342c0d62cf874ccb8b657ce85d91efe0a1e324c97e68e6d7ce35feb4ffe2ca617"></a>
<a id="amodem_2ubx_2protocol_8h_html_a342c0d62cf874ccb8b657ce85d91efe0a29354369703a5e54ae7e49edfff886ff"></a>
<a id="amodem_2ubx_2protocol_8h_html_a342c0d62cf874ccb8b657ce85d91efe0aa60a16ce7e100e06e0bab9a3922003a6"></a>
<a id="amodem_2ubx_2protocol_8h_html_a359b0f88d3769af43c2b1699eb172f23"></a>
<a id="amodem_2ubx_2protocol_8h_html_a359b0f88d3769af43c2b1699eb172f23a34b4b516760245d0a5bbfcbb5937d74c"></a>
<a id="amodem_2ubx_2protocol_8h_html_a359b0f88d3769af43c2b1699eb172f23a6fe85d7688c6730a492981fdc4623c67"></a>
<a id="amodem_2ubx_2protocol_8h_html_a359b0f88d3769af43c2b1699eb172f23a8bc6c6397d5bc342ebe0ea36522e96a5"></a>
<a id="amodem_2ubx_2protocol_8h_html_a359b0f88d3769af43c2b1699eb172f23a8eeae948253c11b7f097dd06896e66f8"></a>
<a id="amodem_2ubx_2protocol_8h_html_a359b0f88d3769af43c2b1699eb172f23ab6c294e0f55696a8c90ec8211673ca80"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7a036303b6caf601b73bfb48b3a7423309"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7a871b880c791ad49c55164856ac4f83f9"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7a89a96eb89044b208d3a6c29fc273fa26"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7aa31397b2154b0f1f9b1e906c91a6bc8c"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7ace6e98ad1c1ac7232327d42b0f4302ef"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7ad2c8bf68306ca6bb22e88c5c6d957453"></a>
<a id="amodem_2ubx_2protocol_8h_html_a43766ad4c0fd1d31fd547c090e3f39b6"></a>
<a id="amodem_2ubx_2protocol_8h_html_a43766ad4c0fd1d31fd547c090e3f39b6a1621ed3281429f96fc598d90cc388c95"></a>
<a id="amodem_2ubx_2protocol_8h_html_a43766ad4c0fd1d31fd547c090e3f39b6a67b9cba109cc8f57a38c41b1d521e3c7"></a>
<a id="amodem_2ubx_2protocol_8h_html_a43766ad4c0fd1d31fd547c090e3f39b6aaef8449ed29d6dd76bdd34157d873896"></a>
<a id="amodem_2ubx_2protocol_8h_html_a450f46250ef486af4f933e69ddbb42d2"></a>
<a id="amodem_2ubx_2protocol_8h_html_a4c64b9118da471baa6a7a88ee345bf66"></a>
<a id="amodem_2ubx_2protocol_8h_html_a58dc8b84784731500aa7f55afeb7e582"></a>
<a id="amodem_2ubx_2protocol_8h_html_a58dc8b84784731500aa7f55afeb7e582a43616a8ad2465c7521aa9ed28460cf57"></a>
<a id="amodem_2ubx_2protocol_8h_html_a58dc8b84784731500aa7f55afeb7e582a61cbc043ccd0a96ba2327d7bd95189c6"></a>
<a id="amodem_2ubx_2protocol_8h_html_a58dc8b84784731500aa7f55afeb7e582a73aeb813a098d600dfb60561bc042e2a"></a>
<a id="amodem_2ubx_2protocol_8h_html_a58dc8b84784731500aa7f55afeb7e582a9f36e6c7688a62737beb203e82de91ef"></a>
<a id="amodem_2ubx_2protocol_8h_html_a58dc8b84784731500aa7f55afeb7e582af5ccdcc3eed53b0906b83667443e3667"></a>
<a id="amodem_2ubx_2protocol_8h_html_a5cc2a8f42fd62032afa3cd7687452896"></a>
<a id="amodem_2ubx_2protocol_8h_html_a5cc2a8f42fd62032afa3cd7687452896a0e9177345e82ad614c1ab4c8b52b9265"></a>
<a id="amodem_2ubx_2protocol_8h_html_a5cc2a8f42fd62032afa3cd7687452896a7fd6f4b7557dfa6511dcb6354963d342"></a>
<a id="amodem_2ubx_2protocol_8h_html_a5cc2a8f42fd62032afa3cd7687452896ac02d28b95ef601af32dc898e35ad252e"></a>
<a id="amodem_2ubx_2protocol_8h_html_a5cc2a8f42fd62032afa3cd7687452896aca25f86cc1d85c60b1d67509d0e9506b"></a>
<a id="amodem_2ubx_2protocol_8h_html_a621d2fae9721b6dc62a71801f3b7952e"></a>
<a id="amodem_2ubx_2protocol_8h_html_a621d2fae9721b6dc62a71801f3b7952ea30f66599c483f622607f0b13ad0451f8"></a>
<a id="amodem_2ubx_2protocol_8h_html_a621d2fae9721b6dc62a71801f3b7952ea519dc8f11c80b5a08771fbc36c70fbb8"></a>
<a id="amodem_2ubx_2protocol_8h_html_a621d2fae9721b6dc62a71801f3b7952ea5be3c906a6c528f65575990041b7e6ce"></a>
<a id="amodem_2ubx_2protocol_8h_html_a621d2fae9721b6dc62a71801f3b7952ea7a2d00bdb7fef5ff7da1d3a682a1b82e"></a>
<a id="amodem_2ubx_2protocol_8h_html_a621d2fae9721b6dc62a71801f3b7952eab7ed326b5da1087afb8d531d97bb9f16"></a>
<a id="amodem_2ubx_2protocol_8h_html_a621d2fae9721b6dc62a71801f3b7952eacc3989fab9e22270c389b0318bbe45ea"></a>
<a id="amodem_2ubx_2protocol_8h_html_a6711a33292bf25327950406b96585690"></a>
<a id="amodem_2ubx_2protocol_8h_html_a6711a33292bf25327950406b96585690a2dad67829bb51786024771c0d5a6d103"></a>
<a id="amodem_2ubx_2protocol_8h_html_a6711a33292bf25327950406b96585690a31a403a2013dc9da3da56366fa95f19b"></a>
<a id="amodem_2ubx_2protocol_8h_html_a6711a33292bf25327950406b96585690a4e14cf64a03e9d37af198870b0616497"></a>
<a id="amodem_2ubx_2protocol_8h_html_a6711a33292bf25327950406b96585690a931ed807a91dd1f0e6e2cfa013860cbe"></a>
<a id="amodem_2ubx_2protocol_8h_html_a6711a33292bf25327950406b96585690ac3f1631647cfd0246be61fc78549a9f7"></a>
<a id="amodem_2ubx_2protocol_8h_html_a6711a33292bf25327950406b96585690adca8434b24978430d03939b81d76fbb9"></a>
<a id="amodem_2ubx_2protocol_8h_html_a887b1fa6af0d6d08cc51ed65de64a78a"></a>
<a id="amodem_2ubx_2protocol_8h_html_a887b1fa6af0d6d08cc51ed65de64a78aa019364b4a4482098acc0d7821b456b83"></a>
<a id="amodem_2ubx_2protocol_8h_html_a887b1fa6af0d6d08cc51ed65de64a78aae7769c1dd298aabbad37ddaf6260eb4d"></a>
<a id="amodem_2ubx_2protocol_8h_html_a887b1fa6af0d6d08cc51ed65de64a78aaeacece1ca309918fa3abe7a02911f5ca"></a>
<a id="amodem_2ubx_2protocol_8h_html_a887b1fa6af0d6d08cc51ed65de64a78aaeea043882f976e34008f261e1b2ee5ac"></a>
<a id="amodem_2ubx_2protocol_8h_html_a8a935ea7debb4ac73ea99c98d6ef4d3b"></a>
<a id="amodem_2ubx_2protocol_8h_html_a8a935ea7debb4ac73ea99c98d6ef4d3ba8f887b777e29fc05107ac406d4a87458"></a>
<a id="amodem_2ubx_2protocol_8h_html_a8a935ea7debb4ac73ea99c98d6ef4d3bae87d4355340186b8a049346e3076f9ae"></a>
<a id="amodem_2ubx_2protocol_8h_html_a94709ee4f4afe0194790893251ee2b4c"></a>
<a id="amodem_2ubx_2protocol_8h_html_a94709ee4f4afe0194790893251ee2b4ca06c8d5338db83ce4a74a92228f04ffb1"></a>
<a id="amodem_2ubx_2protocol_8h_html_a94709ee4f4afe0194790893251ee2b4ca461834aa0d5d6ddec370ecd247e330e6"></a>
<a id="amodem_2ubx_2protocol_8h_html_a94709ee4f4afe0194790893251ee2b4caea0ef9695c70807a5bdfb1725f31ea3f"></a>
<a id="amodem_2ubx_2protocol_8h_html_a94709ee4f4afe0194790893251ee2b4caf762dc50babaacd4cbb1ce753a8c0ae9"></a>
<a id="amodem_2ubx_2protocol_8h_html_a9e5e9af7a281e53f2b950089ee66561f"></a>
<a id="amodem_2ubx_2protocol_8h_html_a9e5e9af7a281e53f2b950089ee66561fa172bc7d2ed80cadb4077ae42233764b2"></a>
<a id="amodem_2ubx_2protocol_8h_html_a9e5e9af7a281e53f2b950089ee66561fa1a39257d816910b26f2323b61a278519"></a>
<a id="amodem_2ubx_2protocol_8h_html_a9e5e9af7a281e53f2b950089ee66561fa4f147b313644dba74c95930038201cf7"></a>
<a id="amodem_2ubx_2protocol_8h_html_a9e5e9af7a281e53f2b950089ee66561fa59c3bbc8cb2a44e26920adbe0251375b"></a>
<a id="amodem_2ubx_2protocol_8h_html_a9e5e9af7a281e53f2b950089ee66561fa6d89a732b306e21feeaee51cdbcc0bed"></a>
<a id="amodem_2ubx_2protocol_8h_html_a9e5e9af7a281e53f2b950089ee66561fa736709e926d95754fef9260c596530e2"></a>
<a id="amodem_2ubx_2protocol_8h_html_a9e5e9af7a281e53f2b950089ee66561fa8a2a4bb1bb5b7f69960fdcde374f2ee6"></a>
<a id="amodem_2ubx_2protocol_8h_html_a9e5e9af7a281e53f2b950089ee66561fa9bb36ad38aca4f118fe1bdc2f0351476"></a>
<a id="amodem_2ubx_2protocol_8h_html_a9e5e9af7a281e53f2b950089ee66561faa062bfc1af7cc119d025dee309ac1d25"></a>
<a id="amodem_2ubx_2protocol_8h_html_a9e5e9af7a281e53f2b950089ee66561fae4640365810ae80e8c24507fd7279f3d"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6c"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6ca07aa8c55e3504c0d19b1e123f4d2e7c7"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6ca263a724b491a6303d5486828a49a8961"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6ca2a5cc3b49abc9be0c6bbab0a9963ba03"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6ca39492ba0c78d0290819b9410e2e55781"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6ca5174a26b3b79356bf06402de46bc0774"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6ca58ad56a546a2df6c9359927375da9904"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6ca5c12f57e0b4de16d09fc42f23740908b"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6ca6435225efac8c7ef6e336a84fa2e8932"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6ca7f1d764aa078c284c575ec610d4f4853"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6ca8787502b2d9a14d2ce79b1ce1713d6f3"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6ca884ab2ce56a1f7a08d4b9d06b944ad37"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6ca99b8f62b1d204b335a06ed6f3ef214e6"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6caa2c68fe9d01bc4acf3054d667f3e2a77"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6cac84f9ad61c85bbce60e680639c3d88ad"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6cad58d4ac5b57cbdd42d360560cc16fc0e"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6cae3c6e42e75e69a34d7017d2f2aa3c70d"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6cae6a2501b586793e75cdd0085170a9a27"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6caef6c925e20f072665bf55e435d37a6ac"></a>
<a id="amodem_2ubx_2protocol_8h_html_aa221b68c53f25634d9f2f435f28c1a6cafea982067c784c47ae5b1ad7e91b4191"></a>
<a id="amodem_2ubx_2protocol_8h_html_acdc0d9b7d25df6aba6bb091e7034f5ba"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18a0d9d5044c9df2a6b61b7a46a4f24e895"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18a1e35a224f4809d3a59d0f1570bf382bb"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18a418aca13d3bd1608869494d26559e52f"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18a5e4eaf66a7356e73b4c6e4949160f321"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18a760de1a9f06cc6d4832da868d01702c4"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18a7e7c3645f46ba3c2e8329ae3a9eeaa79"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18a898b493832d06586cf48f9a2545651d0"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18a8c700fd2062d8dc51c5e4b28c98c6cf0"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18a8f46002e33dddab6782bad93ab3fd8b1"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18aba0a811e14f9e87bd47bfbeaad24e11b"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18ac9200dedb25cfa03b80f4336e86db5ed"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18aee43a865c5815ce058261f5f0550fa2b"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad7e0ffe55e8dbd97caa5bc089d33540c"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad7e0ffe55e8dbd97caa5bc089d33540ca1fe2554bbbf05c86d3f9b0bc50927c1b"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad7e0ffe55e8dbd97caa5bc089d33540caca3b7f2a39ff93b91b8317245e8375ab"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad8d6229db563db619d4f0a9f225fb640"></a>
<a id="amodem_2ubx_2protocol_8h_html_adb6a6e16f193bc70840b2dd12dbc9baa"></a>
<a id="amodem_2ubx_2protocol_8h_html_adb6a6e16f193bc70840b2dd12dbc9baaa3af5f6c24fade976d4ece339e9240114"></a>
<a id="amodem_2ubx_2protocol_8h_html_adb6a6e16f193bc70840b2dd12dbc9baaa5c7c1a24670995305bcb8e98cfd1fa19"></a>
<a id="amodem_2ubx_2protocol_8h_html_adb6a6e16f193bc70840b2dd12dbc9baaaa0ee1de6e26bb0585f24fddbe3d7ec9a"></a>
<a id="amodem_2ubx_2protocol_8h_html_adb6a6e16f193bc70840b2dd12dbc9baaaccb591a437d0ed7cca8888f41b855efb"></a>
<a id="amodem_2ubx_2protocol_8h_html_afbba8ada09d6c6489d52a3b9dc31725f"></a>
<a id="amodem_2ubx_2protocol_8h_html_afbba8ada09d6c6489d52a3b9dc31725fa3661b89022659975720d3a022b21f194"></a>
<a id="amodem_2ubx_2protocol_8h_html_afbba8ada09d6c6489d52a3b9dc31725fa7dcaa32f001d1a7b5b071cdf7621081e"></a>
<a id="amodem_2ubx_2protocol_8h_html_afbba8ada09d6c6489d52a3b9dc31725fa95ea7c01a987a1e334f41c79642b8139"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astring_8h_html_af0f01bffcd16daa9143f6014d10a25ad"></a>
<a id="astructubx__ack_html"></a>
<a id="astructubx__ack_html_ab68abe2083b8446a2e3ffc4b603ac47d"></a>
<a id="astructubx__cfg__msg__rate_html"></a>
<a id="astructubx__cfg__msg__rate_html_a7a030b3e70356b899ed7284e750041b0"></a>
<a id="astructubx__cfg__msg__rate_html_aee7d34d68f3665c665f8ae4bc6d1a04a"></a>
<a id="astructubx__cfg__nav5_html"></a>
<a id="astructubx__cfg__nav5_html_a19d69c52edac0f65e2892b4c476d5a76"></a>
<a id="astructubx__cfg__nav5_html_a2e7353d4ef2f0b3eef4ae3d1cc2be5ed"></a>
<a id="astructubx__cfg__nav5_html_a2ee4fc58054c5f049890914c73089c99"></a>
<a id="astructubx__cfg__nav5_html_a4d8537de40aa5c98ae2e2183da9d44c3"></a>
<a id="astructubx__cfg__nav5_html_a564548f9609493061e995219f6397060"></a>
<a id="astructubx__cfg__nav5_html_a5afd803452c65c4f03b122c9ff59cf2b"></a>
<a id="astructubx__cfg__nav5_html_a6108faff3832cab3d734020c030c5c6c"></a>
<a id="astructubx__cfg__nav5_html_a648e22442293b24b2aa8b264a78b9bd2"></a>
<a id="astructubx__cfg__nav5_html_a70f931b76bcd7a07a225648a15e73493"></a>
<a id="astructubx__cfg__nav5_html_a7c7f4338463e4d0c8040971ec31dc92c"></a>
<a id="astructubx__cfg__nav5_html_aab1b8aec77c186c576be839f728bba70"></a>
<a id="astructubx__cfg__nav5_html_ab6b5cd2ef8db8c281f77c6684f6f8c0c"></a>
<a id="astructubx__cfg__nav5_html_abb48bda50e725eb8c2973518b468916f"></a>
<a id="astructubx__cfg__nav5_html_abf2a3de97f8d9cade6ec18408452938a"></a>
<a id="astructubx__cfg__nav5_html_ac3d21a048e77c404bcfa180af2e41992"></a>
<a id="astructubx__cfg__nav5_html_ace7d12cf8f63904274e658a6afe149d5"></a>
<a id="astructubx__cfg__nav5_html_ad78a8828482ce26597f80f5e5a548afd"></a>
<a id="astructubx__cfg__nav5_html_ae0ecd871977ad119009cf1a2ac617327"></a>
<a id="astructubx__cfg__nav5_html_af915a692066df1855c270e106c1981ca"></a>
<a id="astructubx__cfg__prt_html"></a>
<a id="astructubx__cfg__prt_html_a1d4df224a3a9e7e6031a418745ee4e95"></a>
<a id="astructubx__cfg__prt_html_a1f4f3ab473e80648043b792bc4d5022f"></a>
<a id="astructubx__cfg__prt_html_a571753eb8aba5610fb7bc3546b7bfce9"></a>
<a id="astructubx__cfg__prt_html_a836be3302c1e038fbc09712242a51e69"></a>
<a id="astructubx__cfg__prt_html_a960fd4543476b89b56f23dd29774b196"></a>
<a id="astructubx__cfg__prt_html_aba6bef46b7818a2396b77a0b1245ecc5"></a>
<a id="astructubx__cfg__prt_html_ac83072a87e0b29b30e6406f4f61cf26d"></a>
<a id="astructubx__cfg__prt_html_ad2bf468b82cc86ae1ce99c2fa129c231"></a>
<a id="astructubx__cfg__prt_html_af5a445ab598a2b93e884c916fe13affc"></a>
<a id="astructubx__cfg__rate_html"></a>
<a id="astructubx__cfg__rate_html_a444822a3a37dd51313bfc6968a3b4721"></a>
<a id="astructubx__cfg__rate_html_aafcbb36f844534c77e698dceccb2f5dc"></a>
<a id="astructubx__cfg__rate_html_ae64d779c4a3fe255710be8f742f5b6c6"></a>
<a id="astructubx__cfg__rst_html"></a>
<a id="astructubx__cfg__rst_html_a1a63d295cf71e23a4afdb31637741b4f"></a>
<a id="astructubx__cfg__rst_html_a7d7e94ffc6aa9518a31b3f829a732362"></a>
<a id="astructubx__cfg__rst_html_aa1f7a46662f14e498b8bce84fb349d33"></a>
<a id="astructubx__cfg__val__hdr_html"></a>
<a id="astructubx__cfg__val__hdr_html_a4d7a91e9521428e5b528ced88b030cd3"></a>
<a id="astructubx__cfg__val__hdr_html_a6206dc714df9656cc37e0b802ab541b8"></a>
<a id="astructubx__cfg__val__hdr_html_aa835050e25c8db0a5a88954ff0def88c"></a>
<a id="astructubx__cfg__val__u16_html"></a>
<a id="astructubx__cfg__val__u16_html_a32e877f1e2f60b209fbcdd057aa82c4f"></a>
<a id="astructubx__cfg__val__u16_html_a6226f1b8f4cb89cb318c07ff8ddcbbde"></a>
<a id="astructubx__cfg__val__u16_html_a87a9c181318e297935bb1eb65093d4a8"></a>
<a id="astructubx__cfg__val__u32_html"></a>
<a id="astructubx__cfg__val__u32_html_a2c1d446c7c8bef80052d2438fb998d58"></a>
<a id="astructubx__cfg__val__u32_html_ab02aa8d3b7039c06692a805aed30f246"></a>
<a id="astructubx__cfg__val__u32_html_adc51df7bc8a50e1ca8843067bb309ac9"></a>
<a id="astructubx__cfg__val__u8_html"></a>
<a id="astructubx__cfg__val__u8_html_a2c1cbf9a552608150eafc1f2d92b03b5"></a>
<a id="astructubx__cfg__val__u8_html_a325aaaf688433cab710d0c3e835fb9ed"></a>
<a id="astructubx__cfg__val__u8_html_a793646932ce054ab8561078981f57250"></a>
<a id="astructubx__frame__match_html"></a>
<a id="astructubx__frame__match_html_a36c5fd74bd6d506111b1ef2ac39cb68a"></a>
<a id="astructubx__frame__match_html_abbc954596995ca2dfe65de3e310e02a0"></a>
<a id="astructubx__frame__match_html_ae65eaf921576c61ad758bfedc56d89c6"></a>
<a id="astructubx__frame__match_html_af78f70c27f4334fd1dcaac72d9e4ece6"></a>
<a id="astructubx__frame_html"></a>
<a id="astructubx__frame_html_a2dcc29a82e7dfff2d1e4194f1bc035e8"></a>
<a id="astructubx__frame_html_a4e578da5900365d498708f7a61d48ba4"></a>
<a id="astructubx__frame_html_a70c465b5bd1e9837c253d78fb210f4ce"></a>
<a id="astructubx__frame_html_a77b5030a6b95aef58b1c17f0368dd7ce"></a>
<a id="astructubx__frame_html_ac61fb72df7c1cd8a9bacb787071cb77d"></a>
<a id="astructubx__frame_html_acf80f38e8f26bb32848ae2978a1f87a1"></a>
<a id="astructubx__mon__gnss_html"></a>
<a id="astructubx__mon__gnss_html_a045256bfbf8fe9b398ef77d10e00395a"></a>
<a id="astructubx__mon__gnss_html_a2b94264d40d0aa740b20d9fa9565d155"></a>
<a id="astructubx__mon__gnss_html_a34b9073dda3d6ad734109cea8ba5a0d2"></a>
<a id="astructubx__mon__gnss_html_a8f76d361c23ae4a94d29277be0aa36f8"></a>
<a id="astructubx__mon__gnss_html_ad09bcd6e739e385c275f8a1cae8725b3"></a>
<a id="astructubx__mon__gnss_html_ae004377f656dede9b0ebe98caeea588f"></a>
<a id="astructubx__mon__gnss_html_aebcccc44a80ef3b327d7d479ccb5ebe5"></a>
<a id="astructubx__mon__ver_html"></a>
<a id="astructubx__mon__ver_html_a07a2fdbe52fa48e9412f39bff1256318"></a>
<a id="astructubx__mon__ver_html_aa0495c27ac850d56ddaa92bc4689ba7f"></a>
<a id="astructubx__nav__pvt_html"></a>
<a id="astructubx__nav__pvt_html_a10b14934d80d80d3c2f0c36866bd4a64"></a>
<a id="astructubx__nav__pvt_html_a1753595f0a3935449dee4d0c57e88a6e"></a>
<a id="astructubx__nav__pvt_html_a17c628b0acca293f068b58eff32ae4dd"></a>
<a id="astructubx__nav__pvt_html_a18b61263b433dc5f81c2becff9c6743c"></a>
<a id="astructubx__nav__pvt_html_a1bdc3cb0e4a2b6bef1c4216963e5c29c"></a>
<a id="astructubx__nav__pvt_html_a1c21c3b882412f36f96c59cda1d948d9"></a>
<a id="astructubx__nav__pvt_html_a1d50e696fa2684b55d04c652c85f2e16"></a>
<a id="astructubx__nav__pvt_html_a2ff7d8bcc13ee956d9535c61efefada6"></a>
<a id="astructubx__nav__pvt_html_a34ec5fc41c4b323b4719803f1ff01bed"></a>
<a id="astructubx__nav__pvt_html_a38a8612a53966a1d598bf6d17443da7d"></a>
<a id="astructubx__nav__pvt_html_a39b72f654fc8130c611ac839189914ed"></a>
<a id="astructubx__nav__pvt_html_a3b780d7b790b07a8ee23431969cbc318"></a>
<a id="astructubx__nav__pvt_html_a426086b12ff09fb8a00dd4623fea307e"></a>
<a id="astructubx__nav__pvt_html_a450638fda7b9d1929145575e4c576ec1"></a>
<a id="astructubx__nav__pvt_html_a4958a6c11bd812477d11467ab3384161"></a>
<a id="astructubx__nav__pvt_html_a4f63a0f15b823e5258fdb826d2636828"></a>
<a id="astructubx__nav__pvt_html_a7e5dc3449e52a36cb2bc5841bbf6fec8"></a>
<a id="astructubx__nav__pvt_html_a80139f6d95bf943f5c6de6af1ea50e3e"></a>
<a id="astructubx__nav__pvt_html_a84c6640806485f270b8d51d06cc49709"></a>
<a id="astructubx__nav__pvt_html_a8fc4b24fb8ffde02d306bc1b6770b1d8"></a>
<a id="astructubx__nav__pvt_html_a955d0f7927f68f540f2e9a2c91e46e79"></a>
<a id="astructubx__nav__pvt_html_aa332fc93448eb6b30ad8bbaa5760db5c"></a>
<a id="astructubx__nav__pvt_html_aa8b31a49c2844501505412da226872e1"></a>
<a id="astructubx__nav__pvt_html_ab0df156e9f8009bebfbbdb39c63c4191"></a>
<a id="astructubx__nav__pvt_html_abd97f003ba43b70ffea2e9fdf5702c4f"></a>
<a id="astructubx__nav__pvt_html_ac0265c113f01ae2bab8553eb7148e3ae"></a>
<a id="astructubx__nav__pvt_html_acbb58f36eb572ce27b050a8c7540f91d"></a>
<a id="astructubx__nav__pvt_html_ad90042dc5e00b91f004badcb0c3a5f4c"></a>
<a id="astructubx__nav__pvt_html_ae47fc34dfd91687590bd96afe2fab091"></a>
<a id="astructubx__nav__pvt_html_ae6ba97f3406b9fdbbf04c4bb3e744668"></a>
<a id="astructubx__nav__pvt_html_aea613eb3d604d33120e82c569c5f10e9"></a>
<a id="astructubx__nav__pvt_html_aeadb05fe45a3a0539c899129e40059fd"></a>
<a id="astructubx__nav__pvt_html_aeb710663626935d21c77a5cfe1030795"></a>
<a id="astructubx__nav__pvt_html_af5b3e0e70b3470bd1686ddbfefb419f9"></a>
<a id="astructubx__nav__sat_1_1ubx__nav__sat__info_html"></a>
<a id="astructubx__nav__sat_1_1ubx__nav__sat__info_html_a04fc29e6cf9f1ff6f1f638ae633d5a11"></a>
<a id="astructubx__nav__sat_1_1ubx__nav__sat__info_html_a3a50255230b6ed80bfa4eb8ff83acf89"></a>
<a id="astructubx__nav__sat_1_1ubx__nav__sat__info_html_a442709d1e9b43ae8c27606a5fb878c89"></a>
<a id="astructubx__nav__sat_1_1ubx__nav__sat__info_html_a83e6ba9e50cc24fc0d80de3947daf571"></a>
<a id="astructubx__nav__sat_1_1ubx__nav__sat__info_html_a9133131e06119371d14be09f99b24a8e"></a>
<a id="astructubx__nav__sat_1_1ubx__nav__sat__info_html_ab7ba4e9d36ab136c0bb8fde9b4f9b3e5"></a>
<a id="astructubx__nav__sat_1_1ubx__nav__sat__info_html_ac6872360564b383ce2cd5a061717c8fe"></a>
<a id="astructubx__nav__sat_html"></a>
<a id="astructubx__nav__sat_html_a6f5bf3da0f5633aa95ff4d736656cb21"></a>
<a id="astructubx__nav__sat_html_a7204f8b1b28f3dc0970fa62567885cdc"></a>
<a id="astructubx__nav__sat_html_aac587fd77fa832021ebca87e7897eb2e"></a>
<a id="astructubx__nav__sat_html_ade983d7b35cf81a6d769979f7cb5919d"></a>
<a id="astructubx__nav__sat_html_ae0bea798d815cc25e837e3fa394fb429"></a>

```c
/*
 * Copyright (c) 2025 Croxel Inc.
 * Copyright (c) 2025 CogniPilot Foundation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MODEM_UBX_PROTOCOL_H_
#define ZEPHYR_INCLUDE_MODEM_UBX_PROTOCOL_H_

#include <stdint.h>
#include <zephyr/modem/ubx/checksum.h>

#define UBX_FRAME_HEADER_SZ                     6
#define UBX_FRAME_FOOTER_SZ                     2
#define UBX_FRAME_SZ_WITHOUT_PAYLOAD            (UBX_FRAME_HEADER_SZ + UBX_FRAME_FOOTER_SZ)
#define UBX_FRAME_SZ(payload_size)              (payload_size + UBX_FRAME_SZ_WITHOUT_PAYLOAD)

#define UBX_PREAMBLE_SYNC_CHAR_1                0xB5
#define UBX_PREAMBLE_SYNC_CHAR_2                0x62

#define UBX_FRAME_PREAMBLE_SYNC_CHAR_1_IDX      0
#define UBX_FRAME_PREAMBLE_SYNC_CHAR_2_IDX      1
#define UBX_FRAME_MSG_CLASS_IDX                 2

#define UBX_PAYLOAD_SZ_MAX                      512
#define UBX_FRAME_SZ_MAX                        UBX_FRAME_SZ(UBX_PAYLOAD_SZ_MAX)

struct ubx_frame {
        uint8_t preamble_sync_char_1;
        uint8_t preamble_sync_char_2;
        uint8_t class;
        uint8_t id;
        uint16_t payload_size;
        uint8_t payload_and_checksum[];
};

struct ubx_frame_match {
        uint8_t class;
        uint8_t id;
        struct {
                uint8_t *buf;
                uint16_t len;
        } payload;
};

enum ubx_class_id {
        UBX_CLASS_ID_NAV = 0x01,  /* Navigation Results Messages */
        UBX_CLASS_ID_RXM = 0x02,  /* Receiver Manager Messages */
        UBX_CLASS_ID_INF = 0x04,  /* Information Messages */
        UBX_CLASS_ID_ACK = 0x05,  /* Ack/Nak Messages */
        UBX_CLASS_ID_CFG = 0x06,  /* Configuration Input Messages */
        UBX_CLASS_ID_UPD = 0x09,  /* Firmware Update Messages */
        UBX_CLASS_ID_MON = 0x0A,  /* Monitoring Messages */
        UBX_CLASS_ID_TIM = 0x0D,  /* Timing Messages */
        UBX_CLASS_ID_MGA = 0x13,  /* Multiple GNSS Assistance Messages */
        UBX_CLASS_ID_LOG = 0x21,  /* Logging Messages */
        UBX_CLASS_ID_SEC = 0x27,  /* Security Feature Messages */
        UBX_CLASS_ID_NMEA_STD = 0xF0, /* Note: Only used to configure message rate */
        UBX_CLASS_ID_NMEA_PUBX = 0xF1, /* Note: Only used to configure message rate */
};

enum ubx_msg_id_nav {
        UBX_MSG_ID_NAV_PVT = 0x07,
        UBX_MSG_ID_NAV_SAT = 0x35,
};

enum ubx_nav_fix_type {
        UBX_NAV_FIX_TYPE_NO_FIX = 0,
        UBX_NAV_FIX_TYPE_DR = 1,
        UBX_NAV_FIX_TYPE_2D = 2,
        UBX_NAV_FIX_TYPE_3D = 3,
        UBX_NAV_FIX_TYPE_GNSS_DR_COMBINED = 4,
        UBX_NAV_FIX_TYPE_TIME_ONLY = 5,
};

enum ubx_nav_hp_dgnss_mode {
        UBX_NAV_HP_DGNSS_MODE_RTK_FLOAT = 2,
        UBX_NAV_HP_DGNSS_MODE_RTK_FIXED = 3,
};

#define UBX_NAV_PVT_VALID_DATE                          BIT(0)
#define UBX_NAV_PVT_VALID_TIME                          BIT(1)
#define UBX_NAV_PVT_VALID_UTC_TOD                       BIT(2)
#define UBX_NAV_PVT_VALID_MAGN                          BIT(3)

#define UBX_NAV_PVT_FLAGS_GNSS_FIX_OK                   BIT(0)
#define UBX_NAV_PVT_FLAGS_GNSS_CARR_SOLN_FLOATING       BIT(6)
#define UBX_NAV_PVT_FLAGS_GNSS_CARR_SOLN_FIXED          BIT(7)

#define UBX_NAV_PVT_FLAGS3_INVALID_LLH                  BIT(0)

struct ubx_nav_pvt {
        struct {
                uint32_t itow;
                uint16_t year;
                uint8_t month;
                uint8_t day;
                uint8_t hour;
                uint8_t minute;
                uint8_t second;
                uint8_t valid;
                uint32_t tacc;
                int32_t nano;
        } __packed time;
        uint8_t fix_type;
        uint8_t flags;
        uint8_t flags2;
        struct {
                uint8_t num_sv;
                int32_t longitude; /* Longitude. Degrees. scaling: 1e-7 */
                int32_t latitude; /* Latitude. Degrees. scaling: 1e-7 */
                int32_t height; /* Height above ellipsoid. mm */
                int32_t hmsl; /* Height above mean sea level. mm */
                uint32_t horiz_acc; /* Horizontal accuracy estimate. mm */
                uint32_t vert_acc; /* Vertical accuracy estimate. mm */
                int32_t vel_north; /* NED north velocity. mm/s */
                int32_t vel_east; /* NED east velocity. mm/s */
                int32_t vel_down; /* NED down velocity. mm/s */
                int32_t ground_speed; /* Ground Speed (2D). mm/s */
                int32_t head_motion; /* Heading of Motion (2D). Degrees. scaling: 1e-5 */
                uint32_t speed_acc; /* Speed accuracy estimated. mm/s */
                uint32_t head_acc;
                uint16_t pdop; /* scaling: 1e-2 */
                uint16_t flags3;
                uint32_t reserved;
                int32_t head_vehicle; /* Heading of vehicle (2D). Degrees. Valid if
                                       * flags.head_vehicle_valid is set.
                                       */
                int16_t mag_decl; /* Magnetic declination. Degrees. */
                uint16_t magacc; /* Magnetic declination accuracy. Degrees. scaling: 1e-2 */
        } __packed nav;
} __packed;

enum ubx_nav_sat_health {
        UBX_NAV_SAT_HEALTH_UNKNOWN = 0,
        UBX_NAV_SAT_HEALTH_HEALTHY = 1,
        UBX_NAV_SAT_HEALTH_UNHEALTHY = 2,
};

enum ubx_gnss_id {
        UBX_GNSS_ID_GPS = 0,
        UBX_GNSS_ID_SBAS = 1,
        UBX_GNSS_ID_GALILEO = 2,
        UBX_GNSS_ID_BEIDOU = 3,
        UBX_GNSS_ID_QZSS = 5,
        UBX_GNSS_ID_GLONASS = 6,
};

#define UBX_NAV_SAT_FLAGS_SV_USED                       BIT(3)
#define UBX_NAV_SAT_FLAGS_RTCM_CORR_USED                BIT(17)

struct ubx_nav_sat {
        uint32_t itow;
        uint8_t version; /* Message version. */
        uint8_t num_sv;
        uint16_t reserved1;
        struct ubx_nav_sat_info {
                uint8_t gnss_id; /* See ubx_gnss_id */
                uint8_t sv_id;
                uint8_t cno; /* Carrier-to-noise ratio. dBHz */
                int8_t elevation; /* Elevation (range: +/- 90). Degrees */
                int16_t azimuth; /* Azimuth (range: 0 - 360). Degrees */
                int16_t pseu_res; /* Pseudorange Residual. Meters */
                uint32_t flags;
        } sat[];
};

enum ubx_msg_id_ack {
        UBX_MSG_ID_ACK = 0x01,
        UBX_MSG_ID_NAK = 0x00
};

enum ubx_msg_id_cfg {
        UBX_MSG_ID_CFG_PRT = 0x00,
        UBX_MSG_ID_CFG_MSG = 0x01,
        UBX_MSG_ID_CFG_RST = 0x04,
        UBX_MSG_ID_CFG_RATE = 0x08,
        UBX_MSG_ID_CFG_NAV5 = 0x24,
        UBX_MSG_ID_CFG_VAL_SET = 0x8A,
        UBX_MSG_ID_CFG_VAL_GET = 0x8B,
};

enum ubx_msg_id_mon {
        UBX_MSG_ID_MON_VER = 0x04,
        UBX_MSG_ID_MON_GNSS = 0x28,
};

struct ubx_ack {
        uint8_t class;
        uint8_t id;
};

#define UBX_GNSS_SELECTION_GPS                          BIT(0)
#define UBX_GNSS_SELECTION_GLONASS                      BIT(1)
#define UBX_GNSS_SELECTION_BEIDOU                       BIT(2)
#define UBX_GNSS_SELECTION_GALILEO                      BIT(3)

struct ubx_mon_gnss {
        uint8_t ver;
        struct {
                uint8_t supported;
                uint8_t default_enabled;
                uint8_t enabled;
        } selection;
        uint8_t simultaneous;
        uint8_t reserved1[3];
} __packed;

enum ubx_cfg_port_id {
        UBX_CFG_PORT_ID_DDC = 0,
        UBX_CFG_PORT_ID_UART = 1,
        UBX_CFG_PORT_ID_USB = 2,
        UBX_CFG_PORT_ID_SPI = 3,
};

enum ubx_cfg_char_len {
        UBX_CFG_PRT_PORT_MODE_CHAR_LEN_5 = 0, /* Not supported */
        UBX_CFG_PRT_PORT_MODE_CHAR_LEN_6 = 1, /* Not supported */
        UBX_CFG_PRT_PORT_MODE_CHAR_LEN_7 = 2, /* Supported only with parity */
        UBX_CFG_PRT_PORT_MODE_CHAR_LEN_8 = 3,
};

enum ubx_cfg_parity {
        UBX_CFG_PRT_PORT_MODE_PARITY_EVEN = 0,
        UBX_CFG_PRT_PORT_MODE_PARITY_ODD = 1,
        UBX_CFG_PRT_PORT_MODE_PARITY_NONE = 4,
};

enum ubx_cfg_stop_bits {
        UBX_CFG_PRT_PORT_MODE_STOP_BITS_1 = 0,
        UBX_CFG_PRT_PORT_MODE_STOP_BITS_1_5 = 1,
        UBX_CFG_PRT_PORT_MODE_STOP_BITS_2 = 2,
        UBX_CFG_PRT_PORT_MODE_STOP_BITS_0_5 = 3,
};

#define UBX_CFG_PRT_MODE_CHAR_LEN(val)                  (((val) & BIT_MASK(2)) << 6)
#define UBX_CFG_PRT_MODE_PARITY(val)                    (((val) & BIT_MASK(3)) << 9)
#define UBX_CFG_PRT_MODE_STOP_BITS(val)                 (((val) & BIT_MASK(2)) << 12)

#define UBX_CFG_PRT_PROTO_MASK_UBX                      BIT(0)
#define UBX_CFG_PRT_PROTO_MASK_NMEA                     BIT(1)
#define UBX_CFG_PRT_PROTO_MASK_RTCM3                    BIT(5)

struct ubx_cfg_prt {
        uint8_t port_id; /* See ubx_cfg_port_id */
        uint8_t reserved1;
        uint16_t rx_ready_pin;
        uint32_t mode;
        uint32_t baudrate;
        uint16_t in_proto_mask;
        uint16_t out_proto_mask;
        uint16_t flags;
        uint16_t reserved2;
};

enum ubx_dyn_model {
        UBX_DYN_MODEL_PORTABLE = 0,
        UBX_DYN_MODEL_STATIONARY = 2,
        UBX_DYN_MODEL_PEDESTRIAN = 3,
        UBX_DYN_MODEL_AUTOMOTIVE = 4,
        UBX_DYN_MODEL_SEA = 5,
        UBX_DYN_MODEL_AIRBORNE_1G = 6,
        UBX_DYN_MODEL_AIRBORNE_2G = 7,
        UBX_DYN_MODEL_AIRBORNE_4G = 8,
        UBX_DYN_MODEL_WRIST = 9,
        UBX_DYN_MODEL_BIKE = 10,
};

enum ubx_fix_mode {
        UBX_FIX_MODE_2D_ONLY = 1,
        UBX_FIX_MODE_3D_ONLY = 2,
        UBX_FIX_MODE_AUTO = 3,
};

enum ubx_utc_standard {
        UBX_UTC_STANDARD_AUTOMATIC = 0,
        UBX_UTC_STANDARD_GPS = 3,
        UBX_UTC_STANDARD_GALILEO = 5,
        UBX_UTC_STANDARD_GLONASS = 6,
        UBX_UTC_STANDARD_BEIDOU = 7,
};

#define UBX_CFG_NAV5_APPLY_DYN                  BIT(0)
#define UBX_CFG_NAV5_APPLY_FIX_MODE             BIT(2)

struct ubx_cfg_nav5 {
        uint16_t apply;
        uint8_t dyn_model; /* Dynamic platform model. See ubx_dyn_model */
        uint8_t fix_mode; /* Position fixing mode. See ubx_fix_mode */
        int32_t fixed_alt; /* Fixed altitude for 2D fix mode. Meters */
        uint32_t fixed_alt_var; /* Variance for Fixed altitude in 2D mode. Sq. meters */
        int8_t min_elev; /* Minimum Elevation to use a GNSS satellite in Navigation. Degrees */
        uint8_t dr_limit; /* Reserved */
        uint16_t p_dop; /* Position DOP mask */
        uint16_t t_dop; /* Time DOP mask */
        uint16_t p_acc; /* Position accuracy mask. Meters */
        uint16_t t_acc; /* Time accuracy mask. Meters */
        uint8_t static_hold_thresh; /* Static hold threshold. cm/s */
        uint8_t dgnss_timeout; /* DGNSS timeout. Seconds */
        uint8_t cno_thresh_num_svs; /* Number of satellites required above cno_thresh */
        uint8_t cno_thresh; /* C/N0 threshold for GNSS signals. dbHz */
        uint8_t reserved1[2];
        uint16_t static_hold_max_dist; /* Static hold distance threshold. Meters */
        uint8_t utc_standard; /* UTC standard to be used. See ubx_utc_standard */
        uint8_t reserved2[5];
} __packed;

enum ubx_cfg_rst_start_mode {
        UBX_CFG_RST_HOT_START = 0x0000,
        UBX_CFG_RST_WARM_START = 0x0001,
        UBX_CFG_RST_COLD_START = 0xFFFF,
};

enum ubx_cfg_rst_mode {
        UBX_CFG_RST_MODE_HW = 0x00,
        UBX_CFG_RST_MODE_SW = 0x01,
        UBX_CFG_RST_MODE_GNSS_STOP = 0x08,
        UBX_CFG_RST_MODE_GNSS_START = 0x09,
};

struct ubx_cfg_rst {
        uint16_t nav_bbr_mask;
        uint8_t reset_mode;
        uint8_t reserved;
};

enum ubx_cfg_rate_time_ref {
        UBX_CFG_RATE_TIME_REF_UTC = 0,
        UBX_CFG_RATE_TIME_REF_GPS = 1,
        UBX_CFG_RATE_TIME_REF_GLONASS = 2,
        UBX_CFG_RATE_TIME_REF_BEIDOU = 3,
        UBX_CFG_RATE_TIME_REF_GALILEO = 4,
        UBX_CFG_RATE_TIME_REF_NAVIC = 5,
};

struct ubx_cfg_rate {
        uint16_t meas_rate_ms;
        uint16_t nav_rate;
        uint16_t time_ref;
};

enum ubx_cfg_val_ver {
        UBX_CFG_VAL_VER_SIMPLE = 0,
        UBX_CFG_VAL_VER_TRANSACTION = 1,
};

struct ubx_cfg_val_hdr {
        uint8_t ver; /* See ubx_cfg_val_ver */
        uint8_t layer;
        uint16_t position;
} __packed;

struct ubx_cfg_val_u8 {
        struct ubx_cfg_val_hdr hdr;
        uint32_t key;
        uint8_t value;
} __packed;

struct ubx_cfg_val_u16 {
        struct ubx_cfg_val_hdr hdr;
        uint32_t key;
        uint16_t value;
} __packed;

struct ubx_cfg_val_u32 {
        struct ubx_cfg_val_hdr hdr;
        uint32_t key;
        uint32_t value;
} __packed;

enum ubx_msg_id_nmea_std {
        UBX_MSG_ID_NMEA_STD_DTM = 0x0A,
        UBX_MSG_ID_NMEA_STD_GBQ = 0x44,
        UBX_MSG_ID_NMEA_STD_GBS = 0x09,
        UBX_MSG_ID_NMEA_STD_GGA = 0x00,
        UBX_MSG_ID_NMEA_STD_GLL = 0x01,
        UBX_MSG_ID_NMEA_STD_GLQ = 0x43,
        UBX_MSG_ID_NMEA_STD_GNQ = 0x42,
        UBX_MSG_ID_NMEA_STD_GNS = 0x0D,
        UBX_MSG_ID_NMEA_STD_GPQ = 0x40,
        UBX_MSG_ID_NMEA_STD_GRS = 0x06,
        UBX_MSG_ID_NMEA_STD_GSA = 0x02,
        UBX_MSG_ID_NMEA_STD_GST = 0x07,
        UBX_MSG_ID_NMEA_STD_GSV = 0x03,
        UBX_MSG_ID_NMEA_STD_RMC = 0x04,
        UBX_MSG_ID_NMEA_STD_THS = 0x0E,
        UBX_MSG_ID_NMEA_STD_TXT = 0x41,
        UBX_MSG_ID_NMEA_STD_VLW = 0x0F,
        UBX_MSG_ID_NMEA_STD_VTG = 0x05,
        UBX_MSG_ID_NMEA_STD_ZDA = 0x08,
};

enum ubx_msg_id_nmea_pubx {
        UBX_MSG_ID_NMEA_PUBX_CONFIG = 0x41,
        UBX_MSG_ID_NMEA_PUBX_POSITION = 0x00,
        UBX_MSG_ID_NMEA_PUBX_RATE = 0x40,
        UBX_MSG_ID_NMEA_PUBX_SVSTATUS = 0x03,
        UBX_MSG_ID_NMEA_PUBX_TIME = 0x04,
};

struct ubx_cfg_msg_rate {
        uint8_t class;
        uint8_t id;
        uint8_t rate;
};

struct ubx_mon_ver {
        char sw_ver[30];
        char hw_ver[10];
};

static inline uint16_t ubx_calc_checksum(const struct ubx_frame *frame, size_t len)
{
        uint8_t ck_a = 0;
        uint8_t ck_b = 0;
        const uint8_t *data = (const uint8_t *)frame;

        if (len != UBX_FRAME_SZ(frame->payload_size)) {
                return 0xFFFF;
        }

        for (int i = UBX_FRAME_MSG_CLASS_IDX ; i < (UBX_FRAME_SZ(frame->payload_size) - 2) ; i++) {
                ck_a = ck_a + data[i];
                ck_b = ck_b + ck_a;
        }

        return ((ck_a & 0xFF) | ((ck_b & 0xFF) << 8));
}

static inline int ubx_frame_encode(uint8_t class, uint8_t id,
                                    const uint8_t *payload, size_t payload_len,
                                    uint8_t *buf, size_t buf_len)
{
        if (buf_len < UBX_FRAME_SZ(payload_len)) {
                return -EINVAL;
        }

        struct ubx_frame *frame = (struct ubx_frame *)buf;

        frame->preamble_sync_char_1 = UBX_PREAMBLE_SYNC_CHAR_1;
        frame->preamble_sync_char_2 = UBX_PREAMBLE_SYNC_CHAR_2;
        frame->class = class;
        frame->id = id;
        frame->payload_size = payload_len;
        memcpy(frame->payload_and_checksum, payload, payload_len);

        uint16_t checksum = ubx_calc_checksum(frame, UBX_FRAME_SZ(payload_len));

        frame->payload_and_checksum[payload_len] = checksum & 0xFF;
        frame->payload_and_checksum[payload_len + 1] = (checksum >> 8) & 0xFF;

        return UBX_FRAME_SZ(payload_len);
}

#define UBX_FRAME_DEFINE(_name, _frame)                                                            \
        const static struct ubx_frame _name = _frame

#define UBX_FRAME_ARRAY_DEFINE(_name, ...)                                                         \
        const struct ubx_frame *_name[] = {__VA_ARGS__};

#define UBX_FRAME_ACK_INITIALIZER(_class_id, _msg_id)                                              \
        UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_ACK, UBX_MSG_ID_ACK, _class_id, _msg_id)

#define UBX_FRAME_NAK_INITIALIZER(_class_id, _msg_id)                                              \
        UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_ACK, UBX_MSG_ID_NAK, _class_id, _msg_id)

#define UBX_FRAME_CFG_RST_INITIALIZER(_start_mode, _reset_mode)                                    \
        UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_RST,                        \
                                      (_start_mode & 0xFF), ((_start_mode >> 8) & 0xFF),           \
                                       _reset_mode, 0)

#define UBX_FRAME_CFG_RATE_INITIALIZER(_meas_rate_ms, _nav_rate, _time_ref)                        \
        UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_RATE,                       \
                                      (_meas_rate_ms & 0xFF), ((_meas_rate_ms >> 8) & 0xFF),       \
                                      (_nav_rate & 0xFF), ((_nav_rate >> 8) & 0xFF),               \
                                      (_time_ref & 0xFF), ((_time_ref >> 8) & 0xFF))

#define UBX_FRAME_CFG_MSG_RATE_INITIALIZER(_class_id, _msg_id, _rate)                              \
        UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_MSG,                        \
                                      _class_id, _msg_id, _rate)

#define UBX_FRAME_CFG_VAL_SET_U8_INITIALIZER(_key, _value)                                         \
        UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_VAL_SET,                    \
                                      0x00, 0x01, 0x00, 0x00,                                      \
                                      ((_key) & 0xFF), (((_key) >> 8) & 0xFF),                     \
                                      (((_key) >> 16) & 0xFF), (((_key) >> 24) & 0xFF),            \
                                      ((_value) & 0xFF))

#define UBX_FRAME_CFG_VAL_SET_U16_INITIALIZER(_key, _value)                                        \
        UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_VAL_SET,                    \
                                      0x00, 0x01, 0x00, 0x00,                                      \
                                      ((_key) & 0xFF), (((_key) >> 8) & 0xFF),                     \
                                      (((_key) >> 16) & 0xFF), (((_key) >> 24) & 0xFF),            \
                                      ((_value) & 0xFF), (((_value) >> 8) & 0xFF))

#define UBX_FRAME_CFG_VAL_SET_U32_INITIALIZER(_key, _value)                                        \
        UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_VAL_SET,                    \
                                      0x00, 0x01, 0x00, 0x00,                                      \
                                      ((_key) & 0xFF), (((_key) >> 8) & 0xFF),                     \
                                      (((_key) >> 16) & 0xFF), (((_key) >> 24) & 0xFF),            \
                                      ((_value) & 0xFF), (((_value) >> 8) & 0xFF),                 \
                                      (((_value) >> 16) & 0xFF), (((_value) >> 24) & 0xFF))

#define UBX_FRAME_CFG_VAL_GET_INITIALIZER(_key)                                                    \
        UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_VAL_GET,                    \
                                      0x00, 0x00, 0x00, 0x00,                                      \
                                      ((_key) & 0xFF), (((_key) >> 8) & 0xFF),                     \
                                      (((_key) >> 16) & 0xFF), (((_key) >> 24) & 0xFF))

#define UBX_FRAME_INITIALIZER_PAYLOAD(_class_id, _msg_id, ...)                                     \
        _UBX_FRAME_INITIALIZER_PAYLOAD(_class_id, _msg_id, __VA_ARGS__)

#define _UBX_FRAME_INITIALIZER_PAYLOAD(_class_id, _msg_id, ...)                                    \
        {                                                                                          \
                .preamble_sync_char_1 = UBX_PREAMBLE_SYNC_CHAR_1,                                  \
                .preamble_sync_char_2 = UBX_PREAMBLE_SYNC_CHAR_2,                                  \
                .class = _class_id,                                                                \
                .id = _msg_id,                                                                     \
                .payload_size = (NUM_VA_ARGS(__VA_ARGS__)) & 0xFFFF,                               \
                .payload_and_checksum = {                                                          \
                        __VA_ARGS__,                                                               \
                        UBX_CSUM(_class_id, _msg_id,                                               \
                                 ((NUM_VA_ARGS(__VA_ARGS__)) & 0xFF),                              \
                                 (((NUM_VA_ARGS(__VA_ARGS__)) >> 8) & 0xFF),                       \
                                 __VA_ARGS__),                                                     \
                },                                                                                 \
        }

#define UBX_FRAME_GET_INITIALIZER(_class_id, _msg_id)                                              \
        {                                                                                          \
                .preamble_sync_char_1 = UBX_PREAMBLE_SYNC_CHAR_1,                                  \
                .preamble_sync_char_2 = UBX_PREAMBLE_SYNC_CHAR_2,                                  \
                .class = _class_id,                                                                \
                .id = _msg_id,                                                                     \
                .payload_size = 0,                                                                 \
                .payload_and_checksum = {                                                          \
                        UBX_CSUM(_class_id, _msg_id, 0, 0),                                        \
                },                                                                                 \
        }

#endif /* ZEPHYR_INCLUDE_MODEM_UBX_PROTOCOL_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Croxel Inc.。

版权（Copyright）：© 2025 CogniPilot Foundation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 48 行

导航结果消息（Navigation Results Messages）。

### 注释 3：原第 49 行

接收机管理消息（Receiver Manager Messages）。

### 注释 4：原第 50 行

信息消息（Information Messages）。

### 注释 5：原第 51 行

确认／否认消息（Ack/Nak Messages）。

### 注释 6：原第 52 行

配置输入消息（Configuration Input Messages）。

### 注释 7：原第 53 行

固件更新消息（Firmware Update Messages）。

### 注释 8：原第 54 行

监测消息（Monitoring Messages）。

### 注释 9：原第 55 行

定时消息（Timing Messages）。

### 注释 10：原第 56 行

多星座全球导航卫星系统（GNSS）辅助消息。

### 注释 11：原第 57 行

日志记录消息（Logging Messages）。

### 注释 12：原第 58 行

安全功能消息（Security Feature Messages）。

### 注释 13：原第 59 行

注意：仅用于配置消息频率（Message Rate）。

### 注释 14：原第 60 行

注意：仅用于配置消息频率（Message Rate）。

### 注释 15：原第 111 行

经度（Longitude），单位为度，缩放系数为 `1e-7`。

### 注释 16：原第 112 行

纬度（Latitude），单位为度，缩放系数为 `1e-7`。

### 注释 17：原第 113 行

椭球面高（Height above Ellipsoid），单位为毫米。

### 注释 18：原第 114 行

平均海平面高（Height above Mean Sea Level），单位为毫米。

### 注释 19：原第 115 行

水平精度估计（Horizontal Accuracy Estimate），单位为毫米。

### 注释 20：原第 116 行

垂直精度估计（Vertical Accuracy Estimate），单位为毫米。

### 注释 21：原第 117 行

北－东－地坐标系（NED）的向北速度，单位为毫米／秒。

### 注释 22：原第 118 行

北－东－地坐标系（NED）的向东速度，单位为毫米／秒。

### 注释 23：原第 119 行

北－东－地坐标系（NED）的向下速度，单位为毫米／秒。

### 注释 24：原第 120 行

二维地面速度（Ground Speed, 2D），单位为毫米／秒。

### 注释 25：原第 121 行

二维运动航向（Heading of Motion, 2D），单位为度，缩放系数为 `1e-5`。

### 注释 26：原第 122 行

速度精度估计（Speed Accuracy Estimate），单位为毫米／秒。

### 注释 27：原第 126 行

缩放系数（Scaling）为 `1e-2`。

### 注释 28：原第 129 行

二维车辆航向（Heading of Vehicle, 2D），单位为度。仅在 `flags.head_vehicle_valid` 置位时有效。

### 注释 29：原第 132 行

磁偏角（Magnetic Declination），单位为度。

### 注释 30：原第 133 行

磁偏角精度（Magnetic Declination Accuracy），单位为度，缩放系数为 `1e-2`。

### 注释 31：原第 157 行

消息版本（Message Version）。

### 注释 32：原第 161 行

参见 `ubx_gnss_id`。

### 注释 33：原第 163 行

载噪比（Carrier-to-noise Ratio），单位为 dBHz。

### 注释 34：原第 164 行

仰角（Elevation），范围为 ±90，单位为度。

### 注释 35：原第 165 行

方位角（Azimuth），范围为 0–360，单位为度。

### 注释 36：原第 166 行

伪距残差（Pseudorange Residual），单位为米。

### 注释 37：原第 220 行

不支持。

### 注释 38：原第 221 行

不支持。

### 注释 39：原第 222 行

仅在启用奇偶校验（Parity）时支持。

### 注释 40：原第 248 行

参见 `ubx_cfg_port_id`。

### 注释 41：原第 291 行

动态平台模型（Dynamic Platform Model），参见 `ubx_dyn_model`。

### 注释 42：原第 292 行

定位模式（Position Fixing Mode），参见 `ubx_fix_mode`。

### 注释 43：原第 293 行

二维定位模式（2D Fix Mode）的固定高度（Fixed Altitude），单位为米。

### 注释 44：原第 294 行

二维模式下固定高度的方差（Variance），单位为平方米。

### 注释 45：原第 295 行

导航中使用 GNSS 卫星所需的最小仰角（Minimum Elevation），单位为度。

### 注释 46：原第 296 行

保留（Reserved）。

### 注释 47：原第 297 行

位置精度因子掩码（Position DOP Mask）。

### 注释 48：原第 298 行

时间精度因子掩码（Time DOP Mask）。

### 注释 49：原第 299 行

位置精度掩码（Position Accuracy Mask），单位为米。

### 注释 50：原第 300 行

时间精度掩码（Time Accuracy Mask），单位为米。

> 译注：原文此处单位为 `Meters`，按原文保留；未将其改成时间单位。

### 注释 51：原第 301 行

静态保持阈值（Static Hold Threshold），单位为厘米／秒。

### 注释 52：原第 302 行

差分 GNSS（DGNSS）超时，单位为秒。

### 注释 53：原第 303 行

要求载噪比高于 `cno_thresh` 的卫星数量。

### 注释 54：原第 304 行

GNSS 信号的载噪密度比（C/N0）阈值，单位为 dBHz。

### 注释 55：原第 306 行

静态保持距离阈值（Static Hold Distance Threshold），单位为米。

### 注释 56：原第 307 行

要使用的协调世界时（UTC）标准，参见 `ubx_utc_standard`。

### 注释 57：原第 351 行

参见 `ubx_cfg_val_ver`。

### 注释 58：原第 545 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MODEM_UBX_PROTOCOL_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/modem/ubx/checksum.h](../checksum_reference/P002_UBX校验和头文件参考.md)
- [ubx_frame](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [preamble_sync_char_1](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md#acf80f38e8f26bb32848ae2978a1f87a1)
- [preamble_sync_char_2](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md#ac61fb72df7c1cd8a9bacb787071cb77d)
- [id](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md#a4e578da5900365d498708f7a61d48ba4)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [payload_size](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md#a77b5030a6b95aef58b1c17f0368dd7ce)
- [payload_and_checksum](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md#a70c465b5bd1e9837c253d78fb210f4ce)
- [ubx_frame_match](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md)
- [id](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md#ae65eaf921576c61ad758bfedc56d89c6)
- [buf](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md#af78f70c27f4334fd1dcaac72d9e4ece6)
- [len](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md#a36c5fd74bd6d506111b1ef2ac39cb68a)
- [payload](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md#abbc954596995ca2dfe65de3e310e02a0)
- [ubx_class_id](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18)
- [UBX_CLASS_ID_NAV](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a8f46002e33dddab6782bad93ab3fd8b1)
- [UBX_CLASS_ID_RXM](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a5e4eaf66a7356e73b4c6e4949160f321)
- [UBX_CLASS_ID_INF](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a898b493832d06586cf48f9a2545651d0)
- [UBX_CLASS_ID_ACK](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18aee43a865c5815ce058261f5f0550fa2b)
- [UBX_CLASS_ID_CFG](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c)
- [UBX_CLASS_ID_UPD](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18aba0a811e14f9e87bd47bfbeaad24e11b)
- [UBX_CLASS_ID_MON](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18ac9200dedb25cfa03b80f4336e86db5ed)
- [UBX_CLASS_ID_TIM](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a8c700fd2062d8dc51c5e4b28c98c6cf0)
- [UBX_CLASS_ID_MGA](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a418aca13d3bd1608869494d26559e52f)
- [UBX_CLASS_ID_LOG](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a1e35a224f4809d3a59d0f1570bf382bb)
- [UBX_CLASS_ID_SEC](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a760de1a9f06cc6d4832da868d01702c4)
- [UBX_CLASS_ID_NMEA_STD](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a7e7c3645f46ba3c2e8329ae3a9eeaa79)
- [UBX_CLASS_ID_NMEA_PUBX](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad0dac3b7e7cbf3649aa5b8813e40fc18a0d9d5044c9df2a6b61b7a46a4f24e895)
- [ubx_msg_id_nav](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a8a935ea7debb4ac73ea99c98d6ef4d3b)
- [UBX_MSG_ID_NAV_PVT](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a8a935ea7debb4ac73ea99c98d6ef4d3ba8f887b777e29fc05107ac406d4a87458)
- [UBX_MSG_ID_NAV_SAT](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a8a935ea7debb4ac73ea99c98d6ef4d3bae87d4355340186b8a049346e3076f9ae)
- [ubx_nav_fix_type](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a173b6c1016562da43b8131b8d8f04fef)
- [UBX_NAV_FIX_TYPE_NO_FIX](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a173b6c1016562da43b8131b8d8f04fefad351fdc11590580b88ba5b486113e498)
- [UBX_NAV_FIX_TYPE_DR](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a173b6c1016562da43b8131b8d8f04fefae28182c06da19d2b498f92d09d74b33e)
- [UBX_NAV_FIX_TYPE_2D](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a173b6c1016562da43b8131b8d8f04fefae47dad429327e6a0cc89e339729b2651)
- [UBX_NAV_FIX_TYPE_3D](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a173b6c1016562da43b8131b8d8f04fefa1f8c2845d6e8e41f62cc28b7f1681f43)
- [UBX_NAV_FIX_TYPE_GNSS_DR_COMBINED](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a173b6c1016562da43b8131b8d8f04fefa648f596240841758588749574998bd71)
- [UBX_NAV_FIX_TYPE_TIME_ONLY](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a173b6c1016562da43b8131b8d8f04fefa2c20469f6893f651ad14b8ed6a7c3845)
- [ubx_nav_hp_dgnss_mode](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a3384ec6c907acb911c4a9c32bcd473ca)
- [UBX_NAV_HP_DGNSS_MODE_RTK_FLOAT](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a3384ec6c907acb911c4a9c32bcd473caaec46850a66dfd2d6bfcb18849a737fdc)
- [UBX_NAV_HP_DGNSS_MODE_RTK_FIXED](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a3384ec6c907acb911c4a9c32bcd473caa521219142a95c322e501497ab6262798)
- [ubx_nav_pvt](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [itow](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a426086b12ff09fb8a00dd4623fea307e)
- [year](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a84c6640806485f270b8d51d06cc49709)
- [month](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#ad90042dc5e00b91f004badcb0c3a5f4c)
- [day](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#aeadb05fe45a3a0539c899129e40059fd)
- [hour](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#aeb710663626935d21c77a5cfe1030795)
- [minute](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a18b61263b433dc5f81c2becff9c6743c)
- [second](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a10b14934d80d80d3c2f0c36866bd4a64)
- [valid](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a450638fda7b9d1929145575e4c576ec1)
- [tacc](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a1753595f0a3935449dee4d0c57e88a6e)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [nano](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a1c21c3b882412f36f96c59cda1d948d9)
- [time](../api_file_reference/P187_____w__zephyr__zephyr__lib__libc__minimal__include__time.h_文件参考.md#a99ef1cb2c789827dd5db3886dccf9067)
- [fix_type](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a3b780d7b790b07a8ee23431969cbc318)
- [flags](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a1bdc3cb0e4a2b6bef1c4216963e5c29c)
- [flags2](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a2ff7d8bcc13ee956d9535c61efefada6)
- [num_sv](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#aea613eb3d604d33120e82c569c5f10e9)
- [longitude](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#ae47fc34dfd91687590bd96afe2fab091)
- [latitude](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a34ec5fc41c4b323b4719803f1ff01bed)
- [height](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#ab0df156e9f8009bebfbbdb39c63c4191)
- [hmsl](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#ae6ba97f3406b9fdbbf04c4bb3e744668)
- [horiz_acc](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#acbb58f36eb572ce27b050a8c7540f91d)
- [vert_acc](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#af5b3e0e70b3470bd1686ddbfefb419f9)
- [vel_north](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a1d50e696fa2684b55d04c652c85f2e16)
- [vel_east](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a17c628b0acca293f068b58eff32ae4dd)
- [vel_down](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a4958a6c11bd812477d11467ab3384161)
- [ground_speed](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a38a8612a53966a1d598bf6d17443da7d)
- [head_motion](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#abd97f003ba43b70ffea2e9fdf5702c4f)
- [speed_acc](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a955d0f7927f68f540f2e9a2c91e46e79)
- [head_acc](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#aa332fc93448eb6b30ad8bbaa5760db5c)
- [pdop](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a7e5dc3449e52a36cb2bc5841bbf6fec8)
- [flags3](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a39b72f654fc8130c611ac839189914ed)
- [reserved](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a80139f6d95bf943f5c6de6af1ea50e3e)
- [head_vehicle](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a8fc4b24fb8ffde02d306bc1b6770b1d8)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [mag_decl](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a4f63a0f15b823e5258fdb826d2636828)
- [magacc](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#ac0265c113f01ae2bab8553eb7148e3ae)
- [nav](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#aa8b31a49c2844501505412da226872e1)
- [ubx_nav_sat_health](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#afbba8ada09d6c6489d52a3b9dc31725f)
- [UBX_NAV_SAT_HEALTH_UNKNOWN](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#afbba8ada09d6c6489d52a3b9dc31725fa3661b89022659975720d3a022b21f194)
- [UBX_NAV_SAT_HEALTH_HEALTHY](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#afbba8ada09d6c6489d52a3b9dc31725fa7dcaa32f001d1a7b5b071cdf7621081e)
- [UBX_NAV_SAT_HEALTH_UNHEALTHY](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#afbba8ada09d6c6489d52a3b9dc31725fa95ea7c01a987a1e334f41c79642b8139)
- [ubx_gnss_id](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a6711a33292bf25327950406b96585690)
- [UBX_GNSS_ID_GPS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a6711a33292bf25327950406b96585690adca8434b24978430d03939b81d76fbb9)
- [UBX_GNSS_ID_SBAS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a6711a33292bf25327950406b96585690a31a403a2013dc9da3da56366fa95f19b)
- [UBX_GNSS_ID_GALILEO](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a6711a33292bf25327950406b96585690a931ed807a91dd1f0e6e2cfa013860cbe)
- [UBX_GNSS_ID_BEIDOU](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a6711a33292bf25327950406b96585690ac3f1631647cfd0246be61fc78549a9f7)
- [UBX_GNSS_ID_QZSS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a6711a33292bf25327950406b96585690a2dad67829bb51786024771c0d5a6d103)
- [UBX_GNSS_ID_GLONASS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a6711a33292bf25327950406b96585690a4e14cf64a03e9d37af198870b0616497)
- [ubx_nav_sat](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md)
- [itow](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md#aac587fd77fa832021ebca87e7897eb2e)
- [version](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md#a7204f8b1b28f3dc0970fa62567885cdc)
- [num_sv](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md#ae0bea798d815cc25e837e3fa394fb429)
- [reserved1](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md#a6f5bf3da0f5633aa95ff4d736656cb21)
- [ubx_nav_sat_info](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md)
- [gnss_id](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#a04fc29e6cf9f1ff6f1f638ae633d5a11)
- [sv_id](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#ab7ba4e9d36ab136c0bb8fde9b4f9b3e5)
- [cno](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#a83e6ba9e50cc24fc0d80de3947daf571)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [elevation](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#a9133131e06119371d14be09f99b24a8e)
- [azimuth](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#a3a50255230b6ed80bfa4eb8ff83acf89)
- [pseu_res](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#a442709d1e9b43ae8c27606a5fb878c89)
- [flags](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#ac6872360564b383ce2cd5a061717c8fe)
- [sat](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md#ade983d7b35cf81a6d769979f7cb5919d)
- [ubx_msg_id_ack](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a260c4adbe9524bd747127a4e3f14bbca)
- [UBX_MSG_ID_ACK](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a260c4adbe9524bd747127a4e3f14bbcaa88bba7f61485369188998bc1c18b2511)
- [UBX_MSG_ID_NAK](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a260c4adbe9524bd747127a4e3f14bbcaacd2316ff6386c7eb2da90de1f4466469)
- [ubx_msg_id_cfg](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a3cf04300758f1802e0703428707035d7)
- [UBX_MSG_ID_CFG_PRT](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a3cf04300758f1802e0703428707035d7a871b880c791ad49c55164856ac4f83f9)
- [UBX_MSG_ID_CFG_MSG](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a3cf04300758f1802e0703428707035d7ace6e98ad1c1ac7232327d42b0f4302ef)
- [UBX_MSG_ID_CFG_RST](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a3cf04300758f1802e0703428707035d7ad2c8bf68306ca6bb22e88c5c6d957453)
- [UBX_MSG_ID_CFG_RATE](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a3cf04300758f1802e0703428707035d7a89a96eb89044b208d3a6c29fc273fa26)
- [UBX_MSG_ID_CFG_NAV5](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a3cf04300758f1802e0703428707035d7a036303b6caf601b73bfb48b3a7423309)
- [UBX_MSG_ID_CFG_VAL_SET](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3)
- [UBX_MSG_ID_CFG_VAL_GET](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a3cf04300758f1802e0703428707035d7aa31397b2154b0f1f9b1e906c91a6bc8c)
- [ubx_msg_id_mon](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a0d969e434f941cf5af7143cca0cf0fe4)
- [UBX_MSG_ID_MON_VER](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a0d969e434f941cf5af7143cca0cf0fe4a43aa77232e6c2aed82ecf2033c0a06b0)
- [UBX_MSG_ID_MON_GNSS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a0d969e434f941cf5af7143cca0cf0fe4a66c14a28074edc8631bd6b47f5c45888)
- [ubx_ack](../sensor_navigation_model_reference/P056_ubx_ack_结构体.md)
- [id](../sensor_navigation_model_reference/P056_ubx_ack_结构体.md#ab68abe2083b8446a2e3ffc4b603ac47d)
- [ubx_mon_gnss](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md)
- [ver](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#aebcccc44a80ef3b327d7d479ccb5ebe5)
- [supported](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#a8f76d361c23ae4a94d29277be0aa36f8)
- [default_enabled](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#a2b94264d40d0aa740b20d9fa9565d155)
- [enabled](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#ad09bcd6e739e385c275f8a1cae8725b3)
- [selection](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#ae004377f656dede9b0ebe98caeea588f)
- [simultaneous](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#a34b9073dda3d6ad734109cea8ba5a0d2)
- [reserved1](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#a045256bfbf8fe9b398ef77d10e00395a)
- [ubx_cfg_port_id](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#adb6a6e16f193bc70840b2dd12dbc9baa)
- [UBX_CFG_PORT_ID_DDC](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#adb6a6e16f193bc70840b2dd12dbc9baaa5c7c1a24670995305bcb8e98cfd1fa19)
- [UBX_CFG_PORT_ID_UART](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#adb6a6e16f193bc70840b2dd12dbc9baaaccb591a437d0ed7cca8888f41b855efb)
- [UBX_CFG_PORT_ID_USB](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#adb6a6e16f193bc70840b2dd12dbc9baaa3af5f6c24fade976d4ece339e9240114)
- [UBX_CFG_PORT_ID_SPI](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#adb6a6e16f193bc70840b2dd12dbc9baaaa0ee1de6e26bb0585f24fddbe3d7ec9a)
- [ubx_cfg_char_len](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a887b1fa6af0d6d08cc51ed65de64a78a)
- [UBX_CFG_PRT_PORT_MODE_CHAR_LEN_5](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a887b1fa6af0d6d08cc51ed65de64a78aa019364b4a4482098acc0d7821b456b83)
- [UBX_CFG_PRT_PORT_MODE_CHAR_LEN_6](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a887b1fa6af0d6d08cc51ed65de64a78aaeea043882f976e34008f261e1b2ee5ac)
- [UBX_CFG_PRT_PORT_MODE_CHAR_LEN_7](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a887b1fa6af0d6d08cc51ed65de64a78aaeacece1ca309918fa3abe7a02911f5ca)
- [UBX_CFG_PRT_PORT_MODE_CHAR_LEN_8](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a887b1fa6af0d6d08cc51ed65de64a78aae7769c1dd298aabbad37ddaf6260eb4d)
- [ubx_cfg_parity](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a2e5de1479afbcf20caa3300282bb0d1a)
- [UBX_CFG_PRT_PORT_MODE_PARITY_EVEN](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a2e5de1479afbcf20caa3300282bb0d1aa1ef24c67f4e90f7c6fb011ec433ebb68)
- [UBX_CFG_PRT_PORT_MODE_PARITY_ODD](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a2e5de1479afbcf20caa3300282bb0d1aa5db544370f64f19224e9243eae0942ac)
- [UBX_CFG_PRT_PORT_MODE_PARITY_NONE](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a2e5de1479afbcf20caa3300282bb0d1aa46b4ba80de7ca4c9d1ea403dd6efb385)
- [ubx_cfg_stop_bits](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a94709ee4f4afe0194790893251ee2b4c)
- [UBX_CFG_PRT_PORT_MODE_STOP_BITS_1](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a94709ee4f4afe0194790893251ee2b4caf762dc50babaacd4cbb1ce753a8c0ae9)
- [UBX_CFG_PRT_PORT_MODE_STOP_BITS_1_5](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a94709ee4f4afe0194790893251ee2b4ca06c8d5338db83ce4a74a92228f04ffb1)
- [UBX_CFG_PRT_PORT_MODE_STOP_BITS_2](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a94709ee4f4afe0194790893251ee2b4caea0ef9695c70807a5bdfb1725f31ea3f)
- [UBX_CFG_PRT_PORT_MODE_STOP_BITS_0_5](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a94709ee4f4afe0194790893251ee2b4ca461834aa0d5d6ddec370ecd247e330e6)
- [ubx_cfg_prt](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md)
- [port_id](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#af5a445ab598a2b93e884c916fe13affc)
- [reserved1](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#aba6bef46b7818a2396b77a0b1245ecc5)
- [rx_ready_pin](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#a1d4df224a3a9e7e6031a418745ee4e95)
- [mode](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#a571753eb8aba5610fb7bc3546b7bfce9)
- [baudrate](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#ac83072a87e0b29b30e6406f4f61cf26d)
- [in_proto_mask](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#a960fd4543476b89b56f23dd29774b196)
- [out_proto_mask](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#a1f4f3ab473e80648043b792bc4d5022f)
- [flags](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#a836be3302c1e038fbc09712242a51e69)
- [reserved2](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#ad2bf468b82cc86ae1ce99c2fa129c231)
- [ubx_dyn_model](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a9e5e9af7a281e53f2b950089ee66561f)
- [UBX_DYN_MODEL_PORTABLE](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a9e5e9af7a281e53f2b950089ee66561fa59c3bbc8cb2a44e26920adbe0251375b)
- [UBX_DYN_MODEL_STATIONARY](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a9e5e9af7a281e53f2b950089ee66561fa4f147b313644dba74c95930038201cf7)
- [UBX_DYN_MODEL_PEDESTRIAN](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a9e5e9af7a281e53f2b950089ee66561fa8a2a4bb1bb5b7f69960fdcde374f2ee6)
- [UBX_DYN_MODEL_AUTOMOTIVE](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a9e5e9af7a281e53f2b950089ee66561fa736709e926d95754fef9260c596530e2)
- [UBX_DYN_MODEL_SEA](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a9e5e9af7a281e53f2b950089ee66561fa6d89a732b306e21feeaee51cdbcc0bed)
- [UBX_DYN_MODEL_AIRBORNE_1G](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a9e5e9af7a281e53f2b950089ee66561fa9bb36ad38aca4f118fe1bdc2f0351476)
- [UBX_DYN_MODEL_AIRBORNE_2G](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a9e5e9af7a281e53f2b950089ee66561fa1a39257d816910b26f2323b61a278519)
- [UBX_DYN_MODEL_AIRBORNE_4G](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a9e5e9af7a281e53f2b950089ee66561fae4640365810ae80e8c24507fd7279f3d)
- [UBX_DYN_MODEL_WRIST](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a9e5e9af7a281e53f2b950089ee66561fa172bc7d2ed80cadb4077ae42233764b2)
- [UBX_DYN_MODEL_BIKE](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a9e5e9af7a281e53f2b950089ee66561faa062bfc1af7cc119d025dee309ac1d25)
- [ubx_fix_mode](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a342c0d62cf874ccb8b657ce85d91efe0)
- [UBX_FIX_MODE_2D_ONLY](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a342c0d62cf874ccb8b657ce85d91efe0a29354369703a5e54ae7e49edfff886ff)
- [UBX_FIX_MODE_3D_ONLY](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a342c0d62cf874ccb8b657ce85d91efe0aa60a16ce7e100e06e0bab9a3922003a6)
- [UBX_FIX_MODE_AUTO](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a342c0d62cf874ccb8b657ce85d91efe0a1e324c97e68e6d7ce35feb4ffe2ca617)
- [ubx_utc_standard](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a359b0f88d3769af43c2b1699eb172f23)
- [UBX_UTC_STANDARD_AUTOMATIC](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a359b0f88d3769af43c2b1699eb172f23a8bc6c6397d5bc342ebe0ea36522e96a5)
- [UBX_UTC_STANDARD_GPS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a359b0f88d3769af43c2b1699eb172f23a34b4b516760245d0a5bbfcbb5937d74c)
- [UBX_UTC_STANDARD_GALILEO](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a359b0f88d3769af43c2b1699eb172f23a6fe85d7688c6730a492981fdc4623c67)
- [UBX_UTC_STANDARD_GLONASS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a359b0f88d3769af43c2b1699eb172f23ab6c294e0f55696a8c90ec8211673ca80)
- [UBX_UTC_STANDARD_BEIDOU](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a359b0f88d3769af43c2b1699eb172f23a8eeae948253c11b7f097dd06896e66f8)
- [ubx_cfg_nav5](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md)
- [apply](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a564548f9609493061e995219f6397060)
- [dyn_model](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a70f931b76bcd7a07a225648a15e73493)
- [fix_mode](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#aab1b8aec77c186c576be839f728bba70)
- [fixed_alt](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#af915a692066df1855c270e106c1981ca)
- [fixed_alt_var](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#abb48bda50e725eb8c2973518b468916f)
- [min_elev](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a2e7353d4ef2f0b3eef4ae3d1cc2be5ed)
- [dr_limit](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#ace7d12cf8f63904274e658a6afe149d5)
- [p_dop](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a7c7f4338463e4d0c8040971ec31dc92c)
- [t_dop](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a4d8537de40aa5c98ae2e2183da9d44c3)
- [p_acc](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a19d69c52edac0f65e2892b4c476d5a76)
- [t_acc](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#ad78a8828482ce26597f80f5e5a548afd)
- [static_hold_thresh](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a5afd803452c65c4f03b122c9ff59cf2b)
- [dgnss_timeout](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a2ee4fc58054c5f049890914c73089c99)
- [cno_thresh_num_svs](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a648e22442293b24b2aa8b264a78b9bd2)
- [cno_thresh](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#abf2a3de97f8d9cade6ec18408452938a)
- [reserved1](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#ab6b5cd2ef8db8c281f77c6684f6f8c0c)
- [static_hold_max_dist](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a6108faff3832cab3d734020c030c5c6c)
- [utc_standard](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#ae0ecd871977ad119009cf1a2ac617327)
- [reserved2](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#ac3d21a048e77c404bcfa180af2e41992)
- [ubx_cfg_rst_start_mode](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a43766ad4c0fd1d31fd547c090e3f39b6)
- [UBX_CFG_RST_HOT_START](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a43766ad4c0fd1d31fd547c090e3f39b6a67b9cba109cc8f57a38c41b1d521e3c7)
- [UBX_CFG_RST_WARM_START](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a43766ad4c0fd1d31fd547c090e3f39b6a1621ed3281429f96fc598d90cc388c95)
- [UBX_CFG_RST_COLD_START](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a43766ad4c0fd1d31fd547c090e3f39b6aaef8449ed29d6dd76bdd34157d873896)
- [ubx_cfg_rst_mode](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a5cc2a8f42fd62032afa3cd7687452896)
- [UBX_CFG_RST_MODE_HW](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a5cc2a8f42fd62032afa3cd7687452896ac02d28b95ef601af32dc898e35ad252e)
- [UBX_CFG_RST_MODE_SW](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a5cc2a8f42fd62032afa3cd7687452896a7fd6f4b7557dfa6511dcb6354963d342)
- [UBX_CFG_RST_MODE_GNSS_STOP](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a5cc2a8f42fd62032afa3cd7687452896a0e9177345e82ad614c1ab4c8b52b9265)
- [UBX_CFG_RST_MODE_GNSS_START](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a5cc2a8f42fd62032afa3cd7687452896aca25f86cc1d85c60b1d67509d0e9506b)
- [ubx_cfg_rst](../sensor_navigation_model_reference/P061_ubx_cfg_rst_结构体.md)
- [nav_bbr_mask](../sensor_navigation_model_reference/P061_ubx_cfg_rst_结构体.md#a7d7e94ffc6aa9518a31b3f829a732362)
- [reset_mode](../sensor_navigation_model_reference/P061_ubx_cfg_rst_结构体.md#a1a63d295cf71e23a4afdb31637741b4f)
- [reserved](../sensor_navigation_model_reference/P061_ubx_cfg_rst_结构体.md#aa1f7a46662f14e498b8bce84fb349d33)
- [ubx_cfg_rate_time_ref](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a621d2fae9721b6dc62a71801f3b7952e)
- [UBX_CFG_RATE_TIME_REF_UTC](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a621d2fae9721b6dc62a71801f3b7952eacc3989fab9e22270c389b0318bbe45ea)
- [UBX_CFG_RATE_TIME_REF_GPS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a621d2fae9721b6dc62a71801f3b7952ea7a2d00bdb7fef5ff7da1d3a682a1b82e)
- [UBX_CFG_RATE_TIME_REF_GLONASS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a621d2fae9721b6dc62a71801f3b7952ea519dc8f11c80b5a08771fbc36c70fbb8)
- [UBX_CFG_RATE_TIME_REF_BEIDOU](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a621d2fae9721b6dc62a71801f3b7952ea30f66599c483f622607f0b13ad0451f8)
- [UBX_CFG_RATE_TIME_REF_GALILEO](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a621d2fae9721b6dc62a71801f3b7952eab7ed326b5da1087afb8d531d97bb9f16)
- [UBX_CFG_RATE_TIME_REF_NAVIC](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a621d2fae9721b6dc62a71801f3b7952ea5be3c906a6c528f65575990041b7e6ce)
- [ubx_cfg_rate](../sensor_navigation_model_reference/P060_ubx_cfg_rate_结构体.md)
- [meas_rate_ms](../sensor_navigation_model_reference/P060_ubx_cfg_rate_结构体.md#ae64d779c4a3fe255710be8f742f5b6c6)
- [nav_rate](../sensor_navigation_model_reference/P060_ubx_cfg_rate_结构体.md#aafcbb36f844534c77e698dceccb2f5dc)
- [time_ref](../sensor_navigation_model_reference/P060_ubx_cfg_rate_结构体.md#a444822a3a37dd51313bfc6968a3b4721)
- [ubx_cfg_val_ver](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad7e0ffe55e8dbd97caa5bc089d33540c)
- [UBX_CFG_VAL_VER_SIMPLE](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad7e0ffe55e8dbd97caa5bc089d33540ca1fe2554bbbf05c86d3f9b0bc50927c1b)
- [UBX_CFG_VAL_VER_TRANSACTION](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad7e0ffe55e8dbd97caa5bc089d33540caca3b7f2a39ff93b91b8317245e8375ab)
- [ubx_cfg_val_hdr](../sensor_navigation_model_reference/P062_ubx_cfg_val_hdr_结构体.md)
- [ver](../sensor_navigation_model_reference/P062_ubx_cfg_val_hdr_结构体.md#a4d7a91e9521428e5b528ced88b030cd3)
- [layer](../sensor_navigation_model_reference/P062_ubx_cfg_val_hdr_结构体.md#aa835050e25c8db0a5a88954ff0def88c)
- [position](../sensor_navigation_model_reference/P062_ubx_cfg_val_hdr_结构体.md#a6206dc714df9656cc37e0b802ab541b8)
- [ubx_cfg_val_u8](../sensor_navigation_model_reference/P065_ubx_cfg_val_u8_结构体.md)
- [hdr](../sensor_navigation_model_reference/P065_ubx_cfg_val_u8_结构体.md#a793646932ce054ab8561078981f57250)
- [key](../sensor_navigation_model_reference/P065_ubx_cfg_val_u8_结构体.md#a2c1cbf9a552608150eafc1f2d92b03b5)
- [value](../sensor_navigation_model_reference/P065_ubx_cfg_val_u8_结构体.md#a325aaaf688433cab710d0c3e835fb9ed)
- [ubx_cfg_val_u16](../sensor_navigation_model_reference/P063_ubx_cfg_val_u16_结构体.md)
- [hdr](../sensor_navigation_model_reference/P063_ubx_cfg_val_u16_结构体.md#a32e877f1e2f60b209fbcdd057aa82c4f)
- [key](../sensor_navigation_model_reference/P063_ubx_cfg_val_u16_结构体.md#a87a9c181318e297935bb1eb65093d4a8)
- [value](../sensor_navigation_model_reference/P063_ubx_cfg_val_u16_结构体.md#a6226f1b8f4cb89cb318c07ff8ddcbbde)
- [ubx_cfg_val_u32](../sensor_navigation_model_reference/P064_ubx_cfg_val_u32_结构体.md)
- [hdr](../sensor_navigation_model_reference/P064_ubx_cfg_val_u32_结构体.md#adc51df7bc8a50e1ca8843067bb309ac9)
- [key](../sensor_navigation_model_reference/P064_ubx_cfg_val_u32_结构体.md#ab02aa8d3b7039c06692a805aed30f246)
- [value](../sensor_navigation_model_reference/P064_ubx_cfg_val_u32_结构体.md#a2c1d446c7c8bef80052d2438fb998d58)
- [ubx_msg_id_nmea_std](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6c)
- [UBX_MSG_ID_NMEA_STD_DTM](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6cac84f9ad61c85bbce60e680639c3d88ad)
- [UBX_MSG_ID_NMEA_STD_GBQ](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6ca5174a26b3b79356bf06402de46bc0774)
- [UBX_MSG_ID_NMEA_STD_GBS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6caef6c925e20f072665bf55e435d37a6ac)
- [UBX_MSG_ID_NMEA_STD_GGA](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6ca07aa8c55e3504c0d19b1e123f4d2e7c7)
- [UBX_MSG_ID_NMEA_STD_GLL](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6ca6435225efac8c7ef6e336a84fa2e8932)
- [UBX_MSG_ID_NMEA_STD_GLQ](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6ca263a724b491a6303d5486828a49a8961)
- [UBX_MSG_ID_NMEA_STD_GNQ](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6caa2c68fe9d01bc4acf3054d667f3e2a77)
- [UBX_MSG_ID_NMEA_STD_GNS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6cafea982067c784c47ae5b1ad7e91b4191)
- [UBX_MSG_ID_NMEA_STD_GPQ](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6ca39492ba0c78d0290819b9410e2e55781)
- [UBX_MSG_ID_NMEA_STD_GRS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6ca7f1d764aa078c284c575ec610d4f4853)
- [UBX_MSG_ID_NMEA_STD_GSA](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6cae3c6e42e75e69a34d7017d2f2aa3c70d)
- [UBX_MSG_ID_NMEA_STD_GST](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6ca99b8f62b1d204b335a06ed6f3ef214e6)
- [UBX_MSG_ID_NMEA_STD_GSV](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6ca2a5cc3b49abc9be0c6bbab0a9963ba03)
- [UBX_MSG_ID_NMEA_STD_RMC](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6ca8787502b2d9a14d2ce79b1ce1713d6f3)
- [UBX_MSG_ID_NMEA_STD_THS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6ca884ab2ce56a1f7a08d4b9d06b944ad37)
- [UBX_MSG_ID_NMEA_STD_TXT](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6cad58d4ac5b57cbdd42d360560cc16fc0e)
- [UBX_MSG_ID_NMEA_STD_VLW](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6ca58ad56a546a2df6c9359927375da9904)
- [UBX_MSG_ID_NMEA_STD_VTG](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6ca5c12f57e0b4de16d09fc42f23740908b)
- [UBX_MSG_ID_NMEA_STD_ZDA](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#aa221b68c53f25634d9f2f435f28c1a6cae6a2501b586793e75cdd0085170a9a27)
- [ubx_msg_id_nmea_pubx](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a58dc8b84784731500aa7f55afeb7e582)
- [UBX_MSG_ID_NMEA_PUBX_CONFIG](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a58dc8b84784731500aa7f55afeb7e582a43616a8ad2465c7521aa9ed28460cf57)
- [UBX_MSG_ID_NMEA_PUBX_POSITION](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a58dc8b84784731500aa7f55afeb7e582a61cbc043ccd0a96ba2327d7bd95189c6)
- [UBX_MSG_ID_NMEA_PUBX_RATE](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a58dc8b84784731500aa7f55afeb7e582af5ccdcc3eed53b0906b83667443e3667)
- [UBX_MSG_ID_NMEA_PUBX_SVSTATUS](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a58dc8b84784731500aa7f55afeb7e582a73aeb813a098d600dfb60561bc042e2a)
- [UBX_MSG_ID_NMEA_PUBX_TIME](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a58dc8b84784731500aa7f55afeb7e582a9f36e6c7688a62737beb203e82de91ef)
- [ubx_cfg_msg_rate](../sensor_navigation_model_reference/P057_ubx_cfg_msg_rate_结构体.md)
- [id](../sensor_navigation_model_reference/P057_ubx_cfg_msg_rate_结构体.md#aee7d34d68f3665c665f8ae4bc6d1a04a)
- [rate](../sensor_navigation_model_reference/P057_ubx_cfg_msg_rate_结构体.md#a7a030b3e70356b899ed7284e750041b0)
- [ubx_mon_ver](../sensor_navigation_model_reference/P069_ubx_mon_ver_结构体.md)
- [sw_ver](../sensor_navigation_model_reference/P069_ubx_mon_ver_结构体.md#aa0495c27ac850d56ddaa92bc4689ba7f)
- [hw_ver](../sensor_navigation_model_reference/P069_ubx_mon_ver_结构体.md#a07a2fdbe52fa48e9412f39bff1256318)
- [ubx_calc_checksum](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a450f46250ef486af4f933e69ddbb42d2)
- [UBX_FRAME_SZ](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a4c64b9118da471baa6a7a88ee345bf66)
- [UBX_FRAME_MSG_CLASS_IDX](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a2c667ef9bb2d12effb251f4df6827c73)
- [ubx_frame_encode](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#acdc0d9b7d25df6aba6bb091e7034f5ba)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [UBX_PREAMBLE_SYNC_CHAR_1](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#a1693f3584605a0197076cba71c79b0df)
- [UBX_PREAMBLE_SYNC_CHAR_2](../api_file_supplement_reference/P071_zephyr__modem__ubx__protocol.h_文件参考.md#ad8d6229db563db619d4f0a9f225fb640)
- [class](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md#a2dcc29a82e7dfff2d1e4194f1bc035e8)
- [memcpy](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md#af0f01bffcd16daa9143f6014d10a25ad)
- [checksum.h](../checksum_reference/P002_UBX校验和头文件参考.md)
- [ubx_ack::id](../sensor_navigation_model_reference/P056_ubx_ack_结构体.md#ab68abe2083b8446a2e3ffc4b603ac47d)
- [ubx_cfg_msg_rate::rate](../sensor_navigation_model_reference/P057_ubx_cfg_msg_rate_结构体.md#a7a030b3e70356b899ed7284e750041b0)
- [ubx_cfg_msg_rate::id](../sensor_navigation_model_reference/P057_ubx_cfg_msg_rate_结构体.md#aee7d34d68f3665c665f8ae4bc6d1a04a)
- [ubx_cfg_nav5::p_acc](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a19d69c52edac0f65e2892b4c476d5a76)
- [ubx_cfg_nav5::min_elev](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a2e7353d4ef2f0b3eef4ae3d1cc2be5ed)
- [ubx_cfg_nav5::dgnss_timeout](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a2ee4fc58054c5f049890914c73089c99)
- [ubx_cfg_nav5::t_dop](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a4d8537de40aa5c98ae2e2183da9d44c3)
- [ubx_cfg_nav5::apply](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a564548f9609493061e995219f6397060)
- [ubx_cfg_nav5::static_hold_thresh](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a5afd803452c65c4f03b122c9ff59cf2b)
- [ubx_cfg_nav5::static_hold_max_dist](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a6108faff3832cab3d734020c030c5c6c)
- [ubx_cfg_nav5::cno_thresh_num_svs](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a648e22442293b24b2aa8b264a78b9bd2)
- [ubx_cfg_nav5::dyn_model](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a70f931b76bcd7a07a225648a15e73493)
- [ubx_cfg_nav5::p_dop](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#a7c7f4338463e4d0c8040971ec31dc92c)
- [ubx_cfg_nav5::fix_mode](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#aab1b8aec77c186c576be839f728bba70)
- [ubx_cfg_nav5::reserved1](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#ab6b5cd2ef8db8c281f77c6684f6f8c0c)
- [ubx_cfg_nav5::fixed_alt_var](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#abb48bda50e725eb8c2973518b468916f)
- [ubx_cfg_nav5::cno_thresh](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#abf2a3de97f8d9cade6ec18408452938a)
- [ubx_cfg_nav5::reserved2](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#ac3d21a048e77c404bcfa180af2e41992)
- [ubx_cfg_nav5::dr_limit](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#ace7d12cf8f63904274e658a6afe149d5)
- [ubx_cfg_nav5::t_acc](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#ad78a8828482ce26597f80f5e5a548afd)
- [ubx_cfg_nav5::utc_standard](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#ae0ecd871977ad119009cf1a2ac617327)
- [ubx_cfg_nav5::fixed_alt](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md#af915a692066df1855c270e106c1981ca)
- [ubx_cfg_prt::rx_ready_pin](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#a1d4df224a3a9e7e6031a418745ee4e95)
- [ubx_cfg_prt::out_proto_mask](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#a1f4f3ab473e80648043b792bc4d5022f)
- [ubx_cfg_prt::mode](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#a571753eb8aba5610fb7bc3546b7bfce9)
- [ubx_cfg_prt::flags](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#a836be3302c1e038fbc09712242a51e69)
- [ubx_cfg_prt::in_proto_mask](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#a960fd4543476b89b56f23dd29774b196)
- [ubx_cfg_prt::reserved1](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#aba6bef46b7818a2396b77a0b1245ecc5)
- [ubx_cfg_prt::baudrate](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#ac83072a87e0b29b30e6406f4f61cf26d)
- [ubx_cfg_prt::reserved2](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#ad2bf468b82cc86ae1ce99c2fa129c231)
- [ubx_cfg_prt::port_id](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md#af5a445ab598a2b93e884c916fe13affc)
- [ubx_cfg_rate::time_ref](../sensor_navigation_model_reference/P060_ubx_cfg_rate_结构体.md#a444822a3a37dd51313bfc6968a3b4721)
- [ubx_cfg_rate::nav_rate](../sensor_navigation_model_reference/P060_ubx_cfg_rate_结构体.md#aafcbb36f844534c77e698dceccb2f5dc)
- [ubx_cfg_rate::meas_rate_ms](../sensor_navigation_model_reference/P060_ubx_cfg_rate_结构体.md#ae64d779c4a3fe255710be8f742f5b6c6)
- [ubx_cfg_rst::reset_mode](../sensor_navigation_model_reference/P061_ubx_cfg_rst_结构体.md#a1a63d295cf71e23a4afdb31637741b4f)
- [ubx_cfg_rst::nav_bbr_mask](../sensor_navigation_model_reference/P061_ubx_cfg_rst_结构体.md#a7d7e94ffc6aa9518a31b3f829a732362)
- [ubx_cfg_rst::reserved](../sensor_navigation_model_reference/P061_ubx_cfg_rst_结构体.md#aa1f7a46662f14e498b8bce84fb349d33)
- [ubx_cfg_val_hdr::ver](../sensor_navigation_model_reference/P062_ubx_cfg_val_hdr_结构体.md#a4d7a91e9521428e5b528ced88b030cd3)
- [ubx_cfg_val_hdr::position](../sensor_navigation_model_reference/P062_ubx_cfg_val_hdr_结构体.md#a6206dc714df9656cc37e0b802ab541b8)
- [ubx_cfg_val_hdr::layer](../sensor_navigation_model_reference/P062_ubx_cfg_val_hdr_结构体.md#aa835050e25c8db0a5a88954ff0def88c)
- [ubx_cfg_val_u16::hdr](../sensor_navigation_model_reference/P063_ubx_cfg_val_u16_结构体.md#a32e877f1e2f60b209fbcdd057aa82c4f)
- [ubx_cfg_val_u16::value](../sensor_navigation_model_reference/P063_ubx_cfg_val_u16_结构体.md#a6226f1b8f4cb89cb318c07ff8ddcbbde)
- [ubx_cfg_val_u16::key](../sensor_navigation_model_reference/P063_ubx_cfg_val_u16_结构体.md#a87a9c181318e297935bb1eb65093d4a8)
- [ubx_cfg_val_u32::value](../sensor_navigation_model_reference/P064_ubx_cfg_val_u32_结构体.md#a2c1d446c7c8bef80052d2438fb998d58)
- [ubx_cfg_val_u32::key](../sensor_navigation_model_reference/P064_ubx_cfg_val_u32_结构体.md#ab02aa8d3b7039c06692a805aed30f246)
- [ubx_cfg_val_u32::hdr](../sensor_navigation_model_reference/P064_ubx_cfg_val_u32_结构体.md#adc51df7bc8a50e1ca8843067bb309ac9)
- [ubx_cfg_val_u8::key](../sensor_navigation_model_reference/P065_ubx_cfg_val_u8_结构体.md#a2c1cbf9a552608150eafc1f2d92b03b5)
- [ubx_cfg_val_u8::value](../sensor_navigation_model_reference/P065_ubx_cfg_val_u8_结构体.md#a325aaaf688433cab710d0c3e835fb9ed)
- [ubx_cfg_val_u8::hdr](../sensor_navigation_model_reference/P065_ubx_cfg_val_u8_结构体.md#a793646932ce054ab8561078981f57250)
- [ubx_frame_match::len](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md#a36c5fd74bd6d506111b1ef2ac39cb68a)
- [ubx_frame_match::payload](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md#abbc954596995ca2dfe65de3e310e02a0)
- [ubx_frame_match::id](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md#ae65eaf921576c61ad758bfedc56d89c6)
- [ubx_frame_match::buf](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md#af78f70c27f4334fd1dcaac72d9e4ece6)
- [ubx_frame::class](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md#a2dcc29a82e7dfff2d1e4194f1bc035e8)
- [ubx_frame::id](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md#a4e578da5900365d498708f7a61d48ba4)
- [ubx_frame::payload_and_checksum](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md#a70c465b5bd1e9837c253d78fb210f4ce)
- [ubx_frame::payload_size](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md#a77b5030a6b95aef58b1c17f0368dd7ce)
- [ubx_frame::preamble_sync_char_2](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md#ac61fb72df7c1cd8a9bacb787071cb77d)
- [ubx_frame::preamble_sync_char_1](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md#acf80f38e8f26bb32848ae2978a1f87a1)
- [ubx_mon_gnss::reserved1](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#a045256bfbf8fe9b398ef77d10e00395a)
- [ubx_mon_gnss::default_enabled](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#a2b94264d40d0aa740b20d9fa9565d155)
- [ubx_mon_gnss::simultaneous](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#a34b9073dda3d6ad734109cea8ba5a0d2)
- [ubx_mon_gnss::supported](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#a8f76d361c23ae4a94d29277be0aa36f8)
- [ubx_mon_gnss::enabled](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#ad09bcd6e739e385c275f8a1cae8725b3)
- [ubx_mon_gnss::selection](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#ae004377f656dede9b0ebe98caeea588f)
- [ubx_mon_gnss::ver](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md#aebcccc44a80ef3b327d7d479ccb5ebe5)
- [ubx_mon_ver::hw_ver](../sensor_navigation_model_reference/P069_ubx_mon_ver_结构体.md#a07a2fdbe52fa48e9412f39bff1256318)
- [ubx_mon_ver::sw_ver](../sensor_navigation_model_reference/P069_ubx_mon_ver_结构体.md#aa0495c27ac850d56ddaa92bc4689ba7f)
- [ubx_nav_pvt::second](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a10b14934d80d80d3c2f0c36866bd4a64)
- [ubx_nav_pvt::tacc](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a1753595f0a3935449dee4d0c57e88a6e)
- [ubx_nav_pvt::vel_east](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a17c628b0acca293f068b58eff32ae4dd)
- [ubx_nav_pvt::minute](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a18b61263b433dc5f81c2becff9c6743c)
- [ubx_nav_pvt::flags](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a1bdc3cb0e4a2b6bef1c4216963e5c29c)
- [ubx_nav_pvt::nano](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a1c21c3b882412f36f96c59cda1d948d9)
- [ubx_nav_pvt::vel_north](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a1d50e696fa2684b55d04c652c85f2e16)
- [ubx_nav_pvt::flags2](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a2ff7d8bcc13ee956d9535c61efefada6)
- [ubx_nav_pvt::latitude](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a34ec5fc41c4b323b4719803f1ff01bed)
- [ubx_nav_pvt::ground_speed](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a38a8612a53966a1d598bf6d17443da7d)
- [ubx_nav_pvt::flags3](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a39b72f654fc8130c611ac839189914ed)
- [ubx_nav_pvt::fix_type](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a3b780d7b790b07a8ee23431969cbc318)
- [ubx_nav_pvt::itow](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a426086b12ff09fb8a00dd4623fea307e)
- [ubx_nav_pvt::valid](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a450638fda7b9d1929145575e4c576ec1)
- [ubx_nav_pvt::vel_down](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a4958a6c11bd812477d11467ab3384161)
- [ubx_nav_pvt::mag_decl](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a4f63a0f15b823e5258fdb826d2636828)
- [ubx_nav_pvt::pdop](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a7e5dc3449e52a36cb2bc5841bbf6fec8)
- [ubx_nav_pvt::reserved](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a80139f6d95bf943f5c6de6af1ea50e3e)
- [ubx_nav_pvt::year](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a84c6640806485f270b8d51d06cc49709)
- [ubx_nav_pvt::head_vehicle](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a8fc4b24fb8ffde02d306bc1b6770b1d8)
- [ubx_nav_pvt::speed_acc](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#a955d0f7927f68f540f2e9a2c91e46e79)
- [ubx_nav_pvt::head_acc](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#aa332fc93448eb6b30ad8bbaa5760db5c)
- [ubx_nav_pvt::nav](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#aa8b31a49c2844501505412da226872e1)
- [ubx_nav_pvt::height](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#ab0df156e9f8009bebfbbdb39c63c4191)
- [ubx_nav_pvt::head_motion](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#abd97f003ba43b70ffea2e9fdf5702c4f)
- [ubx_nav_pvt::magacc](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#ac0265c113f01ae2bab8553eb7148e3ae)
- [ubx_nav_pvt::horiz_acc](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#acbb58f36eb572ce27b050a8c7540f91d)
- [ubx_nav_pvt::month](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#ad90042dc5e00b91f004badcb0c3a5f4c)
- [ubx_nav_pvt::longitude](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#ae47fc34dfd91687590bd96afe2fab091)
- [ubx_nav_pvt::hmsl](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#ae6ba97f3406b9fdbbf04c4bb3e744668)
- [ubx_nav_pvt::num_sv](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#aea613eb3d604d33120e82c569c5f10e9)
- [ubx_nav_pvt::day](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#aeadb05fe45a3a0539c899129e40059fd)
- [ubx_nav_pvt::hour](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#aeb710663626935d21c77a5cfe1030795)
- [ubx_nav_pvt::vert_acc](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md#af5b3e0e70b3470bd1686ddbfefb419f9)
- [ubx_nav_sat::ubx_nav_sat_info](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md)
- [ubx_nav_sat::ubx_nav_sat_info::gnss_id](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#a04fc29e6cf9f1ff6f1f638ae633d5a11)
- [ubx_nav_sat::ubx_nav_sat_info::azimuth](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#a3a50255230b6ed80bfa4eb8ff83acf89)
- [ubx_nav_sat::ubx_nav_sat_info::pseu_res](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#a442709d1e9b43ae8c27606a5fb878c89)
- [ubx_nav_sat::ubx_nav_sat_info::cno](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#a83e6ba9e50cc24fc0d80de3947daf571)
- [ubx_nav_sat::ubx_nav_sat_info::elevation](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#a9133131e06119371d14be09f99b24a8e)
- [ubx_nav_sat::ubx_nav_sat_info::sv_id](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#ab7ba4e9d36ab136c0bb8fde9b4f9b3e5)
- [ubx_nav_sat::ubx_nav_sat_info::flags](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md#ac6872360564b383ce2cd5a061717c8fe)
- [ubx_nav_sat::reserved1](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md#a6f5bf3da0f5633aa95ff4d736656cb21)
- [ubx_nav_sat::version](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md#a7204f8b1b28f3dc0970fa62567885cdc)
- [ubx_nav_sat::itow](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md#aac587fd77fa832021ebca87e7897eb2e)
- [ubx_nav_sat::sat](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md#ade983d7b35cf81a6d769979f7cb5919d)
- [ubx_nav_sat::num_sv](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md#ae0bea798d815cc25e837e3fa394fb429)

---

[上一章](P003_if_arp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_net_ip.h_源码浏览.md)
