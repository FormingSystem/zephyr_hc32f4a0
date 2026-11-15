---
id: learning.zephyr-docs.api-source-runtime-reference.page-45
title: ppp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_ppp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h.html)。

## 45.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00081"></a>
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
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00113"></a>
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
<a id="l00148"></a>
<a id="foldopen00152"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="foldopen00212"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="foldopen00237"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
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
<a id="l00368"></a>
<a id="foldopen00370"></a>
<a id="l00370"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="foldopen00390"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="foldopen00396"></a>
<a id="l00396"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="foldopen00408"></a>
<a id="l00408"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="foldopen00414"></a>
<a id="l00414"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00424"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00443"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00460"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00477"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
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
<a id="l00601"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="foldopen00619"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="foldopen00623"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="foldopen00627"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="foldopen00631"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="foldopen00642"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="foldopen00656"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="foldopen00670"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="foldopen00684"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="foldopen00703"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="foldopen00723"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__net__core_html_ga8e5393f3bdd85491f221324e637c3896"></a>
<a id="agroup__net__l2_html_gac7db0cc6c56d371a5803873074ec2516"></a>
<a id="agroup__ppp_html_ga1064e3d8c6aa3d3161e399d6937162b6"></a>
<a id="agroup__ppp_html_ga1436cf5cfcb6752e41c9e06a0ee30030"></a>
<a id="agroup__ppp_html_ga15afa05abc0446201c912c75644306bf"></a>
<a id="agroup__ppp_html_ga284e237a6323f2daffc444a73a4b8b6b"></a>
<a id="agroup__ppp_html_ga2e5d0ae66bf076123cb29effc0a8e894"></a>
<a id="agroup__ppp_html_ga4f6104cff735f9829762b6552a7346bf"></a>
<a id="agroup__ppp_html_ga716727874cecc8ee358da6c76adedc0a"></a>
<a id="agroup__ppp_html_ga74e94e9fcae30bc386c5e3d951ed5882"></a>
<a id="agroup__ppp_html_ga8ad7cc0d142a6e7ea82c45bec2cc3670"></a>
<a id="agroup__ppp_html_ga9893a7c93b3d23b96b4d83aa1204c500"></a>
<a id="agroup__ppp_html_gaa584f3427a21343ab692b5ec3a9573ec"></a>
<a id="agroup__ppp_html_gaabf883cfefc9910b9b9d8931e68b320c"></a>
<a id="agroup__ppp_html_gaad7380b3a502f4b649348b733124f21a"></a>
<a id="agroup__ppp_html_gac8f3d915c930d61831bcb13d6201b15c"></a>
<a id="agroup__ppp_html_gad7f41d9012098ed1a04f897e252cc32d"></a>
<a id="agroup__ppp_html_gad96b2c77cf6a066d55d78c5d63cb9bd0"></a>
<a id="agroup__ppp_html_gaf30172a9fead40463d129a5afeaf1ac3"></a>
<a id="agroup__ppp_html_gga1064e3d8c6aa3d3161e399d6937162b6a124bafb002549c2de4cb293f5e158fd9"></a>
<a id="agroup__ppp_html_gga1064e3d8c6aa3d3161e399d6937162b6a176055a8c0483c7c8b6b0d416b676964"></a>
<a id="agroup__ppp_html_gga1064e3d8c6aa3d3161e399d6937162b6a3913e2668196db10d17f8d7ffa86c6a6"></a>
<a id="agroup__ppp_html_gga1064e3d8c6aa3d3161e399d6937162b6a3b315dc4f10305923bba2bfbe2fa05ad"></a>
<a id="agroup__ppp_html_gga1064e3d8c6aa3d3161e399d6937162b6a7319a35a35044ca3f5fcc1ed6460fb3b"></a>
<a id="agroup__ppp_html_gga1064e3d8c6aa3d3161e399d6937162b6a7d154ff3643ba4de8cf358bd81361552"></a>
<a id="agroup__ppp_html_gga1064e3d8c6aa3d3161e399d6937162b6a80771bc5d12ab8dcf78f87c872b0f41b"></a>
<a id="agroup__ppp_html_gga1064e3d8c6aa3d3161e399d6937162b6af156d53ee18de3907210c910667e8931"></a>
<a id="agroup__ppp_html_gga284e237a6323f2daffc444a73a4b8b6ba0492bfbaebc3f126327c74dbe56ce76a"></a>
<a id="agroup__ppp_html_gga284e237a6323f2daffc444a73a4b8b6ba51a5c6e5d16fbb607597f0d2f6a12af7"></a>
<a id="agroup__ppp_html_gga284e237a6323f2daffc444a73a4b8b6ba621902d0a6ca3efa0aa20c43c32164af"></a>
<a id="agroup__ppp_html_gga284e237a6323f2daffc444a73a4b8b6ba647d283023ee50299c1d9ca376cce4f4"></a>
<a id="agroup__ppp_html_gga284e237a6323f2daffc444a73a4b8b6babdff682a09630e713867c3241d56954d"></a>
<a id="agroup__ppp_html_gga284e237a6323f2daffc444a73a4b8b6bac1f10a2aa5edcb826621304de596a5b7"></a>
<a id="agroup__ppp_html_gga8ad7cc0d142a6e7ea82c45bec2cc3670a0a9da56ae134b701f5a8b31c3f1c9bfe"></a>
<a id="agroup__ppp_html_gga8ad7cc0d142a6e7ea82c45bec2cc3670a0b974fd7b99c28a8d06f096be1ed9cc6"></a>
<a id="agroup__ppp_html_gga8ad7cc0d142a6e7ea82c45bec2cc3670a1b311302ecabb507c34b1f77cba36f25"></a>
<a id="agroup__ppp_html_gga8ad7cc0d142a6e7ea82c45bec2cc3670a22dae8ee345f9664042eef54086f4de9"></a>
<a id="agroup__ppp_html_gga8ad7cc0d142a6e7ea82c45bec2cc3670a25f326220ab531e93140b7c6bddd0d21"></a>
<a id="agroup__ppp_html_gga8ad7cc0d142a6e7ea82c45bec2cc3670a40b5032dabf9c697e761aa2cff0b2e44"></a>
<a id="agroup__ppp_html_gga8ad7cc0d142a6e7ea82c45bec2cc3670a4cdde6fe10fcfa862742751e1152887b"></a>
<a id="agroup__ppp_html_gga8ad7cc0d142a6e7ea82c45bec2cc3670a7a51ef2d8d979ded98e0aad680f1b6e2"></a>
<a id="agroup__ppp_html_gga8ad7cc0d142a6e7ea82c45bec2cc3670ab17a70f864ac04b8b52f8ca1edc4d2e0"></a>
<a id="agroup__ppp_html_gga8ad7cc0d142a6e7ea82c45bec2cc3670ac66b190ff6dd0884dfba62da40ee2206"></a>
<a id="agroup__ppp_html_ggac8f3d915c930d61831bcb13d6201b15ca01e51712c002e5ce746d93376b4f2cef"></a>
<a id="agroup__ppp_html_ggac8f3d915c930d61831bcb13d6201b15ca3c37fd8819b98caa7f9b3b94aff53524"></a>
<a id="agroup__ppp_html_ggac8f3d915c930d61831bcb13d6201b15ca3ed6d42c4b65271955a308c4e7a437a9"></a>
<a id="agroup__ppp_html_ggac8f3d915c930d61831bcb13d6201b15ca59c791ebec909b03a42659d08be2bcf8"></a>
<a id="agroup__ppp_html_ggac8f3d915c930d61831bcb13d6201b15caa702a3993d2a8f7d7878e1c6f43772d3"></a>
<a id="agroup__ppp_html_ggac8f3d915c930d61831bcb13d6201b15cab135e1ef16bb071e1490d77b51de3bd4"></a>
<a id="agroup__ppp_html_ggac8f3d915c930d61831bcb13d6201b15cabedb2479b9edd3fcefe7a84d2deb41fe"></a>
<a id="agroup__ppp_html_ggac8f3d915c930d61831bcb13d6201b15cae36a806e93ebdacd7c3ad3f536c03743"></a>
<a id="agroup__ppp_html_ggaf30172a9fead40463d129a5afeaf1ac3a0448dc4b9a89736d6878a4e99e6e61b7"></a>
<a id="agroup__ppp_html_ggaf30172a9fead40463d129a5afeaf1ac3ac291788404cda3f6c30130d097d43858"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="agroup__wifi__mgmt_html_ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__mgmt_8h_html"></a>
<a id="anet__pkt_8h_html"></a>
<a id="anet__stats_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructipcp__options_html"></a>
<a id="astructipcp__options_html_a3026cdd5c023b9f1d584e12f9c6e362d"></a>
<a id="astructipcp__options_html_a558db348a124a5a5489b5ca3181ba52e"></a>
<a id="astructipcp__options_html_a703bfd73411418a54e1c769f814f3531"></a>
<a id="astructipv6cp__options_html"></a>
<a id="astructipv6cp__options_html_a4962f03fcf645257306ceeb95116ddce"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructlcp__options_html"></a>
<a id="astructlcp__options_html_a028da648c4b8cdd9330d9195a161e847"></a>
<a id="astructlcp__options_html_a2672e1374c25aac1571adccadda5283e"></a>
<a id="astructlcp__options_html_a3479abfcee498aca22ec2ca461e985d5"></a>
<a id="astructlcp__options_html_a560d009cb642fff99ef83a9e6c056c6b"></a>
<a id="astructlcp__options_html_a68d9f004596bfac6dea9b14bd22e9dda"></a>
<a id="astructlcp__options_html_ae176ccd3d5c747f28023c0621714f340"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__in__addr_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnet__stats__ppp_html"></a>
<a id="astructppp__api_html"></a>
<a id="astructppp__api_html_a42576f1d58920f48a0d0adf888f99006"></a>
<a id="astructppp__api_html_aa0ec35e57f22674ef06f8cc3bc09987f"></a>
<a id="astructppp__api_html_ab85010475c4f03a48ad7629ed4947626"></a>
<a id="astructppp__api_html_acc4e82fbaa8b933040b0a77da8a3cae0"></a>
<a id="astructppp__context_html"></a>
<a id="astructppp__context_html_a1afa42c99b098407f8bba11e50178c84"></a>
<a id="astructppp__context_html_a1c6674bad19047abcc3097bf5ff5f31d"></a>
<a id="astructppp__context_html_a2e04c6e411fe5b07d9d2cda1a61db57f"></a>
<a id="astructppp__context_html_a37f609192ee6b739d7018d5a07ce179f"></a>
<a id="astructppp__context_html_a3b0bfb9c3ceece34565b282efa74390e"></a>
<a id="astructppp__context_html_a3d97c93b183ca455daf0e3bc2b9c25e1"></a>
<a id="astructppp__context_html_a4d91bf9e6e36415b13be02ccf03d3e40"></a>
<a id="astructppp__context_html_a52227a05ce8a63f3a4f7535e60fdf979"></a>
<a id="astructppp__context_html_a5671d7ba465c424004f0460e5ed0d3ba"></a>
<a id="astructppp__context_html_a6afb964ef87696fdadb5cb0c714bd841"></a>
<a id="astructppp__context_html_a6b327cafe07a0807163589471a9bdae8"></a>
<a id="astructppp__context_html_a7705aedba900cf1de66b02ad488b7161"></a>
<a id="astructppp__context_html_a7b4ee6988626cb69c012a0b58c27bef5"></a>
<a id="astructppp__context_html_a7ef9ac6bb1f86ea417032fe93fc7e8a0"></a>
<a id="astructppp__context_html_a7f103857c7412a6ee9471b6c67baea71"></a>
<a id="astructppp__context_html_a80c2c3248c47fac7fce8d463cfbc0c9f"></a>
<a id="astructppp__context_html_a80fffd30b145b0842e36299ac78d5da8"></a>
<a id="astructppp__context_html_a861216f943c5af5d5db58f10ba4263ac"></a>
<a id="astructppp__context_html_a9d9d3bc0e8434ad93d1904905a2ad75f"></a>
<a id="astructppp__context_html_a9dd6e156897c53d488344bbbe05d4ae1"></a>
<a id="astructppp__context_html_ab139c8d6f1d16c702cb9ca92a7f82178"></a>
<a id="astructppp__context_html_ac555024228a1e1d830c915a098428bc5"></a>
<a id="astructppp__context_html_acdee16f229cb6aa0672630de1d3ee39b"></a>
<a id="astructppp__context_html_ae784688e2d78f7427c6672583e326d94"></a>
<a id="astructppp__fsm_html"></a>
<a id="astructppp__fsm_html_a054fd1e61e667072a552eadf54634ffc"></a>
<a id="astructppp__fsm_html_a099cc834fc5e2d062ee4410a1de729c2"></a>
<a id="astructppp__fsm_html_a0a0523fe16fe45a756615b62e8673828"></a>
<a id="astructppp__fsm_html_a0e3cd20db2e06d6d0e85478c013e36db"></a>
<a id="astructppp__fsm_html_a117a5df8fed62b57a59580a2513fc1c3"></a>
<a id="astructppp__fsm_html_a2032a922d2e356155c5a4c86cf48ff3d"></a>
<a id="astructppp__fsm_html_a2ba52396156dd1ec63d67dc6ae0a2d5a"></a>
<a id="astructppp__fsm_html_a31d84f3fa6246bd70d664dbae6845c4b"></a>
<a id="astructppp__fsm_html_a39a7d8b02a0c905ea27565445295c4f2"></a>
<a id="astructppp__fsm_html_a42777bc7c5f904cbac6bb0b16615fb02"></a>
<a id="astructppp__fsm_html_a42bb4a40d88893d461d93202c4ad8e2a"></a>
<a id="astructppp__fsm_html_a489c2d992e03e126ba2d1bbfe7a71b85"></a>
<a id="astructppp__fsm_html_a55c0fe60eb84f33386ec90691ee0f707"></a>
<a id="astructppp__fsm_html_a64330e89597eac2b8b841d0f95389473"></a>
<a id="astructppp__fsm_html_a7e125f9011a9377d18dc523b1f84964f"></a>
<a id="astructppp__fsm_html_a844c8747b299d3614e5ccff892b45d5c"></a>
<a id="astructppp__fsm_html_a8fe52ffe2a17c03ff0432e36c9d43578"></a>
<a id="astructppp__fsm_html_a90dad2f780b4573559c76e6a67e44f4c"></a>
<a id="astructppp__fsm_html_a9192c71ef82436c519ac3b8ccd38a089"></a>
<a id="astructppp__fsm_html_aa1ca37605ab7934c16a5260d531efa00"></a>
<a id="astructppp__fsm_html_aa302cfe79c73fe081d2642cf54d1d3cf"></a>
<a id="astructppp__fsm_html_ab430e0240f35718f6eaf8f9052a4edde"></a>
<a id="astructppp__fsm_html_ab955d11b75231e94ec1613d5c8c027e1"></a>
<a id="astructppp__fsm_html_ad0967edee7fee72368732876ca6bc5e7"></a>
<a id="astructppp__fsm_html_ad7f2d5d09acb298d29ebc60b4f748478"></a>
<a id="astructppp__fsm_html_ae033ee41d66ec568dc4244115730114a"></a>
<a id="astructppp__fsm_html_ae0c0b33d5e51a01a63b5afbf5012c0f5"></a>
<a id="astructppp__fsm_html_ae4f68c11709ab03445b853c12c11c787"></a>
<a id="astructppp__fsm_html_aecdcdfa2f7264c7b1b2202a23327fa3b"></a>
<a id="astructppp__fsm_html_afb0296b0d8e9b60594781cfd5f8acee3"></a>

