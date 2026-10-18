---
id: learning.zephyr-docs.api-source-system-reference.page-22
title: net_context.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__context_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_net\_context.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__context_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__context_8h.html)。

## 22.1\_原始可见代码（Source Code）

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
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
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
<a id="l00057"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="foldopen00207"></a>
<a id="l00207"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00447"></a>
<a id="l00449"></a>
<a id="l00451"></a>
<a id="l00453"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00458"></a>
<a id="l00460"></a>
<a id="l00462"></a>
<a id="l00464"></a>
<a id="l00466"></a>
<a id="l00468"></a>
<a id="l00470"></a>
<a id="l00472"></a>
<a id="l00474"></a>
<a id="l00476"></a>
<a id="l00478"></a>
<a id="l00480"></a>
<a id="l00482"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00500"></a>
<a id="l00501"></a>
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
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="foldopen00528"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="foldopen00542"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="foldopen00557"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00570"></a>
<a id="l00580"></a>
<a id="foldopen00581"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="foldopen00598"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="foldopen00618"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="foldopen00634"></a>
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
<a id="l00660"></a>
<a id="foldopen00661"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="foldopen00677"></a>
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
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="foldopen00709"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="foldopen00734"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="foldopen00752"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="foldopen00767"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00783"></a>
<a id="foldopen00784"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="foldopen00799"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="foldopen00816"></a>
<a id="l00816"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="foldopen00836"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="foldopen00850"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00852"></a>
<a id="l00853"></a>
<a id="l00854"></a>
<a id="l00855"></a>
<a id="foldopen00866"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00869"></a>
<a id="l00870"></a>
<a id="foldopen00880"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="foldopen00928"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="foldopen00941"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="foldopen00957"></a>
<a id="l00957"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00961"></a>
<a id="foldopen00971"></a>
<a id="l00971"></a>
<a id="l00972"></a>
<a id="l00973"></a>
<a id="l00974"></a>
<a id="l00975"></a>
<a id="l00976"></a>
<a id="l00977"></a>
<a id="l00978"></a>
<a id="l00989"></a>
<a id="l00990"></a>
<a id="l00991"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l01003"></a>
<a id="l01004"></a>
<a id="l01005"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="l01009"></a>
<a id="l01010"></a>
<a id="l01020"></a>
<a id="l01021"></a>
<a id="l01022"></a>
<a id="l01023"></a>
<a id="l01024"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="foldopen01027"></a>
<a id="l01027"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="l01032"></a>
<a id="l01033"></a>
<a id="l01034"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="foldopen01051"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01054"></a>
<a id="l01055"></a>
<a id="l01056"></a>
<a id="l01057"></a>
<a id="l01075"></a>
<a id="l01076"></a>
<a id="l01077"></a>
<a id="l01078"></a>
<a id="l01079"></a>
<a id="l01093"></a>
<a id="l01094"></a>
<a id="l01107"></a>
<a id="l01108"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="foldopen01132"></a>
<a id="l01132"></a>
<a id="l01133"></a>
<a id="l01134"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01151"></a>
<a id="l01152"></a>
<a id="l01153"></a>
<a id="l01154"></a>
<a id="l01155"></a>
<a id="l01156"></a>
<a id="foldopen01157"></a>
<a id="l01157"></a>
<a id="l01158"></a>
<a id="l01159"></a>
<a id="l01160"></a>
<a id="l01161"></a>
<a id="l01162"></a>
<a id="l01163"></a>
<a id="l01164"></a>
<a id="l01165"></a>
<a id="l01176"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="l01179"></a>
<a id="l01180"></a>
<a id="l01181"></a>
<a id="foldopen01182"></a>
<a id="l01182"></a>
<a id="l01183"></a>
<a id="l01184"></a>
<a id="l01185"></a>
<a id="l01186"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="l01191"></a>
<a id="l01192"></a>
<a id="l01193"></a>
<a id="l01194"></a>
<a id="l01206"></a>
<a id="l01207"></a>
<a id="l01208"></a>
<a id="l01209"></a>
<a id="l01220"></a>
<a id="l01221"></a>
<a id="l01222"></a>
<a id="l01251"></a>
<a id="l01252"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01283"></a>
<a id="l01284"></a>
<a id="l01285"></a>
<a id="l01286"></a>
<a id="l01287"></a>
<a id="l01307"></a>
<a id="l01308"></a>
<a id="l01309"></a>
<a id="l01310"></a>
<a id="l01311"></a>
<a id="l01312"></a>
<a id="l01313"></a>
<a id="l01335"></a>
<a id="l01336"></a>
<a id="l01337"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="l01340"></a>
<a id="l01341"></a>
<a id="l01342"></a>
<a id="l01343"></a>
<a id="l01364"></a>
<a id="l01365"></a>
<a id="l01366"></a>
<a id="l01367"></a>
<a id="l01368"></a>
<a id="l01369"></a>
<a id="l01370"></a>
<a id="l01407"></a>
<a id="l01408"></a>
<a id="l01409"></a>
<a id="l01410"></a>
<a id="l01411"></a>
<a id="l01432"></a>
<a id="l01433"></a>
<a id="l01434"></a>
<a id="foldopen01436"></a>
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
<a id="l01447"></a>
<a id="l01448"></a>
<a id="l01449"></a>
<a id="l01450"></a>
<a id="l01451"></a>
<a id="l01452"></a>
<a id="l01453"></a>
<a id="l01454"></a>
<a id="l01455"></a>
<a id="l01456"></a>
<a id="l01457"></a>
<a id="l01458"></a>
<a id="l01459"></a>
<a id="l01460"></a>
<a id="l01461"></a>
<a id="l01462"></a>
<a id="l01463"></a>
<a id="l01464"></a>
<a id="l01465"></a>
<a id="l01466"></a>
<a id="l01467"></a>
<a id="l01468"></a>
<a id="l01469"></a>
<a id="l01470"></a>
<a id="l01471"></a>
<a id="l01472"></a>
<a id="l01473"></a>
<a id="l01474"></a>
<a id="l01475"></a>
<a id="l01476"></a>
<a id="l01477"></a>
<a id="l01478"></a>
<a id="l01479"></a>
<a id="l01480"></a>
<a id="l01491"></a>
<a id="l01492"></a>
<a id="l01493"></a>
<a id="l01494"></a>
<a id="l01505"></a>
<a id="l01506"></a>
<a id="l01507"></a>
<a id="l01508"></a>
<a id="l01520"></a>
<a id="l01521"></a>
<a id="l01522"></a>
<a id="l01523"></a>
<a id="l01524"></a>
<a id="l01525"></a>
<a id="l01526"></a>
<a id="l01527"></a>
<a id="l01528"></a>
<a id="l01529"></a>
<a id="l01530"></a>
<a id="l01531"></a>
<a id="l01532"></a>
<a id="l01540"></a>
<a id="l01541"></a>
<a id="l01549"></a>
<a id="l01550"></a>
<a id="l01571"></a>
<a id="l01572"></a>
<a id="l01573"></a>
<a id="l01574"></a>
<a id="l01575"></a>
<a id="l01576"></a>
<a id="l01577"></a>
<a id="l01578"></a>
<a id="l01579"></a>
<a id="l01580"></a>
<a id="l01581"></a>
<a id="l01582"></a>
<a id="l01583"></a>
<a id="l01584"></a>
<a id="l01598"></a>
<a id="l01599"></a>
<a id="l01600"></a>
<a id="l01601"></a>
<a id="l01602"></a>
<a id="l01603"></a>
<a id="l01604"></a>
<a id="l01608"></a>
<a id="l01609"></a>
<a id="aatomic_8h_html"></a>
<a id="adplpmtud_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__ip__4__6_html_ga090f4770cd630517b5391d36e3705e41"></a>
<a id="agroup__ip__4__6_html_ga1df641bd5978219a7da51ea25ea8ac2f"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="agroup__ip__4__6_html_ga502492205736b373fa35c0524ba3d4e6"></a>
<a id="agroup__ip__4__6_html_ga8702e764fa49396587469a102870b109"></a>
<a id="agroup__ip__4__6_html_ga8b4cfadf1b284e52d6905ca88657b48a"></a>
<a id="agroup__ip__4__6_html_gaaab4268707dbe08348b98fb028e7aa5c"></a>
<a id="agroup__ip__4__6_html_gac53da21004b2bdc93b878da2ec4590bd"></a>
<a id="agroup__ip__4__6_html_gaf06819bf427cc58be1229b27b373ca31"></a>
<a id="agroup__ip__4__6_html_ggaaab4268707dbe08348b98fb028e7aa5ca6f049fea24a6d2d5279e736ececf3c83"></a>
<a id="agroup__ip__4__6_html_ggaaab4268707dbe08348b98fb028e7aa5ca892feaa0f7556622a3491683e69b6ac2"></a>
<a id="agroup__ip__4__6_html_ggaaab4268707dbe08348b98fb028e7aa5caff1fd09b4fa81b8e0e8a73132c8fa3e4"></a>
<a id="agroup__net__context_html_ga01c11c1dfce101df046df9ade00ed277"></a>
<a id="agroup__net__context_html_ga0cbf8377e7757881033aab3e718b1a61"></a>
<a id="agroup__net__context_html_ga0d391690d9d6972ce6f4baedeab64b11"></a>
<a id="agroup__net__context_html_ga10399e3f3d159de9325ac7632ce25c51"></a>
<a id="agroup__net__context_html_ga11672ca3ebdae63b0013ad76959304d5"></a>
<a id="agroup__net__context_html_ga11801119ad1d62db0302479c133adb35"></a>
<a id="agroup__net__context_html_ga120ae8d4ff788ab21b19c11ed1738a71"></a>
<a id="agroup__net__context_html_ga1b056999d9ab8f2d3b3c0f4788f36cdd"></a>
<a id="agroup__net__context_html_ga1d6b64e302c546db589c661f4b6bda98"></a>
<a id="agroup__net__context_html_ga2023f160b4d2ebc05d665d119611ef25"></a>
<a id="agroup__net__context_html_ga24b4d99dddc4fabf383f5d8079650337"></a>
<a id="agroup__net__context_html_ga2f6d614158c999fa68e518393c0a9c35"></a>
<a id="agroup__net__context_html_ga2f8fccd2453227706e313ac056f1c6ef"></a>
<a id="agroup__net__context_html_ga37bbecc848430590d5d68d2880c83c1e"></a>
<a id="agroup__net__context_html_ga37fbf84456a4142330d74eed1f3c24f6"></a>
<a id="agroup__net__context_html_ga3803c0d738fbb9d786f401aacc10a4d3"></a>
<a id="agroup__net__context_html_ga3bb4bbd522ede36213bafe86f2d1d770"></a>
<a id="agroup__net__context_html_ga3db832f40b6a0b975a282ef354a7bffc"></a>
<a id="agroup__net__context_html_ga40c6ef5b1f8b846e5b205947e87ce585"></a>
<a id="agroup__net__context_html_ga41d258362d6a7a703bc0b65d08e2b4c4"></a>
<a id="agroup__net__context_html_ga423103d5c386b602737e23ee81f2a961"></a>
<a id="agroup__net__context_html_ga4c0ef9540a0d7e800c4529274f5c22f4"></a>
<a id="agroup__net__context_html_ga4c3de0a3b7f27dd8ac9d0f415710faad"></a>
<a id="agroup__net__context_html_ga53bd5f35a142f1d43f90d3bde99778e0"></a>
<a id="agroup__net__context_html_ga581582c0461b36088d21d0fd433cc284"></a>
<a id="agroup__net__context_html_ga5c3a841ff54ddb53cedcccefde5a7d7a"></a>
<a id="agroup__net__context_html_ga5e2f5fcc08863a4090bc04040ee88d29"></a>
<a id="agroup__net__context_html_ga717b1aaa11d589bfe929d98be5be19ed"></a>
<a id="agroup__net__context_html_ga74f919185f8af074c2d90aa04733dd2a"></a>
<a id="agroup__net__context_html_ga7f4d732a99cb9e86fcd5226fbbb727f4"></a>
<a id="agroup__net__context_html_ga8e93032d6b65d9b5dfc0f64ecdf3a6b5"></a>
<a id="agroup__net__context_html_ga977b08a77586e0e4752bff725139427c"></a>
<a id="agroup__net__context_html_ga99b5f0ded5d56b735e051ede5651f435"></a>
<a id="agroup__net__context_html_ga9bd6b5e9429b6e845d41f6cbf242c092"></a>
<a id="agroup__net__context_html_ga9cdb3e5849a5b2663e0a38ac2a39a427"></a>
<a id="agroup__net__context_html_gaa337bccec2c1df42540f236bb33a70e1"></a>
<a id="agroup__net__context_html_gaa82d80fa18693b98dc363c35104075ba"></a>
<a id="agroup__net__context_html_gaa973878eb7f6bf69d91da992edad6409"></a>
<a id="agroup__net__context_html_gaac934209341db606a4d563b3c48cce45"></a>
<a id="agroup__net__context_html_gab03a354899ff68f6b9d127bc3bb5e17d"></a>
<a id="agroup__net__context_html_gab2a2064fa33613a60ad40597d0971774"></a>
<a id="agroup__net__context_html_gab3caccfe9fa1bc7ce0e4654192a5de93"></a>
<a id="agroup__net__context_html_gab3cc2a13e24f9c263bc40cc87d752a9f"></a>
<a id="agroup__net__context_html_gabb751f7d213d00f8eec72a67f4ce3491"></a>
<a id="agroup__net__context_html_gabbb9472c54b2fbe0b519dcb68e02a44e"></a>
<a id="agroup__net__context_html_gac793e1def18200416e3f679067c56ab3"></a>
<a id="agroup__net__context_html_gac8f6e3a16d52e8e376c38eec0ed8a940"></a>
<a id="agroup__net__context_html_gac9b4cf9beecaac5bf05db3111c803678"></a>
<a id="agroup__net__context_html_gad9350d40a884315ff9de4032a8d6ae71"></a>
<a id="agroup__net__context_html_gadcd0049229580244ea89fbc98bf23a81"></a>
<a id="agroup__net__context_html_gadf41291ca5be067e830d121000ca3f51"></a>
<a id="agroup__net__context_html_gadf4ab08eb39803909e585b16ce68307a"></a>
<a id="agroup__net__context_html_gae3082af116955d4175c025a02b296c91"></a>
<a id="agroup__net__context_html_gae3b3892b921e4694a18e7bacee63841d"></a>
<a id="agroup__net__context_html_gaefead18501a966af4a7f71eb23ac17c7"></a>
<a id="agroup__net__context_html_gaf05114d2edc8b5fb485fd37f3d0821ba"></a>
<a id="agroup__net__context_html_gaf29d5ee244c552d78171938a903fbaca"></a>
<a id="agroup__net__context_html_gaf915131b95b159e299f034768cefdaea"></a>
<a id="agroup__net__context_html_gafa485a6fae8237dd7e6856f4567b2317"></a>
<a id="agroup__net__context_html_gafd68de53778cbd807d0e45209a83df05"></a>
<a id="agroup__net__context_html_gafe6b8c9af4464cd471285817d6d61087"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da104d851b3c8884c875dbbc9d1e6c64ae"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da12c660c9ee2dd9d9d2de36980949aa9f"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da38adf4f5e3fba71f152a05c208e6f9f0"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da3f5fea1c10f55d4db1d72bba2959445e"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da469d1d21e088eba6f96ec0a679636ba7"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da4c24ea3a7cafcd9eddfc15a5725d75d2"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da61c105080d36bca8b4405527af4aaac4"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da6441103cc8e0e3cf724d2ea79cf18dcb"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da69e538d1b4732c865384340989f011c8"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da885dadd317c676c4d9be316df29ff276"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da98136d42db895cf6f3e35ee418e0b7eb"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da98f7a13028a2deb6eee31f1bad7c20b7"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da9db3637a09382655835493aed186a549"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17da9dec13665201fdc9be87490cde2f3253"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17daa3a443af92a7bc45aa9cc81ca4a1de0c"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17dab1615ef9a3bf84daf964a445476bc04c"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17dab4dd4a3acee76f82c37fd16fd5f53867"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17dacd227331833af7fb92b84f3ceb80f3ab"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17dad5099786ebcdc0198cf3cd1db465387d"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17dad6b8627398a90dd622f433e8b3fee3a3"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17dae0ed5497e4d356ca2bdea0a120dcb6ee"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17dae72a8a6e3f4a7a14370cd1267820c71d"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17dae95fc08de9277a59c42d6bf6355ec201"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c"></a>
<a id="agroup__net__context_html_ggab03a354899ff68f6b9d127bc3bb5e17daf50b6d1ab2da2df3b2ba1f991fc8011e"></a>
<a id="agroup__net__if_html_ga02445f6c61f0d29f56ac0ef59e025630"></a>
<a id="agroup__net__if_html_ga72708cdb7f133fe5d7edf819756c3516"></a>
<a id="agroup__semaphore__apis_html_gab9be3cf1988af2cd6afdace52d497c84"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="akernel_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="anet__stats_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aposix_2sys_2socket_8h_html_adee01662b0cf762a014efd87ab811276"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructk__condvar_html"></a>
<a id="astructk__fifo_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__context_html"></a>
<a id="astructnet__context_html_a0ae23462dcc7f84c95e0cc69dfeb6d5a"></a>
<a id="astructnet__context_html_a1511a41860e1b47b5b7652e9b350aaf4"></a>
<a id="astructnet__context_html_a1679e131dd6626bc210f23938df3fbcb"></a>
<a id="astructnet__context_html_a2c6f6d484e8744ec97aa966d6f0079c7"></a>
<a id="astructnet__context_html_a300e382f78b20f220fc1b450784bbd3c"></a>
<a id="astructnet__context_html_a329f737a3eaf0a57aa6700c59f3733dd"></a>
<a id="astructnet__context_html_a38c83746c8b2fcddf187a20299d6eb3c"></a>
<a id="astructnet__context_html_a709208a159d6795c5c8a56ff38732609"></a>
<a id="astructnet__context_html_a730e72866e94ed1695010b50c618a281"></a>
<a id="astructnet__context_html_a899af7c9b63a2da0ec43646f2d40a146"></a>
<a id="astructnet__context_html_a8a548b4c545411f6110e42182b0b99b0"></a>
<a id="astructnet__context_html_a9a9116844b52dc0366f770f3e6c572eb"></a>
<a id="astructnet__context_html_ab6d310ba4253933448584fa40e6ff4b7"></a>
<a id="astructnet__context_html_abc30f85e6016901b1d6fbb771b07370d"></a>
<a id="astructnet__context_html_abd8ff1b4826535df911d2af14b46e312"></a>
<a id="astructnet__context_html_abfb04fc163636498f72b29aa12087e19"></a>
<a id="astructnet__context_html_ad71d151e1e9e35b934949482066f1947"></a>
<a id="astructnet__context_html_adee6e668bfae2749df9b986d0049f10b"></a>
<a id="astructnet__context_html_ae56374afa462895448945327f6c772fa"></a>
<a id="astructnet__context_html_af551b252faf29ee6018d4bd783c5f2b4"></a>
<a id="astructnet__context_html_af9801980b3f2bb16f5ea2126a6e18cb4"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__in6__addr_html"></a>
<a id="astructnet__in__addr_html"></a>
<a id="astructnet__msghdr_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnet__sockaddr_html"></a>

