---
id: learning.zephyr-docs.api-source-packet-gnss-reference.page-5
title: net_ip.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_net\_ip.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)。

## 5.1\_原始可见代码（Source Code）

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
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00064"></a>
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
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="foldopen00089"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="foldopen00156"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="foldopen00180"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="foldopen00188"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="foldopen00195"></a>
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
<a id="foldopen00206"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="foldopen00229"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="foldopen00288"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="foldopen00295"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="foldopen00306"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="foldopen00314"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="foldopen00339"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="foldopen00352"></a>
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
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
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
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
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
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
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
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="foldopen00462"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00465"></a>
<a id="l00467"></a>
<a id="l00468"></a>
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
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00508"></a>
<a id="foldopen00510"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="foldopen00514"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00544"></a>
<a id="foldopen00546"></a>
<a id="l00546"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="foldopen00567"></a>
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
<a id="l00578"></a>
<a id="l00579"></a>
<a id="foldopen00581"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="foldopen00590"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="foldopen00598"></a>
<a id="l00598"></a>
<a id="l00600"></a>
<a id="l00602"></a>
<a id="l00604"></a>
<a id="l00606"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
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
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00662"></a>
<a id="l00664"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00673"></a>
<a id="l00675"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00691"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="l00694"></a>
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
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00718"></a>
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
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00744"></a>
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
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00769"></a>
<a id="l00774"></a>
<a id="foldopen00776"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="foldopen00787"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="foldopen00796"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="foldopen00805"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="foldopen00813"></a>
<a id="l00813"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="foldopen00824"></a>
<a id="l00824"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00841"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="foldopen00851"></a>
<a id="l00851"></a>
<a id="l00852"></a>
<a id="l00853"></a>
<a id="l00854"></a>
<a id="l00855"></a>
<a id="l00857"></a>
<a id="l00858"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00865"></a>
<a id="foldopen00873"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00879"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="l00882"></a>
<a id="l00884"></a>
<a id="foldopen00892"></a>
<a id="l00892"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="l00899"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00907"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="foldopen00920"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="l00922"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="foldopen00936"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="l00938"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="foldopen00950"></a>
<a id="l00950"></a>
<a id="l00951"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00955"></a>
<a id="l00956"></a>
<a id="l00957"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00961"></a>
<a id="l00962"></a>
<a id="l00963"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="l00966"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="l00970"></a>
<a id="l00971"></a>
<a id="l00972"></a>
<a id="l00973"></a>
<a id="l00974"></a>
<a id="l00975"></a>
<a id="l00976"></a>
<a id="l00977"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="foldopen00988"></a>
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
<a id="l00999"></a>
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
<a id="l01013"></a>
<a id="l01014"></a>
<a id="l01015"></a>
<a id="l01016"></a>
<a id="l01018"></a>
<a id="foldopen01026"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01032"></a>
<a id="l01033"></a>
<a id="l01034"></a>
<a id="l01035"></a>
<a id="l01037"></a>
<a id="foldopen01045"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01054"></a>
<a id="l01056"></a>
<a id="foldopen01064"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="l01066"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="l01073"></a>
<a id="l01075"></a>
<a id="foldopen01083"></a>
<a id="l01083"></a>
<a id="l01084"></a>
<a id="l01085"></a>
<a id="l01086"></a>
<a id="l01087"></a>
<a id="foldopen01097"></a>
<a id="l01097"></a>
<a id="l01098"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01101"></a>
<a id="l01102"></a>
<a id="l01103"></a>
<a id="l01104"></a>
<a id="l01105"></a>
<a id="l01106"></a>
<a id="l01107"></a>
<a id="l01108"></a>
<a id="l01109"></a>
<a id="l01110"></a>
<a id="l01111"></a>
<a id="l01112"></a>
<a id="l01113"></a>
<a id="l01114"></a>
<a id="l01115"></a>
<a id="foldopen01124"></a>
<a id="l01124"></a>
<a id="l01125"></a>
<a id="l01126"></a>
<a id="foldopen01133"></a>
<a id="l01133"></a>
<a id="l01134"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="foldopen01145"></a>
<a id="l01145"></a>
<a id="l01146"></a>
<a id="l01147"></a>
<a id="l01148"></a>
<a id="l01149"></a>
<a id="l01150"></a>
<a id="foldopen01159"></a>
<a id="l01159"></a>
<a id="l01160"></a>
<a id="l01161"></a>
<a id="l01162"></a>
<a id="l01163"></a>
<a id="l01164"></a>
<a id="foldopen01173"></a>
<a id="l01173"></a>
<a id="l01174"></a>
<a id="l01175"></a>
<a id="l01176"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="foldopen01187"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="l01191"></a>
<a id="l01192"></a>
<a id="foldopen01201"></a>
<a id="l01201"></a>
<a id="l01202"></a>
<a id="l01203"></a>
<a id="l01204"></a>
<a id="l01205"></a>
<a id="l01206"></a>
<a id="l01207"></a>
<a id="l01209"></a>
<a id="l01210"></a>
<a id="l01211"></a>
<a id="l01212"></a>
<a id="l01214"></a>
<a id="foldopen01222"></a>
<a id="l01222"></a>
<a id="l01223"></a>
<a id="l01224"></a>
<a id="l01225"></a>
<a id="l01226"></a>
<a id="foldopen01234"></a>
<a id="l01234"></a>
<a id="l01235"></a>
<a id="l01236"></a>
<a id="l01237"></a>
<a id="l01238"></a>
<a id="l01239"></a>
<a id="foldopen01247"></a>
<a id="l01247"></a>
<a id="l01248"></a>
<a id="l01249"></a>
<a id="l01250"></a>
<a id="l01251"></a>
<a id="foldopen01259"></a>
<a id="l01259"></a>
<a id="l01260"></a>
<a id="l01261"></a>
<a id="l01262"></a>
<a id="l01263"></a>
<a id="foldopen01273"></a>
<a id="l01273"></a>
<a id="l01274"></a>
<a id="l01275"></a>
<a id="l01276"></a>
<a id="l01277"></a>
<a id="l01278"></a>
<a id="l01279"></a>
<a id="l01280"></a>
<a id="l01281"></a>
<a id="l01282"></a>
<a id="l01283"></a>
<a id="l01289"></a>
<a id="l01290"></a>
<a id="l01296"></a>
<a id="l01297"></a>
<a id="l01303"></a>
<a id="l01304"></a>
<a id="l01305"></a>
<a id="l01306"></a>
<a id="l01307"></a>
<a id="l01308"></a>
<a id="foldopen01318"></a>
<a id="l01318"></a>
<a id="l01319"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="l01322"></a>
<a id="l01323"></a>
<a id="l01325"></a>
<a id="l01326"></a>
<a id="l01327"></a>
<a id="l01328"></a>
<a id="l01329"></a>
<a id="l01330"></a>
<a id="l01331"></a>
<a id="l01332"></a>
<a id="l01333"></a>
<a id="l01334"></a>
<a id="l01335"></a>
<a id="l01336"></a>
<a id="l01337"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="l01340"></a>
<a id="l01341"></a>
<a id="l01342"></a>
<a id="l01343"></a>
<a id="l01344"></a>
<a id="l01345"></a>
<a id="l01346"></a>
<a id="l01347"></a>
<a id="l01349"></a>
<a id="l01350"></a>
<a id="l01351"></a>
<a id="l01352"></a>
<a id="l01361"></a>
<a id="l01362"></a>
<a id="l01363"></a>
<a id="l01364"></a>
<a id="l01365"></a>
<a id="l01366"></a>
<a id="l01367"></a>
<a id="l01368"></a>
<a id="l01369"></a>
<a id="l01370"></a>
<a id="l01371"></a>
<a id="foldopen01372"></a>
<a id="l01372"></a>
<a id="l01373"></a>
<a id="l01374"></a>
<a id="l01375"></a>
<a id="l01376"></a>
<a id="l01377"></a>
<a id="l01378"></a>
<a id="l01379"></a>
<a id="l01380"></a>
<a id="l01381"></a>
<a id="l01383"></a>
<a id="l01384"></a>
<a id="l01385"></a>
<a id="l01386"></a>
<a id="l01387"></a>
<a id="l01388"></a>
<a id="l01389"></a>
<a id="l01390"></a>
<a id="l01391"></a>
<a id="l01392"></a>
<a id="l01393"></a>
<a id="l01394"></a>
<a id="l01395"></a>
<a id="l01396"></a>
<a id="l01398"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="foldopen01411"></a>
<a id="l01411"></a>
<a id="l01412"></a>
<a id="l01413"></a>
<a id="l01414"></a>
<a id="l01415"></a>
<a id="l01416"></a>
<a id="l01417"></a>
<a id="l01418"></a>
<a id="l01419"></a>
<a id="l01420"></a>
<a id="l01421"></a>
<a id="l01422"></a>
<a id="l01424"></a>
<a id="l01425"></a>
<a id="l01426"></a>
<a id="l01427"></a>
<a id="l01428"></a>
<a id="l01429"></a>
<a id="l01430"></a>
<a id="l01432"></a>
<a id="foldopen01440"></a>
<a id="l01440"></a>
<a id="l01441"></a>
<a id="l01442"></a>
<a id="l01443"></a>
<a id="l01444"></a>
<a id="l01446"></a>
<a id="l01447"></a>
<a id="l01448"></a>
<a id="l01449"></a>
<a id="l01450"></a>
<a id="l01451"></a>
<a id="l01452"></a>
<a id="l01453"></a>
<a id="l01455"></a>
<a id="foldopen01464"></a>
<a id="l01464"></a>
<a id="l01465"></a>
<a id="l01466"></a>
<a id="l01467"></a>
<a id="l01468"></a>
<a id="l01470"></a>
<a id="l01471"></a>
<a id="l01472"></a>
<a id="l01473"></a>
<a id="l01474"></a>
<a id="l01476"></a>
<a id="l01478"></a>
<a id="l01479"></a>
<a id="l01480"></a>
<a id="l01481"></a>
<a id="l01482"></a>
<a id="l01483"></a>
<a id="l01484"></a>
<a id="l01485"></a>
<a id="l01487"></a>
<a id="foldopen01498"></a>
<a id="l01498"></a>
<a id="l01499"></a>
<a id="l01500"></a>
<a id="l01501"></a>
<a id="l01502"></a>
<a id="l01503"></a>
<a id="foldopen01513"></a>
<a id="l01513"></a>
<a id="l01514"></a>
<a id="l01515"></a>
<a id="l01516"></a>
<a id="l01517"></a>
<a id="l01518"></a>
<a id="l01519"></a>
<a id="foldopen01527"></a>
<a id="l01527"></a>
<a id="l01528"></a>
<a id="l01529"></a>
<a id="l01530"></a>
<a id="l01531"></a>
<a id="l01533"></a>
<a id="l01534"></a>
<a id="l01535"></a>
<a id="l01536"></a>
<a id="l01537"></a>
<a id="l01538"></a>
<a id="l01539"></a>
<a id="l01540"></a>
<a id="l01541"></a>
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
<a id="l01554"></a>
<a id="l01555"></a>
<a id="l01556"></a>
<a id="l01558"></a>
<a id="foldopen01566"></a>
<a id="l01566"></a>
<a id="l01567"></a>
<a id="l01568"></a>
<a id="l01569"></a>
<a id="l01570"></a>
<a id="foldopen01580"></a>
<a id="l01580"></a>
<a id="l01581"></a>
<a id="l01582"></a>
<a id="l01583"></a>
<a id="l01584"></a>
<a id="foldopen01594"></a>
<a id="l01594"></a>
<a id="l01595"></a>
<a id="l01596"></a>
<a id="l01597"></a>
<a id="l01598"></a>
<a id="foldopen01608"></a>
<a id="l01608"></a>
<a id="l01609"></a>
<a id="l01610"></a>
<a id="l01611"></a>
<a id="l01612"></a>
<a id="foldopen01622"></a>
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
<a id="l01642"></a>
<a id="l01643"></a>
<a id="l01644"></a>
<a id="l01645"></a>
<a id="l01646"></a>
<a id="l01647"></a>
<a id="l01648"></a>
<a id="l01649"></a>
<a id="l01651"></a>
<a id="foldopen01662"></a>
<a id="l01662"></a>
<a id="l01663"></a>
<a id="l01664"></a>
<a id="l01665"></a>
<a id="l01666"></a>
<a id="l01667"></a>
<a id="l01669"></a>
<a id="l01670"></a>
<a id="l01671"></a>
<a id="l01672"></a>
<a id="l01673"></a>
<a id="l01674"></a>
<a id="l01675"></a>
<a id="l01676"></a>
<a id="l01677"></a>
<a id="l01679"></a>
<a id="l01688"></a>
<a id="foldopen01689"></a>
<a id="l01689"></a>
<a id="l01690"></a>
<a id="l01691"></a>
<a id="l01692"></a>
<a id="l01693"></a>
<a id="l01703"></a>
<a id="foldopen01704"></a>
<a id="l01704"></a>
<a id="l01705"></a>
<a id="l01706"></a>
<a id="l01707"></a>
<a id="l01708"></a>
<a id="l01709"></a>
<a id="l01711"></a>
<a id="l01712"></a>
<a id="l01713"></a>
<a id="l01714"></a>
<a id="l01715"></a>
<a id="l01717"></a>
<a id="l01727"></a>
<a id="foldopen01728"></a>
<a id="l01728"></a>
<a id="l01729"></a>
<a id="l01730"></a>
<a id="l01731"></a>
<a id="l01732"></a>
<a id="l01733"></a>
<a id="l01741"></a>
<a id="foldopen01742"></a>
<a id="l01742"></a>
<a id="l01743"></a>
<a id="l01744"></a>
<a id="l01745"></a>
<a id="l01746"></a>
<a id="l01747"></a>
<a id="l01748"></a>
<a id="l01749"></a>
<a id="l01750"></a>
<a id="l01751"></a>
<a id="l01752"></a>
<a id="l01753"></a>
<a id="l01754"></a>
<a id="l01755"></a>
<a id="l01756"></a>
<a id="l01757"></a>
<a id="foldopen01770"></a>
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
<a id="foldopen01791"></a>
<a id="l01791"></a>
<a id="l01792"></a>
<a id="l01793"></a>
<a id="l01794"></a>
<a id="l01795"></a>
<a id="foldopen01801"></a>
<a id="l01801"></a>
<a id="l01802"></a>
<a id="l01803"></a>
<a id="l01804"></a>
<a id="l01805"></a>
<a id="foldopen01812"></a>
<a id="l01812"></a>
<a id="l01813"></a>
<a id="l01814"></a>
<a id="l01815"></a>
<a id="l01816"></a>
<a id="l01817"></a>
<a id="l01818"></a>
<a id="l01819"></a>
<a id="foldopen01828"></a>
<a id="l01828"></a>
<a id="l01829"></a>
<a id="l01830"></a>
<a id="l01831"></a>
<a id="l01832"></a>
<a id="l01833"></a>
<a id="l01834"></a>
<a id="l01835"></a>
<a id="l01836"></a>
<a id="l01837"></a>
<a id="l01838"></a>
<a id="foldopen01847"></a>
<a id="l01847"></a>
<a id="l01848"></a>
<a id="l01849"></a>
<a id="l01850"></a>
<a id="l01851"></a>
<a id="l01852"></a>
<a id="l01871"></a>
<a id="l01872"></a>
<a id="l01873"></a>
<a id="l01874"></a>
<a id="l01875"></a>
<a id="l01876"></a>
<a id="l01877"></a>
<a id="foldopen01884"></a>
<a id="l01884"></a>
<a id="l01885"></a>
<a id="l01886"></a>
<a id="l01887"></a>
<a id="l01888"></a>
<a id="l01889"></a>
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
<a id="l01929"></a>
<a id="l01930"></a>
<a id="l01931"></a>
<a id="l01932"></a>
<a id="l01933"></a>
<a id="l01934"></a>
<a id="l01935"></a>
<a id="l01936"></a>
<a id="l01937"></a>
<a id="l01938"></a>
<a id="l01939"></a>
<a id="l01941"></a>
<a id="foldopen01947"></a>
<a id="l01947"></a>
<a id="l01948"></a>
<a id="l01949"></a>
<a id="l01950"></a>
<a id="l01951"></a>
<a id="l01952"></a>
<a id="l01953"></a>
<a id="l01954"></a>
<a id="l01955"></a>
<a id="l01956"></a>
<a id="foldopen01965"></a>
<a id="l01965"></a>
<a id="l01966"></a>
<a id="l01967"></a>
<a id="l01968"></a>
<a id="l01969"></a>
<a id="foldopen01978"></a>
<a id="l01978"></a>
<a id="l01979"></a>
<a id="l01980"></a>
<a id="l01981"></a>
<a id="l01982"></a>
<a id="foldopen01991"></a>
<a id="l01991"></a>
<a id="l01992"></a>
<a id="l01993"></a>
<a id="l01994"></a>
<a id="l01995"></a>
<a id="foldopen02004"></a>
<a id="l02004"></a>
<a id="l02005"></a>
<a id="l02006"></a>
<a id="l02007"></a>
<a id="l02008"></a>
<a id="l02017"></a>
<a id="foldopen02018"></a>
<a id="l02018"></a>
<a id="l02019"></a>
<a id="l02020"></a>
<a id="l02021"></a>
<a id="l02022"></a>
<a id="l02031"></a>
<a id="foldopen02032"></a>
<a id="l02032"></a>
<a id="l02033"></a>
<a id="l02034"></a>
<a id="l02035"></a>
<a id="l02036"></a>
<a id="l02045"></a>
<a id="foldopen02046"></a>
<a id="l02046"></a>
<a id="l02047"></a>
<a id="l02048"></a>
<a id="l02049"></a>
<a id="l02050"></a>
<a id="l02059"></a>
<a id="foldopen02060"></a>
<a id="l02060"></a>
<a id="l02061"></a>
<a id="l02062"></a>
<a id="l02063"></a>
<a id="l02064"></a>
<a id="l02078"></a>
<a id="l02079"></a>
<a id="l02091"></a>
<a id="l02092"></a>
<a id="l02093"></a>
<a id="l02104"></a>
<a id="l02105"></a>
<a id="l02106"></a>
<a id="l02117"></a>
<a id="l02118"></a>
<a id="l02119"></a>
<a id="l02141"></a>
<a id="l02142"></a>
<a id="l02143"></a>
<a id="l02171"></a>
<a id="l02172"></a>
<a id="l02173"></a>
<a id="l02183"></a>
<a id="l02184"></a>
<a id="l02193"></a>
<a id="l02194"></a>
<a id="l02203"></a>
<a id="l02204"></a>
<a id="foldopen02213"></a>
<a id="l02213"></a>
<a id="l02214"></a>
<a id="l02215"></a>
<a id="l02216"></a>
<a id="l02217"></a>
<a id="l02218"></a>
<a id="l02219"></a>
<a id="l02220"></a>
<a id="l02221"></a>
<a id="l02222"></a>
<a id="l02223"></a>
<a id="l02224"></a>
<a id="l02225"></a>
<a id="l02226"></a>
<a id="l02227"></a>
<a id="l02228"></a>
<a id="l02229"></a>
<a id="l02230"></a>
<a id="l02231"></a>
<a id="l02232"></a>
<a id="l02233"></a>
<a id="l02234"></a>
<a id="l02235"></a>
<a id="l02236"></a>
<a id="l02237"></a>
<a id="l02238"></a>
<a id="l02239"></a>
<a id="l02240"></a>
<a id="l02241"></a>
<a id="l02242"></a>
<a id="l02243"></a>
<a id="l02244"></a>
<a id="l02245"></a>
<a id="l02246"></a>
<a id="l02247"></a>
<a id="foldopen02259"></a>
<a id="l02259"></a>
<a id="l02260"></a>
<a id="l02261"></a>
<a id="l02262"></a>
<a id="l02263"></a>
<a id="foldopen02274"></a>
<a id="l02274"></a>
<a id="l02275"></a>
<a id="l02276"></a>
<a id="l02277"></a>
<a id="l02278"></a>
<a id="l02290"></a>
<a id="l02291"></a>
<a id="l02300"></a>
<a id="l02301"></a>
<a id="l02310"></a>
<a id="l02311"></a>
<a id="foldopen02320"></a>
<a id="l02320"></a>
<a id="l02321"></a>
<a id="l02322"></a>
<a id="l02323"></a>
<a id="l02324"></a>
<a id="l02325"></a>
<a id="l02326"></a>
<a id="l02327"></a>
<a id="l02328"></a>
<a id="l02329"></a>
<a id="l02330"></a>
<a id="l02331"></a>
<a id="l02332"></a>
<a id="l02333"></a>
<a id="l02334"></a>
<a id="l02335"></a>
<a id="l02336"></a>
<a id="l02337"></a>
<a id="l02338"></a>
<a id="l02339"></a>
<a id="l02340"></a>
<a id="l02341"></a>
<a id="foldopen02349"></a>
<a id="l02349"></a>
<a id="l02350"></a>
<a id="l02351"></a>
<a id="l02352"></a>
<a id="l02353"></a>
<a id="l02354"></a>
<a id="l02363"></a>
<a id="l02364"></a>
<a id="foldopen02372"></a>
<a id="l02372"></a>
<a id="l02373"></a>
<a id="l02374"></a>
<a id="l02375"></a>
<a id="l02376"></a>
<a id="l02377"></a>
<a id="l02378"></a>
<a id="l02379"></a>
<a id="l02380"></a>
<a id="l02381"></a>
<a id="l02382"></a>
<a id="l02383"></a>
<a id="l02384"></a>
<a id="l02385"></a>
<a id="l02386"></a>
<a id="l02387"></a>
<a id="l02388"></a>
<a id="l02389"></a>
<a id="l02390"></a>
<a id="l02391"></a>
<a id="l02402"></a>
<a id="l02403"></a>
<a id="l02404"></a>
<a id="foldopen02405"></a>
<a id="l02405"></a>
<a id="l02406"></a>
<a id="l02407"></a>
<a id="l02408"></a>
<a id="l02409"></a>
<a id="l02410"></a>
<a id="l02411"></a>
<a id="l02412"></a>
<a id="l02413"></a>
<a id="l02414"></a>
<a id="l02422"></a>
<a id="l02423"></a>
<a id="l02424"></a>
<a id="foldopen02425"></a>
<a id="l02425"></a>
<a id="l02426"></a>
<a id="l02427"></a>
<a id="l02428"></a>
<a id="l02429"></a>
<a id="l02430"></a>
<a id="l02431"></a>
<a id="l02432"></a>
<a id="l02433"></a>
<a id="l02434"></a>
<a id="l02435"></a>
<a id="l02436"></a>
<a id="l02437"></a>
<a id="l02438"></a>
<a id="l02439"></a>
<a id="l02440"></a>
<a id="l02441"></a>
<a id="l02442"></a>
<a id="l02443"></a>
<a id="l02444"></a>
<a id="l02448"></a>
<a id="l02449"></a>
<a id="agroup__ip__4__6_html_ga090f4770cd630517b5391d36e3705e41"></a>
<a id="agroup__ip__4__6_html_ga096d280f0373e50c4d40fb1b3dac2b2c"></a>
<a id="agroup__ip__4__6_html_ga0b67ffabad5b8a10da72301681206b31"></a>
<a id="agroup__ip__4__6_html_ga0d22051f0ff5545b9b08e133804389f1"></a>
<a id="agroup__ip__4__6_html_ga10a82ea9ba9ca19f3b773bdd53c978e0"></a>
<a id="agroup__ip__4__6_html_ga13b4094cc06599c9af46e5e68e1c3bc3"></a>
<a id="agroup__ip__4__6_html_ga14bc7018e3dd7c3e320b44a077343ce4"></a>
<a id="agroup__ip__4__6_html_ga1695009388402938dcc2e49b526ebd1f"></a>
<a id="agroup__ip__4__6_html_ga19bff1dd7eb407e25842ce28e04b08d9"></a>
<a id="agroup__ip__4__6_html_ga1d87e71e47d20a815dfd6acedb27bb98"></a>
<a id="agroup__ip__4__6_html_ga1df641bd5978219a7da51ea25ea8ac2f"></a>
<a id="agroup__ip__4__6_html_ga1eefdabf590090be9f98bdf4a2f43bb4"></a>
<a id="agroup__ip__4__6_html_ga204eae0889a15f6369da607a705cb059"></a>
<a id="agroup__ip__4__6_html_ga209390ff940aa0f0746c3a4fd4e98806"></a>
<a id="agroup__ip__4__6_html_ga2716cdb6f85693d7c5a96446a7a41e03"></a>
<a id="agroup__ip__4__6_html_ga2a2c730105721706af1fddad5bf9be2e"></a>
<a id="agroup__ip__4__6_html_ga2a508682693ec99b8006a1a1026772ea"></a>
<a id="agroup__ip__4__6_html_ga2a9657d756c655322d960ef54f4b9ac4"></a>
<a id="agroup__ip__4__6_html_ga2f25895894c9a24467000118464a8ffe"></a>
<a id="agroup__ip__4__6_html_ga32e58fc83532ef57eeb6ff952f17288d"></a>
<a id="agroup__ip__4__6_html_ga32ffb42c62169ac9b34a0faa7c7ffd12"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="agroup__ip__4__6_html_ga3d471601814ad2f4c2f9e6fb91055067"></a>
<a id="agroup__ip__4__6_html_ga403e318543fe3707bc9773b9b646610a"></a>
<a id="agroup__ip__4__6_html_ga418a57b9f12205de21cbe83951e960bb"></a>
<a id="agroup__ip__4__6_html_ga4314c59af790e537e384e969c58fab9d"></a>
<a id="agroup__ip__4__6_html_ga43b6e313f5a938d688d3bc734a299408"></a>
<a id="agroup__ip__4__6_html_ga45774258112186b5989b974df934dff1"></a>
<a id="agroup__ip__4__6_html_ga45f18bd1ec2040f9f21b5aaf4ffe696d"></a>
<a id="agroup__ip__4__6_html_ga4837ff0eece26b00ae46ed7c16997a97"></a>
<a id="agroup__ip__4__6_html_ga4925e6f3734b8fc1d9cb1ca1a510b5f1"></a>
<a id="agroup__ip__4__6_html_ga49d57fb1fa9db8f5fb357daab9b5cc87"></a>
<a id="agroup__ip__4__6_html_ga4c35814a1f56101f96e790d0dc97925b"></a>
<a id="agroup__ip__4__6_html_ga4e7578614f7f0660c5a62d7746a3772c"></a>
<a id="agroup__ip__4__6_html_ga4e91a4298604a916731bf591acc7b326"></a>
<a id="agroup__ip__4__6_html_ga502492205736b373fa35c0524ba3d4e6"></a>
<a id="agroup__ip__4__6_html_ga53fb4ce0130fc8d665ddfd466d2a5eb8"></a>
<a id="agroup__ip__4__6_html_ga5aef9855e39e03a4ce2d6626040c8ae9"></a>
<a id="agroup__ip__4__6_html_ga5d9e16e8f439be6f94fb3f72de13bdac"></a>
<a id="agroup__ip__4__6_html_ga5e1650330284b6e295e5f714037b1d65"></a>
<a id="agroup__ip__4__6_html_ga62623cbb70b70c87c05ba25cfd4b06c0"></a>
<a id="agroup__ip__4__6_html_ga6379fc7d08ed2668ac917fd370a80ef1"></a>
<a id="agroup__ip__4__6_html_ga63f48d08fc2811198739ce20a72584df"></a>
<a id="agroup__ip__4__6_html_ga646cd9e85f7110bc45dc276bf8e31ef1"></a>
<a id="agroup__ip__4__6_html_ga6651e4feab1a236888e85049a9ef8066"></a>
<a id="agroup__ip__4__6_html_ga6704d86fb9962bdb6d27a41d4053bfc7"></a>
<a id="agroup__ip__4__6_html_ga677fe0c0ebe6bcdd6a7a7d7805841671"></a>
<a id="agroup__ip__4__6_html_ga6943b9d84c55709aaad323c1127a1949"></a>
<a id="agroup__ip__4__6_html_ga721da18d2a3cfd9b3a56e9efc9f6e58b"></a>
<a id="agroup__ip__4__6_html_ga744f26c0e560ba2b6682c40c27b53f62"></a>
<a id="agroup__ip__4__6_html_ga75ffcc08e621c2d47d1ae043fce2acad"></a>
<a id="agroup__ip__4__6_html_ga78436f11373210789ed9d5d640c6daf7"></a>
<a id="agroup__ip__4__6_html_ga7946673bd60ca80392d4440e23028f54"></a>
<a id="agroup__ip__4__6_html_ga7a207761e4879c140f48f93978cb2f0b"></a>
<a id="agroup__ip__4__6_html_ga7b3c41ae9b3962090d72c130a9fa61b1"></a>
<a id="agroup__ip__4__6_html_ga7fe843d70cbb04a6f4c022483346ad23"></a>
<a id="agroup__ip__4__6_html_ga8047c58777b659f8a8cdb2f24ca24355"></a>
<a id="agroup__ip__4__6_html_ga83d4270557a164eef75e1ae656470ef1"></a>
<a id="agroup__ip__4__6_html_ga84d11fc7badd399d2c164ed21baa87c9"></a>
<a id="agroup__ip__4__6_html_ga871cb575f79b9e53834c13bfc9e5bd82"></a>
<a id="agroup__ip__4__6_html_ga8846a826e8b69c01fc92239a596ca002"></a>
<a id="agroup__ip__4__6_html_ga88930e91e400b4eca0a9392288490268"></a>
<a id="agroup__ip__4__6_html_ga8b4cfadf1b284e52d6905ca88657b48a"></a>
<a id="agroup__ip__4__6_html_ga8b794f251cf8412c769ab415902a9f32"></a>
<a id="agroup__ip__4__6_html_ga8be77d043d4d1d29e0879b3b22274629"></a>
<a id="agroup__ip__4__6_html_ga9084b403ca6a591d24f975e669560b6c"></a>
<a id="agroup__ip__4__6_html_ga9086c7f94792f5af574b6eb14a6261b1"></a>
<a id="agroup__ip__4__6_html_ga919149bde5d0f1319ba60a9b8de1a1bc"></a>
<a id="agroup__ip__4__6_html_ga91b134a31f3e29889a11bd3da518c483"></a>
<a id="agroup__ip__4__6_html_ga929a6597b2a4669e42cb416a84fd568f"></a>
<a id="agroup__ip__4__6_html_ga9495dd7d6ef4a3251f0ba3a7508522d5"></a>
<a id="agroup__ip__4__6_html_ga9654007b0a3c4d033df1ec3d00bd26ee"></a>
<a id="agroup__ip__4__6_html_ga9af9b1750c2db50a170e1b694df24227"></a>
<a id="agroup__ip__4__6_html_ga9e7bf1c3503039c78f99f3deab277d4f"></a>
<a id="agroup__ip__4__6_html_gaa1f6ecf0788bac4ca943011f0ad87fb9"></a>
<a id="agroup__ip__4__6_html_gaa559a6315ce432c9bc180b14cafa978f"></a>
<a id="agroup__ip__4__6_html_gaa77b299f53e5535ac4c4bea1b6531a34"></a>
<a id="agroup__ip__4__6_html_gaaab4268707dbe08348b98fb028e7aa5c"></a>
<a id="agroup__ip__4__6_html_gaacd8f2ea7894a0abb7a3d43a1ef60c29"></a>
<a id="agroup__ip__4__6_html_gaaed285ea1b276ad90404957560f82c77"></a>
<a id="agroup__ip__4__6_html_gab1b5d776e0b10043c0538629ed4a5b8b"></a>
<a id="agroup__ip__4__6_html_gab2d4e2746a080ff0dfbb67a8e09c15b4"></a>
<a id="agroup__ip__4__6_html_gabc3691a9ff73dcadadf52ec740cb0e99"></a>
<a id="agroup__ip__4__6_html_gac01309e4ca866366921148fa9ef74b4f"></a>
<a id="agroup__ip__4__6_html_gac20bcc70c84cff88fa68e1ab583da35f"></a>
<a id="agroup__ip__4__6_html_gac2616b300be2e4b7ed7e0ddffa5234f1"></a>
<a id="agroup__ip__4__6_html_gac3bb5fb48ed95d43a7beb2e4f7c1c6d0"></a>
<a id="agroup__ip__4__6_html_gac53da21004b2bdc93b878da2ec4590bd"></a>
<a id="agroup__ip__4__6_html_gad072b3bf7bc05927fe27f5503a31f25c"></a>
<a id="agroup__ip__4__6_html_gad4ed43b91fbaa2844fa509c603fafae6"></a>
<a id="agroup__ip__4__6_html_gad520342d393f523c56a98fa618876b54"></a>
<a id="agroup__ip__4__6_html_gadce220ef01f6f329152e74f2143cbaa3"></a>
<a id="agroup__ip__4__6_html_gadf685d461f89090441348d2028082078"></a>
<a id="agroup__ip__4__6_html_gae1660acfdbf897afbc6119ae608e476f"></a>
<a id="agroup__ip__4__6_html_gae18466011462c20add53de2e01505b92"></a>
<a id="agroup__ip__4__6_html_gae20291eed240d648d0ef7e13822f925f"></a>
<a id="agroup__ip__4__6_html_gae20b3c01d1ee1fe7526b58eb4c0bf98c"></a>
<a id="agroup__ip__4__6_html_gae74c9ba7ff4addbce7f931bd6fa91fa0"></a>
<a id="agroup__ip__4__6_html_gae87ef466e77ded673ed7e593d3eddffd"></a>
<a id="agroup__ip__4__6_html_gae9ac492caeb14ab3796fcbb752c6d7f1"></a>
<a id="agroup__ip__4__6_html_gaec37f4f9d223e5be3c141ec1ae4ef288"></a>
<a id="agroup__ip__4__6_html_gaf06819bf427cc58be1229b27b373ca31"></a>
<a id="agroup__ip__4__6_html_gaf41e178ed45d6a483e240f939cd2f41d"></a>
<a id="agroup__ip__4__6_html_gaf731738fb1761208739976d767736f87"></a>
<a id="agroup__ip__4__6_html_gaf91b9c08e327589eb0fd33d5754743cf"></a>
<a id="agroup__ip__4__6_html_gaf92aa225bda78a3e016f6120b60c8885"></a>
<a id="agroup__ip__4__6_html_gafbc331616a5360c68804e8bc2f653cdd"></a>
<a id="agroup__ip__4__6_html_gafbe40461a645cf11fc8b3a07e1d9156e"></a>
<a id="agroup__ip__4__6_html_gafecee2d4a331dc85ad962b81a6303e41"></a>
<a id="agroup__ip__4__6_html_gaff4efbe342d50083aaf33c994d864fcd"></a>
<a id="agroup__ip__4__6_html_gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df"></a>
<a id="agroup__ip__4__6_html_gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9"></a>
<a id="agroup__ip__4__6_html_gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3"></a>
<a id="agroup__ip__4__6_html_gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a"></a>
<a id="agroup__ip__4__6_html_gga721da18d2a3cfd9b3a56e9efc9f6e58ba29ed7248420f90939300dffdd23bb07c"></a>
<a id="agroup__ip__4__6_html_gga721da18d2a3cfd9b3a56e9efc9f6e58ba3f7f371f1d1729ad514f976f68738e47"></a>
<a id="agroup__ip__4__6_html_gga721da18d2a3cfd9b3a56e9efc9f6e58ba5d6d30723e865cab7561cc8c963c3658"></a>
<a id="agroup__ip__4__6_html_gga721da18d2a3cfd9b3a56e9efc9f6e58ba9ac0cafee2ab1cb5f16780fa17da5b8f"></a>
<a id="agroup__ip__4__6_html_gga721da18d2a3cfd9b3a56e9efc9f6e58bab13ec8077bb568971e80f9869b8d0529"></a>
<a id="agroup__ip__4__6_html_gga721da18d2a3cfd9b3a56e9efc9f6e58bab8506c41543969d01e4aaaa49c0932ab"></a>
<a id="agroup__ip__4__6_html_gga721da18d2a3cfd9b3a56e9efc9f6e58baebb51afe0c7e1cfe37a330f6b0d72341"></a>
<a id="agroup__ip__4__6_html_gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1"></a>
<a id="agroup__ip__4__6_html_gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c"></a>
<a id="agroup__ip__4__6_html_ggaaab4268707dbe08348b98fb028e7aa5ca6f049fea24a6d2d5279e736ececf3c83"></a>
<a id="agroup__ip__4__6_html_ggaaab4268707dbe08348b98fb028e7aa5ca892feaa0f7556622a3491683e69b6ac2"></a>
<a id="agroup__ip__4__6_html_ggaaab4268707dbe08348b98fb028e7aa5caff1fd09b4fa81b8e0e8a73132c8fa3e4"></a>
<a id="agroup__ip__4__6_html_ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef"></a>
<a id="agroup__ip__4__6_html_ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05"></a>
<a id="agroup__ip__4__6_html_ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354"></a>
<a id="agroup__ip__4__6_html_ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a"></a>
<a id="agroup__ip__4__6_html_ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792"></a>
<a id="agroup__ip__4__6_html_ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce"></a>
<a id="agroup__ip__4__6_html_ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0"></a>
<a id="agroup__ip__4__6_html_ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b"></a>
<a id="agroup__ip__4__6_html_ggaf06819bf427cc58be1229b27b373ca31a0ecceb13b5404e0699fa368306aeda25"></a>
<a id="agroup__ip__4__6_html_ggaf06819bf427cc58be1229b27b373ca31a195a3c7b388ce05b61f64c9c9be9a092"></a>
<a id="agroup__ip__4__6_html_ggaf06819bf427cc58be1229b27b373ca31a2ac71d272f68c66ce42ac81de4891896"></a>
<a id="agroup__ip__4__6_html_ggaf06819bf427cc58be1229b27b373ca31a3a5c18feadc81db1bf688b83120feb5a"></a>
<a id="agroup__ip__4__6_html_ggaf06819bf427cc58be1229b27b373ca31a41d4bfab7d2a68dd7b707eb70ed88b41"></a>
<a id="agroup__ip__4__6_html_ggaf06819bf427cc58be1229b27b373ca31a4d7100f9fe0efb9e8ef6cb75e8c5ac97"></a>
<a id="agroup__ip__4__6_html_ggaf06819bf427cc58be1229b27b373ca31a6ea6f123682a20c7895fd867504ada89"></a>
<a id="agroup__ip__4__6_html_ggaf06819bf427cc58be1229b27b373ca31acc28399f823adaa247347ab125eb37f4"></a>
<a id="agroup__ip__4__6_html_ggaf06819bf427cc58be1229b27b373ca31ace713634caddd3efe8190dc0988b87a1"></a>
<a id="agroup__ip__4__6_html_ggaf06819bf427cc58be1229b27b373ca31aebe8a029d9f87fb41c5f11b6366c1692"></a>
<a id="agroup__ip__4__6_html_ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6"></a>
<a id="agroup__ip__4__6_html_ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4"></a>
<a id="agroup__ip__4__6_html_ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db"></a>
<a id="agroup__ip__4__6_html_ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e"></a>
<a id="agroup__ip__4__6_html_ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006"></a>
<a id="agroup__net__linkaddr_html_ga5680cf2ac9302bbee824148f36193b2b"></a>
<a id="agroup__net__linkaddr_html_gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="ain_8h_html_a73e57c1190f8731fb8b0217f929c4e1b"></a>
<a id="ain_8h_html_a75e4bdec5e6afb661e8cbae72452fde7"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="anet__compat_8h_html"></a>
<a id="anet__linkaddr_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astring_8h_html"></a>
<a id="astring_8h_html_a4137694174d4ca2fad886a1db355015c"></a>
<a id="astring_8h_html_ad8bfbfa1e4ad284ded921dd775735521"></a>
<a id="astring_8h_html_af0f01bffcd16daa9143f6014d10a25ad"></a>
<a id="astructgroup_html"></a>
<a id="astructnet__cmsghdr_html"></a>
<a id="astructnet__cmsghdr_html_a306a55e0b7ab30d6258c71e92566f727"></a>
<a id="astructnet__cmsghdr_html_a3f8abb9fbf85597c885ac045df9492b5"></a>
<a id="astructnet__cmsghdr_html_aa44e7136defe85d81bec20aa00cc6668"></a>
<a id="astructnet__cmsghdr_html_aee333d1c9f262de2135a9bed3bca1d98"></a>
<a id="astructnet__if__addr_html"></a>
<a id="astructnet__if__config_html"></a>
<a id="astructnet__if__mcast__addr_html"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__ifreq_html"></a>
<a id="astructnet__ifreq_html_ad3147844bf168ff8f19893e89e3d04dd"></a>
<a id="astructnet__in6__addr_html"></a>
<a id="astructnet__in6__addr_html_a18fb132bfd7ac8945a981b8bb76e83ed"></a>
<a id="astructnet__in6__addr_html_ac2d541ca17ee6fa482765014f447f41a"></a>
<a id="astructnet__in6__addr_html_adfee3135d20aa7b5252aab9b9803bcd7"></a>
<a id="astructnet__in6__pktinfo_html"></a>
<a id="astructnet__in6__pktinfo_html_a471aed9984659549af97a694685869a3"></a>
<a id="astructnet__in6__pktinfo_html_af16fc143121a3557d338f8476fb0d0dd"></a>
<a id="astructnet__in__addr_html"></a>
<a id="astructnet__in__addr_html_aac03b71ad3fbe365fa80a1f0a8b53cc5"></a>
<a id="astructnet__in__addr_html_ac8181820613973fc7d6b5db0e3e53abd"></a>
<a id="astructnet__in__addr_html_ad3ca9f01bd03dbe69617eae95743bfa4"></a>
<a id="astructnet__in__addr_html_adca8424f8e83574c7f7d57a2138e7b8c"></a>
<a id="astructnet__in__pktinfo_html"></a>
<a id="astructnet__in__pktinfo_html_a00e5cde6d36f127d2f0710c541038ca0"></a>
<a id="astructnet__in__pktinfo_html_a75c8fff8b98862aef9ceba341b9276fe"></a>
<a id="astructnet__in__pktinfo_html_ad1fb0298ae64454f28f7e4b6738bf7fe"></a>
<a id="astructnet__iovec_html"></a>
<a id="astructnet__iovec_html_a85bbdc499845cf65f24e485ffb4220b8"></a>
<a id="astructnet__iovec_html_a9d64976623638c5856ff0bb76e41fe73"></a>
<a id="astructnet__ip__mreq_html"></a>
<a id="astructnet__ip__mreq_html_a1bef08a9e287288095ae7589489bbbb8"></a>
<a id="astructnet__ip__mreq_html_a9c4f5c84afbfd49f20bef330ade6a88a"></a>
<a id="astructnet__ip__mreqn_html"></a>
<a id="astructnet__ip__mreqn_html_a3d89352335683bfcda267b47c591ba1f"></a>
<a id="astructnet__ip__mreqn_html_abb6dbf4f2aae8fe0e3fc4ec5b6d0fdf8"></a>
<a id="astructnet__ip__mreqn_html_ac0ac21d6427ca1654eefe6fb903c4d99"></a>
<a id="astructnet__ipv6__mreq_html"></a>
<a id="astructnet__ipv6__mreq_html_a17fd782a854df2a8c793aaec9892420d"></a>
<a id="astructnet__ipv6__mreq_html_a3903141b4b67e2dfc977b3fad38d24a8"></a>
<a id="astructnet__linger_html"></a>
<a id="astructnet__linger_html_a8e93ff6b67e724cb24de03c21c5f99af"></a>
<a id="astructnet__linger_html_a9dab7be2bea49133c219cdfb154e9fdf"></a>
<a id="astructnet__linkaddr_html"></a>
<a id="astructnet__linkaddr_html_a58de2645f8c7d31c97026f0bd5262881"></a>
<a id="astructnet__linkaddr_html_a5f5b4c3d353261d0fab8011aa09f00d7"></a>
<a id="astructnet__linkaddr_html_a7b2f8ebe68b557eb9cbb4c2f2ecd70e0"></a>
<a id="astructnet__msghdr_html"></a>
<a id="astructnet__msghdr_html_a0a07694671a1725d5ec8af16de3d6778"></a>
<a id="astructnet__msghdr_html_a1263d9b8942042b7cf21727f8312ff7d"></a>
<a id="astructnet__msghdr_html_a38ea33c4a18d07022b89129107b6ffa5"></a>
<a id="astructnet__msghdr_html_a66dcca1e90e25dabe949842873b6edc4"></a>
<a id="astructnet__msghdr_html_a6e12f22fc1750226e706e64529bb84bd"></a>
<a id="astructnet__msghdr_html_a8f46d780cccad65cc755fb71eacf52ea"></a>
<a id="astructnet__msghdr_html_adbadc26695f3646aae690721e99d558a"></a>
<a id="astructnet__packet__mreq_html"></a>
<a id="astructnet__packet__mreq_html_a0f775f8c4c00a0f6ffd5f14b82379133"></a>
<a id="astructnet__packet__mreq_html_a382435d63e1ffda9197ca3984629e31d"></a>
<a id="astructnet__packet__mreq_html_a5f4e8579b69cd082baa79ffa3f3ab77f"></a>
<a id="astructnet__packet__mreq_html_a87a230e77612ab9bd25b6d5d6021615c"></a>
<a id="astructnet__sockaddr__can_html"></a>
<a id="astructnet__sockaddr__can_html_a597d33def7c50f84f2b17c320b7ca6c5"></a>
<a id="astructnet__sockaddr__can_html_a7e25be69230e5887a8326e991ddba6e0"></a>
<a id="astructnet__sockaddr__in6_html"></a>
<a id="astructnet__sockaddr__in6_html_a0f3796809a828ca81f097cdbd9f923c5"></a>
<a id="astructnet__sockaddr__in6_html_a38d03d2142c103f21726389952d969b9"></a>
<a id="astructnet__sockaddr__in6_html_a7fd7828614ca34044d5e05f446e37683"></a>
<a id="astructnet__sockaddr__in6_html_abd547e6daf4a9dd86a5c8349c0b80b04"></a>
<a id="astructnet__sockaddr__in_html"></a>
<a id="astructnet__sockaddr__in_html_a099706d7572442b073f9efffe3df7000"></a>
<a id="astructnet__sockaddr__in_html_a3cd81a45a4c8bc3ab18247378aeee123"></a>
<a id="astructnet__sockaddr__in_html_a5acd06c9decdae8344c05d32b47746b1"></a>
<a id="astructnet__sockaddr__ll_html"></a>
<a id="astructnet__sockaddr__ll_html_a40552f91379790433041e2620d7800d7"></a>
<a id="astructnet__sockaddr__ll_html_a7dc05521a96c49b14dfbb178ab6ca14a"></a>
<a id="astructnet__sockaddr__ll_html_a8c7064a9685e009f179a2582af50c198"></a>
<a id="astructnet__sockaddr__ll_html_a917c8c2df6482ae6427ced625bc00555"></a>
<a id="astructnet__sockaddr__ll_html_ac575672a144a28f49b3e63ee157ec8c9"></a>
<a id="astructnet__sockaddr__ll_html_acee20fa52f5544b0675064ff7c8c08ed"></a>
<a id="astructnet__sockaddr__ll_html_aff9f7cf10eaceab03a9ce582c2d76fea"></a>
<a id="astructnet__sockaddr__nm_html"></a>
<a id="astructnet__sockaddr__nm_html_a62ab3cea810b51107cc92cf43b2de6d9"></a>
<a id="astructnet__sockaddr__nm_html_a78e154af8b9530de3b12743115c91792"></a>
<a id="astructnet__sockaddr__nm_html_ad2f9976b5c6e46f8969e83bbcefdbeb9"></a>
<a id="astructnet__sockaddr__nm_html_aeaef27e6db3cca162dfd66337ccb629b"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructnet__sockaddr_html_a5cf76ac4582ea3c90fc871a44656490a"></a>
<a id="astructnet__tuple_html"></a>
<a id="astructnet__tuple_html_a8f9a1aab3c3aedeead795ca6624d4d6d"></a>
<a id="astructnet__tuple_html_a9a1cd0dd55a9e866cb0e910120362b7e"></a>
<a id="astructnet__tuple_html_aa9eeba2c8e263afbf6368e04353d6014"></a>
<a id="astructnet__tuple_html_ab4c31093a23bc60d8dcf5b784e3fb39a"></a>
<a id="astructnet__tuple_html_af7004f8f8d74d49d6771393825612294"></a>
<a id="asys_2byteorder_8h_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c


