---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-2
title: audio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_audio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)。

## 2.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="foldopen00121"></a>
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
<a id="foldopen00148"></a>
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
<a id="foldopen00163"></a>
<a id="l00163"></a>
<a id="l00169"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="foldopen00202"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="foldopen00218"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="foldopen00230"></a>
<a id="l00230"></a>
<a id="l00236"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00248"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="foldopen00320"></a>
<a id="l00320"></a>
<a id="l00327"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="foldopen00344"></a>
<a id="l00344"></a>
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
<a id="l00364"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00821"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00890"></a>
<a id="l00891"></a>
<a id="l00892"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00948"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="l00966"></a>
<a id="l00967"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00994"></a>
<a id="l00995"></a>
<a id="l00996"></a>
<a id="l01009"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01023"></a>
<a id="l01024"></a>
<a id="l01026"></a>
<a id="l01036"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01063"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="l01066"></a>
<a id="l01078"></a>
<a id="l01079"></a>
<a id="l01080"></a>
<a id="l01092"></a>
<a id="l01093"></a>
<a id="l01104"></a>
<a id="l01105"></a>
<a id="l01106"></a>
<a id="l01117"></a>
<a id="l01118"></a>
<a id="l01129"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="l01146"></a>
<a id="l01157"></a>
<a id="l01158"></a>
<a id="l01159"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01173"></a>
<a id="l01174"></a>
<a id="l01185"></a>
<a id="l01186"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01201"></a>
<a id="l01202"></a>
<a id="l01203"></a>
<a id="l01214"></a>
<a id="l01215"></a>
<a id="l01216"></a>
<a id="l01228"></a>
<a id="l01229"></a>
<a id="l01230"></a>
<a id="l01243"></a>
<a id="l01244"></a>
<a id="l01245"></a>
<a id="l01246"></a>
<a id="l01258"></a>
<a id="l01259"></a>
<a id="l01260"></a>
<a id="l01273"></a>
<a id="l01274"></a>
<a id="l01285"></a>
<a id="l01286"></a>
<a id="l01287"></a>
<a id="l01300"></a>
<a id="l01301"></a>
<a id="l01312"></a>
<a id="l01313"></a>
<a id="l01314"></a>
<a id="l01327"></a>
<a id="l01328"></a>
<a id="l01329"></a>
<a id="l01341"></a>
<a id="l01342"></a>
<a id="l01343"></a>
<a id="l01357"></a>
<a id="l01358"></a>
<a id="l01359"></a>
<a id="l01370"></a>
<a id="l01371"></a>
<a id="l01372"></a>
<a id="l01385"></a>
<a id="l01386"></a>
<a id="l01387"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01414"></a>
<a id="l01415"></a>
<a id="l01426"></a>
<a id="l01427"></a>
<a id="l01428"></a>
<a id="l01441"></a>
<a id="l01442"></a>
<a id="l01443"></a>
<a id="l01455"></a>
<a id="l01456"></a>
<a id="l01457"></a>
<a id="l01458"></a>
<a id="l01471"></a>
<a id="l01472"></a>
<a id="l01483"></a>
<a id="l01484"></a>
<a id="l01485"></a>
<a id="l01497"></a>
<a id="l01498"></a>
<a id="l01499"></a>
<a id="l01509"></a>
<a id="l01510"></a>
<a id="l01511"></a>
<a id="l01524"></a>
<a id="l01525"></a>
<a id="l01526"></a>
<a id="l01537"></a>
<a id="l01538"></a>
<a id="l01539"></a>
<a id="l01552"></a>
<a id="l01553"></a>
<a id="l01554"></a>
<a id="l01570"></a>
<a id="l01571"></a>
<a id="l01572"></a>
<a id="l01585"></a>
<a id="l01586"></a>
<a id="l01587"></a>
<a id="l01599"></a>
<a id="l01600"></a>
<a id="l01601"></a>
<a id="l01614"></a>
<a id="l01615"></a>
<a id="l01616"></a>
<a id="l01628"></a>
<a id="l01629"></a>
<a id="l01630"></a>
<a id="l01632"></a>
<a id="l01641"></a>
<a id="foldopen01651"></a>
<a id="l01651"></a>
<a id="l01652"></a>
<a id="l01653"></a>
<a id="l01654"></a>
<a id="l01655"></a>
<a id="l01656"></a>
<a id="l01657"></a>
<a id="l01658"></a>
<a id="l01659"></a>
<a id="l01660"></a>
<a id="l01661"></a>
<a id="l01662"></a>
<a id="l01663"></a>
<a id="l01664"></a>
<a id="l01665"></a>
<a id="l01666"></a>
<a id="l01667"></a>
<a id="l01668"></a>
<a id="l01669"></a>
<a id="l01670"></a>
<a id="l01671"></a>
<a id="l01672"></a>
<a id="l01673"></a>
<a id="l01674"></a>
<a id="l01675"></a>
<a id="l01676"></a>
<a id="l01677"></a>
<a id="l01678"></a>
<a id="l01679"></a>
<a id="l01680"></a>
<a id="l01681"></a>
<a id="l01682"></a>
<a id="l01683"></a>
<a id="l01684"></a>
<a id="foldopen01692"></a>
<a id="l01692"></a>
<a id="l01693"></a>
<a id="l01694"></a>
<a id="l01695"></a>
<a id="l01696"></a>
<a id="l01697"></a>
<a id="l01698"></a>
<a id="l01699"></a>
<a id="l01700"></a>
<a id="l01701"></a>
<a id="l01702"></a>
<a id="l01703"></a>
<a id="l01704"></a>
<a id="l01705"></a>
<a id="l01706"></a>
<a id="l01707"></a>
<a id="l01708"></a>
<a id="l01709"></a>
<a id="l01710"></a>
<a id="l01711"></a>
<a id="l01712"></a>
<a id="l01713"></a>
<a id="l01714"></a>
<a id="l01715"></a>
<a id="l01716"></a>
<a id="l01717"></a>
<a id="l01718"></a>
<a id="l01719"></a>
<a id="l01720"></a>
<a id="l01721"></a>
<a id="l01722"></a>
<a id="l01723"></a>
<a id="l01724"></a>
<a id="l01725"></a>
<a id="l01726"></a>
<a id="l01727"></a>
<a id="l01728"></a>
<a id="l01729"></a>
<a id="l01730"></a>
<a id="l01731"></a>
<a id="foldopen01739"></a>
<a id="l01739"></a>
<a id="l01740"></a>
<a id="l01741"></a>
<a id="l01742"></a>
<a id="l01743"></a>
<a id="l01744"></a>
<a id="l01745"></a>
<a id="l01746"></a>
<a id="l01747"></a>
<a id="l01748"></a>
<a id="l01749"></a>
<a id="l01750"></a>
<a id="foldopen01760"></a>
<a id="l01760"></a>
<a id="l01761"></a>
<a id="l01762"></a>
<a id="l01763"></a>
<a id="l01764"></a>
<a id="l01765"></a>
<a id="l01766"></a>
<a id="l01767"></a>
<a id="l01768"></a>
<a id="l01769"></a>
<a id="l01770"></a>
<a id="l01771"></a>
<a id="l01772"></a>
<a id="l01773"></a>
<a id="l01774"></a>
<a id="l01775"></a>
<a id="l01776"></a>
<a id="l01777"></a>
<a id="l01778"></a>
<a id="l01779"></a>
<a id="l01780"></a>
<a id="l01781"></a>
<a id="l01782"></a>
<a id="l01783"></a>
<a id="l01784"></a>
<a id="l01785"></a>
<a id="l01786"></a>
<a id="l01787"></a>
<a id="l01788"></a>
<a id="l01789"></a>
<a id="l01790"></a>
<a id="l01791"></a>
<a id="l01792"></a>
<a id="l01793"></a>
<a id="l01803"></a>
<a id="foldopen01804"></a>
<a id="l01804"></a>
<a id="l01805"></a>
<a id="l01806"></a>
<a id="l01807"></a>
<a id="l01808"></a>
<a id="l01809"></a>
<a id="l01810"></a>
<a id="l01811"></a>
<a id="l01812"></a>
<a id="l01813"></a>
<a id="l01814"></a>
<a id="l01815"></a>
<a id="l01816"></a>
<a id="l01817"></a>
<a id="l01818"></a>
<a id="l01819"></a>
<a id="l01829"></a>
<a id="foldopen01830"></a>
<a id="l01830"></a>
<a id="l01831"></a>
<a id="l01832"></a>
<a id="l01833"></a>
<a id="l01834"></a>
<a id="l01835"></a>
<a id="l01836"></a>
<a id="l01837"></a>
<a id="l01838"></a>
<a id="l01839"></a>
<a id="l01840"></a>
<a id="l01841"></a>
<a id="l01842"></a>
<a id="l01843"></a>
<a id="l01844"></a>
<a id="l01845"></a>
<a id="l01846"></a>
<a id="l01847"></a>
<a id="l01848"></a>
<a id="l01849"></a>
<a id="l01850"></a>
<a id="l01851"></a>
<a id="l01852"></a>
<a id="l01853"></a>
<a id="foldopen01863"></a>
<a id="l01863"></a>
<a id="l01864"></a>
<a id="l01865"></a>
<a id="l01866"></a>
<a id="l01867"></a>
<a id="l01868"></a>
<a id="l01869"></a>
<a id="l01870"></a>
<a id="l01871"></a>
<a id="l01872"></a>
<a id="l01873"></a>
<a id="l01874"></a>
<a id="l01875"></a>
<a id="l01876"></a>
<a id="l01877"></a>
<a id="l01878"></a>
<a id="l01879"></a>
<a id="l01880"></a>
<a id="l01881"></a>
<a id="l01882"></a>
<a id="l01883"></a>
<a id="l01884"></a>
<a id="l01885"></a>
<a id="l01886"></a>
<a id="l01887"></a>
<a id="l01888"></a>
<a id="l01889"></a>
<a id="l01890"></a>
<a id="l01891"></a>
<a id="l01892"></a>
<a id="l01893"></a>
<a id="l01894"></a>
<a id="l01895"></a>
<a id="l01896"></a>
<a id="l01897"></a>
<a id="l01898"></a>
<a id="l01899"></a>
<a id="l01900"></a>
<a id="l01901"></a>
<a id="l01902"></a>
<a id="l01903"></a>
<a id="l01904"></a>
<a id="l01905"></a>
<a id="l01906"></a>
<a id="l01907"></a>
<a id="l01908"></a>
<a id="l01909"></a>
<a id="l01910"></a>
<a id="l01911"></a>
<a id="l01912"></a>
<a id="l01913"></a>
<a id="l01914"></a>
<a id="l01915"></a>
<a id="l01916"></a>
<a id="l01917"></a>
<a id="l01918"></a>
<a id="l01919"></a>
<a id="l01920"></a>
<a id="l01921"></a>
<a id="l01922"></a>
<a id="l01923"></a>
<a id="l01924"></a>
<a id="l01925"></a>
<a id="l01926"></a>
<a id="l01927"></a>
<a id="l01928"></a>
<a id="l01930"></a>
<a id="l01931"></a>
<a id="l01932"></a>
<a id="l01933"></a>
<a id="l01935"></a>
<a id="l01936"></a>
<a id="aassigned__numbers_8h_html"></a>
<a id="aatomic_8h_html"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="abuf_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="adata_8h_html"></a>
<a id="agatt_8h_html"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga16d403ec4db7be997682331ad365ff5f"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga207fbf0fbca9b24cba02c7f1d184e7f5"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga61230848c02098352320fe751332c4e8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga6d4aff1f93dc0b902e4b5d1355f15760"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga83701b5eadfcbc9b84dc0b1a85ebeb74"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga8e99fb678cc011bb8c9f6e1858bae0d7"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga9230ec4d7518bd243207ba2decb1a974"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gaafc1106d5d305874ee2f540c850ff5b4"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gab53d0dd62bceff97cf8eed7d8cf80354"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gae695b5d17359967703f2509db1671fa5"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gaf37e8e19f956afb3c3a413cbaa1a21f5"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gaf58823a56eb36cfd22e582ab1ea3d015"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gafb379ffa88388cc1397960155bbb2ab3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a890d2723c8b23127ab4a1cb8b6b1118d"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5"></a>
<a id="agroup__bt__audio__codec__cap_html_ga00a8ad22713dab761c81d1b8481c037d"></a>
<a id="agroup__bt__audio__codec__cap_html_ga0c2c816b0b2b85aa5dd38f21caceea40"></a>
<a id="agroup__bt__audio__codec__cap_html_ga12336de7d908bda94427caee4dc080e0"></a>
<a id="agroup__bt__audio__codec__cap_html_ga194d938896ee65601bdce96d68c84885"></a>
<a id="agroup__bt__audio__codec__cap_html_ga1f06789782541beab9aab4914f91bb57"></a>
<a id="agroup__bt__audio__codec__cap_html_ga1fdfd8c36f4131bcf4ffd2b7f176b631"></a>
<a id="agroup__bt__audio__codec__cap_html_ga3095dea36e60e75cbfe786d3c2f11866"></a>
<a id="agroup__bt__audio__codec__cap_html_ga3346db1f59cb35b9b9e5255424adb6e4"></a>
<a id="agroup__bt__audio__codec__cap_html_ga33725c3b2c06d6c22030bb5a77d702b0"></a>
<a id="agroup__bt__audio__codec__cap_html_ga3785bc41f56f8f2a09248396dadb31da"></a>
<a id="agroup__bt__audio__codec__cap_html_ga3c8df3fe79f0bb96c4e15e7c2502bf89"></a>
<a id="agroup__bt__audio__codec__cap_html_ga40848f5375d1e58622c580112c282f2e"></a>
<a id="agroup__bt__audio__codec__cap_html_ga43d2ec3a4d621c26843de82db7fd2189"></a>
<a id="agroup__bt__audio__codec__cap_html_ga461add2808a1eca8993222d2b31d5a5f"></a>
<a id="agroup__bt__audio__codec__cap_html_ga4f1ea56f2c1c21420f078d35081ceee5"></a>
<a id="agroup__bt__audio__codec__cap_html_ga53e5df6cc4cfbed12b59a6a506657772"></a>
<a id="agroup__bt__audio__codec__cap_html_ga555db1eff71a3bc79a5bcb959c0198cc"></a>
<a id="agroup__bt__audio__codec__cap_html_ga5c2ecbb4d0cef26dd2cc5d023e70a163"></a>
<a id="agroup__bt__audio__codec__cap_html_ga5cc7f360049c38c8de631ea33dbc44ab"></a>
<a id="agroup__bt__audio__codec__cap_html_ga5e267dfad978cd3d52be9c31a4fac0be"></a>
<a id="agroup__bt__audio__codec__cap_html_ga63d5e083f03ec06939ee1cd0355c8c2a"></a>
<a id="agroup__bt__audio__codec__cap_html_ga69aecd7e98f90a5162ff8ea3373b43d4"></a>
<a id="agroup__bt__audio__codec__cap_html_ga7fe0d4553d6accf5c89645cbf86149bf"></a>
<a id="agroup__bt__audio__codec__cap_html_ga88bb1da63b7ea0f95dd236aa1024cfb8"></a>
<a id="agroup__bt__audio__codec__cap_html_ga88ee657b5bd3f847bb75c9620ddb142f"></a>
<a id="agroup__bt__audio__codec__cap_html_gaa1d382b4fa53f7cbe8426df53a3317ce"></a>
<a id="agroup__bt__audio__codec__cap_html_gaa1dbf81c437c983af0144bf62433666c"></a>
<a id="agroup__bt__audio__codec__cap_html_gaa949089f2c6c143041e6cb61338e0ddc"></a>
<a id="agroup__bt__audio__codec__cap_html_gaaa8c6783241b1b70349354b3e36c696c"></a>
<a id="agroup__bt__audio__codec__cap_html_gab34d0369ce08efcd407d33956d32632e"></a>
<a id="agroup__bt__audio__codec__cap_html_gab4ccc7cb7d779acb20185ae808dd8bbe"></a>
<a id="agroup__bt__audio__codec__cap_html_gab8c80a0f55041f026d453fd88cdeb727"></a>
<a id="agroup__bt__audio__codec__cap_html_gabc9962212ad65339ff02ba1389d5f9f8"></a>
<a id="agroup__bt__audio__codec__cap_html_gac00aabc7329027852a7caf5cdff2bc26"></a>
<a id="agroup__bt__audio__codec__cap_html_gac0655c0bd6552ab8a265076d7d0cd1b2"></a>
<a id="agroup__bt__audio__codec__cap_html_gac1c42460cd3c55bbfbd467f84ab2d78d"></a>
<a id="agroup__bt__audio__codec__cap_html_gac3bf5dd414271bb1dcbc6590994cff6b"></a>
<a id="agroup__bt__audio__codec__cap_html_gacd3de0306a22d1a1d9ba09b4ac4f4e09"></a>
<a id="agroup__bt__audio__codec__cap_html_gadb39b0ee1f65cdd2457fdf2c3142c040"></a>
<a id="agroup__bt__audio__codec__cap_html_gaf6b2717823f9f3136237ed6a6515449e"></a>
<a id="agroup__bt__audio__codec__cap_html_gafb631b55b69b256c60b9cf3c7f418ff8"></a>
<a id="agroup__bt__audio__codec__cap_html_gafbb0d6282d989e8bc70caada2845b337"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga03284b8474d65443d7ecc8bdfc6f04c6"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga0782a3d9254fb76b441c6c2492571556"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga0fd6e6baf1b4f22d60768aaed6f42e8e"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga1f76f82bff63b876eb761a0bf0377428"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga225e05df1f0d1efb709c972187901495"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga22ae14fce65b757e31f391c4bdcae328"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga2ca9e616d20d7513c60ce905f046ac7b"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga2dd3afe41b22e989fb46614f89550007"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga2e557fe726a49dc99754da16f7cc60af"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga3e24c2ba8de502600e647cb2f84e3ec4"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga4a4982e3bd0e8c944b584196ef146f6c"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga4cc4e1bb941206e7f1541a57fc92b8e9"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga4f5cbacebedc8d7df02d1c47b140bf3c"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga503be053422217502d6108b045791e02"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga55e3cbaeacf15fcb1f24a16eb28db99c"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga59716b95fcea3404ff8c078564b0e29c"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga5cd2af1bb44c6eb5bafe824f005a77f0"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga5d80babcd6f381014e1fae98a755e1d3"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga66143aa7dcc726e06a12660b8f90fc5a"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga67d83559cbe6cfab235f2e588cbc398c"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga6935d1c40b3178b0c8fa877ee93d1e53"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga6bdbc0a0b929fdbdc75db479aec858df"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga707c679db0193197b56acabfb08f8d1f"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga7d8306f98cb00f06e68a1df417825f0d"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga866cdec28194056dc9e274d0436b45c2"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga93052db14c857097e7cf9abc34b7fc39"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga99163729034e816eaef7195505d5ae20"></a>
<a id="agroup__bt__audio__codec__cfg_html_ga99ab4f6d2a18f2a9b4e3da47f63fc9e0"></a>
<a id="agroup__bt__audio__codec__cfg_html_gaa0f9b9f608c7af881d5a928a3ae397b2"></a>
<a id="agroup__bt__audio__codec__cfg_html_gab10f22938780530b1d1b95695382902e"></a>
<a id="agroup__bt__audio__codec__cfg_html_gab40bad609f17d24e7e0e9ffcebe4e912"></a>
<a id="agroup__bt__audio__codec__cfg_html_gab46f830daa1d9a907f47eb2a9eed7337"></a>
<a id="agroup__bt__audio__codec__cfg_html_gab5d8b5877de4fe16c0e06a1d4f0d15ce"></a>
<a id="agroup__bt__audio__codec__cfg_html_gac119989d5dcfa36becf4edd0ae7c6138"></a>
<a id="agroup__bt__audio__codec__cfg_html_gac9cf20bafbe24b34034bfb6ee7aaf03e"></a>
<a id="agroup__bt__audio__codec__cfg_html_gad3857d0ca008854df5966501caa261ba"></a>
<a id="agroup__bt__audio__codec__cfg_html_gad8525a57d35e3e34ea591f7e20e2512d"></a>
<a id="agroup__bt__audio__codec__cfg_html_gadba0723f9d8a9546b659fba139051374"></a>
<a id="agroup__bt__audio__codec__cfg_html_gade9cb53287ab3356fb57ba8a454a3aad"></a>
<a id="agroup__bt__audio__codec__cfg_html_gae712e0f8e84aeb4ad2528da34907e29d"></a>
<a id="agroup__bt__audio__codec__cfg_html_gae98335e87394a491b4a311d867a5e32d"></a>
<a id="agroup__bt__audio__codec__cfg_html_gaea087663426a49bb6ff4859800aecb84"></a>
<a id="agroup__bt__audio__codec__cfg_html_gaede61b65d2037c7fbf6c4c4e090990be"></a>
<a id="agroup__bt__audio__codec__cfg_html_gaf0eecb02a05f0cc2b75ae9fb32c03913"></a>
<a id="agroup__bt__audio__codec__cfg_html_gaf869e7ce0c9dd467fb03e8503d36c58a"></a>
<a id="agroup__bt__audio__codec__cfg_html_gafbbcd69fac18ed0201a5e0156209b049"></a>
<a id="agroup__bt__audio__to__str_html_ga1dd5865429e2438e0d4f88e891eda975"></a>
<a id="agroup__bt__audio__to__str_html_ga26436fc678423ff1cf3543d381359d0f"></a>
<a id="agroup__bt__audio__to__str_html_ga6926c4e8bda0874769177a903276c072"></a>
<a id="agroup__bt__audio__to__str_html_ga6b9cc74dafcf03056862ae9823bce58d"></a>
<a id="agroup__bt__audio__to__str_html_ga795742ed8d91e2b675fbcdaeee7a71ec"></a>
<a id="agroup__bt__audio__to__str_html_gaa1b9f7166fd6e6797da65d9537357324"></a>
<a id="agroup__bt__audio__to__str_html_gadd3bac4f1f1b334cb60f5783fdc15c14"></a>
<a id="agroup__bt__audio_html_ga5bd899fb5e4d844058184913866e462f"></a>
<a id="agroup__bt__audio_html_ga62108a3dcc3e35f7b31a99f7a33679e6"></a>
<a id="agroup__bt__audio_html_ga640af4e254e73f5c4646e9be4e99f3d1"></a>
<a id="agroup__bt__audio_html_ga87415f8dddd38b3f5641c96e9722a44a"></a>
<a id="agroup__bt__audio_html_gab6e5f793d514626deca21940d35d8f21"></a>
<a id="agroup__bt__audio_html_gabbd1b9c46caa9a19de6c95b08c31e5b5"></a>
<a id="agroup__bt__audio_html_gaf629628fc13be7a1693ceb1d32b743f2"></a>
<a id="agroup__bt__audio_html_gafd8574b16141162c95653f0aa2bf6ff7"></a>
<a id="agroup__bt__audio_html_gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8"></a>
<a id="agroup__bt__audio_html_gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c"></a>
<a id="agroup__bt__audio_html_gga62108a3dcc3e35f7b31a99f7a33679e6a93ec0567d248d4cfc9cd60c26cbc50ef"></a>
<a id="agroup__bt__audio_html_gga62108a3dcc3e35f7b31a99f7a33679e6a971aeaf3e2df14f5ed75965a31188f80"></a>
<a id="agroup__bt__audio_html_gga62108a3dcc3e35f7b31a99f7a33679e6aec4cf0f851e64e034ead8a075c93eda8"></a>
<a id="agroup__bt__audio_html_gga640af4e254e73f5c4646e9be4e99f3d1a0b7e1713ff85524953baeb4e7e085d96"></a>
<a id="agroup__bt__audio_html_gga640af4e254e73f5c4646e9be4e99f3d1a3793a0bbbb7daa399086ce7db0a24a38"></a>
<a id="agroup__bt__audio_html_gga640af4e254e73f5c4646e9be4e99f3d1acd5c965423632650196768589a75bd95"></a>
<a id="ahci_8h_html"></a>
<a id="aiso_8h_html"></a>
<a id="alc3_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__audio__codec__cap_html"></a>
<a id="astructbt__audio__codec__cap_html_a3b91269e16a3d63b3128a527caa5e3ff"></a>
<a id="astructbt__audio__codec__cap_html_a455638aac9167d288a1e7a9fccabc49d"></a>
<a id="astructbt__audio__codec__cap_html_a763222d12a87958a5ba806303f98829a"></a>
<a id="astructbt__audio__codec__cap_html_a822a06f815091cc580ca2e5bbb3126f7"></a>
<a id="astructbt__audio__codec__cap_html_a900a77db09e72de61d4ff652c6dbb10b"></a>
<a id="astructbt__audio__codec__cap_html_acec4f5e31752d81d4dbf441223e7f44c"></a>
<a id="astructbt__audio__codec__cap_html_acf3e22c6db1533fff7015acbc7eca196"></a>
<a id="astructbt__audio__codec__cap_html_ae3892731e7ca05f3ec426c70f0d9e1a9"></a>
<a id="astructbt__audio__codec__cap_html_afe806521d5aac36e9f6c6a0598500a8f"></a>
<a id="astructbt__audio__codec__cfg_html"></a>
<a id="astructbt__audio__codec__cfg_html_a1e69a5c017e9571b50aba721f86876fb"></a>
<a id="astructbt__audio__codec__cfg_html_a2996ab3f6ae1cab09ff5e3329b42468e"></a>
<a id="astructbt__audio__codec__cfg_html_a4f84974ea14b773ad8e2fd7c0ffa0c7f"></a>
<a id="astructbt__audio__codec__cfg_html_a571a8b875dd0acac50e82620dc6d9aab"></a>
<a id="astructbt__audio__codec__cfg_html_a664e21bcd6002b21d4b1b53d866db32d"></a>
<a id="astructbt__audio__codec__cfg_html_a8a5a789e9993a48ce4c83a2156c1f43c"></a>
<a id="astructbt__audio__codec__cfg_html_a9386056bb02908407c9e3aad48abbd87"></a>
<a id="astructbt__audio__codec__cfg_html_a9e2c8081950a0830ffc270245ab308c1"></a>
<a id="astructbt__audio__codec__cfg_html_aa2f99ec31ff3eb9b7b738bc8a1170f20"></a>
<a id="astructbt__audio__codec__cfg_html_aa71d0e75b36f6dc664fdcd2e092f8d57"></a>
<a id="astructbt__audio__codec__cfg_html_ad3709d5321f6faeb392452cb3b21023b"></a>
<a id="astructbt__audio__codec__octets__per__codec__frame_html"></a>
<a id="astructbt__audio__codec__octets__per__codec__frame_html_aa8b234fa137273cd16230ebabc5f8ef4"></a>
<a id="astructbt__audio__codec__octets__per__codec__frame_html_ae09686799077b13e78b856b1e7e63b6a"></a>
<a id="astructbt__data_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2020 Intel Corporation
 * Copyright (c) 2020-2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_AUDIO_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_AUDIO_H_


