---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-15
title: zephyr__sd__sd_spec.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr__sd__sd_spec.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md)。

## 15.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
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
<a id="foldopen00028"></a>
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
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
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
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
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
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="foldopen00155"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
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
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="foldopen00214"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="foldopen00241"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="foldopen00260"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00272"></a>
<a id="l00274"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="foldopen00297"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="foldopen00315"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
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
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="foldopen00346"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="foldopen00359"></a>
<a id="l00359"></a>
<a id="l00361"></a>
<a id="l00363"></a>
<a id="l00365"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="foldopen00371"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="foldopen00377"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="foldopen00392"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="foldopen00408"></a>
<a id="l00408"></a>
<a id="l00410"></a>
<a id="l00412"></a>
<a id="l00414"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00420"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="foldopen00430"></a>
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
<a id="foldopen00448"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="foldopen00460"></a>
<a id="l00460"></a>
<a id="l00462"></a>
<a id="l00464"></a>
<a id="l00466"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="foldopen00476"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="foldopen00488"></a>
<a id="l00488"></a>
<a id="l00490"></a>
<a id="l00492"></a>
<a id="l00494"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="foldopen00505"></a>
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
<a id="foldopen00521"></a>
<a id="l00521"></a>
<a id="l00523"></a>
<a id="l00525"></a>
<a id="l00527"></a>
<a id="l00529"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="foldopen00541"></a>
<a id="l00541"></a>
<a id="l00543"></a>
<a id="l00545"></a>
<a id="l00547"></a>
<a id="l00549"></a>
<a id="l00551"></a>
<a id="l00553"></a>
<a id="l00555"></a>
<a id="l00557"></a>
<a id="l00559"></a>
<a id="l00561"></a>
<a id="l00563"></a>
<a id="l00565"></a>
<a id="l00567"></a>
<a id="l00569"></a>
<a id="l00571"></a>
<a id="l00573"></a>
<a id="l00575"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="foldopen00585"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
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
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="foldopen00612"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="foldopen00624"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="foldopen00638"></a>
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
<a id="foldopen00654"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="foldopen00671"></a>
<a id="l00671"></a>
<a id="l00673"></a>
<a id="l00675"></a>
<a id="l00677"></a>
<a id="l00679"></a>
<a id="l00681"></a>
<a id="l00683"></a>
<a id="l00685"></a>
<a id="l00687"></a>
<a id="l00689"></a>
<a id="l00691"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="foldopen00701"></a>
<a id="l00701"></a>
<a id="l00703"></a>
<a id="l00705"></a>
<a id="l00707"></a>
<a id="l00709"></a>
<a id="l00711"></a>
<a id="l00713"></a>
<a id="l00715"></a>
<a id="l00717"></a>
<a id="l00719"></a>
<a id="l00721"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="foldopen00731"></a>
<a id="l00731"></a>
<a id="l00733"></a>
<a id="l00735"></a>
<a id="l00737"></a>
<a id="l00739"></a>
<a id="l00741"></a>
<a id="l00743"></a>
<a id="l00745"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="foldopen00755"></a>
<a id="l00755"></a>
<a id="l00757"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="foldopen00767"></a>
<a id="l00767"></a>
<a id="l00769"></a>
<a id="l00771"></a>
<a id="l00773"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="foldopen00786"></a>
<a id="l00786"></a>
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
<a id="foldopen00803"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00817"></a>
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
<a id="l00869"></a>
<a id="l00870"></a>
<a id="l00871"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00879"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00888"></a>
<a id="l00889"></a>
<a id="l00890"></a>
<a id="l00891"></a>
<a id="l00892"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="foldopen00905"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="foldopen00920"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="l00922"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="l00933"></a>
<a id="l00934"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys-util_html_gab7b18750ddf0850461f926ae151ca7fa"></a>
<a id="agroup__sys-util_html_gaee55275295c076c6d23c994777623253"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a0378338c2747ba8947d8ffcb18f77d51"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a0da09225692b10e51140d4f15ba1dd0a"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a35b942802a4238882440f2e470f2555f"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a35c39a93dfcc239fcb80db70449af99e"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a400dc3acd2ae8320f130dbea80c81969"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a45bc2d4b117d144ef5191719f9b6c297"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a4aa36f7d8ceaa3cdab300915453b64b5"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a54546b311e446754738a9b6f1e3eaea4"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a56c94068ecb32eb9ced47d4a3bf95481"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a5c85e3208bb686d8ded9ae0fe7bd9d53"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a753b0fc3e44a4376998e5887ed2c5901"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a7c9bfc788861214fae86e22443e9484a"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a7ccf37711e67b58534689997ac1375df"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a7e34ea8ce2a215c2a76f4184b84a06f2"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a7ef64e231154de2e461005af29918b86"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a8c3edf14ca3a6e04c1949a40cd3fb135"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a99c20a704cce28fee37b9b0f14b2ff15"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a9cd6e9c88c3989531a71015147496895"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99a9dcb2e5fb6a5a53c6cb02422fd1fef3c"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99aa3183436decfa0e42ac0461629258ba3"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99aa58b1d9f75b639dc1b28163988bc8aa3"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99aa5f2d8c27d0b7ae780734cb4bedbf8a4"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99aa7c628982851eba38074d02e9e335b57"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99ab590e9d9b3213f31a2399ef379d066aa"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99abd97c835c80320637579c692d6f57878"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99ad6d6f1ccdabc2970ac2ab6c7a853b37e"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99ad822462692847b4e8433157cd75eef70"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99adc7e589c9352cddf856b2e868f93a097"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99adca664fbf5ff0b4d174ca21641e01004"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99aef4ee3246cd66cd7d48f1dabf3fcd7ef"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99af48292861388f111b0afad64f0352664"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99af48c850f0aa9e9f9dbce8fc8855f6a2a"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99afa15c17b4fb95747b444616b085b4905"></a>
<a id="asd__spec_8h_html_a072705601a34c697515f74acb0474c99affcc3d18f6bda30fb3fd34916d8f61fe"></a>
<a id="asd__spec_8h_html_a0769bcc2f15d43383f4e5a6c845c51aa"></a>
<a id="asd__spec_8h_html_a0769bcc2f15d43383f4e5a6c845c51aaa01aef2529fc39dc455c0fb8f2e9cc434"></a>
<a id="asd__spec_8h_html_a0769bcc2f15d43383f4e5a6c845c51aaa239f02ae958dc3e25032825bb4c067e7"></a>
<a id="asd__spec_8h_html_a0769bcc2f15d43383f4e5a6c845c51aaa669934175190e5416a0d04c3c94acb4b"></a>
<a id="asd__spec_8h_html_a0769bcc2f15d43383f4e5a6c845c51aaa7127f5d946ea6bb4ec19b96033aafc4b"></a>
<a id="asd__spec_8h_html_a0769bcc2f15d43383f4e5a6c845c51aaa984a5e7f75a4418ca29141f5c6031d1e"></a>
<a id="asd__spec_8h_html_a1c77191f9cb8c50e8e2a03cda2984dbc"></a>
<a id="asd__spec_8h_html_a1c77191f9cb8c50e8e2a03cda2984dbca03fc81eeed7047ad914ce6590511dfa3"></a>
<a id="asd__spec_8h_html_a1c77191f9cb8c50e8e2a03cda2984dbca2a4278c079a227145f63f5f2d860146a"></a>
<a id="asd__spec_8h_html_a1c77191f9cb8c50e8e2a03cda2984dbca305b2fb720b5191c762b77b886152ca8"></a>
<a id="asd__spec_8h_html_a1c77191f9cb8c50e8e2a03cda2984dbca36f78cdbd8fcc962c2247d7fc1f33f9b"></a>
<a id="asd__spec_8h_html_a1c77191f9cb8c50e8e2a03cda2984dbcaa4a44bb015be3cbcf180f34a39ba8e05"></a>
<a id="asd__spec_8h_html_a1c77191f9cb8c50e8e2a03cda2984dbcaca51b75cde3505fd672391b9d7a7997a"></a>
<a id="asd__spec_8h_html_a1c77191f9cb8c50e8e2a03cda2984dbcacf330302cc8ef7f55d76c2cace40649e"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a0d82c7d93c187de5c40c0ff83fe8a478"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a22413680849a7645c7e8c585b5184203"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a32b2c65c90d0d5b8df5e4a82e9b95a6d"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a34b03331e8f7a9ea6b67da6b68c7e0ed"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a3532733bc007df5009801bd6f09e45c9"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a4c35ca3a8db652008204cf0cfc8e2339"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a5dcd82e4fe5a34646a617a5031fdc638"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a78472618e8523bf73ca65aee6b0a8318"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a7c44711a51e8175ebcaf4be24e2daec3"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a855f8e4399cf3ce0c05c6089f3439ec2"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a91e216f8a1753b4719ee91819a926dde"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a92718e4bd4bccaa2fe4a8780228004d7"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6a96e26220a32f9b6e9e0bdd8c94d48eaf"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6aa5657942fb906d58ef2b7bed05137f23"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6ad74407536823c1ea3afdf41d4b858b1c"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6ae64496ba1520651f8bac35af2531eaf8"></a>
<a id="asd__spec_8h_html_a1cfd2df5ec76eeb915fd3689408a65d6af779f08bfb2fd73a717ea3789ccad509"></a>
<a id="asd__spec_8h_html_a2093143614e52f69e173289391d7e91c"></a>
<a id="asd__spec_8h_html_a2093143614e52f69e173289391d7e91ca10f805e3f66366474428718cb4569da0"></a>
<a id="asd__spec_8h_html_a2093143614e52f69e173289391d7e91cac3e8d67442f59c35b57d19d81b5d0d66"></a>
<a id="asd__spec_8h_html_a238de48c0cb55d173b6b874f4930c537"></a>
<a id="asd__spec_8h_html_a238de48c0cb55d173b6b874f4930c537a18b21e5e76bea0263f475ecc228c0301"></a>
<a id="asd__spec_8h_html_a238de48c0cb55d173b6b874f4930c537a2e3c01bc8d16641d7b500ce1244dbb03"></a>
<a id="asd__spec_8h_html_a238de48c0cb55d173b6b874f4930c537ae0605a0d9fc89e094a40b03e96c02339"></a>
<a id="asd__spec_8h_html_a238de48c0cb55d173b6b874f4930c537af82a5f23e51bf3ac3b7bec137269f540"></a>
<a id="asd__spec_8h_html_a250ae2ce54e941895a720b565632350e"></a>
<a id="asd__spec_8h_html_a250ae2ce54e941895a720b565632350eabd26fc6f76267231c78eae8be9ebb885"></a>
<a id="asd__spec_8h_html_a250ae2ce54e941895a720b565632350eac1212149d096232e75d1d090abb4974c"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a018af73c25e22c6e5313e5e3cff57e92"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a1071312f18c64077e6964e421ef00ead"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a17007c3d37f047e6db56491a4230e8a8"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a1f043936c614ac39b75f3835dc498b94"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a246619651470476238452550068db8a0"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a3d791855e6df402d5bfd92ce216a9a4b"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a3f6ebe270ba873bab3407ee7d655b53d"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a4cb1cc23687e7a1854d8af0c76876a20"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a4d32525a631342d78f73b6296e148666"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a560f91eb371bfea5cf6c5c036cc9c096"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a6323aa0a8cbfb59f8209a37c8135079c"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a6673f837fa5a98b573886c5e6429c644"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6a89c4025349ece0021cd627101f0efdd1"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6aa7a656a21495fbf64666b2b80236e4e4"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6ac0aa0897e1bbf45b0f5f4de73d733477"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6ac5613e6858d2c9217165ab4cbb240012"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6ad75d7d47a3d5fcc39a68c08546e9793b"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6adb3e45e84da812297359d6054baa69ba"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6ae923fdf459570657220ec225cbed7336"></a>
<a id="asd__spec_8h_html_a296cbe236e9e36dc79ca30eb54e6bcc6af0baaa7f71d144c7e5edade4b2445813"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8a13c703d344a1e03c1aa5881a77980085"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8a221dc45c7b73f6f96a63acbeb3e5e121"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8a24ea8c9db5531b5404bb667da26ac5d0"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8a2c639715b63769e9a431a93e636f007e"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8a32c9f5017cd49c9ca4b352269de6eeff"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8a4a3b8dc88c6349fb5f49ed3062a39a17"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8a572d53afafb39341e0cdb80d2d041d2c"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8a5bd0506d7efbecdc42eb8fae1427dc37"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8a63c0eee223946b1ae2b187bb585dfde4"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8a69e1d369d668d63071410078a31099a0"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8a74d01430b854f42ea84dba9d3ce45b16"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8a988f18b9f418744721b0fc91f2432449"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8ab1ff3da74a0dea49ffe7ac1d945ec4e6"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8abecfcd6d212185c74b57941c3fa58233"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8ac8848c5cdf177737744da3283f7140d5"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8ac988a54239b7d9e182f1b2f480567e66"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8adf578325509923b46e3ff4fbd74889ad"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8aee24df1d628479fe2d920839a0bf5012"></a>
<a id="asd__spec_8h_html_a313c45576db4ae219288fb4fbaad4bd8af63af4938d5aad64bac19fac42aedd10"></a>
<a id="asd__spec_8h_html_a314c38b1b0603c003e67b5dec2228d4b"></a>
<a id="asd__spec_8h_html_a314c38b1b0603c003e67b5dec2228d4ba0cd41f5198ce06ce5925b3f52d48b0a2"></a>
<a id="asd__spec_8h_html_a314c38b1b0603c003e67b5dec2228d4ba32ad0894344bc4980f9206022ed0f877"></a>
<a id="asd__spec_8h_html_a314c38b1b0603c003e67b5dec2228d4ba435b458d33f1568cb76b77a3ea2e1eb8"></a>
<a id="asd__spec_8h_html_a314c38b1b0603c003e67b5dec2228d4ba9eec5ff6f7d4c7512212cb48719dcabf"></a>
<a id="asd__spec_8h_html_a3a542344967c5c1912bde216559e7cd6"></a>
<a id="asd__spec_8h_html_a3a542344967c5c1912bde216559e7cd6a075731d15b2f4b7c7448d6d4ee059880"></a>
<a id="asd__spec_8h_html_a3a542344967c5c1912bde216559e7cd6a2a9baef178307d6e6006ea88b4da383c"></a>
<a id="asd__spec_8h_html_a3a542344967c5c1912bde216559e7cd6a617d1991d70033df3b39eef7ccb98b48"></a>
<a id="asd__spec_8h_html_a3a542344967c5c1912bde216559e7cd6a900536b934da03f8e8590de3e3d56296"></a>
<a id="asd__spec_8h_html_a3a542344967c5c1912bde216559e7cd6a9b69d64108c6564bc313e4fb2b53f61c"></a>
<a id="asd__spec_8h_html_a3a542344967c5c1912bde216559e7cd6ac2cc5967daee0a3e9ef61c9c486b3a6c"></a>
<a id="asd__spec_8h_html_a3a542344967c5c1912bde216559e7cd6ac62397290371f5fb3fdf8d4b52fb3575"></a>
<a id="asd__spec_8h_html_a3a542344967c5c1912bde216559e7cd6ad7a10f97094ddb96f26ab44fc34de12a"></a>
<a id="asd__spec_8h_html_a3a542344967c5c1912bde216559e7cd6adef5748e2622dab22da33504bbafa149"></a>
<a id="asd__spec_8h_html_a476ec98763d90a5cba336cbf22d6d553"></a>
<a id="asd__spec_8h_html_a476ec98763d90a5cba336cbf22d6d553a59fb3a34a7dba6ed1c86bca21cf97871"></a>
<a id="asd__spec_8h_html_a476ec98763d90a5cba336cbf22d6d553a759c63670d0dd41590fdb940a48ac4dd"></a>
<a id="asd__spec_8h_html_a5466ef2e30578d03c61831aa09fd7b9a"></a>
<a id="asd__spec_8h_html_a5466ef2e30578d03c61831aa09fd7b9aa106c43d63c3b3c02d3835ccf542f3190"></a>
<a id="asd__spec_8h_html_a5466ef2e30578d03c61831aa09fd7b9aa5c5c100c048986ecfed728690d05ac55"></a>
<a id="asd__spec_8h_html_a5466ef2e30578d03c61831aa09fd7b9aa72e9ad81edf54b7139a758d47fe54dd5"></a>
<a id="asd__spec_8h_html_a5466ef2e30578d03c61831aa09fd7b9aaad6eabbee29e4ff07bdf93a9162aea6b"></a>
<a id="asd__spec_8h_html_a5466ef2e30578d03c61831aa09fd7b9aad61b9d180a8de3c01be2e892c45504fb"></a>
<a id="asd__spec_8h_html_a5466ef2e30578d03c61831aa09fd7b9aaff651e04c107beb23e0bd76d03029b26"></a>
<a id="asd__spec_8h_html_a5ac0e70389dc6ccec515530df4eab972"></a>
<a id="asd__spec_8h_html_a5ac0e70389dc6ccec515530df4eab972a134ed84475be6f55a0f3d3ae9201cbe9"></a>
<a id="asd__spec_8h_html_a5ac0e70389dc6ccec515530df4eab972a83f1d375e4c5aa645759cc4e4462f8e0"></a>
<a id="asd__spec_8h_html_a5ac0e70389dc6ccec515530df4eab972ad548c59ebbb5045e437157cb9186de19"></a>
<a id="asd__spec_8h_html_a5ac0e70389dc6ccec515530df4eab972af44faa0f33705ecbd37b5f3544105e34"></a>
<a id="asd__spec_8h_html_a66c69cd7d7818af86b6a91fad68334c2"></a>
<a id="asd__spec_8h_html_a66c69cd7d7818af86b6a91fad68334c2a1b1e411f733ad6c1dc41896744441a48"></a>
<a id="asd__spec_8h_html_a66c69cd7d7818af86b6a91fad68334c2aa3e190aa6edb9f6eb7e29b78fc6f1a8a"></a>
<a id="asd__spec_8h_html_a66c69cd7d7818af86b6a91fad68334c2ad5753bf6fae3f43ef8ce7cb7eb169b61"></a>
<a id="asd__spec_8h_html_a66c69cd7d7818af86b6a91fad68334c2ad870ea9b9fc07a4af81bce3c82330441"></a>
<a id="asd__spec_8h_html_a6b42b86d8f2ba4f29787c7c6f3d97f36"></a>
<a id="asd__spec_8h_html_a6b42b86d8f2ba4f29787c7c6f3d97f36a022acb9d379c5ecf9935150ec6f51ffc"></a>
<a id="asd__spec_8h_html_a6b42b86d8f2ba4f29787c7c6f3d97f36a30f38c9e54bed572ca315fdeb9122103"></a>
<a id="asd__spec_8h_html_a6b42b86d8f2ba4f29787c7c6f3d97f36a360c72912e023e5b21363f3701deaa50"></a>
<a id="asd__spec_8h_html_a6b42b86d8f2ba4f29787c7c6f3d97f36a5593992de690adb1022b7926d1508ab3"></a>
<a id="asd__spec_8h_html_a6b42b86d8f2ba4f29787c7c6f3d97f36a90413fe7dfd8568eeac79709ece7a549"></a>
<a id="asd__spec_8h_html_a6b42b86d8f2ba4f29787c7c6f3d97f36ae07a7ef1ffce64bab52c5f6612a96716"></a>
<a id="asd__spec_8h_html_a6b42b86d8f2ba4f29787c7c6f3d97f36aef2ef100dab4187c8600ea721e8726dd"></a>
<a id="asd__spec_8h_html_a76f7ea4b395028ad5d8cc5eee32656e3"></a>
<a id="asd__spec_8h_html_a76f7ea4b395028ad5d8cc5eee32656e3a72c39e3140ddd3990c3cbe7c6c867bb1"></a>
<a id="asd__spec_8h_html_a76f7ea4b395028ad5d8cc5eee32656e3ae126f56fd639cbd686321a088d1e05e6"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61a0c8a74f1b50f574b64184bf1cdc1458f"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61a4cfc3b5856c525eda63b3a8b5fce5ae2"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61a541be7abf94851538a38f69c2ecb6b5f"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61a5f680f7a518294d7a706b73bbecbdb73"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61a624191bea93e1a350073fe2e5d5adaf1"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61a69d58775148ae7daf65598d6cf90488d"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61a76356316ead27df98dac310eed775707"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61a83a9f603da11b75f200d3bb62528cda4"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61a8ae4a104d50c0bdcae4722de0d5ee605"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61a98c205ed0f08df1a2f9e2801f02bbe7f"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61aca49de7bd24df65fd6448a7e570b04a8"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61acd85dd4f874ed9088e6d7a2260d7bc50"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61ae344e23bbc73a6f2ed17d10618bf7a5a"></a>
<a id="asd__spec_8h_html_a7b20cc85df2d9f5ce6c010907d7d5c61ae5e13b78bf3fdece36190e48136927bf"></a>
<a id="asd__spec_8h_html_a947520a05fc99c25449fab98d0d02b1e"></a>
<a id="asd__spec_8h_html_a9660a61775e481ae4093e11ce9336539"></a>
<a id="asd__spec_8h_html_a9660a61775e481ae4093e11ce9336539a14dec2b314ed13974dbba31f33a5eab9"></a>
<a id="asd__spec_8h_html_a9660a61775e481ae4093e11ce9336539a16c56ed964cc6bbb5cc6f0cb857d4f10"></a>
<a id="asd__spec_8h_html_a9660a61775e481ae4093e11ce9336539a39e410f7f5c51753bf415f727551b9fb"></a>
<a id="asd__spec_8h_html_a9660a61775e481ae4093e11ce9336539a5c37aeeb3c68d7b3dbe8b9001a00507c"></a>
<a id="asd__spec_8h_html_a9660a61775e481ae4093e11ce9336539a66ecc8c1a73181d70e23424cf718728d"></a>
<a id="asd__spec_8h_html_a9660a61775e481ae4093e11ce9336539a66ef44acd4ff3fafc2d49120df4b3c10"></a>
<a id="asd__spec_8h_html_a9660a61775e481ae4093e11ce9336539a788a77f1e7a468c14ef57319ef8938f3"></a>
<a id="asd__spec_8h_html_a9660a61775e481ae4093e11ce9336539a9570bb04b0181b4fbdc96cace060d187"></a>
<a id="asd__spec_8h_html_a9660a61775e481ae4093e11ce9336539ad5e9d57ee155e1b919f6cc213b05424f"></a>
<a id="asd__spec_8h_html_a9660a61775e481ae4093e11ce9336539ae9369c1cd7595ab83289fc356e9cc1b6"></a>
<a id="asd__spec_8h_html_a97f4810585247f5fed41110413e49853"></a>
<a id="asd__spec_8h_html_a97f4810585247f5fed41110413e49853a488b1aac4a0658c8b04b94b7556a2c5b"></a>
<a id="asd__spec_8h_html_a97f4810585247f5fed41110413e49853a5e617dd9de3620481b89e517bd2c3a4b"></a>
<a id="asd__spec_8h_html_a97f4810585247f5fed41110413e49853a8c620d198b195d913ad3ff913434d764"></a>
<a id="asd__spec_8h_html_a97f4810585247f5fed41110413e49853aa38ef885442708891b4ddc4a83c6ff66"></a>
<a id="asd__spec_8h_html_a98c4f218acfa21e124aa22e9fe209437"></a>
<a id="asd__spec_8h_html_a98c4f218acfa21e124aa22e9fe209437a0d907c1a9e69435433c5bf19bfacbd73"></a>
<a id="asd__spec_8h_html_a98c4f218acfa21e124aa22e9fe209437a1258364107909d0c4f8e9b7dba59300c"></a>
<a id="asd__spec_8h_html_a98c4f218acfa21e124aa22e9fe209437a16d3fd179853f1f15b980d2b82b572be"></a>
<a id="asd__spec_8h_html_a98c4f218acfa21e124aa22e9fe209437a2e75506280c1b4d5866f4dd8f2518be8"></a>
<a id="asd__spec_8h_html_a98c4f218acfa21e124aa22e9fe209437a7496edd5c7ec694d2d175bf751de1458"></a>
<a id="asd__spec_8h_html_a98c4f218acfa21e124aa22e9fe209437a988758fe0720e6fc33564076e3bc51bf"></a>
<a id="asd__spec_8h_html_a98c4f218acfa21e124aa22e9fe209437aa0c70fee97e29875394efc2a4c2fa274"></a>
<a id="asd__spec_8h_html_a98c4f218acfa21e124aa22e9fe209437aa8b8f850196e47799cb9b2cd06650520"></a>
<a id="asd__spec_8h_html_a98c4f218acfa21e124aa22e9fe209437ac353a0c3c1ac62920efdc42879a81cff"></a>
<a id="asd__spec_8h_html_a98c4f218acfa21e124aa22e9fe209437aca7d98319db6a23b30625828807e2143"></a>
<a id="asd__spec_8h_html_a98c4f218acfa21e124aa22e9fe209437af85839612e4fcc94eb2bd0986bd1740c"></a>
<a id="asd__spec_8h_html_aa0686c333989b0551d3af5eb01de4065"></a>
<a id="asd__spec_8h_html_aa0686c333989b0551d3af5eb01de4065a081f03ba34d8cd168ab5d4172d3c8d6a"></a>
<a id="asd__spec_8h_html_aa0686c333989b0551d3af5eb01de4065a135f072a7d9ee5967a49f7a164816854"></a>
<a id="asd__spec_8h_html_aa0686c333989b0551d3af5eb01de4065a1ddcc2a60e6f83538151fc93ad434ddf"></a>
<a id="asd__spec_8h_html_aa0686c333989b0551d3af5eb01de4065a3feb7a1594dc32703d2fbf6e43e77c0c"></a>
<a id="asd__spec_8h_html_aa0686c333989b0551d3af5eb01de4065a59ead4a70e76c9b2d6c817f4e2847998"></a>
<a id="asd__spec_8h_html_aa0686c333989b0551d3af5eb01de4065a5d6d02968e18dd84af3583d282179e64"></a>
<a id="asd__spec_8h_html_aa0686c333989b0551d3af5eb01de4065abebe32c9b1e107c729f4e6ecf501ee1e"></a>
<a id="asd__spec_8h_html_aa0686c333989b0551d3af5eb01de4065ac906ebc564bfc63a7f4ce0350db6667b"></a>
<a id="asd__spec_8h_html_aa0686c333989b0551d3af5eb01de4065acccc283c3dc4a36992e76ea0b6f4d68b"></a>
<a id="asd__spec_8h_html_aa1b9e80034c783cc7ff43dc79ac5878f"></a>
<a id="asd__spec_8h_html_aa1b9e80034c783cc7ff43dc79ac5878fa3f8fde9c17c04f4500f5a86cf4d9e7df"></a>
<a id="asd__spec_8h_html_aa1b9e80034c783cc7ff43dc79ac5878fa47bb6389f20ceb840612266fedac0f7a"></a>
<a id="asd__spec_8h_html_aa1b9e80034c783cc7ff43dc79ac5878fa8f693e2ff4acfb3d652106fc25f8758f"></a>
<a id="asd__spec_8h_html_aa1b9e80034c783cc7ff43dc79ac5878fa92bcd0ee78ddba8dc551c7917a37a792"></a>
<a id="asd__spec_8h_html_aa1b9e80034c783cc7ff43dc79ac5878fac853010c32e85d30f9f5936851ac4ddb"></a>
<a id="asd__spec_8h_html_aa1b9e80034c783cc7ff43dc79ac5878fad33e5499a36259f5b881ce524a1f4159"></a>
<a id="asd__spec_8h_html_aa1b9e80034c783cc7ff43dc79ac5878faedbd66fd01bb87a4f55291c299589db7"></a>
<a id="asd__spec_8h_html_aa1b9e80034c783cc7ff43dc79ac5878faf74a4730cc3507a35179fe09da721a19"></a>
<a id="asd__spec_8h_html_aaf06bb2dcb6e359e08bae37d2f36bbc3"></a>
<a id="asd__spec_8h_html_aaf06bb2dcb6e359e08bae37d2f36bbc3a0a59356a4db1abd3f72a8c9778b04e66"></a>
<a id="asd__spec_8h_html_aaf06bb2dcb6e359e08bae37d2f36bbc3a4eb47f187f4aee8228b09a37d4669a4f"></a>
<a id="asd__spec_8h_html_aaf06bb2dcb6e359e08bae37d2f36bbc3a9c77ef6b4da1f8ac56ebe8be03504b69"></a>
<a id="asd__spec_8h_html_aaf06bb2dcb6e359e08bae37d2f36bbc3aa07d3031debe394b369d93fde728d406"></a>
<a id="asd__spec_8h_html_aaf06bb2dcb6e359e08bae37d2f36bbc3aae5e5c58313c1216448474da513ca2b6"></a>
<a id="asd__spec_8h_html_aaf06bb2dcb6e359e08bae37d2f36bbc3ae4785671c3a4dca332c10c9bc0a72fba"></a>
<a id="asd__spec_8h_html_aaf06bb2dcb6e359e08bae37d2f36bbc3ae50961a0eb0f59776a156facf51e4620"></a>
<a id="asd__spec_8h_html_abf77ec1ad65cc9c99dc930ed7a96301a"></a>
<a id="asd__spec_8h_html_abf77ec1ad65cc9c99dc930ed7a96301aa3525ee751a482ae1cd816e2674ac3160"></a>
<a id="asd__spec_8h_html_abf77ec1ad65cc9c99dc930ed7a96301aa39605b86ccfad6196721ddfbb84b33d6"></a>
<a id="asd__spec_8h_html_abf77ec1ad65cc9c99dc930ed7a96301aa9e3d0d084a7d8ad1b9d08e6b699084e6"></a>
<a id="asd__spec_8h_html_abf77ec1ad65cc9c99dc930ed7a96301aac09ddfacee85353e243d6a8cfe7eeba8"></a>
<a id="asd__spec_8h_html_ac12657ae7d3b8abc562d4d7929a86b65"></a>
<a id="asd__spec_8h_html_ac12657ae7d3b8abc562d4d7929a86b65a364c7067e73960bae74ed80320adb223"></a>
<a id="asd__spec_8h_html_ac12657ae7d3b8abc562d4d7929a86b65a6cd553669599181b3677cea94687f025"></a>
<a id="asd__spec_8h_html_ac12657ae7d3b8abc562d4d7929a86b65a6d2084ba4c729c2cb019582b975f652f"></a>
<a id="asd__spec_8h_html_ac12657ae7d3b8abc562d4d7929a86b65a9b12d90cd1590f68fc1031449c4560ec"></a>
<a id="asd__spec_8h_html_ac12657ae7d3b8abc562d4d7929a86b65aa23a07a4fe6f6dd8292215221d97d5e2"></a>
<a id="asd__spec_8h_html_ac12657ae7d3b8abc562d4d7929a86b65acc46ce7f993b3eb81c6a2a2daad84c34"></a>
<a id="asd__spec_8h_html_ac86d8a44f37c771cb666f69a516dff81"></a>
<a id="asd__spec_8h_html_ac86d8a44f37c771cb666f69a516dff81a0f4fc7047a7c813b9ada618ed05e09a4"></a>
<a id="asd__spec_8h_html_ac86d8a44f37c771cb666f69a516dff81a43b7acda3747eb2233c2f2a433ff71c7"></a>
<a id="asd__spec_8h_html_ac86d8a44f37c771cb666f69a516dff81a87a4c0efb7e10cccce939af5f60343ad"></a>
<a id="asd__spec_8h_html_ac86d8a44f37c771cb666f69a516dff81a9a960567b8ecbd6feff7e6337fc98567"></a>
<a id="asd__spec_8h_html_ac86d8a44f37c771cb666f69a516dff81aa0d4721b24d0cd71d6a8fbfc666a6e7c"></a>
<a id="asd__spec_8h_html_ac86d8a44f37c771cb666f69a516dff81ab84ae4edfcca8ccae2a0df0643d04ca2"></a>
<a id="asd__spec_8h_html_ac86d8a44f37c771cb666f69a516dff81aba4f3f30eaa7d3368743f78f3c355269"></a>
<a id="asd__spec_8h_html_ac86d8a44f37c771cb666f69a516dff81ad49da8223b68d35a4d95d6b48bb8a3f7"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155a"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa02d458f5c51dfb7554e17bad1acb591a"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa0815a9749fc47ea398752e886e222b65"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa0b9e2ded1a4aa629d698f3ba5584bcc2"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa1388a4a737946b04de90dcec9c719837"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa153195025c02879f23af882b6a4d7af4"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa3ac808a14aa22446db1101fe5f2cbfab"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa3c9f8c1239694b9bda4aca0d7f40a929"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa4ad410b3a28df509ab875d26ae431e21"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa4cf46d638fd781b73edd03b61dd5d1a2"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa51199d1fa7c1cda33fde647843394d65"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa6e3c05c3b4a44c9ec63f89554850abbc"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa72c5d7592912c25f0440fa38664dfc13"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa94c0a61d8f8aeb5ed7a13846eb81dfae"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aaa33240a72b4aeff90e48d8dd3b9419c5"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aaac890f2e8917f249f729e273f4180c8d"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aab6413ec799d46c7341e48f0b5146f400"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aab852db2cfe8d7581e1ad7a1c2aee5406"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aab8635ae93d3d927f662e88c9e55305eb"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aabb622edfda732a5fd3fec2b042951254"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aac5fb430e08cbab9b2cbf2015202641e2"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aac6c818a2d7443a820c3f027e2d799ad2"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aac7cb6855c33427bdf0a4e7d344281aaf"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aac99e88e470b5ecb04885b0289a96a2c8"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aafe9dd6c272ec4d1c04efdfa4d7e12870"></a>
<a id="asd__spec_8h_html_ae1956c4b374e2c8b6a585596e93ac345"></a>
<a id="asd__spec_8h_html_ae1956c4b374e2c8b6a585596e93ac345a17160707005c580fbd52dbd6b99699dd"></a>
<a id="asd__spec_8h_html_ae1956c4b374e2c8b6a585596e93ac345a39200c50c7e22c096db3ce1dd3fe78d5"></a>
<a id="asd__spec_8h_html_ae1956c4b374e2c8b6a585596e93ac345a4ea17060afbcd026387172c1af57bb43"></a>
<a id="asd__spec_8h_html_ae1956c4b374e2c8b6a585596e93ac345ae51a5474387816c03970aa0f8058b002"></a>
<a id="asd__spec_8h_html_ae82da8038d71cf36ce2237504b498930"></a>
<a id="asd__spec_8h_html_ae82da8038d71cf36ce2237504b498930a433d8a39f77a612dd8104ca49c71a76f"></a>
<a id="asd__spec_8h_html_ae82da8038d71cf36ce2237504b498930a787fb937df1275cb3d169e1dade2fb37"></a>
<a id="asd__spec_8h_html_ae82da8038d71cf36ce2237504b498930a7b6cef084cb3b83a91c05964951b05a6"></a>
<a id="asd__spec_8h_html_ae82da8038d71cf36ce2237504b498930a88f373b6ac9335667eb8adab49a04e10"></a>
<a id="asd__spec_8h_html_ae82da8038d71cf36ce2237504b498930aa858c50e3f53d635857084ab5801a204"></a>
<a id="asd__spec_8h_html_ae82da8038d71cf36ce2237504b498930aad980a4d433ffcf189a2e77b5d765861"></a>
<a id="asd__spec_8h_html_ae82da8038d71cf36ce2237504b498930aea7ebe2a07e1ed7727262d522815355b"></a>
<a id="asd__spec_8h_html_af9783799f316cbaed12e18ce9944b09d"></a>
<a id="asd__spec_8h_html_af9783799f316cbaed12e18ce9944b09da2cedd0b40bf81afb35792150b2d4964a"></a>
<a id="asd__spec_8h_html_af9783799f316cbaed12e18ce9944b09dabd4f3ffac3f52efe797ce3ee3c31a03f"></a>
<a id="asd__spec_8h_html_af9783799f316cbaed12e18ce9944b09dacf4d28d56a6c4925944ffc99072d46e9"></a>
<a id="asd__spec_8h_html_af9783799f316cbaed12e18ce9944b09daf5448a25c8b5a8411f059469112ef2be"></a>
<a id="asd__spec_8h_html_af9783799f316cbaed12e18ce9944b09dafed77d2aed13d59fa6645cb06fc21c43"></a>
<a id="asd__spec_8h_html_afeec7c838fcf2d5c01cf653e305c749a"></a>
<a id="asd__spec_8h_html_afeec7c838fcf2d5c01cf653e305c749aa02b4afca69adad8d7f220b8e4a76db45"></a>
<a id="asd__spec_8h_html_afeec7c838fcf2d5c01cf653e305c749aa0558ef06a64c10456d220e66a5bc0f8b"></a>
<a id="asd__spec_8h_html_afeec7c838fcf2d5c01cf653e305c749aa104798e5266441d5a2f356f50b01cb35"></a>
<a id="asd__spec_8h_html_afeec7c838fcf2d5c01cf653e305c749aa2511277c6c4ebe38bc7179312292710b"></a>
<a id="asd__spec_8h_html_afeec7c838fcf2d5c01cf653e305c749aa5458d4988d7076d854bd695307771858"></a>
<a id="asd__spec_8h_html_afeec7c838fcf2d5c01cf653e305c749aa923c57b4134ad360ed3f6abbabfa87f1"></a>
<a id="asd__spec_8h_html_afeec7c838fcf2d5c01cf653e305c749aab78269976cbb673b4e00d6059ec38f80"></a>
<a id="asd__spec_8h_html_afeec7c838fcf2d5c01cf653e305c749aac1f502da56d7d50b70898329da1ad21a"></a>
<a id="asd__spec_8h_html_afeec7c838fcf2d5c01cf653e305c749aad9777c04b150a28916f894f54417286c"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructmmc__device__type_html"></a>
<a id="astructmmc__device__type_html_a12bb36ef4914b9182f08c4310c85d70d"></a>
<a id="astructmmc__device__type_html_a24bee6ea4bd6d209b53b05fb9e040b38"></a>
<a id="astructmmc__device__type_html_a3f4bbe853ef59313a84acb5737cafdf4"></a>
<a id="astructmmc__device__type_html_a5d338770aca6d893e094f57211b0339e"></a>
<a id="astructmmc__device__type_html_a65bc5ecdb11da48c08a06d4c5c386590"></a>
<a id="astructmmc__device__type_html_a7027fdec8b21be17a2ba97b2b19a13da"></a>
<a id="astructmmc__device__type_html_aaa7bb99717ecde9e6cf265a6c5bb33f0"></a>
<a id="astructmmc__device__type_html_ab19f29678c18ba8740758ca136fd7744"></a>
<a id="astructmmc__ext__csd_html"></a>
<a id="astructmmc__ext__csd_html_a25fe8f962635be3d40b449203e7d34a2"></a>
<a id="astructmmc__ext__csd_html_a286b2783ac15dbec6fa3953f0cd69af4"></a>
<a id="astructmmc__ext__csd_html_a29a7f7502e6e6d93e76392b8ac45356f"></a>
<a id="astructmmc__ext__csd_html_a3a38f805cac18f3429f57edc7cbf2134"></a>
<a id="astructmmc__ext__csd_html_a3aafc3e2b5b59cb79535411178a35efe"></a>
<a id="astructmmc__ext__csd_html_a3ee512cb3c0e3698d940c04eed3aa665"></a>
<a id="astructmmc__ext__csd_html_a44aa7d6d1282a00a1875e92fb5b3c4b8"></a>
<a id="astructmmc__ext__csd_html_a4c26010052a69e060742e0a05b6ad98b"></a>
<a id="astructmmc__ext__csd_html_a63545477058cce0c5727637bcbb06a47"></a>
<a id="astructmmc__ext__csd_html_aa5089c06fcc9b6b60749388b594a12f5"></a>
<a id="astructmmc__ext__csd_html_acab002b3a28a3dc9bf58187e9e19a9fe"></a>
<a id="astructsd__cid_html"></a>
<a id="astructsd__cid_html_a11ec5fa23ae13ee084c093b27c1d381a"></a>
<a id="astructsd__cid_html_a46f36abc3c2b1f3e9aa34c199d2bfcf3"></a>
<a id="astructsd__cid_html_a50fbbc6844a1fde29a25a803ed9d0df7"></a>
<a id="astructsd__cid_html_a7d97bc0f58c766abd2501d923e163d40"></a>
<a id="astructsd__cid_html_aba79f6a5bdf963772ac3c77ac209faf2"></a>
<a id="astructsd__cid_html_ace04f0f28cb7e058e69fbbc643f66052"></a>
<a id="astructsd__csd_html"></a>
<a id="astructsd__csd_html_a029a893cdcd3765864c70476eb6dd64e"></a>
<a id="astructsd__csd_html_a06f6aef4f4745a78bcf769df5415daa6"></a>
<a id="astructsd__csd_html_a0d1efea12c467eacd0d0f98a0bb0ac91"></a>
<a id="astructsd__csd_html_a37b15b70967c9317183b3e5e7837b228"></a>
<a id="astructsd__csd_html_a53b364ce0db06b9217259afeb625da44"></a>
<a id="astructsd__csd_html_a583c715045b5934ad94ab9cf61b25b06"></a>
<a id="astructsd__csd_html_a8bfd2c42066d85058d01076fcaa7a32d"></a>
<a id="astructsd__csd_html_a96bc4672222dece77d29ffc9287c59ac"></a>
<a id="astructsd__csd_html_a9c362eff38daf7d00776416ed064de24"></a>
<a id="astructsd__csd_html_a9d5a952bc6c2a6967e9a88cd93f19e89"></a>
<a id="astructsd__csd_html_aa868cfc1db75eb2913d21bffeaf29fd9"></a>
<a id="astructsd__csd_html_ab8d5ae38b19f7ea83b0856ad093c65cb"></a>
<a id="astructsd__csd_html_ad2f31731d7ec0b101d911fe20b5d94db"></a>
<a id="astructsd__csd_html_ad35b07abba80e9929c5eed40e37d25b3"></a>
<a id="astructsd__csd_html_adff7d405662589ec44f4d0a6b3548760"></a>
<a id="astructsd__csd_html_ae10b32787aeedd4789d657eb1ef492eb"></a>
<a id="astructsd__csd_html_ae39272173a5253d0d11ef04a2e129db6"></a>
<a id="astructsd__csd_html_af93239157610a6eeea420c29432d5412"></a>
<a id="astructsd__scr_html"></a>
<a id="astructsd__scr_html_a15f60bc2115b943ce938f3a96dd8e547"></a>
<a id="astructsd__scr_html_a3fc37c731dfb5c5596b6389152479c07"></a>
<a id="astructsd__scr_html_a40d30ccc4daf2c32f2ac162b402f3887"></a>
<a id="astructsd__scr_html_a9016ca73a668499289c52355ebb83cb1"></a>
<a id="astructsd__scr_html_a9f8254b5fe6911156bae727e29262f5a"></a>
<a id="astructsd__scr_html_aba20efcf752335f1a86d0a86607d92d0"></a>
<a id="astructsd__scr_html_abda65da85e20979a1fc71f2aea1f947b"></a>
<a id="astructsd__scr_html_ae6201af1083efa828cced000874bf197"></a>
<a id="astructsd__switch__caps_html"></a>
<a id="astructsd__switch__caps_html_a29024de744d65fb3d8fe51c4d4424aee"></a>
<a id="astructsd__switch__caps_html_a4b531af598bea14c90b8973daf1422dc"></a>
<a id="astructsd__switch__caps_html_a7262e4be5e3f59d047e569e1c24f04b3"></a>
<a id="astructsd__switch__caps_html_a7465b3fe6bd1f317eeb3283a25da7278"></a>
<a id="astructsd__switch__caps_html_ab09d80f61bc79857ee39604959c8a578"></a>
<a id="astructsdio__cis_html"></a>
<a id="astructsdio__cis_html_a04c8a774c65f683185e5a32e15afb67c"></a>
<a id="astructsdio__cis_html_a1b340e20630994f91314be17dd9055ca"></a>
<a id="astructsdio__cis_html_a56d3ee1d6b8d0d87e0efdbda15b7076d"></a>
<a id="astructsdio__cis_html_a86a01890f31788ae5465b1c8dc47bcf2"></a>
<a id="astructsdio__cis_html_ad38be5cade97ac92de62094d8e3b8549"></a>
<a id="astructsdio__cis_html_ad52e1df89176f728734ce0e69fb2b4c8"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright 2022-2023 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/*
 * SD card specification
 */