/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_NET_IP_H_
#define ZEPHYR_INCLUDE_NET_NET_IP_H_


#include <string.h>
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/byteorder.h>
#include <zephyr/toolchain.h>

#include <zephyr/net/net_linkaddr.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Specifying VLAN tag here in order to avoid circular dependencies */
#define NET_VLAN_TAG_UNSPEC 0x0fff

/* Protocol families. */
#define NET_PF_UNSPEC   0
#define NET_PF_INET     1
#define NET_PF_INET6    2
#define NET_PF_PACKET   3
#define NET_PF_CAN      4
#define NET_PF_NET_MGMT 5
#define NET_PF_LOCAL    6
#define NET_PF_UNIX     NET_PF_LOCAL

/* Address families. */
#define NET_AF_UNSPEC      NET_PF_UNSPEC
#define NET_AF_INET        NET_PF_INET
#define NET_AF_INET6       NET_PF_INET6
#define NET_AF_PACKET      NET_PF_PACKET
#define NET_AF_CAN         NET_PF_CAN
#define NET_AF_NET_MGMT    NET_PF_NET_MGMT
#define NET_AF_LOCAL       NET_PF_LOCAL
#define NET_AF_UNIX        NET_PF_UNIX

enum net_ip_protocol {
        NET_IPPROTO_IP = 0,
        NET_IPPROTO_ICMP = 1,
        NET_IPPROTO_IGMP = 2,
        NET_IPPROTO_ETH_P_ALL = 3,
        NET_IPPROTO_IPIP = 4,
        NET_IPPROTO_TCP = 6,
        NET_IPPROTO_UDP = 17,
        NET_IPPROTO_IPV6 = 41,
        NET_IPPROTO_ICMPV6 = 58,
        NET_IPPROTO_RAW = 255,
};