#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/audio/lc3.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/buf.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/data.h>
#include <zephyr/bluetooth/gatt.h>
#include <zephyr/bluetooth/hci.h>
#include <zephyr/bluetooth/iso.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_AUDIO_BROADCAST_ID_SIZE               3U
#define BT_AUDIO_BROADCAST_ID_MAX                0xFFFFFFU
#define BT_AUDIO_PD_PREF_NONE                    0x000000U
#define BT_AUDIO_PD_MAX                          0xFFFFFFU
#define BT_AUDIO_RTN_PREF_NONE                   0xFFU

#define BT_AUDIO_LANG_SIZE 3U

#define BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT(...)                                                 \
        ((enum bt_audio_codec_cap_chan_count)((FOR_EACH(BIT, (|), __VA_ARGS__)) >> 1))

struct bt_audio_codec_octets_per_codec_frame {
        uint16_t min;
        uint16_t max;
};

#define BT_AUDIO_METADATA_TYPE_IS_KNOWN(_type)                                                     \
        (IN_RANGE((_type), BT_AUDIO_METADATA_TYPE_PREF_CONTEXT,                                    \
                  BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE) ||                                   \
         (_type) == BT_AUDIO_METADATA_TYPE_EXTENDED || (_type) == BT_AUDIO_METADATA_TYPE_VENDOR)

