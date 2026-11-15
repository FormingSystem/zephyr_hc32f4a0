---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-3
title: bap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_bap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)。

## 3.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
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
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="foldopen00123"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00133"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00143"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="foldopen00153"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="foldopen00165"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="foldopen00180"></a>
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
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="foldopen00220"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="foldopen00233"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="foldopen00238"></a>
<a id="l00238"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="foldopen00336"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="foldopen00354"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="foldopen00369"></a>
<a id="l00369"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="foldopen00391"></a>
<a id="l00391"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="foldopen00439"></a>
<a id="l00439"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="foldopen00453"></a>
<a id="l00453"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="foldopen00495"></a>
<a id="l00495"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00591"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="foldopen00641"></a>
<a id="l00641"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="foldopen00704"></a>
<a id="l00704"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00748"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="foldopen00753"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00813"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00852"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="foldopen00898"></a>
<a id="l00898"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00921"></a>
<a id="l00922"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="l00938"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="l00983"></a>
<a id="l00984"></a>
<a id="l00996"></a>
<a id="l00997"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01035"></a>
<a id="l01036"></a>
<a id="l01059"></a>
<a id="l01060"></a>
<a id="l01084"></a>
<a id="l01085"></a>
<a id="l01103"></a>
<a id="l01104"></a>
<a id="l01119"></a>
<a id="l01120"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01158"></a>
<a id="l01159"></a>
<a id="l01165"></a>
<a id="foldopen01167"></a>
<a id="l01167"></a>
<a id="l01186"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01206"></a>
<a id="l01207"></a>
<a id="l01208"></a>
<a id="l01209"></a>
<a id="l01223"></a>
<a id="l01224"></a>
<a id="l01225"></a>
<a id="l01239"></a>
<a id="l01240"></a>
<a id="l01241"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="l01268"></a>
<a id="l01269"></a>
<a id="l01270"></a>
<a id="l01282"></a>
<a id="l01283"></a>
<a id="l01295"></a>
<a id="l01296"></a>
<a id="l01309"></a>
<a id="l01310"></a>
<a id="l01311"></a>
<a id="l01322"></a>
<a id="l01323"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="l01350"></a>
<a id="l01351"></a>
<a id="l01362"></a>
<a id="l01363"></a>
<a id="l01374"></a>
<a id="l01375"></a>
<a id="l01387"></a>
<a id="l01388"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01402"></a>
<a id="l01404"></a>
<a id="l01410"></a>
<a id="foldopen01412"></a>
<a id="l01412"></a>
<a id="l01414"></a>
<a id="l01415"></a>
<a id="l01417"></a>
<a id="l01418"></a>
<a id="l01419"></a>
<a id="foldopen01426"></a>
<a id="l01426"></a>
<a id="l01428"></a>
<a id="l01429"></a>
<a id="l01431"></a>
<a id="l01432"></a>
<a id="l01433"></a>
<a id="foldopen01435"></a>
<a id="l01435"></a>
<a id="l01437"></a>
<a id="l01438"></a>
<a id="l01440"></a>
<a id="l01441"></a>
<a id="l01449"></a>
<a id="l01450"></a>
<a id="l01451"></a>
<a id="l01460"></a>
<a id="l01461"></a>
<a id="l01470"></a>
<a id="l01471"></a>
<a id="l01479"></a>
<a id="l01480"></a>
<a id="l01481"></a>
<a id="l01482"></a>
<a id="l01496"></a>
<a id="l01497"></a>
<a id="l01498"></a>
<a id="l01514"></a>
<a id="l01515"></a>
<a id="l01516"></a>
<a id="l01536"></a>
<a id="l01537"></a>
<a id="l01538"></a>
<a id="l01539"></a>
<a id="l01550"></a>
<a id="l01551"></a>
<a id="l01560"></a>
<a id="l01561"></a>
<a id="l01562"></a>
<a id="l01574"></a>
<a id="l01575"></a>
<a id="l01576"></a>
<a id="l01577"></a>
<a id="foldopen01579"></a>
<a id="l01579"></a>
<a id="l01587"></a>
<a id="l01588"></a>
<a id="l01596"></a>
<a id="l01597"></a>
<a id="l01603"></a>
<a id="l01604"></a>
<a id="l01610"></a>
<a id="l01611"></a>
<a id="l01617"></a>
<a id="l01618"></a>
<a id="l01624"></a>
<a id="l01625"></a>
<a id="l01627"></a>
<a id="l01628"></a>
<a id="l01634"></a>
<a id="l01635"></a>
<a id="l01642"></a>
<a id="l01643"></a>
<a id="l01644"></a>
<a id="l01650"></a>
<a id="l01651"></a>
<a id="l01657"></a>
<a id="l01658"></a>
<a id="l01660"></a>
<a id="l01661"></a>
<a id="l01662"></a>
<a id="l01663"></a>
<a id="l01673"></a>
<a id="l01674"></a>
<a id="l01675"></a>
<a id="foldopen01677"></a>
<a id="l01677"></a>
<a id="l01688"></a>
<a id="l01689"></a>
<a id="l01700"></a>
<a id="l01701"></a>
<a id="l01702"></a>
<a id="l01713"></a>
<a id="l01714"></a>
<a id="l01715"></a>
<a id="l01725"></a>
<a id="l01726"></a>
<a id="l01727"></a>
<a id="l01740"></a>
<a id="l01741"></a>
<a id="l01742"></a>
<a id="l01753"></a>
<a id="l01754"></a>
<a id="l01755"></a>
<a id="l01768"></a>
<a id="l01769"></a>
<a id="l01770"></a>
<a id="l01783"></a>
<a id="l01784"></a>
<a id="l01785"></a>
<a id="l01796"></a>
<a id="l01797"></a>
<a id="l01798"></a>
<a id="l01809"></a>
<a id="l01810"></a>
<a id="l01811"></a>
<a id="l01822"></a>
<a id="l01823"></a>
<a id="l01824"></a>
<a id="l01839"></a>
<a id="l01840"></a>
<a id="l01841"></a>
<a id="l01853"></a>
<a id="l01854"></a>
<a id="l01867"></a>
<a id="l01868"></a>
<a id="l01871"></a>
<a id="l01873"></a>
<a id="l01874"></a>
<a id="l01884"></a>
<a id="l01885"></a>
<a id="l01894"></a>
<a id="l01895"></a>
<a id="l01914"></a>
<a id="l01915"></a>
<a id="l01929"></a>
<a id="l01930"></a>
<a id="l01931"></a>
<a id="l01942"></a>
<a id="l01943"></a>
<a id="l01951"></a>
<a id="l01953"></a>
<a id="l01955"></a>
<a id="l01956"></a>
<a id="foldopen01958"></a>
<a id="l01958"></a>
<a id="l01960"></a>
<a id="l01962"></a>
<a id="l01964"></a>
<a id="l01965"></a>
<a id="l01966"></a>
<a id="foldopen01968"></a>
<a id="l01968"></a>
<a id="l01970"></a>
<a id="l01972"></a>
<a id="l01974"></a>
<a id="l01975"></a>
<a id="l01976"></a>
<a id="l01985"></a>
<a id="l01986"></a>
<a id="l01995"></a>
<a id="l01996"></a>
<a id="l02005"></a>
<a id="l02006"></a>
<a id="l02015"></a>
<a id="l02016"></a>
<a id="l02026"></a>
<a id="l02027"></a>
<a id="l02039"></a>
<a id="l02040"></a>
<a id="l02041"></a>
<a id="l02042"></a>
<a id="l02043"></a>
<a id="l02053"></a>
<a id="l02054"></a>
<a id="l02055"></a>
<a id="l02065"></a>
<a id="l02066"></a>
<a id="l02067"></a>
<a id="l02077"></a>
<a id="l02078"></a>
<a id="l02079"></a>
<a id="l02090"></a>
<a id="l02091"></a>
<a id="l02092"></a>
<a id="l02101"></a>
<a id="l02102"></a>
<a id="l02112"></a>
<a id="l02113"></a>
<a id="l02114"></a>
<a id="l02126"></a>
<a id="l02127"></a>
<a id="l02128"></a>
<a id="l02129"></a>
<a id="l02130"></a>
<a id="l02144"></a>
<a id="l02145"></a>
<a id="l02146"></a>
<a id="l02148"></a>
<a id="l02155"></a>
<a id="foldopen02161"></a>
<a id="l02161"></a>
<a id="l02167"></a>
<a id="l02168"></a>
<a id="l02175"></a>
<a id="l02176"></a>
<a id="l02179"></a>
<a id="l02181"></a>
<a id="l02182"></a>
<a id="l02192"></a>
<a id="l02193"></a>
<a id="l02203"></a>
<a id="l02204"></a>
<a id="foldopen02206"></a>
<a id="l02206"></a>
<a id="l02208"></a>
<a id="l02209"></a>
<a id="l02210"></a>
<a id="l02216"></a>
<a id="l02217"></a>
<a id="l02219"></a>
<a id="l02220"></a>
<a id="l02221"></a>
<a id="l02222"></a>
<a id="foldopen02224"></a>
<a id="l02224"></a>
<a id="l02226"></a>
<a id="l02227"></a>
<a id="l02229"></a>
<a id="l02230"></a>
<a id="l02232"></a>
<a id="l02233"></a>
<a id="l02234"></a>
<a id="foldopen02236"></a>
<a id="l02236"></a>
<a id="l02238"></a>
<a id="l02239"></a>
<a id="l02241"></a>
<a id="l02242"></a>
<a id="l02244"></a>
<a id="l02245"></a>
<a id="l02253"></a>
<a id="l02254"></a>
<a id="l02256"></a>
<a id="l02257"></a>
<a id="l02268"></a>
<a id="l02269"></a>
<a id="l02270"></a>
<a id="l02278"></a>
<a id="l02279"></a>
<a id="l02287"></a>
<a id="l02288"></a>
<a id="l02296"></a>
<a id="l02297"></a>
<a id="l02298"></a>
<a id="l02299"></a>
<a id="l02316"></a>
<a id="l02317"></a>
<a id="l02318"></a>
<a id="l02338"></a>
<a id="l02339"></a>
<a id="l02340"></a>
<a id="l02353"></a>
<a id="l02354"></a>
<a id="l02355"></a>
<a id="l02367"></a>
<a id="l02368"></a>
<a id="l02369"></a>
<a id="l02380"></a>
<a id="l02381"></a>
<a id="l02392"></a>
<a id="l02393"></a>
<a id="l02408"></a>
<a id="l02409"></a>
<a id="l02410"></a>
<a id="l02420"></a>
<a id="l02421"></a>
<a id="l02422"></a>
<a id="l02434"></a>
<a id="l02435"></a>
<a id="l02436"></a>
<a id="l02438"></a>
<a id="l02445"></a>
<a id="foldopen02447"></a>
<a id="l02447"></a>
<a id="l02458"></a>
<a id="l02459"></a>
<a id="l02460"></a>
<a id="l02473"></a>
<a id="l02474"></a>
<a id="l02481"></a>
<a id="l02482"></a>
<a id="l02489"></a>
<a id="l02490"></a>
<a id="l02493"></a>
<a id="l02495"></a>
<a id="l02496"></a>
<a id="l02510"></a>
<a id="l02511"></a>
<a id="l02530"></a>
<a id="l02531"></a>
<a id="l02532"></a>
<a id="l02552"></a>
<a id="l02553"></a>
<a id="l02554"></a>
<a id="l02555"></a>
<a id="l02566"></a>
<a id="l02567"></a>
<a id="l02579"></a>
<a id="l02580"></a>
<a id="l02582"></a>
<a id="l02596"></a>
<a id="l02597"></a>
<a id="l02608"></a>
<a id="l02609"></a>
<a id="l02621"></a>
<a id="l02622"></a>
<a id="l02623"></a>
<a id="l02632"></a>
<a id="l02633"></a>
<a id="l02634"></a>
<a id="foldopen02636"></a>
<a id="l02636"></a>
<a id="l02638"></a>
<a id="l02639"></a>
<a id="l02641"></a>
<a id="l02642"></a>
<a id="l02649"></a>
<a id="l02650"></a>
<a id="l02652"></a>
<a id="l02653"></a>
<a id="l02655"></a>
<a id="l02656"></a>
<a id="l02658"></a>
<a id="l02659"></a>
<a id="l02661"></a>
<a id="l02662"></a>
<a id="l02663"></a>
<a id="l02682"></a>
<a id="l02683"></a>
<a id="foldopen02685"></a>
<a id="l02685"></a>
<a id="l02687"></a>
<a id="l02688"></a>
<a id="l02690"></a>
<a id="l02691"></a>
<a id="l02693"></a>
<a id="l02694"></a>
<a id="l02696"></a>
<a id="l02697"></a>
<a id="l02699"></a>
<a id="l02700"></a>
<a id="l02701"></a>
<a id="l02715"></a>
<a id="l02716"></a>
<a id="l02730"></a>
<a id="l02731"></a>
<a id="l02742"></a>
<a id="l02743"></a>
<a id="l02744"></a>
<a id="l02751"></a>
<a id="l02752"></a>
<a id="l02753"></a>
<a id="l02762"></a>
<a id="l02763"></a>
<a id="l02764"></a>
<a id="l02765"></a>
<a id="l02766"></a>
<a id="l02773"></a>
<a id="l02774"></a>
<a id="l02775"></a>
<a id="foldopen02781"></a>
<a id="l02781"></a>
<a id="l02791"></a>
<a id="l02792"></a>
<a id="l02793"></a>
<a id="l02803"></a>
<a id="l02804"></a>
<a id="l02805"></a>
<a id="l02815"></a>
<a id="l02816"></a>
<a id="l02817"></a>
<a id="l02824"></a>
<a id="l02825"></a>
<a id="l02832"></a>
<a id="l02833"></a>
<a id="l02840"></a>
<a id="l02841"></a>
<a id="l02848"></a>
<a id="l02849"></a>
<a id="l02856"></a>
<a id="l02857"></a>
<a id="l02864"></a>
<a id="l02865"></a>
<a id="l02872"></a>
<a id="l02873"></a>
<a id="l02876"></a>
<a id="l02878"></a>
<a id="l02879"></a>
<a id="l02896"></a>
<a id="l02897"></a>
<a id="l02922"></a>
<a id="l02923"></a>
<a id="l02924"></a>
<a id="l02938"></a>
<a id="l02939"></a>
<a id="l02949"></a>
<a id="l02950"></a>
<a id="l02960"></a>
<a id="l02961"></a>
<a id="l02962"></a>
<a id="foldopen02964"></a>
<a id="l02964"></a>
<a id="l02966"></a>
<a id="l02967"></a>
<a id="l02969"></a>
<a id="l02970"></a>
<a id="l02972"></a>
<a id="l02973"></a>
<a id="l02975"></a>
<a id="l02976"></a>
<a id="l02982"></a>
<a id="l02983"></a>
<a id="l02985"></a>
<a id="l02986"></a>
<a id="l02992"></a>
<a id="l02993"></a>
<a id="l02994"></a>
<a id="l03008"></a>
<a id="l03009"></a>
<a id="l03010"></a>
<a id="foldopen03012"></a>
<a id="l03012"></a>
<a id="l03014"></a>
<a id="l03015"></a>
<a id="l03017"></a>
<a id="l03018"></a>
<a id="l03024"></a>
<a id="l03025"></a>
<a id="l03027"></a>
<a id="l03028"></a>
<a id="l03030"></a>
<a id="l03031"></a>
<a id="l03032"></a>
<a id="l03046"></a>
<a id="l03047"></a>
<a id="l03048"></a>
<a id="l03063"></a>
<a id="l03064"></a>
<a id="l03065"></a>
<a id="l03066"></a>
<a id="l03080"></a>
<a id="l03081"></a>
<a id="l03096"></a>
<a id="l03097"></a>
<a id="l03099"></a>
<a id="l03100"></a>
<a id="l03101"></a>
<a id="l03102"></a>
<a id="l03103"></a>
<a id="l03104"></a>
<a id="aaddr_8h_html"></a>
<a id="aascs_8h_html"></a>
<a id="aassigned__numbers_8h_html"></a>
<a id="abluetooth_2audio_2audio_8h_html"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="abluetooth_2uuid_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="adata_8h_html"></a>
<a id="agap_8h_html"></a>
<a id="agroup__bt__ascs_html_ga9ca1630544a336b15af8a8e8934c5a45"></a>
<a id="agroup__bt__ascs_html_ga9f7efa749c75edd32dc50503397ab9d1"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga61230848c02098352320fe751332c4e8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gafb379ffa88388cc1397960155bbb2ab3"></a>
<a id="agroup__bt__audio_html_ga5bd899fb5e4d844058184913866e462f"></a>
<a id="agroup__bt__bap__broadcast__sink_html_ga0637d1957db70ad39e0608ed07e75166"></a>
<a id="agroup__bt__bap__broadcast__sink_html_ga1020b21bfb4195aeb5823197145b1fe9"></a>
<a id="agroup__bt__bap__broadcast__sink_html_ga1b83ead634d990e954f233d0208c5a85"></a>
<a id="agroup__bt__bap__broadcast__sink_html_ga8b9d6cb409a3671654e053475ada3fda"></a>
<a id="agroup__bt__bap__broadcast__sink_html_gacadebb5ce8aab5f5b8f1ff7e0fa57805"></a>
<a id="agroup__bt__bap__broadcast__source_html_ga12e0a4856115a8eb297fe2d1fc130155"></a>
<a id="agroup__bt__bap__broadcast__source_html_ga173ddb24e554afc1b16305cca69ad923"></a>
<a id="agroup__bt__bap__broadcast__source_html_ga36a885581eec5cab8b3f652db19b9aba"></a>
<a id="agroup__bt__bap__broadcast__source_html_ga9d543b9282e0dadca3afe3a97e385b15"></a>
<a id="agroup__bt__bap__broadcast__source_html_gabecaa9db7be5cb03ed997ba478878d40"></a>
<a id="agroup__bt__bap__broadcast__source_html_gac4640f5207599d51c1a63ff47f3c1d5a"></a>
<a id="agroup__bt__bap__broadcast__source_html_gac75ad00b8f9a1cd7048677a33b17acda"></a>
<a id="agroup__bt__bap__broadcast__source_html_gacc8d26c42c6b4ae6dc11af84ec4af616"></a>
<a id="agroup__bt__bap__broadcast__source_html_gacdebfc435eebd47cf9cd05099a5f78e0"></a>
<a id="agroup__bt__bap__broadcast__source_html_gafe07e4c6962858500fcf66415a173be8"></a>
<a id="agroup__bt__bap__broadcast__source_html_gaff2cfdadbff3ebe1e2efb660dee56f02"></a>
<a id="agroup__bt__bap__broadcast_html_ga051e1f8aa2faf3ba7a973356138fd2d3"></a>
<a id="agroup__bt__bap__broadcast_html_ga10e2e32dc2802ba55d55c77148331f6a"></a>
<a id="agroup__bt__bap__broadcast_html_ga29423a39d76ad16f0586d82a23c07ba7"></a>
<a id="agroup__bt__bap__broadcast_html_ga37df3bf1e18d2d8e9388541217b2e366"></a>
<a id="agroup__bt__bap__broadcast_html_ga4f85ee43984cb2f3139b41da7b9b1aee"></a>
<a id="agroup__bt__bap__broadcast_html_ga539f92b71ec34f0551ef6240d83b972e"></a>
<a id="agroup__bt__bap__broadcast_html_ga5e6e0b758409cbdde93c0f648ef5e5e8"></a>
<a id="agroup__bt__bap__broadcast_html_ga6deab5a8b7a16ddf0c3685d4003694e1"></a>
<a id="agroup__bt__bap__broadcast_html_ga920e3409f1978b803bcf6bc8d05ac8f6"></a>
<a id="agroup__bt__bap__broadcast_html_gaa5cb191df7807ea87f1fba1871ca8ebe"></a>
<a id="agroup__bt__bap__broadcast_html_gadcae0230168564da1ee8b3c577ce27d7"></a>
<a id="agroup__bt__bap__broadcast_html_gae75e05a002dee8336eb066ae8231ea0c"></a>
<a id="agroup__bt__bap__broadcast_html_gaf91f45bcf7df2f368c5abeb116b65dd0"></a>
<a id="agroup__bt__bap__broadcast_html_gafb9d9544f38c7ad2613fff1679eb1f0c"></a>
<a id="agroup__bt__bap__unicast__client_html_ga34dbdce6133f8366df453ec937fb47d2"></a>
<a id="agroup__bt__bap__unicast__client_html_ga4ba0e4c3fa7ec3a36a64a19c80027504"></a>
<a id="agroup__bt__bap__unicast__client_html_ga9cc792cd1eaaa79d56f3df0e2341cbf6"></a>
<a id="agroup__bt__bap__unicast__client_html_gaafd53b5f45d998b44e94a1b58e93ba21"></a>
<a id="agroup__bt__bap__unicast__client_html_gacd684504c8127ff4f8d038cc06718e5e"></a>
<a id="agroup__bt__bap__unicast__client_html_gacef9c88f66762e8de19303d20dafa0bb"></a>
<a id="agroup__bt__bap__unicast__client_html_gad106ae43201100940d9145d291fe9ca3"></a>
<a id="agroup__bt__bap__unicast__client_html_gad608ee07c8a50abf586a3bc31921f032"></a>
<a id="agroup__bt__bap__unicast__client_html_gad963bdda290df96036a68b00cc940eca"></a>
<a id="agroup__bt__bap__unicast__client_html_gade70f04ae1a828b43b3b44fa8933f674"></a>
<a id="agroup__bt__bap__unicast__client_html_gaee092a4e918a67bb5fd94cb78cc21141"></a>
<a id="agroup__bt__bap__unicast__client_html_gaf0e5a38208e90176292e745933b5e29e"></a>
<a id="agroup__bt__bap__unicast__server_html_ga6ef3b9e877ffdc04cc48fda6713a0209"></a>
<a id="agroup__bt__bap__unicast__server_html_ga7669133936bc13f7ab38817db9ce69c0"></a>
<a id="agroup__bt__bap__unicast__server_html_ga98b170c9f371d7d60c3dde9aff3f6d6b"></a>
<a id="agroup__bt__bap__unicast__server_html_gab3ea6014854e6290f058c87e866c3191"></a>
<a id="agroup__bt__bap__unicast__server_html_gabb2b96d8de285dff7cbade83768d9aff"></a>
<a id="agroup__bt__bap__unicast__server_html_gadf984f12bdeadcfc814dc2fc770cb7bf"></a>
<a id="agroup__bt__bap__unicast__server_html_gafe7640d6269ec95c8af6d7549fac785d"></a>
<a id="agroup__bt__bap_html_ga09785690db551677a043fcaa2fdb7f29"></a>
<a id="agroup__bt__bap_html_ga0afe6c927729697e2f984cefcbc7c0f1"></a>
<a id="agroup__bt__bap_html_ga0fd2bb35909fc19e3e9cff068ba9e9aa"></a>
<a id="agroup__bt__bap_html_ga13a859b31b0310ec22339ec7ed0754f8"></a>
<a id="agroup__bt__bap_html_ga13e9b6d571a613d689b8ba58bae64ae3"></a>
<a id="agroup__bt__bap_html_ga37a5f9d7198739eef8bde6764da30de9"></a>
<a id="agroup__bt__bap_html_ga381c1f3b386ecbdfd570eb125882161e"></a>
<a id="agroup__bt__bap_html_ga443c212a736852305715452e7f165a9e"></a>
<a id="agroup__bt__bap_html_ga47eb6219d730d75ddc4f49dceac7e928"></a>
<a id="agroup__bt__bap_html_ga496c8a2f599d997a7e6e033bda5f0c36"></a>
<a id="agroup__bt__bap_html_ga575a109efb0fd1644634ce6e0288499b"></a>
<a id="agroup__bt__bap_html_ga5e0b0f70d247e131fa542fae16826a22"></a>
<a id="agroup__bt__bap_html_ga63b69967aa92224a2bd9cf79eb41773e"></a>
<a id="agroup__bt__bap_html_ga679cdeb6e555bfc9ce20f38e493000ee"></a>
<a id="agroup__bt__bap_html_ga6c240f1cdb33945197700e4fe106ef2c"></a>
<a id="agroup__bt__bap_html_ga6eb2a782d761da12d112356cfe723ff0"></a>
<a id="agroup__bt__bap_html_ga6f52e58767303ded16cb6289f094895a"></a>
<a id="agroup__bt__bap_html_ga7632ab444dbf99387871f7d0c90b11ba"></a>
<a id="agroup__bt__bap_html_ga76cae35df980b78a10551811050b2760"></a>
<a id="agroup__bt__bap_html_ga8f2dc67c35299334d21c7dee7b8664ae"></a>
<a id="agroup__bt__bap_html_ga94fce2b4346b1026d53e0b860ca7fbf2"></a>
<a id="agroup__bt__bap_html_ga98ac067e66d263aa41fc6f8df6bb9126"></a>
<a id="agroup__bt__bap_html_gaa0e012446238c916abc84d6c0de89bf3"></a>
<a id="agroup__bt__bap_html_gaa75f2cd2c36fdaef04a62c95bec6e2e3"></a>
<a id="agroup__bt__bap_html_gaa7df3f6b906241ad5291295a6ddcf1e4"></a>
<a id="agroup__bt__bap_html_gaa9c292a7dcb470926d8d7d4be699a0c7"></a>
<a id="agroup__bt__bap_html_gaaecbb590e5d073829d4c150e4fd2d8aa"></a>
<a id="agroup__bt__bap_html_gaaf94f1f0dda7ef356c0f9ae79b5c60e4"></a>
<a id="agroup__bt__bap_html_gab29c1e134156dceaa6c67abae9239378"></a>
<a id="agroup__bt__bap_html_gab59c5ebc4fef28da34d8a54b1244c33b"></a>
<a id="agroup__bt__bap_html_gab6f1a12699a9437c6575c70df33d5be0"></a>
<a id="agroup__bt__bap_html_gabab24c44e9833029965475ad7b149e6e"></a>
<a id="agroup__bt__bap_html_gabcec07689c13a996bcb9d2d417347dbb"></a>
<a id="agroup__bt__bap_html_gabec9fd0a2966e1811fd4770855050510"></a>
<a id="agroup__bt__bap_html_gac022f38269742f16ff6887840ef5ba9a"></a>
<a id="agroup__bt__bap_html_gac551e9b0d53fd50f3a9e9c08447f0296"></a>
<a id="agroup__bt__bap_html_gac878ed89242cac9a8514e8e4f1da4d9d"></a>
<a id="agroup__bt__bap_html_gac93cb4cab33d0b937e752bc0b71cad9e"></a>
<a id="agroup__bt__bap_html_gada72bcd3951eff2bc6b70c02dcaed98b"></a>
<a id="agroup__bt__bap_html_gaf15e5ec5bca364f6a3e7a43b1f27da68"></a>
<a id="agroup__bt__bap_html_gaf210a91e1ff11d9bf7792ba47d1e1b4a"></a>
<a id="agroup__bt__bap_html_gaf236a87ae461ad48ec59f487780b4824"></a>
<a id="agroup__bt__bap_html_gaf610cd6cddd52622f95cfd35b19ee841"></a>
<a id="agroup__bt__bap_html_gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c"></a>
<a id="agroup__bt__bap_html_gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202"></a>
<a id="agroup__bt__bap_html_gga37a5f9d7198739eef8bde6764da30de9a406ad3527d9d92e4e8b213fe52794298"></a>
<a id="agroup__bt__bap_html_gga37a5f9d7198739eef8bde6764da30de9afe1ffd5db8e36f8082a2ef7545e04a94"></a>
<a id="agroup__bt__bap_html_gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2"></a>
<a id="agroup__bt__bap_html_gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4"></a>
<a id="agroup__bt__bap_html_gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b"></a>
<a id="agroup__bt__bap_html_gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10"></a>
<a id="agroup__bt__bap_html_gga5e8ebf4db88f94f44828bb6f41e81d44ab41e06fe31c57bb7dac5a77acb53be73"></a>
<a id="agroup__bt__bap_html_gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147"></a>
<a id="agroup__bt__bap_html_gga5e8ebf4db88f94f44828bb6f41e81d44af5bc162fe51c445cb3c77bcf640bbe28"></a>
<a id="agroup__bt__bap_html_ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf"></a>
<a id="agroup__bt__bap_html_ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647"></a>
<a id="agroup__bt__bap_html_ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc"></a>
<a id="agroup__bt__bap_html_ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb"></a>
<a id="agroup__bt__bap_html_ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d"></a>
<a id="agroup__bt__bap_html_ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332"></a>
<a id="agroup__bt__bap_html_ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961"></a>
<a id="agroup__bt__bap_html_ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688"></a>
<a id="agroup__bt__bap_html_ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c"></a>
<a id="agroup__bt__bap_html_ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523"></a>
<a id="agroup__bt__bap_html_ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8"></a>
<a id="agroup__bt__bap_html_ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710"></a>
<a id="agroup__bt__iso_html_ga5551cab9896764eec39b8e6102e561e5"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="aiso_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__addr__le__t_html"></a>
<a id="astructbt__audio__codec__cap_html"></a>
<a id="astructbt__audio__codec__cfg_html"></a>
<a id="astructbt__bap__ascs__rsp_html"></a>
<a id="astructbt__bap__base__codec__id_html"></a>
<a id="astructbt__bap__base__codec__id_html_a0aadd7e53f72efd8c0e33dd9a8eca177"></a>
<a id="astructbt__bap__base__codec__id_html_a49802819cc3129a993320b95472f2262"></a>
<a id="astructbt__bap__base__codec__id_html_a9031aaf6a3f6e0acf68f1bfaed39b819"></a>
<a id="astructbt__bap__base__subgroup__bis_html"></a>
<a id="astructbt__bap__base__subgroup__bis_html_aa53f22b29e447822e8bb36d9245bfc77"></a>
<a id="astructbt__bap__base__subgroup__bis_html_ac4132c798c04c0f93c944dc91891221e"></a>
<a id="astructbt__bap__base__subgroup__bis_html_ad0f5dff3150c36b1625f1f6f206d41d2"></a>
<a id="astructbt__bap__bass__subgroup_html"></a>
<a id="astructbt__bap__bass__subgroup_html_a851fda16d0856714ebf4d3970c4d2e4b"></a>
<a id="astructbt__bap__bass__subgroup_html_ac8061995eb73ba30e335e37714396ff5"></a>
<a id="astructbt__bap__bass__subgroup_html_ace1c1ff5d2f5cc79838653d468166664"></a>
<a id="astructbt__bap__broadcast__assistant__add__src__param_html"></a>
<a id="astructbt__bap__broadcast__assistant__add__src__param_html_a17b67d65b6840c3d4480027b7deb31a5"></a>
<a id="astructbt__bap__broadcast__assistant__add__src__param_html_a2b04d75ca9a740a7d819eae1bcc5cba7"></a>
<a id="astructbt__bap__broadcast__assistant__add__src__param_html_a390cd8d887cd256ee74b39b9b516cac4"></a>
<a id="astructbt__bap__broadcast__assistant__add__src__param_html_ab8423e5cce4a6c9ac142221d2e816763"></a>
<a id="astructbt__bap__broadcast__assistant__add__src__param_html_acaecbbf7b3c96fe5ca53f90e92fa1e5e"></a>
<a id="astructbt__bap__broadcast__assistant__add__src__param_html_ad9af814e8a232230d4ee97c459f47747"></a>
<a id="astructbt__bap__broadcast__assistant__add__src__param_html_ae50b6b5a3f2c92f01e7070c605b37dde"></a>
<a id="astructbt__bap__broadcast__assistant__cb_html"></a>
<a id="astructbt__bap__broadcast__assistant__cb_html_a01ad0a89db9041670f6a68d6f1680988"></a>
<a id="astructbt__bap__broadcast__assistant__cb_html_a09de9cb86dad76b485ff52257a0c68dc"></a>
<a id="astructbt__bap__broadcast__assistant__cb_html_a629ff4299b8ae5bcbddf28338caddfd0"></a>
<a id="astructbt__bap__broadcast__assistant__cb_html_a80296a38e664aabff7ec27e007c59e95"></a>
<a id="astructbt__bap__broadcast__assistant__cb_html_ab24e3ecb9764ca833524b787126b8c2c"></a>
<a id="astructbt__bap__broadcast__assistant__cb_html_ab88d98b1e742ccd36aac69069ebf3f61"></a>
<a id="astructbt__bap__broadcast__assistant__cb_html_ad2bdfcc0147a751910d82232a77e34f8"></a>
<a id="astructbt__bap__broadcast__assistant__cb_html_ad909b9e6e3c35be10a29ee5a4b7213fb"></a>
<a id="astructbt__bap__broadcast__assistant__cb_html_af0cf259088cd793152390b21813a9481"></a>
<a id="astructbt__bap__broadcast__assistant__cb_html_af3fb53d95cdc7ba202657e4c54e0b2b8"></a>
<a id="astructbt__bap__broadcast__assistant__mod__src__param_html"></a>
<a id="astructbt__bap__broadcast__assistant__mod__src__param_html_a2383ec98b14054e0bc66bb4a0ae7b8b6"></a>
<a id="astructbt__bap__broadcast__assistant__mod__src__param_html_a42b12c6d9f5c622433c9c1f0c72726c1"></a>
<a id="astructbt__bap__broadcast__assistant__mod__src__param_html_a5bc7c0a491872d655296bbb979402a62"></a>
<a id="astructbt__bap__broadcast__assistant__mod__src__param_html_a794bb68c8a73edfe3d44dbe9a0bf2830"></a>
<a id="astructbt__bap__broadcast__assistant__mod__src__param_html_aebaa104384dcbec7bb952a27f3acc24d"></a>
<a id="astructbt__bap__broadcast__sink__cb_html"></a>
<a id="astructbt__bap__broadcast__sink__cb_html_a1adf2124ec9a16c3c68774194febd0fc"></a>
<a id="astructbt__bap__broadcast__sink__cb_html_a1dd64d7c764ddd6c531bdd5b1890694f"></a>
<a id="astructbt__bap__broadcast__sink__cb_html_a23390a63acbcf831a177a550d1012047"></a>
<a id="astructbt__bap__broadcast__sink__cb_html_a6af7aa849cebad26cdf382a1c97a681f"></a>
<a id="astructbt__bap__broadcast__sink_html"></a>
<a id="astructbt__bap__broadcast__source__cb_html"></a>
<a id="astructbt__bap__broadcast__source__cb_html_a1108c983823ee3331d8343db4ec9c0c5"></a>
<a id="astructbt__bap__broadcast__source__cb_html_a66b62e90c1cdfa2c2963bafe99670f92"></a>
<a id="astructbt__bap__broadcast__source__param_html"></a>
<a id="astructbt__bap__broadcast__source__param_html_a11b03e3d63ca2e116e743d9efde920be"></a>
<a id="astructbt__bap__broadcast__source__param_html_a493fa57a80e21a288854b2e3e1df775a"></a>
<a id="astructbt__bap__broadcast__source__param_html_a50c29b5a2bcae162c0bbda32102a30cc"></a>
<a id="astructbt__bap__broadcast__source__param_html_a5e155c3b92b4f9de3c9e6efa377097e3"></a>
<a id="astructbt__bap__broadcast__source__param_html_a6291842b49a55f6b2767dc95c9e874f3"></a>
<a id="astructbt__bap__broadcast__source__param_html_a6a05b6448f55cf5f52f90e44d83146dc"></a>
<a id="astructbt__bap__broadcast__source__param_html_a71abc0496153a9b8eab402bfaaf92e72"></a>
<a id="astructbt__bap__broadcast__source__param_html_a7552bf9a4ff5441b13669effe23abb8c"></a>
<a id="astructbt__bap__broadcast__source__param_html_aab1799ab671500b02c1ab0e023ac43f7"></a>
<a id="astructbt__bap__broadcast__source__stream__param_html"></a>
<a id="astructbt__bap__broadcast__source__stream__param_html_a9c92fb50b62d963e01b1506b790fb5e1"></a>
<a id="astructbt__bap__broadcast__source__stream__param_html_aa1925bb8a770c05b34928d7220177ffa"></a>
<a id="astructbt__bap__broadcast__source__stream__param_html_ac79a76ad748673ca4bd52c597cd073df"></a>
<a id="astructbt__bap__broadcast__source__subgroup__param_html"></a>
<a id="astructbt__bap__broadcast__source__subgroup__param_html_a4d5d610b562fc34c8840e4eed037ba86"></a>
<a id="astructbt__bap__broadcast__source__subgroup__param_html_a701d9480ffae2351149de6b962095d32"></a>
<a id="astructbt__bap__broadcast__source__subgroup__param_html_a9719e89d8979f9502023e0032814c477"></a>
<a id="astructbt__bap__broadcast__source_html"></a>
<a id="astructbt__bap__ep__info_html"></a>
<a id="astructbt__bap__ep__info_html_a07e8878e7e6a8ee059639330ffa78c1c"></a>
<a id="astructbt__bap__ep__info_html_a30698c71f556ca876a1c69bffefac653"></a>
<a id="astructbt__bap__ep__info_html_a54dd673e21455c85193df844f3aa4083"></a>
<a id="astructbt__bap__ep__info_html_a650727747d0a093528544c3e16255feb"></a>
<a id="astructbt__bap__ep__info_html_a819ac77dcf7cb6985e97f290a666ed09"></a>
<a id="astructbt__bap__ep__info_html_abb0dc6d25744cd734f8fd6ba2bc84b24"></a>
<a id="astructbt__bap__ep__info_html_abbad124bf9e40ed530b2a33fefbadc84"></a>
<a id="astructbt__bap__ep__info_html_ad5201e9b9623e8ff8e74e1be87ece864"></a>
<a id="astructbt__bap__ep_html"></a>
<a id="astructbt__bap__qos__cfg__pref_html"></a>
<a id="astructbt__bap__qos__cfg_html"></a>
<a id="astructbt__bap__qos__cfg_html_a294709496f7779ee4cb7aa542da8832b"></a>
<a id="astructbt__bap__qos__cfg_html_a597b81261511ec820caa66bd091ab896"></a>
<a id="astructbt__bap__qos__cfg_html_a60057a7812cdc5b26f839e68dc4603c4"></a>
<a id="astructbt__bap__qos__cfg_html_a912ee316aa2ddb00ebab7bb78af0f34a"></a>
<a id="astructbt__bap__qos__cfg_html_a97094ac8254ff3e97790943a5c71cdf3"></a>
<a id="astructbt__bap__qos__cfg_html_aaaa4a88499cfd1f90e409fa98891bf2c"></a>
<a id="astructbt__bap__qos__cfg_html_abf8a1b76cc0735b9aec1962d2ce574ec"></a>
<a id="astructbt__bap__qos__cfg_html_ac50ea51e1645546d8f8faa58c64672ce"></a>
<a id="astructbt__bap__qos__cfg_html_acb84f2da73e865e38dcefa92007f01e1"></a>
<a id="astructbt__bap__qos__cfg_html_addf190fac00b2fb99c0d1abf13eb20b3"></a>
<a id="astructbt__bap__scan__delegator__add__src__param_html"></a>
<a id="astructbt__bap__scan__delegator__add__src__param_html_a0945a707a9a50a152220463ba1678de0"></a>
<a id="astructbt__bap__scan__delegator__add__src__param_html_a12bed26ffdc9d4683a5fcdf512a194eb"></a>
<a id="astructbt__bap__scan__delegator__add__src__param_html_a502d263982995c99559714f07d74443f"></a>
<a id="astructbt__bap__scan__delegator__add__src__param_html_a751106648b8f040747b5ffb804932798"></a>
<a id="astructbt__bap__scan__delegator__add__src__param_html_a80817dd3bc046d76baabd62e470ad797"></a>
<a id="astructbt__bap__scan__delegator__add__src__param_html_a8e8eda4139e460800c6195b4c5f246e2"></a>
<a id="astructbt__bap__scan__delegator__add__src__param_html_ac64d1608bede3b9fbac5f86488a3ac79"></a>
<a id="astructbt__bap__scan__delegator__cb_html"></a>
<a id="astructbt__bap__scan__delegator__cb_html_a0ea55963f92361f35e68eadcf10306b1"></a>
<a id="astructbt__bap__scan__delegator__cb_html_a1ca1642de4bcf3f6552d09761168b1fc"></a>
<a id="astructbt__bap__scan__delegator__cb_html_a5b918538cfe0edaa69155f891981eeae"></a>
<a id="astructbt__bap__scan__delegator__cb_html_a5d95631d95ae1085071c9b795eca1a8e"></a>
<a id="astructbt__bap__scan__delegator__cb_html_a78d011c817e60725a0ef14c68bd655cd"></a>
<a id="astructbt__bap__scan__delegator__cb_html_a8da03993be622b5d25e8bd462dfd16c5"></a>
<a id="astructbt__bap__scan__delegator__cb_html_a92351aea994520cd08f87d3d579d6e3b"></a>
<a id="astructbt__bap__scan__delegator__cb_html_ae41d499d75123a1b70b778e8e95edcc3"></a>
<a id="astructbt__bap__scan__delegator__cb_html_af862ad2d51d60e57cc50e20c256fde35"></a>
<a id="astructbt__bap__scan__delegator__mod__src__param_html"></a>
<a id="astructbt__bap__scan__delegator__mod__src__param_html_a11b4c6d787bd2c828e565282daf5cf2f"></a>
<a id="astructbt__bap__scan__delegator__mod__src__param_html_aa8dcd7983005ffd23779db6b6ccfb752"></a>
<a id="astructbt__bap__scan__delegator__mod__src__param_html_ab189593d0125cd443331bcb390d5502e"></a>
<a id="astructbt__bap__scan__delegator__mod__src__param_html_ae387a2c0613545ae3acd372780f738bb"></a>
<a id="astructbt__bap__scan__delegator__mod__src__param_html_aecc8b74632dcb2b17b9a358e00c75d31"></a>
<a id="astructbt__bap__scan__delegator__recv__state_html"></a>
<a id="astructbt__bap__scan__delegator__recv__state_html_a1755a6332c86aeaf624d3c540037772a"></a>
<a id="astructbt__bap__scan__delegator__recv__state_html_a1c268bb7b340c874935f186c0ba2a253"></a>
<a id="astructbt__bap__scan__delegator__recv__state_html_a30fbad06780fd7bca9aacdf14ecaf4a0"></a>
<a id="astructbt__bap__scan__delegator__recv__state_html_a49030d5859dfc21e9a4478b6ed20994e"></a>
<a id="astructbt__bap__scan__delegator__recv__state_html_a6153ea6bbfe7057c39f6b652a4e6e34e"></a>
<a id="astructbt__bap__scan__delegator__recv__state_html_aa03e02a1832950e4a53ff2fe803c14a6"></a>
<a id="astructbt__bap__scan__delegator__recv__state_html_aa97765bdbaa43a280645eb62c0035b82"></a>
<a id="astructbt__bap__scan__delegator__recv__state_html_abaa80f30cf2e84ee873d18eaedd4159d"></a>
<a id="astructbt__bap__scan__delegator__recv__state_html_ac770a5ad001f73d3acaf2b36827f9343"></a>
<a id="astructbt__bap__stream__ops_html"></a>
<a id="astructbt__bap__stream__ops_html_a09f31dc30de9c880758ec4a1468e59f0"></a>
<a id="astructbt__bap__stream__ops_html_a1c67137b439a87647994530710d9e075"></a>
<a id="astructbt__bap__stream__ops_html_a23616f17ef90a03db2f78df180887897"></a>
<a id="astructbt__bap__stream__ops_html_a33b07c51394dea6d632f42aec89a1510"></a>
<a id="astructbt__bap__stream__ops_html_a37876562731d7dbbcd5f5613621b78ca"></a>
<a id="astructbt__bap__stream__ops_html_a3fc784b8a2a7c1a5b19dece3619c130e"></a>
<a id="astructbt__bap__stream__ops_html_a533d5ea96aa67b9b74b19c55afd43df1"></a>
<a id="astructbt__bap__stream__ops_html_a553777c6b6bdda3e0e8c03f3915404cd"></a>
<a id="astructbt__bap__stream__ops_html_a7f595e37d40b94510bf09c1f82b479f3"></a>
<a id="astructbt__bap__stream__ops_html_a953c7174297f1a27ceed012dced53c5a"></a>
<a id="astructbt__bap__stream__ops_html_ab50ea295069a2cd1ab6f4353052262f5"></a>
<a id="astructbt__bap__stream__ops_html_afa90da66b69835c9df73068aa6373778"></a>
<a id="astructbt__bap__stream_html"></a>
<a id="astructbt__bap__stream_html_a17d91a06d581cd4341d035eb76d8e0b2"></a>
<a id="astructbt__bap__stream_html_a286b95d990433995a7ee74b7c3ec2f59"></a>
<a id="astructbt__bap__stream_html_a46a1f70c1a1fe4696039be14adf3c9b6"></a>
<a id="astructbt__bap__stream_html_a503bd9d7e7f594d090bcbe7fc5e313fc"></a>
<a id="astructbt__bap__stream_html_a90e49f0d9abeabeff602e5409d8416e4"></a>
<a id="astructbt__bap__stream_html_adb95fe7a0b981a46898382ee45fd99df"></a>
<a id="astructbt__bap__stream_html_af871d28b2cca8e4deba66997badbeca2"></a>
<a id="astructbt__bap__stream_html_afe81620dd215aebe04ddc9e36dc7d2dd"></a>
<a id="astructbt__bap__unicast__client__cb_html"></a>
<a id="astructbt__bap__unicast__client__cb_html_a15dd1277b37dcd96a545bb6d450c2f9d"></a>
<a id="astructbt__bap__unicast__client__cb_html_a1f2f7476506b6b798c1f26371217956e"></a>
<a id="astructbt__bap__unicast__client__cb_html_a23b82e9f4174bcc2130d6f4570990180"></a>
<a id="astructbt__bap__unicast__client__cb_html_a3c55f4e23607b1e655b5f520d691bf33"></a>
<a id="astructbt__bap__unicast__client__cb_html_a47f86af7675fcf6ac86fad578437afa9"></a>
<a id="astructbt__bap__unicast__client__cb_html_a5c2d9ec444699ae5c75736115aab0b71"></a>
<a id="astructbt__bap__unicast__client__cb_html_a64546cd17ac346dcb4bbfad5bd9f9616"></a>
<a id="astructbt__bap__unicast__client__cb_html_a7b5fcba437b1532dbac796a48fee2f6a"></a>
<a id="astructbt__bap__unicast__client__cb_html_a7dc1f2486bdabf37b85d0b347563e314"></a>
<a id="astructbt__bap__unicast__client__cb_html_a814a5b22c3f75b7708dac5cfdb55292f"></a>
<a id="astructbt__bap__unicast__client__cb_html_abf8ec1b630220172887e3d3d4c550992"></a>
<a id="astructbt__bap__unicast__client__cb_html_ac49c3b8283552213623608498a7befd2"></a>
<a id="astructbt__bap__unicast__client__cb_html_ae473ecc92b5c02a29742d0ba0c51ef4a"></a>
<a id="astructbt__bap__unicast__client__cb_html_ae5c31f2540eb39c5b8272b5ae1e867fd"></a>
<a id="astructbt__bap__unicast__group__info_html"></a>
<a id="astructbt__bap__unicast__group__info_html_a05ecedc6350f6961d9794f854bf5be37"></a>
<a id="astructbt__bap__unicast__group__info_html_a0cfbd31f735e4d18ac95f2e7d2a31f9a"></a>
<a id="astructbt__bap__unicast__group__info_html_a15731dd811989ea465f2b2b490502db4"></a>
<a id="astructbt__bap__unicast__group__info_html_a180fe8c6c0081da2f2cb38b3df0fadaf"></a>
<a id="astructbt__bap__unicast__group__info_html_a1e49ada1c3a60ac73e29cc32f95a9533"></a>
<a id="astructbt__bap__unicast__group__info_html_a25208a4e06afd726c6f6f0714233526a"></a>
<a id="astructbt__bap__unicast__group__info_html_a70883292203e5f37f71238f0b659aa31"></a>
<a id="astructbt__bap__unicast__group__info_html_a74730a75337b985b7260297b1ecf8a21"></a>
<a id="astructbt__bap__unicast__group__info_html_a9c12fa3c837c300528dce41c8789e301"></a>
<a id="astructbt__bap__unicast__group__info_html_aa310b32478893830907878f59a65f876"></a>
<a id="astructbt__bap__unicast__group__info_html_ac701205d557f5cdb27663e2521082681"></a>
<a id="astructbt__bap__unicast__group__info_html_aee9990d7b3a7e7c8230fb5f4eb7198b8"></a>
<a id="astructbt__bap__unicast__group__param_html"></a>
<a id="astructbt__bap__unicast__group__param_html_a278797713b97a6520247b01caa2938b9"></a>
<a id="astructbt__bap__unicast__group__param_html_a6829c82346ca70772a4ab0dc93fbb88f"></a>
<a id="astructbt__bap__unicast__group__param_html_a72e2c6dbeb7b7778f92af5cab2474a7e"></a>
<a id="astructbt__bap__unicast__group__param_html_a7980c8e5c66a11507701ce2679b461ed"></a>
<a id="astructbt__bap__unicast__group__param_html_a9cd09b720fa9a31364878ba205b3b58c"></a>
<a id="astructbt__bap__unicast__group__param_html_aefae7dfccdaed2bc3f59ca63689d4f2e"></a>
<a id="astructbt__bap__unicast__group__stream__pair__param_html"></a>
<a id="astructbt__bap__unicast__group__stream__pair__param_html_ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d"></a>
<a id="astructbt__bap__unicast__group__stream__pair__param_html_ae73a11aab16a60806d1a941306c1822a"></a>
<a id="astructbt__bap__unicast__group__stream__param_html"></a>
<a id="astructbt__bap__unicast__group__stream__param_html_a8424dfd660759a6dd226f53413069a8a"></a>
<a id="astructbt__bap__unicast__group__stream__param_html_acfa192fed73b27fb194881f0021fcb35"></a>
<a id="astructbt__bap__unicast__group_html"></a>
<a id="astructbt__bap__unicast__server__cb_html"></a>
<a id="astructbt__bap__unicast__server__cb_html_a22f1af95f055bce79e3810b9682024cf"></a>
<a id="astructbt__bap__unicast__server__cb_html_a2d50b6c328607fc46d85eaf12633f13d"></a>
<a id="astructbt__bap__unicast__server__cb_html_a48fb3021507a708a0847a1ebec6075ba"></a>
<a id="astructbt__bap__unicast__server__cb_html_a5fe98295e41c426a12ab4a7875b665c8"></a>
<a id="astructbt__bap__unicast__server__cb_html_a7424079675204fba02339ddc661b77c5"></a>
<a id="astructbt__bap__unicast__server__cb_html_a7bed12780fdf780227d38b61d76d099b"></a>
<a id="astructbt__bap__unicast__server__cb_html_a932296643929403c11512ff4ee7f7879"></a>
<a id="astructbt__bap__unicast__server__cb_html_a9f5169f0bcdb3a6560f0767ec117b3c6"></a>
<a id="astructbt__bap__unicast__server__cb_html_ad179b35a5a5685edb8f0ac1b791d5271"></a>
<a id="astructbt__bap__unicast__server__register__param_html"></a>
<a id="astructbt__bap__unicast__server__register__param_html_a88635d5926173f23f411402b5961f783"></a>
<a id="astructbt__bap__unicast__server__register__param_html_ab4963c035d75404831ec1293c7f40f95"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__data_html"></a>
<a id="astructbt__iso__biginfo_html"></a>
<a id="astructbt__iso__chan_html"></a>
<a id="astructbt__iso__recv__info_html"></a>
<a id="astructbt__iso__tx__info_html"></a>
<a id="astructbt__le__ext__adv_html"></a>
<a id="astructbt__le__per__adv__sync_html"></a>
<a id="astructbt__le__scan__recv__info_html"></a>
<a id="astructgroup_html"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="astructnet__buf_html"></a>
<a id="autil__macro_8h_html"></a>

