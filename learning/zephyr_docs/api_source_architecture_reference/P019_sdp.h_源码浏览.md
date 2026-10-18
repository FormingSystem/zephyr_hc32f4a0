---
id: learning.zephyr-docs.api-source-architecture-reference.page-19
title: sdp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_sdp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h.html)。

## 19.1\_原始可见代码（Source Code）

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
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
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
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00268"></a>
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
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="foldopen00338"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="foldopen00346"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="foldopen00352"></a>
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
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="foldopen00403"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="foldopen00411"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="foldopen00421"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="foldopen00440"></a>
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
<a id="l00470"></a>
<a id="foldopen00480"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="foldopen00492"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="foldopen00505"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="foldopen00518"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="foldopen00531"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="foldopen00544"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="foldopen00557"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="foldopen00599"></a>
<a id="l00599"></a>
<a id="l00601"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00648"></a>
<a id="l00650"></a>
<a id="l00652"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="foldopen00666"></a>
<a id="l00666"></a>
<a id="l00668"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="foldopen00674"></a>
<a id="l00674"></a>
<a id="l00682"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="foldopen00688"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00692"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="l00697"></a>
<a id="l00699"></a>
<a id="l00701"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00851"></a>
<a id="l00852"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="foldopen00916"></a>
<a id="l00916"></a>
<a id="l00918"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="l00922"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="foldopen00935"></a>
<a id="l00935"></a>
<a id="l00937"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00948"></a>
<a id="foldopen00953"></a>
<a id="l00953"></a>
<a id="l00955"></a>
<a id="l00957"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="foldopen00964"></a>
<a id="l00964"></a>
<a id="l00966"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="l00970"></a>
<a id="foldopen00976"></a>
<a id="l00976"></a>
<a id="l00977"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="l00984"></a>
<a id="foldopen00992"></a>
<a id="l00992"></a>
<a id="l00994"></a>
<a id="l00996"></a>
<a id="l00998"></a>
<a id="l01000"></a>
<a id="l01002"></a>
<a id="l01004"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="l01009"></a>
<a id="foldopen01021"></a>
<a id="l01021"></a>
<a id="l01023"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01058"></a>
<a id="l01059"></a>
<a id="l01073"></a>
<a id="l01074"></a>
<a id="l01075"></a>
<a id="l01091"></a>
<a id="l01092"></a>
<a id="l01093"></a>
<a id="l01094"></a>
<a id="l01106"></a>
<a id="l01107"></a>
<a id="l01126"></a>
<a id="l01127"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01132"></a>
<a id="l01136"></a>
<a id="l01137"></a>
<a id="abluetooth_2uuid_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__sdp_html_ga07ca5d4f383d74004478cfd6ead2b80a"></a>
<a id="agroup__bt__sdp_html_ga0ce1314e052881eec5a43f571857960e"></a>
<a id="agroup__bt__sdp_html_ga2cb42ca8e487071682c37124ab56f2ab"></a>
<a id="agroup__bt__sdp_html_ga2d1040ccd11d1dd4c697525ebc323243"></a>
<a id="agroup__bt__sdp_html_ga2eb0646597a44e0e3cb0234d2c12a2d7"></a>
<a id="agroup__bt__sdp_html_ga3bad45ab578c0277a320ac241692f799"></a>
<a id="agroup__bt__sdp_html_ga44658df825a40f820a31e7adb4240d25"></a>
<a id="agroup__bt__sdp_html_ga5e4a45b7b860d82a111480c9f25c2666"></a>
<a id="agroup__bt__sdp_html_ga6006e3cd593ef793273fb291913790fa"></a>
<a id="agroup__bt__sdp_html_ga71809908bb73150258b2a5ab3c2f8517"></a>
<a id="agroup__bt__sdp_html_ga71e7d75850becf4ead62668c8e7bebbc"></a>
<a id="agroup__bt__sdp_html_ga9a815c6efe976f29e9f6f35a566245fd"></a>
<a id="agroup__bt__sdp_html_ga9df34b18af051782377229a18e6d3887"></a>
<a id="agroup__bt__sdp_html_ga9e7d4bd0a407fe8254410f907db90f00"></a>
<a id="agroup__bt__sdp_html_gaa104046a9e6e15f05961bf8652ecec16"></a>
<a id="agroup__bt__sdp_html_gab7d3e8bc83efff28cf9118710b5486fc"></a>
<a id="agroup__bt__sdp_html_gaba31a2327e4bba56ef2ac831b166e66a"></a>
<a id="agroup__bt__sdp_html_gac395eff18a4d2af3d955e276bf13963a"></a>
<a id="agroup__bt__sdp_html_gacf20a00d84e6eed2c128284fe9c52024"></a>
<a id="agroup__bt__sdp_html_gad672a89277b276d1b702fe07302c468e"></a>
<a id="agroup__bt__sdp_html_gae1c3110dfe24a939cc02d998c4699ca7"></a>
<a id="agroup__bt__sdp_html_gaed089d52f57cb25d2b02b2adbc60a36a"></a>
<a id="agroup__bt__sdp_html_gaf69723cff6dce7e86f0f0240ec3e2041"></a>
<a id="agroup__bt__sdp_html_gaf754bbfd9cdc0e6a2bf7d6c46fab3f29"></a>
<a id="agroup__bt__sdp_html_gga278df12ff5def68ca4663defd178582ca94e15ea86b69d65ca9c1947d1e2157ef"></a>
<a id="agroup__bt__sdp_html_gga278df12ff5def68ca4663defd178582ca990fbea48866b2acb7ccd67391b19636"></a>
<a id="agroup__bt__sdp_html_gga5e4a45b7b860d82a111480c9f25c2666a154bbb29fb26d007838c87def4cd34f8"></a>
<a id="agroup__bt__sdp_html_gga5e4a45b7b860d82a111480c9f25c2666a27eccef21d812956c6ae7ff9194e20e4"></a>
<a id="agroup__bt__sdp_html_gga5e4a45b7b860d82a111480c9f25c2666a5917deef84a7af5d5f908d4058732b1e"></a>
<a id="agroup__bt__sdp_html_gga5e4a45b7b860d82a111480c9f25c2666a5af87613192cda6a05fa280d2df8574b"></a>
<a id="agroup__bt__sdp_html_gga5e4a45b7b860d82a111480c9f25c2666a80b8652e39dae70c61443adf4f29fb4d"></a>
<a id="agroup__bt__sdp_html_gga5e4a45b7b860d82a111480c9f25c2666acaf932b38a1e17ca9e85c055096fa1da"></a>
<a id="agroup__bt__sdp_html_gga88019838cb3e5317fce93f4933583d94a5b8c3260e5aaaa08e86a099ccfeee41f"></a>
<a id="agroup__bt__sdp_html_gga88019838cb3e5317fce93f4933583d94a64fff103816cfc0215b9b3909786fa4e"></a>
<a id="agroup__bt__sdp_html_gga88019838cb3e5317fce93f4933583d94a9ce8c93cf1754fc7047951e891f66ff2"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__sdp__attr__value__int_html"></a>
<a id="astructbt__sdp__attr__value__int_html_a12c991cdf87a2d48d1c5b3d5cb639ead"></a>
<a id="astructbt__sdp__attr__value__int_html_a282cf4821d1ba734df65e447687bb8ec"></a>
<a id="astructbt__sdp__attr__value__int_html_a4dd9e9eae0d95dcc3af855d711ead35e"></a>
<a id="astructbt__sdp__attr__value__int_html_a9fe2006da0ce55441dcffd4080ac287a"></a>
<a id="astructbt__sdp__attr__value__int_html_ad114c103a0d2248cffdf5a0a458e8c57"></a>
<a id="astructbt__sdp__attr__value__int_html_ae2eeaa2eaf83b7923ea5f6d743d480b7"></a>
<a id="astructbt__sdp__attr__value__pair_html"></a>
<a id="astructbt__sdp__attr__value__pair_html_a505490ce660a6c15b2b59efaa5fb6057"></a>
<a id="astructbt__sdp__attr__value__pair_html_a533ee8ab9d9dec24faf52c2dc016bb1d"></a>
<a id="astructbt__sdp__attr__value__text_html"></a>
<a id="astructbt__sdp__attr__value__text_html_a440091666ca041db641c709ed172ba2d"></a>
<a id="astructbt__sdp__attr__value__text_html_a89161e7cfe2185b16b2e114b85209621"></a>
<a id="astructbt__sdp__attr__value__uint_html"></a>
<a id="astructbt__sdp__attr__value__uint_html_a4752a1517d75c13454db83f095b5da4f"></a>
<a id="astructbt__sdp__attr__value__uint_html_a5741e3d3c00c8dc8085d496692d1114c"></a>
<a id="astructbt__sdp__attr__value__uint_html_a7b609be27cad4508d2713b169d8bd4b5"></a>
<a id="astructbt__sdp__attr__value__uint_html_a7dae539fd3f8232842fe4a1bebca1824"></a>
<a id="astructbt__sdp__attr__value__uint_html_ae0a02d6f23b160c98022f58b9c38ab37"></a>
<a id="astructbt__sdp__attr__value__uint_html_af88e041745b2e69ac207afc5e4d369c1"></a>
<a id="astructbt__sdp__attr__value__url_html"></a>
<a id="astructbt__sdp__attr__value__url_html_a7ff5d8b06952b873f6b5c60129fa346f"></a>
<a id="astructbt__sdp__attr__value__url_html_aed7f8929167df11bb0db2249fc5957d9"></a>
<a id="astructbt__sdp__attr__value_html"></a>
<a id="astructbt__sdp__attr__value_html_a2fc1e977a5b82f16b160c898cca1cff7"></a>
<a id="astructbt__sdp__attr__value_html_a36fe39424a1f3ed59c2f7addf6a3eb8a"></a>
<a id="astructbt__sdp__attr__value_html_a7a1c4a780d8712fbf16df75f8ebae05f"></a>
<a id="astructbt__sdp__attr__value_html_ae5b6d1e373b37e2627b34e6da549098f"></a>
<a id="astructbt__sdp__attr__value_html_af1582544193e9598183d8bf6ea722dbc"></a>
<a id="astructbt__sdp__attr__value_html_af6e3f74c2c405153654fcade2608eca0"></a>
<a id="astructbt__sdp__attribute__id__list_html"></a>
<a id="astructbt__sdp__attribute__id__list_html_a3f0c472e904dd86bf95f8623b1d04d73"></a>
<a id="astructbt__sdp__attribute__id__list_html_af38e30a77ad8b0a2e981d6a38caffa2d"></a>
<a id="astructbt__sdp__attribute__id__range_html"></a>
<a id="astructbt__sdp__attribute__id__range_html_a2d5deb3e68536e0d7c90bc25e2bc1fbe"></a>
<a id="astructbt__sdp__attribute__id__range_html_a30a7eca0679107ef24154998bba35b78"></a>
<a id="astructbt__sdp__attribute_html"></a>
<a id="astructbt__sdp__attribute_html_a1221009053aa7911ea82b3169ea330a1"></a>
<a id="astructbt__sdp__attribute_html_a424c2ae038fda8dfd96e2a9cd876f9a1"></a>
<a id="astructbt__sdp__client__result_html"></a>
<a id="astructbt__sdp__client__result_html_aa1d12c7e550773963691e3b40ec6dd8e"></a>
<a id="astructbt__sdp__client__result_html_aa223dc666cbeaaebea462362188c531d"></a>
<a id="astructbt__sdp__data__elem_html"></a>
<a id="astructbt__sdp__data__elem_html_a0572a0c34ddf3ba340ee63d28c330dd1"></a>
<a id="astructbt__sdp__data__elem_html_a88b38121f91d55ca796dedb99b1e18d6"></a>
<a id="astructbt__sdp__data__elem_html_a8b7f4943ad968953edb7a3a6f541369b"></a>
<a id="astructbt__sdp__data__elem_html_ac6d5cbc71d1133f30bc20919ffd2d263"></a>
<a id="astructbt__sdp__discover__params_html"></a>
<a id="astructbt__sdp__discover__params_html_a2be942f3d0f18c56567dafa45af9c53e"></a>
<a id="astructbt__sdp__discover__params_html_a4c6073d7afda09be462902f5a95eaaed"></a>
<a id="astructbt__sdp__discover__params_html_a650143f0733958cf1186543c3469facc"></a>
<a id="astructbt__sdp__discover__params_html_a6f8728e5b74211852e2ce8872c21e5fb"></a>
<a id="astructbt__sdp__discover__params_html_a7854bf938c439af66b4a0d721f2bd1c1"></a>
<a id="astructbt__sdp__discover__params_html_acec0306279408087352804fdf76560de"></a>
<a id="astructbt__sdp__record_html"></a>
<a id="astructbt__sdp__record_html_a07caa07efa3c4bea065db4f39a72d70b"></a>
<a id="astructbt__sdp__record_html_a2bbcb54c385f88d512c1ccd4cf5e05ff"></a>
<a id="astructbt__sdp__record_html_ad54ca76a96964df3a6ac909eb54274df"></a>
<a id="astructbt__sdp__record_html_ad8ee5b17c45ca32696a492bc9c62d4fd"></a>
<a id="astructbt__sdp__record_html_ae94becbbce55a43661ef0c563e314b6b"></a>
<a id="astructbt__uuid_html"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructuuid_html"></a>