#define BT_AUDIO_UNICAST_ANNOUNCEMENT_GENERAL    0x00U
#define BT_AUDIO_UNICAST_ANNOUNCEMENT_TARGETED   0x01U

#define BT_AUDIO_CODEC_DATA(_type, _bytes...)                                                      \
        (sizeof((uint8_t)_type) + sizeof((uint8_t[]){_bytes})), (_type), _bytes

#define BT_AUDIO_CODEC_CFG(_id, _cid, _vid, _data, _meta)                                          \
        ((struct bt_audio_codec_cfg){                                                              \
                /* Use HCI data path as default, can be overwritten by application */              \
                .path_id = BT_ISO_DATA_PATH_HCI,                                                   \
                .ctlr_transcode = false,                                                           \
                COND_CODE_1(IS_ENABLED(CONFIG_BT_BAP_UNICAST),                                     \
                            (.target_latency = BT_AUDIO_CODEC_CFG_TARGET_LATENCY_BALANCED,         \
                             .target_phy = BT_AUDIO_CODEC_CFG_TARGET_PHY_2M,),                     \
                            ())                                                                    \
                .id = _id,                                                                         \
                .cid = _cid,                                                                       \
                .vid = _vid,                                                                       \
                .data_len = sizeof((uint8_t[])_data),                                              \
                .data = _data,                                                                     \
                .meta_len = sizeof((uint8_t[])_meta),                                              \
                .meta = _meta,                                                                     \
        })

#define BT_AUDIO_CODEC_CAP(_id, _cid, _vid, _data, _meta)                                          \
        ((struct bt_audio_codec_cap){                                                              \
                /* Use HCI data path as default, can be overwritten by application */              \
                .path_id = BT_ISO_DATA_PATH_HCI,                                                   \
                .ctlr_transcode = false,                                                           \
                .id = (_id),                                                                       \
                .cid = (_cid),                                                                     \
                .vid = (_vid),                                                                     \
                .data_len = sizeof((uint8_t[])_data),                                              \
                .data = _data,                                                                     \
                .meta_len = sizeof((uint8_t[])_meta),                                              \
                .meta = _meta,                                                                     \
        })

