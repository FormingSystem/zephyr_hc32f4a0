---
id: learning.zephyr-docs.api-source-system-reference.page-3
title: bluetooth.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_bluetooth.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)。

## 3.1\_原始可见代码（Source Code）

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
<a id="l00067"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00095"></a>
<a id="l00096"></a>
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
<a id="foldopen00117"></a>
<a id="l00117"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00132"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="foldopen00156"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="foldopen00174"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="foldopen00227"></a>
<a id="l00227"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="foldopen00618"></a>
<a id="l00618"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00644"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00656"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="foldopen00691"></a>
<a id="l00691"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00853"></a>
<a id="l00854"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="foldopen00916"></a>
<a id="l00916"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00957"></a>
<a id="l00958"></a>
<a id="l00960"></a>
<a id="l00961"></a>
<a id="l00974"></a>
<a id="l00975"></a>
<a id="l00988"></a>
<a id="l00989"></a>
<a id="l01005"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="foldopen01020"></a>
<a id="l01020"></a>
<a id="l01021"></a>
<a id="l01022"></a>
<a id="l01023"></a>
<a id="l01024"></a>
<a id="l01025"></a>
<a id="foldopen01027"></a>
<a id="l01027"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01037"></a>
<a id="l01038"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="foldopen01061"></a>
<a id="l01061"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="l01076"></a>
<a id="l01077"></a>
<a id="l01079"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01089"></a>
<a id="l01090"></a>
<a id="l01098"></a>
<a id="l01099"></a>
<a id="l01106"></a>
<a id="l01107"></a>
<a id="l01115"></a>
<a id="l01116"></a>
<a id="l01124"></a>
<a id="l01125"></a>
<a id="l01126"></a>
<a id="l01127"></a>
<a id="foldopen01137"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01141"></a>
<a id="l01142"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="l01146"></a>
<a id="l01147"></a>
<a id="foldopen01157"></a>
<a id="l01157"></a>
<a id="l01158"></a>
<a id="l01159"></a>
<a id="l01160"></a>
<a id="l01161"></a>
<a id="l01162"></a>
<a id="l01163"></a>
<a id="l01191"></a>
<a id="foldopen01192"></a>
<a id="l01192"></a>
<a id="l01193"></a>
<a id="l01194"></a>
<a id="l01195"></a>
<a id="foldopen01212"></a>
<a id="l01212"></a>
<a id="l01213"></a>
<a id="l01214"></a>
<a id="l01215"></a>
<a id="foldopen01216"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="foldopen01221"></a>
<a id="l01221"></a>
<a id="l01222"></a>
<a id="l01223"></a>
<a id="foldopen01225"></a>
<a id="l01225"></a>
<a id="l01226"></a>
<a id="l01227"></a>
<a id="l01228"></a>
<a id="l01229"></a>
<a id="foldopen01231"></a>
<a id="l01231"></a>
<a id="l01232"></a>
<a id="l01233"></a>
<a id="l01234"></a>
<a id="foldopen01236"></a>
<a id="l01236"></a>
<a id="l01237"></a>
<a id="l01238"></a>
<a id="l01239"></a>
<a id="l01240"></a>
<a id="l01241"></a>
<a id="foldopen01243"></a>
<a id="l01243"></a>
<a id="l01244"></a>
<a id="l01245"></a>
<a id="l01246"></a>
<a id="foldopen01248"></a>
<a id="l01248"></a>
<a id="l01249"></a>
<a id="l01250"></a>
<a id="l01251"></a>
<a id="l01252"></a>
<a id="l01253"></a>
<a id="foldopen01255"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01258"></a>
<a id="l01259"></a>
<a id="l01260"></a>
<a id="foldopen01264"></a>
<a id="l01264"></a>
<a id="l01265"></a>
<a id="l01266"></a>
<a id="l01267"></a>
<a id="l01268"></a>
<a id="l01269"></a>
<a id="foldopen01276"></a>
<a id="l01276"></a>
<a id="l01277"></a>
<a id="l01278"></a>
<a id="l01279"></a>
<a id="l01280"></a>
<a id="l01281"></a>
<a id="foldopen01288"></a>
<a id="l01288"></a>
<a id="l01289"></a>
<a id="l01290"></a>
<a id="l01291"></a>
<a id="l01292"></a>
<a id="l01293"></a>
<a id="l01294"></a>
<a id="foldopen01303"></a>
<a id="l01303"></a>
<a id="l01304"></a>
<a id="l01305"></a>
<a id="l01306"></a>
<a id="l01307"></a>
<a id="l01308"></a>
<a id="l01309"></a>
<a id="foldopen01318"></a>
<a id="l01318"></a>
<a id="l01319"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="l01322"></a>
<a id="foldopen01323"></a>
<a id="l01323"></a>
<a id="l01324"></a>
<a id="l01325"></a>
<a id="l01326"></a>
<a id="l01358"></a>
<a id="l01359"></a>
<a id="l01360"></a>
<a id="l01361"></a>
<a id="l01374"></a>
<a id="l01375"></a>
<a id="l01376"></a>
<a id="l01384"></a>
<a id="l01385"></a>
<a id="l01405"></a>
<a id="l01406"></a>
<a id="l01407"></a>
<a id="l01408"></a>
<a id="foldopen01422"></a>
<a id="l01422"></a>
<a id="l01447"></a>
<a id="l01448"></a>
<a id="l01467"></a>
<a id="l01468"></a>
<a id="l01469"></a>
<a id="l01485"></a>
<a id="l01486"></a>
<a id="l01487"></a>
<a id="l01498"></a>
<a id="l01499"></a>
<a id="l01535"></a>
<a id="l01536"></a>
<a id="l01537"></a>
<a id="l01538"></a>
<a id="l01551"></a>
<a id="l01552"></a>
<a id="l01553"></a>
<a id="l01565"></a>
<a id="l01566"></a>
<a id="l01578"></a>
<a id="l01579"></a>
<a id="foldopen01581"></a>
<a id="l01581"></a>
<a id="l01583"></a>
<a id="l01584"></a>
<a id="l01586"></a>
<a id="l01587"></a>
<a id="l01588"></a>
<a id="foldopen01590"></a>
<a id="l01590"></a>
<a id="l01592"></a>
<a id="l01593"></a>
<a id="l01595"></a>
<a id="l01596"></a>
<a id="l01598"></a>
<a id="l01599"></a>
<a id="l01600"></a>
<a id="foldopen01602"></a>
<a id="l01602"></a>
<a id="l01604"></a>
<a id="l01605"></a>
<a id="l01607"></a>
<a id="l01608"></a>
<a id="l01615"></a>
<a id="l01616"></a>
<a id="l01637"></a>
<a id="l01638"></a>
<a id="l01640"></a>
<a id="l01641"></a>
<a id="l01643"></a>
<a id="l01644"></a>
<a id="l01645"></a>
<a id="l01655"></a>
<a id="l01656"></a>
<a id="l01657"></a>
<a id="l01673"></a>
<a id="l01674"></a>
<a id="l01675"></a>
<a id="l01689"></a>
<a id="l01690"></a>
<a id="l01691"></a>
<a id="l01706"></a>
<a id="l01707"></a>
<a id="l01708"></a>
<a id="l01728"></a>
<a id="l01729"></a>
<a id="foldopen01740"></a>
<a id="l01740"></a>
<a id="l01742"></a>
<a id="l01743"></a>
<a id="l01745"></a>
<a id="l01746"></a>
<a id="l01748"></a>
<a id="l01749"></a>
<a id="l01751"></a>
<a id="l01752"></a>
<a id="l01753"></a>
<a id="l01769"></a>
<a id="l01770"></a>
<a id="l01771"></a>
<a id="l01789"></a>
<a id="l01790"></a>
<a id="l01802"></a>
<a id="l01803"></a>
<a id="foldopen01816"></a>
<a id="l01816"></a>
<a id="l01818"></a>
<a id="l01819"></a>
<a id="l01821"></a>
<a id="l01822"></a>
<a id="l01824"></a>
<a id="l01825"></a>
<a id="l01827"></a>
<a id="l01828"></a>
<a id="l01830"></a>
<a id="l01831"></a>
<a id="l01837"></a>
<a id="l01838"></a>
<a id="l01845"></a>
<a id="l01846"></a>
<a id="l01848"></a>
<a id="l01849"></a>
<a id="l01851"></a>
<a id="l01852"></a>
<a id="l01854"></a>
<a id="l01855"></a>
<a id="l01857"></a>
<a id="l01858"></a>
<a id="l01859"></a>
<a id="l01860"></a>
<a id="l01861"></a>
<a id="foldopen01872"></a>
<a id="l01872"></a>
<a id="l01874"></a>
<a id="l01875"></a>
<a id="l01877"></a>
<a id="l01878"></a>
<a id="l01880"></a>
<a id="l01881"></a>
<a id="l01882"></a>
<a id="foldopen01894"></a>
<a id="l01894"></a>
<a id="l01896"></a>
<a id="l01897"></a>
<a id="l01899"></a>
<a id="l01900"></a>
<a id="l01906"></a>
<a id="l01907"></a>
<a id="l01913"></a>
<a id="l01914"></a>
<a id="l01916"></a>
<a id="l01917"></a>
<a id="l01919"></a>
<a id="l01920"></a>
<a id="l01922"></a>
<a id="l01923"></a>
<a id="l01924"></a>
<a id="l01925"></a>
<a id="foldopen01933"></a>
<a id="l01933"></a>
<a id="l01935"></a>
<a id="l01936"></a>
<a id="l01937"></a>
<a id="l01956"></a>
<a id="foldopen01957"></a>
<a id="l01957"></a>
<a id="l01968"></a>
<a id="l01969"></a>
<a id="l01970"></a>
<a id="l01981"></a>
<a id="l01982"></a>
<a id="l01983"></a>
<a id="l01997"></a>
<a id="l01998"></a>
<a id="l01999"></a>
<a id="l02000"></a>
<a id="l02011"></a>
<a id="l02012"></a>
<a id="l02013"></a>
<a id="l02024"></a>
<a id="l02025"></a>
<a id="l02033"></a>
<a id="l02034"></a>
<a id="l02035"></a>
<a id="l02036"></a>
<a id="l02037"></a>
<a id="l02038"></a>
<a id="foldopen02040"></a>
<a id="l02040"></a>
<a id="l02042"></a>
<a id="l02043"></a>
<a id="l02050"></a>
<a id="l02051"></a>
<a id="l02057"></a>
<a id="l02058"></a>
<a id="l02060"></a>
<a id="l02061"></a>
<a id="l02063"></a>
<a id="l02064"></a>
<a id="l02066"></a>
<a id="l02067"></a>
<a id="l02069"></a>
<a id="l02070"></a>
<a id="l02072"></a>
<a id="l02073"></a>
<a id="l02074"></a>
<a id="foldopen02086"></a>
<a id="l02086"></a>
<a id="l02093"></a>
<a id="l02094"></a>
<a id="l02102"></a>
<a id="l02103"></a>
<a id="l02105"></a>
<a id="l02106"></a>
<a id="l02114"></a>
<a id="l02115"></a>
<a id="l02122"></a>
<a id="l02123"></a>
<a id="l02124"></a>
<a id="l02136"></a>
<a id="l02137"></a>
<a id="l02150"></a>
<a id="l02151"></a>
<a id="foldopen02153"></a>
<a id="l02153"></a>
<a id="l02155"></a>
<a id="l02156"></a>
<a id="l02158"></a>
<a id="l02159"></a>
<a id="l02161"></a>
<a id="l02162"></a>
<a id="l02164"></a>
<a id="l02165"></a>
<a id="l02166"></a>
<a id="l02175"></a>
<a id="l02176"></a>
<a id="l02177"></a>
<a id="l02186"></a>
<a id="l02187"></a>
<a id="l02188"></a>
<a id="l02205"></a>
<a id="l02206"></a>
<a id="l02207"></a>
<a id="l02224"></a>
<a id="l02225"></a>
<a id="l02240"></a>
<a id="l02241"></a>
<a id="l02252"></a>
<a id="l02253"></a>
<a id="l02263"></a>
<a id="l02264"></a>
<a id="l02274"></a>
<a id="l02275"></a>
<a id="foldopen02277"></a>
<a id="l02277"></a>
<a id="l02279"></a>
<a id="l02280"></a>
<a id="l02286"></a>
<a id="l02287"></a>
<a id="l02294"></a>
<a id="l02295"></a>
<a id="l02302"></a>
<a id="l02303"></a>
<a id="l02305"></a>
<a id="l02306"></a>
<a id="l02313"></a>
<a id="l02314"></a>
<a id="l02321"></a>
<a id="l02322"></a>
<a id="l02323"></a>
<a id="foldopen02334"></a>
<a id="l02334"></a>
<a id="l02341"></a>
<a id="l02342"></a>
<a id="l02349"></a>
<a id="l02350"></a>
<a id="l02352"></a>
<a id="l02353"></a>
<a id="l02354"></a>
<a id="l02367"></a>
<a id="l02368"></a>
<a id="l02369"></a>
<a id="l02370"></a>
<a id="l02371"></a>
<a id="l02384"></a>
<a id="l02385"></a>
<a id="l02386"></a>
<a id="l02387"></a>
<a id="l02401"></a>
<a id="l02402"></a>
<a id="l02403"></a>
<a id="l02404"></a>
<a id="l02418"></a>
<a id="l02419"></a>
<a id="l02433"></a>
<a id="l02434"></a>
<a id="l02446"></a>
<a id="l02447"></a>
<a id="l02455"></a>
<a id="l02456"></a>
<a id="l02457"></a>
<a id="foldopen02458"></a>
<a id="l02458"></a>
<a id="l02460"></a>
<a id="l02461"></a>
<a id="l02463"></a>
<a id="l02464"></a>
<a id="l02466"></a>
<a id="l02467"></a>
<a id="l02469"></a>
<a id="l02470"></a>
<a id="l02476"></a>
<a id="l02477"></a>
<a id="l02491"></a>
<a id="l02492"></a>
<a id="l02493"></a>
<a id="foldopen02494"></a>
<a id="l02494"></a>
<a id="l02496"></a>
<a id="l02497"></a>
<a id="l02505"></a>
<a id="l02506"></a>
<a id="l02507"></a>
<a id="foldopen02509"></a>
<a id="l02509"></a>
<a id="l02511"></a>
<a id="l02512"></a>
<a id="l02514"></a>
<a id="l02515"></a>
<a id="l02524"></a>
<a id="l02525"></a>
<a id="l02534"></a>
<a id="l02535"></a>
<a id="l02542"></a>
<a id="l02543"></a>
<a id="l02549"></a>
<a id="l02550"></a>
<a id="l02556"></a>
<a id="l02557"></a>
<a id="l02558"></a>
<a id="foldopen02560"></a>
<a id="l02560"></a>
<a id="l02567"></a>
<a id="l02568"></a>
<a id="l02570"></a>
<a id="l02571"></a>
<a id="l02577"></a>
<a id="l02578"></a>
<a id="l02584"></a>
<a id="l02585"></a>
<a id="l02594"></a>
<a id="l02595"></a>
<a id="l02604"></a>
<a id="l02605"></a>
<a id="l02611"></a>
<a id="l02612"></a>
<a id="l02614"></a>
<a id="l02615"></a>
<a id="l02617"></a>
<a id="l02618"></a>
<a id="l02634"></a>
<a id="l02635"></a>
<a id="l02636"></a>
<a id="foldopen02647"></a>
<a id="l02647"></a>
<a id="l02648"></a>
<a id="l02655"></a>
<a id="l02656"></a>
<a id="l02657"></a>
<a id="l02659"></a>
<a id="l02660"></a>
<a id="l02661"></a>
<a id="l02662"></a>
<a id="l02663"></a>
<a id="foldopen02672"></a>
<a id="l02672"></a>
<a id="l02673"></a>
<a id="l02674"></a>
<a id="l02675"></a>
<a id="l02676"></a>
<a id="l02677"></a>
<a id="l02678"></a>
<a id="l02679"></a>
<a id="l02680"></a>
<a id="l02681"></a>
<a id="l02682"></a>
<a id="foldopen02691"></a>
<a id="l02691"></a>
<a id="l02692"></a>
<a id="l02693"></a>
<a id="l02694"></a>
<a id="l02695"></a>
<a id="foldopen02699"></a>
<a id="l02699"></a>
<a id="l02700"></a>
<a id="l02701"></a>
<a id="l02702"></a>
<a id="l02703"></a>
<a id="foldopen02709"></a>
<a id="l02709"></a>
<a id="l02710"></a>
<a id="l02711"></a>
<a id="l02712"></a>
<a id="l02713"></a>
<a id="l02714"></a>
<a id="l02715"></a>
<a id="foldopen02722"></a>
<a id="l02722"></a>
<a id="l02723"></a>
<a id="l02724"></a>
<a id="l02725"></a>
<a id="l02726"></a>
<a id="foldopen02733"></a>
<a id="l02733"></a>
<a id="l02734"></a>
<a id="l02735"></a>
<a id="l02736"></a>
<a id="l02737"></a>
<a id="l02738"></a>
<a id="l02739"></a>
<a id="foldopen02744"></a>
<a id="l02744"></a>
<a id="l02745"></a>
<a id="l02746"></a>
<a id="l02747"></a>
<a id="l02748"></a>
<a id="l02749"></a>
<a id="l02750"></a>
<a id="foldopen02758"></a>
<a id="l02758"></a>
<a id="l02759"></a>
<a id="l02760"></a>
<a id="l02761"></a>
<a id="l02762"></a>
<a id="l02763"></a>
<a id="l02764"></a>
<a id="l02802"></a>
<a id="l02803"></a>
<a id="l02813"></a>
<a id="l02814"></a>
<a id="l02828"></a>
<a id="l02829"></a>
<a id="l02837"></a>
<a id="l02838"></a>
<a id="l02853"></a>
<a id="l02854"></a>
<a id="l02869"></a>
<a id="l02870"></a>
<a id="l02883"></a>
<a id="l02884"></a>
<a id="l02900"></a>
<a id="l02901"></a>
<a id="l02918"></a>
<a id="l02919"></a>
<a id="l02939"></a>
<a id="l02940"></a>
<a id="l02941"></a>
<a id="l02942"></a>
<a id="foldopen02944"></a>
<a id="l02944"></a>
<a id="l02946"></a>
<a id="l02947"></a>
<a id="l02949"></a>
<a id="l02950"></a>
<a id="l02951"></a>
<a id="foldopen02953"></a>
<a id="l02953"></a>
<a id="l02957"></a>
<a id="l02958"></a>
<a id="l02960"></a>
<a id="l02961"></a>
<a id="l02962"></a>
<a id="l02995"></a>
<a id="l02996"></a>
<a id="l03024"></a>
<a id="l03025"></a>
<a id="l03026"></a>
<a id="l03037"></a>
<a id="l03038"></a>
<a id="foldopen03040"></a>
<a id="l03040"></a>
<a id="l03042"></a>
<a id="l03043"></a>
<a id="l03044"></a>
<a id="l03053"></a>
<a id="l03054"></a>
<a id="l03055"></a>
<a id="l03056"></a>
<a id="foldopen03058"></a>
<a id="l03058"></a>
<a id="l03060"></a>
<a id="l03062"></a>
<a id="l03069"></a>
<a id="l03070"></a>
<a id="l03071"></a>
<a id="l03092"></a>
<a id="l03093"></a>
<a id="l03109"></a>
<a id="l03110"></a>
<a id="l03111"></a>
<a id="foldopen03121"></a>
<a id="l03121"></a>
<a id="l03127"></a>
<a id="l03128"></a>
<a id="l03130"></a>
<a id="l03131"></a>
<a id="l03137"></a>
<a id="l03138"></a>
<a id="l03139"></a>
<a id="l03150"></a>
<a id="l03151"></a>
<a id="l03152"></a>
<a id="foldopen03161"></a>
<a id="l03161"></a>
<a id="l03171"></a>
<a id="l03172"></a>
<a id="l03179"></a>
<a id="l03180"></a>
<a id="l03182"></a>
<a id="l03183"></a>
<a id="l03185"></a>
<a id="l03186"></a>
<a id="l03187"></a>
<a id="l03200"></a>
<a id="l03201"></a>
<a id="l03202"></a>
<a id="l03203"></a>
<a id="l03216"></a>
<a id="l03217"></a>
<a id="l03221"></a>
<a id="l03222"></a>
<a id="l03223"></a>
<a id="l03224"></a>
<a id="l03228"></a>
<a id="l03229"></a>
<a id="aaddr_8h_html"></a>
<a id="abluetooth_2crypto_8h_html"></a>
<a id="aclassic_8h_html"></a>
<a id="adata_8h_html"></a>
<a id="agap_8h_html"></a>
<a id="agroup__bt__gap__defines_html_ga100e1c20813630848a1a80390e8a06a0"></a>
<a id="agroup__bt__gap__defines_html_gae9356673ee78d9abb27891738344513a"></a>
<a id="agroup__bt__gap_html_ga0532ed768ab4f9d69c202066d2f87e66"></a>
<a id="agroup__bt__gap_html_ga061bf84b989b2c96ab51d2ca0debb017"></a>
<a id="agroup__bt__gap_html_ga06d0ae35cbf4382679cc3cfe612cee4d"></a>
<a id="agroup__bt__gap_html_ga07e4510de7e72c6ed6196b3da9fb40be"></a>
<a id="agroup__bt__gap_html_ga08f872078045bbef4aca19761f25eeb8"></a>
<a id="agroup__bt__gap_html_ga0a58e5a050170e84a80f8d5bb3516ec7"></a>
<a id="agroup__bt__gap_html_ga0f23f4ed48e8679646f247ea0d687094"></a>
<a id="agroup__bt__gap_html_ga100efac4a49984e06202c63c4e5955cd"></a>
<a id="agroup__bt__gap_html_ga1776e310b9d80898e6b32d50c4fe0b49"></a>
<a id="agroup__bt__gap_html_ga1aabdb81cb1a1841ff0fb91d849123fc"></a>
<a id="agroup__bt__gap_html_ga1b15206fc552d597c12af369d48ff7d5"></a>
<a id="agroup__bt__gap_html_ga1c53d22b6e2dee38c825c58f3eeee9b4"></a>
<a id="agroup__bt__gap_html_ga1c864c4b183f9a86c9f70a11471c5b15"></a>
<a id="agroup__bt__gap_html_ga27c4961f3c7270a7f1caeadb4107854b"></a>
<a id="agroup__bt__gap_html_ga296d1adf3c9ed2f2c65bb75b887d59ee"></a>
<a id="agroup__bt__gap_html_ga309a67de79cc215db1d33251f267f361"></a>
<a id="agroup__bt__gap_html_ga35b76ea7ce79721e47ca4164e08b2dfb"></a>
<a id="agroup__bt__gap_html_ga3dc0c6a0c6a77f4db63ee2ff8329a4c5"></a>
<a id="agroup__bt__gap_html_ga40f2f7fdb09aba3c5137f680e67792f0"></a>
<a id="agroup__bt__gap_html_ga453074db3964f1b57b92ac7afb0b4fac"></a>
<a id="agroup__bt__gap_html_ga4ee87bbf79e6ac844d14c3dafb2dadf4"></a>
<a id="agroup__bt__gap_html_ga5398783ab4a5dc854b18e37fb10774eb"></a>
<a id="agroup__bt__gap_html_ga544ccde35638d8f580942d830fe9f242"></a>
<a id="agroup__bt__gap_html_ga5909bd768c23a19a42a660e3b814c981"></a>
<a id="agroup__bt__gap_html_ga59532b37412b1b93f81cf5cc1bab0534"></a>
<a id="agroup__bt__gap_html_ga59e9fc635846ab92af19d483de58ed88"></a>
<a id="agroup__bt__gap_html_ga5b5e51f79896d674bf6b70b2251e79d4"></a>
<a id="agroup__bt__gap_html_ga62310a27f7fea925dfcf3abd7c454787"></a>
<a id="agroup__bt__gap_html_ga650faa2a86f54499f4bc5a8657a55a87"></a>
<a id="agroup__bt__gap_html_ga652eef01e5256e0d820cd1f4db877429"></a>
<a id="agroup__bt__gap_html_ga6bb77c0808c761753650cde28ddb013e"></a>
<a id="agroup__bt__gap_html_ga731f4b37a9e5cc13a6816ea23f751b0b"></a>
<a id="agroup__bt__gap_html_ga7486aab863ca497a50dacf81657f48d4"></a>
<a id="agroup__bt__gap_html_ga7a595421c232b15ad96b52f0300fd960"></a>
<a id="agroup__bt__gap_html_ga7de30fe5040b85bb9212e3a8fec4ac45"></a>
<a id="agroup__bt__gap_html_ga8046c2b06d3dad0d6c8184de492517d2"></a>
<a id="agroup__bt__gap_html_ga80e870fa1de40c404c64624bef439067"></a>
<a id="agroup__bt__gap_html_ga820c5f3721e72662e558cc4576b6111b"></a>
<a id="agroup__bt__gap_html_ga83126917373c0bcaa24964dd1d8bde46"></a>
<a id="agroup__bt__gap_html_ga8d05bd864d98b5b43595eb256e464024"></a>
<a id="agroup__bt__gap_html_ga9a406ebfefac3dd09935a4ae0e317817"></a>
<a id="agroup__bt__gap_html_ga9ab41e118b5496c196e56b8b5d023275"></a>
<a id="agroup__bt__gap_html_gaa0658bd53df1d5e8e89e13330e4fd0ae"></a>
<a id="agroup__bt__gap_html_gaa0c218ff3c78b26dcfaa726ee30267a6"></a>
<a id="agroup__bt__gap_html_gaa26f90b188caa50ca12247b7911a0a5f"></a>
<a id="agroup__bt__gap_html_gaa2de1a1ab523606b36a4c445fb0c3b84"></a>
<a id="agroup__bt__gap_html_gaa72029a2759123ec776061d2e80bf3a1"></a>
<a id="agroup__bt__gap_html_gaa8bf6854e7ad1fe7e0805737576e5d1a"></a>
<a id="agroup__bt__gap_html_gaad0039d4b524a0eef31158dc9b24a497"></a>
<a id="agroup__bt__gap_html_gaad380b7f8984f8522c1b79f9bdc04905"></a>
<a id="agroup__bt__gap_html_gaae6b8583f7d5457f20b03dccd146425e"></a>
<a id="agroup__bt__gap_html_gab1576c66b08dc855b2d17fc562f36724"></a>
<a id="agroup__bt__gap_html_gab4b5773898e2a1eef21557915a21c996"></a>
<a id="agroup__bt__gap_html_gabb3353edc8a3a8d29a0370049b20cbe4"></a>
<a id="agroup__bt__gap_html_gabc115fd3fff6d00ae878a31613bf70aa"></a>
<a id="agroup__bt__gap_html_gabfaf265a48dd09ea02d114e2023c14a6"></a>
<a id="agroup__bt__gap_html_gac06c9f55cf1da46e0d64b4d9af984ecb"></a>
<a id="agroup__bt__gap_html_gac2718f2128b3f8c79b12d760771c8378"></a>
<a id="agroup__bt__gap_html_gac45d16bfe21c3c38e834c293e5ebc42b"></a>
<a id="agroup__bt__gap_html_gac5e19c26b53a08dadb8efa7ecc692ad6"></a>
<a id="agroup__bt__gap_html_gac87df899d1e363c63162988157ee6d00"></a>
<a id="agroup__bt__gap_html_gac8bb3609a3d6da69ff736809e45f5c8a"></a>
<a id="agroup__bt__gap_html_gac942d7e3cae8fca22080f93bf9528ee9"></a>
<a id="agroup__bt__gap_html_gac96199a4e5e6cfb789c1bd1c0e67d6fe"></a>
<a id="agroup__bt__gap_html_gaceabbbe6e844650f791010e53c9df6a4"></a>
<a id="agroup__bt__gap_html_gad02b855dd7a26e3910b247fa73f19297"></a>
<a id="agroup__bt__gap_html_gad2e3caef88d52d720e8e4d21df767b02"></a>
<a id="agroup__bt__gap_html_gad731f829b3566be3e56485b2a64f80b1"></a>
<a id="agroup__bt__gap_html_gad922d894b25e86de3f81ce77200a13fd"></a>
<a id="agroup__bt__gap_html_gae11eb8ad254418c38a0e8689df25a159"></a>
<a id="agroup__bt__gap_html_gae60a45dde6b4d9f4c54a2a6070254f11"></a>
<a id="agroup__bt__gap_html_gaf0729453790aab1bd3d52c623be3b35a"></a>
<a id="agroup__bt__gap_html_gaf0f436c55482d9429f674303ae3aa815"></a>
<a id="agroup__bt__gap_html_gaf6cd906690a51ebed04bea4f4ef716ff"></a>
<a id="agroup__bt__gap_html_gaf81a1dd7a628d1a2f25c6b53b0679809"></a>
<a id="agroup__bt__gap_html_gaf8b28f54c68251024b869f3b0d1c1282"></a>
<a id="agroup__bt__gap_html_gaf980473379afa477c09e19912d40d29e"></a>
<a id="agroup__bt__gap_html_gafbf81dab68b0e484d4742471c722fc28"></a>
<a id="agroup__bt__gap_html_gafd0e7ccca93a8347a4ca6cca88e77899"></a>
<a id="agroup__bt__gap_html_gga544ccde35638d8f580942d830fe9f242a4423f4792711b21cf38a4e63c148760d"></a>
<a id="agroup__bt__gap_html_gga544ccde35638d8f580942d830fe9f242afe851bf904c1cfed3ff10a57430d6a07"></a>
<a id="agroup__bt__gap_html_gga6bb77c0808c761753650cde28ddb013ea492cf25dc85090cfa72d5e2bdc0917f3"></a>
<a id="agroup__bt__gap_html_gga6bb77c0808c761753650cde28ddb013eac26ccfbb5c715b515ef82c1993eff03b"></a>
<a id="agroup__bt__gap_html_gga6bb77c0808c761753650cde28ddb013ead690730da823fcb31f102f154a23b01c"></a>
<a id="agroup__bt__gap_html_gga820c5f3721e72662e558cc4576b6111ba2694870b7ebd2dcd0b3834367f7d7061"></a>
<a id="agroup__bt__gap_html_gga820c5f3721e72662e558cc4576b6111ba3f0be549ca5cac1cfbdec2f2227e73dc"></a>
<a id="agroup__bt__gap_html_gga820c5f3721e72662e558cc4576b6111ba433ae469b27e820fdfd2a1d562010991"></a>
<a id="agroup__bt__gap_html_gga820c5f3721e72662e558cc4576b6111bab0725048806858083be9ab3fcd9a36ed"></a>
<a id="agroup__bt__gap_html_gga820c5f3721e72662e558cc4576b6111bad924f620ed6fdadbbea03f8e343b9d0c"></a>
<a id="agroup__bt__gap_html_gga820c5f3721e72662e558cc4576b6111baed2f78d682b5fbd1adf89c2f005e4f48"></a>
<a id="agroup__bt__gap_html_gga820c5f3721e72662e558cc4576b6111baef90aceabc3f9d0b17b7f3415152fca2"></a>
<a id="agroup__bt__gap_html_ggaad0039d4b524a0eef31158dc9b24a497a1d636d176d18199b7d5bcb17865b3a1c"></a>
<a id="agroup__bt__gap_html_ggaad0039d4b524a0eef31158dc9b24a497a1fcee00e6de549746f81de0bf43caeab"></a>
<a id="agroup__bt__gap_html_ggaad0039d4b524a0eef31158dc9b24a497a32a025f5c47db4957e72d292e748eda9"></a>
<a id="agroup__bt__gap_html_ggab4b5773898e2a1eef21557915a21c996a0af65ac48e068f7e6f1815cb151d4394"></a>
<a id="agroup__bt__gap_html_ggab4b5773898e2a1eef21557915a21c996a16f171c649dd090333e9822a92b4bbdb"></a>
<a id="agroup__bt__gap_html_ggab4b5773898e2a1eef21557915a21c996a79cdd7e96e41f4236642edfbcb1b666d"></a>
<a id="agroup__bt__gap_html_ggab4b5773898e2a1eef21557915a21c996a7ff0c79b2675e7b7512379e2cbedc0a6"></a>
<a id="agroup__bt__gap_html_ggab4b5773898e2a1eef21557915a21c996aad3f19e5849b6d6813fa88257082e185"></a>
<a id="agroup__bt__gap_html_ggab4b5773898e2a1eef21557915a21c996af7a25b6790b138b2b88de3c7d81cb0ae"></a>
<a id="agroup__bt__gap_html_ggac942d7e3cae8fca22080f93bf9528ee9a0f52e38e513ec7eefcbc5c86c36f002e"></a>
<a id="agroup__bt__gap_html_ggac942d7e3cae8fca22080f93bf9528ee9a5c702876d70d5eadc4df6e59d96b8320"></a>
<a id="agroup__bt__gap_html_ggac942d7e3cae8fca22080f93bf9528ee9a99034652a92249e6d04065d68352020b"></a>
<a id="agroup__bt__gap_html_ggac942d7e3cae8fca22080f93bf9528ee9a9ec2b0c346c2cab7f61c2efcc8e37db2"></a>
<a id="agroup__bt__gap_html_ggac942d7e3cae8fca22080f93bf9528ee9aaa256e560f013eb74415d817154b8f4e"></a>
<a id="agroup__bt__gap_html_ggac942d7e3cae8fca22080f93bf9528ee9ae35a6eb572a2842e4cc2fc3677e19b53"></a>
<a id="agroup__bt__gap_html_ggac942d7e3cae8fca22080f93bf9528ee9ae9a88caa6a83da8b1697a6167629bf7e"></a>
<a id="agroup__bt__gap_html_ggac942d7e3cae8fca22080f93bf9528ee9aeeef50a544edc104b39e4ef0c9a58d6c"></a>
<a id="agroup__bt__gap_html_ggae60a45dde6b4d9f4c54a2a6070254f11a38cebc2ae885ff630b34c603e2ec6403"></a>
<a id="agroup__bt__gap_html_ggae60a45dde6b4d9f4c54a2a6070254f11a9524537e4cb726f4ff10ba93381bb27f"></a>
<a id="agroup__bt__gap_html_ggae60a45dde6b4d9f4c54a2a6070254f11aa2c689d726eacfb18d87655b1f587518"></a>
<a id="agroup__bt__gap_html_ggaf980473379afa477c09e19912d40d29ea731c507ed451eb6f8f8372849185b006"></a>
<a id="agroup__bt__gap_html_ggaf980473379afa477c09e19912d40d29eaf202213813092ba298cd046aed687f22"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28a1563b053f457833d1a3d11c8dc4d394b"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28a185e0f884f8b0ce79625448638de8fab"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28a22958d8539d661ad7ca8d3f1173e7e5e"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28a407cf5ae358d3c00dd7e47dfaad3ec6e"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28a807ba316edc49c8448a8ff7d497173f5"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28a89f7494620236c976bf1a76a880e2a28"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28a928b376123819cb0a69fbb5b35608dbf"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28a9a35ede118224d6ed17f252fff6bb47e"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28aa6a61768ad4102f199d3970791118bb8"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28ab46741616f8bfe50c4b492d1f7970779"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28ab9ee87ad3a24312174ae46f904fe9c56"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28abd9cb02691d7e025fe3fea9a80123275"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28abdcf1c80662061fa30575e1f9fc6cf6f"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28ad01c4962a350d3218ba0cabd713708b1"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28ad5efef3d01731110dbd71d5a5dc9baaf"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28ae60eafe69ef10b84f61a1f4accf789c9"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28ae864aefcdfbecaffe823b9b144fe0a6b"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28aecff4fe3ac3d1fba3f6fa76c77713859"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28afd164ec5476f5e2d9aedf50032946872"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="ahci__types_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astring_8h_html"></a>
<a id="astructbt__addr__le__t_html"></a>
<a id="astructbt__bond__info_html"></a>
<a id="astructbt__bond__info_html_a6b328ce30fd53bb73ecd8e033bb91d1f"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__data_html"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html"></a>
<a id="astructbt__iso__biginfo_html"></a>
<a id="astructbt__le__adv__param_html"></a>
<a id="astructbt__le__adv__param_html_a1c09c2bcf9600a644e194ecd3367d200"></a>
<a id="astructbt__le__adv__param_html_a2a978c60153eb03697769bc72928f4ef"></a>
<a id="astructbt__le__adv__param_html_a4cf31f54f067fffa3c848adc2ffd7119"></a>
<a id="astructbt__le__adv__param_html_a6e2f0e1b76495afe7fe661e8698d0909"></a>
<a id="astructbt__le__adv__param_html_a9911e9bfc97ff0c48a6decae3f922e95"></a>
<a id="astructbt__le__adv__param_html_aca8ff5a4f5d29184535162f007b2d39e"></a>
<a id="astructbt__le__adv__param_html_af957bd92b949536af2b2db0db7b2b425"></a>
<a id="astructbt__le__adv__param_html_afeba6973dca99d8ee818fdde0c22cb59"></a>
<a id="astructbt__le__ext__adv__cb_html"></a>
<a id="astructbt__le__ext__adv__cb_html_a251ea84adf8b6cc14bae051d74edc1fe"></a>
<a id="astructbt__le__ext__adv__cb_html_a277dc3269741d40b644ae3c777198fab"></a>
<a id="astructbt__le__ext__adv__cb_html_a6b26be418789c6e5087dab1100cb56a8"></a>
<a id="astructbt__le__ext__adv__cb_html_a7aad0fbd8e531e70f661500c338d870e"></a>
<a id="astructbt__le__ext__adv__cb_html_a85b8887c9ef443d18b71e9561e7dde60"></a>
<a id="astructbt__le__ext__adv__cb_html_ab6452d9b3449847bf009c3d43c051922"></a>
<a id="astructbt__le__ext__adv__connected__info_html"></a>
<a id="astructbt__le__ext__adv__connected__info_html_a157efa6206b418f768582107c566fde2"></a>
<a id="astructbt__le__ext__adv__info_html"></a>
<a id="astructbt__le__ext__adv__info_html_a06aa727cd2523914bc7509713585bffd"></a>
<a id="astructbt__le__ext__adv__info_html_a0ae2f62772732a6db460d4a0127dd17a"></a>
<a id="astructbt__le__ext__adv__info_html_a0dd0aa8a26fe1ef5813fa07732c5c4c9"></a>
<a id="astructbt__le__ext__adv__info_html_a19877c440137814ec0e4aa1a1270f6fe"></a>
<a id="astructbt__le__ext__adv__info_html_a485e4a8124fddee897fe744836cbfb24"></a>
<a id="astructbt__le__ext__adv__info_html_ad802b5af32353d757a84e5039c973f3a"></a>
<a id="astructbt__le__ext__adv__scanned__info_html"></a>
<a id="astructbt__le__ext__adv__scanned__info_html_a4431f157891d2c1a7d0e40f7e879ac3d"></a>
<a id="astructbt__le__ext__adv__sent__info_html"></a>
<a id="astructbt__le__ext__adv__sent__info_html_a80f661efd35b069c2f8700851e9429a2"></a>
<a id="astructbt__le__ext__adv__start__param_html"></a>
<a id="astructbt__le__ext__adv__start__param_html_a80bb1ef4316dd75ea1268241333f4346"></a>
<a id="astructbt__le__ext__adv__start__param_html_ab45ae0bfdb144071efcc64c30648388f"></a>
<a id="astructbt__le__ext__adv_html"></a>
<a id="astructbt__le__local__features_html"></a>
<a id="astructbt__le__local__features_html_a19cecbe8574229844e9416842bc42b0c"></a>
<a id="astructbt__le__local__features_html_a22ce370b338f687ce6860435cc0ec9c5"></a>
<a id="astructbt__le__local__features_html_a516ca4b44a693f045a45eedf375c9ea6"></a>
<a id="astructbt__le__local__features_html_a8b413bf80ccd7e3af67f7e1c28a1beeb"></a>
<a id="astructbt__le__local__features_html_a932af365332149ec620413a8504d342c"></a>
<a id="astructbt__le__local__features_html_aa2dc6363feab37af195ee192f2b906f1"></a>
<a id="astructbt__le__local__features_html_ac86ae6974627ddb2e34b0d028cdcfe32"></a>
<a id="astructbt__le__local__features_html_ad7b95feb82c1dece8bb8bb7969efa2ec"></a>
<a id="astructbt__le__oob__sc__data_html"></a>
<a id="astructbt__le__oob__sc__data_html_a9bd93f1e9e41e241d0f84ae16ae47ba1"></a>
<a id="astructbt__le__oob__sc__data_html_afa64bcc048d0e8709e262e2848a39d2c"></a>
<a id="astructbt__le__oob_html"></a>
<a id="astructbt__le__oob_html_a17cfed7683efbf5b5954847d655d7424"></a>
<a id="astructbt__le__oob_html_a80ccd4ab120a880adfff9aba3b19b4fd"></a>
<a id="astructbt__le__per__adv__data__request_html"></a>
<a id="astructbt__le__per__adv__data__request_html_a766991899bc3e689adec36bf1f12e802"></a>
<a id="astructbt__le__per__adv__data__request_html_a779ed161919c3117f6ce165deb0a9b0a"></a>
<a id="astructbt__le__per__adv__param_html"></a>
<a id="astructbt__le__per__adv__param_html_a07302e13735f502b8950a92b365ef14a"></a>
<a id="astructbt__le__per__adv__param_html_a0a8606c103fd91f3222bae6c9f1204fd"></a>
<a id="astructbt__le__per__adv__param_html_a28655741c63775a274c42ad5057d4a1d"></a>
<a id="astructbt__le__per__adv__param_html_a49da44a3c0e4e866ffccffae5a9a22f7"></a>
<a id="astructbt__le__per__adv__param_html_a61308cfe72ad23372dfd2a3bd2550726"></a>
<a id="astructbt__le__per__adv__param_html_a67116b81e8ce968cf411843646801ac4"></a>
<a id="astructbt__le__per__adv__param_html_a9b80c2427171920f466601e7e8468814"></a>
<a id="astructbt__le__per__adv__param_html_af8be989979c98a17828819ec43dd0b49"></a>
<a id="astructbt__le__per__adv__response__info_html"></a>
<a id="astructbt__le__per__adv__response__info_html_a1b87ab77f5c7d4ee0c1c612bcfb424d5"></a>
<a id="astructbt__le__per__adv__response__info_html_a2db58fb452a07290ab4a50892c682837"></a>
<a id="astructbt__le__per__adv__response__info_html_a52b0c612b09cfcb3eb2ea475614c34b8"></a>
<a id="astructbt__le__per__adv__response__info_html_a7ed20f695e0d696eaab7cddc4e3c11fb"></a>
<a id="astructbt__le__per__adv__response__info_html_a83cc642c9f22c767421644e7d8233001"></a>
<a id="astructbt__le__per__adv__response__info_html_ab17f33cb713d258bf6c863a64e5aba07"></a>
<a id="astructbt__le__per__adv__response__params_html"></a>
<a id="astructbt__le__per__adv__response__params_html_a0cec222d5ba8cc9e20939d441646c913"></a>
<a id="astructbt__le__per__adv__response__params_html_a1af01d0a027fb8659615874acbd388f9"></a>
<a id="astructbt__le__per__adv__response__params_html_a3fc8ab0feb06714b28d22439cce60e41"></a>
<a id="astructbt__le__per__adv__response__params_html_aea0428083ccd5f4dccc17e494f38b7c3"></a>
<a id="astructbt__le__per__adv__subevent__data__params_html"></a>
<a id="astructbt__le__per__adv__subevent__data__params_html_a1354e9505239de3c42969138d719d775"></a>
<a id="astructbt__le__per__adv__subevent__data__params_html_a46103c988d8ac360b7e26310a0322b4e"></a>
<a id="astructbt__le__per__adv__subevent__data__params_html_a55f2da6041b538b3bc4bff38cd4d2953"></a>
<a id="astructbt__le__per__adv__subevent__data__params_html_a86d858606943a82917835a0172e88663"></a>
<a id="astructbt__le__per__adv__sync__cb_html"></a>
<a id="astructbt__le__per__adv__sync__cb_html_a1977d27941063773c953a5f1dfa9ca76"></a>
<a id="astructbt__le__per__adv__sync__cb_html_a5576248e2eaef2afebe606e05e55f05f"></a>
<a id="astructbt__le__per__adv__sync__cb_html_a656b4802f79d4a472c2367ade144d72e"></a>
<a id="astructbt__le__per__adv__sync__cb_html_a815be4343ab589df433a551663c5f4a1"></a>
<a id="astructbt__le__per__adv__sync__cb_html_aa44efa17bc28da1952785063a9baf6a9"></a>
<a id="astructbt__le__per__adv__sync__cb_html_acbd565a39918e5dfe7603a020e73daec"></a>
<a id="astructbt__le__per__adv__sync__cb_html_ad2dc168696fbd22f7e3a089ac56f62d7"></a>
<a id="astructbt__le__per__adv__sync__info_html"></a>
<a id="astructbt__le__per__adv__sync__info_html_a365a0d8577429e4ee96e977071c9a906"></a>
<a id="astructbt__le__per__adv__sync__info_html_a4d9520ea6a803f8fe4f41190f55c26e5"></a>
<a id="astructbt__le__per__adv__sync__info_html_ac10fc2e2d3ec2160db8c2aac148d18a2"></a>
<a id="astructbt__le__per__adv__sync__info_html_acc0ef26c38279c9a67f8992005c2e58a"></a>
<a id="astructbt__le__per__adv__sync__param_html"></a>
<a id="astructbt__le__per__adv__sync__param_html_a301cfd3d6e5620d29c021ababe104754"></a>
<a id="astructbt__le__per__adv__sync__param_html_a4252f2b3b453c2f9c8fbf8c35a618ff2"></a>
<a id="astructbt__le__per__adv__sync__param_html_a70795642ee94dd9e87f0cf251c095e7f"></a>
<a id="astructbt__le__per__adv__sync__param_html_ac93adedad747f61a771ac5445e486b74"></a>
<a id="astructbt__le__per__adv__sync__param_html_af9abb65547fb5bfea65f4c22963c7da0"></a>
<a id="astructbt__le__per__adv__sync__recv__info_html"></a>
<a id="astructbt__le__per__adv__sync__recv__info_html_a1591907e3cb1f4565b9d26c18bccc7d2"></a>
<a id="astructbt__le__per__adv__sync__recv__info_html_a1a9dccd6d7592868b5604ec16a5f1540"></a>
<a id="astructbt__le__per__adv__sync__recv__info_html_a21b0ca87e46c6897282ebd877e45114e"></a>
<a id="astructbt__le__per__adv__sync__recv__info_html_a5817bd4fba2c93adebcebe007650b6eb"></a>
<a id="astructbt__le__per__adv__sync__recv__info_html_a65f1a2adb7c3d740cb8262ae7f5a7c3e"></a>
<a id="astructbt__le__per__adv__sync__recv__info_html_a74f6dc1745a756faca2e323292024730"></a>
<a id="astructbt__le__per__adv__sync__recv__info_html_aa17c9d917469f121448ed4e1db485700"></a>
<a id="astructbt__le__per__adv__sync__state__info_html"></a>
<a id="astructbt__le__per__adv__sync__state__info_html_a4b0a3b7e36f935e06072304d6b92579f"></a>
<a id="astructbt__le__per__adv__sync__subevent__params_html"></a>
<a id="astructbt__le__per__adv__sync__subevent__params_html_a5ac4e81ddd63797f921105748344c125"></a>
<a id="astructbt__le__per__adv__sync__subevent__params_html_a6b23cd4b7e6a3f1d65b9a7eff85bcfb4"></a>
<a id="astructbt__le__per__adv__sync__subevent__params_html_a867c66bf09461a4369da3d250701d2ae"></a>
<a id="astructbt__le__per__adv__sync__synced__info_html"></a>
<a id="astructbt__le__per__adv__sync__synced__info_html_a0dd4b7646da0fadc48e94ff3dc91ef83"></a>
<a id="astructbt__le__per__adv__sync__synced__info_html_a5304e1826face35c506f3b8f6cad7df2"></a>
<a id="astructbt__le__per__adv__sync__synced__info_html_a5489c3038f7fff596316a456fc8d580b"></a>
<a id="astructbt__le__per__adv__sync__synced__info_html_a7bdec5d34b97602aa56c1006dbaf79c4"></a>
<a id="astructbt__le__per__adv__sync__synced__info_html_a7ca99b0596b08d153d3ba5310adab125"></a>
<a id="astructbt__le__per__adv__sync__synced__info_html_a8b7709011541e95ceaeac379cc3143bb"></a>
<a id="astructbt__le__per__adv__sync__synced__info_html_a9e01fb9462c4874a60ebc5359fe5df14"></a>
<a id="astructbt__le__per__adv__sync__synced__info_html_aaab25f36577948d55b6379abe0590c69"></a>
<a id="astructbt__le__per__adv__sync__synced__info_html_ada4cda53aa87f29d54f6cd88134efe14"></a>
<a id="astructbt__le__per__adv__sync__synced__info_html_adee2bdafa86a0c3c1dfb4660e85396a3"></a>
<a id="astructbt__le__per__adv__sync__synced__info_html_ae9a696dd9dc28b7505e406961ca89b9a"></a>
<a id="astructbt__le__per__adv__sync__term__info_html"></a>
<a id="astructbt__le__per__adv__sync__term__info_html_a2b76ccd5e4c9933f2c05db2ec5b8e2fc"></a>
<a id="astructbt__le__per__adv__sync__term__info_html_a429b8b665eacbfe9db013a571b829bac"></a>
<a id="astructbt__le__per__adv__sync__term__info_html_a7a5f2ecccaf698bad86f10d9a7d16189"></a>
<a id="astructbt__le__per__adv__sync__transfer__param_html"></a>
<a id="astructbt__le__per__adv__sync__transfer__param_html_a0b3ee6df1b409e64a064ffb6ac632cce"></a>
<a id="astructbt__le__per__adv__sync__transfer__param_html_a5bfa84c6bdacdf8893a0951a5ce71fc6"></a>
<a id="astructbt__le__per__adv__sync__transfer__param_html_a840e7cfac3a2947e5128d704067aaf7e"></a>
<a id="astructbt__le__per__adv__sync_html"></a>
<a id="astructbt__le__scan__cb_html"></a>
<a id="astructbt__le__scan__cb_html_a2f57f3fee46bd137065f4c57d0cd5157"></a>
<a id="astructbt__le__scan__cb_html_a50dbc5e7618fd488e9acb7ad8f104a63"></a>
<a id="astructbt__le__scan__cb_html_a71d73c1da28d4a27626f77d96a5b3541"></a>
<a id="astructbt__le__scan__param_html"></a>
<a id="astructbt__le__scan__param_html_a02d75322390287c3fa754bf915660d0c"></a>
<a id="astructbt__le__scan__param_html_a2f4e053d97c62b6fdf42a245908607f8"></a>
<a id="astructbt__le__scan__param_html_a37a7ee82e86a91cf7a9c2adf60bb526a"></a>
<a id="astructbt__le__scan__param_html_a3e71ce551dcc7762c29e2316996e2912"></a>
<a id="astructbt__le__scan__param_html_a67a20bc94a3d98fa10af7b5b42dde328"></a>
<a id="astructbt__le__scan__param_html_a93166af55dca71393c60cb3f7ac6d809"></a>
<a id="astructbt__le__scan__param_html_ac815b05fee8ce0dd24228305b7596207"></a>
<a id="astructbt__le__scan__recv__info_html"></a>
<a id="astructbt__le__scan__recv__info_html_a1060c5937708ff81a64f068e02fc7826"></a>
<a id="astructbt__le__scan__recv__info_html_a2addeba6d2ec8e55dc5379adf6519148"></a>
<a id="astructbt__le__scan__recv__info_html_a4df8d4e1fdd7514d170744856ebe7015"></a>
<a id="astructbt__le__scan__recv__info_html_a6189ed8453cb7907f34dc7dfaf1343bd"></a>
<a id="astructbt__le__scan__recv__info_html_a8885283f39e3ece5d7ff7d5b5d588696"></a>
<a id="astructbt__le__scan__recv__info_html_a88f677733147245ccbf861c7fc5e0f11"></a>
<a id="astructbt__le__scan__recv__info_html_a907fb7ec3c78d68da5015a8c3afc3084"></a>
<a id="astructbt__le__scan__recv__info_html_ac797291291dc7ba7ac171ed7f24f0d16"></a>
<a id="astructbt__le__scan__recv__info_html_adccb2ce5c6d228bd7f8f050088629524"></a>
<a id="astructbt__le__scan__recv__info_html_af29ddfb59e286af9ca465cbd5a91bf2d"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="astructnet__buf__simple_html_ad232efff435f425d30ac78f5abf2d8b1"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2017 Nordic Semiconductor ASA
 * Copyright (c) 2015-2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_BLUETOOTH_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_BLUETOOTH_H_