```c


/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_SDP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_SDP_H_


#include <sys/types.h>

#include <zephyr/bluetooth/uuid.h>
#include <zephyr/bluetooth/conn.h>

#ifdef __cplusplus
extern "C" {
#endif

/*
 * All definitions are based on Bluetooth Assigned Numbers
 * of the Bluetooth Specification
 */

#define BT_SDP_SDP_SERVER_SVCLASS           0x1000
#define BT_SDP_BROWSE_GRP_DESC_SVCLASS      0x1001
#define BT_SDP_PUBLIC_BROWSE_GROUP          0x1002
#define BT_SDP_SERIAL_PORT_SVCLASS          0x1101
#define BT_SDP_LAN_ACCESS_SVCLASS           0x1102
#define BT_SDP_DIALUP_NET_SVCLASS           0x1103
#define BT_SDP_IRMC_SYNC_SVCLASS            0x1104
#define BT_SDP_OBEX_OBJPUSH_SVCLASS         0x1105
#define BT_SDP_OBEX_FILETRANS_SVCLASS       0x1106
#define BT_SDP_IRMC_SYNC_CMD_SVCLASS        0x1107
#define BT_SDP_HEADSET_SVCLASS              0x1108
#define BT_SDP_CORDLESS_TELEPHONY_SVCLASS   0x1109
#define BT_SDP_AUDIO_SOURCE_SVCLASS         0x110a
#define BT_SDP_AUDIO_SINK_SVCLASS           0x110b
#define BT_SDP_AV_REMOTE_TARGET_SVCLASS     0x110c
#define BT_SDP_ADVANCED_AUDIO_SVCLASS       0x110d
#define BT_SDP_AV_REMOTE_SVCLASS            0x110e
#define BT_SDP_AV_REMOTE_CONTROLLER_SVCLASS 0x110f
#define BT_SDP_INTERCOM_SVCLASS             0x1110
#define BT_SDP_FAX_SVCLASS                  0x1111
#define BT_SDP_HEADSET_AGW_SVCLASS          0x1112
#define BT_SDP_WAP_SVCLASS                  0x1113
#define BT_SDP_WAP_CLIENT_SVCLASS           0x1114
#define BT_SDP_PANU_SVCLASS                 0x1115
#define BT_SDP_NAP_SVCLASS                  0x1116
#define BT_SDP_GN_SVCLASS                   0x1117
#define BT_SDP_DIRECT_PRINTING_SVCLASS      0x1118
#define BT_SDP_REFERENCE_PRINTING_SVCLASS   0x1119
#define BT_SDP_IMAGING_SVCLASS              0x111a
#define BT_SDP_IMAGING_RESPONDER_SVCLASS    0x111b
#define BT_SDP_IMAGING_ARCHIVE_SVCLASS      0x111c
#define BT_SDP_IMAGING_REFOBJS_SVCLASS      0x111d
#define BT_SDP_HANDSFREE_SVCLASS            0x111e
#define BT_SDP_HANDSFREE_AGW_SVCLASS        0x111f
#define BT_SDP_DIRECT_PRT_REFOBJS_SVCLASS   0x1120
#define BT_SDP_REFLECTED_UI_SVCLASS         0x1121
#define BT_SDP_BASIC_PRINTING_SVCLASS       0x1122
#define BT_SDP_PRINTING_STATUS_SVCLASS      0x1123
#define BT_SDP_HID_SVCLASS                  0x1124
#define BT_SDP_HCR_SVCLASS                  0x1125
#define BT_SDP_HCR_PRINT_SVCLASS            0x1126
#define BT_SDP_HCR_SCAN_SVCLASS             0x1127
#define BT_SDP_CIP_SVCLASS                  0x1128
#define BT_SDP_VIDEO_CONF_GW_SVCLASS        0x1129
#define BT_SDP_UDI_MT_SVCLASS               0x112a
#define BT_SDP_UDI_TA_SVCLASS               0x112b
#define BT_SDP_AV_SVCLASS                   0x112c
#define BT_SDP_SAP_SVCLASS                  0x112d
#define BT_SDP_PBAP_PCE_SVCLASS             0x112e
#define BT_SDP_PBAP_PSE_SVCLASS             0x112f
#define BT_SDP_PBAP_SVCLASS                 0x1130
#define BT_SDP_MAP_MSE_SVCLASS              0x1132
#define BT_SDP_MAP_MCE_SVCLASS              0x1133
#define BT_SDP_MAP_SVCLASS                  0x1134
#define BT_SDP_GNSS_SVCLASS                 0x1135
#define BT_SDP_GNSS_SERVER_SVCLASS          0x1136
#define BT_SDP_MPS_SC_SVCLASS               0x113a
#define BT_SDP_MPS_SVCLASS                  0x113b
#define BT_SDP_PNP_INFO_SVCLASS             0x1200
#define BT_SDP_GENERIC_NETWORKING_SVCLASS   0x1201
#define BT_SDP_GENERIC_FILETRANS_SVCLASS    0x1202
#define BT_SDP_GENERIC_AUDIO_SVCLASS        0x1203
#define BT_SDP_GENERIC_TELEPHONY_SVCLASS    0x1204
#define BT_SDP_UPNP_SVCLASS                 0x1205
#define BT_SDP_UPNP_IP_SVCLASS              0x1206
#define BT_SDP_UPNP_PAN_SVCLASS             0x1300
#define BT_SDP_UPNP_LAP_SVCLASS             0x1301
#define BT_SDP_UPNP_L2CAP_SVCLASS           0x1302
#define BT_SDP_VIDEO_SOURCE_SVCLASS         0x1303
#define BT_SDP_VIDEO_SINK_SVCLASS           0x1304
#define BT_SDP_VIDEO_DISTRIBUTION_SVCLASS   0x1305
#define BT_SDP_HDP_SVCLASS                  0x1400
#define BT_SDP_HDP_SOURCE_SVCLASS           0x1401
#define BT_SDP_HDP_SINK_SVCLASS             0x1402
#define BT_SDP_GENERIC_ACCESS_SVCLASS       0x1800
#define BT_SDP_GENERIC_ATTRIB_SVCLASS       0x1801
#define BT_SDP_APPLE_AGENT_SVCLASS          0x2112

#define BT_SDP_SERVER_RECORD_HANDLE 0x0000

#define BT_SDP_ATTR_RECORD_HANDLE               0x0000
#define BT_SDP_ATTR_SVCLASS_ID_LIST             0x0001
#define BT_SDP_ATTR_RECORD_STATE                0x0002
#define BT_SDP_ATTR_SERVICE_ID                  0x0003
#define BT_SDP_ATTR_PROTO_DESC_LIST             0x0004
#define BT_SDP_ATTR_BROWSE_GRP_LIST             0x0005
#define BT_SDP_ATTR_LANG_BASE_ATTR_ID_LIST      0x0006
#define BT_SDP_ATTR_SVCINFO_TTL                 0x0007
#define BT_SDP_ATTR_SERVICE_AVAILABILITY        0x0008
#define BT_SDP_ATTR_PROFILE_DESC_LIST           0x0009
#define BT_SDP_ATTR_DOC_URL                     0x000a
#define BT_SDP_ATTR_CLNT_EXEC_URL               0x000b
#define BT_SDP_ATTR_ICON_URL                    0x000c
#define BT_SDP_ATTR_ADD_PROTO_DESC_LIST         0x000d

#define BT_SDP_ATTR_GROUP_ID                    0x0200
#define BT_SDP_ATTR_IP_SUBNET                   0x0200
#define BT_SDP_ATTR_VERSION_NUM_LIST            0x0200
#define BT_SDP_ATTR_SUPPORTED_FEATURES_LIST     0x0200
#define BT_SDP_ATTR_GOEP_L2CAP_PSM              0x0200
#define BT_SDP_ATTR_SVCDB_STATE                 0x0201

#define BT_SDP_ATTR_MPSD_SCENARIOS              0x0200
#define BT_SDP_ATTR_MPMD_SCENARIOS              0x0201
#define BT_SDP_ATTR_MPS_DEPENDENCIES            0x0202

#define BT_SDP_ATTR_SERVICE_VERSION             0x0300
#define BT_SDP_ATTR_EXTERNAL_NETWORK            0x0301
#define BT_SDP_ATTR_SUPPORTED_DATA_STORES_LIST  0x0301
#define BT_SDP_ATTR_DATA_EXCHANGE_SPEC          0x0301
#define BT_SDP_ATTR_NETWORK                     0x0301
#define BT_SDP_ATTR_FAX_CLASS1_SUPPORT          0x0302
#define BT_SDP_ATTR_REMOTE_AUDIO_VOLUME_CONTROL 0x0302
#define BT_SDP_ATTR_MCAP_SUPPORTED_PROCEDURES   0x0302
#define BT_SDP_ATTR_FAX_CLASS20_SUPPORT         0x0303
#define BT_SDP_ATTR_SUPPORTED_FORMATS_LIST      0x0303
#define BT_SDP_ATTR_FAX_CLASS2_SUPPORT          0x0304
#define BT_SDP_ATTR_AUDIO_FEEDBACK_SUPPORT      0x0305
#define BT_SDP_ATTR_NETWORK_ADDRESS             0x0306
#define BT_SDP_ATTR_WAP_GATEWAY                 0x0307
#define BT_SDP_ATTR_HOMEPAGE_URL                0x0308
#define BT_SDP_ATTR_WAP_STACK_TYPE              0x0309
#define BT_SDP_ATTR_SECURITY_DESC               0x030a
#define BT_SDP_ATTR_NET_ACCESS_TYPE             0x030b
#define BT_SDP_ATTR_MAX_NET_ACCESSRATE          0x030c
#define BT_SDP_ATTR_IP4_SUBNET                  0x030d
#define BT_SDP_ATTR_IP6_SUBNET                  0x030e
#define BT_SDP_ATTR_SUPPORTED_CAPABILITIES      0x0310
#define BT_SDP_ATTR_SUPPORTED_FEATURES          0x0311
#define BT_SDP_ATTR_SUPPORTED_FUNCTIONS         0x0312
#define BT_SDP_ATTR_TOTAL_IMAGING_DATA_CAPACITY 0x0313
#define BT_SDP_ATTR_SUPPORTED_REPOSITORIES      0x0314
#define BT_SDP_ATTR_MAS_INSTANCE_ID             0x0315
#define BT_SDP_ATTR_SUPPORTED_MESSAGE_TYPES     0x0316
#define BT_SDP_ATTR_PBAP_SUPPORTED_FEATURES     0x0317
#define BT_SDP_ATTR_MAP_SUPPORTED_FEATURES      0x0317

#define BT_SDP_ATTR_SPECIFICATION_ID            0x0200
#define BT_SDP_ATTR_VENDOR_ID                   0x0201
#define BT_SDP_ATTR_PRODUCT_ID                  0x0202
#define BT_SDP_ATTR_VERSION                     0x0203
#define BT_SDP_ATTR_PRIMARY_RECORD              0x0204
#define BT_SDP_ATTR_VENDOR_ID_SOURCE            0x0205

#define BT_SDP_ATTR_HID_DEVICE_RELEASE_NUMBER   0x0200
#define BT_SDP_ATTR_HID_PARSER_VERSION          0x0201
#define BT_SDP_ATTR_HID_DEVICE_SUBCLASS         0x0202
#define BT_SDP_ATTR_HID_COUNTRY_CODE            0x0203
#define BT_SDP_ATTR_HID_VIRTUAL_CABLE           0x0204
#define BT_SDP_ATTR_HID_RECONNECT_INITIATE      0x0205
#define BT_SDP_ATTR_HID_DESCRIPTOR_LIST         0x0206
#define BT_SDP_ATTR_HID_LANG_ID_BASE_LIST       0x0207
#define BT_SDP_ATTR_HID_SDP_DISABLE             0x0208
#define BT_SDP_ATTR_HID_BATTERY_POWER           0x0209
#define BT_SDP_ATTR_HID_REMOTE_WAKEUP           0x020a
#define BT_SDP_ATTR_HID_PROFILE_VERSION         0x020b
#define BT_SDP_ATTR_HID_SUPERVISION_TIMEOUT     0x020c
#define BT_SDP_ATTR_HID_NORMALLY_CONNECTABLE    0x020d
#define BT_SDP_ATTR_HID_BOOT_DEVICE             0x020e
#define BT_SDP_ATTR_HID_SSR_HOST_MAX_LATENCY    0x020f
#define BT_SDP_ATTR_HID_SSR_HOST_MIN_TIMEOUT    0x0210

/*
 * These identifiers are based on the SDP spec stating that
 * "base attribute id of the primary (universal) language must be 0x0100"
 *
 * Other languages should have their own offset; e.g.:
 * #define XXXLangBase yyyy
 * #define AttrServiceName_XXX 0x0000+XXXLangBase
 */
#define BT_SDP_PRIMARY_LANG_BASE  0x0100

#define BT_SDP_ATTR_SVCNAME_PRIMARY (0x0000 + BT_SDP_PRIMARY_LANG_BASE)
#define BT_SDP_ATTR_SVCDESC_PRIMARY (0x0001 + BT_SDP_PRIMARY_LANG_BASE)
#define BT_SDP_ATTR_PROVNAME_PRIMARY (0x0002 + BT_SDP_PRIMARY_LANG_BASE)

#define BT_SDP_PROTO_SDP           0x0001
#define BT_SDP_PROTO_UDP           0x0002
#define BT_SDP_PROTO_RFCOMM        0x0003
#define BT_SDP_PROTO_TCP           0x0004
#define BT_SDP_PROTO_TCS_BIN       0x0005
#define BT_SDP_PROTO_TCS_AT        0x0006
#define BT_SDP_PROTO_ATT           0x0007
#define BT_SDP_PROTO_OBEX          0x0008
#define BT_SDP_PROTO_IP            0x0009
#define BT_SDP_PROTO_FTP           0x000a
#define BT_SDP_PROTO_HTTP          0x000c
#define BT_SDP_PROTO_WSP           0x000e
#define BT_SDP_PROTO_BNEP          0x000f
#define BT_SDP_PROTO_UPNP          0x0010
#define BT_SDP_PROTO_HID           0x0011
#define BT_SDP_PROTO_HARDCOPY_CTRL 0x0012
#define BT_SDP_PROTO_HARDCOPY_DATA 0x0014
#define BT_SDP_PROTO_HARDCOPY_NTF  0x0016
#define BT_SDP_PROTO_AVCTP         0x0017
#define BT_SDP_PROTO_AVDTP         0x0019
#define BT_SDP_PROTO_CMTP          0x001b
#define BT_SDP_PROTO_MCAP_CTRL     0x001e
#define BT_SDP_PROTO_MCAP_DATA     0x001f
#define BT_SDP_PROTO_L2CAP         0x0100

#define BT_SDP_DATA_NIL        0x00
#define BT_SDP_UINT8           0x08
#define BT_SDP_UINT16          0x09
#define BT_SDP_UINT32          0x0a
#define BT_SDP_UINT64          0x0b
#define BT_SDP_UINT128         0x0c
#define BT_SDP_INT8            0x10
#define BT_SDP_INT16           0x11
#define BT_SDP_INT32           0x12
#define BT_SDP_INT64           0x13
#define BT_SDP_INT128          0x14
#define BT_SDP_UUID_UNSPEC     0x18
#define BT_SDP_UUID16          0x19
#define BT_SDP_UUID32          0x1a
#define BT_SDP_UUID128         0x1c
#define BT_SDP_TEXT_STR_UNSPEC 0x20
#define BT_SDP_TEXT_STR8       0x25
#define BT_SDP_TEXT_STR16      0x26
#define BT_SDP_TEXT_STR32      0x27
#define BT_SDP_BOOL            0x28
#define BT_SDP_SEQ_UNSPEC      0x30
#define BT_SDP_SEQ8            0x35
#define BT_SDP_SEQ16           0x36
#define BT_SDP_SEQ32           0x37
#define BT_SDP_ALT_UNSPEC      0x38
#define BT_SDP_ALT8            0x3d
#define BT_SDP_ALT16           0x3e
#define BT_SDP_ALT32           0x3f
#define BT_SDP_URL_STR_UNSPEC  0x40
#define BT_SDP_URL_STR8        0x45
#define BT_SDP_URL_STR16       0x46
#define BT_SDP_URL_STR32       0x47

#define BT_SDP_TYPE_DESC_MASK 0xf8
#define BT_SDP_SIZE_DESC_MASK 0x07
#define BT_SDP_SIZE_INDEX_OFFSET 5

struct bt_sdp_data_elem {
        uint8_t        type;
        uint32_t       data_size;
        uint32_t       total_size;
        const void *data;
};

struct bt_sdp_attribute {
        uint16_t                id;
        struct bt_sdp_data_elem val;
};

struct bt_sdp_record {
        uint32_t                    handle;
        struct bt_sdp_attribute     *attrs;
        size_t                      attr_count;
        uint8_t                     index;
        sys_snode_t                 node;
};

/*
 * ---------------------------------------------------    ------------------
 * | Service Hdl | Attr list ptr | Attr count | Next | -> | Service Hdl | ...
 * ---------------------------------------------------    ------------------
 */

#define BT_SDP_ARRAY_8(...) ((uint8_t[]) {__VA_ARGS__})

#define BT_SDP_ARRAY_16(...) ((uint16_t[]) {__VA_ARGS__})

#define BT_SDP_ARRAY_32(...) ((uint32_t[]) {__VA_ARGS__})

#define BT_SDP_ARRAY_UUID_128(w32, w1, w2, w3, w48) \
        BT_SDP_ARRAY_8(BT_UUID_128_ENCODE(w32, w1, w2, w3, w48))

#define BT_SDP_TYPE_SIZE(_type) .type = _type, \
                        .data_size = BIT(_type & BT_SDP_SIZE_DESC_MASK), \
                        .total_size = BIT(_type & BT_SDP_SIZE_DESC_MASK) + 1

#define BT_SDP_TYPE_SIZE_VAR(_type, _size) .type = _type, \
                        .data_size = _size, \
                        .total_size = BIT((_type & BT_SDP_SIZE_DESC_MASK) - \
                                          BT_SDP_SIZE_INDEX_OFFSET) + _size + 1

#define BT_SDP_DATA_ELEM_LIST(...) ((struct bt_sdp_data_elem[]) {__VA_ARGS__})


#define BT_SDP_NEW_SERVICE \
{ \
        BT_SDP_ATTR_RECORD_HANDLE, \
        { BT_SDP_TYPE_SIZE(BT_SDP_UINT32), BT_SDP_ARRAY_32(0) } \
}, \
{ \
        BT_SDP_ATTR_RECORD_STATE, \
        { BT_SDP_TYPE_SIZE(BT_SDP_UINT32), BT_SDP_ARRAY_32(0) } \
}, \
{ \
        BT_SDP_ATTR_LANG_BASE_ATTR_ID_LIST, \
        { BT_SDP_TYPE_SIZE_VAR(BT_SDP_SEQ8, 9), \
          BT_SDP_DATA_ELEM_LIST( \
                { BT_SDP_TYPE_SIZE(BT_SDP_UINT16), BT_SDP_ARRAY_8('n', 'e') }, \
                { BT_SDP_TYPE_SIZE(BT_SDP_UINT16), BT_SDP_ARRAY_16(106) }, \
                { BT_SDP_TYPE_SIZE(BT_SDP_UINT16), \
                        BT_SDP_ARRAY_16(BT_SDP_PRIMARY_LANG_BASE) } \
          ), \
        } \
}, \
{ \
        BT_SDP_ATTR_BROWSE_GRP_LIST, \
        { BT_SDP_TYPE_SIZE_VAR(BT_SDP_SEQ8, 3), \
          BT_SDP_DATA_ELEM_LIST( \
                { BT_SDP_TYPE_SIZE(BT_SDP_UUID16), \
                        BT_SDP_ARRAY_16(BT_SDP_PUBLIC_BROWSE_GROUP) }, \
          ), \
        } \
}


#define BT_SDP_LIST(_att_id, _type_size, _data_elem_seq) \
{ \
        _att_id, { _type_size, _data_elem_seq } \
}

#define BT_SDP_SERVICE_ID(_uuid) \
{ \
        BT_SDP_ATTR_SERVICE_ID, \
        { BT_SDP_TYPE_SIZE(BT_SDP_UUID16), &((struct bt_uuid_16) _uuid) } \
}

#define BT_SDP_SERVICE_NAME(_name) \
{ \
        BT_SDP_ATTR_SVCNAME_PRIMARY, \
        { BT_SDP_TYPE_SIZE_VAR(BT_SDP_TEXT_STR8, (sizeof(_name)-1)), _name } \
}

#define BT_SDP_SUPPORTED_FEATURES(_features) \
{ \
        BT_SDP_ATTR_SUPPORTED_FEATURES, \
        { BT_SDP_TYPE_SIZE(BT_SDP_UINT16), BT_SDP_ARRAY_16(_features) } \
}

#define BT_SDP_SUPPORTED_CAPABILITIES(_capabilities) \
{ \
        BT_SDP_ATTR_SUPPORTED_CAPABILITIES, \
        { BT_SDP_TYPE_SIZE(BT_SDP_UINT8), BT_SDP_ARRAY_8(_capabilities) } \
}

#define BT_SDP_SUPPORTED_FUNCTIONS(_functions) \
{ \
        BT_SDP_ATTR_SUPPORTED_FUNCTIONS, \
        { BT_SDP_TYPE_SIZE(BT_SDP_UINT32), BT_SDP_ARRAY_32(_functions) } \
}

#define BT_SDP_RECORD(_attrs) \
{ \
        .attrs = _attrs, \
        .attr_count = ARRAY_SIZE((_attrs)), \
}

/* Server API */

int bt_sdp_register_service(struct bt_sdp_record *service);

int bt_sdp_unregister_service(struct bt_sdp_record *service);

/* Client API */

struct bt_sdp_client_result {
        struct net_buf        *resp_buf;
        bool                   next_record_hint;
};

enum {
        BT_SDP_DISCOVER_UUID_STOP = 0,
        BT_SDP_DISCOVER_UUID_CONTINUE,
};

struct bt_sdp_discover_params;

typedef uint8_t (*bt_sdp_discover_func_t)(struct bt_conn *conn, struct bt_sdp_client_result *result,
                                          const struct bt_sdp_discover_params *params);

enum {
        BT_SDP_DISCOVER_SERVICE_SEARCH,
        BT_SDP_DISCOVER_SERVICE_ATTR,
        BT_SDP_DISCOVER_SERVICE_SEARCH_ATTR,
};

#define BT_SDP_ATTR_ID_RANGE(beginning, ending) {(beginning), (ending)}

struct bt_sdp_attribute_id_range {
        uint16_t beginning;
        uint16_t ending;
};

struct bt_sdp_attribute_id_list {
        size_t count;
        struct bt_sdp_attribute_id_range *ranges;
};

struct bt_sdp_discover_params {
        sys_snode_t _node;
        union {
                const struct bt_uuid *uuid;
                uint32_t handle;
        };
        bt_sdp_discover_func_t func;
        struct net_buf_pool *pool;
        uint8_t type;
        struct bt_sdp_attribute_id_list *ids;
};


int bt_sdp_discover(struct bt_conn *conn, struct bt_sdp_discover_params *params);

int bt_sdp_discover_cancel(struct bt_conn *conn,
                           struct bt_sdp_discover_params *params);


/* Helper types & functions for SDP client to get essential data from server */

int bt_sdp_get_proto_param(const struct net_buf *buf, uint16_t proto,
                           uint16_t *param);

int bt_sdp_get_addl_proto_param(const struct net_buf *buf, uint16_t proto, uint8_t index,
                                uint16_t *param);

int bt_sdp_get_profile_version(const struct net_buf *buf, uint16_t profile,
                               uint16_t *version);

int bt_sdp_get_features(const struct net_buf *buf, uint16_t *features);

int bt_sdp_get_vendor_id(const struct net_buf *buf, uint16_t *vendor_id);

int bt_sdp_get_product_id(const struct net_buf *buf, uint16_t *product_id);

int bt_sdp_record_parse(const struct net_buf *buf,
                        bool (*func)(const struct bt_sdp_attribute *attr, void *user_data),
                        void *user_data);

bool bt_sdp_has_attr(const struct net_buf *buf, uint16_t attr_id);

int bt_sdp_get_attr(const struct net_buf *buf, uint16_t attr_id, struct bt_sdp_attribute *attr);

struct bt_sdp_attr_value_uint {
        uint8_t size;
        union {
                uint8_t u8;
                uint16_t u16;
                uint32_t u32;
                uint64_t u64;
                uint8_t u128[BIT(BT_SDP_UINT128 & BT_SDP_SIZE_DESC_MASK)];
        };
};

struct bt_sdp_attr_value_int {
        uint8_t size;
        union {
                int8_t s8;
                int16_t s16;
                int32_t s32;
                int64_t s64;
                uint8_t s128[BIT(BT_SDP_INT128 & BT_SDP_SIZE_DESC_MASK)];
        };
};

struct bt_sdp_attr_value_text {
        uint32_t len;
        uint8_t *text;
};

struct bt_sdp_attr_value_url {
        uint32_t len;
        uint8_t *url;
};

enum bt_sdp_attr_value_type {
        BT_SDP_ATTR_VALUE_TYPE_NONE = 0,
        BT_SDP_ATTR_VALUE_TYPE_UINT,
        BT_SDP_ATTR_VALUE_TYPE_SINT,
        BT_SDP_ATTR_VALUE_TYPE_BOOL,
        BT_SDP_ATTR_VALUE_TYPE_TEXT,
        BT_SDP_ATTR_VALUE_TYPE_URL,
};

struct bt_sdp_attr_value {
        enum bt_sdp_attr_value_type type;
        union {
                bool value;
                struct bt_sdp_attr_value_uint uint;
                struct bt_sdp_attr_value_int sint;
                struct bt_sdp_attr_value_text text;
                struct bt_sdp_attr_value_url url;
        };
};

struct bt_sdp_attr_value_pair {
        struct bt_uuid *uuid;
        struct bt_sdp_attr_value *value;
};

int bt_sdp_attr_value_parse(const struct bt_sdp_attribute *attr,
                            bool (*func)(const struct bt_sdp_attr_value_pair *value,
                                         void *user_data),
                            void *user_data);

bool bt_sdp_attr_has_uuid(const struct bt_sdp_attribute *attr, const struct bt_uuid *uuid);

int bt_sdp_attr_read(const struct bt_sdp_attribute *attr, const struct bt_uuid *uuid,
                     struct bt_sdp_attr_value *value);

int bt_sdp_attr_addl_proto_parse(const struct bt_sdp_attribute *attr,
                                 bool (*func)(const struct bt_sdp_attribute *attr, void *user_data),
                                 void *user_data);

ssize_t bt_sdp_attr_addl_proto_count(const struct bt_sdp_attribute *attr);

int bt_sdp_attr_addl_proto_read(const struct bt_sdp_attribute *attr, uint16_t index,
                                const struct bt_uuid *uuid, struct bt_sdp_attr_value *value);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_SDP_H_ */
```

