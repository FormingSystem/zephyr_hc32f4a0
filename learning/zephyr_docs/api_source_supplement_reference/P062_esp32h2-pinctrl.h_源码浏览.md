---
id: learning.zephyr-docs.api-source-supplement-reference.page-62
title: esp32h2-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32h2-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_esp32h2-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp32h2-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp32h2-pinctrl_8h.html)。

## 62.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00025"></a>
<a id="l00053"></a>
<a id="l00055"></a>
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
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00085"></a>
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
<a id="l00105"></a>
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
<a id="l00130"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
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
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00180"></a>
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
<a id="l00205"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
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
<a id="l00230"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
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
<a id="l00255"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
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
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
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
<a id="l00330"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
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
<a id="l00355"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00380"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
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
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00405"></a>
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
<a id="l00430"></a>
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
<a id="l00455"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
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
<a id="l00480"></a>
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
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00505"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00530"></a>
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
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00555"></a>
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
<a id="l00578"></a>
<a id="l00580"></a>
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
<a id="l00605"></a>
<a id="l00610"></a>
<a id="l00611"></a>
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
<a id="l00630"></a>
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
<a id="l00655"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00680"></a>
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
<a id="l00705"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00730"></a>
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
<a id="l00755"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00780"></a>
<a id="l00785"></a>
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
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00805"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00814"></a>
<a id="l00815"></a>
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
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00830"></a>
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
<a id="l00855"></a>
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
<a id="l00880"></a>
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
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00905"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="l00922"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00930"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="l00938"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00948"></a>
<a id="l00949"></a>
<a id="l00950"></a>
<a id="l00951"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00955"></a>
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
<a id="l00980"></a>
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
<a id="l00999"></a>
<a id="l01000"></a>
<a id="l01001"></a>
<a id="l01002"></a>
<a id="l01003"></a>
<a id="l01005"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01012"></a>
<a id="l01013"></a>
<a id="l01014"></a>
<a id="l01015"></a>
<a id="l01016"></a>
<a id="l01017"></a>
<a id="l01018"></a>
<a id="l01019"></a>
<a id="l01020"></a>
<a id="l01021"></a>
<a id="l01022"></a>
<a id="l01023"></a>
<a id="l01024"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01028"></a>
<a id="l01030"></a>
<a id="l01035"></a>
<a id="l01036"></a>
<a id="l01037"></a>
<a id="l01038"></a>
<a id="l01039"></a>
<a id="l01040"></a>
<a id="l01041"></a>
<a id="l01042"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01055"></a>
<a id="l01060"></a>
<a id="l01061"></a>
<a id="l01062"></a>
<a id="l01063"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="l01066"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="l01073"></a>
<a id="l01074"></a>
<a id="l01075"></a>
<a id="l01076"></a>
<a id="l01077"></a>
<a id="l01078"></a>
<a id="l01080"></a>
<a id="l01085"></a>
<a id="l01086"></a>
<a id="l01087"></a>
<a id="l01088"></a>
<a id="l01089"></a>
<a id="l01090"></a>
<a id="l01091"></a>
<a id="l01092"></a>
<a id="l01093"></a>
<a id="l01094"></a>
<a id="l01095"></a>
<a id="l01096"></a>
<a id="l01097"></a>
<a id="l01098"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01101"></a>
<a id="l01102"></a>
<a id="l01103"></a>
<a id="l01105"></a>
<a id="l01110"></a>
<a id="l01111"></a>
<a id="l01112"></a>
<a id="l01113"></a>
<a id="l01114"></a>
<a id="l01115"></a>
<a id="l01116"></a>
<a id="l01117"></a>
<a id="l01118"></a>
<a id="l01119"></a>
<a id="l01120"></a>
<a id="l01121"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="l01125"></a>
<a id="l01126"></a>
<a id="l01127"></a>
<a id="l01128"></a>
<a id="l01130"></a>
<a id="l01135"></a>
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
<a id="l01146"></a>
<a id="l01147"></a>
<a id="l01148"></a>
<a id="l01149"></a>
<a id="l01150"></a>
<a id="l01151"></a>
<a id="l01152"></a>
<a id="l01153"></a>
<a id="l01155"></a>
<a id="l01160"></a>
<a id="l01161"></a>
<a id="l01162"></a>
<a id="l01163"></a>
<a id="l01164"></a>
<a id="l01165"></a>
<a id="l01166"></a>
<a id="l01167"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="l01170"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01173"></a>
<a id="l01174"></a>
<a id="l01175"></a>
<a id="l01176"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="l01180"></a>
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
<a id="l01195"></a>
<a id="l01196"></a>
<a id="l01197"></a>
<a id="l01198"></a>
<a id="l01199"></a>
<a id="l01200"></a>
<a id="l01201"></a>
<a id="l01202"></a>
<a id="l01203"></a>
<a id="l01205"></a>
<a id="l01210"></a>
<a id="l01211"></a>
<a id="l01212"></a>
<a id="l01213"></a>
<a id="l01214"></a>
<a id="l01215"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01220"></a>
<a id="l01221"></a>
<a id="l01222"></a>
<a id="l01223"></a>
<a id="l01224"></a>
<a id="l01225"></a>
<a id="l01226"></a>
<a id="l01227"></a>
<a id="l01228"></a>
<a id="l01230"></a>
<a id="l01235"></a>
<a id="l01236"></a>
<a id="l01237"></a>
<a id="l01238"></a>
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
<a id="l01255"></a>
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
<a id="l01271"></a>
<a id="l01272"></a>
<a id="l01273"></a>
<a id="l01274"></a>
<a id="l01275"></a>
<a id="l01276"></a>
<a id="l01277"></a>
<a id="l01278"></a>
<a id="l01280"></a>
<a id="l01285"></a>
<a id="l01286"></a>
<a id="l01287"></a>
<a id="l01288"></a>
<a id="l01289"></a>
<a id="l01290"></a>
<a id="l01291"></a>
<a id="l01292"></a>
<a id="l01293"></a>
<a id="l01294"></a>
<a id="l01295"></a>
<a id="l01296"></a>
<a id="l01297"></a>
<a id="l01298"></a>
<a id="l01299"></a>
<a id="l01300"></a>
<a id="l01301"></a>
<a id="l01302"></a>
<a id="l01303"></a>
<a id="l01305"></a>
<a id="l01310"></a>
<a id="l01311"></a>
<a id="l01312"></a>
<a id="l01313"></a>
<a id="l01314"></a>
<a id="l01315"></a>
<a id="l01316"></a>
<a id="l01317"></a>
<a id="l01318"></a>
<a id="l01319"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="l01322"></a>
<a id="l01323"></a>
<a id="l01324"></a>
<a id="l01325"></a>
<a id="l01326"></a>
<a id="l01327"></a>
<a id="l01328"></a>
<a id="l01330"></a>
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
<a id="l01348"></a>
<a id="l01349"></a>
<a id="l01350"></a>
<a id="l01351"></a>
<a id="l01352"></a>
<a id="l01353"></a>
<a id="l01355"></a>
<a id="l01360"></a>
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
<a id="l01372"></a>
<a id="l01373"></a>
<a id="l01374"></a>
<a id="l01375"></a>
<a id="l01376"></a>
<a id="l01377"></a>
<a id="l01378"></a>
<a id="l01380"></a>
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
<a id="l01397"></a>
<a id="l01398"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01402"></a>
<a id="l01403"></a>
<a id="l01405"></a>
<a id="l01410"></a>
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
<a id="l01423"></a>
<a id="l01424"></a>
<a id="l01425"></a>
<a id="l01426"></a>
<a id="l01427"></a>
<a id="l01428"></a>
<a id="l01430"></a>
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
<a id="l01447"></a>
<a id="l01448"></a>
<a id="l01449"></a>
<a id="l01450"></a>
<a id="l01451"></a>
<a id="l01452"></a>
<a id="l01453"></a>
<a id="l01455"></a>
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
<a id="l01480"></a>
<a id="l01485"></a>
<a id="l01486"></a>
<a id="l01487"></a>
<a id="l01488"></a>
<a id="l01489"></a>
<a id="l01490"></a>
<a id="l01491"></a>
<a id="l01492"></a>
<a id="l01493"></a>
<a id="l01494"></a>
<a id="l01495"></a>
<a id="l01496"></a>
<a id="l01497"></a>
<a id="l01498"></a>
<a id="l01499"></a>
<a id="l01500"></a>
<a id="l01501"></a>
<a id="l01502"></a>
<a id="l01503"></a>
<a id="l01505"></a>
<a id="l01510"></a>
<a id="l01511"></a>
<a id="l01512"></a>
<a id="l01513"></a>
<a id="l01514"></a>
<a id="l01515"></a>
<a id="l01516"></a>
<a id="l01517"></a>
<a id="l01518"></a>
<a id="l01519"></a>
<a id="l01520"></a>
<a id="l01521"></a>
<a id="l01522"></a>
<a id="l01523"></a>
<a id="l01524"></a>
<a id="l01525"></a>
<a id="l01526"></a>
<a id="l01527"></a>
<a id="l01528"></a>
<a id="l01530"></a>
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
<a id="l01555"></a>
<a id="l01560"></a>
<a id="l01561"></a>
<a id="l01562"></a>
<a id="l01563"></a>
<a id="l01564"></a>
<a id="l01565"></a>
<a id="l01566"></a>
<a id="l01567"></a>
<a id="l01568"></a>
<a id="l01569"></a>
<a id="l01570"></a>
<a id="l01571"></a>
<a id="l01572"></a>
<a id="l01573"></a>
<a id="l01574"></a>
<a id="l01575"></a>
<a id="l01576"></a>
<a id="l01577"></a>
<a id="l01578"></a>
<a id="l01580"></a>
<a id="l01585"></a>
<a id="l01586"></a>
<a id="l01587"></a>
<a id="l01588"></a>
<a id="l01589"></a>
<a id="l01590"></a>
<a id="l01591"></a>
<a id="l01592"></a>
<a id="l01593"></a>
<a id="l01594"></a>
<a id="l01595"></a>
<a id="l01596"></a>
<a id="l01597"></a>
<a id="l01598"></a>
<a id="l01599"></a>
<a id="l01600"></a>
<a id="l01601"></a>
<a id="l01602"></a>
<a id="l01603"></a>
<a id="l01605"></a>
<a id="l01610"></a>
<a id="l01611"></a>
<a id="l01612"></a>
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
<a id="l01627"></a>
<a id="l01628"></a>
<a id="l01630"></a>
<a id="l01635"></a>
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
<a id="l01650"></a>
<a id="l01651"></a>
<a id="l01652"></a>
<a id="l01653"></a>
<a id="l01655"></a>
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
<a id="l01680"></a>
<a id="l01685"></a>
<a id="l01686"></a>
<a id="l01687"></a>
<a id="l01688"></a>
<a id="l01689"></a>
<a id="l01690"></a>
<a id="l01691"></a>
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
<a id="l01705"></a>
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
<a id="l01730"></a>
<a id="l01735"></a>
<a id="l01736"></a>
<a id="l01737"></a>
<a id="l01738"></a>
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
<a id="l01751"></a>
<a id="l01752"></a>
<a id="l01753"></a>
<a id="l01755"></a>
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
<a id="l01780"></a>
<a id="l01785"></a>
<a id="l01786"></a>
<a id="l01787"></a>
<a id="l01788"></a>
<a id="l01789"></a>
<a id="l01790"></a>
<a id="l01791"></a>
<a id="l01792"></a>
<a id="l01793"></a>
<a id="l01794"></a>
<a id="l01795"></a>
<a id="l01796"></a>
<a id="l01797"></a>
<a id="l01798"></a>
<a id="l01799"></a>
<a id="l01800"></a>
<a id="l01801"></a>
<a id="l01802"></a>
<a id="l01803"></a>
<a id="l01805"></a>
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
<a id="l01820"></a>
<a id="l01821"></a>
<a id="l01822"></a>
<a id="l01823"></a>
<a id="l01824"></a>
<a id="l01825"></a>
<a id="l01826"></a>
<a id="l01827"></a>
<a id="l01828"></a>
<a id="l01830"></a>
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
<a id="l01855"></a>
<a id="l01860"></a>
<a id="l01861"></a>
<a id="l01862"></a>
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
<a id="l01880"></a>
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
<a id="l01905"></a>
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
<a id="l01935"></a>
<a id="l01936"></a>
<a id="l01937"></a>
<a id="l01938"></a>
<a id="l01939"></a>
<a id="l01940"></a>
<a id="l01941"></a>
<a id="l01942"></a>
<a id="l01943"></a>
<a id="l01944"></a>
<a id="l01945"></a>
<a id="l01946"></a>
<a id="l01947"></a>
<a id="l01948"></a>
<a id="l01949"></a>
<a id="l01950"></a>
<a id="l01951"></a>
<a id="l01952"></a>
<a id="l01953"></a>
<a id="l01955"></a>
<a id="l01960"></a>
<a id="l01961"></a>
<a id="l01962"></a>
<a id="l01963"></a>
<a id="l01964"></a>
<a id="l01965"></a>
<a id="l01966"></a>
<a id="l01967"></a>
<a id="l01968"></a>
<a id="l01969"></a>
<a id="l01970"></a>
<a id="l01971"></a>
<a id="l01972"></a>
<a id="l01973"></a>
<a id="l01974"></a>
<a id="l01975"></a>
<a id="l01976"></a>
<a id="l01977"></a>
<a id="l01978"></a>
<a id="l01980"></a>
<a id="l01985"></a>
<a id="l01986"></a>
<a id="l01987"></a>
<a id="l01988"></a>
<a id="l01989"></a>
<a id="l01990"></a>
<a id="l01991"></a>
<a id="l01992"></a>
<a id="l01993"></a>
<a id="l01994"></a>
<a id="l01995"></a>
<a id="l01996"></a>
<a id="l01997"></a>
<a id="l01998"></a>
<a id="l01999"></a>
<a id="l02000"></a>
<a id="l02001"></a>
<a id="l02002"></a>
<a id="l02003"></a>
<a id="l02005"></a>
<a id="l02010"></a>
<a id="l02011"></a>
<a id="l02012"></a>
<a id="l02013"></a>
<a id="l02014"></a>
<a id="l02015"></a>
<a id="l02016"></a>
<a id="l02017"></a>
<a id="l02018"></a>
<a id="l02019"></a>
<a id="l02020"></a>
<a id="l02021"></a>
<a id="l02022"></a>
<a id="l02023"></a>
<a id="l02024"></a>
<a id="l02025"></a>
<a id="l02026"></a>
<a id="l02027"></a>
<a id="l02028"></a>
<a id="l02030"></a>
<a id="l02035"></a>
<a id="l02036"></a>
<a id="l02037"></a>
<a id="l02038"></a>
<a id="l02039"></a>
<a id="l02040"></a>
<a id="l02041"></a>
<a id="l02042"></a>
<a id="l02043"></a>
<a id="l02044"></a>
<a id="l02045"></a>
<a id="l02046"></a>
<a id="l02047"></a>
<a id="l02048"></a>
<a id="l02049"></a>
<a id="l02050"></a>
<a id="l02051"></a>
<a id="l02052"></a>
<a id="l02053"></a>
<a id="l02055"></a>
<a id="l02060"></a>
<a id="l02061"></a>
<a id="l02062"></a>
<a id="l02063"></a>
<a id="l02064"></a>
<a id="l02065"></a>
<a id="l02066"></a>
<a id="l02067"></a>
<a id="l02068"></a>
<a id="l02069"></a>
<a id="l02070"></a>
<a id="l02071"></a>
<a id="l02072"></a>
<a id="l02073"></a>
<a id="l02074"></a>
<a id="l02075"></a>
<a id="l02076"></a>
<a id="l02077"></a>
<a id="l02078"></a>
<a id="l02080"></a>
<a id="l02082"></a>
<a id="l02084"></a>
<a id="l02085"></a>
<a id="aesp-pinctrl-common_8h_html"></a>
<a id="aesp32h2-gpio-sigmap_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * NOTE: Autogenerated file using esp_genpinctrl.py
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32H2_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32H2_PINCTRL_H_