#ifndef ZEPHYR_INCLUDE_SD_SD_SPEC_H_
#define ZEPHYR_INCLUDE_SD_SD_SPEC_H_

#include <stdint.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif

enum sd_opcode {
        SD_GO_IDLE_STATE = 0,
        MMC_SEND_OP_COND = 1,
        SD_ALL_SEND_CID = 2,
        SD_SEND_RELATIVE_ADDR = 3,
        MMC_SEND_RELATIVE_ADDR = 3,
        SDIO_SEND_OP_COND = 5, /* SDIO cards only */
        SD_SWITCH = 6,
        SD_SELECT_CARD = 7,
        SD_SEND_IF_COND = 8,
        MMC_SEND_EXT_CSD = 8,
        SD_SEND_CSD = 9,
        SD_SEND_CID = 10,
        SD_VOL_SWITCH = 11,
        SD_STOP_TRANSMISSION = 12,
        SD_SEND_STATUS = 13,
        MMC_CHECK_BUS_TEST = 14,
        SD_GO_INACTIVE_STATE = 15,
        SD_SET_BLOCK_SIZE = 16,
        SD_READ_SINGLE_BLOCK = 17,
        SD_READ_MULTIPLE_BLOCK = 18,
        SD_SEND_TUNING_BLOCK = 19,
        MMC_SEND_BUS_TEST = 19,
        MMC_SEND_TUNING_BLOCK = 21,
        SD_SET_BLOCK_COUNT = 23,
        SD_WRITE_SINGLE_BLOCK = 24,
        SD_WRITE_MULTIPLE_BLOCK = 25,
        SD_ERASE_BLOCK_START = 32,
        SD_ERASE_BLOCK_END = 33,
        SD_ERASE_BLOCK_OPERATION = 38,
        SDIO_RW_DIRECT = 52,
        SDIO_RW_EXTENDED = 53,
        SD_APP_CMD = 55,
        SD_SPI_READ_OCR = 58, /* SPI mode only */
        SD_SPI_CRC_ON_OFF = 59, /* SPI mode only */
};