```c


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_BAP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_BAP_H_


#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/audio/ascs.h>
#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/data.h>
#include <zephyr/bluetooth/gap.h>
#include <zephyr/bluetooth/iso.h>
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_BAP_BASS_MAX_SUBGROUPS                                                                  \
        COND_CODE_1(CONFIG_BT_AUDIO, (CONFIG_BT_BAP_BASS_MAX_SUBGROUPS), (0))

#define BT_BASE_MAX_SIZE (UINT8_MAX - 1 /* type */ - BT_UUID_SIZE_16)

#define BT_BAP_INVALID_BROADCAST_ID 0xFFFFFFFFU

#define BT_BAP_PD_UNSET 0xFFFFFFFFU

#define BT_BAP_ADV_PARAM_CONN_QUICK                                                                \
        BT_LE_ADV_PARAM(BT_LE_ADV_OPT_CONN | BT_LE_ADV_OPT_EXT_ADV, BT_GAP_MS_TO_ADV_INTERVAL(20), \
                        BT_GAP_MS_TO_ADV_INTERVAL(30), NULL)

#define BT_BAP_ADV_PARAM_CONN_REDUCED                                                              \
        BT_LE_ADV_PARAM(BT_LE_ADV_OPT_CONN | BT_LE_ADV_OPT_EXT_ADV,                                \
                        BT_GAP_MS_TO_ADV_INTERVAL(150), BT_GAP_MS_TO_ADV_INTERVAL(150), NULL)

#define BT_BAP_CONN_PARAM_SHORT_7_5                                                                \
        BT_LE_CONN_PARAM(BT_GAP_US_TO_CONN_INTERVAL(7500), BT_GAP_MS_TO_CONN_INTERVAL(30), 0,      \
                         BT_GAP_MS_TO_CONN_TIMEOUT(4000))

#define BT_BAP_CONN_PARAM_SHORT_10                                                                 \
        BT_LE_CONN_PARAM(BT_GAP_MS_TO_CONN_INTERVAL(10), BT_GAP_MS_TO_CONN_INTERVAL(30), 0,        \
                         BT_GAP_MS_TO_CONN_TIMEOUT(4000))

#define BT_BAP_CONN_PARAM_RELAXED                                                                  \
        BT_LE_CONN_PARAM(BT_GAP_MS_TO_CONN_INTERVAL(50), BT_GAP_MS_TO_CONN_INTERVAL(70), 0,        \
                         BT_GAP_MS_TO_CONN_TIMEOUT(4000))

#define BT_BAP_ADV_PARAM_BROADCAST_FAST                                                            \
        BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV, BT_GAP_MS_TO_ADV_INTERVAL(60),                      \
                        BT_GAP_MS_TO_ADV_INTERVAL(60), NULL)

#define BT_BAP_ADV_PARAM_BROADCAST_SLOW                                                            \
        BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV, BT_GAP_MS_TO_ADV_INTERVAL(150),                     \
                        BT_GAP_MS_TO_ADV_INTERVAL(150), NULL)

#define BT_BAP_PER_ADV_PARAM_BROADCAST_FAST                                                        \
        BT_LE_PER_ADV_PARAM(BT_GAP_MS_TO_PER_ADV_INTERVAL(60), BT_GAP_MS_TO_PER_ADV_INTERVAL(60),  \
                            BT_LE_PER_ADV_OPT_NONE)

#define BT_BAP_PER_ADV_PARAM_BROADCAST_SLOW                                                        \
        BT_LE_PER_ADV_PARAM(BT_GAP_MS_TO_PER_ADV_INTERVAL(150),                                    \
                            BT_GAP_MS_TO_PER_ADV_INTERVAL(150), BT_LE_PER_ADV_OPT_NONE)

#define BT_BAP_BASS_VALID_BIT_BITFIELD(_bis_bitfield)                                              \
        ((_bis_bitfield) == 0U || (_bis_bitfield) == BT_BAP_BIS_SYNC_NO_PREF ||                    \
         BT_ISO_VALID_BIS_BITFIELD(_bis_bitfield))

#define BT_BAP_QOS_CFG(_interval, _framing, _phy, _sdu, _rtn, _latency, _pd)                       \
        ((struct bt_bap_qos_cfg){                                                                  \
                .interval = _interval,                                                             \
                .framing = _framing,                                                               \
                .phy = _phy,                                                                       \
                .sdu = _sdu,                                                                       \
                .rtn = _rtn,                                                                       \
                IF_ENABLED(UTIL_OR(IS_ENABLED(CONFIG_BT_BAP_BROADCAST_SOURCE),                     \
                                   IS_ENABLED(CONFIG_BT_BAP_UNICAST)),                             \
                           (.latency = _latency,))                                                 \
                .pd = _pd,                                                                         \
        })

enum bt_bap_qos_cfg_framing {
        BT_BAP_QOS_CFG_FRAMING_UNFRAMED = 0x00,
        BT_BAP_QOS_CFG_FRAMING_FRAMED = 0x01,
};

enum {
        BT_BAP_QOS_CFG_1M = BIT(0U),
        BT_BAP_QOS_CFG_2M = BIT(1U),
        BT_BAP_QOS_CFG_CODED = BIT(2U),
};

#define BT_BAP_QOS_CFG_UNFRAMED(_interval, _sdu, _rtn, _latency, _pd)                              \
        BT_BAP_QOS_CFG(_interval, BT_BAP_QOS_CFG_FRAMING_UNFRAMED, BT_BAP_QOS_CFG_2M, _sdu, _rtn,  \
                       _latency, _pd)

#define BT_BAP_QOS_CFG_FRAMED(_interval, _sdu, _rtn, _latency, _pd)                                \
        BT_BAP_QOS_CFG(_interval, BT_BAP_QOS_CFG_FRAMING_FRAMED, BT_BAP_QOS_CFG_2M, _sdu, _rtn,    \
                       _latency, _pd)

struct bt_bap_qos_cfg {
        uint32_t pd;

        struct {
                enum bt_bap_qos_cfg_framing framing;

                uint8_t phy;

                uint8_t rtn;

                uint16_t sdu;

#if defined(CONFIG_BT_BAP_BROADCAST_SOURCE) || defined(CONFIG_BT_BAP_UNICAST) ||                   \
        defined(__DOXYGEN__)
                uint16_t latency;
#endif /*  CONFIG_BT_BAP_BROADCAST_SOURCE || CONFIG_BT_BAP_UNICAST */

                uint32_t interval;

#if defined(CONFIG_BT_ISO_TEST_PARAMS) || defined(__DOXYGEN__)
                uint16_t max_pdu;

                uint8_t burst_number;

                uint8_t num_subevents;
#endif /* CONFIG_BT_ISO_TEST_PARAMS */
        };
};

enum bt_bap_pa_state {
        BT_BAP_PA_STATE_NOT_SYNCED = 0x00,

        BT_BAP_PA_STATE_INFO_REQ = 0x01,

        BT_BAP_PA_STATE_SYNCED = 0x02,

        BT_BAP_PA_STATE_FAILED = 0x03,

        BT_BAP_PA_STATE_NO_PAST = 0x04,
};

enum bt_bap_big_enc_state {
        BT_BAP_BIG_ENC_STATE_NO_ENC = 0x00,

        BT_BAP_BIG_ENC_STATE_BCODE_REQ = 0x01,

        BT_BAP_BIG_ENC_STATE_DEC = 0x02,

        BT_BAP_BIG_ENC_STATE_BAD_CODE = 0x03,
};

enum bt_bap_bass_att_err {
        BT_BAP_BASS_ERR_OPCODE_NOT_SUPPORTED = 0x80,

        BT_BAP_BASS_ERR_INVALID_SRC_ID = 0x81,
};

#define BT_BAP_PA_INTERVAL_UNKNOWN             0xFFFFU

#define BT_BAP_BIS_SYNC_NO_PREF 0xFFFFFFFFU
#define BT_BAP_BIS_SYNC_FAILED  0xFFFFFFFFU

enum bt_bap_ep_state {
        BT_BAP_EP_STATE_IDLE = 0x00,

        BT_BAP_EP_STATE_CODEC_CONFIGURED = 0x01,

        BT_BAP_EP_STATE_QOS_CONFIGURED = 0x02,

        BT_BAP_EP_STATE_ENABLING = 0x03,

        BT_BAP_EP_STATE_STREAMING = 0x04,

        BT_BAP_EP_STATE_DISABLING = 0x05,

        BT_BAP_EP_STATE_RELEASING = 0x06,
};

struct bt_bap_broadcast_source;

struct bt_bap_broadcast_sink;

struct bt_bap_unicast_group;

struct bt_bap_ep;

struct bt_bap_bass_subgroup {
        uint32_t bis_sync;

        uint8_t metadata_len;

#if defined(CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE) || defined(__DOXYGEN__)
        uint8_t metadata[CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE];
#endif /* CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE */
};

struct bt_bap_scan_delegator_recv_state {
        uint8_t src_id;

        bt_addr_le_t addr;

        uint8_t adv_sid;

        enum bt_bap_pa_state pa_sync_state;

        enum bt_bap_big_enc_state encrypt_state;

        uint32_t broadcast_id;

        uint8_t bad_code[BT_ISO_BROADCAST_CODE_SIZE];

        uint8_t num_subgroups;

        struct bt_bap_bass_subgroup subgroups[BT_BAP_BASS_MAX_SUBGROUPS];
};

struct bt_bap_scan_delegator_cb {
        void (*recv_state_updated)(struct bt_conn *conn,
                                   const struct bt_bap_scan_delegator_recv_state *recv_state);

        int (*pa_sync_req)(struct bt_conn *conn,
                           const struct bt_bap_scan_delegator_recv_state *recv_state,
                           bool past_avail, uint16_t pa_interval);

        int (*pa_sync_term_req)(struct bt_conn *conn,
                                const struct bt_bap_scan_delegator_recv_state *recv_state);

        void (*broadcast_code)(struct bt_conn *conn,
                               const struct bt_bap_scan_delegator_recv_state *recv_state,
                               const uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE]);
        int (*bis_sync_req)(struct bt_conn *conn,
                            const struct bt_bap_scan_delegator_recv_state *recv_state,
                            const uint32_t bis_sync_req[BT_BAP_BASS_MAX_SUBGROUPS]);
        void (*scanning_state)(struct bt_conn *conn, bool is_scanning);
        int (*add_source)(struct bt_conn *conn,
                          const struct bt_bap_scan_delegator_recv_state *recv_state);

        int (*modify_source)(struct bt_conn *conn,
                             const struct bt_bap_scan_delegator_recv_state *recv_state);

        int (*remove_source)(struct bt_conn *conn, uint8_t src_id);
};

struct bt_bap_ep_info {
        uint8_t id;

        enum bt_bap_ep_state state;

        enum bt_audio_dir dir;

        struct bt_iso_chan *iso_chan;

        bool can_send;

        bool can_recv;

        struct bt_bap_ep *paired_ep;

        const struct bt_bap_qos_cfg_pref *qos_pref;
};

int bt_bap_ep_get_info(const struct bt_bap_ep *ep, struct bt_bap_ep_info *info);

struct bt_conn *bt_bap_ep_get_conn(const struct bt_bap_ep *ep);

struct bt_bap_stream {
        struct bt_conn *conn;

        struct bt_bap_ep *ep;

        const struct bt_audio_codec_cfg *codec_cfg;

        const struct bt_bap_qos_cfg *qos;

        struct bt_bap_stream_ops *ops;

        void *user_data;

        struct bt_iso_chan *iso;

        void *group;

#if defined(CONFIG_BT_BAP_DEBUG_STREAM_SEQ_NUM) || defined(__DOXYGEN__)
        uint16_t _prev_seq_num;
#endif /* CONFIG_BT_BAP_DEBUG_STREAM_SEQ_NUM */

        sys_snode_t _node;
};

struct bt_bap_stream_ops {
#if defined(CONFIG_BT_BAP_UNICAST) || defined(__DOXYGEN__)
        void (*codec_configured)(struct bt_bap_stream *stream,
                                 const struct bt_bap_qos_cfg_pref *pref);

        void (*qos_configured)(struct bt_bap_stream *stream);

        void (*enabled)(struct bt_bap_stream *stream);

        void (*metadata_updated)(struct bt_bap_stream *stream);

        void (*disabled)(struct bt_bap_stream *stream);

        void (*released)(struct bt_bap_stream *stream);
#endif /* CONFIG_BT_BAP_UNICAST */

        void (*started)(struct bt_bap_stream *stream);

        void (*stopped)(struct bt_bap_stream *stream, uint8_t reason);

#if defined(CONFIG_BT_AUDIO_RX) || defined(__DOXYGEN__)
        void (*recv)(struct bt_bap_stream *stream, const struct bt_iso_recv_info *info,
                     struct net_buf *buf);
#endif /* CONFIG_BT_AUDIO_RX */

#if defined(CONFIG_BT_AUDIO_TX) || defined(__DOXYGEN__)
        void (*sent)(struct bt_bap_stream *stream);
#endif /* CONFIG_BT_AUDIO_TX */

        void (*connected)(struct bt_bap_stream *stream);

        void (*disconnected)(struct bt_bap_stream *stream, uint8_t reason);
};

struct bt_bap_unicast_server_register_param {
        uint8_t snk_cnt;

        uint8_t src_cnt;
};

void bt_bap_stream_cb_register(struct bt_bap_stream *stream, struct bt_bap_stream_ops *ops);

int bt_bap_stream_config(struct bt_conn *conn, struct bt_bap_stream *stream, struct bt_bap_ep *ep,
                         const struct bt_audio_codec_cfg *codec_cfg);

int bt_bap_stream_reconfig(struct bt_bap_stream *stream,
                           const struct bt_audio_codec_cfg *codec_cfg);

int bt_bap_stream_qos(struct bt_conn *conn, struct bt_bap_unicast_group *group);

int bt_bap_stream_enable(struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len);

int bt_bap_stream_metadata(struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len);

int bt_bap_stream_disable(struct bt_bap_stream *stream);

int bt_bap_stream_connect(struct bt_bap_stream *stream);

int bt_bap_stream_start(struct bt_bap_stream *stream);

int bt_bap_stream_stop(struct bt_bap_stream *stream);

int bt_bap_stream_release(struct bt_bap_stream *stream);

int bt_bap_stream_send(struct bt_bap_stream *stream, struct net_buf *buf, uint16_t seq_num);

int bt_bap_stream_send_ts(struct bt_bap_stream *stream, struct net_buf *buf, uint16_t seq_num,
                          uint32_t ts);

int bt_bap_stream_get_tx_sync(struct bt_bap_stream *stream, struct bt_iso_tx_info *info);


struct bt_bap_unicast_server_cb {
        int (*config)(struct bt_conn *conn, const struct bt_bap_ep *ep, enum bt_audio_dir dir,
                      const struct bt_audio_codec_cfg *codec_cfg, struct bt_bap_stream **stream,
                      struct bt_bap_qos_cfg_pref *const pref, struct bt_bap_ascs_rsp *rsp);

        int (*reconfig)(struct bt_bap_stream *stream, enum bt_audio_dir dir,
                        const struct bt_audio_codec_cfg *codec_cfg,
                        struct bt_bap_qos_cfg_pref *const pref, struct bt_bap_ascs_rsp *rsp);

        int (*qos)(struct bt_bap_stream *stream, const struct bt_bap_qos_cfg *qos,
                   struct bt_bap_ascs_rsp *rsp);

        int (*enable)(struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len,
                      struct bt_bap_ascs_rsp *rsp);

        int (*start)(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp);

        int (*metadata)(struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len,
                        struct bt_bap_ascs_rsp *rsp);

        int (*disable)(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp);

        int (*stop)(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp);

        int (*release)(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp);
};

int bt_bap_unicast_server_register(const struct bt_bap_unicast_server_register_param *param);

int bt_bap_unicast_server_unregister(void);

int bt_bap_unicast_server_register_cb(const struct bt_bap_unicast_server_cb *cb);

int bt_bap_unicast_server_unregister_cb(const struct bt_bap_unicast_server_cb *cb);

typedef bool (*bt_bap_ep_func_t)(struct bt_bap_ep *ep, void *user_data);

int bt_bap_unicast_server_foreach_ep(struct bt_conn *conn, bt_bap_ep_func_t func, void *user_data);

int bt_bap_unicast_server_config_ase(struct bt_conn *conn, struct bt_bap_stream *stream,
                                     const struct bt_audio_codec_cfg *codec_cfg,
                                     const struct bt_bap_qos_cfg_pref *qos_pref);
 /* End of group bt_bap_unicast_server */


struct bt_bap_unicast_group_stream_param {
        struct bt_bap_stream *stream;

        const struct bt_bap_qos_cfg *qos;
};

struct bt_bap_unicast_group_stream_pair_param {
        struct bt_bap_unicast_group_stream_param *rx_param;

        struct bt_bap_unicast_group_stream_param *tx_param;
};

struct bt_bap_unicast_group_param {
        size_t params_count;

        struct bt_bap_unicast_group_stream_pair_param *params;

        uint8_t packing;

#if defined(CONFIG_BT_ISO_TEST_PARAMS) || defined(__DOXYGEN__)
        uint8_t c_to_p_ft;

        uint8_t p_to_c_ft;

        uint16_t iso_interval;
#endif /* CONFIG_BT_ISO_TEST_PARAMS */
};

int bt_bap_unicast_group_create(struct bt_bap_unicast_group_param *param,
                                struct bt_bap_unicast_group **unicast_group);

int bt_bap_unicast_group_reconfig(struct bt_bap_unicast_group *unicast_group,
                                  const struct bt_bap_unicast_group_param *param);

int bt_bap_unicast_group_add_streams(struct bt_bap_unicast_group *unicast_group,
                                     struct bt_bap_unicast_group_stream_pair_param params[],
                                     size_t num_param);

int bt_bap_unicast_group_delete(struct bt_bap_unicast_group *unicast_group);

typedef bool (*bt_bap_unicast_group_foreach_stream_func_t)(struct bt_bap_stream *stream,
                                                           void *user_data);

int bt_bap_unicast_group_foreach_stream(struct bt_bap_unicast_group *unicast_group,
                                        bt_bap_unicast_group_foreach_stream_func_t func,
                                        void *user_data);

struct bt_bap_unicast_group_info {
        uint32_t sink_pd;

        uint32_t source_pd;

        uint32_t c_to_p_interval;

        uint32_t p_to_c_interval;

        uint16_t c_to_p_latency;

        uint16_t p_to_c_latency;

        enum bt_bap_qos_cfg_framing framing;

        uint8_t packing;

        bool has_been_connected;

#if defined(CONFIG_BT_ISO_TEST_PARAMS) || defined(__DOXYGEN__)
        uint8_t c_to_p_ft;

        uint8_t p_to_c_ft;

        uint16_t iso_interval;
#endif /* CONFIG_BT_ISO_TEST_PARAMS */
};

int bt_bap_unicast_group_get_info(const struct bt_bap_unicast_group *unicast_group,
                                  struct bt_bap_unicast_group_info *info);

struct bt_bap_unicast_client_cb {
        void (*location)(struct bt_conn *conn, enum bt_audio_dir dir, enum bt_audio_location loc);

        void (*supported_contexts)(struct bt_conn *conn, enum bt_audio_context snk_ctx,
                                   enum bt_audio_context src_ctx);

        void (*available_contexts)(struct bt_conn *conn, enum bt_audio_context snk_ctx,
                                   enum bt_audio_context src_ctx);

        void (*config)(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code,
                       enum bt_bap_ascs_reason reason);

        void (*qos)(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code,
                    enum bt_bap_ascs_reason reason);

        void (*enable)(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code,
                       enum bt_bap_ascs_reason reason);

        void (*start)(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code,
                      enum bt_bap_ascs_reason reason);

        void (*stop)(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code,
                     enum bt_bap_ascs_reason reason);

        void (*disable)(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code,
                        enum bt_bap_ascs_reason reason);

        void (*metadata)(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code,
                         enum bt_bap_ascs_reason reason);

        void (*release)(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code,
                        enum bt_bap_ascs_reason reason);

        void (*pac_record)(struct bt_conn *conn, enum bt_audio_dir dir,
                           const struct bt_audio_codec_cap *codec_cap);

        void (*endpoint)(struct bt_conn *conn, enum bt_audio_dir dir, struct bt_bap_ep *ep);

        void (*discover)(struct bt_conn *conn, int err, enum bt_audio_dir dir);

        sys_snode_t _node;
};

int bt_bap_unicast_client_register_cb(struct bt_bap_unicast_client_cb *cb);

int bt_bap_unicast_client_unregister_cb(struct bt_bap_unicast_client_cb *cb);

int bt_bap_unicast_client_discover(struct bt_conn *conn, enum bt_audio_dir dir);

int bt_bap_unicast_client_qos_from_group(const struct bt_bap_stream *stream,
                                         struct bt_bap_qos_cfg *qos);

bool bt_bap_qos_cfg_eq(const struct bt_bap_qos_cfg *a, const struct bt_bap_qos_cfg *b);
 /* End of group bt_bap_unicast_client */

struct bt_bap_base_subgroup;
struct bt_bap_base;

struct bt_bap_base_codec_id {
        uint8_t id;
        uint16_t cid;
        uint16_t vid;
};

struct bt_bap_base_subgroup_bis {
        uint8_t index;
        uint8_t data_len;
        uint8_t *data;
};

const struct bt_bap_base *bt_bap_base_get_base_from_ad(const struct bt_data *ad);

int bt_bap_base_get_size(const struct bt_bap_base *base);

int bt_bap_base_get_pres_delay(const struct bt_bap_base *base);

int bt_bap_base_get_subgroup_count(const struct bt_bap_base *base);

int bt_bap_base_get_bis_indexes(const struct bt_bap_base *base, uint32_t *bis_indexes);

int bt_bap_base_foreach_subgroup(const struct bt_bap_base *base,
                                 bool (*func)(const struct bt_bap_base_subgroup *subgroup,
                                              void *user_data),
                                 void *user_data);

int bt_bap_base_get_subgroup_codec_id(const struct bt_bap_base_subgroup *subgroup,
                                      struct bt_bap_base_codec_id *codec_id);

int bt_bap_base_get_subgroup_codec_data(const struct bt_bap_base_subgroup *subgroup,
                                        uint8_t **data);

int bt_bap_base_get_subgroup_codec_meta(const struct bt_bap_base_subgroup *subgroup,
                                        uint8_t **meta);

int bt_bap_base_subgroup_codec_to_codec_cfg(const struct bt_bap_base_subgroup *subgroup,
                                            struct bt_audio_codec_cfg *codec_cfg);

int bt_bap_base_get_subgroup_bis_count(const struct bt_bap_base_subgroup *subgroup);

int bt_bap_base_subgroup_get_bis_indexes(const struct bt_bap_base_subgroup *subgroup,
                                         uint32_t *bis_indexes);

int bt_bap_base_subgroup_foreach_bis(const struct bt_bap_base_subgroup *subgroup,
                                     bool (*func)(const struct bt_bap_base_subgroup_bis *bis,
                                                  void *user_data),
                                     void *user_data);

int bt_bap_base_subgroup_bis_codec_to_codec_cfg(const struct bt_bap_base_subgroup_bis *bis,
                                                struct bt_audio_codec_cfg *codec_cfg);
 /* End of group bt_bap_broadcast */


struct bt_bap_broadcast_source_cb {
        void (*started)(struct bt_bap_broadcast_source *source);

        void (*stopped)(struct bt_bap_broadcast_source *source, uint8_t reason);

        sys_snode_t _node;
};

int bt_bap_broadcast_source_register_cb(struct bt_bap_broadcast_source_cb *cb);

int bt_bap_broadcast_source_unregister_cb(struct bt_bap_broadcast_source_cb *cb);

struct bt_bap_broadcast_source_stream_param {
        struct bt_bap_stream *stream;

#if CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE > 0 || defined(__DOXYGEN__)
        size_t data_len;

        const uint8_t *data;
#endif /* CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE > 0 */
};

struct bt_bap_broadcast_source_subgroup_param {
        size_t params_count;

        struct bt_bap_broadcast_source_stream_param *params;

        const struct bt_audio_codec_cfg *codec_cfg;
};

struct bt_bap_broadcast_source_param {
        size_t params_count;

        struct bt_bap_broadcast_source_subgroup_param *params;

        const struct bt_bap_qos_cfg *qos;

        uint8_t packing;

        bool encryption;

        uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE];

#if defined(CONFIG_BT_ISO_TEST_PARAMS) || defined(__DOXYGEN__)
        uint8_t irc;

        uint8_t pto;

        uint16_t iso_interval;
#endif /* CONFIG_BT_ISO_TEST_PARAMS */
};

int bt_bap_broadcast_source_create(struct bt_bap_broadcast_source_param *param,
                                   struct bt_bap_broadcast_source **source);

int bt_bap_broadcast_source_reconfig(struct bt_bap_broadcast_source *source,
                                     struct bt_bap_broadcast_source_param *param);

int bt_bap_broadcast_source_update_metadata(struct bt_bap_broadcast_source *source,
                                            const uint8_t meta[], size_t meta_len);

int bt_bap_broadcast_source_start(struct bt_bap_broadcast_source *source,
                                  struct bt_le_ext_adv *adv);

int bt_bap_broadcast_source_stop(struct bt_bap_broadcast_source *source);

int bt_bap_broadcast_source_delete(struct bt_bap_broadcast_source *source);

int bt_bap_broadcast_source_get_base(struct bt_bap_broadcast_source *source,
                                     struct net_buf_simple *base_buf);

typedef bool (*bt_bap_broadcast_source_foreach_stream_func_t)(struct bt_bap_stream *stream,
                                                              void *user_data);

int bt_bap_broadcast_source_foreach_stream(struct bt_bap_broadcast_source *source,
                                           bt_bap_broadcast_source_foreach_stream_func_t func,
                                           void *user_data); /* End of bt_bap_broadcast_source */


struct bt_bap_broadcast_sink_cb {
        void (*base_recv)(struct bt_bap_broadcast_sink *sink, const struct bt_bap_base *base,
                          size_t base_size);

        void (*syncable)(struct bt_bap_broadcast_sink *sink, const struct bt_iso_biginfo *biginfo);

        void (*started)(struct bt_bap_broadcast_sink *sink);

        void (*stopped)(struct bt_bap_broadcast_sink *sink, uint8_t reason);

        sys_snode_t _node;
};

int bt_bap_broadcast_sink_register_cb(struct bt_bap_broadcast_sink_cb *cb);

int bt_bap_broadcast_sink_create(struct bt_le_per_adv_sync *pa_sync, uint32_t broadcast_id,
                                 struct bt_bap_broadcast_sink **sink);

int bt_bap_broadcast_sink_sync(struct bt_bap_broadcast_sink *sink, uint32_t indexes_bitfield,
                               struct bt_bap_stream *streams[],
                               const uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE]);

int bt_bap_broadcast_sink_stop(struct bt_bap_broadcast_sink *sink);

int bt_bap_broadcast_sink_delete(struct bt_bap_broadcast_sink *sink);
 /* End of group bt_bap_broadcast_sink */

int bt_bap_scan_delegator_register(struct bt_bap_scan_delegator_cb *cb);

int bt_bap_scan_delegator_unregister(void);

int bt_bap_scan_delegator_set_pa_state(uint8_t src_id,
                                       enum bt_bap_pa_state pa_state);

int bt_bap_scan_delegator_set_bis_sync_state(uint8_t src_id,
                                             uint32_t bis_synced[BT_BAP_BASS_MAX_SUBGROUPS]);

struct bt_bap_scan_delegator_add_src_param {
        bt_addr_le_t addr;

        uint8_t sid;

        enum bt_bap_pa_state pa_state;

        enum bt_bap_big_enc_state encrypt_state;

        uint32_t broadcast_id;

        uint8_t num_subgroups;

        struct bt_bap_bass_subgroup subgroups[BT_BAP_BASS_MAX_SUBGROUPS];
};

int bt_bap_scan_delegator_add_src(const struct bt_bap_scan_delegator_add_src_param *param);

struct bt_bap_scan_delegator_mod_src_param {
        uint8_t src_id;

        enum bt_bap_big_enc_state encrypt_state;

        uint32_t broadcast_id;

        uint8_t num_subgroups;

        struct bt_bap_bass_subgroup subgroups[BT_BAP_BASS_MAX_SUBGROUPS];
};

int bt_bap_scan_delegator_mod_src(const struct bt_bap_scan_delegator_mod_src_param *param);

int bt_bap_scan_delegator_rem_src(uint8_t src_id);

typedef bool (*bt_bap_scan_delegator_state_func_t)(
        const struct bt_bap_scan_delegator_recv_state *recv_state, void *user_data);

void bt_bap_scan_delegator_foreach_state(bt_bap_scan_delegator_state_func_t func,
                                         void *user_data);

const struct bt_bap_scan_delegator_recv_state *bt_bap_scan_delegator_find_state(
        bt_bap_scan_delegator_state_func_t func, void *user_data);

/******************************** CLIENT API ********************************/

typedef void (*bt_bap_broadcast_assistant_write_cb)(struct bt_conn *conn,
                                                    int err);

struct bt_bap_broadcast_assistant_cb {
        void (*discover)(struct bt_conn *conn, int err,
                         uint8_t recv_state_count);

        void (*scan)(const struct bt_le_scan_recv_info *info,
                     uint32_t broadcast_id);

        void (*recv_state)(struct bt_conn *conn, int err,
                           const struct bt_bap_scan_delegator_recv_state *state);

        void (*recv_state_removed)(struct bt_conn *conn, uint8_t src_id);

        void (*scan_start)(struct bt_conn *conn, int err);

        void (*scan_stop)(struct bt_conn *conn, int err);

        void (*add_src)(struct bt_conn *conn, int err);

        void (*mod_src)(struct bt_conn *conn, int err);

        void (*broadcast_code)(struct bt_conn *conn, int err);

        void (*rem_src)(struct bt_conn *conn, int err);

        sys_snode_t _node;
};

int bt_bap_broadcast_assistant_discover(struct bt_conn *conn);

int bt_bap_broadcast_assistant_scan_start(struct bt_conn *conn,
                                          bool start_scan);

int bt_bap_broadcast_assistant_scan_stop(struct bt_conn *conn);

int bt_bap_broadcast_assistant_register_cb(struct bt_bap_broadcast_assistant_cb *cb);

int bt_bap_broadcast_assistant_unregister_cb(struct bt_bap_broadcast_assistant_cb *cb);


struct bt_bap_broadcast_assistant_add_src_param {
        bt_addr_le_t addr;

        uint8_t adv_sid;

        bool pa_sync;

        uint32_t broadcast_id;

        uint16_t pa_interval;

        uint8_t num_subgroups;

        struct bt_bap_bass_subgroup *subgroups;
};

int bt_bap_broadcast_assistant_add_src(
        struct bt_conn *conn, const struct bt_bap_broadcast_assistant_add_src_param *param);

struct bt_bap_broadcast_assistant_mod_src_param {
        uint8_t src_id;

        bool pa_sync;

        uint16_t pa_interval;

        uint8_t num_subgroups;

        struct bt_bap_bass_subgroup *subgroups;
};

int bt_bap_broadcast_assistant_mod_src(
        struct bt_conn *conn, const struct bt_bap_broadcast_assistant_mod_src_param *param);

int bt_bap_broadcast_assistant_set_broadcast_code(
        struct bt_conn *conn, uint8_t src_id,
        const uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE]);

int bt_bap_broadcast_assistant_rem_src(struct bt_conn *conn, uint8_t src_id);

int bt_bap_broadcast_assistant_read_recv_state(struct bt_conn *conn, uint8_t idx);
 /* end of bt_bap */

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_BAP_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 55 行

类型（type）。

### 注释 2：原第 293 行

条件表达式：`CONFIG_BT_BAP_BROADCAST_SOURCE || CONFIG_BT_BAP_UNICAST`。

### 注释 3：原第 331 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_TEST_PARAMS`。

