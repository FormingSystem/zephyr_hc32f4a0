---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-17
title: zephyr__drivers__mspi.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr__drivers__mspi.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P017_zephyr__drivers__mspi.h_头文件参考.md)。

## 17.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00037"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00060"></a>
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
<a id="foldopen00086"></a>
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
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00107"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00125"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="foldopen00139"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="foldopen00159"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="foldopen00168"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
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
<a id="foldopen00200"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00210"></a>
<a id="foldopen00214"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="foldopen00221"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="foldopen00233"></a>
<a id="l00233"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="foldopen00243"></a>
<a id="l00243"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="foldopen00269"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="foldopen00279"></a>
<a id="l00279"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00299"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="foldopen00321"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="foldopen00337"></a>
<a id="l00337"></a>
<a id="l00339"></a>
<a id="l00343"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00349"></a>
<a id="l00355"></a>
<a id="foldopen00363"></a>
<a id="l00363"></a>
<a id="l00370"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="foldopen00382"></a>
<a id="l00382"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00390"></a>
<a id="l00392"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="foldopen00402"></a>
<a id="l00402"></a>
<a id="l00404"></a>
<a id="l00406"></a>
<a id="l00408"></a>
<a id="l00410"></a>
<a id="l00412"></a>
<a id="l00414"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00420"></a>
<a id="l00422"></a>
<a id="l00424"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00430"></a>
<a id="l00436"></a>
<a id="foldopen00440"></a>
<a id="l00440"></a>
<a id="l00442"></a>
<a id="l00444"></a>
<a id="l00446"></a>
<a id="l00448"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="foldopen00456"></a>
<a id="l00456"></a>
<a id="l00458"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="foldopen00466"></a>
<a id="l00466"></a>
<a id="l00468"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00482"></a>
<a id="l00487"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="foldopen00554"></a>
<a id="l00554"></a>
<a id="l00556"></a>
<a id="l00558"></a>
<a id="l00560"></a>
<a id="l00562"></a>
<a id="l00564"></a>
<a id="l00566"></a>
<a id="l00568"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00574"></a>
<a id="l00579"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00667"></a>
<a id="l00672"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="foldopen00745"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00767"></a>
<a id="l00772"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="l00823"></a>
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
<a id="l00852"></a>
<a id="l00853"></a>
<a id="l00854"></a>
<a id="l00855"></a>
<a id="l00856"></a>
<a id="l00857"></a>
<a id="l00858"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00870"></a>
<a id="l00875"></a>
<a id="foldopen00891"></a>
<a id="l00891"></a>
<a id="l00892"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="foldopen00923"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="foldopen00929"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="foldopen00935"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="foldopen00941"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="foldopen00947"></a>
<a id="l00947"></a>
<a id="l00948"></a>
<a id="l00949"></a>
<a id="foldopen00953"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00955"></a>
<a id="foldopen00959"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00961"></a>
<a id="l00963"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="adrivers_2mspi_2devicetree_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__mspi__callback__api_html_ga29421f748fdb89c823e1a48ff69cf0f4"></a>
<a id="agroup__mspi__callback__api_html_ga967f5fed63f08ac2d5a88625b030cd14"></a>
<a id="agroup__mspi__configure__api_html_ga46c2b98e99ecea045c1ecac4bdf3f087"></a>
<a id="agroup__mspi__configure__api_html_ga957b6ecd96c9f942f75bbe500898930d"></a>
<a id="agroup__mspi__configure__api_html_gaa25a7f97ab3437d4544832a0e7474f4a"></a>
<a id="agroup__mspi__configure__api_html_gaa3c1eae8b3000c9bafcc26f14a8beb8b"></a>
<a id="agroup__mspi__configure__api_html_gac025129882f814b59d5726c01f0138ce"></a>
<a id="agroup__mspi__configure__api_html_gacf287e08b6ce4898524884e8de22b806"></a>
<a id="agroup__mspi__configure__api_html_gaff82af1cfc99b9e78cec17ea27f79ab6"></a>
<a id="agroup__mspi__configure__api_html_ggaa25a7f97ab3437d4544832a0e7474f4aafae0ccedcd3b8f05e798037bf5414237"></a>
<a id="agroup__mspi__interface__backend_html_ga002c5d3cc7d6691130dee0f42b928894"></a>
<a id="agroup__mspi__interface__backend_html_ga092c8bb0879977a8cc8eea5d1662c34b"></a>
<a id="agroup__mspi__interface__backend_html_ga17b551f4d9f980fde8eabcaae3318617"></a>
<a id="agroup__mspi__interface__backend_html_ga2ff9209634fb241e2f7323e749df612e"></a>
<a id="agroup__mspi__interface__backend_html_ga407713e07f23756564814402342c9c97"></a>
<a id="agroup__mspi__interface__backend_html_ga7e3bae501067b045e9ed8d0efbe6e61d"></a>
<a id="agroup__mspi__interface__backend_html_gad6d65ef0d523f22592ff17c04698f663"></a>
<a id="agroup__mspi__interface__backend_html_gadd66b118b76a4ee7ef252afc6b830bfa"></a>
<a id="agroup__mspi__interface_html_ga116259bbb1d12a10c2ba9e6051f2f000"></a>
<a id="agroup__mspi__interface_html_ga20e348d7a9f1f9b32078a3bf6c4e82b9"></a>
<a id="agroup__mspi__interface_html_ga283275f86fe186f4b5e30110ae0d506b"></a>
<a id="agroup__mspi__interface_html_ga3625cde1379e66cb66a8cb3803ab2e44"></a>
<a id="agroup__mspi__interface_html_ga3f211cd81e05cb9ee073a2722f6b22d8"></a>
<a id="agroup__mspi__interface_html_ga498f10591acf5dc7ec88e0aa98e537d6"></a>
<a id="agroup__mspi__interface_html_ga4cd05950729893e08ef0d4a12e2242d5"></a>
<a id="agroup__mspi__interface_html_ga632af162124ca2959a21ca3759e1cc9e"></a>
<a id="agroup__mspi__interface_html_ga704e4d3759d3261b4468e9d9900e578c"></a>
<a id="agroup__mspi__interface_html_ga71c447d059acf7a8055c380243f3a647"></a>
<a id="agroup__mspi__interface_html_ga904dfc1c800fb9832f7c6200f767f9a5"></a>
<a id="agroup__mspi__interface_html_gaa2131d9846bbfd74488a6ae1c2003e68"></a>
<a id="agroup__mspi__interface_html_gab33e9840b0937c944f4e1a2525534cb1"></a>
<a id="agroup__mspi__interface_html_gac127ef78c7b66c7eebe03782abf08c40"></a>
<a id="agroup__mspi__interface_html_gga116259bbb1d12a10c2ba9e6051f2f000a5a7235fe9c633206906d76d329f623a8"></a>
<a id="agroup__mspi__interface_html_gga116259bbb1d12a10c2ba9e6051f2f000abea5c6920a3e81fe332c2a76e4d838a1"></a>
<a id="agroup__mspi__interface_html_gga20e348d7a9f1f9b32078a3bf6c4e82b9a13a3f16c4273ca6f28671663d0ecf33c"></a>
<a id="agroup__mspi__interface_html_gga20e348d7a9f1f9b32078a3bf6c4e82b9ac05ddc8ca44f1c70d3c3748e21fe80d3"></a>
<a id="agroup__mspi__interface_html_gga283275f86fe186f4b5e30110ae0d506ba375e0b870800e0982b3715417e109a22"></a>
<a id="agroup__mspi__interface_html_gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae"></a>
<a id="agroup__mspi__interface_html_gga3625cde1379e66cb66a8cb3803ab2e44a08e9349361779ce246bb7da6a1f3012d"></a>
<a id="agroup__mspi__interface_html_gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345"></a>
<a id="agroup__mspi__interface_html_gga3f211cd81e05cb9ee073a2722f6b22d8a11af11e286399c7e2f1fbcadca44ea83"></a>
<a id="agroup__mspi__interface_html_gga3f211cd81e05cb9ee073a2722f6b22d8a6a862f1d9931725be7789bd982d2937a"></a>
<a id="agroup__mspi__interface_html_gga498f10591acf5dc7ec88e0aa98e537d6a044160eb569add203f06d963f57d3541"></a>
<a id="agroup__mspi__interface_html_gga498f10591acf5dc7ec88e0aa98e537d6a213d4457305ab45d31b9c06ec85d2b8a"></a>
<a id="agroup__mspi__interface_html_gga4cd05950729893e08ef0d4a12e2242d5a325aa40170de5621e89aa2def557f85a"></a>
<a id="agroup__mspi__interface_html_gga4cd05950729893e08ef0d4a12e2242d5a9c538a902c3e5fa1086c0f0fcee4b7e6"></a>
<a id="agroup__mspi__interface_html_gga4cd05950729893e08ef0d4a12e2242d5ad47099019f15f97d83bc6435e5e76a61"></a>
<a id="agroup__mspi__interface_html_gga4cd05950729893e08ef0d4a12e2242d5aeeaf87802ecc90ada4c39f65fc0e8af0"></a>
<a id="agroup__mspi__interface_html_gga4cd05950729893e08ef0d4a12e2242d5afb1c2030d871cbbaa4341df7989a5a64"></a>
<a id="agroup__mspi__interface_html_gga632af162124ca2959a21ca3759e1cc9ea3004e6ae8226294b669f2207e928f928"></a>
<a id="agroup__mspi__interface_html_gga632af162124ca2959a21ca3759e1cc9ea31222dc35adf9bed70571b9b640aca97"></a>
<a id="agroup__mspi__interface_html_gga632af162124ca2959a21ca3759e1cc9ea66753cdf13762a1dd995638ff71544e0"></a>
<a id="agroup__mspi__interface_html_gga704e4d3759d3261b4468e9d9900e578ca415e431b25ac4a12f35b139ccb77ba48"></a>
<a id="agroup__mspi__interface_html_gga704e4d3759d3261b4468e9d9900e578ca8c93d56778ea1cbf901db1a4b9fee870"></a>
<a id="agroup__mspi__interface_html_gga704e4d3759d3261b4468e9d9900e578cabbde8c1ad9a5a8a9a3ca4ce33e2c0705"></a>
<a id="agroup__mspi__interface_html_gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647a0d7032e045c80ca266e98f8c6684af65"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647a0e954604ea419f6a4fdea59e620bdcd9"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647a13385127a309507ff01559122e03623a"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647a135b081210bd5aabf5b610fe90212809"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647a1a2e21a3cbf0ee42977cc8a43efd3fac"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647a4a476e51f0d3613aab1bc9c1b335bab2"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647a4aba5c75b43e1a87c66e940069b5b27f"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647a51f46405fe8923a8b0c39bc2aad1ba0b"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647a56ceb1ba2a93a626623a13f148282537"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647a60b857bd38b0cced89462771edccd9f5"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647a67ae821a16a6280aca165ebf67bd2489"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647a99f486fd1f01684ac232d503af1abf2b"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647aa2ba135123fe9c89ce50fd86dfea759b"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647aba8ef6308b3e06a2ace1cc0f225d66ca"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647acc1d59bd6682933d364f060f31f26878"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647acdea4576df8e6d7d48cc289305237120"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647ad07911eacaa2bde26a497c391e5c9946"></a>
<a id="agroup__mspi__interface_html_gga71c447d059acf7a8055c380243f3a647ae7c13ba10174e6f3f90161af69890872"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5a1882d6c9772a1fa1e9e255fe3883d86b"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5a1b3112af8589ef5e2493fc6545c4945a"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5a1d6b2be620bf17c4daecad66ba011573"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5a49283124787af5787d64c71bf38e3caa"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5a8225b99a3943f35b1c713af462a2d5da"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5a9826a30dc94c734cdad9f91148cb8673"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5a9f726ce3043c03703d48bcdc45edcbdb"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5aaee80ab69881b09ec6b85dbaaa9e8663"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5abe9925279cee8433d2b11cc3614c5a5a"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5ac70792100fe11a07c020c9825c1cdfbf"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5ac79eb0c07038226a74411ca211d9b725"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5ade6a4a01f3281e5331b3e16f1222eb02"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5af65a413ec9c72d6c7acf5154a618870a"></a>
<a id="agroup__mspi__interface_html_ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0"></a>
<a id="agroup__mspi__interface_html_ggaa2131d9846bbfd74488a6ae1c2003e68a388bbd530a438507dbfa9208ec1ebf39"></a>
<a id="agroup__mspi__interface_html_ggaa2131d9846bbfd74488a6ae1c2003e68a51f3574f42456a11cc3fcd17c1195dd9"></a>
<a id="agroup__mspi__interface_html_ggaa2131d9846bbfd74488a6ae1c2003e68a8cea9da4829a0769e3be8b8a32b79984"></a>
<a id="agroup__mspi__interface_html_ggaa2131d9846bbfd74488a6ae1c2003e68a96f82a24b684a7debe0ac32070fa53bc"></a>
<a id="agroup__mspi__interface_html_ggab33e9840b0937c944f4e1a2525534cb1a5cff8419a9236cc835a62b124debe498"></a>
<a id="agroup__mspi__interface_html_ggab33e9840b0937c944f4e1a2525534cb1a63fb981aab764d752c1166fc112094a1"></a>
<a id="agroup__mspi__interface_html_ggab33e9840b0937c944f4e1a2525534cb1aa315ad9c5ba56979914b21208920aad7"></a>
<a id="agroup__mspi__interface_html_ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277"></a>
<a id="agroup__mspi__interface_html_ggab33e9840b0937c944f4e1a2525534cb1af587e68d07441f3262ab164f48e783c0"></a>
<a id="agroup__mspi__interface_html_ggac127ef78c7b66c7eebe03782abf08c40a5e34cb52b8e8475f9457a9cab7a424ed"></a>
<a id="agroup__mspi__interface_html_ggac127ef78c7b66c7eebe03782abf08c40aacecd5fab6e2ed50be75d882eaadadd6"></a>
<a id="agroup__mspi__transfer__api_html_ga8c98c73e322c575b759ce911cc115129"></a>
<a id="agroup__mspi__transfer__api_html_gaa656820a834bcde0d06041cff8f0d5e1"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys-util_html_ga3c12c6d36ad0aa481a3436923d21f4f8"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructgpio__dt__spec_html"></a>
<a id="astructmspi__callback__context_html"></a>
<a id="astructmspi__callback__context_html_a5649bddfac23544522969fc9e500eb0c"></a>
<a id="astructmspi__callback__context_html_ab2225b77f4d9e0403192c0ab11482e2e"></a>
<a id="astructmspi__ce__control_html"></a>
<a id="astructmspi__ce__control_html_a1f1b6f5583abc08c8c7fae95e1a29a7a"></a>
<a id="astructmspi__ce__control_html_abc3e35be0b7b3f5c118b0d16033125ba"></a>
<a id="astructmspi__cfg_html"></a>
<a id="astructmspi__cfg_html_a1192af56f714a42aa667a40e369b185e"></a>
<a id="astructmspi__cfg_html_a20f6e453165b6ac22a42906604a3258a"></a>
<a id="astructmspi__cfg_html_a2cf6e063074f86973cf03324637d656a"></a>
<a id="astructmspi__cfg_html_a4053a398f6390e45ef6da385756f14bf"></a>
<a id="astructmspi__cfg_html_a449894e0e58f96b775b4cc1c1eb83e77"></a>
<a id="astructmspi__cfg_html_a6d24969046f175f158a5dae05e9284b1"></a>
<a id="astructmspi__cfg_html_a9a76198688b4acac9101274a71bfbf9c"></a>
<a id="astructmspi__cfg_html_ab33e45d7802cf777a595d87058e8bfb5"></a>
<a id="astructmspi__cfg_html_af54bbbfbe07d88325117131fefe265ef"></a>
<a id="astructmspi__cfg_html_afef0fe6991e28a4496e51333963fd3d1"></a>
<a id="astructmspi__dev__cfg_html"></a>
<a id="astructmspi__dev__cfg_html_a0b0c9f101656e67d71d191b656738d2d"></a>
<a id="astructmspi__dev__cfg_html_a0da8c2ccf80fdf610fcdd7fae7d159f8"></a>
<a id="astructmspi__dev__cfg_html_a28cf9d7887e9f840344e2804c4040bc4"></a>
<a id="astructmspi__dev__cfg_html_a2bb78caec28fadcecd787fc8a573a336"></a>
<a id="astructmspi__dev__cfg_html_a3ec3e22e25440ac5eecf0f9b2d79b9e0"></a>
<a id="astructmspi__dev__cfg_html_a60eeb1503018fa47cc5618d150f09aa8"></a>
<a id="astructmspi__dev__cfg_html_a6dbe113d5075b1b22896c7d0c281bd3d"></a>
<a id="astructmspi__dev__cfg_html_a9490d822b67d7fab123f32f38b0ccef8"></a>
<a id="astructmspi__dev__cfg_html_a9feb1c35f7e1f5c43489771e13f2af8d"></a>
<a id="astructmspi__dev__cfg_html_aae492d2e5bad4b266779be9f5bb12ee9"></a>
<a id="astructmspi__dev__cfg_html_ab6ed7eeb6d4b31530e06f69706b98278"></a>
<a id="astructmspi__dev__cfg_html_abf8d45f88d0c8e1c4ee52ea238ff4466"></a>
<a id="astructmspi__dev__cfg_html_ac9f47b226289005271a800739707456b"></a>
<a id="astructmspi__dev__cfg_html_acac2a0913bfbfe1f3b5e34ff1b71ff42"></a>
<a id="astructmspi__dev__cfg_html_ad0f5c1a4cd3002313087a9b1fe6cf7a1"></a>
<a id="astructmspi__dev__cfg_html_affdcd07ac3d3d25b8a8e0882277af39a"></a>
<a id="astructmspi__dev__id_html"></a>
<a id="astructmspi__dev__id_html_aab54e4f449d4cfb87c5c6f0ccd1d7bfb"></a>
<a id="astructmspi__dev__id_html_ac79d41731c8599f23b666f78cdb58bf0"></a>
<a id="astructmspi__driver__api_html"></a>
<a id="astructmspi__driver__api_html_a05c3dad20834850a833663dd896fa6eb"></a>
<a id="astructmspi__driver__api_html_a15a53b61fcd32d0436323ad85c75f62a"></a>
<a id="astructmspi__driver__api_html_a1a4593ada09a204004a11dcb6031c18f"></a>
<a id="astructmspi__driver__api_html_a31bf25f0ce01b9aada76f6b0030b05be"></a>
<a id="astructmspi__driver__api_html_a70c612ee3b997682b7e9f06119d7e756"></a>
<a id="astructmspi__driver__api_html_a77553c6ea19e8803dcabc4deccf35619"></a>
<a id="astructmspi__driver__api_html_aa0a42a85841370693ce054ed859d1fd8"></a>
<a id="astructmspi__driver__api_html_aae8c346182a9c437891044afc0b16e07"></a>
<a id="astructmspi__dt__spec_html"></a>
<a id="astructmspi__dt__spec_html_aaedbcdc55394032e3af50ec7d2e8f439"></a>
<a id="astructmspi__dt__spec_html_ab21ff3d5959b78f5b5cdc7fcf70e8756"></a>
<a id="astructmspi__event__data_html"></a>
<a id="astructmspi__event__data_html_a1bb8c4591ced464181927b0c00003205"></a>
<a id="astructmspi__event__data_html_a4b926cf5abb4f23bb7e1f85fecd323ef"></a>
<a id="astructmspi__event__data_html_a6e71714475e45a0d758aa49db33ff57e"></a>
<a id="astructmspi__event__data_html_ab1138c26f9a6b11b75e1e50fb3e5d8e9"></a>
<a id="astructmspi__event__data_html_af788dc5374778055d1ee9fddbe2a4d8d"></a>
<a id="astructmspi__event_html"></a>
<a id="astructmspi__event_html_a65079ed0fcdb2ca607dab070f2ed010b"></a>
<a id="astructmspi__event_html_aeeb42b82bd219169e6f185ecdcc2129d"></a>
<a id="astructmspi__memmap__cfg_html"></a>
<a id="astructmspi__memmap__cfg_html_a3ac0e8a0ee3ee9936f25c3a1a2fdfa19"></a>
<a id="astructmspi__memmap__cfg_html_a7736a88d44b6fa3b30373b12ebad4100"></a>
<a id="astructmspi__memmap__cfg_html_a9a1309b447dbc47473436df6b66f9ef3"></a>
<a id="astructmspi__memmap__cfg_html_ac7ded0cfb89863d88672c112a32fa136"></a>
<a id="astructmspi__scramble__cfg_html"></a>
<a id="astructmspi__scramble__cfg_html_a362ce29f7748d28e818e2c809bd4cedd"></a>
<a id="astructmspi__scramble__cfg_html_a8d6d5b47b3d777674b974a6c79337b43"></a>
<a id="astructmspi__scramble__cfg_html_adf56743768432f22f0a5090e1b823a67"></a>
<a id="astructmspi__timing__cfg_html"></a>
<a id="astructmspi__xfer__packet_html"></a>
<a id="astructmspi__xfer__packet_html_a050a827d0ee0349cd7a006de20b1db0c"></a>
<a id="astructmspi__xfer__packet_html_a08dae9b6fbda60f06430cb2b842280b9"></a>
<a id="astructmspi__xfer__packet_html_a0b7b3d68ff46173378e4076b439e35ac"></a>
<a id="astructmspi__xfer__packet_html_a2717e86b7fbb01be65a4955a8e26ebc0"></a>
<a id="astructmspi__xfer__packet_html_aedc8eadfb3a0737c3984b130ec21d96c"></a>
<a id="astructmspi__xfer__packet_html_afb408ea48ff8863c9714d39c4f7c8a2c"></a>
<a id="astructmspi__xfer_html"></a>
<a id="astructmspi__xfer_html_a335fd5fb02bc75053902c4d1b294af57"></a>
<a id="astructmspi__xfer_html_a387dd891ab994d75561b50a094427d22"></a>
<a id="astructmspi__xfer_html_a4061b26045ef860b8c9a6509ff054bc3"></a>
<a id="astructmspi__xfer_html_a49e4102b694ffb5f9afe72c81fb7ca94"></a>
<a id="astructmspi__xfer_html_a98f23415592095749a853f3d850d399f"></a>
<a id="astructmspi__xfer_html_aa763b87b9219d6c325a9f45d8d108d02"></a>
<a id="astructmspi__xfer_html_abf10b3fed96161447ffb7a8a6dce7649"></a>
<a id="astructmspi__xfer_html_ace851e368d69b76092f8429d83d963fd"></a>
<a id="astructmspi__xfer_html_adfe7adf63f83f40d1ab92ed511f4e917"></a>
<a id="astructmspi__xfer_html_ae2e7a475ac4bcec88f12742642087505"></a>
<a id="astructmspi__xfer_html_afa30e0fac32c6c3e7a3c9d7e29ccc8cb"></a>
<a id="astructmspi__xfer_html_afd83aa864cf300e9848ef46b7331ca5a"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2025, Ambiq Micro Inc. <www.ambiq.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MSPI_H_
#define ZEPHYR_INCLUDE_MSPI_H_

