---
id: learning.zephyr-docs.api-source-system-reference.page-24
title: net_event.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_net\_event.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h.html)。

## 24.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00027"></a>
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
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
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
<a id="l00210"></a>
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
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
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
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
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
<a id="l00258"></a>
<a id="foldopen00260"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="foldopen00264"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="foldopen00268"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="foldopen00272"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="foldopen00276"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="foldopen00280"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="foldopen00284"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="foldopen00288"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="foldopen00292"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="foldopen00296"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="foldopen00300"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="foldopen00304"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="foldopen00308"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="foldopen00312"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="foldopen00316"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="foldopen00320"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="foldopen00324"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="foldopen00328"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="foldopen00332"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="foldopen00336"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="foldopen00340"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="foldopen00344"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="foldopen00348"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="foldopen00352"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="foldopen00356"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="foldopen00360"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="foldopen00364"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="foldopen00368"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="foldopen00372"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="foldopen00376"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="foldopen00380"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="foldopen00384"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="foldopen00388"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="foldopen00392"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="foldopen00396"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="foldopen00400"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="foldopen00404"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="foldopen00408"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="foldopen00412"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="foldopen00416"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="foldopen00420"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="foldopen00424"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="foldopen00428"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="foldopen00432"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="foldopen00436"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="foldopen00440"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="foldopen00447"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="foldopen00451"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="foldopen00458"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="foldopen00466"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="foldopen00471"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="foldopen00475"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="foldopen00479"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="foldopen00483"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="foldopen00487"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="foldopen00491"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="foldopen00506"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="foldopen00510"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="foldopen00514"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="foldopen00518"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="foldopen00522"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="foldopen00526"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="foldopen00530"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="foldopen00534"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="foldopen00538"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="foldopen00542"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="foldopen00553"></a>
<a id="l00553"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="foldopen00571"></a>
<a id="l00571"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="foldopen00585"></a>
<a id="l00585"></a>
<a id="l00587"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="foldopen00600"></a>
<a id="l00600"></a>
<a id="l00602"></a>
<a id="l00604"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="foldopen00617"></a>
<a id="l00617"></a>
<a id="l00619"></a>
<a id="l00621"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="foldopen00634"></a>
<a id="l00634"></a>
<a id="l00636"></a>
<a id="l00638"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="foldopen00649"></a>
<a id="l00649"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="foldopen00664"></a>
<a id="l00664"></a>
<a id="l00666"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="foldopen00678"></a>
<a id="l00678"></a>
<a id="l00680"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="foldopen00692"></a>
<a id="l00692"></a>
<a id="l00694"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="agroup__wifi__mgmt_html_ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6"></a>
<a id="ahostname_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="anet__mgmt_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructnet__event__ipv4__pmtu__info_html"></a>
<a id="astructnet__event__ipv4__pmtu__info_html_ae4f6951aed4253428a7ac4273b8b43fe"></a>
<a id="astructnet__event__ipv4__pmtu__info_html_aea25f385ece879bfc624f2d54f42d219"></a>
<a id="astructnet__event__ipv4__route_html"></a>
<a id="astructnet__event__ipv4__route_html_a1b4cf425bb860b6a2b210ce49969218b"></a>
<a id="astructnet__event__ipv4__route_html_a6db2fd490100464f4085202cbd30acc2"></a>
<a id="astructnet__event__ipv4__route_html_afe30f770f0776d0116bb737a7130ce0f"></a>
<a id="astructnet__event__ipv6__addr_html"></a>
<a id="astructnet__event__ipv6__addr_html_a2a4cbf602f98c30fd7cd5d024c569115"></a>
<a id="astructnet__event__ipv6__nbr_html"></a>
<a id="astructnet__event__ipv6__nbr_html_adeb139ad70e794d1a805315ffd1fcbee"></a>
<a id="astructnet__event__ipv6__nbr_html_ae18f586f643f893d71ab25921eb3ccb3"></a>
<a id="astructnet__event__ipv6__pe__filter_html"></a>
<a id="astructnet__event__ipv6__pe__filter_html_a07961a42f5ff8ca98615164192b8ca5a"></a>
<a id="astructnet__event__ipv6__pe__filter_html_a20e3beb1a70c1ff4c4aabe95456df1e0"></a>
<a id="astructnet__event__ipv6__pmtu__info_html"></a>
<a id="astructnet__event__ipv6__pmtu__info_html_a52e5078e0f39cb5e95d4e5bc42674480"></a>
<a id="astructnet__event__ipv6__pmtu__info_html_a5614582b5a0c361355c29abaf1045b62"></a>
<a id="astructnet__event__ipv6__prefix_html"></a>
<a id="astructnet__event__ipv6__prefix_html_a3d70216e13fc0f78e08eb27f34fe8ace"></a>
<a id="astructnet__event__ipv6__prefix_html_a6d7b0323896e43a04931ece4daaa09c4"></a>
<a id="astructnet__event__ipv6__prefix_html_ada864bb20887133a472363a5f66208ee"></a>
<a id="astructnet__event__ipv6__route_html"></a>
<a id="astructnet__event__ipv6__route_html_aa1f21f6963befb3f94183d02c6d2d23f"></a>
<a id="astructnet__event__ipv6__route_html_ae47c91ba21747f56b6e3ee0bd5ec199f"></a>
<a id="astructnet__event__ipv6__route_html_af9498993cb46796e1d2f150a49bfb067"></a>
<a id="astructnet__event__l4__hostname_html"></a>
<a id="astructnet__event__l4__hostname_html_a8e04c33dfb1c251a0deaa29081283245"></a>
<a id="astructnet__event__packet__mcast_html"></a>
<a id="astructnet__event__packet__mcast_html_a381a3493e2ca457eb5dda2516193e280"></a>
<a id="astructnet__event__packet__mcast_html_ade122db0aa2fb8b72064da6dc3e4afe7"></a>
<a id="astructnet__in6__addr_html"></a>
<a id="astructnet__in__addr_html"></a>
<a id="astructnet__linkaddr_html"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_NET_EVENT_H_
#define ZEPHYR_INCLUDE_NET_NET_EVENT_H_