struct bt_audio_codec_cap {
        uint8_t path_id;
        bool ctlr_transcode;
        uint8_t id;
        uint16_t cid;
        uint16_t vid;
#if CONFIG_BT_AUDIO_CODEC_CAP_MAX_DATA_SIZE > 0 || defined(__DOXYGEN__)
        size_t data_len;
        uint8_t data[CONFIG_BT_AUDIO_CODEC_CAP_MAX_DATA_SIZE];
#endif /* CONFIG_BT_AUDIO_CODEC_CAP_MAX_DATA_SIZE > 0 */
#if defined(CONFIG_BT_AUDIO_CODEC_CAP_MAX_METADATA_SIZE) || defined(__DOXYGEN__)
        size_t meta_len;
        uint8_t meta[CONFIG_BT_AUDIO_CODEC_CAP_MAX_METADATA_SIZE];
#endif /* CONFIG_BT_AUDIO_CODEC_CAP_MAX_METADATA_SIZE */
};

enum bt_audio_codec_cfg_target_latency {
        BT_AUDIO_CODEC_CFG_TARGET_LATENCY_LOW = 0x01,

        BT_AUDIO_CODEC_CFG_TARGET_LATENCY_BALANCED = 0x02,

        BT_AUDIO_CODEC_CFG_TARGET_LATENCY_HIGH = 0x03,
};

enum bt_audio_codec_cfg_target_phy {
        BT_AUDIO_CODEC_CFG_TARGET_PHY_1M = 0x01,

        BT_AUDIO_CODEC_CFG_TARGET_PHY_2M = 0x02,

        BT_AUDIO_CODEC_CFG_TARGET_PHY_CODED = 0x03,
};

struct bt_audio_codec_cfg {
        uint8_t path_id;
        bool ctlr_transcode;
#if defined(CONFIG_BT_BAP_UNICAST) || defined(__DOXYGEN__)
        enum bt_audio_codec_cfg_target_latency target_latency;
        enum bt_audio_codec_cfg_target_phy target_phy;
#endif /* CONFIG_BT_BAP_UNICAST */
        uint8_t  id;
        uint16_t cid;
        uint16_t vid;
#if CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE > 0 || defined(__DOXYGEN__)
        size_t data_len;
        uint8_t data[CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE];
#endif /* CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE > 0 */
#if CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE > 0 || defined(__DOXYGEN__)
        size_t meta_len;
        uint8_t meta[CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE];
#endif /* CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE > 0 */
};

int bt_audio_data_parse(const uint8_t ltv[], size_t size,
                        bool (*func)(struct bt_data *data, void *user_data), void *user_data);

int bt_audio_data_get_val(const uint8_t ltv_data[], size_t size, uint8_t type,
                          const uint8_t **data);

uint8_t bt_audio_get_chan_count(enum bt_audio_location chan_allocation);

enum bt_audio_dir {
        BT_AUDIO_DIR_SINK = 0x01,
        BT_AUDIO_DIR_SOURCE = 0x02,
};

static inline const char *bt_audio_dir_to_str(enum bt_audio_dir dir)
{
        switch (dir) {
        case BT_AUDIO_DIR_SINK:
                return "Sink";
        case BT_AUDIO_DIR_SOURCE:
                return "Source";
        default:
                return "Unknown";
        }
}


int bt_audio_codec_cfg_freq_to_freq_hz(enum bt_audio_codec_cfg_freq freq);

int bt_audio_codec_cfg_freq_hz_to_freq(uint32_t freq_hz);

int bt_audio_codec_cfg_get_freq(const struct bt_audio_codec_cfg *codec_cfg);

int bt_audio_codec_cfg_set_freq(struct bt_audio_codec_cfg *codec_cfg,
                                enum bt_audio_codec_cfg_freq freq);

int bt_audio_codec_cfg_frame_dur_to_frame_dur_us(enum bt_audio_codec_cfg_frame_dur frame_dur);

int bt_audio_codec_cfg_frame_dur_us_to_frame_dur(uint32_t frame_dur_us);

int bt_audio_codec_cfg_get_frame_dur(const struct bt_audio_codec_cfg *codec_cfg);

int bt_audio_codec_cfg_set_frame_dur(struct bt_audio_codec_cfg *codec_cfg,
                                     enum bt_audio_codec_cfg_frame_dur frame_dur);

int bt_audio_codec_cfg_get_chan_allocation(const struct bt_audio_codec_cfg *codec_cfg,
                                           enum bt_audio_location *chan_allocation,
                                           bool fallback_to_default);

int bt_audio_codec_cfg_set_chan_allocation(struct bt_audio_codec_cfg *codec_cfg,
                                           enum bt_audio_location chan_allocation);

int bt_audio_codec_cfg_get_octets_per_frame(const struct bt_audio_codec_cfg *codec_cfg);

int bt_audio_codec_cfg_set_octets_per_frame(struct bt_audio_codec_cfg *codec_cfg,
                                            uint16_t octets_per_frame);

int bt_audio_codec_cfg_get_frame_blocks_per_sdu(const struct bt_audio_codec_cfg *codec_cfg,
                                                bool fallback_to_default);

int bt_audio_codec_cfg_set_frame_blocks_per_sdu(struct bt_audio_codec_cfg *codec_cfg,
                                                uint8_t frame_blocks);

int bt_audio_codec_cfg_get_val(const struct bt_audio_codec_cfg *codec_cfg,
                               enum bt_audio_codec_cfg_type type, const uint8_t **data);

int bt_audio_codec_cfg_set_val(struct bt_audio_codec_cfg *codec_cfg,
                               enum bt_audio_codec_cfg_type type, const uint8_t *data,
                               size_t data_len);

int bt_audio_codec_cfg_unset_val(struct bt_audio_codec_cfg *codec_cfg,
                                 enum bt_audio_codec_cfg_type type);

int bt_audio_codec_cfg_meta_get_val(const struct bt_audio_codec_cfg *codec_cfg, uint8_t type,
                                    const uint8_t **data);

int bt_audio_codec_cfg_meta_set_val(struct bt_audio_codec_cfg *codec_cfg,
                                    enum bt_audio_metadata_type type, const uint8_t *data,
                                    size_t data_len);

int bt_audio_codec_cfg_meta_unset_val(struct bt_audio_codec_cfg *codec_cfg,
                                      enum bt_audio_metadata_type type);
int bt_audio_codec_cfg_meta_get_pref_context(const struct bt_audio_codec_cfg *codec_cfg,
                                             bool fallback_to_default);

int bt_audio_codec_cfg_meta_set_pref_context(struct bt_audio_codec_cfg *codec_cfg,
                                             enum bt_audio_context ctx);

int bt_audio_codec_cfg_meta_get_stream_context(const struct bt_audio_codec_cfg *codec_cfg);

int bt_audio_codec_cfg_meta_set_stream_context(struct bt_audio_codec_cfg *codec_cfg,
                                               enum bt_audio_context ctx);

int bt_audio_codec_cfg_meta_get_program_info(const struct bt_audio_codec_cfg *codec_cfg,
                                             const uint8_t **program_info);

int bt_audio_codec_cfg_meta_set_program_info(struct bt_audio_codec_cfg *codec_cfg,
                                             const uint8_t *program_info, size_t program_info_len);

int bt_audio_codec_cfg_meta_get_lang(const struct bt_audio_codec_cfg *codec_cfg,
                                     const uint8_t **lang);

int bt_audio_codec_cfg_meta_set_lang(struct bt_audio_codec_cfg *codec_cfg,
                                     const uint8_t lang[BT_AUDIO_LANG_SIZE]);

int bt_audio_codec_cfg_meta_get_ccid_list(const struct bt_audio_codec_cfg *codec_cfg,
                                          const uint8_t **ccid_list);

int bt_audio_codec_cfg_meta_set_ccid_list(struct bt_audio_codec_cfg *codec_cfg,
                                          const uint8_t *ccid_list, size_t ccid_list_len);

int bt_audio_codec_cfg_meta_get_parental_rating(const struct bt_audio_codec_cfg *codec_cfg);

int bt_audio_codec_cfg_meta_set_parental_rating(struct bt_audio_codec_cfg *codec_cfg,
                                                enum bt_audio_parental_rating parental_rating);

int bt_audio_codec_cfg_meta_get_program_info_uri(const struct bt_audio_codec_cfg *codec_cfg,
                                                 const uint8_t **program_info_uri);

int bt_audio_codec_cfg_meta_set_program_info_uri(struct bt_audio_codec_cfg *codec_cfg,
                                                 const uint8_t *program_info_uri,
                                                 size_t program_info_uri_len);

int bt_audio_codec_cfg_meta_get_audio_active_state(const struct bt_audio_codec_cfg *codec_cfg);

int bt_audio_codec_cfg_meta_set_audio_active_state(struct bt_audio_codec_cfg *codec_cfg,
                                                   enum bt_audio_active_state state);

int bt_audio_codec_cfg_meta_get_bcast_audio_immediate_rend_flag(
        const struct bt_audio_codec_cfg *codec_cfg);

int bt_audio_codec_cfg_meta_set_bcast_audio_immediate_rend_flag(
        struct bt_audio_codec_cfg *codec_cfg);

int bt_audio_codec_cfg_meta_get_assisted_listening_stream(
        const struct bt_audio_codec_cfg *codec_cfg);

int bt_audio_codec_cfg_meta_set_assisted_listening_stream(
        struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_assisted_listening_stream val);

int bt_audio_codec_cfg_meta_get_broadcast_name(const struct bt_audio_codec_cfg *codec_cfg,
                                               const uint8_t **broadcast_name);

int bt_audio_codec_cfg_meta_set_broadcast_name(struct bt_audio_codec_cfg *codec_cfg,
                                               const uint8_t *broadcast_name,
                                               size_t broadcast_name_len);

int bt_audio_codec_cfg_meta_get_extended(const struct bt_audio_codec_cfg *codec_cfg,
                                         const uint8_t **extended_meta);

int bt_audio_codec_cfg_meta_set_extended(struct bt_audio_codec_cfg *codec_cfg,
                                         const uint8_t *extended_meta, size_t extended_meta_len);

int bt_audio_codec_cfg_meta_get_vendor(const struct bt_audio_codec_cfg *codec_cfg,
                                       const uint8_t **vendor_meta);

int bt_audio_codec_cfg_meta_set_vendor(struct bt_audio_codec_cfg *codec_cfg,
                                       const uint8_t *vendor_meta, size_t vendor_meta_len); /* End of bt_audio_codec_cfg */


int bt_audio_codec_cap_get_val(const struct bt_audio_codec_cap *codec_cap,
                               enum bt_audio_codec_cap_type type, const uint8_t **data);

