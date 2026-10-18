---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-21
title: ots.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ots_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_ots.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ots_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ots_8h.html)。

## 21.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
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
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00057"></a>
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
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00108"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="foldopen00136"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="foldopen00143"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="foldopen00157"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="foldopen00164"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="foldopen00178"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="foldopen00185"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="foldopen00192"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="foldopen00199"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="foldopen00206"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="foldopen00213"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="foldopen00217"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00243"></a>
<a id="l00244"></a>
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
<a id="l00260"></a>
<a id="l00261"></a>
<a id="foldopen00262"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="foldopen00271"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="foldopen00285"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="foldopen00292"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="foldopen00299"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="foldopen00306"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="foldopen00313"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="foldopen00320"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="foldopen00327"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="foldopen00334"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="foldopen00341"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="foldopen00348"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="foldopen00355"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="foldopen00362"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="foldopen00369"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="foldopen00376"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="foldopen00383"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="foldopen00390"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="foldopen00397"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="foldopen00404"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00408"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="foldopen00426"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="foldopen00433"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="foldopen00440"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="foldopen00447"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="foldopen00454"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="foldopen00461"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="foldopen00468"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="foldopen00475"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="foldopen00479"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00488"></a>
<a id="l00490"></a>
<a id="l00492"></a>
<a id="l00494"></a>
<a id="l00496"></a>
<a id="l00498"></a>
<a id="l00500"></a>
<a id="l00502"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="foldopen00508"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="foldopen00523"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="foldopen00564"></a>
<a id="l00564"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="foldopen00578"></a>
<a id="l00578"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="foldopen00606"></a>
<a id="l00606"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00691"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="foldopen00757"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="foldopen00824"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00846"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="foldopen00853"></a>
<a id="l00853"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00888"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00915"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="l00943"></a>
<a id="l00944"></a>
<a id="l00954"></a>
<a id="l00955"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="l00970"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00989"></a>
<a id="l00990"></a>
<a id="l00991"></a>
<a id="l00992"></a>
<a id="l01000"></a>
<a id="l01001"></a>
<a id="l01002"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01012"></a>
<a id="l01020"></a>
<a id="l01021"></a>
<a id="l01022"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="l01032"></a>
<a id="l01044"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01060"></a>
<a id="l01061"></a>
<a id="l01062"></a>
<a id="l01079"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01082"></a>
<a id="l01098"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01111"></a>
<a id="l01112"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="foldopen01136"></a>
<a id="l01136"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01141"></a>
<a id="l01142"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="l01151"></a>
<a id="l01152"></a>
<a id="l01153"></a>
<a id="foldopen01165"></a>
<a id="l01165"></a>
<a id="l01166"></a>
<a id="l01167"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="l01170"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01173"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="abluetooth_2uuid_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agatt_8h_html"></a>
<a id="agroup__bt__ots_html_ga1c9dcb35c8f07432fd9249a34e597819"></a>
<a id="agroup__bt__ots_html_ga5f2d0b0e4d54e00a1a96157fcfaf172b"></a>
<a id="agroup__bt__ots_html_ga63e4408702fee1be0501a715cd32c957"></a>
<a id="agroup__bt__ots_html_ga70cae251cf40a5c3c8d2a8c7e1f1e181"></a>
<a id="agroup__bt__ots_html_ga81997ab2f1718c6856e676eb9b3f72bb"></a>
<a id="agroup__bt__ots_html_ga8324cc14e8812648cc3663144591af89"></a>
<a id="agroup__bt__ots_html_ga872ba5a73fa4e617b9d48e7361af74c7"></a>
<a id="agroup__bt__ots_html_ga89fc03d68725de0b5f306c899452b1a8"></a>
<a id="agroup__bt__ots_html_ga8ad1c53325c1b77271307507317a5965"></a>
<a id="agroup__bt__ots_html_ga936f392c880c9d1a73f2bd632e5b63e0"></a>
<a id="agroup__bt__ots_html_ga9444b064c616718dae1577b21540fb9a"></a>
<a id="agroup__bt__ots_html_ga9cfd057d39ce3fe9bbecaa103ec44f77"></a>
<a id="agroup__bt__ots_html_gaa1a9db6e8aa6ee716e4fdd2e34157f46"></a>
<a id="agroup__bt__ots_html_gabba031c38c7503c1f434a761d9f65df4"></a>
<a id="agroup__bt__ots_html_gabe485816a2e536758a7ce85c593ea486"></a>
<a id="agroup__bt__ots_html_gabe637ba9febb514f7346d71696b70c73"></a>
<a id="agroup__bt__ots_html_gabf59844edd0ffd434acd94bad9a7b52c"></a>
<a id="agroup__bt__ots_html_gac270137f15596777287f68b3d6a6a11c"></a>
<a id="agroup__bt__ots_html_gac84ed7f16fa86d87531d04e2957568f9"></a>
<a id="agroup__bt__ots_html_gac9be2770fc7f2932ea2e31392d956f0a"></a>
<a id="agroup__bt__ots_html_gadefd2ccb46a686a4aa2999da5851184b"></a>
<a id="agroup__bt__ots_html_gaebdd2b8a80948d1050d42fa3963cc863"></a>
<a id="agroup__bt__ots_html_gaf11589afc37efe18dcac122835a4c95d"></a>
<a id="agroup__bt__ots_html_gafc71de8fd65212045fa26b2a81e3876d"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf"></a>
<a id="agroup__bt__ots_html_gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9"></a>
<a id="agroup__bt__ots_html_gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d"></a>
<a id="agroup__bt__ots_html_gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660"></a>
<a id="agroup__bt__ots_html_gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af"></a>
<a id="agroup__bt__ots_html_gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713"></a>
<a id="agroup__bt__ots_html_gga9bbade1b48363f0f486968723afefb45a04e4ab3e722a23370a63288c3eba8cdf"></a>
<a id="agroup__bt__ots_html_gga9bbade1b48363f0f486968723afefb45a35a3d25b637ac80e658102f27aeb7f5e"></a>
<a id="agroup__bt__ots_html_gga9bbade1b48363f0f486968723afefb45a44cb8e7804c86fce7c2eab3f3f0743c2"></a>
<a id="agroup__bt__ots_html_gga9bbade1b48363f0f486968723afefb45ac47367e5e775fa6690ac5bc03e187095"></a>
<a id="agroup__bt__ots_html_gga9bbade1b48363f0f486968723afefb45aca9770dfa7fbec3a6bc0bccb4e9e41e5"></a>
<a id="agroup__bt__ots_html_gga9bbade1b48363f0f486968723afefb45ada06e9d807f7c197bd332c0e7ca21ffb"></a>
<a id="agroup__bt__ots_html_gga9bbade1b48363f0f486968723afefb45af7c08a3c53273ac6452f607a23826e2f"></a>
<a id="agroup__bt__ots_html_gga9bbade1b48363f0f486968723afefb45aff8f3ce21a85b397b64b5d03a5fe8af9"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed"></a>
<a id="agroup__bt__ots_html_ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2"></a>
<a id="agroup__bt__ots_html_ggaebdd2b8a80948d1050d42fa3963cc863a1c2d68fccd8f252b54a11879a6dd53ab"></a>
<a id="agroup__bt__ots_html_ggaebdd2b8a80948d1050d42fa3963cc863a91d201f7f01809e2af10e10008d4eb8a"></a>
<a id="agroup__crc_html_gafc24e79ed7f978f5bb813091ef318982"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="aprintk_8h_html_a0b0af71688f7e9170103d771d4e1eab2"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__gatt__discover__params_html"></a>
<a id="astructbt__gatt__read__params_html"></a>
<a id="astructbt__gatt__subscribe__params_html"></a>
<a id="astructbt__gatt__write__params_html"></a>
<a id="astructbt__ots__cb_html"></a>
<a id="astructbt__ots__cb_html_a0c95b2bc382474be3c1ae849936a8206"></a>
<a id="astructbt__ots__cb_html_a2ef2245c017015b81c0f276f00fd6f79"></a>
<a id="astructbt__ots__cb_html_a2fd78b43691e83c1faa86c1748ab2359"></a>
<a id="astructbt__ots__cb_html_a600fa13a97f39e3bd53c524039e2733c"></a>
<a id="astructbt__ots__cb_html_ab67ca0032b8b2fd9b8fbe6c117c186dd"></a>
<a id="astructbt__ots__cb_html_ae31da190c9c6bee086e4d7f8fcd6fbb5"></a>
<a id="astructbt__ots__cb_html_ae8602aef0fd001d6768dc20c8873742d"></a>
<a id="astructbt__ots__client__cb_html"></a>
<a id="astructbt__ots__client__cb_html_a2baaf13c8de4ade034f2b58896225e0d"></a>
<a id="astructbt__ots__client__cb_html_ab6c03b98fc5c68aa8c76ada23b7dff1c"></a>
<a id="astructbt__ots__client__cb_html_ace98d27220e394b0990a8274bbd43026"></a>
<a id="astructbt__ots__client__cb_html_ad5537da9ced98a15620a7fb1e77b0218"></a>
<a id="astructbt__ots__client__cb_html_ae95f3b85758c04279ada801c001086bc"></a>
<a id="astructbt__ots__client_html"></a>
<a id="astructbt__ots__client_html_a0e6a0d97a1b8edc7a282aec12d95b0dc"></a>
<a id="astructbt__ots__client_html_a39818a4d776056212e82c4ba0626d0f1"></a>
<a id="astructbt__ots__client_html_a3aded7f58deb7f13c1c5adaa073f45f8"></a>
<a id="astructbt__ots__client_html_a65608146d1a3e141635a015eb5092ab1"></a>
<a id="astructbt__ots__client_html_a6ff62fb7570269358888c9ab865a5ec6"></a>
<a id="astructbt__ots__client_html_a787b4851389e5da47a93969db6b3edcf"></a>
<a id="astructbt__ots__client_html_a83c5d653692dc3d7dbcfd5c8e2361f96"></a>
<a id="astructbt__ots__client_html_a83cf53f6f7737620ea39dccbebe26dd4"></a>
<a id="astructbt__ots__client_html_a87d273e283941a3b9f1402e2b514134b"></a>
<a id="astructbt__ots__client_html_a8913d240d90b77ea72612ddbf816f528"></a>
<a id="astructbt__ots__client_html_a8a6d138d506a5e2732f4c51971533ce9"></a>
<a id="astructbt__ots__client_html_a98a75a8ed52a2b97be1ea273a21b8775"></a>
<a id="astructbt__ots__client_html_a99727a6d064d79c3078a04b1d6d046db"></a>
<a id="astructbt__ots__client_html_aa98ae5a468c46f1ffbfd08a6e82f420d"></a>
<a id="astructbt__ots__client_html_aabd4a625a341b4f7bdcdcff03e7ae76f"></a>
<a id="astructbt__ots__client_html_ac0fac55db40bf66aff358ce906fc8172"></a>
<a id="astructbt__ots__client_html_acbee05e7b1cd5c325a6982c6b32a732d"></a>
<a id="astructbt__ots__client_html_ad56aaee2630d75a1bb5faf0f56486c0a"></a>
<a id="astructbt__ots__client_html_ae2eebd727fd908ef2b2074c9c0b2ab4f"></a>
<a id="astructbt__ots__client_html_ae902c29051540141852869dd94edf7e0"></a>
<a id="astructbt__ots__client_html_aff756cfa5f9431ed288563a95877cb53"></a>
<a id="astructbt__ots__date__time_html"></a>
<a id="astructbt__ots__date__time_html_a09ca928752dc844e89de3957d1baae3c"></a>
<a id="astructbt__ots__date__time_html_a4eb6899dbce61478b97025958c62f586"></a>
<a id="astructbt__ots__date__time_html_ac3959eac8188df6114d70aed1ccbf3f4"></a>
<a id="astructbt__ots__date__time_html_acc118b311bfdcb3c2f7801121831fcd6"></a>
<a id="astructbt__ots__date__time_html_ae139a310b4d17078f52bfbe7707e185a"></a>
<a id="astructbt__ots__date__time_html_af348ad2613ba309de6a93d357bcce3bc"></a>
<a id="astructbt__ots__feat_html"></a>
<a id="astructbt__ots__feat_html_a309b3e38a0f15c49c06a5ffeb873cef3"></a>
<a id="astructbt__ots__feat_html_a714abba341b1f4a50edfa73dd5048f28"></a>
<a id="astructbt__ots__init__param_html"></a>
<a id="astructbt__ots__init__param_html_a22887673f03decf840470cb555f2b7f0"></a>
<a id="astructbt__ots__init__param_html_a563c25963aa84726630252eb5aca7cc6"></a>
<a id="astructbt__ots__obj__add__param_html"></a>
<a id="astructbt__ots__obj__add__param_html_a721734439b43e40324c3a548b5a4eb34"></a>
<a id="astructbt__ots__obj__add__param_html_afdbaf218850d4bf3f40f7a9e8d7b0595"></a>
<a id="astructbt__ots__obj__created__desc_html"></a>
<a id="astructbt__ots__obj__created__desc_html_a50b2b2ae0b87690d1995187bae577e8c"></a>
<a id="astructbt__ots__obj__created__desc_html_adb52cffa29c08ee1131415faeaf13cda"></a>
<a id="astructbt__ots__obj__created__desc_html_af69db0a3c56c6d3085f20fbb405b436e"></a>
<a id="astructbt__ots__obj__metadata_html"></a>
<a id="astructbt__ots__obj__metadata_html_a63b154d9a40a170acc8a632cbb00602f"></a>
<a id="astructbt__ots__obj__metadata_html_a6a564d53607261992bb4d3fc9035c23c"></a>
<a id="astructbt__ots__obj__metadata_html_a91f8183d1eac783b277fe6b040378b2f"></a>
<a id="astructbt__ots__obj__metadata_html_aa4ffe00ede40ff23ab5788c82ec2ac38"></a>
<a id="astructbt__ots__obj__metadata_html_aa51fd3166fedebbe0d6c66cfbe9ba649"></a>
<a id="astructbt__ots__obj__metadata_html_aabaa62092e281f3278b69297eedcc7d6"></a>
<a id="astructbt__ots__obj__metadata_html_aee93aef1932e9c8b4cb0c8055e5cb055"></a>
<a id="astructbt__ots__obj__metadata_html_afd451a3b531250db1d45eb6ddb4d9b0f"></a>
<a id="astructbt__ots__obj__size_html"></a>
<a id="astructbt__ots__obj__size_html_a217290f0fae68a54046eef50ac2a3773"></a>
<a id="astructbt__ots__obj__size_html_a86a5675532eae69d40b3305436e81cfb"></a>
<a id="astructbt__ots__obj__type_html"></a>
<a id="astructbt__ots__obj__type_html_a89a8dbe566579422df503dd577ea8d42"></a>
<a id="astructbt__ots__obj__type_html_ae39b7a368314d1a771cf3573d2077095"></a>
<a id="astructbt__ots__obj__type_html_aedf0e5d45f6f4912a8eeae077eda17be"></a>
<a id="astructbt__ots_html"></a>
<a id="astructbt__uuid__128_html"></a>
<a id="astructbt__uuid__16_html"></a>
<a id="astructbt__uuid_html"></a>
<a id="asys_2byteorder_8h_html"></a>
<a id="asys_2byteorder_8h_html_aa6950654cc7fd67ab4f83235da59665a"></a>
<a id="asys_2crc_8h_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2020-2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_OTS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_OTS_H_


