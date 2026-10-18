---
id: learning.zephyr-docs.api-source-reference.page-47
title: auxdisplay.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/auxdisplay_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_auxdisplay.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/auxdisplay_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/auxdisplay_8h.html)。

## 47.1\_原始可见代码（Source Code）

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
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="foldopen00108"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00120"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00141"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="foldopen00277"></a>
<a id="l00277"></a>
<a id="l00281"></a>
<a id="l00285"></a>
<a id="l00289"></a>
<a id="l00293"></a>
<a id="l00297"></a>
<a id="l00301"></a>
<a id="l00305"></a>
<a id="l00309"></a>
<a id="l00313"></a>
<a id="l00317"></a>
<a id="l00321"></a>
<a id="l00325"></a>
<a id="l00329"></a>
<a id="l00333"></a>
<a id="l00337"></a>
<a id="l00341"></a>
<a id="l00345"></a>
<a id="l00349"></a>
<a id="l00353"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00363"></a>
<a id="l00372"></a>
<a id="l00373"></a>
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
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
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
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
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
<a id="l00518"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
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
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
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
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00695"></a>
<a id="l00696"></a>
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
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
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
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00781"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00810"></a>
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
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00851"></a>
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
<a id="l00869"></a>
<a id="l00870"></a>
<a id="l00871"></a>
<a id="l00872"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga095f0b08e482727a05973f4263d30093"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga15ddaa101a8399febff08e065d2b8878"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga1d30d7d50f3052f31d73367034a78ac3"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga25df80bc845a83f0bcdd2bc9083e595a"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga266a31661ae5370e11b5f2eccb9d0a55"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga3afc243389b001683f4ee5466678100d"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga44a9dac2fea0b3eef65dd140e4f81105"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga4c76fd207dcaf659481725416ec4de66"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga585ea33c13736d0500766c75c7145b48"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga59ee336b7cbbc56a8f02331caad74ba8"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga6971aee119d3806e161c2b6c5c0158d4"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga6d95cc2416de90adf2613e33106e5405"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga7ad06a27ebff673599d1e92e7714bd20"></a>
<a id="agroup__auxdisplay__interface__backend_html_ga7caf2a44b902627aec02bdcb2491b4a5"></a>
<a id="agroup__auxdisplay__interface__backend_html_gaa0d87c8648d244816df62c29a6fb07e0"></a>
<a id="agroup__auxdisplay__interface__backend_html_gab1af1819efa902c0cf448a8fda8dd3dc"></a>
<a id="agroup__auxdisplay__interface__backend_html_gab9caf3b35dd3a22f6f5bbae6568a3e8d"></a>
<a id="agroup__auxdisplay__interface__backend_html_gac3679902422c05974d1262ab3e002169"></a>
<a id="agroup__auxdisplay__interface__backend_html_gadf5064c065e5c9cd417152ee2210dafb"></a>
<a id="agroup__auxdisplay__interface__backend_html_gafe80906adf675409f28cf95306dc7b0a"></a>
<a id="agroup__auxdisplay__interface_html_ga02e8e930203cfb1410752a0ffee9a34e"></a>
<a id="agroup__auxdisplay__interface_html_ga1f5be6fefc759607d2859a648a1fb3b8"></a>
<a id="agroup__auxdisplay__interface_html_ga1f9e363765d715edb899901a14c54674"></a>
<a id="agroup__auxdisplay__interface_html_ga231dd862cda34ea4c0c8870675556f8d"></a>
<a id="agroup__auxdisplay__interface_html_ga28aef24928543329c706513cc7e5b814"></a>
<a id="agroup__auxdisplay__interface_html_ga2af115a23f370e0770b3c998ecf0b96b"></a>
<a id="agroup__auxdisplay__interface_html_ga34b31b70fdc57e33fc46f1048cc25e1a"></a>
<a id="agroup__auxdisplay__interface_html_ga37bd5403c876ff294be5ea72292de4b4"></a>
<a id="agroup__auxdisplay__interface_html_ga4dd5cba56d4b90b77ae8ad02122ef81c"></a>
<a id="agroup__auxdisplay__interface_html_ga5f95ac69e18091883e7121103014be10"></a>
<a id="agroup__auxdisplay__interface_html_ga625f399720417715090793c7f6d63f7e"></a>
<a id="agroup__auxdisplay__interface_html_ga7102ec9941f8b3131a18e4ff7b640241"></a>
<a id="agroup__auxdisplay__interface_html_ga7191475b362f728cc92eb07cb1f2ed00"></a>
<a id="agroup__auxdisplay__interface_html_ga78861a5414ac95e9ca77436c0b82acc2"></a>
<a id="agroup__auxdisplay__interface_html_ga7930b8287b2cefa08af90a755fd5651c"></a>
<a id="agroup__auxdisplay__interface_html_ga87064057ae857f81431e6e9f139a6aaa"></a>
<a id="agroup__auxdisplay__interface_html_ga98b0be37fc76df0ae4dec0bef6c94504"></a>
<a id="agroup__auxdisplay__interface_html_ga9c6302789d9cc9e481dd7c54ef370988"></a>
<a id="agroup__auxdisplay__interface_html_gaa5a643603353319946c823cc959b74b3"></a>
<a id="agroup__auxdisplay__interface_html_gaf03a1068b0aed1f27ee9e2e61066da08"></a>
<a id="agroup__auxdisplay__interface_html_gaf10ebdbe821894ccbeccb35bfa985fea"></a>
<a id="agroup__auxdisplay__interface_html_gafb18729b4897cea83dbfc1c7241f5b2d"></a>
<a id="agroup__auxdisplay__interface_html_gaffb3c1c41d810355fe2da3558ebba0c2"></a>
<a id="agroup__auxdisplay__interface_html_gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352"></a>
<a id="agroup__auxdisplay__interface_html_gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3"></a>
<a id="agroup__auxdisplay__interface_html_gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599"></a>
<a id="agroup__auxdisplay__interface_html_gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23"></a>
<a id="agroup__auxdisplay__interface_html_gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404"></a>
<a id="agroup__auxdisplay__interface_html_gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28"></a>
<a id="agroup__auxdisplay__interface_html_gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructauxdisplay__capabilities_html"></a>
<a id="astructauxdisplay__capabilities_html_a15e3926754baaefffa1eff45573a59b1"></a>
<a id="astructauxdisplay__capabilities_html_a4b66412a2000fe09f30c555befbd11d0"></a>
<a id="astructauxdisplay__capabilities_html_a55ac50abb253e64e9fb7be6542801dc9"></a>
<a id="astructauxdisplay__capabilities_html_ac0fc352a5799328211ae6f8c94cdcd7a"></a>
<a id="astructauxdisplay__capabilities_html_ace4d7b099428e5f7164c3e9e318c1feb"></a>
<a id="astructauxdisplay__capabilities_html_ad77f390f5a6bdbebabc703fdc77322a3"></a>
<a id="astructauxdisplay__capabilities_html_adc88b37e9f73a98560099c94c8797741"></a>
<a id="astructauxdisplay__capabilities_html_af1bcdc27adb678ca4447614a22366aba"></a>
<a id="astructauxdisplay__character_html"></a>
<a id="astructauxdisplay__character_html_a217dd562886158efec238649fb4ade04"></a>
<a id="astructauxdisplay__character_html_a4b011716576201818278aa853bfe542e"></a>
<a id="astructauxdisplay__character_html_a9f0bb424b9918e0f0c07c12eb4235677"></a>
<a id="astructauxdisplay__custom__data_html"></a>
<a id="astructauxdisplay__custom__data_html_aa9c3b2af7c07e71e8cc5cd3eae058729"></a>
<a id="astructauxdisplay__custom__data_html_ac995ecff9634acbc535a47b37134c6e1"></a>
<a id="astructauxdisplay__custom__data_html_acfd41be1569cc43bd09824c5e46b8d51"></a>
<a id="astructauxdisplay__driver__api_html"></a>
<a id="astructauxdisplay__driver__api_html_a125ae58199d088b69798476154993112"></a>
<a id="astructauxdisplay__driver__api_html_a163a4be1fc6ee573d893488b33fca489"></a>
<a id="astructauxdisplay__driver__api_html_a2645cbcf10191d7d2c8e83b26c4bda7e"></a>
<a id="astructauxdisplay__driver__api_html_a26c4c871f4b55ef671cb3efe5f45b819"></a>
<a id="astructauxdisplay__driver__api_html_a375a125f4b1de808d9fd7cddc9013c21"></a>
<a id="astructauxdisplay__driver__api_html_a3a8ca50150440d30a6267f0494ab03e0"></a>
<a id="astructauxdisplay__driver__api_html_a761472ca5d4f17d5f25922a6f3aa90d5"></a>
<a id="astructauxdisplay__driver__api_html_a76d0849a3edb9e0d7ef892832f2bbeb2"></a>
<a id="astructauxdisplay__driver__api_html_a7bc90af6d38d9ea853cb8360360af143"></a>
<a id="astructauxdisplay__driver__api_html_a838eacf860746e846602acf518ad56bb"></a>
<a id="astructauxdisplay__driver__api_html_a926903e94c19a7167d20d15fd4cdaa5d"></a>
<a id="astructauxdisplay__driver__api_html_a933054e57982b898f9544438d0d9829a"></a>
<a id="astructauxdisplay__driver__api_html_a9e3301bce6a3a98be1f390981b683431"></a>
<a id="astructauxdisplay__driver__api_html_ab646760f55a3b211ae49ac53c977f919"></a>
<a id="astructauxdisplay__driver__api_html_ab7d64386691f3df09c4268deb6b6f4fb"></a>
<a id="astructauxdisplay__driver__api_html_ac2b6300187110c4d7f778d2fdf97f46e"></a>
<a id="astructauxdisplay__driver__api_html_ad34aa550c542518f564c376777067bbd"></a>
<a id="astructauxdisplay__driver__api_html_ad91b99ae3f81bea042ea45cc83624faf"></a>
<a id="astructauxdisplay__driver__api_html_af65285a6e2311b590a8983575845c762"></a>
<a id="astructauxdisplay__driver__api_html_afa89a0d6fdf07934abee57f46525c851"></a>
<a id="astructauxdisplay__light_html"></a>
<a id="astructauxdisplay__light_html_a4cd0c416ce77a45949feb90ae9f254a1"></a>
<a id="astructauxdisplay__light_html_a8f40f5fd3f825f1ee8c34891804cc003"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructdevice_html_a4a2e6a2cfeb6efed7d5383c33458f46d"></a>