```c


/*
 * Copyright (c) 2016 Intel Corporation
 * Copyright (c) 2021 Nordic Semiconductor
 * Copyright (c) 2025 Aerlync Labs Inc.
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_NET_CONTEXT_H_
#define ZEPHYR_INCLUDE_NET_NET_CONTEXT_H_


#include <zephyr/kernel.h>
#include <zephyr/sys/atomic.h>

#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_stats.h>
#include <zephyr/net/dplpmtud.h>

#ifdef __cplusplus
extern "C" {
#endif

#define NET_CONTEXT_IN_USE BIT(0)


enum net_context_state {
        NET_CONTEXT_IDLE = 0,
        NET_CONTEXT_UNCONNECTED = 0,
        NET_CONTEXT_CONFIGURING = 1,
        NET_CONTEXT_CONNECTING = 1,
        NET_CONTEXT_READY = 2,
        NET_CONTEXT_CONNECTED = 2,
        NET_CONTEXT_LISTENING = 3,
};


#define NET_CONTEXT_FAMILY (BIT(3) | BIT(4) | BIT(5))

#define NET_CONTEXT_TYPE   (BIT(6) | BIT(7))

#define NET_CONTEXT_REMOTE_ADDR_SET  BIT(8)

#define NET_CONTEXT_BOUND_TO_IFACE BIT(9)

#define NET_CONTEXT_LOCAL_ADDR_SET BIT(10)

struct net_context;

typedef void (*net_context_recv_cb_t)(struct net_context *context,
                                      struct net_pkt *pkt,
                                      union net_ip_header *ip_hdr,
                                      union net_proto_header *proto_hdr,
                                      int status,
                                      void *user_data);

typedef void (*net_context_send_cb_t)(struct net_context *context,
                                      int status,
                                      void *user_data);

typedef void (*net_tcp_accept_cb_t)(struct net_context *new_context,
                                    struct net_sockaddr *addr,
                                    net_socklen_t addrlen,
                                    int status,
                                    void *user_data);

typedef void (*net_context_connect_cb_t)(struct net_context *context,
                                         int status,
                                         void *user_data);

/* The net_pkt_get_slab_func_t is here in order to avoid circular
 * dependency between net_pkt.h and net_context.h
 */
typedef struct k_mem_slab *(*net_pkt_get_slab_func_t)(void);

/* The net_pkt_get_pool_func_t is here in order to avoid circular
 * dependency between net_pkt.h and net_context.h
 */
typedef struct net_buf_pool *(*net_pkt_get_pool_func_t)(void);

struct net_tcp;

struct net_conn_handle;

__net_socket struct net_context {
        void *fifo_reserved;

        void *user_data;

        atomic_t refcount;

        struct k_mutex lock;

        union {
                struct net_sockaddr local;
                struct net_sockaddr_storage local_storage;
        };

        union {
                struct net_sockaddr remote;
                struct net_sockaddr_storage remote_storage;
        };

        struct net_conn_handle *conn_handler;

        net_context_recv_cb_t recv_cb;

        net_context_send_cb_t send_cb;

        net_context_connect_cb_t connect_cb;

#if defined(CONFIG_NET_CONTEXT_NET_PKT_POOL)
        net_pkt_get_slab_func_t tx_slab;

        net_pkt_get_pool_func_t data_pool;
#endif /* CONFIG_NET_CONTEXT_NET_PKT_POOL */

#if defined(CONFIG_NET_TCP)
        void *tcp;
#endif /* CONFIG_NET_TCP */

#if defined(CONFIG_NET_CONTEXT_SYNC_RECV)
        struct k_sem recv_data_wait;
#endif /* CONFIG_NET_CONTEXT_SYNC_RECV */

#if defined(CONFIG_NET_CONTEXT_LINGER)
        struct k_sem linger_sem;
#endif /* CONFIG_NET_CONTEXT_LINGER */

#if defined(CONFIG_NET_SOCKETS)
        void *socket_data;

        int sock_error;

        union {
                struct k_fifo recv_q;
                struct k_fifo accept_q;
        };

        struct {
                struct k_condvar recv;

                struct k_mutex *lock;
        } cond;
#endif /* CONFIG_NET_SOCKETS */

#if defined(CONFIG_NET_OFFLOAD)
        void *offload_context;
#endif /* CONFIG_NET_OFFLOAD */

#if defined(CONFIG_NET_SOCKETS_CAN)
        int can_filter_id;
#endif /* CONFIG_NET_SOCKETS_CAN */

        struct {
#if defined(CONFIG_NET_CONTEXT_PRIORITY)
                uint8_t priority;
#endif
#if defined(CONFIG_NET_CONTEXT_TXTIME)
                bool txtime;
#endif
#if defined(CONFIG_SOCKS)
                struct {
                        struct net_sockaddr addr;
                        net_socklen_t addrlen;
                } proxy;
#endif
#if defined(CONFIG_NET_CONTEXT_CLAMP_PORT_RANGE)
                uint32_t port_range;
#endif
#if defined(CONFIG_NET_CONTEXT_RCVTIMEO)
                k_timeout_t rcvtimeo;
#endif
#if defined(CONFIG_NET_CONTEXT_SNDTIMEO)
                k_timeout_t sndtimeo;
#endif
#if defined(CONFIG_NET_CONTEXT_RCVBUF)
                uint16_t rcvbuf;
#endif
#if defined(CONFIG_NET_CONTEXT_SNDBUF)
                uint16_t sndbuf;
#endif
#if defined(CONFIG_NET_CONTEXT_DSCP_ECN)
                uint8_t dscp_ecn;
#endif
#if defined(CONFIG_NET_CONTEXT_REUSEADDR)
                bool reuseaddr;
#endif
#if defined(CONFIG_NET_CONTEXT_REUSEPORT)
                bool reuseport;
#endif
#if defined(CONFIG_NET_IPV4_MAPPING_TO_IPV6)
                bool ipv6_v6only;
#endif
#if defined(CONFIG_NET_CONTEXT_RECV_PKTINFO)
                bool recv_pktinfo;
#endif
#if defined(CONFIG_NET_CONTEXT_RECV_HOPLIMIT)
                bool recv_hoplimit;
#endif
#if defined(CONFIG_NET_IPV6)
                uint16_t addr_preferences;
#endif
#if defined(CONFIG_NET_IPV6) || defined(CONFIG_NET_IPV4)
                union {
                        uint8_t ipv6_mcast_ifindex;

                        uint8_t ipv4_mcast_ifindex;
                };
                union {
                        bool ipv6_mcast_loop;
                        bool ipv4_mcast_loop;
                };

                bool dont_fragment;
#endif /* CONFIG_NET_IPV6 || CONFIG_NET_IPV4 */

#if defined(CONFIG_NET_CONTEXT_TIMESTAMPING)
                uint8_t timestamping;
#endif

#if defined(CONFIG_NET_CONTEXT_LINGER)
                struct net_linger linger;
#endif /* CONFIG_NET_CONTEXT_LINGER */

#if defined(CONFIG_NET_UDP_OPTIONS)
                struct {
                        uint32_t enabled;
                        uint32_t required;
                        bool drop_all_opts;
                        uint16_t mds;
                        struct net_udp_opt_mrds mrds;
#if defined(CONFIG_NET_UDP_OPTIONS_DPLPMTUD)
                        struct {
                                struct net_dplpmtud_path path;
                                struct k_work_delayable timer;
                                uint32_t token;
                                uint16_t probe_size;
                                bool enabled;
                                bool app_respond;
                                bool base_confirmed;
                                struct k_work echo_work;
                                struct net_sockaddr_storage echo_peer;
                                net_socklen_t echo_peerlen;
                                uint32_t echo_token;
                                bool echo_pending;
                                uint32_t echo_last_ms;
                        } dplpmtud;
#endif /* CONFIG_NET_UDP_OPTIONS_DPLPMTUD */
                } udp_opt;
#endif
        } options;

        uint16_t proto;

        uint16_t flags;

        int8_t iface;

        union {
                struct {
                        uint8_t ipv6_hop_limit;
                        uint8_t ipv6_mcast_hop_limit;
                };
                struct {
                        uint8_t ipv4_ttl;
                        uint8_t ipv4_mcast_ttl;
                };
        };

#if defined(CONFIG_SOCKS)
        bool proxy_enabled;
#endif

};

static inline bool net_context_is_used(struct net_context *context)
{
        NET_ASSERT(context);

        return context->flags & NET_CONTEXT_IN_USE;
}

static inline bool net_context_is_bound_to_iface(struct net_context *context)
{
        NET_ASSERT(context);

        return context->flags & NET_CONTEXT_BOUND_TO_IFACE;
}

static inline bool net_context_is_local_addr_set(struct net_context *context)
{
        NET_ASSERT(context);

        return context->flags & NET_CONTEXT_LOCAL_ADDR_SET;
}


#define NET_CONTEXT_STATE_SHIFT 1
#define NET_CONTEXT_STATE_MASK 0x03


static inline
enum net_context_state net_context_get_state(struct net_context *context)
{
        NET_ASSERT(context);

        return (enum net_context_state)
                ((context->flags >> NET_CONTEXT_STATE_SHIFT) &
                NET_CONTEXT_STATE_MASK);
}

static inline void net_context_set_state(struct net_context *context,
                                         enum net_context_state state)
{
        NET_ASSERT(context);

        context->flags &= ~(NET_CONTEXT_STATE_MASK << NET_CONTEXT_STATE_SHIFT);
        context->flags |= ((state & NET_CONTEXT_STATE_MASK) <<
                           NET_CONTEXT_STATE_SHIFT);
}

static inline net_sa_family_t net_context_get_family(struct net_context *context)
{
        NET_ASSERT(context);

        return ((context->flags & NET_CONTEXT_FAMILY) >> 3);
}

static inline void net_context_set_family(struct net_context *context,
                                          net_sa_family_t family)
{
        uint8_t flag = 0U;

        NET_ASSERT(context);

        if (family == NET_AF_UNSPEC || family == NET_AF_INET || family == NET_AF_INET6 ||
            family == NET_AF_PACKET || family == NET_AF_CAN) {
                /* Family is in BIT(4), BIT(5) and BIT(6) */
                flag = (uint8_t)(family << 3);
        }

        context->flags |= flag;
}

static inline
enum net_sock_type net_context_get_type(struct net_context *context)
{
        NET_ASSERT(context);

        return (enum net_sock_type)((context->flags & NET_CONTEXT_TYPE) >> 6);
}

static inline void net_context_set_type(struct net_context *context,
                                        enum net_sock_type type)
{
        uint16_t flag = 0U;

        NET_ASSERT(context);

        if (type == NET_SOCK_DGRAM || type == NET_SOCK_STREAM || type == NET_SOCK_RAW) {
                /* Type is in BIT(6) and BIT(7)*/
                flag = (uint16_t)(type << 6);
        }

        context->flags |= flag;
}

#if defined(CONFIG_NET_SOCKETS_CAN)
static inline void net_context_set_can_filter_id(struct net_context *context,
                                             int filter_id)
{
        NET_ASSERT(context);

        context->can_filter_id = filter_id;
}
#else
static inline void net_context_set_can_filter_id(struct net_context *context,
                                             int filter_id)
{
        ARG_UNUSED(context);
        ARG_UNUSED(filter_id);
}
#endif

#if defined(CONFIG_NET_SOCKETS_CAN)
static inline int net_context_get_can_filter_id(struct net_context *context)
{
        NET_ASSERT(context);

        return context->can_filter_id;
}
#else
static inline int net_context_get_can_filter_id(struct net_context *context)
{
        ARG_UNUSED(context);

        return -1;
}
#endif

static inline uint16_t net_context_get_proto(struct net_context *context)
{
        return context->proto;
}

static inline void net_context_set_proto(struct net_context *context,
                                         uint16_t proto)
{
        context->proto = proto;
}

static inline
struct net_if *net_context_get_iface(struct net_context *context)
{
        NET_ASSERT(context);

        return net_if_get_by_index(context->iface);
}

static inline void net_context_set_iface(struct net_context *context,
                                         struct net_if *iface)
{
        NET_ASSERT(context);
        NET_ASSERT(iface);

        context->iface = (uint8_t)net_if_get_by_iface(iface);
}

static inline void net_context_bind_iface(struct net_context *context,
                                          struct net_if *iface)
{
        NET_ASSERT(context);
        NET_ASSERT(iface);

        context->flags |= NET_CONTEXT_BOUND_TO_IFACE;
        net_context_set_iface(context, iface);
}

static inline uint8_t net_context_get_ipv4_ttl(struct net_context *context)
{
        return context->ipv4_ttl;
}

static inline void net_context_set_ipv4_ttl(struct net_context *context,
                                            uint8_t ttl)
{
        context->ipv4_ttl = ttl;
}

static inline uint8_t net_context_get_ipv4_mcast_ttl(struct net_context *context)
{
        return context->ipv4_mcast_ttl;
}

static inline void net_context_set_ipv4_mcast_ttl(struct net_context *context,
                                                  uint8_t ttl)
{
        context->ipv4_mcast_ttl = ttl;
}

#if defined(CONFIG_NET_IPV4)
static inline bool net_context_get_ipv4_mcast_loop(struct net_context *context)
{
        return context->options.ipv4_mcast_loop;
}

static inline void net_context_set_ipv4_mcast_loop(struct net_context *context,
                                                   bool ipv4_mcast_loop)
{
        context->options.ipv4_mcast_loop = ipv4_mcast_loop;
}
#endif

static inline uint8_t net_context_get_ipv6_hop_limit(struct net_context *context)
{
        return context->ipv6_hop_limit;
}

static inline void net_context_set_ipv6_hop_limit(struct net_context *context,
                                                  uint8_t hop_limit)
{
        context->ipv6_hop_limit = hop_limit;
}

static inline uint8_t net_context_get_ipv6_mcast_hop_limit(struct net_context *context)
{
        return context->ipv6_mcast_hop_limit;
}

static inline void net_context_set_ipv6_mcast_hop_limit(struct net_context *context,
                                                        uint8_t hop_limit)
{
        context->ipv6_mcast_hop_limit = hop_limit;
}

#if defined(CONFIG_NET_IPV6)

static inline bool net_context_get_ipv6_mcast_loop(struct net_context *context)
{
        return context->options.ipv6_mcast_loop;
}

static inline void net_context_set_ipv6_mcast_loop(struct net_context *context,
                                                   bool ipv6_mcast_loop)
{
        context->options.ipv6_mcast_loop = ipv6_mcast_loop;
}

#endif

#if defined(CONFIG_SOCKS)
static inline void net_context_set_proxy_enabled(struct net_context *context,
                                                 bool enable)
{
        context->proxy_enabled = enable;
}
#else
static inline void net_context_set_proxy_enabled(struct net_context *context,
                                                 bool enable)
{
        ARG_UNUSED(context);
        ARG_UNUSED(enable);
}
#endif

#if defined(CONFIG_SOCKS)
static inline bool net_context_is_proxy_enabled(struct net_context *context)
{
        return context->proxy_enabled;
}
#else
static inline bool net_context_is_proxy_enabled(struct net_context *context)
{
        ARG_UNUSED(context);
        return false;
}
#endif

int net_context_get(net_sa_family_t family,
                    enum net_sock_type type,
                    uint16_t ip_proto,
                    struct net_context **context);

int net_context_put(struct net_context *context);

int net_context_ref(struct net_context *context);

int net_context_unref(struct net_context *context);

static inline void net_context_signal_linger(struct net_context *context)
{
#if defined(CONFIG_NET_CONTEXT_LINGER)
        k_sem_give(&context->linger_sem);
#else
        ARG_UNUSED(context);
#endif /* CONFIG_NET_CONTEXT_LINGER */
}

#if defined(CONFIG_NET_IPV4)
int net_context_create_ipv4_new(struct net_context *context,
                                struct net_pkt *pkt,
                                const struct net_in_addr *src,
                                const struct net_in_addr *dst);
#else
static inline int net_context_create_ipv4_new(struct net_context *context,
                                              struct net_pkt *pkt,
                                              const struct net_in_addr *src,
                                              const struct net_in_addr *dst)
{
        return -1;
}
#endif /* CONFIG_NET_IPV4 */

#if defined(CONFIG_NET_IPV6)
int net_context_create_ipv6_new(struct net_context *context,
                                struct net_pkt *pkt,
                                const struct net_in6_addr *src,
                                const struct net_in6_addr *dst);
#else
static inline int net_context_create_ipv6_new(struct net_context *context,
                                              struct net_pkt *pkt,
                                              const struct net_in6_addr *src,
                                              const struct net_in6_addr *dst)
{
        ARG_UNUSED(context);
        ARG_UNUSED(pkt);
        ARG_UNUSED(src);
        ARG_UNUSED(dst);
        return -1;
}
#endif /* CONFIG_NET_IPV6 */

int net_context_bind(struct net_context *context,
                     const struct net_sockaddr *addr,
                     net_socklen_t addrlen);

int net_context_listen(struct net_context *context,
                       int backlog);

int net_context_connect(struct net_context *context,
                        const struct net_sockaddr *addr,
                        net_socklen_t addrlen,
                        net_context_connect_cb_t cb,
                        k_timeout_t timeout,
                        void *user_data);

int net_context_accept(struct net_context *context,
                       net_tcp_accept_cb_t cb,
                       k_timeout_t timeout,
                       void *user_data);

int net_context_send(struct net_context *context,
                     const void *buf,
                     size_t len,
                     net_context_send_cb_t cb,
                     k_timeout_t timeout,
                     void *user_data);

int net_context_sendto(struct net_context *context,
                       const void *buf,
                       size_t len,
                       const struct net_sockaddr *dst_addr,
                       net_socklen_t addrlen,
                       net_context_send_cb_t cb,
                       k_timeout_t timeout,
                       void *user_data);

int net_context_sendmsg(struct net_context *context,
                        const struct net_msghdr *msghdr,
                        int flags,
                        net_context_send_cb_t cb,
                        k_timeout_t timeout,
                        void *user_data);

int net_context_recv(struct net_context *context,
                     net_context_recv_cb_t cb,
                     k_timeout_t timeout,
                     void *user_data);

int net_context_update_recv_wnd(struct net_context *context,
                                int32_t delta);

enum net_context_option {
        NET_OPT_PRIORITY          = 1,
        NET_OPT_TXTIME            = 2,
        NET_OPT_SOCKS5            = 3,
        NET_OPT_RCVTIMEO          = 4,
        NET_OPT_SNDTIMEO          = 5,
        NET_OPT_RCVBUF            = 6,
        NET_OPT_SNDBUF            = 7,
        NET_OPT_DSCP_ECN          = 8,
        NET_OPT_REUSEADDR         = 9,
        NET_OPT_REUSEPORT         = 10,
        NET_OPT_IPV6_V6ONLY       = 11,
        NET_OPT_RECV_PKTINFO      = 12,
        NET_OPT_MCAST_TTL         = 13,
        NET_OPT_MCAST_HOP_LIMIT   = 14,
        NET_OPT_UNICAST_HOP_LIMIT = 15,
        NET_OPT_TTL               = 16,
        NET_OPT_ADDR_PREFERENCES  = 17,
        NET_OPT_TIMESTAMPING      = 18,
        NET_OPT_MCAST_IFINDEX     = 19,
        NET_OPT_MTU               = 20,
        NET_OPT_LOCAL_PORT_RANGE  = 21,
        NET_OPT_IPV6_MCAST_LOOP   = 22,
        NET_OPT_IPV4_MCAST_LOOP   = 23,
        NET_OPT_RECV_HOPLIMIT     = 24,
        NET_OPT_DONT_FRAGMENT     = 25,
        NET_OPT_LINGER            = 26,
        NET_OPT_UDP_OPT           = 27,
        NET_OPT_UDP_OPT_OCS       = 28,
        NET_OPT_UDP_OPT_APC       = 29,
        NET_OPT_UDP_OPT_FRAG      = 30,
        NET_OPT_UDP_OPT_MDS       = 31,
        NET_OPT_UDP_OPT_MRDS      = 32,
        NET_OPT_UDP_OPT_REQ       = 33,
        NET_OPT_UDP_OPT_RES       = 34,
        NET_OPT_UDP_OPT_TIME      = 35,
        NET_OPT_UDP_OPT_AUTH      = 36,
        NET_OPT_UDP_OPT_EXP       = 37,
        NET_OPT_UDP_OPT_UCMP      = 38,
        NET_OPT_UDP_OPT_UENC      = 39,
        NET_OPT_UDP_OPT_UEXP      = 40,
        NET_OPT_UDP_OPT_DPLPMTUD  = 41,
        NET_OPT_UDP_OPT_DPLPMTUD_APP_RESPOND = 42,
};

int net_context_set_option(struct net_context *context,
                           enum net_context_option option,
                           const void *value, uint32_t len);

int net_context_get_option(struct net_context *context,
                           enum net_context_option option,
                           void *value, uint32_t *len);

#if defined(CONFIG_NET_UDP_OPTIONS_DPLPMTUD) || defined(__DOXYGEN__)
int net_context_set_udp_dplpmtud(struct net_context *context, bool enable);
#else
static inline int net_context_set_udp_dplpmtud(struct net_context *context,
                                               bool enable)
{
        ARG_UNUSED(context);
        ARG_UNUSED(enable);

        return -ENOTSUP;
}
#endif /* CONFIG_NET_UDP_OPTIONS_DPLPMTUD */

typedef void (*net_context_cb_t)(struct net_context *context, void *user_data);

void net_context_foreach(net_context_cb_t cb, void *user_data);

#if defined(CONFIG_NET_CONTEXT_NET_PKT_POOL)
static inline void net_context_setup_pools(struct net_context *context,
                                           net_pkt_get_slab_func_t tx_slab,
                                           net_pkt_get_pool_func_t data_pool)
{
        NET_ASSERT(context);

        context->tx_slab = tx_slab;
        context->data_pool = data_pool;
}
#else
#define net_context_setup_pools(context, tx_slab, data_pool)
#endif

bool net_context_port_in_use(enum net_ip_protocol ip_proto,
        uint16_t local_port, const struct net_sockaddr *local_addr);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_NET_CONTEXT_H_ */
```