enum net_ip_protocol_secure {
        NET_IPPROTO_TLS_1_0 = 256,
        NET_IPPROTO_TLS_1_1 = 257,
        NET_IPPROTO_TLS_1_2 = 258,
        NET_IPPROTO_TLS_1_3 = 259,
        NET_IPPROTO_DTLS_1_0 = 272,
        NET_IPPROTO_DTLS_1_2 = 273,
        NET_IPPROTO_QUIC = 511,
};

enum net_sock_type {
        NET_SOCK_STREAM = 1,
        NET_SOCK_DGRAM,
        NET_SOCK_RAW
};

#define net_ntohs(x) sys_be16_to_cpu(x)

#define net_ntohl(x) sys_be32_to_cpu(x)

#define net_ntohll(x) sys_be64_to_cpu(x)

#define net_htons(x) sys_cpu_to_be16(x)

#define net_htonl(x) sys_cpu_to_be32(x)

#define net_htonll(x) sys_cpu_to_be64(x)

struct net_in6_addr {
        union {
                uint8_t s6_addr[16];
                uint16_t s6_addr16[8];
                uint32_t s6_addr32[4];
        };
};

#define NET_IPV6_ADDR_SIZE 16

struct net_in_addr {
        union {
                uint8_t s4_addr[4];
                uint16_t s4_addr16[2];
                uint32_t s4_addr32[1];
                uint32_t s_addr;
        };
};

#define NET_IPV4_ADDR_SIZE 4

typedef unsigned short int net_sa_family_t;

typedef uint32_t net_socklen_t;

/*
 * Note that the sin_port and sin6_port are in network byte order
 * in various net_sockaddr* structs.
 */

struct net_sockaddr_in6 {
        net_sa_family_t         sin6_family;
        uint16_t                sin6_port;
        struct net_in6_addr     sin6_addr;
        uint8_t                 sin6_scope_id;
};

struct net_sockaddr_in {
        net_sa_family_t         sin_family;
        uint16_t                sin_port;
        struct net_in_addr      sin_addr;
};

struct net_sockaddr_ll {
        net_sa_family_t sll_family;
        uint16_t        sll_protocol;
        int             sll_ifindex;
        uint16_t        sll_hatype;
        uint8_t         sll_pkttype;
        uint8_t         sll_halen;
        uint8_t         sll_addr[8];
};

struct net_sockaddr_can {
        net_sa_family_t can_family;
        int             can_ifindex;
};

struct net_sockaddr_nm {
        net_sa_family_t nm_family;

        int nm_ifindex;

        uintptr_t nm_pid;

        uint64_t nm_mask;
};


struct net_sockaddr_in6_ptr {
        net_sa_family_t         sin6_family;
        uint16_t                sin6_port;
        struct net_in6_addr    *sin6_addr;
        uint8_t                 sin6_scope_id;
};

struct net_sockaddr_in_ptr {
        net_sa_family_t         sin_family;
        uint16_t                sin_port;
        struct net_in_addr     *sin_addr;
};