```c
/*
 * Copyright (c) 2022-2023 Jamie McCrae
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_AUXDISPLAY_H_
#define ZEPHYR_INCLUDE_DRIVERS_AUXDISPLAY_H_


#include <stdint.h>
#include <stddef.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

#define AUXDISPLAY_LIGHT_NOT_SUPPORTED 0

typedef uint32_t auxdisplay_mode_t;

enum auxdisplay_position {
        AUXDISPLAY_POSITION_ABSOLUTE = 0,

        AUXDISPLAY_POSITION_RELATIVE,

        AUXDISPLAY_POSITION_RELATIVE_DIRECTION,

        AUXDISPLAY_POSITION_COUNT,
};

enum auxdisplay_direction {
        AUXDISPLAY_DIRECTION_RIGHT = 0,

        AUXDISPLAY_DIRECTION_LEFT,

        AUXDISPLAY_DIRECTION_COUNT,
};

struct auxdisplay_light {
        uint8_t minimum;

        uint8_t maximum;
};

struct auxdisplay_capabilities {
        uint16_t columns;

        uint16_t rows;

        auxdisplay_mode_t mode;

        struct auxdisplay_light brightness;

        struct auxdisplay_light backlight;

        uint8_t custom_characters;

        uint8_t custom_character_width;

        uint8_t custom_character_height;
};

struct auxdisplay_custom_data {
        uint8_t *data;

        uint16_t len;

        uint32_t options;
};

struct auxdisplay_character {
        uint8_t index;

        uint8_t *data;

        uint8_t character_code;
};


typedef int (*auxdisplay_display_on_t)(const struct device *dev);

typedef int (*auxdisplay_display_off_t)(const struct device *dev);

typedef int (*auxdisplay_cursor_set_enabled_t)(const struct device *dev, bool enabled);

typedef int (*auxdisplay_position_blinking_set_enabled_t)(const struct device *dev,
                                                          bool enabled);

typedef int (*auxdisplay_cursor_shift_set_t)(const struct device *dev, uint8_t direction,
                                             bool display_shift);

typedef int (*auxdisplay_cursor_position_set_t)(const struct device *dev,
                                                enum auxdisplay_position type,
                                                int16_t x, int16_t y);

typedef int (*auxdisplay_cursor_position_get_t)(const struct device *dev, int16_t *x,
                                                int16_t *y);

typedef int (*auxdisplay_display_position_set_t)(const struct device *dev,
                                                 enum auxdisplay_position type,
                                                 int16_t x, int16_t y);

typedef int (*auxdisplay_display_position_get_t)(const struct device *dev, int16_t *x,
                                                 int16_t *y);

typedef int (*auxdisplay_capabilities_get_t)(const struct device *dev,
                                             struct auxdisplay_capabilities *capabilities);

typedef int (*auxdisplay_clear_t)(const struct device *dev);

typedef int (*auxdisplay_brightness_get_t)(const struct device *dev, uint8_t *brightness);

typedef int (*auxdisplay_brightness_set_t)(const struct device *dev, uint8_t brightness);

typedef int (*auxdisplay_backlight_get_t)(const struct device *dev, uint8_t *backlight);

typedef int (*auxdisplay_backlight_set_t)(const struct device *dev, uint8_t backlight);

typedef int (*auxdisplay_is_busy_t)(const struct device *dev);

typedef int (*auxdisplay_custom_character_set_t)(const struct device *dev,
                                                 struct auxdisplay_character *character);

typedef int (*auxdisplay_write_t)(const struct device *dev, const uint8_t *data, uint16_t len);

typedef int (*auxdisplay_custom_command_t)(const struct device *dev,
                                           struct auxdisplay_custom_data *command);

typedef int (*auxdisplay_custom_indicator_set_t)(const struct device *dev,
                                                 uint8_t index, bool enable);

__subsystem struct auxdisplay_driver_api {
        auxdisplay_display_on_t display_on;
        auxdisplay_display_off_t display_off;
        auxdisplay_cursor_set_enabled_t cursor_set_enabled;
        auxdisplay_position_blinking_set_enabled_t position_blinking_set_enabled;
        auxdisplay_cursor_shift_set_t cursor_shift_set;
        auxdisplay_cursor_position_set_t cursor_position_set;
        auxdisplay_cursor_position_get_t cursor_position_get;
        auxdisplay_display_position_set_t display_position_set;
        auxdisplay_display_position_get_t display_position_get;
        auxdisplay_capabilities_get_t capabilities_get;
        auxdisplay_clear_t clear;
        auxdisplay_brightness_get_t brightness_get;
        auxdisplay_brightness_set_t brightness_set;
        auxdisplay_backlight_get_t backlight_get;
        auxdisplay_backlight_set_t backlight_set;
        auxdisplay_is_busy_t is_busy;
        auxdisplay_custom_character_set_t custom_character_set;
        auxdisplay_write_t write;
        auxdisplay_custom_command_t custom_command;
        auxdisplay_custom_indicator_set_t custom_indicator_set;
};


__syscall int auxdisplay_display_on(const struct device *dev);

static inline int z_impl_auxdisplay_display_on(const struct device *dev)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->display_on) {
                return -ENOSYS;
        }

        return api->display_on(dev);
}

__syscall int auxdisplay_display_off(const struct device *dev);

static inline int z_impl_auxdisplay_display_off(const struct device *dev)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->display_off) {
                return -ENOSYS;
        }

        return api->display_off(dev);
}

__syscall int auxdisplay_cursor_set_enabled(const struct device *dev,
                                            bool enabled);

static inline int z_impl_auxdisplay_cursor_set_enabled(const struct device *dev,
                                                       bool enabled)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->cursor_set_enabled) {
                return -ENOSYS;
        }

        return api->cursor_set_enabled(dev, enabled);
}

__syscall int auxdisplay_position_blinking_set_enabled(const struct device *dev,
                                                       bool enabled);

static inline int z_impl_auxdisplay_position_blinking_set_enabled(const struct device *dev,
                                                                  bool enabled)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->position_blinking_set_enabled) {
                return -ENOSYS;
        }

        return api->position_blinking_set_enabled(dev, enabled);
}

__syscall int auxdisplay_cursor_shift_set(const struct device *dev,
                                          uint8_t direction, bool display_shift);

static inline int z_impl_auxdisplay_cursor_shift_set(const struct device *dev,
                                                     uint8_t direction,
                                                     bool display_shift)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->cursor_shift_set) {
                return -ENOSYS;
        }

        if (direction >= AUXDISPLAY_DIRECTION_COUNT) {
                return -EINVAL;
        }

        return api->cursor_shift_set(dev, direction, display_shift);
}

__syscall int auxdisplay_cursor_position_set(const struct device *dev,
                                             enum auxdisplay_position type,
                                             int16_t x, int16_t y);

static inline int z_impl_auxdisplay_cursor_position_set(const struct device *dev,
                                                        enum auxdisplay_position type,
                                                        int16_t x, int16_t y)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->cursor_position_set) {
                return -ENOSYS;
        } else if (type >= AUXDISPLAY_POSITION_COUNT) {
                return -EINVAL;
        } else if (type == AUXDISPLAY_POSITION_ABSOLUTE && (x < 0 || y < 0)) {
                return -EINVAL;
        }

        return api->cursor_position_set(dev, type, x, y);
}

__syscall int auxdisplay_cursor_position_get(const struct device *dev,
                                             int16_t *x, int16_t *y);

static inline int z_impl_auxdisplay_cursor_position_get(const struct device *dev,
                                                        int16_t *x, int16_t *y)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->cursor_position_get) {
                return -ENOSYS;
        }

        return api->cursor_position_get(dev, x, y);
}

__syscall int auxdisplay_display_position_set(const struct device *dev,
                                              enum auxdisplay_position type,
                                              int16_t x, int16_t y);

static inline int z_impl_auxdisplay_display_position_set(const struct device *dev,
                                                         enum auxdisplay_position type,
                                                         int16_t x, int16_t y)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->display_position_set) {
                return -ENOSYS;
        } else if (type >= AUXDISPLAY_POSITION_COUNT) {
                return -EINVAL;
        } else if (type == AUXDISPLAY_POSITION_ABSOLUTE && (x < 0 || y < 0)) {
                return -EINVAL;
        }

        return api->display_position_set(dev, type, x, y);
}

__syscall int auxdisplay_display_position_get(const struct device *dev,
                                              int16_t *x, int16_t *y);

static inline int z_impl_auxdisplay_display_position_get(const struct device *dev,
                                                         int16_t *x, int16_t *y)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->display_position_get) {
                return -ENOSYS;
        }

        return api->display_position_get(dev, x, y);
}

__syscall int auxdisplay_capabilities_get(const struct device *dev,
                                          struct auxdisplay_capabilities *capabilities);

static inline int z_impl_auxdisplay_capabilities_get(const struct device *dev,
                                                     struct auxdisplay_capabilities *capabilities)
{
        return DEVICE_API_GET(auxdisplay, dev)->capabilities_get(dev, capabilities);
}

__syscall int auxdisplay_clear(const struct device *dev);

static inline int z_impl_auxdisplay_clear(const struct device *dev)
{
        return DEVICE_API_GET(auxdisplay, dev)->clear(dev);
}

__syscall int auxdisplay_brightness_get(const struct device *dev,
                                        uint8_t *brightness);

static inline int z_impl_auxdisplay_brightness_get(const struct device *dev,
                                                   uint8_t *brightness)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->brightness_get) {
                return -ENOSYS;
        }

        return api->brightness_get(dev, brightness);
}

__syscall int auxdisplay_brightness_set(const struct device *dev,
                                        uint8_t brightness);

static inline int z_impl_auxdisplay_brightness_set(const struct device *dev,
                                                   uint8_t brightness)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->brightness_set) {
                return -ENOSYS;
        }

        return api->brightness_set(dev, brightness);
}

__syscall int auxdisplay_backlight_get(const struct device *dev,
                                       uint8_t *backlight);

static inline int z_impl_auxdisplay_backlight_get(const struct device *dev,
                                                  uint8_t *backlight)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->backlight_get) {
                return -ENOSYS;
        }

        return api->backlight_get(dev, backlight);
}

__syscall int auxdisplay_backlight_set(const struct device *dev,
                                       uint8_t backlight);

static inline int z_impl_auxdisplay_backlight_set(const struct device *dev,
                                                  uint8_t backlight)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->backlight_set) {
                return -ENOSYS;
        }

        return api->backlight_set(dev, backlight);
}

__syscall int auxdisplay_is_busy(const struct device *dev);

static inline int z_impl_auxdisplay_is_busy(const struct device *dev)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->is_busy) {
                return -ENOSYS;
        }

        return api->is_busy(dev);
}

__syscall int auxdisplay_custom_character_set(const struct device *dev,
                                              struct auxdisplay_character *character);

static inline int z_impl_auxdisplay_custom_character_set(const struct device *dev,
                                                         struct auxdisplay_character *character)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->custom_character_set) {
                return -ENOSYS;
        }

        return api->custom_character_set(dev, character);
}

__syscall int auxdisplay_write(const struct device *dev, const uint8_t *data,
                               uint16_t len);

static inline int z_impl_auxdisplay_write(const struct device *dev,
                                          const uint8_t *data, uint16_t len)
{
        return DEVICE_API_GET(auxdisplay, dev)->write(dev, data, len);
}

__syscall int auxdisplay_custom_command(const struct device *dev,
                                        struct auxdisplay_custom_data *data);

static inline int z_impl_auxdisplay_custom_command(const struct device *dev,
                                                   struct auxdisplay_custom_data *data)
{
        const struct auxdisplay_driver_api *api = DEVICE_API_GET(auxdisplay, dev);

        if (!api->custom_command) {
                return -ENOSYS;
        }

        return api->custom_command(dev, data);
}

__syscall int auxdisplay_custom_indicator_set(const struct device *dev,
                                              uint8_t index, bool enable);

static inline int z_impl_auxdisplay_custom_indicator_set(const struct device *dev,
                                                         uint8_t index, bool enable)
{
        struct auxdisplay_driver_api *api = (struct auxdisplay_driver_api *)dev->api;

        if (!api->custom_indicator_set) {
                return -ENOSYS;
        }

        return api->custom_indicator_set(dev, index, enable);
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/auxdisplay.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_AUXDISPLAY_H_ */
```