## 22.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2016 Intel Corporation。

版权（Copyright）：© 2021 Nordic Semiconductor。

版权（Copyright）：© 2025 Aerlync Labs Inc.。

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 171 行

将 `net_pkt_get_slab_func_t` 放在这里，是为了避免 `net_pkt.h` 与 `net_context.h` 之间形成循环依赖（Circular Dependency）。

### 注释 3：原第 184 行

将 `net_pkt_get_pool_func_t` 放在这里，是为了避免 `net_pkt.h` 与 `net_context.h` 之间形成循环依赖（Circular Dependency）。

### 注释 4：原第 270 行

条件编译配置（Configuration）标记：`CONFIG_NET_CONTEXT_NET_PKT_POOL`。

### 注释 5：原第 275 行

条件编译配置（Configuration）标记：`CONFIG_NET_TCP`。

### 注释 6：原第 282 行

条件编译配置（Configuration）标记：`CONFIG_NET_CONTEXT_SYNC_RECV`。

### 注释 7：原第 290 行

条件编译配置（Configuration）标记：`CONFIG_NET_CONTEXT_LINGER`。

### 注释 8：原第 315 行

条件编译配置（Configuration）标记：`CONFIG_NET_SOCKETS`。

### 注释 9：原第 320 行

条件编译配置（Configuration）标记：`CONFIG_NET_OFFLOAD`。

