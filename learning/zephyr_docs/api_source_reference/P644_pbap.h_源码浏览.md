---
id: learning.zephyr-docs.api-source-reference.page-644
title: pbap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pbap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第644章\_pbap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pbap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pbap_8h.html)。

## 644.1\_原始可见代码（Source Code）

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
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="foldopen00132"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="foldopen00208"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="foldopen00244"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="foldopen00268"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00272"></a>
<a id="l00274"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="foldopen00286"></a>
<a id="l00286"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="foldopen00399"></a>
<a id="l00399"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="foldopen00612"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="foldopen00728"></a>
<a id="l00728"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="foldopen00751"></a>
<a id="l00751"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="foldopen00771"></a>
<a id="l00771"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00861"></a>
<a id="l00862"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00876"></a>
<a id="l00887"></a>
<a id="l00888"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="l00933"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00961"></a>
<a id="l00962"></a>
<a id="l00963"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="aerrno_8h_html"></a>
<a id="agoep_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a2b91abe9e010465f9514f37477b993e0"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a2d2ff2c6ec42d9e80dc4e841e19d31ee"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a48f773daa7f2dabaadc37142ec32ffd1"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a4b7a12b0e11747d1a470e8f559b55ea8"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a613e95b96eaba0522070b620b4b90953"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a7e38ca653283f53b62fa4b21f48d998a"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a881d3098a198dc1eced2150a213d1054"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9aacc05fd2528e29fbd53eb5ff940f9079"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9aba8108ac6b050d3dad845a5e8cb42eaf"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9acfbc9161dddf6859dd8e8ac70cf8d446"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9af449d3c85fbec550c76e29287a626789"></a>
<a id="agroup__bt__pbap_html_ga07f8db1528fc15bed243fc5da787354f"></a>
<a id="agroup__bt__pbap_html_ga09e255e0c5328a1f1e7286b7100eeb61"></a>
<a id="agroup__bt__pbap_html_ga15403745f42ba10ba1dd9552895e111d"></a>
<a id="agroup__bt__pbap_html_ga15c39f4afb996a37b43acd51cc82ed53"></a>
<a id="agroup__bt__pbap_html_ga29d4e867858a96606a623313acc808d9"></a>
<a id="agroup__bt__pbap_html_ga5af0c3016e948bc27df328432ffa9455"></a>
<a id="agroup__bt__pbap_html_ga5cf30994d6344a67b22eb01baf863b1b"></a>
<a id="agroup__bt__pbap_html_ga71ba43da527c77f3eaf7d43ae5c22cae"></a>
<a id="agroup__bt__pbap_html_ga72b9420a34975c9691690977169bcec6"></a>
<a id="agroup__bt__pbap_html_ga76ceaa735d7bc5ee97d665d497b896cd"></a>
<a id="agroup__bt__pbap_html_ga81e3d8885dddfae8f8e2714ef9173949"></a>
<a id="agroup__bt__pbap_html_ga9766bda140034251ba3287bfa116f359"></a>
<a id="agroup__bt__pbap_html_ga9d9697d62b6bdbbc4feb0cf4b9776b58"></a>
<a id="agroup__bt__pbap_html_ga9fcd75bb18c48756dfa4695890662ab0"></a>
<a id="agroup__bt__pbap_html_gaae2eac838c1b825f5d31d7073608e56d"></a>
<a id="agroup__bt__pbap_html_gab24a2cb71edfa1d5e59c33fabc01c7d9"></a>
<a id="agroup__bt__pbap_html_gab326aadad5f12827f08f6525b7dc5458"></a>
<a id="agroup__bt__pbap_html_gab37e9ea163060e8b770da56e5a6415cb"></a>
<a id="agroup__bt__pbap_html_gac1f07e0eb9b256010fdbcf29b71701c6"></a>
<a id="agroup__bt__pbap_html_gac511c99ae0c2d0f391f5dbf150599390"></a>
<a id="agroup__bt__pbap_html_gac6c48c5b202c19567a4ddb008626f174"></a>
<a id="agroup__bt__pbap_html_gac76cb47df9f747f222d7cdbe627d3ead"></a>
<a id="agroup__bt__pbap_html_gac8ef77affecb5316991afca6c1005f62"></a>
<a id="agroup__bt__pbap_html_gacdcbb62a6999c833e4e6d0846aad28d6"></a>
<a id="agroup__bt__pbap_html_gad407918b6c075045339aecd55b70db21"></a>
<a id="agroup__bt__pbap_html_gadbc19ba92332972e5d22e213c7618fa0"></a>
<a id="agroup__bt__pbap_html_gadc3ace27caf970d0f2f8c8278e50c7fc"></a>
<a id="agroup__bt__pbap_html_gadd0760a5999620762367a5dda62018b7"></a>
<a id="agroup__bt__pbap_html_gae26500d48fae5f26946ab7a4e261993c"></a>
<a id="agroup__bt__pbap_html_gae51b98f9472a284aba377a0343a6335f"></a>
<a id="agroup__bt__pbap_html_gae9506155e96d3f641ee928754439f579"></a>
<a id="agroup__bt__pbap_html_gafa7ebec6db37286b0ca54ed1d9f4ca02"></a>
<a id="agroup__bt__pbap_html_gafc697dd2db191451f1d2334f5758be69"></a>
<a id="agroup__bt__pbap_html_gga5cf30994d6344a67b22eb01baf863b1ba0fa84dbd58771867b547805099689a3a"></a>
<a id="agroup__bt__pbap_html_gga5cf30994d6344a67b22eb01baf863b1baf5f30663b6083d8c09950e71dc6e1e0b"></a>
<a id="agroup__bt__pbap_html_gga76ceaa735d7bc5ee97d665d497b896cda338230ca0c8d07ca4a5cced68cf9faf4"></a>
<a id="agroup__bt__pbap_html_gga76ceaa735d7bc5ee97d665d497b896cda4f1435ad0230025a1bf612fd38df67a9"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a07399ae04375a6c435f34815b734aabb"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a095c248ed7a21c3024843b06c8757c65"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a0d8adde858f93c7d5b765fb0488f22ce"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a12d9060eef27b4c048064df7b00faf7f"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a1622cc47e9c5d359d327b9175829b005"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a1c16e137b53c6c88152ed49d693dd32b"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a1fe34f3b6c0a3c9ca0966106052faa61"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a2bd2e420601d0d8dfd6d308b48ab3cf5"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a2f7b5161e2440abaa4dbcaf4351f9dc8"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a31e2f9be865df16c883964b8abaea828"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a392c7a7f408f80443e330e7e8317790f"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a4eccbde165789980859146504dc6ad79"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a534c44365efffc777b134db0d7158d01"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a587cb6926e50eca38c633019312208d5"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a5cb26f5f8d5baff7b2d28e030db326f1"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a6af54c454719c9a5baa75db6feb3c6e6"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a728ddfce7f0f93564e6e657d3fd9f9ca"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a7cfcd8e622d1adb99c5ad598b2642720"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a8030f80cf155692c1728775885c0786b"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a8eeef93a6fb6d1f90688444d4c025d75"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a9b2cb462f56b4abbda146fc3b6e0250b"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a9dc945e68284feb0c84c3f266b504e9a"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949a9e6232e6968a9604421a81a4d364e868"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949aa5acc89efeae0ef6fabbcdbc5c461cf0"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949aaedbb7e84f50781fa88eaff8859bf0c0"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949ab1029f770ff972cd56ca27149697b3c1"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949ab98d31a99ac92b189b8963f275d6846b"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949aba04655292e204ffea1ea8e6f868990a"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949abbf728e6870fb11e11095741261dce74"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949ac94b5f034af49ba23222988ac05dca41"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949ad1b5c9ec39747786c90c89b190235b5e"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949ae97d497323807766a249a354d9c73440"></a>
<a id="agroup__bt__pbap_html_gga81e3d8885dddfae8f8e2714ef9173949af45314b48bb91277d8ad84d29e44ce54"></a>
<a id="agroup__bt__pbap_html_gga9d9697d62b6bdbbc4feb0cf4b9776b58a26f8b1cb1f6bc983b1508b5a2e298a3e"></a>
<a id="agroup__bt__pbap_html_gga9d9697d62b6bdbbc4feb0cf4b9776b58a2f4a1259666bfbf84c8c8ac02faa8683"></a>
<a id="agroup__bt__pbap_html_gga9d9697d62b6bdbbc4feb0cf4b9776b58a3130502de3a9c28985692f8d93b6ad08"></a>
<a id="agroup__bt__pbap_html_gga9d9697d62b6bdbbc4feb0cf4b9776b58a661acfbba2e792ee4444453650db00eb"></a>
<a id="agroup__bt__pbap_html_gga9d9697d62b6bdbbc4feb0cf4b9776b58a722cfbba810a0646a340d8bba82282fa"></a>
<a id="agroup__bt__pbap_html_gga9d9697d62b6bdbbc4feb0cf4b9776b58a7cab8c591dca0bc0279c6463ece416d6"></a>
<a id="agroup__bt__pbap_html_gga9d9697d62b6bdbbc4feb0cf4b9776b58a806a9638aa9ca07d52f2dbb6946b6594"></a>
<a id="agroup__bt__pbap_html_gga9d9697d62b6bdbbc4feb0cf4b9776b58a904e13430e8318623f1a785b94caee93"></a>
<a id="agroup__bt__pbap_html_gga9d9697d62b6bdbbc4feb0cf4b9776b58a9f3978e6433273f9a1af3e0c91ae33cd"></a>
<a id="agroup__bt__pbap_html_gga9d9697d62b6bdbbc4feb0cf4b9776b58aa0c1cbc8611c6a5f39d1d61858ea85cb"></a>
<a id="agroup__bt__pbap_html_gga9d9697d62b6bdbbc4feb0cf4b9776b58ab34bbcad2a7fe5c2b9f2efa511b69ccf"></a>
<a id="agroup__bt__pbap_html_ggac6c48c5b202c19567a4ddb008626f174a59e2999c6d5af45b12c88d8bf78c7252"></a>
<a id="agroup__bt__pbap_html_ggac6c48c5b202c19567a4ddb008626f174ab03a1c4e18ea46da6c28fe83a850b510"></a>
<a id="agroup__bt__pbap_html_ggac6c48c5b202c19567a4ddb008626f174accbdbbf7c94a707b77c6b249760f37a1"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0a0bc424753f8b1da0b3209c38925c6162"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0a2cf69d5233c590f708571c2447539025"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0a32182e2f399ec292ea652dd7f04bbdee"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0a4a1bbc25a06c89dd948542ec700a7323"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0a4eb10ced494b26ad1380f6808574716c"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0a60027135eafa915cac55a1cc59d68b4f"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0a66bf205d11a351aa10fba0c6648600db"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0a7894ebcf543e20b5c3369ec6632fb9c9"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0a793e24d13b717616ee8eb09792d19310"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0aa17305107ed8979b917dab98f04442bf"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0abea06880695df75ef9ca68e94e4596b4"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0ac9aade48ff6a95d27443f817daf6ba75"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0acc1b3f202aa38ff027a63aecb9108641"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0acfbe210e7ef87a3a07b00f05b62f7616"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0aeac485e4bb2ca3d4fcdaf0e76fd55a08"></a>
<a id="agroup__bt__pbap_html_ggadbc19ba92332972e5d22e213c7618fa0af4a5a102fc189ad256b75091522d1b66"></a>
<a id="agroup__bt__pbap_html_ggadc3ace27caf970d0f2f8c8278e50c7fca99adb79a6d49413c2c3dc83ff4686e5d"></a>
<a id="agroup__bt__pbap_html_ggadd0760a5999620762367a5dda62018b7a58a43511704fe46d8f8cdbb8d0e6f9fe"></a>
<a id="agroup__bt__pbap_html_ggadd0760a5999620762367a5dda62018b7aa3f4d6139aad54ee40d60c9ab474dc48"></a>
<a id="agroup__bt__pbap_html_ggadd0760a5999620762367a5dda62018b7aaf5d738a116dd37e2bc18bec07858415"></a>
<a id="agroup__bt__pbap_html_ggadd0760a5999620762367a5dda62018b7adf8db04f430e9b19d75fd6396f6bf0f2"></a>
<a id="agroup__bt__pbap_html_ggae51b98f9472a284aba377a0343a6335fa04a72163c9a4aa1ca94e096fc61c0110"></a>
<a id="agroup__bt__pbap_html_ggae51b98f9472a284aba377a0343a6335fa09b908bca7982fc1818791c6ff2a9d54"></a>
<a id="agroup__bt__pbap_html_ggae51b98f9472a284aba377a0343a6335fa208cd02d7acabf2f6444292d2f0290ec"></a>
<a id="agroup__bt__pbap_html_ggae51b98f9472a284aba377a0343a6335fa8f549e342b61b7bb4533eac1c4019a8f"></a>
<a id="agroup__bt__pbap_html_ggae51b98f9472a284aba377a0343a6335faa77889b21608736c840c5870236b8b7f"></a>
<a id="agroup__bt__pbap_html_ggae51b98f9472a284aba377a0343a6335faa7ab39682e0f35c54ff5e67c76b3741c"></a>
<a id="agroup__bt__pbap_html_ggae51b98f9472a284aba377a0343a6335faa9087f0238d221a036a599b2bcceee5e"></a>
<a id="agroup__bt__pbap_html_ggae51b98f9472a284aba377a0343a6335fadd13a4cd31cacd5a1ee3738f6514d7bf"></a>
<a id="agroup__bt__pbap_html_ggae51b98f9472a284aba377a0343a6335faeba96c52f51b6bcf64cdab4826104603"></a>
<a id="agroup__bt__pbap_html_ggae51b98f9472a284aba377a0343a6335fafcac813cc74198792f97e1eba6594a93"></a>
<a id="agroup__bt__pbap_html_ggafc697dd2db191451f1d2334f5758be69a7216e629be9047a08a48be8210c272bc"></a>
<a id="agroup__bt__pbap_html_ggafc697dd2db191451f1d2334f5758be69a7c22ec68b0d24778b1a0677b31f335a3"></a>
<a id="agroup__bt__pbap_html_ggafc697dd2db191451f1d2334f5758be69afb959ef0be8bd3e0e06eb26d8a186772"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys-util_html_gacfdade52af3ced2d87472cec47d14a76"></a>
<a id="akernel_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astring_8h_html"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__goep__transport__l2cap__server_html"></a>
<a id="astructbt__goep__transport__rfcomm__server_html"></a>
<a id="astructbt__goep__transport_html"></a>
<a id="astructbt__goep_html"></a>
<a id="astructbt__obex__client_html"></a>
<a id="astructbt__obex__server_html"></a>
<a id="astructbt__pbap__pce__cb_html"></a>
<a id="astructbt__pbap__pce__cb_html_a22175f0418e8e58a8a09eccc37f4dfc3"></a>
<a id="astructbt__pbap__pce__cb_html_a3e643a024fa72df83836669d87803f95"></a>
<a id="astructbt__pbap__pce__cb_html_a3fd377996356c7cf6b6e6f15f731f249"></a>
<a id="astructbt__pbap__pce__cb_html_a3fd9b659366d8804e9b575c8146f2767"></a>
<a id="astructbt__pbap__pce__cb_html_a6aab1615dc299ed1b9c37f6c89462c77"></a>
<a id="astructbt__pbap__pce__cb_html_a7c912fe7083ffcb9944e103e8f9ff314"></a>
<a id="astructbt__pbap__pce__cb_html_a865670561310a210b6dd3c701d9b8e9c"></a>
<a id="astructbt__pbap__pce__cb_html_aa9cab8cafac0fa94c1994b95498a3f76"></a>
<a id="astructbt__pbap__pce__cb_html_ac89246b832f6d548d41bf79b2059e3e2"></a>
<a id="astructbt__pbap__pce__cb_html_adf7bef6a90e1db928a077d1db4955c07"></a>
<a id="astructbt__pbap__pce__cb_html_aeb6cb005d085610ff73004ebf855e50d"></a>
<a id="astructbt__pbap__pce_html"></a>
<a id="astructbt__pbap__pce_html_aa1b9c9c733cf5e7277697a2e6119204b"></a>
<a id="astructbt__pbap__pse__cb_html"></a>
<a id="astructbt__pbap__pse__cb_html_a1601fff1b1b320de8c20f62a0b3779b4"></a>
<a id="astructbt__pbap__pse__cb_html_a16cb90f530643c371cdb63ad0af24cfa"></a>
<a id="astructbt__pbap__pse__cb_html_a2fb6ed5d1728989b3356664d1b037dce"></a>
<a id="astructbt__pbap__pse__cb_html_a508df68d361d6bbcac77c07326ad216c"></a>
<a id="astructbt__pbap__pse__cb_html_a7fa67e965c441cf8d6b8a1382c68e7cf"></a>
<a id="astructbt__pbap__pse__cb_html_a99fb49679cf7f737e3d6d431fe529006"></a>
<a id="astructbt__pbap__pse__cb_html_a9ad9db6bff9050ab7253101058356b45"></a>
<a id="astructbt__pbap__pse__cb_html_a9b79c775e8f4bc1196f0496e1e4042af"></a>
<a id="astructbt__pbap__pse__cb_html_a9f524ac72b376c1ce033574d75cdc5a0"></a>
<a id="astructbt__pbap__pse__cb_html_aae32aaaf8d68858542127abcbadbd113"></a>
<a id="astructbt__pbap__pse__cb_html_ada011b1e352408abfcf67795bf3672e5"></a>
<a id="astructbt__pbap__pse__l2cap_html"></a>
<a id="astructbt__pbap__pse__l2cap_html_a34e91052e02e8d9e043093cffd207157"></a>
<a id="astructbt__pbap__pse__l2cap_html_ae6342b794786c14db63503a9d0ce2e48"></a>
<a id="astructbt__pbap__pse__rfcomm_html"></a>
<a id="astructbt__pbap__pse__rfcomm_html_a376163bc7b0344f71b44b75494145cac"></a>
<a id="astructbt__pbap__pse__rfcomm_html_a7901c8e1856b829a7580331f5e5f629b"></a>
<a id="astructbt__pbap__pse_html"></a>
<a id="astructbt__pbap__pse_html_a05196786dfb6f2d4e2a3e6add38bc3d1"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf_html"></a>