#include "esp-pinctrl-common.h"
#include "esp32h2-gpio-sigmap.h"




#define I2C0_SCL_GPIO0 ESP32_PINMUX(0, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO1 ESP32_PINMUX(1, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO2 ESP32_PINMUX(2, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO3 ESP32_PINMUX(3, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO4 ESP32_PINMUX(4, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO5 ESP32_PINMUX(5, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO8 ESP32_PINMUX(8, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO9 ESP32_PINMUX(9, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO10 ESP32_PINMUX(10, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO11 ESP32_PINMUX(11, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO12 ESP32_PINMUX(12, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO13 ESP32_PINMUX(13, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO14 ESP32_PINMUX(14, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO22 ESP32_PINMUX(22, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO23 ESP32_PINMUX(23, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO24 ESP32_PINMUX(24, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO25 ESP32_PINMUX(25, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO26 ESP32_PINMUX(26, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)
#define I2C0_SCL_GPIO27 ESP32_PINMUX(27, ESP_I2CEXT0_SCL_IN, ESP_I2CEXT0_SCL_OUT)

#define I2C0_SDA_GPIO0 ESP32_PINMUX(0, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO1 ESP32_PINMUX(1, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO2 ESP32_PINMUX(2, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO3 ESP32_PINMUX(3, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO4 ESP32_PINMUX(4, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO5 ESP32_PINMUX(5, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO8 ESP32_PINMUX(8, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO9 ESP32_PINMUX(9, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO10 ESP32_PINMUX(10, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO11 ESP32_PINMUX(11, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO12 ESP32_PINMUX(12, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO13 ESP32_PINMUX(13, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO14 ESP32_PINMUX(14, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO22 ESP32_PINMUX(22, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO23 ESP32_PINMUX(23, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO24 ESP32_PINMUX(24, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO25 ESP32_PINMUX(25, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO26 ESP32_PINMUX(26, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)
#define I2C0_SDA_GPIO27 ESP32_PINMUX(27, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)