```c
/*
 * Copyright (c) 2019 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_PPP_H_
#define ZEPHYR_INCLUDE_NET_PPP_H_

#include <zephyr/net/net_if.h>
#include <zephyr/net/net_pkt.h>
#include <zephyr/net/net_stats.h>
#include <zephyr/net/net_mgmt.h>

#ifdef __cplusplus
extern "C" {
#endif


#define PPP_MRU CONFIG_NET_PPP_MTU_MRU

#define PPP_MTU PPP_MRU

#define PPP_MAX_TERMINATE_REASON_LEN 32

#define PPP_INTERFACE_IDENTIFIER_LEN 8

struct ppp_api {
        struct net_if_api iface_api;

        int (*start)(const struct device *dev);

        int (*stop)(const struct device *dev);

        int (*send)(const struct device *dev, struct net_pkt *pkt);

#if defined(CONFIG_NET_STATISTICS_PPP)
        struct net_stats_ppp *(*get_stats)(const struct device *dev);
#endif
};

/* Make sure that the network interface API is properly setup inside
 * PPP API struct (it is the first one).
 */
BUILD_ASSERT(offsetof(struct ppp_api, iface_api) == 0);

enum ppp_protocol_type {
        PPP_IP     = 0x0021,
        PPP_IPV6   = 0x0057,
        PPP_IPCP   = 0x8021,
        PPP_ECP    = 0x8053,
        PPP_IPV6CP = 0x8057,
        PPP_CCP    = 0x80FD,
        PPP_LCP    = 0xc021,
        PPP_PAP    = 0xc023,
        PPP_CHAP   = 0xc223,
        PPP_EAP    = 0xc227,
};

enum ppp_phase {
        PPP_DEAD,
        PPP_ESTABLISH,
        PPP_AUTH,
        PPP_NETWORK,
        PPP_RUNNING,
        PPP_TERMINATE,
};


enum ppp_state {
        PPP_INITIAL,
        PPP_STARTING,
        PPP_CLOSED,
        PPP_STOPPED,
        PPP_CLOSING,
        PPP_STOPPING,
        PPP_REQUEST_SENT,
        PPP_ACK_RECEIVED,
        PPP_ACK_SENT,
        PPP_OPENED
};

enum ppp_packet_type {
        PPP_CONFIGURE_REQ  = 1,
        PPP_CONFIGURE_ACK  = 2,
        PPP_CONFIGURE_NACK = 3,
        PPP_CONFIGURE_REJ  = 4,
        PPP_TERMINATE_REQ  = 5,
        PPP_TERMINATE_ACK  = 6,
        PPP_CODE_REJ       = 7,
        PPP_PROTOCOL_REJ   = 8,
        PPP_ECHO_REQ       = 9,
        PPP_ECHO_REPLY     = 10,
        PPP_DISCARD_REQ    = 11
};


enum lcp_option_type {
        LCP_OPTION_RESERVED = 0,

        LCP_OPTION_MRU = 1,

        LCP_OPTION_ASYNC_CTRL_CHAR_MAP = 2,

        LCP_OPTION_AUTH_PROTO = 3,

        LCP_OPTION_QUALITY_PROTO = 4,

        LCP_OPTION_MAGIC_NUMBER = 5,

        LCP_OPTION_PROTO_COMPRESS = 7,

        LCP_OPTION_ADDR_CTRL_COMPRESS = 8
} __packed;

enum ipcp_option_type {
        IPCP_OPTION_RESERVED = 0,

        IPCP_OPTION_IP_ADDRESSES = 1,

        IPCP_OPTION_IP_COMP_PROTO = 2,

        IPCP_OPTION_IP_ADDRESS = 3,

        /* RFC 1877 */

        IPCP_OPTION_DNS1 = 129,

        IPCP_OPTION_NBNS1 = 130,

        IPCP_OPTION_DNS2 = 131,

        IPCP_OPTION_NBNS2 = 132,
} __packed;

enum ipv6cp_option_type {
        IPV6CP_OPTION_RESERVED = 0,

        IPV6CP_OPTION_INTERFACE_IDENTIFIER = 1,
} __packed;

typedef void (*net_ppp_lcp_echo_reply_cb_t)(void *user_data,
                                            size_t user_data_len);

struct ppp_my_option_data;
struct ppp_my_option_info;

struct ppp_fsm {
        struct k_work_delayable timer;

        struct {
                int (*config_info_ack)(struct ppp_fsm *fsm,
                                       struct net_pkt *pkt,
                                       uint16_t length);

                struct net_pkt *(*config_info_add)(struct ppp_fsm *fsm);

                int  (*config_info_len)(struct ppp_fsm *fsm);

                int (*config_info_nack)(struct ppp_fsm *fsm,
                                        struct net_pkt *pkt,
                                        uint16_t length,
                                        bool rejected);

                int (*config_info_req)(struct ppp_fsm *fsm,
                                       struct net_pkt *pkt,
                                       uint16_t length,
                                       struct net_pkt *ret_pkt);

                int (*config_info_rej)(struct ppp_fsm *fsm,
                                       struct net_pkt *pkt,
                                       uint16_t length);

                void (*config_info_reset)(struct ppp_fsm *fsm);

                void (*up)(struct ppp_fsm *fsm);

                void (*down)(struct ppp_fsm *fsm);

                void (*starting)(struct ppp_fsm *fsm);

                void (*finished)(struct ppp_fsm *fsm);

                void (*proto_reject)(struct ppp_fsm *fsm);

                void (*retransmit)(struct ppp_fsm *fsm);

                enum net_verdict (*proto_extension)(struct ppp_fsm *fsm,
                                                    enum ppp_packet_type code,
                                                    uint8_t id,
                                                    struct net_pkt *pkt);
        } cb;

        struct {
                const struct ppp_my_option_info *info;

                struct ppp_my_option_data *data;

                size_t count;
        } my_options;

        uint32_t flags;
;
        uint32_t retransmits;

        uint32_t nack_loops;

        uint32_t recv_nack_loops;

        char terminate_reason[PPP_MAX_TERMINATE_REASON_LEN];

        uint16_t protocol;

        enum ppp_state state;

        const char *name;

        uint8_t id;

        uint8_t req_id;

        uint8_t ack_received : 1;
};


#define PPP_MY_OPTION_ACKED     BIT(0)
#define PPP_MY_OPTION_REJECTED  BIT(1)

struct ppp_my_option_data {
        uint32_t flags;
};

#if defined(CONFIG_NET_L2_PPP_OPTION_DNS_USE)
#define IPCP_NUM_MY_OPTIONS     3
#else
#define IPCP_NUM_MY_OPTIONS     1
#endif
#define IPV6CP_NUM_MY_OPTIONS   1

enum ppp_flags {
        PPP_CARRIER_UP,
};


struct lcp_options {
        uint32_t magic;

        uint32_t async_map;

        uint16_t mru;

        uint16_t auth_proto;

        bool pfc;

        bool acfc;
};

#define LCP_NUM_MY_OPTIONS      (1                                              \
        + IS_ENABLED(CONFIG_NET_L2_PPP_OPTION_MRU)                      \
        + IS_ENABLED(CONFIG_NET_L2_PPP_OPTION_PFC)                      \
        + IS_ENABLED(CONFIG_NET_L2_PPP_OPTION_ACFC))

struct ipcp_options {
        struct net_in_addr address;

        struct net_in_addr dns1_address;

        struct net_in_addr dns2_address;
};

struct ipv6cp_options {
        uint8_t iid[PPP_INTERFACE_IDENTIFIER_LEN];
};

struct ppp_context {
        atomic_t flags;

        struct k_work_delayable startup;

        struct {
                struct ppp_fsm fsm;

                struct lcp_options my_options;

                struct lcp_options peer_options;

                uint32_t magic;

                struct ppp_my_option_data my_options_data[LCP_NUM_MY_OPTIONS];
        } lcp;

#if defined(CONFIG_NET_IPV4)
        struct {
                struct ppp_fsm fsm;

                struct ipcp_options my_options;

                struct ipcp_options peer_options;

                struct ppp_my_option_data my_options_data[IPCP_NUM_MY_OPTIONS];
        } ipcp;
#endif

#if defined(CONFIG_NET_IPV6)
        struct {
                struct ppp_fsm fsm;

                struct ipv6cp_options my_options;

                struct ipv6cp_options peer_options;

                struct ppp_my_option_data my_options_data[IPV6CP_NUM_MY_OPTIONS];
        } ipv6cp;
#endif

#if defined(CONFIG_NET_L2_PPP_PAP)
        struct {
                struct ppp_fsm fsm;
        } pap;
#endif

#if defined(CONFIG_NET_SHELL)
        struct {
                struct {
                        net_ppp_lcp_echo_reply_cb_t cb;

                        void *user_data;

                        size_t user_data_len;
                } echo_reply;

                struct k_sem wait_echo_reply;

                uint32_t echo_req_data;

                uint32_t echo_reply_data;
        } shell;
#endif

        struct net_if *iface;

        enum ppp_phase phase;

        struct k_sem wait_ppp_link_terminated;

        struct k_sem wait_ppp_link_down;

        enum net_l2_flags ppp_l2_flags;

        int network_protos_open;

        int network_protos_up;

        uint16_t is_ready_to_serve : 1;

        uint16_t is_enabled : 1;

        uint16_t is_enable_done : 1;

        uint16_t is_ipcp_up : 1;

        uint16_t is_ipcp_open : 1;

        uint16_t is_ipv6cp_up : 1;

        uint16_t is_ipv6cp_open : 1;

        uint16_t is_pap_up : 1;

        uint16_t is_pap_open : 1;
};

void net_ppp_init(struct net_if *iface);

/* Management API for PPP */


#define PPP_L2_CTX_TYPE struct ppp_context

#define NET_PPP_LAYER   NET_MGMT_LAYER_L2
#define NET_PPP_CODE    NET_MGMT_LAYER_CODE_PPP
#define NET_PPP_BASE    (NET_MGMT_IFACE_BIT |                           \
                         NET_MGMT_LAYER(NET_PPP_LAYER) |                \
                         NET_MGMT_LAYER_CODE(NET_PPP_CODE))
#define NET_PPP_EVENT   (NET_PPP_BASE | NET_MGMT_EVENT_BIT)

enum {
        NET_EVENT_PPP_CMD_CARRIER_ON_VAL,
        NET_EVENT_PPP_CMD_CARRIER_OFF_VAL,
        NET_EVENT_PPP_CMD_PHASE_RUNNING_VAL,
        NET_EVENT_PPP_CMD_PHASE_DEAD_VAL,

        NET_EVENT_PPP_CMD_MAX
};

BUILD_ASSERT(NET_EVENT_PPP_CMD_MAX <= NET_MGMT_MAX_COMMANDS,
             "Number of events in net_event_ppp_cmd exceeds the limit");

enum net_event_ppp_cmd {
        NET_MGMT_CMD(NET_EVENT_PPP_CMD_CARRIER_ON),
        NET_MGMT_CMD(NET_EVENT_PPP_CMD_CARRIER_OFF),
        NET_MGMT_CMD(NET_EVENT_PPP_CMD_PHASE_RUNNING),
        NET_MGMT_CMD(NET_EVENT_PPP_CMD_PHASE_DEAD),
};

struct net_if;


#define NET_PPP_DEFAULT_ASYNC_MAP (0xffffffffU)

uint32_t ppp_peer_async_control_character_map(struct net_if *iface);

#define NET_EVENT_PPP_CARRIER_ON                                        \
        (NET_PPP_EVENT | NET_EVENT_PPP_CMD_CARRIER_ON)

#define NET_EVENT_PPP_CARRIER_OFF                                       \
        (NET_PPP_EVENT | NET_EVENT_PPP_CMD_CARRIER_OFF)

#define NET_EVENT_PPP_PHASE_RUNNING                                     \
        (NET_PPP_EVENT | NET_EVENT_PPP_CMD_PHASE_RUNNING)

#define NET_EVENT_PPP_PHASE_DEAD                                        \
        (NET_PPP_EVENT | NET_EVENT_PPP_CMD_PHASE_DEAD)

#if defined(CONFIG_NET_L2_PPP_MGMT)
void ppp_mgmt_raise_carrier_on_event(struct net_if *iface);
#else
static inline void ppp_mgmt_raise_carrier_on_event(struct net_if *iface)
{
        ARG_UNUSED(iface);
}
#endif

#if defined(CONFIG_NET_L2_PPP_MGMT)
void ppp_mgmt_raise_carrier_off_event(struct net_if *iface);
#else
static inline void ppp_mgmt_raise_carrier_off_event(struct net_if *iface)
{
        ARG_UNUSED(iface);
}
#endif

#if defined(CONFIG_NET_L2_PPP_MGMT)
void ppp_mgmt_raise_phase_running_event(struct net_if *iface);
#else
static inline void ppp_mgmt_raise_phase_running_event(struct net_if *iface)
{
        ARG_UNUSED(iface);
}
#endif

#if defined(CONFIG_NET_L2_PPP_MGMT)
void ppp_mgmt_raise_phase_dead_event(struct net_if *iface);
#else
static inline void ppp_mgmt_raise_phase_dead_event(struct net_if *iface)
{
        ARG_UNUSED(iface);
}
#endif

#if defined(CONFIG_NET_L2_PPP)
int net_ppp_ping(int idx, int32_t timeout);
#else
static inline int net_ppp_ping(int idx, int32_t timeout)
{
        ARG_UNUSED(idx);
        ARG_UNUSED(timeout);

        return -ENOTSUP;
}
#endif

#if defined(CONFIG_NET_L2_PPP) && defined(CONFIG_NET_SHELL)
struct ppp_context *net_ppp_context_get(int idx);
#else
static inline struct ppp_context *net_ppp_context_get(int idx)
{
        ARG_UNUSED(idx);

        return NULL;
}
#endif

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_PPP_H_ */
```