### 注释 4：原第 449 行

条件编译配置（Configuration）标记：`CONFIG_BT_AUDIO_CODEC_CFG_MAX_METADATA_SIZE`。

### 注释 5：原第 744 行

条件编译配置（Configuration）标记：`CONFIG_BT_BAP_DEBUG_STREAM_SEQ_NUM`。

### 注释 6：原第 814 行

条件编译配置（Configuration）标记：`CONFIG_BT_BAP_UNICAST`。

### 注释 7：原第 850 行

条件编译配置（Configuration）标记：`CONFIG_BT_AUDIO_RX`。

### 注释 8：原第 866 行

条件编译配置（Configuration）标记：`CONFIG_BT_AUDIO_TX`。

### 注释 9：原第 1402 行

`bt_bap_unicast_server` 分组结束。

### 注释 10：原第 1480 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_TEST_PARAMS`。

### 注释 11：原第 1661 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_TEST_PARAMS`。

### 注释 12：原第 1943 行

`bt_bap_unicast_client` 分组结束。

### 注释 13：原第 2146 行

`bt_bap_broadcast` 分组结束。

### 注释 14：原第 2220 行

条件表达式：`CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE > 0`。

### 注释 15：原第 2297 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_TEST_PARAMS`。

### 注释 16：原第 2436 行