#define I2C1_SCL_GPIO0 ESP32_PINMUX(0, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO1 ESP32_PINMUX(1, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO2 ESP32_PINMUX(2, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO3 ESP32_PINMUX(3, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO4 ESP32_PINMUX(4, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO5 ESP32_PINMUX(5, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO8 ESP32_PINMUX(8, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO9 ESP32_PINMUX(9, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO10 ESP32_PINMUX(10, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO11 ESP32_PINMUX(11, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO12 ESP32_PINMUX(12, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO13 ESP32_PINMUX(13, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO14 ESP32_PINMUX(14, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO22 ESP32_PINMUX(22, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO23 ESP32_PINMUX(23, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO24 ESP32_PINMUX(24, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO25 ESP32_PINMUX(25, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO26 ESP32_PINMUX(26, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)
#define I2C1_SCL_GPIO27 ESP32_PINMUX(27, ESP_I2CEXT1_SCL_IN, ESP_I2CEXT1_SCL_OUT)

#define I2C1_SDA_GPIO0 ESP32_PINMUX(0, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO1 ESP32_PINMUX(1, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO2 ESP32_PINMUX(2, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO3 ESP32_PINMUX(3, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO4 ESP32_PINMUX(4, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO5 ESP32_PINMUX(5, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO8 ESP32_PINMUX(8, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO9 ESP32_PINMUX(9, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO10 ESP32_PINMUX(10, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO11 ESP32_PINMUX(11, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO12 ESP32_PINMUX(12, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO13 ESP32_PINMUX(13, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO14 ESP32_PINMUX(14, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO22 ESP32_PINMUX(22, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO23 ESP32_PINMUX(23, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO24 ESP32_PINMUX(24, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO25 ESP32_PINMUX(25, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO26 ESP32_PINMUX(26, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)
#define I2C1_SDA_GPIO27 ESP32_PINMUX(27, ESP_I2CEXT1_SDA_IN, ESP_I2CEXT1_SDA_OUT)

#define I2S_I_BCK_GPIO0 ESP32_PINMUX(0, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO1 ESP32_PINMUX(1, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO2 ESP32_PINMUX(2, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO3 ESP32_PINMUX(3, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO4 ESP32_PINMUX(4, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO5 ESP32_PINMUX(5, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO8 ESP32_PINMUX(8, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO9 ESP32_PINMUX(9, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO10 ESP32_PINMUX(10, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO11 ESP32_PINMUX(11, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO12 ESP32_PINMUX(12, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO13 ESP32_PINMUX(13, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO14 ESP32_PINMUX(14, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO22 ESP32_PINMUX(22, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO23 ESP32_PINMUX(23, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO24 ESP32_PINMUX(24, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO25 ESP32_PINMUX(25, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO26 ESP32_PINMUX(26, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)
#define I2S_I_BCK_GPIO27 ESP32_PINMUX(27, ESP_I2SI_BCK_IN, ESP_I2SI_BCK_OUT)

#define I2S_I_SD_GPIO0 ESP32_PINMUX(0, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO1 ESP32_PINMUX(1, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO2 ESP32_PINMUX(2, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO3 ESP32_PINMUX(3, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO4 ESP32_PINMUX(4, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO5 ESP32_PINMUX(5, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO8 ESP32_PINMUX(8, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO9 ESP32_PINMUX(9, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO10 ESP32_PINMUX(10, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO11 ESP32_PINMUX(11, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO12 ESP32_PINMUX(12, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO13 ESP32_PINMUX(13, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO14 ESP32_PINMUX(14, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO22 ESP32_PINMUX(22, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO23 ESP32_PINMUX(23, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO24 ESP32_PINMUX(24, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO25 ESP32_PINMUX(25, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO26 ESP32_PINMUX(26, ESP_I2SI_SD_IN, ESP_NOSIG)
#define I2S_I_SD_GPIO27 ESP32_PINMUX(27, ESP_I2SI_SD_IN, ESP_NOSIG)

#define I2S_I_WS_GPIO0 ESP32_PINMUX(0, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO1 ESP32_PINMUX(1, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO2 ESP32_PINMUX(2, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO3 ESP32_PINMUX(3, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO4 ESP32_PINMUX(4, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO5 ESP32_PINMUX(5, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO8 ESP32_PINMUX(8, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO9 ESP32_PINMUX(9, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO10 ESP32_PINMUX(10, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO11 ESP32_PINMUX(11, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO12 ESP32_PINMUX(12, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO13 ESP32_PINMUX(13, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO14 ESP32_PINMUX(14, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO22 ESP32_PINMUX(22, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO23 ESP32_PINMUX(23, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO24 ESP32_PINMUX(24, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO25 ESP32_PINMUX(25, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO26 ESP32_PINMUX(26, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)
#define I2S_I_WS_GPIO27 ESP32_PINMUX(27, ESP_I2SI_WS_IN, ESP_I2SI_WS_OUT)

#define I2S_MCLK_GPIO0 ESP32_PINMUX(0, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO1 ESP32_PINMUX(1, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO2 ESP32_PINMUX(2, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO3 ESP32_PINMUX(3, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO4 ESP32_PINMUX(4, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO5 ESP32_PINMUX(5, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO8 ESP32_PINMUX(8, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO9 ESP32_PINMUX(9, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO10 ESP32_PINMUX(10, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO11 ESP32_PINMUX(11, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO12 ESP32_PINMUX(12, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO13 ESP32_PINMUX(13, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO14 ESP32_PINMUX(14, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO22 ESP32_PINMUX(22, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO23 ESP32_PINMUX(23, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO24 ESP32_PINMUX(24, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO25 ESP32_PINMUX(25, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO26 ESP32_PINMUX(26, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)
#define I2S_MCLK_GPIO27 ESP32_PINMUX(27, ESP_I2S_MCLK_IN, ESP_I2S_MCLK_OUT)

#define I2S_O_BCK_GPIO0 ESP32_PINMUX(0, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO1 ESP32_PINMUX(1, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO2 ESP32_PINMUX(2, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO3 ESP32_PINMUX(3, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO4 ESP32_PINMUX(4, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO5 ESP32_PINMUX(5, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO8 ESP32_PINMUX(8, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO9 ESP32_PINMUX(9, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO10 ESP32_PINMUX(10, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO11 ESP32_PINMUX(11, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO12 ESP32_PINMUX(12, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO13 ESP32_PINMUX(13, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO14 ESP32_PINMUX(14, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO22 ESP32_PINMUX(22, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO23 ESP32_PINMUX(23, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO24 ESP32_PINMUX(24, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO25 ESP32_PINMUX(25, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO26 ESP32_PINMUX(26, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)
#define I2S_O_BCK_GPIO27 ESP32_PINMUX(27, ESP_I2SO_BCK_IN, ESP_I2SO_BCK_OUT)

#define I2S_O_SD_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_I2SO_SD_OUT)
#define I2S_O_SD_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_I2SO_SD_OUT)

#define I2S_O_WS_GPIO0 ESP32_PINMUX(0, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO1 ESP32_PINMUX(1, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO2 ESP32_PINMUX(2, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO3 ESP32_PINMUX(3, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO4 ESP32_PINMUX(4, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO5 ESP32_PINMUX(5, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO8 ESP32_PINMUX(8, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO9 ESP32_PINMUX(9, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO10 ESP32_PINMUX(10, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO11 ESP32_PINMUX(11, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO12 ESP32_PINMUX(12, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO13 ESP32_PINMUX(13, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO14 ESP32_PINMUX(14, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO22 ESP32_PINMUX(22, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO23 ESP32_PINMUX(23, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO24 ESP32_PINMUX(24, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO25 ESP32_PINMUX(25, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO26 ESP32_PINMUX(26, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)
#define I2S_O_WS_GPIO27 ESP32_PINMUX(27, ESP_I2SO_WS_IN, ESP_I2SO_WS_OUT)

#define LEDC_CH0_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)
#define LEDC_CH0_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT0)