#include <stdbool.h>
#include <stdint.h>
#include <string.h>

#include <zephyr/bluetooth/gap.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/crypto.h>
#include <zephyr/bluetooth/data.h>
#include <zephyr/bluetooth/hci_types.h>
#include <zephyr/bluetooth/classic/classic.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif


#define BT_ID_DEFAULT 0

#define BT_IRK_SIZE 16U

 #if defined(CONFIG_BT_LE_EXTENDED_FEAT_SET)
 #define BT_LE_LOCAL_SUPPORTED_FEATURES_SIZE \
         (BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE + \
          (CONFIG_BT_LE_MAX_LOCAL_SUPPORTED_FEATURE_PAGE * BT_HCI_LE_BYTES_PER_FEATURE_PAGE))
 #else
 #define BT_LE_LOCAL_SUPPORTED_FEATURES_SIZE BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE
 #endif
struct bt_le_ext_adv;

struct bt_le_per_adv_sync;

/* Don't require everyone to include conn.h */
struct bt_conn;

/* Don't require everyone to include iso.h */
struct bt_iso_biginfo;

/* Don't require everyone to include direction.h */
struct bt_df_per_adv_sync_iq_samples_report;

struct bt_le_ext_adv_sent_info {
        uint8_t num_sent;
};

struct bt_le_ext_adv_connected_info {
        struct bt_conn *conn;
};