### 注释 10：原第 324 行

条件编译配置（Configuration）标记：`CONFIG_NET_SOCKETS_CAN`。

### 注释 11：原第 429 行

条件编译（Conditional Compilation）：`CONFIG_NET_IPV6 || CONFIG_NET_IPV4`。

### 注释 12：原第 442 行

条件编译配置（Configuration）标记：`CONFIG_NET_CONTEXT_LINGER`。

### 注释 13：原第 488 行

条件编译配置（Configuration）标记：`CONFIG_NET_UDP_OPTIONS_DPLPMTUD`。

### 注释 14：原第 643 行

地址族（Family）位于 `BIT(4)`、`BIT(5)` 和 `BIT(6)`。

### 注释 15：原第 685 行

类型（Type）位于 `BIT(6)` 和 `BIT(7)`。

### 注释 16：原第 1138 行

条件编译配置（Configuration）标记：`CONFIG_NET_CONTEXT_LINGER`。

### 注释 17：原第 1164 行

条件编译配置（Configuration）标记：`CONFIG_NET_IPV4`。

### 注释 18：原第 1193 行

条件编译配置（Configuration）标记：`CONFIG_NET_IPV6`。

### 注释 19：原第 1531 行

条件编译配置（Configuration）标记：`CONFIG_NET_UDP_OPTIONS_DPLPMTUD`。