#define LEDC_CH1_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)
#define LEDC_CH1_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT1)

#define LEDC_CH2_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)
#define LEDC_CH2_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT2)

#define LEDC_CH3_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)
#define LEDC_CH3_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT3)

#define LEDC_CH4_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)
#define LEDC_CH4_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT4)

#define LEDC_CH5_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)
#define LEDC_CH5_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_LEDC_LS_SIG_OUT5)

#define MCPWM0_CAP0_GPIO0 ESP32_PINMUX(0, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO1 ESP32_PINMUX(1, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO2 ESP32_PINMUX(2, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO3 ESP32_PINMUX(3, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO4 ESP32_PINMUX(4, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO5 ESP32_PINMUX(5, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO8 ESP32_PINMUX(8, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO9 ESP32_PINMUX(9, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO10 ESP32_PINMUX(10, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO11 ESP32_PINMUX(11, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO12 ESP32_PINMUX(12, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO13 ESP32_PINMUX(13, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO14 ESP32_PINMUX(14, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO22 ESP32_PINMUX(22, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO23 ESP32_PINMUX(23, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO24 ESP32_PINMUX(24, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO25 ESP32_PINMUX(25, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO26 ESP32_PINMUX(26, ESP_PWM0_CAP0_IN, ESP_NOSIG)
#define MCPWM0_CAP0_GPIO27 ESP32_PINMUX(27, ESP_PWM0_CAP0_IN, ESP_NOSIG)

#define MCPWM0_CAP1_GPIO0 ESP32_PINMUX(0, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO1 ESP32_PINMUX(1, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO2 ESP32_PINMUX(2, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO3 ESP32_PINMUX(3, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO4 ESP32_PINMUX(4, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO5 ESP32_PINMUX(5, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO8 ESP32_PINMUX(8, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO9 ESP32_PINMUX(9, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO10 ESP32_PINMUX(10, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO11 ESP32_PINMUX(11, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO12 ESP32_PINMUX(12, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO13 ESP32_PINMUX(13, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO14 ESP32_PINMUX(14, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO22 ESP32_PINMUX(22, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO23 ESP32_PINMUX(23, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO24 ESP32_PINMUX(24, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO25 ESP32_PINMUX(25, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO26 ESP32_PINMUX(26, ESP_PWM0_CAP1_IN, ESP_NOSIG)
#define MCPWM0_CAP1_GPIO27 ESP32_PINMUX(27, ESP_PWM0_CAP1_IN, ESP_NOSIG)

#define MCPWM0_CAP2_GPIO0 ESP32_PINMUX(0, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO1 ESP32_PINMUX(1, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO2 ESP32_PINMUX(2, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO3 ESP32_PINMUX(3, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO4 ESP32_PINMUX(4, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO5 ESP32_PINMUX(5, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO8 ESP32_PINMUX(8, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO9 ESP32_PINMUX(9, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO10 ESP32_PINMUX(10, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO11 ESP32_PINMUX(11, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO12 ESP32_PINMUX(12, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO13 ESP32_PINMUX(13, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO14 ESP32_PINMUX(14, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO22 ESP32_PINMUX(22, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO23 ESP32_PINMUX(23, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO24 ESP32_PINMUX(24, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO25 ESP32_PINMUX(25, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO26 ESP32_PINMUX(26, ESP_PWM0_CAP2_IN, ESP_NOSIG)
#define MCPWM0_CAP2_GPIO27 ESP32_PINMUX(27, ESP_PWM0_CAP2_IN, ESP_NOSIG)

#define MCPWM0_FAULT0_GPIO0 ESP32_PINMUX(0, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO1 ESP32_PINMUX(1, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO2 ESP32_PINMUX(2, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO3 ESP32_PINMUX(3, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO4 ESP32_PINMUX(4, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO5 ESP32_PINMUX(5, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO8 ESP32_PINMUX(8, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO9 ESP32_PINMUX(9, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO10 ESP32_PINMUX(10, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO11 ESP32_PINMUX(11, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO12 ESP32_PINMUX(12, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO13 ESP32_PINMUX(13, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO14 ESP32_PINMUX(14, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO22 ESP32_PINMUX(22, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO23 ESP32_PINMUX(23, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO24 ESP32_PINMUX(24, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO25 ESP32_PINMUX(25, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO26 ESP32_PINMUX(26, ESP_PWM0_F0_IN, ESP_NOSIG)
#define MCPWM0_FAULT0_GPIO27 ESP32_PINMUX(27, ESP_PWM0_F0_IN, ESP_NOSIG)

#define MCPWM0_FAULT1_GPIO0 ESP32_PINMUX(0, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO1 ESP32_PINMUX(1, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO2 ESP32_PINMUX(2, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO3 ESP32_PINMUX(3, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO4 ESP32_PINMUX(4, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO5 ESP32_PINMUX(5, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO8 ESP32_PINMUX(8, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO9 ESP32_PINMUX(9, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO10 ESP32_PINMUX(10, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO11 ESP32_PINMUX(11, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO12 ESP32_PINMUX(12, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO13 ESP32_PINMUX(13, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO14 ESP32_PINMUX(14, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO22 ESP32_PINMUX(22, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO23 ESP32_PINMUX(23, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO24 ESP32_PINMUX(24, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO25 ESP32_PINMUX(25, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO26 ESP32_PINMUX(26, ESP_PWM0_F1_IN, ESP_NOSIG)
#define MCPWM0_FAULT1_GPIO27 ESP32_PINMUX(27, ESP_PWM0_F1_IN, ESP_NOSIG)

#define MCPWM0_FAULT2_GPIO0 ESP32_PINMUX(0, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO1 ESP32_PINMUX(1, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO2 ESP32_PINMUX(2, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO3 ESP32_PINMUX(3, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO4 ESP32_PINMUX(4, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO5 ESP32_PINMUX(5, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO8 ESP32_PINMUX(8, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO9 ESP32_PINMUX(9, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO10 ESP32_PINMUX(10, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO11 ESP32_PINMUX(11, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO12 ESP32_PINMUX(12, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO13 ESP32_PINMUX(13, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO14 ESP32_PINMUX(14, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO22 ESP32_PINMUX(22, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO23 ESP32_PINMUX(23, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO24 ESP32_PINMUX(24, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO25 ESP32_PINMUX(25, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO26 ESP32_PINMUX(26, ESP_PWM0_F2_IN, ESP_NOSIG)
#define MCPWM0_FAULT2_GPIO27 ESP32_PINMUX(27, ESP_PWM0_F2_IN, ESP_NOSIG)

#define MCPWM0_OUT0A_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_PWM0_OUT0A)
#define MCPWM0_OUT0A_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_PWM0_OUT0A)

#define MCPWM0_OUT0B_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_PWM0_OUT0B)
#define MCPWM0_OUT0B_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_PWM0_OUT0B)

#define MCPWM0_OUT1A_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_PWM0_OUT1A)
#define MCPWM0_OUT1A_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_PWM0_OUT1A)

#define MCPWM0_OUT1B_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_PWM0_OUT1B)
#define MCPWM0_OUT1B_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_PWM0_OUT1B)

#define MCPWM0_OUT2A_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_PWM0_OUT2A)
#define MCPWM0_OUT2A_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_PWM0_OUT2A)

#define MCPWM0_OUT2B_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_PWM0_OUT2B)
#define MCPWM0_OUT2B_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_PWM0_OUT2B)

#define MCPWM0_SYNC0_GPIO0 ESP32_PINMUX(0, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO1 ESP32_PINMUX(1, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO2 ESP32_PINMUX(2, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO3 ESP32_PINMUX(3, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO4 ESP32_PINMUX(4, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO5 ESP32_PINMUX(5, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO8 ESP32_PINMUX(8, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO9 ESP32_PINMUX(9, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO10 ESP32_PINMUX(10, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO11 ESP32_PINMUX(11, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO12 ESP32_PINMUX(12, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO13 ESP32_PINMUX(13, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO14 ESP32_PINMUX(14, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO22 ESP32_PINMUX(22, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO23 ESP32_PINMUX(23, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO24 ESP32_PINMUX(24, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO25 ESP32_PINMUX(25, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO26 ESP32_PINMUX(26, ESP_PWM0_SYNC0_IN, ESP_NOSIG)
#define MCPWM0_SYNC0_GPIO27 ESP32_PINMUX(27, ESP_PWM0_SYNC0_IN, ESP_NOSIG)