struct bt_le_ext_adv_scanned_info {
        bt_addr_le_t *addr;
};

struct bt_le_per_adv_data_request {
        uint8_t start;

        uint8_t count;
};

struct bt_le_per_adv_response_info {
        uint8_t subevent;

        uint8_t tx_status;

        int8_t tx_power;

        int8_t rssi;

        uint8_t cte_type;

        uint8_t response_slot;
};

struct bt_le_ext_adv_cb {
        void (*sent)(struct bt_le_ext_adv *adv,
                     struct bt_le_ext_adv_sent_info *info);

        void (*connected)(struct bt_le_ext_adv *adv,
                          struct bt_le_ext_adv_connected_info *info);

        void (*scanned)(struct bt_le_ext_adv *adv,
                        struct bt_le_ext_adv_scanned_info *info);

#if defined(CONFIG_BT_PRIVACY) || defined(__DOXYGEN__)
        bool (*rpa_expired)(struct bt_le_ext_adv *adv);
#endif /* defined(CONFIG_BT_PRIVACY) */

#if defined(CONFIG_BT_PER_ADV_RSP) || defined(__DOXYGEN__)
        void (*pawr_data_request)(struct bt_le_ext_adv *adv,
                                  const struct bt_le_per_adv_data_request *request);
        void (*pawr_response)(struct bt_le_ext_adv *adv, struct bt_le_per_adv_response_info *info,
                              struct net_buf_simple *buf);

#endif /* defined(CONFIG_BT_PER_ADV_RSP) */
};