## 45.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 71 行

确保网络接口 API 正确放置在 PPP API 结构体内，即作为其第一个成员。

### 注释 3：原第 194 行

RFC 1877。

### 注释 4：原第 566 行

PPP 管理 API（Management API）。

### 注释 5：原第 739 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PPP_H_`。

## 45.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h.html)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [ppp_api](../network_service_model_reference/P042_ppp_api_结构体.md)
- [iface_api](../network_service_model_reference/P042_ppp_api_结构体.md#acc4e82fbaa8b933040b0a77da8a3cae0)
- [start](../network_service_model_reference/P042_ppp_api_结构体.md#ab85010475c4f03a48ad7629ed4947626)
- [device](../device_reference/P002_设备对象结构.md)
- [stop](../network_service_model_reference/P042_ppp_api_结构体.md#a42576f1d58920f48a0d0adf888f99006)
- [send](../network_service_model_reference/P042_ppp_api_结构体.md#aa0ec35e57f22674ef06f8cc3bc09987f)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_stats_ppp](../network_core_model_reference/P144_net_stats_ppp_结构体.md)
- [ppp_protocol_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga8ad7cc0d142a6e7ea82c45bec2cc3670)
- [PPP_IP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0b974fd7b99c28a8d06f096be1ed9cc6)
- [PPP_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0a9da56ae134b701f5a8b31c3f1c9bfe)
- [PPP_IPCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a25f326220ab531e93140b7c6bddd0d21)
- [PPP_ECP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a40b5032dabf9c697e761aa2cff0b2e44)
- [PPP_IPV6CP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670ab17a70f864ac04b8b52f8ca1edc4d2e0)
- [PPP_CCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a4cdde6fe10fcfa862742751e1152887b)
- [PPP_LCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a22dae8ee345f9664042eef54086f4de9)
- [PPP_PAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670ac66b190ff6dd0884dfba62da40ee2206)
- [PPP_CHAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a1b311302ecabb507c34b1f77cba36f25)
- [PPP_EAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a7a51ef2d8d979ded98e0aad680f1b6e2)
- [ppp_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga284e237a6323f2daffc444a73a4b8b6b)
- [PPP_DEAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6babdff682a09630e713867c3241d56954d)
- [PPP_ESTABLISH](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6ba647d283023ee50299c1d9ca376cce4f4)
- [PPP_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6ba0492bfbaebc3f126327c74dbe56ce76a)
- [PPP_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6ba621902d0a6ca3efa0aa20c43c32164af)
- [PPP_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6ba51a5c6e5d16fbb607597f0d2f6a12af7)
- [PPP_TERMINATE](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6bac1f10a2aa5edcb826621304de596a5b7)
- [lcp_option_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gac8f3d915c930d61831bcb13d6201b15c)
- [LCP_OPTION_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15caa702a3993d2a8f7d7878e1c6f43772d3)
- [LCP_OPTION_MRU](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15cabedb2479b9edd3fcefe7a84d2deb41fe)
- [LCP_OPTION_ASYNC_CTRL_CHAR_MAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15ca01e51712c002e5ce746d93376b4f2cef)
- [LCP_OPTION_AUTH_PROTO](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15cae36a806e93ebdacd7c3ad3f536c03743)
- [LCP_OPTION_QUALITY_PROTO](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15ca3ed6d42c4b65271955a308c4e7a437a9)
- [LCP_OPTION_MAGIC_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15ca59c791ebec909b03a42659d08be2bcf8)
- [LCP_OPTION_PROTO_COMPRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15cab135e1ef16bb071e1490d77b51de3bd4)
- [LCP_OPTION_ADDR_CTRL_COMPRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15ca3c37fd8819b98caa7f9b3b94aff53524)
- [ipcp_option_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga1064e3d8c6aa3d3161e399d6937162b6)
- [IPCP_OPTION_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a7319a35a35044ca3f5fcc1ed6460fb3b)
- [IPCP_OPTION_IP_ADDRESSES](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a80771bc5d12ab8dcf78f87c872b0f41b)
- [IPCP_OPTION_IP_COMP_PROTO](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a3913e2668196db10d17f8d7ffa86c6a6)
- [IPCP_OPTION_IP_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a124bafb002549c2de4cb293f5e158fd9)
- [IPCP_OPTION_DNS1](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6af156d53ee18de3907210c910667e8931)
- [IPCP_OPTION_NBNS1](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a7d154ff3643ba4de8cf358bd81361552)
- [IPCP_OPTION_DNS2](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a176055a8c0483c7c8b6b0d416b676964)
- [IPCP_OPTION_NBNS2](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a3b315dc4f10305923bba2bfbe2fa05ad)
- [ipv6cp_option_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaf30172a9fead40463d129a5afeaf1ac3)
- [IPV6CP_OPTION_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggaf30172a9fead40463d129a5afeaf1ac3ac291788404cda3f6c30130d097d43858)
- [IPV6CP_OPTION_INTERFACE_IDENTIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggaf30172a9fead40463d129a5afeaf1ac3a0448dc4b9a89736d6878a4e99e6e61b7)
- [net_ppp_lcp_echo_reply_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga15afa05abc0446201c912c75644306bf)
- [ppp_fsm](../network_service_model_reference/P044_ppp_fsm_结构体.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [timer](../network_service_model_reference/P044_ppp_fsm_结构体.md#ae033ee41d66ec568dc4244115730114a)
- [config_info_ack](../network_service_model_reference/P044_ppp_fsm_结构体.md#a42bb4a40d88893d461d93202c4ad8e2a)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [config_info_len](../network_service_model_reference/P044_ppp_fsm_结构体.md#a099cc834fc5e2d062ee4410a1de729c2)
- [config_info_nack](../network_service_model_reference/P044_ppp_fsm_结构体.md#ad0967edee7fee72368732876ca6bc5e7)
- [config_info_req](../network_service_model_reference/P044_ppp_fsm_结构体.md#ab430e0240f35718f6eaf8f9052a4edde)
- [config_info_rej](../network_service_model_reference/P044_ppp_fsm_结构体.md#a90dad2f780b4573559c76e6a67e44f4c)
- [config_info_reset](../network_service_model_reference/P044_ppp_fsm_结构体.md#afb0296b0d8e9b60594781cfd5f8acee3)
- [up](../network_service_model_reference/P044_ppp_fsm_结构体.md#aa1ca37605ab7934c16a5260d531efa00)
- [down](../network_service_model_reference/P044_ppp_fsm_结构体.md#a2ba52396156dd1ec63d67dc6ae0a2d5a)
- [starting](../network_service_model_reference/P044_ppp_fsm_结构体.md#ad7f2d5d09acb298d29ebc60b4f748478)
- [finished](../network_service_model_reference/P044_ppp_fsm_结构体.md#aecdcdfa2f7264c7b1b2202a23327fa3b)
- [proto_reject](../network_service_model_reference/P044_ppp_fsm_结构体.md#ae4f68c11709ab03445b853c12c11c787)
- [retransmit](../network_service_model_reference/P044_ppp_fsm_结构体.md#ae0c0b33d5e51a01a63b5afbf5012c0f5)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [proto_extension](../network_service_model_reference/P044_ppp_fsm_结构体.md#aa302cfe79c73fe081d2642cf54d1d3cf)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [id](../network_service_model_reference/P044_ppp_fsm_结构体.md#a844c8747b299d3614e5ccff892b45d5c)
- [cb](../network_service_model_reference/P044_ppp_fsm_结构体.md#a0e3cd20db2e06d6d0e85478c013e36db)
- [info](../network_service_model_reference/P044_ppp_fsm_结构体.md#a117a5df8fed62b57a59580a2513fc1c3)
- [data](../network_service_model_reference/P044_ppp_fsm_结构体.md#a64330e89597eac2b8b841d0f95389473)
- [count](../network_service_model_reference/P044_ppp_fsm_结构体.md#a7e125f9011a9377d18dc523b1f84964f)
- [my_options](../network_service_model_reference/P044_ppp_fsm_结构体.md#a39a7d8b02a0c905ea27565445295c4f2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](../network_service_model_reference/P044_ppp_fsm_结构体.md#a489c2d992e03e126ba2d1bbfe7a71b85)
- [retransmits](../network_service_model_reference/P044_ppp_fsm_结构体.md#a31d84f3fa6246bd70d664dbae6845c4b)
- [nack_loops](../network_service_model_reference/P044_ppp_fsm_结构体.md#a0a0523fe16fe45a756615b62e8673828)
- [recv_nack_loops](../network_service_model_reference/P044_ppp_fsm_结构体.md#a55c0fe60eb84f33386ec90691ee0f707)
- [terminate_reason](../network_service_model_reference/P044_ppp_fsm_结构体.md#a054fd1e61e667072a552eadf54634ffc)
- [PPP_MAX_TERMINATE_REASON_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga2e5d0ae66bf076123cb29effc0a8e894)
- [protocol](../network_service_model_reference/P044_ppp_fsm_结构体.md#a2032a922d2e356155c5a4c86cf48ff3d)
- [state](../network_service_model_reference/P044_ppp_fsm_结构体.md#ab955d11b75231e94ec1613d5c8c027e1)
- [name](../network_service_model_reference/P044_ppp_fsm_结构体.md#a9192c71ef82436c519ac3b8ccd38a089)
- [req_id](../network_service_model_reference/P044_ppp_fsm_结构体.md#a8fe52ffe2a17c03ff0432e36c9d43578)
- [ack_received](../network_service_model_reference/P044_ppp_fsm_结构体.md#a42777bc7c5f904cbac6bb0b16615fb02)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [lcp_options](../network_service_model_reference/P028_lcp_options_结构体.md)
- [magic](../network_service_model_reference/P028_lcp_options_结构体.md#a68d9f004596bfac6dea9b14bd22e9dda)
- [async_map](../network_service_model_reference/P028_lcp_options_结构体.md#a2672e1374c25aac1571adccadda5283e)
- [mru](../network_service_model_reference/P028_lcp_options_结构体.md#a028da648c4b8cdd9330d9195a161e847)
- [auth_proto](../network_service_model_reference/P028_lcp_options_结构体.md#a560d009cb642fff99ef83a9e6c056c6b)
- [pfc](../network_service_model_reference/P028_lcp_options_结构体.md#ae176ccd3d5c747f28023c0621714f340)
- [acfc](../network_service_model_reference/P028_lcp_options_结构体.md#a3479abfcee498aca22ec2ca461e985d5)
- [ipcp_options](../network_service_model_reference/P026_ipcp_options_结构体.md)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [address](../network_service_model_reference/P026_ipcp_options_结构体.md#a703bfd73411418a54e1c769f814f3531)
- [dns1_address](../network_service_model_reference/P026_ipcp_options_结构体.md#a558db348a124a5a5489b5ca3181ba52e)
- [dns2_address](../network_service_model_reference/P026_ipcp_options_结构体.md#a3026cdd5c023b9f1d584e12f9c6e362d)
- [ipv6cp_options](../network_service_model_reference/P027_ipv6cp_options_结构体.md)
- [iid](../network_service_model_reference/P027_ipv6cp_options_结构体.md#a4962f03fcf645257306ceeb95116ddce)
- [PPP_INTERFACE_IDENTIFIER_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaad7380b3a502f4b649348b733124f21a)
- [ppp_context](../network_service_model_reference/P043_ppp_context_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [flags](../network_service_model_reference/P043_ppp_context_结构体.md#a6b327cafe07a0807163589471a9bdae8)
- [startup](../network_service_model_reference/P043_ppp_context_结构体.md#a5671d7ba465c424004f0460e5ed0d3ba)
- [fsm](../network_service_model_reference/P043_ppp_context_结构体.md#ac555024228a1e1d830c915a098428bc5)
- [my_options](../network_service_model_reference/P043_ppp_context_结构体.md#a37f609192ee6b739d7018d5a07ce179f)
- [peer_options](../network_service_model_reference/P043_ppp_context_结构体.md#a80fffd30b145b0842e36299ac78d5da8)
- [magic](../network_service_model_reference/P043_ppp_context_结构体.md#a4d91bf9e6e36415b13be02ccf03d3e40)
- [my_options_data](../network_service_model_reference/P043_ppp_context_结构体.md#a9d9d3bc0e8434ad93d1904905a2ad75f)
- [LCP_NUM_MY_OPTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaa584f3427a21343ab692b5ec3a9573ec)
- [lcp](../network_service_model_reference/P043_ppp_context_结构体.md#a7705aedba900cf1de66b02ad488b7161)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [iface](../network_service_model_reference/P043_ppp_context_结构体.md#a3b0bfb9c3ceece34565b282efa74390e)
- [phase](../network_service_model_reference/P043_ppp_context_结构体.md#a6afb964ef87696fdadb5cb0c714bd841)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [wait_ppp_link_terminated](../network_service_model_reference/P043_ppp_context_结构体.md#a1afa42c99b098407f8bba11e50178c84)
- [wait_ppp_link_down](../network_service_model_reference/P043_ppp_context_结构体.md#ae784688e2d78f7427c6672583e326d94)
- [net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)
- [ppp_l2_flags](../network_service_model_reference/P043_ppp_context_结构体.md#a1c6674bad19047abcc3097bf5ff5f31d)
- [network_protos_open](../network_service_model_reference/P043_ppp_context_结构体.md#a2e04c6e411fe5b07d9d2cda1a61db57f)
- [network_protos_up](../network_service_model_reference/P043_ppp_context_结构体.md#a9dd6e156897c53d488344bbbe05d4ae1)
- [is_ready_to_serve](../network_service_model_reference/P043_ppp_context_结构体.md#a3d97c93b183ca455daf0e3bc2b9c25e1)
- [is_enabled](../network_service_model_reference/P043_ppp_context_结构体.md#a7f103857c7412a6ee9471b6c67baea71)
- [is_enable_done](../network_service_model_reference/P043_ppp_context_结构体.md#acdee16f229cb6aa0672630de1d3ee39b)
- [is_ipcp_up](../network_service_model_reference/P043_ppp_context_结构体.md#a861216f943c5af5d5db58f10ba4263ac)
- [is_ipcp_open](../network_service_model_reference/P043_ppp_context_结构体.md#a7ef9ac6bb1f86ea417032fe93fc7e8a0)
- [is_ipv6cp_up](../network_service_model_reference/P043_ppp_context_结构体.md#a7b4ee6988626cb69c012a0b58c27bef5)
- [is_ipv6cp_open](../network_service_model_reference/P043_ppp_context_结构体.md#ab139c8d6f1d16c702cb9ca92a7f82178)
- [is_pap_up](../network_service_model_reference/P043_ppp_context_结构体.md#a52227a05ce8a63f3a4f7535e60fdf979)
- [is_pap_open](../network_service_model_reference/P043_ppp_context_结构体.md#a80c2c3248c47fac7fce8d463cfbc0c9f)
- [net_ppp_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaabf883cfefc9910b9b9d8931e68b320c)
- [NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)
- [ppp_peer_async_control_character_map](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga716727874cecc8ee358da6c76adedc0a)
- [ppp_mgmt_raise_carrier_on_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga1436cf5cfcb6752e41c9e06a0ee30030)
- [ppp_mgmt_raise_carrier_off_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gad96b2c77cf6a066d55d78c5d63cb9bd0)
- [ppp_mgmt_raise_phase_running_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga74e94e9fcae30bc386c5e3d951ed5882)
- [ppp_mgmt_raise_phase_dead_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gad7f41d9012098ed1a04f897e252cc32d)
- [net_ppp_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga9893a7c93b3d23b96b4d83aa1204c500)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [net_ppp_context_get](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga4f6104cff735f9829762b6552a7346bf)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h.html)
- [ipcp_options::dns2_address](../network_service_model_reference/P026_ipcp_options_结构体.md#a3026cdd5c023b9f1d584e12f9c6e362d)
- [ipcp_options::dns1_address](../network_service_model_reference/P026_ipcp_options_结构体.md#a558db348a124a5a5489b5ca3181ba52e)
- [ipcp_options::address](../network_service_model_reference/P026_ipcp_options_结构体.md#a703bfd73411418a54e1c769f814f3531)
- [ipv6cp_options::iid](../network_service_model_reference/P027_ipv6cp_options_结构体.md#a4962f03fcf645257306ceeb95116ddce)
- [lcp_options::mru](../network_service_model_reference/P028_lcp_options_结构体.md#a028da648c4b8cdd9330d9195a161e847)
- [lcp_options::async_map](../network_service_model_reference/P028_lcp_options_结构体.md#a2672e1374c25aac1571adccadda5283e)
- [lcp_options::acfc](../network_service_model_reference/P028_lcp_options_结构体.md#a3479abfcee498aca22ec2ca461e985d5)
- [lcp_options::auth_proto](../network_service_model_reference/P028_lcp_options_结构体.md#a560d009cb642fff99ef83a9e6c056c6b)
- [lcp_options::magic](../network_service_model_reference/P028_lcp_options_结构体.md#a68d9f004596bfac6dea9b14bd22e9dda)
- [lcp_options::pfc](../network_service_model_reference/P028_lcp_options_结构体.md#ae176ccd3d5c747f28023c0621714f340)
- [ppp_api::stop](../network_service_model_reference/P042_ppp_api_结构体.md#a42576f1d58920f48a0d0adf888f99006)
- [ppp_api::send](../network_service_model_reference/P042_ppp_api_结构体.md#aa0ec35e57f22674ef06f8cc3bc09987f)
- [ppp_api::start](../network_service_model_reference/P042_ppp_api_结构体.md#ab85010475c4f03a48ad7629ed4947626)
- [ppp_api::iface_api](../network_service_model_reference/P042_ppp_api_结构体.md#acc4e82fbaa8b933040b0a77da8a3cae0)
- [ppp_context::wait_ppp_link_terminated](../network_service_model_reference/P043_ppp_context_结构体.md#a1afa42c99b098407f8bba11e50178c84)
- [ppp_context::ppp_l2_flags](../network_service_model_reference/P043_ppp_context_结构体.md#a1c6674bad19047abcc3097bf5ff5f31d)
- [ppp_context::network_protos_open](../network_service_model_reference/P043_ppp_context_结构体.md#a2e04c6e411fe5b07d9d2cda1a61db57f)
- [ppp_context::my_options](../network_service_model_reference/P043_ppp_context_结构体.md#a37f609192ee6b739d7018d5a07ce179f)
- [ppp_context::iface](../network_service_model_reference/P043_ppp_context_结构体.md#a3b0bfb9c3ceece34565b282efa74390e)
- [ppp_context::is_ready_to_serve](../network_service_model_reference/P043_ppp_context_结构体.md#a3d97c93b183ca455daf0e3bc2b9c25e1)
- [ppp_context::magic](../network_service_model_reference/P043_ppp_context_结构体.md#a4d91bf9e6e36415b13be02ccf03d3e40)
- [ppp_context::is_pap_up](../network_service_model_reference/P043_ppp_context_结构体.md#a52227a05ce8a63f3a4f7535e60fdf979)
- [ppp_context::startup](../network_service_model_reference/P043_ppp_context_结构体.md#a5671d7ba465c424004f0460e5ed0d3ba)
- [ppp_context::phase](../network_service_model_reference/P043_ppp_context_结构体.md#a6afb964ef87696fdadb5cb0c714bd841)
- [ppp_context::flags](../network_service_model_reference/P043_ppp_context_结构体.md#a6b327cafe07a0807163589471a9bdae8)
- [ppp_context::lcp](../network_service_model_reference/P043_ppp_context_结构体.md#a7705aedba900cf1de66b02ad488b7161)
- [ppp_context::is_ipv6cp_up](../network_service_model_reference/P043_ppp_context_结构体.md#a7b4ee6988626cb69c012a0b58c27bef5)
- [ppp_context::is_ipcp_open](../network_service_model_reference/P043_ppp_context_结构体.md#a7ef9ac6bb1f86ea417032fe93fc7e8a0)
- [ppp_context::is_enabled](../network_service_model_reference/P043_ppp_context_结构体.md#a7f103857c7412a6ee9471b6c67baea71)
- [ppp_context::is_pap_open](../network_service_model_reference/P043_ppp_context_结构体.md#a80c2c3248c47fac7fce8d463cfbc0c9f)
- [ppp_context::peer_options](../network_service_model_reference/P043_ppp_context_结构体.md#a80fffd30b145b0842e36299ac78d5da8)
- [ppp_context::is_ipcp_up](../network_service_model_reference/P043_ppp_context_结构体.md#a861216f943c5af5d5db58f10ba4263ac)
- [ppp_context::my_options_data](../network_service_model_reference/P043_ppp_context_结构体.md#a9d9d3bc0e8434ad93d1904905a2ad75f)
- [ppp_context::network_protos_up](../network_service_model_reference/P043_ppp_context_结构体.md#a9dd6e156897c53d488344bbbe05d4ae1)
- [ppp_context::is_ipv6cp_open](../network_service_model_reference/P043_ppp_context_结构体.md#ab139c8d6f1d16c702cb9ca92a7f82178)
- [ppp_context::fsm](../network_service_model_reference/P043_ppp_context_结构体.md#ac555024228a1e1d830c915a098428bc5)
- [ppp_context::is_enable_done](../network_service_model_reference/P043_ppp_context_结构体.md#acdee16f229cb6aa0672630de1d3ee39b)
- [ppp_context::wait_ppp_link_down](../network_service_model_reference/P043_ppp_context_结构体.md#ae784688e2d78f7427c6672583e326d94)
- [ppp_fsm::terminate_reason](../network_service_model_reference/P044_ppp_fsm_结构体.md#a054fd1e61e667072a552eadf54634ffc)
- [ppp_fsm::config_info_len](../network_service_model_reference/P044_ppp_fsm_结构体.md#a099cc834fc5e2d062ee4410a1de729c2)
- [ppp_fsm::nack_loops](../network_service_model_reference/P044_ppp_fsm_结构体.md#a0a0523fe16fe45a756615b62e8673828)
- [ppp_fsm::cb](../network_service_model_reference/P044_ppp_fsm_结构体.md#a0e3cd20db2e06d6d0e85478c013e36db)
- [ppp_fsm::info](../network_service_model_reference/P044_ppp_fsm_结构体.md#a117a5df8fed62b57a59580a2513fc1c3)
- [ppp_fsm::protocol](../network_service_model_reference/P044_ppp_fsm_结构体.md#a2032a922d2e356155c5a4c86cf48ff3d)
- [ppp_fsm::down](../network_service_model_reference/P044_ppp_fsm_结构体.md#a2ba52396156dd1ec63d67dc6ae0a2d5a)
- [ppp_fsm::retransmits](../network_service_model_reference/P044_ppp_fsm_结构体.md#a31d84f3fa6246bd70d664dbae6845c4b)
- [ppp_fsm::my_options](../network_service_model_reference/P044_ppp_fsm_结构体.md#a39a7d8b02a0c905ea27565445295c4f2)
- [ppp_fsm::ack_received](../network_service_model_reference/P044_ppp_fsm_结构体.md#a42777bc7c5f904cbac6bb0b16615fb02)
- [ppp_fsm::config_info_ack](../network_service_model_reference/P044_ppp_fsm_结构体.md#a42bb4a40d88893d461d93202c4ad8e2a)
- [ppp_fsm::flags](../network_service_model_reference/P044_ppp_fsm_结构体.md#a489c2d992e03e126ba2d1bbfe7a71b85)
- [ppp_fsm::recv_nack_loops](../network_service_model_reference/P044_ppp_fsm_结构体.md#a55c0fe60eb84f33386ec90691ee0f707)
- [ppp_fsm::data](../network_service_model_reference/P044_ppp_fsm_结构体.md#a64330e89597eac2b8b841d0f95389473)
- [ppp_fsm::count](../network_service_model_reference/P044_ppp_fsm_结构体.md#a7e125f9011a9377d18dc523b1f84964f)
- [ppp_fsm::id](../network_service_model_reference/P044_ppp_fsm_结构体.md#a844c8747b299d3614e5ccff892b45d5c)
- [ppp_fsm::req_id](../network_service_model_reference/P044_ppp_fsm_结构体.md#a8fe52ffe2a17c03ff0432e36c9d43578)
- [ppp_fsm::config_info_rej](../network_service_model_reference/P044_ppp_fsm_结构体.md#a90dad2f780b4573559c76e6a67e44f4c)
- [ppp_fsm::name](../network_service_model_reference/P044_ppp_fsm_结构体.md#a9192c71ef82436c519ac3b8ccd38a089)
- [ppp_fsm::up](../network_service_model_reference/P044_ppp_fsm_结构体.md#aa1ca37605ab7934c16a5260d531efa00)
- [ppp_fsm::proto_extension](../network_service_model_reference/P044_ppp_fsm_结构体.md#aa302cfe79c73fe081d2642cf54d1d3cf)
- [ppp_fsm::config_info_req](../network_service_model_reference/P044_ppp_fsm_结构体.md#ab430e0240f35718f6eaf8f9052a4edde)
- [ppp_fsm::state](../network_service_model_reference/P044_ppp_fsm_结构体.md#ab955d11b75231e94ec1613d5c8c027e1)
- [ppp_fsm::config_info_nack](../network_service_model_reference/P044_ppp_fsm_结构体.md#ad0967edee7fee72368732876ca6bc5e7)
- [ppp_fsm::starting](../network_service_model_reference/P044_ppp_fsm_结构体.md#ad7f2d5d09acb298d29ebc60b4f748478)
- [ppp_fsm::timer](../network_service_model_reference/P044_ppp_fsm_结构体.md#ae033ee41d66ec568dc4244115730114a)
- [ppp_fsm::retransmit](../network_service_model_reference/P044_ppp_fsm_结构体.md#ae0c0b33d5e51a01a63b5afbf5012c0f5)
- [ppp_fsm::proto_reject](../network_service_model_reference/P044_ppp_fsm_结构体.md#ae4f68c11709ab03445b853c12c11c787)
- [ppp_fsm::finished](../network_service_model_reference/P044_ppp_fsm_结构体.md#aecdcdfa2f7264c7b1b2202a23327fa3b)
- [ppp_fsm::config_info_reset](../network_service_model_reference/P044_ppp_fsm_结构体.md#afb0296b0d8e9b60594781cfd5f8acee3)

---

[上一章](P044_mpipe_thread.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P046_nxp-fmeas.h_源码浏览.md)