#define MCPWM0_SYNC1_GPIO0 ESP32_PINMUX(0, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO1 ESP32_PINMUX(1, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO2 ESP32_PINMUX(2, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO3 ESP32_PINMUX(3, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO4 ESP32_PINMUX(4, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO5 ESP32_PINMUX(5, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO8 ESP32_PINMUX(8, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO9 ESP32_PINMUX(9, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO10 ESP32_PINMUX(10, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO11 ESP32_PINMUX(11, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO12 ESP32_PINMUX(12, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO13 ESP32_PINMUX(13, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO14 ESP32_PINMUX(14, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO22 ESP32_PINMUX(22, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO23 ESP32_PINMUX(23, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO24 ESP32_PINMUX(24, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO25 ESP32_PINMUX(25, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO26 ESP32_PINMUX(26, ESP_PWM0_SYNC1_IN, ESP_NOSIG)
#define MCPWM0_SYNC1_GPIO27 ESP32_PINMUX(27, ESP_PWM0_SYNC1_IN, ESP_NOSIG)

#define MCPWM0_SYNC2_GPIO0 ESP32_PINMUX(0, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO1 ESP32_PINMUX(1, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO2 ESP32_PINMUX(2, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO3 ESP32_PINMUX(3, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO4 ESP32_PINMUX(4, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO5 ESP32_PINMUX(5, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO8 ESP32_PINMUX(8, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO9 ESP32_PINMUX(9, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO10 ESP32_PINMUX(10, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO11 ESP32_PINMUX(11, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO12 ESP32_PINMUX(12, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO13 ESP32_PINMUX(13, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO14 ESP32_PINMUX(14, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO22 ESP32_PINMUX(22, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO23 ESP32_PINMUX(23, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO24 ESP32_PINMUX(24, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO25 ESP32_PINMUX(25, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO26 ESP32_PINMUX(26, ESP_PWM0_SYNC2_IN, ESP_NOSIG)
#define MCPWM0_SYNC2_GPIO27 ESP32_PINMUX(27, ESP_PWM0_SYNC2_IN, ESP_NOSIG)

#define PCNT0_CH0CTRL_GPIO0 ESP32_PINMUX(0, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO1 ESP32_PINMUX(1, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO2 ESP32_PINMUX(2, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO3 ESP32_PINMUX(3, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO4 ESP32_PINMUX(4, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO5 ESP32_PINMUX(5, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO8 ESP32_PINMUX(8, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO9 ESP32_PINMUX(9, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO10 ESP32_PINMUX(10, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO11 ESP32_PINMUX(11, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO12 ESP32_PINMUX(12, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO13 ESP32_PINMUX(13, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO14 ESP32_PINMUX(14, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO22 ESP32_PINMUX(22, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO23 ESP32_PINMUX(23, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO24 ESP32_PINMUX(24, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO25 ESP32_PINMUX(25, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO26 ESP32_PINMUX(26, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0CTRL_GPIO27 ESP32_PINMUX(27, ESP_PCNT_CTRL_CH0_IN0, ESP_NOSIG)

#define PCNT0_CH0SIG_GPIO0 ESP32_PINMUX(0, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO1 ESP32_PINMUX(1, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO2 ESP32_PINMUX(2, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO3 ESP32_PINMUX(3, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO4 ESP32_PINMUX(4, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO5 ESP32_PINMUX(5, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO8 ESP32_PINMUX(8, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO9 ESP32_PINMUX(9, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO10 ESP32_PINMUX(10, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO11 ESP32_PINMUX(11, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO12 ESP32_PINMUX(12, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO13 ESP32_PINMUX(13, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO14 ESP32_PINMUX(14, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO22 ESP32_PINMUX(22, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO23 ESP32_PINMUX(23, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO24 ESP32_PINMUX(24, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO25 ESP32_PINMUX(25, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO26 ESP32_PINMUX(26, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)
#define PCNT0_CH0SIG_GPIO27 ESP32_PINMUX(27, ESP_PCNT_SIG_CH0_IN0, ESP_NOSIG)

#define PCNT0_CH1CTRL_GPIO0 ESP32_PINMUX(0, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO1 ESP32_PINMUX(1, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO2 ESP32_PINMUX(2, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO3 ESP32_PINMUX(3, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO4 ESP32_PINMUX(4, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO5 ESP32_PINMUX(5, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO8 ESP32_PINMUX(8, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO9 ESP32_PINMUX(9, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO10 ESP32_PINMUX(10, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO11 ESP32_PINMUX(11, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO12 ESP32_PINMUX(12, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO13 ESP32_PINMUX(13, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO14 ESP32_PINMUX(14, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO22 ESP32_PINMUX(22, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO23 ESP32_PINMUX(23, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO24 ESP32_PINMUX(24, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO25 ESP32_PINMUX(25, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO26 ESP32_PINMUX(26, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1CTRL_GPIO27 ESP32_PINMUX(27, ESP_PCNT_CTRL_CH1_IN0, ESP_NOSIG)

#define PCNT0_CH1SIG_GPIO0 ESP32_PINMUX(0, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO1 ESP32_PINMUX(1, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO2 ESP32_PINMUX(2, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO3 ESP32_PINMUX(3, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO4 ESP32_PINMUX(4, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO5 ESP32_PINMUX(5, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO8 ESP32_PINMUX(8, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO9 ESP32_PINMUX(9, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO10 ESP32_PINMUX(10, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO11 ESP32_PINMUX(11, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO12 ESP32_PINMUX(12, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO13 ESP32_PINMUX(13, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO14 ESP32_PINMUX(14, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO22 ESP32_PINMUX(22, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO23 ESP32_PINMUX(23, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO24 ESP32_PINMUX(24, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO25 ESP32_PINMUX(25, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO26 ESP32_PINMUX(26, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)
#define PCNT0_CH1SIG_GPIO27 ESP32_PINMUX(27, ESP_PCNT_SIG_CH1_IN0, ESP_NOSIG)

#define PCNT1_CH0CTRL_GPIO0 ESP32_PINMUX(0, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO1 ESP32_PINMUX(1, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO2 ESP32_PINMUX(2, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO3 ESP32_PINMUX(3, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO4 ESP32_PINMUX(4, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO5 ESP32_PINMUX(5, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO8 ESP32_PINMUX(8, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO9 ESP32_PINMUX(9, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO10 ESP32_PINMUX(10, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO11 ESP32_PINMUX(11, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO12 ESP32_PINMUX(12, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO13 ESP32_PINMUX(13, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO14 ESP32_PINMUX(14, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO22 ESP32_PINMUX(22, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO23 ESP32_PINMUX(23, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO24 ESP32_PINMUX(24, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO25 ESP32_PINMUX(25, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO26 ESP32_PINMUX(26, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0CTRL_GPIO27 ESP32_PINMUX(27, ESP_PCNT_CTRL_CH0_IN1, ESP_NOSIG)

#define PCNT1_CH0SIG_GPIO0 ESP32_PINMUX(0, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO1 ESP32_PINMUX(1, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO2 ESP32_PINMUX(2, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO3 ESP32_PINMUX(3, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO4 ESP32_PINMUX(4, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO5 ESP32_PINMUX(5, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO8 ESP32_PINMUX(8, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO9 ESP32_PINMUX(9, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO10 ESP32_PINMUX(10, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO11 ESP32_PINMUX(11, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO12 ESP32_PINMUX(12, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO13 ESP32_PINMUX(13, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO14 ESP32_PINMUX(14, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO22 ESP32_PINMUX(22, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO23 ESP32_PINMUX(23, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO24 ESP32_PINMUX(24, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO25 ESP32_PINMUX(25, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO26 ESP32_PINMUX(26, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)
#define PCNT1_CH0SIG_GPIO27 ESP32_PINMUX(27, ESP_PCNT_SIG_CH0_IN1, ESP_NOSIG)

#define PCNT1_CH1CTRL_GPIO0 ESP32_PINMUX(0, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO1 ESP32_PINMUX(1, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO2 ESP32_PINMUX(2, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO3 ESP32_PINMUX(3, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO4 ESP32_PINMUX(4, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO5 ESP32_PINMUX(5, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO8 ESP32_PINMUX(8, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO9 ESP32_PINMUX(9, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO10 ESP32_PINMUX(10, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO11 ESP32_PINMUX(11, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO12 ESP32_PINMUX(12, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO13 ESP32_PINMUX(13, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO14 ESP32_PINMUX(14, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO22 ESP32_PINMUX(22, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO23 ESP32_PINMUX(23, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO24 ESP32_PINMUX(24, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO25 ESP32_PINMUX(25, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO26 ESP32_PINMUX(26, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1CTRL_GPIO27 ESP32_PINMUX(27, ESP_PCNT_CTRL_CH1_IN1, ESP_NOSIG)