enum sd_app_cmd {
        SD_APP_SET_BUS_WIDTH = 6,
        SD_APP_SEND_STATUS = 13,
        SD_APP_SEND_NUM_WRITTEN_BLK = 22,
        SD_APP_SET_WRITE_BLK_ERASE_CNT = 23,
        SD_APP_SEND_OP_COND = 41,
        SD_APP_CLEAR_CARD_DETECT = 42,
        SD_APP_SEND_SCR = 51,
};

enum sd_r1_status {
        /* Bits 0-2 reserved */
        SD_R1_AUTH_ERR = BIT(3),
        /* Bit 4 reserved for SDIO */
        SD_R1_APP_CMD = BIT(5),
        SD_R1_FX_EVENT = BIT(6),
        /* Bit 7 reserved */
        SD_R1_RDY_DATA = BIT(8),
        SD_R1_CUR_STATE = (0xFU << 9),
        SD_R1_ERASE_RESET = BIT(13),
        SD_R1_ECC_DISABLED = BIT(14),
        SD_R1_ERASE_SKIP = BIT(15),
        SD_R1_CSD_OVERWRITE = BIT(16),
        /* Bits 17-18 reserved */
        SD_R1_ERR = BIT(19),
        SD_R1_CC_ERR = BIT(20),
        SD_R1_ECC_FAIL = BIT(21),
        SD_R1_ILLEGAL_CMD = BIT(22),
        SD_R1_CRC_ERR = BIT(23),
        SD_R1_UNLOCK_FAIL = BIT(24),
        SD_R1_CARD_LOCKED = BIT(25),
        SD_R1_WP_VIOLATION = BIT(26),
        SD_R1_ERASE_PARAM = BIT(27),
        SD_R1_ERASE_SEQ_ERR = BIT(28),
        SD_R1_BLOCK_LEN_ERR = BIT(29),
        SD_R1_ADDR_ERR = BIT(30),
        SD_R1_OUT_OF_RANGE = BIT(31),
        SD_R1_ERR_FLAGS = (SD_R1_AUTH_ERR |
                        SD_R1_ERASE_SKIP |
                        SD_R1_CSD_OVERWRITE |
                        SD_R1_ERR |
                        SD_R1_CC_ERR |
                        SD_R1_ECC_FAIL |
                        SD_R1_ILLEGAL_CMD |
                        SD_R1_CRC_ERR |
                        SD_R1_UNLOCK_FAIL |
                        SD_R1_WP_VIOLATION |
                        SD_R1_ERASE_PARAM |
                        SD_R1_ERASE_SEQ_ERR |
                        SD_R1_BLOCK_LEN_ERR |
                        SD_R1_ADDR_ERR |
                        SD_R1_OUT_OF_RANGE),
        SD_R1ERR_NONE = 0,
};