int bt_audio_codec_cap_set_val(struct bt_audio_codec_cap *codec_cap,
                               enum bt_audio_codec_cap_type type, const uint8_t *data,
                               size_t data_len);

int bt_audio_codec_cap_unset_val(struct bt_audio_codec_cap *codec_cap,
                                 enum bt_audio_codec_cap_type type);

int bt_audio_codec_cap_get_freq(const struct bt_audio_codec_cap *codec_cap);

int bt_audio_codec_cap_set_freq(struct bt_audio_codec_cap *codec_cap,
                                enum bt_audio_codec_cap_freq freq);

int bt_audio_codec_cap_get_frame_dur(const struct bt_audio_codec_cap *codec_cap);

int bt_audio_codec_cap_set_frame_dur(struct bt_audio_codec_cap *codec_cap,
                                     enum bt_audio_codec_cap_frame_dur frame_dur);

int bt_audio_codec_cap_get_supported_audio_chan_counts(const struct bt_audio_codec_cap *codec_cap,
                                                       bool fallback_to_default);

int bt_audio_codec_cap_set_supported_audio_chan_counts(
        struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_chan_count chan_count);

int bt_audio_codec_cap_get_octets_per_frame(
        const struct bt_audio_codec_cap *codec_cap,
        struct bt_audio_codec_octets_per_codec_frame *codec_frame);

int bt_audio_codec_cap_set_octets_per_frame(
        struct bt_audio_codec_cap *codec_cap,
        const struct bt_audio_codec_octets_per_codec_frame *codec_frame);

int bt_audio_codec_cap_get_max_codec_frames_per_sdu(const struct bt_audio_codec_cap *codec_cap,
                                                    bool fallback_to_default);

int bt_audio_codec_cap_set_max_codec_frames_per_sdu(struct bt_audio_codec_cap *codec_cap,
                                                    uint8_t codec_frames_per_sdu);

int bt_audio_codec_cap_meta_get_val(const struct bt_audio_codec_cap *codec_cap, uint8_t type,
                                    const uint8_t **data);

int bt_audio_codec_cap_meta_set_val(struct bt_audio_codec_cap *codec_cap,
                                    enum bt_audio_metadata_type type, const uint8_t *data,
                                    size_t data_len);

int bt_audio_codec_cap_meta_unset_val(struct bt_audio_codec_cap *codec_cap,
                                      enum bt_audio_metadata_type type);

int bt_audio_codec_cap_meta_get_pref_context(const struct bt_audio_codec_cap *codec_cap);

int bt_audio_codec_cap_meta_set_pref_context(struct bt_audio_codec_cap *codec_cap,
                                             enum bt_audio_context ctx);

int bt_audio_codec_cap_meta_get_stream_context(const struct bt_audio_codec_cap *codec_cap);

int bt_audio_codec_cap_meta_set_stream_context(struct bt_audio_codec_cap *codec_cap,
                                               enum bt_audio_context ctx);

int bt_audio_codec_cap_meta_get_program_info(const struct bt_audio_codec_cap *codec_cap,
                                             const uint8_t **program_info);

int bt_audio_codec_cap_meta_set_program_info(struct bt_audio_codec_cap *codec_cap,
                                             const uint8_t *program_info, size_t program_info_len);

int bt_audio_codec_cap_meta_get_lang(const struct bt_audio_codec_cap *codec_cap,
                                     const uint8_t **lang);

int bt_audio_codec_cap_meta_set_lang(struct bt_audio_codec_cap *codec_cap,
                                     const uint8_t lang[BT_AUDIO_LANG_SIZE]);

int bt_audio_codec_cap_meta_get_ccid_list(const struct bt_audio_codec_cap *codec_cap,
                                          const uint8_t **ccid_list);

int bt_audio_codec_cap_meta_set_ccid_list(struct bt_audio_codec_cap *codec_cap,
                                          const uint8_t *ccid_list, size_t ccid_list_len);

int bt_audio_codec_cap_meta_get_parental_rating(const struct bt_audio_codec_cap *codec_cap);

int bt_audio_codec_cap_meta_set_parental_rating(struct bt_audio_codec_cap *codec_cap,
                                                enum bt_audio_parental_rating parental_rating);

int bt_audio_codec_cap_meta_get_program_info_uri(const struct bt_audio_codec_cap *codec_cap,
                                                 const uint8_t **program_info_uri);

int bt_audio_codec_cap_meta_set_program_info_uri(struct bt_audio_codec_cap *codec_cap,
                                                 const uint8_t *program_info_uri,
                                                 size_t program_info_uri_len);

int bt_audio_codec_cap_meta_get_audio_active_state(const struct bt_audio_codec_cap *codec_cap);

int bt_audio_codec_cap_meta_set_audio_active_state(struct bt_audio_codec_cap *codec_cap,
                                                   enum bt_audio_active_state state);

int bt_audio_codec_cap_meta_get_bcast_audio_immediate_rend_flag(
        const struct bt_audio_codec_cap *codec_cap);

int bt_audio_codec_cap_meta_set_bcast_audio_immediate_rend_flag(
        struct bt_audio_codec_cap *codec_cap);

int bt_audio_codec_cap_meta_get_assisted_listening_stream(
        const struct bt_audio_codec_cap *codec_cap);

int bt_audio_codec_cap_meta_set_assisted_listening_stream(
        struct bt_audio_codec_cap *codec_cap, enum bt_audio_assisted_listening_stream val);

int bt_audio_codec_cap_meta_get_broadcast_name(const struct bt_audio_codec_cap *codec_cap,
                                               const uint8_t **broadcast_name);

int bt_audio_codec_cap_meta_set_broadcast_name(struct bt_audio_codec_cap *codec_cap,
                                               const uint8_t *broadcast_name,
                                               size_t broadcast_name_len);
int bt_audio_codec_cap_meta_get_extended(const struct bt_audio_codec_cap *codec_cap,
                                         const uint8_t **extended_meta);

int bt_audio_codec_cap_meta_set_extended(struct bt_audio_codec_cap *codec_cap,
                                         const uint8_t *extended_meta, size_t extended_meta_len);

int bt_audio_codec_cap_meta_get_vendor(const struct bt_audio_codec_cap *codec_cap,
                                       const uint8_t **vendor_meta);

int bt_audio_codec_cap_meta_set_vendor(struct bt_audio_codec_cap *codec_cap,
                                       const uint8_t *vendor_meta, size_t vendor_meta_len);
 /* End of bt_audio_codec_cap */


static inline char *bt_audio_context_bit_to_str(enum bt_audio_context context)
{
        switch (context) {
        case BT_AUDIO_CONTEXT_TYPE_NONE:
                return "None";
        case BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED:
                return "Unspecified";
        case BT_AUDIO_CONTEXT_TYPE_CONVERSATIONAL:
                return "Conversational";
        case BT_AUDIO_CONTEXT_TYPE_MEDIA:
                return "Media";
        case BT_AUDIO_CONTEXT_TYPE_GAME:
                return "Game";
        case BT_AUDIO_CONTEXT_TYPE_INSTRUCTIONAL:
                return "Instructional";
        case BT_AUDIO_CONTEXT_TYPE_VOICE_ASSISTANTS:
                return "Voice assistant";
        case BT_AUDIO_CONTEXT_TYPE_LIVE:
                return "Live";
        case BT_AUDIO_CONTEXT_TYPE_SOUND_EFFECTS:
                return "Sound effects";
        case BT_AUDIO_CONTEXT_TYPE_NOTIFICATIONS:
                return "Notifications";
        case BT_AUDIO_CONTEXT_TYPE_RINGTONE:
                return "Ringtone";
        case BT_AUDIO_CONTEXT_TYPE_ALERTS:
                return "Alerts";
        case BT_AUDIO_CONTEXT_TYPE_EMERGENCY_ALARM:
                return "Emergency alarm";
        default:
                return "Unknown context";
        }
}

static inline char *bt_audio_parental_rating_to_str(enum bt_audio_parental_rating parental_rating)
{
        switch (parental_rating) {
        case BT_AUDIO_PARENTAL_RATING_NO_RATING:
                return "No rating";
        case BT_AUDIO_PARENTAL_RATING_AGE_ANY:
                return "Any";
        case BT_AUDIO_PARENTAL_RATING_AGE_5_OR_ABOVE:
                return "Age 5 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_6_OR_ABOVE:
                return "Age 6 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_7_OR_ABOVE:
                return "Age 7 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_8_OR_ABOVE:
                return "Age 8 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_9_OR_ABOVE:
                return "Age 9 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_10_OR_ABOVE:
                return "Age 10 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_11_OR_ABOVE:
                return "Age 11 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_12_OR_ABOVE:
                return "Age 12 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_13_OR_ABOVE:
                return "Age 13 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_14_OR_ABOVE:
                return "Age 14 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_15_OR_ABOVE:
                return "Age 15 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_16_OR_ABOVE:
                return "Age 16 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_17_OR_ABOVE:
                return "Age 17 or above";
        case BT_AUDIO_PARENTAL_RATING_AGE_18_OR_ABOVE:
                return "Age 18 or above";
        default:
                return "Unknown rating";
        }
}

static inline char *bt_audio_active_state_to_str(enum bt_audio_active_state state)
{
        switch (state) {
        case BT_AUDIO_ACTIVE_STATE_DISABLED:
                return "Disabled";
        case BT_AUDIO_ACTIVE_STATE_ENABLED:
                return "Enabled";
        default:
                return "Unknown active state";
        }
}

static inline char *bt_audio_codec_cap_freq_bit_to_str(enum bt_audio_codec_cap_freq freq)
{
        switch (freq) {
        case BT_AUDIO_CODEC_CAP_FREQ_8KHZ:
                return "8000 Hz";
        case BT_AUDIO_CODEC_CAP_FREQ_11KHZ:
                return "11025 Hz";
        case BT_AUDIO_CODEC_CAP_FREQ_16KHZ:
                return "16000 Hz";
        case BT_AUDIO_CODEC_CAP_FREQ_22KHZ:
                return "22050 Hz";
        case BT_AUDIO_CODEC_CAP_FREQ_24KHZ:
                return "24000 Hz";
        case BT_AUDIO_CODEC_CAP_FREQ_32KHZ:
                return "32000 Hz";
        case BT_AUDIO_CODEC_CAP_FREQ_44KHZ:
                return "44100 Hz";
        case BT_AUDIO_CODEC_CAP_FREQ_48KHZ:
                return "48000 Hz";
        case BT_AUDIO_CODEC_CAP_FREQ_88KHZ:
                return "88200 Hz";
        case BT_AUDIO_CODEC_CAP_FREQ_96KHZ:
                return "96000 Hz";
        case BT_AUDIO_CODEC_CAP_FREQ_176KHZ:
                return "176400 Hz";
        case BT_AUDIO_CODEC_CAP_FREQ_192KHZ:
                return "192000 Hz";
        case BT_AUDIO_CODEC_CAP_FREQ_384KHZ:
                return "384000 Hz";
        default:
                return "Unknown supported frequency";
        }
}