#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_mgmt.h>
#include <zephyr/net/hostname.h>

#ifdef __cplusplus
extern "C" {
#endif



/* Network Interface events */
#define NET_IF_LAYER            NET_MGMT_LAYER_L2
#define NET_IF_CORE_CODE        NET_MGMT_LAYER_CODE_IFACE
#define NET_EVENT_IF_BASE       (NET_MGMT_EVENT_BIT |                   \
                                 NET_MGMT_IFACE_BIT |                   \
                                 NET_MGMT_LAYER(NET_IF_LAYER) | \
                                 NET_MGMT_LAYER_CODE(NET_IF_CORE_CODE))

enum {
        NET_EVENT_IF_CMD_DOWN_VAL,
        NET_EVENT_IF_CMD_UP_VAL,
        NET_EVENT_IF_CMD_ADMIN_DOWN_VAL,
        NET_EVENT_IF_CMD_ADMIN_UP_VAL,

        NET_EVENT_IF_CMD_MAX
};

BUILD_ASSERT(NET_EVENT_IF_CMD_MAX <= NET_MGMT_MAX_COMMANDS,
             "Number of events in net_event_if_cmd exceeds the limit");

enum net_event_if_cmd {
        NET_MGMT_CMD(NET_EVENT_IF_CMD_DOWN),
        NET_MGMT_CMD(NET_EVENT_IF_CMD_UP),
        NET_MGMT_CMD(NET_EVENT_IF_CMD_ADMIN_DOWN),
        NET_MGMT_CMD(NET_EVENT_IF_CMD_ADMIN_UP),
};

/* Packet socket (L2) events */
#define NET_PACKET_LAYER        NET_MGMT_LAYER_L2
#define NET_PACKET_CORE_CODE    NET_MGMT_LAYER_CODE_PACKET
#define NET_EVENT_PACKET_BASE   (NET_MGMT_EVENT_BIT |                   \
                                 NET_MGMT_IFACE_BIT |                   \
                                 NET_MGMT_LAYER(NET_PACKET_LAYER) |     \
                                 NET_MGMT_LAYER_CODE(NET_PACKET_CORE_CODE))

enum {
        NET_EVENT_PACKET_CMD_MCAST_MEMBERSHIP_ADD_VAL,
        NET_EVENT_PACKET_CMD_MCAST_MEMBERSHIP_DROP_VAL,

        NET_EVENT_PACKET_CMD_MAX
};

BUILD_ASSERT(NET_EVENT_PACKET_CMD_MAX <= NET_MGMT_MAX_COMMANDS,
             "Number of events in net_event_packet_cmd exceeds the limit");

enum net_event_packet_cmd {
        NET_MGMT_CMD(NET_EVENT_PACKET_CMD_MCAST_MEMBERSHIP_ADD),
        NET_MGMT_CMD(NET_EVENT_PACKET_CMD_MCAST_MEMBERSHIP_DROP),
};