#include <errno.h>

#include <zephyr/sys/__assert.h>
#include <zephyr/types.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>

#ifdef __cplusplus
extern "C" {
#endif


enum mspi_op_mode {
        MSPI_OP_MODE_CONTROLLER     = 0,
        MSPI_OP_MODE_PERIPHERAL     = 1,
};

enum mspi_duplex {
        MSPI_HALF_DUPLEX            = 0,
        MSPI_FULL_DUPLEX            = 1,
};

enum mspi_io_mode {
        MSPI_IO_MODE_SINGLE         = 0,
        MSPI_IO_MODE_DUAL           = 1,
        MSPI_IO_MODE_DUAL_1_1_2     = 2,
        MSPI_IO_MODE_DUAL_1_2_2     = 3,
        MSPI_IO_MODE_QUAD           = 4,
        MSPI_IO_MODE_QUAD_1_1_4     = 5,
        MSPI_IO_MODE_QUAD_1_4_4     = 6,
        MSPI_IO_MODE_OCTAL          = 7,
        MSPI_IO_MODE_OCTAL_1_1_8    = 8,
        MSPI_IO_MODE_OCTAL_1_8_8    = 9,
        MSPI_IO_MODE_HEX            = 10,
        MSPI_IO_MODE_HEX_8_8_16     = 11,
        MSPI_IO_MODE_HEX_8_16_16    = 12,
        MSPI_IO_MODE_MAX,
};

enum mspi_data_rate {
        MSPI_DATA_RATE_SINGLE       = 0,
        MSPI_DATA_RATE_S_S_D        = 1,
        MSPI_DATA_RATE_S_D_D        = 2,
        MSPI_DATA_RATE_DUAL         = 3,
        MSPI_DATA_RATE_MAX,
};

enum mspi_cpp_mode {
        MSPI_CPP_MODE_0             = 0,
        MSPI_CPP_MODE_1             = 1,
        MSPI_CPP_MODE_2             = 2,
        MSPI_CPP_MODE_3             = 3,
};

enum mspi_endian {
        MSPI_XFER_LITTLE_ENDIAN     = 0,
        MSPI_XFER_BIG_ENDIAN        = 1,
};

enum mspi_ce_polarity {
        MSPI_CE_ACTIVE_LOW          = 0,
        MSPI_CE_ACTIVE_HIGH         = 1,
};

enum mspi_bus_event {
        MSPI_BUS_RESET              = 0,
        MSPI_BUS_ERROR              = 1,
        MSPI_BUS_XFER_COMPLETE      = 2,
        MSPI_BUS_TIMEOUT            = 3,
        MSPI_BUS_EVENT_MAX,
};

enum mspi_bus_event_cb_mask {
        MSPI_BUS_NO_CB              = 0,
        MSPI_BUS_RESET_CB           = BIT(0),
        MSPI_BUS_ERROR_CB           = BIT(1),
        MSPI_BUS_XFER_COMPLETE_CB   = BIT(2),
        MSPI_BUS_TIMEOUT_CB         = BIT(3),
};

enum mspi_xfer_mode {
        MSPI_PIO,
        MSPI_DMA,
};

enum mspi_xfer_priority {
        MSPI_XFER_PRIORITY_LOW,
        MSPI_XFER_PRIORITY_MEDIUM,
        MSPI_XFER_PRIORITY_HIGH,
};

enum mspi_xfer_direction {
        MSPI_RX,
        MSPI_TX,
};

enum mspi_dev_cfg_mask {
        MSPI_DEVICE_CONFIG_NONE         = 0,
        MSPI_DEVICE_CONFIG_CE_NUM       = BIT(0),
        MSPI_DEVICE_CONFIG_FREQUENCY    = BIT(1),
        MSPI_DEVICE_CONFIG_IO_MODE      = BIT(2),
        MSPI_DEVICE_CONFIG_DATA_RATE    = BIT(3),
        MSPI_DEVICE_CONFIG_CPP          = BIT(4),
        MSPI_DEVICE_CONFIG_ENDIAN       = BIT(5),
        MSPI_DEVICE_CONFIG_CE_POL       = BIT(6),
        MSPI_DEVICE_CONFIG_DQS          = BIT(7),
        MSPI_DEVICE_CONFIG_RX_DUMMY     = BIT(8),
        MSPI_DEVICE_CONFIG_TX_DUMMY     = BIT(9),
        MSPI_DEVICE_CONFIG_READ_CMD     = BIT(10),
        MSPI_DEVICE_CONFIG_WRITE_CMD    = BIT(11),
        MSPI_DEVICE_CONFIG_CMD_LEN      = BIT(12),
        MSPI_DEVICE_CONFIG_ADDR_LEN     = BIT(13),
        MSPI_DEVICE_CONFIG_MEM_BOUND    = BIT(14),
        MSPI_DEVICE_CONFIG_BREAK_TIME   = BIT(15),
        MSPI_DEVICE_CONFIG_ALL          = BIT_MASK(16),
};

enum mspi_memmap_permit {
        MSPI_MEMMAP_READ_WRITE     = 0,
        MSPI_MEMMAP_READ_ONLY      = 1,
};


enum mspi_timing_param {
        MSPI_TIMING_PARAM_DUMMY
};

struct mspi_timing_cfg {
#ifdef __cplusplus
        /* For C++ compatibility. */
        uint8_t dummy;
#endif
};

struct mspi_dev_id {
        struct gpio_dt_spec     ce;
        uint16_t                dev_idx;
};

struct mspi_cfg {
        uint8_t                 channel_num;
        enum mspi_op_mode       op_mode;
        enum mspi_duplex        duplex;
        bool                    dqs_support;
        bool                    sw_multi_periph;
        struct gpio_dt_spec     *ce_group;
        uint32_t                num_ce_gpios;
        uint32_t                num_periph;
        uint32_t                max_freq;
        bool                    re_init;
};

struct mspi_dt_spec {
        const struct device     *bus;
        struct mspi_cfg         config;
};

struct mspi_dev_cfg {
        uint8_t                 ce_num;
        uint32_t                freq;
        enum mspi_io_mode       io_mode;
        enum mspi_data_rate     data_rate;
        enum mspi_cpp_mode      cpp;
        enum mspi_endian        endian;
        enum mspi_ce_polarity   ce_polarity;
        bool                    dqs_enable;
        uint16_t                rx_dummy;
        uint16_t                tx_dummy;
        uint32_t                read_cmd;
        uint32_t                write_cmd;
        uint8_t                 cmd_length;
        uint8_t                 addr_length;
        uint32_t                mem_boundary;
        uint32_t                time_to_break;
};

struct mspi_memmap_cfg {
        bool                    enable;
        uint32_t                address_offset;
        uint32_t                size;
        enum mspi_memmap_permit permission;
};

struct mspi_scramble_cfg {
        bool                    enable;
        uint32_t                address_offset;
        uint32_t                size;
};



struct mspi_ce_control {
        struct gpio_dt_spec         gpio;
        uint32_t                    delay;
};

struct mspi_xfer_packet {
        enum mspi_xfer_direction    dir;
        enum mspi_bus_event_cb_mask cb_mask;
        uint32_t                    cmd;
        uint32_t                    address;
        uint32_t                    num_bytes;
        uint8_t                     *data_buf;
};

struct mspi_xfer {
        bool                        async;
        enum mspi_xfer_mode         xfer_mode;
        uint16_t                    tx_dummy;
        uint16_t                    rx_dummy;
        uint8_t                     cmd_length;
        uint8_t                     addr_length;
        bool                        hold_ce;
        struct mspi_ce_control      ce_sw_ctrl;
        enum mspi_xfer_priority     priority;
        const struct mspi_xfer_packet *packets;
        uint32_t                    num_packet;
        uint32_t                    timeout;
};



struct mspi_event_data {
        const struct device         *controller;
        const struct mspi_dev_id    *dev_id;
        const struct mspi_xfer_packet *packet;
        uint32_t                    status;
        uint32_t                    packet_idx;
};

struct mspi_event {
        enum mspi_bus_event         evt_type;
        struct mspi_event_data      evt_data;
};

struct mspi_callback_context {
        struct mspi_event           mspi_evt;
        void                        *ctx;
};

typedef void (*mspi_callback_handler_t)(struct mspi_callback_context *mspi_cb_ctx, ...);



typedef int (*mspi_api_config)(const struct mspi_dt_spec *spec);

typedef int (*mspi_api_dev_config)(const struct device *controller,
                                   const struct mspi_dev_id *dev_id,
                                   const enum mspi_dev_cfg_mask param_mask,
                                   const struct mspi_dev_cfg *cfg);

typedef int (*mspi_api_get_channel_status)(const struct device *controller, uint8_t ch);

typedef int (*mspi_api_transceive)(const struct device *controller,
                                   const struct mspi_dev_id *dev_id,
                                   const struct mspi_xfer *req);

typedef int (*mspi_api_register_callback)(const struct device *controller,
                                          const struct mspi_dev_id *dev_id,
                                          const enum mspi_bus_event evt_type,
                                          mspi_callback_handler_t cb,
                                          struct mspi_callback_context *ctx);

typedef int (*mspi_api_memmap_config)(const struct device *controller,
                                      const struct mspi_dev_id *dev_id,
                                      const struct mspi_memmap_cfg *memmap_cfg);

typedef int (*mspi_api_scramble_config)(const struct device *controller,
                                        const struct mspi_dev_id *dev_id,
                                        const struct mspi_scramble_cfg *scramble_cfg);

typedef int (*mspi_api_timing_config)(const struct device *controller,
                                      const struct mspi_dev_id *dev_id, const uint32_t param_mask,
                                      void *timing_cfg);

__subsystem struct mspi_driver_api {
        mspi_api_config                config;
        mspi_api_dev_config            dev_config;
        mspi_api_get_channel_status    get_channel_status;
        mspi_api_transceive            transceive;
        mspi_api_register_callback     register_callback;
        mspi_api_memmap_config         memmap_config;
        mspi_api_scramble_config       scramble_config;
        mspi_api_timing_config         timing_config;
};



__syscall int mspi_config(const struct mspi_dt_spec *spec);

static inline int z_impl_mspi_config(const struct mspi_dt_spec *spec)
{
        return DEVICE_API_GET(mspi, spec->bus)->config(spec);
}

__syscall int mspi_dev_config(const struct device *controller,
                              const struct mspi_dev_id *dev_id,
                              const enum mspi_dev_cfg_mask param_mask,
                              const struct mspi_dev_cfg *cfg);

static inline int z_impl_mspi_dev_config(const struct device *controller,
                                         const struct mspi_dev_id *dev_id,
                                         const enum mspi_dev_cfg_mask param_mask,
                                         const struct mspi_dev_cfg *cfg)
{
        return DEVICE_API_GET(mspi, controller)->dev_config(controller, dev_id, param_mask, cfg);
}

__syscall int mspi_get_channel_status(const struct device *controller, uint8_t ch);

static inline int z_impl_mspi_get_channel_status(const struct device *controller, uint8_t ch)
{
        return DEVICE_API_GET(mspi, controller)->get_channel_status(controller, ch);
}



__syscall int mspi_transceive(const struct device *controller,
                              const struct mspi_dev_id *dev_id,
                              const struct mspi_xfer *req);

static inline int z_impl_mspi_transceive(const struct device *controller,
                                         const struct mspi_dev_id *dev_id,
                                         const struct mspi_xfer *req)
{
        const struct mspi_driver_api *api = DEVICE_API_GET(mspi, controller);

        if (!api->transceive) {
                return -ENOTSUP;
        }

        return api->transceive(controller, dev_id, req);
}

static inline int mspi_transceive_data_only(const struct device *controller,
                                            const struct mspi_dev_id *dev_id,
                                            const struct mspi_xfer_packet *packets,
                                            uint32_t num_packet,
                                            enum mspi_xfer_mode xfer_mode,
                                            bool async,
                                            uint32_t timeout)
{
        struct mspi_xfer xfer = {
                .async       = async,
                .xfer_mode   = xfer_mode,
                .cmd_length  = 0,
                .addr_length = 0,
                .packets     = packets,
                .num_packet  = num_packet,
                .timeout     = timeout,
        };

        return mspi_transceive(controller, dev_id, &xfer);
}



__syscall int mspi_memmap_config(const struct device *controller,
                                 const struct mspi_dev_id *dev_id,
                                 const struct mspi_memmap_cfg *cfg);

static inline int z_impl_mspi_memmap_config(const struct device *controller,
                                            const struct mspi_dev_id *dev_id,
                                            const struct mspi_memmap_cfg *cfg)
{
        const struct mspi_driver_api *api = DEVICE_API_GET(mspi, controller);

        if (!api->memmap_config) {
                return -ENOTSUP;
        }

        return api->memmap_config(controller, dev_id, cfg);
}

__syscall int mspi_scramble_config(const struct device *controller,
                                   const struct mspi_dev_id *dev_id,
                                   const struct mspi_scramble_cfg *cfg);

static inline int z_impl_mspi_scramble_config(const struct device *controller,
                                              const struct mspi_dev_id *dev_id,
                                              const struct mspi_scramble_cfg *cfg)
{
        const struct mspi_driver_api *api = DEVICE_API_GET(mspi, controller);

        if (!api->scramble_config) {
                return -ENOTSUP;
        }

        return api->scramble_config(controller, dev_id, cfg);
}

__syscall int mspi_timing_config(const struct device *controller,
                                 const struct mspi_dev_id *dev_id,
                                 const uint32_t param_mask, void *cfg);

static inline int z_impl_mspi_timing_config(const struct device *controller,
                                            const struct mspi_dev_id *dev_id,
                                            const uint32_t param_mask, void *cfg)
{
        const struct mspi_driver_api *api = DEVICE_API_GET(mspi, controller);

        if (!api->timing_config) {
                return -ENOTSUP;
        }

        return api->timing_config(controller, dev_id, param_mask, cfg);
}



static inline int mspi_register_callback(const struct device *controller,
                                         const struct mspi_dev_id *dev_id,
                                         const enum mspi_bus_event evt_type,
                                         mspi_callback_handler_t cb,
                                         struct mspi_callback_context *ctx)
{
        const struct mspi_driver_api *api = DEVICE_API_GET(mspi, controller);

        if (!api->register_callback) {
                return -ENOTSUP;
        }

        return api->register_callback(controller, dev_id, evt_type, cb, ctx);
}


#ifdef __cplusplus
}
#endif