#define SD_R1_CURRENT_STATE(x) (((x) & SD_R1_CUR_STATE) >> 9U)

enum sd_r1_current_state {
        SDMMC_R1_IDLE = 0U,
        SDMMC_R1_READY = 1U,
        SDMMC_R1_IDENTIFY = 2U,
        SDMMC_R1_STANDBY = 3U,
        SDMMC_R1_TRANSFER = 4U,
        SDMMC_R1_SEND_DATA = 5U,
        SDMMC_R1_RECIVE_DATA = 6U,
        SDMMC_R1_PROGRAM = 7U,
        SDMMC_R1_DISCONNECT = 8U,
};

enum sd_spi_r1_error_flag {
        SD_SPI_R1PARAMETER_ERR = BIT(6),
        SD_SPI_R1ADDRESS_ERR = BIT(5),
        SD_SPI_R1ERASE_SEQ_ERR = BIT(4),
        SD_SPI_R1CMD_CRC_ERR = BIT(3),
        SD_SPI_R1ILLEGAL_CMD_ERR = BIT(2),
        SD_SPI_R1ERASE_RESET = BIT(1),
        SD_SPI_R1IDLE_STATE = BIT(0),
};

enum sd_spi_r2_status {
        SDHC_SPI_R2_CARD_LOCKED = BIT(8),
        SDHC_SPI_R2_UNLOCK_FAIL = BIT(9),
        SDHC_SPI_R2_ERR = BIT(10),
        SDHC_SPI_R2_CC_ERR = BIT(11),
        SDHC_SPI_R2_ECC_FAIL = BIT(12),
        SDHC_SPI_R2_WP_VIOLATION = BIT(13),
        SDHC_SPI_R2_ERASE_PARAM = BIT(14),
        SDHC_SPI_R2_OUT_OF_RANGE = BIT(15),
};

/* Byte length of SD SPI mode command */
#define SD_SPI_CMD_SIZE 6
#define SD_SPI_CMD_BODY_SIZE (SD_SPI_CMD_SIZE - 1)
/* Byte length of CRC16 appended to data blocks in SPI mode */
#define SD_SPI_CRC16_SIZE 2

/* SPI Command flags */
#define SD_SPI_START 0x80
#define SD_SPI_TX 0x40
#define SD_SPI_CMD 0x3F

/* SPI Data block tokens */
#define SD_SPI_TOKEN_SINGLE 0xFE
#define SD_SPI_TOKEN_MULTI_WRITE 0xFC
#define SD_SPI_TOKEN_STOP_TRAN 0xFD

/* SPI Data block responses */
#define SD_SPI_RESPONSE_ACCEPTED 0x05
#define SD_SPI_RESPONSE_CRC_ERR 0x0B
#define SD_SPI_RESPONSE_WRITE_ERR 0x0C

/* Masks used in SD interface condition query (CMD8) */
#define SD_IF_COND_VHS_MASK (0x0F << 8)
#define SD_IF_COND_VHS_3V3 BIT(8)
#define SD_IF_COND_CHECK 0xAA

enum sd_rsp_type {
        /* Native response types (lower 4 bits) */
        SD_RSP_TYPE_NONE = 0U,
        SD_RSP_TYPE_R1 = 1U,
        SD_RSP_TYPE_R1b = 2U,
        SD_RSP_TYPE_R2 = 3U,
        SD_RSP_TYPE_R3 = 4U,
        SD_RSP_TYPE_R4 = 5U,
        SD_RSP_TYPE_R5 = 6U,
        SD_RSP_TYPE_R5b = 7U,
        SD_RSP_TYPE_R6 = 8U,
        SD_RSP_TYPE_R7 = 9U,
        /* SPI response types (bits [7:4]) */
        SD_SPI_RSP_TYPE_R1 = (1U << 4),
        SD_SPI_RSP_TYPE_R1b = (2U << 4),
        SD_SPI_RSP_TYPE_R2 = (3U << 4),
        SD_SPI_RSP_TYPE_R3 = (4U << 4),
        SD_SPI_RSP_TYPE_R4 = (5U << 4),
        SD_SPI_RSP_TYPE_R5 = (6U << 4),
        SD_SPI_RSP_TYPE_R7 = (7U << 4),
};

enum sd_support_flag {
        SD_HIGH_CAPACITY_FLAG = BIT(1),
        SD_4BITS_WIDTH = BIT(2),
        SD_SDHC_FLAG = BIT(3),
        SD_SDXC_FLAG = BIT(4),
        SD_1800MV_FLAG = BIT(5),
        SD_3000MV_FLAG = BIT(6),
        SD_CMD23_FLAG = BIT(7),
        SD_SPEED_CLASS_CONTROL_FLAG = BIT(8),
        SD_MEM_PRESENT_FLAG = BIT(9),
};


enum sd_ocr_flag {
        SD_OCR_PWR_BUSY_FLAG = BIT(31),
        SD_OCR_HOST_CAP_FLAG = BIT(30),
        SD_OCR_CARD_CAP_FLAG = SD_OCR_HOST_CAP_FLAG,
        SD_OCR_SWITCH_18_REQ_FLAG = BIT(24),
        SD_OCR_SWITCH_18_ACCEPT_FLAG = SD_OCR_SWITCH_18_REQ_FLAG,
        SD_OCR_VDD27_28FLAG = BIT(15),
        SD_OCR_VDD28_29FLAG = BIT(16),
        SD_OCR_VDD29_30FLAG = BIT(17),
        SD_OCR_VDD30_31FLAG = BIT(18),
        SD_OCR_VDD31_32FLAG = BIT(19),
        SD_OCR_VDD32_33FLAG = BIT(20),
        SD_OCR_VDD33_34FLAG = BIT(21),
        SD_OCR_VDD34_35FLAG = BIT(22),
        SD_OCR_VDD35_36FLAG = BIT(23),
};

enum mmc_ocr_flag {
        MMC_OCR_VDD170_195FLAG = BIT(7),
        MMC_OCR_VDD20_26FLAG = 0x7F << 8,
        MMC_OCR_VDD27_36FLAG = 0x1FF << 15,
        MMC_OCR_SECTOR_MODE = BIT(30),
        MMC_OCR_PWR_BUSY_FLAG = BIT(31)
};

#define SDIO_OCR_IO_NUMBER_SHIFT 28
/* Lower 24 bits hold SDIO I/O OCR */
#define SDIO_IO_OCR_MASK 0xFFFFFF

enum sdio_ocr_flag {
        SDIO_OCR_IO_READY_FLAG = BIT(31),
        SDIO_OCR_IO_NUMBER = (7U << 28U),
        SDIO_OCR_MEM_PRESENT_FLAG = BIT(27),
        SDIO_OCR_180_VOL_FLAG = BIT(24),
        SDIO_OCR_VDD20_21FLAG = BIT(8),
        SDIO_OCR_VDD21_22FLAG = BIT(9),
        SDIO_OCR_VDD22_23FLAG = BIT(10),
        SDIO_OCR_VDD23_24FLAG = BIT(11),
        SDIO_OCR_VDD24_25FLAG = BIT(12),
        SDIO_OCR_VDD25_26FLAG = BIT(13),
        SDIO_OCR_VDD26_27FLAG = BIT(14),
        SDIO_OCR_VDD27_28FLAG = BIT(15),
        SDIO_OCR_VDD28_29FLAG = BIT(16),
        SDIO_OCR_VDD29_30FLAG = BIT(17),
        SDIO_OCR_VDD30_31FLAG = BIT(18),
        SDIO_OCR_VDD31_32FLAG = BIT(19),
        SDIO_OCR_VDD32_33FLAG = BIT(20),
        SDIO_OCR_VDD33_34FLAG = BIT(21),
        SDIO_OCR_VDD34_35FLAG = BIT(22),
        SDIO_OCR_VDD35_36FLAG = BIT(23),
};


enum sd_switch_arg {
        SD_SWITCH_CHECK = 0U,
        SD_SWITCH_SET = 1U,
};

enum sd_group_num {
        SD_GRP_TIMING_MODE = 0U,
        SD_GRP_CMD_SYS_MODE = 1U,
        SD_GRP_DRIVER_STRENGTH_MODE = 2U,
        SD_GRP_CURRENT_LIMIT_MODE = 3U,
};

/* Maximum data rate possible for SD high speed cards */
enum hs_max_data_rate {
        HS_UNSUPPORTED = 0,
        HS_MAX_DTR = MHZ(50),
};

/* Maximum data rate possible for SD uhs cards */
enum uhs_max_data_rate {
        UHS_UNSUPPORTED = 0,
        UHS_SDR12_MAX_DTR = MHZ(25),
        UHS_SDR25_MAX_DTR = MHZ(50),
        UHS_SDR50_MAX_DTR = MHZ(100),
        UHS_SDR104_MAX_DTR = MHZ(208),
        UHS_DDR50_MAX_DTR = MHZ(50),
};

enum sd_bus_speed {
        UHS_SDR12_BUS_SPEED = BIT(0),
        DEFAULT_BUS_SPEED = BIT(0),
        HIGH_SPEED_BUS_SPEED = BIT(1),
        UHS_SDR25_BUS_SPEED = BIT(1),
        UHS_SDR50_BUS_SPEED = BIT(2),
        UHS_SDR104_BUS_SPEED = BIT(3),
        UHS_DDR50_BUS_SPEED = BIT(4),
};

enum sd_timing_mode {
        SD_TIMING_DEFAULT = 0U,
        SD_TIMING_SDR12 = 0U,
        SD_TIMING_HIGH_SPEED = 1U,
        SD_TIMING_SDR25 = 1U,
        SD_TIMING_SDR50 = 2U,
        SD_TIMING_SDR104 = 3U,
        SD_TIMING_DDR50 = 4U,
};

enum sdhc_clock_speed {
        SDMMC_CLOCK_400KHZ = KHZ(400),
        SD_CLOCK_25MHZ = MHZ(25),
        SD_CLOCK_50MHZ = MHZ(50),
        SD_CLOCK_100MHZ = MHZ(100),
        SD_CLOCK_208MHZ = MHZ(208),
        MMC_CLOCK_26MHZ = MHZ(26),
        MMC_CLOCK_52MHZ = MHZ(52),
        MMC_CLOCK_DDR52 = MHZ(52),
        MMC_CLOCK_HS200 = MHZ(200),
        MMC_CLOCK_HS400 = MHZ(200), /* Same clock freq as HS200, just DDR */
};

enum sd_current_setting {
        SD_SET_CURRENT_200MA = 0,
        SD_SET_CURRENT_400MA = 1,
        SD_SET_CURRENT_600MA = 2,
        SD_SET_CURRENT_800MA = 3,
};

enum sd_current_limit {
        SD_MAX_CURRENT_200MA = BIT(0),
        SD_MAX_CURRENT_400MA = BIT(1),
        SD_MAX_CURRENT_600MA = BIT(2),
        SD_MAX_CURRENT_800MA = BIT(3),
};

enum sd_driver_type {
        SD_DRIVER_TYPE_B = 0x1,
        SD_DRIVER_TYPE_A = 0x2,
        SD_DRIVER_TYPE_C = 0x4,
        SD_DRIVER_TYPE_D = 0x8,
};

enum sd_driver_strength {
        SD_DRV_STRENGTH_TYPEB = 0U,
        SD_DRV_STRENGTH_TYPEA = 1U,
        SD_DRV_STRENGTH_TYPEC = 2U,
        SD_DRV_STRENGTH_TYPED = 3U,
};

struct sd_switch_caps {
        enum hs_max_data_rate hs_max_dtr;
        enum uhs_max_data_rate uhs_max_dtr;
        enum sd_bus_speed bus_speed;
        enum sd_driver_type sd_drv_type;
        enum sd_current_limit sd_current_limit;
};


#define SD_PRODUCT_NAME_BYTES 5

struct sd_cid {
        uint8_t manufacturer;
        uint16_t application;
        uint8_t name[SD_PRODUCT_NAME_BYTES];
        uint8_t version;
        uint32_t ser_num;
        uint16_t date;
};

struct sd_csd {
        uint8_t csd_structure;
        uint8_t read_time1;
        uint8_t read_time2;
        uint8_t xfer_rate;
        uint16_t cmd_class;
        uint8_t read_blk_len;
        uint16_t flags;
        uint32_t device_size;
        uint8_t read_current_min;
        uint8_t read_current_max;
        uint8_t write_current_min;
        uint8_t write_current_max;
        uint8_t dev_size_mul;
        uint8_t erase_size;
        uint8_t write_prtect_size;
        uint8_t write_speed_factor;
        uint8_t write_blk_len;
        uint8_t file_fmt;
};

enum mmc_csd_freq {
        MMC_MAXFREQ_100KHZ = 0U << 0U,
        MMC_MAXFREQ_1MHZ = 1U << 0U,
        MMC_MAXFREQ_10MHZ = 2U << 0U,
        MMC_MAXFREQ_100MHZ = 3U << 0U,
        MMC_MAXFREQ_MULT_10 = 1U << 3U,
        MMC_MAXFREQ_MULT_12 = 2U << 3U,
        MMC_MAXFREQ_MULT_13 = 3U << 3U,
        MMC_MAXFREQ_MULT_15 = 4U << 3U,
        MMC_MAXFREQ_MULT_20 = 5U << 3U,
        MMC_MAXFREQ_MULT_26 = 6U << 3U,
        MMC_MAXFREQ_MULT_30 = 7U << 3U,
        MMC_MAXFREQ_MULT_35 = 8U << 3U,
        MMC_MAXFREQ_MULT_40 = 9U << 3U,
        MMC_MAXFREQ_MULT_45 = 0xAU << 3U,
        MMC_MAXFREQ_MULT_52 = 0xBU << 3U,
        MMC_MAXFREQ_MULT_55 = 0xCU << 3U,
        MMC_MAXFREQ_MULT_60 = 0xDU << 3U,
        MMC_MAXFREQ_MULT_70 = 0xEU << 3U,
        MMC_MAXFREQ_MULT_80 = 0xFU << 3u
};