static inline char *
bt_audio_codec_cap_frame_dur_bit_to_str(enum bt_audio_codec_cap_frame_dur frame_dur)
{
        switch (frame_dur) {
        case BT_AUDIO_CODEC_CAP_DURATION_7_5:
                return "7.5 ms";
        case BT_AUDIO_CODEC_CAP_DURATION_10:
                return "10 ms";
        case BT_AUDIO_CODEC_CAP_DURATION_PREFER_7_5:
                return "7.5 ms preferred";
        case BT_AUDIO_CODEC_CAP_DURATION_PREFER_10:
                return "10 ms preferred";
        default:
                return "Unknown frame duration";
        }
}

static inline char *
bt_audio_codec_cap_chan_count_bit_to_str(enum bt_audio_codec_cap_chan_count chan_count)
{
        switch (chan_count) {
        case BT_AUDIO_CODEC_CAP_CHAN_COUNT_1:
                return "1 channel";
        case BT_AUDIO_CODEC_CAP_CHAN_COUNT_2:
                return "2 channels";
        case BT_AUDIO_CODEC_CAP_CHAN_COUNT_3:
                return "3 channels";
        case BT_AUDIO_CODEC_CAP_CHAN_COUNT_4:
                return "4 channels";
        case BT_AUDIO_CODEC_CAP_CHAN_COUNT_5:
                return "5 channels";
        case BT_AUDIO_CODEC_CAP_CHAN_COUNT_6:
                return "6 channels";
        case BT_AUDIO_CODEC_CAP_CHAN_COUNT_7:
                return "7 channels";
        case BT_AUDIO_CODEC_CAP_CHAN_COUNT_8:
                return "8 channels";
        default:
                return "Unknown channel count";
        }
}

static inline char *bt_audio_location_bit_to_str(enum bt_audio_location location)
{
        switch (location) {
        case BT_AUDIO_LOCATION_MONO_AUDIO:
                return "Mono";
        case BT_AUDIO_LOCATION_FRONT_LEFT:
                return "Front left";
        case BT_AUDIO_LOCATION_FRONT_RIGHT:
                return "Front right";
        case BT_AUDIO_LOCATION_FRONT_CENTER:
                return "Front center";
        case BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_1:
                return "Low frequency effects 1";
        case BT_AUDIO_LOCATION_BACK_LEFT:
                return "Back left";
        case BT_AUDIO_LOCATION_BACK_RIGHT:
                return "Back right";
        case BT_AUDIO_LOCATION_FRONT_LEFT_OF_CENTER:
                return "Front left of center";
        case BT_AUDIO_LOCATION_FRONT_RIGHT_OF_CENTER:
                return "Front right of center";
        case BT_AUDIO_LOCATION_BACK_CENTER:
                return "Back center";
        case BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_2:
                return "Low frequency effects 2";
        case BT_AUDIO_LOCATION_SIDE_LEFT:
                return "Side left";
        case BT_AUDIO_LOCATION_SIDE_RIGHT:
                return "Side right";
        case BT_AUDIO_LOCATION_TOP_FRONT_LEFT:
                return "Top front left";
        case BT_AUDIO_LOCATION_TOP_FRONT_RIGHT:
                return "Top front right";
        case BT_AUDIO_LOCATION_TOP_FRONT_CENTER:
                return "Top front center";
        case BT_AUDIO_LOCATION_TOP_CENTER:
                return "Top center";
        case BT_AUDIO_LOCATION_TOP_BACK_LEFT:
                return "Top back left";
        case BT_AUDIO_LOCATION_TOP_BACK_RIGHT:
                return "Top back right";
        case BT_AUDIO_LOCATION_TOP_SIDE_LEFT:
                return "Top side left";
        case BT_AUDIO_LOCATION_TOP_SIDE_RIGHT:
                return "Top side right";
        case BT_AUDIO_LOCATION_TOP_BACK_CENTER:
                return "Top back center";
        case BT_AUDIO_LOCATION_BOTTOM_FRONT_CENTER:
                return "Bottom front center";
        case BT_AUDIO_LOCATION_BOTTOM_FRONT_LEFT:
                return "Bottom front left";
        case BT_AUDIO_LOCATION_BOTTOM_FRONT_RIGHT:
                return "Bottom front right";
        case BT_AUDIO_LOCATION_FRONT_LEFT_WIDE:
                return "Front left wide";
        case BT_AUDIO_LOCATION_FRONT_RIGHT_WIDE:
                return "Front right wde";
        case BT_AUDIO_LOCATION_LEFT_SURROUND:
                return "Left surround";
        case BT_AUDIO_LOCATION_RIGHT_SURROUND:
                return "Right surround";
        default:
                return "Unknown location";
        }
}
 /* End of bt_audio_to_str */
#ifdef __cplusplus
}
#endif
 /* end of bt_audio */

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2020 Intel Corporation。

版权（Copyright）：© 2020-2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 123 行

默认使用 HCI 数据路径（data path），应用程序可以覆盖此设置。

### 注释 3：原第 150 行

默认使用 HCI 数据路径（data path），应用程序可以覆盖此设置。

### 注释 4：原第 187 行

条件表达式：`CONFIG_BT_AUDIO_CODEC_CAP_MAX_DATA_SIZE > 0`。

### 注释 5：原第 193 行

条件编译配置（Configuration）标记：`CONFIG_BT_AUDIO_CODEC_CAP_MAX_METADATA_SIZE`。

### 注释 6：原第 254 行

条件编译配置（Configuration）标记：`CONFIG_BT_BAP_UNICAST`。

### 注释 7：原第 266 行

条件表达式：`CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE > 0`。

### 注释 8：原第 272 行

条件表达式：`CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE > 0`。

### 注释 9：原第 1024 行

`bt_audio_codec_cfg` 文档分组结束。

### 注释 10：原第 1630 行

`bt_audio_codec_cap` 文档分组结束。

### 注释 11：原第 1928 行

`bt_audio_to_str` 文档分组结束。

### 注释 12：原第 1933 行

`bt_audio` 文档分组结束。