`bt_bap_broadcast_source` 分组结束。

### 注释 17：原第 2580 行

`bt_bap_broadcast_sink` 分组结束。

### 注释 18：原第 2765 行

客户端 API（CLIENT API）分隔标题。

### 注释 19：原第 3097 行

`bt_bap` 分组结束。

### 注释 20：原第 3104 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_BAP_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [zephyr/bluetooth/audio/ascs.h](https://docs.zephyrproject.org/latest/doxygen/html/ascs_8h.html)
- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [zephyr/bluetooth/gap.h](https://docs.zephyrproject.org/latest/doxygen/html/gap_8h.html)
- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h.html)
- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [bt_bap_qos_cfg_framing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga37a5f9d7198739eef8bde6764da30de9)
- [BT_BAP_QOS_CFG_FRAMING_UNFRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga37a5f9d7198739eef8bde6764da30de9afe1ffd5db8e36f8082a2ef7545e04a94)
- [BT_BAP_QOS_CFG_FRAMING_FRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga37a5f9d7198739eef8bde6764da30de9a406ad3527d9d92e4e8b213fe52794298)
- [BT_BAP_QOS_CFG_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e8ebf4db88f94f44828bb6f41e81d44af5bc162fe51c445cb3c77bcf640bbe28)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_BAP_QOS_CFG_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147)
- [BT_BAP_QOS_CFG_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e8ebf4db88f94f44828bb6f41e81d44ab41e06fe31c57bb7dac5a77acb53be73)
- [bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pd](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#addf190fac00b2fb99c0d1abf13eb20b3)
- [framing](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#a60057a7812cdc5b26f839e68dc4603c4)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [phy](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#ac50ea51e1645546d8f8faa58c64672ce)
- [rtn](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#aaaa4a88499cfd1f90e409fa98891bf2c)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [sdu](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#a294709496f7779ee4cb7aa542da8832b)
- [latency](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#a912ee316aa2ddb00ebab7bb78af0f34a)
- [interval](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#abf8a1b76cc0735b9aec1962d2ce574ec)
- [max_pdu](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#acb84f2da73e865e38dcefa92007f01e1)
- [burst_number](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#a597b81261511ec820caa66bd091ab896)
- [num_subevents](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#a97094ac8254ff3e97790943a5c71cdf3)
- [bt_bap_pa_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac551e9b0d53fd50f3a9e9c08447f0296)
- [BT_BAP_PA_STATE_NOT_SYNCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf)
- [BT_BAP_PA_STATE_INFO_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb)
- [BT_BAP_PA_STATE_SYNCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc)
- [BT_BAP_PA_STATE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647)
- [BT_BAP_PA_STATE_NO_PAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d)
- [bt_bap_big_enc_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga5e0b0f70d247e131fa542fae16826a22)
- [BT_BAP_BIG_ENC_STATE_NO_ENC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4)
- [BT_BAP_BIG_ENC_STATE_BCODE_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2)
- [BT_BAP_BIG_ENC_STATE_DEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10)
- [BT_BAP_BIG_ENC_STATE_BAD_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b)
- [bt_bap_bass_att_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga13e9b6d571a613d689b8ba58bae64ae3)
- [BT_BAP_BASS_ERR_OPCODE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c)
- [BT_BAP_BASS_ERR_INVALID_SRC_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202)
- [bt_bap_ep_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf210a91e1ff11d9bf7792ba47d1e1b4a)
- [BT_BAP_EP_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961)
- [BT_BAP_EP_STATE_CODEC_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688)
- [BT_BAP_EP_STATE_QOS_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523)
- [BT_BAP_EP_STATE_ENABLING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332)
- [BT_BAP_EP_STATE_STREAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710)
- [BT_BAP_EP_STATE_DISABLING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8)
- [BT_BAP_EP_STATE_RELEASING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c)
- [bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)
- [bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)
- [bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)
- [bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)
- [bt_bap_bass_subgroup](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md)
- [bis_sync](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md#ac8061995eb73ba30e335e37714396ff5)
- [metadata_len](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md#ace1c1ff5d2f5cc79838653d468166664)
- [metadata](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md#a851fda16d0856714ebf4d3970c4d2e4b)
- [bt_bap_scan_delegator_recv_state](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md)
- [src_id](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#a1755a6332c86aeaf624d3c540037772a)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [addr](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#a6153ea6bbfe7057c39f6b652a4e6e34e)
- [adv_sid](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#aa03e02a1832950e4a53ff2fe803c14a6)
- [pa_sync_state](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#a30fbad06780fd7bca9aacdf14ecaf4a0)
- [encrypt_state](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#ac770a5ad001f73d3acaf2b36827f9343)
- [broadcast_id](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#abaa80f30cf2e84ee873d18eaedd4159d)
- [bad_code](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#a1c268bb7b340c874935f186c0ba2a253)
- [BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)
- [num_subgroups](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#aa97765bdbaa43a280645eb62c0035b82)
- [subgroups](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#a49030d5859dfc21e9a4478b6ed20994e)
- [BT_BAP_BASS_MAX_SUBGROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga443c212a736852305715452e7f165a9e)
- [bt_bap_scan_delegator_cb](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md)
- [recv_state_updated](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a5d95631d95ae1085071c9b795eca1a8e)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [pa_sync_req](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a0ea55963f92361f35e68eadcf10306b1)
- [pa_sync_term_req](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a5b918538cfe0edaa69155f891981eeae)
- [broadcast_code](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a78d011c817e60725a0ef14c68bd655cd)
- [bis_sync_req](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a92351aea994520cd08f87d3d579d6e3b)
- [scanning_state](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#ae41d499d75123a1b70b778e8e95edcc3)
- [add_source](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a1ca1642de4bcf3f6552d09761168b1fc)
- [modify_source](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#af862ad2d51d60e57cc50e20c256fde35)
- [remove_source](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a8da03993be622b5d25e8bd462dfd16c5)
- [bt_bap_ep_info](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md)
- [id](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#a07e8878e7e6a8ee059639330ffa78c1c)
- [state](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#a650727747d0a093528544c3e16255feb)
- [bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)
- [dir](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#abb0dc6d25744cd734f8fd6ba2bc84b24)
- [bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)
- [iso_chan](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#a54dd673e21455c85193df844f3aa4083)
- [can_send](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#abbad124bf9e40ed530b2a33fefbadc84)
- [can_recv](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#a30698c71f556ca876a1c69bffefac653)
- [paired_ep](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#a819ac77dcf7cb6985e97f290a666ed09)
- [bt_bap_qos_cfg_pref](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md)
- [qos_pref](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#ad5201e9b9623e8ff8e74e1be87ece864)
- [bt_bap_ep_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf15e5ec5bca364f6a3e7a43b1f27da68)
- [bt_bap_ep_get_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga575a109efb0fd1644634ce6e0288499b)
- [bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)
- [conn](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#adb95fe7a0b981a46898382ee45fd99df)
- [ep](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#af871d28b2cca8e4deba66997badbeca2)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [codec_cfg](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#a286b95d990433995a7ee74b7c3ec2f59)
- [qos](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#a503bd9d7e7f594d090bcbe7fc5e313fc)
- [bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)
- [ops](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#a46a1f70c1a1fe4696039be14adf3c9b6)
- [user_data](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#afe81620dd215aebe04ddc9e36dc7d2dd)
- [iso](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#a90e49f0d9abeabeff602e5409d8416e4)
- [group](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#a17d91a06d581cd4341d035eb76d8e0b2)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [codec_configured](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#afa90da66b69835c9df73068aa6373778)
- [qos_configured](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a23616f17ef90a03db2f78df180887897)
- [enabled](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a1c67137b439a87647994530710d9e075)
- [metadata_updated](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a553777c6b6bdda3e0e8c03f3915404cd)
- [disabled](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a3fc784b8a2a7c1a5b19dece3619c130e)
- [released](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a37876562731d7dbbcd5f5613621b78ca)
- [started](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a7f595e37d40b94510bf09c1f82b479f3)
- [stopped](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#ab50ea295069a2cd1ab6f4353052262f5)
- [recv](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a09f31dc30de9c880758ec4a1468e59f0)
- [bt_iso_recv_info](../bluetooth_connection_model_reference/P086_bt_iso_recv_info_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [sent](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a33b07c51394dea6d632f42aec89a1510)
- [connected](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a533d5ea96aa67b9b74b19c55afd43df1)
- [disconnected](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a953c7174297f1a27ceed012dced53c5a)
- [bt_bap_unicast_server_register_param](../bluetooth_le_audio_model_reference/P042_bt_bap_unicast_server_register_param_结构体.md)
- [snk_cnt](../bluetooth_le_audio_model_reference/P042_bt_bap_unicast_server_register_param_结构体.md#a88635d5926173f23f411402b5961f783)
- [src_cnt](../bluetooth_le_audio_model_reference/P042_bt_bap_unicast_server_register_param_结构体.md#ab4963c035d75404831ec1293c7f40f95)
- [bt_bap_stream_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gab29c1e134156dceaa6c67abae9239378)
- [bt_bap_stream_config](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaaecbb590e5d073829d4c150e4fd2d8aa)
- [bt_bap_stream_reconfig](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa7df3f6b906241ad5291295a6ddcf1e4)
- [bt_bap_stream_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac878ed89242cac9a8514e8e4f1da4d9d)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [bt_bap_stream_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga13a859b31b0310ec22339ec7ed0754f8)
- [bt_bap_stream_metadata](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0afe6c927729697e2f984cefcbc7c0f1)
- [bt_bap_stream_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0fd2bb35909fc19e3e9cff068ba9e9aa)
- [bt_bap_stream_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa75f2cd2c36fdaef04a62c95bec6e2e3)
- [bt_bap_stream_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga8f2dc67c35299334d21c7dee7b8664ae)
- [bt_bap_stream_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gada72bcd3951eff2bc6b70c02dcaed98b)
- [bt_bap_stream_release](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaaf94f1f0dda7ef356c0f9ae79b5c60e4)
- [bt_bap_stream_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga63b69967aa92224a2bd9cf79eb41773e)
- [bt_bap_stream_send_ts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa0e012446238c916abc84d6c0de89bf3)
- [bt_bap_stream_get_tx_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga47eb6219d730d75ddc4f49dceac7e928)
- [bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)
- [bt_bap_unicast_server_cb](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md)
- [config](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#ad179b35a5a5685edb8f0ac1b791d5271)
- [bt_bap_ascs_rsp](../bluetooth_le_audio_model_reference/P010_bt_bap_ascs_rsp_结构体.md)
- [reconfig](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a7bed12780fdf780227d38b61d76d099b)
- [qos](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a2d50b6c328607fc46d85eaf12633f13d)
- [enable](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a7424079675204fba02339ddc661b77c5)
- [start](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a48fb3021507a708a0847a1ebec6075ba)
- [metadata](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a5fe98295e41c426a12ab4a7875b665c8)
- [disable](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a22f1af95f055bce79e3810b9682024cf)
- [stop](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a932296643929403c11512ff4ee7f7879)
- [release](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a9f5169f0bcdb3a6560f0767ec117b3c6)
- [bt_bap_unicast_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html#gab3ea6014854e6290f058c87e866c3191)
- [bt_bap_unicast_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html#ga6ef3b9e877ffdc04cc48fda6713a0209)
- [bt_bap_unicast_server_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html#ga7669133936bc13f7ab38817db9ce69c0)
- [bt_bap_unicast_server_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html#gadf984f12bdeadcfc814dc2fc770cb7bf)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_bap_ep_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html#gabb2b96d8de285dff7cbade83768d9aff)
- [bt_bap_unicast_server_foreach_ep](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html#gafe7640d6269ec95c8af6d7549fac785d)
- [bt_bap_unicast_server_config_ase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html#ga98b170c9f371d7d60c3dde9aff3f6d6b)
- [bt_bap_unicast_group_stream_param](../bluetooth_le_audio_model_reference/P040_bt_bap_unicast_group_stream_param_结构体.md)
- [stream](../bluetooth_le_audio_model_reference/P040_bt_bap_unicast_group_stream_param_结构体.md#acfa192fed73b27fb194881f0021fcb35)
- [qos](../bluetooth_le_audio_model_reference/P040_bt_bap_unicast_group_stream_param_结构体.md#a8424dfd660759a6dd226f53413069a8a)
- [bt_bap_unicast_group_stream_pair_param](../bluetooth_le_audio_model_reference/P039_bt_bap_unicast_group_stream_pair_param_结构体.md)
- [rx_param](../bluetooth_le_audio_model_reference/P039_bt_bap_unicast_group_stream_pair_param_结构体.md#ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d)
- [tx_param](../bluetooth_le_audio_model_reference/P039_bt_bap_unicast_group_stream_pair_param_结构体.md#ae73a11aab16a60806d1a941306c1822a)
- [bt_bap_unicast_group_param](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md)
- [params_count](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md#a9cd09b720fa9a31364878ba205b3b58c)
- [params](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md#aefae7dfccdaed2bc3f59ca63689d4f2e)
- [packing](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md#a6829c82346ca70772a4ab0dc93fbb88f)
- [c_to_p_ft](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md#a7980c8e5c66a11507701ce2679b461ed)
- [p_to_c_ft](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md#a72e2c6dbeb7b7778f92af5cab2474a7e)
- [iso_interval](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md#a278797713b97a6520247b01caa2938b9)
- [bt_bap_unicast_group_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gaafd53b5f45d998b44e94a1b58e93ba21)
- [bt_bap_unicast_group_reconfig](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gacd684504c8127ff4f8d038cc06718e5e)
- [bt_bap_unicast_group_add_streams](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#ga9cc792cd1eaaa79d56f3df0e2341cbf6)
- [bt_bap_unicast_group_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#ga34dbdce6133f8366df453ec937fb47d2)
- [bt_bap_unicast_group_foreach_stream_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gaf0e5a38208e90176292e745933b5e29e)
- [bt_bap_unicast_group_foreach_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gad608ee07c8a50abf586a3bc31921f032)
- [bt_bap_unicast_group_info](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md)
- [sink_pd](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a74730a75337b985b7260297b1ecf8a21)
- [source_pd](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a05ecedc6350f6961d9794f854bf5be37)
- [c_to_p_interval](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#aa310b32478893830907878f59a65f876)
- [p_to_c_interval](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a70883292203e5f37f71238f0b659aa31)
- [c_to_p_latency](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a9c12fa3c837c300528dce41c8789e301)
- [p_to_c_latency](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a25208a4e06afd726c6f6f0714233526a)
- [framing](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a0cfbd31f735e4d18ac95f2e7d2a31f9a)
- [packing](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#ac701205d557f5cdb27663e2521082681)
- [has_been_connected](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a180fe8c6c0081da2f2cb38b3df0fadaf)
- [c_to_p_ft](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a1e49ada1c3a60ac73e29cc32f95a9533)
- [p_to_c_ft](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a15731dd811989ea465f2b2b490502db4)
- [iso_interval](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#aee9990d7b3a7e7c8230fb5f4eb7198b8)
- [bt_bap_unicast_group_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#ga4ba0e4c3fa7ec3a36a64a19c80027504)
- [bt_bap_unicast_client_cb](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md)
- [location](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a64546cd17ac346dcb4bbfad5bd9f9616)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [supported_contexts](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a814a5b22c3f75b7708dac5cfdb55292f)
- [bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)
- [available_contexts](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#ac49c3b8283552213623608498a7befd2)
- [config](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#ae5c31f2540eb39c5b8272b5ae1e867fd)
- [bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)
- [bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)
- [qos](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a23b82e9f4174bcc2130d6f4570990180)
- [enable](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a15dd1277b37dcd96a545bb6d450c2f9d)
- [start](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a5c2d9ec444699ae5c75736115aab0b71)
- [stop](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#abf8ec1b630220172887e3d3d4c550992)
- [disable](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a47f86af7675fcf6ac86fad578437afa9)
- [metadata](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a7b5fcba437b1532dbac796a48fee2f6a)
- [release](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a7dc1f2486bdabf37b85d0b347563e314)
- [pac_record](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a3c55f4e23607b1e655b5f520d691bf33)
- [bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)
- [endpoint](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#ae473ecc92b5c02a29742d0ba0c51ef4a)
- [discover](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a1f2f7476506b6b798c1f26371217956e)
- [bt_bap_unicast_client_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gade70f04ae1a828b43b3b44fa8933f674)
- [bt_bap_unicast_client_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gaee092a4e918a67bb5fd94cb78cc21141)
- [bt_bap_unicast_client_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gacef9c88f66762e8de19303d20dafa0bb)
- [bt_bap_unicast_client_qos_from_group](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gad963bdda290df96036a68b00cc940eca)
- [bt_bap_qos_cfg_eq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gad106ae43201100940d9145d291fe9ca3)
- [bt_bap_base_codec_id](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md)
- [id](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md#a9031aaf6a3f6e0acf68f1bfaed39b819)
- [cid](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md#a0aadd7e53f72efd8c0e33dd9a8eca177)
- [vid](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md#a49802819cc3129a993320b95472f2262)
- [bt_bap_base_subgroup_bis](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md)
- [index](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md#ad0f5dff3150c36b1625f1f6f206d41d2)
- [data_len](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md#ac4132c798c04c0f93c944dc91891221e)
- [data](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md#aa53f22b29e447822e8bb36d9245bfc77)
- [bt_bap_base_get_base_from_ad](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#ga29423a39d76ad16f0586d82a23c07ba7)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [bt_bap_base_get_size](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#ga539f92b71ec34f0551ef6240d83b972e)
- [bt_bap_base_get_pres_delay](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#gaf91f45bcf7df2f368c5abeb116b65dd0)
- [bt_bap_base_get_subgroup_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#gadcae0230168564da1ee8b3c577ce27d7)
- [bt_bap_base_get_bis_indexes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#ga6deab5a8b7a16ddf0c3685d4003694e1)
- [bt_bap_base_foreach_subgroup](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#ga5e6e0b758409cbdde93c0f648ef5e5e8)
- [bt_bap_base_get_subgroup_codec_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#gae75e05a002dee8336eb066ae8231ea0c)
- [bt_bap_base_get_subgroup_codec_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#ga10e2e32dc2802ba55d55c77148331f6a)
- [bt_bap_base_get_subgroup_codec_meta](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#gafb9d9544f38c7ad2613fff1679eb1f0c)
- [bt_bap_base_subgroup_codec_to_codec_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#ga920e3409f1978b803bcf6bc8d05ac8f6)
- [bt_bap_base_get_subgroup_bis_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#ga051e1f8aa2faf3ba7a973356138fd2d3)
- [bt_bap_base_subgroup_get_bis_indexes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#ga37df3bf1e18d2d8e9388541217b2e366)
- [bt_bap_base_subgroup_foreach_bis](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#ga4f85ee43984cb2f3139b41da7b9b1aee)
- [bt_bap_base_subgroup_bis_codec_to_codec_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html#gaa5cb191df7807ea87f1fba1871ca8ebe)
- [bt_bap_broadcast_source_cb](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md)
- [started](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md#a1108c983823ee3331d8343db4ec9c0c5)
- [stopped](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md#a66b62e90c1cdfa2c2963bafe99670f92)
- [bt_bap_broadcast_source_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#gac75ad00b8f9a1cd7048677a33b17acda)
- [bt_bap_broadcast_source_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#gacc8d26c42c6b4ae6dc11af84ec4af616)
- [bt_bap_broadcast_source_stream_param](../bluetooth_le_audio_model_reference/P022_bt_bap_broadcast_source_stream_param_结构体.md)
- [stream](../bluetooth_le_audio_model_reference/P022_bt_bap_broadcast_source_stream_param_结构体.md#a9c92fb50b62d963e01b1506b790fb5e1)
- [data_len](../bluetooth_le_audio_model_reference/P022_bt_bap_broadcast_source_stream_param_结构体.md#ac79a76ad748673ca4bd52c597cd073df)
- [data](../bluetooth_le_audio_model_reference/P022_bt_bap_broadcast_source_stream_param_结构体.md#aa1925bb8a770c05b34928d7220177ffa)
- [bt_bap_broadcast_source_subgroup_param](../bluetooth_le_audio_model_reference/P023_bt_bap_broadcast_source_subgroup_param_结构体.md)
- [params_count](../bluetooth_le_audio_model_reference/P023_bt_bap_broadcast_source_subgroup_param_结构体.md#a701d9480ffae2351149de6b962095d32)
- [params](../bluetooth_le_audio_model_reference/P023_bt_bap_broadcast_source_subgroup_param_结构体.md#a9719e89d8979f9502023e0032814c477)
- [codec_cfg](../bluetooth_le_audio_model_reference/P023_bt_bap_broadcast_source_subgroup_param_结构体.md#a4d5d610b562fc34c8840e4eed037ba86)
- [bt_bap_broadcast_source_param](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md)
- [params_count](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a5e155c3b92b4f9de3c9e6efa377097e3)
- [params](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a6291842b49a55f6b2767dc95c9e874f3)
- [qos](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a71abc0496153a9b8eab402bfaaf92e72)
- [packing](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a493fa57a80e21a288854b2e3e1df775a)
- [encryption](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a7552bf9a4ff5441b13669effe23abb8c)
- [broadcast_code](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a6a05b6448f55cf5f52f90e44d83146dc)
- [irc](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#aab1799ab671500b02c1ab0e023ac43f7)
- [pto](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a50c29b5a2bcae162c0bbda32102a30cc)
- [iso_interval](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a11b03e3d63ca2e116e743d9efde920be)
- [bt_bap_broadcast_source_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#gacdebfc435eebd47cf9cd05099a5f78e0)
- [bt_bap_broadcast_source_reconfig](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#gabecaa9db7be5cb03ed997ba478878d40)
- [bt_bap_broadcast_source_update_metadata](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#gaff2cfdadbff3ebe1e2efb660dee56f02)
- [bt_bap_broadcast_source_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#gac4640f5207599d51c1a63ff47f3c1d5a)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_bap_broadcast_source_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#ga36a885581eec5cab8b3f652db19b9aba)
- [bt_bap_broadcast_source_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#ga12e0a4856115a8eb297fe2d1fc130155)
- [bt_bap_broadcast_source_get_base](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#gafe07e4c6962858500fcf66415a173be8)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_bap_broadcast_source_foreach_stream_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#ga173ddb24e554afc1b16305cca69ad923)
- [bt_bap_broadcast_source_foreach_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#ga9d543b9282e0dadca3afe3a97e385b15)
- [bt_bap_broadcast_sink_cb](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md)
- [base_recv](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md#a1adf2124ec9a16c3c68774194febd0fc)
- [syncable](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md#a23390a63acbcf831a177a550d1012047)
- [bt_iso_biginfo](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md)
- [started](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md#a6af7aa849cebad26cdf382a1c97a681f)
- [stopped](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md#a1dd64d7c764ddd6c531bdd5b1890694f)
- [bt_bap_broadcast_sink_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html#ga1b83ead634d990e954f233d0208c5a85)
- [bt_bap_broadcast_sink_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html#ga0637d1957db70ad39e0608ed07e75166)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [bt_bap_broadcast_sink_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html#gacadebb5ce8aab5f5b8f1ff7e0fa57805)
- [bt_bap_broadcast_sink_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html#ga1020b21bfb4195aeb5823197145b1fe9)
- [bt_bap_broadcast_sink_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html#ga8b9d6cb409a3671654e053475ada3fda)
- [bt_bap_scan_delegator_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga7632ab444dbf99387871f7d0c90b11ba)
- [bt_bap_scan_delegator_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga6f52e58767303ded16cb6289f094895a)
- [bt_bap_scan_delegator_set_pa_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga381c1f3b386ecbdfd570eb125882161e)
- [bt_bap_scan_delegator_set_bis_sync_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf610cd6cddd52622f95cfd35b19ee841)
- [bt_bap_scan_delegator_add_src_param](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md)
- [addr](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#a751106648b8f040747b5ffb804932798)
- [sid](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#a80817dd3bc046d76baabd62e470ad797)
- [pa_state](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#a0945a707a9a50a152220463ba1678de0)
- [encrypt_state](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#a502d263982995c99559714f07d74443f)
- [broadcast_id](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#a8e8eda4139e460800c6195b4c5f246e2)
- [num_subgroups](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#a12bed26ffdc9d4683a5fcdf512a194eb)
- [subgroups](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#ac64d1608bede3b9fbac5f86488a3ac79)
- [bt_bap_scan_delegator_add_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga6eb2a782d761da12d112356cfe723ff0)
- [bt_bap_scan_delegator_mod_src_param](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md)
- [src_id](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md#ae387a2c0613545ae3acd372780f738bb)
- [encrypt_state](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md#aecc8b74632dcb2b17b9a358e00c75d31)
- [broadcast_id](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md#a11b4c6d787bd2c828e565282daf5cf2f)
- [num_subgroups](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md#aa8dcd7983005ffd23779db6b6ccfb752)
- [subgroups](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md#ab189593d0125cd443331bcb390d5502e)
- [bt_bap_scan_delegator_mod_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac022f38269742f16ff6887840ef5ba9a)
- [bt_bap_scan_delegator_rem_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga6c240f1cdb33945197700e4fe106ef2c)
- [bt_bap_scan_delegator_state_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf236a87ae461ad48ec59f487780b4824)
- [bt_bap_scan_delegator_foreach_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gab6f1a12699a9437c6575c70df33d5be0)
- [bt_bap_scan_delegator_find_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gabec9fd0a2966e1811fd4770855050510)
- [bt_bap_broadcast_assistant_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga496c8a2f599d997a7e6e033bda5f0c36)
- [bt_bap_broadcast_assistant_cb](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md)
- [discover](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#a01ad0a89db9041670f6a68d6f1680988)
- [scan](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#ab88d98b1e742ccd36aac69069ebf3f61)
- [bt_le_scan_recv_info](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md)
- [recv_state](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#a629ff4299b8ae5bcbddf28338caddfd0)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [recv_state_removed](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#af3fb53d95cdc7ba202657e4c54e0b2b8)
- [scan_start](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#ad2bdfcc0147a751910d82232a77e34f8)
- [scan_stop](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#a80296a38e664aabff7ec27e007c59e95)
- [add_src](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#ad909b9e6e3c35be10a29ee5a4b7213fb)
- [mod_src](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#ab24e3ecb9764ca833524b787126b8c2c)
- [broadcast_code](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#a09de9cb86dad76b485ff52257a0c68dc)
- [rem_src](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#af0cf259088cd793152390b21813a9481)
- [bt_bap_broadcast_assistant_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gab59c5ebc4fef28da34d8a54b1244c33b)
- [bt_bap_broadcast_assistant_scan_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga98ac067e66d263aa41fc6f8df6bb9126)
- [bt_bap_broadcast_assistant_scan_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga76cae35df980b78a10551811050b2760)
- [bt_bap_broadcast_assistant_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gabab24c44e9833029965475ad7b149e6e)
- [bt_bap_broadcast_assistant_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga679cdeb6e555bfc9ce20f38e493000ee)
- [bt_bap_broadcast_assistant_add_src_param](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md)
- [addr](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#a2b04d75ca9a740a7d819eae1bcc5cba7)
- [adv_sid](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#a390cd8d887cd256ee74b39b9b516cac4)
- [pa_sync](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#ad9af814e8a232230d4ee97c459f47747)
- [broadcast_id](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#ae50b6b5a3f2c92f01e7070c605b37dde)
- [pa_interval](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#acaecbbf7b3c96fe5ca53f90e92fa1e5e)
- [num_subgroups](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#a17b67d65b6840c3d4480027b7deb31a5)
- [subgroups](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#ab8423e5cce4a6c9ac142221d2e816763)
- [bt_bap_broadcast_assistant_add_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac93cb4cab33d0b937e752bc0b71cad9e)
- [bt_bap_broadcast_assistant_mod_src_param](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md)
- [src_id](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md#a5bc7c0a491872d655296bbb979402a62)
- [pa_sync](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md#a794bb68c8a73edfe3d44dbe9a0bf2830)
- [pa_interval](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md#aebaa104384dcbec7bb952a27f3acc24d)
- [num_subgroups](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md#a42b12c6d9f5c622433c9c1f0c72726c1)
- [subgroups](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md#a2383ec98b14054e0bc66bb4a0ae7b8b6)
- [bt_bap_broadcast_assistant_mod_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa9c292a7dcb470926d8d7d4be699a0c7)
- [bt_bap_broadcast_assistant_set_broadcast_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gabcec07689c13a996bcb9d2d417347dbb)
- [bt_bap_broadcast_assistant_rem_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga09785690db551677a043fcaa2fdb7f29)
- [bt_bap_broadcast_assistant_read_recv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga94fce2b4346b1026d53e0b860ca7fbf2)
- [addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [ascs.h](https://docs.zephyrproject.org/latest/doxygen/html/ascs_8h.html)
- [assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [gap.h](https://docs.zephyrproject.org/latest/doxygen/html/gap_8h.html)
- [iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_bap_base_codec_id::cid](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md#a0aadd7e53f72efd8c0e33dd9a8eca177)
- [bt_bap_base_codec_id::vid](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md#a49802819cc3129a993320b95472f2262)
- [bt_bap_base_codec_id::id](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md#a9031aaf6a3f6e0acf68f1bfaed39b819)
- [bt_bap_base_subgroup_bis::data](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md#aa53f22b29e447822e8bb36d9245bfc77)
- [bt_bap_base_subgroup_bis::data_len](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md#ac4132c798c04c0f93c944dc91891221e)
- [bt_bap_base_subgroup_bis::index](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md#ad0f5dff3150c36b1625f1f6f206d41d2)
- [bt_bap_bass_subgroup::metadata](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md#a851fda16d0856714ebf4d3970c4d2e4b)
- [bt_bap_bass_subgroup::bis_sync](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md#ac8061995eb73ba30e335e37714396ff5)
- [bt_bap_bass_subgroup::metadata_len](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md#ace1c1ff5d2f5cc79838653d468166664)
- [bt_bap_broadcast_assistant_add_src_param::num_subgroups](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#a17b67d65b6840c3d4480027b7deb31a5)
- [bt_bap_broadcast_assistant_add_src_param::addr](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#a2b04d75ca9a740a7d819eae1bcc5cba7)
- [bt_bap_broadcast_assistant_add_src_param::adv_sid](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#a390cd8d887cd256ee74b39b9b516cac4)
- [bt_bap_broadcast_assistant_add_src_param::subgroups](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#ab8423e5cce4a6c9ac142221d2e816763)
- [bt_bap_broadcast_assistant_add_src_param::pa_interval](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#acaecbbf7b3c96fe5ca53f90e92fa1e5e)
- [bt_bap_broadcast_assistant_add_src_param::pa_sync](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#ad9af814e8a232230d4ee97c459f47747)
- [bt_bap_broadcast_assistant_add_src_param::broadcast_id](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md#ae50b6b5a3f2c92f01e7070c605b37dde)
- [bt_bap_broadcast_assistant_cb::discover](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#a01ad0a89db9041670f6a68d6f1680988)
- [bt_bap_broadcast_assistant_cb::broadcast_code](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#a09de9cb86dad76b485ff52257a0c68dc)
- [bt_bap_broadcast_assistant_cb::recv_state](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#a629ff4299b8ae5bcbddf28338caddfd0)
- [bt_bap_broadcast_assistant_cb::scan_stop](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#a80296a38e664aabff7ec27e007c59e95)
- [bt_bap_broadcast_assistant_cb::mod_src](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#ab24e3ecb9764ca833524b787126b8c2c)
- [bt_bap_broadcast_assistant_cb::scan](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#ab88d98b1e742ccd36aac69069ebf3f61)
- [bt_bap_broadcast_assistant_cb::scan_start](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#ad2bdfcc0147a751910d82232a77e34f8)
- [bt_bap_broadcast_assistant_cb::add_src](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#ad909b9e6e3c35be10a29ee5a4b7213fb)
- [bt_bap_broadcast_assistant_cb::rem_src](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#af0cf259088cd793152390b21813a9481)
- [bt_bap_broadcast_assistant_cb::recv_state_removed](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md#af3fb53d95cdc7ba202657e4c54e0b2b8)
- [bt_bap_broadcast_assistant_mod_src_param::subgroups](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md#a2383ec98b14054e0bc66bb4a0ae7b8b6)
- [bt_bap_broadcast_assistant_mod_src_param::num_subgroups](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md#a42b12c6d9f5c622433c9c1f0c72726c1)
- [bt_bap_broadcast_assistant_mod_src_param::src_id](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md#a5bc7c0a491872d655296bbb979402a62)
- [bt_bap_broadcast_assistant_mod_src_param::pa_sync](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md#a794bb68c8a73edfe3d44dbe9a0bf2830)
- [bt_bap_broadcast_assistant_mod_src_param::pa_interval](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md#aebaa104384dcbec7bb952a27f3acc24d)
- [bt_bap_broadcast_sink_cb::base_recv](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md#a1adf2124ec9a16c3c68774194febd0fc)
- [bt_bap_broadcast_sink_cb::stopped](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md#a1dd64d7c764ddd6c531bdd5b1890694f)
- [bt_bap_broadcast_sink_cb::syncable](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md#a23390a63acbcf831a177a550d1012047)
- [bt_bap_broadcast_sink_cb::started](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md#a6af7aa849cebad26cdf382a1c97a681f)
- [bt_bap_broadcast_source_cb::started](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md#a1108c983823ee3331d8343db4ec9c0c5)
- [bt_bap_broadcast_source_cb::stopped](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md#a66b62e90c1cdfa2c2963bafe99670f92)
- [bt_bap_broadcast_source_param::iso_interval](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a11b03e3d63ca2e116e743d9efde920be)
- [bt_bap_broadcast_source_param::packing](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a493fa57a80e21a288854b2e3e1df775a)
- [bt_bap_broadcast_source_param::pto](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a50c29b5a2bcae162c0bbda32102a30cc)
- [bt_bap_broadcast_source_param::params_count](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a5e155c3b92b4f9de3c9e6efa377097e3)
- [bt_bap_broadcast_source_param::params](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a6291842b49a55f6b2767dc95c9e874f3)
- [bt_bap_broadcast_source_param::broadcast_code](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a6a05b6448f55cf5f52f90e44d83146dc)
- [bt_bap_broadcast_source_param::qos](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a71abc0496153a9b8eab402bfaaf92e72)
- [bt_bap_broadcast_source_param::encryption](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#a7552bf9a4ff5441b13669effe23abb8c)
- [bt_bap_broadcast_source_param::irc](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md#aab1799ab671500b02c1ab0e023ac43f7)
- [bt_bap_broadcast_source_stream_param::stream](../bluetooth_le_audio_model_reference/P022_bt_bap_broadcast_source_stream_param_结构体.md#a9c92fb50b62d963e01b1506b790fb5e1)
- [bt_bap_broadcast_source_stream_param::data](../bluetooth_le_audio_model_reference/P022_bt_bap_broadcast_source_stream_param_结构体.md#aa1925bb8a770c05b34928d7220177ffa)
- [bt_bap_broadcast_source_stream_param::data_len](../bluetooth_le_audio_model_reference/P022_bt_bap_broadcast_source_stream_param_结构体.md#ac79a76ad748673ca4bd52c597cd073df)
- [bt_bap_broadcast_source_subgroup_param::codec_cfg](../bluetooth_le_audio_model_reference/P023_bt_bap_broadcast_source_subgroup_param_结构体.md#a4d5d610b562fc34c8840e4eed037ba86)
- [bt_bap_broadcast_source_subgroup_param::params_count](../bluetooth_le_audio_model_reference/P023_bt_bap_broadcast_source_subgroup_param_结构体.md#a701d9480ffae2351149de6b962095d32)
- [bt_bap_broadcast_source_subgroup_param::params](../bluetooth_le_audio_model_reference/P023_bt_bap_broadcast_source_subgroup_param_结构体.md#a9719e89d8979f9502023e0032814c477)
- [bt_bap_ep_info::id](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#a07e8878e7e6a8ee059639330ffa78c1c)
- [bt_bap_ep_info::can_recv](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#a30698c71f556ca876a1c69bffefac653)
- [bt_bap_ep_info::iso_chan](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#a54dd673e21455c85193df844f3aa4083)
- [bt_bap_ep_info::state](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#a650727747d0a093528544c3e16255feb)
- [bt_bap_ep_info::paired_ep](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#a819ac77dcf7cb6985e97f290a666ed09)
- [bt_bap_ep_info::dir](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#abb0dc6d25744cd734f8fd6ba2bc84b24)
- [bt_bap_ep_info::can_send](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#abbad124bf9e40ed530b2a33fefbadc84)
- [bt_bap_ep_info::qos_pref](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md#ad5201e9b9623e8ff8e74e1be87ece864)
- [bt_bap_qos_cfg::sdu](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#a294709496f7779ee4cb7aa542da8832b)
- [bt_bap_qos_cfg::burst_number](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#a597b81261511ec820caa66bd091ab896)
- [bt_bap_qos_cfg::framing](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#a60057a7812cdc5b26f839e68dc4603c4)
- [bt_bap_qos_cfg::latency](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#a912ee316aa2ddb00ebab7bb78af0f34a)
- [bt_bap_qos_cfg::num_subevents](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#a97094ac8254ff3e97790943a5c71cdf3)
- [bt_bap_qos_cfg::rtn](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#aaaa4a88499cfd1f90e409fa98891bf2c)
- [bt_bap_qos_cfg::interval](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#abf8a1b76cc0735b9aec1962d2ce574ec)
- [bt_bap_qos_cfg::phy](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#ac50ea51e1645546d8f8faa58c64672ce)
- [bt_bap_qos_cfg::max_pdu](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#acb84f2da73e865e38dcefa92007f01e1)
- [bt_bap_qos_cfg::pd](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md#addf190fac00b2fb99c0d1abf13eb20b3)
- [bt_bap_scan_delegator_add_src_param::pa_state](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#a0945a707a9a50a152220463ba1678de0)
- [bt_bap_scan_delegator_add_src_param::num_subgroups](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#a12bed26ffdc9d4683a5fcdf512a194eb)
- [bt_bap_scan_delegator_add_src_param::encrypt_state](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#a502d263982995c99559714f07d74443f)
- [bt_bap_scan_delegator_add_src_param::addr](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#a751106648b8f040747b5ffb804932798)
- [bt_bap_scan_delegator_add_src_param::sid](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#a80817dd3bc046d76baabd62e470ad797)
- [bt_bap_scan_delegator_add_src_param::broadcast_id](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#a8e8eda4139e460800c6195b4c5f246e2)
- [bt_bap_scan_delegator_add_src_param::subgroups](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md#ac64d1608bede3b9fbac5f86488a3ac79)
- [bt_bap_scan_delegator_cb::pa_sync_req](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a0ea55963f92361f35e68eadcf10306b1)
- [bt_bap_scan_delegator_cb::add_source](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a1ca1642de4bcf3f6552d09761168b1fc)
- [bt_bap_scan_delegator_cb::pa_sync_term_req](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a5b918538cfe0edaa69155f891981eeae)
- [bt_bap_scan_delegator_cb::recv_state_updated](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a5d95631d95ae1085071c9b795eca1a8e)
- [bt_bap_scan_delegator_cb::broadcast_code](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a78d011c817e60725a0ef14c68bd655cd)
- [bt_bap_scan_delegator_cb::remove_source](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a8da03993be622b5d25e8bd462dfd16c5)
- [bt_bap_scan_delegator_cb::bis_sync_req](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a92351aea994520cd08f87d3d579d6e3b)
- [bt_bap_scan_delegator_cb::scanning_state](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#ae41d499d75123a1b70b778e8e95edcc3)
- [bt_bap_scan_delegator_cb::modify_source](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#af862ad2d51d60e57cc50e20c256fde35)
- [bt_bap_scan_delegator_mod_src_param::broadcast_id](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md#a11b4c6d787bd2c828e565282daf5cf2f)
- [bt_bap_scan_delegator_mod_src_param::num_subgroups](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md#aa8dcd7983005ffd23779db6b6ccfb752)
- [bt_bap_scan_delegator_mod_src_param::subgroups](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md#ab189593d0125cd443331bcb390d5502e)
- [bt_bap_scan_delegator_mod_src_param::src_id](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md#ae387a2c0613545ae3acd372780f738bb)
- [bt_bap_scan_delegator_mod_src_param::encrypt_state](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md#aecc8b74632dcb2b17b9a358e00c75d31)
- [bt_bap_scan_delegator_recv_state::src_id](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#a1755a6332c86aeaf624d3c540037772a)
- [bt_bap_scan_delegator_recv_state::bad_code](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#a1c268bb7b340c874935f186c0ba2a253)
- [bt_bap_scan_delegator_recv_state::pa_sync_state](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#a30fbad06780fd7bca9aacdf14ecaf4a0)
- [bt_bap_scan_delegator_recv_state::subgroups](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#a49030d5859dfc21e9a4478b6ed20994e)
- [bt_bap_scan_delegator_recv_state::addr](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#a6153ea6bbfe7057c39f6b652a4e6e34e)
- [bt_bap_scan_delegator_recv_state::adv_sid](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#aa03e02a1832950e4a53ff2fe803c14a6)
- [bt_bap_scan_delegator_recv_state::num_subgroups](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#aa97765bdbaa43a280645eb62c0035b82)
- [bt_bap_scan_delegator_recv_state::broadcast_id](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#abaa80f30cf2e84ee873d18eaedd4159d)
- [bt_bap_scan_delegator_recv_state::encrypt_state](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md#ac770a5ad001f73d3acaf2b36827f9343)
- [bt_bap_stream_ops::recv](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a09f31dc30de9c880758ec4a1468e59f0)
- [bt_bap_stream_ops::enabled](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a1c67137b439a87647994530710d9e075)
- [bt_bap_stream_ops::qos_configured](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a23616f17ef90a03db2f78df180887897)
- [bt_bap_stream_ops::sent](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a33b07c51394dea6d632f42aec89a1510)
- [bt_bap_stream_ops::released](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a37876562731d7dbbcd5f5613621b78ca)
- [bt_bap_stream_ops::disabled](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a3fc784b8a2a7c1a5b19dece3619c130e)
- [bt_bap_stream_ops::connected](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a533d5ea96aa67b9b74b19c55afd43df1)
- [bt_bap_stream_ops::metadata_updated](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a553777c6b6bdda3e0e8c03f3915404cd)
- [bt_bap_stream_ops::started](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a7f595e37d40b94510bf09c1f82b479f3)
- [bt_bap_stream_ops::disconnected](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a953c7174297f1a27ceed012dced53c5a)
- [bt_bap_stream_ops::stopped](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#ab50ea295069a2cd1ab6f4353052262f5)
- [bt_bap_stream_ops::codec_configured](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#afa90da66b69835c9df73068aa6373778)
- [bt_bap_stream::group](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#a17d91a06d581cd4341d035eb76d8e0b2)
- [bt_bap_stream::codec_cfg](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#a286b95d990433995a7ee74b7c3ec2f59)
- [bt_bap_stream::ops](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#a46a1f70c1a1fe4696039be14adf3c9b6)
- [bt_bap_stream::qos](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#a503bd9d7e7f594d090bcbe7fc5e313fc)
- [bt_bap_stream::iso](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#a90e49f0d9abeabeff602e5409d8416e4)
- [bt_bap_stream::conn](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#adb95fe7a0b981a46898382ee45fd99df)
- [bt_bap_stream::ep](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#af871d28b2cca8e4deba66997badbeca2)
- [bt_bap_stream::user_data](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md#afe81620dd215aebe04ddc9e36dc7d2dd)
- [bt_bap_unicast_client_cb::enable](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a15dd1277b37dcd96a545bb6d450c2f9d)
- [bt_bap_unicast_client_cb::discover](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a1f2f7476506b6b798c1f26371217956e)
- [bt_bap_unicast_client_cb::qos](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a23b82e9f4174bcc2130d6f4570990180)
- [bt_bap_unicast_client_cb::pac_record](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a3c55f4e23607b1e655b5f520d691bf33)
- [bt_bap_unicast_client_cb::disable](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a47f86af7675fcf6ac86fad578437afa9)
- [bt_bap_unicast_client_cb::start](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a5c2d9ec444699ae5c75736115aab0b71)
- [bt_bap_unicast_client_cb::location](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a64546cd17ac346dcb4bbfad5bd9f9616)
- [bt_bap_unicast_client_cb::metadata](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a7b5fcba437b1532dbac796a48fee2f6a)
- [bt_bap_unicast_client_cb::release](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a7dc1f2486bdabf37b85d0b347563e314)
- [bt_bap_unicast_client_cb::supported_contexts](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#a814a5b22c3f75b7708dac5cfdb55292f)
- [bt_bap_unicast_client_cb::stop](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#abf8ec1b630220172887e3d3d4c550992)
- [bt_bap_unicast_client_cb::available_contexts](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#ac49c3b8283552213623608498a7befd2)
- [bt_bap_unicast_client_cb::endpoint](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#ae473ecc92b5c02a29742d0ba0c51ef4a)
- [bt_bap_unicast_client_cb::config](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md#ae5c31f2540eb39c5b8272b5ae1e867fd)
- [bt_bap_unicast_group_info::source_pd](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a05ecedc6350f6961d9794f854bf5be37)
- [bt_bap_unicast_group_info::framing](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a0cfbd31f735e4d18ac95f2e7d2a31f9a)
- [bt_bap_unicast_group_info::p_to_c_ft](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a15731dd811989ea465f2b2b490502db4)
- [bt_bap_unicast_group_info::has_been_connected](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a180fe8c6c0081da2f2cb38b3df0fadaf)
- [bt_bap_unicast_group_info::c_to_p_ft](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a1e49ada1c3a60ac73e29cc32f95a9533)
- [bt_bap_unicast_group_info::p_to_c_latency](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a25208a4e06afd726c6f6f0714233526a)
- [bt_bap_unicast_group_info::p_to_c_interval](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a70883292203e5f37f71238f0b659aa31)
- [bt_bap_unicast_group_info::sink_pd](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a74730a75337b985b7260297b1ecf8a21)
- [bt_bap_unicast_group_info::c_to_p_latency](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#a9c12fa3c837c300528dce41c8789e301)
- [bt_bap_unicast_group_info::c_to_p_interval](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#aa310b32478893830907878f59a65f876)
- [bt_bap_unicast_group_info::packing](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#ac701205d557f5cdb27663e2521082681)
- [bt_bap_unicast_group_info::iso_interval](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md#aee9990d7b3a7e7c8230fb5f4eb7198b8)
- [bt_bap_unicast_group_param::iso_interval](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md#a278797713b97a6520247b01caa2938b9)
- [bt_bap_unicast_group_param::packing](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md#a6829c82346ca70772a4ab0dc93fbb88f)
- [bt_bap_unicast_group_param::p_to_c_ft](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md#a72e2c6dbeb7b7778f92af5cab2474a7e)
- [bt_bap_unicast_group_param::c_to_p_ft](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md#a7980c8e5c66a11507701ce2679b461ed)
- [bt_bap_unicast_group_param::params_count](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md#a9cd09b720fa9a31364878ba205b3b58c)
- [bt_bap_unicast_group_param::params](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md#aefae7dfccdaed2bc3f59ca63689d4f2e)
- [bt_bap_unicast_group_stream_pair_param::rx_param](../bluetooth_le_audio_model_reference/P039_bt_bap_unicast_group_stream_pair_param_结构体.md#ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d)
- [bt_bap_unicast_group_stream_pair_param::tx_param](../bluetooth_le_audio_model_reference/P039_bt_bap_unicast_group_stream_pair_param_结构体.md#ae73a11aab16a60806d1a941306c1822a)
- [bt_bap_unicast_group_stream_param::qos](../bluetooth_le_audio_model_reference/P040_bt_bap_unicast_group_stream_param_结构体.md#a8424dfd660759a6dd226f53413069a8a)
- [bt_bap_unicast_group_stream_param::stream](../bluetooth_le_audio_model_reference/P040_bt_bap_unicast_group_stream_param_结构体.md#acfa192fed73b27fb194881f0021fcb35)
- [bt_bap_unicast_server_cb::disable](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a22f1af95f055bce79e3810b9682024cf)
- [bt_bap_unicast_server_cb::qos](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a2d50b6c328607fc46d85eaf12633f13d)
- [bt_bap_unicast_server_cb::start](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a48fb3021507a708a0847a1ebec6075ba)
- [bt_bap_unicast_server_cb::metadata](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a5fe98295e41c426a12ab4a7875b665c8)
- [bt_bap_unicast_server_cb::enable](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a7424079675204fba02339ddc661b77c5)
- [bt_bap_unicast_server_cb::reconfig](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a7bed12780fdf780227d38b61d76d099b)
- [bt_bap_unicast_server_cb::stop](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a932296643929403c11512ff4ee7f7879)
- [bt_bap_unicast_server_cb::release](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#a9f5169f0bcdb3a6560f0767ec117b3c6)
- [bt_bap_unicast_server_cb::config](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md#ad179b35a5a5685edb8f0ac1b791d5271)
- [bt_bap_unicast_server_register_param::snk_cnt](../bluetooth_le_audio_model_reference/P042_bt_bap_unicast_server_register_param_结构体.md#a88635d5926173f23f411402b5961f783)
- [bt_bap_unicast_server_register_param::src_cnt](../bluetooth_le_audio_model_reference/P042_bt_bap_unicast_server_register_param_结构体.md#ab4963c035d75404831ec1293c7f40f95)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P002_avrcp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_bcm2836-l1.h_源码浏览.md)
