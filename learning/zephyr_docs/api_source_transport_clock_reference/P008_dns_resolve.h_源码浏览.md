---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-8
title: dns_resolve.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_dns\_resolve.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h.html)。

## 8.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00036"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
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
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00296"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="foldopen00334"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="foldopen00342"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="foldopen00350"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="foldopen00364"></a>
<a id="l00364"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="foldopen00376"></a>
<a id="l00376"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00382"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00387"></a>
<a id="l00389"></a>
<a id="l00392"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00401"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00407"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="foldopen00422"></a>
<a id="l00422"></a>
<a id="l00424"></a>
<a id="l00426"></a>
<a id="l00428"></a>
<a id="l00430"></a>
<a id="l00432"></a>
<a id="l00434"></a>
<a id="l00436"></a>
<a id="l00438"></a>
<a id="l00440"></a>
<a id="l00442"></a>
<a id="l00444"></a>
<a id="l00446"></a>
<a id="l00448"></a>
<a id="l00450"></a>
<a id="l00452"></a>
<a id="l00454"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00505"></a>
<a id="foldopen00509"></a>
<a id="l00509"></a>
<a id="foldopen00511"></a>
<a id="l00511"></a>
<a id="l00513"></a>
<a id="l00515"></a>
<a id="l00517"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00543"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00549"></a>
<a id="l00551"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="foldopen00566"></a>
<a id="l00566"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00627"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00652"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00678"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="foldopen00930"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="l00933"></a>
<a id="l00934"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="l00938"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00951"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="foldopen00965"></a>
<a id="l00965"></a>
<a id="l00966"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="l00970"></a>
<a id="l00971"></a>
<a id="foldopen01000"></a>
<a id="l01000"></a>
<a id="l01001"></a>
<a id="l01002"></a>
<a id="l01003"></a>
<a id="l01004"></a>
<a id="l01005"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="l01009"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01012"></a>
<a id="l01013"></a>
<a id="l01014"></a>
<a id="l01015"></a>
<a id="foldopen01025"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="foldopen01041"></a>
<a id="l01041"></a>
<a id="l01042"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01054"></a>
<a id="l01056"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="l01069"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="l01073"></a>
<a id="l01074"></a>
<a id="l01075"></a>
<a id="l01077"></a>
<a id="l01078"></a>
<a id="l01079"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01082"></a>
<a id="aatomic_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__dns__resolve_html_ga13a7cbc3b59a12278f4b035013c03b1d"></a>
<a id="agroup__dns__resolve_html_ga1d3bb0319531bfe0ae95f48bdc51c56f"></a>
<a id="agroup__dns__resolve_html_ga24f9bc24e2021b6b528bb15e4fcca49b"></a>
<a id="agroup__dns__resolve_html_ga27a85c421014373f6aad89634adf8c7d"></a>
<a id="agroup__dns__resolve_html_ga3326e98da31313d33861565fe0a10bdf"></a>
<a id="agroup__dns__resolve_html_ga3cf4e94af65585d89b4a0650dbd9d46e"></a>
<a id="agroup__dns__resolve_html_ga3d22eed1d6d017e5bd7a2344775d33b7"></a>
<a id="agroup__dns__resolve_html_ga4db137a83d3917bcad1489e25a639666"></a>
<a id="agroup__dns__resolve_html_ga54ae7aaf53b36951b27f09e1cc82df55"></a>
<a id="agroup__dns__resolve_html_ga54c85b9c69c9a44f2e7bb78165cebfcb"></a>
<a id="agroup__dns__resolve_html_ga5baf1fea0482fb3a940b4f5350a3c58e"></a>
<a id="agroup__dns__resolve_html_ga7169c5a920fb1b0d77910a6ab922e3f0"></a>
<a id="agroup__dns__resolve_html_ga71eab0f9dd0bc7c02c0d55e7dc6741f3"></a>
<a id="agroup__dns__resolve_html_ga7701ddd6b6c5923f0d122a2bcf898cbf"></a>
<a id="agroup__dns__resolve_html_ga7892b3eda301db358b1f18720a2f638c"></a>
<a id="agroup__dns__resolve_html_ga7b6c39611abd40d2d0510c9e38383ecc"></a>
<a id="agroup__dns__resolve_html_ga8a4330071b7161e1738dd91b1f6d6097"></a>
<a id="agroup__dns__resolve_html_ga924d2d4d3b5205a605f4ab69dffdf294"></a>
<a id="agroup__dns__resolve_html_gab04f3b2347e9c59346c10180c6c9ffbc"></a>
<a id="agroup__dns__resolve_html_gaba564a71c4fb4c44fae69015e880b0db"></a>
<a id="agroup__dns__resolve_html_gac709b355684d44e943c26c6953187df4"></a>
<a id="agroup__dns__resolve_html_gac8a1d620f07641e4e64ad0757c31aa45"></a>
<a id="agroup__dns__resolve_html_gae292786587c511c223481f77a4f43017"></a>
<a id="agroup__dns__resolve_html_gae69cd758e99ea93ef8aac28366918b87"></a>
<a id="agroup__dns__resolve_html_gaeda02f82b12e9b7b4dea9fd66be123a7"></a>
<a id="agroup__dns__resolve_html_gaf2854ca9b839e7cba073e75202ac7e38"></a>
<a id="agroup__dns__resolve_html_gaf28f6f8baa97d0b2341e1bdc02b6cb8c"></a>
<a id="agroup__dns__resolve_html_gaf491764b213a891f296c9f91c35b1b72"></a>
<a id="agroup__dns__resolve_html_gaf891d7e21bddc8fbd029209b4339c01d"></a>
<a id="agroup__dns__resolve_html_gafe22d0ef90c581982561ef0c33d1f722"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea8440de8b7109dfcca71acca6c7ac4103"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58ea9989bb26c930dcf90b5aaab224f19793"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58eaba718125a826939380fdbcc9c1fb4512"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58eae932d5596c55d090cf2ebe43ad59bd35"></a>
<a id="agroup__dns__resolve_html_gga5baf1fea0482fb3a940b4f5350a3c58eaeb7d2677167f5bc230da2eea2a81d06c"></a>
<a id="agroup__dns__resolve_html_gga7169c5a920fb1b0d77910a6ab922e3f0a0b8a4c108a7ae4742d2235b64c3d8c06"></a>
<a id="agroup__dns__resolve_html_gga7169c5a920fb1b0d77910a6ab922e3f0a128aa925168ae2b096ff879c7648d2e4"></a>
<a id="agroup__dns__resolve_html_gga7169c5a920fb1b0d77910a6ab922e3f0a2e976a8ed83e609b4836444d7a95d65d"></a>
<a id="agroup__dns__resolve_html_gga7169c5a920fb1b0d77910a6ab922e3f0a42c3f3d5876b275f764a67e1bf43d850"></a>
<a id="agroup__dns__resolve_html_gga7169c5a920fb1b0d77910a6ab922e3f0a69676b0e82ee456e5faa935e39c1c3fa"></a>
<a id="agroup__dns__resolve_html_gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134"></a>
<a id="agroup__dns__resolve_html_gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049"></a>
<a id="agroup__dns__resolve_html_gga7169c5a920fb1b0d77910a6ab922e3f0aed30f5d6a68ef4503ca6f3d60d1c0e6a"></a>
<a id="agroup__dns__resolve_html_gga8a4330071b7161e1738dd91b1f6d6097a6a5d547c65f5d265bfd4f1968ed3db98"></a>
<a id="agroup__dns__resolve_html_gga8a4330071b7161e1738dd91b1f6d6097a80ada4858b77463f1af5b06660aaaf3b"></a>
<a id="agroup__dns__resolve_html_gga8a4330071b7161e1738dd91b1f6d6097a9f582f9d2424409736f32ac0051fc582"></a>
<a id="agroup__dns__resolve_html_gga8a4330071b7161e1738dd91b1f6d6097af0b69e02c8e086e64ce194cd66507672"></a>
<a id="agroup__dns__resolve_html_ggaeda02f82b12e9b7b4dea9fd66be123a7a53fc14584c90542121f4b1cd61658c33"></a>
<a id="agroup__dns__resolve_html_ggaeda02f82b12e9b7b4dea9fd66be123a7a687bf289d220cfaffbf8c89d9ce5b4c9"></a>
<a id="agroup__dns__resolve_html_ggaeda02f82b12e9b7b4dea9fd66be123a7a7eba9f4f6d3bb94c480417e85583463b"></a>
<a id="agroup__dns__resolve_html_ggaeda02f82b12e9b7b4dea9fd66be123a7a8e2e0f2cf2997d9519a52dfa9052fdf9"></a>
<a id="agroup__dns__resolve_html_ggaeda02f82b12e9b7b4dea9fd66be123a7aa6df19967b1ac123c79c5812ec62a902"></a>
<a id="agroup__dns__resolve_html_ggaeda02f82b12e9b7b4dea9fd66be123a7ad12f850b810647113633234ae818b84b"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="akernel_8h_html"></a>
<a id="anet__core_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="asocket__poll_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdns__addrinfo_html"></a>
<a id="astructdns__addrinfo_html_a21db6675aef2f8bafb83846343eae9ce"></a>
<a id="astructdns__addrinfo_html_a266971c18f120e455ba9ea522644a7ae"></a>
<a id="astructdns__addrinfo_html_a57ed2208756cbac08b811e98d4828dfd"></a>
<a id="astructdns__addrinfo_html_a6dd760be324864177dbbad21c21a6cfe"></a>
<a id="astructdns__addrinfo_html_a9bdea16062e9f86b48fde8d5c3440a44"></a>
<a id="astructdns__addrinfo_html_ac130969f14020524d2c427888309656d"></a>
<a id="astructdns__addrinfo_html_aec286947b75b6f6689bd2df8bd7e761f"></a>
<a id="astructdns__addrinfo_html_af9a9458751ddb65219f3b5f6730df558"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_a106464bda8d56283b06251c37964906b"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_a168fea99e8c6760cab49611ceb5a6fc1"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_a1dccc8f927ba987da56c5d704ab67e1a"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_a28174f11134146a800588f5e32d4a147"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_a334caa7c36c9b10d3fff51bfdee68e72"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_a4260371a741b3c2e752848955eee5cae"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_a5402d71d11a3ef006703a1a8e6cc7651"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_a6a1c93f3eab8f9aa55dbb26e704bb343"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_a6f76b200b8c421399987be83b72b9230"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_a773e2ad2bedb2d1030df3590e9a14173"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_a8473953176dd2310fb4cfe28fb04948d"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_a8810792264f30d55b03d53a775bc68fa"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_aa2f4ee968b610ba74cdd7880076e1508"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_aacf4003ce035658038ae44773091f2d0"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_ac3209c8e0fec2f52ee4da56b388ecda6"></a>
<a id="astructdns__resolve__context_1_1dns__pending__query_html_af5796eb469e2fe3bcebea2ad55a8fd78"></a>
<a id="astructdns__resolve__context_1_1dns__server__info_html"></a>
<a id="astructdns__resolve__context_1_1dns__server__info_html_a211583df0f70ea94b6fb38785bd6b08c"></a>
<a id="astructdns__resolve__context_1_1dns__server__info_html_a376e382dcee794c822b17d5d9eeb2c0d"></a>
<a id="astructdns__resolve__context_1_1dns__server__info_html_a65114f0c580f06ca2a5262c5336e682e"></a>
<a id="astructdns__resolve__context_1_1dns__server__info_html_a7f15ba79ca39d6403ebd41d8fef017c3"></a>
<a id="astructdns__resolve__context_1_1dns__server__info_html_a9d5e279f80a571fdca057ed552db3b92"></a>
<a id="astructdns__resolve__context_1_1dns__server__info_html_ab0aa7615cba374226bee823302d5b94a"></a>
<a id="astructdns__resolve__context_html"></a>
<a id="astructdns__resolve__context_html_a250a016056fd44533eeffc30419ec283"></a>
<a id="astructdns__resolve__context_html_a402a4a2adfe3859f8dab749b44b7d8e6"></a>
<a id="astructdns__resolve__context_html_a596053473b44be4977947632a1abb51e"></a>
<a id="astructdns__resolve__context_html_a8613ff54a235c211ba2cc3d232cb10a2"></a>
<a id="astructdns__resolve__context_html_a88f6600061cdb8e9f34802fe2a0a7d5a"></a>
<a id="astructdns__resolve__context_html_a9d1ada3ab20399f750acfee94e8e6cd7"></a>
<a id="astructdns__resolve__private_html"></a>
<a id="astructdns__resolve__private_html_a02840f7d43947d1b427a8acdd4e58c44"></a>
<a id="astructdns__resolve__private_html_a47a7aaae4fbb4686a1df617a35f20239"></a>
<a id="astructdns__resolve__private_html_a4d5ea0631d22c224771df2609b2ff450"></a>
<a id="astructdns__resolve__srv_html"></a>
<a id="astructdns__resolve__srv_html_a338bc4db1b0fb51c074467e04bb0f955"></a>
<a id="astructdns__resolve__srv_html_a55e8628a7bf305794fe10d114b32d25f"></a>
<a id="astructdns__resolve__srv_html_aacda738fbb4bb3826fc229868432d29b"></a>
<a id="astructdns__resolve__srv_html_aaf1b0b289ffbeacd1df9cbcbad7f2563"></a>
<a id="astructdns__resolve__srv_html_ab205aab04f4c271db1c5ff5c52e427ff"></a>
<a id="astructdns__resolve__txt_html"></a>
<a id="astructdns__resolve__txt_html_a332e2e090d86a7ff1278a5dc825f0843"></a>
<a id="astructdns__resolve__txt_html_a70076b35c818d2b67fdf0f38262a59e9"></a>
<a id="astructk__mutex_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructk__timepoint__t_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_ade8055f804d5a1fea13e55d71d92a5e7"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructzsock__pollfd_html"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_DNS_RESOLVE_H_
#define ZEPHYR_INCLUDE_NET_DNS_RESOLVE_H_