/* IPv6 Events */
#define NET_IPV6_LAYER          NET_MGMT_LAYER_L3
#define NET_IPV6_CORE_CODE      NET_MGMT_LAYER_CODE_IPV6
#define NET_EVENT_IPV6_BASE     (NET_MGMT_EVENT_BIT |                   \
                                 NET_MGMT_IFACE_BIT |                   \
                                 NET_MGMT_LAYER(NET_IPV6_LAYER) |       \
                                 NET_MGMT_LAYER_CODE(NET_IPV6_CORE_CODE))

enum {
        NET_EVENT_IPV6_CMD_ADDR_ADD_VAL,
        NET_EVENT_IPV6_CMD_ADDR_DEL_VAL,
        NET_EVENT_IPV6_CMD_MADDR_ADD_VAL,
        NET_EVENT_IPV6_CMD_MADDR_DEL_VAL,
        NET_EVENT_IPV6_CMD_PREFIX_ADD_VAL,
        NET_EVENT_IPV6_CMD_PREFIX_DEL_VAL,
        NET_EVENT_IPV6_CMD_MCAST_JOIN_VAL,
        NET_EVENT_IPV6_CMD_MCAST_LEAVE_VAL,
        NET_EVENT_IPV6_CMD_ROUTER_ADD_VAL,
        NET_EVENT_IPV6_CMD_ROUTER_DEL_VAL,
        NET_EVENT_IPV6_CMD_ROUTE_ADD_VAL,
        NET_EVENT_IPV6_CMD_ROUTE_DEL_VAL,
        NET_EVENT_IPV6_CMD_DAD_SUCCEED_VAL,
        NET_EVENT_IPV6_CMD_DAD_FAILED_VAL,
        NET_EVENT_IPV6_CMD_NBR_ADD_VAL,
        NET_EVENT_IPV6_CMD_NBR_DEL_VAL,
        NET_EVENT_IPV6_CMD_DHCP_START_VAL,
        NET_EVENT_IPV6_CMD_DHCP_BOUND_VAL,
        NET_EVENT_IPV6_CMD_DHCP_STOP_VAL,
        NET_EVENT_IPV6_CMD_ADDR_DEPRECATED_VAL,
        NET_EVENT_IPV6_CMD_PE_ENABLED_VAL,
        NET_EVENT_IPV6_CMD_PE_DISABLED_VAL,
        NET_EVENT_IPV6_CMD_PE_FILTER_ADD_VAL,
        NET_EVENT_IPV6_CMD_PE_FILTER_DEL_VAL,
        NET_EVENT_IPV6_CMD_PMTU_CHANGED_VAL,

        NET_EVENT_IPV6_CMD_MAX
};

BUILD_ASSERT(NET_EVENT_IPV6_CMD_MAX <= NET_MGMT_MAX_COMMANDS,
             "Number of events in net_event_ipv6_cmd exceeds the limit");

enum net_event_ipv6_cmd {
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_ADDR_ADD),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_ADDR_DEL),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_MADDR_ADD),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_MADDR_DEL),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_PREFIX_ADD),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_PREFIX_DEL),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_MCAST_JOIN),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_MCAST_LEAVE),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_ROUTER_ADD),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_ROUTER_DEL),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_ROUTE_ADD),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_ROUTE_DEL),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_DAD_SUCCEED),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_DAD_FAILED),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_NBR_ADD),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_NBR_DEL),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_DHCP_START),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_DHCP_BOUND),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_DHCP_STOP),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_ADDR_DEPRECATED),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_PE_ENABLED),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_PE_DISABLED),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_PE_FILTER_ADD),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_PE_FILTER_DEL),
        NET_MGMT_CMD(NET_EVENT_IPV6_CMD_PMTU_CHANGED),
};

/* IPv4 Events*/
#define NET_IPV4_LAYER          NET_MGMT_LAYER_L3
#define NET_IPV4_CORE_CODE      NET_MGMT_LAYER_CODE_IPV4
#define NET_EVENT_IPV4_BASE     (NET_MGMT_EVENT_BIT |                   \
                                 NET_MGMT_IFACE_BIT |                   \
                                 NET_MGMT_LAYER(NET_IPV4_LAYER) |       \
                                 NET_MGMT_LAYER_CODE(NET_IPV4_CORE_CODE))

