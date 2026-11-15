---
id: learning.zephyr-docs.api-source-reference.page-24
title: alif-ensemble-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_alif-ensemble-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-pinctrl_8h.html)。

## 24.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00025"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00154"></a>
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
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00243"></a>
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
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
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
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
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
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00325"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00414"></a>
<a id="l00421"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00488"></a>
<a id="l00495"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00575"></a>
<a id="l00582"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00664"></a>
<a id="l00671"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00691"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00752"></a>
<a id="l00759"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00781"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00841"></a>
<a id="l00848"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00852"></a>
<a id="l00853"></a>
<a id="l00854"></a>
<a id="l00855"></a>
<a id="l00856"></a>
<a id="l00857"></a>
<a id="l00858"></a>
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
<a id="l00871"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00888"></a>
<a id="l00890"></a>
<a id="l00891"></a>
<a id="l00892"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00918"></a>
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
<a id="l00937"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00949"></a>
<a id="l00950"></a>
<a id="l00951"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00955"></a>
<a id="l00956"></a>
<a id="l00957"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00961"></a>
<a id="l00962"></a>
<a id="l00963"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="l00966"></a>
<a id="l00967"></a>
<a id="l00969"></a>
<a id="l00970"></a>
<a id="l00971"></a>
<a id="l00972"></a>
<a id="l00973"></a>
<a id="l00974"></a>
<a id="l00975"></a>
<a id="l00976"></a>
<a id="l00977"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="l00984"></a>
<a id="l00985"></a>
<a id="l00986"></a>
<a id="l00987"></a>
<a id="l00989"></a>
<a id="l00990"></a>
<a id="l00991"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l00995"></a>
<a id="l00996"></a>
<a id="l00997"></a>
<a id="l00999"></a>
<a id="l01000"></a>
<a id="l01001"></a>
<a id="l01002"></a>
<a id="l01003"></a>
<a id="l01004"></a>
<a id="l01005"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01009"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01012"></a>
<a id="l01013"></a>
<a id="l01014"></a>
<a id="l01015"></a>
<a id="l01016"></a>
<a id="l01017"></a>
<a id="l01019"></a>
<a id="l01026"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="l01032"></a>
<a id="l01033"></a>
<a id="l01034"></a>
<a id="l01035"></a>
<a id="l01036"></a>
<a id="l01038"></a>
<a id="l01039"></a>
<a id="l01040"></a>
<a id="l01041"></a>
<a id="l01042"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01054"></a>
<a id="l01055"></a>
<a id="l01056"></a>
<a id="l01058"></a>
<a id="l01059"></a>
<a id="l01060"></a>
<a id="l01061"></a>
<a id="l01062"></a>
<a id="l01063"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="l01066"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="l01073"></a>
<a id="l01074"></a>
<a id="l01075"></a>
<a id="l01076"></a>
<a id="l01078"></a>
<a id="l01079"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01082"></a>
<a id="l01083"></a>
<a id="l01084"></a>
<a id="l01085"></a>
<a id="l01086"></a>
<a id="l01088"></a>
<a id="l01089"></a>
<a id="l01090"></a>
<a id="l01091"></a>
<a id="l01092"></a>
<a id="l01093"></a>
<a id="l01094"></a>
<a id="l01095"></a>
<a id="l01096"></a>
<a id="l01098"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01101"></a>
<a id="l01102"></a>
<a id="l01103"></a>
<a id="l01104"></a>
<a id="l01105"></a>
<a id="l01106"></a>
<a id="l01108"></a>
<a id="l01115"></a>
<a id="l01117"></a>
<a id="l01118"></a>
<a id="l01119"></a>
<a id="l01120"></a>
<a id="l01121"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="l01125"></a>
<a id="l01127"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01132"></a>
<a id="l01133"></a>
<a id="l01134"></a>
<a id="l01135"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01141"></a>
<a id="l01142"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="l01147"></a>
<a id="l01148"></a>
<a id="l01149"></a>
<a id="l01150"></a>
<a id="l01151"></a>
<a id="l01152"></a>
<a id="l01153"></a>
<a id="l01154"></a>
<a id="l01155"></a>
<a id="l01157"></a>
<a id="l01158"></a>
<a id="l01159"></a>
<a id="l01160"></a>
<a id="l01161"></a>
<a id="l01162"></a>
<a id="l01163"></a>
<a id="l01164"></a>
<a id="l01165"></a>
<a id="l01167"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="l01170"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01173"></a>
<a id="l01174"></a>
<a id="l01175"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="l01179"></a>
<a id="l01180"></a>
<a id="l01181"></a>
<a id="l01182"></a>
<a id="l01183"></a>
<a id="l01184"></a>
<a id="l01186"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="l01191"></a>
<a id="l01192"></a>
<a id="l01194"></a>
<a id="l01201"></a>
<a id="l01203"></a>
<a id="l01204"></a>
<a id="l01205"></a>
<a id="l01206"></a>
<a id="l01207"></a>
<a id="l01208"></a>
<a id="l01209"></a>
<a id="l01210"></a>
<a id="l01211"></a>
<a id="l01213"></a>
<a id="l01214"></a>
<a id="l01215"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01220"></a>
<a id="l01222"></a>
<a id="l01223"></a>
<a id="l01224"></a>
<a id="l01225"></a>
<a id="l01226"></a>
<a id="l01227"></a>
<a id="l01228"></a>
<a id="l01229"></a>
<a id="l01231"></a>
<a id="l01232"></a>
<a id="l01233"></a>
<a id="l01234"></a>
<a id="l01235"></a>
<a id="l01236"></a>
<a id="l01237"></a>
<a id="l01238"></a>
<a id="l01240"></a>
<a id="l01241"></a>
<a id="l01242"></a>
<a id="l01243"></a>
<a id="l01244"></a>
<a id="l01245"></a>
<a id="l01246"></a>
<a id="l01247"></a>
<a id="l01249"></a>
<a id="l01250"></a>
<a id="l01251"></a>
<a id="l01252"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="l01258"></a>
<a id="l01259"></a>
<a id="l01260"></a>
<a id="l01261"></a>
<a id="l01262"></a>
<a id="l01263"></a>
<a id="l01264"></a>
<a id="l01265"></a>
<a id="l01267"></a>
<a id="l01268"></a>
<a id="l01269"></a>
<a id="l01270"></a>
<a id="l01271"></a>
<a id="l01272"></a>
<a id="l01273"></a>
<a id="l01274"></a>
<a id="l01276"></a>
<a id="l01283"></a>
<a id="l01285"></a>
<a id="l01286"></a>
<a id="l01287"></a>
<a id="l01288"></a>
<a id="l01289"></a>
<a id="l01290"></a>
<a id="l01291"></a>
<a id="l01293"></a>
<a id="l01294"></a>
<a id="l01295"></a>
<a id="l01296"></a>
<a id="l01297"></a>
<a id="l01298"></a>
<a id="l01299"></a>
<a id="l01300"></a>
<a id="l01302"></a>
<a id="l01303"></a>
<a id="l01304"></a>
<a id="l01305"></a>
<a id="l01306"></a>
<a id="l01307"></a>
<a id="l01308"></a>
<a id="l01309"></a>
<a id="l01311"></a>
<a id="l01312"></a>
<a id="l01313"></a>
<a id="l01314"></a>
<a id="l01315"></a>
<a id="l01316"></a>
<a id="l01318"></a>
<a id="l01319"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="l01322"></a>
<a id="l01323"></a>
<a id="l01324"></a>
<a id="l01326"></a>
<a id="l01327"></a>
<a id="l01328"></a>
<a id="l01329"></a>
<a id="l01330"></a>
<a id="l01331"></a>
<a id="l01332"></a>
<a id="l01334"></a>
<a id="l01335"></a>
<a id="l01336"></a>
<a id="l01337"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="l01340"></a>
<a id="l01342"></a>
<a id="l01343"></a>
<a id="l01344"></a>
<a id="l01345"></a>
<a id="l01346"></a>
<a id="l01347"></a>
<a id="l01348"></a>
<a id="l01350"></a>
<a id="l01357"></a>
<a id="l01359"></a>
<a id="l01360"></a>
<a id="l01362"></a>
<a id="l01363"></a>
<a id="l01365"></a>
<a id="l01366"></a>
<a id="l01368"></a>
<a id="l01369"></a>
<a id="l01371"></a>
<a id="l01372"></a>
<a id="l01374"></a>
<a id="l01375"></a>
<a id="l01377"></a>
<a id="l01378"></a>
<a id="l01380"></a>
<a id="l01381"></a>
<a id="l01383"></a>
<a id="l01390"></a>
<a id="l01392"></a>
<a id="l01393"></a>
<a id="l01394"></a>
<a id="l01396"></a>
<a id="l01397"></a>
<a id="l01398"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01402"></a>
<a id="l01404"></a>
<a id="l01405"></a>
<a id="l01406"></a>
<a id="l01408"></a>
<a id="l01409"></a>
<a id="l01410"></a>
<a id="l01412"></a>
<a id="l01413"></a>
<a id="l01414"></a>
<a id="l01416"></a>
<a id="l01417"></a>
<a id="l01418"></a>
<a id="l01420"></a>
<a id="l01421"></a>
<a id="l01422"></a>
<a id="l01424"></a>
<a id="l01431"></a>
<a id="l01433"></a>
<a id="l01434"></a>
<a id="l01435"></a>
<a id="l01437"></a>
<a id="l01438"></a>
<a id="l01439"></a>
<a id="l01441"></a>
<a id="l01442"></a>
<a id="l01443"></a>
<a id="l01445"></a>
<a id="l01446"></a>
<a id="l01447"></a>
<a id="l01449"></a>
<a id="l01450"></a>
<a id="l01451"></a>
<a id="l01453"></a>
<a id="l01454"></a>
<a id="l01455"></a>
<a id="l01457"></a>
<a id="l01458"></a>
<a id="l01459"></a>
<a id="l01461"></a>
<a id="l01462"></a>
<a id="l01463"></a>
<a id="l01465"></a>
<a id="l01466"></a>

