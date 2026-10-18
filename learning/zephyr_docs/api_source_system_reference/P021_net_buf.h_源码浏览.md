---
id: learning.zephyr-docs.api-source-system-reference.page-21
title: net_buf.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_net\_buf.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)。

## 21.1\_原始可见代码（Source Code）

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
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="foldopen00151"></a>
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
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00855"></a>
<a id="l00856"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00879"></a>
<a id="l00880"></a>
<a id="l00891"></a>
<a id="l00892"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="foldopen00914"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="foldopen00928"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="foldopen00942"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="foldopen00961"></a>
<a id="l00961"></a>
<a id="l00962"></a>
<a id="l00963"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="foldopen00983"></a>
<a id="l00983"></a>
<a id="l00984"></a>
<a id="l00985"></a>
<a id="l00986"></a>
<a id="l00987"></a>
<a id="l00988"></a>
<a id="l00989"></a>
<a id="l00990"></a>
<a id="l00991"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l00995"></a>
<a id="l00996"></a>
<a id="l00997"></a>
<a id="l00998"></a>
<a id="foldopen01006"></a>
<a id="l01006"></a>
<a id="l01008"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01012"></a>
<a id="foldopen01021"></a>
<a id="l01021"></a>
<a id="l01022"></a>
<a id="l01023"></a>
<a id="l01024"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="foldopen01037"></a>
<a id="l01037"></a>
<a id="l01038"></a>
<a id="l01039"></a>
<a id="l01040"></a>
<a id="l01041"></a>
<a id="l01042"></a>
<a id="l01043"></a>
<a id="l01053"></a>
<a id="l01054"></a>
<a id="foldopen01062"></a>
<a id="l01062"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="l01100"></a>
<a id="l01102"></a>
<a id="l01104"></a>
<a id="l01105"></a>
<a id="l01106"></a>
<a id="l01107"></a>
<a id="l01108"></a>
<a id="l01109"></a>
<a id="l01110"></a>
<a id="l01111"></a>
<a id="l01112"></a>
<a id="l01114"></a>
<a id="l01116"></a>
<a id="l01118"></a>
<a id="l01119"></a>
<a id="l01121"></a>
<a id="l01122"></a>
<a id="l01124"></a>
<a id="l01125"></a>
<a id="l01127"></a>
<a id="l01128"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01133"></a>
<a id="l01134"></a>
<a id="l01136"></a>
<a id="l01137"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01141"></a>
<a id="l01142"></a>
<a id="l01143"></a>
<a id="l01147"></a>
<a id="l01148"></a>
<a id="l01149"></a>
<a id="l01151"></a>
<a id="l01152"></a>
<a id="l01154"></a>
<a id="l01155"></a>
<a id="l01157"></a>
<a id="l01158"></a>
<a id="l01163"></a>
<a id="l01164"></a>
<a id="l01165"></a>
<a id="l01167"></a>
<a id="l01169"></a>
<a id="l01170"></a>
<a id="l01172"></a>
<a id="l01173"></a>
<a id="l01174"></a>
<a id="l01176"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="l01179"></a>
<a id="l01180"></a>
<a id="l01181"></a>
<a id="l01182"></a>
<a id="l01183"></a>
<a id="l01184"></a>
<a id="l01185"></a>
<a id="l01186"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="l01192"></a>
<a id="foldopen01198"></a>
<a id="l01198"></a>
<a id="l01200"></a>
<a id="l01201"></a>
<a id="l01203"></a>
<a id="l01204"></a>
<a id="l01206"></a>
<a id="l01207"></a>
<a id="l01209"></a>
<a id="l01210"></a>
<a id="l01212"></a>
<a id="l01213"></a>
<a id="l01214"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01219"></a>
<a id="l01220"></a>
<a id="l01222"></a>
<a id="l01223"></a>
<a id="l01225"></a>
<a id="l01226"></a>
<a id="l01227"></a>
<a id="l01229"></a>
<a id="l01230"></a>
<a id="l01232"></a>
<a id="l01233"></a>
<a id="l01235"></a>
<a id="l01236"></a>
<a id="l01237"></a>
<a id="l01239"></a>
<a id="l01240"></a>
<a id="l01241"></a>
<a id="l01242"></a>
<a id="l01243"></a>
<a id="l01244"></a>
<a id="l01245"></a>
<a id="l01246"></a>
<a id="l01247"></a>
<a id="l01248"></a>
<a id="l01249"></a>
<a id="l01250"></a>
<a id="l01251"></a>
<a id="l01252"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01258"></a>
<a id="l01259"></a>
<a id="l01260"></a>
<a id="l01261"></a>
<a id="l01262"></a>
<a id="l01263"></a>
<a id="l01264"></a>
<a id="l01265"></a>
<a id="l01266"></a>
<a id="l01267"></a>
<a id="l01268"></a>
<a id="l01269"></a>
<a id="l01270"></a>
<a id="l01272"></a>
<a id="foldopen01300"></a>
<a id="l01300"></a>
<a id="l01301"></a>
<a id="l01302"></a>
<a id="l01303"></a>
<a id="l01304"></a>
<a id="l01305"></a>
<a id="l01306"></a>
<a id="l01308"></a>
<a id="l01309"></a>
<a id="l01310"></a>
<a id="l01311"></a>
<a id="l01312"></a>
<a id="l01313"></a>
<a id="l01314"></a>
<a id="l01316"></a>
<a id="foldopen01345"></a>
<a id="l01345"></a>
<a id="l01346"></a>
<a id="l01347"></a>
<a id="l01348"></a>
<a id="l01349"></a>
<a id="l01350"></a>
<a id="l01351"></a>
<a id="l01352"></a>
<a id="l01353"></a>
<a id="l01354"></a>
<a id="l01355"></a>
<a id="l01356"></a>
<a id="l01357"></a>
<a id="l01358"></a>
<a id="l01359"></a>
<a id="l01360"></a>
<a id="l01362"></a>
<a id="l01364"></a>
<a id="foldopen01389"></a>
<a id="l01389"></a>
<a id="l01390"></a>
<a id="l01391"></a>
<a id="l01392"></a>
<a id="l01393"></a>
<a id="l01394"></a>
<a id="l01395"></a>
<a id="l01396"></a>
<a id="l01397"></a>
<a id="l01398"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01432"></a>
<a id="l01433"></a>
<a id="l01434"></a>
<a id="l01435"></a>
<a id="l01436"></a>
<a id="l01437"></a>
<a id="l01438"></a>
<a id="l01439"></a>
<a id="l01440"></a>
<a id="l01441"></a>
<a id="l01442"></a>
<a id="l01443"></a>
<a id="l01444"></a>
<a id="l01445"></a>
<a id="l01446"></a>
<a id="foldopen01468"></a>
<a id="l01468"></a>
<a id="l01469"></a>
<a id="l01470"></a>
<a id="l01478"></a>
<a id="l01479"></a>
<a id="l01492"></a>
<a id="l01493"></a>
<a id="l01494"></a>
<a id="foldopen01508"></a>
<a id="l01508"></a>
<a id="l01509"></a>
<a id="l01510"></a>
<a id="l01511"></a>
<a id="l01512"></a>
<a id="foldopen01522"></a>
<a id="l01522"></a>
<a id="l01523"></a>
<a id="l01524"></a>
<a id="l01525"></a>
<a id="l01526"></a>
<a id="l01527"></a>
<a id="l01542"></a>
<a id="l01543"></a>
<a id="l01544"></a>
<a id="l01545"></a>
<a id="l01546"></a>
<a id="l01547"></a>
<a id="l01548"></a>
<a id="l01549"></a>
<a id="l01550"></a>
<a id="l01551"></a>
<a id="l01552"></a>
<a id="l01553"></a>
<a id="foldopen01557"></a>
<a id="l01557"></a>
<a id="l01558"></a>
<a id="l01559"></a>
<a id="l01560"></a>
<a id="l01561"></a>
<a id="l01562"></a>
<a id="l01578"></a>
<a id="l01579"></a>
<a id="l01580"></a>
<a id="l01581"></a>
<a id="l01582"></a>
<a id="l01583"></a>
<a id="l01584"></a>
<a id="l01585"></a>
<a id="l01586"></a>
<a id="l01587"></a>
<a id="l01588"></a>
<a id="l01589"></a>
<a id="l01590"></a>
<a id="l01591"></a>
<a id="l01613"></a>
<a id="l01614"></a>
<a id="l01615"></a>
<a id="l01616"></a>
<a id="l01617"></a>
<a id="l01618"></a>
<a id="l01619"></a>
<a id="l01620"></a>
<a id="l01621"></a>
<a id="l01622"></a>
<a id="l01623"></a>
<a id="l01624"></a>
<a id="l01625"></a>
<a id="l01626"></a>
<a id="foldopen01636"></a>
<a id="l01636"></a>
<a id="l01637"></a>
<a id="l01638"></a>
<a id="l01639"></a>
<a id="l01640"></a>
<a id="l01641"></a>
<a id="l01642"></a>
<a id="l01643"></a>
<a id="l01644"></a>
<a id="l01645"></a>
<a id="l01646"></a>
<a id="l01647"></a>
<a id="l01648"></a>
<a id="l01649"></a>
<a id="l01657"></a>
<a id="l01658"></a>
<a id="l01667"></a>
<a id="l01668"></a>
<a id="l01679"></a>
<a id="l01680"></a>
<a id="l01690"></a>
<a id="l01691"></a>
<a id="l01699"></a>
<a id="l01700"></a>
<a id="l01701"></a>
<a id="l01702"></a>
<a id="l01703"></a>
<a id="l01704"></a>
<a id="l01705"></a>
<a id="l01706"></a>
<a id="l01714"></a>
<a id="l01715"></a>
<a id="foldopen01739"></a>
<a id="l01739"></a>
<a id="l01740"></a>
<a id="l01741"></a>
<a id="l01742"></a>
<a id="l01743"></a>
<a id="foldopen01752"></a>
<a id="l01752"></a>
<a id="l01753"></a>
<a id="l01754"></a>
<a id="l01755"></a>
<a id="l01756"></a>
<a id="l01757"></a>
<a id="l01758"></a>
<a id="l01759"></a>
<a id="l01760"></a>
<a id="l01774"></a>
<a id="l01775"></a>
<a id="l01776"></a>
<a id="foldopen01784"></a>
<a id="l01784"></a>
<a id="l01785"></a>
<a id="l01786"></a>
<a id="l01787"></a>
<a id="l01788"></a>
<a id="l01798"></a>
<a id="l01799"></a>
<a id="foldopen01808"></a>
<a id="l01808"></a>
<a id="l01809"></a>
<a id="l01810"></a>
<a id="l01811"></a>
<a id="l01812"></a>
<a id="foldopen01824"></a>
<a id="l01824"></a>
<a id="l01825"></a>
<a id="l01826"></a>
<a id="l01827"></a>
<a id="l01828"></a>
<a id="foldopen01841"></a>
<a id="l01841"></a>
<a id="l01842"></a>
<a id="l01843"></a>
<a id="l01844"></a>
<a id="l01845"></a>
<a id="l01846"></a>
<a id="foldopen01858"></a>
<a id="l01858"></a>
<a id="l01859"></a>
<a id="l01860"></a>
<a id="l01861"></a>
<a id="l01862"></a>
<a id="foldopen01873"></a>
<a id="l01873"></a>
<a id="l01874"></a>
<a id="l01875"></a>
<a id="l01876"></a>
<a id="l01877"></a>
<a id="foldopen01888"></a>
<a id="l01888"></a>
<a id="l01889"></a>
<a id="l01890"></a>
<a id="l01891"></a>
<a id="l01892"></a>
<a id="foldopen01903"></a>
<a id="l01903"></a>
<a id="l01904"></a>
<a id="l01905"></a>
<a id="l01906"></a>
<a id="l01907"></a>
<a id="foldopen01918"></a>
<a id="l01918"></a>
<a id="l01919"></a>
<a id="l01920"></a>
<a id="l01921"></a>
<a id="l01922"></a>
<a id="foldopen01933"></a>
<a id="l01933"></a>
<a id="l01934"></a>
<a id="l01935"></a>
<a id="l01936"></a>
<a id="l01937"></a>
<a id="foldopen01948"></a>
<a id="l01948"></a>
<a id="l01949"></a>
<a id="l01950"></a>
<a id="l01951"></a>
<a id="l01952"></a>
<a id="foldopen01963"></a>
<a id="l01963"></a>
<a id="l01964"></a>
<a id="l01965"></a>
<a id="l01966"></a>
<a id="l01967"></a>
<a id="foldopen01978"></a>
<a id="l01978"></a>
<a id="l01979"></a>
<a id="l01980"></a>
<a id="l01981"></a>
<a id="l01982"></a>
<a id="foldopen01993"></a>
<a id="l01993"></a>
<a id="l01994"></a>
<a id="l01995"></a>
<a id="l01996"></a>
<a id="l01997"></a>
<a id="foldopen02008"></a>
<a id="l02008"></a>
<a id="l02009"></a>
<a id="l02010"></a>
<a id="l02011"></a>
<a id="l02012"></a>
<a id="foldopen02023"></a>
<a id="l02023"></a>
<a id="l02024"></a>
<a id="l02025"></a>
<a id="l02026"></a>
<a id="l02027"></a>
<a id="foldopen02038"></a>
<a id="l02038"></a>
<a id="l02039"></a>
<a id="l02040"></a>
<a id="l02041"></a>
<a id="l02042"></a>
<a id="foldopen02053"></a>
<a id="l02053"></a>
<a id="l02054"></a>
<a id="l02055"></a>
<a id="l02056"></a>
<a id="l02057"></a>
<a id="foldopen02068"></a>
<a id="l02068"></a>
<a id="l02069"></a>
<a id="l02070"></a>
<a id="l02071"></a>
<a id="l02072"></a>
<a id="foldopen02083"></a>
<a id="l02083"></a>
<a id="l02084"></a>
<a id="l02085"></a>
<a id="l02086"></a>
<a id="l02087"></a>
<a id="foldopen02098"></a>
<a id="l02098"></a>
<a id="l02099"></a>
<a id="l02100"></a>
<a id="l02101"></a>
<a id="l02102"></a>
<a id="foldopen02113"></a>
<a id="l02113"></a>
<a id="l02114"></a>
<a id="l02115"></a>
<a id="l02116"></a>
<a id="l02117"></a>
<a id="foldopen02128"></a>
<a id="l02128"></a>
<a id="l02129"></a>
<a id="l02130"></a>
<a id="l02131"></a>
<a id="l02132"></a>
<a id="foldopen02143"></a>
<a id="l02143"></a>
<a id="l02144"></a>
<a id="l02145"></a>
<a id="l02146"></a>
<a id="l02147"></a>
<a id="foldopen02158"></a>
<a id="l02158"></a>
<a id="l02159"></a>
<a id="l02160"></a>
<a id="l02161"></a>
<a id="l02162"></a>
<a id="foldopen02173"></a>
<a id="l02173"></a>
<a id="l02174"></a>
<a id="l02175"></a>
<a id="l02176"></a>
<a id="l02177"></a>
<a id="foldopen02188"></a>
<a id="l02188"></a>
<a id="l02189"></a>
<a id="l02190"></a>
<a id="l02191"></a>
<a id="l02192"></a>
<a id="foldopen02203"></a>
<a id="l02203"></a>
<a id="l02204"></a>
<a id="l02205"></a>
<a id="l02206"></a>
<a id="l02207"></a>
<a id="foldopen02218"></a>
<a id="l02218"></a>
<a id="l02219"></a>
<a id="l02220"></a>
<a id="l02221"></a>
<a id="l02222"></a>
<a id="foldopen02233"></a>
<a id="l02233"></a>
<a id="l02234"></a>
<a id="l02235"></a>
<a id="l02236"></a>
<a id="l02237"></a>
<a id="foldopen02248"></a>
<a id="l02248"></a>
<a id="l02249"></a>
<a id="l02250"></a>
<a id="l02251"></a>
<a id="l02252"></a>
<a id="foldopen02264"></a>
<a id="l02264"></a>
<a id="l02265"></a>
<a id="l02266"></a>
<a id="l02267"></a>
<a id="l02268"></a>
<a id="foldopen02281"></a>
<a id="l02281"></a>
<a id="l02282"></a>
<a id="l02283"></a>
<a id="l02284"></a>
<a id="l02285"></a>
<a id="l02286"></a>
<a id="foldopen02295"></a>
<a id="l02295"></a>
<a id="l02296"></a>
<a id="l02297"></a>
<a id="l02298"></a>
<a id="l02299"></a>
<a id="foldopen02309"></a>
<a id="l02309"></a>
<a id="l02310"></a>
<a id="l02311"></a>
<a id="l02312"></a>
<a id="l02313"></a>
<a id="foldopen02323"></a>
<a id="l02323"></a>
<a id="l02324"></a>
<a id="l02325"></a>
<a id="l02326"></a>
<a id="l02327"></a>
<a id="foldopen02337"></a>
<a id="l02337"></a>
<a id="l02338"></a>
<a id="l02339"></a>
<a id="l02340"></a>
<a id="l02341"></a>
<a id="foldopen02351"></a>
<a id="l02351"></a>
<a id="l02352"></a>
<a id="l02353"></a>
<a id="l02354"></a>
<a id="l02355"></a>
<a id="foldopen02365"></a>
<a id="l02365"></a>
<a id="l02366"></a>
<a id="l02367"></a>
<a id="l02368"></a>
<a id="l02369"></a>
<a id="foldopen02379"></a>
<a id="l02379"></a>
<a id="l02380"></a>
<a id="l02381"></a>
<a id="l02382"></a>
<a id="l02383"></a>
<a id="foldopen02393"></a>
<a id="l02393"></a>
<a id="l02394"></a>
<a id="l02395"></a>
<a id="l02396"></a>
<a id="l02397"></a>
<a id="foldopen02407"></a>
<a id="l02407"></a>
<a id="l02408"></a>
<a id="l02409"></a>
<a id="l02410"></a>
<a id="l02411"></a>
<a id="foldopen02421"></a>
<a id="l02421"></a>
<a id="l02422"></a>
<a id="l02423"></a>
<a id="l02424"></a>
<a id="l02425"></a>
<a id="foldopen02435"></a>
<a id="l02435"></a>
<a id="l02436"></a>
<a id="l02437"></a>
<a id="l02438"></a>
<a id="l02439"></a>
<a id="foldopen02449"></a>
<a id="l02449"></a>
<a id="l02450"></a>
<a id="l02451"></a>
<a id="l02452"></a>
<a id="l02453"></a>
<a id="foldopen02463"></a>
<a id="l02463"></a>
<a id="l02464"></a>
<a id="l02465"></a>
<a id="l02466"></a>
<a id="l02467"></a>
<a id="foldopen02479"></a>
<a id="l02479"></a>
<a id="l02480"></a>
<a id="l02481"></a>
<a id="l02482"></a>
<a id="l02483"></a>
<a id="foldopen02495"></a>
<a id="l02495"></a>
<a id="l02496"></a>
<a id="l02497"></a>
<a id="l02498"></a>
<a id="l02499"></a>
<a id="foldopen02510"></a>
<a id="l02510"></a>
<a id="l02511"></a>
<a id="l02512"></a>
<a id="l02513"></a>
<a id="l02514"></a>
<a id="foldopen02525"></a>
<a id="l02525"></a>
<a id="l02526"></a>
<a id="l02527"></a>
<a id="l02528"></a>
<a id="l02529"></a>
<a id="foldopen02540"></a>
<a id="l02540"></a>
<a id="l02541"></a>
<a id="l02542"></a>
<a id="l02543"></a>
<a id="l02544"></a>
<a id="foldopen02555"></a>
<a id="l02555"></a>
<a id="l02556"></a>
<a id="l02557"></a>
<a id="l02558"></a>
<a id="l02559"></a>
<a id="foldopen02570"></a>
<a id="l02570"></a>
<a id="l02571"></a>
<a id="l02572"></a>
<a id="l02573"></a>
<a id="l02574"></a>
<a id="foldopen02585"></a>
<a id="l02585"></a>
<a id="l02586"></a>
<a id="l02587"></a>
<a id="l02588"></a>
<a id="l02589"></a>
<a id="foldopen02600"></a>
<a id="l02600"></a>
<a id="l02601"></a>
<a id="l02602"></a>
<a id="l02603"></a>
<a id="l02604"></a>
<a id="foldopen02615"></a>
<a id="l02615"></a>
<a id="l02616"></a>
<a id="l02617"></a>
<a id="l02618"></a>
<a id="l02619"></a>
<a id="foldopen02630"></a>
<a id="l02630"></a>
<a id="l02631"></a>
<a id="l02632"></a>
<a id="l02633"></a>
<a id="l02634"></a>
<a id="foldopen02645"></a>
<a id="l02645"></a>
<a id="l02646"></a>
<a id="l02647"></a>
<a id="l02648"></a>
<a id="l02649"></a>
<a id="foldopen02660"></a>
<a id="l02660"></a>
<a id="l02661"></a>
<a id="l02662"></a>
<a id="l02663"></a>
<a id="l02664"></a>
<a id="foldopen02675"></a>
<a id="l02675"></a>
<a id="l02676"></a>
<a id="l02677"></a>
<a id="l02678"></a>
<a id="l02679"></a>
<a id="foldopen02690"></a>
<a id="l02690"></a>
<a id="l02691"></a>
<a id="l02692"></a>
<a id="l02693"></a>
<a id="l02694"></a>
<a id="foldopen02704"></a>
<a id="l02704"></a>
<a id="l02705"></a>
<a id="l02706"></a>
<a id="l02707"></a>
<a id="l02708"></a>
<a id="foldopen02718"></a>
<a id="l02718"></a>
<a id="l02719"></a>
<a id="l02720"></a>
<a id="l02721"></a>
<a id="l02722"></a>
<a id="foldopen02737"></a>
<a id="l02737"></a>
<a id="l02738"></a>
<a id="l02739"></a>
<a id="l02740"></a>
<a id="l02741"></a>
<a id="foldopen02757"></a>
<a id="l02757"></a>
<a id="l02758"></a>
<a id="l02759"></a>
<a id="l02760"></a>
<a id="l02761"></a>
<a id="foldopen02771"></a>
<a id="l02771"></a>
<a id="l02772"></a>
<a id="l02773"></a>
<a id="l02774"></a>
<a id="l02775"></a>
<a id="l02781"></a>
<a id="l02782"></a>
<a id="l02794"></a>
<a id="l02795"></a>
<a id="l02812"></a>
<a id="l02813"></a>
<a id="l02823"></a>
<a id="l02824"></a>
<a id="l02825"></a>
<a id="l02826"></a>
<a id="l02827"></a>
<a id="l02828"></a>
<a id="l02829"></a>
<a id="l02830"></a>
<a id="l02831"></a>
<a id="l02832"></a>
<a id="l02848"></a>
<a id="l02849"></a>
<a id="l02850"></a>
<a id="l02865"></a>
<a id="l02866"></a>
<a id="l02867"></a>
<a id="l02891"></a>
<a id="l02892"></a>
<a id="l02893"></a>
<a id="l02894"></a>
<a id="l02909"></a>
<a id="l02910"></a>
<a id="foldopen02924"></a>
<a id="l02924"></a>
<a id="l02925"></a>
<a id="l02926"></a>
<a id="l02927"></a>
<a id="l02928"></a>
<a id="l02929"></a>
<a id="l02930"></a>
<a id="l02931"></a>
<a id="l02932"></a>
<a id="l02933"></a>
<a id="l02934"></a>
<a id="l02935"></a>
<a id="l02936"></a>
<a id="l02937"></a>
<a id="l02938"></a>
<a id="l02939"></a>
<a id="l02940"></a>
<a id="l02941"></a>
<a id="l02942"></a>
<a id="foldopen02953"></a>
<a id="l02953"></a>
<a id="l02954"></a>
<a id="l02955"></a>
<a id="l02956"></a>
<a id="l02957"></a>
<a id="l02958"></a>
<a id="l02959"></a>
<a id="l02960"></a>
<a id="l02961"></a>
<a id="l02962"></a>
<a id="l02963"></a>
<a id="l02964"></a>
<a id="l02968"></a>
<a id="l02969"></a>
<a id="l02970"></a>
<a id="l02971"></a>
<a id="l02972"></a>
<a id="l02973"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__atomic__apis_html_ga33bb426a17535bd1022895a7e44b32fa"></a>
<a id="agroup__atomic__apis_html_ga587e3134cd8176e7b1c00361711ee2df"></a>
<a id="agroup__atomic__apis_html_gacad6866fa4c844026cd9f8c3fb60ecd7"></a>
<a id="agroup__lifo__apis_html_gad662e36b1df8b9013e2dc61f9dfe3a8b"></a>
<a id="agroup__net__buf_html_ga0186c153b72a379affdd3e2e3994b5a7"></a>
<a id="agroup__net__buf_html_ga040279b601191367dee013bab9916d8d"></a>
<a id="agroup__net__buf_html_ga042ce3f2e7e3fd0948ca2623fff36746"></a>
<a id="agroup__net__buf_html_ga050bdaccaec842482a02b096aa0c999f"></a>
<a id="agroup__net__buf_html_ga055f6eb7d5fbc9a3cf529a9ed00970c4"></a>
<a id="agroup__net__buf_html_ga09a261c615136fd39834cd301fc692e7"></a>
<a id="agroup__net__buf_html_ga0b57f9ca2f3837e94cd7862e37efc01c"></a>
<a id="agroup__net__buf_html_ga0c147d9f95e2224696a8ace26f63a300"></a>
<a id="agroup__net__buf_html_ga0d7e310802a2bc7b2078f9310827535f"></a>
<a id="agroup__net__buf_html_ga0e5d3d938becfefc4f4b4d083cb467aa"></a>
<a id="agroup__net__buf_html_ga0f19da70bfc8f597680ee02c21226a77"></a>
<a id="agroup__net__buf_html_ga0f3cd9f9b364a2d2125aea19221d3e1e"></a>
<a id="agroup__net__buf_html_ga11d489aedcca82117965fa6ba9d11ca5"></a>
<a id="agroup__net__buf_html_ga1292f38b096fd80e31889aff44b0c021"></a>
<a id="agroup__net__buf_html_ga145f4b2de7548814eaa7ba86fb123989"></a>
<a id="agroup__net__buf_html_ga1906e637c848948f5780428a99b3341e"></a>
<a id="agroup__net__buf_html_ga19bdefe740fe94a42fba76d71b4ef6e2"></a>
<a id="agroup__net__buf_html_ga1a53892ed75f994bbbb3a2bcf1743d3c"></a>
<a id="agroup__net__buf_html_ga1ea39c7d7e9ba4e10d31d818e45e192a"></a>
<a id="agroup__net__buf_html_ga218d4a0c160c57a44946154478724cb3"></a>
<a id="agroup__net__buf_html_ga29387b2a672bf2bb8739046a46f3601f"></a>
<a id="agroup__net__buf_html_ga2c937164e648fe8b854cb1144051b6b9"></a>
<a id="agroup__net__buf_html_ga2d7096280d4fa6f5e32c4674d542889b"></a>
<a id="agroup__net__buf_html_ga30776d2b21f06d244c083af5c25b0f3e"></a>
<a id="agroup__net__buf_html_ga32b90364091ade229830686f03b25d4c"></a>
<a id="agroup__net__buf_html_ga36b27c6373eb245f777164065386d100"></a>
<a id="agroup__net__buf_html_ga38df82e6ba9bc2c75133200f7fa75353"></a>
<a id="agroup__net__buf_html_ga3bf1bcff840dddd721f2c49ef0ed7c56"></a>
<a id="agroup__net__buf_html_ga3c1e80741a49691e69e57c891d3edb05"></a>
<a id="agroup__net__buf_html_ga43ff5faab0b099a355b9b96b7b0e3d8c"></a>
<a id="agroup__net__buf_html_ga447b9c6be3fe04a50eb35dd29f190b6d"></a>
<a id="agroup__net__buf_html_ga4b537e913e132448cbf56976504ddddd"></a>
<a id="agroup__net__buf_html_ga4c24d445d6b75c850a9e95fb242a50e1"></a>
<a id="agroup__net__buf_html_ga4c9d2ac72a176c49ec224353b5566eb9"></a>
<a id="agroup__net__buf_html_ga4d1dd56ca8d32d3cfda114fd36761d0d"></a>
<a id="agroup__net__buf_html_ga4e2fef883228f7de41af3cf90648c3c5"></a>
<a id="agroup__net__buf_html_ga4ff24d6ae1aff46e17647ef91db593ca"></a>
<a id="agroup__net__buf_html_ga50cd64438d8f218e3d1ef8b53b7d41a6"></a>
<a id="agroup__net__buf_html_ga512f84e686ff70a5589557575ccda1f8"></a>
<a id="agroup__net__buf_html_ga534366f3b5c7f41a28372c12149ca005"></a>
<a id="agroup__net__buf_html_ga5543d00c96f83970f8dbf3670a9dc3fc"></a>
<a id="agroup__net__buf_html_ga560bd7b181c7f08599ae9241b6ce99fd"></a>
<a id="agroup__net__buf_html_ga57150a1ba09b28e5c3b04bdefce7ed8e"></a>
<a id="agroup__net__buf_html_ga5be8c9f33df5b31c15df193a7116ce25"></a>
<a id="agroup__net__buf_html_ga5c4038cb3aa506c3cad7a2505392aa50"></a>
<a id="agroup__net__buf_html_ga5da86c8ea703ab3f01c408cce73b0651"></a>
<a id="agroup__net__buf_html_ga5eb09afeff062af577094d2d3f5fdec8"></a>
<a id="agroup__net__buf_html_ga5f051078f1ffcc40e9ad40e7545a084f"></a>
<a id="agroup__net__buf_html_ga5f8f2e2244eb574b3e57d09d85412967"></a>
<a id="agroup__net__buf_html_ga602a99833bd401a0ada5bd5defa7a2ff"></a>
<a id="agroup__net__buf_html_ga602fae83e2ecf47552a11f9282619932"></a>
<a id="agroup__net__buf_html_ga61878a9bd7462ca925eac39181f2972c"></a>
<a id="agroup__net__buf_html_ga62790f9644102f4952c250f6513a2ada"></a>
<a id="agroup__net__buf_html_ga646d680491753b3ed29fa83c26732d1a"></a>
<a id="agroup__net__buf_html_ga64df9754665440370340c6dddde625d1"></a>
<a id="agroup__net__buf_html_ga65924b8234c91dfc09069ba06242a6b7"></a>
<a id="agroup__net__buf_html_ga66b44897e336f31e3ecbf4717bec274e"></a>
<a id="agroup__net__buf_html_ga67da71ba5942cc11e95aa5ba02cb8552"></a>
<a id="agroup__net__buf_html_ga686df794ec6881625b54454a33587bab"></a>
<a id="agroup__net__buf_html_ga68934e105c4b3a8e27aa61b3ec5526db"></a>
<a id="agroup__net__buf_html_ga69bdaf4373693bb468cf3876e9edf239"></a>
<a id="agroup__net__buf_html_ga69fbfbd72b17783c5ee12b4b2ac9af46"></a>
<a id="agroup__net__buf_html_ga6b43ad0740b23c0544d706c77c9f1e13"></a>
<a id="agroup__net__buf_html_ga6d2dfc45e1e5acf21fe08359a4f92a18"></a>
<a id="agroup__net__buf_html_ga6dd756ff8332d076f5d37c69e6c534b5"></a>
<a id="agroup__net__buf_html_ga6f346a9af570528d238592851240fd74"></a>
<a id="agroup__net__buf_html_ga70cb98da91de098a92fbd69712c2bde7"></a>
<a id="agroup__net__buf_html_ga71bb306d2ce459a60a8c3fc6dac54c90"></a>
<a id="agroup__net__buf_html_ga739249547eb37b839b3c1ebdbcb88d28"></a>
<a id="agroup__net__buf_html_ga73e2c42fc23e857a46553084b747c996"></a>
<a id="agroup__net__buf_html_ga745ab6f34138b506b42f78e0975a5d2e"></a>
<a id="agroup__net__buf_html_ga7476ec7222d074e7dc9783e7ed9cd800"></a>
<a id="agroup__net__buf_html_ga771634e50e2bf7c291565ce6b2af7e85"></a>
<a id="agroup__net__buf_html_ga79dc411da328b847dcf1903d71eaf011"></a>
<a id="agroup__net__buf_html_ga7e0e2d0adbe9062d08f5d8afc7acd89e"></a>
<a id="agroup__net__buf_html_ga7e9daccec8cae1b9bfda52b0758adf0c"></a>
<a id="agroup__net__buf_html_ga7eeee45b6639146d1492f92263ee4f51"></a>
<a id="agroup__net__buf_html_ga7fac47a2a25eaca39c5d14f1f55b485d"></a>
<a id="agroup__net__buf_html_ga827bd85eba0dbd098790d84d22e8e32d"></a>
<a id="agroup__net__buf_html_ga8473bdffadc05b22335a321df89f4b83"></a>
<a id="agroup__net__buf_html_ga852654f7e59951bf3536e3f4e98761bf"></a>
<a id="agroup__net__buf_html_ga85c505321484a50ed9422f24934ed077"></a>
<a id="agroup__net__buf_html_ga8662e6bada476c0d48cebea4661b2ac1"></a>
<a id="agroup__net__buf_html_ga868ac2bea103fed568b461cbcd45eda2"></a>
<a id="agroup__net__buf_html_ga87338399d8ecd64a894908ed4a2f710b"></a>
<a id="agroup__net__buf_html_ga87524ac50e53ba59c6692af10cf001b9"></a>
<a id="agroup__net__buf_html_ga8ac58ad4f73b498bef2ff3ac7e30c6c3"></a>
<a id="agroup__net__buf_html_ga8b9edd213da2d48dfb8d70a8d307ba13"></a>
<a id="agroup__net__buf_html_ga8c24d0761d6d38facb6cca60c7c13c0c"></a>
<a id="agroup__net__buf_html_ga8d258ef1e4241c438a726486bc7fe766"></a>
<a id="agroup__net__buf_html_ga8de937e8775879712ea0acbf60327a95"></a>
<a id="agroup__net__buf_html_ga8e31a7b6537d7634e346236534d2a6d0"></a>
<a id="agroup__net__buf_html_ga8fe6feb191ab338e91bd62f44e184deb"></a>
<a id="agroup__net__buf_html_ga8ff9344b8d8deba1b72b8fca048a525c"></a>
<a id="agroup__net__buf_html_ga903f59c8dea1b2c54969b567fe315041"></a>
<a id="agroup__net__buf_html_ga9093202ba0a22bfa519bbe32d4585186"></a>
<a id="agroup__net__buf_html_ga910f2b9df58fb0706aa40e3b80f235aa"></a>
<a id="agroup__net__buf_html_ga93f9f84845601df4ffc118be1ffd2fee"></a>
<a id="agroup__net__buf_html_ga96a2b1f07f3a7958057d9c7cc1f01b73"></a>
<a id="agroup__net__buf_html_ga97909a33c374a5c757fd2faf582139b7"></a>
<a id="agroup__net__buf_html_ga97c9046185d6a1e9235bf6914c72dfc4"></a>
<a id="agroup__net__buf_html_ga9a3df35e2287cbcfe1b60e2efa52c64e"></a>
<a id="agroup__net__buf_html_ga9abd2bccc90cf654556c18322888d131"></a>
<a id="agroup__net__buf_html_ga9b39384162a91d7d07e037a9ada782dd"></a>
<a id="agroup__net__buf_html_ga9b74d094a45daf74cd230eaa4fcbc065"></a>
<a id="agroup__net__buf_html_ga9c676fdbd6e999a9eab26b13d3608e0c"></a>
<a id="agroup__net__buf_html_ga9cd6d30ea47a91647d3c4a60d82b5cd4"></a>
<a id="agroup__net__buf_html_ga9e8d016ce384378142fdec6c8dde2457"></a>
<a id="agroup__net__buf_html_gaa2daf3b20074ff1a23806ce88becebf5"></a>
<a id="agroup__net__buf_html_gaa665830dad59ac957f79c7f1cc84aed5"></a>
<a id="agroup__net__buf_html_gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8"></a>
<a id="agroup__net__buf_html_gaaa838083c610f7426c509efaae69a511"></a>
<a id="agroup__net__buf_html_gaab0e3bcc21c958c01ef076cd0efe087c"></a>
<a id="agroup__net__buf_html_gaac5cd20776d8e7bb4db77cbe5366373c"></a>
<a id="agroup__net__buf_html_gaaeacbdf3cfda12691c75253015e5c19a"></a>
<a id="agroup__net__buf_html_gaaf654110fb6a8bdfc27433945d4d1308"></a>
<a id="agroup__net__buf_html_gab6c84c6846c06c2b339bc88df35e2655"></a>
<a id="agroup__net__buf_html_gab93d22797c3f406179c4c145241d6abb"></a>
<a id="agroup__net__buf_html_gabe52d6735d835edc361666bb3413b907"></a>
<a id="agroup__net__buf_html_gabedcb728bc2fc0c2b5319a8fd87e8273"></a>
<a id="agroup__net__buf_html_gabf5b098aa0926d9b7fb88baff8a3e2d8"></a>
<a id="agroup__net__buf_html_gabfbcb051019ff210cc2b85adcf4bc821"></a>
<a id="agroup__net__buf_html_gabfddd4956ec1e356002a3122fea74b72"></a>
<a id="agroup__net__buf_html_gac032b44db4a845dba8303fecfe1b63e7"></a>
<a id="agroup__net__buf_html_gac0628bbbe5d9c2b82766d5a17e767696"></a>
<a id="agroup__net__buf_html_gac37209c1e5097e5610860943fb7d0115"></a>
<a id="agroup__net__buf_html_gac3f955f8fecc0e5971d2e5e8176e973e"></a>
<a id="agroup__net__buf_html_gac9a09897f44e708f920064826aa2f703"></a>
<a id="agroup__net__buf_html_gacce707d646d7008ec3167af1a0b20da8"></a>
<a id="agroup__net__buf_html_gacdf048dc0afc7ef67027117e0d51d3a3"></a>
<a id="agroup__net__buf_html_gace5ad98eac4772db3b0fa2181912f1f0"></a>
<a id="agroup__net__buf_html_gacf4e2eba52975ba6728c79274a769d0f"></a>
<a id="agroup__net__buf_html_gad07f0d49a7db99063077de493e7b0712"></a>
<a id="agroup__net__buf_html_gad0c3b8fdeaad6437c3dfcbb03fa52426"></a>
<a id="agroup__net__buf_html_gad4ee42b023881f80211fbeca53a0f25d"></a>
<a id="agroup__net__buf_html_gad59d180ae81b55f6d618565a37d25dba"></a>
<a id="agroup__net__buf_html_gad652ef7d2895f8077c366a564b785291"></a>
<a id="agroup__net__buf_html_gad65bcaf8401e6f5ffff81a998cfb8fe5"></a>
<a id="agroup__net__buf_html_gad669c07efe5cb90ebffcc76d9c1029a1"></a>
<a id="agroup__net__buf_html_gad954b9f37790d5e7087db7db7bdedd41"></a>
<a id="agroup__net__buf_html_gadb433fb4a1a61702c0615359a4340171"></a>
<a id="agroup__net__buf_html_gadc6ae86245c2a2607c671a524227b026"></a>
<a id="agroup__net__buf_html_gadd6d01a3b1efd0de16f9bef975809404"></a>
<a id="agroup__net__buf_html_gae2920eab3c56d0d462811b83961df466"></a>
<a id="agroup__net__buf_html_gae36458ba05a4ab89e429be4cfd264440"></a>
<a id="agroup__net__buf_html_gae4e64a23708ed910fb6c3ab8ba481a4c"></a>
<a id="agroup__net__buf_html_gae8ba33b6592ef7fd859b35d63b285d87"></a>
<a id="agroup__net__buf_html_gae8ecc1fbc9dfc007f1b4e932cfaf2f1d"></a>
<a id="agroup__net__buf_html_gae9321a469cc751c58cfb532afd57d265"></a>
<a id="agroup__net__buf_html_gaebb95f08dbd4d38a250170aa78ddeb44"></a>
<a id="agroup__net__buf_html_gaecbc6adf16469e3366c88445ea7a553a"></a>
<a id="agroup__net__buf_html_gaed64e9f2b969f2c0d99cd281e73c860a"></a>
<a id="agroup__net__buf_html_gaedb10a84b352a3d7716bef979af2ab31"></a>
<a id="agroup__net__buf_html_gaedc5ffe19bb0ec438e633023c3c5de74"></a>
<a id="agroup__net__buf_html_gaedd36481657a7a9d108659d56e131721"></a>
<a id="agroup__net__buf_html_gaef433d92734dd8691c292abdb823ba0e"></a>
<a id="agroup__net__buf_html_gaef938c3ab676a5bd5bf8338b8d7cb30c"></a>
<a id="agroup__net__buf_html_gaefab4a755cf4fb7d2b4a142a9351c189"></a>
<a id="agroup__net__buf_html_gaf19bf75c3d4d645b1eebf9254aa22790"></a>
<a id="agroup__net__buf_html_gaf1a89eb15eed79003412ba5a32a35cf6"></a>
<a id="agroup__net__buf_html_gaf2df457abe3e56d47107b76bdc004756"></a>
<a id="agroup__net__buf_html_gaf4d80e2878e3c790fff206bec820f03f"></a>
<a id="agroup__net__buf_html_gaf508f74e5e050a7294e8a70bd3725fc3"></a>
<a id="agroup__net__buf_html_gaf5ab4a5fe4a6226be72a510fea0ed8a8"></a>
<a id="agroup__net__buf_html_gafea2201655955ab004b5f77106998ae9"></a>
<a id="agroup__net__buf_html_gaffd49f2de8e72d5f7585b4e5167923d8"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_ga3acffbd305ee72dcd4593c0d8af64a4f"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructk__lifo_html"></a>
<a id="astructk__spinlock_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf__pool_html_a2a9141d7cd20cd98818a92dc5bc99f56"></a>
<a id="astructnet__buf__pool_html_a3fdf83b4c0b5acefbb761da285791ad2"></a>
<a id="astructnet__buf__pool_html_a4718ecec19d7e2ccaf04b6ff61120975"></a>
<a id="astructnet__buf__pool_html_a55b57f4f573c7e752c3ccf2f92f25626"></a>
<a id="astructnet__buf__pool_html_a617bd8f77e55481d97183da8c0c62cc5"></a>
<a id="astructnet__buf__pool_html_a97e5b2e51238e859f93882a8008ba305"></a>
<a id="astructnet__buf__pool_html_ae92fc3f3f51be63ccdeee9614d21cc34"></a>
<a id="astructnet__buf__simple__state_html"></a>
<a id="astructnet__buf__simple__state_html_a4061f8e50e14289b1ec999ef490c8fbf"></a>
<a id="astructnet__buf__simple__state_html_af0e544fe2b018a7ff0b30970e9de8253"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="astructnet__buf__simple_html_ad232efff435f425d30ac78f5abf2d8b1"></a>
<a id="astructnet__buf__simple_html_ae6dc4aa029a67d3911293618eb30caa6"></a>
<a id="astructnet__buf__simple_html_ae8707c50d70c26b53281b40eb1720cf3"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_a1522d81a002804223e25300a6961f527"></a>
<a id="astructnet__buf_html_a1fa032cc23854c35eae013020823fa88"></a>
<a id="astructnet__buf_html_a42da518a82f4c37c45814b4f8c5f2731"></a>
<a id="astructnet__buf_html_a45f294bac054d64034bddcc4c6574d29"></a>
<a id="astructnet__buf_html_a5cc70f57e5b776cfa12b2d556e5958f3"></a>
<a id="astructnet__buf_html_a65db7bed62d7211114767e6ce58dad75"></a>
<a id="astructnet__buf_html_aa4fcce2e2894fc5dbd9cc74fc020647e"></a>
<a id="astructnet__buf_html_ac6eef59915e7ce167442fdacbbfb5e56"></a>
<a id="astructnet__buf_html_ade8055f804d5a1fea13e55d71d92a5e7"></a>
<a id="astructnet__buf_html_ae75b7ca728fb7440ea483be8bf88bc38"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="asys_2util_8h_html"></a>