#include <zephyr/kernel.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/socket_poll.h>
#include <zephyr/net/net_core.h>
#include <zephyr/sys/atomic.h>

#ifdef __cplusplus
extern "C" {
#endif


enum dns_query_type {
        DNS_QUERY_TYPE_A = 1,
        DNS_QUERY_TYPE_CNAME = 5,
        DNS_QUERY_TYPE_PTR = 12,
        DNS_QUERY_TYPE_TXT = 16,
        DNS_QUERY_TYPE_AAAA = 28,
        DNS_QUERY_TYPE_SRV = 33,
        DNS_QUERY_TYPE_ANY = 255,
        DNS_QUERY_TYPE_RESERVED = 65535,
};


#define DNS_RR_TYPE_PRIVATE_START_VALUE 65280
#define DNS_RR_TYPE_PRIVATE_END_VALUE 65534

static inline bool dns_query_type_is_private(enum dns_query_type type)
{
        unsigned int val = (unsigned int)type;

        return (val >= DNS_RR_TYPE_PRIVATE_START_VALUE &&
                val <= DNS_RR_TYPE_PRIVATE_END_VALUE);
}

enum dns_server_source {
        DNS_SOURCE_UNKNOWN = 0,
        DNS_SOURCE_MANUAL,
        DNS_SOURCE_DHCPV4,
        DNS_SOURCE_DHCPV6,
        DNS_SOURCE_IPV6_RA,
        DNS_SOURCE_PPP,
};

#if defined(CONFIG_DNS_RESOLVER_MAX_NAME_LEN)
#define DNS_MAX_NAME_SIZE CONFIG_DNS_RESOLVER_MAX_NAME_LEN
#else
#define DNS_MAX_NAME_SIZE 20
#endif /* CONFIG_DNS_RESOLVER_MAX_NAME_LEN */

#if defined(CONFIG_DNS_RESOLVER_MAX_TEXT_LEN)
#define DNS_MAX_TEXT_SIZE CONFIG_DNS_RESOLVER_MAX_TEXT_LEN
#else
#define DNS_MAX_TEXT_SIZE 64
#endif /* CONFIG_DNS_RESOLVER_MAX_TEXT_LEN */

#if defined(CONFIG_DNS_RESOLVER_MAX_PRIVATE_DATA_LEN)
#define DNS_MAX_PRIVATE_DATA_SIZE CONFIG_DNS_RESOLVER_MAX_PRIVATE_DATA_LEN
#else
#define DNS_MAX_PRIVATE_DATA_SIZE 128
#endif /* CONFIG_DNS_RESOLVER_MAX_PRIVATE_DATA_LEN */


#define DNS_BUF_TIMEOUT K_MSEC(500) /* ms */

/* This value is recommended by RFC 1035 */
#if defined(CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE)
#define DNS_RESOLVER_MAX_BUF_SIZE CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE
#else
#define DNS_RESOLVER_MAX_BUF_SIZE 512
#endif /* CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE */

/* Make sure that we can compile things even if CONFIG_DNS_RESOLVER
 * is not enabled.
 */
#if defined(CONFIG_DNS_RESOLVER_MAX_SERVERS)
#define DNS_RESOLVER_MAX_SERVERS CONFIG_DNS_RESOLVER_MAX_SERVERS
#else
#define DNS_RESOLVER_MAX_SERVERS 0
#endif

#if defined(CONFIG_DNS_NUM_CONCUR_QUERIES)
#define DNS_NUM_CONCUR_QUERIES CONFIG_DNS_NUM_CONCUR_QUERIES
#else
#define DNS_NUM_CONCUR_QUERIES 1
#endif

#if defined(CONFIG_NET_IF_MAX_IPV6_COUNT)
#define MAX_IPV6_IFACE_COUNT CONFIG_NET_IF_MAX_IPV6_COUNT
#else
#define MAX_IPV6_IFACE_COUNT 1
#endif

#if defined(CONFIG_NET_IF_MAX_IPV4_COUNT)
#define MAX_IPV4_IFACE_COUNT CONFIG_NET_IF_MAX_IPV4_COUNT
#else
#define MAX_IPV4_IFACE_COUNT 1
#endif

/* If mDNS is enabled, then add some extra well known multicast servers to the
 * server list.
 */
#if defined(CONFIG_MDNS_RESOLVER)
#if defined(CONFIG_NET_IPV6) && defined(CONFIG_NET_IPV4)
#define MDNS_SERVER_COUNT 2
#else
#define MDNS_SERVER_COUNT 1
#endif /* CONFIG_NET_IPV6 && CONFIG_NET_IPV4 */
#else
#define MDNS_SERVER_COUNT 0
#endif /* CONFIG_MDNS_RESOLVER */

/* If LLMNR is enabled, then add some extra well known multicast servers to the
 * server list.
 */
#if defined(CONFIG_LLMNR_RESOLVER)
#if defined(CONFIG_NET_IPV6) && defined(CONFIG_NET_IPV4)
#define LLMNR_SERVER_COUNT 2
#else
#define LLMNR_SERVER_COUNT 1
#endif /* CONFIG_NET_IPV6 && CONFIG_NET_IPV4 */
#else
#define LLMNR_SERVER_COUNT 0
#endif /* CONFIG_MDNS_RESOLVER */

#define DNS_MAX_MCAST_SERVERS (MDNS_SERVER_COUNT + LLMNR_SERVER_COUNT)

#if defined(CONFIG_MDNS_RESPONDER)
#if defined(CONFIG_NET_IPV6)
#define MDNS_MAX_IPV6_IFACE_COUNT CONFIG_NET_IF_MAX_IPV6_COUNT
#else
#define MDNS_MAX_IPV6_IFACE_COUNT 0
#endif /* CONFIG_NET_IPV6 */

#if defined(CONFIG_NET_IPV4)
#define MDNS_MAX_IPV4_IFACE_COUNT CONFIG_NET_IF_MAX_IPV4_COUNT
#else
#define MDNS_MAX_IPV4_IFACE_COUNT 0
#endif /* CONFIG_NET_IPV4 */

#define MDNS_MAX_POLL (MDNS_MAX_IPV4_IFACE_COUNT + MDNS_MAX_IPV6_IFACE_COUNT)
#else
#define MDNS_MAX_POLL 0
#endif /* CONFIG_MDNS_RESPONDER */

#if defined(CONFIG_LLMNR_RESPONDER)
#if defined(CONFIG_NET_IPV6) && defined(CONFIG_NET_IPV4)
#define LLMNR_MAX_POLL 2
#else
#define LLMNR_MAX_POLL 1
#endif
#else
#define LLMNR_MAX_POLL 0
#endif /* CONFIG_LLMNR_RESPONDER */

#define DNS_RESOLVER_MAX_POLL (DNS_RESOLVER_MAX_SERVERS + DNS_MAX_MCAST_SERVERS)

/* Cap the max poll to 32 */
BUILD_ASSERT(DNS_RESOLVER_MAX_POLL <= 32,
             "DNS_RESOLVER_MAX_POLL " STRINGIFY(DNS_RESOLVER_MAX_POLL)
             " must be smaller or equal than " STRINGIFY(32));

#define DNS_DISPATCHER_MAX_POLL (DNS_RESOLVER_MAX_POLL + MDNS_MAX_POLL + LLMNR_MAX_POLL)

#if defined(CONFIG_ZVFS_POLL_MAX)
BUILD_ASSERT(CONFIG_ZVFS_POLL_MAX >= DNS_DISPATCHER_MAX_POLL,
             "CONFIG_ZVFS_POLL_MAX must be larger than " STRINGIFY(DNS_DISPATCHER_MAX_POLL));
#endif

enum dns_socket_type {
        DNS_SOCKET_RESOLVER = 1,
        DNS_SOCKET_RESPONDER = 2
};

struct dns_resolve_context;
struct mdns_responder_context;
struct dns_socket_dispatcher;

typedef int (*dns_socket_dispatcher_cb)(struct dns_socket_dispatcher *ctx, int sock,
                                        struct net_sockaddr *addr, size_t addrlen,
                                        struct net_buf *buf, size_t data_len);

struct dns_socket_dispatcher {
        sys_snode_t node;
        const struct net_socket_service_desc *svc;
        union {
                void *ctx;
                struct dns_resolve_context *resolve_ctx;
                struct mdns_responder_context *mdns_ctx;
        };

        enum dns_socket_type type;
        union {
                struct net_sockaddr_storage local_addr_storage;
                /* Use the local_addr_storage instead of this one. */
                struct net_sockaddr local_addr;
        };
        dns_socket_dispatcher_cb cb;
        struct zsock_pollfd *fds;
        int fds_len;
        int sock;
        int ifindex;
        struct dns_socket_dispatcher *pair;
        bool paired;
        struct k_mutex lock;
        k_timeout_t buf_timeout;
};

int dns_dispatcher_register(struct dns_socket_dispatcher *ctx);

int dns_dispatcher_unregister(struct dns_socket_dispatcher *ctx);


enum dns_resolve_extension {
        DNS_RESOLVE_NONE = 0,
        DNS_RESOLVE_TXT,
        DNS_RESOLVE_SRV,
        DNS_RESOLVE_PRIVATE,
};

struct dns_resolve_txt {
        size_t textlen;
        char   text[DNS_MAX_TEXT_SIZE + 1];
};

struct dns_resolve_srv {
        uint16_t priority;
        uint16_t weight;
        uint16_t port;
        size_t   targetlen;
        char     target[DNS_MAX_NAME_SIZE + 1];
};

struct dns_resolve_private {
        uint16_t type;
        size_t datalen;
        uint8_t data[DNS_MAX_PRIVATE_DATA_SIZE];
};

struct dns_addrinfo {
        uint8_t ai_family;

        union {
                struct {
                        net_socklen_t ai_addrlen;

                        union {
                                struct net_sockaddr_storage ai_addr_storage;
                                struct net_sockaddr ai_addr;
                        };

                        char ai_canonname[DNS_MAX_NAME_SIZE + 1];
                };

                struct {
                        enum dns_resolve_extension ai_extension;

                        union {
                                struct dns_resolve_txt ai_txt;
                                struct dns_resolve_srv ai_srv;
#if defined(CONFIG_DNS_RESOLVER_PRIVATE_RR_SUPPORT) || defined(__DOXYGEN__)
                                struct dns_resolve_private ai_private;
#endif /* CONFIG_DNS_RESOLVER_PRIVATE_RR_SUPPORT */
                        };
                };
        };
};

enum dns_resolve_status {
        DNS_EAI_BADFLAGS    = -1,
        DNS_EAI_NONAME      = -2,
        DNS_EAI_AGAIN       = -3,
        DNS_EAI_FAIL        = -4,
        DNS_EAI_NODATA      = -5,
        DNS_EAI_FAMILY      = -6,
        DNS_EAI_SOCKTYPE    = -7,
        DNS_EAI_SERVICE     = -8,
        DNS_EAI_ADDRFAMILY  = -9,
        DNS_EAI_MEMORY      = -10,
        DNS_EAI_SYSTEM      = -11,
        DNS_EAI_OVERFLOW    = -12,
        DNS_EAI_INPROGRESS  = -100,
        DNS_EAI_CANCELED    = -101,
        DNS_EAI_NOTCANCELED = -102,
        DNS_EAI_ALLDONE     = -103,
        DNS_EAI_IDN_ENCODE  = -105,
};

typedef void (*dns_resolve_cb_t)(enum dns_resolve_status status,
                                 struct dns_addrinfo *info,
                                 void *user_data);

typedef void (*dns_resolve_pkt_fw_cb_t)(struct net_buf *dns_data, size_t buf_len, void *user_data);


enum dns_resolve_context_state {
        DNS_RESOLVE_CONTEXT_UNINITIALIZED = 0,
        DNS_RESOLVE_CONTEXT_ACTIVE,
        DNS_RESOLVE_CONTEXT_DEACTIVATING,
        DNS_RESOLVE_CONTEXT_INACTIVE,
};


struct dns_resolve_context {
        struct dns_server_info {
                union {
                        struct net_sockaddr_storage dns_server_addr;
                        struct net_sockaddr dns_server;
                };

                int sock;

                int if_index;

                enum dns_server_source source;

                uint8_t is_mdns : 1;

                uint8_t is_llmnr : 1;

                struct dns_socket_dispatcher dispatcher;

                bool in_dispatch;
        } servers[DNS_RESOLVER_MAX_POLL];

        struct zsock_pollfd fds[DNS_RESOLVER_MAX_POLL];

        struct k_mutex lock;

        k_timeout_t buf_timeout;

        struct dns_pending_query {
                struct k_work_delayable timer;

                struct dns_resolve_context *ctx;

                dns_resolve_cb_t cb;

                void *user_data;

                const char *query;

                enum dns_query_type query_type;

                uint16_t id;

                uint16_t query_hash;

                uint16_t orig_query_hash;

                /* Number of additional queries sent to resolve CNAME record
                 * name aliases.
                 */
                uint8_t additional_queries;

                bool cb_called;

                k_timepoint_t deadline;

                struct {
                        atomic_t sent;

                        atomic_t pending;

                        atomic_t failed;
                } servers;

                enum dns_resolve_status last_status;
        } queries[DNS_NUM_CONCUR_QUERIES];

        enum dns_resolve_context_state state;

#if defined(CONFIG_DNS_RESOLVER_PACKET_FORWARDING) || defined(__DOXYGEN__)
        dns_resolve_pkt_fw_cb_t pkt_fw_cb;
#endif /* CONFIG_DNS_RESOLVER_PACKET_FORWARDING */

        int init_called;
};


struct mdns_probe_user_data {
        struct mdns_responder_context *ctx;
        char query[DNS_MAX_NAME_SIZE + 1];
        uint16_t dns_id;
};

struct mdns_responder_context {
        struct net_sockaddr_storage server_addr;
        struct dns_socket_dispatcher dispatcher;
        struct zsock_pollfd fds[1];
        int sock;
        struct net_if *iface;
#if defined(CONFIG_MDNS_RESPONDER_PROBE)
        struct k_work_delayable probe_timer;
        struct dns_resolve_context probe_ctx;
        struct mdns_probe_user_data probe_data;
#endif
};


int dns_resolve_init(struct dns_resolve_context *ctx,
                     const char *dns_servers_str[],
                     const struct net_sockaddr *dns_servers_sa[]);

int dns_resolve_init_default(struct dns_resolve_context *ctx);

int dns_resolve_close(struct dns_resolve_context *ctx);

bool dns_resolve_is_active(struct dns_resolve_context *ctx);

int dns_resolve_reconfigure(struct dns_resolve_context *ctx,
                            const char *servers_str[],
                            const struct net_sockaddr *servers_sa[],
                            enum dns_server_source source);

int dns_resolve_reconfigure_with_interfaces(struct dns_resolve_context *ctx,
                                            const char *servers_str[],
                                            const struct net_sockaddr *servers_sa[],
                                            int interfaces[],
                                            enum dns_server_source source);

int dns_resolve_remove(struct dns_resolve_context *ctx, int if_index);

int dns_resolve_remove_source(struct dns_resolve_context *ctx, int if_index,
                              enum dns_server_source source);

int dns_resolve_remove_server_addresses(struct dns_resolve_context *ctx,
                                        const struct net_sockaddr *servers_sa[],
                                        int interfaces[]);

int dns_resolve_cancel(struct dns_resolve_context *ctx,
                       uint16_t dns_id);

int dns_resolve_cancel_with_name(struct dns_resolve_context *ctx,
                                 uint16_t dns_id,
                                 const char *query_name,
                                 enum dns_query_type query_type);

int dns_resolve_name(struct dns_resolve_context *ctx,
                     const char *query,
                     enum dns_query_type type,
                     uint16_t *dns_id,
                     dns_resolve_cb_t cb,
                     void *user_data,
                     int32_t timeout);

static inline int dns_resolve_service(struct dns_resolve_context *ctx,
                                      const char *query,
                                      uint16_t *dns_id,
                                      dns_resolve_cb_t cb,
                                      void *user_data,
                                      int32_t timeout)
{
        return dns_resolve_name(ctx, query, DNS_QUERY_TYPE_PTR,
                                dns_id, cb, user_data, timeout);
}

struct dns_resolve_context *dns_resolve_get_default(void);

#if defined(CONFIG_DNS_RESOLVER_PACKET_FORWARDING) || defined(__DOXYGEN__)
static inline void dns_resolve_enable_packet_forwarding(struct dns_resolve_context *ctx,
                                                        dns_resolve_pkt_fw_cb_t cb)
{
        ctx->pkt_fw_cb = cb;
}
#endif /* CONFIG_DNS_RESOLVER_PACKET_FORWARDING */

static inline int dns_get_addr_info(const char *query,
                                    enum dns_query_type type,
                                    uint16_t *dns_id,
                                    dns_resolve_cb_t cb,
                                    void *user_data,
                                    int32_t timeout)
{
        return dns_resolve_name(dns_resolve_get_default(),
                                query,
                                type,
                                dns_id,
                                cb,
                                user_data,
                                timeout);
}

static inline int dns_cancel_addr_info(uint16_t dns_id)
{
        return dns_resolve_cancel(dns_resolve_get_default(), dns_id);
}

static inline int dns_cancel_addr_info_with_name(const char *query_name,
                                        enum dns_query_type query_type,
                                        uint16_t dns_id)
{
        return dns_resolve_cancel_with_name(dns_resolve_get_default(),
                                dns_id,
                                query_name,
                                query_type);
}



const char *dns_get_source_str(enum dns_server_source source);

#if defined(CONFIG_DNS_RESOLVER_AUTO_INIT)
void dns_init_resolver(void);

#else
#define dns_init_resolver(...)
#endif /* CONFIG_DNS_RESOLVER_AUTO_INIT */


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_DNS_RESOLVE_H_ */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2017 Intel Corporation。

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 102 行

条件编译配置（Configuration）标记：`CONFIG_DNS_RESOLVER_MAX_NAME_LEN`。

### 注释 3：原第 109 行

条件编译配置（Configuration）标记：`CONFIG_DNS_RESOLVER_MAX_TEXT_LEN`。

### 注释 4：原第 116 行

条件编译配置（Configuration）标记：`CONFIG_DNS_RESOLVER_MAX_PRIVATE_DATA_LEN`。

### 注释 5：原第 120 行

毫秒（ms）。

### 注释 6：原第 122 行

RFC 1035 推荐使用此值。

### 注释 7：原第 127 行

条件编译配置（Configuration）标记：`CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE`。

### 注释 8：原第 129 行

确保即使未启用 `CONFIG_DNS_RESOLVER`，也能够编译。

### 注释 9：原第 156 行

如果启用多播域名系统（mDNS），则向服务器列表添加一些额外的知名多播服务器。

### 注释 10：原第 164 行

条件表达式：`CONFIG_NET_IPV6 && CONFIG_NET_IPV4`。

### 注释 11：原第 167 行

条件编译配置（Configuration）标记：`CONFIG_MDNS_RESOLVER`。

### 注释 12：原第 169 行

如果启用链路本地多播名称解析（LLMNR），则向服务器列表添加一些额外的知名多播服务器。

### 注释 13：原第 177 行

条件表达式：`CONFIG_NET_IPV6 && CONFIG_NET_IPV4`。

### 注释 14：原第 180 行

条件编译配置（Configuration）标记：`CONFIG_MDNS_RESOLVER`。

### 注释 15：原第 189 行

条件编译配置（Configuration）标记：`CONFIG_NET_IPV6`。

### 注释 16：原第 195 行

条件编译配置（Configuration）标记：`CONFIG_NET_IPV4`。

### 注释 17：原第 200 行

条件编译配置（Configuration）标记：`CONFIG_MDNS_RESPONDER`。

### 注释 18：原第 210 行

条件编译配置（Configuration）标记：`CONFIG_LLMNR_RESPONDER`。

### 注释 19：原第 214 行

将最大轮询数（max poll）限制为 32。

### 注释 20：原第 279 行

请使用 `local_addr_storage` 代替此字段。

### 注释 21：原第 413 行

条件编译配置（Configuration）标记：`CONFIG_DNS_RESOLVER_PRIVATE_RR_SUPPORT`。

### 注释 22：原第 615 行

为解析规范名称（CNAME）记录中的名称别名而额外发送的查询数量。

### 注释 23：原第 648 行

条件编译配置（Configuration）标记：`CONFIG_DNS_RESOLVER_PACKET_FORWARDING`。

### 注释 24：原第 970 行

条件编译配置（Configuration）标记：`CONFIG_DNS_RESOLVER_PACKET_FORWARDING`。

### 注释 25：原第 1074 行

条件编译配置（Configuration）标记：`CONFIG_DNS_RESOLVER_AUTO_INIT`。

### 注释 26：原第 1082 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_DNS_RESOLVE_H_`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/socket_poll.h](../api_file_reference/P401_zephyr__net__socket_poll.h_文件参考.md)
- [zephyr/net/net_core.h](../api_file_interface_reference/P037_zephyr__net__net_core.h_文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [dns_query_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7169c5a920fb1b0d77910a6ab922e3f0)
- [DNS_QUERY_TYPE_A](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134)
- [DNS_QUERY_TYPE_CNAME](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a128aa925168ae2b096ff879c7648d2e4)
- [DNS_QUERY_TYPE_PTR](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a69676b0e82ee456e5faa935e39c1c3fa)
- [DNS_QUERY_TYPE_TXT](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a42c3f3d5876b275f764a67e1bf43d850)
- [DNS_QUERY_TYPE_AAAA](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049)
- [DNS_QUERY_TYPE_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a2e976a8ed83e609b4836444d7a95d65d)
- [DNS_QUERY_TYPE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a0b8a4c108a7ae4742d2235b64c3d8c06)
- [DNS_QUERY_TYPE_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0aed30f5d6a68ef4503ca6f3d60d1c0e6a)
- [dns_query_type_is_private](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga13a7cbc3b59a12278f4b035013c03b1d)
- [DNS_RR_TYPE_PRIVATE_START_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga924d2d4d3b5205a605f4ab69dffdf294)
- [DNS_RR_TYPE_PRIVATE_END_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga4db137a83d3917bcad1489e25a639666)
- [dns_server_source](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaeda02f82b12e9b7b4dea9fd66be123a7)
- [DNS_SOURCE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a8e2e0f2cf2997d9519a52dfa9052fdf9)
- [DNS_SOURCE_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a53fc14584c90542121f4b1cd61658c33)
- [DNS_SOURCE_DHCPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a7eba9f4f6d3bb94c480417e85583463b)
- [DNS_SOURCE_DHCPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7ad12f850b810647113633234ae818b84b)
- [DNS_SOURCE_IPV6_RA](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a687bf289d220cfaffbf8c89d9ce5b4c9)
- [DNS_SOURCE_PPP](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7aa6df19967b1ac123c79c5812ec62a902)
- [dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [dns_resolve_extension](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga8a4330071b7161e1738dd91b1f6d6097)
- [DNS_RESOLVE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga8a4330071b7161e1738dd91b1f6d6097a80ada4858b77463f1af5b06660aaaf3b)
- [DNS_RESOLVE_TXT](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga8a4330071b7161e1738dd91b1f6d6097a6a5d547c65f5d265bfd4f1968ed3db98)
- [DNS_RESOLVE_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga8a4330071b7161e1738dd91b1f6d6097af0b69e02c8e086e64ce194cd66507672)
- [DNS_RESOLVE_PRIVATE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga8a4330071b7161e1738dd91b1f6d6097a9f582f9d2424409736f32ac0051fc582)
- [dns_resolve_txt](../network_application_model_reference/P024_dns_resolve_txt_结构体.md)
- [textlen](../network_application_model_reference/P024_dns_resolve_txt_结构体.md#a332e2e090d86a7ff1278a5dc825f0843)
- [text](../network_application_model_reference/P024_dns_resolve_txt_结构体.md#a70076b35c818d2b67fdf0f38262a59e9)
- [DNS_MAX_TEXT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7b6c39611abd40d2d0510c9e38383ecc)
- [dns_resolve_srv](../network_application_model_reference/P023_dns_resolve_srv_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [priority](../network_application_model_reference/P023_dns_resolve_srv_结构体.md#a338bc4db1b0fb51c074467e04bb0f955)
- [weight](../network_application_model_reference/P023_dns_resolve_srv_结构体.md#aaf1b0b289ffbeacd1df9cbcbad7f2563)
- [port](../network_application_model_reference/P023_dns_resolve_srv_结构体.md#ab205aab04f4c271db1c5ff5c52e427ff)
- [targetlen](../network_application_model_reference/P023_dns_resolve_srv_结构体.md#aacda738fbb4bb3826fc229868432d29b)
- [target](../network_application_model_reference/P023_dns_resolve_srv_结构体.md#a55e8628a7bf305794fe10d114b32d25f)
- [DNS_MAX_NAME_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaba564a71c4fb4c44fae69015e880b0db)
- [dns_resolve_private](../network_application_model_reference/P022_dns_resolve_private_结构体.md)
- [type](../network_application_model_reference/P022_dns_resolve_private_结构体.md#a4d5ea0631d22c224771df2609b2ff450)
- [datalen](../network_application_model_reference/P022_dns_resolve_private_结构体.md#a47a7aaae4fbb4686a1df617a35f20239)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../network_application_model_reference/P022_dns_resolve_private_结构体.md#a02840f7d43947d1b427a8acdd4e58c44)
- [DNS_MAX_PRIVATE_DATA_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gac709b355684d44e943c26c6953187df4)
- [dns_addrinfo](../network_application_model_reference/P018_dns_addrinfo_结构体.md)
- [ai_family](../network_application_model_reference/P018_dns_addrinfo_结构体.md#af9a9458751ddb65219f3b5f6730df558)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [ai_addrlen](../network_application_model_reference/P018_dns_addrinfo_结构体.md#aec286947b75b6f6689bd2df8bd7e761f)
- [ai_addr_storage](../network_application_model_reference/P018_dns_addrinfo_结构体.md#a6dd760be324864177dbbad21c21a6cfe)
- [ai_canonname](../network_application_model_reference/P018_dns_addrinfo_结构体.md#a21db6675aef2f8bafb83846343eae9ce)
- [ai_extension](../network_application_model_reference/P018_dns_addrinfo_结构体.md#ac130969f14020524d2c427888309656d)
- [ai_txt](../network_application_model_reference/P018_dns_addrinfo_结构体.md#a57ed2208756cbac08b811e98d4828dfd)
- [ai_srv](../network_application_model_reference/P018_dns_addrinfo_结构体.md#a266971c18f120e455ba9ea522644a7ae)
- [ai_private](../network_application_model_reference/P018_dns_addrinfo_结构体.md#a9bdea16062e9f86b48fde8d5c3440a44)
- [dns_resolve_status](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga5baf1fea0482fb3a940b4f5350a3c58e)
- [DNS_EAI_BADFLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea9989bb26c930dcf90b5aaab224f19793)
- [DNS_EAI_NONAME](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f)
- [DNS_EAI_AGAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9)
- [DNS_EAI_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455)
- [DNS_EAI_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2)
- [DNS_EAI_FAMILY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea8440de8b7109dfcca71acca6c7ac4103)
- [DNS_EAI_SOCKTYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eaba718125a826939380fdbcc9c1fb4512)
- [DNS_EAI_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eaeb7d2677167f5bc230da2eea2a81d06c)
- [DNS_EAI_ADDRFAMILY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d)
- [DNS_EAI_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673)
- [DNS_EAI_SYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eae932d5596c55d090cf2ebe43ad59bd35)
- [DNS_EAI_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f)
- [DNS_EAI_INPROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3)
- [DNS_EAI_CANCELED](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3)
- [DNS_EAI_NOTCANCELED](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f)
- [DNS_EAI_ALLDONE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836)
- [DNS_EAI_IDN_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4)
- [dns_resolve_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gafe22d0ef90c581982561ef0c33d1f722)
- [dns_resolve_pkt_fw_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7892b3eda301db358b1f18720a2f638c)
- [user_data](../network_core_model_reference/P046_net_buf_结构体.md#ade8055f804d5a1fea13e55d71d92a5e7)
- [dns_server_info](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md)
- [dns_server_addr](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md#a376e382dcee794c822b17d5d9eeb2c0d)
- [sock](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md#ab0aa7615cba374226bee823302d5b94a)
- [if_index](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md#a9d5e279f80a571fdca057ed552db3b92)
- [source](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md#a65114f0c580f06ca2a5262c5336e682e)
- [is_mdns](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md#a211583df0f70ea94b6fb38785bd6b08c)
- [is_llmnr](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md#a7f15ba79ca39d6403ebd41d8fef017c3)
- [servers](../network_application_model_reference/P019_dns_resolve_context_结构体.md#a8613ff54a235c211ba2cc3d232cb10a2)
- [zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [lock](../network_application_model_reference/P019_dns_resolve_context_结构体.md#a9d1ada3ab20399f750acfee94e8e6cd7)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [buf_timeout](../network_application_model_reference/P019_dns_resolve_context_结构体.md#a402a4a2adfe3859f8dab749b44b7d8e6)
- [dns_pending_query](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [timer](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a6f76b200b8c421399987be83b72b9230)
- [ctx](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a4260371a741b3c2e752848955eee5cae)
- [cb](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#aacf4003ce035658038ae44773091f2d0)
- [user_data](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a6a1c93f3eab8f9aa55dbb26e704bb343)
- [query](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a106464bda8d56283b06251c37964906b)
- [query_type](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#af5796eb469e2fe3bcebea2ad55a8fd78)
- [id](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a773e2ad2bedb2d1030df3590e9a14173)
- [query_hash](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a168fea99e8c6760cab49611ceb5a6fc1)
- [orig_query_hash](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a1dccc8f927ba987da56c5d704ab67e1a)
- [additional_queries](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a334caa7c36c9b10d3fff51bfdee68e72)
- [cb_called](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#ac3209c8e0fec2f52ee4da56b388ecda6)
- [k_timepoint_t](../timer_reference/P088_内核时间点类型.md)
- [deadline](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a28174f11134146a800588f5e32d4a147)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [sent](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a5402d71d11a3ef006703a1a8e6cc7651)
- [pending](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#aa2f4ee968b610ba74cdd7880076e1508)
- [failed](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a8810792264f30d55b03d53a775bc68fa)
- [last_status](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a8473953176dd2310fb4cfe28fb04948d)
- [queries](../network_application_model_reference/P019_dns_resolve_context_结构体.md#a596053473b44be4977947632a1abb51e)
- [state](../network_application_model_reference/P019_dns_resolve_context_结构体.md#a88f6600061cdb8e9f34802fe2a0a7d5a)
- [pkt_fw_cb](../network_application_model_reference/P019_dns_resolve_context_结构体.md#a250a016056fd44533eeffc30419ec283)
- [dns_resolve_init](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga27a85c421014373f6aad89634adf8c7d)
- [dns_resolve_init_default](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga71eab0f9dd0bc7c02c0d55e7dc6741f3)
- [dns_resolve_close](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gab04f3b2347e9c59346c10180c6c9ffbc)
- [dns_resolve_is_active](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3cf4e94af65585d89b4a0650dbd9d46e)
- [dns_resolve_reconfigure](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga1d3bb0319531bfe0ae95f48bdc51c56f)
- [dns_resolve_reconfigure_with_interfaces](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3d22eed1d6d017e5bd7a2344775d33b7)
- [dns_resolve_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga54c85b9c69c9a44f2e7bb78165cebfcb)
- [dns_resolve_remove_source](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gae292786587c511c223481f77a4f43017)
- [dns_resolve_remove_server_addresses](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf491764b213a891f296c9f91c35b1b72)
- [dns_resolve_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7701ddd6b6c5923f0d122a2bcf898cbf)
- [dns_resolve_cancel_with_name](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf2854ca9b839e7cba073e75202ac7e38)
- [dns_resolve_name](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga24f9bc24e2021b6b528bb15e4fcca49b)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [dns_resolve_service](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf28f6f8baa97d0b2341e1bdc02b6cb8c)
- [dns_resolve_get_default](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gae69cd758e99ea93ef8aac28366918b87)
- [dns_resolve_enable_packet_forwarding](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3326e98da31313d33861565fe0a10bdf)
- [dns_get_addr_info](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf891d7e21bddc8fbd029209b4339c01d)
- [dns_cancel_addr_info](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga54ae7aaf53b36951b27f09e1cc82df55)
- [dns_cancel_addr_info_with_name](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gac8a1d620f07641e4e64ad0757c31aa45)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_core.h](../api_file_interface_reference/P037_zephyr__net__net_core.h_文件参考.md)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [socket_poll.h](../api_file_reference/P401_zephyr__net__socket_poll.h_文件参考.md)
- [dns_addrinfo::ai_canonname](../network_application_model_reference/P018_dns_addrinfo_结构体.md#a21db6675aef2f8bafb83846343eae9ce)
- [dns_addrinfo::ai_srv](../network_application_model_reference/P018_dns_addrinfo_结构体.md#a266971c18f120e455ba9ea522644a7ae)
- [dns_addrinfo::ai_txt](../network_application_model_reference/P018_dns_addrinfo_结构体.md#a57ed2208756cbac08b811e98d4828dfd)
- [dns_addrinfo::ai_addr_storage](../network_application_model_reference/P018_dns_addrinfo_结构体.md#a6dd760be324864177dbbad21c21a6cfe)
- [dns_addrinfo::ai_private](../network_application_model_reference/P018_dns_addrinfo_结构体.md#a9bdea16062e9f86b48fde8d5c3440a44)
- [dns_addrinfo::ai_extension](../network_application_model_reference/P018_dns_addrinfo_结构体.md#ac130969f14020524d2c427888309656d)
- [dns_addrinfo::ai_addrlen](../network_application_model_reference/P018_dns_addrinfo_结构体.md#aec286947b75b6f6689bd2df8bd7e761f)
- [dns_addrinfo::ai_family](../network_application_model_reference/P018_dns_addrinfo_结构体.md#af9a9458751ddb65219f3b5f6730df558)
- [dns_resolve_context::dns_pending_query](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md)
- [dns_resolve_context::dns_pending_query::query](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a106464bda8d56283b06251c37964906b)
- [dns_resolve_context::dns_pending_query::query_hash](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a168fea99e8c6760cab49611ceb5a6fc1)
- [dns_resolve_context::dns_pending_query::orig_query_hash](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a1dccc8f927ba987da56c5d704ab67e1a)
- [dns_resolve_context::dns_pending_query::deadline](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a28174f11134146a800588f5e32d4a147)
- [dns_resolve_context::dns_pending_query::additional_queries](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a334caa7c36c9b10d3fff51bfdee68e72)
- [dns_resolve_context::dns_pending_query::ctx](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a4260371a741b3c2e752848955eee5cae)
- [dns_resolve_context::dns_pending_query::sent](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a5402d71d11a3ef006703a1a8e6cc7651)
- [dns_resolve_context::dns_pending_query::user_data](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a6a1c93f3eab8f9aa55dbb26e704bb343)
- [dns_resolve_context::dns_pending_query::timer](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a6f76b200b8c421399987be83b72b9230)
- [dns_resolve_context::dns_pending_query::id](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a773e2ad2bedb2d1030df3590e9a14173)
- [dns_resolve_context::dns_pending_query::last_status](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a8473953176dd2310fb4cfe28fb04948d)
- [dns_resolve_context::dns_pending_query::failed](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#a8810792264f30d55b03d53a775bc68fa)
- [dns_resolve_context::dns_pending_query::pending](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#aa2f4ee968b610ba74cdd7880076e1508)
- [dns_resolve_context::dns_pending_query::cb](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#aacf4003ce035658038ae44773091f2d0)
- [dns_resolve_context::dns_pending_query::cb_called](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#ac3209c8e0fec2f52ee4da56b388ecda6)
- [dns_resolve_context::dns_pending_query::query_type](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md#af5796eb469e2fe3bcebea2ad55a8fd78)
- [dns_resolve_context::dns_server_info](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md)
- [dns_resolve_context::dns_server_info::is_mdns](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md#a211583df0f70ea94b6fb38785bd6b08c)
- [dns_resolve_context::dns_server_info::dns_server_addr](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md#a376e382dcee794c822b17d5d9eeb2c0d)
- [dns_resolve_context::dns_server_info::source](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md#a65114f0c580f06ca2a5262c5336e682e)
- [dns_resolve_context::dns_server_info::is_llmnr](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md#a7f15ba79ca39d6403ebd41d8fef017c3)
- [dns_resolve_context::dns_server_info::if_index](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md#a9d5e279f80a571fdca057ed552db3b92)
- [dns_resolve_context::dns_server_info::sock](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md#ab0aa7615cba374226bee823302d5b94a)
- [dns_resolve_context::pkt_fw_cb](../network_application_model_reference/P019_dns_resolve_context_结构体.md#a250a016056fd44533eeffc30419ec283)
- [dns_resolve_context::buf_timeout](../network_application_model_reference/P019_dns_resolve_context_结构体.md#a402a4a2adfe3859f8dab749b44b7d8e6)
- [dns_resolve_context::queries](../network_application_model_reference/P019_dns_resolve_context_结构体.md#a596053473b44be4977947632a1abb51e)
- [dns_resolve_context::servers](../network_application_model_reference/P019_dns_resolve_context_结构体.md#a8613ff54a235c211ba2cc3d232cb10a2)
- [dns_resolve_context::state](../network_application_model_reference/P019_dns_resolve_context_结构体.md#a88f6600061cdb8e9f34802fe2a0a7d5a)
- [dns_resolve_context::lock](../network_application_model_reference/P019_dns_resolve_context_结构体.md#a9d1ada3ab20399f750acfee94e8e6cd7)
- [dns_resolve_private::data](../network_application_model_reference/P022_dns_resolve_private_结构体.md#a02840f7d43947d1b427a8acdd4e58c44)
- [dns_resolve_private::datalen](../network_application_model_reference/P022_dns_resolve_private_结构体.md#a47a7aaae4fbb4686a1df617a35f20239)
- [dns_resolve_private::type](../network_application_model_reference/P022_dns_resolve_private_结构体.md#a4d5ea0631d22c224771df2609b2ff450)
- [dns_resolve_srv::priority](../network_application_model_reference/P023_dns_resolve_srv_结构体.md#a338bc4db1b0fb51c074467e04bb0f955)
- [dns_resolve_srv::target](../network_application_model_reference/P023_dns_resolve_srv_结构体.md#a55e8628a7bf305794fe10d114b32d25f)
- [dns_resolve_srv::targetlen](../network_application_model_reference/P023_dns_resolve_srv_结构体.md#aacda738fbb4bb3826fc229868432d29b)
- [dns_resolve_srv::weight](../network_application_model_reference/P023_dns_resolve_srv_结构体.md#aaf1b0b289ffbeacd1df9cbcbad7f2563)
- [dns_resolve_srv::port](../network_application_model_reference/P023_dns_resolve_srv_结构体.md#ab205aab04f4c271db1c5ff5c52e427ff)
- [dns_resolve_txt::textlen](../network_application_model_reference/P024_dns_resolve_txt_结构体.md#a332e2e090d86a7ff1278a5dc825f0843)
- [dns_resolve_txt::text](../network_application_model_reference/P024_dns_resolve_txt_结构体.md#a70076b35c818d2b67fdf0f38262a59e9)
- [net_buf::user_data](../network_core_model_reference/P046_net_buf_结构体.md#ade8055f804d5a1fea13e55d71d92a5e7)

---

[上一章](P007_dma_mcux_lpc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P009_audio.h_源码浏览.md)