#include <stdbool.h>
#include <stdint.h>

#include <sys/types.h>

#include <zephyr/sys/byteorder.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/crc.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/bluetooth/gatt.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_OTS_OBJ_ID_SIZE 6

#define BT_OTS_OBJ_ID_MIN 0x000000000100ULL

#define BT_OTS_OBJ_ID_MAX 0xFFFFFFFFFFFFULL

#define OTS_OBJ_ID_DIR_LIST 0x000000000000ULL

#define BT_OTS_OBJ_ID_MASK BIT64_MASK(48)

#define BT_OTS_OBJ_ID_STR_LEN 15

struct bt_ots_obj_type {
        union {
                /* Used to indicate UUID type */
                struct bt_uuid uuid;

                /* 16-bit UUID value */
                struct bt_uuid_16 uuid_16;

                /* 128-bit UUID value */
                struct bt_uuid_128 uuid_128;
        };
};

enum {
        BT_OTS_OBJ_PROP_DELETE    = 0,

        BT_OTS_OBJ_PROP_EXECUTE   = 1,

        BT_OTS_OBJ_PROP_READ      = 2,

        BT_OTS_OBJ_PROP_WRITE     = 3,

        BT_OTS_OBJ_PROP_APPEND    = 4,

        BT_OTS_OBJ_PROP_TRUNCATE  = 5,