enum {
        NET_EVENT_IPV4_CMD_ADDR_ADD_VAL,
        NET_EVENT_IPV4_CMD_ADDR_DEL_VAL,
        NET_EVENT_IPV4_CMD_MADDR_ADD_VAL,
        NET_EVENT_IPV4_CMD_MADDR_DEL_VAL,
        NET_EVENT_IPV4_CMD_ROUTER_ADD_VAL,
        NET_EVENT_IPV4_CMD_ROUTER_DEL_VAL,
        NET_EVENT_IPV4_CMD_ROUTE_ADD_VAL,
        NET_EVENT_IPV4_CMD_ROUTE_DEL_VAL,
        NET_EVENT_IPV4_CMD_DHCP_START_VAL,
        NET_EVENT_IPV4_CMD_DHCP_BOUND_VAL,
        NET_EVENT_IPV4_CMD_DHCP_STOP_VAL,
        NET_EVENT_IPV4_CMD_MCAST_JOIN_VAL,
        NET_EVENT_IPV4_CMD_MCAST_LEAVE_VAL,
        NET_EVENT_IPV4_CMD_ACD_SUCCEED_VAL,
        NET_EVENT_IPV4_CMD_ACD_FAILED_VAL,
        NET_EVENT_IPV4_CMD_ACD_CONFLICT_VAL,
        NET_EVENT_IPV4_CMD_PMTU_CHANGED_VAL,

        NET_EVENT_IPV4_CMD_MAX
};

BUILD_ASSERT(NET_EVENT_IPV4_CMD_MAX <= NET_MGMT_MAX_COMMANDS,
             "Number of events in net_event_ipv4_cmd exceeds the limit");

enum net_event_ipv4_cmd {
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_ADDR_ADD),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_ADDR_DEL),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_MADDR_ADD),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_MADDR_DEL),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_ROUTER_ADD),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_ROUTER_DEL),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_ROUTE_ADD),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_ROUTE_DEL),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_DHCP_START),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_DHCP_BOUND),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_DHCP_STOP),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_MCAST_JOIN),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_MCAST_LEAVE),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_ACD_SUCCEED),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_ACD_FAILED),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_ACD_CONFLICT),
        NET_MGMT_CMD(NET_EVENT_IPV4_CMD_PMTU_CHANGED),
};

/* L4 network events */
#define NET_L4_LAYER            NET_MGMT_LAYER_L4
#define NET_L4_CORE_CODE        NET_MGMT_LAYER_CODE_L4
#define NET_EVENT_L4_BASE       (NET_MGMT_EVENT_BIT |                   \
                                 NET_MGMT_IFACE_BIT |                   \
                                 NET_MGMT_LAYER(NET_L4_LAYER) | \
                                 NET_MGMT_LAYER_CODE(NET_L4_CORE_CODE))

enum {
        NET_EVENT_L4_CMD_CONNECTED_VAL,
        NET_EVENT_L4_CMD_DISCONNECTED_VAL,
        NET_EVENT_L4_CMD_IPV4_CONNECTED_VAL,
        NET_EVENT_L4_CMD_IPV4_DISCONNECTED_VAL,
        NET_EVENT_L4_CMD_IPV6_CONNECTED_VAL,
        NET_EVENT_L4_CMD_IPV6_DISCONNECTED_VAL,
        NET_EVENT_L4_CMD_DNS_SERVER_ADD_VAL,
        NET_EVENT_L4_CMD_DNS_SERVER_DEL_VAL,
        NET_EVENT_L4_CMD_HOSTNAME_CHANGED_VAL,
        NET_EVENT_L4_CMD_CAPTURE_STARTED_VAL,
        NET_EVENT_L4_CMD_CAPTURE_STOPPED_VAL,
        NET_EVENT_L4_CMD_VPN_CONNECTED_VAL,
        NET_EVENT_L4_CMD_VPN_DISCONNECTED_VAL,
        NET_EVENT_L4_CMD_VPN_PEER_ADD_VAL,
        NET_EVENT_L4_CMD_VPN_PEER_DEL_VAL,
        NET_EVENT_L4_CMD_DNS_SERVERS_RECONFIGURED_VAL,
        NET_EVENT_L4_CMD_IF_CONNECTED_VAL,
        NET_EVENT_L4_CMD_IF_DISCONNECTED_VAL,

        NET_EVENT_L4_CMD_MAX
};

BUILD_ASSERT(NET_EVENT_L4_CMD_MAX <= NET_MGMT_MAX_COMMANDS,
             "Number of events in net_event_l4_cmd exceeds the limit");