#include <zephyr/drivers/mspi/devicetree.h>

#include <zephyr/sys/util_macro.h>

#define MSPI_MEMMAP_CFG_STRUCT_DECLARE(_name)                                                     \
        IF_ENABLED(CONFIG_MSPI_MEMMAP, (struct mspi_memmap_cfg _name;))

#define MSPI_MEMMAP_BASE_ADDR_DECLARE(_name)                                                      \
        IF_ENABLED(CONFIG_MSPI_MEMMAP, (uint32_t _name;))

#define MSPI_SCRAMBLE_CFG_STRUCT_DECLARE(_name)                                                   \
        IF_ENABLED(CONFIG_MSPI_SCRAMBLE, (struct mspi_scramble_cfg _name;))

#define MSPI_TIMING_CFG_STRUCT_DECLARE(_name)                                                     \
        IF_ENABLED(CONFIG_MSPI_TIMING, (mspi_timing_cfg _name;))

#define MSPI_TIMING_PARAM_DECLARE(_name)                                                          \
        IF_ENABLED(CONFIG_MSPI_TIMING, (mspi_timing_param _name;))

#define MSPI_OPTIONAL_CFG_STRUCT_INIT(code, _name, _object)                                       \
        IF_ENABLED(code, (._name = _object,))

#define MSPI_MEMMAP_BASE_ADDR_INIT(_name, _bus)                                                   \
        IF_ENABLED(CONFIG_MSPI_MEMMAP, (._name = DT_REG_ADDR_BY_IDX(_bus, 1),))