#define PCNT1_CH1SIG_GPIO0 ESP32_PINMUX(0, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO1 ESP32_PINMUX(1, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO2 ESP32_PINMUX(2, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO3 ESP32_PINMUX(3, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO4 ESP32_PINMUX(4, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO5 ESP32_PINMUX(5, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO8 ESP32_PINMUX(8, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO9 ESP32_PINMUX(9, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO10 ESP32_PINMUX(10, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO11 ESP32_PINMUX(11, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO12 ESP32_PINMUX(12, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO13 ESP32_PINMUX(13, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO14 ESP32_PINMUX(14, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO22 ESP32_PINMUX(22, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO23 ESP32_PINMUX(23, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO24 ESP32_PINMUX(24, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO25 ESP32_PINMUX(25, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO26 ESP32_PINMUX(26, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)
#define PCNT1_CH1SIG_GPIO27 ESP32_PINMUX(27, ESP_PCNT_SIG_CH1_IN1, ESP_NOSIG)

#define PCNT2_CH0CTRL_GPIO0 ESP32_PINMUX(0, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO1 ESP32_PINMUX(1, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO2 ESP32_PINMUX(2, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO3 ESP32_PINMUX(3, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO4 ESP32_PINMUX(4, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO5 ESP32_PINMUX(5, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO8 ESP32_PINMUX(8, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO9 ESP32_PINMUX(9, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO10 ESP32_PINMUX(10, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO11 ESP32_PINMUX(11, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO12 ESP32_PINMUX(12, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO13 ESP32_PINMUX(13, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO14 ESP32_PINMUX(14, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO22 ESP32_PINMUX(22, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO23 ESP32_PINMUX(23, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO24 ESP32_PINMUX(24, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO25 ESP32_PINMUX(25, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO26 ESP32_PINMUX(26, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0CTRL_GPIO27 ESP32_PINMUX(27, ESP_PCNT_CTRL_CH0_IN2, ESP_NOSIG)

#define PCNT2_CH0SIG_GPIO0 ESP32_PINMUX(0, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO1 ESP32_PINMUX(1, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO2 ESP32_PINMUX(2, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO3 ESP32_PINMUX(3, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO4 ESP32_PINMUX(4, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO5 ESP32_PINMUX(5, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO8 ESP32_PINMUX(8, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO9 ESP32_PINMUX(9, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO10 ESP32_PINMUX(10, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO11 ESP32_PINMUX(11, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO12 ESP32_PINMUX(12, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO13 ESP32_PINMUX(13, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO14 ESP32_PINMUX(14, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO22 ESP32_PINMUX(22, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO23 ESP32_PINMUX(23, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO24 ESP32_PINMUX(24, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO25 ESP32_PINMUX(25, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO26 ESP32_PINMUX(26, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)
#define PCNT2_CH0SIG_GPIO27 ESP32_PINMUX(27, ESP_PCNT_SIG_CH0_IN2, ESP_NOSIG)

#define PCNT2_CH1CTRL_GPIO0 ESP32_PINMUX(0, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO1 ESP32_PINMUX(1, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO2 ESP32_PINMUX(2, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO3 ESP32_PINMUX(3, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO4 ESP32_PINMUX(4, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO5 ESP32_PINMUX(5, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO8 ESP32_PINMUX(8, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO9 ESP32_PINMUX(9, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO10 ESP32_PINMUX(10, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO11 ESP32_PINMUX(11, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO12 ESP32_PINMUX(12, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO13 ESP32_PINMUX(13, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO14 ESP32_PINMUX(14, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO22 ESP32_PINMUX(22, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO23 ESP32_PINMUX(23, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO24 ESP32_PINMUX(24, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO25 ESP32_PINMUX(25, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO26 ESP32_PINMUX(26, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1CTRL_GPIO27 ESP32_PINMUX(27, ESP_PCNT_CTRL_CH1_IN2, ESP_NOSIG)

#define PCNT2_CH1SIG_GPIO0 ESP32_PINMUX(0, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO1 ESP32_PINMUX(1, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO2 ESP32_PINMUX(2, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO3 ESP32_PINMUX(3, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO4 ESP32_PINMUX(4, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO5 ESP32_PINMUX(5, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO8 ESP32_PINMUX(8, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO9 ESP32_PINMUX(9, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO10 ESP32_PINMUX(10, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO11 ESP32_PINMUX(11, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO12 ESP32_PINMUX(12, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO13 ESP32_PINMUX(13, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO14 ESP32_PINMUX(14, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO22 ESP32_PINMUX(22, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO23 ESP32_PINMUX(23, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO24 ESP32_PINMUX(24, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO25 ESP32_PINMUX(25, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO26 ESP32_PINMUX(26, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)
#define PCNT2_CH1SIG_GPIO27 ESP32_PINMUX(27, ESP_PCNT_SIG_CH1_IN2, ESP_NOSIG)

#define PCNT3_CH0CTRL_GPIO0 ESP32_PINMUX(0, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO1 ESP32_PINMUX(1, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO2 ESP32_PINMUX(2, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO3 ESP32_PINMUX(3, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO4 ESP32_PINMUX(4, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO5 ESP32_PINMUX(5, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO8 ESP32_PINMUX(8, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO9 ESP32_PINMUX(9, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO10 ESP32_PINMUX(10, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO11 ESP32_PINMUX(11, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO12 ESP32_PINMUX(12, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO13 ESP32_PINMUX(13, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO14 ESP32_PINMUX(14, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO22 ESP32_PINMUX(22, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO23 ESP32_PINMUX(23, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO24 ESP32_PINMUX(24, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO25 ESP32_PINMUX(25, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO26 ESP32_PINMUX(26, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0CTRL_GPIO27 ESP32_PINMUX(27, ESP_PCNT_CTRL_CH0_IN3, ESP_NOSIG)

#define PCNT3_CH0SIG_GPIO0 ESP32_PINMUX(0, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO1 ESP32_PINMUX(1, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO2 ESP32_PINMUX(2, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO3 ESP32_PINMUX(3, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO4 ESP32_PINMUX(4, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO5 ESP32_PINMUX(5, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO8 ESP32_PINMUX(8, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO9 ESP32_PINMUX(9, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO10 ESP32_PINMUX(10, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO11 ESP32_PINMUX(11, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO12 ESP32_PINMUX(12, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO13 ESP32_PINMUX(13, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO14 ESP32_PINMUX(14, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO22 ESP32_PINMUX(22, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO23 ESP32_PINMUX(23, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO24 ESP32_PINMUX(24, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO25 ESP32_PINMUX(25, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO26 ESP32_PINMUX(26, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)
#define PCNT3_CH0SIG_GPIO27 ESP32_PINMUX(27, ESP_PCNT_SIG_CH0_IN3, ESP_NOSIG)

#define PCNT3_CH1CTRL_GPIO0 ESP32_PINMUX(0, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO1 ESP32_PINMUX(1, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO2 ESP32_PINMUX(2, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO3 ESP32_PINMUX(3, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO4 ESP32_PINMUX(4, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO5 ESP32_PINMUX(5, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO8 ESP32_PINMUX(8, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO9 ESP32_PINMUX(9, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO10 ESP32_PINMUX(10, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO11 ESP32_PINMUX(11, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO12 ESP32_PINMUX(12, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO13 ESP32_PINMUX(13, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO14 ESP32_PINMUX(14, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO22 ESP32_PINMUX(22, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO23 ESP32_PINMUX(23, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO24 ESP32_PINMUX(24, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO25 ESP32_PINMUX(25, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO26 ESP32_PINMUX(26, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1CTRL_GPIO27 ESP32_PINMUX(27, ESP_PCNT_CTRL_CH1_IN3, ESP_NOSIG)

#define PCNT3_CH1SIG_GPIO0 ESP32_PINMUX(0, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO1 ESP32_PINMUX(1, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO2 ESP32_PINMUX(2, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO3 ESP32_PINMUX(3, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO4 ESP32_PINMUX(4, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO5 ESP32_PINMUX(5, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO8 ESP32_PINMUX(8, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO9 ESP32_PINMUX(9, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO10 ESP32_PINMUX(10, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO11 ESP32_PINMUX(11, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO12 ESP32_PINMUX(12, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO13 ESP32_PINMUX(13, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO14 ESP32_PINMUX(14, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO22 ESP32_PINMUX(22, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO23 ESP32_PINMUX(23, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO24 ESP32_PINMUX(24, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO25 ESP32_PINMUX(25, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO26 ESP32_PINMUX(26, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)
#define PCNT3_CH1SIG_GPIO27 ESP32_PINMUX(27, ESP_PCNT_SIG_CH1_IN3, ESP_NOSIG)