struct net_sockaddr_ll_ptr {
        net_sa_family_t sll_family;
        uint16_t        sll_protocol;
        int             sll_ifindex;
        uint16_t        sll_hatype;
        uint8_t         sll_pkttype;
        uint8_t         sll_halen;
        uint8_t        *sll_addr;
};

struct net_sockaddr_un_ptr {
        net_sa_family_t sun_family;
        char           *sun_path;
};

struct net_sockaddr_can_ptr {
        net_sa_family_t can_family;
        int             can_ifindex;
};


#if !defined(HAVE_IOVEC)
struct net_iovec {
        void  *iov_base;
        size_t iov_len;
};
#endif

struct net_msghdr {
        void             *msg_name;
        net_socklen_t     msg_namelen;
        struct net_iovec *msg_iov;
        size_t            msg_iovlen;
        void             *msg_control;
        size_t            msg_controllen;
        int               msg_flags;
};

struct net_cmsghdr {
        net_socklen_t cmsg_len;
        int           cmsg_level;
        int           cmsg_type;
        z_max_align_t cmsg_data[];
};

struct net_linger {
        int l_onoff;
        int l_linger;
};


/* Alignment for headers and data. These are arch specific but define
 * them here atm if not found already.
 */
#if !defined(NET_ALIGN_H)
#define NET_ALIGN_H(x) ROUND_UP(x, __alignof__(struct net_cmsghdr))
#endif
#if !defined(NET_ALIGN_D)
#define NET_ALIGN_D(x) ROUND_UP(x, __alignof__(z_max_align_t))
#endif


#if !defined(NET_CMSG_FIRSTHDR)
#define NET_CMSG_FIRSTHDR(msghdr)                                 \
        ((msghdr)->msg_controllen >= sizeof(struct net_cmsghdr) ? \
         (struct net_cmsghdr *)((msghdr)->msg_control) : NULL)
#endif

#if !defined(NET_CMSG_NXTHDR)
#define NET_CMSG_NXTHDR(msghdr, cmsg)                                    \
        (((cmsg) == NULL) ? NET_CMSG_FIRSTHDR(msghdr) :                  \
         (((cmsg)->cmsg_len < sizeof(struct net_cmsghdr) ||              \
           (cmsg)->cmsg_len > (size_t)((uint8_t *)((msghdr)->msg_control) + \
                                       (msghdr)->msg_controllen -        \
                                       (uint8_t *)(cmsg)) ||             \
           (uint8_t *)(cmsg) + NET_ALIGN_H((cmsg)->cmsg_len) +           \
           NET_ALIGN_D(sizeof(struct net_cmsghdr)) >                     \
           (uint8_t *)((msghdr)->msg_control) + (msghdr)->msg_controllen) ? \
          NULL :                                                         \
          (struct net_cmsghdr *)((uint8_t *)(cmsg) +                     \
                                 NET_ALIGN_H((cmsg)->cmsg_len))))
#endif

#if !defined(NET_CMSG_DATA)
#define NET_CMSG_DATA(cmsg) ((uint8_t *)(cmsg) + NET_ALIGN_D(sizeof(struct net_cmsghdr)))
#endif

#if !defined(NET_CMSG_SPACE)
#define NET_CMSG_SPACE(length) (NET_ALIGN_D(sizeof(struct net_cmsghdr)) + NET_ALIGN_H(length))
#endif

#if !defined(NET_CMSG_LEN)
#define NET_CMSG_LEN(length) (NET_ALIGN_D(sizeof(struct net_cmsghdr)) + length)
#endif


/* Packet types.  */
#define NET_PACKET_HOST         0     /* To us            */
#define NET_PACKET_BROADCAST    1     /* To all           */
#define NET_PACKET_MULTICAST    2     /* To group         */
#define NET_PACKET_OTHERHOST    3     /* To someone else  */
#define NET_PACKET_OUTGOING     4     /* Originated by us */
#define NET_PACKET_LOOPBACK     5
#define NET_PACKET_FASTROUTE    6

/* ARP protocol HARDWARE identifiers. */
#define NET_ARPHRD_ETHER 1
#define NET_ARPHRD_PPP   512

/* Note: These macros are defined in a specific order.
 * The largest sockaddr size is the last one.
 */
#if defined(CONFIG_NET_IPV4)
#undef NET_SOCKADDR_MAX_SIZE
#undef NET_SOCKADDR_PTR_MAX_SIZE
#define NET_SOCKADDR_MAX_SIZE (sizeof(struct net_sockaddr_in))
#define NET_SOCKADDR_PTR_MAX_SIZE (sizeof(struct net_sockaddr_in_ptr))
#endif

#if defined(CONFIG_NET_SOCKETS_PACKET)
#undef NET_SOCKADDR_MAX_SIZE
#undef NET_SOCKADDR_PTR_MAX_SIZE
#define NET_SOCKADDR_MAX_SIZE (sizeof(struct net_sockaddr_ll))
#define NET_SOCKADDR_PTR_MAX_SIZE (sizeof(struct net_sockaddr_ll_ptr))
#endif

#if defined(CONFIG_NET_IPV6)
#undef NET_SOCKADDR_MAX_SIZE
#define NET_SOCKADDR_MAX_SIZE (sizeof(struct net_sockaddr_in6))
#if !defined(CONFIG_NET_SOCKETS_PACKET)
#undef NET_SOCKADDR_PTR_MAX_SIZE
#define NET_SOCKADDR_PTR_MAX_SIZE (sizeof(struct net_sockaddr_in6_ptr))
#endif
#endif

#if defined(CONFIG_NET_NATIVE_OFFLOADED_SOCKETS)
#define UNIX_PATH_MAX 108
#undef NET_SOCKADDR_MAX_SIZE
/* Define NET_SOCKADDR_MAX_SIZE to be struct of net_sa_family_t + char[UNIX_PATH_MAX] */
#define NET_SOCKADDR_MAX_SIZE (UNIX_PATH_MAX+sizeof(net_sa_family_t))
#if !defined(CONFIG_NET_SOCKETS_PACKET)
#undef NET_SOCKADDR_PTR_MAX_SIZE
#define NET_SOCKADDR_PTR_MAX_SIZE (sizeof(struct net_sockaddr_un_ptr))
#endif
#endif

#if !defined(CONFIG_NET_IPV4)
#if !defined(CONFIG_NET_IPV6)
#if !defined(CONFIG_NET_SOCKETS_PACKET)
#if !defined(CONFIG_NET_NATIVE_OFFLOADED_SOCKETS)
#define NET_SOCKADDR_MAX_SIZE (sizeof(struct net_sockaddr_in6))
#define NET_SOCKADDR_PTR_MAX_SIZE (sizeof(struct net_sockaddr_in6_ptr))
#endif
#endif
#endif
#endif


#define SOCKADDR_ALIGN (4)

struct net_sockaddr {
        net_sa_family_t sa_family;
        char data[NET_SOCKADDR_MAX_SIZE - sizeof(net_sa_family_t)];
} __aligned(SOCKADDR_ALIGN);


struct net_sockaddr_ptr {
        net_sa_family_t family;
        char data[NET_SOCKADDR_PTR_MAX_SIZE - sizeof(net_sa_family_t)];
} __aligned(SOCKADDR_ALIGN);

/* Same as sockaddr in our case */
struct net_sockaddr_storage {
        net_sa_family_t ss_family;
        char data[NET_SOCKADDR_MAX_SIZE - sizeof(net_sa_family_t)];
} __aligned(SOCKADDR_ALIGN);

/* Socket address struct for UNIX domain sockets */
struct net_sockaddr_un {
        net_sa_family_t sun_family;    /* NET_AF_UNIX */
        char            sun_path[NET_SOCKADDR_MAX_SIZE - sizeof(net_sa_family_t)];
};

struct net_addr {
        net_sa_family_t family;
        union {
#if defined(CONFIG_NET_NAMESPACE_COMPAT_MODE)
                struct net_in6_addr net_in6_addr;
                struct net_in_addr net_in_addr;
#else
                struct net_in6_addr in6_addr;
                struct net_in_addr in_addr;
#endif
        };
};

extern const struct net_in6_addr net_in6addr_any;

extern const struct net_in6_addr net_in6addr_loopback;


#define NET_IN6ADDR_ANY_INIT { { { 0, 0, 0, 0, 0, 0, 0, 0,      \
                                   0, 0, 0, 0, 0, 0, 0, 0 } } }

#define NET_IN6ADDR_LOOPBACK_INIT { { { 0, 0, 0, 0, 0, 0, 0, 0, \
                                        0, 0, 0, 0, 0, 0, 0, 1 } } }

#define NET_INADDR_ANY 0

#define NET_INADDR_BROADCAST 0xffffffff

#define NET_INADDR_ANY_INIT { { { NET_INADDR_ANY } } }

#define NET_INADDR_LOOPBACK_INIT  { { { 127, 0, 0, 1 } } }

#define NET_INET_ADDRSTRLEN 16

#define NET_INET6_ADDRSTRLEN 46


/* These are for internal usage of the stack */
#define NET_IPV6_ADDR_LEN sizeof("xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxx.xxx.xxx.xxx")
#define NET_IPV4_ADDR_LEN sizeof("xxx.xxx.xxx.xxx")


enum net_ip_mtu {
#if defined(CONFIG_NET_NATIVE_IPV6)
        NET_IPV6_MTU = CONFIG_NET_IPV6_MTU,
#else
        NET_IPV6_MTU = 1280,
#endif

#if defined(CONFIG_NET_NATIVE_IPV4)
        NET_IPV4_MTU = CONFIG_NET_IPV4_MTU,
#else
        NET_IPV4_MTU = 576,
#endif
};

enum net_priority {
        NET_PRIORITY_BK = 1,
        NET_PRIORITY_BE = 0,
        NET_PRIORITY_EE = 2,
        NET_PRIORITY_CA = 3,
        NET_PRIORITY_VI = 4,
        NET_PRIORITY_VO = 5,
        NET_PRIORITY_IC = 6,
        NET_PRIORITY_NC = 7
} __packed;

#define NET_MAX_PRIORITIES 8

struct net_tuple {
        struct net_addr *remote_addr;
        struct net_addr *local_addr;
        uint16_t remote_port;
        uint16_t local_port;
        enum net_ip_protocol ip_proto;
};

enum net_addr_state {
        NET_ADDR_ANY_STATE = -1,
        NET_ADDR_TENTATIVE = 0,
        NET_ADDR_PREFERRED,
        NET_ADDR_DEPRECATED,
} __packed;

enum net_addr_type {
        NET_ADDR_ANY = 0,
        NET_ADDR_AUTOCONF,
        NET_ADDR_DHCP,
        NET_ADDR_MANUAL,
        NET_ADDR_OVERRIDABLE,
} __packed;


struct net_ipv6_hdr {
        uint8_t vtc;
        uint8_t tcflow;
        uint16_t flow;
        uint16_t len;
        uint8_t nexthdr;
        uint8_t hop_limit;
        uint8_t src[NET_IPV6_ADDR_SIZE];
        uint8_t dst[NET_IPV6_ADDR_SIZE];
} __packed;

struct net_ipv6_frag_hdr {
        uint8_t nexthdr;
        uint8_t reserved;
        uint16_t offset;
        uint32_t id;
} __packed;

struct net_ipv4_hdr {
        uint8_t vhl;
        uint8_t tos;
        uint16_t len;
        uint8_t id[2];
        uint8_t offset[2];
        uint8_t ttl;
        uint8_t proto;
        uint16_t chksum;
        uint8_t src[NET_IPV4_ADDR_SIZE];
        uint8_t dst[NET_IPV4_ADDR_SIZE];
} __packed;

struct net_icmp_hdr {
        uint8_t type;
        uint8_t code;
        uint16_t chksum;
} __packed;

struct net_udp_hdr {
        uint16_t src_port;
        uint16_t dst_port;
        uint16_t len;
        uint16_t chksum;
} __packed;

struct net_udp_opt_mrds {
        uint16_t size;
        uint8_t segs;
};

struct net_udp_opt_time {
        uint32_t tsval;
        uint32_t tsecr;
};

struct net_tcp_hdr {
        uint16_t src_port;
        uint16_t dst_port;
        uint8_t seq[4];
        uint8_t ack[4];
        uint8_t offset;
        uint8_t flags;
        uint8_t wnd[2];
        uint16_t chksum;
        uint8_t urg[2];
        uint8_t optdata[0];
} __packed;

static inline const char *net_addr_type2str(enum net_addr_type type)
{
        switch (type) {
        case NET_ADDR_AUTOCONF:
                return "AUTO";
        case NET_ADDR_DHCP:
                return "DHCP";
        case NET_ADDR_MANUAL:
                return "MANUAL";
        case NET_ADDR_OVERRIDABLE:
                return "OVERRIDE";
        case NET_ADDR_ANY:
        default:
                break;
        }

        return "<unknown>";
}

/* IPv6 extension headers types */
#define NET_IPV6_NEXTHDR_HBHO        0
#define NET_IPV6_NEXTHDR_DESTO       60
#define NET_IPV6_NEXTHDR_ROUTING     43
#define NET_IPV6_NEXTHDR_FRAG        44
#define NET_IPV6_NEXTHDR_NONE        59

union net_ip_header {
        struct net_ipv4_hdr *ipv4;
        struct net_ipv6_hdr *ipv6;
};

union net_proto_header {
        struct net_udp_hdr *udp;
        struct net_tcp_hdr *tcp;
};

#define NET_UDPH_LEN    8                       /* Size of UDP header */
#define NET_TCPH_LEN    20                      /* Size of TCP header */
#define NET_ICMPH_LEN   4                       /* Size of ICMP header */

#define NET_IPV6H_LEN      40                   /* Size of IPv6 header */
#define NET_ICMPV6H_LEN    NET_ICMPH_LEN        /* Size of ICMPv6 header */
#define NET_IPV6UDPH_LEN   (NET_UDPH_LEN + NET_IPV6H_LEN) /* IPv6 + UDP */
#define NET_IPV6TCPH_LEN   (NET_TCPH_LEN + NET_IPV6H_LEN) /* IPv6 + TCP */
#define NET_IPV6ICMPH_LEN  (NET_IPV6H_LEN + NET_ICMPH_LEN) /* ICMPv6 + IPv6 */
#define NET_IPV6_FRAGH_LEN 8

#define NET_IPV4H_LEN      20                   /* Size of IPv4 header */
#define NET_ICMPV4H_LEN    NET_ICMPH_LEN        /* Size of ICMPv4 header */
#define NET_IPV4UDPH_LEN   (NET_UDPH_LEN + NET_IPV4H_LEN) /* IPv4 + UDP */
#define NET_IPV4TCPH_LEN   (NET_TCPH_LEN + NET_IPV4H_LEN) /* IPv4 + TCP */
#define NET_IPV4ICMPH_LEN  (NET_IPV4H_LEN + NET_ICMPH_LEN) /* ICMPv4 + IPv4 */

#define NET_IPV6H_LENGTH_OFFSET         0x04    /* Offset of the Length field in the IPv6 header */

#define NET_IPV6_FRAGH_OFFSET_MASK      0xfff8  /* Mask for the 13-bit Fragment Offset field */
#define NET_IPV4_FRAGH_OFFSET_MASK      0x1fff  /* Mask for the 13-bit Fragment Offset field */
#define NET_IPV4_MORE_FRAG_MASK         0x2000  /* Mask for the 1-bit More Fragments field */
#define NET_IPV4_DO_NOT_FRAG_MASK       0x4000  /* Mask for the 1-bit Do Not Fragment field */

#if defined(CONFIG_NET_INTERFACE_NAME)
#define NET_IFNAMSIZ CONFIG_NET_INTERFACE_NAME_LEN
#else
#if defined(Z_DEVICE_MAX_NAME_LEN)
#define NET_IFNAMSIZ Z_DEVICE_MAX_NAME_LEN
#else
#define NET_IFNAMSIZ 1
#endif /* Z_DEVICE_MAX_NAME_LEN */
#endif /* CONFIG_NET_INTERFACE_NAME */



struct net_ifreq {
        char ifr_name[NET_IFNAMSIZ];
};


struct net_in_pktinfo {
        unsigned int       ipi_ifindex;
        struct net_in_addr ipi_spec_dst;
        struct net_in_addr ipi_addr;
};

struct net_ip_mreqn {
        struct net_in_addr imr_multiaddr;
        struct net_in_addr imr_address;
        int                imr_ifindex;
};

struct net_ip_mreq  {
        struct net_in_addr imr_multiaddr;
        struct net_in_addr imr_interface;
};

struct net_ipv6_mreq {
        struct net_in6_addr ipv6mr_multiaddr;

        int ipv6mr_ifindex;
};

struct net_packet_mreq {
        int mr_ifindex;

        uint16_t mr_type;

        uint16_t mr_alen;

        uint8_t mr_address[NET_LINK_ADDR_MAX_LENGTH];
};

#define NET_PACKET_MR_MULTICAST 0
#define NET_PACKET_MR_PROMISC   1
#define NET_PACKET_MR_ALLMULTI  2

struct net_in6_pktinfo {
        struct net_in6_addr ipi6_addr;
        unsigned int        ipi6_ifindex;
};

static inline bool net_ipv6_is_addr_loopback_raw(const uint8_t *addr)
{
        return UNALIGNED_GET((uint32_t *)addr) == 0 &&
               UNALIGNED_GET((uint32_t *)addr + 1) == 0 &&
               UNALIGNED_GET((uint32_t *)addr + 2) == 0 &&
               net_ntohl(UNALIGNED_GET((uint32_t *)addr + 3)) == 1;
}

static inline bool net_ipv6_is_addr_loopback(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_loopback_raw(addr->s6_addr);
}

static inline bool net_ipv6_is_addr_mcast_raw(const uint8_t *addr)
{
        return addr[0] == 0xff;
}

static inline bool net_ipv6_is_addr_mcast(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_mcast_raw(addr->s6_addr);
}

struct net_if;
struct net_if_config;