### 注释 20：原第 1609 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_CONTEXT_H_`。

## 22.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__context_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/net_stats.h](../api_file_configuration_reference/P059_zephyr__net__net_stats.h_文件参考.md)
- [zephyr/net/dplpmtud.h](https://docs.zephyrproject.org/latest/doxygen/html/dplpmtud_8h.html)
- [net_context](../network_core_model_reference/P055_net_context_结构体.md)
- [net_context_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafa485a6fae8237dd7e6856f4567b2317)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_context_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab3caccfe9fa1bc7ce0e4654192a5de93)
- [user_data](../network_core_model_reference/P055_net_context_结构体.md#a1679e131dd6626bc210f23938df3fbcb)
- [net_tcp_accept_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaf05114d2edc8b5fb485fd37f3d0821ba)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [net_context_connect_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga120ae8d4ff788ab21b19c11ed1738a71)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [fifo_reserved](../network_core_model_reference/P055_net_context_结构体.md#a2c6f6d484e8744ec97aa966d6f0079c7)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [refcount](../network_core_model_reference/P055_net_context_结构体.md#a0ae23462dcc7f84c95e0cc69dfeb6d5a)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [lock](../network_core_model_reference/P055_net_context_结构体.md#a730e72866e94ed1695010b50c618a281)
- [local](../network_core_model_reference/P055_net_context_结构体.md#a899af7c9b63a2da0ec43646f2d40a146)
- [local_storage](../network_core_model_reference/P055_net_context_结构体.md#a709208a159d6795c5c8a56ff38732609)
- [remote](../network_core_model_reference/P055_net_context_结构体.md#a1511a41860e1b47b5b7652e9b350aaf4)
- [remote_storage](../network_core_model_reference/P055_net_context_结构体.md#a8a548b4c545411f6110e42182b0b99b0)
- [conn_handler](../network_core_model_reference/P055_net_context_结构体.md#abd8ff1b4826535df911d2af14b46e312)
- [recv_cb](../network_core_model_reference/P055_net_context_结构体.md#af551b252faf29ee6018d4bd783c5f2b4)
- [send_cb](../network_core_model_reference/P055_net_context_结构体.md#a38c83746c8b2fcddf187a20299d6eb3c)
- [connect_cb](../network_core_model_reference/P055_net_context_结构体.md#abc30f85e6016901b1d6fbb771b07370d)
- [net_pkt_get_slab_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga3bb4bbd522ede36213bafe86f2d1d770)
- [net_pkt_get_pool_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gae3082af116955d4175c025a02b296c91)
- [tcp](../network_core_model_reference/P055_net_context_结构体.md#adee6e668bfae2749df9b986d0049f10b)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [k_condvar](../synchronization_reference/P011_内核条件变量结构.md)
- [recv](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [options](../network_core_model_reference/P055_net_context_结构体.md#ae56374afa462895448945327f6c772fa)
- [proto](../network_core_model_reference/P055_net_context_结构体.md#abfb04fc163636498f72b29aa12087e19)
- [flags](../network_core_model_reference/P055_net_context_结构体.md#a300e382f78b20f220fc1b450784bbd3c)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [iface](../network_core_model_reference/P055_net_context_结构体.md#ad71d151e1e9e35b934949482066f1947)
- [ipv6_hop_limit](../network_core_model_reference/P055_net_context_结构体.md#af9801980b3f2bb16f5ea2126a6e18cb4)
- [ipv6_mcast_hop_limit](../network_core_model_reference/P055_net_context_结构体.md#ab6d310ba4253933448584fa40e6ff4b7)
- [ipv4_ttl](../network_core_model_reference/P055_net_context_结构体.md#a9a9116844b52dc0366f770f3e6c572eb)
- [ipv4_mcast_ttl](../network_core_model_reference/P055_net_context_结构体.md#a329f737a3eaf0a57aa6700c59f3733dd)
- [net_context_is_used](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga423103d5c386b602737e23ee81f2a961)
- [NET_CONTEXT_IN_USE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga5e2f5fcc08863a4090bc04040ee88d29)
- [net_context_is_bound_to_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga2f6d614158c999fa68e518393c0a9c35)
- [NET_CONTEXT_BOUND_TO_IFACE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaa337bccec2c1df42540f236bb33a70e1)
- [net_context_is_local_addr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga8e93032d6b65d9b5dfc0f64ecdf3a6b5)
- [NET_CONTEXT_LOCAL_ADDR_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga717b1aaa11d589bfe929d98be5be19ed)
- [net_context_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga53bd5f35a142f1d43f90d3bde99778e0)
- [net_context_set_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaac934209341db606a4d563b3c48cce45)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [net_context_get_family](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga4c3de0a3b7f27dd8ac9d0f415710faad)
- [NET_CONTEXT_FAMILY](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gac8f6e3a16d52e8e376c38eec0ed8a940)
- [net_context_set_family](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga37bbecc848430590d5d68d2880c83c1e)
- [NET_AF_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8702e764fa49396587469a102870b109)
- [NET_AF_INET](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gac53da21004b2bdc93b878da2ec4590bd)
- [NET_AF_INET6](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga502492205736b373fa35c0524ba3d4e6)
- [NET_AF_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga090f4770cd630517b5391d36e3705e41)
- [NET_AF_CAN](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga1df641bd5978219a7da51ea25ea8ac2f)
- [net_sock_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaaab4268707dbe08348b98fb028e7aa5c)
- [net_context_get_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga24b4d99dddc4fabf383f5d8079650337)
- [NET_CONTEXT_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gac9b4cf9beecaac5bf05db3111c803678)
- [net_context_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga01c11c1dfce101df046df9ade00ed277)
- [NET_SOCK_DGRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaaab4268707dbe08348b98fb028e7aa5caff1fd09b4fa81b8e0e8a73132c8fa3e4)
- [NET_SOCK_STREAM](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaaab4268707dbe08348b98fb028e7aa5ca6f049fea24a6d2d5279e736ececf3c83)
- [NET_SOCK_RAW](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ggaaab4268707dbe08348b98fb028e7aa5ca892feaa0f7556622a3491683e69b6ac2)
- [net_context_set_can_filter_id](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga581582c0461b36088d21d0fd433cc284)
- [net_context_get_can_filter_id](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga7f4d732a99cb9e86fcd5226fbbb727f4)
- [net_context_get_proto](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gadf41291ca5be067e830d121000ca3f51)
- [net_context_set_proto](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gadcd0049229580244ea89fbc98bf23a81)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_context_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafe6b8c9af4464cd471285817d6d61087)
- [net_if_get_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga72708cdb7f133fe5d7edf819756c3516)
- [net_context_set_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga10399e3f3d159de9325ac7632ce25c51)
- [net_if_get_by_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga02445f6c61f0d29f56ac0ef59e025630)
- [net_context_bind_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga2f8fccd2453227706e313ac056f1c6ef)
- [net_context_get_ipv4_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga9cdb3e5849a5b2663e0a38ac2a39a427)
- [net_context_set_ipv4_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga11672ca3ebdae63b0013ad76959304d5)
- [net_context_get_ipv4_mcast_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga3db832f40b6a0b975a282ef354a7bffc)
- [net_context_set_ipv4_mcast_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab2a2064fa33613a60ad40597d0971774)
- [net_context_get_ipv6_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga977b08a77586e0e4752bff725139427c)
- [net_context_set_ipv6_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga0cbf8377e7757881033aab3e718b1a61)
- [net_context_get_ipv6_mcast_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga99b5f0ded5d56b735e051ede5651f435)
- [net_context_set_ipv6_mcast_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaf29d5ee244c552d78171938a903fbaca)
- [net_context_set_proxy_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga9bd6b5e9429b6e845d41f6cbf242c092)
- [net_context_is_proxy_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga5c3a841ff54ddb53cedcccefde5a7d7a)
- [net_context_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga37fbf84456a4142330d74eed1f3c24f6)
- [net_context_put](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga1d6b64e302c546db589c661f4b6bda98)
- [net_context_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga4c0ef9540a0d7e800c4529274f5c22f4)
- [net_context_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga0d391690d9d6972ce6f4baedeab64b11)
- [net_context_signal_linger](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga11801119ad1d62db0302479c133adb35)
- [k_sem_give](../synchronization_reference/P008_信号量公共接口.md#gab9be3cf1988af2cd6afdace52d497c84)
- [net_context_create_ipv4_new](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gae3b3892b921e4694a18e7bacee63841d)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_context_create_ipv6_new](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaa973878eb7f6bf69d91da992edad6409)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [net_context_bind](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga2023f160b4d2ebc05d665d119611ef25)
- [net_context_listen](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga3803c0d738fbb9d786f401aacc10a4d3)
- [net_context_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gadf4ab08eb39803909e585b16ce68307a)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_context_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga1b056999d9ab8f2d3b3c0f4788f36cdd)
- [net_context_send](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gac793e1def18200416e3f679067c56ab3)
- [net_context_sendto](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafd68de53778cbd807d0e45209a83df05)
- [net_context_sendmsg](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaf915131b95b159e299f034768cefdaea)
- [net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [net_context_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga74f919185f8af074c2d90aa04733dd2a)
- [net_context_update_recv_wnd](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab3cc2a13e24f9c263bc40cc87d752a9f)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [net_context_option](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab03a354899ff68f6b9d127bc3bb5e17d)
- [NET_OPT_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c)
- [NET_OPT_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184)
- [NET_OPT_SOCKS5](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c)
- [NET_OPT_RCVTIMEO](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076)
- [NET_OPT_SNDTIMEO](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668)
- [NET_OPT_RCVBUF](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1)
- [NET_OPT_SNDBUF](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08)
- [NET_OPT_DSCP_ECN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c)
- [NET_OPT_REUSEADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561)
- [NET_OPT_REUSEPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4)
- [NET_OPT_IPV6_V6ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c)
- [NET_OPT_RECV_PKTINFO](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a)
- [NET_OPT_MCAST_TTL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e)
- [NET_OPT_MCAST_HOP_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d)
- [NET_OPT_UNICAST_HOP_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3)
- [NET_OPT_TTL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184)
- [NET_OPT_ADDR_PREFERENCES](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d)
- [NET_OPT_TIMESTAMPING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2)
- [NET_OPT_MCAST_IFINDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da98136d42db895cf6f3e35ee418e0b7eb)
- [NET_OPT_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dad6b8627398a90dd622f433e8b3fee3a3)
- [NET_OPT_LOCAL_PORT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da469d1d21e088eba6f96ec0a679636ba7)
- [NET_OPT_IPV6_MCAST_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dab1615ef9a3bf84daf964a445476bc04c)
- [NET_OPT_IPV4_MCAST_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da38adf4f5e3fba71f152a05c208e6f9f0)
- [NET_OPT_RECV_HOPLIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da3f5fea1c10f55d4db1d72bba2959445e)
- [NET_OPT_DONT_FRAGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dad5099786ebcdc0198cf3cd1db465387d)
- [NET_OPT_LINGER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dae0ed5497e4d356ca2bdea0a120dcb6ee)
- [NET_OPT_UDP_OPT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dacd227331833af7fb92b84f3ceb80f3ab)
- [NET_OPT_UDP_OPT_OCS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da9dec13665201fdc9be87490cde2f3253)
- [NET_OPT_UDP_OPT_APC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da69e538d1b4732c865384340989f011c8)
- [NET_OPT_UDP_OPT_FRAG](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da9db3637a09382655835493aed186a549)
- [NET_OPT_UDP_OPT_MDS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da104d851b3c8884c875dbbc9d1e6c64ae)
- [NET_OPT_UDP_OPT_MRDS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da12c660c9ee2dd9d9d2de36980949aa9f)
- [NET_OPT_UDP_OPT_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da6441103cc8e0e3cf724d2ea79cf18dcb)
- [NET_OPT_UDP_OPT_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dae72a8a6e3f4a7a14370cd1267820c71d)
- [NET_OPT_UDP_OPT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da61c105080d36bca8b4405527af4aaac4)
- [NET_OPT_UDP_OPT_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dab4dd4a3acee76f82c37fd16fd5f53867)
- [NET_OPT_UDP_OPT_EXP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daa3a443af92a7bc45aa9cc81ca4a1de0c)
- [NET_OPT_UDP_OPT_UCMP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da98f7a13028a2deb6eee31f1bad7c20b7)
- [NET_OPT_UDP_OPT_UENC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dae95fc08de9277a59c42d6bf6355ec201)
- [NET_OPT_UDP_OPT_UEXP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da885dadd317c676c4d9be316df29ff276)
- [NET_OPT_UDP_OPT_DPLPMTUD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da4c24ea3a7cafcd9eddfc15a5725d75d2)
- [NET_OPT_UDP_OPT_DPLPMTUD_APP_RESPOND](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daf50b6d1ab2da2df3b2ba1f991fc8011e)
- [net_context_set_option](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga40c6ef5b1f8b846e5b205947e87ce585)
- [net_context_get_option](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gabbb9472c54b2fbe0b519dcb68e02a44e)
- [net_context_set_udp_dplpmtud](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaefead18501a966af4a7f71eb23ac17c7)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [net_context_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaa82d80fa18693b98dc363c35104075ba)
- [net_context_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gabb751f7d213d00f8eec72a67f4ce3491)
- [net_context_setup_pools](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga41d258362d6a7a703bc0b65d08e2b4c4)
- [net_context_port_in_use](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gad9350d40a884315ff9de4032a8d6ae71)
- [net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [dplpmtud.h](https://docs.zephyrproject.org/latest/doxygen/html/dplpmtud_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_stats.h](../api_file_configuration_reference/P059_zephyr__net__net_stats.h_文件参考.md)
- [net_context::refcount](../network_core_model_reference/P055_net_context_结构体.md#a0ae23462dcc7f84c95e0cc69dfeb6d5a)
- [net_context::remote](../network_core_model_reference/P055_net_context_结构体.md#a1511a41860e1b47b5b7652e9b350aaf4)
- [net_context::user_data](../network_core_model_reference/P055_net_context_结构体.md#a1679e131dd6626bc210f23938df3fbcb)
- [net_context::fifo_reserved](../network_core_model_reference/P055_net_context_结构体.md#a2c6f6d484e8744ec97aa966d6f0079c7)
- [net_context::flags](../network_core_model_reference/P055_net_context_结构体.md#a300e382f78b20f220fc1b450784bbd3c)
- [net_context::ipv4_mcast_ttl](../network_core_model_reference/P055_net_context_结构体.md#a329f737a3eaf0a57aa6700c59f3733dd)
- [net_context::send_cb](../network_core_model_reference/P055_net_context_结构体.md#a38c83746c8b2fcddf187a20299d6eb3c)
- [net_context::local_storage](../network_core_model_reference/P055_net_context_结构体.md#a709208a159d6795c5c8a56ff38732609)
- [net_context::lock](../network_core_model_reference/P055_net_context_结构体.md#a730e72866e94ed1695010b50c618a281)
- [net_context::local](../network_core_model_reference/P055_net_context_结构体.md#a899af7c9b63a2da0ec43646f2d40a146)
- [net_context::remote_storage](../network_core_model_reference/P055_net_context_结构体.md#a8a548b4c545411f6110e42182b0b99b0)
- [net_context::ipv4_ttl](../network_core_model_reference/P055_net_context_结构体.md#a9a9116844b52dc0366f770f3e6c572eb)
- [net_context::ipv6_mcast_hop_limit](../network_core_model_reference/P055_net_context_结构体.md#ab6d310ba4253933448584fa40e6ff4b7)
- [net_context::connect_cb](../network_core_model_reference/P055_net_context_结构体.md#abc30f85e6016901b1d6fbb771b07370d)
- [net_context::conn_handler](../network_core_model_reference/P055_net_context_结构体.md#abd8ff1b4826535df911d2af14b46e312)
- [net_context::proto](../network_core_model_reference/P055_net_context_结构体.md#abfb04fc163636498f72b29aa12087e19)
- [net_context::iface](../network_core_model_reference/P055_net_context_结构体.md#ad71d151e1e9e35b934949482066f1947)
- [net_context::tcp](../network_core_model_reference/P055_net_context_结构体.md#adee6e668bfae2749df9b986d0049f10b)
- [net_context::options](../network_core_model_reference/P055_net_context_结构体.md#ae56374afa462895448945327f6c772fa)
- [net_context::recv_cb](../network_core_model_reference/P055_net_context_结构体.md#af551b252faf29ee6018d4bd783c5f2b4)
- [net_context::ipv6_hop_limit](../network_core_model_reference/P055_net_context_结构体.md#af9801980b3f2bb16f5ea2126a6e18cb4)

---

[上一章](P021_net_buf.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P023_net_core.h_源码浏览.md)