enum mmc_timing_mode {
        MMC_LEGACY_TIMING = 0U,
        MMC_HS_TIMING = 1U,
        MMC_HS200_TIMING = 2U,
        MMC_HS400_TIMING = 3U
};

enum mmc_driver_strengths {
        mmc_driv_type0 = 0U,
        mmc_driv_type1 = 1U,
        mmc_driv_type2 = 2U,
        mmc_driv_type3 = 3U,
        mmc_driv_type4 = 4U
};


struct mmc_device_type {
        bool MMC_HS400_DDR_1200MV;
        bool MMC_HS400_DDR_1800MV;
        bool MMC_HS200_SDR_1200MV;
        bool MMC_HS200_SDR_1800MV;
        bool MMC_HS_DDR_1200MV;
        bool MMC_HS_DDR_1800MV;
        bool MMC_HS_52_DV;
        bool MMC_HS_26_DV;
};

enum mmc_ext_csd_rev {
        MMC_5_1 = 8U,
        MMC_5_0 = 7U,
        MMC_4_5 = 6U,
        MMC_4_4 = 5U,
        MMC_4_3 = 3U,
        MMC_4_2 = 2U,
        MMC_4_1 = 1U,
        MMC_4_0 = 0U
};

struct mmc_ext_csd {
        uint32_t sec_count;
        uint8_t bus_width;
        bool enhanced_strobe_support;
        enum mmc_timing_mode hs_timing;
        struct mmc_device_type device_type;
        enum mmc_ext_csd_rev rev;
        uint8_t power_class;
        uint8_t mmc_driver_strengths;
        uint8_t pwr_class_200MHZ_VCCQ195;
        uint8_t pwr_class_HS400;
        uint32_t cache_size;
};

enum sd_csd_flag {
        SD_CSD_READ_BLK_PARTIAL_FLAG = BIT(0),
        SD_CSD_WRITE_BLK_MISALIGN_FLAG = BIT(1),
        SD_CSD_READ_BLK_MISALIGN_FLAG = BIT(2),
        SD_CSD_DSR_IMPLEMENTED_FLAG = BIT(3),
        SD_CSD_ERASE_BLK_EN_FLAG = BIT(4),
        SD_CSD_WRITE_PROTECT_GRP_EN_FLAG = BIT(5),
        SD_CSD_WRITE_BLK_PARTIAL_FLAG = BIT(6),
        SD_CSD_FILE_FMT_GRP_FLAG = BIT(7),
        SD_CSD_COPY_FLAG = BIT(8),
        SD_CSD_PERMANENT_WRITE_PROTECT_FLAG = BIT(9),
        SD_CSD_TMP_WRITE_PROTECT_FLAG = BIT(10),
};

struct sd_scr {
        uint8_t scr_structure;
        uint8_t sd_spec;
        uint16_t flags;
        uint8_t sd_sec;
        uint8_t sd_width;
        uint8_t sd_ext_sec;
        uint8_t cmd_support;
        uint32_t rsvd;
};

enum sd_scr_flag {
        SD_SCR_DATA_STATUS_AFTER_ERASE = BIT(0),
        SD_SCR_SPEC3 = BIT(1),
};

enum sd_spec_version {
        SD_SPEC_VER1_0 = BIT(0),
        SD_SPEC_VER1_1 = BIT(1),
        SD_SPEC_VER2_0 = BIT(2),
        SD_SPEC_VER3_0 = BIT(3),
};


#define SDMMC_DEFAULT_BLOCK_SIZE 512
#define MMC_EXT_CSD_BYTES 512
enum sdio_func_num {
        SDIO_FUNC_NUM_0 = 0,
        SDIO_FUNC_NUM_1 = 1,
        SDIO_FUNC_NUM_2 = 2,
        SDIO_FUNC_NUM_3 = 3,
        SDIO_FUNC_NUM_4 = 4,
        SDIO_FUNC_NUM_5 = 5,
        SDIO_FUNC_NUM_6 = 6,
        SDIO_FUNC_NUM_7 = 7,
        SDIO_FUNC_MEMORY = 8,
};

enum sdio_io_dir {
        SDIO_IO_READ = 0,
        SDIO_IO_WRITE = 1,
};

#define SDIO_CMD_ARG_RW_SHIFT 31
#define SDIO_CMD_ARG_FUNC_NUM_SHIFT 28
#define SDIO_DIRECT_CMD_ARG_RAW_SHIFT 27
#define SDIO_CMD_ARG_REG_ADDR_SHIFT 9
#define SDIO_CMD_ARG_REG_ADDR_MASK 0x1FFFF
#define SDIO_DIRECT_CMD_DATA_MASK 0xFF

#define SDIO_EXTEND_CMD_ARG_BLK_SHIFT 27
#define SDIO_EXTEND_CMD_ARG_OP_CODE_SHIFT 26

#define SDIO_CCCR_CCCR 0x00
#define SDIO_CCCR_CCCR_REV_MASK 0x0F
#define SDIO_CCCR_CCCR_REV_SHIFT 0x0
#define SDIO_CCCR_CCCR_REV_1_00 0x0
#define SDIO_CCCR_CCCR_REV_1_10 0x1
#define SDIO_CCCR_CCCR_REV_2_00 0x2
#define SDIO_CCCR_CCCR_REV_3_00 0x3

#define SDIO_CCCR_SD 0x01
#define SDIO_CCCR_SD_SPEC_MASK 0x0F
#define SDIO_CCCR_SD_SPEC_SHIFT 0x0

#define SDIO_CCCR_IO_EN 0x02

#define SDIO_CCCR_IO_RD 0x03

#define SDIO_CCCR_INT_EN 0x04

#define SDIO_CCCR_INT_P 0x05

#define SDIO_CCCR_ABORT 0x06

#define SDIO_CCCR_BUS_IF 0x07
#define SDIO_CCCR_BUS_IF_WIDTH_MASK 0x3
#define SDIO_CCCR_BUS_IF_WIDTH_1_BIT 0x00
#define SDIO_CCCR_BUS_IF_WIDTH_4_BIT 0x02
#define SDIO_CCCR_BUS_IF_WIDTH_8_BIT 0x03

#define SDIO_CCCR_CAPS 0x08
#define SDIO_CCCR_CAPS_SDC BIT(0)
#define SDIO_CCCR_CAPS_SMB BIT(1)
#define SDIO_CCCR_CAPS_SRW BIT(2)
#define SDIO_CCCR_CAPS_SBS BIT(3)
#define SDIO_CCCR_CAPS_S4MI BIT(4)
#define SDIO_CCCR_CAPS_E4MI BIT(5)
#define SDIO_CCCR_CAPS_LSC BIT(6)
#define SDIO_CCCR_CAPS_BLS BIT(7)

#define SDIO_CCCR_CIS 0x09

#define SDIO_CCCR_SPEED 0x13
#define SDIO_CCCR_SPEED_SHS BIT(0)
#define SDIO_CCCR_SPEED_MASK 0xE
#define SDIO_CCCR_SPEED_SHIFT 0x1
#define SDIO_CCCR_SPEED_SDR12 0x0
#define SDIO_CCCR_SPEED_HS 0x1
#define SDIO_CCCR_SPEED_SDR25 0x1
#define SDIO_CCCR_SPEED_SDR50 0x2
#define SDIO_CCCR_SPEED_SDR104 0x3
#define SDIO_CCCR_SPEED_DDR50 0x4

#define SDIO_CCCR_UHS 0x14
#define SDIO_CCCR_UHS_SDR50 BIT(0)
#define SDIO_CCCR_UHS_SDR104 BIT(1)
#define SDIO_CCCR_UHS_DDR50 BIT(2)

#define SDIO_CCCR_DRIVE_STRENGTH 0x15
#define SDIO_CCCR_DRIVE_STRENGTH_A BIT(0)
#define SDIO_CCCR_DRIVE_STRENGTH_C BIT(1)
#define SDIO_CCCR_DRIVE_STRENGTH_D BIT(2)

#define SDIO_FBR_BASE(n) ((n) * 0x100)

#define SDIO_FBR_CIS 0x09
#define SDIO_FBR_CSA 0x0C
#define SDIO_FBR_BLK_SIZE 0x10


#define SDIO_MAX_IO_NUMS 7

#define SDIO_TPL_CODE_NULL 0x00
#define SDIO_TPL_CODE_MANIFID 0x20
#define SDIO_TPL_CODE_FUNCID 0x21
#define SDIO_TPL_CODE_FUNCE 0x22
#define SDIO_TPL_CODE_END 0xFF

enum sdio_cccr_flags {
        SDIO_SUPPORT_HS = BIT(0),
        SDIO_SUPPORT_SDR50 = BIT(1),
        SDIO_SUPPORT_SDR104 = BIT(2),
        SDIO_SUPPORT_DDR50 = BIT(3),
        SDIO_SUPPORT_4BIT_LS_BUS = BIT(4),
        SDIO_SUPPORT_MULTIBLOCK = BIT(5),
};

struct sdio_cis {
        /* Manufacturer ID string tuple */
        uint16_t manf_id;
        uint16_t manf_code;
        /* Function identification tuple */
        uint8_t func_id;
        /* Function extension table */
        uint16_t max_blk_size;
        uint8_t max_speed;
        uint16_t rdy_timeout;
};

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SD_SD_SPEC_H_ */
```

## 15.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022-2023 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 7 行

SD 卡规范（Specification）。

### 注释 3：原第 34 行

仅适用于 SDIO 卡。

### 注释 4：原第 61 行

仅适用于 SPI 模式。

### 注释 5：原第 62 行

仅适用于 SPI 模式。

### 注释 6：原第 87 行

位 0–2 保留。

### 注释 7：原第 89 行

位 4 为 SDIO 保留。

### 注释 8：原第 92 行

位 7 保留。

### 注释 9：原第 99 行

位 17–18 保留。

### 注释 10：原第 182 行

SD SPI 模式命令的字节长度。

### 注释 11：原第 185 行

SPI 模式下附加在数据块后的 CRC-16 的字节长度。

### 注释 12：原第 188 行

SPI 命令标志（Command flags）。

### 注释 13：原第 193 行

SPI 数据块令牌（Data block tokens）。

### 注释 14：原第 198 行

SPI 数据块响应（Data block responses）。

### 注释 15：原第 203 行

SD 接口条件查询（Interface condition query，CMD8）使用的掩码。

### 注释 16：原第 215 行

原生响应类型（Native response types），位于低 4 位。

### 注释 17：原第 226 行

SPI 响应类型，位于位 `[7:4]`。

### 注释 18：原第 306 行

低 24 位保存 SDIO I/O 的操作条件寄存器（OCR）值。

### 注释 19：原第 370 行

SD 高速卡（High speed cards）可达到的最大数据速率。

### 注释 20：原第 376 行

SD 超高速卡（UHS cards）可达到的最大数据速率。

### 注释 21：原第 440 行

时钟频率与 HS200 相同，但采用双数据速率（DDR）。

### 注释 22：原第 921 行

制造商 ID 字符串元组（Tuple）。

### 注释 23：原第 924 行

功能标识元组（Function identification tuple）。

### 注释 24：原第 926 行

功能扩展表（Function extension table）。

### 注释 25：原第 936 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SD_SD_SPEC_H_`。