typedef void (*bt_ready_cb_t)(int err);

int bt_enable(bt_ready_cb_t cb);

int bt_disable(void);

bool bt_is_ready(void);

int bt_set_name(const char *name);

const char *bt_get_name(void);

uint16_t bt_get_appearance(void);

int bt_set_appearance(uint16_t new_appearance);

void bt_id_get(bt_addr_le_t *addrs, size_t *count);

int bt_id_create(bt_addr_le_t *addr, uint8_t *irk);

int bt_id_reset(uint8_t id, bt_addr_le_t *addr, uint8_t *irk);

int bt_id_delete(uint8_t id);

int bt_id_reset_irk(uint8_t id, uint8_t *irk);

struct bt_le_local_features {
        uint8_t features[BT_LE_LOCAL_SUPPORTED_FEATURES_SIZE];

        uint64_t states;

        uint16_t acl_mtu;
        uint8_t acl_pkts;

        uint16_t iso_mtu;
        uint8_t iso_pkts;

        uint8_t rl_size;

        uint16_t max_adv_data_len;
};

int bt_le_get_local_features(struct bt_le_local_features *local_features);

enum bt_le_adv_opt {
        BT_LE_ADV_OPT_NONE = 0,

        BT_LE_ADV_OPT_CONN = BIT(0) | BIT(1),

        BT_LE_ADV_OPT_USE_IDENTITY = BIT(2),

        BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY = BIT(4),

        BT_LE_ADV_OPT_DIR_ADDR_RPA = BIT(5),

        BT_LE_ADV_OPT_FILTER_SCAN_REQ = BIT(6),

        BT_LE_ADV_OPT_FILTER_CONN = BIT(7),

        BT_LE_ADV_OPT_NOTIFY_SCAN_REQ = BIT(8),

        BT_LE_ADV_OPT_SCANNABLE = BIT(9),

        BT_LE_ADV_OPT_EXT_ADV = BIT(10),

        BT_LE_ADV_OPT_NO_2M = BIT(11),

        BT_LE_ADV_OPT_CODED = BIT(12),

        BT_LE_ADV_OPT_ANONYMOUS = BIT(13),

        BT_LE_ADV_OPT_USE_TX_POWER = BIT(14),

        BT_LE_ADV_OPT_DISABLE_CHAN_37 = BIT(15),

        BT_LE_ADV_OPT_DISABLE_CHAN_38 = BIT(16),

        BT_LE_ADV_OPT_DISABLE_CHAN_39 = BIT(17),

        BT_LE_ADV_OPT_USE_NRPA = BIT(19),

        BT_LE_ADV_OPT_REQUIRE_S2_CODING = BIT(20),

        BT_LE_ADV_OPT_REQUIRE_S8_CODING = BIT(21),

        BT_LE_ADV_OPT_TX_POWER = BIT(22),
};

struct bt_le_adv_param {
        uint8_t  id;

        uint8_t  sid;

        uint8_t  secondary_max_skip;

        int8_t tx_power;

        uint32_t options;

        uint32_t interval_min;

        uint32_t interval_max;

        const bt_addr_le_t *peer;
};

static inline void bt_le_adv_param_set_tx_power(struct bt_le_adv_param *param, int8_t tx_power)
{
        param->options |= BT_LE_ADV_OPT_TX_POWER;
        param->tx_power = tx_power;
}

enum bt_le_per_adv_opt {
        BT_LE_PER_ADV_OPT_NONE = 0,

        BT_LE_PER_ADV_OPT_USE_TX_POWER = BIT(1),

        BT_LE_PER_ADV_OPT_INCLUDE_ADI = BIT(2),
};

struct bt_le_per_adv_param {
        uint16_t interval_min;

        uint16_t interval_max;

        uint32_t options;

#if defined(CONFIG_BT_PER_ADV_RSP) || defined(__DOXYGEN__)
        uint8_t num_subevents;

        uint8_t subevent_interval;

        uint8_t response_slot_delay;

        uint8_t response_slot_spacing;

        uint8_t num_response_slots;
#endif /* CONFIG_BT_PER_ADV_RSP */
};

#define BT_LE_ADV_PARAM_INIT(_options, _int_min, _int_max, _peer) \
{ \
        .id = BT_ID_DEFAULT, \
        .sid = 0, \
        .secondary_max_skip = 0, \
        .options = (_options), \
        .interval_min = (_int_min), \
        .interval_max = (_int_max), \
        .peer = (_peer), \
}

#define BT_LE_ADV_PARAM(_options, _int_min, _int_max, _peer) \
        ((const struct bt_le_adv_param[]) { \
                BT_LE_ADV_PARAM_INIT(_options, _int_min, _int_max, _peer) \
         })

#define BT_LE_ADV_CONN_DIR(_peer) BT_LE_ADV_PARAM(BT_LE_ADV_OPT_CONN, 0, 0, _peer)


#define BT_LE_ADV_CONN_FAST_1                                                                      \
        BT_LE_ADV_PARAM(BT_LE_ADV_OPT_CONN, BT_GAP_ADV_FAST_INT_MIN_1, BT_GAP_ADV_FAST_INT_MAX_1,  \
                        NULL)

#define BT_LE_ADV_CONN_FAST_2                                                                      \
        BT_LE_ADV_PARAM(BT_LE_ADV_OPT_CONN, BT_GAP_ADV_FAST_INT_MIN_2, BT_GAP_ADV_FAST_INT_MAX_2,  \
                        NULL)

#define BT_LE_ADV_CONN_DIR_LOW_DUTY(_peer)                                                         \
        BT_LE_ADV_PARAM(BT_LE_ADV_OPT_CONN | BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY,                      \
                        BT_GAP_ADV_FAST_INT_MIN_2, BT_GAP_ADV_FAST_INT_MAX_2, _peer)

#define BT_LE_ADV_NCONN BT_LE_ADV_PARAM(0, BT_GAP_ADV_FAST_INT_MIN_2, \
                                        BT_GAP_ADV_FAST_INT_MAX_2, NULL)

#define BT_LE_ADV_NCONN_IDENTITY BT_LE_ADV_PARAM(BT_LE_ADV_OPT_USE_IDENTITY, \
                                                 BT_GAP_ADV_FAST_INT_MIN_2, \
                                                 BT_GAP_ADV_FAST_INT_MAX_2, \
                                                 NULL)

#define BT_LE_EXT_ADV_CONN                                                                         \
        BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV | BT_LE_ADV_OPT_CONN, BT_GAP_ADV_FAST_INT_MIN_2,     \
                        BT_GAP_ADV_FAST_INT_MAX_2, NULL)

#define BT_LE_EXT_ADV_SCAN BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV | \
                                           BT_LE_ADV_OPT_SCANNABLE, \
                                           BT_GAP_ADV_FAST_INT_MIN_2, \
                                           BT_GAP_ADV_FAST_INT_MAX_2, \
                                           NULL)

#define BT_LE_EXT_ADV_NCONN BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV, \
                                            BT_GAP_ADV_FAST_INT_MIN_2, \
                                            BT_GAP_ADV_FAST_INT_MAX_2, NULL)

#define BT_LE_EXT_ADV_NCONN_IDENTITY \
                BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV | \
                                BT_LE_ADV_OPT_USE_IDENTITY, \
                                BT_GAP_ADV_FAST_INT_MIN_2, \
                                BT_GAP_ADV_FAST_INT_MAX_2, NULL)

#define BT_LE_EXT_ADV_CODED_NCONN BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV | \
                                                  BT_LE_ADV_OPT_CODED, \
                                                  BT_GAP_ADV_FAST_INT_MIN_2, \
                                                  BT_GAP_ADV_FAST_INT_MAX_2, \
                                                  NULL)

#define BT_LE_EXT_ADV_CODED_NCONN_IDENTITY \
                BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV | BT_LE_ADV_OPT_CODED | \
                                BT_LE_ADV_OPT_USE_IDENTITY, \
                                BT_GAP_ADV_FAST_INT_MIN_2, \
                                BT_GAP_ADV_FAST_INT_MAX_2, NULL)