## 19.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 32 行

所有定义均基于蓝牙规范（Bluetooth Specification）中的蓝牙分配编号（Bluetooth Assigned Numbers）。

### 注释 3：原第 217 行

这些标识（Identifiers）依据服务发现协议（SDP）规范，其规定主语言（通用语言，Primary / Universal Language）的基础属性标识（Base Attribute ID）必须为 `0x0100`。

其他语言应使用各自的偏移（Offset），例如：

```c
#define XXXLangBase yyyy
#define AttrServiceName_XXX 0x0000+XXXLangBase
```

### 注释 4：原第 360 行

服务记录链接结构（Service Record Chain）：每个记录包含服务句柄（Service Hdl）、属性列表指针（Attr List Ptr）、属性数量（Attr Count）和下一记录指针（Next）；`Next` 指向后续服务记录，其开头同样是服务句柄。

### 注释 5：原第 563 行

服务器 API（Server API）。

### 注释 6：原第 596 行

客户端 API（Client API）。

### 注释 7：原第 779 行

供 SDP 客户端从服务器获取必要数据的辅助类型与函数（Helper Types and Functions）。

### 注释 8：原第 1137 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_SDP_H_`。

## 19.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h.html)
- [sys/types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [bt_sdp_data_elem](../bluetooth_service_model_reference/P169_bt_sdp_data_elem_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [type](../bluetooth_service_model_reference/P169_bt_sdp_data_elem_结构体.md#ac6d5cbc71d1133f30bc20919ffd2d263)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [data_size](../bluetooth_service_model_reference/P169_bt_sdp_data_elem_结构体.md#a88b38121f91d55ca796dedb99b1e18d6)
- [total_size](../bluetooth_service_model_reference/P169_bt_sdp_data_elem_结构体.md#a8b7f4943ad968953edb7a3a6f541369b)
- [data](../bluetooth_service_model_reference/P169_bt_sdp_data_elem_结构体.md#a0572a0c34ddf3ba340ee63d28c330dd1)
- [bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [id](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md#a1221009053aa7911ea82b3169ea330a1)
- [val](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md#a424c2ae038fda8dfd96e2a9cd876f9a1)
- [bt_sdp_record](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md)
- [handle](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md#ae94becbbce55a43661ef0c563e314b6b)
- [attrs](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md#ad8ee5b17c45ca32696a492bc9c62d4fd)
- [attr_count](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md#a2bbcb54c385f88d512c1ccd4cf5e05ff)
- [index](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md#ad54ca76a96964df3a6ac909eb54274df)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md#a07caa07efa3c4bea065db4f39a72d70b)
- [bt_sdp_register_service](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga6006e3cd593ef793273fb291913790fa)
- [bt_sdp_unregister_service](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga71e7d75850becf4ead62668c8e7bebbc)
- [bt_sdp_client_result](../bluetooth_service_model_reference/P168_bt_sdp_client_result_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [resp_buf](../bluetooth_service_model_reference/P168_bt_sdp_client_result_结构体.md#aa223dc666cbeaaebea462362188c531d)
- [next_record_hint](../bluetooth_service_model_reference/P168_bt_sdp_client_result_结构体.md#aa1d12c7e550773963691e3b40ec6dd8e)
- [BT_SDP_DISCOVER_UUID_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga278df12ff5def68ca4663defd178582ca990fbea48866b2acb7ccd67391b19636)
- [BT_SDP_DISCOVER_UUID_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga278df12ff5def68ca4663defd178582ca94e15ea86b69d65ca9c1947d1e2157ef)
- [bt_sdp_discover_params](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md)
- [bt_sdp_discover_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad672a89277b276d1b702fe07302c468e)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [BT_SDP_DISCOVER_SERVICE_SEARCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga88019838cb3e5317fce93f4933583d94a9ce8c93cf1754fc7047951e891f66ff2)
- [BT_SDP_DISCOVER_SERVICE_ATTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga88019838cb3e5317fce93f4933583d94a5b8c3260e5aaaa08e86a099ccfeee41f)
- [BT_SDP_DISCOVER_SERVICE_SEARCH_ATTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga88019838cb3e5317fce93f4933583d94a64fff103816cfc0215b9b3909786fa4e)
- [bt_sdp_attribute_id_range](../bluetooth_service_model_reference/P167_bt_sdp_attribute_id_range_结构体.md)
- [beginning](../bluetooth_service_model_reference/P167_bt_sdp_attribute_id_range_结构体.md#a30a7eca0679107ef24154998bba35b78)
- [ending](../bluetooth_service_model_reference/P167_bt_sdp_attribute_id_range_结构体.md#a2d5deb3e68536e0d7c90bc25e2bc1fbe)
- [bt_sdp_attribute_id_list](../bluetooth_service_model_reference/P166_bt_sdp_attribute_id_list_结构体.md)
- [count](../bluetooth_service_model_reference/P166_bt_sdp_attribute_id_list_结构体.md#a3f0c472e904dd86bf95f8623b1d04d73)
- [ranges](../bluetooth_service_model_reference/P166_bt_sdp_attribute_id_list_结构体.md#af38e30a77ad8b0a2e981d6a38caffa2d)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [uuid](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#a4c6073d7afda09be462902f5a95eaaed)
- [handle](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#a2be942f3d0f18c56567dafa45af9c53e)
- [func](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#a650143f0733958cf1186543c3469facc)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [pool](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#a6f8728e5b74211852e2ce8872c21e5fb)
- [type](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#acec0306279408087352804fdf76560de)
- [ids](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#a7854bf938c439af66b4a0d721f2bd1c1)
- [bt_sdp_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga44658df825a40f820a31e7adb4240d25)
- [bt_sdp_discover_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2eb0646597a44e0e3cb0234d2c12a2d7)
- [bt_sdp_get_proto_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf69723cff6dce7e86f0f0240ec3e2041)
- [bt_sdp_get_addl_proto_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaba31a2327e4bba56ef2ac831b166e66a)
- [bt_sdp_get_profile_version](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9e7d4bd0a407fe8254410f907db90f00)
- [bt_sdp_get_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gae1c3110dfe24a939cc02d998c4699ca7)
- [bt_sdp_get_vendor_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaed089d52f57cb25d2b02b2adbc60a36a)
- [bt_sdp_get_product_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga71809908bb73150258b2a5ab3c2f8517)
- [bt_sdp_record_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga0ce1314e052881eec5a43f571857960e)
- [bt_sdp_has_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2cb42ca8e487071682c37124ab56f2ab)
- [bt_sdp_get_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9df34b18af051782377229a18e6d3887)
- [bt_sdp_attr_value_uint](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md)
- [size](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md#a5741e3d3c00c8dc8085d496692d1114c)
- [u8](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md#a7dae539fd3f8232842fe4a1bebca1824)
- [u16](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md#af88e041745b2e69ac207afc5e4d369c1)
- [u32](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md#ae0a02d6f23b160c98022f58b9c38ab37)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [u64](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md#a4752a1517d75c13454db83f095b5da4f)
- [u128](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md#a7b609be27cad4508d2713b169d8bd4b5)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_SDP_UINT128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9a815c6efe976f29e9f6f35a566245fd)
- [BT_SDP_SIZE_DESC_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2d1040ccd11d1dd4c697525ebc323243)
- [bt_sdp_attr_value_int](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md)
- [size](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md#a4dd9e9eae0d95dcc3af855d711ead35e)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [s8](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md#a282cf4821d1ba734df65e447687bb8ec)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [s16](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md#ae2eeaa2eaf83b7923ea5f6d743d480b7)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [s32](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md#ad114c103a0d2248cffdf5a0a458e8c57)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [s64](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md#a12c991cdf87a2d48d1c5b3d5cb639ead)
- [s128](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md#a9fe2006da0ce55441dcffd4080ac287a)
- [BT_SDP_INT128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf754bbfd9cdc0e6a2bf7d6c46fab3f29)
- [bt_sdp_attr_value_text](../bluetooth_service_model_reference/P162_bt_sdp_attr_value_text_结构体.md)
- [len](../bluetooth_service_model_reference/P162_bt_sdp_attr_value_text_结构体.md#a89161e7cfe2185b16b2e114b85209621)
- [text](../bluetooth_service_model_reference/P162_bt_sdp_attr_value_text_结构体.md#a440091666ca041db641c709ed172ba2d)
- [bt_sdp_attr_value_url](../bluetooth_service_model_reference/P164_bt_sdp_attr_value_url_结构体.md)
- [len](../bluetooth_service_model_reference/P164_bt_sdp_attr_value_url_结构体.md#a7ff5d8b06952b873f6b5c60129fa346f)
- [url](../bluetooth_service_model_reference/P164_bt_sdp_attr_value_url_结构体.md#aed7f8929167df11bb0db2249fc5957d9)
- [bt_sdp_attr_value_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5e4a45b7b860d82a111480c9f25c2666)
- [BT_SDP_ATTR_VALUE_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666acaf932b38a1e17ca9e85c055096fa1da)
- [BT_SDP_ATTR_VALUE_TYPE_UINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a5af87613192cda6a05fa280d2df8574b)
- [BT_SDP_ATTR_VALUE_TYPE_SINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a5917deef84a7af5d5f908d4058732b1e)
- [BT_SDP_ATTR_VALUE_TYPE_BOOL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a154bbb29fb26d007838c87def4cd34f8)
- [BT_SDP_ATTR_VALUE_TYPE_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a80b8652e39dae70c61443adf4f29fb4d)
- [BT_SDP_ATTR_VALUE_TYPE_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a27eccef21d812956c6ae7ff9194e20e4)
- [bt_sdp_attr_value](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md)
- [type](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md#a36fe39424a1f3ed59c2f7addf6a3eb8a)
- [value](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md#af1582544193e9598183d8bf6ea722dbc)
- [uint](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md#a7a1c4a780d8712fbf16df75f8ebae05f)
- [sint](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md#ae5b6d1e373b37e2627b34e6da549098f)
- [text](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md#a2fc1e977a5b82f16b160c898cca1cff7)
- [url](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md#af6e3f74c2c405153654fcade2608eca0)
- [bt_sdp_attr_value_pair](../bluetooth_service_model_reference/P161_bt_sdp_attr_value_pair_结构体.md)
- [uuid](../bluetooth_service_model_reference/P161_bt_sdp_attr_value_pair_结构体.md#a533ee8ab9d9dec24faf52c2dc016bb1d)
- [value](../bluetooth_service_model_reference/P161_bt_sdp_attr_value_pair_结构体.md#a505490ce660a6c15b2b59efaa5fb6057)
- [bt_sdp_attr_value_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab7d3e8bc83efff28cf9118710b5486fc)
- [bt_sdp_attr_has_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga07ca5d4f383d74004478cfd6ead2b80a)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_sdp_attr_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3bad45ab578c0277a320ac241692f799)
- [bt_sdp_attr_addl_proto_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac395eff18a4d2af3d955e276bf13963a)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [bt_sdp_attr_addl_proto_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa104046a9e6e15f05961bf8652ecec16)
- [bt_sdp_attr_addl_proto_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gacf20a00d84e6eed2c128284fe9c52024)
- [uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [bt_sdp_attr_value_int::s64](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md#a12c991cdf87a2d48d1c5b3d5cb639ead)
- [bt_sdp_attr_value_int::s8](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md#a282cf4821d1ba734df65e447687bb8ec)
- [bt_sdp_attr_value_int::size](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md#a4dd9e9eae0d95dcc3af855d711ead35e)
- [bt_sdp_attr_value_int::s128](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md#a9fe2006da0ce55441dcffd4080ac287a)
- [bt_sdp_attr_value_int::s32](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md#ad114c103a0d2248cffdf5a0a458e8c57)
- [bt_sdp_attr_value_int::s16](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md#ae2eeaa2eaf83b7923ea5f6d743d480b7)
- [bt_sdp_attr_value_pair::value](../bluetooth_service_model_reference/P161_bt_sdp_attr_value_pair_结构体.md#a505490ce660a6c15b2b59efaa5fb6057)
- [bt_sdp_attr_value_pair::uuid](../bluetooth_service_model_reference/P161_bt_sdp_attr_value_pair_结构体.md#a533ee8ab9d9dec24faf52c2dc016bb1d)
- [bt_sdp_attr_value_text::text](../bluetooth_service_model_reference/P162_bt_sdp_attr_value_text_结构体.md#a440091666ca041db641c709ed172ba2d)
- [bt_sdp_attr_value_text::len](../bluetooth_service_model_reference/P162_bt_sdp_attr_value_text_结构体.md#a89161e7cfe2185b16b2e114b85209621)
- [bt_sdp_attr_value_uint::u64](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md#a4752a1517d75c13454db83f095b5da4f)
- [bt_sdp_attr_value_uint::size](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md#a5741e3d3c00c8dc8085d496692d1114c)
- [bt_sdp_attr_value_uint::u128](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md#a7b609be27cad4508d2713b169d8bd4b5)
- [bt_sdp_attr_value_uint::u8](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md#a7dae539fd3f8232842fe4a1bebca1824)
- [bt_sdp_attr_value_uint::u32](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md#ae0a02d6f23b160c98022f58b9c38ab37)
- [bt_sdp_attr_value_uint::u16](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md#af88e041745b2e69ac207afc5e4d369c1)
- [bt_sdp_attr_value_url::len](../bluetooth_service_model_reference/P164_bt_sdp_attr_value_url_结构体.md#a7ff5d8b06952b873f6b5c60129fa346f)
- [bt_sdp_attr_value_url::url](../bluetooth_service_model_reference/P164_bt_sdp_attr_value_url_结构体.md#aed7f8929167df11bb0db2249fc5957d9)
- [bt_sdp_attr_value::text](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md#a2fc1e977a5b82f16b160c898cca1cff7)
- [bt_sdp_attr_value::type](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md#a36fe39424a1f3ed59c2f7addf6a3eb8a)
- [bt_sdp_attr_value::uint](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md#a7a1c4a780d8712fbf16df75f8ebae05f)
- [bt_sdp_attr_value::sint](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md#ae5b6d1e373b37e2627b34e6da549098f)
- [bt_sdp_attr_value::value](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md#af1582544193e9598183d8bf6ea722dbc)
- [bt_sdp_attr_value::url](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md#af6e3f74c2c405153654fcade2608eca0)
- [bt_sdp_attribute_id_list::count](../bluetooth_service_model_reference/P166_bt_sdp_attribute_id_list_结构体.md#a3f0c472e904dd86bf95f8623b1d04d73)
- [bt_sdp_attribute_id_list::ranges](../bluetooth_service_model_reference/P166_bt_sdp_attribute_id_list_结构体.md#af38e30a77ad8b0a2e981d6a38caffa2d)
- [bt_sdp_attribute_id_range::ending](../bluetooth_service_model_reference/P167_bt_sdp_attribute_id_range_结构体.md#a2d5deb3e68536e0d7c90bc25e2bc1fbe)
- [bt_sdp_attribute_id_range::beginning](../bluetooth_service_model_reference/P167_bt_sdp_attribute_id_range_结构体.md#a30a7eca0679107ef24154998bba35b78)
- [bt_sdp_attribute::id](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md#a1221009053aa7911ea82b3169ea330a1)
- [bt_sdp_attribute::val](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md#a424c2ae038fda8dfd96e2a9cd876f9a1)
- [bt_sdp_client_result::next_record_hint](../bluetooth_service_model_reference/P168_bt_sdp_client_result_结构体.md#aa1d12c7e550773963691e3b40ec6dd8e)
- [bt_sdp_client_result::resp_buf](../bluetooth_service_model_reference/P168_bt_sdp_client_result_结构体.md#aa223dc666cbeaaebea462362188c531d)
- [bt_sdp_data_elem::data](../bluetooth_service_model_reference/P169_bt_sdp_data_elem_结构体.md#a0572a0c34ddf3ba340ee63d28c330dd1)
- [bt_sdp_data_elem::data_size](../bluetooth_service_model_reference/P169_bt_sdp_data_elem_结构体.md#a88b38121f91d55ca796dedb99b1e18d6)
- [bt_sdp_data_elem::total_size](../bluetooth_service_model_reference/P169_bt_sdp_data_elem_结构体.md#a8b7f4943ad968953edb7a3a6f541369b)
- [bt_sdp_data_elem::type](../bluetooth_service_model_reference/P169_bt_sdp_data_elem_结构体.md#ac6d5cbc71d1133f30bc20919ffd2d263)
- [bt_sdp_discover_params::handle](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#a2be942f3d0f18c56567dafa45af9c53e)
- [bt_sdp_discover_params::uuid](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#a4c6073d7afda09be462902f5a95eaaed)
- [bt_sdp_discover_params::func](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#a650143f0733958cf1186543c3469facc)
- [bt_sdp_discover_params::pool](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#a6f8728e5b74211852e2ce8872c21e5fb)
- [bt_sdp_discover_params::ids](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#a7854bf938c439af66b4a0d721f2bd1c1)
- [bt_sdp_discover_params::type](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#acec0306279408087352804fdf76560de)
- [bt_sdp_record::node](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md#a07caa07efa3c4bea065db4f39a72d70b)
- [bt_sdp_record::attr_count](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md#a2bbcb54c385f88d512c1ccd4cf5e05ff)
- [bt_sdp_record::index](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md#ad54ca76a96964df3a6ac909eb54274df)
- [bt_sdp_record::attrs](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md#ad8ee5b17c45ca32696a492bc9c62d4fd)
- [bt_sdp_record::handle](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md#ae94becbbce55a43661ef0c563e314b6b)

---

[上一章](P018_sam0_eic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P020_sections.h_源码浏览.md)