#define RMT_IN0_GPIO0  ESP32_PINMUX(0, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO1  ESP32_PINMUX(1, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO2  ESP32_PINMUX(2, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO3  ESP32_PINMUX(3, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO4  ESP32_PINMUX(4, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO5  ESP32_PINMUX(5, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO8  ESP32_PINMUX(8, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO9  ESP32_PINMUX(9, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO10 ESP32_PINMUX(10, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO11 ESP32_PINMUX(11, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO12 ESP32_PINMUX(12, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO13 ESP32_PINMUX(13, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO14 ESP32_PINMUX(14, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO22 ESP32_PINMUX(22, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO23 ESP32_PINMUX(23, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO24 ESP32_PINMUX(24, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO25 ESP32_PINMUX(25, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO26 ESP32_PINMUX(26, ESP_RMT_SIG_IN0, ESP_NOSIG)
#define RMT_IN0_GPIO27 ESP32_PINMUX(27, ESP_RMT_SIG_IN0, ESP_NOSIG)

#define RMT_IN1_GPIO0  ESP32_PINMUX(0, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO1  ESP32_PINMUX(1, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO2  ESP32_PINMUX(2, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO3  ESP32_PINMUX(3, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO4  ESP32_PINMUX(4, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO5  ESP32_PINMUX(5, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO8  ESP32_PINMUX(8, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO9  ESP32_PINMUX(9, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO10 ESP32_PINMUX(10, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO11 ESP32_PINMUX(11, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO12 ESP32_PINMUX(12, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO13 ESP32_PINMUX(13, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO14 ESP32_PINMUX(14, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO22 ESP32_PINMUX(22, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO23 ESP32_PINMUX(23, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO24 ESP32_PINMUX(24, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO25 ESP32_PINMUX(25, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO26 ESP32_PINMUX(26, ESP_RMT_SIG_IN1, ESP_NOSIG)
#define RMT_IN1_GPIO27 ESP32_PINMUX(27, ESP_RMT_SIG_IN1, ESP_NOSIG)

#define RMT_OUT0_GPIO0  ESP32_PINMUX(0, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO1  ESP32_PINMUX(1, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO2  ESP32_PINMUX(2, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO3  ESP32_PINMUX(3, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO4  ESP32_PINMUX(4, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO5  ESP32_PINMUX(5, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO8  ESP32_PINMUX(8, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO9  ESP32_PINMUX(9, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_RMT_SIG_OUT0)
#define RMT_OUT0_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_RMT_SIG_OUT0)

#define RMT_OUT1_GPIO0  ESP32_PINMUX(0, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO1  ESP32_PINMUX(1, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO2  ESP32_PINMUX(2, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO3  ESP32_PINMUX(3, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO4  ESP32_PINMUX(4, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO5  ESP32_PINMUX(5, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO8  ESP32_PINMUX(8, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO9  ESP32_PINMUX(9, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_RMT_SIG_OUT1)
#define RMT_OUT1_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_RMT_SIG_OUT1)

#define SPIM2_CSEL_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_FSPICS0_OUT)
#define SPIM2_CSEL_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_FSPICS0_OUT)

#define SPIM2_CSEL1_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_FSPICS1_OUT)
#define SPIM2_CSEL1_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_FSPICS1_OUT)

#define SPIM2_CSEL2_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_FSPICS2_OUT)
#define SPIM2_CSEL2_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_FSPICS2_OUT)

#define SPIM2_CSEL3_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_FSPICS3_OUT)
#define SPIM2_CSEL3_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_FSPICS3_OUT)

#define SPIM2_CSEL4_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_FSPICS4_OUT)
#define SPIM2_CSEL4_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_FSPICS4_OUT)

#define SPIM2_CSEL5_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_FSPICS5_OUT)
#define SPIM2_CSEL5_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_FSPICS5_OUT)

#define SPIM2_MISO_GPIO0 ESP32_PINMUX(0, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO1 ESP32_PINMUX(1, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO2 ESP32_PINMUX(2, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO3 ESP32_PINMUX(3, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO4 ESP32_PINMUX(4, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO5 ESP32_PINMUX(5, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO8 ESP32_PINMUX(8, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO9 ESP32_PINMUX(9, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO10 ESP32_PINMUX(10, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO11 ESP32_PINMUX(11, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO12 ESP32_PINMUX(12, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO13 ESP32_PINMUX(13, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO14 ESP32_PINMUX(14, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO22 ESP32_PINMUX(22, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO23 ESP32_PINMUX(23, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO24 ESP32_PINMUX(24, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO25 ESP32_PINMUX(25, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO26 ESP32_PINMUX(26, ESP_FSPIQ_IN, ESP_NOSIG)
#define SPIM2_MISO_GPIO27 ESP32_PINMUX(27, ESP_FSPIQ_IN, ESP_NOSIG)

#define SPIM2_MOSI_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_FSPID_OUT)
#define SPIM2_MOSI_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_FSPID_OUT)

#define SPIM2_SCLK_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_FSPICLK_OUT)
#define SPIM2_SCLK_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_FSPICLK_OUT)

#define TWAI_BUS_OFF_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)
#define TWAI_BUS_OFF_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_TWAI_BUS_OFF_ON)

#define TWAI_CLKOUT_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_TWAI_CLKOUT)
#define TWAI_CLKOUT_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_TWAI_CLKOUT)

#define TWAI_RX_GPIO0 ESP32_PINMUX(0, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO1 ESP32_PINMUX(1, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO2 ESP32_PINMUX(2, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO3 ESP32_PINMUX(3, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO4 ESP32_PINMUX(4, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO5 ESP32_PINMUX(5, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO8 ESP32_PINMUX(8, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO9 ESP32_PINMUX(9, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO10 ESP32_PINMUX(10, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO11 ESP32_PINMUX(11, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO12 ESP32_PINMUX(12, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO13 ESP32_PINMUX(13, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO14 ESP32_PINMUX(14, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO22 ESP32_PINMUX(22, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO23 ESP32_PINMUX(23, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO24 ESP32_PINMUX(24, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO25 ESP32_PINMUX(25, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO26 ESP32_PINMUX(26, ESP_TWAI_RX, ESP_NOSIG)
#define TWAI_RX_GPIO27 ESP32_PINMUX(27, ESP_TWAI_RX, ESP_NOSIG)

#define TWAI_TX_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_TWAI_TX)
#define TWAI_TX_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_TWAI_TX)

#define UART0_CTS_GPIO0 ESP32_PINMUX(0, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO1 ESP32_PINMUX(1, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO2 ESP32_PINMUX(2, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO3 ESP32_PINMUX(3, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO4 ESP32_PINMUX(4, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO5 ESP32_PINMUX(5, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO8 ESP32_PINMUX(8, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO9 ESP32_PINMUX(9, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO10 ESP32_PINMUX(10, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO11 ESP32_PINMUX(11, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO12 ESP32_PINMUX(12, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO13 ESP32_PINMUX(13, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO14 ESP32_PINMUX(14, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO22 ESP32_PINMUX(22, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO23 ESP32_PINMUX(23, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO24 ESP32_PINMUX(24, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO25 ESP32_PINMUX(25, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO26 ESP32_PINMUX(26, ESP_U0CTS_IN, ESP_NOSIG)
#define UART0_CTS_GPIO27 ESP32_PINMUX(27, ESP_U0CTS_IN, ESP_NOSIG)

#define UART0_DSR_GPIO0 ESP32_PINMUX(0, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO1 ESP32_PINMUX(1, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO2 ESP32_PINMUX(2, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO3 ESP32_PINMUX(3, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO4 ESP32_PINMUX(4, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO5 ESP32_PINMUX(5, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO8 ESP32_PINMUX(8, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO9 ESP32_PINMUX(9, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO10 ESP32_PINMUX(10, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO11 ESP32_PINMUX(11, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO12 ESP32_PINMUX(12, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO13 ESP32_PINMUX(13, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO14 ESP32_PINMUX(14, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO22 ESP32_PINMUX(22, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO23 ESP32_PINMUX(23, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO24 ESP32_PINMUX(24, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO25 ESP32_PINMUX(25, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO26 ESP32_PINMUX(26, ESP_U0DSR_IN, ESP_NOSIG)
#define UART0_DSR_GPIO27 ESP32_PINMUX(27, ESP_U0DSR_IN, ESP_NOSIG)

#define UART0_DTR_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_U0DTR_OUT)
#define UART0_DTR_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_U0DTR_OUT)

#define UART0_RTS_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_U0RTS_OUT)
#define UART0_RTS_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_U0RTS_OUT)

#define UART0_RX_GPIO0 ESP32_PINMUX(0, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO1 ESP32_PINMUX(1, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO2 ESP32_PINMUX(2, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO3 ESP32_PINMUX(3, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO4 ESP32_PINMUX(4, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO5 ESP32_PINMUX(5, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO8 ESP32_PINMUX(8, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO9 ESP32_PINMUX(9, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO10 ESP32_PINMUX(10, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO11 ESP32_PINMUX(11, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO12 ESP32_PINMUX(12, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO13 ESP32_PINMUX(13, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO14 ESP32_PINMUX(14, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO22 ESP32_PINMUX(22, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO23 ESP32_PINMUX(23, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO24 ESP32_PINMUX(24, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO25 ESP32_PINMUX(25, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO26 ESP32_PINMUX(26, ESP_U0RXD_IN, ESP_NOSIG)
#define UART0_RX_GPIO27 ESP32_PINMUX(27, ESP_U0RXD_IN, ESP_NOSIG)