#define BT_LE_EXT_ADV_START_PARAM_INIT(_timeout, _n_evts) \
{ \
        .timeout = (_timeout), \
        .num_events = (_n_evts), \
}

#define BT_LE_EXT_ADV_START_PARAM(_timeout, _n_evts) \
        ((const struct bt_le_ext_adv_start_param[]) { \
                BT_LE_EXT_ADV_START_PARAM_INIT((_timeout), (_n_evts)) \
        })

#define BT_LE_EXT_ADV_START_DEFAULT BT_LE_EXT_ADV_START_PARAM(0, 0)

#define BT_LE_PER_ADV_PARAM_INIT(_int_min, _int_max, _options) \
{ \
        .interval_min = (_int_min), \
        .interval_max = (_int_max), \
        .options = (_options), \
}

#define BT_LE_PER_ADV_PARAM(_int_min, _int_max, _options) \
        ((struct bt_le_per_adv_param[]) { \
                BT_LE_PER_ADV_PARAM_INIT(_int_min, _int_max, _options) \
        })

#define BT_LE_PER_ADV_DEFAULT BT_LE_PER_ADV_PARAM(BT_GAP_PER_ADV_SLOW_INT_MIN, \
                                                  BT_GAP_PER_ADV_SLOW_INT_MAX, \
                                                  BT_LE_PER_ADV_OPT_NONE)

int bt_le_adv_start(const struct bt_le_adv_param *param,
                    const struct bt_data *ad, size_t ad_len,
                    const struct bt_data *sd, size_t sd_len);

int bt_le_adv_update_data(const struct bt_data *ad, size_t ad_len,
                          const struct bt_data *sd, size_t sd_len);

int bt_le_adv_stop(void);

int bt_le_ext_adv_create(const struct bt_le_adv_param *param,
                         const struct bt_le_ext_adv_cb *cb,
                         struct bt_le_ext_adv **adv);

struct bt_le_ext_adv_start_param {
        uint16_t timeout;

        uint8_t  num_events;
};

int bt_le_ext_adv_start(struct bt_le_ext_adv *adv,
                        const struct bt_le_ext_adv_start_param *param);

int bt_le_ext_adv_stop(struct bt_le_ext_adv *adv);

int bt_le_ext_adv_set_data(struct bt_le_ext_adv *adv,
                           const struct bt_data *ad, size_t ad_len,
                           const struct bt_data *sd, size_t sd_len);

int bt_le_ext_adv_update_param(struct bt_le_ext_adv *adv,
                               const struct bt_le_adv_param *param);

int bt_le_ext_adv_delete(struct bt_le_ext_adv *adv);

uint8_t bt_le_ext_adv_get_index(const struct bt_le_ext_adv *adv);

enum bt_le_ext_adv_state {
        BT_LE_EXT_ADV_STATE_DISABLED,

        BT_LE_EXT_ADV_STATE_ENABLED,
};

enum bt_le_per_adv_state {
        BT_LE_PER_ADV_STATE_NONE,

        BT_LE_PER_ADV_STATE_DISABLED,

        BT_LE_PER_ADV_STATE_ENABLED,
};

struct bt_le_ext_adv_info {
        uint8_t                    id;

        int8_t                     tx_power;

        uint8_t                    sid;

        const bt_addr_le_t         *addr;

        enum bt_le_ext_adv_state ext_adv_state;

        enum bt_le_per_adv_state per_adv_state;
};

int bt_le_ext_adv_get_info(const struct bt_le_ext_adv *adv,
                           struct bt_le_ext_adv_info *info);

typedef void bt_le_scan_cb_t(const bt_addr_le_t *addr, int8_t rssi,
                             uint8_t adv_type, struct net_buf_simple *buf);

int bt_le_per_adv_set_param(struct bt_le_ext_adv *adv,
                            const struct bt_le_per_adv_param *param);

int bt_le_per_adv_set_data(const struct bt_le_ext_adv *adv,
                           const struct bt_data *ad, size_t ad_len);

int bt_le_per_adv_update_did(const struct bt_le_ext_adv *adv);

struct bt_le_per_adv_subevent_data_params {
        uint8_t subevent;

        uint8_t response_slot_start;

        uint8_t response_slot_count;

        const struct net_buf_simple *data;
};

int bt_le_per_adv_set_subevent_data(const struct bt_le_ext_adv *adv, uint8_t num_subevents,
                                    const struct bt_le_per_adv_subevent_data_params *params);

int bt_le_per_adv_start(struct bt_le_ext_adv *adv);

int bt_le_per_adv_stop(struct bt_le_ext_adv *adv);

struct bt_le_per_adv_sync_synced_info {
        const bt_addr_le_t *addr;

        uint8_t sid;

        uint16_t interval;

        uint8_t phy;

        bool recv_enabled;

        uint16_t service_data;

        struct bt_conn *conn;
#if defined(CONFIG_BT_PER_ADV_SYNC_RSP) || defined(__DOXYGEN__)
        uint8_t num_subevents;

        uint8_t subevent_interval;

        uint8_t response_slot_delay;

        uint8_t response_slot_spacing;

#endif /* CONFIG_BT_PER_ADV_SYNC_RSP */
};

struct bt_le_per_adv_sync_term_info {
        const bt_addr_le_t *addr;

        uint8_t sid;

        uint8_t reason;
};

struct bt_le_per_adv_sync_recv_info {
        const bt_addr_le_t *addr;

        uint8_t sid;

        int8_t tx_power;

        int8_t rssi;

        uint8_t cte_type;
#if defined(CONFIG_BT_PER_ADV_SYNC_RSP) || defined(__DOXYGEN__)
        uint16_t periodic_event_counter;

        uint8_t subevent;
#endif /* CONFIG_BT_PER_ADV_SYNC_RSP */
};

struct bt_le_per_adv_sync_state_info {
        bool recv_enabled;
};


struct bt_le_per_adv_sync_cb {
        void (*synced)(struct bt_le_per_adv_sync *sync,
                       struct bt_le_per_adv_sync_synced_info *info);

        void (*term)(struct bt_le_per_adv_sync *sync,
                     const struct bt_le_per_adv_sync_term_info *info);

        void (*recv)(struct bt_le_per_adv_sync *sync,
                     const struct bt_le_per_adv_sync_recv_info *info,
                     struct net_buf_simple *buf);

        void (*state_changed)(struct bt_le_per_adv_sync *sync,
                              const struct bt_le_per_adv_sync_state_info *info);

        void (*biginfo)(struct bt_le_per_adv_sync *sync, const struct bt_iso_biginfo *biginfo);

        void (*cte_report_cb)(struct bt_le_per_adv_sync *sync,
                              struct bt_df_per_adv_sync_iq_samples_report const *info);

        sys_snode_t node;
};

enum bt_le_per_adv_sync_opt {
        BT_LE_PER_ADV_SYNC_OPT_NONE = 0,

        BT_LE_PER_ADV_SYNC_OPT_USE_PER_ADV_LIST = BIT(0),

        BT_LE_PER_ADV_SYNC_OPT_REPORTING_INITIALLY_DISABLED = BIT(1),

        BT_LE_PER_ADV_SYNC_OPT_FILTER_DUPLICATE = BIT(2),

        BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOA = BIT(3),

        BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_1US = BIT(4),

        BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_2US = BIT(5),

        BT_LE_PER_ADV_SYNC_OPT_SYNC_ONLY_CONST_TONE_EXT = BIT(6),
};

struct bt_le_per_adv_sync_param {
        bt_addr_le_t addr;

        uint8_t sid;

        uint32_t options;

        uint16_t skip;

        uint16_t timeout;
};

uint8_t bt_le_per_adv_sync_get_index(struct bt_le_per_adv_sync *per_adv_sync);

struct bt_le_per_adv_sync *bt_le_per_adv_sync_lookup_index(uint8_t index);

struct bt_le_per_adv_sync_info {
        bt_addr_le_t addr;

        uint8_t sid;

        uint16_t interval;

        uint8_t phy;
};

int bt_le_per_adv_sync_get_info(struct bt_le_per_adv_sync *per_adv_sync,
                                struct bt_le_per_adv_sync_info *info);

struct bt_le_per_adv_sync *bt_le_per_adv_sync_lookup_addr(const bt_addr_le_t *adv_addr,
                                                          uint8_t sid);

int bt_le_per_adv_sync_create(const struct bt_le_per_adv_sync_param *param,
                              struct bt_le_per_adv_sync **out_sync);

int bt_le_per_adv_sync_delete(struct bt_le_per_adv_sync *per_adv_sync);

int bt_le_per_adv_sync_cb_register(struct bt_le_per_adv_sync_cb *cb);

int bt_le_per_adv_sync_cb_unregister(struct bt_le_per_adv_sync_cb *cb);

int bt_le_per_adv_sync_recv_enable(struct bt_le_per_adv_sync *per_adv_sync);

int bt_le_per_adv_sync_recv_disable(struct bt_le_per_adv_sync *per_adv_sync);

enum bt_le_per_adv_sync_transfer_opt {
        BT_LE_PER_ADV_SYNC_TRANSFER_OPT_NONE = 0,

        BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOA = BIT(0),

        BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_1US = BIT(1),

        BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_2US = BIT(2),

        BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_ONLY_CTE = BIT(3),

        BT_LE_PER_ADV_SYNC_TRANSFER_OPT_REPORTING_INITIALLY_DISABLED = BIT(4),

        BT_LE_PER_ADV_SYNC_TRANSFER_OPT_FILTER_DUPLICATES = BIT(5),
};

struct bt_le_per_adv_sync_transfer_param {
        uint16_t skip;

        uint16_t timeout;

        uint32_t options;
};

int bt_le_per_adv_sync_transfer(const struct bt_le_per_adv_sync *per_adv_sync,
                                const struct bt_conn *conn,
                                uint16_t service_data);


int bt_le_per_adv_set_info_transfer(const struct bt_le_ext_adv *adv,
                                    const struct bt_conn *conn,
                                    uint16_t service_data);

int bt_le_per_adv_sync_transfer_subscribe(
        const struct bt_conn *conn,
        const struct bt_le_per_adv_sync_transfer_param *param);

int bt_le_per_adv_sync_transfer_unsubscribe(const struct bt_conn *conn);

int bt_le_per_adv_list_add(const bt_addr_le_t *addr, uint8_t sid);

int bt_le_per_adv_list_remove(const bt_addr_le_t *addr, uint8_t sid);

int bt_le_per_adv_list_clear(void);


enum bt_le_scan_opt {
        BT_LE_SCAN_OPT_NONE = 0,

        BT_LE_SCAN_OPT_FILTER_DUPLICATE = BIT(0),

        BT_LE_SCAN_OPT_FILTER_ACCEPT_LIST = BIT(1),

        BT_LE_SCAN_OPT_CODED = BIT(2),

        BT_LE_SCAN_OPT_NO_1M = BIT(3),

        BT_LE_SCAN_OPT_EXT_FILTER_POLICY = BIT(4),
};

enum bt_le_scan_type {
        BT_LE_SCAN_TYPE_PASSIVE = 0x00,

        BT_LE_SCAN_TYPE_ACTIVE = 0x01,
};

struct bt_le_scan_param {
        uint8_t  type;

        uint8_t options;

        uint16_t interval;

        uint16_t window;

        uint16_t timeout;

        uint16_t interval_coded;

        uint16_t window_coded;
};

struct bt_le_scan_recv_info {
        const bt_addr_le_t *addr;

        uint8_t sid;

        int8_t rssi;

        int8_t tx_power;

        uint8_t adv_type;

        uint16_t adv_props;

        uint16_t interval;

        uint8_t primary_phy;

        uint8_t secondary_phy;

        const bt_addr_le_t *direct_addr;
};

struct bt_le_scan_cb {

        void (*recv)(const struct bt_le_scan_recv_info *info,
                     struct net_buf_simple *buf);

        void (*timeout)(void);

        sys_snode_t node;
};

#define BT_LE_SCAN_PARAM_INIT(_type, _options, _interval, _window) \
{ \
        .type = (_type), \
        .options = (_options), \
        .interval = (_interval), \
        .window = (_window), \
        .timeout = 0, \
        .interval_coded = 0, \
        .window_coded = 0, \
}

#define BT_LE_SCAN_PARAM(_type, _options, _interval, _window) \
        ((struct bt_le_scan_param[]) { \
                BT_LE_SCAN_PARAM_INIT(_type, _options, _interval, _window) \
         })

#define BT_LE_SCAN_ACTIVE BT_LE_SCAN_PARAM(BT_LE_SCAN_TYPE_ACTIVE, \
                                           BT_LE_SCAN_OPT_FILTER_DUPLICATE, \
                                           BT_GAP_SCAN_FAST_INTERVAL, \
                                           BT_GAP_SCAN_FAST_WINDOW)

#define BT_LE_SCAN_ACTIVE_CONTINUOUS BT_LE_SCAN_PARAM(BT_LE_SCAN_TYPE_ACTIVE, \
                                                      BT_LE_SCAN_OPT_FILTER_DUPLICATE, \
                                                      BT_GAP_SCAN_FAST_INTERVAL_MIN, \
                                                      BT_GAP_SCAN_FAST_WINDOW)
BUILD_ASSERT(BT_GAP_SCAN_FAST_WINDOW == BT_GAP_SCAN_FAST_INTERVAL_MIN,
             "Continuous scanning is requested by setting window and interval equal.");

#define BT_LE_SCAN_PASSIVE BT_LE_SCAN_PARAM(BT_LE_SCAN_TYPE_PASSIVE, \
                                            BT_LE_SCAN_OPT_FILTER_DUPLICATE, \
                                            BT_GAP_SCAN_FAST_INTERVAL, \
                                            BT_GAP_SCAN_FAST_WINDOW)

#define BT_LE_SCAN_PASSIVE_CONTINUOUS BT_LE_SCAN_PARAM(BT_LE_SCAN_TYPE_PASSIVE, \
                                                       BT_LE_SCAN_OPT_FILTER_DUPLICATE, \
                                                       BT_GAP_SCAN_FAST_INTERVAL_MIN, \
                                                       BT_GAP_SCAN_FAST_WINDOW)
BUILD_ASSERT(BT_GAP_SCAN_FAST_WINDOW == BT_GAP_SCAN_FAST_INTERVAL_MIN,
             "Continuous scanning is requested by setting window and interval equal.");

#define BT_LE_SCAN_CODED_ACTIVE \
                BT_LE_SCAN_PARAM(BT_LE_SCAN_TYPE_ACTIVE, \
                                 BT_LE_SCAN_OPT_CODED | \
                                 BT_LE_SCAN_OPT_FILTER_DUPLICATE, \
                                 BT_GAP_SCAN_FAST_INTERVAL, \
                                 BT_GAP_SCAN_FAST_WINDOW)

#define BT_LE_SCAN_CODED_PASSIVE \
                BT_LE_SCAN_PARAM(BT_LE_SCAN_TYPE_PASSIVE, \
                                 BT_LE_SCAN_OPT_CODED | \
                                 BT_LE_SCAN_OPT_FILTER_DUPLICATE, \
                                 BT_GAP_SCAN_FAST_INTERVAL, \
                                 BT_GAP_SCAN_FAST_WINDOW)

int bt_le_scan_start(const struct bt_le_scan_param *param, bt_le_scan_cb_t cb);

int bt_le_scan_stop(void);

int bt_le_scan_cb_register(struct bt_le_scan_cb *cb);

void bt_le_scan_cb_unregister(struct bt_le_scan_cb *cb);

int bt_le_filter_accept_list_add(const bt_addr_le_t *addr);

int bt_le_filter_accept_list_remove(const bt_addr_le_t *addr);

int bt_le_filter_accept_list_clear(void);

int bt_le_set_chan_map(uint8_t chan_map[5]);

int bt_le_set_rpa_timeout(uint16_t new_rpa_timeout);

void bt_data_parse(struct net_buf_simple *ad,
                   bool (*func)(struct bt_data *data, void *user_data),
                   void *user_data);

struct bt_le_oob_sc_data {
        uint8_t r[16];