```c


/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_PBAP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_PBAP_H_


#include <zephyr/kernel.h>
#include <string.h>
#include <errno.h>
#include <stdbool.h>

#include <zephyr/bluetooth/classic/goep.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_PBAP_UUID                                                                               \
        (const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
                BT_UUID_128_ENCODE(0x796135f0, 0xf0c5, 0x11d8, 0x0966, 0x0800200c9a66))

#define BT_PBAP_PULL_PHONE_BOOK_TYPE "x-bt/phonebook"

#define BT_PBAP_PULL_VCARD_LISTING_TYPE "x-bt/vcard-listing"

#define BT_PBAP_PULL_VCARD_ENTRY_TYPE "x-bt/vcard"

#define BT_PBAP_SET_PHONE_BOOK_FLAGS_UP                                                            \
        (BT_OBEX_SETPATH_FLAG_BACKUP | BT_OBEX_SETPATH_FLAG_NO_CREATE)

#define BT_PBAP_SET_PHONE_BOOK_FLAGS_DOWN_OR_ROOT BT_OBEX_SETPATH_FLAG_NO_CREATE

enum __packed bt_pbap_rsp_code {
        BT_PBAP_RSP_CODE_CONTINUE = BT_OBEX_RSP_CODE_CONTINUE,
        BT_PBAP_RSP_CODE_OK = BT_OBEX_RSP_CODE_OK,
        BT_PBAP_RSP_CODE_SUCCESS = BT_OBEX_RSP_CODE_SUCCESS,
        BT_PBAP_RSP_CODE_BAD_REQ = BT_OBEX_RSP_CODE_BAD_REQ,
        BT_PBAP_RSP_CODE_UNAUTH = BT_OBEX_RSP_CODE_UNAUTH,
        BT_PBAP_RSP_CODE_FORBIDDEN = BT_OBEX_RSP_CODE_FORBIDDEN,
        BT_PBAP_RSP_CODE_NOT_FOUND = BT_OBEX_RSP_CODE_NOT_FOUND,
        BT_PBAP_RSP_CODE_NOT_ACCEPT = BT_OBEX_RSP_CODE_NOT_ACCEPT,
        BT_PBAP_RSP_CODE_PRECON_FAIL = BT_OBEX_RSP_CODE_PRECON_FAIL,
        BT_PBAP_RSP_CODE_NOT_IMPL = BT_OBEX_RSP_CODE_NOT_IMPL,
        BT_PBAP_RSP_CODE_UNAVAIL = BT_OBEX_RSP_CODE_UNAVAIL,
};

enum bt_pbap_appl_param_order {
        BT_PBAP_APPL_PARAM_ORDER_INDEXED = 0x00,
        BT_PBAP_APPL_PARAM_ORDER_ALPHABETICAL = 0x01,
        BT_PBAP_APPL_PARAM_ORDER_PHONETIC = 0x02,
};

enum bt_pbap_appl_param_search_property {
        BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NAME = 0x00,
        BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NUMBER = 0x01,
        BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_SOUND = 0x02,
};

enum bt_pbap_appl_param_format {
        BT_PBAP_APPL_PARAM_FORMAT_2_1 = 0x00,
        BT_PBAP_APPL_PARAM_FORMAT_3_0 = 0x01,
};

enum bt_pbap_appl_param_vcard_selector_operator {
        BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_OR = 0x00,
        BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_AND = 0x01,
};

enum bt_pbap_appl_param_reset_new_missed_calls {
        BT_PBAP_APPL_PARAM_RESET_NEW_MISSED_CALLS = 0x01,
};

enum bt_pbap_appl_param_property_mask {
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_VERSION = BIT64(0),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_FN = BIT64(1),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_N = BIT64(2),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PHOTO = BIT64(3),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_BDAY = BIT64(4),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ADR = BIT64(5),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LABEL = BIT64(6),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TEL = BIT64(7),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_EMAIL = BIT64(8),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_MAILER = BIT64(9),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TZ = BIT64(10),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_GEO = BIT64(11),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TITLE = BIT64(12),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ROLE = BIT64(13),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LOGO = BIT64(14),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_AGENT = BIT64(15),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ORG = BIT64(16),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NOTE = BIT64(17),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_REV = BIT64(18),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SOUND = BIT64(19),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_URL = BIT64(20),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_UID = BIT64(21),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_KEY = BIT64(22),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NICKNAME = BIT64(23),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CATEGORIES = BIT64(24),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PRODID = BIT64(25),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CLASS = BIT64(26),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SORT_STRING = BIT64(27),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_IRMC_CALL_DATETIME = BIT64(28),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_SPEEDDIALKEY = BIT64(29),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UCI = BIT64(30),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UID = BIT64(31),
        BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PROPRIETARY_FILTER = BIT64(39),
};

enum __packed bt_pbap_appl_param_tag_id {
        BT_PBAP_APPL_PARAM_TAG_ID_ORDER = 0x01,
        BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_VALUE = 0x02,
        BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_PROPERTY = 0x03,
        BT_PBAP_APPL_PARAM_TAG_ID_MAX_LIST_COUNT = 0x04,
        BT_PBAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET = 0x05,
        BT_PBAP_APPL_PARAM_TAG_ID_PROPERTY_SELECTOR = 0x06,
        BT_PBAP_APPL_PARAM_TAG_ID_FORMAT = 0x07,
        BT_PBAP_APPL_PARAM_TAG_ID_PHONEBOOK_SIZE = 0x08,
        BT_PBAP_APPL_PARAM_TAG_ID_NEW_MISSED_CALLS = 0x09,
        BT_PBAP_APPL_PARAM_TAG_ID_PRIMARY_FOLDER_VERSION = 0x0a,
        BT_PBAP_APPL_PARAM_TAG_ID_SECONDARY_FOLDER_VERSION = 0x0b,
        BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR = 0x0c,
        BT_PBAP_APPL_PARAM_TAG_ID_DATABASE_IDENTIFIER = 0x0d,
        BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR_OPERATOR = 0x0e,
        BT_PBAP_APPL_PARAM_TAG_ID_RESET_NEW_MISSED_CALLS = 0x0f,
        BT_PBAP_APPL_PARAM_TAG_ID_SUPPORTED_FEATURES = 0x10,
};

enum bt_pbap_supported_feature {
        BT_PBAP_SUPPORTED_FEATURE_DOWNLOAD = BIT(0),
        BT_PBAP_SUPPORTED_FEATURE_BROWSING = BIT(1),
        BT_PBAP_SUPPORTED_FEATURE_DATABASE_IDENTIFIER = BIT(2),
        BT_PBAP_SUPPORTED_FEATURE_FOLDER_VERSION_COUNTERS = BIT(3),
        BT_PBAP_SUPPORTED_FEATURE_VCARD_SELECTOR = BIT(4),
        BT_PBAP_SUPPORTED_FEATURE_ENHANCED_MISSED_CALLS = BIT(5),
        BT_PBAP_SUPPORTED_FEATURE_UCI_VCARD_PROPERTY = BIT(6),
        BT_PBAP_SUPPORTED_FEATURE_UID_VCARD_PROPERTY = BIT(7),
        BT_PBAP_SUPPORTED_FEATURE_CONTACT_REFERENCING = BIT(8),
        BT_PBAP_SUPPORTED_FEATURE_DEFAULT_CONTACT_IMAGE = BIT(9),
};

enum bt_pbap_supported_repositories {
        BT_PBAP_SUPPORTED_REPOSITORIES_LOCAL_PHONE_BOOK = BIT(0),
        BT_PBAP_SUPPORTED_REPOSITORIES_SIM = BIT(1),
        BT_PBAP_SUPPORTED_REPOSITORIES_SPEED_DIAL = BIT(2),
        BT_PBAP_SUPPORTED_REPOSITORIES_FAVORITES = BIT(3),
};

struct bt_pbap_pce;

struct bt_pbap_pce_cb {
        void (*rfcomm_connected)(struct bt_conn *conn, struct bt_pbap_pce *pbap_pce);

        void (*rfcomm_disconnected)(struct bt_pbap_pce *pbap_pce);

        void (*l2cap_connected)(struct bt_conn *conn, struct bt_pbap_pce *pbap_pce);

        void (*l2cap_disconnected)(struct bt_pbap_pce *pbap_pce);

        void (*connect)(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, uint8_t version,
                        uint16_t mopl, struct net_buf *buf);

        void (*disconnect)(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf);

        void (*pull_phone_book)(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code,
                                struct net_buf *buf);

        void (*pull_vcard_listing)(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code,
                                   struct net_buf *buf);

        void (*pull_vcard_entry)(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code,
                                 struct net_buf *buf);

        void (*set_phone_book)(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf);

        void (*abort)(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf);
};

struct bt_pbap_pce {
        struct bt_pbap_pce_cb *cb;

        struct bt_goep_transport _goep_transport;

        struct bt_goep _goep;

        atomic_t _transport_state;

        uint32_t _conn_id;

        struct bt_obex_client _client;

        atomic_t _state;

        void (*_rsp_cb)(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf);

        const char *_req_type;
};

int bt_pbap_pce_rfcomm_connect(struct bt_conn *conn, struct bt_pbap_pce *pbap_pce,
                               struct bt_pbap_pce_cb *cb, uint8_t channel);

int bt_pbap_pce_rfcomm_disconnect(struct bt_pbap_pce *pbap_pce);

int bt_pbap_pce_l2cap_connect(struct bt_conn *conn, struct bt_pbap_pce *pbap_pce,
                              struct bt_pbap_pce_cb *cb, uint16_t psm);

int bt_pbap_pce_l2cap_disconnect(struct bt_pbap_pce *pbap_pce);

struct net_buf *bt_pbap_pce_create_pdu(struct bt_pbap_pce *pbap_pce, struct net_buf_pool *pool);

int bt_pbap_pce_connect(struct bt_pbap_pce *pbap_pce, uint16_t mopl, struct net_buf *buf);

int bt_pbap_pce_disconnect(struct bt_pbap_pce *pbap_pce, struct net_buf *buf);

int bt_pbap_pce_pull_phone_book(struct bt_pbap_pce *pbap_pce, struct net_buf *buf);

int bt_pbap_pce_pull_vcard_listing(struct bt_pbap_pce *pbap_pce, struct net_buf *buf);

int bt_pbap_pce_pull_vcard_entry(struct bt_pbap_pce *pbap_pce, struct net_buf *buf);

int bt_pbap_pce_set_phone_book(struct bt_pbap_pce *pbap_pce, uint8_t flags, struct net_buf *buf);

int bt_pbap_pce_abort(struct bt_pbap_pce *pbap_pce, struct net_buf *buf);

struct bt_pbap_pse;

struct bt_pbap_pse_cb {

        void (*rfcomm_connected)(struct bt_conn *conn, struct bt_pbap_pse *pbap_pse);

        void (*rfcomm_disconnected)(struct bt_pbap_pse *pbap_pse);

        void (*l2cap_connected)(struct bt_conn *conn, struct bt_pbap_pse *pbap_pse);

        void (*l2cap_disconnected)(struct bt_pbap_pse *pbap_pse);

        void (*connect)(struct bt_pbap_pse *pbap_pse, uint8_t version, uint16_t mopl,
                        struct net_buf *buf);

        void (*disconnect)(struct bt_pbap_pse *pbap_pse, struct net_buf *buf);

        void (*pull_phone_book)(struct bt_pbap_pse *pbap_pse, struct net_buf *buf);

        void (*pull_vcard_listing)(struct bt_pbap_pse *pbap_pse, struct net_buf *buf);

        void (*pull_vcard_entry)(struct bt_pbap_pse *pbap_pse, struct net_buf *buf);

        void (*set_phone_book)(struct bt_pbap_pse *pbap_pse, uint8_t flags, struct net_buf *buf);

        void (*abort)(struct bt_pbap_pse *pbap_pse, struct net_buf *buf);
};

struct bt_pbap_pse_rfcomm {
        struct bt_goep_transport_rfcomm_server server;

        int (*accept)(struct bt_conn *conn, struct bt_pbap_pse_rfcomm *pbap_pse_rfcomm,
                      struct bt_pbap_pse **pbap_pse);
};

struct bt_pbap_pse_l2cap {
        struct bt_goep_transport_l2cap_server server;

        int (*accept)(struct bt_conn *conn, struct bt_pbap_pse_l2cap *pbap_pse_l2cap,
                      struct bt_pbap_pse **pbap_pse);
};

struct bt_pbap_pse {
        struct bt_pbap_pse_cb *cb;

        struct bt_goep_transport _goep_transport;

        struct bt_goep _goep;

        atomic_t _transport_state;

        uint32_t _conn_id;

        struct bt_obex_server _server;

        atomic_t _state;

        void (*_req_cb)(struct bt_pbap_pse *pse, struct net_buf *buf);

        const char *_optype;

        atomic_t _flags;
};

struct net_buf *bt_pbap_pse_create_pdu(struct bt_pbap_pse *pbap_pse, struct net_buf_pool *pool);

int bt_pbap_pse_rfcomm_register(struct bt_pbap_pse_rfcomm *server);

int bt_pbap_pse_l2cap_register(struct bt_pbap_pse_l2cap *server);

int bt_pbap_pse_register(struct bt_pbap_pse *pbap_pse, struct bt_pbap_pse_cb *cb);

int bt_pbap_pse_connect_rsp(struct bt_pbap_pse *pbap_pse, uint16_t mopl, uint8_t rsp_code,
                            struct net_buf *buf);

int bt_pbap_pse_disconnect_rsp(struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf);

int bt_pbap_pse_pull_phone_book_rsp(struct bt_pbap_pse *pbap_pse, uint8_t rsp_code,
                                    struct net_buf *buf);

int bt_pbap_pse_pull_vcard_listing_rsp(struct bt_pbap_pse *pbap_pse, uint8_t rsp_code,
                                       struct net_buf *buf);

int bt_pbap_pse_pull_vcard_entry_rsp(struct bt_pbap_pse *pbap_pse, uint8_t rsp_code,
                                     struct net_buf *buf);

int bt_pbap_pse_set_phone_book_rsp(struct bt_pbap_pse *pbap_pse, uint8_t rsp_code,
                                   struct net_buf *buf);

int bt_pbap_pse_abort_rsp(struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_PBAP_H_ */
```