        BT_OTS_OBJ_PROP_PATCH     = 6,

        BT_OTS_OBJ_PROP_MARKED    = 7,
};

#define BT_OTS_OBJ_SET_PROP_DELETE(prop) \
        WRITE_BIT(prop, BT_OTS_OBJ_PROP_DELETE, 1)

#define BT_OTS_OBJ_SET_PROP_EXECUTE(prop) \
        WRITE_BIT(prop, BT_OTS_OBJ_PROP_EXECUTE, 1)

#define BT_OTS_OBJ_SET_PROP_READ(prop) \
        WRITE_BIT(prop, BT_OTS_OBJ_PROP_READ, 1)

#define BT_OTS_OBJ_SET_PROP_WRITE(prop) \
        WRITE_BIT(prop, BT_OTS_OBJ_PROP_WRITE, 1)

#define BT_OTS_OBJ_SET_PROP_APPEND(prop) \
        WRITE_BIT(prop, BT_OTS_OBJ_PROP_APPEND, 1)

#define BT_OTS_OBJ_SET_PROP_TRUNCATE(prop) \
        WRITE_BIT(prop, BT_OTS_OBJ_PROP_TRUNCATE, 1)

#define BT_OTS_OBJ_SET_PROP_PATCH(prop) \
        WRITE_BIT(prop, BT_OTS_OBJ_PROP_PATCH, 1)

#define BT_OTS_OBJ_SET_PROP_MARKED(prop) \
        WRITE_BIT(prop, BT_OTS_OBJ_PROP_MARKED, 1)

#define BT_OTS_OBJ_GET_PROP_DELETE(prop) \
        ((prop) & BIT(BT_OTS_OBJ_PROP_DELETE))

#define BT_OTS_OBJ_GET_PROP_EXECUTE(prop) \
        ((prop) & BIT(BT_OTS_OBJ_PROP_EXECUTE))

#define BT_OTS_OBJ_GET_PROP_READ(prop) \
        ((prop) & BIT(BT_OTS_OBJ_PROP_READ))

#define BT_OTS_OBJ_GET_PROP_WRITE(prop) \
        ((prop) & BIT(BT_OTS_OBJ_PROP_WRITE))

#define BT_OTS_OBJ_GET_PROP_APPEND(prop) \
        ((prop) & BIT(BT_OTS_OBJ_PROP_APPEND))

#define BT_OTS_OBJ_GET_PROP_TRUNCATE(prop) \
        ((prop) & BIT(BT_OTS_OBJ_PROP_TRUNCATE))

#define BT_OTS_OBJ_GET_PROP_PATCH(prop) \
        ((prop) & BIT(BT_OTS_OBJ_PROP_PATCH))

#define BT_OTS_OBJ_GET_PROP_MARKED(prop) \
        ((prop) & BIT(BT_OTS_OBJ_PROP_MARKED))

struct bt_ots_obj_size {
        uint32_t cur;

        uint32_t alloc;
} __packed;

enum {
        BT_OTS_OACP_FEAT_CREATE     = 0,

        BT_OTS_OACP_FEAT_DELETE     = 1,

        BT_OTS_OACP_FEAT_CHECKSUM   = 2,

        BT_OTS_OACP_FEAT_EXECUTE    = 3,

        BT_OTS_OACP_FEAT_READ       = 4,

        BT_OTS_OACP_FEAT_WRITE      = 5,

        BT_OTS_OACP_FEAT_APPEND     = 6,

        BT_OTS_OACP_FEAT_TRUNCATE   = 7,

        BT_OTS_OACP_FEAT_PATCH      = 8,

        BT_OTS_OACP_FEAT_ABORT      = 9,
};

/*
 * @enum bt_ots_oacp_write_op_mode
 * @brief Mode Parameter for OACP Write Op Code.
 */
enum bt_ots_oacp_write_op_mode {
        BT_OTS_OACP_WRITE_OP_MODE_NONE = 0,
        BT_OTS_OACP_WRITE_OP_MODE_TRUNCATE = BIT(1),
};

#define BT_OTS_OACP_SET_FEAT_CREATE(feat) \
        WRITE_BIT(feat, BT_OTS_OACP_FEAT_CREATE, 1)

#define BT_OTS_OACP_SET_FEAT_DELETE(feat) \
        WRITE_BIT(feat, BT_OTS_OACP_FEAT_DELETE, 1)