## 47.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022-2023 Jamie McCrae。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 872 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_AUXDISPLAY_H_`。

## 47.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/auxdisplay_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [auxdisplay_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga78861a5414ac95e9ca77436c0b82acc2)
- [auxdisplay_position](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga98b0be37fc76df0ae4dec0bef6c94504)
- [AUXDISPLAY_POSITION_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404)
- [AUXDISPLAY_POSITION_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28)
- [AUXDISPLAY_POSITION_RELATIVE_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558)
- [AUXDISPLAY_POSITION_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23)
- [auxdisplay_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga5f95ac69e18091883e7121103014be10)
- [AUXDISPLAY_DIRECTION_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599)
- [AUXDISPLAY_DIRECTION_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352)
- [AUXDISPLAY_DIRECTION_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3)
- [auxdisplay_light](../driver_model_reference/P023_辅助显示器亮度.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [minimum](../driver_model_reference/P023_辅助显示器亮度.md#a4cd0c416ce77a45949feb90ae9f254a1)
- [maximum](../driver_model_reference/P023_辅助显示器亮度.md#a8f40f5fd3f825f1ee8c34891804cc003)
- [auxdisplay_capabilities](../driver_model_reference/P019_辅助显示器能力.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [columns](../driver_model_reference/P019_辅助显示器能力.md#ac0fc352a5799328211ae6f8c94cdcd7a)
- [rows](../driver_model_reference/P019_辅助显示器能力.md#af1bcdc27adb678ca4447614a22366aba)
- [mode](../driver_model_reference/P019_辅助显示器能力.md#a55ac50abb253e64e9fb7be6542801dc9)
- [brightness](../driver_model_reference/P019_辅助显示器能力.md#a15e3926754baaefffa1eff45573a59b1)
- [backlight](../driver_model_reference/P019_辅助显示器能力.md#ace4d7b099428e5f7164c3e9e318c1feb)
- [custom_characters](../driver_model_reference/P019_辅助显示器能力.md#a4b66412a2000fe09f30c555befbd11d0)
- [custom_character_width](../driver_model_reference/P019_辅助显示器能力.md#ad77f390f5a6bdbebabc703fdc77322a3)
- [custom_character_height](../driver_model_reference/P019_辅助显示器能力.md#adc88b37e9f73a98560099c94c8797741)
- [auxdisplay_custom_data](../driver_model_reference/P021_辅助显示器自定义数据.md)
- [data](../driver_model_reference/P021_辅助显示器自定义数据.md#acfd41be1569cc43bd09824c5e46b8d51)
- [len](../driver_model_reference/P021_辅助显示器自定义数据.md#ac995ecff9634acbc535a47b37134c6e1)
- [options](../driver_model_reference/P021_辅助显示器自定义数据.md#aa9c3b2af7c07e71e8cc5cd3eae058729)
- [auxdisplay_character](../driver_model_reference/P020_辅助显示器字符.md)
- [index](../driver_model_reference/P020_辅助显示器字符.md#a9f0bb424b9918e0f0c07c12eb4235677)
- [data](../driver_model_reference/P020_辅助显示器字符.md#a4b011716576201818278aa853bfe542e)
- [character_code](../driver_model_reference/P020_辅助显示器字符.md#a217dd562886158efec238649fb4ade04)
- [auxdisplay_display_on_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#gab1af1819efa902c0cf448a8fda8dd3dc)
- [device](../device_reference/P002_设备对象结构.md)
- [auxdisplay_display_off_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga3afc243389b001683f4ee5466678100d)
- [auxdisplay_cursor_set_enabled_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga266a31661ae5370e11b5f2eccb9d0a55)
- [auxdisplay_position_blinking_set_enabled_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga44a9dac2fea0b3eef65dd140e4f81105)
- [auxdisplay_cursor_shift_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga4c76fd207dcaf659481725416ec4de66)
- [auxdisplay_cursor_position_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#gac3679902422c05974d1262ab3e002169)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [auxdisplay_cursor_position_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga585ea33c13736d0500766c75c7145b48)
- [auxdisplay_display_position_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga15ddaa101a8399febff08e065d2b8878)
- [auxdisplay_display_position_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#gab9caf3b35dd3a22f6f5bbae6568a3e8d)
- [auxdisplay_capabilities_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#gafe80906adf675409f28cf95306dc7b0a)
- [auxdisplay_clear_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga6d95cc2416de90adf2613e33106e5405)
- [auxdisplay_brightness_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga095f0b08e482727a05973f4263d30093)
- [auxdisplay_brightness_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga7ad06a27ebff673599d1e92e7714bd20)
- [auxdisplay_backlight_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga7caf2a44b902627aec02bdcb2491b4a5)
- [auxdisplay_backlight_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#gadf5064c065e5c9cd417152ee2210dafb)
- [auxdisplay_is_busy_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#gaa0d87c8648d244816df62c29a6fb07e0)
- [auxdisplay_custom_character_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga25df80bc845a83f0bcdd2bc9083e595a)
- [auxdisplay_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga6971aee119d3806e161c2b6c5c0158d4)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [auxdisplay_custom_command_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga1d30d7d50f3052f31d73367034a78ac3)
- [auxdisplay_custom_indicator_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface__backend.html#ga59ee336b7cbbc56a8f02331caad74ba8)
- [auxdisplay_driver_api](../driver_model_reference/P022_辅助显示器驱动接口.md)
- [display_on](../driver_model_reference/P022_辅助显示器驱动接口.md#a2645cbcf10191d7d2c8e83b26c4bda7e)
- [display_off](../driver_model_reference/P022_辅助显示器驱动接口.md#a761472ca5d4f17d5f25922a6f3aa90d5)
- [cursor_set_enabled](../driver_model_reference/P022_辅助显示器驱动接口.md#a9e3301bce6a3a98be1f390981b683431)
- [position_blinking_set_enabled](../driver_model_reference/P022_辅助显示器驱动接口.md#a933054e57982b898f9544438d0d9829a)
- [cursor_shift_set](../driver_model_reference/P022_辅助显示器驱动接口.md#ab7d64386691f3df09c4268deb6b6f4fb)
- [cursor_position_set](../driver_model_reference/P022_辅助显示器驱动接口.md#a26c4c871f4b55ef671cb3efe5f45b819)
- [cursor_position_get](../driver_model_reference/P022_辅助显示器驱动接口.md#ad34aa550c542518f564c376777067bbd)
- [display_position_set](../driver_model_reference/P022_辅助显示器驱动接口.md#a125ae58199d088b69798476154993112)
- [display_position_get](../driver_model_reference/P022_辅助显示器驱动接口.md#a163a4be1fc6ee573d893488b33fca489)
- [capabilities_get](../driver_model_reference/P022_辅助显示器驱动接口.md#a838eacf860746e846602acf518ad56bb)
- [clear](../driver_model_reference/P022_辅助显示器驱动接口.md#ab646760f55a3b211ae49ac53c977f919)
- [brightness_get](../driver_model_reference/P022_辅助显示器驱动接口.md#a76d0849a3edb9e0d7ef892832f2bbeb2)
- [brightness_set](../driver_model_reference/P022_辅助显示器驱动接口.md#ac2b6300187110c4d7f778d2fdf97f46e)
- [backlight_get](../driver_model_reference/P022_辅助显示器驱动接口.md#a7bc90af6d38d9ea853cb8360360af143)
- [backlight_set](../driver_model_reference/P022_辅助显示器驱动接口.md#a375a125f4b1de808d9fd7cddc9013c21)
- [is_busy](../driver_model_reference/P022_辅助显示器驱动接口.md#a926903e94c19a7167d20d15fd4cdaa5d)
- [custom_character_set](../driver_model_reference/P022_辅助显示器驱动接口.md#afa89a0d6fdf07934abee57f46525c851)
- [write](../driver_model_reference/P022_辅助显示器驱动接口.md#a3a8ca50150440d30a6267f0494ab03e0)
- [custom_command](../driver_model_reference/P022_辅助显示器驱动接口.md#af65285a6e2311b590a8983575845c762)
- [custom_indicator_set](../driver_model_reference/P022_辅助显示器驱动接口.md#ad91b99ae3f81bea042ea45cc83624faf)
- [auxdisplay_display_on](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaffb3c1c41d810355fe2da3558ebba0c2)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [auxdisplay_display_off](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga625f399720417715090793c7f6d63f7e)
- [auxdisplay_cursor_set_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga7191475b362f728cc92eb07cb1f2ed00)
- [auxdisplay_position_blinking_set_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga7102ec9941f8b3131a18e4ff7b640241)
- [auxdisplay_cursor_shift_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gafb18729b4897cea83dbfc1c7241f5b2d)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [auxdisplay_cursor_position_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga9c6302789d9cc9e481dd7c54ef370988)
- [auxdisplay_cursor_position_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga37bd5403c876ff294be5ea72292de4b4)
- [auxdisplay_display_position_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga02e8e930203cfb1410752a0ffee9a34e)
- [auxdisplay_display_position_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga1f9e363765d715edb899901a14c54674)
- [auxdisplay_capabilities_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga4dd5cba56d4b90b77ae8ad02122ef81c)
- [auxdisplay_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaa5a643603353319946c823cc959b74b3)
- [auxdisplay_brightness_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga1f5be6fefc759607d2859a648a1fb3b8)
- [auxdisplay_brightness_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga34b31b70fdc57e33fc46f1048cc25e1a)
- [auxdisplay_backlight_get](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaf10ebdbe821894ccbeccb35bfa985fea)
- [auxdisplay_backlight_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga28aef24928543329c706513cc7e5b814)
- [auxdisplay_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga2af115a23f370e0770b3c998ecf0b96b)
- [auxdisplay_custom_character_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#gaf03a1068b0aed1f27ee9e2e61066da08)
- [auxdisplay_write](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga231dd862cda34ea4c0c8870675556f8d)
- [auxdisplay_custom_command](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga87064057ae857f81431e6e9f139a6aaa)
- [auxdisplay_custom_indicator_set](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html#ga7930b8287b2cefa08af90a755fd5651c)
- [api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [auxdisplay_capabilities::brightness](../driver_model_reference/P019_辅助显示器能力.md#a15e3926754baaefffa1eff45573a59b1)
- [auxdisplay_capabilities::custom_characters](../driver_model_reference/P019_辅助显示器能力.md#a4b66412a2000fe09f30c555befbd11d0)
- [auxdisplay_capabilities::mode](../driver_model_reference/P019_辅助显示器能力.md#a55ac50abb253e64e9fb7be6542801dc9)
- [auxdisplay_capabilities::columns](../driver_model_reference/P019_辅助显示器能力.md#ac0fc352a5799328211ae6f8c94cdcd7a)
- [auxdisplay_capabilities::backlight](../driver_model_reference/P019_辅助显示器能力.md#ace4d7b099428e5f7164c3e9e318c1feb)
- [auxdisplay_capabilities::custom_character_width](../driver_model_reference/P019_辅助显示器能力.md#ad77f390f5a6bdbebabc703fdc77322a3)
- [auxdisplay_capabilities::custom_character_height](../driver_model_reference/P019_辅助显示器能力.md#adc88b37e9f73a98560099c94c8797741)
- [auxdisplay_capabilities::rows](../driver_model_reference/P019_辅助显示器能力.md#af1bcdc27adb678ca4447614a22366aba)
- [auxdisplay_character::character_code](../driver_model_reference/P020_辅助显示器字符.md#a217dd562886158efec238649fb4ade04)
- [auxdisplay_character::data](../driver_model_reference/P020_辅助显示器字符.md#a4b011716576201818278aa853bfe542e)
- [auxdisplay_character::index](../driver_model_reference/P020_辅助显示器字符.md#a9f0bb424b9918e0f0c07c12eb4235677)
- [auxdisplay_custom_data::options](../driver_model_reference/P021_辅助显示器自定义数据.md#aa9c3b2af7c07e71e8cc5cd3eae058729)
- [auxdisplay_custom_data::len](../driver_model_reference/P021_辅助显示器自定义数据.md#ac995ecff9634acbc535a47b37134c6e1)
- [auxdisplay_custom_data::data](../driver_model_reference/P021_辅助显示器自定义数据.md#acfd41be1569cc43bd09824c5e46b8d51)
- [auxdisplay_driver_api::display_position_set](../driver_model_reference/P022_辅助显示器驱动接口.md#a125ae58199d088b69798476154993112)
- [auxdisplay_driver_api::display_position_get](../driver_model_reference/P022_辅助显示器驱动接口.md#a163a4be1fc6ee573d893488b33fca489)
- [auxdisplay_driver_api::display_on](../driver_model_reference/P022_辅助显示器驱动接口.md#a2645cbcf10191d7d2c8e83b26c4bda7e)
- [auxdisplay_driver_api::cursor_position_set](../driver_model_reference/P022_辅助显示器驱动接口.md#a26c4c871f4b55ef671cb3efe5f45b819)
- [auxdisplay_driver_api::backlight_set](../driver_model_reference/P022_辅助显示器驱动接口.md#a375a125f4b1de808d9fd7cddc9013c21)
- [auxdisplay_driver_api::write](../driver_model_reference/P022_辅助显示器驱动接口.md#a3a8ca50150440d30a6267f0494ab03e0)
- [auxdisplay_driver_api::display_off](../driver_model_reference/P022_辅助显示器驱动接口.md#a761472ca5d4f17d5f25922a6f3aa90d5)
- [auxdisplay_driver_api::brightness_get](../driver_model_reference/P022_辅助显示器驱动接口.md#a76d0849a3edb9e0d7ef892832f2bbeb2)
- [auxdisplay_driver_api::backlight_get](../driver_model_reference/P022_辅助显示器驱动接口.md#a7bc90af6d38d9ea853cb8360360af143)
- [auxdisplay_driver_api::capabilities_get](../driver_model_reference/P022_辅助显示器驱动接口.md#a838eacf860746e846602acf518ad56bb)
- [auxdisplay_driver_api::is_busy](../driver_model_reference/P022_辅助显示器驱动接口.md#a926903e94c19a7167d20d15fd4cdaa5d)
- [auxdisplay_driver_api::position_blinking_set_enabled](../driver_model_reference/P022_辅助显示器驱动接口.md#a933054e57982b898f9544438d0d9829a)
- [auxdisplay_driver_api::cursor_set_enabled](../driver_model_reference/P022_辅助显示器驱动接口.md#a9e3301bce6a3a98be1f390981b683431)
- [auxdisplay_driver_api::clear](../driver_model_reference/P022_辅助显示器驱动接口.md#ab646760f55a3b211ae49ac53c977f919)
- [auxdisplay_driver_api::cursor_shift_set](../driver_model_reference/P022_辅助显示器驱动接口.md#ab7d64386691f3df09c4268deb6b6f4fb)
- [auxdisplay_driver_api::brightness_set](../driver_model_reference/P022_辅助显示器驱动接口.md#ac2b6300187110c4d7f778d2fdf97f46e)
- [auxdisplay_driver_api::cursor_position_get](../driver_model_reference/P022_辅助显示器驱动接口.md#ad34aa550c542518f564c376777067bbd)
- [auxdisplay_driver_api::custom_indicator_set](../driver_model_reference/P022_辅助显示器驱动接口.md#ad91b99ae3f81bea042ea45cc83624faf)
- [auxdisplay_driver_api::custom_command](../driver_model_reference/P022_辅助显示器驱动接口.md#af65285a6e2311b590a8983575845c762)
- [auxdisplay_driver_api::custom_character_set](../driver_model_reference/P022_辅助显示器驱动接口.md#afa89a0d6fdf07934abee57f46525c851)
- [auxdisplay_light::minimum](../driver_model_reference/P023_辅助显示器亮度.md#a4cd0c416ce77a45949feb90ae9f254a1)
- [auxdisplay_light::maximum](../driver_model_reference/P023_辅助显示器亮度.md#a8f40f5fd3f825f1ee8c34891804cc003)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [device::api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

---

[上一章](P046_autohandler.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P048_avrcp_cover_art.h_源码浏览.md)