enum net_event_l4_cmd {
        NET_MGMT_CMD(NET_EVENT_L4_CMD_CONNECTED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_DISCONNECTED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_IPV4_CONNECTED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_IPV4_DISCONNECTED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_IPV6_CONNECTED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_IPV6_DISCONNECTED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_DNS_SERVER_ADD),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_DNS_SERVER_DEL),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_HOSTNAME_CHANGED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_CAPTURE_STARTED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_CAPTURE_STOPPED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_VPN_CONNECTED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_VPN_DISCONNECTED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_VPN_PEER_ADD),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_VPN_PEER_DEL),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_DNS_SERVERS_RECONFIGURED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_IF_CONNECTED),
        NET_MGMT_CMD(NET_EVENT_L4_CMD_IF_DISCONNECTED),
};


#define NET_EVENT_IF_DOWN                                       \
        (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_DOWN)

#define NET_EVENT_IF_UP                                         \
        (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_UP)

#define NET_EVENT_IF_ADMIN_DOWN                                 \
        (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_ADMIN_DOWN)

#define NET_EVENT_IF_ADMIN_UP                                   \
        (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_ADMIN_UP)

#define NET_EVENT_PACKET_MCAST_MEMBERSHIP_ADD                           \
        (NET_EVENT_PACKET_BASE | NET_EVENT_PACKET_CMD_MCAST_MEMBERSHIP_ADD)

#define NET_EVENT_PACKET_MCAST_MEMBERSHIP_DROP                          \
        (NET_EVENT_PACKET_BASE | NET_EVENT_PACKET_CMD_MCAST_MEMBERSHIP_DROP)

#define NET_EVENT_IPV6_ADDR_ADD                                 \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ADDR_ADD)

#define NET_EVENT_IPV6_ADDR_DEL                                 \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ADDR_DEL)

#define NET_EVENT_IPV6_MADDR_ADD                                \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MADDR_ADD)

#define NET_EVENT_IPV6_MADDR_DEL                                \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MADDR_DEL)

#define NET_EVENT_IPV6_PREFIX_ADD                               \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PREFIX_ADD)

#define NET_EVENT_IPV6_PREFIX_DEL                               \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PREFIX_DEL)

#define NET_EVENT_IPV6_MCAST_JOIN                               \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MCAST_JOIN)

#define NET_EVENT_IPV6_MCAST_LEAVE                              \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MCAST_LEAVE)

#define NET_EVENT_IPV6_ROUTER_ADD                               \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTER_ADD)

#define NET_EVENT_IPV6_ROUTER_DEL                               \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTER_DEL)

#define NET_EVENT_IPV6_ROUTE_ADD                                \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTE_ADD)

#define NET_EVENT_IPV6_ROUTE_DEL                                \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTE_DEL)

#define NET_EVENT_IPV6_DAD_SUCCEED                              \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DAD_SUCCEED)

#define NET_EVENT_IPV6_DAD_FAILED                               \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DAD_FAILED)

#define NET_EVENT_IPV6_NBR_ADD                                  \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_NBR_ADD)

#define NET_EVENT_IPV6_NBR_DEL                                  \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_NBR_DEL)

#define NET_EVENT_IPV6_DHCP_START                               \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DHCP_START)

#define NET_EVENT_IPV6_DHCP_BOUND                               \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DHCP_BOUND)

#define NET_EVENT_IPV6_DHCP_STOP                                \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DHCP_STOP)

#define NET_EVENT_IPV6_ADDR_DEPRECATED                          \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ADDR_DEPRECATED)

#define NET_EVENT_IPV6_PE_ENABLED                               \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_ENABLED)

#define NET_EVENT_IPV6_PE_DISABLED                              \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_DISABLED)

#define NET_EVENT_IPV6_PE_FILTER_ADD                            \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_FILTER_ADD)

#define NET_EVENT_IPV6_PE_FILTER_DEL                            \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_FILTER_DEL)

#define NET_EVENT_IPV6_PMTU_CHANGED                             \
        (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PMTU_CHANGED)

#define NET_EVENT_IPV4_ADDR_ADD                                 \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ADDR_ADD)

#define NET_EVENT_IPV4_ADDR_DEL                                 \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ADDR_DEL)

#define NET_EVENT_IPV4_MADDR_ADD                                \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MADDR_ADD)

#define NET_EVENT_IPV4_MADDR_DEL                                \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MADDR_DEL)