```c


/*
 * Copyright (c) 2015 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_NET_BUF_H_
#define ZEPHYR_INCLUDE_NET_BUF_H_

#include <stddef.h>
#include <zephyr/types.h>
#include <zephyr/sys/util.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif


/* Alignment needed for various parts of the buffer definition */
#if CONFIG_NET_BUF_ALIGNMENT == 0
#define __net_buf_align __aligned(sizeof(void *))
#else
#define __net_buf_align __aligned(CONFIG_NET_BUF_ALIGNMENT)
#endif

#define NET_BUF_SIMPLE_DEFINE(_name, _size)     \
        uint8_t net_buf_data_##_name[_size];       \
        struct net_buf_simple _name = {         \
                .data   = net_buf_data_##_name, \
                .len    = 0,                    \
                .size   = _size,                \
                .__buf  = net_buf_data_##_name, \
        }

#define NET_BUF_SIMPLE_DEFINE_STATIC(_name, _size)        \
        static __noinit uint8_t net_buf_data_##_name[_size]; \
        static struct net_buf_simple _name = {            \
                .data   = net_buf_data_##_name,           \
                .len    = 0,                              \
                .size   = _size,                          \
                .__buf  = net_buf_data_##_name,           \
        }

struct net_buf_simple {
        uint8_t *data;

        uint16_t len;

        uint16_t size;

        uint8_t *__buf;
};

#define NET_BUF_SIMPLE(_size)                        \
        ((struct net_buf_simple *)(&(struct {        \
                struct net_buf_simple buf;           \
                uint8_t data[_size];                 \
        }) {                                         \
                .buf.size = _size,                   \
        }))

static inline void net_buf_simple_init(struct net_buf_simple *buf,
                                       size_t reserve_head)
{
        if (!buf->__buf) {
                buf->__buf = (uint8_t *)buf + sizeof(*buf);
        }

        buf->data = buf->__buf + reserve_head;
        buf->len = 0U;
}

void net_buf_simple_init_with_data(struct net_buf_simple *buf,
                                   void *data, size_t size);

static inline void net_buf_simple_reset(struct net_buf_simple *buf)
{
        buf->len  = 0U;
        buf->data = buf->__buf;
}

void net_buf_simple_clone(const struct net_buf_simple *original,
                          struct net_buf_simple *clone);

void *net_buf_simple_add(struct net_buf_simple *buf, size_t len);

void *net_buf_simple_add_mem(struct net_buf_simple *buf, const void *mem,
                             size_t len);

uint8_t *net_buf_simple_add_u8(struct net_buf_simple *buf, uint8_t val);

void net_buf_simple_add_le16(struct net_buf_simple *buf, uint16_t val);

void net_buf_simple_add_be16(struct net_buf_simple *buf, uint16_t val);

void net_buf_simple_add_le24(struct net_buf_simple *buf, uint32_t val);

void net_buf_simple_add_be24(struct net_buf_simple *buf, uint32_t val);

void net_buf_simple_add_le32(struct net_buf_simple *buf, uint32_t val);

void net_buf_simple_add_be32(struct net_buf_simple *buf, uint32_t val);

void net_buf_simple_add_le40(struct net_buf_simple *buf, uint64_t val);

void net_buf_simple_add_be40(struct net_buf_simple *buf, uint64_t val);

void net_buf_simple_add_le48(struct net_buf_simple *buf, uint64_t val);

void net_buf_simple_add_be48(struct net_buf_simple *buf, uint64_t val);

void net_buf_simple_add_le64(struct net_buf_simple *buf, uint64_t val);

void net_buf_simple_add_be64(struct net_buf_simple *buf, uint64_t val);

void *net_buf_simple_remove_mem(struct net_buf_simple *buf, size_t len);

uint8_t net_buf_simple_remove_u8(struct net_buf_simple *buf);

uint16_t net_buf_simple_remove_le16(struct net_buf_simple *buf);

uint16_t net_buf_simple_remove_be16(struct net_buf_simple *buf);

uint32_t net_buf_simple_remove_le24(struct net_buf_simple *buf);

uint32_t net_buf_simple_remove_be24(struct net_buf_simple *buf);

uint32_t net_buf_simple_remove_le32(struct net_buf_simple *buf);

uint32_t net_buf_simple_remove_be32(struct net_buf_simple *buf);

uint64_t net_buf_simple_remove_le40(struct net_buf_simple *buf);

uint64_t net_buf_simple_remove_be40(struct net_buf_simple *buf);

uint64_t net_buf_simple_remove_le48(struct net_buf_simple *buf);

uint64_t net_buf_simple_remove_be48(struct net_buf_simple *buf);

uint64_t net_buf_simple_remove_le64(struct net_buf_simple *buf);

uint64_t net_buf_simple_remove_be64(struct net_buf_simple *buf);

void *net_buf_simple_push(struct net_buf_simple *buf, size_t len);

void *net_buf_simple_push_mem(struct net_buf_simple *buf, const void *mem,
                              size_t len);

void net_buf_simple_push_le16(struct net_buf_simple *buf, uint16_t val);

void net_buf_simple_push_be16(struct net_buf_simple *buf, uint16_t val);

void net_buf_simple_push_u8(struct net_buf_simple *buf, uint8_t val);

void net_buf_simple_push_le24(struct net_buf_simple *buf, uint32_t val);

void net_buf_simple_push_be24(struct net_buf_simple *buf, uint32_t val);

void net_buf_simple_push_le32(struct net_buf_simple *buf, uint32_t val);

void net_buf_simple_push_be32(struct net_buf_simple *buf, uint32_t val);

void net_buf_simple_push_le40(struct net_buf_simple *buf, uint64_t val);

void net_buf_simple_push_be40(struct net_buf_simple *buf, uint64_t val);

void net_buf_simple_push_le48(struct net_buf_simple *buf, uint64_t val);

void net_buf_simple_push_be48(struct net_buf_simple *buf, uint64_t val);

void net_buf_simple_push_le64(struct net_buf_simple *buf, uint64_t val);

void net_buf_simple_push_be64(struct net_buf_simple *buf, uint64_t val);

void *net_buf_simple_pull(struct net_buf_simple *buf, size_t len);

void *net_buf_simple_pull_mem(struct net_buf_simple *buf, size_t len);

uint8_t net_buf_simple_pull_u8(struct net_buf_simple *buf);

uint16_t net_buf_simple_pull_le16(struct net_buf_simple *buf);

uint16_t net_buf_simple_pull_be16(struct net_buf_simple *buf);

uint32_t net_buf_simple_pull_le24(struct net_buf_simple *buf);

uint32_t net_buf_simple_pull_be24(struct net_buf_simple *buf);

uint32_t net_buf_simple_pull_le32(struct net_buf_simple *buf);

uint32_t net_buf_simple_pull_be32(struct net_buf_simple *buf);

uint64_t net_buf_simple_pull_le40(struct net_buf_simple *buf);

uint64_t net_buf_simple_pull_be40(struct net_buf_simple *buf);

uint64_t net_buf_simple_pull_le48(struct net_buf_simple *buf);

uint64_t net_buf_simple_pull_be48(struct net_buf_simple *buf);

uint64_t net_buf_simple_pull_le64(struct net_buf_simple *buf);

uint64_t net_buf_simple_pull_be64(struct net_buf_simple *buf);

static inline uint8_t *net_buf_simple_tail(const struct net_buf_simple *buf)
{
        return buf->data + buf->len;
}

static inline size_t net_buf_simple_headroom(const struct net_buf_simple *buf)
{
        return buf->data - buf->__buf;
}

static inline size_t net_buf_simple_tailroom(const struct net_buf_simple *buf)
{
        return buf->size - net_buf_simple_headroom(buf) - buf->len;
}

__deprecated static inline uint16_t net_buf_simple_max_len(const struct net_buf_simple *buf)
{
        return buf->size - net_buf_simple_headroom(buf);
}

static inline bool net_buf_simple_is_valid(const struct net_buf_simple *buf)
{
        size_t headroom;

        if (buf == NULL || buf->__buf == NULL || buf->data < buf->__buf) {
                return false;
        }

        headroom = net_buf_simple_headroom(buf);
        if (headroom > buf->size) {
                return false;
        }

        return (size_t)buf->len <= (size_t)(buf->size - headroom);
}

struct net_buf_simple_state {
        uint16_t offset;
        uint16_t len;
};

static inline void net_buf_simple_save(const struct net_buf_simple *buf,
                                       struct net_buf_simple_state *state)
{
        state->offset = (uint16_t)net_buf_simple_headroom(buf);
        state->len = buf->len;
}

static inline void net_buf_simple_restore(struct net_buf_simple *buf,
                                          struct net_buf_simple_state *state)
{
        buf->data = buf->__buf + state->offset;
        buf->len = state->len;
}

#define NET_BUF_EXTERNAL_DATA  BIT(0)

struct net_buf {
        sys_snode_t node;

        struct net_buf *frags;

        union {
                atomic_t ref_word;
                struct {
#if defined(CONFIG_BIG_ENDIAN)
                        /* atomic_t is typedef'd as long (BUILD_ASSERTed in
                         * lib/net_buf/buf.c); on a 64-bit big-endian build
                         * the byte struct needs 4 bytes of padding so that
                         * `ref` lands on the least-significant byte of
                         * ref_word.
                         */
#if (__SIZEOF_LONG__ == 8)
                        uint8_t _ref_word_pad[4];
#endif
                        uint8_t user_data_size;

                        uint8_t pool_id;

                        uint8_t flags;

                        uint8_t ref;
#else
                        uint8_t ref;

                        uint8_t flags;

                        uint8_t pool_id;

                        uint8_t user_data_size;
#endif
                };
        };

        union {
                /* The ABI of this struct must match net_buf_simple */
                struct {
                        uint8_t *data;

                        uint16_t len;

                        uint16_t size;

                        uint8_t *__buf;
                };

                struct net_buf_simple b;
        };

        uint8_t user_data[] __net_buf_align;
};


struct net_buf_data_cb {
        uint8_t * __must_check (*alloc)(struct net_buf *buf, size_t *size,
                           k_timeout_t timeout);
        uint8_t * __must_check (*ref)(struct net_buf *buf, uint8_t *data);
        void   (*unref)(struct net_buf *buf, uint8_t *data);
};

struct net_buf_data_alloc {
        const struct net_buf_data_cb *cb;
        void *alloc_data;
        size_t max_alloc_size;
        size_t alignment;
};


struct net_buf_pool {
        struct k_lifo free;

        struct k_spinlock lock;

        const uint16_t buf_count;

        uint16_t uninit_count;

        uint8_t user_data_size;

#if defined(CONFIG_NET_BUF_POOL_USAGE)
        atomic_t avail_count;

        const uint16_t pool_size;

        uint16_t max_used;

        const char *name;
#endif /* CONFIG_NET_BUF_POOL_USAGE */

        void (*const destroy)(struct net_buf *buf);

        const struct net_buf_data_alloc *alloc;

        struct net_buf * const __bufs;
};

#define NET_BUF_POOL_USAGE_INIT(_pool, _count) \
        IF_ENABLED(CONFIG_NET_BUF_POOL_USAGE, (.avail_count = ATOMIC_INIT(_count),)) \
        IF_ENABLED(CONFIG_NET_BUF_POOL_USAGE, (.max_used = 0,)) \
        IF_ENABLED(CONFIG_NET_BUF_POOL_USAGE, (.name = STRINGIFY(_pool),))

#define NET_BUF_POOL_INITIALIZER(_pool, _alloc, _bufs, _count, _ud_size, _destroy) \
        {                                                                          \
                .free = Z_LIFO_INITIALIZER(_pool.free),                            \
                .lock = { },                                                       \
                .buf_count = _count,                                               \
                .uninit_count = _count,                                            \
                .user_data_size = _ud_size,                                        \
                NET_BUF_POOL_USAGE_INIT(_pool, _count)                             \
                .destroy = _destroy,                                               \
                .alloc = _alloc,                                                   \
                .__bufs = (struct net_buf *)_bufs,                                 \
        }

#define _NET_BUF_ARRAY_DEFINE(_name, _count, _ud_size)                                         \
        struct _net_buf_##_name { uint8_t b[sizeof(struct net_buf)];                           \
                                  uint8_t ud[_ud_size]; } __net_buf_align;                     \
        BUILD_ASSERT(_ud_size <= UINT8_MAX);                                                   \
        BUILD_ASSERT(offsetof(struct net_buf, user_data) ==                                    \
                     offsetof(struct _net_buf_##_name, ud), "Invalid offset");                 \
        BUILD_ASSERT(__alignof__(struct net_buf) ==                                            \
                     __alignof__(struct _net_buf_##_name), "Invalid alignment");               \
        BUILD_ASSERT(sizeof(struct _net_buf_##_name) ==                                        \
                     ROUND_UP(sizeof(struct net_buf) + _ud_size, __alignof__(struct net_buf)), \
                     "Size cannot be determined");                                             \
        static struct _net_buf_##_name _net_buf_##_name[_count] __noinit

extern const struct net_buf_data_alloc net_buf_heap_alloc;

#define NET_BUF_POOL_HEAP_DEFINE(_name, _count, _ud_size, _destroy)          \
        _NET_BUF_ARRAY_DEFINE(_name, _count, _ud_size);                      \
        static STRUCT_SECTION_ITERABLE(net_buf_pool, _name) =                \
                NET_BUF_POOL_INITIALIZER(_name, &net_buf_heap_alloc,         \
                                         _net_buf_##_name, _count, _ud_size, \
                                         _destroy)


struct net_buf_pool_fixed {
        uint8_t *data_pool;
};

extern const struct net_buf_data_cb net_buf_fixed_cb;


#define NET_BUF_POOL_FIXED_DEFINE(_name, _count, _data_size, _ud_size, _destroy) \
        _NET_BUF_ARRAY_DEFINE(_name, _count, _ud_size);                        \
        static uint8_t __noinit net_buf_data_##_name[_count][_data_size] __net_buf_align; \
        static const struct net_buf_pool_fixed net_buf_fixed_##_name = {       \
                .data_pool = (uint8_t *)net_buf_data_##_name,                  \
        };                                                                     \
        static const struct net_buf_data_alloc net_buf_fixed_alloc_##_name = { \
                .cb = &net_buf_fixed_cb,                                       \
                .alloc_data = (void *)&net_buf_fixed_##_name,                  \
                .max_alloc_size = _data_size,                                  \
        };                                                                     \
        static STRUCT_SECTION_ITERABLE(net_buf_pool, _name) =                  \
                NET_BUF_POOL_INITIALIZER(_name, &net_buf_fixed_alloc_##_name,  \
                                         _net_buf_##_name, _count, _ud_size,   \
                                         _destroy)

extern const struct net_buf_data_cb net_buf_var_cb;

#define NET_BUF_POOL_VAR_DEFINE(_name, _count, _data_size, _ud_size, _destroy) \
        _NET_BUF_ARRAY_DEFINE(_name, _count, _ud_size);                        \
        K_HEAP_DEFINE(net_buf_mem_pool_##_name, _data_size);                   \
        static const struct net_buf_data_alloc net_buf_data_alloc_##_name = {  \
                .cb = &net_buf_var_cb,                                         \
                .alloc_data = &net_buf_mem_pool_##_name,                       \
                .max_alloc_size = 0,                                           \
        };                                                                     \
        static STRUCT_SECTION_ITERABLE(net_buf_pool, _name) =                  \
                NET_BUF_POOL_INITIALIZER(_name, &net_buf_data_alloc_##_name,   \
                                         _net_buf_##_name, _count, _ud_size,   \
                                         _destroy)

#define NET_BUF_POOL_VAR_ALIGN_DEFINE(_name, _count, _data_size, _ud_size,     \
                                      _destroy, _align)                        \
        _NET_BUF_ARRAY_DEFINE(_name, _count, _ud_size);                        \
        K_HEAP_DEFINE(net_buf_mem_pool_##_name, _data_size);                   \
        static const struct net_buf_data_alloc net_buf_data_alloc_##_name = {  \
                .cb = &net_buf_var_cb,                                         \
                .alloc_data = &net_buf_mem_pool_##_name,                       \
                .max_alloc_size = 0,                                           \
                .alignment = _align,                                           \
        };                                                                     \
        static STRUCT_SECTION_ITERABLE(net_buf_pool, _name) =                  \
                NET_BUF_POOL_INITIALIZER(_name, &net_buf_data_alloc_##_name,   \
                                         _net_buf_##_name, _count, _ud_size,   \
                                         _destroy)

#define NET_BUF_POOL_DEFINE(_name, _count, _size, _ud_size, _destroy)        \
        NET_BUF_POOL_FIXED_DEFINE(_name, _count, _size, _ud_size, _destroy)

struct net_buf_pool *net_buf_pool_get(int id);

int net_buf_id(const struct net_buf *buf);

#if defined(CONFIG_NET_BUF_POOL_USAGE) || defined(__DOXYGEN__)
static inline size_t net_buf_get_available(struct net_buf_pool *pool)
{
        return (size_t)atomic_get(&pool->avail_count);
}

static inline size_t net_buf_get_max_used(struct net_buf_pool *pool)
{
        return (size_t)pool->max_used;
}
#endif /* defined(CONFIG_NET_BUF_POOL_USAGE) || defined(__DOXYGEN__) */

#if defined(CONFIG_NET_BUF_LOG)
struct net_buf * __must_check net_buf_alloc_fixed_debug(struct net_buf_pool *pool,
                                                        k_timeout_t timeout,
                                                        const char *func,
                                                        int line);
#define net_buf_alloc_fixed(_pool, _timeout) \
        net_buf_alloc_fixed_debug(_pool, _timeout, __func__, __LINE__)
#else
struct net_buf * __must_check net_buf_alloc_fixed(struct net_buf_pool *pool,
                                                  k_timeout_t timeout);
#endif

static inline struct net_buf * __must_check net_buf_alloc(struct net_buf_pool *pool,
                                                          k_timeout_t timeout)
{
        return net_buf_alloc_fixed(pool, timeout);
}

#if defined(CONFIG_NET_BUF_LOG)
struct net_buf * __must_check net_buf_alloc_len_debug(struct net_buf_pool *pool,
                                                      size_t size,
                                                      k_timeout_t timeout,
                                                      const char *func,
                                                      int line);
#define net_buf_alloc_len(_pool, _size, _timeout) \
        net_buf_alloc_len_debug(_pool, _size, _timeout, __func__, __LINE__)
#else
struct net_buf * __must_check net_buf_alloc_len(struct net_buf_pool *pool,
                                                size_t size,
                                                k_timeout_t timeout);
#endif

#if defined(CONFIG_NET_BUF_LOG)
struct net_buf * __must_check net_buf_alloc_with_data_debug(struct net_buf_pool *pool,
                                                            void *data, size_t size,
                                                            k_timeout_t timeout,
                                                            const char *func, int line);
#define net_buf_alloc_with_data(_pool, _data_, _size, _timeout)         \
        net_buf_alloc_with_data_debug(_pool, _data_, _size, _timeout,   \
                                      __func__, __LINE__)
#else
struct net_buf * __must_check net_buf_alloc_with_data(struct net_buf_pool *pool,
                                                      void *data, size_t size,
                                                      k_timeout_t timeout);
#endif

static inline void net_buf_destroy(struct net_buf *buf)
{
        struct net_buf_pool *pool = net_buf_pool_get(buf->pool_id);

        if (buf->__buf) {
                if (!(buf->flags & NET_BUF_EXTERNAL_DATA)) {
                        pool->alloc->cb->unref(buf, buf->__buf);
                }
                buf->__buf = NULL;
        }

        k_lifo_put(&pool->free, buf);
}

void net_buf_reset(struct net_buf *buf);

void net_buf_simple_reserve(struct net_buf_simple *buf, size_t reserve);

void net_buf_slist_put(sys_slist_t *list, struct net_buf *buf);

struct net_buf * __must_check net_buf_slist_get(sys_slist_t *list);

#if defined(CONFIG_NET_BUF_LOG)
void net_buf_unref_debug(struct net_buf *buf, const char *func, int line);
#define net_buf_unref(_buf) \
        net_buf_unref_debug(_buf, __func__, __LINE__)
#else
void net_buf_unref(struct net_buf *buf);
#endif

struct net_buf * __must_check net_buf_ref(struct net_buf *buf);

static inline struct net_buf *__must_check net_buf_take(struct net_buf **orig)
{
        return (struct net_buf *)atomic_ptr_clear((atomic_ptr_t *)orig);
}

static inline void net_buf_drop(struct net_buf **orig)
{
        struct net_buf *buf = net_buf_take(orig);

        if (buf != NULL) {
                net_buf_unref(buf);
        }
}

struct net_buf * __must_check net_buf_clone(struct net_buf *buf,
                                            k_timeout_t timeout);

static inline void * __must_check net_buf_user_data(const struct net_buf *buf)
{
        return (void *)buf->user_data;
}

int net_buf_user_data_copy(struct net_buf *dst, const struct net_buf *src);

static inline void net_buf_reserve(struct net_buf *buf, size_t reserve)
{
        net_buf_simple_reserve(&buf->b, reserve);
}

static inline void *net_buf_add(struct net_buf *buf, size_t len)
{
        return net_buf_simple_add(&buf->b, len);
}

static inline void *net_buf_add_mem(struct net_buf *buf, const void *mem,
                                    size_t len)
{
        return net_buf_simple_add_mem(&buf->b, mem, len);
}

static inline uint8_t *net_buf_add_u8(struct net_buf *buf, uint8_t val)
{
        return net_buf_simple_add_u8(&buf->b, val);
}

static inline void net_buf_add_le16(struct net_buf *buf, uint16_t val)
{
        net_buf_simple_add_le16(&buf->b, val);
}

static inline void net_buf_add_be16(struct net_buf *buf, uint16_t val)
{
        net_buf_simple_add_be16(&buf->b, val);
}

static inline void net_buf_add_le24(struct net_buf *buf, uint32_t val)
{
        net_buf_simple_add_le24(&buf->b, val);
}

static inline void net_buf_add_be24(struct net_buf *buf, uint32_t val)
{
        net_buf_simple_add_be24(&buf->b, val);
}

static inline void net_buf_add_le32(struct net_buf *buf, uint32_t val)
{
        net_buf_simple_add_le32(&buf->b, val);
}

static inline void net_buf_add_be32(struct net_buf *buf, uint32_t val)
{
        net_buf_simple_add_be32(&buf->b, val);
}

static inline void net_buf_add_le40(struct net_buf *buf, uint64_t val)
{
        net_buf_simple_add_le40(&buf->b, val);
}

static inline void net_buf_add_be40(struct net_buf *buf, uint64_t val)
{
        net_buf_simple_add_be40(&buf->b, val);
}

static inline void net_buf_add_le48(struct net_buf *buf, uint64_t val)
{
        net_buf_simple_add_le48(&buf->b, val);
}

static inline void net_buf_add_be48(struct net_buf *buf, uint64_t val)
{
        net_buf_simple_add_be48(&buf->b, val);
}

static inline void net_buf_add_le64(struct net_buf *buf, uint64_t val)
{
        net_buf_simple_add_le64(&buf->b, val);
}

static inline void net_buf_add_be64(struct net_buf *buf, uint64_t val)
{
        net_buf_simple_add_be64(&buf->b, val);
}

static inline void *net_buf_remove_mem(struct net_buf *buf, size_t len)
{
        return net_buf_simple_remove_mem(&buf->b, len);
}

static inline uint8_t net_buf_remove_u8(struct net_buf *buf)
{
        return net_buf_simple_remove_u8(&buf->b);
}

static inline uint16_t net_buf_remove_le16(struct net_buf *buf)
{
        return net_buf_simple_remove_le16(&buf->b);
}

static inline uint16_t net_buf_remove_be16(struct net_buf *buf)
{
        return net_buf_simple_remove_be16(&buf->b);
}

static inline uint32_t net_buf_remove_be24(struct net_buf *buf)
{
        return net_buf_simple_remove_be24(&buf->b);
}

static inline uint32_t net_buf_remove_le24(struct net_buf *buf)
{
        return net_buf_simple_remove_le24(&buf->b);
}

static inline uint32_t net_buf_remove_le32(struct net_buf *buf)
{
        return net_buf_simple_remove_le32(&buf->b);
}

static inline uint32_t net_buf_remove_be32(struct net_buf *buf)
{
        return net_buf_simple_remove_be32(&buf->b);
}

static inline uint64_t net_buf_remove_le40(struct net_buf *buf)
{
        return net_buf_simple_remove_le40(&buf->b);
}

static inline uint64_t net_buf_remove_be40(struct net_buf *buf)
{
        return net_buf_simple_remove_be40(&buf->b);
}

static inline uint64_t net_buf_remove_le48(struct net_buf *buf)
{
        return net_buf_simple_remove_le48(&buf->b);
}

static inline uint64_t net_buf_remove_be48(struct net_buf *buf)
{
        return net_buf_simple_remove_be48(&buf->b);
}

static inline uint64_t net_buf_remove_le64(struct net_buf *buf)
{
        return net_buf_simple_remove_le64(&buf->b);
}

static inline uint64_t net_buf_remove_be64(struct net_buf *buf)
{
        return net_buf_simple_remove_be64(&buf->b);
}

static inline void *net_buf_push(struct net_buf *buf, size_t len)
{
        return net_buf_simple_push(&buf->b, len);
}

static inline void *net_buf_push_mem(struct net_buf *buf, const void *mem,
                                     size_t len)
{
        return net_buf_simple_push_mem(&buf->b, mem, len);
}

static inline void net_buf_push_u8(struct net_buf *buf, uint8_t val)
{
        net_buf_simple_push_u8(&buf->b, val);
}

static inline void net_buf_push_le16(struct net_buf *buf, uint16_t val)
{
        net_buf_simple_push_le16(&buf->b, val);
}

static inline void net_buf_push_be16(struct net_buf *buf, uint16_t val)
{
        net_buf_simple_push_be16(&buf->b, val);
}

static inline void net_buf_push_le24(struct net_buf *buf, uint32_t val)
{
        net_buf_simple_push_le24(&buf->b, val);
}

static inline void net_buf_push_be24(struct net_buf *buf, uint32_t val)
{
        net_buf_simple_push_be24(&buf->b, val);
}

static inline void net_buf_push_le32(struct net_buf *buf, uint32_t val)
{
        net_buf_simple_push_le32(&buf->b, val);
}

static inline void net_buf_push_be32(struct net_buf *buf, uint32_t val)
{
        net_buf_simple_push_be32(&buf->b, val);
}

static inline void net_buf_push_le40(struct net_buf *buf, uint64_t val)
{
        net_buf_simple_push_le40(&buf->b, val);
}

static inline void net_buf_push_be40(struct net_buf *buf, uint64_t val)
{
        net_buf_simple_push_be40(&buf->b, val);
}

static inline void net_buf_push_le48(struct net_buf *buf, uint64_t val)
{
        net_buf_simple_push_le48(&buf->b, val);
}

static inline void net_buf_push_be48(struct net_buf *buf, uint64_t val)
{
        net_buf_simple_push_be48(&buf->b, val);
}

static inline void net_buf_push_le64(struct net_buf *buf, uint64_t val)
{
        net_buf_simple_push_le64(&buf->b, val);
}

static inline void net_buf_push_be64(struct net_buf *buf, uint64_t val)
{
        net_buf_simple_push_be64(&buf->b, val);
}

static inline void *net_buf_pull(struct net_buf *buf, size_t len)
{
        return net_buf_simple_pull(&buf->b, len);
}

static inline void *net_buf_pull_mem(struct net_buf *buf, size_t len)
{
        return net_buf_simple_pull_mem(&buf->b, len);
}

static inline uint8_t net_buf_pull_u8(struct net_buf *buf)
{
        return net_buf_simple_pull_u8(&buf->b);
}

static inline uint16_t net_buf_pull_le16(struct net_buf *buf)
{
        return net_buf_simple_pull_le16(&buf->b);
}

static inline uint16_t net_buf_pull_be16(struct net_buf *buf)
{
        return net_buf_simple_pull_be16(&buf->b);
}

static inline uint32_t net_buf_pull_le24(struct net_buf *buf)
{
        return net_buf_simple_pull_le24(&buf->b);
}

static inline uint32_t net_buf_pull_be24(struct net_buf *buf)
{
        return net_buf_simple_pull_be24(&buf->b);
}

static inline uint32_t net_buf_pull_le32(struct net_buf *buf)
{
        return net_buf_simple_pull_le32(&buf->b);
}

static inline uint32_t net_buf_pull_be32(struct net_buf *buf)
{
        return net_buf_simple_pull_be32(&buf->b);
}

static inline uint64_t net_buf_pull_le40(struct net_buf *buf)
{
        return net_buf_simple_pull_le40(&buf->b);
}

static inline uint64_t net_buf_pull_be40(struct net_buf *buf)
{
        return net_buf_simple_pull_be40(&buf->b);
}

static inline uint64_t net_buf_pull_le48(struct net_buf *buf)
{
        return net_buf_simple_pull_le48(&buf->b);
}

static inline uint64_t net_buf_pull_be48(struct net_buf *buf)
{
        return net_buf_simple_pull_be48(&buf->b);
}

static inline uint64_t net_buf_pull_le64(struct net_buf *buf)
{
        return net_buf_simple_pull_le64(&buf->b);
}

static inline uint64_t net_buf_pull_be64(struct net_buf *buf)
{
        return net_buf_simple_pull_be64(&buf->b);
}

static inline size_t net_buf_tailroom(const struct net_buf *buf)
{
        return net_buf_simple_tailroom(&buf->b);
}

static inline size_t net_buf_headroom(const struct net_buf *buf)
{
        return net_buf_simple_headroom(&buf->b);
}

__deprecated static inline uint16_t net_buf_max_len(const struct net_buf *buf)
{
        return buf->size - net_buf_headroom(buf);
}

static inline bool net_buf_is_valid(const struct net_buf *buf)
{
        return buf != NULL && buf->ref > 0 && net_buf_simple_is_valid(&buf->b);
}

static inline uint8_t *net_buf_tail(const struct net_buf *buf)
{
        return net_buf_simple_tail(&buf->b);
}

struct net_buf *net_buf_frag_last(struct net_buf *frags);

void net_buf_frag_insert(struct net_buf *parent, struct net_buf *frag);

struct net_buf *net_buf_frag_add(struct net_buf *head, struct net_buf *frag);

#if defined(CONFIG_NET_BUF_LOG)
struct net_buf *net_buf_frag_del_debug(struct net_buf *parent,
                                       struct net_buf *frag,
                                       const char *func, int line);
#define net_buf_frag_del(_parent, _frag) \
        net_buf_frag_del_debug(_parent, _frag, __func__, __LINE__)
#else
struct net_buf *net_buf_frag_del(struct net_buf *parent, struct net_buf *frag);
#endif

size_t net_buf_linearize(void *dst, size_t dst_len,
                         const struct net_buf *src, size_t offset, size_t len);

typedef struct net_buf * __must_check (*net_buf_allocator_cb)(k_timeout_t timeout,
                                                              void *user_data);

size_t net_buf_append_bytes(struct net_buf *buf, size_t len,
                            const void *value, k_timeout_t timeout,
                            net_buf_allocator_cb allocate_cb, void *user_data);

size_t net_buf_data_match(const struct net_buf *buf, size_t offset, const void *data, size_t len);

static inline struct net_buf *net_buf_skip(struct net_buf *buf, size_t len)
{
        while (buf != NULL && len > 0U) {
                size_t to_skip = MIN(len, buf->len);

                /* A zero-capacity fragment has no data buffer to pull from */
                if (to_skip > 0U) {
                        net_buf_pull(buf, to_skip);
                        len -= to_skip;
                }

                if (buf->len == 0U) {
                        buf = net_buf_frag_del(NULL, buf);
                }
        }

        return buf;
}

static inline size_t net_buf_frags_len(const struct net_buf *buf)
{
        size_t bytes = 0;

        while (buf) {
                bytes += buf->len;
                buf = buf->frags;
        }

        return bytes;
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_BUF_H_ */
```