#define BT_OTS_OACP_SET_FEAT_CHECKSUM(feat) \
        WRITE_BIT(feat, BT_OTS_OACP_FEAT_CHECKSUM, 1)

#define BT_OTS_OACP_SET_FEAT_EXECUTE(feat) \
        WRITE_BIT(feat, BT_OTS_OACP_FEAT_EXECUTE, 1)

#define BT_OTS_OACP_SET_FEAT_READ(feat) \
        WRITE_BIT(feat, BT_OTS_OACP_FEAT_READ, 1)

#define BT_OTS_OACP_SET_FEAT_WRITE(feat) \
        WRITE_BIT(feat, BT_OTS_OACP_FEAT_WRITE, 1)

#define BT_OTS_OACP_SET_FEAT_APPEND(feat) \
        WRITE_BIT(feat, BT_OTS_OACP_FEAT_APPEND, 1)

#define BT_OTS_OACP_SET_FEAT_TRUNCATE(feat) \
        WRITE_BIT(feat, BT_OTS_OACP_FEAT_TRUNCATE, 1)

#define BT_OTS_OACP_SET_FEAT_PATCH(feat) \
        WRITE_BIT(feat, BT_OTS_OACP_FEAT_PATCH, 1)

#define BT_OTS_OACP_SET_FEAT_ABORT(feat) \
        WRITE_BIT(feat, BT_OTS_OACP_FEAT_ABORT, 1)

#define BT_OTS_OACP_GET_FEAT_CREATE(feat) \
        ((feat) & BIT(BT_OTS_OACP_FEAT_CREATE))

#define BT_OTS_OACP_GET_FEAT_DELETE(feat) \
        ((feat) & BIT(BT_OTS_OACP_FEAT_DELETE))

#define BT_OTS_OACP_GET_FEAT_CHECKSUM(feat) \
        ((feat) & BIT(BT_OTS_OACP_FEAT_CHECKSUM))

#define BT_OTS_OACP_GET_FEAT_EXECUTE(feat) \
        ((feat) & BIT(BT_OTS_OACP_FEAT_EXECUTE))

#define BT_OTS_OACP_GET_FEAT_READ(feat) \
        ((feat) & BIT(BT_OTS_OACP_FEAT_READ))

#define BT_OTS_OACP_GET_FEAT_WRITE(feat) \
        ((feat) & BIT(BT_OTS_OACP_FEAT_WRITE))

#define BT_OTS_OACP_GET_FEAT_APPEND(feat) \
        ((feat) & BIT(BT_OTS_OACP_FEAT_APPEND))

#define BT_OTS_OACP_GET_FEAT_TRUNCATE(feat) \
        ((feat) & BIT(BT_OTS_OACP_FEAT_TRUNCATE))

#define BT_OTS_OACP_GET_FEAT_PATCH(feat) \
        ((feat) & BIT(BT_OTS_OACP_FEAT_PATCH))

#define BT_OTS_OACP_GET_FEAT_ABORT(feat) \
        ((feat) & BIT(BT_OTS_OACP_FEAT_ABORT))

enum {
        BT_OTS_OLCP_FEAT_GO_TO      = 0,

        BT_OTS_OLCP_FEAT_ORDER      = 1,

        BT_OTS_OLCP_FEAT_NUM_REQ    = 2,

        BT_OTS_OLCP_FEAT_CLEAR      = 3,
};

#define BT_OTS_OLCP_SET_FEAT_GO_TO(feat) \
        WRITE_BIT(feat, BT_OTS_OLCP_FEAT_GO_TO, 1)

#define BT_OTS_OLCP_SET_FEAT_ORDER(feat) \
        WRITE_BIT(feat, BT_OTS_OLCP_FEAT_ORDER, 1)

#define BT_OTS_OLCP_SET_FEAT_NUM_REQ(feat) \
        WRITE_BIT(feat, BT_OTS_OLCP_FEAT_NUM_REQ, 1)

#define BT_OTS_OLCP_SET_FEAT_CLEAR(feat) \
        WRITE_BIT(feat, BT_OTS_OLCP_FEAT_CLEAR, 1)

#define BT_OTS_OLCP_GET_FEAT_GO_TO(feat) \
        ((feat) & BIT(BT_OTS_OLCP_FEAT_GO_TO))

#define BT_OTS_OLCP_GET_FEAT_ORDER(feat) \
        ((feat) & BIT(BT_OTS_OLCP_FEAT_ORDER))

#define BT_OTS_OLCP_GET_FEAT_NUM_REQ(feat) \
        ((feat) & BIT(BT_OTS_OLCP_FEAT_NUM_REQ))

#define BT_OTS_OLCP_GET_FEAT_CLEAR(feat) \
        ((feat) & BIT(BT_OTS_OLCP_FEAT_CLEAR))

struct bt_ots_feat {
        /* OACP Features */
        uint32_t oacp;

        /* OLCP Features */
        uint32_t olcp;
} __packed;

enum {
        BT_OTS_METADATA_REQ_NAME                        = BIT(0),
        BT_OTS_METADATA_REQ_TYPE                        = BIT(1),
        BT_OTS_METADATA_REQ_SIZE                        = BIT(2),
        BT_OTS_METADATA_REQ_CREATED                     = BIT(3),
        BT_OTS_METADATA_REQ_MODIFIED                    = BIT(4),
        BT_OTS_METADATA_REQ_ID                          = BIT(5),
        BT_OTS_METADATA_REQ_PROPS                       = BIT(6),
        BT_OTS_METADATA_REQ_ALL                         = 0x7F,
};

struct bt_ots_date_time {
        uint16_t year;
        uint8_t month;
        uint8_t day;
        uint8_t hours;
        uint8_t minutes;
        uint8_t seconds;
};
#define BT_OTS_DATE_TIME_FIELD_SIZE 7

struct bt_ots_obj_metadata {

#if defined(CONFIG_BT_OTS) || defined(__DOXYGEN__)
        char                           *name;
#endif /* CONFIG_BT_OTS */

#if defined(CONFIG_BT_OTS_CLIENT) || defined(__DOXYGEN__)
        /* TODO: Unify client/server name */
        char                           name_c[CONFIG_BT_OTS_OBJ_MAX_NAME_LEN + 1];
#endif /* CONFIG_BT_OTS_CLIENT */

        struct bt_ots_obj_type         type;

        struct bt_ots_obj_size         size;

#if defined(CONFIG_BT_OTS_CLIENT) || defined(__DOXYGEN__)
        struct bt_ots_date_time        first_created;

        struct bt_ots_date_time        modified;

        uint64_t                       id;
#endif /* CONFIG_BT_OTS_CLIENT */

        uint32_t                       props;
};

struct bt_ots;

struct bt_ots_obj_add_param {
        uint32_t size;

        struct bt_ots_obj_type type;
};

struct bt_ots_obj_created_desc {
        char *name;

        struct bt_ots_obj_size size;

        uint32_t props;
};

struct bt_ots_cb {
        int (*obj_created)(struct bt_ots *ots, struct bt_conn *conn, uint64_t id,
                           const struct bt_ots_obj_add_param *add_param,
                           struct bt_ots_obj_created_desc *created_desc);