extern struct net_if_addr *net_if_ipv6_addr_lookup_raw(const uint8_t *addr,
                                                       struct net_if **ret);

static inline bool net_ipv6_is_my_addr_raw(const uint8_t *addr)
{
        return net_if_ipv6_addr_lookup_raw(addr, NULL) != NULL;
}

extern struct net_if_addr *net_if_ipv6_addr_lookup(const struct net_in6_addr *addr,
                                                   struct net_if **iface);

static inline bool net_ipv6_is_my_addr(struct net_in6_addr *addr)
{
        return net_if_ipv6_addr_lookup(addr, NULL) != NULL;
}

extern struct net_if_mcast_addr *net_if_ipv6_maddr_lookup(
        const struct net_in6_addr *addr, struct net_if **iface);

static inline bool net_ipv6_is_my_maddr(struct net_in6_addr *maddr)
{
        return net_if_ipv6_maddr_lookup(maddr, NULL) != NULL;
}

static inline bool net_ipv6_is_prefix(const uint8_t *addr1,
                                      const uint8_t *addr2,
                                      uint8_t length)
{
        uint8_t bits = 128 - length;
        uint8_t bytes = length / 8U;
        uint8_t remain = bits % 8;
        uint8_t mask;

        if (length > 128) {
                return false;
        }

        if (memcmp(addr1, addr2, bytes)) {
                return false;
        }

        if (!remain) {
                /* No remaining bits, the prefixes are the same as first
                 * bytes are the same.
                 */
                return true;
        }

        /* Create a mask that has remaining most significant bits set */
        mask = (uint8_t)((0xff << (8 - remain)) ^ 0xff) << remain;

        return (addr1[bytes] & mask) == (addr2[bytes] & mask);
}


static inline void net_ipv6_addr_prefix_mask(const uint8_t *inaddr,
                                             uint8_t *outaddr,
                                             uint8_t prefix_len)
{
        uint8_t bits = 128 - prefix_len;
        uint8_t bytes = prefix_len / 8U;
        uint8_t remain = bits % 8;
        uint8_t mask;

        memset(outaddr, 0, 16U);
        memcpy(outaddr, inaddr, bytes);

        if (!remain) {
                /* No remaining bits, the prefixes are the same as first
                 * bytes are the same.
                 */
                return;
        }

        /* Create a mask that has remaining most significant bits set */
        mask = (uint8_t)((0xff << (8 - remain)) ^ 0xff) << remain;
        outaddr[bytes] = inaddr[bytes] & mask;
}

static inline bool net_ipv4_is_addr_loopback_raw(const uint8_t *addr)
{
        return addr[0] == 127U;
}

static inline bool net_ipv4_is_addr_loopback(const struct net_in_addr *addr)
{
        return net_ipv4_is_addr_loopback_raw(addr->s4_addr);
}

static inline bool net_ipv4_is_addr_unspecified_raw(const uint8_t *addr)
{
        return UNALIGNED_GET((uint32_t *)addr) == 0;
}

static inline bool net_ipv4_is_addr_unspecified(const struct net_in_addr *addr)
{
        return net_ipv4_is_addr_unspecified_raw(addr->s4_addr);
}

static inline bool net_ipv4_is_addr_mcast_raw(const uint8_t *addr)
{
        return (net_ntohl(UNALIGNED_GET((uint32_t *)addr)) & 0xF0000000) == 0xE0000000;
}

static inline bool net_ipv4_is_addr_mcast(const struct net_in_addr *addr)
{
        return net_ipv4_is_addr_mcast_raw(addr->s4_addr);
}

static inline bool net_ipv4_is_ll_addr_raw(const uint8_t *addr)
{
        return (net_ntohl(UNALIGNED_GET((uint32_t *)addr)) & 0xFFFF0000) == 0xA9FE0000;
}

static inline bool net_ipv4_is_ll_addr(const struct net_in_addr *addr)
{
        return net_ipv4_is_ll_addr_raw(addr->s4_addr);
}

static inline bool net_ipv4_is_private_addr(const struct net_in_addr *addr)
{
        uint32_t masked_24, masked_16, masked_12, masked_10, masked_8;

        masked_24 = net_ntohl(UNALIGNED_GET(&addr->s_addr)) & 0xFFFFFF00;
        masked_16 = masked_24 & 0xFFFF0000;
        masked_12 = masked_24 & 0xFFF00000;
        masked_10 = masked_24 & 0xFFC00000;
        masked_8 = masked_24 & 0xFF000000;

        return masked_8  == 0x0A000000 || /* 10.0.0.0/8      */
               masked_10 == 0x64400000 || /* 100.64.0.0/10   */
               masked_12 == 0xAC100000 || /* 172.16.0.0/12   */
               masked_16 == 0xC0A80000 || /* 192.168.0.0/16  */
               masked_24 == 0xC0000200 || /* 192.0.2.0/24    */
               masked_24 == 0xC0336400 || /* 192.51.100.0/24 */
               masked_24 == 0xCB007100;   /* 203.0.113.0/24  */
}

#define net_ipaddr_copy(dest, src) \
        UNALIGNED_PUT(UNALIGNED_GET(src), dest)

static inline void net_ipv4_addr_copy_raw(uint8_t *dest,
                                          const uint8_t *src)
{
        net_ipaddr_copy((struct net_in_addr *)dest, (const struct net_in_addr *)src);
}

static inline void net_ipv6_addr_copy_raw(uint8_t *dest,
                                          const uint8_t *src)
{
        memcpy(dest, src, sizeof(struct net_in6_addr));
}

static inline bool net_ipv4_addr_cmp_raw(const uint8_t *addr1,
                                         const uint8_t *addr2)
{
        return UNALIGNED_GET((uint32_t *)addr1) == UNALIGNED_GET((uint32_t *)addr2);
}

static inline bool net_ipv4_addr_cmp(const struct net_in_addr *addr1,
                                     const struct net_in_addr *addr2)
{
        return net_ipv4_addr_cmp_raw(addr1->s4_addr, addr2->s4_addr);
}

static inline bool net_ipv6_addr_cmp(const struct net_in6_addr *addr1,
                                     const struct net_in6_addr *addr2)
{
        return !memcmp(addr1, addr2, sizeof(struct net_in6_addr));
}

static inline bool net_ipv6_addr_cmp_raw(const uint8_t *addr1,
                                         const uint8_t *addr2)
{
        return net_ipv6_addr_cmp((const struct net_in6_addr *)addr1,
                                 (const struct net_in6_addr *)addr2);
}

static inline bool net_ipv6_is_ll_addr_raw(const uint8_t *addr)
{
        return UNALIGNED_GET((uint16_t *)addr) == net_htons(0xFE80);
}

static inline bool net_ipv6_is_ll_addr(const struct net_in6_addr *addr)
{
        return net_ipv6_is_ll_addr_raw(addr->s6_addr);
}

static inline bool net_ipv6_is_sl_addr(const struct net_in6_addr *addr)
{
        return UNALIGNED_GET(&addr->s6_addr16[0]) == net_htons(0xFEC0);
}


static inline bool net_ipv6_is_ula_addr(const struct net_in6_addr *addr)
{
        return addr->s6_addr[0] == 0xFD;
}

static inline bool net_ipv6_is_global_addr(const struct net_in6_addr *addr)
{
        return (addr->s6_addr[0] & 0xE0) == 0x20;
}

static inline bool net_ipv6_is_private_addr(const struct net_in6_addr *addr)
{
        uint32_t masked_32, masked_7;

        masked_32 = net_ntohl(UNALIGNED_GET(&addr->s6_addr32[0]));
        masked_7 = masked_32 & 0xfc000000;

        return masked_32 == 0x20010db8 || /* 2001:db8::/32 */
               masked_7  == 0xfc000000;   /* fc00::/7      */
}

const struct net_in6_addr *net_ipv6_unspecified_address(void);

const struct net_in_addr *net_ipv4_unspecified_address(void);

const struct net_in_addr *net_ipv4_broadcast_address(void);

struct net_if;
extern bool net_if_ipv4_addr_mask_cmp(struct net_if *iface,
                                      const struct net_in_addr *addr);

static inline bool net_ipv4_addr_mask_cmp(struct net_if *iface,
                                          const struct net_in_addr *addr)
{
        return net_if_ipv4_addr_mask_cmp(iface, addr);
}

extern bool net_if_ipv4_is_addr_bcast_raw(struct net_if *iface,
                                          const uint8_t *addr);

#if defined(CONFIG_NET_NATIVE_IPV4)
static inline bool net_ipv4_is_addr_bcast_raw(struct net_if *iface,
                                              const uint8_t *addr)
{
        if (net_ipv4_addr_cmp_raw(addr, net_ipv4_broadcast_address()->s4_addr)) {
                return true;
        }

        return net_if_ipv4_is_addr_bcast_raw(iface, addr);
}
#else
static inline bool net_ipv4_is_addr_bcast_raw(struct net_if *iface,
                                              const uint8_t *addr)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(addr);

        return false;
}
#endif

extern bool net_if_ipv4_is_addr_bcast(struct net_if *iface,
                                      const struct net_in_addr *addr);

#if defined(CONFIG_NET_NATIVE_IPV4)
static inline bool net_ipv4_is_addr_bcast(struct net_if *iface,
                                          const struct net_in_addr *addr)
{
        if (net_ipv4_addr_cmp(addr, net_ipv4_broadcast_address())) {
                return true;
        }

        return net_if_ipv4_is_addr_bcast(iface, addr);
}
#else
static inline bool net_ipv4_is_addr_bcast(struct net_if *iface,
                                          const struct net_in_addr *addr)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(addr);

        return false;
}
#endif

extern struct net_if_addr *net_if_ipv4_addr_lookup_raw(const uint8_t *addr,
                                                       struct net_if **ret);

static inline bool net_ipv4_is_my_addr_raw(const uint8_t *addr)
{
        bool ret;

        ret = net_if_ipv4_addr_lookup_raw(addr, NULL) != NULL;
        if (!ret) {
                ret = net_ipv4_is_addr_bcast_raw(NULL, addr);
        }

        return ret;
}

extern struct net_if_addr *net_if_ipv4_addr_lookup(const struct net_in_addr *addr,
                                                   struct net_if **iface);

static inline bool net_ipv4_is_my_addr(const struct net_in_addr *addr)
{
        bool ret;

        ret = net_if_ipv4_addr_lookup(addr, NULL) != NULL;
        if (!ret) {
                ret = net_ipv4_is_addr_bcast(NULL, addr);
        }

        return ret;
}

static inline bool net_ipv6_is_addr_unspecified_raw(const uint8_t *addr)
{
        return UNALIGNED_GET((uint32_t *)addr) == 0 &&
               UNALIGNED_GET((uint32_t *)addr + 1) == 0 &&
               UNALIGNED_GET((uint32_t *)addr + 2) == 0 &&
               UNALIGNED_GET((uint32_t *)addr + 3) == 0;
}

static inline bool net_ipv6_is_addr_unspecified(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_unspecified_raw(addr->s6_addr);
}

static inline bool net_ipv6_is_addr_solicited_node_raw(const uint8_t *addr)
{
        return UNALIGNED_GET((uint32_t *)addr) == net_htonl(0xff020000) &&
               UNALIGNED_GET((uint32_t *)addr + 1) == 0x00000000 &&
               UNALIGNED_GET((uint32_t *)addr + 2) == net_htonl(0x00000001) &&
               ((UNALIGNED_GET((uint32_t *)addr + 3) & net_htonl(0xff000000)) ==
                net_htonl(0xff000000));
}

static inline bool net_ipv6_is_addr_solicited_node(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_solicited_node_raw(addr->s6_addr);
}

static inline bool net_ipv6_is_addr_mcast_scope_raw(const uint8_t *addr,
                                                    int scope)
{
        return (addr[0] == 0xff) && ((addr[1] & 0xF) == scope);
}

static inline int net_ipv6_get_addr_mcast_scope_raw(const uint8_t *addr)
{
        if (addr[0] == 0xff) {
                return (addr[1] & 0xF);
        }

        return -1;
}

static inline bool net_ipv6_is_addr_mcast_scope(const struct net_in6_addr *addr,
                                                int scope)
{
        return net_ipv6_is_addr_mcast_scope_raw(addr->s6_addr, scope);
}

static inline bool net_ipv6_is_same_mcast_scope(const struct net_in6_addr *addr_1,
                                                const struct net_in6_addr *addr_2)
{
        return (addr_1->s6_addr[0] == 0xff) && (addr_2->s6_addr[0] == 0xff) &&
                (addr_1->s6_addr[1] == addr_2->s6_addr[1]);
}

static inline int net_ipv6_get_addr_mcast_scope(const struct net_in6_addr *addr)
{
        return net_ipv6_get_addr_mcast_scope_raw(addr->s6_addr);
}

static inline bool net_ipv6_is_addr_mcast_iface_raw(const uint8_t *addr)
{
        return net_ipv6_is_addr_mcast_scope_raw(addr, 0x01);
}

static inline bool net_ipv6_is_addr_mcast_link_raw(const uint8_t *addr)
{
        return net_ipv6_is_addr_mcast_scope_raw(addr, 0x02);
}

static inline bool net_ipv6_is_addr_mcast_mesh_raw(const uint8_t *addr)
{
        return net_ipv6_is_addr_mcast_scope_raw(addr, 0x03);
}

static inline bool net_ipv6_is_addr_mcast_site_raw(const uint8_t *addr)
{
        return net_ipv6_is_addr_mcast_scope_raw(addr, 0x05);
}

static inline bool net_ipv6_is_addr_mcast_org_raw(const uint8_t *addr)
{
        return net_ipv6_is_addr_mcast_scope_raw(addr, 0x08);
}

static inline bool net_ipv6_is_addr_mcast_global(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_mcast_scope(addr, 0x0e);
}

static inline bool net_ipv6_is_addr_mcast_iface(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_mcast_scope(addr, 0x01);
}

static inline bool net_ipv6_is_addr_mcast_link(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_mcast_scope(addr, 0x02);
}

static inline bool net_ipv6_is_addr_mcast_mesh(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_mcast_scope(addr, 0x03);
}

static inline bool net_ipv6_is_addr_mcast_site(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_mcast_scope(addr, 0x05);
}

static inline bool net_ipv6_is_addr_mcast_org(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_mcast_scope(addr, 0x08);
}

static inline bool net_ipv6_is_addr_mcast_group_raw(const uint8_t *addr,
                                                    const uint8_t *group)
{
        return UNALIGNED_GET((uint16_t *)addr + 1) == UNALIGNED_GET((uint16_t *)group + 1) &&
               UNALIGNED_GET((uint32_t *)addr + 1) == UNALIGNED_GET((uint32_t *)group + 1) &&
               UNALIGNED_GET((uint32_t *)addr + 2) == UNALIGNED_GET((uint32_t *)group + 2) &&
               UNALIGNED_GET((uint32_t *)addr + 3) == UNALIGNED_GET((uint32_t *)group + 3);
}

static inline bool net_ipv6_is_addr_mcast_group(const struct net_in6_addr *addr,
                                                const struct net_in6_addr *group)
{
        return net_ipv6_is_addr_mcast_group_raw(addr->s6_addr, group->s6_addr);
}

static inline bool net_ipv6_is_addr_mcast_all_nodes_group_raw(const uint8_t *addr)
{
        static const uint8_t all_nodes_mcast_group[NET_IPV6_ADDR_SIZE] = {
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x01,
        };

        return net_ipv6_is_addr_mcast_group_raw(addr, all_nodes_mcast_group);
}

static inline bool
net_ipv6_is_addr_mcast_all_nodes_group(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_mcast_all_nodes_group_raw(addr->s6_addr);
}

static inline bool
net_ipv6_is_addr_mcast_iface_all_nodes(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_mcast_iface(addr) &&
               net_ipv6_is_addr_mcast_all_nodes_group(addr);
}

static inline bool net_ipv6_is_addr_mcast_link_all_nodes_raw(const uint8_t *addr)
{
        return net_ipv6_is_addr_mcast_link_raw(addr) &&
               net_ipv6_is_addr_mcast_all_nodes_group_raw(addr);
}

static inline bool
net_ipv6_is_addr_mcast_link_all_nodes(const struct net_in6_addr *addr)
{
        return net_ipv6_is_addr_mcast_link(addr) &&
               net_ipv6_is_addr_mcast_all_nodes_group(addr);
}

static inline
void net_ipv6_addr_create_solicited_node(const struct net_in6_addr *src,
                                         struct net_in6_addr *dst)
{
        dst->s6_addr[0]   = 0xFF;
        dst->s6_addr[1]   = 0x02;
        UNALIGNED_PUT(0, &dst->s6_addr16[1]);
        UNALIGNED_PUT(0, &dst->s6_addr16[2]);
        UNALIGNED_PUT(0, &dst->s6_addr16[3]);
        UNALIGNED_PUT(0, &dst->s6_addr16[4]);
        dst->s6_addr[10]  = 0U;
        dst->s6_addr[11]  = 0x01;
        dst->s6_addr[12]  = 0xFF;
        dst->s6_addr[13]  = src->s6_addr[13];
        UNALIGNED_PUT(UNALIGNED_GET(&src->s6_addr16[7]), &dst->s6_addr16[7]);
}

static inline void net_ipv6_addr_create(struct net_in6_addr *addr,
                                        uint16_t addr0, uint16_t addr1,
                                        uint16_t addr2, uint16_t addr3,
                                        uint16_t addr4, uint16_t addr5,
                                        uint16_t addr6, uint16_t addr7)
{
        UNALIGNED_PUT(net_htons(addr0), &addr->s6_addr16[0]);
        UNALIGNED_PUT(net_htons(addr1), &addr->s6_addr16[1]);
        UNALIGNED_PUT(net_htons(addr2), &addr->s6_addr16[2]);
        UNALIGNED_PUT(net_htons(addr3), &addr->s6_addr16[3]);
        UNALIGNED_PUT(net_htons(addr4), &addr->s6_addr16[4]);
        UNALIGNED_PUT(net_htons(addr5), &addr->s6_addr16[5]);
        UNALIGNED_PUT(net_htons(addr6), &addr->s6_addr16[6]);
        UNALIGNED_PUT(net_htons(addr7), &addr->s6_addr16[7]);
}

