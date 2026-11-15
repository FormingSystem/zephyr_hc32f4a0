---
id: learning.zephyr-docs.api-source-device-reference.page-20
title: hci_vs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_hci\_vs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_runtime_reference/P017_zephyr__bluetooth__hci_vs.h_文件参考.md)。

## 20.1\_原始可见代码（Source Code）

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
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00046"></a>
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
<a id="foldopen00074"></a>
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
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00105"></a>
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
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00125"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00136"></a>
<a id="l00136"></a>
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
<a id="foldopen00150"></a>
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
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
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
<a id="foldopen00172"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="foldopen00187"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="foldopen00195"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="foldopen00200"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="foldopen00209"></a>
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
<a id="foldopen00220"></a>
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
<a id="l00232"></a>
<a id="l00233"></a>
<a id="foldopen00234"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="foldopen00241"></a>
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
<a id="foldopen00253"></a>
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
<a id="foldopen00264"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="foldopen00275"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="foldopen00281"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="foldopen00286"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="foldopen00293"></a>
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
<a id="foldopen00307"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
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
<a id="l00327"></a>
<a id="l00328"></a>
<a id="foldopen00329"></a>
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
<a id="foldopen00340"></a>
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
<a id="foldopen00363"></a>
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
<a id="foldopen00381"></a>
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
<a id="foldopen00397"></a>
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
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="foldopen00418"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="foldopen00425"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="foldopen00428"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="foldopen00435"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="foldopen00440"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="foldopen00446"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="foldopen00452"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="foldopen00457"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="foldopen00465"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="aaddr_8h_html"></a>
<a id="ahci_8h_html"></a>
<a id="ahci__types_8h_html"></a>
<a id="ahci__vs_8h_html_a9a91c493cc947492d5a172a15abe9a4e"></a>
<a id="ahci__vs_8h_html_aa90c2106bbb977f1ea8532212ff01b4d"></a>
<a id="ahci__vs_8h_html_afc9ea0e4f2260bf59336f2c66532d9b1"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructbt__addr__le__t_html"></a>
<a id="astructbt__addr__t_html"></a>
<a id="astructbt__hci__cp__mesh__advertise__cancel_html"></a>
<a id="astructbt__hci__cp__mesh__advertise__cancel_html_acd1409f2299c6bbddffd62d5e10e6e7c"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html_a1a5a5964eeff05fa232543756d234759"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html_a6718fd6031b2351eb033333a7302a21b"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html_a78ecf7aa6ebf0739a585fed2a8710301"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html_a85a7e965b8004cac3a4bc0107844c69b"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html_a92f0163ec0854296ab76e49741d45196"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html_aa5bf4322faa354cc6de0c707502b4ed0"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html_aae34dd11723383b5559dc102c59213c2"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html_ac097c1ee537d9a480ae16205eafc7105"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html_ada4348480db5f95acaad86bfa2ddbc7e"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html_adfb3acf9ea540d8405c5979115053b15"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html_ae395b4a53ff9e7af8885b9583562022a"></a>
<a id="astructbt__hci__cp__mesh__advertise__timed_html_aee05619f0ed3b79f3bce5676c1f3aa8a"></a>
<a id="astructbt__hci__cp__mesh__advertise_html"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_a0b190fcabae8555e65a251b37ab5b232"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_a0b22a8e1109db932f86bb7312dfeca9e"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_a278c21295c73947d7b0971a6ac043d62"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_a3cf773db54448d5f7b3da652a798c712"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_a46242ef61b79723e5136373fa534a292"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_a5ea37039c817d58d13feb98d5658cbf1"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_a67aef4d217cb6b5762b4f823c8f234df"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_a6ac4b4dad0ce54e69afd2b8e1f6cdf4f"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_a6b6248069fa1e7eaf6825c52e38c3e78"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_a7ec17216955ac784cd213b11038c3521"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_a9ed6d2b96d9aa417ccd996e650bb00fa"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_ab1b873984143301808f23824074e4df8"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_ad2af78fa8d14f1334b52f659f3497b4e"></a>
<a id="astructbt__hci__cp__mesh__advertise_html_af1482ed0255e35d7a2016017dab8713a"></a>
<a id="astructbt__hci__cp__mesh__set__scan__filter_html"></a>
<a id="astructbt__hci__cp__mesh__set__scan__filter_html_a3f99242946f3a5a8322a8333d9c58b30"></a>
<a id="astructbt__hci__cp__mesh__set__scan__filter_html_a41737323ab5723ce781f77f5752915e3"></a>
<a id="astructbt__hci__cp__mesh__set__scan__filter_html_a4e72bcfac1beec704d860034abcf22c0"></a>
<a id="astructbt__hci__cp__mesh__set__scan__filter_html_aa1e74c7f4dc39cf2ad0c130bf8dafa72"></a>
<a id="astructbt__hci__cp__mesh__set__scanning_html"></a>
<a id="astructbt__hci__cp__mesh__set__scanning_html_a2b27e80def9b437c16de186d5371e140"></a>
<a id="astructbt__hci__cp__mesh__set__scanning_html_ac7cf268f484a575268fc6aa0f1b44cce"></a>
<a id="astructbt__hci__cp__mesh__set__scanning_html_aed23ad3e51e459bbc86945576a8113ef"></a>
<a id="astructbt__hci__cp__mesh_html"></a>
<a id="astructbt__hci__cp__mesh_html_af29f0e2fd21f226143e0908c43c72a0f"></a>
<a id="astructbt__hci__cp__vs__read__tx__power__level_html"></a>
<a id="astructbt__hci__cp__vs__read__tx__power__level_html_a2bb528f003b22b88eec0d7389c84034f"></a>
<a id="astructbt__hci__cp__vs__read__tx__power__level_html_a776450ea2132fab77b9350ae46d3a1b5"></a>
<a id="astructbt__hci__cp__vs__reset_html"></a>
<a id="astructbt__hci__cp__vs__reset_html_aa3a47f4d2a593a9c756893ec28e49a00"></a>
<a id="astructbt__hci__cp__vs__set__event__mask_html"></a>
<a id="astructbt__hci__cp__vs__set__event__mask_html_ad5883adb065f04e923ff64093c78949a"></a>
<a id="astructbt__hci__cp__vs__set__min__num__used__chans_html"></a>
<a id="astructbt__hci__cp__vs__set__min__num__used__chans_html_a68262baddf6b7d2d42d61ad4c2690567"></a>
<a id="astructbt__hci__cp__vs__set__min__num__used__chans_html_a8cfa13723348bb43c19ceaa56fad2b1c"></a>
<a id="astructbt__hci__cp__vs__set__min__num__used__chans_html_aae4d29392f389a20f9be86870defc954"></a>
<a id="astructbt__hci__cp__vs__set__scan__req__reports_html"></a>
<a id="astructbt__hci__cp__vs__set__scan__req__reports_html_ac99b6b1fee39a2330c6d0c214c737fd3"></a>
<a id="astructbt__hci__cp__vs__set__trace__enable_html"></a>
<a id="astructbt__hci__cp__vs__set__trace__enable_html_a18c3c81f13599a12903b12e350703dc5"></a>
<a id="astructbt__hci__cp__vs__set__trace__enable_html_a5676627500b6c5aff5986c53a0ba13a7"></a>
<a id="astructbt__hci__cp__vs__set__usb__transport__mode_html"></a>
<a id="astructbt__hci__cp__vs__set__usb__transport__mode_html_a651867bbfbc6ff642fbc294488259b4e"></a>
<a id="astructbt__hci__cp__vs__write__bd__addr_html"></a>
<a id="astructbt__hci__cp__vs__write__bd__addr_html_af54e126fff610467dd730902893b6cd2"></a>
<a id="astructbt__hci__cp__vs__write__tx__power__level_html"></a>
<a id="astructbt__hci__cp__vs__write__tx__power__level_html_a27e1b402a9a1a8850f551a18651e914e"></a>
<a id="astructbt__hci__cp__vs__write__tx__power__level_html_abd7f6c92c1463ec35cfd552ffce50b53"></a>
<a id="astructbt__hci__cp__vs__write__tx__power__level_html_adff511831f183e031d9c61781d337b9d"></a>
<a id="astructbt__hci__evt__mesh__adv__complete_html"></a>
<a id="astructbt__hci__evt__mesh__adv__complete_html_a2c9240a7fa61dad2c7a29b1ad4e555b1"></a>
<a id="astructbt__hci__evt__mesh__scan__report_html"></a>
<a id="astructbt__hci__evt__mesh__scan__report_html_a20d5ffe0df68bee1205a5ee1a5abd6b2"></a>
<a id="astructbt__hci__evt__mesh__scan__report_html_a281d2c97835fb2f42c6fb322a26d8899"></a>
<a id="astructbt__hci__evt__mesh__scan__report_html_a3d283dd74c33b01fffb42bd4560c6e47"></a>
<a id="astructbt__hci__evt__mesh__scan__report_html_a573ad980305fb7c10b731a1867c97d1b"></a>
<a id="astructbt__hci__evt__mesh__scan__report_html_aa62526739d11d0fa2614e0822f3d70a7"></a>
<a id="astructbt__hci__evt__mesh__scan__report_html_af8fb2e61dfe3a3860bf68af0ee8626e6"></a>
<a id="astructbt__hci__evt__mesh__scanning__report_html"></a>
<a id="astructbt__hci__evt__mesh__scanning__report_html_a5daf719f2f5ec6e47f7a93d47d5c2b17"></a>
<a id="astructbt__hci__evt__mesh__scanning__report_html_aa63b838e431b358bf1a3495998dfd952"></a>
<a id="astructbt__hci__evt__mesh_html"></a>
<a id="astructbt__hci__evt__mesh_html_aaa8104b855bba787c69851ae7872a03e"></a>
<a id="astructbt__hci__evt__mesh_html_ac0186d74e355c90c866dda51605b85ac"></a>
<a id="astructbt__hci__evt__vs__fatal__error__trace__data_html"></a>
<a id="astructbt__hci__evt__vs__fatal__error__trace__data_html_a467d2de2a3b26ddef8c412957abfd820"></a>
<a id="astructbt__hci__evt__vs__fatal__error__trace__data_html_ae1efc729b0c079fa922dcfffab6cdfa6"></a>
<a id="astructbt__hci__evt__vs__fatal__error_html"></a>
<a id="astructbt__hci__evt__vs__fatal__error_html_a15e84185f74e84e1f9ccd83dc4fa2798"></a>
<a id="astructbt__hci__evt__vs__fatal__error_html_aefd553e85eedb6e205da39916c5553aa"></a>
<a id="astructbt__hci__evt__vs__le__connection__iq__report_html"></a>
<a id="astructbt__hci__evt__vs__le__connection__iq__report_html_a55a290121f661f155684d37fa0df77d2"></a>
<a id="astructbt__hci__evt__vs__le__connection__iq__report_html_a71227b896453143a6a4ad11b7e985a16"></a>
<a id="astructbt__hci__evt__vs__le__connection__iq__report_html_a87d4a6ebd1cc172816f3fe786c22f058"></a>
<a id="astructbt__hci__evt__vs__le__connection__iq__report_html_a941d0e025334a0c041cc7a59b69f0af3"></a>
<a id="astructbt__hci__evt__vs__le__connection__iq__report_html_a959c7e2b910aec90f8b186550cb7f4d8"></a>
<a id="astructbt__hci__evt__vs__le__connection__iq__report_html_aa2a9c3589bf8e152627a79c17102ec7c"></a>
<a id="astructbt__hci__evt__vs__le__connection__iq__report_html_aaa29121a6b7fc8f9a76e6b83f6b80f4d"></a>
<a id="astructbt__hci__evt__vs__le__connection__iq__report_html_ab96606229994abe966f03c65d57e5568"></a>
<a id="astructbt__hci__evt__vs__le__connection__iq__report_html_abb2b6e915f8de6ad2013a79d0b4ee288"></a>
<a id="astructbt__hci__evt__vs__le__connection__iq__report_html_ad714bb1f2292764eba9c506bcc72bccd"></a>
<a id="astructbt__hci__evt__vs__le__connection__iq__report_html_af634fa464d4ca435ea935ae58db86cfa"></a>
<a id="astructbt__hci__evt__vs__le__connectionless__iq__report_html"></a>
<a id="astructbt__hci__evt__vs__le__connectionless__iq__report_html_a17c9d19883c9d8e34f300fbff614b475"></a>
<a id="astructbt__hci__evt__vs__le__connectionless__iq__report_html_a2698510deb6bd8943bf57104f96673db"></a>
<a id="astructbt__hci__evt__vs__le__connectionless__iq__report_html_a5fcd776dce904763c5cc6fab9a1373f4"></a>
<a id="astructbt__hci__evt__vs__le__connectionless__iq__report_html_a808a2a134104c69073af253a3c4dd1bd"></a>
<a id="astructbt__hci__evt__vs__le__connectionless__iq__report_html_a9b7eb8a5cf363c3aec96b49853056dc7"></a>
<a id="astructbt__hci__evt__vs__le__connectionless__iq__report_html_a9c199121ac475d635fc51289e8eba979"></a>
<a id="astructbt__hci__evt__vs__le__connectionless__iq__report_html_ab6911af90d85c565615c437715d9c7eb"></a>
<a id="astructbt__hci__evt__vs__le__connectionless__iq__report_html_ac0b077d7b5e2b7c5ce61b3060913cad5"></a>
<a id="astructbt__hci__evt__vs__le__connectionless__iq__report_html_ad15beccc7c2207565678ebef72346158"></a>
<a id="astructbt__hci__evt__vs__le__connectionless__iq__report_html_af5b27c1504ce4ff8afe23c28a9ac423f"></a>
<a id="astructbt__hci__evt__vs__scan__req__rx_html"></a>
<a id="astructbt__hci__evt__vs__scan__req__rx_html_a56613220a50bc50a771f432b7e617d5b"></a>
<a id="astructbt__hci__evt__vs__scan__req__rx_html_acbfa7ec0a3ab1f94f53598a9d8242aba"></a>
<a id="astructbt__hci__evt__vs__trace__info_html"></a>
<a id="astructbt__hci__evt__vs__trace__info_html_ae524df8cc722cda0fa86127a6b8e56da"></a>
<a id="astructbt__hci__evt__vs__trace__info_html_af563e07c5364df229eb767e545c8aaa2"></a>
<a id="astructbt__hci__evt__vs_html"></a>
<a id="astructbt__hci__evt__vs_html_aadf6dd6172922d32a4a40be003f09876"></a>
<a id="astructbt__hci__le__iq__sample16_html"></a>
<a id="astructbt__hci__le__iq__sample16_html_aa317d2a9f451eeecb35ff05044ea6dc3"></a>
<a id="astructbt__hci__le__iq__sample16_html_ace47fd665d57f7ad7eb0a04ec8e54a47"></a>
<a id="astructbt__hci__mesh__pattern_html"></a>
<a id="astructbt__hci__mesh__pattern_html_a2ab9eac21c74a03416007f5b7d0f5bc4"></a>
<a id="astructbt__hci__mesh__pattern_html_a78e52a2890db71c501885f575bc80de4"></a>
<a id="astructbt__hci__rp__mesh__advertise__cancel_html"></a>
<a id="astructbt__hci__rp__mesh__advertise__cancel_html_abcc6cd11403b34f04ff4e128628d7484"></a>
<a id="astructbt__hci__rp__mesh__advertise__cancel_html_ac8a13ab9c91a88859803dcf9f80658af"></a>
<a id="astructbt__hci__rp__mesh__advertise__cancel_html_afd121f3bb6d3453e7ec0bd9b895a3ccb"></a>
<a id="astructbt__hci__rp__mesh__advertise__timed_html"></a>
<a id="astructbt__hci__rp__mesh__advertise__timed_html_a15527bfd94e49f654b15fc188aa7c83a"></a>
<a id="astructbt__hci__rp__mesh__advertise__timed_html_a17b39cd87b8392ef1ac7d721a55f6fab"></a>
<a id="astructbt__hci__rp__mesh__advertise__timed_html_a84554f3b501a48373e9f58875e6a46be"></a>
<a id="astructbt__hci__rp__mesh__advertise_html"></a>
<a id="astructbt__hci__rp__mesh__advertise_html_a0b88358de3223b528cdd424db25f05a0"></a>
<a id="astructbt__hci__rp__mesh__advertise_html_a1514ae798eb501a0fcb02a48d222d62e"></a>
<a id="astructbt__hci__rp__mesh__advertise_html_aa5a8760133b1f1554797f91a9c4cd8e3"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html_a06de566ae223d750a4d367575ca2a8a0"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html_a1fbb06dca694411d58af86dee7a547fc"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html_a41b1c570c26ee911bd5f9b005492cb95"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html_a50276763a447e1942b28ef33401c3a54"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html_a5464a608f37c74f1d43e83d8877e405e"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html_a6bc6ec02023723b280cb643bd19a6178"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html_a9088d94213a80dfe7f3fb78188f24e05"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html_aa000cd8242e6122d11dae17c726cf15a"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html_abcc86aae5c91a0b551d6b7686c807349"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html_aeb49bfa06dc5b7200392c363ed6d67b0"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html_af2f158774100ab0ca1537e69b3918eaa"></a>
<a id="astructbt__hci__rp__mesh__get__opts_html_af607a95cd367be6950a3185c2df2aca8"></a>
<a id="astructbt__hci__rp__mesh__set__scan__filter_html"></a>
<a id="astructbt__hci__rp__mesh__set__scan__filter_html_a029223e5cfca25fc8b0565211734125e"></a>
<a id="astructbt__hci__rp__mesh__set__scan__filter_html_a2c832868fd092e235171a8e963c3eaf9"></a>
<a id="astructbt__hci__rp__mesh__set__scan__filter_html_afad78bfd78bb399cdeba73ccd10a66fe"></a>
<a id="astructbt__hci__rp__mesh__set__scanning_html"></a>
<a id="astructbt__hci__rp__mesh__set__scanning_html_a88bee72d8dfb306d5f52b40789c6e0f1"></a>
<a id="astructbt__hci__rp__mesh__set__scanning_html_afef848e9b6ad1e264d9e7ccc12391da6"></a>
<a id="astructbt__hci__rp__vs__read__build__info_html"></a>
<a id="astructbt__hci__rp__vs__read__build__info_html_aba2aaa3916221768412eed39cc85ab5f"></a>
<a id="astructbt__hci__rp__vs__read__build__info_html_acdebc0d6f8d713075c6e5e69cf136ea3"></a>
<a id="astructbt__hci__rp__vs__read__chip__temp_html"></a>
<a id="astructbt__hci__rp__vs__read__chip__temp_html_a2487c86e1975f69f307e70624abf9519"></a>
<a id="astructbt__hci__rp__vs__read__chip__temp_html_a324034b28a6526e195de576432f8ed32"></a>
<a id="astructbt__hci__rp__vs__read__host__stack__cmds_html"></a>
<a id="astructbt__hci__rp__vs__read__host__stack__cmds_html_a27b591f7784aaec063afc37105c00880"></a>
<a id="astructbt__hci__rp__vs__read__host__stack__cmds_html_a374e54391bcb72b5cde885cb04269e9a"></a>
<a id="astructbt__hci__rp__vs__read__host__stack__cmds_html_ac11d1ed48e49f9ce1d31709be76aed95"></a>
<a id="astructbt__hci__rp__vs__read__key__hierarchy__roots_html"></a>
<a id="astructbt__hci__rp__vs__read__key__hierarchy__roots_html_a3ab9afeea4cc59853ef5a2f04ee39405"></a>
<a id="astructbt__hci__rp__vs__read__key__hierarchy__roots_html_a5ce7b3ba72b129191d8a7d73f9978682"></a>
<a id="astructbt__hci__rp__vs__read__key__hierarchy__roots_html_a62c6df2ac691c06f481189fb61b0f99c"></a>
<a id="astructbt__hci__rp__vs__read__static__addrs_html"></a>
<a id="astructbt__hci__rp__vs__read__static__addrs_html_a482a0984602d4d59ef9572d4e1053a99"></a>
<a id="astructbt__hci__rp__vs__read__static__addrs_html_af3ddb349e82e7a5edcb86300c8d8a548"></a>
<a id="astructbt__hci__rp__vs__read__static__addrs_html_af8175d96852a67ebcfa4da5019e618e9"></a>
<a id="astructbt__hci__rp__vs__read__supported__commands_html"></a>
<a id="astructbt__hci__rp__vs__read__supported__commands_html_a699129590cb1f5a3418d8e0eab3868e4"></a>
<a id="astructbt__hci__rp__vs__read__supported__commands_html_afe9e5d1647b0cea192fa281367dc6c85"></a>
<a id="astructbt__hci__rp__vs__read__supported__features_html"></a>
<a id="astructbt__hci__rp__vs__read__supported__features_html_a0459b49e864d3069d4ba818ef2ed59ca"></a>
<a id="astructbt__hci__rp__vs__read__supported__features_html_a40468d71ba659d8ef593d82aca0bc583"></a>
<a id="astructbt__hci__rp__vs__read__tx__power__level_html"></a>
<a id="astructbt__hci__rp__vs__read__tx__power__level_html_a86f8e314571df0dfbc0995fb14108650"></a>
<a id="astructbt__hci__rp__vs__read__tx__power__level_html_ae1e1ee5319283a725c1eb1ab3ad13481"></a>
<a id="astructbt__hci__rp__vs__read__tx__power__level_html_ae2755a4ba68c73c5bb97f58400d8b16d"></a>
<a id="astructbt__hci__rp__vs__read__tx__power__level_html_ae5011313891d5ac4eaf0383e125bf786"></a>
<a id="astructbt__hci__rp__vs__read__usb__transport__mode_html"></a>
<a id="astructbt__hci__rp__vs__read__usb__transport__mode_html_a25070132401d9b3d3dcd3f325f66da64"></a>
<a id="astructbt__hci__rp__vs__read__usb__transport__mode_html_a7fdfe43b633c153fd9e7cf1f470b435f"></a>
<a id="astructbt__hci__rp__vs__read__usb__transport__mode_html_aec8f1c7acd972d00b8f1070ed444b155"></a>
<a id="astructbt__hci__rp__vs__read__version__info_html"></a>
<a id="astructbt__hci__rp__vs__read__version__info_html_a147b0b73db111465549196ed67ca60d6"></a>
<a id="astructbt__hci__rp__vs__read__version__info_html_a24ad5440e85d2e91c0495a3b06ac7469"></a>
<a id="astructbt__hci__rp__vs__read__version__info_html_a43fc428c7ea444be2100e970b444f51a"></a>
<a id="astructbt__hci__rp__vs__read__version__info_html_a47b4d799df9aeca67f6136264e13ef16"></a>
<a id="astructbt__hci__rp__vs__read__version__info_html_a7cdff04c26d2f5864a07fc0a7c31a89a"></a>
<a id="astructbt__hci__rp__vs__read__version__info_html_a7e69f89d5562205f780dc05128b5d46a"></a>
<a id="astructbt__hci__rp__vs__read__version__info_html_abd4ea8df7b338e48490ceafae1b8e6be"></a>
<a id="astructbt__hci__rp__vs__write__tx__power__level_html"></a>
<a id="astructbt__hci__rp__vs__write__tx__power__level_html_a0ba154d288f23fb5d859d620a9205a68"></a>
<a id="astructbt__hci__rp__vs__write__tx__power__level_html_a2d462d79165a3fbc98a3a24c6d6ad8fa"></a>
<a id="astructbt__hci__rp__vs__write__tx__power__level_html_a6a8c6103c609f2c05cfb46476e23d58e"></a>
<a id="astructbt__hci__rp__vs__write__tx__power__level_html_ac7c2eb75ec96f79d67c0a7b3ce851e14"></a>
<a id="astructbt__hci__vs__cmd_html"></a>
<a id="astructbt__hci__vs__cmd_html_a1ca54af74a178506b954fe8e43a04895"></a>
<a id="astructbt__hci__vs__cmd_html_a640c7523215b676dd8922d95c136cc4b"></a>
<a id="astructbt__hci__vs__fatal__error__cpu__data__cortex__m_html"></a>
<a id="astructbt__hci__vs__fatal__error__cpu__data__cortex__m_html_a5e288372cda1b5f3b9efa50fe0b11e9e"></a>
<a id="astructbt__hci__vs__fatal__error__cpu__data__cortex__m_html_a6cceefed2a7df499e8896ddccde37345"></a>
<a id="astructbt__hci__vs__fatal__error__cpu__data__cortex__m_html_a7800c9dfe98acaade644ba91029d66a9"></a>
<a id="astructbt__hci__vs__fatal__error__cpu__data__cortex__m_html_a7a440cf730c9c79e5fe7d74e5a06fc64"></a>
<a id="astructbt__hci__vs__fatal__error__cpu__data__cortex__m_html_a7e35f8040302ade2b8df6555599064a9"></a>
<a id="astructbt__hci__vs__fatal__error__cpu__data__cortex__m_html_a92fa1e12c760a72ada99be671ecff8f6"></a>
<a id="astructbt__hci__vs__fatal__error__cpu__data__cortex__m_html_ac376de594e6da67c443d462eecb76026"></a>
<a id="astructbt__hci__vs__fatal__error__cpu__data__cortex__m_html_ae5ca14da9c1964077c718b2d148c9375"></a>
<a id="astructbt__hci__vs__fatal__error__stack__frame_html"></a>
<a id="astructbt__hci__vs__fatal__error__stack__frame_html_a1530d501d5fd5dade63219e16ddd5d85"></a>
<a id="astructbt__hci__vs__fatal__error__stack__frame_html_a89e4ede59af9b37fcaeee00ea028f930"></a>
<a id="astructbt__hci__vs__fatal__error__stack__frame_html_ac2f93a05158d4c170848ee4afdfe1bd1"></a>
<a id="astructbt__hci__vs__static__addr_html"></a>
<a id="astructbt__hci__vs__static__addr_html_aa9b61e3f589465c68a4b6356c9de8b66"></a>
<a id="astructbt__hci__vs__static__addr_html_afef2fbf31b7d5101ee48e51476c81698"></a>
<a id="astructnet__buf_html"></a>