#include <zephyr/syscalls/mspi.h>
#endif /* ZEPHYR_INCLUDE_MSPI_H_ */
```

## 17.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025, Ambiq Micro Inc. <www.ambiq.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 223 行

用于兼容 C++。

### 注释 3：原第 968 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MSPI_H_`。

## 17.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P017_zephyr__drivers__mspi.h_头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [mspi_op_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga3f211cd81e05cb9ee073a2722f6b22d8)
- [MSPI_OP_MODE_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga3f211cd81e05cb9ee073a2722f6b22d8a6a862f1d9931725be7789bd982d2937a)
- [MSPI_OP_MODE_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga3f211cd81e05cb9ee073a2722f6b22d8a11af11e286399c7e2f1fbcadca44ea83)
- [mspi_duplex](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga20e348d7a9f1f9b32078a3bf6c4e82b9)
- [MSPI_HALF_DUPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga20e348d7a9f1f9b32078a3bf6c4e82b9ac05ddc8ca44f1c70d3c3748e21fe80d3)
- [MSPI_FULL_DUPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga20e348d7a9f1f9b32078a3bf6c4e82b9a13a3f16c4273ca6f28671663d0ecf33c)
- [mspi_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga904dfc1c800fb9832f7c6200f767f9a5)
- [MSPI_IO_MODE_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd)
- [MSPI_IO_MODE_DUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a9826a30dc94c734cdad9f91148cb8673)
- [MSPI_IO_MODE_DUAL_1_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a8225b99a3943f35b1c713af462a2d5da)
- [MSPI_IO_MODE_DUAL_1_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5aaee80ab69881b09ec6b85dbaaa9e8663)
- [MSPI_IO_MODE_QUAD](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5af65a413ec9c72d6c7acf5154a618870a)
- [MSPI_IO_MODE_QUAD_1_1_4](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5abe9925279cee8433d2b11cc3614c5a5a)
- [MSPI_IO_MODE_QUAD_1_4_4](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a1b3112af8589ef5e2493fc6545c4945a)
- [MSPI_IO_MODE_OCTAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5ac79eb0c07038226a74411ca211d9b725)
- [MSPI_IO_MODE_OCTAL_1_1_8](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5ac70792100fe11a07c020c9825c1cdfbf)
- [MSPI_IO_MODE_OCTAL_1_8_8](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a1d6b2be620bf17c4daecad66ba011573)
- [MSPI_IO_MODE_HEX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a1882d6c9772a1fa1e9e255fe3883d86b)
- [MSPI_IO_MODE_HEX_8_8_16](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5ade6a4a01f3281e5331b3e16f1222eb02)
- [MSPI_IO_MODE_HEX_8_16_16](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a49283124787af5787d64c71bf38e3caa)
- [MSPI_IO_MODE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a9f726ce3043c03703d48bcdc45edcbdb)
- [mspi_data_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gaa2131d9846bbfd74488a6ae1c2003e68)
- [MSPI_DATA_RATE_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0)
- [MSPI_DATA_RATE_S_S_D](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a388bbd530a438507dbfa9208ec1ebf39)
- [MSPI_DATA_RATE_S_D_D](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a8cea9da4829a0769e3be8b8a32b79984)
- [MSPI_DATA_RATE_DUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a96f82a24b684a7debe0ac32070fa53bc)
- [MSPI_DATA_RATE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a51f3574f42456a11cc3fcd17c1195dd9)
- [mspi_cpp_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga704e4d3759d3261b4468e9d9900e578c)
- [MSPI_CPP_MODE_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90)
- [MSPI_CPP_MODE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga704e4d3759d3261b4468e9d9900e578ca8c93d56778ea1cbf901db1a4b9fee870)
- [MSPI_CPP_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga704e4d3759d3261b4468e9d9900e578cabbde8c1ad9a5a8a9a3ca4ce33e2c0705)
- [MSPI_CPP_MODE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga704e4d3759d3261b4468e9d9900e578ca415e431b25ac4a12f35b139ccb77ba48)
- [mspi_endian](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga3625cde1379e66cb66a8cb3803ab2e44)
- [MSPI_XFER_LITTLE_ENDIAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345)
- [MSPI_XFER_BIG_ENDIAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga3625cde1379e66cb66a8cb3803ab2e44a08e9349361779ce246bb7da6a1f3012d)
- [mspi_ce_polarity](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga283275f86fe186f4b5e30110ae0d506b)
- [MSPI_CE_ACTIVE_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae)
- [MSPI_CE_ACTIVE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga283275f86fe186f4b5e30110ae0d506ba375e0b870800e0982b3715417e109a22)
- [mspi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5)
- [MSPI_BUS_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5afb1c2030d871cbbaa4341df7989a5a64)
- [MSPI_BUS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5aeeaf87802ecc90ada4c39f65fc0e8af0)
- [MSPI_BUS_XFER_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5ad47099019f15f97d83bc6435e5e76a61)
- [MSPI_BUS_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5a9c538a902c3e5fa1086c0f0fcee4b7e6)
- [MSPI_BUS_EVENT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5a325aa40170de5621e89aa2def557f85a)
- [mspi_bus_event_cb_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gab33e9840b0937c944f4e1a2525534cb1)
- [MSPI_BUS_NO_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277)
- [MSPI_BUS_RESET_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1a63fb981aab764d752c1166fc112094a1)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [MSPI_BUS_ERROR_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1a5cff8419a9236cc835a62b124debe498)
- [MSPI_BUS_XFER_COMPLETE_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1aa315ad9c5ba56979914b21208920aad7)
- [MSPI_BUS_TIMEOUT_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1af587e68d07441f3262ab164f48e783c0)
- [mspi_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga116259bbb1d12a10c2ba9e6051f2f000)
- [MSPI_PIO](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga116259bbb1d12a10c2ba9e6051f2f000abea5c6920a3e81fe332c2a76e4d838a1)
- [MSPI_DMA](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga116259bbb1d12a10c2ba9e6051f2f000a5a7235fe9c633206906d76d329f623a8)
- [mspi_xfer_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga632af162124ca2959a21ca3759e1cc9e)
- [MSPI_XFER_PRIORITY_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga632af162124ca2959a21ca3759e1cc9ea31222dc35adf9bed70571b9b640aca97)
- [MSPI_XFER_PRIORITY_MEDIUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga632af162124ca2959a21ca3759e1cc9ea66753cdf13762a1dd995638ff71544e0)
- [MSPI_XFER_PRIORITY_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga632af162124ca2959a21ca3759e1cc9ea3004e6ae8226294b669f2207e928f928)
- [mspi_xfer_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga498f10591acf5dc7ec88e0aa98e537d6)
- [MSPI_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga498f10591acf5dc7ec88e0aa98e537d6a044160eb569add203f06d963f57d3541)
- [MSPI_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga498f10591acf5dc7ec88e0aa98e537d6a213d4457305ab45d31b9c06ec85d2b8a)
- [mspi_dev_cfg_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga71c447d059acf7a8055c380243f3a647)
- [MSPI_DEVICE_CONFIG_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647acc1d59bd6682933d364f060f31f26878)
- [MSPI_DEVICE_CONFIG_CE_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a4a476e51f0d3613aab1bc9c1b335bab2)
- [MSPI_DEVICE_CONFIG_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a135b081210bd5aabf5b610fe90212809)
- [MSPI_DEVICE_CONFIG_IO_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a4aba5c75b43e1a87c66e940069b5b27f)
- [MSPI_DEVICE_CONFIG_DATA_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a0e954604ea419f6a4fdea59e620bdcd9)
- [MSPI_DEVICE_CONFIG_CPP](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a0d7032e045c80ca266e98f8c6684af65)
- [MSPI_DEVICE_CONFIG_ENDIAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647aba8ef6308b3e06a2ace1cc0f225d66ca)
- [MSPI_DEVICE_CONFIG_CE_POL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a51f46405fe8923a8b0c39bc2aad1ba0b)
- [MSPI_DEVICE_CONFIG_DQS](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a56ceb1ba2a93a626623a13f148282537)
- [MSPI_DEVICE_CONFIG_RX_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a13385127a309507ff01559122e03623a)
- [MSPI_DEVICE_CONFIG_TX_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a60b857bd38b0cced89462771edccd9f5)
- [MSPI_DEVICE_CONFIG_READ_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647ae7c13ba10174e6f3f90161af69890872)
- [MSPI_DEVICE_CONFIG_WRITE_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a99f486fd1f01684ac232d503af1abf2b)
- [MSPI_DEVICE_CONFIG_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a1a2e21a3cbf0ee42977cc8a43efd3fac)
- [MSPI_DEVICE_CONFIG_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647aa2ba135123fe9c89ce50fd86dfea759b)
- [MSPI_DEVICE_CONFIG_MEM_BOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647ad07911eacaa2bde26a497c391e5c9946)
- [MSPI_DEVICE_CONFIG_BREAK_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647acdea4576df8e6d7d48cc289305237120)
- [MSPI_DEVICE_CONFIG_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a67ae821a16a6280aca165ebf67bd2489)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)
- [mspi_memmap_permit](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gac127ef78c7b66c7eebe03782abf08c40)
- [MSPI_MEMMAP_READ_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggac127ef78c7b66c7eebe03782abf08c40a5e34cb52b8e8475f9457a9cab7a424ed)
- [MSPI_MEMMAP_READ_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggac127ef78c7b66c7eebe03782abf08c40aacecd5fab6e2ed50be75d882eaadadd6)
- [mspi_timing_param](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaa25a7f97ab3437d4544832a0e7474f4a)
- [MSPI_TIMING_PARAM_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#ggaa25a7f97ab3437d4544832a0e7474f4aafae0ccedcd3b8f05e798037bf5414237)
- [mspi_timing_cfg](../peripheral_bus_storage_model_reference/P049_mspi_timing_cfg_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [ce](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md#ac79d41731c8599f23b666f78cdb58bf0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [dev_idx](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md#aab54e4f449d4cfb87c5c6f0ccd1d7bfb)
- [mspi_cfg](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md)
- [channel_num](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#af54bbbfbe07d88325117131fefe265ef)
- [op_mode](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#ab33e45d7802cf777a595d87058e8bfb5)
- [duplex](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a449894e0e58f96b775b4cc1c1eb83e77)
- [dqs_support](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a2cf6e063074f86973cf03324637d656a)
- [sw_multi_periph](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a1192af56f714a42aa667a40e369b185e)
- [ce_group](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a4053a398f6390e45ef6da385756f14bf)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [num_ce_gpios](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a20f6e453165b6ac22a42906604a3258a)
- [num_periph](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a6d24969046f175f158a5dae05e9284b1)
- [max_freq](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a9a76198688b4acac9101274a71bfbf9c)
- [re_init](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#afef0fe6991e28a4496e51333963fd3d1)
- [mspi_dt_spec](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bus](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md#ab21ff3d5959b78f5b5cdc7fcf70e8756)
- [config](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md#aaedbcdc55394032e3af50ec7d2e8f439)
- [mspi_dev_cfg](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md)
- [ce_num](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#abf8d45f88d0c8e1c4ee52ea238ff4466)
- [freq](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a9490d822b67d7fab123f32f38b0ccef8)
- [io_mode](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#ad0f5c1a4cd3002313087a9b1fe6cf7a1)
- [data_rate](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a0da8c2ccf80fdf610fcdd7fae7d159f8)
- [cpp](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a2bb78caec28fadcecd787fc8a573a336)
- [endian](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a28cf9d7887e9f840344e2804c4040bc4)
- [ce_polarity](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#ab6ed7eeb6d4b31530e06f69706b98278)
- [dqs_enable](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#affdcd07ac3d3d25b8a8e0882277af39a)
- [rx_dummy](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#aae492d2e5bad4b266779be9f5bb12ee9)
- [tx_dummy](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a9feb1c35f7e1f5c43489771e13f2af8d)
- [read_cmd](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#ac9f47b226289005271a800739707456b)
- [write_cmd](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#acac2a0913bfbfe1f3b5e34ff1b71ff42)
- [cmd_length](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a0b0c9f101656e67d71d191b656738d2d)
- [addr_length](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a6dbe113d5075b1b22896c7d0c281bd3d)
- [mem_boundary](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a3ec3e22e25440ac5eecf0f9b2d79b9e0)
- [time_to_break](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a60eeb1503018fa47cc5618d150f09aa8)
- [mspi_memmap_cfg](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md)
- [enable](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md#ac7ded0cfb89863d88672c112a32fa136)
- [address_offset](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md#a7736a88d44b6fa3b30373b12ebad4100)
- [size](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md#a3ac0e8a0ee3ee9936f25c3a1a2fdfa19)
- [permission](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md#a9a1309b447dbc47473436df6b66f9ef3)
- [mspi_scramble_cfg](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md)
- [enable](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md#a362ce29f7748d28e818e2c809bd4cedd)
- [address_offset](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md#adf56743768432f22f0a5090e1b823a67)
- [size](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md#a8d6d5b47b3d777674b974a6c79337b43)
- [mspi_ce_control](../peripheral_bus_storage_model_reference/P038_mspi_ce_control_结构体.md)
- [gpio](../peripheral_bus_storage_model_reference/P038_mspi_ce_control_结构体.md#a1f1b6f5583abc08c8c7fae95e1a29a7a)
- [delay](../peripheral_bus_storage_model_reference/P038_mspi_ce_control_结构体.md#abc3e35be0b7b3f5c118b0d16033125ba)
- [mspi_xfer_packet](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md)
- [dir](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#afb408ea48ff8863c9714d39c4f7c8a2c)
- [cb_mask](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#aedc8eadfb3a0737c3984b130ec21d96c)
- [cmd](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#a2717e86b7fbb01be65a4955a8e26ebc0)
- [address](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#a08dae9b6fbda60f06430cb2b842280b9)
- [num_bytes](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#a050a827d0ee0349cd7a006de20b1db0c)
- [data_buf](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#a0b7b3d68ff46173378e4076b439e35ac)
- [mspi_xfer](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md)
- [async](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#abf10b3fed96161447ffb7a8a6dce7649)
- [xfer_mode](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#afa30e0fac32c6c3e7a3c9d7e29ccc8cb)
- [tx_dummy](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#adfe7adf63f83f40d1ab92ed511f4e917)
- [rx_dummy](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#a98f23415592095749a853f3d850d399f)
- [cmd_length](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#a387dd891ab994d75561b50a094427d22)
- [addr_length](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#ace851e368d69b76092f8429d83d963fd)
- [hold_ce](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#a335fd5fb02bc75053902c4d1b294af57)
- [ce_sw_ctrl](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#ae2e7a475ac4bcec88f12742642087505)
- [priority](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#aa763b87b9219d6c325a9f45d8d108d02)
- [packets](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#a49e4102b694ffb5f9afe72c81fb7ca94)
- [num_packet](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#a4061b26045ef860b8c9a6509ff054bc3)
- [timeout](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#afd83aa864cf300e9848ef46b7331ca5a)
- [mspi_event_data](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md)
- [controller](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md#af788dc5374778055d1ee9fddbe2a4d8d)
- [dev_id](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md#ab1138c26f9a6b11b75e1e50fb3e5d8e9)
- [packet](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md#a1bb8c4591ced464181927b0c00003205)
- [status](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md#a4b926cf5abb4f23bb7e1f85fecd323ef)
- [packet_idx](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md#a6e71714475e45a0d758aa49db33ff57e)
- [mspi_event](../peripheral_bus_storage_model_reference/P045_mspi_event_结构体.md)
- [evt_type](../peripheral_bus_storage_model_reference/P045_mspi_event_结构体.md#a65079ed0fcdb2ca607dab070f2ed010b)
- [evt_data](../peripheral_bus_storage_model_reference/P045_mspi_event_结构体.md#aeeb42b82bd219169e6f185ecdcc2129d)
- [mspi_callback_context](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md)
- [mspi_evt](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md#a5649bddfac23544522969fc9e500eb0c)
- [ctx](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md#ab2225b77f4d9e0403192c0ab11482e2e)
- [mspi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html#ga29421f748fdb89c823e1a48ff69cf0f4)
- [mspi_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga2ff9209634fb241e2f7323e749df612e)
- [mspi_api_dev_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga7e3bae501067b045e9ed8d0efbe6e61d)
- [mspi_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#gadd66b118b76a4ee7ef252afc6b830bfa)
- [mspi_api_transceive](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga17b551f4d9f980fde8eabcaae3318617)
- [mspi_api_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#gad6d65ef0d523f22592ff17c04698f663)
- [mspi_api_memmap_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga002c5d3cc7d6691130dee0f42b928894)
- [mspi_api_scramble_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga092c8bb0879977a8cc8eea5d1662c34b)
- [mspi_api_timing_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga407713e07f23756564814402342c9c97)
- [mspi_driver_api](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md)
- [config](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#a05c3dad20834850a833663dd896fa6eb)
- [dev_config](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#a1a4593ada09a204004a11dcb6031c18f)
- [get_channel_status](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#a31bf25f0ce01b9aada76f6b0030b05be)
- [transceive](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#aae8c346182a9c437891044afc0b16e07)
- [register_callback](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#a15a53b61fcd32d0436323ad85c75f62a)
- [memmap_config](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#a70c612ee3b997682b7e9f06119d7e756)
- [scramble_config](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#aa0a42a85841370693ce054ed859d1fd8)
- [timing_config](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#a77553c6ea19e8803dcabc4deccf35619)
- [mspi_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#ga46c2b98e99ecea045c1ecac4bdf3f087)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [mspi_dev_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaa3c1eae8b3000c9bafcc26f14a8beb8b)
- [mspi_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#ga957b6ecd96c9f942f75bbe500898930d)
- [mspi_transceive](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__transfer__api.html#ga8c98c73e322c575b759ce911cc115129)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [mspi_transceive_data_only](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__transfer__api.html#gaa656820a834bcde0d06041cff8f0d5e1)
- [mspi_memmap_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gac025129882f814b59d5726c01f0138ce)
- [mspi_scramble_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gacf287e08b6ce4898524884e8de22b806)
- [mspi_timing_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaff82af1cfc99b9e78cec17ea27f79ab6)
- [mspi_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html#ga967f5fed63f08ac2d5a88625b030cd14)
- [zephyr/drivers/mspi/devicetree.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mspi_2devicetree_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [devicetree.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mspi_2devicetree_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mspi_callback_context::mspi_evt](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md#a5649bddfac23544522969fc9e500eb0c)
- [mspi_callback_context::ctx](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md#ab2225b77f4d9e0403192c0ab11482e2e)
- [mspi_ce_control::gpio](../peripheral_bus_storage_model_reference/P038_mspi_ce_control_结构体.md#a1f1b6f5583abc08c8c7fae95e1a29a7a)
- [mspi_ce_control::delay](../peripheral_bus_storage_model_reference/P038_mspi_ce_control_结构体.md#abc3e35be0b7b3f5c118b0d16033125ba)
- [mspi_cfg::sw_multi_periph](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a1192af56f714a42aa667a40e369b185e)
- [mspi_cfg::num_ce_gpios](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a20f6e453165b6ac22a42906604a3258a)
- [mspi_cfg::dqs_support](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a2cf6e063074f86973cf03324637d656a)
- [mspi_cfg::ce_group](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a4053a398f6390e45ef6da385756f14bf)
- [mspi_cfg::duplex](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a449894e0e58f96b775b4cc1c1eb83e77)
- [mspi_cfg::num_periph](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a6d24969046f175f158a5dae05e9284b1)
- [mspi_cfg::max_freq](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#a9a76198688b4acac9101274a71bfbf9c)
- [mspi_cfg::op_mode](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#ab33e45d7802cf777a595d87058e8bfb5)
- [mspi_cfg::channel_num](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#af54bbbfbe07d88325117131fefe265ef)
- [mspi_cfg::re_init](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md#afef0fe6991e28a4496e51333963fd3d1)
- [mspi_dev_cfg::cmd_length](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a0b0c9f101656e67d71d191b656738d2d)
- [mspi_dev_cfg::data_rate](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a0da8c2ccf80fdf610fcdd7fae7d159f8)
- [mspi_dev_cfg::endian](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a28cf9d7887e9f840344e2804c4040bc4)
- [mspi_dev_cfg::cpp](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a2bb78caec28fadcecd787fc8a573a336)
- [mspi_dev_cfg::mem_boundary](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a3ec3e22e25440ac5eecf0f9b2d79b9e0)
- [mspi_dev_cfg::time_to_break](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a60eeb1503018fa47cc5618d150f09aa8)
- [mspi_dev_cfg::addr_length](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a6dbe113d5075b1b22896c7d0c281bd3d)
- [mspi_dev_cfg::freq](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a9490d822b67d7fab123f32f38b0ccef8)
- [mspi_dev_cfg::tx_dummy](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#a9feb1c35f7e1f5c43489771e13f2af8d)
- [mspi_dev_cfg::rx_dummy](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#aae492d2e5bad4b266779be9f5bb12ee9)
- [mspi_dev_cfg::ce_polarity](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#ab6ed7eeb6d4b31530e06f69706b98278)
- [mspi_dev_cfg::ce_num](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#abf8d45f88d0c8e1c4ee52ea238ff4466)
- [mspi_dev_cfg::read_cmd](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#ac9f47b226289005271a800739707456b)
- [mspi_dev_cfg::write_cmd](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#acac2a0913bfbfe1f3b5e34ff1b71ff42)
- [mspi_dev_cfg::io_mode](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#ad0f5c1a4cd3002313087a9b1fe6cf7a1)
- [mspi_dev_cfg::dqs_enable](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md#affdcd07ac3d3d25b8a8e0882277af39a)
- [mspi_dev_id::dev_idx](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md#aab54e4f449d4cfb87c5c6f0ccd1d7bfb)
- [mspi_dev_id::ce](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md#ac79d41731c8599f23b666f78cdb58bf0)
- [mspi_driver_api::config](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#a05c3dad20834850a833663dd896fa6eb)
- [mspi_driver_api::register_callback](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#a15a53b61fcd32d0436323ad85c75f62a)
- [mspi_driver_api::dev_config](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#a1a4593ada09a204004a11dcb6031c18f)
- [mspi_driver_api::get_channel_status](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#a31bf25f0ce01b9aada76f6b0030b05be)
- [mspi_driver_api::memmap_config](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#a70c612ee3b997682b7e9f06119d7e756)
- [mspi_driver_api::timing_config](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#a77553c6ea19e8803dcabc4deccf35619)
- [mspi_driver_api::scramble_config](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#aa0a42a85841370693ce054ed859d1fd8)
- [mspi_driver_api::transceive](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md#aae8c346182a9c437891044afc0b16e07)
- [mspi_dt_spec::config](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md#aaedbcdc55394032e3af50ec7d2e8f439)
- [mspi_dt_spec::bus](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md#ab21ff3d5959b78f5b5cdc7fcf70e8756)
- [mspi_event_data::packet](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md#a1bb8c4591ced464181927b0c00003205)
- [mspi_event_data::status](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md#a4b926cf5abb4f23bb7e1f85fecd323ef)
- [mspi_event_data::packet_idx](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md#a6e71714475e45a0d758aa49db33ff57e)
- [mspi_event_data::dev_id](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md#ab1138c26f9a6b11b75e1e50fb3e5d8e9)
- [mspi_event_data::controller](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md#af788dc5374778055d1ee9fddbe2a4d8d)
- [mspi_event::evt_type](../peripheral_bus_storage_model_reference/P045_mspi_event_结构体.md#a65079ed0fcdb2ca607dab070f2ed010b)
- [mspi_event::evt_data](../peripheral_bus_storage_model_reference/P045_mspi_event_结构体.md#aeeb42b82bd219169e6f185ecdcc2129d)
- [mspi_memmap_cfg::size](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md#a3ac0e8a0ee3ee9936f25c3a1a2fdfa19)
- [mspi_memmap_cfg::address_offset](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md#a7736a88d44b6fa3b30373b12ebad4100)
- [mspi_memmap_cfg::permission](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md#a9a1309b447dbc47473436df6b66f9ef3)
- [mspi_memmap_cfg::enable](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md#ac7ded0cfb89863d88672c112a32fa136)
- [mspi_scramble_cfg::enable](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md#a362ce29f7748d28e818e2c809bd4cedd)
- [mspi_scramble_cfg::size](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md#a8d6d5b47b3d777674b974a6c79337b43)
- [mspi_scramble_cfg::address_offset](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md#adf56743768432f22f0a5090e1b823a67)
- [mspi_xfer_packet::num_bytes](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#a050a827d0ee0349cd7a006de20b1db0c)
- [mspi_xfer_packet::address](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#a08dae9b6fbda60f06430cb2b842280b9)
- [mspi_xfer_packet::data_buf](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#a0b7b3d68ff46173378e4076b439e35ac)
- [mspi_xfer_packet::cmd](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#a2717e86b7fbb01be65a4955a8e26ebc0)
- [mspi_xfer_packet::cb_mask](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#aedc8eadfb3a0737c3984b130ec21d96c)
- [mspi_xfer_packet::dir](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#afb408ea48ff8863c9714d39c4f7c8a2c)
- [mspi_xfer::hold_ce](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#a335fd5fb02bc75053902c4d1b294af57)
- [mspi_xfer::cmd_length](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#a387dd891ab994d75561b50a094427d22)
- [mspi_xfer::num_packet](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#a4061b26045ef860b8c9a6509ff054bc3)
- [mspi_xfer::packets](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#a49e4102b694ffb5f9afe72c81fb7ca94)
- [mspi_xfer::rx_dummy](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#a98f23415592095749a853f3d850d399f)
- [mspi_xfer::priority](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#aa763b87b9219d6c325a9f45d8d108d02)
- [mspi_xfer::async](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#abf10b3fed96161447ffb7a8a6dce7649)
- [mspi_xfer::addr_length](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#ace851e368d69b76092f8429d83d963fd)
- [mspi_xfer::tx_dummy](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#adfe7adf63f83f40d1ab92ed511f4e917)
- [mspi_xfer::ce_sw_ctrl](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#ae2e7a475ac4bcec88f12742642087505)
- [mspi_xfer::xfer_mode](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#afa30e0fac32c6c3e7a3c9d7e29ccc8cb)
- [mspi_xfer::timeout](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#afd83aa864cf300e9848ef46b7331ca5a)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P016_zephyr__drivers__mspi__mspi_cadence.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__drivers__mspi__mspi_dw.h_头文件源码.md)