static inline void net_ipv6_addr_create_ll_allnodes_mcast(struct net_in6_addr *addr)
{
        net_ipv6_addr_create(addr, 0xff02, 0, 0, 0, 0, 0, 0, 0x0001);
}

static inline void net_ipv6_addr_create_ll_allrouters_mcast(struct net_in6_addr *addr)
{
        net_ipv6_addr_create(addr, 0xff02, 0, 0, 0, 0, 0, 0, 0x0002);
}

static inline void net_ipv6_addr_create_v4_mapped(const struct net_in_addr *addr4,
                                                  struct net_in6_addr *addr6)
{
        net_ipv6_addr_create(addr6, 0, 0, 0, 0, 0, 0xffff,
                             net_ntohs(addr4->s4_addr16[0]),
                             net_ntohs(addr4->s4_addr16[1]));
}

static inline bool net_ipv6_addr_is_v4_mapped(const struct net_in6_addr *addr)
{
        if (UNALIGNED_GET(&addr->s6_addr32[0]) == 0 &&
            UNALIGNED_GET(&addr->s6_addr32[1]) == 0 &&
            UNALIGNED_GET(&addr->s6_addr16[5]) == 0xffff) {
                return true;
        }

        return false;
}

static inline void net_ipv6_addr_get_v4_mapped(const struct net_in6_addr *addr6,
                                               struct net_in_addr *addr4)
{
        addr4->s_addr = UNALIGNED_GET(&addr6->s6_addr32[3]);
}

int net_ipv6_addr_generate_iid(struct net_if *iface,
                               const struct net_in6_addr *prefix,
                               uint8_t *network_id, size_t network_id_len,
                               uint8_t dad_counter,
                               struct net_in6_addr *addr,
                               struct net_linkaddr *lladdr);

static inline void net_ipv6_addr_create_iid(struct net_in6_addr *addr,
                                            struct net_linkaddr *lladdr)
{
        (void)net_ipv6_addr_generate_iid(NULL, NULL, NULL, 0, 0, addr, lladdr);
}

static inline bool net_ipv6_addr_based_on_ll_raw(const uint8_t *addr,
                                                 const struct net_linkaddr *lladdr)
{
        if (addr == NULL || lladdr == NULL) {
                return false;
        }

        switch (lladdr->len) {
        case 2:
                if (!memcmp(&addr[14], lladdr->addr, lladdr->len) &&
                    addr[8]  == 0U &&
                    addr[9]  == 0U &&
                    addr[10] == 0U &&
                    addr[11] == 0xff &&
                    addr[12] == 0xfe) {
                        return true;
                }

                break;
        case 6:
                if (lladdr->type == NET_LINK_ETHERNET) {
                        if (!memcmp(&addr[9], &lladdr->addr[1], 2) &&
                            !memcmp(&addr[13], &lladdr->addr[3], 3) &&
                            addr[11] == 0xff &&
                            addr[12] == 0xfe &&
                            (addr[8] ^ 0x02) == lladdr->addr[0]) {
                                return true;
                        }
                }

                break;
        case 8:
                if (sizeof(lladdr->addr) < 8) {
                        return false;
                }

                if (!memcmp(&addr[9], &lladdr->addr[1],
                            lladdr->len - 1) &&
                    (addr[8] ^ 0x02) == lladdr->addr[0]) {
                        return true;
                }

                break;
        default:
                return false;
        }

        return false;
}

static inline bool net_ipv6_addr_based_on_ll(const struct net_in6_addr *addr,
                                             const struct net_linkaddr *lladdr)
{
        if (addr == NULL || lladdr == NULL) {
                return false;
        }

        return net_ipv6_addr_based_on_ll_raw(addr->s6_addr, lladdr);
}

static ALWAYS_INLINE struct net_sockaddr *net_sad(const struct net_sockaddr_storage *addr)
{
        return (struct net_sockaddr *)addr;
}

static ALWAYS_INLINE struct net_sockaddr_storage *net_sas(const struct net_sockaddr *addr)
{
        return (struct net_sockaddr_storage *)addr;
}

static ALWAYS_INLINE struct net_sockaddr_in6 *net_sin6(const struct net_sockaddr *addr)
{
        return (struct net_sockaddr_in6 *)addr;
}

static ALWAYS_INLINE struct net_sockaddr_in *net_sin(const struct net_sockaddr *addr)
{
        return (struct net_sockaddr_in *)addr;
}

static ALWAYS_INLINE
struct net_sockaddr_in6_ptr *net_sin6_ptr(const struct net_sockaddr_ptr *addr)
{
        return (struct net_sockaddr_in6_ptr *)addr;
}

static ALWAYS_INLINE
struct net_sockaddr_in_ptr *net_sin_ptr(const struct net_sockaddr_ptr *addr)
{
        return (struct net_sockaddr_in_ptr *)addr;
}

static ALWAYS_INLINE
struct net_sockaddr_ll_ptr *net_sll_ptr(const struct net_sockaddr_ptr *addr)
{
        return (struct net_sockaddr_ll_ptr *)addr;
}

static ALWAYS_INLINE
struct net_sockaddr_can_ptr *net_can_ptr(const struct net_sockaddr_ptr *addr)
{
        return (struct net_sockaddr_can_ptr *)addr;
}

__syscall int net_addr_pton(net_sa_family_t family, const char *src, void *dst);

__syscall char *net_addr_ntop(net_sa_family_t family, const void *src,
                              char *dst, size_t size);

int net_mask_len_to_netmask(net_sa_family_t family, uint8_t mask_len,
                            struct net_sockaddr *mask);

int net_netmask_to_mask_len(net_sa_family_t family, struct net_sockaddr *mask,
                            uint8_t *mask_len);

bool net_ipaddr_parse(const char *str, size_t str_len,
                      struct net_sockaddr *addr);

const char *net_ipaddr_parse_mask(const char *str, size_t str_len,
                                  struct net_sockaddr *addr, uint8_t *mask_len);

int net_port_set_default(struct net_sockaddr *addr, uint16_t default_port);

int net_port_set(struct net_sockaddr *addr, uint16_t port);

int net_port_get(struct net_sockaddr *addr, uint16_t *port);

static inline bool net_sockaddr_cmp(const struct net_sockaddr *a, const struct net_sockaddr *b)
{
        if (a->sa_family != b->sa_family) {
                return false;
        }

        switch (a->sa_family) {
        case NET_AF_INET: {
                const struct net_sockaddr_in *a4 = net_sin(a);
                const struct net_sockaddr_in *b4 = net_sin(b);

                if (a4->sin_port != b4->sin_port) {
                        return false;
                }

                return net_ipv4_addr_cmp(&a4->sin_addr, &b4->sin_addr);
        }

        case NET_AF_INET6: {
                const struct net_sockaddr_in6 *a6 = net_sin6(a);
                const struct net_sockaddr_in6 *b6 = net_sin6(b);

                if (a6->sin6_port != b6->sin6_port) {
                        return false;
                }

                return net_ipv6_addr_cmp(&a6->sin6_addr, &b6->sin6_addr);
        }

        default:
                /* Invalid address family */
                return false;
        }
}

static inline int32_t net_tcp_seq_cmp(uint32_t seq1, uint32_t seq2)
{
        return (int32_t)(seq1 - seq2);
}

static inline bool net_tcp_seq_greater(uint32_t seq1, uint32_t seq2)
{
        return net_tcp_seq_cmp(seq1, seq2) > 0;
}

int net_bytes_from_str(uint8_t *buf, int buf_len, const char *src);

int net_tx_priority2tc(enum net_priority prio);

int net_rx_priority2tc(enum net_priority prio);

static inline enum net_priority net_vlan2priority(uint8_t priority)
{
        /* Map according to IEEE 802.1Q */
        static const uint8_t vlan2priority[] = {
                NET_PRIORITY_BE,
                NET_PRIORITY_BK,
                NET_PRIORITY_EE,
                NET_PRIORITY_CA,
                NET_PRIORITY_VI,
                NET_PRIORITY_VO,
                NET_PRIORITY_IC,
                NET_PRIORITY_NC
        };

        if (priority >= ARRAY_SIZE(vlan2priority)) {
                /* Use Best Effort as the default priority */
                return NET_PRIORITY_BE;
        }

        return (enum net_priority)vlan2priority[priority];
}

static inline uint8_t net_priority2vlan(enum net_priority priority)
{
        /* The conversion works both ways */
        return (uint8_t)net_vlan2priority(priority);
}

const char *net_family2str(net_sa_family_t family);

static inline size_t net_family2size(net_sa_family_t family)
{
        switch (family) {
        case NET_AF_INET:
                return sizeof(struct net_sockaddr_in);
        case NET_AF_INET6:
                return sizeof(struct net_sockaddr_in6);
        case NET_AF_PACKET:
                return sizeof(struct net_sockaddr_ll);
        case NET_AF_UNIX:
                return sizeof(struct net_sockaddr_un);
        case NET_AF_CAN:
                return sizeof(struct net_sockaddr_can);
        case NET_AF_NET_MGMT:
                return sizeof(struct net_sockaddr_nm);
        default:
                return 0;
        }
}

#if defined(CONFIG_NET_IPV6_PE)
int net_ipv6_pe_add_filter(struct net_in6_addr *addr, bool is_denylist);
#else
static inline int net_ipv6_pe_add_filter(struct net_in6_addr *addr,
                                         bool is_denylist)
{
        ARG_UNUSED(addr);
        ARG_UNUSED(is_denylist);

        return -ENOTSUP;
}
#endif /* CONFIG_NET_IPV6_PE */

#if defined(CONFIG_NET_IPV6_PE)
int net_ipv6_pe_del_filter(struct net_in6_addr *addr);
#else
static inline int net_ipv6_pe_del_filter(struct net_in6_addr *addr)
{
        ARG_UNUSED(addr);

        return -ENOTSUP;
}
#endif /* CONFIG_NET_IPV6_PE */

#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/net_ip.h>

#if defined(CONFIG_NET_NAMESPACE_COMPAT_MODE)
#define ZEPHYR_INCLUDE_NET_COMPAT_MODE_SYMBOLS
#include <zephyr/net/net_compat.h>
#undef ZEPHYR_INCLUDE_NET_COMPAT_MODE_SYMBOLS
#endif /* CONFIG_NET_NAMESPACE_COMPAT_MODE */


#endif /* ZEPHYR_INCLUDE_NET_NET_IP_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 39 行

在此指定虚拟局域网（VLAN）标签，以避免循环依赖（Circular Dependencies）。

### 注释 3：原第 43 行

协议族（Protocol Families）。

### 注释 4：原第 53 行

地址族（Address Families）。

### 注释 5：原第 174 行

注意：各 `net_sockaddr*` 结构体中的 `sin_port` 和 `sin6_port` 均采用网络字节序（Network Byte Order）。

### 注释 6：原第 321 行

消息头与数据的对齐（Alignment）。这些定义与体系结构有关；当前若此前尚未定义，就在此定义。

### 注释 7：原第 396 行

数据包类型（Packet Types）。

### 注释 8：原第 397 行

发给本机（To Us）。

### 注释 9：原第 398 行

发给所有设备（To All）。

### 注释 10：原第 399 行

发给组（To Group）。

### 注释 11：原第 400 行

发给其他设备（To Someone Else）。

### 注释 12：原第 401 行

由本机发出（Originated by Us）。

### 注释 13：原第 405 行

地址解析协议（ARP）的硬件标识符（Hardware Identifiers）。

### 注释 14：原第 409 行

注意：这些宏按特定顺序定义，最大的 `sockaddr` 大小排在最后。

### 注释 15：原第 438 行

将 `NET_SOCKADDR_MAX_SIZE` 定义为包含 `net_sa_family_t` 加 `char[UNIX_PATH_MAX]` 的结构体大小。

### 注释 16：原第 476 行

在这里与 `sockaddr` 相同。

### 注释 17：原第 482 行

UNIX 域套接字（UNIX Domain Sockets）的套接字地址结构体（Socket Address Struct）。

### 注释 18：原第 484 行

UNIX 地址族标识 `NET_AF_UNIX`。

### 注释 19：原第 539 行

这些内容供协议栈（Stack）内部使用。

### 注释 20：原第 712 行

IPv6 扩展头类型（Extension Header Types）。

### 注释 21：原第 733 行

UDP 消息头大小（Header Size）。

### 注释 22：原第 734 行

TCP 消息头大小（Header Size）。

### 注释 23：原第 735 行

ICMP 消息头大小（Header Size）。

### 注释 24：原第 737 行

IPv6 消息头大小（Header Size）。

### 注释 25：原第 738 行

ICMPv6 消息头大小（Header Size）。

### 注释 26：原第 739 行

IPv6 与 UDP 组合消息头（Combined Headers）。

### 注释 27：原第 740 行

IPv6 与 TCP 组合消息头（Combined Headers）。

### 注释 28：原第 741 行

ICMPv6 与 IPv6 组合消息头（Combined Headers）。

### 注释 29：原第 744 行

IPv4 消息头大小（Header Size）。

### 注释 30：原第 745 行

ICMPv4 消息头大小（Header Size）。

### 注释 31：原第 746 行

IPv4 与 UDP 组合消息头（Combined Headers）。

### 注释 32：原第 747 行

IPv4 与 TCP 组合消息头（Combined Headers）。

### 注释 33：原第 748 行

ICMPv4 与 IPv4 组合消息头（Combined Headers）。

### 注释 34：原第 750 行

IPv6 消息头中长度字段（Length Field）的偏移量。

### 注释 35：原第 752 行

13 位分片偏移字段（Fragment Offset Field）的掩码。

### 注释 36：原第 753 行

13 位分片偏移字段（Fragment Offset Field）的掩码。

### 注释 37：原第 754 行

1 位更多分片字段（More Fragments Field）的掩码。

### 注释 38：原第 755 行

1 位禁止分片字段（Do Not Fragment Field）的掩码。

### 注释 39：原第 765 行

设备名称最大长度标识 `Z_DEVICE_MAX_NAME_LEN`。

### 注释 40：原第 766 行

条件编译配置（Configuration）标记：`CONFIG_NET_INTERFACE_NAME`。

### 注释 41：原第 968 行

没有剩余位；由于起始字节相同，前缀（Prefixes）也相同。

### 注释 42：原第 974 行

创建掩码（Mask），将剩余的最高有效位全部置位。

### 注释 43：原第 1001 行

没有剩余位；由于起始字节相同，前缀（Prefixes）也相同。

### 注释 44：原第 1007 行

创建掩码（Mask），将剩余的最高有效位全部置位。

### 注释 45：原第 1107 行

地址前缀（Address Prefix）：`10.0.0.0/8`。

### 注释 46：原第 1108 行

地址前缀（Address Prefix）：`100.64.0.0/10`。

### 注释 47：原第 1109 行

地址前缀（Address Prefix）：`172.16.0.0/12`。

### 注释 48：原第 1110 行

地址前缀（Address Prefix）：`192.168.0.0/16`。

### 注释 49：原第 1111 行

地址前缀（Address Prefix）：`192.0.2.0/24`。

### 注释 50：原第 1112 行

地址前缀（Address Prefix）：`192.51.100.0/24`。

### 注释 51：原第 1113 行

地址前缀（Address Prefix）：`203.0.113.0/24`。

### 注释 52：原第 1280 行

地址前缀（Address Prefix）：`2001:db8::/32`。

### 注释 53：原第 1281 行

地址前缀（Address Prefix）：`fc00::/7`。

### 注释 54：原第 2243 行

无效地址族（Invalid Address Family）。

### 注释 55：原第 2322 行

按 IEEE 802.1Q 映射。

### 注释 56：原第 2335 行

使用尽力而为（Best Effort）作为默认优先级。

### 注释 57：原第 2351 行

转换可双向进行（Works Both Ways）。

### 注释 58：原第 2413 行

条件编译配置（Configuration）标记：`CONFIG_NET_IPV6_PE`。

### 注释 59：原第 2431 行

条件编译配置（Configuration）标记：`CONFIG_NET_IPV6_PE`。

### 注释 60：原第 2443 行

条件编译配置（Configuration）标记：`CONFIG_NET_NAMESPACE_COMPAT_MODE`。