```c
/* hci_vs.h - Bluetooth Host Control Interface Vendor Specific definitions */

/*
 * Copyright (c) 2017-2018 Nordic Semiconductor ASA
 * Copyright (c) 2015-2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_HCI_VS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_HCI_VS_H_

#include <stdint.h>

#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/hci.h>
#include <zephyr/bluetooth/hci_types.h>
#include <zephyr/net_buf.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_VS_CMD_BIT_VERSION                       0
#define BT_VS_CMD_BIT_SUP_CMD                       1
#define BT_VS_CMD_BIT_SUP_FEAT                      2
#define BT_VS_CMD_BIT_SET_EVT_MASK                  3
#define BT_VS_CMD_BIT_RESET                         4
#define BT_VS_CMD_BIT_WRITE_BDADDR                  5
#define BT_VS_CMD_BIT_SET_TRACE_ENABLE              6
#define BT_VS_CMD_BIT_READ_BUILD_INFO               7
#define BT_VS_CMD_BIT_READ_STATIC_ADDRS             8
#define BT_VS_CMD_BIT_READ_KEY_ROOTS                9
#define BT_VS_CMD_BIT_READ_CHIP_TEMP               10
#define BT_VS_CMD_BIT_READ_HOST_STACK_CMD          11
#define BT_VS_CMD_BIT_SET_SCAN_REP_ENABLE          12
#define BT_VS_CMD_BIT_WRITE_TX_POWER               13
#define BT_VS_CMD_BIT_READ_TX_POWER                14

#define BT_VS_CMD_SUP_FEAT(cmd)                 BT_LE_FEAT_TEST(cmd, \
                                                BT_VS_CMD_BIT_SUP_FEAT)

#define BT_VS_CMD_WRITE_BD_ADDR(cmd)            BT_LE_FEAT_TEST(cmd, \
                                                BT_VS_CMD_BIT_WRITE_BDADDR)
#define BT_VS_CMD_READ_STATIC_ADDRS(cmd)        BT_LE_FEAT_TEST(cmd, \
                                                BT_VS_CMD_BIT_READ_STATIC_ADDRS)
#define BT_VS_CMD_READ_KEY_ROOTS(cmd)           BT_LE_FEAT_TEST(cmd, \
                                                BT_VS_CMD_BIT_READ_KEY_ROOTS)

#define BT_HCI_VS_HW_PLAT_INTEL                 0x0001
#define BT_HCI_VS_HW_PLAT_NORDIC                0x0002
#define BT_HCI_VS_HW_PLAT_NXP                   0x0003
#define BT_HCI_VS_HW_PLAT_ESPRESSIF             0x0004

#define BT_HCI_VS_HW_VAR_NORDIC_NRF51X          0x0001
#define BT_HCI_VS_HW_VAR_NORDIC_NRF52X          0x0002
#define BT_HCI_VS_HW_VAR_NORDIC_NRF53X          0x0003
#define BT_HCI_VS_HW_VAR_NORDIC_NRF54HX         0x0004
#define BT_HCI_VS_HW_VAR_NORDIC_NRF54LX         0x0005

#define BT_HCI_VS_HW_VAR_ESP32                  0x0001
#define BT_HCI_VS_HW_VAR_ESP32S3                0x0002
#define BT_HCI_VS_HW_VAR_ESP32C2                0x0003
#define BT_HCI_VS_HW_VAR_ESP32C3                0x0004
#define BT_HCI_VS_HW_VAR_ESP32C6                0x0005
#define BT_HCI_VS_HW_VAR_ESP32H2                0x0006
#define BT_HCI_VS_HW_VAR_ESP32C5                0x0007
#define BT_HCI_VS_HW_VAR_ESP32C61               0x0008

#define BT_HCI_VS_FW_VAR_STANDARD_CTLR          0x0000
#define BT_HCI_VS_FW_VAR_VS_CTLR                0x0001
#define BT_HCI_VS_FW_VAR_FW_LOADER              0x0002
#define BT_HCI_VS_FW_VAR_RESCUE_IMG             0x0003
#define BT_HCI_OP_VS_READ_VERSION_INFO          BT_OP(BT_OGF_VS, 0x0001)
struct bt_hci_rp_vs_read_version_info {
        uint8_t  status;
        uint16_t hw_platform;
        uint16_t hw_variant;
        uint8_t  fw_variant;
        uint8_t  fw_version;
        uint16_t fw_revision;
        uint32_t fw_build;
} __packed;

#define BT_HCI_OP_VS_READ_SUPPORTED_COMMANDS    BT_OP(BT_OGF_VS, 0x0002)
struct bt_hci_rp_vs_read_supported_commands {
        uint8_t  status;
        uint8_t  commands[64];
} __packed;

#define BT_HCI_OP_VS_READ_SUPPORTED_FEATURES    BT_OP(BT_OGF_VS, 0x0003)
struct bt_hci_rp_vs_read_supported_features {
        uint8_t  status;
        uint8_t  features[8];
} __packed;

#define BT_HCI_OP_VS_SET_EVENT_MASK             BT_OP(BT_OGF_VS, 0x0004)
struct bt_hci_cp_vs_set_event_mask {
        uint8_t  event_mask[8];
} __packed;

#define BT_HCI_VS_RESET_SOFT                    0x00
#define BT_HCI_VS_RESET_HARD                    0x01
#define BT_HCI_OP_VS_RESET                      BT_OP(BT_OGF_VS, 0x0005)
struct bt_hci_cp_vs_reset {
        uint8_t  type;
} __packed;

#define BT_HCI_OP_VS_WRITE_BD_ADDR              BT_OP(BT_OGF_VS, 0x0006)
struct bt_hci_cp_vs_write_bd_addr {
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_VS_TRACE_DISABLED                0x00
#define BT_HCI_VS_TRACE_ENABLED                 0x01

#define BT_HCI_VS_TRACE_HCI_EVTS                0x00
#define BT_HCI_VS_TRACE_VDC                     0x01
#define BT_HCI_OP_VS_SET_TRACE_ENABLE           BT_OP(BT_OGF_VS, 0x0007)
struct bt_hci_cp_vs_set_trace_enable {
        uint8_t  enable;
        uint8_t  type;
} __packed;

#define BT_HCI_OP_VS_READ_BUILD_INFO            BT_OP(BT_OGF_VS, 0x0008)
struct bt_hci_rp_vs_read_build_info {
        uint8_t  status;
        uint8_t  info[0];
} __packed;

struct bt_hci_vs_static_addr {
        bt_addr_t bdaddr;
        uint8_t      ir[16];
} __packed;

#define BT_HCI_OP_VS_READ_STATIC_ADDRS          BT_OP(BT_OGF_VS, 0x0009)
struct bt_hci_rp_vs_read_static_addrs {
        uint8_t   status;
        uint8_t   num_addrs;
        struct bt_hci_vs_static_addr a[0];
} __packed;

#define BT_HCI_OP_VS_READ_KEY_HIERARCHY_ROOTS   BT_OP(BT_OGF_VS, 0x000a)
struct bt_hci_rp_vs_read_key_hierarchy_roots {
        uint8_t  status;
        uint8_t  ir[16];
        uint8_t  er[16];
} __packed;

#define BT_HCI_OP_VS_READ_CHIP_TEMP             BT_OP(BT_OGF_VS, 0x000b)
struct bt_hci_rp_vs_read_chip_temp {
        uint8_t  status;
        int8_t  temps;
} __packed;

struct bt_hci_vs_cmd {
        uint16_t vendor_id;
        uint16_t opcode_base;
} __packed;

#define BT_HCI_VS_VID_ANDROID                   0x0001
#define BT_HCI_VS_VID_MICROSOFT                 0x0002
#define BT_HCI_OP_VS_READ_HOST_STACK_CMDS       BT_OP(BT_OGF_VS, 0x000c)
struct bt_hci_rp_vs_read_host_stack_cmds {
        uint8_t   status;
        uint8_t   num_cmds;
        struct bt_hci_vs_cmd c[0];
} __packed;

#define BT_HCI_VS_SCAN_REQ_REPORTS_DISABLED     0x00
#define BT_HCI_VS_SCAN_REQ_REPORTS_ENABLED      0x01
#define BT_HCI_OP_VS_SET_SCAN_REQ_REPORTS       BT_OP(BT_OGF_VS, 0x000d)
struct bt_hci_cp_vs_set_scan_req_reports {
        uint8_t  enable;
} __packed;

#define BT_HCI_VS_LL_HANDLE_TYPE_ADV       0x00
#define BT_HCI_VS_LL_HANDLE_TYPE_SCAN      0x01
#define BT_HCI_VS_LL_HANDLE_TYPE_CONN      0x02
#define BT_HCI_VS_LL_TX_POWER_LEVEL_NO_PREF     0x7F
#define BT_HCI_OP_VS_WRITE_TX_POWER_LEVEL       BT_OP(BT_OGF_VS, 0x000e)
struct bt_hci_cp_vs_write_tx_power_level {
        uint8_t  handle_type;
        uint16_t handle;
        int8_t  tx_power_level;
} __packed;

struct bt_hci_rp_vs_write_tx_power_level {
        uint8_t  status;
        uint8_t  handle_type;
        uint16_t handle;
        int8_t  selected_tx_power;
} __packed;

#define BT_HCI_OP_VS_READ_TX_POWER_LEVEL        BT_OP(BT_OGF_VS, 0x000f)
struct bt_hci_cp_vs_read_tx_power_level {
        uint8_t  handle_type;
        uint16_t handle;
} __packed;

struct bt_hci_rp_vs_read_tx_power_level {
        uint8_t  status;
        uint8_t  handle_type;
        uint16_t handle;
        int8_t  tx_power_level;
} __packed;

#define BT_HCI_OP_VS_READ_USB_TRANSPORT_MODE    BT_OP(BT_OGF_VS, 0x0010)

struct bt_hci_rp_vs_read_usb_transport_mode {
        uint8_t  status;
        uint8_t  num_supported_modes;
        uint8_t  supported_mode[0];
} __packed;

#define BT_HCI_VS_USB_H2_MODE                  0x00
#define BT_HCI_VS_USB_H4_MODE                  0x01

#define BT_HCI_OP_VS_SET_USB_TRANSPORT_MODE    BT_OP(BT_OGF_VS, 0x0011)

struct bt_hci_cp_vs_set_usb_transport_mode {
        uint8_t  mode;
} __packed;

#define BT_HCI_OP_VS_SET_MIN_NUM_USED_CHANS    BT_OP(BT_OGF_VS, 0x0012)

struct bt_hci_cp_vs_set_min_num_used_chans {
        uint16_t handle;
        uint8_t  phys;
        uint8_t  min_used_chans;
} __packed;

/* Events */

struct bt_hci_evt_vs {
        uint8_t  subevent;
} __packed;

#define BT_HCI_EVT_VS_ERROR_DATA_TYPE_STACK_FRAME   0x01
#define BT_HCI_EVT_VS_ERROR_DATA_TYPE_CTRL_ASSERT   0x02
#define BT_HCI_EVT_VS_ERROR_DATA_TYPE_TRACE         0x03
struct bt_hci_vs_fatal_error_cpu_data_cortex_m {
        uint32_t a1;
        uint32_t a2;
        uint32_t a3;
        uint32_t a4;
        uint32_t ip;
        uint32_t lr;
        uint32_t pc;
        uint32_t xpsr;
} __packed;

#define BT_HCI_EVT_VS_ERROR_CPU_TYPE_CORTEX_M  0x01
struct bt_hci_vs_fatal_error_stack_frame {
        uint32_t reason;
        uint8_t cpu_type;
        uint8_t cpu_data[0];
} __packed;

struct bt_hci_evt_vs_fatal_error_trace_data {
        uint64_t pc;
        uint8_t err_info[0];
} __packed;

struct bt_hci_evt_vs_fatal_error {
        uint8_t type;
        uint8_t data[0];
} __packed;

#define BT_HCI_VS_TRACE_LMP_TX                 0x01
#define BT_HCI_VS_TRACE_LMP_RX                 0x02
#define BT_HCI_VS_TRACE_LLCP_TX                0x03
#define BT_HCI_VS_TRACE_LLCP_RX                0x04
#define BT_HCI_VS_TRACE_LE_CONN_IND            0x05
#define BT_HCI_EVT_VS_TRACE_INFO               0x03
struct bt_hci_evt_vs_trace_info {
        uint8_t  type;
        uint8_t  data[0];
} __packed;

#define BT_HCI_EVT_VS_SCAN_REQ_RX              0x04
struct bt_hci_evt_vs_scan_req_rx {
        bt_addr_le_t addr;
        int8_t         rssi;
} __packed;

struct bt_hci_le_iq_sample16 {
        int16_t i;
        int16_t q;
} __packed;

#define BT_HCI_EVT_VS_LE_CONNECTIONLESS_IQ_REPORT 0x5
#define BT_HCI_VS_LE_CTE_REPORT_NO_VALID_SAMPLE   0x8000
struct bt_hci_evt_vs_le_connectionless_iq_report {
        uint16_t sync_handle;
        uint8_t chan_idx;
        int16_t rssi;
        uint8_t rssi_ant_id;
        uint8_t cte_type;
        uint8_t slot_durations;
        uint8_t packet_status;
        uint16_t per_evt_counter;
        uint8_t sample_count;
        struct bt_hci_le_iq_sample16 sample[0];
} __packed;

#define BT_HCI_EVT_VS_LE_CONNECTION_IQ_REPORT 0x6
struct bt_hci_evt_vs_le_connection_iq_report {
        uint16_t conn_handle;
        uint8_t rx_phy;
        uint8_t data_chan_idx;
        int16_t rssi;
        uint8_t rssi_ant_id;
        uint8_t cte_type;
        uint8_t slot_durations;
        uint8_t packet_status;
        uint16_t conn_evt_counter;
        uint8_t sample_count;
        struct bt_hci_le_iq_sample16 sample[0];
} __packed;

/* Event mask bits */

#define BT_EVT_MASK_VS_FATAL_ERROR             BT_EVT_BIT(1)
#define BT_EVT_MASK_VS_TRACE_INFO              BT_EVT_BIT(2)
#define BT_EVT_MASK_VS_SCAN_REQ_RX             BT_EVT_BIT(3)
#define BT_EVT_MASK_VS_LE_CONNECTIONLESS_IQ_REPORT BT_EVT_BIT(4)
#define BT_EVT_MASK_VS_LE_CONNECTION_IQ_REPORT     BT_EVT_BIT(5)

#define DEFAULT_VS_EVT_MASK                                                                        \
        BT_EVT_MASK_VS_FATAL_ERROR | BT_EVT_MASK_VS_TRACE_INFO | BT_EVT_MASK_VS_SCAN_REQ_RX |      \
                BT_EVT_MASK_VS_LE_CONNECTIONLESS_IQ_REPORT |                                       \
                BT_EVT_MASK_VS_LE_CONNECTION_IQ_REPORT

/* Mesh HCI commands */
#define BT_HCI_MESH_REVISION                   0x01

#define BT_HCI_OP_VS_MESH                      BT_OP(BT_OGF_VS, 0x0042)
#define BT_HCI_MESH_EVT_PREFIX                 0xF0

struct bt_hci_cp_mesh {
        uint8_t         opcode;
} __packed;

#define BT_HCI_OC_MESH_GET_OPTS                0x00
struct bt_hci_rp_mesh_get_opts {
        uint8_t      status;
        uint8_t      opcode;
        uint8_t      revision;
        uint8_t      ch_map;
        int8_t      min_tx_power;
        int8_t      max_tx_power;
        uint8_t      max_scan_filter;
        uint8_t      max_filter_pattern;
        uint8_t      max_adv_slot;
        uint8_t      max_tx_window;
        uint8_t      evt_prefix_len;
        uint8_t      evt_prefix;
} __packed;

#define BT_HCI_MESH_PATTERN_LEN_MAX            0x0f

#define BT_HCI_OC_MESH_SET_SCAN_FILTER         0x01
struct bt_hci_mesh_pattern {
        uint8_t pattern_len;
        uint8_t pattern[0];
} __packed;

struct bt_hci_cp_mesh_set_scan_filter {
        uint8_t      scan_filter;
        uint8_t      filter_dup;
        uint8_t      num_patterns;
        struct    bt_hci_mesh_pattern patterns[0];
} __packed;
struct bt_hci_rp_mesh_set_scan_filter {
        uint8_t      status;
        uint8_t      opcode;
        uint8_t      scan_filter;
} __packed;

#define BT_HCI_OC_MESH_ADVERTISE               0x02
struct bt_hci_cp_mesh_advertise {
        uint8_t      adv_slot;
        uint8_t      own_addr_type;
        bt_addr_t random_addr;
        uint8_t      ch_map;
        int8_t      tx_power;
        uint8_t      min_tx_delay;
        uint8_t      max_tx_delay;
        uint8_t      retx_count;
        uint8_t      retx_interval;
        uint8_t      scan_delay;
        uint16_t     scan_duration;
        uint8_t      scan_filter;
        uint8_t      data_len;
        uint8_t      data[31];
} __packed;
struct bt_hci_rp_mesh_advertise {
        uint8_t      status;
        uint8_t      opcode;
        uint8_t      adv_slot;
} __packed;

#define BT_HCI_OC_MESH_ADVERTISE_TIMED         0x03
struct bt_hci_cp_mesh_advertise_timed {
        uint8_t      adv_slot;
        uint8_t      own_addr_type;
        bt_addr_t random_addr;
        uint8_t      ch_map;
        int8_t      tx_power;
        uint8_t      retx_count;
        uint8_t      retx_interval;
        uint32_t     instant;
        uint16_t     tx_delay;
        uint16_t     tx_window;
        uint8_t      data_len;
        uint8_t      data[31];
} __packed;
struct bt_hci_rp_mesh_advertise_timed {
        uint8_t      status;
        uint8_t      opcode;
        uint8_t      adv_slot;
} __packed;

#define BT_HCI_OC_MESH_ADVERTISE_CANCEL        0x04
struct bt_hci_cp_mesh_advertise_cancel {
        uint8_t      adv_slot;
} __packed;
struct bt_hci_rp_mesh_advertise_cancel {
        uint8_t      status;
        uint8_t      opcode;
        uint8_t      adv_slot;
} __packed;

#define BT_HCI_OC_MESH_SET_SCANNING            0x05
struct bt_hci_cp_mesh_set_scanning {
        uint8_t      enable;
        uint8_t      ch_map;
        uint8_t      scan_filter;
} __packed;
struct bt_hci_rp_mesh_set_scanning {
        uint8_t      status;
        uint8_t      opcode;
} __packed;

/* Events */
struct bt_hci_evt_mesh {
        uint8_t  prefix;
        uint8_t  subevent;
} __packed;

#define BT_HCI_EVT_MESH_ADV_COMPLETE           0x00
struct bt_hci_evt_mesh_adv_complete {
        uint8_t         adv_slot;
} __packed;

#define BT_HCI_EVT_MESH_SCANNING_REPORT        0x01
struct bt_hci_evt_mesh_scan_report {
        bt_addr_le_t addr;
        uint8_t         chan;
        int8_t         rssi;
        uint32_t        instant;
        uint8_t         data_len;
        uint8_t         data[0];
} __packed;
struct bt_hci_evt_mesh_scanning_report {
        uint8_t num_reports;
        struct bt_hci_evt_mesh_scan_report reports[0];
} __packed;

struct net_buf *hci_vs_err_stack_frame(unsigned int reason, const struct arch_esf *esf);
struct net_buf *hci_vs_err_trace(const char *file, uint32_t line, uint64_t pc);
struct net_buf *hci_vs_err_assert(const char *file, uint32_t line);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_HCI_VS_H_ */
```