### 注释 13：原第 1936 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [zephyr/bluetooth/audio/lc3.h](https://docs.zephyrproject.org/latest/doxygen/html/lc3_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/bluetooth/buf.h](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h.html)
- [zephyr/bluetooth/hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [bt_audio_codec_octets_per_codec_frame](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [min](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md#aa8b234fa137273cd16230ebabc5f8ef4)
- [max](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md#ae09686799077b13e78b856b1e7e63b6a)
- [bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [path_id](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#a822a06f815091cc580ca2e5bbb3126f7)
- [ctlr_transcode](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#a900a77db09e72de61d4ff652c6dbb10b)
- [id](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#ae3892731e7ca05f3ec426c70f0d9e1a9)
- [cid](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#a763222d12a87958a5ba806303f98829a)
- [vid](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#a3b91269e16a3d63b3128a527caa5e3ff)
- [data_len](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#acf3e22c6db1533fff7015acbc7eca196)
- [data](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#a455638aac9167d288a1e7a9fccabc49d)
- [meta_len](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#afe806521d5aac36e9f6c6a0598500a8f)
- [meta](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#acec4f5e31752d81d4dbf441223e7f44c)
- [bt_audio_codec_cfg_target_latency](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga62108a3dcc3e35f7b31a99f7a33679e6)
- [BT_AUDIO_CODEC_CFG_TARGET_LATENCY_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gga62108a3dcc3e35f7b31a99f7a33679e6aec4cf0f851e64e034ead8a075c93eda8)
- [BT_AUDIO_CODEC_CFG_TARGET_LATENCY_BALANCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gga62108a3dcc3e35f7b31a99f7a33679e6a971aeaf3e2df14f5ed75965a31188f80)
- [BT_AUDIO_CODEC_CFG_TARGET_LATENCY_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gga62108a3dcc3e35f7b31a99f7a33679e6a93ec0567d248d4cfc9cd60c26cbc50ef)
- [bt_audio_codec_cfg_target_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga640af4e254e73f5c4646e9be4e99f3d1)
- [BT_AUDIO_CODEC_CFG_TARGET_PHY_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gga640af4e254e73f5c4646e9be4e99f3d1acd5c965423632650196768589a75bd95)
- [BT_AUDIO_CODEC_CFG_TARGET_PHY_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gga640af4e254e73f5c4646e9be4e99f3d1a0b7e1713ff85524953baeb4e7e085d96)
- [BT_AUDIO_CODEC_CFG_TARGET_PHY_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gga640af4e254e73f5c4646e9be4e99f3d1a3793a0bbbb7daa399086ce7db0a24a38)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [path_id](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a9386056bb02908407c9e3aad48abbd87)
- [ctlr_transcode](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a9e2c8081950a0830ffc270245ab308c1)
- [target_latency](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#aa71d0e75b36f6dc664fdcd2e092f8d57)
- [target_phy](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a571a8b875dd0acac50e82620dc6d9aab)
- [id](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#aa2f99ec31ff3eb9b7b738bc8a1170f20)
- [cid](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a664e21bcd6002b21d4b1b53d866db32d)
- [vid](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a2996ab3f6ae1cab09ff5e3329b42468e)
- [data_len](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a8a5a789e9993a48ce4c83a2156c1f43c)
- [data](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#ad3709d5321f6faeb392452cb3b21023b)
- [meta_len](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a1e69a5c017e9571b50aba721f86876fb)
- [meta](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a4f84974ea14b773ad8e2fd7c0ffa0c7f)
- [bt_audio_data_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gafd8574b16141162c95653f0aa2bf6ff7)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [bt_audio_data_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gabbd1b9c46caa9a19de6c95b08c31e5b5)
- [bt_audio_get_chan_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga87415f8dddd38b3f5641c96e9722a44a)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)
- [BT_AUDIO_DIR_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8)
- [BT_AUDIO_DIR_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c)
- [bt_audio_dir_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gaf629628fc13be7a1693ceb1d32b743f2)
- [bt_audio_codec_cfg_freq_to_freq_hz](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga2e557fe726a49dc99754da16f7cc60af)
- [bt_audio_codec_cfg_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga8e99fb678cc011bb8c9f6e1858bae0d7)
- [bt_audio_codec_cfg_freq_hz_to_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_audio_codec_cfg_get_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gad8525a57d35e3e34ea591f7e20e2512d)
- [bt_audio_codec_cfg_set_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gac119989d5dcfa36becf4edd0ae7c6138)
- [bt_audio_codec_cfg_frame_dur_to_frame_dur_us](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga225e05df1f0d1efb709c972187901495)
- [bt_audio_codec_cfg_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga83701b5eadfcbc9b84dc0b1a85ebeb74)
- [bt_audio_codec_cfg_frame_dur_us_to_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga0782a3d9254fb76b441c6c2492571556)
- [bt_audio_codec_cfg_get_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga2dd3afe41b22e989fb46614f89550007)
- [bt_audio_codec_cfg_set_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga7d8306f98cb00f06e68a1df417825f0d)
- [bt_audio_codec_cfg_get_chan_allocation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gae712e0f8e84aeb4ad2528da34907e29d)
- [bt_audio_codec_cfg_set_chan_allocation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gafbbcd69fac18ed0201a5e0156209b049)
- [bt_audio_codec_cfg_get_octets_per_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga503be053422217502d6108b045791e02)
- [bt_audio_codec_cfg_set_octets_per_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga866cdec28194056dc9e274d0436b45c2)
- [bt_audio_codec_cfg_get_frame_blocks_per_sdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gadba0723f9d8a9546b659fba139051374)
- [bt_audio_codec_cfg_set_frame_blocks_per_sdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gac9cf20bafbe24b34034bfb6ee7aaf03e)
- [bt_audio_codec_cfg_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga707c679db0193197b56acabfb08f8d1f)
- [bt_audio_codec_cfg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga9230ec4d7518bd243207ba2decb1a974)
- [bt_audio_codec_cfg_set_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gab10f22938780530b1d1b95695382902e)
- [bt_audio_codec_cfg_unset_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gad3857d0ca008854df5966501caa261ba)
- [bt_audio_codec_cfg_meta_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gae98335e87394a491b4a311d867a5e32d)
- [bt_audio_codec_cfg_meta_set_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga3e24c2ba8de502600e647cb2f84e3ec4)
- [bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)
- [bt_audio_codec_cfg_meta_unset_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gab46f830daa1d9a907f47eb2a9eed7337)
- [bt_audio_codec_cfg_meta_get_pref_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaea087663426a49bb6ff4859800aecb84)
- [bt_audio_codec_cfg_meta_set_pref_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gab40bad609f17d24e7e0e9ffcebe4e912)
- [bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)
- [bt_audio_codec_cfg_meta_get_stream_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga4cc4e1bb941206e7f1541a57fc92b8e9)
- [bt_audio_codec_cfg_meta_set_stream_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga5cd2af1bb44c6eb5bafe824f005a77f0)
- [bt_audio_codec_cfg_meta_get_program_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga03284b8474d65443d7ecc8bdfc6f04c6)
- [bt_audio_codec_cfg_meta_set_program_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga2ca9e616d20d7513c60ce905f046ac7b)
- [bt_audio_codec_cfg_meta_get_lang](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga55e3cbaeacf15fcb1f24a16eb28db99c)
- [bt_audio_codec_cfg_meta_set_lang](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga93052db14c857097e7cf9abc34b7fc39)
- [BT_AUDIO_LANG_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gab6e5f793d514626deca21940d35d8f21)
- [bt_audio_codec_cfg_meta_get_ccid_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaa0f9b9f608c7af881d5a928a3ae397b2)
- [bt_audio_codec_cfg_meta_set_ccid_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga59716b95fcea3404ff8c078564b0e29c)
- [bt_audio_codec_cfg_meta_get_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaf0eecb02a05f0cc2b75ae9fb32c03913)
- [bt_audio_codec_cfg_meta_set_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gab5d8b5877de4fe16c0e06a1d4f0d15ce)
- [bt_audio_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga6d4aff1f93dc0b902e4b5d1355f15760)
- [bt_audio_codec_cfg_meta_get_program_info_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga6bdbc0a0b929fdbdc75db479aec858df)
- [bt_audio_codec_cfg_meta_set_program_info_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga99163729034e816eaef7195505d5ae20)
- [bt_audio_codec_cfg_meta_get_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga0fd6e6baf1b4f22d60768aaed6f42e8e)
- [bt_audio_codec_cfg_meta_set_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaf869e7ce0c9dd467fb03e8503d36c58a)
- [bt_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga16d403ec4db7be997682331ad365ff5f)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_audio_codec_cfg_meta_get_bcast_audio_immediate_rend_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga66143aa7dcc726e06a12660b8f90fc5a)
- [bt_audio_codec_cfg_meta_set_bcast_audio_immediate_rend_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaede61b65d2037c7fbf6c4c4e090990be)
- [bt_audio_codec_cfg_meta_get_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga22ae14fce65b757e31f391c4bdcae328)
- [bt_audio_codec_cfg_meta_set_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga67d83559cbe6cfab235f2e588cbc398c)
- [bt_audio_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga207fbf0fbca9b24cba02c7f1d184e7f5)
- [bt_audio_codec_cfg_meta_get_broadcast_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga5d80babcd6f381014e1fae98a755e1d3)
- [bt_audio_codec_cfg_meta_set_broadcast_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga4f5cbacebedc8d7df02d1c47b140bf3c)
- [bt_audio_codec_cfg_meta_get_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga1f76f82bff63b876eb761a0bf0377428)
- [bt_audio_codec_cfg_meta_set_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gade9cb53287ab3356fb57ba8a454a3aad)
- [bt_audio_codec_cfg_meta_get_vendor](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga4a4982e3bd0e8c944b584196ef146f6c)
- [bt_audio_codec_cfg_meta_set_vendor](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga6935d1c40b3178b0c8fa877ee93d1e53)
- [bt_audio_codec_cap_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gac3bf5dd414271bb1dcbc6590994cff6b)
- [bt_audio_codec_cap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf58823a56eb36cfd22e582ab1ea3d015)
- [bt_audio_codec_cap_set_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga0c2c816b0b2b85aa5dd38f21caceea40)
- [bt_audio_codec_cap_unset_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gabc9962212ad65339ff02ba1389d5f9f8)
- [bt_audio_codec_cap_get_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaa1dbf81c437c983af0144bf62433666c)
- [bt_audio_codec_cap_set_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gac0655c0bd6552ab8a265076d7d0cd1b2)
- [bt_audio_codec_cap_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaafc1106d5d305874ee2f540c850ff5b4)
- [bt_audio_codec_cap_get_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga12336de7d908bda94427caee4dc080e0)
- [bt_audio_codec_cap_set_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga53e5df6cc4cfbed12b59a6a506657772)
- [bt_audio_codec_cap_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf37e8e19f956afb3c3a413cbaa1a21f5)
- [bt_audio_codec_cap_get_supported_audio_chan_counts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga63d5e083f03ec06939ee1cd0355c8c2a)
- [bt_audio_codec_cap_set_supported_audio_chan_counts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaf6b2717823f9f3136237ed6a6515449e)
- [bt_audio_codec_cap_chan_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gae695b5d17359967703f2509db1671fa5)
- [bt_audio_codec_cap_get_octets_per_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaa949089f2c6c143041e6cb61338e0ddc)
- [bt_audio_codec_cap_set_octets_per_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gac1c42460cd3c55bbfbd467f84ab2d78d)
- [bt_audio_codec_cap_get_max_codec_frames_per_sdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga194d938896ee65601bdce96d68c84885)
- [bt_audio_codec_cap_set_max_codec_frames_per_sdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga3785bc41f56f8f2a09248396dadb31da)
- [bt_audio_codec_cap_meta_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga5c2ecbb4d0cef26dd2cc5d023e70a163)
- [bt_audio_codec_cap_meta_set_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga1fdfd8c36f4131bcf4ffd2b7f176b631)
- [bt_audio_codec_cap_meta_unset_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga40848f5375d1e58622c580112c282f2e)
- [bt_audio_codec_cap_meta_get_pref_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaaa8c6783241b1b70349354b3e36c696c)
- [bt_audio_codec_cap_meta_set_pref_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga7fe0d4553d6accf5c89645cbf86149bf)
- [bt_audio_codec_cap_meta_get_stream_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga88ee657b5bd3f847bb75c9620ddb142f)
- [bt_audio_codec_cap_meta_set_stream_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga5cc7f360049c38c8de631ea33dbc44ab)
- [bt_audio_codec_cap_meta_get_program_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga33725c3b2c06d6c22030bb5a77d702b0)
- [bt_audio_codec_cap_meta_set_program_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga43d2ec3a4d621c26843de82db7fd2189)
- [bt_audio_codec_cap_meta_get_lang](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gafb631b55b69b256c60b9cf3c7f418ff8)
- [bt_audio_codec_cap_meta_set_lang](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga555db1eff71a3bc79a5bcb959c0198cc)
- [bt_audio_codec_cap_meta_get_ccid_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga3095dea36e60e75cbfe786d3c2f11866)
- [bt_audio_codec_cap_meta_set_ccid_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga00a8ad22713dab761c81d1b8481c037d)
- [bt_audio_codec_cap_meta_get_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gab34d0369ce08efcd407d33956d32632e)
- [bt_audio_codec_cap_meta_set_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga5e267dfad978cd3d52be9c31a4fac0be)
- [bt_audio_codec_cap_meta_get_program_info_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gadb39b0ee1f65cdd2457fdf2c3142c040)
- [bt_audio_codec_cap_meta_set_program_info_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gafbb0d6282d989e8bc70caada2845b337)
- [bt_audio_codec_cap_meta_get_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga88bb1da63b7ea0f95dd236aa1024cfb8)
- [bt_audio_codec_cap_meta_set_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gacd3de0306a22d1a1d9ba09b4ac4f4e09)
- [bt_audio_codec_cap_meta_get_bcast_audio_immediate_rend_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gab4ccc7cb7d779acb20185ae808dd8bbe)
- [bt_audio_codec_cap_meta_set_bcast_audio_immediate_rend_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaa1d382b4fa53f7cbe8426df53a3317ce)
- [bt_audio_codec_cap_meta_get_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga4f1ea56f2c1c21420f078d35081ceee5)
- [bt_audio_codec_cap_meta_set_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga3346db1f59cb35b9b9e5255424adb6e4)
- [bt_audio_codec_cap_meta_get_broadcast_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga3c8df3fe79f0bb96c4e15e7c2502bf89)
- [bt_audio_codec_cap_meta_set_broadcast_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga461add2808a1eca8993222d2b31d5a5f)
- [bt_audio_codec_cap_meta_get_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga69aecd7e98f90a5162ff8ea3373b43d4)
- [bt_audio_codec_cap_meta_set_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gac00aabc7329027852a7caf5cdff2bc26)
- [bt_audio_codec_cap_meta_get_vendor](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gab8c80a0f55041f026d453fd88cdeb727)
- [bt_audio_codec_cap_meta_set_vendor](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga1f06789782541beab9aab4914f91bb57)
- [bt_audio_context_bit_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__to__str.html#ga26436fc678423ff1cf3543d381359d0f)
- [BT_AUDIO_CONTEXT_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a890d2723c8b23127ab4a1cb8b6b1118d)
- [BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5)
- [BT_AUDIO_CONTEXT_TYPE_CONVERSATIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e)
- [BT_AUDIO_CONTEXT_TYPE_MEDIA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e)
- [BT_AUDIO_CONTEXT_TYPE_GAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730)
- [BT_AUDIO_CONTEXT_TYPE_INSTRUCTIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4)
- [BT_AUDIO_CONTEXT_TYPE_VOICE_ASSISTANTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e)
- [BT_AUDIO_CONTEXT_TYPE_LIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55)
- [BT_AUDIO_CONTEXT_TYPE_SOUND_EFFECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9)
- [BT_AUDIO_CONTEXT_TYPE_NOTIFICATIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377)
- [BT_AUDIO_CONTEXT_TYPE_RINGTONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3)
- [BT_AUDIO_CONTEXT_TYPE_ALERTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6)
- [BT_AUDIO_CONTEXT_TYPE_EMERGENCY_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1)
- [bt_audio_parental_rating_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__to__str.html#ga6926c4e8bda0874769177a903276c072)
- [BT_AUDIO_PARENTAL_RATING_NO_RATING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c)
- [BT_AUDIO_PARENTAL_RATING_AGE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1)
- [BT_AUDIO_PARENTAL_RATING_AGE_5_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526)
- [BT_AUDIO_PARENTAL_RATING_AGE_6_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc)
- [BT_AUDIO_PARENTAL_RATING_AGE_7_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a)
- [BT_AUDIO_PARENTAL_RATING_AGE_8_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4)
- [BT_AUDIO_PARENTAL_RATING_AGE_9_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd)
- [BT_AUDIO_PARENTAL_RATING_AGE_10_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2)
- [BT_AUDIO_PARENTAL_RATING_AGE_11_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0)
- [BT_AUDIO_PARENTAL_RATING_AGE_12_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7)
- [BT_AUDIO_PARENTAL_RATING_AGE_13_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d)
- [BT_AUDIO_PARENTAL_RATING_AGE_14_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86)
- [BT_AUDIO_PARENTAL_RATING_AGE_15_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077)
- [BT_AUDIO_PARENTAL_RATING_AGE_16_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92)
- [BT_AUDIO_PARENTAL_RATING_AGE_17_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff)
- [BT_AUDIO_PARENTAL_RATING_AGE_18_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071)
- [bt_audio_active_state_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__to__str.html#ga1dd5865429e2438e0d4f88e891eda975)
- [BT_AUDIO_ACTIVE_STATE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3)
- [BT_AUDIO_ACTIVE_STATE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940)
- [bt_audio_codec_cap_freq_bit_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__to__str.html#gadd3bac4f1f1b334cb60f5783fdc15c14)
- [BT_AUDIO_CODEC_CAP_FREQ_8KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83)
- [BT_AUDIO_CODEC_CAP_FREQ_11KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81)
- [BT_AUDIO_CODEC_CAP_FREQ_16KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361)
- [BT_AUDIO_CODEC_CAP_FREQ_22KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982)
- [BT_AUDIO_CODEC_CAP_FREQ_24KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956)
- [BT_AUDIO_CODEC_CAP_FREQ_32KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c)
- [BT_AUDIO_CODEC_CAP_FREQ_44KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3)
- [BT_AUDIO_CODEC_CAP_FREQ_48KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91)
- [BT_AUDIO_CODEC_CAP_FREQ_88KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211)
- [BT_AUDIO_CODEC_CAP_FREQ_96KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663)
- [BT_AUDIO_CODEC_CAP_FREQ_176KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b)
- [BT_AUDIO_CODEC_CAP_FREQ_192KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890)
- [BT_AUDIO_CODEC_CAP_FREQ_384KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2)
- [bt_audio_codec_cap_frame_dur_bit_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__to__str.html#ga6b9cc74dafcf03056862ae9823bce58d)
- [BT_AUDIO_CODEC_CAP_DURATION_7_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441)
- [BT_AUDIO_CODEC_CAP_DURATION_10](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b)
- [BT_AUDIO_CODEC_CAP_DURATION_PREFER_7_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91)
- [BT_AUDIO_CODEC_CAP_DURATION_PREFER_10](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e)
- [bt_audio_codec_cap_chan_count_bit_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__to__str.html#ga795742ed8d91e2b675fbcdaeee7a71ec)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_6](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_7](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943)
- [bt_audio_location_bit_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__to__str.html#gaa1b9f7166fd6e6797da65d9537357324)
- [BT_AUDIO_LOCATION_MONO_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df)
- [BT_AUDIO_LOCATION_FRONT_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b)
- [BT_AUDIO_LOCATION_FRONT_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3)
- [BT_AUDIO_LOCATION_FRONT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337)
- [BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6)
- [BT_AUDIO_LOCATION_BACK_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896)
- [BT_AUDIO_LOCATION_BACK_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa)
- [BT_AUDIO_LOCATION_FRONT_LEFT_OF_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e)
- [BT_AUDIO_LOCATION_FRONT_RIGHT_OF_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692)
- [BT_AUDIO_LOCATION_BACK_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983)
- [BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b)
- [BT_AUDIO_LOCATION_SIDE_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064)
- [BT_AUDIO_LOCATION_SIDE_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd)
- [BT_AUDIO_LOCATION_TOP_FRONT_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9)
- [BT_AUDIO_LOCATION_TOP_FRONT_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d)
- [BT_AUDIO_LOCATION_TOP_FRONT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e)
- [BT_AUDIO_LOCATION_TOP_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f)
- [BT_AUDIO_LOCATION_TOP_BACK_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06)
- [BT_AUDIO_LOCATION_TOP_BACK_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69)
- [BT_AUDIO_LOCATION_TOP_SIDE_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6)
- [BT_AUDIO_LOCATION_TOP_SIDE_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59)
- [BT_AUDIO_LOCATION_TOP_BACK_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd)
- [BT_AUDIO_LOCATION_BOTTOM_FRONT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376)
- [BT_AUDIO_LOCATION_BOTTOM_FRONT_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29)
- [BT_AUDIO_LOCATION_BOTTOM_FRONT_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8)
- [BT_AUDIO_LOCATION_FRONT_LEFT_WIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d)
- [BT_AUDIO_LOCATION_FRONT_RIGHT_WIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71)
- [BT_AUDIO_LOCATION_LEFT_SURROUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6)
- [BT_AUDIO_LOCATION_RIGHT_SURROUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e)
- [assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [buf.h](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h.html)
- [hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h.html)
- [lc3.h](https://docs.zephyrproject.org/latest/doxygen/html/lc3_8h.html)
- [bt_audio_codec_cap::vid](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#a3b91269e16a3d63b3128a527caa5e3ff)
- [bt_audio_codec_cap::data](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#a455638aac9167d288a1e7a9fccabc49d)
- [bt_audio_codec_cap::cid](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#a763222d12a87958a5ba806303f98829a)
- [bt_audio_codec_cap::path_id](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#a822a06f815091cc580ca2e5bbb3126f7)
- [bt_audio_codec_cap::ctlr_transcode](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#a900a77db09e72de61d4ff652c6dbb10b)
- [bt_audio_codec_cap::meta](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#acec4f5e31752d81d4dbf441223e7f44c)
- [bt_audio_codec_cap::data_len](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#acf3e22c6db1533fff7015acbc7eca196)
- [bt_audio_codec_cap::id](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#ae3892731e7ca05f3ec426c70f0d9e1a9)
- [bt_audio_codec_cap::meta_len](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md#afe806521d5aac36e9f6c6a0598500a8f)
- [bt_audio_codec_cfg::meta_len](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a1e69a5c017e9571b50aba721f86876fb)
- [bt_audio_codec_cfg::vid](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a2996ab3f6ae1cab09ff5e3329b42468e)
- [bt_audio_codec_cfg::meta](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a4f84974ea14b773ad8e2fd7c0ffa0c7f)
- [bt_audio_codec_cfg::target_phy](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a571a8b875dd0acac50e82620dc6d9aab)
- [bt_audio_codec_cfg::cid](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a664e21bcd6002b21d4b1b53d866db32d)
- [bt_audio_codec_cfg::data_len](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a8a5a789e9993a48ce4c83a2156c1f43c)
- [bt_audio_codec_cfg::path_id](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a9386056bb02908407c9e3aad48abbd87)
- [bt_audio_codec_cfg::ctlr_transcode](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#a9e2c8081950a0830ffc270245ab308c1)
- [bt_audio_codec_cfg::id](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#aa2f99ec31ff3eb9b7b738bc8a1170f20)
- [bt_audio_codec_cfg::target_latency](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#aa71d0e75b36f6dc664fdcd2e092f8d57)
- [bt_audio_codec_cfg::data](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md#ad3709d5321f6faeb392452cb3b21023b)
- [bt_audio_codec_octets_per_codec_frame::min](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md#aa8b234fa137273cd16230ebabc5f8ef4)
- [bt_audio_codec_octets_per_codec_frame::max](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md#ae09686799077b13e78b856b1e7e63b6a)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P001_access.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_cdb.h_源码浏览.md)