        int (*obj_deleted)(struct bt_ots *ots, struct bt_conn *conn,
                           uint64_t id);

        void (*obj_selected)(struct bt_ots *ots, struct bt_conn *conn,
                             uint64_t id);

        ssize_t (*obj_read)(struct bt_ots *ots, struct bt_conn *conn,
                           uint64_t id, void **data, size_t len,
                           off_t offset);

        ssize_t (*obj_write)(struct bt_ots *ots, struct bt_conn *conn, uint64_t id,
                             const void *data, size_t len, off_t offset,
                             size_t rem);

        void (*obj_name_written)(struct bt_ots *ots, struct bt_conn *conn,
                                 uint64_t id, const char *cur_name, const char *new_name);

        int (*obj_cal_checksum)(struct bt_ots *ots, struct bt_conn *conn, uint64_t id,
                                off_t offset, size_t len, void **data);
};

struct bt_ots_init_param {
        /* OTS features */
        struct bt_ots_feat features;

        /* Callbacks */
        struct bt_ots_cb *cb;
};

int bt_ots_obj_add(struct bt_ots *ots, const struct bt_ots_obj_add_param *param);

int bt_ots_obj_delete(struct bt_ots *ots, uint64_t id);

void *bt_ots_svc_decl_get(struct bt_ots *ots);

int bt_ots_init(struct bt_ots *ots, struct bt_ots_init_param *ots_init);

struct bt_ots *bt_ots_free_instance_get(void);

#define BT_OTS_STOP                       0
#define BT_OTS_CONTINUE                   1

/* TODO: Merge server and client instance as opaque type */
struct bt_ots_client {
        uint16_t start_handle;
        uint16_t end_handle;
        uint16_t feature_handle;
        uint16_t obj_name_handle;
        uint16_t obj_type_handle;
        uint16_t obj_size_handle;
        uint16_t obj_properties_handle;
        uint16_t obj_created_handle;
        uint16_t obj_modified_handle;
        uint16_t obj_id_handle;
        uint16_t oacp_handle;
        uint16_t olcp_handle;

        struct bt_gatt_subscribe_params oacp_sub_params;
        struct bt_gatt_discover_params oacp_sub_disc_params;
        struct bt_gatt_subscribe_params olcp_sub_params;
        struct bt_gatt_discover_params olcp_sub_disc_params;

        struct bt_gatt_write_params write_params;
        struct bt_gatt_read_params read_proc;
        struct bt_ots_client_cb *cb;

        struct bt_ots_feat features;

        struct bt_ots_obj_metadata cur_object;
};

struct bt_ots_client_cb {
        void (*obj_selected)(struct bt_ots_client *ots_inst,
                             struct bt_conn *conn, int err);


        int (*obj_data_read)(struct bt_ots_client *ots_inst,
                             struct bt_conn *conn, uint32_t offset,
                             uint32_t len, uint8_t *data_p, bool is_complete);

        void (*obj_metadata_read)(struct bt_ots_client *ots_inst,
                                  struct bt_conn *conn, int err,
                                  uint8_t metadata_read);

        void (*obj_data_written)(struct bt_ots_client *ots_inst,
                                 struct bt_conn *conn, size_t len);

        void (*obj_checksum_calculated)(struct bt_ots_client *ots_inst, struct bt_conn *conn,
                                        int err, uint32_t checksum);
};

int bt_ots_client_register(struct bt_ots_client *ots_inst);

int bt_ots_client_unregister(uint8_t index);

uint8_t bt_ots_client_indicate_handler(struct bt_conn *conn,
                                       struct bt_gatt_subscribe_params *params,
                                       const void *data, uint16_t length);

int bt_ots_client_read_feature(struct bt_ots_client *otc_inst,
                               struct bt_conn *conn);

int bt_ots_client_select_id(struct bt_ots_client *otc_inst,
                            struct bt_conn *conn,
                            uint64_t obj_id);

int bt_ots_client_select_first(struct bt_ots_client *otc_inst,
                               struct bt_conn *conn);

int bt_ots_client_select_last(struct bt_ots_client *otc_inst,
                              struct bt_conn *conn);

int bt_ots_client_select_next(struct bt_ots_client *otc_inst,
                              struct bt_conn *conn);

int bt_ots_client_select_prev(struct bt_ots_client *otc_inst,
                              struct bt_conn *conn);

int bt_ots_client_read_object_metadata(struct bt_ots_client *otc_inst,
                                       struct bt_conn *conn,
                                       uint8_t metadata);

int bt_ots_client_read_object_data(struct bt_ots_client *otc_inst,
                                   struct bt_conn *conn);

int bt_ots_client_write_object_data(struct bt_ots_client *otc_inst, struct bt_conn *conn,
                                    const void *buf, size_t len, off_t offset,
                                    enum bt_ots_oacp_write_op_mode mode);

int bt_ots_client_get_object_checksum(struct bt_ots_client *otc_inst, struct bt_conn *conn,
                                      off_t offset, size_t len);

typedef int (*bt_ots_client_dirlisting_cb)(struct bt_ots_obj_metadata *meta);

int bt_ots_client_decode_dirlisting(uint8_t *data, uint16_t length,
                                    bt_ots_client_dirlisting_cb cb);

static inline int bt_ots_obj_id_to_str(uint64_t obj_id, char *str, size_t len)
{
        uint8_t id[6];

        sys_put_le48(obj_id, id);

        return snprintk(str, len, "0x%02X%02X%02X%02X%02X%02X",
                        id[5], id[4], id[3], id[2], id[1], id[0]);
}

void bt_ots_metadata_display(struct bt_ots_obj_metadata *metadata,
                             uint16_t count);