```c
/*
 * Copyright (c) 2025 Alif Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ALIF_ENSEMBLE_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ALIF_ENSEMBLE_PINCTRL_H_



#define ALIF_PINMUX_FUNC_POS    0U
#define ALIF_PINMUX_FUNC_MASK   0x7U
#define ALIF_PINMUX_PIN_POS     3U
#define ALIF_PINMUX_PIN_MASK    0x7U
#define ALIF_PINMUX_PORT_POS    6U
#define ALIF_PINMUX_PORT_MASK   0x1FU


#define ALIF_PINMUX(port, pin, func)                                    \
        ((((port) & ALIF_PINMUX_PORT_MASK) << ALIF_PINMUX_PORT_POS) |   \
        (((pin) & ALIF_PINMUX_PIN_MASK) << ALIF_PINMUX_PIN_POS) |       \
        (((func) & ALIF_PINMUX_FUNC_MASK) << ALIF_PINMUX_FUNC_POS))


#define PIN_P0_0__GPIO                  ALIF_PINMUX(0, 0, 0)
#define PIN_P0_0__OSPI0_D0_A            ALIF_PINMUX(0, 0, 1)
#define PIN_P0_0__UART0_RX_A            ALIF_PINMUX(0, 0, 2)
#define PIN_P0_0__I3C_SDA_A             ALIF_PINMUX(0, 0, 3)
#define PIN_P0_0__UT0_T0_A              ALIF_PINMUX(0, 0, 4)
#define PIN_P0_0__LPCAM_HSYNC_B         ALIF_PINMUX(0, 0, 5)
#define PIN_P0_0__CAM_HSYNC_A           ALIF_PINMUX(0, 0, 6)
#define PIN_P0_0__ANA_S0                ALIF_PINMUX(0, 0, 7)

#define PIN_P0_1__GPIO                  ALIF_PINMUX(0, 1, 0)
#define PIN_P0_1__OSPI0_D1_A            ALIF_PINMUX(0, 1, 1)
#define PIN_P0_1__UART0_TX_A            ALIF_PINMUX(0, 1, 2)
#define PIN_P0_1__I3C_SCL_A             ALIF_PINMUX(0, 1, 3)
#define PIN_P0_1__UT0_T1_A              ALIF_PINMUX(0, 1, 4)
#define PIN_P0_1__LPCAM_VSYNC_B         ALIF_PINMUX(0, 1, 5)
#define PIN_P0_1__CAM_VSYNC_A           ALIF_PINMUX(0, 1, 6)
#define PIN_P0_1__ANA_S1                ALIF_PINMUX(0, 1, 7)

#define PIN_P0_2__GPIO                  ALIF_PINMUX(0, 2, 0)
#define PIN_P0_2__OSPI0_D2_A            ALIF_PINMUX(0, 2, 1)
#define PIN_P0_2__UART0_CTS_A           ALIF_PINMUX(0, 2, 2)
#define PIN_P0_2__I2C0_SDA_A            ALIF_PINMUX(0, 2, 3)
#define PIN_P0_2__UT1_T0_A              ALIF_PINMUX(0, 2, 4)
#define PIN_P0_2__LPCAM_PCLK_B          ALIF_PINMUX(0, 2, 5)
#define PIN_P0_2__CAM_PCLK_A            ALIF_PINMUX(0, 2, 6)
#define PIN_P0_2__ANA_S2                ALIF_PINMUX(0, 2, 7)

#define PIN_P0_3__GPIO                  ALIF_PINMUX(0, 3, 0)
#define PIN_P0_3__OSPI0_D3_A            ALIF_PINMUX(0, 3, 1)
#define PIN_P0_3__UART0_RTS_A           ALIF_PINMUX(0, 3, 2)
#define PIN_P0_3__I2C0_SCL_A            ALIF_PINMUX(0, 3, 3)
#define PIN_P0_3__UT1_T1_A              ALIF_PINMUX(0, 3, 4)
#define PIN_P0_3__LPCAM_XVCLK_B         ALIF_PINMUX(0, 3, 5)
#define PIN_P0_3__CAM_XVCLK_A           ALIF_PINMUX(0, 3, 6)
#define PIN_P0_3__ANA_S3                ALIF_PINMUX(0, 3, 7)

#define PIN_P0_4__GPIO                  ALIF_PINMUX(0, 4, 0)
#define PIN_P0_4__OSPI0_D4_A            ALIF_PINMUX(0, 4, 1)
#define PIN_P0_4__UART1_RX_A            ALIF_PINMUX(0, 4, 2)
#define PIN_P0_4__PDM_D0_A              ALIF_PINMUX(0, 4, 3)
#define PIN_P0_4__I2C1_SDA_A            ALIF_PINMUX(0, 4, 4)
#define PIN_P0_4__UT2_T0_A              ALIF_PINMUX(0, 4, 5)
#define PIN_P0_4__CAN_RXD_B             ALIF_PINMUX(0, 4, 6)
#define PIN_P0_4__ANA_S4                ALIF_PINMUX(0, 4, 7)

#define PIN_P0_5__GPIO                  ALIF_PINMUX(0, 5, 0)
#define PIN_P0_5__OSPI0_D5_A            ALIF_PINMUX(0, 5, 1)
#define PIN_P0_5__UART1_TX_A            ALIF_PINMUX(0, 5, 2)
#define PIN_P0_5__PDM_C0_A              ALIF_PINMUX(0, 5, 3)
#define PIN_P0_5__I2C1_SCL_A            ALIF_PINMUX(0, 5, 4)
#define PIN_P0_5__UT2_T1_A              ALIF_PINMUX(0, 5, 5)
#define PIN_P0_5__CAN_TXD_B             ALIF_PINMUX(0, 5, 6)
#define PIN_P0_5__ANA_S5                ALIF_PINMUX(0, 5, 7)

#define PIN_P0_6__GPIO                  ALIF_PINMUX(0, 6, 0)
#define PIN_P0_6__OSPI0_D6_A            ALIF_PINMUX(0, 6, 1)
#define PIN_P0_6__UART1_CTS_A           ALIF_PINMUX(0, 6, 2)
#define PIN_P0_6__PDM_D1_A              ALIF_PINMUX(0, 6, 3)
#define PIN_P0_6__I2C2_SCL_A            ALIF_PINMUX(0, 6, 4)
#define PIN_P0_6__UT3_T0_A              ALIF_PINMUX(0, 6, 5)
#define PIN_P0_6__CAN_STBY_B            ALIF_PINMUX(0, 6, 6)
#define PIN_P0_6__ANA_S6                ALIF_PINMUX(0, 6, 7)

#define PIN_P0_7__GPIO                  ALIF_PINMUX(0, 7, 0)
#define PIN_P0_7__OSPI0_D7_A            ALIF_PINMUX(0, 7, 1)
#define PIN_P0_7__UART1_RTS_A           ALIF_PINMUX(0, 7, 2)
#define PIN_P0_7__PDM_C1_A              ALIF_PINMUX(0, 7, 3)
#define PIN_P0_7__I2C2_SDA_A            ALIF_PINMUX(0, 7, 4)
#define PIN_P0_7__UT3_T1_A              ALIF_PINMUX(0, 7, 5)
#define PIN_P0_7__CDC_DE_B              ALIF_PINMUX(0, 7, 6)
#define PIN_P0_7__ANA_S7                ALIF_PINMUX(0, 7, 7)



#define PIN_P1_0__GPIO                  ALIF_PINMUX(1, 0, 0)
#define PIN_P1_0__UART2_RX_A            ALIF_PINMUX(1, 0, 1)
#define PIN_P1_0__SPI0_MISO_A           ALIF_PINMUX(1, 0, 2)
#define PIN_P1_0__I2C3_SDA_A            ALIF_PINMUX(1, 0, 3)
#define PIN_P1_0__UT4_T0_A              ALIF_PINMUX(1, 0, 4)
#define PIN_P1_0__LPCAM_HSYNC_C         ALIF_PINMUX(1, 0, 5)
#define PIN_P1_0__ETH_RXD0_C            ALIF_PINMUX(1, 0, 6)
#define PIN_P1_0__ANA_S8                ALIF_PINMUX(1, 0, 7)

#define PIN_P1_1__GPIO                  ALIF_PINMUX(1, 1, 0)
#define PIN_P1_1__UART2_TX_A            ALIF_PINMUX(1, 1, 1)
#define PIN_P1_1__SPI0_MOSI_A           ALIF_PINMUX(1, 1, 2)
#define PIN_P1_1__I2C3_SCL_A            ALIF_PINMUX(1, 1, 3)
#define PIN_P1_1__UT4_T1_A              ALIF_PINMUX(1, 1, 4)
#define PIN_P1_1__LPCAM_VSYNC_C         ALIF_PINMUX(1, 1, 5)
#define PIN_P1_1__ETH_RXD1_C            ALIF_PINMUX(1, 1, 6)
#define PIN_P1_1__ANA_S9                ALIF_PINMUX(1, 1, 7)

#define PIN_P1_2__GPIO                  ALIF_PINMUX(1, 2, 0)
#define PIN_P1_2__UART3_RX_A            ALIF_PINMUX(1, 2, 1)
#define PIN_P1_2__SPI0_SCLK_A           ALIF_PINMUX(1, 2, 2)
#define PIN_P1_2__I3C_SDA_B             ALIF_PINMUX(1, 2, 3)
#define PIN_P1_2__UT5_T0_A              ALIF_PINMUX(1, 2, 4)
#define PIN_P1_2__LPCAM_PCLK_C          ALIF_PINMUX(1, 2, 5)
#define PIN_P1_2__ETH_RST_C             ALIF_PINMUX(1, 2, 6)
#define PIN_P1_2__ANA_S10               ALIF_PINMUX(1, 2, 7)

#define PIN_P1_3__GPIO                  ALIF_PINMUX(1, 3, 0)
#define PIN_P1_3__UART3_TX_A            ALIF_PINMUX(1, 3, 1)
#define PIN_P1_3__SPI0_SS0_A            ALIF_PINMUX(1, 3, 2)
#define PIN_P1_3__I3C_SCL_B             ALIF_PINMUX(1, 3, 3)
#define PIN_P1_3__UT5_T1_A              ALIF_PINMUX(1, 3, 4)
#define PIN_P1_3__LPCAM_XVCLK_C         ALIF_PINMUX(1, 3, 5)
#define PIN_P1_3__ETH_TXD0_C            ALIF_PINMUX(1, 3, 6)
#define PIN_P1_3__ANA_S11               ALIF_PINMUX(1, 3, 7)

#define PIN_P1_4__GPIO                  ALIF_PINMUX(1, 4, 0)
#define PIN_P1_4__OSPI0_SS0_A           ALIF_PINMUX(1, 4, 1)
#define PIN_P1_4__UART0_RX_B            ALIF_PINMUX(1, 4, 2)
#define PIN_P1_4__SPI0_SS1_A            ALIF_PINMUX(1, 4, 3)
#define PIN_P1_4__UT6_T0_A              ALIF_PINMUX(1, 4, 4)
#define PIN_P1_4__LPCAM_D0_C            ALIF_PINMUX(1, 4, 5)
#define PIN_P1_4__ETH_TXD1_C            ALIF_PINMUX(1, 4, 6)
#define PIN_P1_4__ANA_S12               ALIF_PINMUX(1, 4, 7)

#define PIN_P1_5__GPIO                  ALIF_PINMUX(1, 5, 0)
#define PIN_P1_5__OSPI0_SS1_A           ALIF_PINMUX(1, 5, 1)
#define PIN_P1_5__UART0_TX_B            ALIF_PINMUX(1, 5, 2)
#define PIN_P1_5__SPI0_SS2_A            ALIF_PINMUX(1, 5, 3)
#define PIN_P1_5__UT6_T1_A              ALIF_PINMUX(1, 5, 4)
#define PIN_P1_5__LPCAM_D1_C            ALIF_PINMUX(1, 5, 5)
#define PIN_P1_5__ETH_TXEN_C            ALIF_PINMUX(1, 5, 6)
#define PIN_P1_5__ANA_S13               ALIF_PINMUX(1, 5, 7)

#define PIN_P1_6__GPIO                  ALIF_PINMUX(1, 6, 0)
#define PIN_P1_6__OSPI0_RXDS_B          ALIF_PINMUX(1, 6, 1)
#define PIN_P1_6__UART1_RX_B            ALIF_PINMUX(1, 6, 2)
#define PIN_P1_6__I2S0_SDI_A            ALIF_PINMUX(1, 6, 3)
#define PIN_P1_6__UT7_T0_A              ALIF_PINMUX(1, 6, 4)
#define PIN_P1_6__LPCAM_D2_C            ALIF_PINMUX(1, 6, 5)
#define PIN_P1_6__ETH_IRQ_C             ALIF_PINMUX(1, 6, 6)
#define PIN_P1_6__ANA_S14               ALIF_PINMUX(1, 6, 7)

#define PIN_P1_7__GPIO                  ALIF_PINMUX(1, 7, 0)
#define PIN_P1_7__OSPI0_SCLK_A          ALIF_PINMUX(1, 7, 1)
#define PIN_P1_7__UART1_TX_B            ALIF_PINMUX(1, 7, 2)
#define PIN_P1_7__I2S0_SDO_A            ALIF_PINMUX(1, 7, 3)
#define PIN_P1_7__UT7_T1_A              ALIF_PINMUX(1, 7, 4)
#define PIN_P1_7__LPCAM_D3_C            ALIF_PINMUX(1, 7, 5)
#define PIN_P1_7__ETH_REFCLK_C          ALIF_PINMUX(1, 7, 6)
#define PIN_P1_7__ANA_S15               ALIF_PINMUX(1, 7, 7)



#define PIN_P2_0__GPIO                  ALIF_PINMUX(2, 0, 0)
#define PIN_P2_0__OSPI0_D0_B            ALIF_PINMUX(2, 0, 1)
#define PIN_P2_0__UART2_RX_B            ALIF_PINMUX(2, 0, 2)
#define PIN_P2_0__LPPDM_DO_A            ALIF_PINMUX(2, 0, 3)
#define PIN_P2_0__UT8_T0_A              ALIF_PINMUX(2, 0, 4)
#define PIN_P2_0__LPCAM_D4_C            ALIF_PINMUX(2, 0, 5)
#define PIN_P2_0__ETH_MDIO_C            ALIF_PINMUX(2, 0, 6)
#define PIN_P2_0__ANA_S16               ALIF_PINMUX(2, 0, 7)

#define PIN_P2_1__GPIO                  ALIF_PINMUX(2, 1, 0)
#define PIN_P2_1__OSPI0_D1_B            ALIF_PINMUX(2, 1, 1)
#define PIN_P2_1__UART2_TX_B            ALIF_PINMUX(2, 1, 2)
#define PIN_P2_1__LPPDM_CO_A            ALIF_PINMUX(2, 1, 3)
#define PIN_P2_1__UT8_T1_A              ALIF_PINMUX(2, 1, 4)
#define PIN_P2_1__LPCAM_D5_C            ALIF_PINMUX(2, 1, 5)
#define PIN_P2_1__ETH_MDC_C             ALIF_PINMUX(2, 1, 6)
#define PIN_P2_1__ANA_S17               ALIF_PINMUX(2, 1, 7)

#define PIN_P2_2__GPIO                  ALIF_PINMUX(2, 2, 0)
#define PIN_P2_2__OSPI0_D2_B            ALIF_PINMUX(2, 2, 1)
#define PIN_P2_2__UART3_RX_B            ALIF_PINMUX(2, 2, 2)
#define PIN_P2_2__LPPDM_D1_A            ALIF_PINMUX(2, 2, 3)
#define PIN_P2_2__UT9_T0_A              ALIF_PINMUX(2, 2, 4)
#define PIN_P2_2__LPCAM_D6_C            ALIF_PINMUX(2, 2, 5)
#define PIN_P2_2__ETH_CRS_DV_C          ALIF_PINMUX(2, 2, 6)
#define PIN_P2_2__ANA_S18               ALIF_PINMUX(2, 2, 7)

#define PIN_P2_3__GPIO                  ALIF_PINMUX(2, 3, 0)
#define PIN_P2_3__OSPI0_D3_B            ALIF_PINMUX(2, 3, 1)
#define PIN_P2_3__UART3_TX_B            ALIF_PINMUX(2, 3, 2)
#define PIN_P2_3__LPPDM_C1_A            ALIF_PINMUX(2, 3, 3)
#define PIN_P2_3__UT9_T1_A              ALIF_PINMUX(2, 3, 4)
#define PIN_P2_3__LPCAM_D7_C            ALIF_PINMUX(2, 3, 5)
#define PIN_P2_3__CDC_PCLK_B            ALIF_PINMUX(2, 3, 6)
#define PIN_P2_3__ANA_S19               ALIF_PINMUX(2, 3, 7)

#define PIN_P2_4__GPIO                  ALIF_PINMUX(2, 4, 0)
#define PIN_P2_4__OSPI0_D4_B            ALIF_PINMUX(2, 4, 1)
#define PIN_P2_4__LPI2S_SDI_A           ALIF_PINMUX(2, 4, 2)
#define PIN_P2_4__SPI1_MISO_A           ALIF_PINMUX(2, 4, 3)
#define PIN_P2_4__UT10_T0_A             ALIF_PINMUX(2, 4, 4)
#define PIN_P2_4__LPCAM_D0_B            ALIF_PINMUX(2, 4, 5)
#define PIN_P2_4__CAM_D0_A              ALIF_PINMUX(2, 4, 6)
#define PIN_P2_4__ANA_S20               ALIF_PINMUX(2, 4, 7)

#define PIN_P2_5__GPIO                  ALIF_PINMUX(2, 5, 0)
#define PIN_P2_5__OSPI0_D5_B            ALIF_PINMUX(2, 5, 1)
#define PIN_P2_5__LPI2S_SDO_A           ALIF_PINMUX(2, 5, 2)
#define PIN_P2_5__SPI1_MOSI_A           ALIF_PINMUX(2, 5, 3)
#define PIN_P2_5__UT10_T1_A             ALIF_PINMUX(2, 5, 4)
#define PIN_P2_5__LPCAM_D1_B            ALIF_PINMUX(2, 5, 5)
#define PIN_P2_5__CAM_D1_A              ALIF_PINMUX(2, 5, 6)
#define PIN_P2_5__ANA_S21               ALIF_PINMUX(2, 5, 7)

#define PIN_P2_6__GPIO                  ALIF_PINMUX(2, 6, 0)
#define PIN_P2_6__OSPI0_D6_B            ALIF_PINMUX(2, 6, 1)
#define PIN_P2_6__LPI2S_SCLK_A          ALIF_PINMUX(2, 6, 2)
#define PIN_P2_6__SPI1_SCLK_A           ALIF_PINMUX(2, 6, 3)
#define PIN_P2_6__UT11_T0_A             ALIF_PINMUX(2, 6, 4)
#define PIN_P2_6__LPCAM_D2_B            ALIF_PINMUX(2, 6, 5)
#define PIN_P2_6__CAM_D2_A              ALIF_PINMUX(2, 6, 6)
#define PIN_P2_6__ANA_S22               ALIF_PINMUX(2, 6, 7)

#define PIN_P2_7__GPIO                  ALIF_PINMUX(2, 7, 0)
#define PIN_P2_7__OSPI0_D7_B            ALIF_PINMUX(2, 7, 1)
#define PIN_P2_7__LPI2S_WS_A            ALIF_PINMUX(2, 7, 2)
#define PIN_P2_7__SPI1_SS0_A            ALIF_PINMUX(2, 7, 3)
#define PIN_P2_7__UT11_T1_A             ALIF_PINMUX(2, 7, 4)
#define PIN_P2_7__LPCAM_D3_B            ALIF_PINMUX(2, 7, 5)
#define PIN_P2_7__CAM_D3_A              ALIF_PINMUX(2, 7, 6)
#define PIN_P2_7__ANA_S23               ALIF_PINMUX(2, 7, 7)



#define PIN_P3_0__GPIO                  ALIF_PINMUX(3, 0, 0)
#define PIN_P3_0__OSPI0_SCLK_B          ALIF_PINMUX(3, 0, 1)
#define PIN_P3_0__UART4_RX_A            ALIF_PINMUX(3, 0, 2)
#define PIN_P3_0__PDM_D0_B              ALIF_PINMUX(3, 0, 3)
#define PIN_P3_0__I2S0_SCLK_A           ALIF_PINMUX(3, 0, 4)
#define PIN_P3_0__QEC0_X_A              ALIF_PINMUX(3, 0, 5)
#define PIN_P3_0__LPCAM_D4_B            ALIF_PINMUX(3, 0, 6)
#define PIN_P3_0__CAM_D4_A              ALIF_PINMUX(3, 0, 7)

#define PIN_P3_1__GPIO                  ALIF_PINMUX(3, 1, 0)
#define PIN_P3_1__OSPI0_SCLKN_B         ALIF_PINMUX(3, 1, 1)
#define PIN_P3_1__UART4_TX_A            ALIF_PINMUX(3, 1, 2)
#define PIN_P3_1__PDM_C0_B              ALIF_PINMUX(3, 1, 3)
#define PIN_P3_1__I2S0_WS_A             ALIF_PINMUX(3, 1, 4)
#define PIN_P3_1__QEC0_Y_A              ALIF_PINMUX(3, 1, 5)
#define PIN_P3_1__LPCAM_D5_B            ALIF_PINMUX(3, 1, 6)
#define PIN_P3_1__CAM_D5_A              ALIF_PINMUX(3, 1, 7)

#define PIN_P3_2__GPIO                  ALIF_PINMUX(3, 2, 0)
#define PIN_P3_2__OSPI0_SS0_B           ALIF_PINMUX(3, 2, 1)
#define PIN_P3_2__PDM_D1_B              ALIF_PINMUX(3, 2, 2)
#define PIN_P3_2__I2S1_SDI_A            ALIF_PINMUX(3, 2, 3)
#define PIN_P3_2__I3C_SDA_C             ALIF_PINMUX(3, 2, 4)
#define PIN_P3_2__QEC0_Z_A              ALIF_PINMUX(3, 2, 5)
#define PIN_P3_2__LPCAM_D6_B            ALIF_PINMUX(3, 2, 6)
#define PIN_P3_2__CAM_D6_A              ALIF_PINMUX(3, 2, 7)

#define PIN_P3_3__GPIO                  ALIF_PINMUX(3, 3, 0)
#define PIN_P3_3__OSPI0_SS1_B           ALIF_PINMUX(3, 3, 1)
#define PIN_P3_3__PDM_C1_B              ALIF_PINMUX(3, 3, 2)
#define PIN_P3_3__I2S1_SDO_A            ALIF_PINMUX(3, 3, 3)
#define PIN_P3_3__I3C_SCL_C             ALIF_PINMUX(3, 3, 4)
#define PIN_P3_3__QEC1_X_A              ALIF_PINMUX(3, 3, 5)
#define PIN_P3_3__LPCAM_D7_B            ALIF_PINMUX(3, 3, 6)
#define PIN_P3_3__CAM_D7_A              ALIF_PINMUX(3, 3, 7)

#define PIN_P3_4__GPIO                  ALIF_PINMUX(3, 4, 0)
#define PIN_P3_4__OSPI0_RXDS_B          ALIF_PINMUX(3, 4, 1)
#define PIN_P3_4__UART5_RX_A            ALIF_PINMUX(3, 4, 2)
#define PIN_P3_4__LPPDM_CO_B            ALIF_PINMUX(3, 4, 3)
#define PIN_P3_4__I2S1_SCLK_A           ALIF_PINMUX(3, 4, 4)
#define PIN_P3_4__I2C0_SCL_B            ALIF_PINMUX(3, 4, 5)
#define PIN_P3_4__QEC1_Y_A              ALIF_PINMUX(3, 4, 6)
#define PIN_P3_4__CAM_D8_A              ALIF_PINMUX(3, 4, 7)

#define PIN_P3_5__GPIO                  ALIF_PINMUX(3, 5, 0)
#define PIN_P3_5__OSPI0_SCLKN_A         ALIF_PINMUX(3, 5, 1)
#define PIN_P3_5__UART5_TX_A            ALIF_PINMUX(3, 5, 2)
#define PIN_P3_5__LPPDM_DO_B            ALIF_PINMUX(3, 5, 3)
#define PIN_P3_5__SPI0_SS1_B            ALIF_PINMUX(3, 5, 4)
#define PIN_P3_5__I2C0_SDA_B            ALIF_PINMUX(3, 5, 5)
#define PIN_P3_5__QEC1_Z_A              ALIF_PINMUX(3, 5, 6)
#define PIN_P3_5__CAM_D9_A              ALIF_PINMUX(3, 5, 7)

#define PIN_P3_6__GPIO                  ALIF_PINMUX(3, 6, 0)
#define PIN_P3_6__HFXO_OUT_A            ALIF_PINMUX(3, 6, 1)
#define PIN_P3_6__LPUART_CTS_B          ALIF_PINMUX(3, 6, 2)
#define PIN_P3_6__LPPDM_C1_B            ALIF_PINMUX(3, 6, 3)
#define PIN_P3_6__SPI0_SS2_B            ALIF_PINMUX(3, 6, 4)
#define PIN_P3_6__I2C1_SDA_B            ALIF_PINMUX(3, 6, 5)
#define PIN_P3_6__QEC2_X_A              ALIF_PINMUX(3, 6, 6)
#define PIN_P3_6__CAM_D10_A             ALIF_PINMUX(3, 6, 7)

#define PIN_P3_7__GPIO                  ALIF_PINMUX(3, 7, 0)
#define PIN_P3_7__JTAG0_TRACECLK        ALIF_PINMUX(3, 7, 1)
#define PIN_P3_7__LPUART_RTS_B          ALIF_PINMUX(3, 7, 2)
#define PIN_P3_7__LPPDM_D1_B            ALIF_PINMUX(3, 7, 3)
#define PIN_P3_7__SPI1_SS1_A            ALIF_PINMUX(3, 7, 4)
#define PIN_P3_7__I2C1_SCL_B            ALIF_PINMUX(3, 7, 5)
#define PIN_P3_7__QEC2_Y_A              ALIF_PINMUX(3, 7, 6)
#define PIN_P3_7__CAM_D11_A             ALIF_PINMUX(3, 7, 7)



#define PIN_P4_0__GPIO                  ALIF_PINMUX(4, 0, 0)
#define PIN_P4_0__JTAG0_TDATA0          ALIF_PINMUX(4, 0, 1)
#define PIN_P4_0__APLL_OUT_A            ALIF_PINMUX(4, 0, 2)
#define PIN_P4_0__I2S1_WS_A             ALIF_PINMUX(4, 0, 3)
#define PIN_P4_0__SPI1_SS2_A            ALIF_PINMUX(4, 0, 4)
#define PIN_P4_0__QEC2_Z_A              ALIF_PINMUX(4, 0, 5)
#define PIN_P4_0__CDC_VSYNC_B           ALIF_PINMUX(4, 0, 6)
#define PIN_P4_0__CAM_D12_A             ALIF_PINMUX(4, 0, 7)

#define PIN_P4_1__GPIO                  ALIF_PINMUX(4, 1, 0)
#define PIN_P4_1__JTAG0_TDATA1          ALIF_PINMUX(4, 1, 1)
#define PIN_P4_1__I2S0_SDI_B            ALIF_PINMUX(4, 1, 2)
#define PIN_P4_1__SPI1_SS3_A            ALIF_PINMUX(4, 1, 3)
#define PIN_P4_1__QEC3_X_A              ALIF_PINMUX(4, 1, 4)
#define PIN_P4_1__SD_CLK_D              ALIF_PINMUX(4, 1, 5)
#define PIN_P4_1__CDC_HSYNC_B           ALIF_PINMUX(4, 1, 6)
#define PIN_P4_1__CAM_D13_A             ALIF_PINMUX(4, 1, 7)

#define PIN_P4_2__GPIO                  ALIF_PINMUX(4, 2, 0)
#define PIN_P4_2__JTAG0_TDATA2          ALIF_PINMUX(4, 2, 1)
#define PIN_P4_2__LPI2C1_SDA_A          ALIF_PINMUX(4, 2, 2)
#define PIN_P4_2__I2S0_SDO_B            ALIF_PINMUX(4, 2, 3)
#define PIN_P4_2__SPI2_MISO_A           ALIF_PINMUX(4, 2, 4)
#define PIN_P4_2__QEC3_Y_A              ALIF_PINMUX(4, 2, 5)
#define PIN_P4_2__SD_CMD_D              ALIF_PINMUX(4, 2, 6)
#define PIN_P4_2__CAM_D14_A             ALIF_PINMUX(4, 2, 7)

#define PIN_P4_3__GPIO                  ALIF_PINMUX(4, 3, 0)
#define PIN_P4_3__JTAG0_TDATA3          ALIF_PINMUX(4, 3, 1)
#define PIN_P4_3__LPI2C1_SCL_A          ALIF_PINMUX(4, 3, 2)
#define PIN_P4_3__I2S0_SCLK_B           ALIF_PINMUX(4, 3, 3)
#define PIN_P4_3__SPI2_MOSI_A           ALIF_PINMUX(4, 3, 4)
#define PIN_P4_3__QEC3_Z_A              ALIF_PINMUX(4, 3, 5)
#define PIN_P4_3__SD_RST_D              ALIF_PINMUX(4, 3, 6)
#define PIN_P4_3__CAM_D15_A             ALIF_PINMUX(4, 3, 7)

#define PIN_P4_4__GPIO                  ALIF_PINMUX(4, 4, 0)
#define PIN_P4_4__JTAG0_TCK             ALIF_PINMUX(4, 4, 1)
#define PIN_P4_4__I2S0_WS_B             ALIF_PINMUX(4, 4, 2)
#define PIN_P4_4__SPI2_SCLK_A           ALIF_PINMUX(4, 4, 3)
#define PIN_P4_4__FAULT0_A              ALIF_PINMUX(4, 4, 4)

#define PIN_P4_5__GPIO                  ALIF_PINMUX(4, 5, 0)
#define PIN_P4_5__JTAG0_TMS             ALIF_PINMUX(4, 5, 1)
#define PIN_P4_5__SPI2_SS0_A            ALIF_PINMUX(4, 5, 2)
#define PIN_P4_5__FAULT1_A              ALIF_PINMUX(4, 5, 3)

#define PIN_P4_6__GPIO                  ALIF_PINMUX(4, 6, 0)
#define PIN_P4_6__JTAG0_TDI             ALIF_PINMUX(4, 6, 1)
#define PIN_P4_6__SPI2_SS1_A            ALIF_PINMUX(4, 6, 2)
#define PIN_P4_6__FAULT2_A              ALIF_PINMUX(4, 6, 3)

#define PIN_P4_7__GPIO                  ALIF_PINMUX(4, 7, 0)
#define PIN_P4_7__JTAG0_TDO             ALIF_PINMUX(4, 7, 1)
#define PIN_P4_7__SPI2_SS2_A            ALIF_PINMUX(4, 7, 2)
#define PIN_P4_7__FAULT3_A              ALIF_PINMUX(4, 7, 3)



#define PIN_P5_0__GPIO                  ALIF_PINMUX(5, 0, 0)
#define PIN_P5_0__OSPI1_RXDS_A          ALIF_PINMUX(5, 0, 1)
#define PIN_P5_0__UART4_RX_C            ALIF_PINMUX(5, 0, 2)
#define PIN_P5_0__PDM_D2_A              ALIF_PINMUX(5, 0, 3)
#define PIN_P5_0__SPI0_MISO_B           ALIF_PINMUX(5, 0, 4)
#define PIN_P5_0__I2C2_SDA_B            ALIF_PINMUX(5, 0, 5)
#define PIN_P5_0__UT0_T0_B              ALIF_PINMUX(5, 0, 6)
#define PIN_P5_0__SD_D0_A               ALIF_PINMUX(5, 0, 7)

#define PIN_P5_1__GPIO                  ALIF_PINMUX(5, 1, 0)
#define PIN_P5_1__OSPI1_SS0_A           ALIF_PINMUX(5, 1, 1)
#define PIN_P5_1__UART4_TX_C            ALIF_PINMUX(5, 1, 2)
#define PIN_P5_1__PDM_D3_A              ALIF_PINMUX(5, 1, 3)
#define PIN_P5_1__SPI0_MOSI_B           ALIF_PINMUX(5, 1, 4)
#define PIN_P5_1__I2C2_SCL_B            ALIF_PINMUX(5, 1, 5)
#define PIN_P5_1__UT0_T1_B              ALIF_PINMUX(5, 1, 6)
#define PIN_P5_1__SD_D1_A               ALIF_PINMUX(5, 1, 7)

#define PIN_P5_2__GPIO                  ALIF_PINMUX(5, 2, 0)
#define PIN_P5_2__OSPI1_SCLKN_A         ALIF_PINMUX(5, 2, 1)
#define PIN_P5_2__UART5_RX_C            ALIF_PINMUX(5, 2, 2)
#define PIN_P5_2__PDM_C3_A              ALIF_PINMUX(5, 2, 3)
#define PIN_P5_2__SPI0_SS0_B            ALIF_PINMUX(5, 2, 4)
#define PIN_P5_2__LPI2C0_SCL_B          ALIF_PINMUX(5, 2, 5)
#define PIN_P5_2__UT1_T0_B              ALIF_PINMUX(5, 2, 6)
#define PIN_P5_2__SD_D2_A               ALIF_PINMUX(5, 2, 7)

#define PIN_P5_3__GPIO                  ALIF_PINMUX(5, 3, 0)
#define PIN_P5_3__OSPI1_SCLK_A          ALIF_PINMUX(5, 3, 1)
#define PIN_P5_3__UART5_TX_C            ALIF_PINMUX(5, 3, 2)
#define PIN_P5_3__SPI0_SCLK_B           ALIF_PINMUX(5, 3, 3)
#define PIN_P5_3__LPI2C0_SDA_B          ALIF_PINMUX(5, 3, 4)
#define PIN_P5_3__UT1_T1_B              ALIF_PINMUX(5, 3, 5)
#define PIN_P5_3__SD_D3_A               ALIF_PINMUX(5, 3, 6)
#define PIN_P5_3__CDC_PCLK_A            ALIF_PINMUX(5, 3, 7)

#define PIN_P5_4__GPIO                  ALIF_PINMUX(5, 4, 0)
#define PIN_P5_4__OSPI1_SS1_A           ALIF_PINMUX(5, 4, 1)
#define PIN_P5_4__UART3_CTS_A           ALIF_PINMUX(5, 4, 2)
#define PIN_P5_4__PDM_D2_B              ALIF_PINMUX(5, 4, 3)
#define PIN_P5_4__SPI0_SS3_A            ALIF_PINMUX(5, 4, 4)
#define PIN_P5_4__UT2_T0_B              ALIF_PINMUX(5, 4, 5)
#define PIN_P5_4__SD_D4_A               ALIF_PINMUX(5, 4, 6)
#define PIN_P5_4__CDC_DE_A              ALIF_PINMUX(5, 4, 7)

#define PIN_P5_5__GPIO                  ALIF_PINMUX(5, 5, 0)
#define PIN_P5_5__OSPI1_SCLK_C          ALIF_PINMUX(5, 5, 1)
#define PIN_P5_5__UART3_RTS_A           ALIF_PINMUX(5, 5, 2)
#define PIN_P5_5__PDM_D3_B              ALIF_PINMUX(5, 5, 3)
#define PIN_P5_5__UT2_T1_B              ALIF_PINMUX(5, 5, 4)
#define PIN_P5_5__SD_D5_A               ALIF_PINMUX(5, 5, 5)
#define PIN_P5_5__ETH_RXD0_A            ALIF_PINMUX(5, 5, 6)
#define PIN_P5_5__CDC_HSYNC_A           ALIF_PINMUX(5, 5, 7)

#define PIN_P5_6__GPIO                  ALIF_PINMUX(5, 6, 0)
#define PIN_P5_6__UART1_CTS_B           ALIF_PINMUX(5, 6, 1)
#define PIN_P5_6__I2C2_SCL_C            ALIF_PINMUX(5, 6, 2)
#define PIN_P5_6__UT3_T0_B              ALIF_PINMUX(5, 6, 3)
#define PIN_P5_6__SD_D6_A               ALIF_PINMUX(5, 6, 4)
#define PIN_P5_6__ETH_RXD1_A            ALIF_PINMUX(5, 6, 5)
#define PIN_P5_6__CDC_VSYNC_A           ALIF_PINMUX(5, 6, 6)

#define PIN_P5_7__GPIO                  ALIF_PINMUX(5, 7, 0)
#define PIN_P5_7__OSPI1_SS0_C           ALIF_PINMUX(5, 7, 1)
#define PIN_P5_7__UART1_RTS_B           ALIF_PINMUX(5, 7, 2)
#define PIN_P5_7__I2C2_SDA_C            ALIF_PINMUX(5, 7, 3)
#define PIN_P5_7__UT3_T1_B              ALIF_PINMUX(5, 7, 4)
#define PIN_P5_7__SD_D7_A               ALIF_PINMUX(5, 7, 5)
#define PIN_P5_7__ETH_RST_A             ALIF_PINMUX(5, 7, 6)



#define PIN_P6_0__GPIO                  ALIF_PINMUX(6, 0, 0)
#define PIN_P6_0__OSPI0_D0_C            ALIF_PINMUX(6, 0, 1)
#define PIN_P6_0__UART4_DE_A            ALIF_PINMUX(6, 0, 2)
#define PIN_P6_0__PDM_D0_C              ALIF_PINMUX(6, 0, 3)
#define PIN_P6_0__UT4_T0_B              ALIF_PINMUX(6, 0, 4)
#define PIN_P6_0__SD_D0_D               ALIF_PINMUX(6, 0, 5)
#define PIN_P6_0__ETH_TXD0_A            ALIF_PINMUX(6, 0, 6)
#define PIN_P6_0__LPSPI_SS1_A           ALIF_PINMUX(6, 0, 7)

#define PIN_P6_1__GPIO                  ALIF_PINMUX(6, 1, 0)
#define PIN_P6_1__OSPI0_D1_C            ALIF_PINMUX(6, 1, 1)
#define PIN_P6_1__UART5_DE_A            ALIF_PINMUX(6, 1, 2)
#define PIN_P6_1__PDM_C0_C              ALIF_PINMUX(6, 1, 3)
#define PIN_P6_1__UT4_T1_B              ALIF_PINMUX(6, 1, 4)
#define PIN_P6_1__SD_D1_D               ALIF_PINMUX(6, 1, 5)
#define PIN_P6_1__ETH_TXD1_A            ALIF_PINMUX(6, 1, 6)
#define PIN_P6_1__LPSPI_SS2_A           ALIF_PINMUX(6, 1, 7)

#define PIN_P6_2__GPIO                  ALIF_PINMUX(6, 2, 0)
#define PIN_P6_2__OSPI0_D2_C            ALIF_PINMUX(6, 2, 1)
#define PIN_P6_2__UART2_CTS_A           ALIF_PINMUX(6, 2, 2)
#define PIN_P6_2__LPI3C_SDA_A           ALIF_PINMUX(6, 2, 3)
#define PIN_P6_2__PDM_D1_C              ALIF_PINMUX(6, 2, 4)
#define PIN_P6_2__UT5_T0_B              ALIF_PINMUX(6, 2, 5)
#define PIN_P6_2__SD_D2_D               ALIF_PINMUX(6, 2, 6)
#define PIN_P6_2__ETH_TXEN_A            ALIF_PINMUX(6, 2, 7)

#define PIN_P6_3__GPIO                  ALIF_PINMUX(6, 3, 0)
#define PIN_P6_3__OSPI0_D3_C            ALIF_PINMUX(6, 3, 1)
#define PIN_P6_3__UART2_RTS_A           ALIF_PINMUX(6, 3, 2)
#define PIN_P6_3__LPI3C_SCL_A           ALIF_PINMUX(6, 3, 3)
#define PIN_P6_3__PDM_C1_C              ALIF_PINMUX(6, 3, 4)
#define PIN_P6_3__UT5_T1_B              ALIF_PINMUX(6, 3, 5)
#define PIN_P6_3__SD_D3_D               ALIF_PINMUX(6, 3, 6)
#define PIN_P6_3__ETH_IRQ_A             ALIF_PINMUX(6, 3, 7)

#define PIN_P6_4__GPIO                  ALIF_PINMUX(6, 4, 0)
#define PIN_P6_4__OSPI0_D4_C            ALIF_PINMUX(6, 4, 1)
#define PIN_P6_4__UART2_CTS_B           ALIF_PINMUX(6, 4, 2)
#define PIN_P6_4__LRFC_OUT_A            ALIF_PINMUX(6, 4, 3)
#define PIN_P6_4__SPI1_SS0_B            ALIF_PINMUX(6, 4, 4)
#define PIN_P6_4__UT6_T0_B              ALIF_PINMUX(6, 4, 5)
#define PIN_P6_4__SD_D4_D               ALIF_PINMUX(6, 4, 6)
#define PIN_P6_4__ETH_REFCLK_A          ALIF_PINMUX(6, 4, 7)

#define PIN_P6_5__GPIO                  ALIF_PINMUX(6, 5, 0)
#define PIN_P6_5__OSPI0_D5_C            ALIF_PINMUX(6, 5, 1)
#define PIN_P6_5__UART2_RTS_B           ALIF_PINMUX(6, 5, 2)
#define PIN_P6_5__LPI2C1_SDA_B          ALIF_PINMUX(6, 5, 3)
#define PIN_P6_5__SPI1_SS1_B            ALIF_PINMUX(6, 5, 4)
#define PIN_P6_5__UT6_T1_B              ALIF_PINMUX(6, 5, 5)
#define PIN_P6_5__SD_D5_D               ALIF_PINMUX(6, 5, 6)
#define PIN_P6_5__ETH_MDIO_A            ALIF_PINMUX(6, 5, 7)

#define PIN_P6_6__GPIO                  ALIF_PINMUX(6, 6, 0)
#define PIN_P6_6__OSPI0_D6_C            ALIF_PINMUX(6, 6, 1)
#define PIN_P6_6__UART0_CTS_B           ALIF_PINMUX(6, 6, 2)
#define PIN_P6_6__LPI2C1_SCL_B          ALIF_PINMUX(6, 6, 3)
#define PIN_P6_6__SPI1_SS2_B            ALIF_PINMUX(6, 6, 4)
#define PIN_P6_6__UT7_T0_B              ALIF_PINMUX(6, 6, 5)
#define PIN_P6_6__SD_D6_D               ALIF_PINMUX(6, 6, 6)
#define PIN_P6_6__ETH_MDC_A             ALIF_PINMUX(6, 6, 7)

#define PIN_P6_7__GPIO                  ALIF_PINMUX(6, 7, 0)
#define PIN_P6_7__OSPI0_D7_C            ALIF_PINMUX(6, 7, 1)
#define PIN_P6_7__UART0_RTS_B           ALIF_PINMUX(6, 7, 2)
#define PIN_P6_7__PDM_C2_A              ALIF_PINMUX(6, 7, 3)
#define PIN_P6_7__SPI1_SS3_B            ALIF_PINMUX(6, 7, 4)
#define PIN_P6_7__UT7_T1_B              ALIF_PINMUX(6, 7, 5)
#define PIN_P6_7__SD_D7_D               ALIF_PINMUX(6, 7, 6)
#define PIN_P6_7__ETH_CRS_DV_A          ALIF_PINMUX(6, 7, 7)



#define PIN_P7_0__GPIO                  ALIF_PINMUX(7, 0, 0)
#define PIN_P7_0__LPUT0_T0_A            ALIF_PINMUX(7, 0, 1)
#define PIN_P7_0__CMP3_OUT_A            ALIF_PINMUX(7, 0, 2)
#define PIN_P7_0__SPI0_MISO_C           ALIF_PINMUX(7, 0, 3)
#define PIN_P7_0__I2C0_SDA_C            ALIF_PINMUX(7, 0, 4)
#define PIN_P7_0__UT8_T0_B              ALIF_PINMUX(7, 0, 5)
#define PIN_P7_0__SD_CMD_A              ALIF_PINMUX(7, 0, 6)
#define PIN_P7_0__CAN_RXD_A             ALIF_PINMUX(7, 0, 7)

#define PIN_P7_1__GPIO                  ALIF_PINMUX(7, 1, 0)
#define PIN_P7_1__LPUT0_T1_A            ALIF_PINMUX(7, 1, 1)
#define PIN_P7_1__CMP2_OUT_A            ALIF_PINMUX(7, 1, 2)
#define PIN_P7_1__SPI0_MOSI_C           ALIF_PINMUX(7, 1, 3)
#define PIN_P7_1__I2C0_SCL_C            ALIF_PINMUX(7, 1, 4)
#define PIN_P7_1__UT8_T1_B              ALIF_PINMUX(7, 1, 5)
#define PIN_P7_1__SD_CLK_A              ALIF_PINMUX(7, 1, 6)
#define PIN_P7_1__CAN_TXD_A             ALIF_PINMUX(7, 1, 7)

#define PIN_P7_2__GPIO                  ALIF_PINMUX(7, 2, 0)
#define PIN_P7_2__LPUT1_T0_A            ALIF_PINMUX(7, 2, 1)
#define PIN_P7_2__UART3_CTS_B           ALIF_PINMUX(7, 2, 2)
#define PIN_P7_2__CMP1_OUT_A            ALIF_PINMUX(7, 2, 3)
#define PIN_P7_2__SPI0_SCLK_C           ALIF_PINMUX(7, 2, 4)
#define PIN_P7_2__I2C1_SDA_C            ALIF_PINMUX(7, 2, 5)
#define PIN_P7_2__UT9_T0_B              ALIF_PINMUX(7, 2, 6)
#define PIN_P7_2__SD_RST_A              ALIF_PINMUX(7, 2, 7)

#define PIN_P7_3__GPIO                  ALIF_PINMUX(7, 3, 0)
#define PIN_P7_3__LPUT1_T1_A            ALIF_PINMUX(7, 3, 1)
#define PIN_P7_3__UART3_RTS_B           ALIF_PINMUX(7, 3, 2)
#define PIN_P7_3__CMP0_OUT_A            ALIF_PINMUX(7, 3, 3)
#define PIN_P7_3__SPI0_SS0_C            ALIF_PINMUX(7, 3, 4)
#define PIN_P7_3__I2C1_SCL_C            ALIF_PINMUX(7, 3, 5)
#define PIN_P7_3__UT9_T1_B              ALIF_PINMUX(7, 3, 6)
#define PIN_P7_3__CAN_STBY_A            ALIF_PINMUX(7, 3, 7)

#define PIN_P7_4__GPIO                  ALIF_PINMUX(7, 4, 0)
#define PIN_P7_4__LPUT2_T0_A            ALIF_PINMUX(7, 4, 1)
#define PIN_P7_4__LPUART_CTS_A          ALIF_PINMUX(7, 4, 2)
#define PIN_P7_4__LPPDM_C2_A            ALIF_PINMUX(7, 4, 3)
#define PIN_P7_4__LPSPI_MISO_A          ALIF_PINMUX(7, 4, 4)
#define PIN_P7_4__LPI2C0_SCL_A          ALIF_PINMUX(7, 4, 5)
#define PIN_P7_4__UT10_T0_B             ALIF_PINMUX(7, 4, 6)

#define PIN_P7_5__GPIO                  ALIF_PINMUX(7, 5, 0)
#define PIN_P7_5__LPUT2_T1_A            ALIF_PINMUX(7, 5, 1)
#define PIN_P7_5__LPUART_RTS_A          ALIF_PINMUX(7, 5, 2)
#define PIN_P7_5__LFXO_OUT_A            ALIF_PINMUX(7, 5, 3)
#define PIN_P7_5__LPPDM_D2_A            ALIF_PINMUX(7, 5, 4)
#define PIN_P7_5__LPSPI_MOSI_A          ALIF_PINMUX(7, 5, 5)
#define PIN_P7_5__LPI2C0_SDA_A          ALIF_PINMUX(7, 5, 6)
#define PIN_P7_5__UT10_T1_B             ALIF_PINMUX(7, 5, 7)

#define PIN_P7_6__GPIO                  ALIF_PINMUX(7, 6, 0)
#define PIN_P7_6__LPI2C1_SDA_C          ALIF_PINMUX(7, 6, 1)
#define PIN_P7_6__LPUART_RX_A           ALIF_PINMUX(7, 6, 2)
#define PIN_P7_6__LPI3C_SDA_B           ALIF_PINMUX(7, 6, 3)
#define PIN_P7_6__LPPDM_C3_A            ALIF_PINMUX(7, 6, 4)
#define PIN_P7_6__LPSPI_SCLK_A          ALIF_PINMUX(7, 6, 5)
#define PIN_P7_6__I3C_SDA_D             ALIF_PINMUX(7, 6, 6)
#define PIN_P7_6__UT11_T0_B             ALIF_PINMUX(7, 6, 7)

#define PIN_P7_7__GPIO                  ALIF_PINMUX(7, 7, 0)
#define PIN_P7_7__LPI2C1_SCL_C          ALIF_PINMUX(7, 7, 1)
#define PIN_P7_7__LPUART_TX_A           ALIF_PINMUX(7, 7, 2)
#define PIN_P7_7__LPI3C_SCL_B           ALIF_PINMUX(7, 7, 3)
#define PIN_P7_7__LPPDM_D3_A            ALIF_PINMUX(7, 7, 4)
#define PIN_P7_7__LPSPI_SS0_A           ALIF_PINMUX(7, 7, 5)
#define PIN_P7_7__I3C_SCL_D             ALIF_PINMUX(7, 7, 6)
#define PIN_P7_7__UT11_T1_B             ALIF_PINMUX(7, 7, 7)



#define PIN_P8_0__GPIO                  ALIF_PINMUX(8, 0, 0)
#define PIN_P8_0__OSPI1_SCLKN_C         ALIF_PINMUX(8, 0, 1)
#define PIN_P8_0__AUDIO_CLK_A           ALIF_PINMUX(8, 0, 2)
#define PIN_P8_0__FAULT0_B              ALIF_PINMUX(8, 0, 3)
#define PIN_P8_0__LPCAM_D0_A            ALIF_PINMUX(8, 0, 4)
#define PIN_P8_0__SD_D0_C               ALIF_PINMUX(8, 0, 5)
#define PIN_P8_0__CDC_D0_A              ALIF_PINMUX(8, 0, 6)
#define PIN_P8_0__CAM_D0_B              ALIF_PINMUX(8, 0, 7)

#define PIN_P8_1__GPIO                  ALIF_PINMUX(8, 1, 0)
#define PIN_P8_1__I2S2_SDI_A            ALIF_PINMUX(8, 1, 1)
#define PIN_P8_1__FAULT1_B              ALIF_PINMUX(8, 1, 2)
#define PIN_P8_1__LPCAM_D1_A            ALIF_PINMUX(8, 1, 3)
#define PIN_P8_1__SD_D1_C               ALIF_PINMUX(8, 1, 4)
#define PIN_P8_1__CDC_D1_A              ALIF_PINMUX(8, 1, 5)
#define PIN_P8_1__CAM_D1_B              ALIF_PINMUX(8, 1, 6)
#define PIN_P8_1__OSPI1_SS1_C           ALIF_PINMUX(8, 1, 7)

#define PIN_P8_2__GPIO                  ALIF_PINMUX(8, 2, 0)
#define PIN_P8_2__I2S2_SDO_A            ALIF_PINMUX(8, 2, 1)
#define PIN_P8_2__SPI0_SS3_B            ALIF_PINMUX(8, 2, 2)
#define PIN_P8_2__FAULT2_B              ALIF_PINMUX(8, 2, 3)
#define PIN_P8_2__LPCAM_D2_A            ALIF_PINMUX(8, 2, 4)
#define PIN_P8_2__SD_D2_C               ALIF_PINMUX(8, 2, 5)
#define PIN_P8_2__CDC_D2_A              ALIF_PINMUX(8, 2, 6)
#define PIN_P8_2__CAM_D2_B              ALIF_PINMUX(8, 2, 7)

#define PIN_P8_3__GPIO                  ALIF_PINMUX(8, 3, 0)
#define PIN_P8_3__I2S2_SCLK_A           ALIF_PINMUX(8, 3, 1)
#define PIN_P8_3__SPI1_MISO_B           ALIF_PINMUX(8, 3, 2)
#define PIN_P8_3__FAULT3_B              ALIF_PINMUX(8, 3, 3)
#define PIN_P8_3__LPCAM_D3_A            ALIF_PINMUX(8, 3, 4)
#define PIN_P8_3__SD_D3_C               ALIF_PINMUX(8, 3, 5)
#define PIN_P8_3__CDC_D3_A              ALIF_PINMUX(8, 3, 6)
#define PIN_P8_3__CAM_D3_B              ALIF_PINMUX(8, 3, 7)

#define PIN_P8_4__GPIO                  ALIF_PINMUX(8, 4, 0)
#define PIN_P8_4__I2S2_WS_A             ALIF_PINMUX(8, 4, 1)
#define PIN_P8_4__SPI1_MOSI_B           ALIF_PINMUX(8, 4, 2)
#define PIN_P8_4__QEC0_X_B              ALIF_PINMUX(8, 4, 3)
#define PIN_P8_4__LPCAM_D4_A            ALIF_PINMUX(8, 4, 4)
#define PIN_P8_4__SD_D4_C               ALIF_PINMUX(8, 4, 5)
#define PIN_P8_4__CDC_D4_A              ALIF_PINMUX(8, 4, 6)
#define PIN_P8_4__CAM_D4_B              ALIF_PINMUX(8, 4, 7)

#define PIN_P8_5__GPIO                  ALIF_PINMUX(8, 5, 0)
#define PIN_P8_5__OSPI0_RXDS1_A         ALIF_PINMUX(8, 5, 1)
#define PIN_P8_5__SPI1_SCLK_B           ALIF_PINMUX(8, 5, 2)
#define PIN_P8_5__QEC0_Y_B              ALIF_PINMUX(8, 5, 3)
#define PIN_P8_5__LPCAM_D5_A            ALIF_PINMUX(8, 5, 4)
#define PIN_P8_5__SD_D5_C               ALIF_PINMUX(8, 5, 5)
#define PIN_P8_5__CDC_D5_A              ALIF_PINMUX(8, 5, 6)
#define PIN_P8_5__CAM_D5_B              ALIF_PINMUX(8, 5, 7)

#define PIN_P8_6__GPIO                  ALIF_PINMUX(8, 6, 0)
#define PIN_P8_6__OSPI1_RXDS1_B         ALIF_PINMUX(8, 6, 1)
#define PIN_P8_6__I2S3_SCLK_B           ALIF_PINMUX(8, 6, 2)
#define PIN_P8_6__QEC0_Z_B              ALIF_PINMUX(8, 6, 3)
#define PIN_P8_6__LPCAM_D6_A            ALIF_PINMUX(8, 6, 4)
#define PIN_P8_6__SD_D6_C               ALIF_PINMUX(8, 6, 5)
#define PIN_P8_6__CDC_D6_A              ALIF_PINMUX(8, 6, 6)
#define PIN_P8_6__CAM_D6_B              ALIF_PINMUX(8, 6, 7)

#define PIN_P8_7__GPIO                  ALIF_PINMUX(8, 7, 0)
#define PIN_P8_7__OSPI0_RXDS1_C         ALIF_PINMUX(8, 7, 1)
#define PIN_P8_7__I2S3_WS_B             ALIF_PINMUX(8, 7, 2)
#define PIN_P8_7__QEC1_X_B              ALIF_PINMUX(8, 7, 3)
#define PIN_P8_7__LPCAM_D7_A            ALIF_PINMUX(8, 7, 4)
#define PIN_P8_7__SD_D7_C               ALIF_PINMUX(8, 7, 5)
#define PIN_P8_7__CDC_D7_A              ALIF_PINMUX(8, 7, 6)
#define PIN_P8_7__CAM_D7_B              ALIF_PINMUX(8, 7, 7)



#define PIN_P9_0__GPIO                  ALIF_PINMUX(9, 0, 0)
#define PIN_P9_0__OSPI1_RXDS1_C         ALIF_PINMUX(9, 0, 1)
#define PIN_P9_0__I2S3_SDI_B            ALIF_PINMUX(9, 0, 2)
#define PIN_P9_0__QEC1_Y_B              ALIF_PINMUX(9, 0, 3)
#define PIN_P9_0__SD_CMD_C              ALIF_PINMUX(9, 0, 4)
#define PIN_P9_0__CDC_D8_A              ALIF_PINMUX(9, 0, 5)
#define PIN_P9_0__CAM_D8_B              ALIF_PINMUX(9, 0, 6)
#define PIN_P9_0__LPSPI_SS3_A           ALIF_PINMUX(9, 0, 7)

#define PIN_P9_1__GPIO                  ALIF_PINMUX(9, 1, 0)
#define PIN_P9_1__LPUART_RX_B           ALIF_PINMUX(9, 1, 1)
#define PIN_P9_1__I2S3_SDO_B            ALIF_PINMUX(9, 1, 2)
#define PIN_P9_1__QEC1_Z_B              ALIF_PINMUX(9, 1, 3)
#define PIN_P9_1__SD_CLK_C              ALIF_PINMUX(9, 1, 4)
#define PIN_P9_1__CDC_D9_A              ALIF_PINMUX(9, 1, 5)
#define PIN_P9_1__CAM_D9_B              ALIF_PINMUX(9, 1, 6)
#define PIN_P9_1__LPSPI_SS4_A           ALIF_PINMUX(9, 1, 7)

#define PIN_P9_2__GPIO                  ALIF_PINMUX(9, 2, 0)
#define PIN_P9_2__LPUART_TX_B           ALIF_PINMUX(9, 2, 1)
#define PIN_P9_2__I2S3_SDI_A            ALIF_PINMUX(9, 2, 2)
#define PIN_P9_2__SPI2_MISO_B           ALIF_PINMUX(9, 2, 3)
#define PIN_P9_2__QEC2_X_B              ALIF_PINMUX(9, 2, 4)
#define PIN_P9_2__SD_RST_C              ALIF_PINMUX(9, 2, 5)
#define PIN_P9_2__CDC_D10_A             ALIF_PINMUX(9, 2, 6)
#define PIN_P9_2__CAM_D10_B             ALIF_PINMUX(9, 2, 7)

#define PIN_P9_3__GPIO                  ALIF_PINMUX(9, 3, 0)
#define PIN_P9_3__HFXO_OUT_B            ALIF_PINMUX(9, 3, 1)
#define PIN_P9_3__UART7_RX_B            ALIF_PINMUX(9, 3, 2)
#define PIN_P9_3__I2S3_SDO_A            ALIF_PINMUX(9, 3, 3)
#define PIN_P9_3__SPI2_MOSI_B           ALIF_PINMUX(9, 3, 4)
#define PIN_P9_3__QEC2_Y_B              ALIF_PINMUX(9, 3, 5)
#define PIN_P9_3__CDC_D11_A             ALIF_PINMUX(9, 3, 6)
#define PIN_P9_3__CAM_D11_B             ALIF_PINMUX(9, 3, 7)

#define PIN_P9_4__GPIO                  ALIF_PINMUX(9, 4, 0)
#define PIN_P9_4__UART7_TX_B            ALIF_PINMUX(9, 4, 1)
#define PIN_P9_4__I2S3_SCLK_A           ALIF_PINMUX(9, 4, 2)
#define PIN_P9_4__SPI2_SCLK_B           ALIF_PINMUX(9, 4, 3)
#define PIN_P9_4__I2C3_SDA_C            ALIF_PINMUX(9, 4, 4)
#define PIN_P9_4__QEC2_Z_B              ALIF_PINMUX(9, 4, 5)
#define PIN_P9_4__CDC_D12_A             ALIF_PINMUX(9, 4, 6)
#define PIN_P9_4__CAM_D12_B             ALIF_PINMUX(9, 4, 7)

#define PIN_P9_5__GPIO                  ALIF_PINMUX(9, 5, 0)
#define PIN_P9_5__OSPI1_D0_C            ALIF_PINMUX(9, 5, 1)
#define PIN_P9_5__I2S3_WS_A             ALIF_PINMUX(9, 5, 2)
#define PIN_P9_5__SPI2_SS0_B            ALIF_PINMUX(9, 5, 3)
#define PIN_P9_5__I2C3_SCL_C            ALIF_PINMUX(9, 5, 4)
#define PIN_P9_5__QEC3_X_B              ALIF_PINMUX(9, 5, 5)
#define PIN_P9_5__CDC_D13_A             ALIF_PINMUX(9, 5, 6)
#define PIN_P9_5__CAM_D13_B             ALIF_PINMUX(9, 5, 7)

#define PIN_P9_6__GPIO                  ALIF_PINMUX(9, 6, 0)
#define PIN_P9_6__OSPI1_D1_C            ALIF_PINMUX(9, 6, 1)
#define PIN_P9_6__AUDIO_CLK_B           ALIF_PINMUX(9, 6, 2)
#define PIN_P9_6__SPI2_SS1_B            ALIF_PINMUX(9, 6, 3)
#define PIN_P9_6__I2C3_SDA_B            ALIF_PINMUX(9, 6, 4)
#define PIN_P9_6__QEC3_Y_B              ALIF_PINMUX(9, 6, 5)
#define PIN_P9_6__CDC_D14_A             ALIF_PINMUX(9, 6, 6)
#define PIN_P9_6__CAM_D14_B             ALIF_PINMUX(9, 6, 7)

#define PIN_P9_7__GPIO                  ALIF_PINMUX(9, 7, 0)
#define PIN_P9_7__OSPI1_D2_C            ALIF_PINMUX(9, 7, 1)
#define PIN_P9_7__UART7_DE_B            ALIF_PINMUX(9, 7, 2)
#define PIN_P9_7__SPI2_SS2_B            ALIF_PINMUX(9, 7, 3)
#define PIN_P9_7__I2C3_SCL_B            ALIF_PINMUX(9, 7, 4)
#define PIN_P9_7__QEC3_Z_B              ALIF_PINMUX(9, 7, 5)
#define PIN_P9_7__CDC_D15_A             ALIF_PINMUX(9, 7, 6)
#define PIN_P9_7__CAM_D15_B             ALIF_PINMUX(9, 7, 7)



#define PIN_P10_0__GPIO                 ALIF_PINMUX(10, 0, 0)
#define PIN_P10_0__OSPI1_D3_C           ALIF_PINMUX(10, 0, 1)
#define PIN_P10_0__UART6_DE_B           ALIF_PINMUX(10, 0, 2)
#define PIN_P10_0__SPI2_SS3_B           ALIF_PINMUX(10, 0, 3)
#define PIN_P10_0__UT0_T0_C             ALIF_PINMUX(10, 0, 4)
#define PIN_P10_0__LPCAM_HSYNC_A        ALIF_PINMUX(10, 0, 5)
#define PIN_P10_0__CDC_D16_A            ALIF_PINMUX(10, 0, 6)
#define PIN_P10_0__CAM_HSYNC_B          ALIF_PINMUX(10, 0, 7)

#define PIN_P10_1__GPIO                 ALIF_PINMUX(10, 1, 0)
#define PIN_P10_1__OSPI1_D4_C           ALIF_PINMUX(10, 1, 1)
#define PIN_P10_1__HSUART0_RX_A         ALIF_PINMUX(10, 1, 2)
#define PIN_P10_1__LPI2S_SDI_B          ALIF_PINMUX(10, 1, 3)
#define PIN_P10_1__UT0_T1_C             ALIF_PINMUX(10, 1, 4)
#define PIN_P10_1__LPCAM_VSYNC_A        ALIF_PINMUX(10, 1, 5)
#define PIN_P10_1__CDC_D17_A            ALIF_PINMUX(10, 1, 6)
#define PIN_P10_1__CAM_VSYNC_B          ALIF_PINMUX(10, 1, 7)

#define PIN_P10_2__GPIO                 ALIF_PINMUX(10, 2, 0)
#define PIN_P10_2__OSPI1_D5_C           ALIF_PINMUX(10, 2, 1)
#define PIN_P10_2__HSUART0_TX_A         ALIF_PINMUX(10, 2, 2)
#define PIN_P10_2__LPI2S_SDO_B          ALIF_PINMUX(10, 2, 3)
#define PIN_P10_2__UT1_T0_C             ALIF_PINMUX(10, 2, 4)
#define PIN_P10_2__LPCAM_PCLK_A         ALIF_PINMUX(10, 2, 5)
#define PIN_P10_2__CDC_D18_A            ALIF_PINMUX(10, 2, 6)
#define PIN_P10_2__CAM_PCLK_B           ALIF_PINMUX(10, 2, 7)

#define PIN_P10_3__GPIO                 ALIF_PINMUX(10, 3, 0)
#define PIN_P10_3__OSPI1_D6_C           ALIF_PINMUX(10, 3, 1)
#define PIN_P10_3__HSUART1_RX_A         ALIF_PINMUX(10, 3, 2)
#define PIN_P10_3__LPI2S_SCLK_B         ALIF_PINMUX(10, 3, 3)
#define PIN_P10_3__UT1_T1_C             ALIF_PINMUX(10, 3, 4)
#define PIN_P10_3__LPCAM_XVCLK_A        ALIF_PINMUX(10, 3, 5)
#define PIN_P10_3__CDC_D19_A            ALIF_PINMUX(10, 3, 6)
#define PIN_P10_3__CAM_XVCLK_B          ALIF_PINMUX(10, 3, 7)

#define PIN_P10_4__GPIO                 ALIF_PINMUX(10, 4, 0)
#define PIN_P10_4__OSPI1_D7_C           ALIF_PINMUX(10, 4, 1)
#define PIN_P10_4__HSUART1_TX_A         ALIF_PINMUX(10, 4, 2)
#define PIN_P10_4__LPI2S_WS_B           ALIF_PINMUX(10, 4, 3)
#define PIN_P10_4__I2C0_SDA_D           ALIF_PINMUX(10, 4, 4)
#define PIN_P10_4__UT2_T0_C             ALIF_PINMUX(10, 4, 5)
#define PIN_P10_4__ETH_TXD0_B           ALIF_PINMUX(10, 4, 6)
#define PIN_P10_4__CDC_D20_A            ALIF_PINMUX(10, 4, 7)

#define PIN_P10_5__GPIO                 ALIF_PINMUX(10, 5, 0)
#define PIN_P10_5__UART6_RX_A           ALIF_PINMUX(10, 5, 1)
#define PIN_P10_5__I2S2_SDI_B           ALIF_PINMUX(10, 5, 2)
#define PIN_P10_5__SPI3_MISO_B          ALIF_PINMUX(10, 5, 3)
#define PIN_P10_5__I2C0_SCL_D           ALIF_PINMUX(10, 5, 4)
#define PIN_P10_5__UT2_T1_C             ALIF_PINMUX(10, 5, 5)
#define PIN_P10_5__ETH_TXD1_B           ALIF_PINMUX(10, 5, 6)
#define PIN_P10_5__CDC_D21_A            ALIF_PINMUX(10, 5, 7)

#define PIN_P10_6__GPIO                 ALIF_PINMUX(10, 6, 0)
#define PIN_P10_6__UART6_TX_A           ALIF_PINMUX(10, 6, 1)
#define PIN_P10_6__I2S2_SDO_B           ALIF_PINMUX(10, 6, 2)
#define PIN_P10_6__SPI3_MOSI_B          ALIF_PINMUX(10, 6, 3)
#define PIN_P10_6__I2C1_SDA_D           ALIF_PINMUX(10, 6, 4)
#define PIN_P10_6__UT3_T0_C             ALIF_PINMUX(10, 6, 5)
#define PIN_P10_6__ETH_TXEN_B           ALIF_PINMUX(10, 6, 6)
#define PIN_P10_6__CDC_D22_A            ALIF_PINMUX(10, 6, 7)

#define PIN_P10_7__GPIO                 ALIF_PINMUX(10, 7, 0)
#define PIN_P10_7__UART7_RX_A           ALIF_PINMUX(10, 7, 1)
#define PIN_P10_7__I2S2_SCLK_B          ALIF_PINMUX(10, 7, 2)
#define PIN_P10_7__SPI3_SCLK_B          ALIF_PINMUX(10, 7, 3)
#define PIN_P10_7__I2C1_SCL_D           ALIF_PINMUX(10, 7, 4)
#define PIN_P10_7__UT3_T1_C             ALIF_PINMUX(10, 7, 5)
#define PIN_P10_7__CDC_D23_A            ALIF_PINMUX(10, 7, 6)
#define PIN_P10_7__OSPI1_RXDS0_C        ALIF_PINMUX(10, 7, 7)



#define PIN_P11_0__GPIO                 ALIF_PINMUX(11, 0, 0)
#define PIN_P11_0__OSPI1_D0_A           ALIF_PINMUX(11, 0, 1)
#define PIN_P11_0__UART7_TX_A           ALIF_PINMUX(11, 0, 2)
#define PIN_P11_0__I2S2_WS_B            ALIF_PINMUX(11, 0, 3)
#define PIN_P11_0__SPI3_SS0_B           ALIF_PINMUX(11, 0, 4)
#define PIN_P11_0__UT4_T0_C             ALIF_PINMUX(11, 0, 5)
#define PIN_P11_0__ETH_REFCLK_B         ALIF_PINMUX(11, 0, 6)
#define PIN_P11_0__CDC_D0_B             ALIF_PINMUX(11, 0, 7)

#define PIN_P11_1__GPIO                 ALIF_PINMUX(11, 1, 0)
#define PIN_P11_1__OSPI1_D1_A           ALIF_PINMUX(11, 1, 1)
#define PIN_P11_1__UART7_DE_A           ALIF_PINMUX(11, 1, 2)
#define PIN_P11_1__SPI3_SS1_B           ALIF_PINMUX(11, 1, 3)
#define PIN_P11_1__UT4_T1_C             ALIF_PINMUX(11, 1, 4)
#define PIN_P11_1__ETH_MDIO_B           ALIF_PINMUX(11, 1, 5)
#define PIN_P11_1__CDC_D1_B             ALIF_PINMUX(11, 1, 6)
#define PIN_P11_1__LPSPI_SS5_A          ALIF_PINMUX(11, 1, 7)

#define PIN_P11_2__GPIO                 ALIF_PINMUX(11, 2, 0)
#define PIN_P11_2__OSPI1_D2_A           ALIF_PINMUX(11, 2, 1)
#define PIN_P11_2__UART6_DE_A           ALIF_PINMUX(11, 2, 2)
#define PIN_P11_2__LPPDM_C2_B           ALIF_PINMUX(11, 2, 3)
#define PIN_P11_2__SPI3_SS2_B           ALIF_PINMUX(11, 2, 4)
#define PIN_P11_2__UT5_T0_C             ALIF_PINMUX(11, 2, 5)
#define PIN_P11_2__ETH_MDC_B            ALIF_PINMUX(11, 2, 6)
#define PIN_P11_2__CDC_D2_B             ALIF_PINMUX(11, 2, 7)

#define PIN_P11_3__GPIO                 ALIF_PINMUX(11, 3, 0)
#define PIN_P11_3__OSPI1_D3_A           ALIF_PINMUX(11, 3, 1)
#define PIN_P11_3__UART5_RX_B           ALIF_PINMUX(11, 3, 2)
#define PIN_P11_3__LPPDM_C3_B           ALIF_PINMUX(11, 3, 3)
#define PIN_P11_3__SPI3_SS3_B           ALIF_PINMUX(11, 3, 4)
#define PIN_P11_3__UT5_T1_C             ALIF_PINMUX(11, 3, 5)
#define PIN_P11_3__ETH_RXD0_B           ALIF_PINMUX(11, 3, 6)
#define PIN_P11_3__CDC_D3_B             ALIF_PINMUX(11, 3, 7)

#define PIN_P11_4__GPIO                 ALIF_PINMUX(11, 4, 0)
#define PIN_P11_4__OSPI1_D4_A           ALIF_PINMUX(11, 4, 1)
#define PIN_P11_4__UART5_TX_B           ALIF_PINMUX(11, 4, 2)
#define PIN_P11_4__PDM_C2_B             ALIF_PINMUX(11, 4, 3)
#define PIN_P11_4__LPSPI_MISO_B         ALIF_PINMUX(11, 4, 4)
#define PIN_P11_4__UT6_T0_C             ALIF_PINMUX(11, 4, 5)
#define PIN_P11_4__ETH_RXD1_B           ALIF_PINMUX(11, 4, 6)
#define PIN_P11_4__CDC_D4_B             ALIF_PINMUX(11, 4, 7)

#define PIN_P11_5__GPIO                 ALIF_PINMUX(11, 5, 0)
#define PIN_P11_5__OSPI1_D5_A           ALIF_PINMUX(11, 5, 1)
#define PIN_P11_5__UART6_RX_B           ALIF_PINMUX(11, 5, 2)
#define PIN_P11_5__PDM_C3_B             ALIF_PINMUX(11, 5, 3)
#define PIN_P11_5__LPSPI_MOSI_B         ALIF_PINMUX(11, 5, 4)
#define PIN_P11_5__UT6_T1_C             ALIF_PINMUX(11, 5, 5)
#define PIN_P11_5__ETH_CRS_DV_B         ALIF_PINMUX(11, 5, 6)
#define PIN_P11_5__CDC_D5_B             ALIF_PINMUX(11, 5, 7)

#define PIN_P11_6__GPIO                 ALIF_PINMUX(11, 6, 0)
#define PIN_P11_6__OSPI1_D6_A           ALIF_PINMUX(11, 6, 1)
#define PIN_P11_6__UART6_TX_B           ALIF_PINMUX(11, 6, 2)
#define PIN_P11_6__LPPDM_D2_B           ALIF_PINMUX(11, 6, 3)
#define PIN_P11_6__LPSPI_SCLK_B         ALIF_PINMUX(11, 6, 4)
#define PIN_P11_6__UT7_T0_C             ALIF_PINMUX(11, 6, 5)
#define PIN_P11_6__ETH_RST_B            ALIF_PINMUX(11, 6, 6)
#define PIN_P11_6__CDC_D6_B             ALIF_PINMUX(11, 6, 7)

#define PIN_P11_7__GPIO                 ALIF_PINMUX(11, 7, 0)
#define PIN_P11_7__OSPI1_D7_A           ALIF_PINMUX(11, 7, 1)
#define PIN_P11_7__UART5_DE_B           ALIF_PINMUX(11, 7, 2)
#define PIN_P11_7__LPPDM_D3_B           ALIF_PINMUX(11, 7, 3)
#define PIN_P11_7__LPSPI_SS_B           ALIF_PINMUX(11, 7, 4)
#define PIN_P11_7__UT7_T1_C             ALIF_PINMUX(11, 7, 5)
#define PIN_P11_7__ETH_IRQ_B            ALIF_PINMUX(11, 7, 6)
#define PIN_P11_7__CDC_D7_B             ALIF_PINMUX(11, 7, 7)



#define PIN_P12_0__GPIO                 ALIF_PINMUX(12, 0, 0)
#define PIN_P12_0__OSPI0_SCLK_C         ALIF_PINMUX(12, 0, 1)
#define PIN_P12_0__AUDIO_CLK_C          ALIF_PINMUX(12, 0, 2)
#define PIN_P12_0__I2S1_SDI_B           ALIF_PINMUX(12, 0, 3)
#define PIN_P12_0__UT8_T0_C             ALIF_PINMUX(12, 0, 4)
#define PIN_P12_0__CDC_D8_B             ALIF_PINMUX(12, 0, 5)
#define PIN_P12_0__OSPI1_D8_B           ALIF_PINMUX(12, 0, 6)
#define PIN_P12_0__LPUT0_T0_B           ALIF_PINMUX(12, 0, 7)

#define PIN_P12_1__GPIO                 ALIF_PINMUX(12, 1, 0)
#define PIN_P12_1__OSPI0_SCLKN_C        ALIF_PINMUX(12, 1, 1)
#define PIN_P12_1__UART4_RX_B           ALIF_PINMUX(12, 1, 2)
#define PIN_P12_1__I2S1_SDO_B           ALIF_PINMUX(12, 1, 3)
#define PIN_P12_1__UT8_T1_C             ALIF_PINMUX(12, 1, 4)
#define PIN_P12_1__CDC_D9_B             ALIF_PINMUX(12, 1, 5)
#define PIN_P12_1__OSPI1_D9_B           ALIF_PINMUX(12, 1, 6)
#define PIN_P12_1__LPUT0_T1_B           ALIF_PINMUX(12, 1, 7)

#define PIN_P12_2__GPIO                 ALIF_PINMUX(12, 2, 0)
#define PIN_P12_2__OSPI0_RXDS_C         ALIF_PINMUX(12, 2, 1)
#define PIN_P12_2__UART4_TX_B           ALIF_PINMUX(12, 2, 2)
#define PIN_P12_2__I2S1_SCLK_B          ALIF_PINMUX(12, 2, 3)
#define PIN_P12_2__UT9_T0_C             ALIF_PINMUX(12, 2, 4)
#define PIN_P12_2__CDC_D10_B            ALIF_PINMUX(12, 2, 5)
#define PIN_P12_2__OSPI1_D10_B          ALIF_PINMUX(12, 2, 6)
#define PIN_P12_2__LPUT1_T0_B           ALIF_PINMUX(12, 2, 7)

#define PIN_P12_3__GPIO                 ALIF_PINMUX(12, 3, 0)
#define PIN_P12_3__OSPI0_SS0_C          ALIF_PINMUX(12, 3, 1)
#define PIN_P12_3__UART4_DE_B           ALIF_PINMUX(12, 3, 2)
#define PIN_P12_3__I2S1_WS_B            ALIF_PINMUX(12, 3, 3)
#define PIN_P12_3__UT9_T1_C             ALIF_PINMUX(12, 3, 4)
#define PIN_P12_3__CDC_D11_B            ALIF_PINMUX(12, 3, 5)
#define PIN_P12_3__OSPI1_D11_B          ALIF_PINMUX(12, 3, 6)
#define PIN_P12_3__LPUT1_T1_B           ALIF_PINMUX(12, 3, 7)

#define PIN_P12_4__GPIO                 ALIF_PINMUX(12, 4, 0)
#define PIN_P12_4__OSPI0_SS1_C          ALIF_PINMUX(12, 4, 1)
#define PIN_P12_4__SPI3_MISO_A          ALIF_PINMUX(12, 4, 2)
#define PIN_P12_4__UT10_T0_C            ALIF_PINMUX(12, 4, 3)
#define PIN_P12_4__CAN_RXD_C            ALIF_PINMUX(12, 4, 4)
#define PIN_P12_4__CDC_D12_B            ALIF_PINMUX(12, 4, 5)
#define PIN_P12_4__OSPI1_D12_B          ALIF_PINMUX(12, 4, 6)
#define PIN_P12_4__LPUT2_T0_B           ALIF_PINMUX(12, 4, 7)

#define PIN_P12_5__GPIO                 ALIF_PINMUX(12, 5, 0)
#define PIN_P12_5__HSUART0_RX_B         ALIF_PINMUX(12, 5, 1)
#define PIN_P12_5__SPI3_MOSI_A          ALIF_PINMUX(12, 5, 2)
#define PIN_P12_5__UT10_T1_C            ALIF_PINMUX(12, 5, 3)
#define PIN_P12_5__CAN_TXD_C            ALIF_PINMUX(12, 5, 4)
#define PIN_P12_5__CDC_D13_B            ALIF_PINMUX(12, 5, 5)
#define PIN_P12_5__OSPI1_D13_B          ALIF_PINMUX(12, 5, 6)
#define PIN_P12_5__LPUT2_T1_B           ALIF_PINMUX(12, 5, 7)

#define PIN_P12_6__GPIO                 ALIF_PINMUX(12, 6, 0)
#define PIN_P12_6__HSUART0_TX_B         ALIF_PINMUX(12, 6, 1)
#define PIN_P12_6__SPI3_SCLK_A          ALIF_PINMUX(12, 6, 2)
#define PIN_P12_6__UT11_T0_C            ALIF_PINMUX(12, 6, 3)
#define PIN_P12_6__CAN_STBY_C           ALIF_PINMUX(12, 6, 4)
#define PIN_P12_6__CDC_D14_B            ALIF_PINMUX(12, 6, 5)
#define PIN_P12_6__OSPI1_D14_B          ALIF_PINMUX(12, 6, 6)

#define PIN_P12_7__GPIO                 ALIF_PINMUX(12, 7, 0)
#define PIN_P12_7__OSPI1_RXDS0_B        ALIF_PINMUX(12, 7, 1)
#define PIN_P12_7__HSUART1_RX_B         ALIF_PINMUX(12, 7, 2)
#define PIN_P12_7__SPI3_SS0_A           ALIF_PINMUX(12, 7, 3)
#define PIN_P12_7__UT11_T1_C            ALIF_PINMUX(12, 7, 4)
#define PIN_P12_7__CDC_D15_B            ALIF_PINMUX(12, 7, 5)



#define PIN_P13_0__GPIO                 ALIF_PINMUX(13, 0, 0)
#define PIN_P13_0__OSPI1_D0_B           ALIF_PINMUX(13, 0, 1)
#define PIN_P13_0__HSUART1_TX_B         ALIF_PINMUX(13, 0, 2)
#define PIN_P13_0__SPI3_SS1_A           ALIF_PINMUX(13, 0, 3)
#define PIN_P13_0__QEC0_X_C             ALIF_PINMUX(13, 0, 4)
#define PIN_P13_0__SD_D0_B              ALIF_PINMUX(13, 0, 5)
#define PIN_P13_0__CDC_D16_B            ALIF_PINMUX(13, 0, 6)
#define PIN_P13_0__OSPI0_D8_A           ALIF_PINMUX(13, 0, 7)

#define PIN_P13_1__GPIO                 ALIF_PINMUX(13, 1, 0)
#define PIN_P13_1__OSPI1_D1_B           ALIF_PINMUX(13, 1, 1)
#define PIN_P13_1__SPI3_SS2_A           ALIF_PINMUX(13, 1, 2)
#define PIN_P13_1__QEC0_Y_C             ALIF_PINMUX(13, 1, 3)
#define PIN_P13_1__SD_D1_B              ALIF_PINMUX(13, 1, 4)
#define PIN_P13_1__CDC_D17_B            ALIF_PINMUX(13, 1, 5)
#define PIN_P13_1__OSPI0_D9_A           ALIF_PINMUX(13, 1, 6)

#define PIN_P13_2__GPIO                 ALIF_PINMUX(13, 2, 0)
#define PIN_P13_2__OSPI1_D2_B           ALIF_PINMUX(13, 2, 1)
#define PIN_P13_2__SPI3_SS3_A           ALIF_PINMUX(13, 2, 2)
#define PIN_P13_2__QEC0_Z_C             ALIF_PINMUX(13, 2, 3)
#define PIN_P13_2__SD_D2_B              ALIF_PINMUX(13, 2, 4)
#define PIN_P13_2__CDC_D18_B            ALIF_PINMUX(13, 2, 5)
#define PIN_P13_2__OSPI0_D10_A          ALIF_PINMUX(13, 2, 6)

#define PIN_P13_3__GPIO                 ALIF_PINMUX(13, 3, 0)
#define PIN_P13_3__OSPI1_D3_B           ALIF_PINMUX(13, 3, 1)
#define PIN_P13_3__SPI2_SS3_A           ALIF_PINMUX(13, 3, 2)
#define PIN_P13_3__QEC1_X_C             ALIF_PINMUX(13, 3, 3)
#define PIN_P13_3__SD_D3_B              ALIF_PINMUX(13, 3, 4)
#define PIN_P13_3__CDC_D19_B            ALIF_PINMUX(13, 3, 5)
#define PIN_P13_3__OSPI0_D11_A          ALIF_PINMUX(13, 3, 6)

#define PIN_P13_4__GPIO                 ALIF_PINMUX(13, 4, 0)
#define PIN_P13_4__OSPI1_D4_B           ALIF_PINMUX(13, 4, 1)
#define PIN_P13_4__LPI2S_SDI_C          ALIF_PINMUX(13, 4, 2)
#define PIN_P13_4__QEC1_Y_C             ALIF_PINMUX(13, 4, 3)
#define PIN_P13_4__SD_D4_B              ALIF_PINMUX(13, 4, 4)
#define PIN_P13_4__CDC_D20_B            ALIF_PINMUX(13, 4, 5)
#define PIN_P13_4__OSPI0_D12_A          ALIF_PINMUX(13, 4, 6)

#define PIN_P13_5__GPIO                 ALIF_PINMUX(13, 5, 0)
#define PIN_P13_5__OSPI1_D5_B           ALIF_PINMUX(13, 5, 1)
#define PIN_P13_5__LPI2S_SDO_C          ALIF_PINMUX(13, 5, 2)
#define PIN_P13_5__QEC1_Z_C             ALIF_PINMUX(13, 5, 3)
#define PIN_P13_5__SD_D5_B              ALIF_PINMUX(13, 5, 4)
#define PIN_P13_5__CDC_D21_B            ALIF_PINMUX(13, 5, 5)
#define PIN_P13_5__OSPI0_D13_A          ALIF_PINMUX(13, 5, 6)

#define PIN_P13_6__GPIO                 ALIF_PINMUX(13, 6, 0)
#define PIN_P13_6__OSPI1_D6_B           ALIF_PINMUX(13, 6, 1)
#define PIN_P13_6__LPI2S_SCLK_C         ALIF_PINMUX(13, 6, 2)
#define PIN_P13_6__QEC2_X_C             ALIF_PINMUX(13, 6, 3)
#define PIN_P13_6__SD_D6_B              ALIF_PINMUX(13, 6, 4)
#define PIN_P13_6__CDC_D22_B            ALIF_PINMUX(13, 6, 5)
#define PIN_P13_6__OSPI0_D14_A          ALIF_PINMUX(13, 6, 6)

#define PIN_P13_7__GPIO                 ALIF_PINMUX(13, 7, 0)
#define PIN_P13_7__OSPI1_D7_B           ALIF_PINMUX(13, 7, 1)
#define PIN_P13_7__LPI2S_WS_C           ALIF_PINMUX(13, 7, 2)
#define PIN_P13_7__QEC2_Y_C             ALIF_PINMUX(13, 7, 3)
#define PIN_P13_7__SD_D7_B              ALIF_PINMUX(13, 7, 4)
#define PIN_P13_7__CDC_D23_B            ALIF_PINMUX(13, 7, 5)
#define PIN_P13_7__OSPI0_D15_A          ALIF_PINMUX(13, 7, 6)



#define PIN_P14_0__GPIO                 ALIF_PINMUX(14, 0, 0)
#define PIN_P14_0__OSPI1_SCLK_B         ALIF_PINMUX(14, 0, 1)
#define PIN_P14_0__UART6_RX_C           ALIF_PINMUX(14, 0, 2)
#define PIN_P14_0__QEC2_Z_C             ALIF_PINMUX(14, 0, 3)
#define PIN_P14_0__SD_CMD_B             ALIF_PINMUX(14, 0, 4)
#define PIN_P14_0__LFRC_OUT_B           ALIF_PINMUX(14, 0, 5)

#define PIN_P14_1__GPIO                 ALIF_PINMUX(14, 1, 0)
#define PIN_P14_1__OSPI1_SCLKN_B        ALIF_PINMUX(14, 1, 1)
#define PIN_P14_1__UART6_TX_C           ALIF_PINMUX(14, 1, 2)
#define PIN_P14_1__APLL_OUT_C           ALIF_PINMUX(14, 1, 3)
#define PIN_P14_1__QEC3_X_C             ALIF_PINMUX(14, 1, 4)
#define PIN_P14_1__SD_CLK_B             ALIF_PINMUX(14, 1, 5)
#define PIN_P14_1__LFXO_OUT_B           ALIF_PINMUX(14, 1, 6)

#define PIN_P14_2__GPIO                 ALIF_PINMUX(14, 2, 0)
#define PIN_P14_2__OSPI1_SS0_B          ALIF_PINMUX(14, 2, 1)
#define PIN_P14_2__UART7_RX_C           ALIF_PINMUX(14, 2, 2)
#define PIN_P14_2__LPI3C_SDA_C          ALIF_PINMUX(14, 2, 3)
#define PIN_P14_2__QEC3_Y_C             ALIF_PINMUX(14, 2, 4)
#define PIN_P14_2__SD_RST_B             ALIF_PINMUX(14, 2, 5)
#define PIN_P14_2__LPSPI_SS5_B          ALIF_PINMUX(14, 2, 6)

#define PIN_P14_3__GPIO                 ALIF_PINMUX(14, 3, 0)
#define PIN_P14_3__OSPI1_SS1_B          ALIF_PINMUX(14, 3, 1)
#define PIN_P14_3__UART7_TX_C           ALIF_PINMUX(14, 3, 2)
#define PIN_P14_3__LPI3C_SCL_C          ALIF_PINMUX(14, 3, 3)
#define PIN_P14_3__QEC3_Z_C             ALIF_PINMUX(14, 3, 4)

#define PIN_P14_4__GPIO                 ALIF_PINMUX(14, 4, 0)
#define PIN_P14_4__CMP3_OUT_B           ALIF_PINMUX(14, 4, 1)
#define PIN_P14_4__SPI1_MISO_C          ALIF_PINMUX(14, 4, 2)
#define PIN_P14_4__FAULT0_C             ALIF_PINMUX(14, 4, 3)
#define PIN_P14_4__OSPI1_RXDS1_A        ALIF_PINMUX(14, 4, 4)
#define PIN_P14_4__LPSPI_SS1_B          ALIF_PINMUX(14, 4, 5)

#define PIN_P14_5__GPIO                 ALIF_PINMUX(14, 5, 0)
#define PIN_P14_5__CMP2_OUT_B           ALIF_PINMUX(14, 5, 1)
#define PIN_P14_5__SPI1_MOSI_C          ALIF_PINMUX(14, 5, 2)
#define PIN_P14_5__FAULT1_C             ALIF_PINMUX(14, 5, 3)
#define PIN_P14_5__OSPI0_RXDS1_B        ALIF_PINMUX(14, 5, 4)
#define PIN_P14_5__LPSPI_SS2_B          ALIF_PINMUX(14, 5, 5)

#define PIN_P14_6__GPIO                 ALIF_PINMUX(14, 6, 0)
#define PIN_P14_6__CMP1_OUT_B           ALIF_PINMUX(14, 6, 1)
#define PIN_P14_6__SPI1_SCLK_C          ALIF_PINMUX(14, 6, 2)
#define PIN_P14_6__FAULT2_C             ALIF_PINMUX(14, 6, 3)
#define PIN_P14_6__OSPI1_D15_B          ALIF_PINMUX(14, 6, 4)
#define PIN_P14_6__LPSPI_SS3_B          ALIF_PINMUX(14, 6, 5)

#define PIN_P14_7__GPIO                 ALIF_PINMUX(14, 7, 0)
#define PIN_P14_7__CMP0_OUT_B           ALIF_PINMUX(14, 7, 1)
#define PIN_P14_7__SPI1_SS0_C           ALIF_PINMUX(14, 7, 2)
#define PIN_P14_7__FAULT3_C             ALIF_PINMUX(14, 7, 3)
#define PIN_P14_7__APLL_OUT_B           ALIF_PINMUX(14, 7, 4)
#define PIN_P14_7__LPSPI_SS4_B          ALIF_PINMUX(14, 7, 5)



#define PIN_P15_0__LPGPIO               ALIF_PINMUX(15, 0, 0)

#define PIN_P15_1__LPGPIO               ALIF_PINMUX(15, 1, 0)

#define PIN_P15_2__LPGPIO               ALIF_PINMUX(15, 2, 0)

#define PIN_P15_3__LPGPIO               ALIF_PINMUX(15, 3, 0)

#define PIN_P15_4__LPGPIO               ALIF_PINMUX(15, 4, 0)

#define PIN_P15_5__LPGPIO               ALIF_PINMUX(15, 5, 0)

#define PIN_P15_6__LPGPIO               ALIF_PINMUX(15, 6, 0)

#define PIN_P15_7__LPGPIO               ALIF_PINMUX(15, 7, 0)



#define PIN_P16_0__GPIO                 ALIF_PINMUX(16, 0, 0)
#define PIN_P16_0__OSPI0_D8_B           ALIF_PINMUX(16, 0, 1)

#define PIN_P16_1__GPIO                 ALIF_PINMUX(16, 1, 0)
#define PIN_P16_1__OSPI0_D9_B           ALIF_PINMUX(16, 1, 1)

#define PIN_P16_2__GPIO                 ALIF_PINMUX(16, 2, 0)
#define PIN_P16_2__OSPI0_D10_B          ALIF_PINMUX(16, 2, 1)

#define PIN_P16_3__GPIO                 ALIF_PINMUX(16, 3, 0)
#define PIN_P16_3__OSPI0_D11_B          ALIF_PINMUX(16, 3, 1)

#define PIN_P16_4__GPIO                 ALIF_PINMUX(16, 4, 0)
#define PIN_P16_4__OSPI0_D12_B          ALIF_PINMUX(16, 4, 1)

#define PIN_P16_5__GPIO                 ALIF_PINMUX(16, 5, 0)
#define PIN_P16_5__OSPI0_D13_B          ALIF_PINMUX(16, 5, 1)

#define PIN_P16_6__GPIO                 ALIF_PINMUX(16, 6, 0)
#define PIN_P16_6__OSPI0_D14_B          ALIF_PINMUX(16, 6, 1)

#define PIN_P16_7__GPIO                 ALIF_PINMUX(16, 7, 0)
#define PIN_P16_7__OSPI0_D15_B          ALIF_PINMUX(16, 7, 1)



#define PIN_P17_0__GPIO                 ALIF_PINMUX(17, 0, 0)
#define PIN_P17_0__OSPI1_D8_C           ALIF_PINMUX(17, 0, 1)

#define PIN_P17_1__GPIO                 ALIF_PINMUX(17, 1, 0)
#define PIN_P17_1__OSPI1_D9_C           ALIF_PINMUX(17, 1, 1)

#define PIN_P17_2__GPIO                 ALIF_PINMUX(17, 2, 0)
#define PIN_P17_2__OSPI1_D10_C          ALIF_PINMUX(17, 2, 1)

#define PIN_P17_3__GPIO                 ALIF_PINMUX(17, 3, 0)
#define PIN_P17_3__OSPI1_D11_C          ALIF_PINMUX(17, 3, 1)

#define PIN_P17_4__GPIO                 ALIF_PINMUX(17, 4, 0)
#define PIN_P17_4__OSPI1_D12_C          ALIF_PINMUX(17, 4, 1)

#define PIN_P17_5__GPIO                 ALIF_PINMUX(17, 5, 0)
#define PIN_P17_5__OSPI1_D13_C          ALIF_PINMUX(17, 5, 1)

#define PIN_P17_6__GPIO                 ALIF_PINMUX(17, 6, 0)
#define PIN_P17_6__OSPI1_D14_C          ALIF_PINMUX(17, 6, 1)

#define PIN_P17_7__GPIO                 ALIF_PINMUX(17, 7, 0)
#define PIN_P17_7__OSPI1_D15_C          ALIF_PINMUX(17, 7, 1)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ALIF_ENSEMBLE_PINCTRL_H_ */
```

## 24.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Alif Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 1466 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ALIF_ENSEMBLE_PINCTRL_H_`。

## 24.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/alif-ensemble-pinctrl_8h.html)

---

[上一章](P023_alif-ensemble-e1c-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P025_ambiq-apollo3-pinctrl.h_源码浏览.md)