#define UART0_TX_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_U0TXD_OUT)
#define UART0_TX_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_U0TXD_OUT)

#define UART1_CTS_GPIO0 ESP32_PINMUX(0, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO1 ESP32_PINMUX(1, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO2 ESP32_PINMUX(2, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO3 ESP32_PINMUX(3, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO4 ESP32_PINMUX(4, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO5 ESP32_PINMUX(5, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO8 ESP32_PINMUX(8, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO9 ESP32_PINMUX(9, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO10 ESP32_PINMUX(10, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO11 ESP32_PINMUX(11, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO12 ESP32_PINMUX(12, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO13 ESP32_PINMUX(13, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO14 ESP32_PINMUX(14, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO22 ESP32_PINMUX(22, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO23 ESP32_PINMUX(23, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO24 ESP32_PINMUX(24, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO25 ESP32_PINMUX(25, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO26 ESP32_PINMUX(26, ESP_U1CTS_IN, ESP_NOSIG)
#define UART1_CTS_GPIO27 ESP32_PINMUX(27, ESP_U1CTS_IN, ESP_NOSIG)

#define UART1_DSR_GPIO0 ESP32_PINMUX(0, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO1 ESP32_PINMUX(1, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO2 ESP32_PINMUX(2, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO3 ESP32_PINMUX(3, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO4 ESP32_PINMUX(4, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO5 ESP32_PINMUX(5, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO8 ESP32_PINMUX(8, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO9 ESP32_PINMUX(9, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO10 ESP32_PINMUX(10, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO11 ESP32_PINMUX(11, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO12 ESP32_PINMUX(12, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO13 ESP32_PINMUX(13, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO14 ESP32_PINMUX(14, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO22 ESP32_PINMUX(22, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO23 ESP32_PINMUX(23, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO24 ESP32_PINMUX(24, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO25 ESP32_PINMUX(25, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO26 ESP32_PINMUX(26, ESP_U1DSR_IN, ESP_NOSIG)
#define UART1_DSR_GPIO27 ESP32_PINMUX(27, ESP_U1DSR_IN, ESP_NOSIG)

#define UART1_DTR_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_U1DTR_OUT)
#define UART1_DTR_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_U1DTR_OUT)

#define UART1_RTS_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_U1RTS_OUT)
#define UART1_RTS_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_U1RTS_OUT)

#define UART1_RX_GPIO0 ESP32_PINMUX(0, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO1 ESP32_PINMUX(1, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO2 ESP32_PINMUX(2, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO3 ESP32_PINMUX(3, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO4 ESP32_PINMUX(4, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO5 ESP32_PINMUX(5, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO8 ESP32_PINMUX(8, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO9 ESP32_PINMUX(9, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO10 ESP32_PINMUX(10, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO11 ESP32_PINMUX(11, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO12 ESP32_PINMUX(12, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO13 ESP32_PINMUX(13, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO14 ESP32_PINMUX(14, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO22 ESP32_PINMUX(22, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO23 ESP32_PINMUX(23, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO24 ESP32_PINMUX(24, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO25 ESP32_PINMUX(25, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO26 ESP32_PINMUX(26, ESP_U1RXD_IN, ESP_NOSIG)
#define UART1_RX_GPIO27 ESP32_PINMUX(27, ESP_U1RXD_IN, ESP_NOSIG)

#define UART1_TX_GPIO0 ESP32_PINMUX(0, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO1 ESP32_PINMUX(1, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO2 ESP32_PINMUX(2, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO3 ESP32_PINMUX(3, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO4 ESP32_PINMUX(4, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO5 ESP32_PINMUX(5, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO8 ESP32_PINMUX(8, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO9 ESP32_PINMUX(9, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_U1TXD_OUT)
#define UART1_TX_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_U1TXD_OUT)

#define SPIS2_CSEL_GPIO0  ESP32_PINMUX(0, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO1  ESP32_PINMUX(1, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO2  ESP32_PINMUX(2, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO3  ESP32_PINMUX(3, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO4  ESP32_PINMUX(4, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO5  ESP32_PINMUX(5, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO8  ESP32_PINMUX(8, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO9  ESP32_PINMUX(9, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO10 ESP32_PINMUX(10, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO11 ESP32_PINMUX(11, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO12 ESP32_PINMUX(12, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO13 ESP32_PINMUX(13, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO14 ESP32_PINMUX(14, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO22 ESP32_PINMUX(22, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO23 ESP32_PINMUX(23, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO24 ESP32_PINMUX(24, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO25 ESP32_PINMUX(25, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO26 ESP32_PINMUX(26, ESP_FSPICS0_IN, ESP_NOSIG)
#define SPIS2_CSEL_GPIO27 ESP32_PINMUX(27, ESP_FSPICS0_IN, ESP_NOSIG)

#define SPIS2_MISO_GPIO0  ESP32_PINMUX(0, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO1  ESP32_PINMUX(1, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO2  ESP32_PINMUX(2, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO3  ESP32_PINMUX(3, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO4  ESP32_PINMUX(4, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO5  ESP32_PINMUX(5, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO8  ESP32_PINMUX(8, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO9  ESP32_PINMUX(9, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO10 ESP32_PINMUX(10, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO11 ESP32_PINMUX(11, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO12 ESP32_PINMUX(12, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO13 ESP32_PINMUX(13, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO14 ESP32_PINMUX(14, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO22 ESP32_PINMUX(22, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO23 ESP32_PINMUX(23, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO24 ESP32_PINMUX(24, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO25 ESP32_PINMUX(25, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO26 ESP32_PINMUX(26, ESP_NOSIG, ESP_FSPIQ_OUT)
#define SPIS2_MISO_GPIO27 ESP32_PINMUX(27, ESP_NOSIG, ESP_FSPIQ_OUT)

#define SPIS2_MOSI_GPIO0  ESP32_PINMUX(0, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO1  ESP32_PINMUX(1, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO2  ESP32_PINMUX(2, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO3  ESP32_PINMUX(3, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO4  ESP32_PINMUX(4, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO5  ESP32_PINMUX(5, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO8  ESP32_PINMUX(8, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO9  ESP32_PINMUX(9, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO10 ESP32_PINMUX(10, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO11 ESP32_PINMUX(11, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO12 ESP32_PINMUX(12, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO13 ESP32_PINMUX(13, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO14 ESP32_PINMUX(14, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO22 ESP32_PINMUX(22, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO23 ESP32_PINMUX(23, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO24 ESP32_PINMUX(24, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO25 ESP32_PINMUX(25, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO26 ESP32_PINMUX(26, ESP_FSPID_IN, ESP_NOSIG)
#define SPIS2_MOSI_GPIO27 ESP32_PINMUX(27, ESP_FSPID_IN, ESP_NOSIG)

#define SPIS2_SCLK_GPIO0  ESP32_PINMUX(0, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO1  ESP32_PINMUX(1, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO2  ESP32_PINMUX(2, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO3  ESP32_PINMUX(3, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO4  ESP32_PINMUX(4, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO5  ESP32_PINMUX(5, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO8  ESP32_PINMUX(8, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO9  ESP32_PINMUX(9, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO10 ESP32_PINMUX(10, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO11 ESP32_PINMUX(11, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO12 ESP32_PINMUX(12, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO13 ESP32_PINMUX(13, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO14 ESP32_PINMUX(14, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO22 ESP32_PINMUX(22, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO23 ESP32_PINMUX(23, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO24 ESP32_PINMUX(24, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO25 ESP32_PINMUX(25, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO26 ESP32_PINMUX(26, ESP_FSPICLK_IN, ESP_NOSIG)
#define SPIS2_SCLK_GPIO27 ESP32_PINMUX(27, ESP_FSPICLK_IN, ESP_NOSIG)



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32H2_PINCTRL_H_ */
```

## 62.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

注意（NOTE）：本文件由 `esp_genpinctrl.py` 自动生成。

### 注释 2：原第 2085 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32H2_PINCTRL_H_`。

## 62.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp32h2-pinctrl_8h.html)
- [esp-pinctrl-common.h](https://docs.zephyrproject.org/latest/doxygen/html/esp-pinctrl-common_8h.html)
- [esp32h2-gpio-sigmap.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32h2-gpio-sigmap_8h.html)

---

[上一章](P061_esp32c61-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P063_esp32p4-pinctrl.h_源码浏览.md)