## 15.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [sd_opcode](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99)
- [SD_GO_IDLE_STATE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a9dcb2e5fb6a5a53c6cb02422fd1fef3c)
- [MMC_SEND_OP_COND](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a54546b311e446754738a9b6f1e3eaea4)
- [SD_ALL_SEND_CID](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99affcc3d18f6bda30fb3fd34916d8f61fe)
- [SD_SEND_RELATIVE_ADDR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a35c39a93dfcc239fcb80db70449af99e)
- [MMC_SEND_RELATIVE_ADDR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a56c94068ecb32eb9ced47d4a3bf95481)
- [SDIO_SEND_OP_COND](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99af48c850f0aa9e9f9dbce8fc8855f6a2a)
- [SD_SWITCH](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a400dc3acd2ae8320f130dbea80c81969)
- [SD_SELECT_CARD](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99afa15c17b4fb95747b444616b085b4905)
- [SD_SEND_IF_COND](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a0da09225692b10e51140d4f15ba1dd0a)
- [MMC_SEND_EXT_CSD](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a7c9bfc788861214fae86e22443e9484a)
- [SD_SEND_CSD](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99adc7e589c9352cddf856b2e868f93a097)
- [SD_SEND_CID](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a8c3edf14ca3a6e04c1949a40cd3fb135)
- [SD_VOL_SWITCH](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99ad6d6f1ccdabc2970ac2ab6c7a853b37e)
- [SD_STOP_TRANSMISSION](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99aa5f2d8c27d0b7ae780734cb4bedbf8a4)
- [SD_SEND_STATUS](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99ad822462692847b4e8433157cd75eef70)
- [MMC_CHECK_BUS_TEST](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a45bc2d4b117d144ef5191719f9b6c297)
- [SD_GO_INACTIVE_STATE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a5c85e3208bb686d8ded9ae0fe7bd9d53)
- [SD_SET_BLOCK_SIZE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99abd97c835c80320637579c692d6f57878)
- [SD_READ_SINGLE_BLOCK](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a99c20a704cce28fee37b9b0f14b2ff15)
- [SD_READ_MULTIPLE_BLOCK](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99aa58b1d9f75b639dc1b28163988bc8aa3)
- [SD_SEND_TUNING_BLOCK](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99af48292861388f111b0afad64f0352664)
- [MMC_SEND_BUS_TEST](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a35b942802a4238882440f2e470f2555f)
- [MMC_SEND_TUNING_BLOCK](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a0378338c2747ba8947d8ffcb18f77d51)
- [SD_SET_BLOCK_COUNT](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a7e34ea8ce2a215c2a76f4184b84a06f2)
- [SD_WRITE_SINGLE_BLOCK](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99adca664fbf5ff0b4d174ca21641e01004)
- [SD_WRITE_MULTIPLE_BLOCK](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a9cd6e9c88c3989531a71015147496895)
- [SD_ERASE_BLOCK_START](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99aa7c628982851eba38074d02e9e335b57)
- [SD_ERASE_BLOCK_END](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a753b0fc3e44a4376998e5887ed2c5901)
- [SD_ERASE_BLOCK_OPERATION](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a4aa36f7d8ceaa3cdab300915453b64b5)
- [SDIO_RW_DIRECT](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a7ef64e231154de2e461005af29918b86)
- [SDIO_RW_EXTENDED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99a7ccf37711e67b58534689997ac1375df)
- [SD_APP_CMD](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99aef4ee3246cd66cd7d48f1dabf3fcd7ef)
- [SD_SPI_READ_OCR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99aa3183436decfa0e42ac0461629258ba3)
- [SD_SPI_CRC_ON_OFF](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a072705601a34c697515f74acb0474c99ab590e9d9b3213f31a2399ef379d066aa)
- [sd_app_cmd](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1c77191f9cb8c50e8e2a03cda2984dbc)
- [SD_APP_SET_BUS_WIDTH](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1c77191f9cb8c50e8e2a03cda2984dbcaca51b75cde3505fd672391b9d7a7997a)
- [SD_APP_SEND_STATUS](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1c77191f9cb8c50e8e2a03cda2984dbca36f78cdbd8fcc962c2247d7fc1f33f9b)
- [SD_APP_SEND_NUM_WRITTEN_BLK](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1c77191f9cb8c50e8e2a03cda2984dbca03fc81eeed7047ad914ce6590511dfa3)
- [SD_APP_SET_WRITE_BLK_ERASE_CNT](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1c77191f9cb8c50e8e2a03cda2984dbcacf330302cc8ef7f55d76c2cace40649e)
- [SD_APP_SEND_OP_COND](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1c77191f9cb8c50e8e2a03cda2984dbca2a4278c079a227145f63f5f2d860146a)
- [SD_APP_CLEAR_CARD_DETECT](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1c77191f9cb8c50e8e2a03cda2984dbcaa4a44bb015be3cbcf180f34a39ba8e05)
- [SD_APP_SEND_SCR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1c77191f9cb8c50e8e2a03cda2984dbca305b2fb720b5191c762b77b886152ca8)
- [sd_r1_status](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155a)
- [SD_R1_AUTH_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aaa33240a72b4aeff90e48d8dd3b9419c5)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SD_R1_APP_CMD](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa72c5d7592912c25f0440fa38664dfc13)
- [SD_R1_FX_EVENT](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aab852db2cfe8d7581e1ad7a1c2aee5406)
- [SD_R1_RDY_DATA](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aac99e88e470b5ecb04885b0289a96a2c8)
- [SD_R1_CUR_STATE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa0815a9749fc47ea398752e886e222b65)
- [SD_R1_ERASE_RESET](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa3c9f8c1239694b9bda4aca0d7f40a929)
- [SD_R1_ECC_DISABLED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa4cf46d638fd781b73edd03b61dd5d1a2)
- [SD_R1_ERASE_SKIP](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa1388a4a737946b04de90dcec9c719837)
- [SD_R1_CSD_OVERWRITE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa0b9e2ded1a4aa629d698f3ba5584bcc2)
- [SD_R1_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aac6c818a2d7443a820c3f027e2d799ad2)
- [SD_R1_CC_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aaac890f2e8917f249f729e273f4180c8d)
- [SD_R1_ECC_FAIL](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aafe9dd6c272ec4d1c04efdfa4d7e12870)
- [SD_R1_ILLEGAL_CMD](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa6e3c05c3b4a44c9ec63f89554850abbc)
- [SD_R1_CRC_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aac5fb430e08cbab9b2cbf2015202641e2)
- [SD_R1_UNLOCK_FAIL](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa51199d1fa7c1cda33fde647843394d65)
- [SD_R1_CARD_LOCKED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa02d458f5c51dfb7554e17bad1acb591a)
- [SD_R1_WP_VIOLATION](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa3ac808a14aa22446db1101fe5f2cbfab)
- [SD_R1_ERASE_PARAM](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa4ad410b3a28df509ab875d26ae431e21)
- [SD_R1_ERASE_SEQ_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa94c0a61d8f8aeb5ed7a13846eb81dfae)
- [SD_R1_BLOCK_LEN_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aabb622edfda732a5fd3fec2b042951254)
- [SD_R1_ADDR_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aa153195025c02879f23af882b6a4d7af4)
- [SD_R1_OUT_OF_RANGE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aac7cb6855c33427bdf0a4e7d344281aaf)
- [SD_R1_ERR_FLAGS](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aab6413ec799d46c7341e48f0b5146f400)
- [SD_R1ERR_NONE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ad38162e32b87d3c01f1ae46d3423155aab8635ae93d3d927f662e88c9e55305eb)
- [sd_r1_current_state](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa0686c333989b0551d3af5eb01de4065)
- [SDMMC_R1_IDLE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa0686c333989b0551d3af5eb01de4065a081f03ba34d8cd168ab5d4172d3c8d6a)
- [SDMMC_R1_READY](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa0686c333989b0551d3af5eb01de4065a135f072a7d9ee5967a49f7a164816854)
- [SDMMC_R1_IDENTIFY](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa0686c333989b0551d3af5eb01de4065a1ddcc2a60e6f83538151fc93ad434ddf)
- [SDMMC_R1_STANDBY](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa0686c333989b0551d3af5eb01de4065ac906ebc564bfc63a7f4ce0350db6667b)
- [SDMMC_R1_TRANSFER](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa0686c333989b0551d3af5eb01de4065a59ead4a70e76c9b2d6c817f4e2847998)
- [SDMMC_R1_SEND_DATA](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa0686c333989b0551d3af5eb01de4065a5d6d02968e18dd84af3583d282179e64)
- [SDMMC_R1_RECIVE_DATA](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa0686c333989b0551d3af5eb01de4065a3feb7a1594dc32703d2fbf6e43e77c0c)
- [SDMMC_R1_PROGRAM](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa0686c333989b0551d3af5eb01de4065acccc283c3dc4a36992e76ea0b6f4d68b)
- [SDMMC_R1_DISCONNECT](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa0686c333989b0551d3af5eb01de4065abebe32c9b1e107c729f4e6ecf501ee1e)
- [sd_spi_r1_error_flag](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aaf06bb2dcb6e359e08bae37d2f36bbc3)
- [SD_SPI_R1PARAMETER_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aaf06bb2dcb6e359e08bae37d2f36bbc3aae5e5c58313c1216448474da513ca2b6)
- [SD_SPI_R1ADDRESS_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aaf06bb2dcb6e359e08bae37d2f36bbc3ae50961a0eb0f59776a156facf51e4620)
- [SD_SPI_R1ERASE_SEQ_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aaf06bb2dcb6e359e08bae37d2f36bbc3aa07d3031debe394b369d93fde728d406)
- [SD_SPI_R1CMD_CRC_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aaf06bb2dcb6e359e08bae37d2f36bbc3ae4785671c3a4dca332c10c9bc0a72fba)
- [SD_SPI_R1ILLEGAL_CMD_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aaf06bb2dcb6e359e08bae37d2f36bbc3a0a59356a4db1abd3f72a8c9778b04e66)
- [SD_SPI_R1ERASE_RESET](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aaf06bb2dcb6e359e08bae37d2f36bbc3a4eb47f187f4aee8228b09a37d4669a4f)
- [SD_SPI_R1IDLE_STATE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aaf06bb2dcb6e359e08bae37d2f36bbc3a9c77ef6b4da1f8ac56ebe8be03504b69)
- [sd_spi_r2_status](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa1b9e80034c783cc7ff43dc79ac5878f)
- [SDHC_SPI_R2_CARD_LOCKED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa1b9e80034c783cc7ff43dc79ac5878fa8f693e2ff4acfb3d652106fc25f8758f)
- [SDHC_SPI_R2_UNLOCK_FAIL](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa1b9e80034c783cc7ff43dc79ac5878fa3f8fde9c17c04f4500f5a86cf4d9e7df)
- [SDHC_SPI_R2_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa1b9e80034c783cc7ff43dc79ac5878faf74a4730cc3507a35179fe09da721a19)
- [SDHC_SPI_R2_CC_ERR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa1b9e80034c783cc7ff43dc79ac5878fad33e5499a36259f5b881ce524a1f4159)
- [SDHC_SPI_R2_ECC_FAIL](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa1b9e80034c783cc7ff43dc79ac5878fac853010c32e85d30f9f5936851ac4ddb)
- [SDHC_SPI_R2_WP_VIOLATION](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa1b9e80034c783cc7ff43dc79ac5878fa92bcd0ee78ddba8dc551c7917a37a792)
- [SDHC_SPI_R2_ERASE_PARAM](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa1b9e80034c783cc7ff43dc79ac5878fa47bb6389f20ceb840612266fedac0f7a)
- [SDHC_SPI_R2_OUT_OF_RANGE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#aa1b9e80034c783cc7ff43dc79ac5878faedbd66fd01bb87a4f55291c299589db7)
- [sd_rsp_type](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6)
- [SD_RSP_TYPE_NONE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6ad74407536823c1ea3afdf41d4b858b1c)
- [SD_RSP_TYPE_R1](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a92718e4bd4bccaa2fe4a8780228004d7)
- [SD_RSP_TYPE_R1b](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6ae64496ba1520651f8bac35af2531eaf8)
- [SD_RSP_TYPE_R2](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a96e26220a32f9b6e9e0bdd8c94d48eaf)
- [SD_RSP_TYPE_R3](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6af779f08bfb2fd73a717ea3789ccad509)
- [SD_RSP_TYPE_R4](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a34b03331e8f7a9ea6b67da6b68c7e0ed)
- [SD_RSP_TYPE_R5](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a91e216f8a1753b4719ee91819a926dde)
- [SD_RSP_TYPE_R5b](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a5dcd82e4fe5a34646a617a5031fdc638)
- [SD_RSP_TYPE_R6](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a3532733bc007df5009801bd6f09e45c9)
- [SD_RSP_TYPE_R7](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6aa5657942fb906d58ef2b7bed05137f23)
- [SD_SPI_RSP_TYPE_R1](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a32b2c65c90d0d5b8df5e4a82e9b95a6d)
- [SD_SPI_RSP_TYPE_R1b](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a22413680849a7645c7e8c585b5184203)
- [SD_SPI_RSP_TYPE_R2](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a855f8e4399cf3ce0c05c6089f3439ec2)
- [SD_SPI_RSP_TYPE_R3](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a7c44711a51e8175ebcaf4be24e2daec3)
- [SD_SPI_RSP_TYPE_R4](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a4c35ca3a8db652008204cf0cfc8e2339)
- [SD_SPI_RSP_TYPE_R5](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a0d82c7d93c187de5c40c0ff83fe8a478)
- [SD_SPI_RSP_TYPE_R7](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a1cfd2df5ec76eeb915fd3689408a65d6a78472618e8523bf73ca65aee6b0a8318)
- [sd_support_flag](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#afeec7c838fcf2d5c01cf653e305c749a)
- [SD_HIGH_CAPACITY_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#afeec7c838fcf2d5c01cf653e305c749aa104798e5266441d5a2f356f50b01cb35)
- [SD_4BITS_WIDTH](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#afeec7c838fcf2d5c01cf653e305c749aa2511277c6c4ebe38bc7179312292710b)
- [SD_SDHC_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#afeec7c838fcf2d5c01cf653e305c749aad9777c04b150a28916f894f54417286c)
- [SD_SDXC_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#afeec7c838fcf2d5c01cf653e305c749aa0558ef06a64c10456d220e66a5bc0f8b)
- [SD_1800MV_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#afeec7c838fcf2d5c01cf653e305c749aab78269976cbb673b4e00d6059ec38f80)
- [SD_3000MV_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#afeec7c838fcf2d5c01cf653e305c749aa5458d4988d7076d854bd695307771858)
- [SD_CMD23_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#afeec7c838fcf2d5c01cf653e305c749aac1f502da56d7d50b70898329da1ad21a)
- [SD_SPEED_CLASS_CONTROL_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#afeec7c838fcf2d5c01cf653e305c749aa02b4afca69adad8d7f220b8e4a76db45)
- [SD_MEM_PRESENT_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#afeec7c838fcf2d5c01cf653e305c749aa923c57b4134ad360ed3f6abbabfa87f1)
- [sd_ocr_flag](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61)
- [SD_OCR_PWR_BUSY_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61a5f680f7a518294d7a706b73bbecbdb73)
- [SD_OCR_HOST_CAP_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61ae344e23bbc73a6f2ed17d10618bf7a5a)
- [SD_OCR_CARD_CAP_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61a4cfc3b5856c525eda63b3a8b5fce5ae2)
- [SD_OCR_SWITCH_18_REQ_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61a69d58775148ae7daf65598d6cf90488d)
- [SD_OCR_SWITCH_18_ACCEPT_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61a541be7abf94851538a38f69c2ecb6b5f)
- [SD_OCR_VDD27_28FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61acd85dd4f874ed9088e6d7a2260d7bc50)
- [SD_OCR_VDD28_29FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61a76356316ead27df98dac310eed775707)
- [SD_OCR_VDD29_30FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61a624191bea93e1a350073fe2e5d5adaf1)
- [SD_OCR_VDD30_31FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61a98c205ed0f08df1a2f9e2801f02bbe7f)
- [SD_OCR_VDD31_32FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61a8ae4a104d50c0bdcae4722de0d5ee605)
- [SD_OCR_VDD32_33FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61a0c8a74f1b50f574b64184bf1cdc1458f)
- [SD_OCR_VDD33_34FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61aca49de7bd24df65fd6448a7e570b04a8)
- [SD_OCR_VDD34_35FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61ae5e13b78bf3fdece36190e48136927bf)
- [SD_OCR_VDD35_36FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a7b20cc85df2d9f5ce6c010907d7d5c61a83a9f603da11b75f200d3bb62528cda4)
- [mmc_ocr_flag](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a0769bcc2f15d43383f4e5a6c845c51aa)
- [MMC_OCR_VDD170_195FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a0769bcc2f15d43383f4e5a6c845c51aaa01aef2529fc39dc455c0fb8f2e9cc434)
- [MMC_OCR_VDD20_26FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a0769bcc2f15d43383f4e5a6c845c51aaa984a5e7f75a4418ca29141f5c6031d1e)
- [MMC_OCR_VDD27_36FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a0769bcc2f15d43383f4e5a6c845c51aaa239f02ae958dc3e25032825bb4c067e7)
- [MMC_OCR_SECTOR_MODE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a0769bcc2f15d43383f4e5a6c845c51aaa669934175190e5416a0d04c3c94acb4b)
- [MMC_OCR_PWR_BUSY_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a0769bcc2f15d43383f4e5a6c845c51aaa7127f5d946ea6bb4ec19b96033aafc4b)
- [sdio_ocr_flag](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6)
- [SDIO_OCR_IO_READY_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6adb3e45e84da812297359d6054baa69ba)
- [SDIO_OCR_IO_NUMBER](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a17007c3d37f047e6db56491a4230e8a8)
- [SDIO_OCR_MEM_PRESENT_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6ae923fdf459570657220ec225cbed7336)
- [SDIO_OCR_180_VOL_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a3f6ebe270ba873bab3407ee7d655b53d)
- [SDIO_OCR_VDD20_21FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6aa7a656a21495fbf64666b2b80236e4e4)
- [SDIO_OCR_VDD21_22FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6ad75d7d47a3d5fcc39a68c08546e9793b)
- [SDIO_OCR_VDD22_23FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a560f91eb371bfea5cf6c5c036cc9c096)
- [SDIO_OCR_VDD23_24FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a89c4025349ece0021cd627101f0efdd1)
- [SDIO_OCR_VDD24_25FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a6323aa0a8cbfb59f8209a37c8135079c)
- [SDIO_OCR_VDD25_26FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6ac0aa0897e1bbf45b0f5f4de73d733477)
- [SDIO_OCR_VDD26_27FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a4d32525a631342d78f73b6296e148666)
- [SDIO_OCR_VDD27_28FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a1f043936c614ac39b75f3835dc498b94)
- [SDIO_OCR_VDD28_29FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a1071312f18c64077e6964e421ef00ead)
- [SDIO_OCR_VDD29_30FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a246619651470476238452550068db8a0)
- [SDIO_OCR_VDD30_31FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a4cb1cc23687e7a1854d8af0c76876a20)
- [SDIO_OCR_VDD31_32FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a018af73c25e22c6e5313e5e3cff57e92)
- [SDIO_OCR_VDD32_33FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6ac5613e6858d2c9217165ab4cbb240012)
- [SDIO_OCR_VDD33_34FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a6673f837fa5a98b573886c5e6429c644)
- [SDIO_OCR_VDD34_35FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6a3d791855e6df402d5bfd92ce216a9a4b)
- [SDIO_OCR_VDD35_36FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a296cbe236e9e36dc79ca30eb54e6bcc6af0baaa7f71d144c7e5edade4b2445813)
- [sd_switch_arg](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a76f7ea4b395028ad5d8cc5eee32656e3)
- [SD_SWITCH_CHECK](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a76f7ea4b395028ad5d8cc5eee32656e3ae126f56fd639cbd686321a088d1e05e6)
- [SD_SWITCH_SET](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a76f7ea4b395028ad5d8cc5eee32656e3a72c39e3140ddd3990c3cbe7c6c867bb1)
- [sd_group_num](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a97f4810585247f5fed41110413e49853)
- [SD_GRP_TIMING_MODE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a97f4810585247f5fed41110413e49853a488b1aac4a0658c8b04b94b7556a2c5b)
- [SD_GRP_CMD_SYS_MODE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a97f4810585247f5fed41110413e49853a8c620d198b195d913ad3ff913434d764)
- [SD_GRP_DRIVER_STRENGTH_MODE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a97f4810585247f5fed41110413e49853a5e617dd9de3620481b89e517bd2c3a4b)
- [SD_GRP_CURRENT_LIMIT_MODE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a97f4810585247f5fed41110413e49853aa38ef885442708891b4ddc4a83c6ff66)
- [hs_max_data_rate](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a2093143614e52f69e173289391d7e91c)
- [HS_UNSUPPORTED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a2093143614e52f69e173289391d7e91cac3e8d67442f59c35b57d19d81b5d0d66)
- [HS_MAX_DTR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a2093143614e52f69e173289391d7e91ca10f805e3f66366474428718cb4569da0)
- [MHZ](../util_reference/P001_通用工具公共接口.md#gab7b18750ddf0850461f926ae151ca7fa)
- [uhs_max_data_rate](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a5466ef2e30578d03c61831aa09fd7b9a)
- [UHS_UNSUPPORTED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a5466ef2e30578d03c61831aa09fd7b9aaad6eabbee29e4ff07bdf93a9162aea6b)
- [UHS_SDR12_MAX_DTR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a5466ef2e30578d03c61831aa09fd7b9aad61b9d180a8de3c01be2e892c45504fb)
- [UHS_SDR25_MAX_DTR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a5466ef2e30578d03c61831aa09fd7b9aa5c5c100c048986ecfed728690d05ac55)
- [UHS_SDR50_MAX_DTR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a5466ef2e30578d03c61831aa09fd7b9aa72e9ad81edf54b7139a758d47fe54dd5)
- [UHS_SDR104_MAX_DTR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a5466ef2e30578d03c61831aa09fd7b9aa106c43d63c3b3c02d3835ccf542f3190)
- [UHS_DDR50_MAX_DTR](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a5466ef2e30578d03c61831aa09fd7b9aaff651e04c107beb23e0bd76d03029b26)
- [sd_bus_speed](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a6b42b86d8f2ba4f29787c7c6f3d97f36)
- [UHS_SDR12_BUS_SPEED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a30f38c9e54bed572ca315fdeb9122103)
- [DEFAULT_BUS_SPEED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a90413fe7dfd8568eeac79709ece7a549)
- [HIGH_SPEED_BUS_SPEED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a5593992de690adb1022b7926d1508ab3)
- [UHS_SDR25_BUS_SPEED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a6b42b86d8f2ba4f29787c7c6f3d97f36ae07a7ef1ffce64bab52c5f6612a96716)
- [UHS_SDR50_BUS_SPEED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a360c72912e023e5b21363f3701deaa50)
- [UHS_SDR104_BUS_SPEED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a6b42b86d8f2ba4f29787c7c6f3d97f36aef2ef100dab4187c8600ea721e8726dd)
- [UHS_DDR50_BUS_SPEED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a022acb9d379c5ecf9935150ec6f51ffc)
- [sd_timing_mode](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae82da8038d71cf36ce2237504b498930)
- [SD_TIMING_DEFAULT](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae82da8038d71cf36ce2237504b498930aa858c50e3f53d635857084ab5801a204)
- [SD_TIMING_SDR12](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae82da8038d71cf36ce2237504b498930aea7ebe2a07e1ed7727262d522815355b)
- [SD_TIMING_HIGH_SPEED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae82da8038d71cf36ce2237504b498930a7b6cef084cb3b83a91c05964951b05a6)
- [SD_TIMING_SDR25](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae82da8038d71cf36ce2237504b498930a433d8a39f77a612dd8104ca49c71a76f)
- [SD_TIMING_SDR50](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae82da8038d71cf36ce2237504b498930a787fb937df1275cb3d169e1dade2fb37)
- [SD_TIMING_SDR104](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae82da8038d71cf36ce2237504b498930aad980a4d433ffcf189a2e77b5d765861)
- [SD_TIMING_DDR50](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae82da8038d71cf36ce2237504b498930a88f373b6ac9335667eb8adab49a04e10)
- [sdhc_clock_speed](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a9660a61775e481ae4093e11ce9336539)
- [SDMMC_CLOCK_400KHZ](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a9660a61775e481ae4093e11ce9336539a16c56ed964cc6bbb5cc6f0cb857d4f10)
- [KHZ](../util_reference/P001_通用工具公共接口.md#gaee55275295c076c6d23c994777623253)
- [SD_CLOCK_25MHZ](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a9660a61775e481ae4093e11ce9336539ad5e9d57ee155e1b919f6cc213b05424f)
- [SD_CLOCK_50MHZ](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a9660a61775e481ae4093e11ce9336539a39e410f7f5c51753bf415f727551b9fb)
- [SD_CLOCK_100MHZ](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a9660a61775e481ae4093e11ce9336539a66ef44acd4ff3fafc2d49120df4b3c10)
- [SD_CLOCK_208MHZ](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a9660a61775e481ae4093e11ce9336539a9570bb04b0181b4fbdc96cace060d187)
- [MMC_CLOCK_26MHZ](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a9660a61775e481ae4093e11ce9336539ae9369c1cd7595ab83289fc356e9cc1b6)
- [MMC_CLOCK_52MHZ](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a9660a61775e481ae4093e11ce9336539a5c37aeeb3c68d7b3dbe8b9001a00507c)
- [MMC_CLOCK_DDR52](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a9660a61775e481ae4093e11ce9336539a66ecc8c1a73181d70e23424cf718728d)
- [MMC_CLOCK_HS200](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a9660a61775e481ae4093e11ce9336539a14dec2b314ed13974dbba31f33a5eab9)
- [MMC_CLOCK_HS400](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a9660a61775e481ae4093e11ce9336539a788a77f1e7a468c14ef57319ef8938f3)
- [sd_current_setting](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a5ac0e70389dc6ccec515530df4eab972)
- [SD_SET_CURRENT_200MA](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a5ac0e70389dc6ccec515530df4eab972a134ed84475be6f55a0f3d3ae9201cbe9)
- [SD_SET_CURRENT_400MA](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a5ac0e70389dc6ccec515530df4eab972ad548c59ebbb5045e437157cb9186de19)
- [SD_SET_CURRENT_600MA](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a5ac0e70389dc6ccec515530df4eab972a83f1d375e4c5aa645759cc4e4462f8e0)
- [SD_SET_CURRENT_800MA](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a5ac0e70389dc6ccec515530df4eab972af44faa0f33705ecbd37b5f3544105e34)
- [sd_current_limit](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a238de48c0cb55d173b6b874f4930c537)
- [SD_MAX_CURRENT_200MA](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a238de48c0cb55d173b6b874f4930c537a18b21e5e76bea0263f475ecc228c0301)
- [SD_MAX_CURRENT_400MA](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a238de48c0cb55d173b6b874f4930c537ae0605a0d9fc89e094a40b03e96c02339)
- [SD_MAX_CURRENT_600MA](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a238de48c0cb55d173b6b874f4930c537af82a5f23e51bf3ac3b7bec137269f540)
- [SD_MAX_CURRENT_800MA](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a238de48c0cb55d173b6b874f4930c537a2e3c01bc8d16641d7b500ce1244dbb03)
- [sd_driver_type](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a314c38b1b0603c003e67b5dec2228d4b)
- [SD_DRIVER_TYPE_B](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a314c38b1b0603c003e67b5dec2228d4ba32ad0894344bc4980f9206022ed0f877)
- [SD_DRIVER_TYPE_A](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a314c38b1b0603c003e67b5dec2228d4ba9eec5ff6f7d4c7512212cb48719dcabf)
- [SD_DRIVER_TYPE_C](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a314c38b1b0603c003e67b5dec2228d4ba0cd41f5198ce06ce5925b3f52d48b0a2)
- [SD_DRIVER_TYPE_D](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a314c38b1b0603c003e67b5dec2228d4ba435b458d33f1568cb76b77a3ea2e1eb8)
- [sd_driver_strength](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a66c69cd7d7818af86b6a91fad68334c2)
- [SD_DRV_STRENGTH_TYPEB](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a66c69cd7d7818af86b6a91fad68334c2a1b1e411f733ad6c1dc41896744441a48)
- [SD_DRV_STRENGTH_TYPEA](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a66c69cd7d7818af86b6a91fad68334c2ad870ea9b9fc07a4af81bce3c82330441)
- [SD_DRV_STRENGTH_TYPEC](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a66c69cd7d7818af86b6a91fad68334c2aa3e190aa6edb9f6eb7e29b78fc6f1a8a)
- [SD_DRV_STRENGTH_TYPED](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a66c69cd7d7818af86b6a91fad68334c2ad5753bf6fae3f43ef8ce7cb7eb169b61)
- [sd_switch_caps](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md)
- [hs_max_dtr](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md#a7465b3fe6bd1f317eeb3283a25da7278)
- [uhs_max_dtr](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md#ab09d80f61bc79857ee39604959c8a578)
- [bus_speed](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md#a29024de744d65fb3d8fe51c4d4424aee)
- [sd_drv_type](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md#a7262e4be5e3f59d047e569e1c24f04b3)
- [sd_current_limit](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md#a4b531af598bea14c90b8973daf1422dc)
- [sd_cid](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [manufacturer](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md#a7d97bc0f58c766abd2501d923e163d40)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [application](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md#a11ec5fa23ae13ee084c093b27c1d381a)
- [name](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md#a46f36abc3c2b1f3e9aa34c199d2bfcf3)
- [SD_PRODUCT_NAME_BYTES](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a947520a05fc99c25449fab98d0d02b1e)
- [version](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md#aba79f6a5bdf963772ac3c77ac209faf2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [ser_num](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md#ace04f0f28cb7e058e69fbbc643f66052)
- [date](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md#a50fbbc6844a1fde29a25a803ed9d0df7)
- [sd_csd](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md)
- [csd_structure](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a37b15b70967c9317183b3e5e7837b228)
- [read_time1](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a583c715045b5934ad94ab9cf61b25b06)
- [read_time2](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a96bc4672222dece77d29ffc9287c59ac)
- [xfer_rate](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#ae39272173a5253d0d11ef04a2e129db6)
- [cmd_class](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a8bfd2c42066d85058d01076fcaa7a32d)
- [read_blk_len](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a06f6aef4f4745a78bcf769df5415daa6)
- [flags](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#ae10b32787aeedd4789d657eb1ef492eb)
- [device_size](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#ad35b07abba80e9929c5eed40e37d25b3)
- [read_current_min](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#aa868cfc1db75eb2913d21bffeaf29fd9)
- [read_current_max](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#ad2f31731d7ec0b101d911fe20b5d94db)
- [write_current_min](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a0d1efea12c467eacd0d0f98a0bb0ac91)
- [write_current_max](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a53b364ce0db06b9217259afeb625da44)
- [dev_size_mul](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a9d5a952bc6c2a6967e9a88cd93f19e89)
- [erase_size](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#ab8d5ae38b19f7ea83b0856ad093c65cb)
- [write_prtect_size](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a029a893cdcd3765864c70476eb6dd64e)
- [write_speed_factor](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a9c362eff38daf7d00776416ed064de24)
- [write_blk_len](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#adff7d405662589ec44f4d0a6b3548760)
- [file_fmt](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#af93239157610a6eeea420c29432d5412)
- [mmc_csd_freq](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8)
- [MMC_MAXFREQ_100KHZ](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8a221dc45c7b73f6f96a63acbeb3e5e121)
- [MMC_MAXFREQ_1MHZ](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8a32c9f5017cd49c9ca4b352269de6eeff)
- [MMC_MAXFREQ_10MHZ](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8af63af4938d5aad64bac19fac42aedd10)
- [MMC_MAXFREQ_100MHZ](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8a13c703d344a1e03c1aa5881a77980085)
- [MMC_MAXFREQ_MULT_10](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8a74d01430b854f42ea84dba9d3ce45b16)
- [MMC_MAXFREQ_MULT_12](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8a4a3b8dc88c6349fb5f49ed3062a39a17)
- [MMC_MAXFREQ_MULT_13](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8a2c639715b63769e9a431a93e636f007e)
- [MMC_MAXFREQ_MULT_15](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8ac988a54239b7d9e182f1b2f480567e66)
- [MMC_MAXFREQ_MULT_20](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8ac8848c5cdf177737744da3283f7140d5)
- [MMC_MAXFREQ_MULT_26](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8ab1ff3da74a0dea49ffe7ac1d945ec4e6)
- [MMC_MAXFREQ_MULT_30](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8a69e1d369d668d63071410078a31099a0)
- [MMC_MAXFREQ_MULT_35](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8a63c0eee223946b1ae2b187bb585dfde4)
- [MMC_MAXFREQ_MULT_40](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8a572d53afafb39341e0cdb80d2d041d2c)
- [MMC_MAXFREQ_MULT_45](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8a5bd0506d7efbecdc42eb8fae1427dc37)
- [MMC_MAXFREQ_MULT_52](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8a988f18b9f418744721b0fc91f2432449)
- [MMC_MAXFREQ_MULT_55](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8abecfcd6d212185c74b57941c3fa58233)
- [MMC_MAXFREQ_MULT_60](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8adf578325509923b46e3ff4fbd74889ad)
- [MMC_MAXFREQ_MULT_70](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8aee24df1d628479fe2d920839a0bf5012)
- [MMC_MAXFREQ_MULT_80](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a313c45576db4ae219288fb4fbaad4bd8a24ea8c9db5531b5404bb667da26ac5d0)
- [mmc_timing_mode](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae1956c4b374e2c8b6a585596e93ac345)
- [MMC_LEGACY_TIMING](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae1956c4b374e2c8b6a585596e93ac345ae51a5474387816c03970aa0f8058b002)
- [MMC_HS_TIMING](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae1956c4b374e2c8b6a585596e93ac345a17160707005c580fbd52dbd6b99699dd)
- [MMC_HS200_TIMING](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae1956c4b374e2c8b6a585596e93ac345a39200c50c7e22c096db3ce1dd3fe78d5)
- [MMC_HS400_TIMING](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ae1956c4b374e2c8b6a585596e93ac345a4ea17060afbcd026387172c1af57bb43)
- [mmc_driver_strengths](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#af9783799f316cbaed12e18ce9944b09d)
- [mmc_driv_type0](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#af9783799f316cbaed12e18ce9944b09dabd4f3ffac3f52efe797ce3ee3c31a03f)
- [mmc_driv_type1](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#af9783799f316cbaed12e18ce9944b09da2cedd0b40bf81afb35792150b2d4964a)
- [mmc_driv_type2](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#af9783799f316cbaed12e18ce9944b09dafed77d2aed13d59fa6645cb06fc21c43)
- [mmc_driv_type3](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#af9783799f316cbaed12e18ce9944b09dacf4d28d56a6c4925944ffc99072d46e9)
- [mmc_driv_type4](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#af9783799f316cbaed12e18ce9944b09daf5448a25c8b5a8411f059469112ef2be)
- [mmc_device_type](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md)
- [MMC_HS400_DDR_1200MV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#ab19f29678c18ba8740758ca136fd7744)
- [MMC_HS400_DDR_1800MV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#a24bee6ea4bd6d209b53b05fb9e040b38)
- [MMC_HS200_SDR_1200MV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#aaa7bb99717ecde9e6cf265a6c5bb33f0)
- [MMC_HS200_SDR_1800MV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#a7027fdec8b21be17a2ba97b2b19a13da)
- [MMC_HS_DDR_1200MV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#a65bc5ecdb11da48c08a06d4c5c386590)
- [MMC_HS_DDR_1800MV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#a5d338770aca6d893e094f57211b0339e)
- [MMC_HS_52_DV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#a3f4bbe853ef59313a84acb5737cafdf4)
- [MMC_HS_26_DV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#a12bb36ef4914b9182f08c4310c85d70d)
- [mmc_ext_csd_rev](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac86d8a44f37c771cb666f69a516dff81)
- [MMC_5_1](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac86d8a44f37c771cb666f69a516dff81ad49da8223b68d35a4d95d6b48bb8a3f7)
- [MMC_5_0](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac86d8a44f37c771cb666f69a516dff81a87a4c0efb7e10cccce939af5f60343ad)
- [MMC_4_5](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac86d8a44f37c771cb666f69a516dff81aa0d4721b24d0cd71d6a8fbfc666a6e7c)
- [MMC_4_4](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac86d8a44f37c771cb666f69a516dff81a43b7acda3747eb2233c2f2a433ff71c7)
- [MMC_4_3](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac86d8a44f37c771cb666f69a516dff81a0f4fc7047a7c813b9ada618ed05e09a4)
- [MMC_4_2](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac86d8a44f37c771cb666f69a516dff81a9a960567b8ecbd6feff7e6337fc98567)
- [MMC_4_1](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac86d8a44f37c771cb666f69a516dff81ab84ae4edfcca8ccae2a0df0643d04ca2)
- [MMC_4_0](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac86d8a44f37c771cb666f69a516dff81aba4f3f30eaa7d3368743f78f3c355269)
- [mmc_ext_csd](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md)
- [sec_count](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a44aa7d6d1282a00a1875e92fb5b3c4b8)
- [bus_width](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a63545477058cce0c5727637bcbb06a47)
- [enhanced_strobe_support](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#aa5089c06fcc9b6b60749388b594a12f5)
- [hs_timing](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a25fe8f962635be3d40b449203e7d34a2)
- [device_type](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a4c26010052a69e060742e0a05b6ad98b)
- [rev](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a3ee512cb3c0e3698d940c04eed3aa665)
- [power_class](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a286b2783ac15dbec6fa3953f0cd69af4)
- [mmc_driver_strengths](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a29a7f7502e6e6d93e76392b8ac45356f)
- [pwr_class_200MHZ_VCCQ195](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#acab002b3a28a3dc9bf58187e9e19a9fe)
- [pwr_class_HS400](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a3a38f805cac18f3429f57edc7cbf2134)
- [cache_size](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a3aafc3e2b5b59cb79535411178a35efe)
- [sd_csd_flag](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a98c4f218acfa21e124aa22e9fe209437)
- [SD_CSD_READ_BLK_PARTIAL_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a98c4f218acfa21e124aa22e9fe209437ac353a0c3c1ac62920efdc42879a81cff)
- [SD_CSD_WRITE_BLK_MISALIGN_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a98c4f218acfa21e124aa22e9fe209437a16d3fd179853f1f15b980d2b82b572be)
- [SD_CSD_READ_BLK_MISALIGN_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a98c4f218acfa21e124aa22e9fe209437aca7d98319db6a23b30625828807e2143)
- [SD_CSD_DSR_IMPLEMENTED_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a98c4f218acfa21e124aa22e9fe209437a1258364107909d0c4f8e9b7dba59300c)
- [SD_CSD_ERASE_BLK_EN_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a98c4f218acfa21e124aa22e9fe209437a0d907c1a9e69435433c5bf19bfacbd73)
- [SD_CSD_WRITE_PROTECT_GRP_EN_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a98c4f218acfa21e124aa22e9fe209437af85839612e4fcc94eb2bd0986bd1740c)
- [SD_CSD_WRITE_BLK_PARTIAL_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a98c4f218acfa21e124aa22e9fe209437aa8b8f850196e47799cb9b2cd06650520)
- [SD_CSD_FILE_FMT_GRP_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a98c4f218acfa21e124aa22e9fe209437a2e75506280c1b4d5866f4dd8f2518be8)
- [SD_CSD_COPY_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a98c4f218acfa21e124aa22e9fe209437a988758fe0720e6fc33564076e3bc51bf)
- [SD_CSD_PERMANENT_WRITE_PROTECT_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a98c4f218acfa21e124aa22e9fe209437a7496edd5c7ec694d2d175bf751de1458)
- [SD_CSD_TMP_WRITE_PROTECT_FLAG](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a98c4f218acfa21e124aa22e9fe209437aa0c70fee97e29875394efc2a4c2fa274)
- [sd_scr](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md)
- [scr_structure](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#a3fc37c731dfb5c5596b6389152479c07)
- [sd_spec](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#ae6201af1083efa828cced000874bf197)
- [flags](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#abda65da85e20979a1fc71f2aea1f947b)
- [sd_sec](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#a9f8254b5fe6911156bae727e29262f5a)
- [sd_width](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#a40d30ccc4daf2c32f2ac162b402f3887)
- [sd_ext_sec](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#a15f60bc2115b943ce938f3a96dd8e547)
- [cmd_support](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#a9016ca73a668499289c52355ebb83cb1)
- [rsvd](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#aba20efcf752335f1a86d0a86607d92d0)
- [sd_scr_flag](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a476ec98763d90a5cba336cbf22d6d553)
- [SD_SCR_DATA_STATUS_AFTER_ERASE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a476ec98763d90a5cba336cbf22d6d553a759c63670d0dd41590fdb940a48ac4dd)
- [SD_SCR_SPEC3](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a476ec98763d90a5cba336cbf22d6d553a59fb3a34a7dba6ed1c86bca21cf97871)
- [sd_spec_version](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#abf77ec1ad65cc9c99dc930ed7a96301a)
- [SD_SPEC_VER1_0](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#abf77ec1ad65cc9c99dc930ed7a96301aa39605b86ccfad6196721ddfbb84b33d6)
- [SD_SPEC_VER1_1](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#abf77ec1ad65cc9c99dc930ed7a96301aac09ddfacee85353e243d6a8cfe7eeba8)
- [SD_SPEC_VER2_0](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#abf77ec1ad65cc9c99dc930ed7a96301aa3525ee751a482ae1cd816e2674ac3160)
- [SD_SPEC_VER3_0](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#abf77ec1ad65cc9c99dc930ed7a96301aa9e3d0d084a7d8ad1b9d08e6b699084e6)
- [sdio_func_num](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6)
- [SDIO_FUNC_NUM_0](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6ad7a10f97094ddb96f26ab44fc34de12a)
- [SDIO_FUNC_NUM_1](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6a900536b934da03f8e8590de3e3d56296)
- [SDIO_FUNC_NUM_2](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6ac2cc5967daee0a3e9ef61c9c486b3a6c)
- [SDIO_FUNC_NUM_3](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6adef5748e2622dab22da33504bbafa149)
- [SDIO_FUNC_NUM_4](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6a9b69d64108c6564bc313e4fb2b53f61c)
- [SDIO_FUNC_NUM_5](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6ac62397290371f5fb3fdf8d4b52fb3575)
- [SDIO_FUNC_NUM_6](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6a2a9baef178307d6e6006ea88b4da383c)
- [SDIO_FUNC_NUM_7](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6a617d1991d70033df3b39eef7ccb98b48)
- [SDIO_FUNC_MEMORY](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6a075731d15b2f4b7c7448d6d4ee059880)
- [sdio_io_dir](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a250ae2ce54e941895a720b565632350e)
- [SDIO_IO_READ](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a250ae2ce54e941895a720b565632350eac1212149d096232e75d1d090abb4974c)
- [SDIO_IO_WRITE](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a250ae2ce54e941895a720b565632350eabd26fc6f76267231c78eae8be9ebb885)
- [sdio_cccr_flags](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac12657ae7d3b8abc562d4d7929a86b65)
- [SDIO_SUPPORT_HS](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac12657ae7d3b8abc562d4d7929a86b65aa23a07a4fe6f6dd8292215221d97d5e2)
- [SDIO_SUPPORT_SDR50](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac12657ae7d3b8abc562d4d7929a86b65acc46ce7f993b3eb81c6a2a2daad84c34)
- [SDIO_SUPPORT_SDR104](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac12657ae7d3b8abc562d4d7929a86b65a9b12d90cd1590f68fc1031449c4560ec)
- [SDIO_SUPPORT_DDR50](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac12657ae7d3b8abc562d4d7929a86b65a6d2084ba4c729c2cb019582b975f652f)
- [SDIO_SUPPORT_4BIT_LS_BUS](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac12657ae7d3b8abc562d4d7929a86b65a6cd553669599181b3677cea94687f025)
- [SDIO_SUPPORT_MULTIBLOCK](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#ac12657ae7d3b8abc562d4d7929a86b65a364c7067e73960bae74ed80320adb223)
- [sdio_cis](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md)
- [manf_id](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md#a04c8a774c65f683185e5a32e15afb67c)
- [manf_code](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md#ad52e1df89176f728734ce0e69fb2b4c8)
- [func_id](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md#ad38be5cade97ac92de62094d8e3b8549)
- [max_blk_size](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md#a1b340e20630994f91314be17dd9055ca)
- [max_speed](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md#a56d3ee1d6b8d0d87e0efdbda15b7076d)
- [rdy_timeout](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md#a86a01890f31788ae5465b1c8dc47bcf2)
- [mmc_device_type::MMC_HS_26_DV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#a12bb36ef4914b9182f08c4310c85d70d)
- [mmc_device_type::MMC_HS400_DDR_1800MV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#a24bee6ea4bd6d209b53b05fb9e040b38)
- [mmc_device_type::MMC_HS_52_DV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#a3f4bbe853ef59313a84acb5737cafdf4)
- [mmc_device_type::MMC_HS_DDR_1800MV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#a5d338770aca6d893e094f57211b0339e)
- [mmc_device_type::MMC_HS_DDR_1200MV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#a65bc5ecdb11da48c08a06d4c5c386590)
- [mmc_device_type::MMC_HS200_SDR_1800MV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#a7027fdec8b21be17a2ba97b2b19a13da)
- [mmc_device_type::MMC_HS200_SDR_1200MV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#aaa7bb99717ecde9e6cf265a6c5bb33f0)
- [mmc_device_type::MMC_HS400_DDR_1200MV](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md#ab19f29678c18ba8740758ca136fd7744)
- [mmc_ext_csd::hs_timing](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a25fe8f962635be3d40b449203e7d34a2)
- [mmc_ext_csd::power_class](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a286b2783ac15dbec6fa3953f0cd69af4)
- [mmc_ext_csd::mmc_driver_strengths](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a29a7f7502e6e6d93e76392b8ac45356f)
- [mmc_ext_csd::pwr_class_HS400](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a3a38f805cac18f3429f57edc7cbf2134)
- [mmc_ext_csd::cache_size](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a3aafc3e2b5b59cb79535411178a35efe)
- [mmc_ext_csd::rev](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a3ee512cb3c0e3698d940c04eed3aa665)
- [mmc_ext_csd::sec_count](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a44aa7d6d1282a00a1875e92fb5b3c4b8)
- [mmc_ext_csd::device_type](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a4c26010052a69e060742e0a05b6ad98b)
- [mmc_ext_csd::bus_width](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#a63545477058cce0c5727637bcbb06a47)
- [mmc_ext_csd::enhanced_strobe_support](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#aa5089c06fcc9b6b60749388b594a12f5)
- [mmc_ext_csd::pwr_class_200MHZ_VCCQ195](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md#acab002b3a28a3dc9bf58187e9e19a9fe)
- [sd_cid::application](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md#a11ec5fa23ae13ee084c093b27c1d381a)
- [sd_cid::name](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md#a46f36abc3c2b1f3e9aa34c199d2bfcf3)
- [sd_cid::date](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md#a50fbbc6844a1fde29a25a803ed9d0df7)
- [sd_cid::manufacturer](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md#a7d97bc0f58c766abd2501d923e163d40)
- [sd_cid::version](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md#aba79f6a5bdf963772ac3c77ac209faf2)
- [sd_cid::ser_num](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md#ace04f0f28cb7e058e69fbbc643f66052)
- [sd_csd::write_prtect_size](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a029a893cdcd3765864c70476eb6dd64e)
- [sd_csd::read_blk_len](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a06f6aef4f4745a78bcf769df5415daa6)
- [sd_csd::write_current_min](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a0d1efea12c467eacd0d0f98a0bb0ac91)
- [sd_csd::csd_structure](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a37b15b70967c9317183b3e5e7837b228)
- [sd_csd::write_current_max](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a53b364ce0db06b9217259afeb625da44)
- [sd_csd::read_time1](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a583c715045b5934ad94ab9cf61b25b06)
- [sd_csd::cmd_class](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a8bfd2c42066d85058d01076fcaa7a32d)
- [sd_csd::read_time2](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a96bc4672222dece77d29ffc9287c59ac)
- [sd_csd::write_speed_factor](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a9c362eff38daf7d00776416ed064de24)
- [sd_csd::dev_size_mul](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#a9d5a952bc6c2a6967e9a88cd93f19e89)
- [sd_csd::read_current_min](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#aa868cfc1db75eb2913d21bffeaf29fd9)
- [sd_csd::erase_size](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#ab8d5ae38b19f7ea83b0856ad093c65cb)
- [sd_csd::read_current_max](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#ad2f31731d7ec0b101d911fe20b5d94db)
- [sd_csd::device_size](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#ad35b07abba80e9929c5eed40e37d25b3)
- [sd_csd::write_blk_len](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#adff7d405662589ec44f4d0a6b3548760)
- [sd_csd::flags](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#ae10b32787aeedd4789d657eb1ef492eb)
- [sd_csd::xfer_rate](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#ae39272173a5253d0d11ef04a2e129db6)
- [sd_csd::file_fmt](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md#af93239157610a6eeea420c29432d5412)
- [sd_scr::sd_ext_sec](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#a15f60bc2115b943ce938f3a96dd8e547)
- [sd_scr::scr_structure](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#a3fc37c731dfb5c5596b6389152479c07)
- [sd_scr::sd_width](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#a40d30ccc4daf2c32f2ac162b402f3887)
- [sd_scr::cmd_support](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#a9016ca73a668499289c52355ebb83cb1)
- [sd_scr::sd_sec](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#a9f8254b5fe6911156bae727e29262f5a)
- [sd_scr::rsvd](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#aba20efcf752335f1a86d0a86607d92d0)
- [sd_scr::flags](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#abda65da85e20979a1fc71f2aea1f947b)
- [sd_scr::sd_spec](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md#ae6201af1083efa828cced000874bf197)
- [sd_switch_caps::bus_speed](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md#a29024de744d65fb3d8fe51c4d4424aee)
- [sd_switch_caps::sd_current_limit](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md#a4b531af598bea14c90b8973daf1422dc)
- [sd_switch_caps::sd_drv_type](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md#a7262e4be5e3f59d047e569e1c24f04b3)
- [sd_switch_caps::hs_max_dtr](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md#a7465b3fe6bd1f317eeb3283a25da7278)
- [sd_switch_caps::uhs_max_dtr](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md#ab09d80f61bc79857ee39604959c8a578)
- [sdio_cis::manf_id](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md#a04c8a774c65f683185e5a32e15afb67c)
- [sdio_cis::max_blk_size](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md#a1b340e20630994f91314be17dd9055ca)
- [sdio_cis::max_speed](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md#a56d3ee1d6b8d0d87e0efdbda15b7076d)
- [sdio_cis::rdy_timeout](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md#a86a01890f31788ae5465b1c8dc47bcf2)
- [sdio_cis::func_id](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md#ad38be5cade97ac92de62094d8e3b8549)
- [sdio_cis::manf_code](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md#ad52e1df89176f728734ce0e69fb2b4c8)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P014_zephyr__drivers__memc.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__drivers__mspi__mspi_cadence.h_头文件源码.md)