## 20.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`hci_vs.h`：蓝牙主机控制接口厂商特定定义（Bluetooth Host Control Interface Vendor Specific Definitions）。

### 注释 2：原第 3 行

版权（Copyright）：© 2017-2018 Nordic Semiconductor ASA。

版权（Copyright）：© 2015-2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 232 行

事件（Events）。

### 注释 4：原第 321 行

事件掩码位（Event Mask Bits）。

### 注释 5：原第 334 行

网状网络主机控制器接口命令（Mesh HCI Commands）。

### 注释 6：原第 445 行

事件（Events）。

### 注释 7：原第 478 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_HCI_VS_H_`。

## 20.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_runtime_reference/P017_zephyr__bluetooth__hci_vs.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [zephyr/bluetooth/hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_hci_rp_vs_read_version_info](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [status](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#a7cdff04c26d2f5864a07fc0a7c31a89a)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [hw_platform](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#a7e69f89d5562205f780dc05128b5d46a)
- [hw_variant](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#abd4ea8df7b338e48490ceafae1b8e6be)
- [fw_variant](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#a24ad5440e85d2e91c0495a3b06ac7469)
- [fw_version](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#a147b0b73db111465549196ed67ca60d6)
- [fw_revision](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#a47b4d799df9aeca67f6136264e13ef16)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [fw_build](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#a43fc428c7ea444be2100e970b444f51a)
- [bt_hci_rp_vs_read_supported_commands](../bluetooth_hci_model_reference/P428_bt_hci_rp_vs_read_supported_commands_结构体.md)
- [status](../bluetooth_hci_model_reference/P428_bt_hci_rp_vs_read_supported_commands_结构体.md#afe9e5d1647b0cea192fa281367dc6c85)
- [commands](../bluetooth_hci_model_reference/P428_bt_hci_rp_vs_read_supported_commands_结构体.md#a699129590cb1f5a3418d8e0eab3868e4)
- [bt_hci_rp_vs_read_supported_features](../bluetooth_hci_model_reference/P429_bt_hci_rp_vs_read_supported_features_结构体.md)
- [status](../bluetooth_hci_model_reference/P429_bt_hci_rp_vs_read_supported_features_结构体.md#a40468d71ba659d8ef593d82aca0bc583)
- [features](../bluetooth_hci_model_reference/P429_bt_hci_rp_vs_read_supported_features_结构体.md#a0459b49e864d3069d4ba818ef2ed59ca)
- [bt_hci_cp_vs_set_event_mask](../bluetooth_hci_model_reference/P177_bt_hci_cp_vs_set_event_mask_结构体.md)
- [event_mask](../bluetooth_hci_model_reference/P177_bt_hci_cp_vs_set_event_mask_结构体.md#ad5883adb065f04e923ff64093c78949a)
- [bt_hci_cp_vs_reset](../bluetooth_hci_model_reference/P176_bt_hci_cp_vs_reset_结构体.md)
- [type](../bluetooth_hci_model_reference/P176_bt_hci_cp_vs_reset_结构体.md#aa3a47f4d2a593a9c756893ec28e49a00)
- [bt_hci_cp_vs_write_bd_addr](../bluetooth_hci_model_reference/P182_bt_hci_cp_vs_write_bd_addr_结构体.md)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P182_bt_hci_cp_vs_write_bd_addr_结构体.md#af54e126fff610467dd730902893b6cd2)
- [bt_hci_cp_vs_set_trace_enable](../bluetooth_hci_model_reference/P180_bt_hci_cp_vs_set_trace_enable_结构体.md)
- [enable](../bluetooth_hci_model_reference/P180_bt_hci_cp_vs_set_trace_enable_结构体.md#a5676627500b6c5aff5986c53a0ba13a7)
- [type](../bluetooth_hci_model_reference/P180_bt_hci_cp_vs_set_trace_enable_结构体.md#a18c3c81f13599a12903b12e350703dc5)
- [bt_hci_rp_vs_read_build_info](../bluetooth_hci_model_reference/P423_bt_hci_rp_vs_read_build_info_结构体.md)
- [status](../bluetooth_hci_model_reference/P423_bt_hci_rp_vs_read_build_info_结构体.md#acdebc0d6f8d713075c6e5e69cf136ea3)
- [info](../bluetooth_hci_model_reference/P423_bt_hci_rp_vs_read_build_info_结构体.md#aba2aaa3916221768412eed39cc85ab5f)
- [bt_hci_vs_static_addr](../bluetooth_hci_model_reference/P449_bt_hci_vs_static_addr_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P449_bt_hci_vs_static_addr_结构体.md#aa9b61e3f589465c68a4b6356c9de8b66)
- [ir](../bluetooth_hci_model_reference/P449_bt_hci_vs_static_addr_结构体.md#afef2fbf31b7d5101ee48e51476c81698)
- [bt_hci_rp_vs_read_static_addrs](../bluetooth_hci_model_reference/P427_bt_hci_rp_vs_read_static_addrs_结构体.md)
- [status](../bluetooth_hci_model_reference/P427_bt_hci_rp_vs_read_static_addrs_结构体.md#af3ddb349e82e7a5edcb86300c8d8a548)
- [num_addrs](../bluetooth_hci_model_reference/P427_bt_hci_rp_vs_read_static_addrs_结构体.md#a482a0984602d4d59ef9572d4e1053a99)
- [a](../bluetooth_hci_model_reference/P427_bt_hci_rp_vs_read_static_addrs_结构体.md#af8175d96852a67ebcfa4da5019e618e9)
- [bt_hci_rp_vs_read_key_hierarchy_roots](../bluetooth_hci_model_reference/P426_bt_hci_rp_vs_read_key_hierarchy_roots_结构体.md)
- [status](../bluetooth_hci_model_reference/P426_bt_hci_rp_vs_read_key_hierarchy_roots_结构体.md#a3ab9afeea4cc59853ef5a2f04ee39405)
- [ir](../bluetooth_hci_model_reference/P426_bt_hci_rp_vs_read_key_hierarchy_roots_结构体.md#a5ce7b3ba72b129191d8a7d73f9978682)
- [er](../bluetooth_hci_model_reference/P426_bt_hci_rp_vs_read_key_hierarchy_roots_结构体.md#a62c6df2ac691c06f481189fb61b0f99c)
- [bt_hci_rp_vs_read_chip_temp](../bluetooth_hci_model_reference/P424_bt_hci_rp_vs_read_chip_temp_结构体.md)
- [status](../bluetooth_hci_model_reference/P424_bt_hci_rp_vs_read_chip_temp_结构体.md#a324034b28a6526e195de576432f8ed32)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [temps](../bluetooth_hci_model_reference/P424_bt_hci_rp_vs_read_chip_temp_结构体.md#a2487c86e1975f69f307e70624abf9519)
- [bt_hci_vs_cmd](../bluetooth_hci_model_reference/P442_bt_hci_vs_cmd_结构体.md)
- [vendor_id](../bluetooth_hci_model_reference/P442_bt_hci_vs_cmd_结构体.md#a640c7523215b676dd8922d95c136cc4b)
- [opcode_base](../bluetooth_hci_model_reference/P442_bt_hci_vs_cmd_结构体.md#a1ca54af74a178506b954fe8e43a04895)
- [bt_hci_rp_vs_read_host_stack_cmds](../bluetooth_hci_model_reference/P425_bt_hci_rp_vs_read_host_stack_cmds_结构体.md)
- [status](../bluetooth_hci_model_reference/P425_bt_hci_rp_vs_read_host_stack_cmds_结构体.md#a374e54391bcb72b5cde885cb04269e9a)
- [num_cmds](../bluetooth_hci_model_reference/P425_bt_hci_rp_vs_read_host_stack_cmds_结构体.md#ac11d1ed48e49f9ce1d31709be76aed95)
- [c](../bluetooth_hci_model_reference/P425_bt_hci_rp_vs_read_host_stack_cmds_结构体.md#a27b591f7784aaec063afc37105c00880)
- [bt_hci_cp_vs_set_scan_req_reports](../bluetooth_hci_model_reference/P179_bt_hci_cp_vs_set_scan_req_reports_结构体.md)
- [enable](../bluetooth_hci_model_reference/P179_bt_hci_cp_vs_set_scan_req_reports_结构体.md#ac99b6b1fee39a2330c6d0c214c737fd3)
- [bt_hci_cp_vs_write_tx_power_level](../bluetooth_hci_model_reference/P183_bt_hci_cp_vs_write_tx_power_level_结构体.md)
- [handle_type](../bluetooth_hci_model_reference/P183_bt_hci_cp_vs_write_tx_power_level_结构体.md#a27e1b402a9a1a8850f551a18651e914e)
- [handle](../bluetooth_hci_model_reference/P183_bt_hci_cp_vs_write_tx_power_level_结构体.md#adff511831f183e031d9c61781d337b9d)
- [tx_power_level](../bluetooth_hci_model_reference/P183_bt_hci_cp_vs_write_tx_power_level_结构体.md#abd7f6c92c1463ec35cfd552ffce50b53)
- [bt_hci_rp_vs_write_tx_power_level](../bluetooth_hci_model_reference/P433_bt_hci_rp_vs_write_tx_power_level_结构体.md)
- [status](../bluetooth_hci_model_reference/P433_bt_hci_rp_vs_write_tx_power_level_结构体.md#a2d462d79165a3fbc98a3a24c6d6ad8fa)
- [handle_type](../bluetooth_hci_model_reference/P433_bt_hci_rp_vs_write_tx_power_level_结构体.md#a0ba154d288f23fb5d859d620a9205a68)
- [handle](../bluetooth_hci_model_reference/P433_bt_hci_rp_vs_write_tx_power_level_结构体.md#ac7c2eb75ec96f79d67c0a7b3ce851e14)
- [selected_tx_power](../bluetooth_hci_model_reference/P433_bt_hci_rp_vs_write_tx_power_level_结构体.md#a6a8c6103c609f2c05cfb46476e23d58e)
- [bt_hci_cp_vs_read_tx_power_level](../bluetooth_hci_model_reference/P175_bt_hci_cp_vs_read_tx_power_level_结构体.md)
- [handle_type](../bluetooth_hci_model_reference/P175_bt_hci_cp_vs_read_tx_power_level_结构体.md#a776450ea2132fab77b9350ae46d3a1b5)
- [handle](../bluetooth_hci_model_reference/P175_bt_hci_cp_vs_read_tx_power_level_结构体.md#a2bb528f003b22b88eec0d7389c84034f)
- [bt_hci_rp_vs_read_tx_power_level](../bluetooth_hci_model_reference/P430_bt_hci_rp_vs_read_tx_power_level_结构体.md)
- [status](../bluetooth_hci_model_reference/P430_bt_hci_rp_vs_read_tx_power_level_结构体.md#ae5011313891d5ac4eaf0383e125bf786)
- [handle_type](../bluetooth_hci_model_reference/P430_bt_hci_rp_vs_read_tx_power_level_结构体.md#a86f8e314571df0dfbc0995fb14108650)
- [handle](../bluetooth_hci_model_reference/P430_bt_hci_rp_vs_read_tx_power_level_结构体.md#ae2755a4ba68c73c5bb97f58400d8b16d)
- [tx_power_level](../bluetooth_hci_model_reference/P430_bt_hci_rp_vs_read_tx_power_level_结构体.md#ae1e1ee5319283a725c1eb1ab3ad13481)
- [bt_hci_rp_vs_read_usb_transport_mode](../bluetooth_hci_model_reference/P431_bt_hci_rp_vs_read_usb_transport_mode_结构体.md)
- [status](../bluetooth_hci_model_reference/P431_bt_hci_rp_vs_read_usb_transport_mode_结构体.md#a7fdfe43b633c153fd9e7cf1f470b435f)
- [num_supported_modes](../bluetooth_hci_model_reference/P431_bt_hci_rp_vs_read_usb_transport_mode_结构体.md#a25070132401d9b3d3dcd3f325f66da64)
- [supported_mode](../bluetooth_hci_model_reference/P431_bt_hci_rp_vs_read_usb_transport_mode_结构体.md#aec8f1c7acd972d00b8f1070ed444b155)
- [bt_hci_cp_vs_set_usb_transport_mode](../bluetooth_hci_model_reference/P181_bt_hci_cp_vs_set_usb_transport_mode_结构体.md)
- [mode](../bluetooth_hci_model_reference/P181_bt_hci_cp_vs_set_usb_transport_mode_结构体.md#a651867bbfbc6ff642fbc294488259b4e)
- [bt_hci_cp_vs_set_min_num_used_chans](../bluetooth_hci_model_reference/P178_bt_hci_cp_vs_set_min_num_used_chans_结构体.md)
- [handle](../bluetooth_hci_model_reference/P178_bt_hci_cp_vs_set_min_num_used_chans_结构体.md#aae4d29392f389a20f9be86870defc954)
- [phys](../bluetooth_hci_model_reference/P178_bt_hci_cp_vs_set_min_num_used_chans_结构体.md#a8cfa13723348bb43c19ceaa56fad2b1c)
- [min_used_chans](../bluetooth_hci_model_reference/P178_bt_hci_cp_vs_set_min_num_used_chans_结构体.md#a68262baddf6b7d2d42d61ad4c2690567)
- [bt_hci_evt_vs](../bluetooth_hci_model_reference/P300_bt_hci_evt_vs_结构体.md)
- [subevent](../bluetooth_hci_model_reference/P300_bt_hci_evt_vs_结构体.md#aadf6dd6172922d32a4a40be003f09876)
- [bt_hci_vs_fatal_error_cpu_data_cortex_m](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md)
- [a1](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#a6cceefed2a7df499e8896ddccde37345)
- [a2](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#ae5ca14da9c1964077c718b2d148c9375)
- [a3](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#a7e35f8040302ade2b8df6555599064a9)
- [a4](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#ac376de594e6da67c443d462eecb76026)
- [ip](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#a5e288372cda1b5f3b9efa50fe0b11e9e)
- [lr](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#a7a440cf730c9c79e5fe7d74e5a06fc64)
- [pc](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#a7800c9dfe98acaade644ba91029d66a9)
- [xpsr](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#a92fa1e12c760a72ada99be671ecff8f6)
- [bt_hci_vs_fatal_error_stack_frame](../bluetooth_hci_model_reference/P448_bt_hci_vs_fatal_error_stack_frame_结构体.md)
- [reason](../bluetooth_hci_model_reference/P448_bt_hci_vs_fatal_error_stack_frame_结构体.md#ac2f93a05158d4c170848ee4afdfe1bd1)
- [cpu_type](../bluetooth_hci_model_reference/P448_bt_hci_vs_fatal_error_stack_frame_结构体.md#a1530d501d5fd5dade63219e16ddd5d85)
- [cpu_data](../bluetooth_hci_model_reference/P448_bt_hci_vs_fatal_error_stack_frame_结构体.md#a89e4ede59af9b37fcaeee00ea028f930)
- [bt_hci_evt_vs_fatal_error_trace_data](../bluetooth_hci_model_reference/P302_bt_hci_evt_vs_fatal_error_trace_data_结构体.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [pc](../bluetooth_hci_model_reference/P302_bt_hci_evt_vs_fatal_error_trace_data_结构体.md#a467d2de2a3b26ddef8c412957abfd820)
- [err_info](../bluetooth_hci_model_reference/P302_bt_hci_evt_vs_fatal_error_trace_data_结构体.md#ae1efc729b0c079fa922dcfffab6cdfa6)
- [bt_hci_evt_vs_fatal_error](../bluetooth_hci_model_reference/P301_bt_hci_evt_vs_fatal_error_结构体.md)
- [type](../bluetooth_hci_model_reference/P301_bt_hci_evt_vs_fatal_error_结构体.md#a15e84185f74e84e1f9ccd83dc4fa2798)
- [data](../bluetooth_hci_model_reference/P301_bt_hci_evt_vs_fatal_error_结构体.md#aefd553e85eedb6e205da39916c5553aa)
- [bt_hci_evt_vs_trace_info](../bluetooth_hci_model_reference/P306_bt_hci_evt_vs_trace_info_结构体.md)
- [type](../bluetooth_hci_model_reference/P306_bt_hci_evt_vs_trace_info_结构体.md#af563e07c5364df229eb767e545c8aaa2)
- [data](../bluetooth_hci_model_reference/P306_bt_hci_evt_vs_trace_info_结构体.md#ae524df8cc722cda0fa86127a6b8e56da)
- [bt_hci_evt_vs_scan_req_rx](../bluetooth_hci_model_reference/P305_bt_hci_evt_vs_scan_req_rx_结构体.md)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [addr](../bluetooth_hci_model_reference/P305_bt_hci_evt_vs_scan_req_rx_结构体.md#a56613220a50bc50a771f432b7e617d5b)
- [rssi](../bluetooth_hci_model_reference/P305_bt_hci_evt_vs_scan_req_rx_结构体.md#acbfa7ec0a3ab1f94f53598a9d8242aba)
- [bt_hci_le_iq_sample16](../bluetooth_hci_model_reference/P324_bt_hci_le_iq_sample16_结构体.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [i](../bluetooth_hci_model_reference/P324_bt_hci_le_iq_sample16_结构体.md#ace47fd665d57f7ad7eb0a04ec8e54a47)
- [q](../bluetooth_hci_model_reference/P324_bt_hci_le_iq_sample16_结构体.md#aa317d2a9f451eeecb35ff05044ea6dc3)
- [bt_hci_evt_vs_le_connectionless_iq_report](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md)
- [sync_handle](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#a9c199121ac475d635fc51289e8eba979)
- [chan_idx](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#ad15beccc7c2207565678ebef72346158)
- [rssi](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#a9b7eb8a5cf363c3aec96b49853056dc7)
- [rssi_ant_id](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#a5fcd776dce904763c5cc6fab9a1373f4)
- [cte_type](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#a808a2a134104c69073af253a3c4dd1bd)
- [slot_durations](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#ac0b077d7b5e2b7c5ce61b3060913cad5)
- [packet_status](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#af5b27c1504ce4ff8afe23c28a9ac423f)
- [per_evt_counter](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#ab6911af90d85c565615c437715d9c7eb)
- [sample_count](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#a2698510deb6bd8943bf57104f96673db)
- [sample](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#a17c9d19883c9d8e34f300fbff614b475)
- [bt_hci_evt_vs_le_connection_iq_report](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md)
- [conn_handle](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#a941d0e025334a0c041cc7a59b69f0af3)
- [rx_phy](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#a959c7e2b910aec90f8b186550cb7f4d8)
- [data_chan_idx](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#af634fa464d4ca435ea935ae58db86cfa)
- [rssi](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#a87d4a6ebd1cc172816f3fe786c22f058)
- [rssi_ant_id](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#a55a290121f661f155684d37fa0df77d2)
- [cte_type](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#ad714bb1f2292764eba9c506bcc72bccd)
- [slot_durations](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#a71227b896453143a6a4ad11b7e985a16)
- [packet_status](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#aa2a9c3589bf8e152627a79c17102ec7c)
- [conn_evt_counter](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#aaa29121a6b7fc8f9a76e6b83f6b80f4d)
- [sample_count](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#ab96606229994abe966f03c65d57e5568)
- [sample](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#abb2b6e915f8de6ad2013a79d0b4ee288)
- [bt_hci_cp_mesh](../bluetooth_hci_model_reference/P141_bt_hci_cp_mesh_结构体.md)
- [opcode](../bluetooth_hci_model_reference/P141_bt_hci_cp_mesh_结构体.md#af29f0e2fd21f226143e0908c43c72a0f)
- [bt_hci_rp_mesh_get_opts](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md)
- [status](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a6bc6ec02023723b280cb643bd19a6178)
- [opcode](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a50276763a447e1942b28ef33401c3a54)
- [revision](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#abcc86aae5c91a0b551d6b7686c807349)
- [ch_map](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a06de566ae223d750a4d367575ca2a8a0)
- [min_tx_power](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#aa000cd8242e6122d11dae17c726cf15a)
- [max_tx_power](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#aeb49bfa06dc5b7200392c363ed6d67b0)
- [max_scan_filter](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a9088d94213a80dfe7f3fb78188f24e05)
- [max_filter_pattern](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a41b1c570c26ee911bd5f9b005492cb95)
- [max_adv_slot](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a1fbb06dca694411d58af86dee7a547fc)
- [max_tx_window](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a5464a608f37c74f1d43e83d8877e405e)
- [evt_prefix_len](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#af607a95cd367be6950a3185c2df2aca8)
- [evt_prefix](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#af2f158774100ab0ca1537e69b3918eaa)
- [bt_hci_mesh_pattern](../bluetooth_hci_model_reference/P327_bt_hci_mesh_pattern_结构体.md)
- [pattern_len](../bluetooth_hci_model_reference/P327_bt_hci_mesh_pattern_结构体.md#a2ab9eac21c74a03416007f5b7d0f5bc4)
- [pattern](../bluetooth_hci_model_reference/P327_bt_hci_mesh_pattern_结构体.md#a78e52a2890db71c501885f575bc80de4)
- [bt_hci_cp_mesh_set_scan_filter](../bluetooth_hci_model_reference/P145_bt_hci_cp_mesh_set_scan_filter_结构体.md)
- [scan_filter](../bluetooth_hci_model_reference/P145_bt_hci_cp_mesh_set_scan_filter_结构体.md#aa1e74c7f4dc39cf2ad0c130bf8dafa72)
- [filter_dup](../bluetooth_hci_model_reference/P145_bt_hci_cp_mesh_set_scan_filter_结构体.md#a41737323ab5723ce781f77f5752915e3)
- [num_patterns](../bluetooth_hci_model_reference/P145_bt_hci_cp_mesh_set_scan_filter_结构体.md#a3f99242946f3a5a8322a8333d9c58b30)
- [patterns](../bluetooth_hci_model_reference/P145_bt_hci_cp_mesh_set_scan_filter_结构体.md#a4e72bcfac1beec704d860034abcf22c0)
- [bt_hci_rp_mesh_set_scan_filter](../bluetooth_hci_model_reference/P397_bt_hci_rp_mesh_set_scan_filter_结构体.md)
- [status](../bluetooth_hci_model_reference/P397_bt_hci_rp_mesh_set_scan_filter_结构体.md#a2c832868fd092e235171a8e963c3eaf9)
- [opcode](../bluetooth_hci_model_reference/P397_bt_hci_rp_mesh_set_scan_filter_结构体.md#a029223e5cfca25fc8b0565211734125e)
- [scan_filter](../bluetooth_hci_model_reference/P397_bt_hci_rp_mesh_set_scan_filter_结构体.md#afad78bfd78bb399cdeba73ccd10a66fe)
- [bt_hci_cp_mesh_advertise](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md)
- [adv_slot](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a7ec17216955ac784cd213b11038c3521)
- [own_addr_type](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a6b6248069fa1e7eaf6825c52e38c3e78)
- [random_addr](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a0b22a8e1109db932f86bb7312dfeca9e)
- [ch_map](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a9ed6d2b96d9aa417ccd996e650bb00fa)
- [tx_power](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#af1482ed0255e35d7a2016017dab8713a)
- [min_tx_delay](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a6ac4b4dad0ce54e69afd2b8e1f6cdf4f)
- [max_tx_delay](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a3cf773db54448d5f7b3da652a798c712)
- [retx_count](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a5ea37039c817d58d13feb98d5658cbf1)
- [retx_interval](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a46242ef61b79723e5136373fa534a292)
- [scan_delay](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a278c21295c73947d7b0971a6ac043d62)
- [scan_duration](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#ab1b873984143301808f23824074e4df8)
- [scan_filter](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a0b190fcabae8555e65a251b37ab5b232)
- [data_len](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a67aef4d217cb6b5762b4f823c8f234df)
- [data](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#ad2af78fa8d14f1334b52f659f3497b4e)
- [bt_hci_rp_mesh_advertise](../bluetooth_hci_model_reference/P393_bt_hci_rp_mesh_advertise_结构体.md)
- [status](../bluetooth_hci_model_reference/P393_bt_hci_rp_mesh_advertise_结构体.md#a1514ae798eb501a0fcb02a48d222d62e)
- [opcode](../bluetooth_hci_model_reference/P393_bt_hci_rp_mesh_advertise_结构体.md#aa5a8760133b1f1554797f91a9c4cd8e3)
- [adv_slot](../bluetooth_hci_model_reference/P393_bt_hci_rp_mesh_advertise_结构体.md#a0b88358de3223b528cdd424db25f05a0)
- [bt_hci_cp_mesh_advertise_timed](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md)
- [adv_slot](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#a92f0163ec0854296ab76e49741d45196)
- [own_addr_type](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#ae395b4a53ff9e7af8885b9583562022a)
- [random_addr](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#ada4348480db5f95acaad86bfa2ddbc7e)
- [ch_map](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#aa5bf4322faa354cc6de0c707502b4ed0)
- [tx_power](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#aae34dd11723383b5559dc102c59213c2)
- [retx_count](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#adfb3acf9ea540d8405c5979115053b15)
- [retx_interval](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#a6718fd6031b2351eb033333a7302a21b)
- [instant](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#a85a7e965b8004cac3a4bc0107844c69b)
- [tx_delay](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#aee05619f0ed3b79f3bce5676c1f3aa8a)
- [tx_window](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#a1a5a5964eeff05fa232543756d234759)
- [data_len](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#a78ecf7aa6ebf0739a585fed2a8710301)
- [data](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#ac097c1ee537d9a480ae16205eafc7105)
- [bt_hci_rp_mesh_advertise_timed](../bluetooth_hci_model_reference/P395_bt_hci_rp_mesh_advertise_timed_结构体.md)
- [status](../bluetooth_hci_model_reference/P395_bt_hci_rp_mesh_advertise_timed_结构体.md#a84554f3b501a48373e9f58875e6a46be)
- [opcode](../bluetooth_hci_model_reference/P395_bt_hci_rp_mesh_advertise_timed_结构体.md#a15527bfd94e49f654b15fc188aa7c83a)
- [adv_slot](../bluetooth_hci_model_reference/P395_bt_hci_rp_mesh_advertise_timed_结构体.md#a17b39cd87b8392ef1ac7d721a55f6fab)
- [bt_hci_cp_mesh_advertise_cancel](../bluetooth_hci_model_reference/P143_bt_hci_cp_mesh_advertise_cancel_结构体.md)
- [adv_slot](../bluetooth_hci_model_reference/P143_bt_hci_cp_mesh_advertise_cancel_结构体.md#acd1409f2299c6bbddffd62d5e10e6e7c)
- [bt_hci_rp_mesh_advertise_cancel](../bluetooth_hci_model_reference/P394_bt_hci_rp_mesh_advertise_cancel_结构体.md)
- [status](../bluetooth_hci_model_reference/P394_bt_hci_rp_mesh_advertise_cancel_结构体.md#ac8a13ab9c91a88859803dcf9f80658af)
- [opcode](../bluetooth_hci_model_reference/P394_bt_hci_rp_mesh_advertise_cancel_结构体.md#abcc6cd11403b34f04ff4e128628d7484)
- [adv_slot](../bluetooth_hci_model_reference/P394_bt_hci_rp_mesh_advertise_cancel_结构体.md#afd121f3bb6d3453e7ec0bd9b895a3ccb)
- [bt_hci_cp_mesh_set_scanning](../bluetooth_hci_model_reference/P146_bt_hci_cp_mesh_set_scanning_结构体.md)
- [enable](../bluetooth_hci_model_reference/P146_bt_hci_cp_mesh_set_scanning_结构体.md#aed23ad3e51e459bbc86945576a8113ef)
- [ch_map](../bluetooth_hci_model_reference/P146_bt_hci_cp_mesh_set_scanning_结构体.md#a2b27e80def9b437c16de186d5371e140)
- [scan_filter](../bluetooth_hci_model_reference/P146_bt_hci_cp_mesh_set_scanning_结构体.md#ac7cf268f484a575268fc6aa0f1b44cce)
- [bt_hci_rp_mesh_set_scanning](../bluetooth_hci_model_reference/P398_bt_hci_rp_mesh_set_scanning_结构体.md)
- [status](../bluetooth_hci_model_reference/P398_bt_hci_rp_mesh_set_scanning_结构体.md#afef848e9b6ad1e264d9e7ccc12391da6)
- [opcode](../bluetooth_hci_model_reference/P398_bt_hci_rp_mesh_set_scanning_结构体.md#a88bee72d8dfb306d5f52b40789c6e0f1)
- [bt_hci_evt_mesh](../bluetooth_hci_model_reference/P283_bt_hci_evt_mesh_结构体.md)
- [prefix](../bluetooth_hci_model_reference/P283_bt_hci_evt_mesh_结构体.md#aaa8104b855bba787c69851ae7872a03e)
- [subevent](../bluetooth_hci_model_reference/P283_bt_hci_evt_mesh_结构体.md#ac0186d74e355c90c866dda51605b85ac)
- [bt_hci_evt_mesh_adv_complete](../bluetooth_hci_model_reference/P284_bt_hci_evt_mesh_adv_complete_结构体.md)
- [adv_slot](../bluetooth_hci_model_reference/P284_bt_hci_evt_mesh_adv_complete_结构体.md#a2c9240a7fa61dad2c7a29b1ad4e555b1)
- [bt_hci_evt_mesh_scan_report](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md)
- [addr](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md#a20d5ffe0df68bee1205a5ee1a5abd6b2)
- [chan](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md#a3d283dd74c33b01fffb42bd4560c6e47)
- [rssi](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md#af8fb2e61dfe3a3860bf68af0ee8626e6)
- [instant](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md#aa62526739d11d0fa2614e0822f3d70a7)
- [data_len](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md#a281d2c97835fb2f42c6fb322a26d8899)
- [data](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md#a573ad980305fb7c10b731a1867c97d1b)
- [bt_hci_evt_mesh_scanning_report](../bluetooth_hci_model_reference/P286_bt_hci_evt_mesh_scanning_report_结构体.md)
- [num_reports](../bluetooth_hci_model_reference/P286_bt_hci_evt_mesh_scanning_report_结构体.md#a5daf719f2f5ec6e47f7a93d47d5c2b17)
- [reports](../bluetooth_hci_model_reference/P286_bt_hci_evt_mesh_scanning_report_结构体.md#aa63b838e431b358bf1a3495998dfd952)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [hci_vs_err_stack_frame](../api_file_runtime_reference/P017_zephyr__bluetooth__hci_vs.h_文件参考.md#aa90c2106bbb977f1ea8532212ff01b4d)
- [hci_vs_err_trace](../api_file_runtime_reference/P017_zephyr__bluetooth__hci_vs.h_文件参考.md#a9a91c493cc947492d5a172a15abe9a4e)
- [hci_vs_err_assert](../api_file_runtime_reference/P017_zephyr__bluetooth__hci_vs.h_文件参考.md#afc9ea0e4f2260bf59336f2c66532d9b1)
- [addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_hci_cp_mesh_advertise_cancel::adv_slot](../bluetooth_hci_model_reference/P143_bt_hci_cp_mesh_advertise_cancel_结构体.md#acd1409f2299c6bbddffd62d5e10e6e7c)
- [bt_hci_cp_mesh_advertise_timed::tx_window](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#a1a5a5964eeff05fa232543756d234759)
- [bt_hci_cp_mesh_advertise_timed::retx_interval](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#a6718fd6031b2351eb033333a7302a21b)
- [bt_hci_cp_mesh_advertise_timed::data_len](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#a78ecf7aa6ebf0739a585fed2a8710301)
- [bt_hci_cp_mesh_advertise_timed::instant](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#a85a7e965b8004cac3a4bc0107844c69b)
- [bt_hci_cp_mesh_advertise_timed::adv_slot](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#a92f0163ec0854296ab76e49741d45196)
- [bt_hci_cp_mesh_advertise_timed::ch_map](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#aa5bf4322faa354cc6de0c707502b4ed0)
- [bt_hci_cp_mesh_advertise_timed::tx_power](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#aae34dd11723383b5559dc102c59213c2)
- [bt_hci_cp_mesh_advertise_timed::data](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#ac097c1ee537d9a480ae16205eafc7105)
- [bt_hci_cp_mesh_advertise_timed::random_addr](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#ada4348480db5f95acaad86bfa2ddbc7e)
- [bt_hci_cp_mesh_advertise_timed::retx_count](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#adfb3acf9ea540d8405c5979115053b15)
- [bt_hci_cp_mesh_advertise_timed::own_addr_type](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#ae395b4a53ff9e7af8885b9583562022a)
- [bt_hci_cp_mesh_advertise_timed::tx_delay](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md#aee05619f0ed3b79f3bce5676c1f3aa8a)
- [bt_hci_cp_mesh_advertise::scan_filter](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a0b190fcabae8555e65a251b37ab5b232)
- [bt_hci_cp_mesh_advertise::random_addr](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a0b22a8e1109db932f86bb7312dfeca9e)
- [bt_hci_cp_mesh_advertise::scan_delay](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a278c21295c73947d7b0971a6ac043d62)
- [bt_hci_cp_mesh_advertise::max_tx_delay](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a3cf773db54448d5f7b3da652a798c712)
- [bt_hci_cp_mesh_advertise::retx_interval](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a46242ef61b79723e5136373fa534a292)
- [bt_hci_cp_mesh_advertise::retx_count](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a5ea37039c817d58d13feb98d5658cbf1)
- [bt_hci_cp_mesh_advertise::data_len](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a67aef4d217cb6b5762b4f823c8f234df)
- [bt_hci_cp_mesh_advertise::min_tx_delay](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a6ac4b4dad0ce54e69afd2b8e1f6cdf4f)
- [bt_hci_cp_mesh_advertise::own_addr_type](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a6b6248069fa1e7eaf6825c52e38c3e78)
- [bt_hci_cp_mesh_advertise::adv_slot](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a7ec17216955ac784cd213b11038c3521)
- [bt_hci_cp_mesh_advertise::ch_map](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#a9ed6d2b96d9aa417ccd996e650bb00fa)
- [bt_hci_cp_mesh_advertise::scan_duration](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#ab1b873984143301808f23824074e4df8)
- [bt_hci_cp_mesh_advertise::data](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#ad2af78fa8d14f1334b52f659f3497b4e)
- [bt_hci_cp_mesh_advertise::tx_power](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md#af1482ed0255e35d7a2016017dab8713a)
- [bt_hci_cp_mesh_set_scan_filter::num_patterns](../bluetooth_hci_model_reference/P145_bt_hci_cp_mesh_set_scan_filter_结构体.md#a3f99242946f3a5a8322a8333d9c58b30)
- [bt_hci_cp_mesh_set_scan_filter::filter_dup](../bluetooth_hci_model_reference/P145_bt_hci_cp_mesh_set_scan_filter_结构体.md#a41737323ab5723ce781f77f5752915e3)
- [bt_hci_cp_mesh_set_scan_filter::patterns](../bluetooth_hci_model_reference/P145_bt_hci_cp_mesh_set_scan_filter_结构体.md#a4e72bcfac1beec704d860034abcf22c0)
- [bt_hci_cp_mesh_set_scan_filter::scan_filter](../bluetooth_hci_model_reference/P145_bt_hci_cp_mesh_set_scan_filter_结构体.md#aa1e74c7f4dc39cf2ad0c130bf8dafa72)
- [bt_hci_cp_mesh_set_scanning::ch_map](../bluetooth_hci_model_reference/P146_bt_hci_cp_mesh_set_scanning_结构体.md#a2b27e80def9b437c16de186d5371e140)
- [bt_hci_cp_mesh_set_scanning::scan_filter](../bluetooth_hci_model_reference/P146_bt_hci_cp_mesh_set_scanning_结构体.md#ac7cf268f484a575268fc6aa0f1b44cce)
- [bt_hci_cp_mesh_set_scanning::enable](../bluetooth_hci_model_reference/P146_bt_hci_cp_mesh_set_scanning_结构体.md#aed23ad3e51e459bbc86945576a8113ef)
- [bt_hci_cp_mesh::opcode](../bluetooth_hci_model_reference/P141_bt_hci_cp_mesh_结构体.md#af29f0e2fd21f226143e0908c43c72a0f)
- [bt_hci_cp_vs_read_tx_power_level::handle](../bluetooth_hci_model_reference/P175_bt_hci_cp_vs_read_tx_power_level_结构体.md#a2bb528f003b22b88eec0d7389c84034f)
- [bt_hci_cp_vs_read_tx_power_level::handle_type](../bluetooth_hci_model_reference/P175_bt_hci_cp_vs_read_tx_power_level_结构体.md#a776450ea2132fab77b9350ae46d3a1b5)
- [bt_hci_cp_vs_reset::type](../bluetooth_hci_model_reference/P176_bt_hci_cp_vs_reset_结构体.md#aa3a47f4d2a593a9c756893ec28e49a00)
- [bt_hci_cp_vs_set_event_mask::event_mask](../bluetooth_hci_model_reference/P177_bt_hci_cp_vs_set_event_mask_结构体.md#ad5883adb065f04e923ff64093c78949a)
- [bt_hci_cp_vs_set_min_num_used_chans::min_used_chans](../bluetooth_hci_model_reference/P178_bt_hci_cp_vs_set_min_num_used_chans_结构体.md#a68262baddf6b7d2d42d61ad4c2690567)
- [bt_hci_cp_vs_set_min_num_used_chans::phys](../bluetooth_hci_model_reference/P178_bt_hci_cp_vs_set_min_num_used_chans_结构体.md#a8cfa13723348bb43c19ceaa56fad2b1c)
- [bt_hci_cp_vs_set_min_num_used_chans::handle](../bluetooth_hci_model_reference/P178_bt_hci_cp_vs_set_min_num_used_chans_结构体.md#aae4d29392f389a20f9be86870defc954)
- [bt_hci_cp_vs_set_scan_req_reports::enable](../bluetooth_hci_model_reference/P179_bt_hci_cp_vs_set_scan_req_reports_结构体.md#ac99b6b1fee39a2330c6d0c214c737fd3)
- [bt_hci_cp_vs_set_trace_enable::type](../bluetooth_hci_model_reference/P180_bt_hci_cp_vs_set_trace_enable_结构体.md#a18c3c81f13599a12903b12e350703dc5)
- [bt_hci_cp_vs_set_trace_enable::enable](../bluetooth_hci_model_reference/P180_bt_hci_cp_vs_set_trace_enable_结构体.md#a5676627500b6c5aff5986c53a0ba13a7)
- [bt_hci_cp_vs_set_usb_transport_mode::mode](../bluetooth_hci_model_reference/P181_bt_hci_cp_vs_set_usb_transport_mode_结构体.md#a651867bbfbc6ff642fbc294488259b4e)
- [bt_hci_cp_vs_write_bd_addr::bdaddr](../bluetooth_hci_model_reference/P182_bt_hci_cp_vs_write_bd_addr_结构体.md#af54e126fff610467dd730902893b6cd2)
- [bt_hci_cp_vs_write_tx_power_level::handle_type](../bluetooth_hci_model_reference/P183_bt_hci_cp_vs_write_tx_power_level_结构体.md#a27e1b402a9a1a8850f551a18651e914e)
- [bt_hci_cp_vs_write_tx_power_level::tx_power_level](../bluetooth_hci_model_reference/P183_bt_hci_cp_vs_write_tx_power_level_结构体.md#abd7f6c92c1463ec35cfd552ffce50b53)
- [bt_hci_cp_vs_write_tx_power_level::handle](../bluetooth_hci_model_reference/P183_bt_hci_cp_vs_write_tx_power_level_结构体.md#adff511831f183e031d9c61781d337b9d)
- [bt_hci_evt_mesh_adv_complete::adv_slot](../bluetooth_hci_model_reference/P284_bt_hci_evt_mesh_adv_complete_结构体.md#a2c9240a7fa61dad2c7a29b1ad4e555b1)
- [bt_hci_evt_mesh_scan_report::addr](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md#a20d5ffe0df68bee1205a5ee1a5abd6b2)
- [bt_hci_evt_mesh_scan_report::data_len](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md#a281d2c97835fb2f42c6fb322a26d8899)
- [bt_hci_evt_mesh_scan_report::chan](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md#a3d283dd74c33b01fffb42bd4560c6e47)
- [bt_hci_evt_mesh_scan_report::data](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md#a573ad980305fb7c10b731a1867c97d1b)
- [bt_hci_evt_mesh_scan_report::instant](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md#aa62526739d11d0fa2614e0822f3d70a7)
- [bt_hci_evt_mesh_scan_report::rssi](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md#af8fb2e61dfe3a3860bf68af0ee8626e6)
- [bt_hci_evt_mesh_scanning_report::num_reports](../bluetooth_hci_model_reference/P286_bt_hci_evt_mesh_scanning_report_结构体.md#a5daf719f2f5ec6e47f7a93d47d5c2b17)
- [bt_hci_evt_mesh_scanning_report::reports](../bluetooth_hci_model_reference/P286_bt_hci_evt_mesh_scanning_report_结构体.md#aa63b838e431b358bf1a3495998dfd952)
- [bt_hci_evt_mesh::prefix](../bluetooth_hci_model_reference/P283_bt_hci_evt_mesh_结构体.md#aaa8104b855bba787c69851ae7872a03e)
- [bt_hci_evt_mesh::subevent](../bluetooth_hci_model_reference/P283_bt_hci_evt_mesh_结构体.md#ac0186d74e355c90c866dda51605b85ac)
- [bt_hci_evt_vs_fatal_error_trace_data::pc](../bluetooth_hci_model_reference/P302_bt_hci_evt_vs_fatal_error_trace_data_结构体.md#a467d2de2a3b26ddef8c412957abfd820)
- [bt_hci_evt_vs_fatal_error_trace_data::err_info](../bluetooth_hci_model_reference/P302_bt_hci_evt_vs_fatal_error_trace_data_结构体.md#ae1efc729b0c079fa922dcfffab6cdfa6)
- [bt_hci_evt_vs_fatal_error::type](../bluetooth_hci_model_reference/P301_bt_hci_evt_vs_fatal_error_结构体.md#a15e84185f74e84e1f9ccd83dc4fa2798)
- [bt_hci_evt_vs_fatal_error::data](../bluetooth_hci_model_reference/P301_bt_hci_evt_vs_fatal_error_结构体.md#aefd553e85eedb6e205da39916c5553aa)
- [bt_hci_evt_vs_le_connection_iq_report::rssi_ant_id](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#a55a290121f661f155684d37fa0df77d2)
- [bt_hci_evt_vs_le_connection_iq_report::slot_durations](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#a71227b896453143a6a4ad11b7e985a16)
- [bt_hci_evt_vs_le_connection_iq_report::rssi](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#a87d4a6ebd1cc172816f3fe786c22f058)
- [bt_hci_evt_vs_le_connection_iq_report::conn_handle](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#a941d0e025334a0c041cc7a59b69f0af3)
- [bt_hci_evt_vs_le_connection_iq_report::rx_phy](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#a959c7e2b910aec90f8b186550cb7f4d8)
- [bt_hci_evt_vs_le_connection_iq_report::packet_status](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#aa2a9c3589bf8e152627a79c17102ec7c)
- [bt_hci_evt_vs_le_connection_iq_report::conn_evt_counter](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#aaa29121a6b7fc8f9a76e6b83f6b80f4d)
- [bt_hci_evt_vs_le_connection_iq_report::sample_count](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#ab96606229994abe966f03c65d57e5568)
- [bt_hci_evt_vs_le_connection_iq_report::sample](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#abb2b6e915f8de6ad2013a79d0b4ee288)
- [bt_hci_evt_vs_le_connection_iq_report::cte_type](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#ad714bb1f2292764eba9c506bcc72bccd)
- [bt_hci_evt_vs_le_connection_iq_report::data_chan_idx](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md#af634fa464d4ca435ea935ae58db86cfa)
- [bt_hci_evt_vs_le_connectionless_iq_report::sample](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#a17c9d19883c9d8e34f300fbff614b475)
- [bt_hci_evt_vs_le_connectionless_iq_report::sample_count](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#a2698510deb6bd8943bf57104f96673db)
- [bt_hci_evt_vs_le_connectionless_iq_report::rssi_ant_id](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#a5fcd776dce904763c5cc6fab9a1373f4)
- [bt_hci_evt_vs_le_connectionless_iq_report::cte_type](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#a808a2a134104c69073af253a3c4dd1bd)
- [bt_hci_evt_vs_le_connectionless_iq_report::rssi](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#a9b7eb8a5cf363c3aec96b49853056dc7)
- [bt_hci_evt_vs_le_connectionless_iq_report::sync_handle](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#a9c199121ac475d635fc51289e8eba979)
- [bt_hci_evt_vs_le_connectionless_iq_report::per_evt_counter](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#ab6911af90d85c565615c437715d9c7eb)
- [bt_hci_evt_vs_le_connectionless_iq_report::slot_durations](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#ac0b077d7b5e2b7c5ce61b3060913cad5)
- [bt_hci_evt_vs_le_connectionless_iq_report::chan_idx](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#ad15beccc7c2207565678ebef72346158)
- [bt_hci_evt_vs_le_connectionless_iq_report::packet_status](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md#af5b27c1504ce4ff8afe23c28a9ac423f)
- [bt_hci_evt_vs_scan_req_rx::addr](../bluetooth_hci_model_reference/P305_bt_hci_evt_vs_scan_req_rx_结构体.md#a56613220a50bc50a771f432b7e617d5b)
- [bt_hci_evt_vs_scan_req_rx::rssi](../bluetooth_hci_model_reference/P305_bt_hci_evt_vs_scan_req_rx_结构体.md#acbfa7ec0a3ab1f94f53598a9d8242aba)
- [bt_hci_evt_vs_trace_info::data](../bluetooth_hci_model_reference/P306_bt_hci_evt_vs_trace_info_结构体.md#ae524df8cc722cda0fa86127a6b8e56da)
- [bt_hci_evt_vs_trace_info::type](../bluetooth_hci_model_reference/P306_bt_hci_evt_vs_trace_info_结构体.md#af563e07c5364df229eb767e545c8aaa2)
- [bt_hci_evt_vs::subevent](../bluetooth_hci_model_reference/P300_bt_hci_evt_vs_结构体.md#aadf6dd6172922d32a4a40be003f09876)
- [bt_hci_le_iq_sample16::q](../bluetooth_hci_model_reference/P324_bt_hci_le_iq_sample16_结构体.md#aa317d2a9f451eeecb35ff05044ea6dc3)
- [bt_hci_le_iq_sample16::i](../bluetooth_hci_model_reference/P324_bt_hci_le_iq_sample16_结构体.md#ace47fd665d57f7ad7eb0a04ec8e54a47)
- [bt_hci_mesh_pattern::pattern_len](../bluetooth_hci_model_reference/P327_bt_hci_mesh_pattern_结构体.md#a2ab9eac21c74a03416007f5b7d0f5bc4)
- [bt_hci_mesh_pattern::pattern](../bluetooth_hci_model_reference/P327_bt_hci_mesh_pattern_结构体.md#a78e52a2890db71c501885f575bc80de4)
- [bt_hci_rp_mesh_advertise_cancel::opcode](../bluetooth_hci_model_reference/P394_bt_hci_rp_mesh_advertise_cancel_结构体.md#abcc6cd11403b34f04ff4e128628d7484)
- [bt_hci_rp_mesh_advertise_cancel::status](../bluetooth_hci_model_reference/P394_bt_hci_rp_mesh_advertise_cancel_结构体.md#ac8a13ab9c91a88859803dcf9f80658af)
- [bt_hci_rp_mesh_advertise_cancel::adv_slot](../bluetooth_hci_model_reference/P394_bt_hci_rp_mesh_advertise_cancel_结构体.md#afd121f3bb6d3453e7ec0bd9b895a3ccb)
- [bt_hci_rp_mesh_advertise_timed::opcode](../bluetooth_hci_model_reference/P395_bt_hci_rp_mesh_advertise_timed_结构体.md#a15527bfd94e49f654b15fc188aa7c83a)
- [bt_hci_rp_mesh_advertise_timed::adv_slot](../bluetooth_hci_model_reference/P395_bt_hci_rp_mesh_advertise_timed_结构体.md#a17b39cd87b8392ef1ac7d721a55f6fab)
- [bt_hci_rp_mesh_advertise_timed::status](../bluetooth_hci_model_reference/P395_bt_hci_rp_mesh_advertise_timed_结构体.md#a84554f3b501a48373e9f58875e6a46be)
- [bt_hci_rp_mesh_advertise::adv_slot](../bluetooth_hci_model_reference/P393_bt_hci_rp_mesh_advertise_结构体.md#a0b88358de3223b528cdd424db25f05a0)
- [bt_hci_rp_mesh_advertise::status](../bluetooth_hci_model_reference/P393_bt_hci_rp_mesh_advertise_结构体.md#a1514ae798eb501a0fcb02a48d222d62e)
- [bt_hci_rp_mesh_advertise::opcode](../bluetooth_hci_model_reference/P393_bt_hci_rp_mesh_advertise_结构体.md#aa5a8760133b1f1554797f91a9c4cd8e3)
- [bt_hci_rp_mesh_get_opts::ch_map](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a06de566ae223d750a4d367575ca2a8a0)
- [bt_hci_rp_mesh_get_opts::max_adv_slot](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a1fbb06dca694411d58af86dee7a547fc)
- [bt_hci_rp_mesh_get_opts::max_filter_pattern](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a41b1c570c26ee911bd5f9b005492cb95)
- [bt_hci_rp_mesh_get_opts::opcode](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a50276763a447e1942b28ef33401c3a54)
- [bt_hci_rp_mesh_get_opts::max_tx_window](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a5464a608f37c74f1d43e83d8877e405e)
- [bt_hci_rp_mesh_get_opts::status](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a6bc6ec02023723b280cb643bd19a6178)
- [bt_hci_rp_mesh_get_opts::max_scan_filter](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#a9088d94213a80dfe7f3fb78188f24e05)
- [bt_hci_rp_mesh_get_opts::min_tx_power](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#aa000cd8242e6122d11dae17c726cf15a)
- [bt_hci_rp_mesh_get_opts::revision](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#abcc86aae5c91a0b551d6b7686c807349)
- [bt_hci_rp_mesh_get_opts::max_tx_power](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#aeb49bfa06dc5b7200392c363ed6d67b0)
- [bt_hci_rp_mesh_get_opts::evt_prefix](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#af2f158774100ab0ca1537e69b3918eaa)
- [bt_hci_rp_mesh_get_opts::evt_prefix_len](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md#af607a95cd367be6950a3185c2df2aca8)
- [bt_hci_rp_mesh_set_scan_filter::opcode](../bluetooth_hci_model_reference/P397_bt_hci_rp_mesh_set_scan_filter_结构体.md#a029223e5cfca25fc8b0565211734125e)
- [bt_hci_rp_mesh_set_scan_filter::status](../bluetooth_hci_model_reference/P397_bt_hci_rp_mesh_set_scan_filter_结构体.md#a2c832868fd092e235171a8e963c3eaf9)
- [bt_hci_rp_mesh_set_scan_filter::scan_filter](../bluetooth_hci_model_reference/P397_bt_hci_rp_mesh_set_scan_filter_结构体.md#afad78bfd78bb399cdeba73ccd10a66fe)
- [bt_hci_rp_mesh_set_scanning::opcode](../bluetooth_hci_model_reference/P398_bt_hci_rp_mesh_set_scanning_结构体.md#a88bee72d8dfb306d5f52b40789c6e0f1)
- [bt_hci_rp_mesh_set_scanning::status](../bluetooth_hci_model_reference/P398_bt_hci_rp_mesh_set_scanning_结构体.md#afef848e9b6ad1e264d9e7ccc12391da6)
- [bt_hci_rp_vs_read_build_info::info](../bluetooth_hci_model_reference/P423_bt_hci_rp_vs_read_build_info_结构体.md#aba2aaa3916221768412eed39cc85ab5f)
- [bt_hci_rp_vs_read_build_info::status](../bluetooth_hci_model_reference/P423_bt_hci_rp_vs_read_build_info_结构体.md#acdebc0d6f8d713075c6e5e69cf136ea3)
- [bt_hci_rp_vs_read_chip_temp::temps](../bluetooth_hci_model_reference/P424_bt_hci_rp_vs_read_chip_temp_结构体.md#a2487c86e1975f69f307e70624abf9519)
- [bt_hci_rp_vs_read_chip_temp::status](../bluetooth_hci_model_reference/P424_bt_hci_rp_vs_read_chip_temp_结构体.md#a324034b28a6526e195de576432f8ed32)
- [bt_hci_rp_vs_read_host_stack_cmds::c](../bluetooth_hci_model_reference/P425_bt_hci_rp_vs_read_host_stack_cmds_结构体.md#a27b591f7784aaec063afc37105c00880)
- [bt_hci_rp_vs_read_host_stack_cmds::status](../bluetooth_hci_model_reference/P425_bt_hci_rp_vs_read_host_stack_cmds_结构体.md#a374e54391bcb72b5cde885cb04269e9a)
- [bt_hci_rp_vs_read_host_stack_cmds::num_cmds](../bluetooth_hci_model_reference/P425_bt_hci_rp_vs_read_host_stack_cmds_结构体.md#ac11d1ed48e49f9ce1d31709be76aed95)
- [bt_hci_rp_vs_read_key_hierarchy_roots::status](../bluetooth_hci_model_reference/P426_bt_hci_rp_vs_read_key_hierarchy_roots_结构体.md#a3ab9afeea4cc59853ef5a2f04ee39405)
- [bt_hci_rp_vs_read_key_hierarchy_roots::ir](../bluetooth_hci_model_reference/P426_bt_hci_rp_vs_read_key_hierarchy_roots_结构体.md#a5ce7b3ba72b129191d8a7d73f9978682)
- [bt_hci_rp_vs_read_key_hierarchy_roots::er](../bluetooth_hci_model_reference/P426_bt_hci_rp_vs_read_key_hierarchy_roots_结构体.md#a62c6df2ac691c06f481189fb61b0f99c)
- [bt_hci_rp_vs_read_static_addrs::num_addrs](../bluetooth_hci_model_reference/P427_bt_hci_rp_vs_read_static_addrs_结构体.md#a482a0984602d4d59ef9572d4e1053a99)
- [bt_hci_rp_vs_read_static_addrs::status](../bluetooth_hci_model_reference/P427_bt_hci_rp_vs_read_static_addrs_结构体.md#af3ddb349e82e7a5edcb86300c8d8a548)
- [bt_hci_rp_vs_read_static_addrs::a](../bluetooth_hci_model_reference/P427_bt_hci_rp_vs_read_static_addrs_结构体.md#af8175d96852a67ebcfa4da5019e618e9)
- [bt_hci_rp_vs_read_supported_commands::commands](../bluetooth_hci_model_reference/P428_bt_hci_rp_vs_read_supported_commands_结构体.md#a699129590cb1f5a3418d8e0eab3868e4)
- [bt_hci_rp_vs_read_supported_commands::status](../bluetooth_hci_model_reference/P428_bt_hci_rp_vs_read_supported_commands_结构体.md#afe9e5d1647b0cea192fa281367dc6c85)
- [bt_hci_rp_vs_read_supported_features::features](../bluetooth_hci_model_reference/P429_bt_hci_rp_vs_read_supported_features_结构体.md#a0459b49e864d3069d4ba818ef2ed59ca)
- [bt_hci_rp_vs_read_supported_features::status](../bluetooth_hci_model_reference/P429_bt_hci_rp_vs_read_supported_features_结构体.md#a40468d71ba659d8ef593d82aca0bc583)
- [bt_hci_rp_vs_read_tx_power_level::handle_type](../bluetooth_hci_model_reference/P430_bt_hci_rp_vs_read_tx_power_level_结构体.md#a86f8e314571df0dfbc0995fb14108650)
- [bt_hci_rp_vs_read_tx_power_level::tx_power_level](../bluetooth_hci_model_reference/P430_bt_hci_rp_vs_read_tx_power_level_结构体.md#ae1e1ee5319283a725c1eb1ab3ad13481)
- [bt_hci_rp_vs_read_tx_power_level::handle](../bluetooth_hci_model_reference/P430_bt_hci_rp_vs_read_tx_power_level_结构体.md#ae2755a4ba68c73c5bb97f58400d8b16d)
- [bt_hci_rp_vs_read_tx_power_level::status](../bluetooth_hci_model_reference/P430_bt_hci_rp_vs_read_tx_power_level_结构体.md#ae5011313891d5ac4eaf0383e125bf786)
- [bt_hci_rp_vs_read_usb_transport_mode::num_supported_modes](../bluetooth_hci_model_reference/P431_bt_hci_rp_vs_read_usb_transport_mode_结构体.md#a25070132401d9b3d3dcd3f325f66da64)
- [bt_hci_rp_vs_read_usb_transport_mode::status](../bluetooth_hci_model_reference/P431_bt_hci_rp_vs_read_usb_transport_mode_结构体.md#a7fdfe43b633c153fd9e7cf1f470b435f)
- [bt_hci_rp_vs_read_usb_transport_mode::supported_mode](../bluetooth_hci_model_reference/P431_bt_hci_rp_vs_read_usb_transport_mode_结构体.md#aec8f1c7acd972d00b8f1070ed444b155)
- [bt_hci_rp_vs_read_version_info::fw_version](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#a147b0b73db111465549196ed67ca60d6)
- [bt_hci_rp_vs_read_version_info::fw_variant](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#a24ad5440e85d2e91c0495a3b06ac7469)
- [bt_hci_rp_vs_read_version_info::fw_build](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#a43fc428c7ea444be2100e970b444f51a)
- [bt_hci_rp_vs_read_version_info::fw_revision](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#a47b4d799df9aeca67f6136264e13ef16)
- [bt_hci_rp_vs_read_version_info::status](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#a7cdff04c26d2f5864a07fc0a7c31a89a)
- [bt_hci_rp_vs_read_version_info::hw_platform](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#a7e69f89d5562205f780dc05128b5d46a)
- [bt_hci_rp_vs_read_version_info::hw_variant](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md#abd4ea8df7b338e48490ceafae1b8e6be)
- [bt_hci_rp_vs_write_tx_power_level::handle_type](../bluetooth_hci_model_reference/P433_bt_hci_rp_vs_write_tx_power_level_结构体.md#a0ba154d288f23fb5d859d620a9205a68)
- [bt_hci_rp_vs_write_tx_power_level::status](../bluetooth_hci_model_reference/P433_bt_hci_rp_vs_write_tx_power_level_结构体.md#a2d462d79165a3fbc98a3a24c6d6ad8fa)
- [bt_hci_rp_vs_write_tx_power_level::selected_tx_power](../bluetooth_hci_model_reference/P433_bt_hci_rp_vs_write_tx_power_level_结构体.md#a6a8c6103c609f2c05cfb46476e23d58e)
- [bt_hci_rp_vs_write_tx_power_level::handle](../bluetooth_hci_model_reference/P433_bt_hci_rp_vs_write_tx_power_level_结构体.md#ac7c2eb75ec96f79d67c0a7b3ce851e14)
- [bt_hci_vs_cmd::opcode_base](../bluetooth_hci_model_reference/P442_bt_hci_vs_cmd_结构体.md#a1ca54af74a178506b954fe8e43a04895)
- [bt_hci_vs_cmd::vendor_id](../bluetooth_hci_model_reference/P442_bt_hci_vs_cmd_结构体.md#a640c7523215b676dd8922d95c136cc4b)
- [bt_hci_vs_fatal_error_cpu_data_cortex_m::ip](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#a5e288372cda1b5f3b9efa50fe0b11e9e)
- [bt_hci_vs_fatal_error_cpu_data_cortex_m::a1](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#a6cceefed2a7df499e8896ddccde37345)
- [bt_hci_vs_fatal_error_cpu_data_cortex_m::pc](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#a7800c9dfe98acaade644ba91029d66a9)
- [bt_hci_vs_fatal_error_cpu_data_cortex_m::lr](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#a7a440cf730c9c79e5fe7d74e5a06fc64)
- [bt_hci_vs_fatal_error_cpu_data_cortex_m::a3](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#a7e35f8040302ade2b8df6555599064a9)
- [bt_hci_vs_fatal_error_cpu_data_cortex_m::xpsr](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#a92fa1e12c760a72ada99be671ecff8f6)
- [bt_hci_vs_fatal_error_cpu_data_cortex_m::a4](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#ac376de594e6da67c443d462eecb76026)
- [bt_hci_vs_fatal_error_cpu_data_cortex_m::a2](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md#ae5ca14da9c1964077c718b2d148c9375)
- [bt_hci_vs_fatal_error_stack_frame::cpu_type](../bluetooth_hci_model_reference/P448_bt_hci_vs_fatal_error_stack_frame_结构体.md#a1530d501d5fd5dade63219e16ddd5d85)
- [bt_hci_vs_fatal_error_stack_frame::cpu_data](../bluetooth_hci_model_reference/P448_bt_hci_vs_fatal_error_stack_frame_结构体.md#a89e4ede59af9b37fcaeee00ea028f930)
- [bt_hci_vs_fatal_error_stack_frame::reason](../bluetooth_hci_model_reference/P448_bt_hci_vs_fatal_error_stack_frame_结构体.md#ac2f93a05158d4c170848ee4afdfe1bd1)
- [bt_hci_vs_static_addr::bdaddr](../bluetooth_hci_model_reference/P449_bt_hci_vs_static_addr_结构体.md#aa9b61e3f589465c68a4b6356c9de8b66)
- [bt_hci_vs_static_addr::ir](../bluetooth_hci_model_reference/P449_bt_hci_vs_static_addr_结构体.md#afef2fbf31b7d5101ee48e51476c81698)

---

[上一章](P019_gptp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P021_irq_multilevel.h_源码浏览.md)