### 注释 61：原第 2449 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_IP_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [string.h](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/byteorder.h](../byteorder_reference/P001_系统字节序头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/net/net_linkaddr.h](../api_file_system_device_reference/P029_zephyr__net__net_linkaddr.h_文件参考.md)
- [net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)
- [NET_IPPROTO_IP](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaf06819bf427cc58be1229b27b373ca31a41d4bfab7d2a68dd7b707eb70ed88b41)
- [NET_IPPROTO_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaf06819bf427cc58be1229b27b373ca31a195a3c7b388ce05b61f64c9c9be9a092)
- [NET_IPPROTO_IGMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaf06819bf427cc58be1229b27b373ca31a6ea6f123682a20c7895fd867504ada89)
- [NET_IPPROTO_ETH_P_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaf06819bf427cc58be1229b27b373ca31aebe8a029d9f87fb41c5f11b6366c1692)
- [NET_IPPROTO_IPIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaf06819bf427cc58be1229b27b373ca31ace713634caddd3efe8190dc0988b87a1)
- [NET_IPPROTO_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaf06819bf427cc58be1229b27b373ca31a0ecceb13b5404e0699fa368306aeda25)
- [NET_IPPROTO_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaf06819bf427cc58be1229b27b373ca31a3a5c18feadc81db1bf688b83120feb5a)
- [NET_IPPROTO_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaf06819bf427cc58be1229b27b373ca31acc28399f823adaa247347ab125eb37f4)
- [NET_IPPROTO_ICMPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaf06819bf427cc58be1229b27b373ca31a2ac71d272f68c66ce42ac81de4891896)
- [NET_IPPROTO_RAW](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaf06819bf427cc58be1229b27b373ca31a4d7100f9fe0efb9e8ef6cb75e8c5ac97)
- [net_ip_protocol_secure](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga721da18d2a3cfd9b3a56e9efc9f6e58b)
- [NET_IPPROTO_TLS_1_0](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga721da18d2a3cfd9b3a56e9efc9f6e58ba5d6d30723e865cab7561cc8c963c3658)
- [NET_IPPROTO_TLS_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga721da18d2a3cfd9b3a56e9efc9f6e58ba3f7f371f1d1729ad514f976f68738e47)
- [NET_IPPROTO_TLS_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga721da18d2a3cfd9b3a56e9efc9f6e58ba29ed7248420f90939300dffdd23bb07c)
- [NET_IPPROTO_TLS_1_3](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga721da18d2a3cfd9b3a56e9efc9f6e58bab13ec8077bb568971e80f9869b8d0529)
- [NET_IPPROTO_DTLS_1_0](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga721da18d2a3cfd9b3a56e9efc9f6e58baebb51afe0c7e1cfe37a330f6b0d72341)
- [NET_IPPROTO_DTLS_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga721da18d2a3cfd9b3a56e9efc9f6e58ba9ac0cafee2ab1cb5f16780fa17da5b8f)
- [NET_IPPROTO_QUIC](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga721da18d2a3cfd9b3a56e9efc9f6e58bab8506c41543969d01e4aaaa49c0932ab)
- [net_sock_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaaab4268707dbe08348b98fb028e7aa5c)
- [NET_SOCK_STREAM](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaaab4268707dbe08348b98fb028e7aa5ca6f049fea24a6d2d5279e736ececf3c83)
- [NET_SOCK_DGRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaaab4268707dbe08348b98fb028e7aa5caff1fd09b4fa81b8e0e8a73132c8fa3e4)
- [NET_SOCK_RAW](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaaab4268707dbe08348b98fb028e7aa5ca892feaa0f7556622a3491683e69b6ac2)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [s6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md#adfee3135d20aa7b5252aab9b9803bcd7)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [s6_addr16](../network_core_model_reference/P094_net_in6_addr_结构体.md#a18fb132bfd7ac8945a981b8bb76e83ed)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [s6_addr32](../network_core_model_reference/P094_net_in6_addr_结构体.md#ac2d541ca17ee6fa482765014f447f41a)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [s4_addr](../network_core_model_reference/P096_net_in_addr_结构体.md#adca8424f8e83574c7f7d57a2138e7b8c)
- [s4_addr16](../network_core_model_reference/P096_net_in_addr_结构体.md#aac03b71ad3fbe365fa80a1f0a8b53cc5)
- [s4_addr32](../network_core_model_reference/P096_net_in_addr_结构体.md#ac8181820613973fc7d6b5db0e3e53abd)
- [s_addr](../network_core_model_reference/P096_net_in_addr_结构体.md#ad3ca9f01bd03dbe69617eae95743bfa4)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [net_sockaddr_in6](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md)
- [sin6_family](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md#a38d03d2142c103f21726389952d969b9)
- [sin6_port](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md#abd547e6daf4a9dd86a5c8349c0b80b04)
- [sin6_addr](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md#a0f3796809a828ca81f097cdbd9f923c5)
- [sin6_scope_id](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md#a7fd7828614ca34044d5e05f446e37683)
- [net_sockaddr_in](../network_core_model_reference/P119_net_sockaddr_in_结构体.md)
- [sin_family](../network_core_model_reference/P119_net_sockaddr_in_结构体.md#a5acd06c9decdae8344c05d32b47746b1)
- [sin_port](../network_core_model_reference/P119_net_sockaddr_in_结构体.md#a099706d7572442b073f9efffe3df7000)
- [sin_addr](../network_core_model_reference/P119_net_sockaddr_in_结构体.md#a3cd81a45a4c8bc3ab18247378aeee123)
- [net_sockaddr_ll](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md)
- [sll_family](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#a8c7064a9685e009f179a2582af50c198)
- [sll_protocol](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#acee20fa52f5544b0675064ff7c8c08ed)
- [sll_ifindex](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#a7dc05521a96c49b14dfbb178ab6ca14a)
- [sll_hatype](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#a917c8c2df6482ae6427ced625bc00555)
- [sll_pkttype](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#a40552f91379790433041e2620d7800d7)
- [sll_halen](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#ac575672a144a28f49b3e63ee157ec8c9)
- [sll_addr](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#aff9f7cf10eaceab03a9ce582c2d76fea)
- [net_sockaddr_can](../network_core_model_reference/P118_net_sockaddr_can_结构体.md)
- [can_family](../network_core_model_reference/P118_net_sockaddr_can_结构体.md#a7e25be69230e5887a8326e991ddba6e0)
- [can_ifindex](../network_core_model_reference/P118_net_sockaddr_can_结构体.md#a597d33def7c50f84f2b17c320b7ca6c5)
- [net_sockaddr_nm](../network_core_model_reference/P122_net_sockaddr_nm_结构体.md)
- [nm_family](../network_core_model_reference/P122_net_sockaddr_nm_结构体.md#aeaef27e6db3cca162dfd66337ccb629b)
- [nm_ifindex](../network_core_model_reference/P122_net_sockaddr_nm_结构体.md#a78e154af8b9530de3b12743115c91792)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [nm_pid](../network_core_model_reference/P122_net_sockaddr_nm_结构体.md#ad2f9976b5c6e46f8969e83bbcefdbeb9)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [nm_mask](../network_core_model_reference/P122_net_sockaddr_nm_结构体.md#a62ab3cea810b51107cc92cf43b2de6d9)
- [net_iovec](../network_core_model_reference/P098_net_iovec_结构体.md)
- [iov_base](../network_core_model_reference/P098_net_iovec_结构体.md#a85bbdc499845cf65f24e485ffb4220b8)
- [iov_len](../network_core_model_reference/P098_net_iovec_结构体.md#a9d64976623638c5856ff0bb76e41fe73)
- [net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)
- [msg_name](../network_core_model_reference/P112_net_msghdr_结构体.md#a8f46d780cccad65cc755fb71eacf52ea)
- [msg_namelen](../network_core_model_reference/P112_net_msghdr_结构体.md#a38ea33c4a18d07022b89129107b6ffa5)
- [msg_iov](../network_core_model_reference/P112_net_msghdr_结构体.md#a1263d9b8942042b7cf21727f8312ff7d)
- [msg_iovlen](../network_core_model_reference/P112_net_msghdr_结构体.md#adbadc26695f3646aae690721e99d558a)
- [msg_control](../network_core_model_reference/P112_net_msghdr_结构体.md#a6e12f22fc1750226e706e64529bb84bd)
- [msg_controllen](../network_core_model_reference/P112_net_msghdr_结构体.md#a66dcca1e90e25dabe949842873b6edc4)
- [msg_flags](../network_core_model_reference/P112_net_msghdr_结构体.md#a0a07694671a1725d5ec8af16de3d6778)
- [net_cmsghdr](../network_core_model_reference/P052_net_cmsghdr_结构体.md)
- [cmsg_len](../network_core_model_reference/P052_net_cmsghdr_结构体.md#a306a55e0b7ab30d6258c71e92566f727)
- [cmsg_level](../network_core_model_reference/P052_net_cmsghdr_结构体.md#a3f8abb9fbf85597c885ac045df9492b5)
- [cmsg_type](../network_core_model_reference/P052_net_cmsghdr_结构体.md#aa44e7136defe85d81bec20aa00cc6668)
- [cmsg_data](../network_core_model_reference/P052_net_cmsghdr_结构体.md#aee333d1c9f262de2135a9bed3bca1d98)
- [net_linger](../network_core_model_reference/P104_net_linger_结构体.md)
- [l_onoff](../network_core_model_reference/P104_net_linger_结构体.md#a8e93ff6b67e724cb24de03c21c5f99af)
- [l_linger](../network_core_model_reference/P104_net_linger_结构体.md#a9dab7be2bea49133c219cdfb154e9fdf)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [sa_family](../network_core_model_reference/P117_net_sockaddr_结构体.md#a5cf76ac4582ea3c90fc871a44656490a)
- [SOCKADDR_ALIGN](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga929a6597b2a4669e42cb416a84fd568f)
- [in6_addr](../api_file_reference/P158_zephyr__posix__netinet__in.h_文件参考.md#a75e4bdec5e6afb661e8cbae72452fde7)
- [in_addr](../api_file_reference/P158_zephyr__posix__netinet__in.h_文件参考.md#a73e57c1190f8731fb8b0217f929c4e1b)
- [net_ip_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga7a207761e4879c140f48f93978cb2f0b)
- [NET_IPV6_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c)
- [NET_IPV4_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1)
- [net_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae87ef466e77ded673ed7e593d3eddffd)
- [NET_PRIORITY_BK](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b)
- [NET_PRIORITY_BE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce)
- [NET_PRIORITY_EE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0)
- [NET_PRIORITY_CA](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354)
- [NET_PRIORITY_VI](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792)
- [NET_PRIORITY_VO](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a)
- [NET_PRIORITY_IC](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05)
- [NET_PRIORITY_NC](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef)
- [net_tuple](../network_core_model_reference/P156_net_tuple_结构体.md)
- [remote_addr](../network_core_model_reference/P156_net_tuple_结构体.md#a8f9a1aab3c3aedeead795ca6624d4d6d)
- [local_addr](../network_core_model_reference/P156_net_tuple_结构体.md#af7004f8f8d74d49d6771393825612294)
- [remote_port](../network_core_model_reference/P156_net_tuple_结构体.md#ab4c31093a23bc60d8dcf5b784e3fb39a)
- [local_port](../network_core_model_reference/P156_net_tuple_结构体.md#a9a1cd0dd55a9e866cb0e910120362b7e)
- [ip_proto](../network_core_model_reference/P156_net_tuple_结构体.md#aa9eeba2c8e263afbf6368e04353d6014)
- [net_addr_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga32e58fc83532ef57eeb6ff952f17288d)
- [NET_ADDR_ANY_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df)
- [NET_ADDR_TENTATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9)
- [NET_ADDR_PREFERRED](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a)
- [NET_ADDR_DEPRECATED](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3)
- [net_addr_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gafecee2d4a331dc85ad962b81a6303e41)
- [NET_ADDR_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6)
- [NET_ADDR_AUTOCONF](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006)
- [NET_ADDR_DHCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db)
- [NET_ADDR_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e)
- [NET_ADDR_OVERRIDABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4)
- [NET_IPV6_ADDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga1eefdabf590090be9f98bdf4a2f43bb4)
- [NET_IPV4_ADDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga10a82ea9ba9ca19f3b773bdd53c978e0)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [net_ifreq](../network_core_model_reference/P093_net_ifreq_结构体.md)
- [ifr_name](../network_core_model_reference/P093_net_ifreq_结构体.md#ad3147844bf168ff8f19893e89e3d04dd)
- [net_in_pktinfo](../network_core_model_reference/P097_net_in_pktinfo_结构体.md)
- [ipi_ifindex](../network_core_model_reference/P097_net_in_pktinfo_结构体.md#a00e5cde6d36f127d2f0710c541038ca0)
- [ipi_spec_dst](../network_core_model_reference/P097_net_in_pktinfo_结构体.md#ad1fb0298ae64454f28f7e4b6738bf7fe)
- [ipi_addr](../network_core_model_reference/P097_net_in_pktinfo_结构体.md#a75c8fff8b98862aef9ceba341b9276fe)
- [net_ip_mreqn](../network_core_model_reference/P100_net_ip_mreqn_结构体.md)
- [imr_multiaddr](../network_core_model_reference/P100_net_ip_mreqn_结构体.md#ac0ac21d6427ca1654eefe6fb903c4d99)
- [imr_address](../network_core_model_reference/P100_net_ip_mreqn_结构体.md#abb6dbf4f2aae8fe0e3fc4ec5b6d0fdf8)
- [imr_ifindex](../network_core_model_reference/P100_net_ip_mreqn_结构体.md#a3d89352335683bfcda267b47c591ba1f)
- [net_ip_mreq](../network_core_model_reference/P099_net_ip_mreq_结构体.md)
- [imr_multiaddr](../network_core_model_reference/P099_net_ip_mreq_结构体.md#a1bef08a9e287288095ae7589489bbbb8)
- [imr_interface](../network_core_model_reference/P099_net_ip_mreq_结构体.md#a9c4f5c84afbfd49f20bef330ade6a88a)
- [net_ipv6_mreq](../network_core_model_reference/P102_net_ipv6_mreq_结构体.md)
- [ipv6mr_multiaddr](../network_core_model_reference/P102_net_ipv6_mreq_结构体.md#a17fd782a854df2a8c793aaec9892420d)
- [ipv6mr_ifindex](../network_core_model_reference/P102_net_ipv6_mreq_结构体.md#a3903141b4b67e2dfc977b3fad38d24a8)
- [net_packet_mreq](../network_core_model_reference/P113_net_packet_mreq_结构体.md)
- [mr_ifindex](../network_core_model_reference/P113_net_packet_mreq_结构体.md#a87a230e77612ab9bd25b6d5d6021615c)
- [mr_type](../network_core_model_reference/P113_net_packet_mreq_结构体.md#a0f775f8c4c00a0f6ffd5f14b82379133)
- [mr_alen](../network_core_model_reference/P113_net_packet_mreq_结构体.md#a5f4e8579b69cd082baa79ffa3f3ab77f)
- [mr_address](../network_core_model_reference/P113_net_packet_mreq_结构体.md#a382435d63e1ffda9197ca3984629e31d)
- [NET_LINK_ADDR_MAX_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga5680cf2ac9302bbee824148f36193b2b)
- [net_in6_pktinfo](../network_core_model_reference/P095_net_in6_pktinfo_结构体.md)
- [ipi6_addr](../network_core_model_reference/P095_net_in6_pktinfo_结构体.md#af16fc143121a3557d338f8476fb0d0dd)
- [ipi6_ifindex](../network_core_model_reference/P095_net_in6_pktinfo_结构体.md#a471aed9984659549af97a694685869a3)
- [net_ntohl](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae18466011462c20add53de2e01505b92)
- [net_ipv6_is_addr_loopback](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga9af9b1750c2db50a170e1b694df24227)
- [net_ipv6_is_addr_mcast](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga418a57b9f12205de21cbe83951e960bb)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_if_config](../network_core_model_reference/P082_net_if_config_结构体.md)
- [net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)
- [net_if_ipv6_addr_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga4314c59af790e537e384e969c58fab9d)
- [net_ipv6_is_my_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga9495dd7d6ef4a3251f0ba3a7508522d5)
- [net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)
- [net_if_ipv6_maddr_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gad520342d393f523c56a98fa618876b54)
- [net_ipv6_is_my_maddr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga19bff1dd7eb407e25842ce28e04b08d9)
- [net_ipv6_is_prefix](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga9654007b0a3c4d033df1ec3d00bd26ee)
- [memcmp](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md#ad8bfbfa1e4ad284ded921dd775735521)
- [net_ipv6_addr_prefix_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga4e91a4298604a916731bf591acc7b326)
- [memset](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md#a4137694174d4ca2fad886a1db355015c)
- [memcpy](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md#af0f01bffcd16daa9143f6014d10a25ad)
- [net_ipv4_is_addr_loopback](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga6379fc7d08ed2668ac917fd370a80ef1)
- [net_ipv4_is_addr_unspecified](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga403e318543fe3707bc9773b9b646610a)
- [net_ipv4_is_addr_mcast](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga2f25895894c9a24467000118464a8ffe)
- [net_ipv4_is_ll_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga6651e4feab1a236888e85049a9ef8066)
- [net_ipv4_is_private_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gadce220ef01f6f329152e74f2143cbaa3)
- [net_ipv4_addr_copy_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf731738fb1761208739976d767736f87)
- [net_ipaddr_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga75ffcc08e621c2d47d1ae043fce2acad)
- [net_ipv6_addr_copy_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga4925e6f3734b8fc1d9cb1ca1a510b5f1)
- [net_ipv4_addr_cmp_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga32ffb42c62169ac9b34a0faa7c7ffd12)
- [net_ipv4_addr_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga204eae0889a15f6369da607a705cb059)
- [net_ipv6_addr_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga6704d86fb9962bdb6d27a41d4053bfc7)
- [net_ipv6_addr_cmp_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gafbe40461a645cf11fc8b3a07e1d9156e)
- [net_htons](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae20291eed240d648d0ef7e13822f925f)
- [net_ipv6_is_ll_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gad072b3bf7bc05927fe27f5503a31f25c)
- [net_ipv6_is_sl_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaec37f4f9d223e5be3c141ec1ae4ef288)
- [net_ipv6_is_ula_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga096d280f0373e50c4d40fb1b3dac2b2c)
- [net_ipv6_is_global_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gab2d4e2746a080ff0dfbb67a8e09c15b4)
- [net_ipv6_is_private_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga3d471601814ad2f4c2f9e6fb91055067)
- [net_ipv6_unspecified_address](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf41e178ed45d6a483e240f939cd2f41d)
- [net_ipv4_unspecified_address](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gac01309e4ca866366921148fa9ef74b4f)
- [net_ipv4_broadcast_address](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga1d87e71e47d20a815dfd6acedb27bb98)
- [net_if_ipv4_addr_mask_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga919149bde5d0f1319ba60a9b8de1a1bc)
- [net_ipv4_addr_mask_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga49d57fb1fa9db8f5fb357daab9b5cc87)
- [net_if_ipv4_is_addr_bcast](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga45774258112186b5989b974df934dff1)
- [net_ipv4_is_addr_bcast](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaff4efbe342d50083aaf33c994d864fcd)
- [net_if_ipv4_addr_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga53fb4ce0130fc8d665ddfd466d2a5eb8)
- [net_ipv4_is_my_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga62623cbb70b70c87c05ba25cfd4b06c0)
- [net_ipv6_is_addr_unspecified](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga2a2c730105721706af1fddad5bf9be2e)
- [net_htonl](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga5d9e16e8f439be6f94fb3f72de13bdac)
- [net_ipv6_is_addr_solicited_node](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaacd8f2ea7894a0abb7a3d43a1ef60c29)
- [net_ipv6_is_addr_mcast_scope](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga91b134a31f3e29889a11bd3da518c483)
- [net_ipv6_is_same_mcast_scope](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gac2616b300be2e4b7ed7e0ddffa5234f1)
- [net_ipv6_get_addr_mcast_scope](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga7fe843d70cbb04a6f4c022483346ad23)
- [net_ipv6_is_addr_mcast_global](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf91b9c08e327589eb0fd33d5754743cf)
- [net_ipv6_is_addr_mcast_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga43b6e313f5a938d688d3bc734a299408)
- [net_ipv6_is_addr_mcast_link](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae1660acfdbf897afbc6119ae608e476f)
- [net_ipv6_is_addr_mcast_mesh](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga2a508682693ec99b8006a1a1026772ea)
- [net_ipv6_is_addr_mcast_site](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga9084b403ca6a591d24f975e669560b6c)
- [net_ipv6_is_addr_mcast_org](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga9e7bf1c3503039c78f99f3deab277d4f)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [net_ipv6_is_addr_mcast_group](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaa559a6315ce432c9bc180b14cafa978f)
- [net_ipv6_is_addr_mcast_all_nodes_group](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gac20bcc70c84cff88fa68e1ab583da35f)
- [net_ipv6_is_addr_mcast_iface_all_nodes](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae9ac492caeb14ab3796fcbb752c6d7f1)
- [net_ipv6_is_addr_mcast_link_all_nodes](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gabc3691a9ff73dcadadf52ec740cb0e99)
- [net_ipv6_addr_create_solicited_node](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gadf685d461f89090441348d2028082078)
- [net_ipv6_addr_create](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaaed285ea1b276ad90404957560f82c77)
- [net_ipv6_addr_create_ll_allnodes_mcast](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga677fe0c0ebe6bcdd6a7a7d7805841671)
- [net_ipv6_addr_create_ll_allrouters_mcast](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae20b3c01d1ee1fe7526b58eb4c0bf98c)
- [net_ipv6_addr_create_v4_mapped](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga2a9657d756c655322d960ef54f4b9ac4)
- [net_ntohs](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga4837ff0eece26b00ae46ed7c16997a97)
- [net_ipv6_addr_is_v4_mapped](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga2716cdb6f85693d7c5a96446a7a41e03)
- [net_ipv6_addr_get_v4_mapped](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga744f26c0e560ba2b6682c40c27b53f62)
- [net_ipv6_addr_generate_iid](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga5aef9855e39e03a4ce2d6626040c8ae9)
- [net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)
- [net_ipv6_addr_create_iid](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga871cb575f79b9e53834c13bfc9e5bd82)
- [len](../network_core_model_reference/P105_net_linkaddr_结构体.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)
- [addr](../network_core_model_reference/P105_net_linkaddr_结构体.md#a58de2645f8c7d31c97026f0bd5262881)
- [type](../network_core_model_reference/P105_net_linkaddr_结构体.md#a5f5b4c3d353261d0fab8011aa09f00d7)
- [NET_LINK_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)
- [net_ipv6_addr_based_on_ll](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga7946673bd60ca80392d4440e23028f54)
- [net_sad](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga13b4094cc06599c9af46e5e68e1c3bc3)
- [net_sas](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga83d4270557a164eef75e1ae656470ef1)
- [net_sin6](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga4e7578614f7f0660c5a62d7746a3772c)
- [net_sin](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf92aa225bda78a3e016f6120b60c8885)
- [net_sin6_ptr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gad4ed43b91fbaa2844fa509c603fafae6)
- [net_sin_ptr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga6943b9d84c55709aaad323c1127a1949)
- [net_sll_ptr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8846a826e8b69c01fc92239a596ca002)
- [net_can_ptr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gab1b5d776e0b10043c0538629ed4a5b8b)
- [net_addr_pton](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga63f48d08fc2811198739ce20a72584df)
- [net_addr_ntop](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gafbc331616a5360c68804e8bc2f653cdd)
- [net_mask_len_to_netmask](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga646cd9e85f7110bc45dc276bf8e31ef1)
- [net_netmask_to_mask_len](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga84d11fc7badd399d2c164ed21baa87c9)
- [net_ipaddr_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga9086c7f94792f5af574b6eb14a6261b1)
- [net_ipaddr_parse_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga5e1650330284b6e295e5f714037b1d65)
- [net_port_set_default](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga45f18bd1ec2040f9f21b5aaf4ffe696d)
- [net_port_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga78436f11373210789ed9d5d640c6daf7)
- [net_port_get](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga0b67ffabad5b8a10da72301681206b31)
- [net_sockaddr_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8047c58777b659f8a8cdb2f24ca24355)
- [NET_AF_INET](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gac53da21004b2bdc93b878da2ec4590bd)
- [NET_AF_INET6](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga502492205736b373fa35c0524ba3d4e6)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [net_tcp_seq_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga1695009388402938dcc2e49b526ebd1f)
- [net_tcp_seq_greater](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaa77b299f53e5535ac4c4bea1b6531a34)
- [net_bytes_from_str](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b794f251cf8412c769ab415902a9f32)
- [net_tx_priority2tc](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae74c9ba7ff4addbce7f931bd6fa91fa0)
- [net_rx_priority2tc](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga7b3c41ae9b3962090d72c130a9fa61b1)
- [net_vlan2priority](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga14bc7018e3dd7c3e320b44a077343ce4)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)
- [net_priority2vlan](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8be77d043d4d1d29e0879b3b22274629)
- [net_family2str](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga4c35814a1f56101f96e790d0dc97925b)
- [net_family2size](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga0d22051f0ff5545b9b08e133804389f1)
- [NET_AF_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga090f4770cd630517b5391d36e3705e41)
- [NET_AF_UNIX](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga88930e91e400b4eca0a9392288490268)
- [NET_AF_CAN](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga1df641bd5978219a7da51ea25ea8ac2f)
- [NET_AF_NET_MGMT](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga209390ff940aa0f0746c3a4fd4e98806)
- [net_ipv6_pe_add_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaa1f6ecf0788bac4ca943011f0ad87fb9)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [net_ipv6_pe_del_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gac3bb5fb48ed95d43a7beb2e4f7c1c6d0)
- [zephyr/net/net_compat.h](../api_file_supplement_reference/P077_zephyr__net__net_compat.h_文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [net_compat.h](../api_file_supplement_reference/P077_zephyr__net__net_compat.h_文件参考.md)
- [net_linkaddr.h](../api_file_system_device_reference/P029_zephyr__net__net_linkaddr.h_文件参考.md)
- [net_cmsghdr::cmsg_len](../network_core_model_reference/P052_net_cmsghdr_结构体.md#a306a55e0b7ab30d6258c71e92566f727)
- [net_cmsghdr::cmsg_level](../network_core_model_reference/P052_net_cmsghdr_结构体.md#a3f8abb9fbf85597c885ac045df9492b5)
- [net_cmsghdr::cmsg_type](../network_core_model_reference/P052_net_cmsghdr_结构体.md#aa44e7136defe85d81bec20aa00cc6668)
- [net_cmsghdr::cmsg_data](../network_core_model_reference/P052_net_cmsghdr_结构体.md#aee333d1c9f262de2135a9bed3bca1d98)
- [net_ifreq::ifr_name](../network_core_model_reference/P093_net_ifreq_结构体.md#ad3147844bf168ff8f19893e89e3d04dd)
- [net_in6_addr::s6_addr16](../network_core_model_reference/P094_net_in6_addr_结构体.md#a18fb132bfd7ac8945a981b8bb76e83ed)
- [net_in6_addr::s6_addr32](../network_core_model_reference/P094_net_in6_addr_结构体.md#ac2d541ca17ee6fa482765014f447f41a)
- [net_in6_addr::s6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md#adfee3135d20aa7b5252aab9b9803bcd7)
- [net_in6_pktinfo::ipi6_ifindex](../network_core_model_reference/P095_net_in6_pktinfo_结构体.md#a471aed9984659549af97a694685869a3)
- [net_in6_pktinfo::ipi6_addr](../network_core_model_reference/P095_net_in6_pktinfo_结构体.md#af16fc143121a3557d338f8476fb0d0dd)
- [net_in_addr::s4_addr16](../network_core_model_reference/P096_net_in_addr_结构体.md#aac03b71ad3fbe365fa80a1f0a8b53cc5)
- [net_in_addr::s4_addr32](../network_core_model_reference/P096_net_in_addr_结构体.md#ac8181820613973fc7d6b5db0e3e53abd)
- [net_in_addr::s_addr](../network_core_model_reference/P096_net_in_addr_结构体.md#ad3ca9f01bd03dbe69617eae95743bfa4)
- [net_in_addr::s4_addr](../network_core_model_reference/P096_net_in_addr_结构体.md#adca8424f8e83574c7f7d57a2138e7b8c)
- [net_in_pktinfo::ipi_ifindex](../network_core_model_reference/P097_net_in_pktinfo_结构体.md#a00e5cde6d36f127d2f0710c541038ca0)
- [net_in_pktinfo::ipi_addr](../network_core_model_reference/P097_net_in_pktinfo_结构体.md#a75c8fff8b98862aef9ceba341b9276fe)
- [net_in_pktinfo::ipi_spec_dst](../network_core_model_reference/P097_net_in_pktinfo_结构体.md#ad1fb0298ae64454f28f7e4b6738bf7fe)
- [net_iovec::iov_base](../network_core_model_reference/P098_net_iovec_结构体.md#a85bbdc499845cf65f24e485ffb4220b8)
- [net_iovec::iov_len](../network_core_model_reference/P098_net_iovec_结构体.md#a9d64976623638c5856ff0bb76e41fe73)
- [net_ip_mreq::imr_multiaddr](../network_core_model_reference/P099_net_ip_mreq_结构体.md#a1bef08a9e287288095ae7589489bbbb8)
- [net_ip_mreq::imr_interface](../network_core_model_reference/P099_net_ip_mreq_结构体.md#a9c4f5c84afbfd49f20bef330ade6a88a)
- [net_ip_mreqn::imr_ifindex](../network_core_model_reference/P100_net_ip_mreqn_结构体.md#a3d89352335683bfcda267b47c591ba1f)
- [net_ip_mreqn::imr_address](../network_core_model_reference/P100_net_ip_mreqn_结构体.md#abb6dbf4f2aae8fe0e3fc4ec5b6d0fdf8)
- [net_ip_mreqn::imr_multiaddr](../network_core_model_reference/P100_net_ip_mreqn_结构体.md#ac0ac21d6427ca1654eefe6fb903c4d99)
- [net_ipv6_mreq::ipv6mr_multiaddr](../network_core_model_reference/P102_net_ipv6_mreq_结构体.md#a17fd782a854df2a8c793aaec9892420d)
- [net_ipv6_mreq::ipv6mr_ifindex](../network_core_model_reference/P102_net_ipv6_mreq_结构体.md#a3903141b4b67e2dfc977b3fad38d24a8)
- [net_linger::l_onoff](../network_core_model_reference/P104_net_linger_结构体.md#a8e93ff6b67e724cb24de03c21c5f99af)
- [net_linger::l_linger](../network_core_model_reference/P104_net_linger_结构体.md#a9dab7be2bea49133c219cdfb154e9fdf)
- [net_linkaddr::addr](../network_core_model_reference/P105_net_linkaddr_结构体.md#a58de2645f8c7d31c97026f0bd5262881)
- [net_linkaddr::type](../network_core_model_reference/P105_net_linkaddr_结构体.md#a5f5b4c3d353261d0fab8011aa09f00d7)
- [net_linkaddr::len](../network_core_model_reference/P105_net_linkaddr_结构体.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)
- [net_msghdr::msg_flags](../network_core_model_reference/P112_net_msghdr_结构体.md#a0a07694671a1725d5ec8af16de3d6778)
- [net_msghdr::msg_iov](../network_core_model_reference/P112_net_msghdr_结构体.md#a1263d9b8942042b7cf21727f8312ff7d)
- [net_msghdr::msg_namelen](../network_core_model_reference/P112_net_msghdr_结构体.md#a38ea33c4a18d07022b89129107b6ffa5)
- [net_msghdr::msg_controllen](../network_core_model_reference/P112_net_msghdr_结构体.md#a66dcca1e90e25dabe949842873b6edc4)
- [net_msghdr::msg_control](../network_core_model_reference/P112_net_msghdr_结构体.md#a6e12f22fc1750226e706e64529bb84bd)
- [net_msghdr::msg_name](../network_core_model_reference/P112_net_msghdr_结构体.md#a8f46d780cccad65cc755fb71eacf52ea)
- [net_msghdr::msg_iovlen](../network_core_model_reference/P112_net_msghdr_结构体.md#adbadc26695f3646aae690721e99d558a)
- [net_packet_mreq::mr_type](../network_core_model_reference/P113_net_packet_mreq_结构体.md#a0f775f8c4c00a0f6ffd5f14b82379133)
- [net_packet_mreq::mr_address](../network_core_model_reference/P113_net_packet_mreq_结构体.md#a382435d63e1ffda9197ca3984629e31d)
- [net_packet_mreq::mr_alen](../network_core_model_reference/P113_net_packet_mreq_结构体.md#a5f4e8579b69cd082baa79ffa3f3ab77f)
- [net_packet_mreq::mr_ifindex](../network_core_model_reference/P113_net_packet_mreq_结构体.md#a87a230e77612ab9bd25b6d5d6021615c)
- [net_sockaddr_can::can_ifindex](../network_core_model_reference/P118_net_sockaddr_can_结构体.md#a597d33def7c50f84f2b17c320b7ca6c5)
- [net_sockaddr_can::can_family](../network_core_model_reference/P118_net_sockaddr_can_结构体.md#a7e25be69230e5887a8326e991ddba6e0)
- [net_sockaddr_in6::sin6_addr](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md#a0f3796809a828ca81f097cdbd9f923c5)
- [net_sockaddr_in6::sin6_family](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md#a38d03d2142c103f21726389952d969b9)
- [net_sockaddr_in6::sin6_scope_id](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md#a7fd7828614ca34044d5e05f446e37683)
- [net_sockaddr_in6::sin6_port](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md#abd547e6daf4a9dd86a5c8349c0b80b04)
- [net_sockaddr_in::sin_port](../network_core_model_reference/P119_net_sockaddr_in_结构体.md#a099706d7572442b073f9efffe3df7000)
- [net_sockaddr_in::sin_addr](../network_core_model_reference/P119_net_sockaddr_in_结构体.md#a3cd81a45a4c8bc3ab18247378aeee123)
- [net_sockaddr_in::sin_family](../network_core_model_reference/P119_net_sockaddr_in_结构体.md#a5acd06c9decdae8344c05d32b47746b1)
- [net_sockaddr_ll::sll_pkttype](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#a40552f91379790433041e2620d7800d7)
- [net_sockaddr_ll::sll_ifindex](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#a7dc05521a96c49b14dfbb178ab6ca14a)
- [net_sockaddr_ll::sll_family](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#a8c7064a9685e009f179a2582af50c198)
- [net_sockaddr_ll::sll_hatype](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#a917c8c2df6482ae6427ced625bc00555)
- [net_sockaddr_ll::sll_halen](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#ac575672a144a28f49b3e63ee157ec8c9)
- [net_sockaddr_ll::sll_protocol](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#acee20fa52f5544b0675064ff7c8c08ed)
- [net_sockaddr_ll::sll_addr](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md#aff9f7cf10eaceab03a9ce582c2d76fea)
- [net_sockaddr_nm::nm_mask](../network_core_model_reference/P122_net_sockaddr_nm_结构体.md#a62ab3cea810b51107cc92cf43b2de6d9)
- [net_sockaddr_nm::nm_ifindex](../network_core_model_reference/P122_net_sockaddr_nm_结构体.md#a78e154af8b9530de3b12743115c91792)
- [net_sockaddr_nm::nm_pid](../network_core_model_reference/P122_net_sockaddr_nm_结构体.md#ad2f9976b5c6e46f8969e83bbcefdbeb9)
- [net_sockaddr_nm::nm_family](../network_core_model_reference/P122_net_sockaddr_nm_结构体.md#aeaef27e6db3cca162dfd66337ccb629b)
- [net_sockaddr::sa_family](../network_core_model_reference/P117_net_sockaddr_结构体.md#a5cf76ac4582ea3c90fc871a44656490a)
- [net_tuple::remote_addr](../network_core_model_reference/P156_net_tuple_结构体.md#a8f9a1aab3c3aedeead795ca6624d4d6d)
- [net_tuple::local_port](../network_core_model_reference/P156_net_tuple_结构体.md#a9a1cd0dd55a9e866cb0e910120362b7e)
- [net_tuple::ip_proto](../network_core_model_reference/P156_net_tuple_结构体.md#aa9eeba2c8e263afbf6368e04353d6014)
- [net_tuple::remote_port](../network_core_model_reference/P156_net_tuple_结构体.md#ab4c31093a23bc60d8dcf5b784e3fb39a)
- [net_tuple::local_addr](../network_core_model_reference/P156_net_tuple_结构体.md#af7004f8f8d74d49d6771393825612294)
- [byteorder.h](../byteorder_reference/P001_系统字节序头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P004_protocol.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_net_pkt.h_源码浏览.md)