#define NET_EVENT_IPV4_ROUTER_ADD                               \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTER_ADD)

#define NET_EVENT_IPV4_ROUTER_DEL                               \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTER_DEL)

#define NET_EVENT_IPV4_ROUTE_ADD                                \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTE_ADD)

#define NET_EVENT_IPV4_ROUTE_DEL                                \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTE_DEL)

#define NET_EVENT_IPV4_DHCP_START                               \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_DHCP_START)

#define NET_EVENT_IPV4_DHCP_BOUND                               \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_DHCP_BOUND)

#define NET_EVENT_IPV4_DHCP_STOP                                \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_DHCP_STOP)

#define NET_EVENT_IPV4_MCAST_JOIN                               \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MCAST_JOIN)

#define NET_EVENT_IPV4_MCAST_LEAVE                              \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MCAST_LEAVE)

#define NET_EVENT_IPV4_ACD_SUCCEED                              \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ACD_SUCCEED)

#define NET_EVENT_IPV4_ACD_FAILED                               \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ACD_FAILED)

#define NET_EVENT_IPV4_ACD_CONFLICT                             \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ACD_CONFLICT)

#define NET_EVENT_IPV4_PMTU_CHANGED                             \
        (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_PMTU_CHANGED)

#define NET_EVENT_L4_CONNECTED                                  \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_CONNECTED)

#define NET_EVENT_L4_DISCONNECTED                       \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DISCONNECTED)


#define NET_EVENT_L4_IPV4_CONNECTED                     \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV4_CONNECTED)

#define NET_EVENT_L4_IPV4_DISCONNECTED                  \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV4_DISCONNECTED)

#define NET_EVENT_L4_IPV6_CONNECTED                     \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV6_CONNECTED)

#define NET_EVENT_L4_IPV6_DISCONNECTED                  \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV6_DISCONNECTED)

#define NET_EVENT_DNS_SERVER_ADD                        \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DNS_SERVER_ADD)

#define NET_EVENT_DNS_SERVER_DEL                        \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DNS_SERVER_DEL)

#define NET_EVENT_DNS_SERVERS_RECONFIGURED              \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DNS_SERVERS_RECONFIGURED)

#define NET_EVENT_HOSTNAME_CHANGED                      \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_HOSTNAME_CHANGED)

#define NET_EVENT_CAPTURE_STARTED                       \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_CAPTURE_STARTED)

#define NET_EVENT_CAPTURE_STOPPED                       \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_CAPTURE_STOPPED)

#define NET_EVENT_VPN_CONNECTED                         \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_CONNECTED)

#define NET_EVENT_VPN_DISCONNECTED                      \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_DISCONNECTED)

#define NET_EVENT_VPN_PEER_ADD                          \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_PEER_ADD)

#define NET_EVENT_VPN_PEER_DEL                          \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_PEER_DEL)

#define NET_EVENT_L4_IF_CONNECTED                       \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IF_CONNECTED)

#define NET_EVENT_L4_IF_DISCONNECTED                    \
        (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IF_DISCONNECTED)

struct net_event_packet_mcast {
        struct net_linkaddr addr;

        uint16_t type;
};

struct net_event_ipv6_addr {
        struct net_in6_addr addr;
};

struct net_event_ipv6_nbr {
        struct net_in6_addr addr;
        int idx;
};

struct net_event_ipv6_route {
        struct net_in6_addr nexthop;
        struct net_in6_addr addr;
        uint8_t prefix_len;
};

struct net_event_ipv4_route {
        struct net_in_addr nexthop;
        struct net_in_addr addr;
        uint8_t prefix_len;
};

struct net_event_ipv6_prefix {
        struct net_in6_addr addr;
        uint8_t len;
        uint32_t lifetime;
};

struct net_event_l4_hostname {
        char hostname[NET_HOSTNAME_SIZE];
};

struct net_event_ipv6_pe_filter {
        struct net_in6_addr prefix;
        bool is_deny_list;
};

struct net_event_ipv4_pmtu_info {
        struct net_in_addr dst;
        uint16_t mtu;
};