        uint8_t c[16];
};

struct bt_le_oob {
        bt_addr_le_t addr;

        struct bt_le_oob_sc_data le_sc_data;
};

int bt_le_oob_get_local(uint8_t id, struct bt_le_oob *oob);

int bt_le_ext_adv_oob_get_local(struct bt_le_ext_adv *adv,
                                struct bt_le_oob *oob);

int bt_unpair(uint8_t id, const bt_addr_le_t *addr);

struct bt_bond_info {
        bt_addr_le_t addr;
};

void bt_foreach_bond(uint8_t id, void (*func)(const struct bt_bond_info *info,
                                           void *user_data),
                     void *user_data);

enum bt_le_addr_res_support {
        BT_LE_ADDR_RES_SUPPORT_UNKNOWN,
        BT_LE_ADDR_RES_SUPPORT_NO,
        BT_LE_ADDR_RES_SUPPORT_YES,
};

enum bt_le_addr_res_support bt_le_bond_addr_res_support(uint8_t id, const bt_addr_le_t *peer);

int bt_configure_data_path(uint8_t dir, uint8_t id, uint8_t vs_config_len,
                           const uint8_t *vs_config);

struct bt_le_per_adv_sync_subevent_params {
        uint16_t properties;

        uint8_t num_subevents;

        uint8_t *subevents;
};

int bt_le_per_adv_sync_subevent(struct bt_le_per_adv_sync *per_adv_sync,
                                struct bt_le_per_adv_sync_subevent_params *params);

struct bt_le_per_adv_response_params {
        uint16_t request_event;

        uint8_t request_subevent;

        uint8_t response_subevent;

        uint8_t response_slot;
};

int bt_le_per_adv_set_response_data(struct bt_le_per_adv_sync *per_adv_sync,
                                    const struct bt_le_per_adv_response_params *params,
                                    const struct net_buf_simple *data);

bool bt_le_bond_exists(uint8_t id, const bt_addr_le_t *addr);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_BLUETOOTH_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2017 Nordic Semiconductor ASA。

版权（Copyright）：© 2015-2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 103 行

不要求所有使用者都包含 `conn.h`。

### 注释 3：原第 106 行

不要求所有使用者都包含 `iso.h`。

### 注释 4：原第 109 行

不要求所有使用者都包含 `direction.h`。

### 注释 5：原第 284 行

条件编译（Conditional Compilation）：`defined(CONFIG_BT_PRIVACY)`。

### 注释 6：原第 321 行

条件编译（Conditional Compilation）：`defined(CONFIG_BT_PER_ADV_RSP)`。

### 注释 7：原第 1125 行

条件编译配置（Configuration）标记：`CONFIG_BT_PER_ADV_RSP`。

### 注释 8：原第 1859 行

条件编译配置（Configuration）标记：`CONFIG_BT_PER_ADV_SYNC_RSP`。

### 注释 9：原第 1923 行

条件编译配置（Configuration）标记：`CONFIG_BT_PER_ADV_SYNC_RSP`。