static inline uint32_t bt_ots_client_calc_checksum(const uint8_t *data, size_t len)
{
        return crc32_ieee(data, len);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_OTS_H_ */
```

## 21.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020-2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 59 行

用于指示通用唯一标识符（UUID）类型。

### 注释 3：原第 62 行

16 位 UUID 值。

### 注释 4：原第 65 行

128 位 UUID 值。

### 注释 5：原第 258 行

@enum bt_ots_oacp_write_op_mode
@brief 对象操作控制点（OACP）写操作码（Write Op Code）的模式参数。

### 注释 6：原第 480 行

对象操作控制点（OACP）的功能（Features）。

### 注释 7：原第 483 行

对象列表控制点（OLCP）的功能（Features）。

### 注释 8：原第 528 行

条件编译配置（Configuration）标记：`CONFIG_BT_OTS`。

### 注释 9：原第 531 行

待办（TODO）：统一客户端／服务器名称。

### 注释 10：原第 534 行

条件编译配置（Configuration）标记：`CONFIG_BT_OTS_CLIENT`。

### 注释 11：原第 551 行

条件编译配置（Configuration）标记：`CONFIG_BT_OTS_CLIENT`。

### 注释 12：原第 758 行

对象传输服务（OTS）的功能（Features）。

### 注释 13：原第 761 行

回调（Callbacks）

### 注释 14：原第 822 行

待办（TODO）：将服务器和客户端实例合并为不透明类型（opaque type）。

### 注释 15：原第 1178 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_OTS_H_`。

## 21.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ots_8h.html)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [sys/types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [zephyr/sys/byteorder.h](../byteorder_reference/P001_系统字节序头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/crc.h](../data_utilities/P004_CRC系统头文件.md)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h.html)
- [bt_ots_obj_type](../bluetooth_service_model_reference/P146_bt_ots_obj_type_结构体.md)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [uuid](../bluetooth_service_model_reference/P146_bt_ots_obj_type_结构体.md#a89a8dbe566579422df503dd577ea8d42)
- [bt_uuid_16](../bluetooth_connection_model_reference/P133_bt_uuid_16_结构体.md)
- [uuid_16](../bluetooth_service_model_reference/P146_bt_ots_obj_type_结构体.md#ae39b7a368314d1a771cf3573d2077095)
- [bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)
- [uuid_128](../bluetooth_service_model_reference/P146_bt_ots_obj_type_结构体.md#aedf0e5d45f6f4912a8eeae077eda17be)
- [BT_OTS_OBJ_PROP_DELETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10)
- [BT_OTS_OBJ_PROP_EXECUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad)
- [BT_OTS_OBJ_PROP_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102)
- [BT_OTS_OBJ_PROP_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2)
- [BT_OTS_OBJ_PROP_APPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775)
- [BT_OTS_OBJ_PROP_TRUNCATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446)
- [BT_OTS_OBJ_PROP_PATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed)
- [BT_OTS_OBJ_PROP_MARKED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3)
- [bt_ots_obj_size](../bluetooth_service_model_reference/P145_bt_ots_obj_size_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [cur](../bluetooth_service_model_reference/P145_bt_ots_obj_size_结构体.md#a217290f0fae68a54046eef50ac2a3773)
- [alloc](../bluetooth_service_model_reference/P145_bt_ots_obj_size_结构体.md#a86a5675532eae69d40b3305436e81cfb)
- [BT_OTS_OACP_FEAT_CREATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9)
- [BT_OTS_OACP_FEAT_DELETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee)
- [BT_OTS_OACP_FEAT_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f)
- [BT_OTS_OACP_FEAT_EXECUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c)
- [BT_OTS_OACP_FEAT_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465)
- [BT_OTS_OACP_FEAT_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab)
- [BT_OTS_OACP_FEAT_APPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b)
- [BT_OTS_OACP_FEAT_TRUNCATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225)
- [BT_OTS_OACP_FEAT_PATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf)
- [BT_OTS_OACP_FEAT_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440)
- [bt_ots_oacp_write_op_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gaebdd2b8a80948d1050d42fa3963cc863)
- [BT_OTS_OACP_WRITE_OP_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ggaebdd2b8a80948d1050d42fa3963cc863a1c2d68fccd8f252b54a11879a6dd53ab)
- [BT_OTS_OACP_WRITE_OP_MODE_TRUNCATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ggaebdd2b8a80948d1050d42fa3963cc863a91d201f7f01809e2af10e10008d4eb8a)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_OTS_OLCP_FEAT_GO_TO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713)
- [BT_OTS_OLCP_FEAT_ORDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d)
- [BT_OTS_OLCP_FEAT_NUM_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660)
- [BT_OTS_OLCP_FEAT_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af)
- [bt_ots_feat](../bluetooth_service_model_reference/P140_bt_ots_feat_结构体.md)
- [oacp](../bluetooth_service_model_reference/P140_bt_ots_feat_结构体.md#a714abba341b1f4a50edfa73dd5048f28)
- [olcp](../bluetooth_service_model_reference/P140_bt_ots_feat_结构体.md#a309b3e38a0f15c49c06a5ffeb873cef3)
- [BT_OTS_METADATA_REQ_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga9bbade1b48363f0f486968723afefb45ada06e9d807f7c197bd332c0e7ca21ffb)
- [BT_OTS_METADATA_REQ_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga9bbade1b48363f0f486968723afefb45aff8f3ce21a85b397b64b5d03a5fe8af9)
- [BT_OTS_METADATA_REQ_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga9bbade1b48363f0f486968723afefb45aca9770dfa7fbec3a6bc0bccb4e9e41e5)
- [BT_OTS_METADATA_REQ_CREATED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga9bbade1b48363f0f486968723afefb45ac47367e5e775fa6690ac5bc03e187095)
- [BT_OTS_METADATA_REQ_MODIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga9bbade1b48363f0f486968723afefb45a35a3d25b637ac80e658102f27aeb7f5e)
- [BT_OTS_METADATA_REQ_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga9bbade1b48363f0f486968723afefb45a44cb8e7804c86fce7c2eab3f3f0743c2)
- [BT_OTS_METADATA_REQ_PROPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga9bbade1b48363f0f486968723afefb45af7c08a3c53273ac6452f607a23826e2f)
- [BT_OTS_METADATA_REQ_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gga9bbade1b48363f0f486968723afefb45a04e4ab3e722a23370a63288c3eba8cdf)
- [bt_ots_date_time](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [year](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md#af348ad2613ba309de6a93d357bcce3bc)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [month](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md#ac3959eac8188df6114d70aed1ccbf3f4)
- [day](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md#a09ca928752dc844e89de3957d1baae3c)
- [hours](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md#ae139a310b4d17078f52bfbe7707e185a)
- [minutes](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md#acc118b311bfdcb3c2f7801121831fcd6)
- [seconds](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md#a4eb6899dbce61478b97025958c62f586)
- [bt_ots_obj_metadata](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md)
- [name](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#a63b154d9a40a170acc8a632cbb00602f)
- [name_c](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#aabaa62092e281f3278b69297eedcc7d6)
- [type](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#aee93aef1932e9c8b4cb0c8055e5cb055)
- [size](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#afd451a3b531250db1d45eb6ddb4d9b0f)
- [first_created](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#a6a564d53607261992bb4d3fc9035c23c)
- [modified](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#a91f8183d1eac783b277fe6b040378b2f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [id](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#aa51fd3166fedebbe0d6c66cfbe9ba649)
- [props](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#aa4ffe00ede40ff23ab5788c82ec2ac38)
- [bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)
- [bt_ots_obj_add_param](../bluetooth_service_model_reference/P142_bt_ots_obj_add_param_结构体.md)
- [size](../bluetooth_service_model_reference/P142_bt_ots_obj_add_param_结构体.md#a721734439b43e40324c3a548b5a4eb34)
- [type](../bluetooth_service_model_reference/P142_bt_ots_obj_add_param_结构体.md#afdbaf218850d4bf3f40f7a9e8d7b0595)
- [bt_ots_obj_created_desc](../bluetooth_service_model_reference/P143_bt_ots_obj_created_desc_结构体.md)
- [name](../bluetooth_service_model_reference/P143_bt_ots_obj_created_desc_结构体.md#af69db0a3c56c6d3085f20fbb405b436e)
- [size](../bluetooth_service_model_reference/P143_bt_ots_obj_created_desc_结构体.md#adb52cffa29c08ee1131415faeaf13cda)
- [props](../bluetooth_service_model_reference/P143_bt_ots_obj_created_desc_结构体.md#a50b2b2ae0b87690d1995187bae577e8c)
- [bt_ots_cb](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md)
- [obj_created](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#a0c95b2bc382474be3c1ae849936a8206)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [obj_deleted](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#a2fd78b43691e83c1faa86c1748ab2359)
- [obj_selected](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#ae8602aef0fd001d6768dc20c8873742d)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [obj_read](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#ab67ca0032b8b2fd9b8fbe6c117c186dd)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [obj_write](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#ae31da190c9c6bee086e4d7f8fcd6fbb5)
- [obj_name_written](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#a600fa13a97f39e3bd53c524039e2733c)
- [obj_cal_checksum](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#a2ef2245c017015b81c0f276f00fd6f79)
- [bt_ots_init_param](../bluetooth_service_model_reference/P141_bt_ots_init_param_结构体.md)
- [features](../bluetooth_service_model_reference/P141_bt_ots_init_param_结构体.md#a563c25963aa84726630252eb5aca7cc6)
- [cb](../bluetooth_service_model_reference/P141_bt_ots_init_param_结构体.md#a22887673f03decf840470cb555f2b7f0)
- [bt_ots_obj_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gabf59844edd0ffd434acd94bad9a7b52c)
- [bt_ots_obj_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga872ba5a73fa4e617b9d48e7361af74c7)
- [bt_ots_svc_decl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gabe637ba9febb514f7346d71696b70c73)
- [bt_ots_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga1c9dcb35c8f07432fd9249a34e597819)
- [bt_ots_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gafc71de8fd65212045fa26b2a81e3876d)
- [bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)
- [start_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a39818a4d776056212e82c4ba0626d0f1)
- [end_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a99727a6d064d79c3078a04b1d6d046db)
- [feature_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a65608146d1a3e141635a015eb5092ab1)
- [obj_name_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#ae902c29051540141852869dd94edf7e0)
- [obj_type_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#ae2eebd727fd908ef2b2074c9c0b2ab4f)
- [obj_size_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a83c5d653692dc3d7dbcfd5c8e2361f96)
- [obj_properties_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#aabd4a625a341b4f7bdcdcff03e7ae76f)
- [obj_created_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#aff756cfa5f9431ed288563a95877cb53)
- [obj_modified_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a83cf53f6f7737620ea39dccbebe26dd4)
- [obj_id_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a6ff62fb7570269358888c9ab865a5ec6)
- [oacp_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#ad56aaee2630d75a1bb5faf0f56486c0a)
- [olcp_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#aa98ae5a468c46f1ffbfd08a6e82f420d)
- [bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)
- [oacp_sub_params](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a98a75a8ed52a2b97be1ea273a21b8775)
- [bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)
- [oacp_sub_disc_params](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a8913d240d90b77ea72612ddbf816f528)
- [olcp_sub_params](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a787b4851389e5da47a93969db6b3edcf)
- [olcp_sub_disc_params](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#acbee05e7b1cd5c325a6982c6b32a732d)
- [bt_gatt_write_params](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md)
- [write_params](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a0e6a0d97a1b8edc7a282aec12d95b0dc)
- [bt_gatt_read_params](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md)
- [read_proc](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a87d273e283941a3b9f1402e2b514134b)
- [bt_ots_client_cb](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md)
- [cb](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a3aded7f58deb7f13c1c5adaa073f45f8)
- [features](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a8a6d138d506a5e2732f4c51971533ce9)
- [cur_object](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#ac0fac55db40bf66aff358ce906fc8172)
- [obj_selected](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md#ace98d27220e394b0990a8274bbd43026)
- [obj_data_read](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md#ae95f3b85758c04279ada801c001086bc)
- [obj_metadata_read](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md#ab6c03b98fc5c68aa8c76ada23b7dff1c)
- [obj_data_written](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md#a2baaf13c8de4ade034f2b58896225e0d)
- [obj_checksum_calculated](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md#ad5537da9ced98a15620a7fb1e77b0218)
- [bt_ots_client_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gadefd2ccb46a686a4aa2999da5851184b)
- [bt_ots_client_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gabba031c38c7503c1f434a761d9f65df4)
- [bt_ots_client_indicate_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gac270137f15596777287f68b3d6a6a11c)
- [bt_ots_client_read_feature](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gaf11589afc37efe18dcac122835a4c95d)
- [bt_ots_client_select_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga5f2d0b0e4d54e00a1a96157fcfaf172b)
- [bt_ots_client_select_first](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga70cae251cf40a5c3c8d2a8c7e1f1e181)
- [bt_ots_client_select_last](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga89fc03d68725de0b5f306c899452b1a8)
- [bt_ots_client_select_next](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga81997ab2f1718c6856e676eb9b3f72bb)
- [bt_ots_client_select_prev](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gac84ed7f16fa86d87531d04e2957568f9)
- [bt_ots_client_read_object_metadata](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga936f392c880c9d1a73f2bd632e5b63e0)
- [bt_ots_client_read_object_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga8ad1c53325c1b77271307507317a5965)
- [bt_ots_client_write_object_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga9444b064c616718dae1577b21540fb9a)
- [bt_ots_client_get_object_checksum](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga9cfd057d39ce3fe9bbecaa103ec44f77)
- [bt_ots_client_dirlisting_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gaa1a9db6e8aa6ee716e4fdd2e34157f46)
- [bt_ots_client_decode_dirlisting](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gabe485816a2e536758a7ce85c593ea486)
- [bt_ots_obj_id_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gac9be2770fc7f2932ea2e31392d956f0a)
- [sys_put_le48](../byteorder_reference/P001_系统字节序头文件参考.md#aa6950654cc7fd67ab4f83235da59665a)
- [snprintk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a0b0af71688f7e9170103d771d4e1eab2)
- [bt_ots_metadata_display](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga8324cc14e8812648cc3663144591af89)
- [bt_ots_client_calc_checksum](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga63e4408702fee1be0501a715cd32c957)
- [crc32_ieee](../data_utilities/P003_CRC计算接口.md#gafc24e79ed7f978f5bb813091ef318982)
- [uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h.html)
- [types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [bt_ots_cb::obj_created](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#a0c95b2bc382474be3c1ae849936a8206)
- [bt_ots_cb::obj_cal_checksum](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#a2ef2245c017015b81c0f276f00fd6f79)
- [bt_ots_cb::obj_deleted](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#a2fd78b43691e83c1faa86c1748ab2359)
- [bt_ots_cb::obj_name_written](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#a600fa13a97f39e3bd53c524039e2733c)
- [bt_ots_cb::obj_read](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#ab67ca0032b8b2fd9b8fbe6c117c186dd)
- [bt_ots_cb::obj_write](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#ae31da190c9c6bee086e4d7f8fcd6fbb5)
- [bt_ots_cb::obj_selected](../bluetooth_service_model_reference/P136_bt_ots_cb_结构体.md#ae8602aef0fd001d6768dc20c8873742d)
- [bt_ots_client_cb::obj_data_written](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md#a2baaf13c8de4ade034f2b58896225e0d)
- [bt_ots_client_cb::obj_metadata_read](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md#ab6c03b98fc5c68aa8c76ada23b7dff1c)
- [bt_ots_client_cb::obj_selected](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md#ace98d27220e394b0990a8274bbd43026)
- [bt_ots_client_cb::obj_checksum_calculated](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md#ad5537da9ced98a15620a7fb1e77b0218)
- [bt_ots_client_cb::obj_data_read](../bluetooth_service_model_reference/P138_bt_ots_client_cb_结构体.md#ae95f3b85758c04279ada801c001086bc)
- [bt_ots_client::write_params](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a0e6a0d97a1b8edc7a282aec12d95b0dc)
- [bt_ots_client::start_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a39818a4d776056212e82c4ba0626d0f1)
- [bt_ots_client::cb](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a3aded7f58deb7f13c1c5adaa073f45f8)
- [bt_ots_client::feature_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a65608146d1a3e141635a015eb5092ab1)
- [bt_ots_client::obj_id_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a6ff62fb7570269358888c9ab865a5ec6)
- [bt_ots_client::olcp_sub_params](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a787b4851389e5da47a93969db6b3edcf)
- [bt_ots_client::obj_size_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a83c5d653692dc3d7dbcfd5c8e2361f96)
- [bt_ots_client::obj_modified_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a83cf53f6f7737620ea39dccbebe26dd4)
- [bt_ots_client::read_proc](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a87d273e283941a3b9f1402e2b514134b)
- [bt_ots_client::oacp_sub_disc_params](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a8913d240d90b77ea72612ddbf816f528)
- [bt_ots_client::features](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a8a6d138d506a5e2732f4c51971533ce9)
- [bt_ots_client::oacp_sub_params](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a98a75a8ed52a2b97be1ea273a21b8775)
- [bt_ots_client::end_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#a99727a6d064d79c3078a04b1d6d046db)
- [bt_ots_client::olcp_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#aa98ae5a468c46f1ffbfd08a6e82f420d)
- [bt_ots_client::obj_properties_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#aabd4a625a341b4f7bdcdcff03e7ae76f)
- [bt_ots_client::cur_object](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#ac0fac55db40bf66aff358ce906fc8172)
- [bt_ots_client::olcp_sub_disc_params](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#acbee05e7b1cd5c325a6982c6b32a732d)
- [bt_ots_client::oacp_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#ad56aaee2630d75a1bb5faf0f56486c0a)
- [bt_ots_client::obj_type_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#ae2eebd727fd908ef2b2074c9c0b2ab4f)
- [bt_ots_client::obj_name_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#ae902c29051540141852869dd94edf7e0)
- [bt_ots_client::obj_created_handle](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md#aff756cfa5f9431ed288563a95877cb53)
- [bt_ots_date_time::day](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md#a09ca928752dc844e89de3957d1baae3c)
- [bt_ots_date_time::seconds](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md#a4eb6899dbce61478b97025958c62f586)
- [bt_ots_date_time::month](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md#ac3959eac8188df6114d70aed1ccbf3f4)
- [bt_ots_date_time::minutes](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md#acc118b311bfdcb3c2f7801121831fcd6)
- [bt_ots_date_time::hours](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md#ae139a310b4d17078f52bfbe7707e185a)
- [bt_ots_date_time::year](../bluetooth_service_model_reference/P139_bt_ots_date_time_结构体.md#af348ad2613ba309de6a93d357bcce3bc)
- [bt_ots_feat::olcp](../bluetooth_service_model_reference/P140_bt_ots_feat_结构体.md#a309b3e38a0f15c49c06a5ffeb873cef3)
- [bt_ots_feat::oacp](../bluetooth_service_model_reference/P140_bt_ots_feat_结构体.md#a714abba341b1f4a50edfa73dd5048f28)
- [bt_ots_init_param::cb](../bluetooth_service_model_reference/P141_bt_ots_init_param_结构体.md#a22887673f03decf840470cb555f2b7f0)
- [bt_ots_init_param::features](../bluetooth_service_model_reference/P141_bt_ots_init_param_结构体.md#a563c25963aa84726630252eb5aca7cc6)
- [bt_ots_obj_add_param::size](../bluetooth_service_model_reference/P142_bt_ots_obj_add_param_结构体.md#a721734439b43e40324c3a548b5a4eb34)
- [bt_ots_obj_add_param::type](../bluetooth_service_model_reference/P142_bt_ots_obj_add_param_结构体.md#afdbaf218850d4bf3f40f7a9e8d7b0595)
- [bt_ots_obj_created_desc::props](../bluetooth_service_model_reference/P143_bt_ots_obj_created_desc_结构体.md#a50b2b2ae0b87690d1995187bae577e8c)
- [bt_ots_obj_created_desc::size](../bluetooth_service_model_reference/P143_bt_ots_obj_created_desc_结构体.md#adb52cffa29c08ee1131415faeaf13cda)
- [bt_ots_obj_created_desc::name](../bluetooth_service_model_reference/P143_bt_ots_obj_created_desc_结构体.md#af69db0a3c56c6d3085f20fbb405b436e)
- [bt_ots_obj_metadata::name](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#a63b154d9a40a170acc8a632cbb00602f)
- [bt_ots_obj_metadata::first_created](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#a6a564d53607261992bb4d3fc9035c23c)
- [bt_ots_obj_metadata::modified](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#a91f8183d1eac783b277fe6b040378b2f)
- [bt_ots_obj_metadata::props](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#aa4ffe00ede40ff23ab5788c82ec2ac38)
- [bt_ots_obj_metadata::id](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#aa51fd3166fedebbe0d6c66cfbe9ba649)
- [bt_ots_obj_metadata::name_c](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#aabaa62092e281f3278b69297eedcc7d6)
- [bt_ots_obj_metadata::type](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#aee93aef1932e9c8b4cb0c8055e5cb055)
- [bt_ots_obj_metadata::size](../bluetooth_service_model_reference/P144_bt_ots_obj_metadata_结构体.md#afd451a3b531250db1d45eb6ddb4d9b0f)
- [bt_ots_obj_size::cur](../bluetooth_service_model_reference/P145_bt_ots_obj_size_结构体.md#a217290f0fae68a54046eef50ac2a3773)
- [bt_ots_obj_size::alloc](../bluetooth_service_model_reference/P145_bt_ots_obj_size_结构体.md#a86a5675532eae69d40b3305436e81cfb)
- [bt_ots_obj_type::uuid](../bluetooth_service_model_reference/P146_bt_ots_obj_type_结构体.md#a89a8dbe566579422df503dd577ea8d42)
- [bt_ots_obj_type::uuid_16](../bluetooth_service_model_reference/P146_bt_ots_obj_type_结构体.md#ae39b7a368314d1a771cf3573d2077095)
- [bt_ots_obj_type::uuid_128](../bluetooth_service_model_reference/P146_bt_ots_obj_type_结构体.md#aedf0e5d45f6f4912a8eeae077eda17be)
- [byteorder.h](../byteorder_reference/P001_系统字节序头文件参考.md)
- [crc.h](../data_utilities/P004_CRC系统头文件.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P020_mchp_rstc_g1.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P022_renesas_rz_dma.h_源码浏览.md)