struct net_event_ipv6_pmtu_info {
        struct net_in6_addr dst;
        uint32_t mtu;
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_NET_EVENT_H_ */
```

## 24.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 30 行

网络接口事件（Network Interface Events）。

### 注释 3：原第 57 行

二层数据包套接字事件（Packet Socket L2 Events）。

### 注释 4：原第 80 行

IPv6 事件（Events）。

### 注释 5：原第 149 行

IPv4 事件（Events）。

### 注释 6：原第 202 行

四层网络事件（L4 Network Events）。

### 注释 7：原第 707 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_EVENT_H_`。

## 24.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [zephyr/net/hostname.h](https://docs.zephyrproject.org/latest/doxygen/html/hostname_8h.html)
- [NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)
- [net_event_packet_mcast](../network_core_model_reference/P073_net_event_packet_mcast_结构体.md)
- [net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)
- [addr](../network_core_model_reference/P073_net_event_packet_mcast_结构体.md#a381a3493e2ca457eb5dda2516193e280)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [type](../network_core_model_reference/P073_net_event_packet_mcast_结构体.md#ade122db0aa2fb8b72064da6dc3e4afe7)
- [net_event_ipv6_addr](../network_core_model_reference/P066_net_event_ipv6_addr_结构体.md)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [addr](../network_core_model_reference/P066_net_event_ipv6_addr_结构体.md#a2a4cbf602f98c30fd7cd5d024c569115)
- [net_event_ipv6_nbr](../network_core_model_reference/P067_net_event_ipv6_nbr_结构体.md)
- [addr](../network_core_model_reference/P067_net_event_ipv6_nbr_结构体.md#ae18f586f643f893d71ab25921eb3ccb3)
- [idx](../network_core_model_reference/P067_net_event_ipv6_nbr_结构体.md#adeb139ad70e794d1a805315ffd1fcbee)
- [net_event_ipv6_route](../network_core_model_reference/P071_net_event_ipv6_route_结构体.md)
- [nexthop](../network_core_model_reference/P071_net_event_ipv6_route_结构体.md#af9498993cb46796e1d2f150a49bfb067)
- [addr](../network_core_model_reference/P071_net_event_ipv6_route_结构体.md#ae47c91ba21747f56b6e3ee0bd5ec199f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [prefix_len](../network_core_model_reference/P071_net_event_ipv6_route_结构体.md#aa1f21f6963befb3f94183d02c6d2d23f)
- [net_event_ipv4_route](../network_core_model_reference/P065_net_event_ipv4_route_结构体.md)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [nexthop](../network_core_model_reference/P065_net_event_ipv4_route_结构体.md#a1b4cf425bb860b6a2b210ce49969218b)
- [addr](../network_core_model_reference/P065_net_event_ipv4_route_结构体.md#afe30f770f0776d0116bb737a7130ce0f)
- [prefix_len](../network_core_model_reference/P065_net_event_ipv4_route_结构体.md#a6db2fd490100464f4085202cbd30acc2)
- [net_event_ipv6_prefix](../network_core_model_reference/P070_net_event_ipv6_prefix_结构体.md)
- [addr](../network_core_model_reference/P070_net_event_ipv6_prefix_结构体.md#ada864bb20887133a472363a5f66208ee)
- [len](../network_core_model_reference/P070_net_event_ipv6_prefix_结构体.md#a3d70216e13fc0f78e08eb27f34fe8ace)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [lifetime](../network_core_model_reference/P070_net_event_ipv6_prefix_结构体.md#a6d7b0323896e43a04931ece4daaa09c4)
- [net_event_l4_hostname](../network_core_model_reference/P072_net_event_l4_hostname_结构体.md)
- [hostname](../network_core_model_reference/P072_net_event_l4_hostname_结构体.md#a8e04c33dfb1c251a0deaa29081283245)
- [net_event_ipv6_pe_filter](../network_core_model_reference/P068_net_event_ipv6_pe_filter_结构体.md)
- [prefix](../network_core_model_reference/P068_net_event_ipv6_pe_filter_结构体.md#a20e3beb1a70c1ff4c4aabe95456df1e0)
- [is_deny_list](../network_core_model_reference/P068_net_event_ipv6_pe_filter_结构体.md#a07961a42f5ff8ca98615164192b8ca5a)
- [net_event_ipv4_pmtu_info](../network_core_model_reference/P064_net_event_ipv4_pmtu_info_结构体.md)
- [dst](../network_core_model_reference/P064_net_event_ipv4_pmtu_info_结构体.md#aea25f385ece879bfc624f2d54f42d219)
- [mtu](../network_core_model_reference/P064_net_event_ipv4_pmtu_info_结构体.md#ae4f6951aed4253428a7ac4273b8b43fe)
- [net_event_ipv6_pmtu_info](../network_core_model_reference/P069_net_event_ipv6_pmtu_info_结构体.md)
- [dst](../network_core_model_reference/P069_net_event_ipv6_pmtu_info_结构体.md#a5614582b5a0c361355c29abaf1045b62)
- [mtu](../network_core_model_reference/P069_net_event_ipv6_pmtu_info_结构体.md#a52e5078e0f39cb5e95d4e5bc42674480)
- [hostname.h](https://docs.zephyrproject.org/latest/doxygen/html/hostname_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [net_event_ipv4_pmtu_info::mtu](../network_core_model_reference/P064_net_event_ipv4_pmtu_info_结构体.md#ae4f6951aed4253428a7ac4273b8b43fe)
- [net_event_ipv4_pmtu_info::dst](../network_core_model_reference/P064_net_event_ipv4_pmtu_info_结构体.md#aea25f385ece879bfc624f2d54f42d219)
- [net_event_ipv4_route::nexthop](../network_core_model_reference/P065_net_event_ipv4_route_结构体.md#a1b4cf425bb860b6a2b210ce49969218b)
- [net_event_ipv4_route::prefix_len](../network_core_model_reference/P065_net_event_ipv4_route_结构体.md#a6db2fd490100464f4085202cbd30acc2)
- [net_event_ipv4_route::addr](../network_core_model_reference/P065_net_event_ipv4_route_结构体.md#afe30f770f0776d0116bb737a7130ce0f)
- [net_event_ipv6_addr::addr](../network_core_model_reference/P066_net_event_ipv6_addr_结构体.md#a2a4cbf602f98c30fd7cd5d024c569115)
- [net_event_ipv6_nbr::idx](../network_core_model_reference/P067_net_event_ipv6_nbr_结构体.md#adeb139ad70e794d1a805315ffd1fcbee)
- [net_event_ipv6_nbr::addr](../network_core_model_reference/P067_net_event_ipv6_nbr_结构体.md#ae18f586f643f893d71ab25921eb3ccb3)
- [net_event_ipv6_pe_filter::is_deny_list](../network_core_model_reference/P068_net_event_ipv6_pe_filter_结构体.md#a07961a42f5ff8ca98615164192b8ca5a)
- [net_event_ipv6_pe_filter::prefix](../network_core_model_reference/P068_net_event_ipv6_pe_filter_结构体.md#a20e3beb1a70c1ff4c4aabe95456df1e0)
- [net_event_ipv6_pmtu_info::mtu](../network_core_model_reference/P069_net_event_ipv6_pmtu_info_结构体.md#a52e5078e0f39cb5e95d4e5bc42674480)
- [net_event_ipv6_pmtu_info::dst](../network_core_model_reference/P069_net_event_ipv6_pmtu_info_结构体.md#a5614582b5a0c361355c29abaf1045b62)
- [net_event_ipv6_prefix::len](../network_core_model_reference/P070_net_event_ipv6_prefix_结构体.md#a3d70216e13fc0f78e08eb27f34fe8ace)
- [net_event_ipv6_prefix::lifetime](../network_core_model_reference/P070_net_event_ipv6_prefix_结构体.md#a6d7b0323896e43a04931ece4daaa09c4)
- [net_event_ipv6_prefix::addr](../network_core_model_reference/P070_net_event_ipv6_prefix_结构体.md#ada864bb20887133a472363a5f66208ee)
- [net_event_ipv6_route::prefix_len](../network_core_model_reference/P071_net_event_ipv6_route_结构体.md#aa1f21f6963befb3f94183d02c6d2d23f)
- [net_event_ipv6_route::addr](../network_core_model_reference/P071_net_event_ipv6_route_结构体.md#ae47c91ba21747f56b6e3ee0bd5ec199f)
- [net_event_ipv6_route::nexthop](../network_core_model_reference/P071_net_event_ipv6_route_结构体.md#af9498993cb46796e1d2f150a49bfb067)
- [net_event_l4_hostname::hostname](../network_core_model_reference/P072_net_event_l4_hostname_结构体.md#a8e04c33dfb1c251a0deaa29081283245)
- [net_event_packet_mcast::addr](../network_core_model_reference/P073_net_event_packet_mcast_结构体.md#a381a3493e2ca457eb5dda2516193e280)
- [net_event_packet_mcast::type](../network_core_model_reference/P073_net_event_packet_mcast_结构体.md#ade122db0aa2fb8b72064da6dc3e4afe7)

---

[上一章](P023_net_core.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P025_npcx_espi.h_源码浏览.md)