## 21.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2015 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 40 行

缓冲区定义（Buffer Definition）各部分所需的对齐（Alignment）。

### 注释 3：原第 1106 行

`atomic_t` 被定义为 `long` 类型别名，`lib/net_buf/buf.c` 中通过 `BUILD_ASSERT` 验证这一点。在 64 位大端构建（Big-Endian Build）中，字节结构体需要 4 字节填充（Padding），使 `ref` 位于 `ref_word` 的最低有效字节（Least-Significant Byte）。

### 注释 4：原第 1148 行

本结构体的应用二进制接口（ABI）必须与 `net_buf_simple` 一致。

### 注释 5：原第 1226 行

条件编译配置（Configuration）标记：`CONFIG_NET_BUF_POOL_USAGE`。

### 注释 6：原第 1526 行

条件编译（Conditional Compilation）：`defined(CONFIG_NET_BUF_POOL_USAGE) || defined(__DOXYGEN__)`。

### 注释 7：原第 2929 行

容量为零的分片（Zero-Capacity Fragment）没有可供提取数据的数据缓冲区（Data Buffer）。

### 注释 8：原第 2973 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_BUF_H_`。

## 21.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../network_core_model_reference/P048_net_buf_simple_结构体.md#ad232efff435f425d30ac78f5abf2d8b1)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [len](../network_core_model_reference/P048_net_buf_simple_结构体.md#ae8707c50d70c26b53281b40eb1720cf3)
- [size](../network_core_model_reference/P048_net_buf_simple_结构体.md#ae6dc4aa029a67d3911293618eb30caa6)
- [net_buf_simple_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga040279b601191367dee013bab9916d8d)
- [net_buf_simple_init_with_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7fac47a2a25eaca39c5d14f1f55b485d)
- [net_buf_simple_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4b537e913e132448cbf56976504ddddd)
- [net_buf_simple_clone](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0186c153b72a379affdd3e2e3994b5a7)
- [net_buf_simple_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga1906e637c848948f5780428a99b3341e)
- [net_buf_simple_add_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac37209c1e5097e5610860943fb7d0115)
- [net_buf_simple_add_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8ff9344b8d8deba1b72b8fca048a525c)
- [net_buf_simple_add_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaa2daf3b20074ff1a23806ce88becebf5)
- [net_buf_simple_add_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga910f2b9df58fb0706aa40e3b80f235aa)
- [net_buf_simple_add_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf1a89eb15eed79003412ba5a32a35cf6)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [net_buf_simple_add_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5eb09afeff062af577094d2d3f5fdec8)
- [net_buf_simple_add_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga3bf1bcff840dddd721f2c49ef0ed7c56)
- [net_buf_simple_add_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaac5cd20776d8e7bb4db77cbe5366373c)
- [net_buf_simple_add_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga67da71ba5942cc11e95aa5ba02cb8552)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [net_buf_simple_add_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga69bdaf4373693bb468cf3876e9edf239)
- [net_buf_simple_add_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5be8c9f33df5b31c15df193a7116ce25)
- [net_buf_simple_add_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gadb433fb4a1a61702c0615359a4340171)
- [net_buf_simple_add_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga79dc411da328b847dcf1903d71eaf011)
- [net_buf_simple_add_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8e31a7b6537d7634e346236534d2a6d0)
- [net_buf_simple_remove_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8473bdffadc05b22335a321df89f4b83)
- [net_buf_simple_remove_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf508f74e5e050a7294e8a70bd3725fc3)
- [net_buf_simple_remove_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0b57f9ca2f3837e94cd7862e37efc01c)
- [net_buf_simple_remove_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga93f9f84845601df4ffc118be1ffd2fee)
- [net_buf_simple_remove_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4e2fef883228f7de41af3cf90648c3c5)
- [net_buf_simple_remove_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9b39384162a91d7d07e037a9ada782dd)
- [net_buf_simple_remove_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9e8d016ce384378142fdec6c8dde2457)
- [net_buf_simple_remove_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)
- [net_buf_simple_remove_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga2c937164e648fe8b854cb1144051b6b9)
- [net_buf_simple_remove_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9abd2bccc90cf654556c18322888d131)
- [net_buf_simple_remove_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac0628bbbe5d9c2b82766d5a17e767696)
- [net_buf_simple_remove_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gab93d22797c3f406179c4c145241d6abb)
- [net_buf_simple_remove_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga560bd7b181c7f08599ae9241b6ce99fd)
- [net_buf_simple_remove_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga602fae83e2ecf47552a11f9282619932)
- [net_buf_simple_push](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga64df9754665440370340c6dddde625d1)
- [net_buf_simple_push_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaaa838083c610f7426c509efaae69a511)
- [net_buf_simple_push_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga50cd64438d8f218e3d1ef8b53b7d41a6)
- [net_buf_simple_push_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga827bd85eba0dbd098790d84d22e8e32d)
- [net_buf_simple_push_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0f19da70bfc8f597680ee02c21226a77)
- [net_buf_simple_push_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabe52d6735d835edc361666bb3413b907)
- [net_buf_simple_push_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabfddd4956ec1e356002a3122fea74b72)
- [net_buf_simple_push_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8662e6bada476c0d48cebea4661b2ac1)
- [net_buf_simple_push_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad0c3b8fdeaad6437c3dfcbb03fa52426)
- [net_buf_simple_push_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga745ab6f34138b506b42f78e0975a5d2e)
- [net_buf_simple_push_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad65bcaf8401e6f5ffff81a998cfb8fe5)
- [net_buf_simple_push_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga66b44897e336f31e3ecbf4717bec274e)
- [net_buf_simple_push_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga1ea39c7d7e9ba4e10d31d818e45e192a)
- [net_buf_simple_push_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga771634e50e2bf7c291565ce6b2af7e85)
- [net_buf_simple_push_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gafea2201655955ab004b5f77106998ae9)
- [net_buf_simple_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf5ab4a5fe4a6226be72a510fea0ed8a8)
- [net_buf_simple_pull_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9c676fdbd6e999a9eab26b13d3608e0c)
- [net_buf_simple_pull_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga09a261c615136fd39834cd301fc692e7)
- [net_buf_simple_pull_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad59d180ae81b55f6d618565a37d25dba)
- [net_buf_simple_pull_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae36458ba05a4ab89e429be4cfd264440)
- [net_buf_simple_pull_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4c9d2ac72a176c49ec224353b5566eb9)
- [net_buf_simple_pull_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4c24d445d6b75c850a9e95fb242a50e1)
- [net_buf_simple_pull_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga38df82e6ba9bc2c75133200f7fa75353)
- [net_buf_simple_pull_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga1a53892ed75f994bbbb3a2bcf1743d3c)
- [net_buf_simple_pull_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad669c07efe5cb90ebffcc76d9c1029a1)
- [net_buf_simple_pull_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaa665830dad59ac957f79c7f1cc84aed5)
- [net_buf_simple_pull_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga69fbfbd72b17783c5ee12b4b2ac9af46)
- [net_buf_simple_pull_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga19bdefe740fe94a42fba76d71b4ef6e2)
- [net_buf_simple_pull_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7e0e2d0adbe9062d08f5d8afc7acd89e)
- [net_buf_simple_pull_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad07f0d49a7db99063077de493e7b0712)
- [net_buf_simple_tail](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8)
- [net_buf_simple_headroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gadc6ae86245c2a2607c671a524227b026)
- [net_buf_simple_tailroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga73e2c42fc23e857a46553084b747c996)
- [net_buf_simple_max_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7476ec7222d074e7dc9783e7ed9cd800)
- [net_buf_simple_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5c4038cb3aa506c3cad7a2505392aa50)
- [net_buf_simple_state](../network_core_model_reference/P049_net_buf_simple_state_结构体.md)
- [offset](../network_core_model_reference/P049_net_buf_simple_state_结构体.md#a4061f8e50e14289b1ec999ef490c8fbf)
- [len](../network_core_model_reference/P049_net_buf_simple_state_结构体.md#af0e544fe2b018a7ff0b30970e9de8253)
- [net_buf_simple_save](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabf5b098aa0926d9b7fb88baff8a3e2d8)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [net_buf_simple_restore](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaedd36481657a7a9d108659d56e131721)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../network_core_model_reference/P046_net_buf_结构体.md#a5cc70f57e5b776cfa12b2d556e5958f3)
- [frags](../network_core_model_reference/P046_net_buf_结构体.md#a1fa032cc23854c35eae013020823fa88)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [user_data_size](../network_core_model_reference/P046_net_buf_结构体.md#a65db7bed62d7211114767e6ce58dad75)
- [pool_id](../network_core_model_reference/P046_net_buf_结构体.md#a45f294bac054d64034bddcc4c6574d29)
- [flags](../network_core_model_reference/P046_net_buf_结构体.md#aa4fcce2e2894fc5dbd9cc74fc020647e)
- [ref](../network_core_model_reference/P046_net_buf_结构体.md#a42da518a82f4c37c45814b4f8c5f2731)
- [data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [size](../network_core_model_reference/P046_net_buf_结构体.md#a1522d81a002804223e25300a6961f527)
- [user_data](../network_core_model_reference/P046_net_buf_结构体.md#ade8055f804d5a1fea13e55d71d92a5e7)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [k_lifo](../queue_reference/P006_内核LIFO结构.md)
- [free](../network_core_model_reference/P047_net_buf_pool_结构体.md#a97e5b2e51238e859f93882a8008ba305)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)
- [lock](../network_core_model_reference/P047_net_buf_pool_结构体.md#ae92fc3f3f51be63ccdeee9614d21cc34)
- [buf_count](../network_core_model_reference/P047_net_buf_pool_结构体.md#a55b57f4f573c7e752c3ccf2f92f25626)
- [uninit_count](../network_core_model_reference/P047_net_buf_pool_结构体.md#a3fdf83b4c0b5acefbb761da285791ad2)
- [user_data_size](../network_core_model_reference/P047_net_buf_pool_结构体.md#a4718ecec19d7e2ccaf04b6ff61120975)
- [destroy](../network_core_model_reference/P047_net_buf_pool_结构体.md#a2a9141d7cd20cd98818a92dc5bc99f56)
- [alloc](../network_core_model_reference/P047_net_buf_pool_结构体.md#a617bd8f77e55481d97183da8c0c62cc5)
- [net_buf_pool_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga145f4b2de7548814eaa7ba86fb123989)
- [net_buf_id](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gacdf048dc0afc7ef67027117e0d51d3a3)
- [net_buf_get_available](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9cd6d30ea47a91647d3c4a60d82b5cd4)
- [atomic_get](../atomic_reference/P001_原子操作公共接口.md#ga33bb426a17535bd1022895a7e44b32fa)
- [net_buf_get_max_used](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad652ef7d2895f8077c366a564b785291)
- [net_buf_alloc_fixed](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga686df794ec6881625b54454a33587bab)
- [net_buf_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga534366f3b5c7f41a28372c12149ca005)
- [net_buf_alloc_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga11d489aedcca82117965fa6ba9d11ca5)
- [net_buf_alloc_with_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8c24d0761d6d38facb6cca60c7c13c0c)
- [net_buf_destroy](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga739249547eb37b839b3c1ebdbcb88d28)
- [NET_BUF_EXTERNAL_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaaeacbdf3cfda12691c75253015e5c19a)
- [k_lifo_put](../queue_reference/P005_LIFO公共接口.md#gad662e36b1df8b9013e2dc61f9dfe3a8b)
- [net_buf_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga1292f38b096fd80e31889aff44b0c021)
- [net_buf_simple_reserve](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0e5d3d938becfefc4f4b4d083cb467aa)
- [net_buf_slist_put](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga6d2dfc45e1e5acf21fe08359a4f92a18)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [net_buf_slist_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga218d4a0c160c57a44946154478724cb3)
- [net_buf_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabedcb728bc2fc0c2b5319a8fd87e8273)
- [net_buf_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga29387b2a672bf2bb8739046a46f3601f)
- [net_buf_take](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4ff24d6ae1aff46e17647ef91db593ca)
- [atomic_ptr_clear](../atomic_reference/P001_原子操作公共接口.md#ga587e3134cd8176e7b1c00361711ee2df)
- [atomic_ptr_t](../atomic_reference/P001_原子操作公共接口.md#gacad6866fa4c844026cd9f8c3fb60ecd7)
- [net_buf_drop](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga6b43ad0740b23c0544d706c77c9f1e13)
- [net_buf_clone](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf4d80e2878e3c790fff206bec820f03f)
- [net_buf_user_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf2df457abe3e56d47107b76bdc004756)
- [net_buf_user_data_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4d1dd56ca8d32d3cfda114fd36761d0d)
- [net_buf_reserve](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8ac58ad4f73b498bef2ff3ac7e30c6c3)
- [net_buf_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga30776d2b21f06d244c083af5c25b0f3e)
- [net_buf_add_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gacf4e2eba52975ba6728c79274a769d0f)
- [net_buf_add_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga868ac2bea103fed568b461cbcd45eda2)
- [net_buf_add_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gadd6d01a3b1efd0de16f9bef975809404)
- [net_buf_add_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga61878a9bd7462ca925eac39181f2972c)
- [net_buf_add_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga32b90364091ade229830686f03b25d4c)
- [net_buf_add_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0f3cd9f9b364a2d2125aea19221d3e1e)
- [net_buf_add_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae8ba33b6592ef7fd859b35d63b285d87)
- [net_buf_add_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5543d00c96f83970f8dbf3670a9dc3fc)
- [net_buf_add_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga62790f9644102f4952c250f6513a2ada)
- [net_buf_add_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga70cb98da91de098a92fbd69712c2bde7)
- [net_buf_add_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf19bf75c3d4d645b1eebf9254aa22790)
- [net_buf_add_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8fe6feb191ab338e91bd62f44e184deb)
- [net_buf_add_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac3f955f8fecc0e5971d2e5e8176e973e)
- [net_buf_add_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga055f6eb7d5fbc9a3cf529a9ed00970c4)
- [net_buf_remove_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gace5ad98eac4772db3b0fa2181912f1f0)
- [net_buf_remove_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad954b9f37790d5e7087db7db7bdedd41)
- [net_buf_remove_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaaf654110fb6a8bdfc27433945d4d1308)
- [net_buf_remove_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5da86c8ea703ab3f01c408cce73b0651)
- [net_buf_remove_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga6f346a9af570528d238592851240fd74)
- [net_buf_remove_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga903f59c8dea1b2c54969b567fe315041)
- [net_buf_remove_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae9321a469cc751c58cfb532afd57d265)
- [net_buf_remove_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gacce707d646d7008ec3167af1a0b20da8)
- [net_buf_remove_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga57150a1ba09b28e5c3b04bdefce7ed8e)
- [net_buf_remove_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae2920eab3c56d0d462811b83961df466)
- [net_buf_remove_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0c147d9f95e2224696a8ace26f63a300)
- [net_buf_remove_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaab0e3bcc21c958c01ef076cd0efe087c)
- [net_buf_remove_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga447b9c6be3fe04a50eb35dd29f190b6d)
- [net_buf_remove_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8b9edd213da2d48dfb8d70a8d307ba13)
- [net_buf_push](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga96a2b1f07f3a7958057d9c7cc1f01b73)
- [net_buf_push_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7e9daccec8cae1b9bfda52b0758adf0c)
- [net_buf_push_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9093202ba0a22bfa519bbe32d4585186)
- [net_buf_push_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gab6c84c6846c06c2b339bc88df35e2655)
- [net_buf_push_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga6dd756ff8332d076f5d37c69e6c534b5)
- [net_buf_push_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga87524ac50e53ba59c6692af10cf001b9)
- [net_buf_push_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga87338399d8ecd64a894908ed4a2f710b)
- [net_buf_push_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga97c9046185d6a1e9235bf6914c72dfc4)
- [net_buf_push_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae4e64a23708ed910fb6c3ab8ba481a4c)
- [net_buf_push_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaefab4a755cf4fb7d2b4a142a9351c189)
- [net_buf_push_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga512f84e686ff70a5589557575ccda1f8)
- [net_buf_push_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga852654f7e59951bf3536e3f4e98761bf)
- [net_buf_push_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabfbcb051019ff210cc2b85adcf4bc821)
- [net_buf_push_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad4ee42b023881f80211fbeca53a0f25d)
- [net_buf_push_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga43ff5faab0b099a355b9b96b7b0e3d8c)
- [net_buf_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaef433d92734dd8691c292abdb823ba0e)
- [net_buf_pull_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaedc5ffe19bb0ec438e633023c3c5de74)
- [net_buf_pull_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga71bb306d2ce459a60a8c3fc6dac54c90)
- [net_buf_pull_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaed64e9f2b969f2c0d99cd281e73c860a)
- [net_buf_pull_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga97909a33c374a5c757fd2faf582139b7)
- [net_buf_pull_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga85c505321484a50ed9422f24934ed077)
- [net_buf_pull_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8de937e8775879712ea0acbf60327a95)
- [net_buf_pull_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5f051078f1ffcc40e9ad40e7545a084f)
- [net_buf_pull_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5f8f2e2244eb574b3e57d09d85412967)
- [net_buf_pull_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga36b27c6373eb245f777164065386d100)
- [net_buf_pull_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga050bdaccaec842482a02b096aa0c999f)
- [net_buf_pull_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7eeee45b6639146d1492f92263ee4f51)
- [net_buf_pull_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga68934e105c4b3a8e27aa61b3ec5526db)
- [net_buf_pull_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9a3df35e2287cbcfe1b60e2efa52c64e)
- [net_buf_pull_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga3c1e80741a49691e69e57c891d3edb05)
- [net_buf_tailroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaecbc6adf16469e3366c88445ea7a553a)
- [net_buf_headroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac9a09897f44e708f920064826aa2f703)
- [net_buf_max_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga65924b8234c91dfc09069ba06242a6b7)
- [net_buf_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8d258ef1e4241c438a726486bc7fe766)
- [net_buf_tail](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaedb10a84b352a3d7716bef979af2ab31)
- [net_buf_frag_last](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga042ce3f2e7e3fd0948ca2623fff36746)
- [net_buf_frag_insert](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac032b44db4a845dba8303fecfe1b63e7)
- [net_buf_frag_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0d7e310802a2bc7b2078f9310827535f)
- [net_buf_frag_del](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga602a99833bd401a0ada5bd5defa7a2ff)
- [net_buf_linearize](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaffd49f2de8e72d5f7585b4e5167923d8)
- [net_buf_allocator_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9b74d094a45daf74cd230eaa4fcbc065)
- [net_buf_append_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga646d680491753b3ed29fa83c26732d1a)
- [net_buf_data_match](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaef938c3ab676a5bd5bf8338b8d7cb30c)
- [net_buf_skip](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga2d7096280d4fa6f5e32c4674d542889b)
- [MIN](../util_reference/P001_通用工具公共接口.md#ga3acffbd305ee72dcd4593c0d8af64a4f)
- [net_buf_frags_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaebb95f08dbd4d38a250170aa78ddeb44)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_buf_pool::destroy](../network_core_model_reference/P047_net_buf_pool_结构体.md#a2a9141d7cd20cd98818a92dc5bc99f56)
- [net_buf_pool::uninit_count](../network_core_model_reference/P047_net_buf_pool_结构体.md#a3fdf83b4c0b5acefbb761da285791ad2)
- [net_buf_pool::user_data_size](../network_core_model_reference/P047_net_buf_pool_结构体.md#a4718ecec19d7e2ccaf04b6ff61120975)
- [net_buf_pool::buf_count](../network_core_model_reference/P047_net_buf_pool_结构体.md#a55b57f4f573c7e752c3ccf2f92f25626)
- [net_buf_pool::alloc](../network_core_model_reference/P047_net_buf_pool_结构体.md#a617bd8f77e55481d97183da8c0c62cc5)
- [net_buf_pool::free](../network_core_model_reference/P047_net_buf_pool_结构体.md#a97e5b2e51238e859f93882a8008ba305)
- [net_buf_pool::lock](../network_core_model_reference/P047_net_buf_pool_结构体.md#ae92fc3f3f51be63ccdeee9614d21cc34)
- [net_buf_simple_state::offset](../network_core_model_reference/P049_net_buf_simple_state_结构体.md#a4061f8e50e14289b1ec999ef490c8fbf)
- [net_buf_simple_state::len](../network_core_model_reference/P049_net_buf_simple_state_结构体.md#af0e544fe2b018a7ff0b30970e9de8253)
- [net_buf_simple::data](../network_core_model_reference/P048_net_buf_simple_结构体.md#ad232efff435f425d30ac78f5abf2d8b1)
- [net_buf_simple::size](../network_core_model_reference/P048_net_buf_simple_结构体.md#ae6dc4aa029a67d3911293618eb30caa6)
- [net_buf_simple::len](../network_core_model_reference/P048_net_buf_simple_结构体.md#ae8707c50d70c26b53281b40eb1720cf3)
- [net_buf::size](../network_core_model_reference/P046_net_buf_结构体.md#a1522d81a002804223e25300a6961f527)
- [net_buf::frags](../network_core_model_reference/P046_net_buf_结构体.md#a1fa032cc23854c35eae013020823fa88)
- [net_buf::ref](../network_core_model_reference/P046_net_buf_结构体.md#a42da518a82f4c37c45814b4f8c5f2731)
- [net_buf::pool_id](../network_core_model_reference/P046_net_buf_结构体.md#a45f294bac054d64034bddcc4c6574d29)
- [net_buf::node](../network_core_model_reference/P046_net_buf_结构体.md#a5cc70f57e5b776cfa12b2d556e5958f3)
- [net_buf::user_data_size](../network_core_model_reference/P046_net_buf_结构体.md#a65db7bed62d7211114767e6ce58dad75)
- [net_buf::flags](../network_core_model_reference/P046_net_buf_结构体.md#aa4fcce2e2894fc5dbd9cc74fc020647e)
- [net_buf::data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [net_buf::user_data](../network_core_model_reference/P046_net_buf_结构体.md#ade8055f804d5a1fea13e55d71d92a5e7)
- [net_buf::len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P020_mqtt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P022_net_context.h_源码浏览.md)