### 注释 10：原第 3229 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_BLUETOOTH_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [string.h](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md)
- [zephyr/bluetooth/gap.h](https://docs.zephyrproject.org/latest/doxygen/html/gap_8h.html)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [zephyr/bluetooth/crypto.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2crypto_8h.html)
- [zephyr/bluetooth/data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [zephyr/bluetooth/classic/classic.h](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_iso_biginfo](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md)
- [bt_df_per_adv_sync_iq_samples_report](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md)
- [bt_le_ext_adv_sent_info](../bluetooth_connection_model_reference/P107_bt_le_ext_adv_sent_info_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [num_sent](../bluetooth_connection_model_reference/P107_bt_le_ext_adv_sent_info_结构体.md#a80f661efd35b069c2f8700851e9429a2)
- [bt_le_ext_adv_connected_info](../bluetooth_connection_model_reference/P104_bt_le_ext_adv_connected_info_结构体.md)
- [conn](../bluetooth_connection_model_reference/P104_bt_le_ext_adv_connected_info_结构体.md#a157efa6206b418f768582107c566fde2)
- [bt_le_ext_adv_scanned_info](../bluetooth_connection_model_reference/P106_bt_le_ext_adv_scanned_info_结构体.md)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [addr](../bluetooth_connection_model_reference/P106_bt_le_ext_adv_scanned_info_结构体.md#a4431f157891d2c1a7d0e40f7e879ac3d)
- [bt_le_per_adv_data_request](../bluetooth_connection_model_reference/P112_bt_le_per_adv_data_request_结构体.md)
- [start](../bluetooth_connection_model_reference/P112_bt_le_per_adv_data_request_结构体.md#a779ed161919c3117f6ce165deb0a9b0a)
- [count](../bluetooth_connection_model_reference/P112_bt_le_per_adv_data_request_结构体.md#a766991899bc3e689adec36bf1f12e802)
- [bt_le_per_adv_response_info](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md)
- [subevent](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md#a1b87ab77f5c7d4ee0c1c612bcfb424d5)
- [tx_status](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md#ab17f33cb713d258bf6c863a64e5aba07)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [tx_power](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md#a7ed20f695e0d696eaab7cddc4e3c11fb)
- [rssi](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md#a2db58fb452a07290ab4a50892c682837)
- [cte_type](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md#a52b0c612b09cfcb3eb2ea475614c34b8)
- [response_slot](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md#a83cc642c9f22c767421644e7d8233001)
- [bt_le_ext_adv_cb](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md)
- [sent](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#a85b8887c9ef443d18b71e9561e7dde60)
- [connected](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#a7aad0fbd8e531e70f661500c338d870e)
- [scanned](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#a277dc3269741d40b644ae3c777198fab)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [rpa_expired](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#a251ea84adf8b6cc14bae051d74edc1fe)
- [pawr_data_request](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#ab6452d9b3449847bf009c3d43c051922)
- [pawr_response](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#a6b26be418789c6e5087dab1100cb56a8)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_ready_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5398783ab4a5dc854b18e37fb10774eb)
- [bt_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac45d16bfe21c3c38e834c293e5ebc42b)
- [bt_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga0a58e5a050170e84a80f8d5bb3516ec7)
- [bt_is_ready](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa8bf6854e7ad1fe7e0805737576e5d1a)
- [bt_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac8bb3609a3d6da69ff736809e45f5c8a)
- [bt_get_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad922d894b25e86de3f81ce77200a13fd)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_get_appearance](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga35b76ea7ce79721e47ca4164e08b2dfb)
- [bt_set_appearance](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf0729453790aab1bd3d52c623be3b35a)
- [bt_id_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga06d0ae35cbf4382679cc3cfe612cee4d)
- [bt_id_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae11eb8ad254418c38a0e8689df25a159)
- [bt_id_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabb3353edc8a3a8d29a0370049b20cbe4)
- [bt_id_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf6cd906690a51ebed04bea4f4ef716ff)
- [bt_id_reset_irk](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7a595421c232b15ad96b52f0300fd960)
- [bt_le_local_features](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md)
- [features](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#a516ca4b44a693f045a45eedf375c9ea6)
- [BT_LE_LOCAL_SUPPORTED_FEATURES_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa26f90b188caa50ca12247b7911a0a5f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [states](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#aa2dc6363feab37af195ee192f2b906f1)
- [acl_mtu](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#a22ce370b338f687ce6860435cc0ec9c5)
- [acl_pkts](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#a19cecbe8574229844e9416842bc42b0c)
- [iso_mtu](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#ad7b95feb82c1dece8bb8bb7969efa2ec)
- [iso_pkts](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#a8b413bf80ccd7e3af67f7e1c28a1beeb)
- [rl_size](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#ac86ae6974627ddb2e34b0d028cdcfe32)
- [max_adv_data_len](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#a932af365332149ec620413a8504d342c)
- [bt_le_get_local_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga650faa2a86f54499f4bc5a8657a55a87)
- [bt_le_adv_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gafbf81dab68b0e484d4742471c722fc28)
- [BT_LE_ADV_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a928b376123819cb0a69fbb5b35608dbf)
- [BT_LE_ADV_OPT_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_LE_ADV_OPT_USE_IDENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a407cf5ae358d3c00dd7e47dfaad3ec6e)
- [BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28afd164ec5476f5e2d9aedf50032946872)
- [BT_LE_ADV_OPT_DIR_ADDR_RPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28abdcf1c80662061fa30575e1f9fc6cf6f)
- [BT_LE_ADV_OPT_FILTER_SCAN_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a807ba316edc49c8448a8ff7d497173f5)
- [BT_LE_ADV_OPT_FILTER_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ad5efef3d01731110dbd71d5a5dc9baaf)
- [BT_LE_ADV_OPT_NOTIFY_SCAN_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a1563b053f457833d1a3d11c8dc4d394b)
- [BT_LE_ADV_OPT_SCANNABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ae60eafe69ef10b84f61a1f4accf789c9)
- [BT_LE_ADV_OPT_EXT_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab)
- [BT_LE_ADV_OPT_NO_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ae864aefcdfbecaffe823b9b144fe0a6b)
- [BT_LE_ADV_OPT_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ad01c4962a350d3218ba0cabd713708b1)
- [BT_LE_ADV_OPT_ANONYMOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a185e0f884f8b0ce79625448638de8fab)
- [BT_LE_ADV_OPT_USE_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28aecff4fe3ac3d1fba3f6fa76c77713859)
- [BT_LE_ADV_OPT_DISABLE_CHAN_37](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ab46741616f8bfe50c4b492d1f7970779)
- [BT_LE_ADV_OPT_DISABLE_CHAN_38](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28abd9cb02691d7e025fe3fea9a80123275)
- [BT_LE_ADV_OPT_DISABLE_CHAN_39](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a89f7494620236c976bf1a76a880e2a28)
- [BT_LE_ADV_OPT_USE_NRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a22958d8539d661ad7ca8d3f1173e7e5e)
- [BT_LE_ADV_OPT_REQUIRE_S2_CODING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a9a35ede118224d6ed17f252fff6bb47e)
- [BT_LE_ADV_OPT_REQUIRE_S8_CODING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28aa6a61768ad4102f199d3970791118bb8)
- [BT_LE_ADV_OPT_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ab9ee87ad3a24312174ae46f904fe9c56)
- [bt_le_adv_param](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md)
- [id](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#af957bd92b949536af2b2db0db7b2b425)
- [sid](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#a6e2f0e1b76495afe7fe661e8698d0909)
- [secondary_max_skip](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#a9911e9bfc97ff0c48a6decae3f922e95)
- [tx_power](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#a1c09c2bcf9600a644e194ecd3367d200)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [options](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#a2a978c60153eb03697769bc72928f4ef)
- [interval_min](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#aca8ff5a4f5d29184535162f007b2d39e)
- [interval_max](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#afeba6973dca99d8ee818fdde0c22cb59)
- [peer](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#a4cf31f54f067fffa3c848adc2ffd7119)
- [bt_le_adv_param_set_tx_power](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga453074db3964f1b57b92ac7afb0b4fac)
- [bt_le_per_adv_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae60a45dde6b4d9f4c54a2a6070254f11)
- [BT_LE_PER_ADV_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggae60a45dde6b4d9f4c54a2a6070254f11aa2c689d726eacfb18d87655b1f587518)
- [BT_LE_PER_ADV_OPT_USE_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggae60a45dde6b4d9f4c54a2a6070254f11a9524537e4cb726f4ff10ba93381bb27f)
- [BT_LE_PER_ADV_OPT_INCLUDE_ADI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggae60a45dde6b4d9f4c54a2a6070254f11a38cebc2ae885ff630b34c603e2ec6403)
- [bt_le_per_adv_param](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md)
- [interval_min](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a49da44a3c0e4e866ffccffae5a9a22f7)
- [interval_max](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a61308cfe72ad23372dfd2a3bd2550726)
- [options](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a9b80c2427171920f466601e7e8468814)
- [num_subevents](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#af8be989979c98a17828819ec43dd0b49)
- [subevent_interval](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a28655741c63775a274c42ad5057d4a1d)
- [response_slot_delay](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a07302e13735f502b8950a92b365ef14a)
- [response_slot_spacing](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a67116b81e8ce968cf411843646801ac4)
- [num_response_slots](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a0a8606c103fd91f3222bae6c9f1204fd)
- [bt_le_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad2e3caef88d52d720e8e4d21df767b02)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [bt_le_adv_update_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9a406ebfefac3dd09935a4ae0e317817)
- [bt_le_adv_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1776e310b9d80898e6b32d50c4fe0b49)
- [bt_le_ext_adv_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad02b855dd7a26e3910b247fa73f19297)
- [bt_le_ext_adv_start_param](../bluetooth_connection_model_reference/P108_bt_le_ext_adv_start_param_结构体.md)
- [timeout](../bluetooth_connection_model_reference/P108_bt_le_ext_adv_start_param_结构体.md#a80bb1ef4316dd75ea1268241333f4346)
- [num_events](../bluetooth_connection_model_reference/P108_bt_le_ext_adv_start_param_结构体.md#ab45ae0bfdb144071efcc64c30648388f)
- [bt_le_ext_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf0f436c55482d9429f674303ae3aa815)
- [bt_le_ext_adv_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1c864c4b183f9a86c9f70a11471c5b15)
- [bt_le_ext_adv_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad731f829b3566be3e56485b2a64f80b1)
- [bt_le_ext_adv_update_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1aabdb81cb1a1841ff0fb91d849123fc)
- [bt_le_ext_adv_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga62310a27f7fea925dfcf3abd7c454787)
- [bt_le_ext_adv_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf8b28f54c68251024b869f3b0d1c1282)
- [bt_le_ext_adv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga544ccde35638d8f580942d830fe9f242)
- [BT_LE_EXT_ADV_STATE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga544ccde35638d8f580942d830fe9f242a4423f4792711b21cf38a4e63c148760d)
- [BT_LE_EXT_ADV_STATE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga544ccde35638d8f580942d830fe9f242afe851bf904c1cfed3ff10a57430d6a07)
- [bt_le_per_adv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6bb77c0808c761753650cde28ddb013e)
- [BT_LE_PER_ADV_STATE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga6bb77c0808c761753650cde28ddb013ead690730da823fcb31f102f154a23b01c)
- [BT_LE_PER_ADV_STATE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga6bb77c0808c761753650cde28ddb013eac26ccfbb5c715b515ef82c1993eff03b)
- [BT_LE_PER_ADV_STATE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga6bb77c0808c761753650cde28ddb013ea492cf25dc85090cfa72d5e2bdc0917f3)
- [bt_le_ext_adv_info](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md)
- [id](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#a06aa727cd2523914bc7509713585bffd)
- [tx_power](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#a485e4a8124fddee897fe744836cbfb24)
- [sid](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#a19877c440137814ec0e4aa1a1270f6fe)
- [addr](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#a0dd0aa8a26fe1ef5813fa07732c5c4c9)
- [ext_adv_state](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#a0ae2f62772732a6db460d4a0127dd17a)
- [per_adv_state](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#ad802b5af32353d757a84e5039c973f3a)
- [bt_le_ext_adv_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac06c9f55cf1da46e0d64b4d9af984ecb)
- [bt_le_scan_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1c53d22b6e2dee38c825c58f3eeee9b4)
- [bt_le_per_adv_set_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa72029a2759123ec776061d2e80bf3a1)
- [bt_le_per_adv_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gafd0e7ccca93a8347a4ca6cca88e77899)
- [bt_le_per_adv_update_did](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga59e9fc635846ab92af19d483de58ed88)
- [bt_le_per_adv_subevent_data_params](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md)
- [subevent](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md#a55f2da6041b538b3bc4bff38cd4d2953)
- [response_slot_start](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md#a1354e9505239de3c42969138d719d775)
- [response_slot_count](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md#a86d858606943a82917835a0172e88663)
- [data](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md#a46103c988d8ac360b7e26310a0322b4e)
- [bt_le_per_adv_set_subevent_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7de30fe5040b85bb9212e3a8fec4ac45)
- [bt_le_per_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga0f23f4ed48e8679646f247ea0d687094)
- [bt_le_per_adv_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1b15206fc552d597c12af369d48ff7d5)
- [bt_le_per_adv_sync_synced_info](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md)
- [addr](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a7ca99b0596b08d153d3ba5310adab125)
- [sid](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a5489c3038f7fff596316a456fc8d580b)
- [interval](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a5304e1826face35c506f3b8f6cad7df2)
- [phy](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a8b7709011541e95ceaeac379cc3143bb)
- [recv_enabled](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a0dd4b7646da0fadc48e94ff3dc91ef83)
- [service_data](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#adee2bdafa86a0c3c1dfb4660e85396a3)
- [conn](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#ada4cda53aa87f29d54f6cd88134efe14)
- [num_subevents](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#aaab25f36577948d55b6379abe0590c69)
- [subevent_interval](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a9e01fb9462c4874a60ebc5359fe5df14)
- [response_slot_delay](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a7bdec5d34b97602aa56c1006dbaf79c4)
- [response_slot_spacing](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#ae9a696dd9dc28b7505e406961ca89b9a)
- [bt_le_per_adv_sync_term_info](../bluetooth_connection_model_reference/P125_bt_le_per_adv_sync_term_info_结构体.md)
- [addr](../bluetooth_connection_model_reference/P125_bt_le_per_adv_sync_term_info_结构体.md#a2b76ccd5e4c9933f2c05db2ec5b8e2fc)
- [sid](../bluetooth_connection_model_reference/P125_bt_le_per_adv_sync_term_info_结构体.md#a7a5f2ecccaf698bad86f10d9a7d16189)
- [reason](../bluetooth_connection_model_reference/P125_bt_le_per_adv_sync_term_info_结构体.md#a429b8b665eacbfe9db013a571b829bac)
- [bt_le_per_adv_sync_recv_info](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md)
- [addr](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#a5817bd4fba2c93adebcebe007650b6eb)
- [sid](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#a21b0ca87e46c6897282ebd877e45114e)
- [tx_power](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#a65f1a2adb7c3d740cb8262ae7f5a7c3e)
- [rssi](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#aa17c9d917469f121448ed4e1db485700)
- [cte_type](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#a1591907e3cb1f4565b9d26c18bccc7d2)
- [periodic_event_counter](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#a74f6dc1745a756faca2e323292024730)
- [subevent](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#a1a9dccd6d7592868b5604ec16a5f1540)
- [bt_le_per_adv_sync_state_info](../bluetooth_connection_model_reference/P122_bt_le_per_adv_sync_state_info_结构体.md)
- [recv_enabled](../bluetooth_connection_model_reference/P122_bt_le_per_adv_sync_state_info_结构体.md#a4b0a3b7e36f935e06072304d6b92579f)
- [bt_le_per_adv_sync_cb](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md)
- [synced](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#a815be4343ab589df433a551663c5f4a1)
- [term](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#acbd565a39918e5dfe7603a020e73daec)
- [recv](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#a5576248e2eaef2afebe606e05e55f05f)
- [state_changed](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#a656b4802f79d4a472c2367ade144d72e)
- [biginfo](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#aa44efa17bc28da1952785063a9baf6a9)
- [cte_report_cb](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#ad2dc168696fbd22f7e3a089ac56f62d7)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#a1977d27941063773c953a5f1dfa9ca76)
- [bt_le_per_adv_sync_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac942d7e3cae8fca22080f93bf9528ee9)
- [BT_LE_PER_ADV_SYNC_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9aeeef50a544edc104b39e4ef0c9a58d6c)
- [BT_LE_PER_ADV_SYNC_OPT_USE_PER_ADV_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9ae9a88caa6a83da8b1697a6167629bf7e)
- [BT_LE_PER_ADV_SYNC_OPT_REPORTING_INITIALLY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9ae35a6eb572a2842e4cc2fc3677e19b53)
- [BT_LE_PER_ADV_SYNC_OPT_FILTER_DUPLICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9a9ec2b0c346c2cab7f61c2efcc8e37db2)
- [BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9aaa256e560f013eb74415d817154b8f4e)
- [BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_1US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9a99034652a92249e6d04065d68352020b)
- [BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_2US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9a0f52e38e513ec7eefcbc5c86c36f002e)
- [BT_LE_PER_ADV_SYNC_OPT_SYNC_ONLY_CONST_TONE_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9a5c702876d70d5eadc4df6e59d96b8320)
- [bt_le_per_adv_sync_param](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md)
- [addr](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md#ac93adedad747f61a771ac5445e486b74)
- [sid](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md#a70795642ee94dd9e87f0cf251c095e7f)
- [options](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md#a4252f2b3b453c2f9c8fbf8c35a618ff2)
- [skip](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md#af9abb65547fb5bfea65f4c22963c7da0)
- [timeout](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md#a301cfd3d6e5620d29c021ababe104754)
- [bt_le_per_adv_sync_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8d05bd864d98b5b43595eb256e464024)
- [bt_le_per_adv_sync_lookup_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga59532b37412b1b93f81cf5cc1bab0534)
- [bt_le_per_adv_sync_info](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md)
- [addr](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md#ac10fc2e2d3ec2160db8c2aac148d18a2)
- [sid](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md#acc0ef26c38279c9a67f8992005c2e58a)
- [interval](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md#a365a0d8577429e4ee96e977071c9a906)
- [phy](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md#a4d9520ea6a803f8fe4f41190f55c26e5)
- [bt_le_per_adv_sync_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabfaf265a48dd09ea02d114e2023c14a6)
- [bt_le_per_adv_sync_lookup_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga83126917373c0bcaa24964dd1d8bde46)
- [bt_le_per_adv_sync_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga061bf84b989b2c96ab51d2ca0debb017)
- [bt_le_per_adv_sync_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa0c218ff3c78b26dcfaa726ee30267a6)
- [bt_le_per_adv_sync_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga4ee87bbf79e6ac844d14c3dafb2dadf4)
- [bt_le_per_adv_sync_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab1576c66b08dc855b2d17fc562f36724)
- [bt_le_per_adv_sync_recv_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga07e4510de7e72c6ed6196b3da9fb40be)
- [bt_le_per_adv_sync_recv_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5)
- [bt_le_per_adv_sync_transfer_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga820c5f3721e72662e558cc4576b6111b)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111baef90aceabc3f9d0b17b7f3415152fca2)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111ba2694870b7ebd2dcd0b3834367f7d7061)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_1US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111bab0725048806858083be9ab3fcd9a36ed)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_2US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111ba433ae469b27e820fdfd2a1d562010991)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_ONLY_CTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111baed2f78d682b5fbd1adf89c2f005e4f48)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_REPORTING_INITIALLY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111ba3f0be549ca5cac1cfbdec2f2227e73dc)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_FILTER_DUPLICATES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111bad924f620ed6fdadbbea03f8e343b9d0c)
- [bt_le_per_adv_sync_transfer_param](../bluetooth_connection_model_reference/P126_bt_le_per_adv_sync_transfer_param_结构体.md)
- [skip](../bluetooth_connection_model_reference/P126_bt_le_per_adv_sync_transfer_param_结构体.md#a840e7cfac3a2947e5128d704067aaf7e)
- [timeout](../bluetooth_connection_model_reference/P126_bt_le_per_adv_sync_transfer_param_结构体.md#a5bfa84c6bdacdf8893a0951a5ce71fc6)
- [options](../bluetooth_connection_model_reference/P126_bt_le_per_adv_sync_transfer_param_结构体.md#a0b3ee6df1b409e64a064ffb6ac632cce)
- [bt_le_per_adv_sync_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf81a1dd7a628d1a2f25c6b53b0679809)
- [bt_le_per_adv_set_info_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac96199a4e5e6cfb789c1bd1c0e67d6fe)
- [bt_le_per_adv_sync_transfer_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa0658bd53df1d5e8e89e13330e4fd0ae)
- [bt_le_per_adv_sync_transfer_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga08f872078045bbef4aca19761f25eeb8)
- [bt_le_per_adv_list_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga27c4961f3c7270a7f1caeadb4107854b)
- [bt_le_per_adv_list_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga100efac4a49984e06202c63c4e5955cd)
- [bt_le_per_adv_list_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5909bd768c23a19a42a660e3b814c981)
- [bt_le_scan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab4b5773898e2a1eef21557915a21c996)
- [BT_LE_SCAN_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996aad3f19e5849b6d6813fa88257082e185)
- [BT_LE_SCAN_OPT_FILTER_DUPLICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a0af65ac48e068f7e6f1815cb151d4394)
- [BT_LE_SCAN_OPT_FILTER_ACCEPT_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996af7a25b6790b138b2b88de3c7d81cb0ae)
- [BT_LE_SCAN_OPT_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a16f171c649dd090333e9822a92b4bbdb)
- [BT_LE_SCAN_OPT_NO_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a7ff0c79b2675e7b7512379e2cbedc0a6)
- [BT_LE_SCAN_OPT_EXT_FILTER_POLICY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a79cdd7e96e41f4236642edfbcb1b666d)
- [bt_le_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf980473379afa477c09e19912d40d29e)
- [BT_LE_SCAN_TYPE_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaf980473379afa477c09e19912d40d29ea731c507ed451eb6f8f8372849185b006)
- [BT_LE_SCAN_TYPE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaf980473379afa477c09e19912d40d29eaf202213813092ba298cd046aed687f22)
- [bt_le_scan_param](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md)
- [type](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#a02d75322390287c3fa754bf915660d0c)
- [options](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#ac815b05fee8ce0dd24228305b7596207)
- [interval](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#a2f4e053d97c62b6fdf42a245908607f8)
- [window](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#a37a7ee82e86a91cf7a9c2adf60bb526a)
- [timeout](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#a3e71ce551dcc7762c29e2316996e2912)
- [interval_coded](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#a67a20bc94a3d98fa10af7b5b42dde328)
- [window_coded](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#a93166af55dca71393c60cb3f7ac6d809)
- [bt_le_scan_recv_info](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md)
- [addr](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a907fb7ec3c78d68da5015a8c3afc3084)
- [sid](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a4df8d4e1fdd7514d170744856ebe7015)
- [rssi](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a88f677733147245ccbf861c7fc5e0f11)
- [tx_power](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a2addeba6d2ec8e55dc5379adf6519148)
- [adv_type](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#adccb2ce5c6d228bd7f8f050088629524)
- [adv_props](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#af29ddfb59e286af9ca465cbd5a91bf2d)
- [interval](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a1060c5937708ff81a64f068e02fc7826)
- [primary_phy](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a6189ed8453cb7907f34dc7dfaf1343bd)
- [secondary_phy](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#ac797291291dc7ba7ac171ed7f24f0d16)
- [direct_addr](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a8885283f39e3ece5d7ff7d5b5d588696)
- [bt_le_scan_cb](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md)
- [recv](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md#a71d73c1da28d4a27626f77d96a5b3541)
- [timeout](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md#a2f57f3fee46bd137065f4c57d0cd5157)
- [node](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md#a50dbc5e7618fd488e9acb7ad8f104a63)
- [BT_GAP_SCAN_FAST_WINDOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga100e1c20813630848a1a80390e8a06a0)
- [BT_GAP_SCAN_FAST_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gae9356673ee78d9abb27891738344513a)
- [bt_le_scan_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac5e19c26b53a08dadb8efa7ecc692ad6)
- [bt_le_scan_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa2de1a1ab523606b36a4c445fb0c3b84)
- [bt_le_scan_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga80e870fa1de40c404c64624bef439067)
- [bt_le_scan_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac2718f2128b3f8c79b12d760771c8378)
- [bt_le_filter_accept_list_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga40f2f7fdb09aba3c5137f680e67792f0)
- [bt_le_filter_accept_list_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga0532ed768ab4f9d69c202066d2f87e66)
- [bt_le_filter_accept_list_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac87df899d1e363c63162988157ee6d00)
- [bt_le_set_chan_map](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabc115fd3fff6d00ae878a31613bf70aa)
- [bt_le_set_rpa_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9ab41e118b5496c196e56b8b5d023275)
- [bt_data_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga652eef01e5256e0d820cd1f4db877429)
- [data](../network_core_model_reference/P048_net_buf_simple_结构体.md#ad232efff435f425d30ac78f5abf2d8b1)
- [bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)
- [r](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md#afa64bcc048d0e8709e262e2848a39d2c)
- [c](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md#a9bd93f1e9e41e241d0f84ae16ae47ba1)
- [bt_le_oob](../bluetooth_connection_model_reference/P110_bt_le_oob_结构体.md)
- [addr](../bluetooth_connection_model_reference/P110_bt_le_oob_结构体.md#a17cfed7683efbf5b5954847d655d7424)
- [le_sc_data](../bluetooth_connection_model_reference/P110_bt_le_oob_结构体.md#a80ccd4ab120a880adfff9aba3b19b4fd)
- [bt_le_oob_get_local](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga296d1adf3c9ed2f2c65bb75b887d59ee)
- [bt_le_ext_adv_oob_get_local](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7486aab863ca497a50dacf81657f48d4)
- [bt_unpair](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaceabbbe6e844650f791010e53c9df6a4)
- [bt_bond_info](../bluetooth_connection_model_reference/P001_bt_bond_info_结构体.md)
- [addr](../bluetooth_connection_model_reference/P001_bt_bond_info_结构体.md#a6b328ce30fd53bb73ecd8e033bb91d1f)
- [bt_foreach_bond](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad380b7f8984f8522c1b79f9bdc04905)
- [bt_le_addr_res_support](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad0039d4b524a0eef31158dc9b24a497)
- [BT_LE_ADDR_RES_SUPPORT_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaad0039d4b524a0eef31158dc9b24a497a32a025f5c47db4957e72d292e748eda9)
- [BT_LE_ADDR_RES_SUPPORT_NO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaad0039d4b524a0eef31158dc9b24a497a1fcee00e6de549746f81de0bf43caeab)
- [BT_LE_ADDR_RES_SUPPORT_YES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaad0039d4b524a0eef31158dc9b24a497a1d636d176d18199b7d5bcb17865b3a1c)
- [bt_le_bond_addr_res_support](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5b5e51f79896d674bf6b70b2251e79d4)
- [bt_configure_data_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8046c2b06d3dad0d6c8184de492517d2)
- [bt_le_per_adv_sync_subevent_params](../bluetooth_connection_model_reference/P123_bt_le_per_adv_sync_subevent_params_结构体.md)
- [properties](../bluetooth_connection_model_reference/P123_bt_le_per_adv_sync_subevent_params_结构体.md#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4)
- [num_subevents](../bluetooth_connection_model_reference/P123_bt_le_per_adv_sync_subevent_params_结构体.md#a867c66bf09461a4369da3d250701d2ae)
- [subevents](../bluetooth_connection_model_reference/P123_bt_le_per_adv_sync_subevent_params_结构体.md#a5ac4e81ddd63797f921105748344c125)
- [bt_le_per_adv_sync_subevent](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga731f4b37a9e5cc13a6816ea23f751b0b)
- [bt_le_per_adv_response_params](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md)
- [request_event](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md#a1af01d0a027fb8659615874acbd388f9)
- [request_subevent](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md#a3fc8ab0feb06714b28d22439cce60e41)
- [response_subevent](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md#a0cec222d5ba8cc9e20939d441646c913)
- [response_slot](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md#aea0428083ccd5f4dccc17e494f38b7c3)
- [bt_le_per_adv_set_response_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaae6b8583f7d5457f20b03dccd146425e)
- [bt_le_bond_exists](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga309a67de79cc215db1d33251f267f361)
- [addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [crypto.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2crypto_8h.html)
- [classic.h](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h.html)
- [data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [gap.h](https://docs.zephyrproject.org/latest/doxygen/html/gap_8h.html)
- [hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_bond_info::addr](../bluetooth_connection_model_reference/P001_bt_bond_info_结构体.md#a6b328ce30fd53bb73ecd8e033bb91d1f)
- [bt_le_adv_param::tx_power](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#a1c09c2bcf9600a644e194ecd3367d200)
- [bt_le_adv_param::options](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#a2a978c60153eb03697769bc72928f4ef)
- [bt_le_adv_param::peer](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#a4cf31f54f067fffa3c848adc2ffd7119)
- [bt_le_adv_param::sid](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#a6e2f0e1b76495afe7fe661e8698d0909)
- [bt_le_adv_param::secondary_max_skip](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#a9911e9bfc97ff0c48a6decae3f922e95)
- [bt_le_adv_param::interval_min](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#aca8ff5a4f5d29184535162f007b2d39e)
- [bt_le_adv_param::id](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#af957bd92b949536af2b2db0db7b2b425)
- [bt_le_adv_param::interval_max](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#afeba6973dca99d8ee818fdde0c22cb59)
- [bt_le_ext_adv_cb::rpa_expired](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#a251ea84adf8b6cc14bae051d74edc1fe)
- [bt_le_ext_adv_cb::scanned](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#a277dc3269741d40b644ae3c777198fab)
- [bt_le_ext_adv_cb::pawr_response](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#a6b26be418789c6e5087dab1100cb56a8)
- [bt_le_ext_adv_cb::connected](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#a7aad0fbd8e531e70f661500c338d870e)
- [bt_le_ext_adv_cb::sent](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#a85b8887c9ef443d18b71e9561e7dde60)
- [bt_le_ext_adv_cb::pawr_data_request](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#ab6452d9b3449847bf009c3d43c051922)
- [bt_le_ext_adv_connected_info::conn](../bluetooth_connection_model_reference/P104_bt_le_ext_adv_connected_info_结构体.md#a157efa6206b418f768582107c566fde2)
- [bt_le_ext_adv_info::id](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#a06aa727cd2523914bc7509713585bffd)
- [bt_le_ext_adv_info::ext_adv_state](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#a0ae2f62772732a6db460d4a0127dd17a)
- [bt_le_ext_adv_info::addr](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#a0dd0aa8a26fe1ef5813fa07732c5c4c9)
- [bt_le_ext_adv_info::sid](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#a19877c440137814ec0e4aa1a1270f6fe)
- [bt_le_ext_adv_info::tx_power](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#a485e4a8124fddee897fe744836cbfb24)
- [bt_le_ext_adv_info::per_adv_state](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#ad802b5af32353d757a84e5039c973f3a)
- [bt_le_ext_adv_scanned_info::addr](../bluetooth_connection_model_reference/P106_bt_le_ext_adv_scanned_info_结构体.md#a4431f157891d2c1a7d0e40f7e879ac3d)
- [bt_le_ext_adv_sent_info::num_sent](../bluetooth_connection_model_reference/P107_bt_le_ext_adv_sent_info_结构体.md#a80f661efd35b069c2f8700851e9429a2)
- [bt_le_ext_adv_start_param::timeout](../bluetooth_connection_model_reference/P108_bt_le_ext_adv_start_param_结构体.md#a80bb1ef4316dd75ea1268241333f4346)
- [bt_le_ext_adv_start_param::num_events](../bluetooth_connection_model_reference/P108_bt_le_ext_adv_start_param_结构体.md#ab45ae0bfdb144071efcc64c30648388f)
- [bt_le_local_features::acl_pkts](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#a19cecbe8574229844e9416842bc42b0c)
- [bt_le_local_features::acl_mtu](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#a22ce370b338f687ce6860435cc0ec9c5)
- [bt_le_local_features::features](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#a516ca4b44a693f045a45eedf375c9ea6)
- [bt_le_local_features::iso_pkts](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#a8b413bf80ccd7e3af67f7e1c28a1beeb)
- [bt_le_local_features::max_adv_data_len](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#a932af365332149ec620413a8504d342c)
- [bt_le_local_features::states](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#aa2dc6363feab37af195ee192f2b906f1)
- [bt_le_local_features::rl_size](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#ac86ae6974627ddb2e34b0d028cdcfe32)
- [bt_le_local_features::iso_mtu](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md#ad7b95feb82c1dece8bb8bb7969efa2ec)
- [bt_le_oob_sc_data::c](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md#a9bd93f1e9e41e241d0f84ae16ae47ba1)
- [bt_le_oob_sc_data::r](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md#afa64bcc048d0e8709e262e2848a39d2c)
- [bt_le_oob::addr](../bluetooth_connection_model_reference/P110_bt_le_oob_结构体.md#a17cfed7683efbf5b5954847d655d7424)
- [bt_le_oob::le_sc_data](../bluetooth_connection_model_reference/P110_bt_le_oob_结构体.md#a80ccd4ab120a880adfff9aba3b19b4fd)
- [bt_le_per_adv_data_request::count](../bluetooth_connection_model_reference/P112_bt_le_per_adv_data_request_结构体.md#a766991899bc3e689adec36bf1f12e802)
- [bt_le_per_adv_data_request::start](../bluetooth_connection_model_reference/P112_bt_le_per_adv_data_request_结构体.md#a779ed161919c3117f6ce165deb0a9b0a)
- [bt_le_per_adv_param::response_slot_delay](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a07302e13735f502b8950a92b365ef14a)
- [bt_le_per_adv_param::num_response_slots](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a0a8606c103fd91f3222bae6c9f1204fd)
- [bt_le_per_adv_param::subevent_interval](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a28655741c63775a274c42ad5057d4a1d)
- [bt_le_per_adv_param::interval_min](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a49da44a3c0e4e866ffccffae5a9a22f7)
- [bt_le_per_adv_param::interval_max](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a61308cfe72ad23372dfd2a3bd2550726)
- [bt_le_per_adv_param::response_slot_spacing](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a67116b81e8ce968cf411843646801ac4)
- [bt_le_per_adv_param::options](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#a9b80c2427171920f466601e7e8468814)
- [bt_le_per_adv_param::num_subevents](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md#af8be989979c98a17828819ec43dd0b49)
- [bt_le_per_adv_response_info::subevent](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md#a1b87ab77f5c7d4ee0c1c612bcfb424d5)
- [bt_le_per_adv_response_info::rssi](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md#a2db58fb452a07290ab4a50892c682837)
- [bt_le_per_adv_response_info::cte_type](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md#a52b0c612b09cfcb3eb2ea475614c34b8)
- [bt_le_per_adv_response_info::tx_power](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md#a7ed20f695e0d696eaab7cddc4e3c11fb)
- [bt_le_per_adv_response_info::response_slot](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md#a83cc642c9f22c767421644e7d8233001)
- [bt_le_per_adv_response_info::tx_status](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md#ab17f33cb713d258bf6c863a64e5aba07)
- [bt_le_per_adv_response_params::response_subevent](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md#a0cec222d5ba8cc9e20939d441646c913)
- [bt_le_per_adv_response_params::request_event](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md#a1af01d0a027fb8659615874acbd388f9)
- [bt_le_per_adv_response_params::request_subevent](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md#a3fc8ab0feb06714b28d22439cce60e41)
- [bt_le_per_adv_response_params::response_slot](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md#aea0428083ccd5f4dccc17e494f38b7c3)
- [bt_le_per_adv_subevent_data_params::response_slot_start](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md#a1354e9505239de3c42969138d719d775)
- [bt_le_per_adv_subevent_data_params::data](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md#a46103c988d8ac360b7e26310a0322b4e)
- [bt_le_per_adv_subevent_data_params::subevent](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md#a55f2da6041b538b3bc4bff38cd4d2953)
- [bt_le_per_adv_subevent_data_params::response_slot_count](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md#a86d858606943a82917835a0172e88663)
- [bt_le_per_adv_sync_cb::node](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#a1977d27941063773c953a5f1dfa9ca76)
- [bt_le_per_adv_sync_cb::recv](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#a5576248e2eaef2afebe606e05e55f05f)
- [bt_le_per_adv_sync_cb::state_changed](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#a656b4802f79d4a472c2367ade144d72e)
- [bt_le_per_adv_sync_cb::synced](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#a815be4343ab589df433a551663c5f4a1)
- [bt_le_per_adv_sync_cb::biginfo](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#aa44efa17bc28da1952785063a9baf6a9)
- [bt_le_per_adv_sync_cb::term](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#acbd565a39918e5dfe7603a020e73daec)
- [bt_le_per_adv_sync_cb::cte_report_cb](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md#ad2dc168696fbd22f7e3a089ac56f62d7)
- [bt_le_per_adv_sync_info::interval](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md#a365a0d8577429e4ee96e977071c9a906)
- [bt_le_per_adv_sync_info::phy](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md#a4d9520ea6a803f8fe4f41190f55c26e5)
- [bt_le_per_adv_sync_info::addr](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md#ac10fc2e2d3ec2160db8c2aac148d18a2)
- [bt_le_per_adv_sync_info::sid](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md#acc0ef26c38279c9a67f8992005c2e58a)
- [bt_le_per_adv_sync_param::timeout](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md#a301cfd3d6e5620d29c021ababe104754)
- [bt_le_per_adv_sync_param::options](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md#a4252f2b3b453c2f9c8fbf8c35a618ff2)
- [bt_le_per_adv_sync_param::sid](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md#a70795642ee94dd9e87f0cf251c095e7f)
- [bt_le_per_adv_sync_param::addr](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md#ac93adedad747f61a771ac5445e486b74)
- [bt_le_per_adv_sync_param::skip](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md#af9abb65547fb5bfea65f4c22963c7da0)
- [bt_le_per_adv_sync_recv_info::cte_type](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#a1591907e3cb1f4565b9d26c18bccc7d2)
- [bt_le_per_adv_sync_recv_info::subevent](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#a1a9dccd6d7592868b5604ec16a5f1540)
- [bt_le_per_adv_sync_recv_info::sid](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#a21b0ca87e46c6897282ebd877e45114e)
- [bt_le_per_adv_sync_recv_info::addr](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#a5817bd4fba2c93adebcebe007650b6eb)
- [bt_le_per_adv_sync_recv_info::tx_power](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#a65f1a2adb7c3d740cb8262ae7f5a7c3e)
- [bt_le_per_adv_sync_recv_info::periodic_event_counter](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#a74f6dc1745a756faca2e323292024730)
- [bt_le_per_adv_sync_recv_info::rssi](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md#aa17c9d917469f121448ed4e1db485700)
- [bt_le_per_adv_sync_state_info::recv_enabled](../bluetooth_connection_model_reference/P122_bt_le_per_adv_sync_state_info_结构体.md#a4b0a3b7e36f935e06072304d6b92579f)
- [bt_le_per_adv_sync_subevent_params::subevents](../bluetooth_connection_model_reference/P123_bt_le_per_adv_sync_subevent_params_结构体.md#a5ac4e81ddd63797f921105748344c125)
- [bt_le_per_adv_sync_subevent_params::properties](../bluetooth_connection_model_reference/P123_bt_le_per_adv_sync_subevent_params_结构体.md#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4)
- [bt_le_per_adv_sync_subevent_params::num_subevents](../bluetooth_connection_model_reference/P123_bt_le_per_adv_sync_subevent_params_结构体.md#a867c66bf09461a4369da3d250701d2ae)
- [bt_le_per_adv_sync_synced_info::recv_enabled](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a0dd4b7646da0fadc48e94ff3dc91ef83)
- [bt_le_per_adv_sync_synced_info::interval](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a5304e1826face35c506f3b8f6cad7df2)
- [bt_le_per_adv_sync_synced_info::sid](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a5489c3038f7fff596316a456fc8d580b)
- [bt_le_per_adv_sync_synced_info::response_slot_delay](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a7bdec5d34b97602aa56c1006dbaf79c4)
- [bt_le_per_adv_sync_synced_info::addr](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a7ca99b0596b08d153d3ba5310adab125)
- [bt_le_per_adv_sync_synced_info::phy](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a8b7709011541e95ceaeac379cc3143bb)
- [bt_le_per_adv_sync_synced_info::subevent_interval](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#a9e01fb9462c4874a60ebc5359fe5df14)
- [bt_le_per_adv_sync_synced_info::num_subevents](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#aaab25f36577948d55b6379abe0590c69)
- [bt_le_per_adv_sync_synced_info::conn](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#ada4cda53aa87f29d54f6cd88134efe14)
- [bt_le_per_adv_sync_synced_info::service_data](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#adee2bdafa86a0c3c1dfb4660e85396a3)
- [bt_le_per_adv_sync_synced_info::response_slot_spacing](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md#ae9a696dd9dc28b7505e406961ca89b9a)
- [bt_le_per_adv_sync_term_info::addr](../bluetooth_connection_model_reference/P125_bt_le_per_adv_sync_term_info_结构体.md#a2b76ccd5e4c9933f2c05db2ec5b8e2fc)
- [bt_le_per_adv_sync_term_info::reason](../bluetooth_connection_model_reference/P125_bt_le_per_adv_sync_term_info_结构体.md#a429b8b665eacbfe9db013a571b829bac)
- [bt_le_per_adv_sync_term_info::sid](../bluetooth_connection_model_reference/P125_bt_le_per_adv_sync_term_info_结构体.md#a7a5f2ecccaf698bad86f10d9a7d16189)
- [bt_le_per_adv_sync_transfer_param::options](../bluetooth_connection_model_reference/P126_bt_le_per_adv_sync_transfer_param_结构体.md#a0b3ee6df1b409e64a064ffb6ac632cce)
- [bt_le_per_adv_sync_transfer_param::timeout](../bluetooth_connection_model_reference/P126_bt_le_per_adv_sync_transfer_param_结构体.md#a5bfa84c6bdacdf8893a0951a5ce71fc6)
- [bt_le_per_adv_sync_transfer_param::skip](../bluetooth_connection_model_reference/P126_bt_le_per_adv_sync_transfer_param_结构体.md#a840e7cfac3a2947e5128d704067aaf7e)
- [bt_le_scan_cb::timeout](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md#a2f57f3fee46bd137065f4c57d0cd5157)
- [bt_le_scan_cb::node](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md#a50dbc5e7618fd488e9acb7ad8f104a63)
- [bt_le_scan_cb::recv](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md#a71d73c1da28d4a27626f77d96a5b3541)
- [bt_le_scan_param::type](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#a02d75322390287c3fa754bf915660d0c)
- [bt_le_scan_param::interval](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#a2f4e053d97c62b6fdf42a245908607f8)
- [bt_le_scan_param::window](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#a37a7ee82e86a91cf7a9c2adf60bb526a)
- [bt_le_scan_param::timeout](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#a3e71ce551dcc7762c29e2316996e2912)
- [bt_le_scan_param::interval_coded](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#a67a20bc94a3d98fa10af7b5b42dde328)
- [bt_le_scan_param::window_coded](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#a93166af55dca71393c60cb3f7ac6d809)
- [bt_le_scan_param::options](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md#ac815b05fee8ce0dd24228305b7596207)
- [bt_le_scan_recv_info::interval](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a1060c5937708ff81a64f068e02fc7826)
- [bt_le_scan_recv_info::tx_power](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a2addeba6d2ec8e55dc5379adf6519148)
- [bt_le_scan_recv_info::sid](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a4df8d4e1fdd7514d170744856ebe7015)
- [bt_le_scan_recv_info::primary_phy](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a6189ed8453cb7907f34dc7dfaf1343bd)
- [bt_le_scan_recv_info::direct_addr](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a8885283f39e3ece5d7ff7d5b5d588696)
- [bt_le_scan_recv_info::rssi](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a88f677733147245ccbf861c7fc5e0f11)
- [bt_le_scan_recv_info::addr](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a907fb7ec3c78d68da5015a8c3afc3084)
- [bt_le_scan_recv_info::secondary_phy](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#ac797291291dc7ba7ac171ed7f24f0d16)
- [bt_le_scan_recv_info::adv_type](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#adccb2ce5c6d228bd7f8f050088629524)
- [bt_le_scan_recv_info::adv_props](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#af29ddfb59e286af9ca465cbd5a91bf2d)
- [net_buf_simple::data](../network_core_model_reference/P048_net_buf_simple_结构体.md#ad232efff435f425d30ac78f5abf2d8b1)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P002_blob_io_flash.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_brg_cfg.h_源码浏览.md)