## 644.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 968 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_PBAP_H_`。

## 644.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pbap_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/bluetooth/classic/goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h.html)
- [bt_pbap_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9d9697d62b6bdbbc4feb0cf4b9776b58)
- [BT_PBAP_RSP_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a661acfbba2e792ee4444453650db00eb)
- [BT_OBEX_RSP_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a7e38ca653283f53b62fa4b21f48d998a)
- [BT_PBAP_RSP_CODE_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a904e13430e8318623f1a785b94caee93)
- [BT_OBEX_RSP_CODE_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a881d3098a198dc1eced2150a213d1054)
- [BT_PBAP_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a26f8b1cb1f6bc983b1508b5a2e298a3e)
- [BT_OBEX_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9af449d3c85fbec550c76e29287a626789)
- [BT_PBAP_RSP_CODE_BAD_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a3130502de3a9c28985692f8d93b6ad08)
- [BT_OBEX_RSP_CODE_BAD_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a2d2ff2c6ec42d9e80dc4e841e19d31ee)
- [BT_PBAP_RSP_CODE_UNAUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a9f3978e6433273f9a1af3e0c91ae33cd)
- [BT_OBEX_RSP_CODE_UNAUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9acfbc9161dddf6859dd8e8ac70cf8d446)
- [BT_PBAP_RSP_CODE_FORBIDDEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a7cab8c591dca0bc0279c6463ece416d6)
- [BT_OBEX_RSP_CODE_FORBIDDEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a4b7a12b0e11747d1a470e8f559b55ea8)
- [BT_PBAP_RSP_CODE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a2f4a1259666bfbf84c8c8ac02faa8683)
- [BT_OBEX_RSP_CODE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a2b91abe9e010465f9514f37477b993e0)
- [BT_PBAP_RSP_CODE_NOT_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a806a9638aa9ca07d52f2dbb6946b6594)
- [BT_OBEX_RSP_CODE_NOT_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a48f773daa7f2dabaadc37142ec32ffd1)
- [BT_PBAP_RSP_CODE_PRECON_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58ab34bbcad2a7fe5c2b9f2efa511b69ccf)
- [BT_OBEX_RSP_CODE_PRECON_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aacc05fd2528e29fbd53eb5ff940f9079)
- [BT_PBAP_RSP_CODE_NOT_IMPL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58aa0c1cbc8611c6a5f39d1d61858ea85cb)
- [BT_OBEX_RSP_CODE_NOT_IMPL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aba8108ac6b050d3dad845a5e8cb42eaf)
- [BT_PBAP_RSP_CODE_UNAVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a722cfbba810a0646a340d8bba82282fa)
- [BT_OBEX_RSP_CODE_UNAVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a613e95b96eaba0522070b620b4b90953)
- [bt_pbap_appl_param_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac6c48c5b202c19567a4ddb008626f174)
- [BT_PBAP_APPL_PARAM_ORDER_INDEXED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggac6c48c5b202c19567a4ddb008626f174ab03a1c4e18ea46da6c28fe83a850b510)
- [BT_PBAP_APPL_PARAM_ORDER_ALPHABETICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggac6c48c5b202c19567a4ddb008626f174a59e2999c6d5af45b12c88d8bf78c7252)
- [BT_PBAP_APPL_PARAM_ORDER_PHONETIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggac6c48c5b202c19567a4ddb008626f174accbdbbf7c94a707b77c6b249760f37a1)
- [bt_pbap_appl_param_search_property](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gafc697dd2db191451f1d2334f5758be69)
- [BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggafc697dd2db191451f1d2334f5758be69afb959ef0be8bd3e0e06eb26d8a186772)
- [BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggafc697dd2db191451f1d2334f5758be69a7c22ec68b0d24778b1a0677b31f335a3)
- [BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggafc697dd2db191451f1d2334f5758be69a7216e629be9047a08a48be8210c272bc)
- [bt_pbap_appl_param_format](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga5cf30994d6344a67b22eb01baf863b1b)
- [BT_PBAP_APPL_PARAM_FORMAT_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga5cf30994d6344a67b22eb01baf863b1baf5f30663b6083d8c09950e71dc6e1e0b)
- [BT_PBAP_APPL_PARAM_FORMAT_3_0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga5cf30994d6344a67b22eb01baf863b1ba0fa84dbd58771867b547805099689a3a)
- [bt_pbap_appl_param_vcard_selector_operator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga76ceaa735d7bc5ee97d665d497b896cd)
- [BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga76ceaa735d7bc5ee97d665d497b896cda338230ca0c8d07ca4a5cced68cf9faf4)
- [BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_AND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga76ceaa735d7bc5ee97d665d497b896cda4f1435ad0230025a1bf612fd38df67a9)
- [bt_pbap_appl_param_reset_new_missed_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gadc3ace27caf970d0f2f8c8278e50c7fc)
- [BT_PBAP_APPL_PARAM_RESET_NEW_MISSED_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadc3ace27caf970d0f2f8c8278e50c7fca99adb79a6d49413c2c3dc83ff4686e5d)
- [bt_pbap_appl_param_property_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga81e3d8885dddfae8f8e2714ef9173949)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a9dc945e68284feb0c84c3f266b504e9a)
- [BIT64](../util_reference/P001_通用工具公共接口.md#gacfdade52af3ced2d87472cec47d14a76)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_FN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a4eccbde165789980859146504dc6ad79)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_N](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a095c248ed7a21c3024843b06c8757c65)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PHOTO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949abbf728e6870fb11e11095741261dce74)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_BDAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ab1029f770ff972cd56ca27149697b3c1)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ADR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a392c7a7f408f80443e330e7e8317790f)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LABEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a534c44365efffc777b134db0d7158d01)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949aba04655292e204ffea1ea8e6f868990a)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ae97d497323807766a249a354d9c73440)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_MAILER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949aaedbb7e84f50781fa88eaff8859bf0c0)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a8eeef93a6fb6d1f90688444d4c025d75)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_GEO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a2bd2e420601d0d8dfd6d308b48ab3cf5)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TITLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a5cb26f5f8d5baff7b2d28e030db326f1)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ROLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a2f7b5161e2440abaa4dbcaf4351f9dc8)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LOGO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949af45314b48bb91277d8ad84d29e44ce54)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_AGENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a8030f80cf155692c1728775885c0786b)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ORG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ac94b5f034af49ba23222988ac05dca41)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a9e6232e6968a9604421a81a4d364e868)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_REV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949aa5acc89efeae0ef6fabbcdbc5c461cf0)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a07399ae04375a6c435f34815b734aabb)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a31e2f9be865df16c883964b8abaea828)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_UID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a0d8adde858f93c7d5b765fb0488f22ce)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a1c16e137b53c6c88152ed49d693dd32b)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NICKNAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a1622cc47e9c5d359d327b9175829b005)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CATEGORIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a9b2cb462f56b4abbda146fc3b6e0250b)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PRODID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a12d9060eef27b4c048064df7b00faf7f)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a728ddfce7f0f93564e6e657d3fd9f9ca)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SORT_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a7cfcd8e622d1adb99c5ad598b2642720)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_IRMC_CALL_DATETIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a6af54c454719c9a5baa75db6feb3c6e6)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_SPEEDDIALKEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ad1b5c9ec39747786c90c89b190235b5e)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a1fe34f3b6c0a3c9ca0966106052faa61)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a587cb6926e50eca38c633019312208d5)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PROPRIETARY_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ab98d31a99ac92b189b8963f275d6846b)
- [bt_pbap_appl_param_tag_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gadbc19ba92332972e5d22e213c7618fa0)
- [BT_PBAP_APPL_PARAM_TAG_ID_ORDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a32182e2f399ec292ea652dd7f04bbdee)
- [BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a4a1bbc25a06c89dd948542ec700a7323)
- [BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_PROPERTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0af4a5a102fc189ad256b75091522d1b66)
- [BT_PBAP_APPL_PARAM_TAG_ID_MAX_LIST_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0aa17305107ed8979b917dab98f04442bf)
- [BT_PBAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a2cf69d5233c590f708571c2447539025)
- [BT_PBAP_APPL_PARAM_TAG_ID_PROPERTY_SELECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a7894ebcf543e20b5c3369ec6632fb9c9)
- [BT_PBAP_APPL_PARAM_TAG_ID_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0ac9aade48ff6a95d27443f817daf6ba75)
- [BT_PBAP_APPL_PARAM_TAG_ID_PHONEBOOK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a0bc424753f8b1da0b3209c38925c6162)
- [BT_PBAP_APPL_PARAM_TAG_ID_NEW_MISSED_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0acc1b3f202aa38ff027a63aecb9108641)
- [BT_PBAP_APPL_PARAM_TAG_ID_PRIMARY_FOLDER_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0abea06880695df75ef9ca68e94e4596b4)
- [BT_PBAP_APPL_PARAM_TAG_ID_SECONDARY_FOLDER_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a793e24d13b717616ee8eb09792d19310)
- [BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0aeac485e4bb2ca3d4fcdaf0e76fd55a08)
- [BT_PBAP_APPL_PARAM_TAG_ID_DATABASE_IDENTIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a60027135eafa915cac55a1cc59d68b4f)
- [BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR_OPERATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0acfbe210e7ef87a3a07b00f05b62f7616)
- [BT_PBAP_APPL_PARAM_TAG_ID_RESET_NEW_MISSED_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a4eb10ced494b26ad1380f6808574716c)
- [BT_PBAP_APPL_PARAM_TAG_ID_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a66bf205d11a351aa10fba0c6648600db)
- [bt_pbap_supported_feature](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gae51b98f9472a284aba377a0343a6335f)
- [BT_PBAP_SUPPORTED_FEATURE_DOWNLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fadd13a4cd31cacd5a1ee3738f6514d7bf)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_PBAP_SUPPORTED_FEATURE_BROWSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335faeba96c52f51b6bcf64cdab4826104603)
- [BT_PBAP_SUPPORTED_FEATURE_DATABASE_IDENTIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335faa77889b21608736c840c5870236b8b7f)
- [BT_PBAP_SUPPORTED_FEATURE_FOLDER_VERSION_COUNTERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fafcac813cc74198792f97e1eba6594a93)
- [BT_PBAP_SUPPORTED_FEATURE_VCARD_SELECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fa04a72163c9a4aa1ca94e096fc61c0110)
- [BT_PBAP_SUPPORTED_FEATURE_ENHANCED_MISSED_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fa09b908bca7982fc1818791c6ff2a9d54)
- [BT_PBAP_SUPPORTED_FEATURE_UCI_VCARD_PROPERTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fa208cd02d7acabf2f6444292d2f0290ec)
- [BT_PBAP_SUPPORTED_FEATURE_UID_VCARD_PROPERTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335faa9087f0238d221a036a599b2bcceee5e)
- [BT_PBAP_SUPPORTED_FEATURE_CONTACT_REFERENCING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335faa7ab39682e0f35c54ff5e67c76b3741c)
- [BT_PBAP_SUPPORTED_FEATURE_DEFAULT_CONTACT_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fa8f549e342b61b7bb4533eac1c4019a8f)
- [bt_pbap_supported_repositories](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gadd0760a5999620762367a5dda62018b7)
- [BT_PBAP_SUPPORTED_REPOSITORIES_LOCAL_PHONE_BOOK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadd0760a5999620762367a5dda62018b7a58a43511704fe46d8f8cdbb8d0e6f9fe)
- [BT_PBAP_SUPPORTED_REPOSITORIES_SIM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadd0760a5999620762367a5dda62018b7aaf5d738a116dd37e2bc18bec07858415)
- [BT_PBAP_SUPPORTED_REPOSITORIES_SPEED_DIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadd0760a5999620762367a5dda62018b7aa3f4d6139aad54ee40d60c9ab474dc48)
- [BT_PBAP_SUPPORTED_REPOSITORIES_FAVORITES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadd0760a5999620762367a5dda62018b7adf8db04f430e9b19d75fd6396f6bf0f2)
- [bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)
- [bt_pbap_pce_cb](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md)
- [rfcomm_connected](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a22175f0418e8e58a8a09eccc37f4dfc3)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [rfcomm_disconnected](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#aeb6cb005d085610ff73004ebf855e50d)
- [l2cap_connected](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a7c912fe7083ffcb9944e103e8f9ff314)
- [l2cap_disconnected](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#aa9cab8cafac0fa94c1994b95498a3f76)
- [connect](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a865670561310a210b6dd3c701d9b8e9c)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [disconnect](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#ac89246b832f6d548d41bf79b2059e3e2)
- [pull_phone_book](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a3fd377996356c7cf6b6e6f15f731f249)
- [pull_vcard_listing](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a3e643a024fa72df83836669d87803f95)
- [pull_vcard_entry](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a3fd9b659366d8804e9b575c8146f2767)
- [set_phone_book](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a6aab1615dc299ed1b9c37f6c89462c77)
- [abort](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#adf7bef6a90e1db928a077d1db4955c07)
- [cb](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md#aa1b9c9c733cf5e7277697a2e6119204b)
- [bt_goep_transport](../bluetooth_service_model_reference/P071_bt_goep_transport_结构体.md)
- [bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)
- [bt_pbap_pce_rfcomm_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9fcd75bb18c48756dfa4695890662ab0)
- [bt_pbap_pce_rfcomm_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gaae2eac838c1b825f5d31d7073608e56d)
- [bt_pbap_pce_l2cap_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gae9506155e96d3f641ee928754439f579)
- [bt_pbap_pce_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gad407918b6c075045339aecd55b70db21)
- [bt_pbap_pce_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gab326aadad5f12827f08f6525b7dc5458)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bt_pbap_pce_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga29d4e867858a96606a623313acc808d9)
- [bt_pbap_pce_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga5af0c3016e948bc27df328432ffa9455)
- [bt_pbap_pce_pull_phone_book](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga07f8db1528fc15bed243fc5da787354f)
- [bt_pbap_pce_pull_vcard_listing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga71ba43da527c77f3eaf7d43ae5c22cae)
- [bt_pbap_pce_pull_vcard_entry](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac1f07e0eb9b256010fdbcf29b71701c6)
- [bt_pbap_pce_set_phone_book](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga15403745f42ba10ba1dd9552895e111d)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bt_pbap_pce_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gab24a2cb71edfa1d5e59c33fabc01c7d9)
- [bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)
- [bt_pbap_pse_cb](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md)
- [rfcomm_connected](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a508df68d361d6bbcac77c07326ad216c)
- [rfcomm_disconnected](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a9b79c775e8f4bc1196f0496e1e4042af)
- [l2cap_connected](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a99fb49679cf7f737e3d6d431fe529006)
- [l2cap_disconnected](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#aae32aaaf8d68858542127abcbadbd113)
- [connect](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#ada011b1e352408abfcf67795bf3672e5)
- [disconnect](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a9ad9db6bff9050ab7253101058356b45)
- [pull_phone_book](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a2fb6ed5d1728989b3356664d1b037dce)
- [pull_vcard_listing](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a16cb90f530643c371cdb63ad0af24cfa)
- [pull_vcard_entry](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a1601fff1b1b320de8c20f62a0b3779b4)
- [set_phone_book](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a9f524ac72b376c1ce033574d75cdc5a0)
- [abort](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a7fa67e965c441cf8d6b8a1382c68e7cf)
- [bt_pbap_pse_rfcomm](../bluetooth_service_model_reference/P154_bt_pbap_pse_rfcomm_结构体.md)
- [bt_goep_transport_rfcomm_server](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md)
- [server](../bluetooth_service_model_reference/P154_bt_pbap_pse_rfcomm_结构体.md#a7901c8e1856b829a7580331f5e5f629b)
- [accept](../bluetooth_service_model_reference/P154_bt_pbap_pse_rfcomm_结构体.md#a376163bc7b0344f71b44b75494145cac)
- [bt_pbap_pse_l2cap](../bluetooth_service_model_reference/P153_bt_pbap_pse_l2cap_结构体.md)
- [bt_goep_transport_l2cap_server](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md)
- [server](../bluetooth_service_model_reference/P153_bt_pbap_pse_l2cap_结构体.md#ae6342b794786c14db63503a9d0ce2e48)
- [accept](../bluetooth_service_model_reference/P153_bt_pbap_pse_l2cap_结构体.md#a34e91052e02e8d9e043093cffd207157)
- [cb](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md#a05196786dfb6f2d4e2a3e6add38bc3d1)
- [bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)
- [bt_pbap_pse_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gae26500d48fae5f26946ab7a4e261993c)
- [bt_pbap_pse_rfcomm_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga72b9420a34975c9691690977169bcec6)
- [bt_pbap_pse_l2cap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gab37e9ea163060e8b770da56e5a6415cb)
- [bt_pbap_pse_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga15c39f4afb996a37b43acd51cc82ed53)
- [bt_pbap_pse_connect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac76cb47df9f747f222d7cdbe627d3ead)
- [bt_pbap_pse_disconnect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gafa7ebec6db37286b0ca54ed1d9f4ca02)
- [bt_pbap_pse_pull_phone_book_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac8ef77affecb5316991afca6c1005f62)
- [bt_pbap_pse_pull_vcard_listing_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac511c99ae0c2d0f391f5dbf150599390)
- [bt_pbap_pse_pull_vcard_entry_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gacdcbb62a6999c833e4e6d0846aad28d6)
- [bt_pbap_pse_set_phone_book_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga09e255e0c5328a1f1e7286b7100eeb61)
- [bt_pbap_pse_abort_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9766bda140034251ba3287bfa116f359)
- [goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [bt_pbap_pce_cb::rfcomm_connected](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a22175f0418e8e58a8a09eccc37f4dfc3)
- [bt_pbap_pce_cb::pull_vcard_listing](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a3e643a024fa72df83836669d87803f95)
- [bt_pbap_pce_cb::pull_phone_book](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a3fd377996356c7cf6b6e6f15f731f249)
- [bt_pbap_pce_cb::pull_vcard_entry](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a3fd9b659366d8804e9b575c8146f2767)
- [bt_pbap_pce_cb::set_phone_book](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a6aab1615dc299ed1b9c37f6c89462c77)
- [bt_pbap_pce_cb::l2cap_connected](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a7c912fe7083ffcb9944e103e8f9ff314)
- [bt_pbap_pce_cb::connect](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#a865670561310a210b6dd3c701d9b8e9c)
- [bt_pbap_pce_cb::l2cap_disconnected](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#aa9cab8cafac0fa94c1994b95498a3f76)
- [bt_pbap_pce_cb::disconnect](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#ac89246b832f6d548d41bf79b2059e3e2)
- [bt_pbap_pce_cb::abort](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#adf7bef6a90e1db928a077d1db4955c07)
- [bt_pbap_pce_cb::rfcomm_disconnected](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md#aeb6cb005d085610ff73004ebf855e50d)
- [bt_pbap_pce::cb](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md#aa1b9c9c733cf5e7277697a2e6119204b)
- [bt_pbap_pse_cb::pull_vcard_entry](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a1601fff1b1b320de8c20f62a0b3779b4)
- [bt_pbap_pse_cb::pull_vcard_listing](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a16cb90f530643c371cdb63ad0af24cfa)
- [bt_pbap_pse_cb::pull_phone_book](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a2fb6ed5d1728989b3356664d1b037dce)
- [bt_pbap_pse_cb::rfcomm_connected](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a508df68d361d6bbcac77c07326ad216c)
- [bt_pbap_pse_cb::abort](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a7fa67e965c441cf8d6b8a1382c68e7cf)
- [bt_pbap_pse_cb::l2cap_connected](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a99fb49679cf7f737e3d6d431fe529006)
- [bt_pbap_pse_cb::disconnect](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a9ad9db6bff9050ab7253101058356b45)
- [bt_pbap_pse_cb::rfcomm_disconnected](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a9b79c775e8f4bc1196f0496e1e4042af)
- [bt_pbap_pse_cb::set_phone_book](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#a9f524ac72b376c1ce033574d75cdc5a0)
- [bt_pbap_pse_cb::l2cap_disconnected](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#aae32aaaf8d68858542127abcbadbd113)
- [bt_pbap_pse_cb::connect](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md#ada011b1e352408abfcf67795bf3672e5)
- [bt_pbap_pse_l2cap::accept](../bluetooth_service_model_reference/P153_bt_pbap_pse_l2cap_结构体.md#a34e91052e02e8d9e043093cffd207157)
- [bt_pbap_pse_l2cap::server](../bluetooth_service_model_reference/P153_bt_pbap_pse_l2cap_结构体.md#ae6342b794786c14db63503a9d0ce2e48)
- [bt_pbap_pse_rfcomm::accept](../bluetooth_service_model_reference/P154_bt_pbap_pse_rfcomm_结构体.md#a376163bc7b0344f71b44b75494145cac)
- [bt_pbap_pse_rfcomm::server](../bluetooth_service_model_reference/P154_bt_pbap_pse_rfcomm_结构体.md#a7901c8e1856b829a7580331f5e5f629b)
- [bt_pbap_pse::cb](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md#a05196786dfb6f2d4e2a3e6add38bc3d1)

---

[上一章](P643_pat9136.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P645_pbp.h_源码浏览.md)
