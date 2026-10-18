---
id: learning.zephyr-docs.api-source-runtime-reference.page-21
title: gatt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_gatt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h.html)。

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
<a id="l00046"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="foldopen00133"></a>
<a id="l00133"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="foldopen00262"></a>
<a id="l00262"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00344"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="foldopen00354"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="foldopen00367"></a>
<a id="l00367"></a>
<a id="l00369"></a>
<a id="l00371"></a>
<a id="l00375"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="foldopen00384"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="foldopen00397"></a>
<a id="l00397"></a>
<a id="l00399"></a>
<a id="l00401"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="foldopen00407"></a>
<a id="l00407"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00422"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="foldopen00427"></a>
<a id="l00427"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00458"></a>
<a id="l00465"></a>
<a id="l00471"></a>
<a id="l00477"></a>
<a id="l00483"></a>
<a id="l00490"></a>
<a id="l00496"></a>
<a id="l00504"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="foldopen00518"></a>
<a id="l00518"></a>
<a id="l00520"></a>
<a id="l00522"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00528"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="foldopen00556"></a>
<a id="l00556"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00562"></a>
<a id="l00568"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="foldopen00580"></a>
<a id="l00580"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00586"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="foldopen00599"></a>
<a id="l00599"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="foldopen00609"></a>
<a id="l00609"></a>
<a id="l00615"></a>
<a id="l00621"></a>
<a id="l00627"></a>
<a id="l00634"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00649"></a>
<a id="foldopen00666"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="foldopen00758"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="foldopen00805"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00879"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="l00882"></a>
<a id="l00898"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="foldopen00909"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00934"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="l00938"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="foldopen00951"></a>
<a id="l00951"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00955"></a>
<a id="l00956"></a>
<a id="foldopen00964"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="l00966"></a>
<a id="l00967"></a>
<a id="foldopen00978"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00998"></a>
<a id="l00999"></a>
<a id="l01000"></a>
<a id="l01001"></a>
<a id="foldopen01009"></a>
<a id="l01009"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01012"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="foldopen01042"></a>
<a id="l01042"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01048"></a>
<a id="foldopen01066"></a>
<a id="l01066"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="l01073"></a>
<a id="l01085"></a>
<a id="l01086"></a>
<a id="l01087"></a>
<a id="l01088"></a>
<a id="l01089"></a>
<a id="l01090"></a>
<a id="l01091"></a>
<a id="l01092"></a>
<a id="foldopen01099"></a>
<a id="l01099"></a>
<a id="l01101"></a>
<a id="l01103"></a>
<a id="l01108"></a>
<a id="l01109"></a>
<a id="l01110"></a>
<a id="foldopen01115"></a>
<a id="l01115"></a>
<a id="l01117"></a>
<a id="l01118"></a>
<a id="l01120"></a>
<a id="l01121"></a>
<a id="l01132"></a>
<a id="l01133"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="l01157"></a>
<a id="l01158"></a>
<a id="l01159"></a>
<a id="l01160"></a>
<a id="l01180"></a>
<a id="l01181"></a>
<a id="l01182"></a>
<a id="l01183"></a>
<a id="l01203"></a>
<a id="l01204"></a>
<a id="l01205"></a>
<a id="l01206"></a>
<a id="foldopen01216"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01220"></a>
<a id="l01221"></a>
<a id="l01222"></a>
<a id="l01223"></a>
<a id="foldopen01236"></a>
<a id="l01236"></a>
<a id="l01237"></a>
<a id="l01238"></a>
<a id="l01239"></a>
<a id="l01240"></a>
<a id="foldopen01250"></a>
<a id="l01250"></a>
<a id="l01251"></a>
<a id="l01252"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="foldopen01265"></a>
<a id="l01265"></a>
<a id="l01266"></a>
<a id="l01267"></a>
<a id="l01268"></a>
<a id="l01269"></a>
<a id="l01286"></a>
<a id="l01287"></a>
<a id="l01288"></a>
<a id="l01289"></a>
<a id="foldopen01297"></a>
<a id="l01297"></a>
<a id="l01298"></a>
<a id="l01299"></a>
<a id="l01300"></a>
<a id="l01318"></a>
<a id="l01319"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="foldopen01331"></a>
<a id="l01331"></a>
<a id="l01332"></a>
<a id="l01333"></a>
<a id="l01334"></a>
<a id="l01351"></a>
<a id="l01352"></a>
<a id="l01353"></a>
<a id="l01354"></a>
<a id="foldopen01362"></a>
<a id="l01362"></a>
<a id="l01363"></a>
<a id="l01364"></a>
<a id="l01365"></a>
<a id="foldopen01380"></a>
<a id="l01380"></a>
<a id="l01381"></a>
<a id="l01382"></a>
<a id="foldopen01395"></a>
<a id="l01395"></a>
<a id="l01396"></a>
<a id="l01397"></a>
<a id="l01398"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01402"></a>
<a id="l01403"></a>
<a id="l01404"></a>
<a id="l01410"></a>
<a id="l01411"></a>
<a id="foldopen01416"></a>
<a id="l01416"></a>
<a id="l01422"></a>
<a id="l01428"></a>
<a id="l01430"></a>
<a id="l01432"></a>
<a id="l01434"></a>
<a id="l01436"></a>
<a id="l01437"></a>
<a id="l01439"></a>
<a id="l01440"></a>
<a id="l01441"></a>
<a id="l01442"></a>
<a id="l01463"></a>
<a id="l01464"></a>
<a id="l01465"></a>
<a id="l01517"></a>
<a id="l01518"></a>
<a id="l01519"></a>
<a id="l01520"></a>
<a id="foldopen01544"></a>
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
<a id="l01557"></a>
<a id="l01558"></a>
<a id="l01559"></a>
<a id="l01560"></a>
<a id="l01561"></a>
<a id="foldopen01581"></a>
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
<a id="l01611"></a>
<a id="l01612"></a>
<a id="l01613"></a>
<a id="l01614"></a>
<a id="l01623"></a>
<a id="l01624"></a>
<a id="l01625"></a>
<a id="foldopen01631"></a>
<a id="l01631"></a>
<a id="l01637"></a>
<a id="l01643"></a>
<a id="l01645"></a>
<a id="l01647"></a>
<a id="l01649"></a>
<a id="l01651"></a>
<a id="l01653"></a>
<a id="l01654"></a>
<a id="l01656"></a>
<a id="l01657"></a>
<a id="l01658"></a>
<a id="l01659"></a>
<a id="l01689"></a>
<a id="l01690"></a>
<a id="l01691"></a>
<a id="l01710"></a>
<a id="l01711"></a>
<a id="l01712"></a>
<a id="l01722"></a>
<a id="l01723"></a>
<a id="l01739"></a>
<a id="l01740"></a>
<a id="l01742"></a>
<a id="l01748"></a>
<a id="foldopen01758"></a>
<a id="l01758"></a>
<a id="l01760"></a>
<a id="l01761"></a>
<a id="l01762"></a>
<a id="l01763"></a>
<a id="l01789"></a>
<a id="l01790"></a>
<a id="l01791"></a>
<a id="l01792"></a>
<a id="l01793"></a>
<a id="l01843"></a>
<a id="l01844"></a>
<a id="l01845"></a>
<a id="l01846"></a>
<a id="foldopen01848"></a>
<a id="l01848"></a>
<a id="l01850"></a>
<a id="l01852"></a>
<a id="l01854"></a>
<a id="l01859"></a>
<a id="l01868"></a>
<a id="l01877"></a>
<a id="l01888"></a>
<a id="l01889"></a>
<a id="l01890"></a>
<a id="l01892"></a>
<a id="l01893"></a>
<a id="foldopen01895"></a>
<a id="l01895"></a>
<a id="l01897"></a>
<a id="l01899"></a>
<a id="l01900"></a>
<a id="l01902"></a>
<a id="l01904"></a>
<a id="l01906"></a>
<a id="l01908"></a>
<a id="l01909"></a>
<a id="l01911"></a>
<a id="l01912"></a>
<a id="l01919"></a>
<a id="l01921"></a>
<a id="l01922"></a>
<a id="l01924"></a>
<a id="l01925"></a>
<a id="l01926"></a>
<a id="l01928"></a>
<a id="l01929"></a>
<a id="l01930"></a>
<a id="l01931"></a>
<a id="l01967"></a>
<a id="l01968"></a>
<a id="l01969"></a>
<a id="l01970"></a>
<a id="l01971"></a>
<a id="l01990"></a>
<a id="l01991"></a>
<a id="l01992"></a>
<a id="l01993"></a>
<a id="foldopen01995"></a>
<a id="l01995"></a>
<a id="l01997"></a>
<a id="l02002"></a>
<a id="l02003"></a>
<a id="l02004"></a>
<a id="l02006"></a>
<a id="l02008"></a>
<a id="l02009"></a>
<a id="l02010"></a>
<a id="l02014"></a>
<a id="l02025"></a>
<a id="l02026"></a>
<a id="l02027"></a>
<a id="l02039"></a>
<a id="l02049"></a>
<a id="l02051"></a>
<a id="l02052"></a>
<a id="l02053"></a>
<a id="l02054"></a>
<a id="l02056"></a>
<a id="l02057"></a>
<a id="l02059"></a>
<a id="l02060"></a>
<a id="l02061"></a>
<a id="l02104"></a>
<a id="l02105"></a>
<a id="l02106"></a>
<a id="l02107"></a>
<a id="l02115"></a>
<a id="l02116"></a>
<a id="l02117"></a>
<a id="foldopen02119"></a>
<a id="l02119"></a>
<a id="l02121"></a>
<a id="l02123"></a>
<a id="l02125"></a>
<a id="l02127"></a>
<a id="l02129"></a>
<a id="l02130"></a>
<a id="l02132"></a>
<a id="l02133"></a>
<a id="l02134"></a>
<a id="l02135"></a>
<a id="l02154"></a>
<a id="l02155"></a>
<a id="l02182"></a>
<a id="l02183"></a>
<a id="l02184"></a>
<a id="l02185"></a>
<a id="l02186"></a>
<a id="foldopen02205"></a>
<a id="l02205"></a>
<a id="l02206"></a>
<a id="l02207"></a>
<a id="l02208"></a>
<a id="l02209"></a>
<a id="l02210"></a>
<a id="l02211"></a>
<a id="l02212"></a>
<a id="l02213"></a>
<a id="l02214"></a>
<a id="l02231"></a>
<a id="l02232"></a>
<a id="l02233"></a>
<a id="l02234"></a>
<a id="l02242"></a>
<a id="l02243"></a>
<a id="l02244"></a>
<a id="foldopen02246"></a>
<a id="l02246"></a>
<a id="l02256"></a>
<a id="l02257"></a>
<a id="l02270"></a>
<a id="l02271"></a>
<a id="l02279"></a>
<a id="l02280"></a>
<a id="l02291"></a>
<a id="l02292"></a>
<a id="l02293"></a>
<a id="l02294"></a>
<a id="l02295"></a>
<a id="foldopen02297"></a>
<a id="l02297"></a>
<a id="l02299"></a>
<a id="l02303"></a>
<a id="l02304"></a>
<a id="l02306"></a>
<a id="l02308"></a>
<a id="l02309"></a>
<a id="l02311"></a>
<a id="l02313"></a>
<a id="l02314"></a>
<a id="l02316"></a>
<a id="l02317"></a>
<a id="l02322"></a>
<a id="l02323"></a>
<a id="l02325"></a>
<a id="l02326"></a>
<a id="l02330"></a>
<a id="l02332"></a>
<a id="l02334"></a>
<a id="l02335"></a>
<a id="l02336"></a>
<a id="l02337"></a>
<a id="l02372"></a>
<a id="l02373"></a>
<a id="l02374"></a>
<a id="l02391"></a>
<a id="l02392"></a>
<a id="l02393"></a>
<a id="l02417"></a>
<a id="l02418"></a>
<a id="l02419"></a>
<a id="l02437"></a>
<a id="l02438"></a>
<a id="l02440"></a>
<a id="l02441"></a>
<a id="l02442"></a>
<a id="l02443"></a>
<a id="l02444"></a>
<a id="l02448"></a>
<a id="l02449"></a>
<a id="aaddr_8h_html"></a>
<a id="aatomic_8h_html"></a>
<a id="aatt_8h_html"></a>
<a id="abluetooth_2uuid_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__atomic__apis_html_ga249c575db9764486197709b327f7370e"></a>
<a id="agroup__bt__att_html_gac593a27ecf029f33f50f990b2947562c"></a>
<a id="agroup__bt__att_html_gad2305f28744276d97aefd26bdb79023c"></a>
<a id="agroup__bt__att_html_ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739"></a>
<a id="agroup__bt__conn_html_gaf0c56cd26c4147f6c9f0faa11fa01783"></a>
<a id="agroup__bt__gatt__client_html_ga0f41da23c6559a8254b04295aff8198d"></a>
<a id="agroup__bt__gatt__client_html_ga1a18dd726ab960a88d7f85f2a014141a"></a>
<a id="agroup__bt__gatt__client_html_ga1ca94b4f2b6c456b6134e05127993569"></a>
<a id="agroup__bt__gatt__client_html_ga2bca8c4a45f41e0400a9e0147f4baf50"></a>
<a id="agroup__bt__gatt__client_html_ga2e914e63b4b91fa56bc3295283c43714"></a>
<a id="agroup__bt__gatt__client_html_ga49439413d12b5a8a1c68735e961ab6fa"></a>
<a id="agroup__bt__gatt__client_html_ga5193dea59a016692f94cf950d6b4f4f7"></a>
<a id="agroup__bt__gatt__client_html_ga56509c9b8f73f729cfa5e75be22d79ae"></a>
<a id="agroup__bt__gatt__client_html_ga791b8bb8a4c085b022fafc0535a63511"></a>
<a id="agroup__bt__gatt__client_html_ga7d4a8e18f51ba6476886a15f81f48e5c"></a>
<a id="agroup__bt__gatt__client_html_ga843a42e68e0497d88d3f655f8ffd58d4"></a>
<a id="agroup__bt__gatt__client_html_ga9fc78e32230637a6f092da2400c50fe7"></a>
<a id="agroup__bt__gatt__client_html_gaa43f45658809908baa72bf4e0ea745ac"></a>
<a id="agroup__bt__gatt__client_html_gab3e53eb5f9bb1eda7bf612ef95755b4d"></a>
<a id="agroup__bt__gatt__client_html_gabd3bcd3c1560956726574faed332fb13"></a>
<a id="agroup__bt__gatt__client_html_gac06a945e5f7939b6716bc4f2cea781bd"></a>
<a id="agroup__bt__gatt__client_html_gaea89c65f17050820d54568f636b6554a"></a>
<a id="agroup__bt__gatt__client_html_ggaa43f45658809908baa72bf4e0ea745aca30bfd3fb4bf4f17653ba00942ba2b2e6"></a>
<a id="agroup__bt__gatt__client_html_ggaa43f45658809908baa72bf4e0ea745aca5640a1e06740a89859c5f4b183d58e79"></a>
<a id="agroup__bt__gatt__client_html_ggaa43f45658809908baa72bf4e0ea745aca56aa5f332d4098e3942d7a902198f7ab"></a>
<a id="agroup__bt__gatt__client_html_ggaa43f45658809908baa72bf4e0ea745acaecdcb3baa850505f459523091c92a1cb"></a>
<a id="agroup__bt__gatt__client_html_ggaa43f45658809908baa72bf4e0ea745acafe1c3dc9380c33debd32a275d5bce8ad"></a>
<a id="agroup__bt__gatt__client_html_ggaea89c65f17050820d54568f636b6554aa0ccb2587aa8f21361c5d73847a33ecbe"></a>
<a id="agroup__bt__gatt__client_html_ggaea89c65f17050820d54568f636b6554aa21be62548b816c7960a54dd6e3b37a97"></a>
<a id="agroup__bt__gatt__client_html_ggaea89c65f17050820d54568f636b6554aa71355dfe0bf30c88f9fe2f7da1ba10ae"></a>
<a id="agroup__bt__gatt__client_html_ggaea89c65f17050820d54568f636b6554aa80afff1c83bb5ebb5603af699f2c26da"></a>
<a id="agroup__bt__gatt__client_html_ggaea89c65f17050820d54568f636b6554aa81a1f8737c415544a0f793f4e626bb61"></a>
<a id="agroup__bt__gatt__client_html_ggaea89c65f17050820d54568f636b6554aada9ac33aa77f6043da8133dcf269478f"></a>
<a id="agroup__bt__gatt__client_html_ggaea89c65f17050820d54568f636b6554aafe2167b873b848935d56f6ee7f2c444c"></a>
<a id="agroup__bt__gatt__server_html_ga1294850e6bdcbe7a8f42f2956fd837a8"></a>
<a id="agroup__bt__gatt__server_html_ga24bae284dbc71cd4075649c4bc348b7c"></a>
<a id="agroup__bt__gatt__server_html_ga270c8a52bf3d512defc373f8c29b59f2"></a>
<a id="agroup__bt__gatt__server_html_ga29421c8788b47b6a648704d27d5f0d28"></a>
<a id="agroup__bt__gatt__server_html_ga2d51136ea1bd6cdb50900639506fd9f7"></a>
<a id="agroup__bt__gatt__server_html_ga2e85b42136e2c6a4cb5b7ad8a2532573"></a>
<a id="agroup__bt__gatt__server_html_ga351fd7658eaecbbfa60f1769119ef733"></a>
<a id="agroup__bt__gatt__server_html_ga35cecaa43b00b374062d29cca1479d85"></a>
<a id="agroup__bt__gatt__server_html_ga4313a63decac2c8b7c4a1764df3d53ea"></a>
<a id="agroup__bt__gatt__server_html_ga4f2272692cc0f1d44638828012296c80"></a>
<a id="agroup__bt__gatt__server_html_ga55e3ef7cb43b8acb0a27643c78390146"></a>
<a id="agroup__bt__gatt__server_html_ga5893166f1b24f437a94ccf1fc57c7917"></a>
<a id="agroup__bt__gatt__server_html_ga5ae96590a0aaa5c4c3863a4a14d80fdd"></a>
<a id="agroup__bt__gatt__server_html_ga5d47ed9eaea22c8f00db14329daee8fe"></a>
<a id="agroup__bt__gatt__server_html_ga5eee6afc6db391ffeda295d298bf6a56"></a>
<a id="agroup__bt__gatt__server_html_ga5fb25c5eec91045dc4c7fd61ef7e528e"></a>
<a id="agroup__bt__gatt__server_html_ga60284611c90729b289fe806524ba9209"></a>
<a id="agroup__bt__gatt__server_html_ga6653de5e245cae6dc12cd0b45acbe028"></a>
<a id="agroup__bt__gatt__server_html_ga74ee552864c563aa5bc939f37395c14a"></a>
<a id="agroup__bt__gatt__server_html_ga8071d6063f85c0a78155f6b2ac2da635"></a>
<a id="agroup__bt__gatt__server_html_ga99738cf4f05eae4c6da17cc3420827d8"></a>
<a id="agroup__bt__gatt__server_html_gaa93b5e0f2870ed135447bead903c175a"></a>
<a id="agroup__bt__gatt__server_html_gab38994257f53473e62e01eff8f236ee1"></a>
<a id="agroup__bt__gatt__server_html_gab4d9cfea04e44445d5dc30ad52842b64"></a>
<a id="agroup__bt__gatt__server_html_gabba965b676650a55cb9934072b34c75e"></a>
<a id="agroup__bt__gatt__server_html_gabd4df0a264dae10e43797992a567be7d"></a>
<a id="agroup__bt__gatt__server_html_gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00"></a>
<a id="agroup__bt__gatt__server_html_gac55832607b95f394d26a64ed1cfe5bba"></a>
<a id="agroup__bt__gatt__server_html_gacae81c0f272bad7e6ac93c0d13b678c6"></a>
<a id="agroup__bt__gatt__server_html_gad2f3272b1dc42378104b492ec7caf6b0"></a>
<a id="agroup__bt__gatt__server_html_gad58b526a06334530c13292d14a11257c"></a>
<a id="agroup__bt__gatt__server_html_gad8d8f513004f391167212d7bf9f7ff10"></a>
<a id="agroup__bt__gatt__server_html_gae5c1e8b7bb1e673e228f03d1d084be9a"></a>
<a id="agroup__bt__gatt__server_html_gaf5bf0205fad5f7ad187b764d23deba6b"></a>
<a id="agroup__bt__gatt__server_html_gaf6d253849932b706ec7f303568980dfa"></a>
<a id="agroup__bt__gatt__server_html_gaf6d3f1e904f1a847afeb30236bad98a2"></a>
<a id="agroup__bt__gatt__server_html_ggab38994257f53473e62e01eff8f236ee1aa3f2a25e27c7065a2c7bb2a9ff09542e"></a>
<a id="agroup__bt__gatt__server_html_ggab38994257f53473e62e01eff8f236ee1aea569feffa4815d3443e12be78c684f5"></a>
<a id="agroup__bt__gatt_html_ga3fd8527a0f3e8f3699dc0d3b0339eba1"></a>
<a id="agroup__bt__gatt_html_ga57e36bf94652531964fd4237c203fe7b"></a>
<a id="agroup__bt__gatt_html_ga830d437c8d0757f53af1de6aa3031906"></a>
<a id="agroup__bt__gatt_html_ga96e57500d2340a45badb23701cc43833"></a>
<a id="agroup__bt__gatt_html_gga830d437c8d0757f53af1de6aa3031906a019cf6118a0cfacbfad20c1cc5838383"></a>
<a id="agroup__bt__gatt_html_gga830d437c8d0757f53af1de6aa3031906a770df41b7d433e8ce349b19e4657ba78"></a>
<a id="agroup__bt__gatt_html_gga830d437c8d0757f53af1de6aa3031906ad4e8f43c03da10c15685bd1a0109708b"></a>
<a id="agroup__bt__gatt_html_gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d"></a>
<a id="agroup__bt__gatt_html_gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf"></a>
<a id="agroup__bt__gatt_html_gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f"></a>
<a id="agroup__bt__gatt_html_gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a"></a>
<a id="agroup__bt__gatt_html_gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17"></a>
<a id="agroup__bt__gatt_html_gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79"></a>
<a id="agroup__bt__gatt_html_gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94"></a>
<a id="agroup__bt__gatt_html_gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583"></a>
<a id="agroup__bt__gatt_html_gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266"></a>
<a id="agroup__bt__gatt_html_gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astring_8h_html"></a>
<a id="astring_8h_html_a4137694174d4ca2fad886a1db355015c"></a>
<a id="astructbt__addr__le__t_html"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__gatt__attr_html"></a>
<a id="astructbt__gatt__attr_html_a074abc719494ca35997a452f526e7ecc"></a>
<a id="astructbt__gatt__attr_html_a0849a40254622080d05e8559c4fdb9e2"></a>
<a id="astructbt__gatt__attr_html_a1ecd78536067f4bded506e0daccefd35"></a>
<a id="astructbt__gatt__attr_html_a6958f507f9ff172018be458ebc86106f"></a>
<a id="astructbt__gatt__attr_html_adeb063fb101fab45dd789c7212c43357"></a>
<a id="astructbt__gatt__attr_html_aeee42a3d3ca15e40cf11cc0c3fde106b"></a>
<a id="astructbt__gatt__authorization__cb_html"></a>
<a id="astructbt__gatt__authorization__cb_html_a7b1bcbe10f12c90ee4e3214e36e9c2a3"></a>
<a id="astructbt__gatt__authorization__cb_html_a7c12bd14f87f91e672eaaf92e1aa6e7b"></a>
<a id="astructbt__gatt__cb_html"></a>
<a id="astructbt__gatt__cb_html_a93fe1a626ab59c38ef56f02671f88980"></a>
<a id="astructbt__gatt__ccc__cfg_html"></a>
<a id="astructbt__gatt__ccc__cfg_html_a92acf7329f66638ac6c657c8eaa795ac"></a>
<a id="astructbt__gatt__ccc__cfg_html_ab316080693b2c4daf5fd45e2c0501c70"></a>
<a id="astructbt__gatt__ccc__cfg_html_ac17ddefe7ca6dbac921ee4c6f44fbf51"></a>
<a id="astructbt__gatt__ccc__managed__user__data_html"></a>
<a id="astructbt__gatt__ccc__managed__user__data_html_a166073fca5a342b859fb42482547b80c"></a>
<a id="astructbt__gatt__ccc__managed__user__data_html_a44987dc5be9442436f6033c30bbb42fd"></a>
<a id="astructbt__gatt__ccc__managed__user__data_html_a7ba4c03ef2a0c2c85e17ef1147934536"></a>
<a id="astructbt__gatt__ccc__managed__user__data_html_a883177671ea068f1dcbab36197abfdfd"></a>
<a id="astructbt__gatt__ccc__managed__user__data_html_afc0c5226be7d9b2d3d039f86960a2ed3"></a>
<a id="astructbt__gatt__ccc_html"></a>
<a id="astructbt__gatt__ccc_html_ac8fa1028c5e87aa025832257b18fa7c3"></a>
<a id="astructbt__gatt__cep_html"></a>
<a id="astructbt__gatt__cep_html_a317442dc204f7632b0c5da8a8a9a98b5"></a>
<a id="astructbt__gatt__chrc_html"></a>
<a id="astructbt__gatt__chrc_html_a2ca6aec1a621fdfd12142a1188d37bd3"></a>
<a id="astructbt__gatt__chrc_html_a81bb8257052d7c8d03b51acaa51e5011"></a>
<a id="astructbt__gatt__chrc_html_af3b4c22ae37b912c8edf58294cc50702"></a>
<a id="astructbt__gatt__cpf_html"></a>
<a id="astructbt__gatt__cpf_html_a1dfbb9fc1e1397d2abec04b216d7ae33"></a>
<a id="astructbt__gatt__cpf_html_a2a9f3d3f72b9acb1ef7f2dc765e5a231"></a>
<a id="astructbt__gatt__cpf_html_a3690a86c942badb2d2698481b03e436d"></a>
<a id="astructbt__gatt__cpf_html_a3c48dd5ea717fbaf510d13c64a370c06"></a>
<a id="astructbt__gatt__cpf_html_ab0ca135a75130b3ffc0c5bf375f3528f"></a>
<a id="astructbt__gatt__discover__params_html"></a>
<a id="astructbt__gatt__discover__params_html_a0d2604e7c3ee8969cb5096cbf5793fdb"></a>
<a id="astructbt__gatt__discover__params_html_a225868498c34411cc3fc2be8e678e85e"></a>
<a id="astructbt__gatt__discover__params_html_a337d7366c12451938f12eec4dc60903e"></a>
<a id="astructbt__gatt__discover__params_html_a65ca3c9aad7c02d48fd35c4d6f69dc70"></a>
<a id="astructbt__gatt__discover__params_html_a77d6665c01902e4e23cf8de8a9436262"></a>
<a id="astructbt__gatt__discover__params_html_a87b130c520ce50f835d0589fd22a844c"></a>
<a id="astructbt__gatt__discover__params_html_ab0f056c90954e1246d897019abd1e7fc"></a>
<a id="astructbt__gatt__discover__params_html_aba7585e3d0eefb323fcde9bcc88e287d"></a>
<a id="astructbt__gatt__exchange__params_html"></a>
<a id="astructbt__gatt__exchange__params_html_a76f4d3e779da9c725914574ac2e22ad1"></a>
<a id="astructbt__gatt__include_html"></a>
<a id="astructbt__gatt__include_html_a54d20cebfd6ba62b692c363acdc25d61"></a>
<a id="astructbt__gatt__include_html_ac7f6c1a8018f483dce14f0fe21031232"></a>
<a id="astructbt__gatt__include_html_afa028e8daae00e3b1bc0b866c4335af3"></a>
<a id="astructbt__gatt__indicate__params_html"></a>
<a id="astructbt__gatt__indicate__params_html_a0e536938123ecb4f3ba6736c1de2a599"></a>
<a id="astructbt__gatt__indicate__params_html_a10ad44140371165951eeac18cb3d0e7f"></a>
<a id="astructbt__gatt__indicate__params_html_acbbee3a71838492416b20bb5cff89801"></a>
<a id="astructbt__gatt__indicate__params_html_ae1d657512c99d5bba6fc99a450a6da32"></a>
<a id="astructbt__gatt__indicate__params_html_aeb346dc4c0e4a298c66f394d037a6514"></a>
<a id="astructbt__gatt__indicate__params_html_af9eb83c3fba49ee3cd6162d5a2791707"></a>
<a id="astructbt__gatt__indicate__params_html_afde06f47d7a817291e437593ea01bccd"></a>
<a id="astructbt__gatt__notify__params_html"></a>
<a id="astructbt__gatt__notify__params_html_a2994cbe737fad725c60427000c21c373"></a>
<a id="astructbt__gatt__notify__params_html_a4a511da0b099ca88d895594caf7aaa6a"></a>
<a id="astructbt__gatt__notify__params_html_a6187d0457763a15a623129e3e9e98e13"></a>
<a id="astructbt__gatt__notify__params_html_a978d7a42c39a098cedf751936f280fac"></a>
<a id="astructbt__gatt__notify__params_html_ace3c6b5f5ed78b9f64c25b868d3bfbe2"></a>
<a id="astructbt__gatt__notify__params_html_adec9a6f6ea0604e82b90dd47bb9951fa"></a>
<a id="astructbt__gatt__notify__params_html_afaa276cff9cbf204c433ca776904ef32"></a>
<a id="astructbt__gatt__read__params_html"></a>
<a id="astructbt__gatt__read__params_html_a0a36063ac0b110fbf57ef6a66f7bece8"></a>
<a id="astructbt__gatt__read__params_html_a1335d1f9aefeff89a57efe78335cb41b"></a>
<a id="astructbt__gatt__read__params_html_a2794b8806933d0e16cfc77f4087fdeda"></a>
<a id="astructbt__gatt__read__params_html_a27f685a45c405bb2784fe369513724ad"></a>
<a id="astructbt__gatt__read__params_html_a3ea107db0b7537c9dccb2aa6d8f916fb"></a>
<a id="astructbt__gatt__read__params_html_a4cf61907bb95a2be6513d214b7030723"></a>
<a id="astructbt__gatt__read__params_html_a521f5d1859dd9271fa2c595012dacd25"></a>
<a id="astructbt__gatt__read__params_html_a77d05cbc54b125fc35d180cf91bf9cb9"></a>
<a id="astructbt__gatt__read__params_html_a86b81f185490e63a07d2a62dd26a7f74"></a>
<a id="astructbt__gatt__read__params_html_a8b2a2b912efe557e24276a654087e75c"></a>
<a id="astructbt__gatt__read__params_html_ac11db1652cd5cee567d666d3697f3a4b"></a>
<a id="astructbt__gatt__read__params_html_ae2ba6ce4043769b86a050fd767248111"></a>
<a id="astructbt__gatt__read__params_html_af37beb6a69b3a6b90da0594b099bd64d"></a>
<a id="astructbt__gatt__scc_html"></a>
<a id="astructbt__gatt__scc_html_aa7ddf1810f6d47e59c364b7489823d00"></a>
<a id="astructbt__gatt__service__static_html"></a>
<a id="astructbt__gatt__service__static_html_a38f9e02241fe37f68df5dd8782b59e9f"></a>
<a id="astructbt__gatt__service__static_html_a84c35a391e372396e2ec89eaf0d4d047"></a>
<a id="astructbt__gatt__service__val_html"></a>
<a id="astructbt__gatt__service__val_html_a683e01db92400e76aed32b7a81369a55"></a>
<a id="astructbt__gatt__service__val_html_a75b6fcf0f9f29ad05ccac0e83bcb31b7"></a>
<a id="astructbt__gatt__service_html"></a>
<a id="astructbt__gatt__service_html_a0281e96ab54519df641f6c489fdc6b5b"></a>
<a id="astructbt__gatt__service_html_a87d8316a92ae04678d7be0ae76ed86cb"></a>
<a id="astructbt__gatt__subscribe__params_html"></a>
<a id="astructbt__gatt__subscribe__params_html_a3bff1209b7a0b5908408a568622d0150"></a>
<a id="astructbt__gatt__subscribe__params_html_a5b34bad1cf39bb3efd5faf516473dd4a"></a>
<a id="astructbt__gatt__subscribe__params_html_a77c53cdfd4143483b33a8ecf6061561e"></a>
<a id="astructbt__gatt__subscribe__params_html_a91595407b8de4e862652e41100668f0a"></a>
<a id="astructbt__gatt__subscribe__params_html_a9248418eb04a5b7a0faed5077c40bf22"></a>
<a id="astructbt__gatt__subscribe__params_html_acf237ef097e8b847eb049fb0a5d4b759"></a>
<a id="astructbt__gatt__subscribe__params_html_ad3a3b9335b85777d65bdf875486e292a"></a>
<a id="astructbt__gatt__subscribe__params_html_ae139848da09705d37fe7c9de4c1a4087"></a>
<a id="astructbt__gatt__subscribe__params_html_aedd24024881e22372505355024cd716b"></a>
<a id="astructbt__gatt__subscribe__params_html_af806d24aa97db1f2e9a021e719598a6d"></a>
<a id="astructbt__gatt__write__params_html"></a>
<a id="astructbt__gatt__write__params_html_a3468e3b75f3f9eda12bc4963f48cf9aa"></a>
<a id="astructbt__gatt__write__params_html_a384c5c15f248df5b327423ca32637bad"></a>
<a id="astructbt__gatt__write__params_html_ab6510ef242e73325adb074322746c27c"></a>
<a id="astructbt__gatt__write__params_html_ad79905c16f7ba5289817de552ece1a48"></a>
<a id="astructbt__gatt__write__params_html_add53cc08465d28f33bc48a1e8649ac1a"></a>
<a id="astructbt__gatt__write__params_html_aded956dac2d398b642faeec81fdb9ec3"></a>
<a id="astructbt__uuid_html"></a>
<a id="astructuuid_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2015-2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_GATT_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_GATT_H_


#include <stdint.h>
#include <stddef.h>
#include <string.h>

#include <sys/types.h>

#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/bluetooth/att.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif

enum bt_gatt_perm {
        BT_GATT_PERM_NONE = 0,

        BT_GATT_PERM_READ = BIT(0),

        BT_GATT_PERM_WRITE = BIT(1),

        BT_GATT_PERM_READ_ENCRYPT = BIT(2),

        BT_GATT_PERM_WRITE_ENCRYPT = BIT(3),

        BT_GATT_PERM_READ_AUTHEN = BIT(4),

        BT_GATT_PERM_WRITE_AUTHEN = BIT(5),

        BT_GATT_PERM_PREPARE_WRITE = BIT(6),

        BT_GATT_PERM_READ_LESC = BIT(7),

        BT_GATT_PERM_WRITE_LESC = BIT(8),
};

#define BT_GATT_ERR(_att_err) (-(_att_err))

enum bt_gatt_attr_write_flag {
        BT_GATT_WRITE_FLAG_PREPARE = BIT(0),

        BT_GATT_WRITE_FLAG_CMD = BIT(1),

        BT_GATT_WRITE_FLAG_EXECUTE = BIT(2),
};

/* Forward declaration of GATT Attribute structure */
struct bt_gatt_attr;

typedef ssize_t (*bt_gatt_attr_read_func_t)(struct bt_conn *conn,
                                            const struct bt_gatt_attr *attr,
                                            void *buf, uint16_t len,
                                            uint16_t offset);

typedef ssize_t (*bt_gatt_attr_write_func_t)(struct bt_conn *conn,
                                             const struct bt_gatt_attr *attr,
                                             const void *buf, uint16_t len,
                                             uint16_t offset, uint8_t flags);

struct bt_gatt_attr {
        const struct bt_uuid *uuid;

        bt_gatt_attr_read_func_t read;

        bt_gatt_attr_write_func_t write;

        void *user_data;

        uint16_t handle;

        uint16_t perm: 15;

        bool _auto_assigned_handle: 1;
};

struct bt_gatt_service_static {
        const struct bt_gatt_attr *attrs;
        size_t attr_count;
};

struct bt_gatt_service {
        struct bt_gatt_attr *attrs;
        size_t attr_count;
        sys_snode_t node;
};

struct bt_gatt_service_val {
        const struct bt_uuid *uuid;
        uint16_t end_handle;
};

struct bt_gatt_include {
        const struct bt_uuid *uuid;
        uint16_t start_handle;
        uint16_t end_handle;
};

struct bt_gatt_cb {
        void (*att_mtu_updated)(struct bt_conn *conn, uint16_t tx, uint16_t rx);

        sys_snode_t node;
};

struct bt_gatt_authorization_cb {
        bool (*read_authorize)(struct bt_conn *conn,
                               const struct bt_gatt_attr *attr);

        bool (*write_authorize)(struct bt_conn *conn,
                                const struct bt_gatt_attr *attr);
};


#define BT_GATT_CHRC_BROADCAST                  0x01
#define BT_GATT_CHRC_READ                       0x02
#define BT_GATT_CHRC_WRITE_WITHOUT_RESP         0x04
#define BT_GATT_CHRC_WRITE                      0x08
#define BT_GATT_CHRC_NOTIFY                     0x10
#define BT_GATT_CHRC_INDICATE                   0x20
#define BT_GATT_CHRC_AUTH                       0x40 __DEPRECATED_MACRO
#define BT_GATT_CHRC_EXT_PROP                   0x80

struct bt_gatt_chrc {
        const struct bt_uuid *uuid;
        uint16_t value_handle;
        uint8_t properties;
};


#define BT_GATT_CEP_RELIABLE_WRITE              0x0001

#define BT_GATT_CEP_WRITABLE_AUX                0x0002

struct bt_gatt_cep {
        uint16_t properties;
};


#define BT_GATT_CCC_NOTIFY                      0x0001
#define BT_GATT_CCC_INDICATE                    0x0002

struct bt_gatt_ccc {
        uint16_t flags;
};


#define BT_GATT_SCC_BROADCAST                   0x0001

struct bt_gatt_scc {
        uint16_t flags;
};

struct bt_gatt_cpf {
        uint8_t format;
        int8_t exponent;
        uint16_t unit;
        uint8_t name_space;
        uint16_t description;
};


static inline const char *bt_gatt_err_to_str(int gatt_err)
{
        return bt_att_err_to_str((gatt_err) < 0 ? -(gatt_err) : (gatt_err));
}

void bt_gatt_cb_register(struct bt_gatt_cb *cb);

int bt_gatt_cb_unregister(struct bt_gatt_cb *cb);

int bt_gatt_authorization_cb_register(const struct bt_gatt_authorization_cb *cb);

int bt_gatt_service_register(struct bt_gatt_service *svc);

int bt_gatt_service_unregister(struct bt_gatt_service *svc);

bool bt_gatt_service_is_registered(const struct bt_gatt_service *svc);

enum bt_gatt_iter {
        BT_GATT_ITER_STOP = 0,
        BT_GATT_ITER_CONTINUE,
};

typedef uint8_t (*bt_gatt_attr_func_t)(const struct bt_gatt_attr *attr,
                                       uint16_t handle,
                                       void *user_data);

void bt_gatt_foreach_attr_type(uint16_t start_handle, uint16_t end_handle,
                               const struct bt_uuid *uuid,
                               const void *attr_data, uint16_t num_matches,
                               bt_gatt_attr_func_t func,
                               void *user_data);

static inline void bt_gatt_foreach_attr(uint16_t start_handle, uint16_t end_handle,
                                        bt_gatt_attr_func_t func,
                                        void *user_data)
{
        bt_gatt_foreach_attr_type(start_handle, end_handle, NULL, NULL, 0, func,
                                  user_data);
}

struct bt_gatt_attr *bt_gatt_attr_next(const struct bt_gatt_attr *attr);

struct bt_gatt_attr *bt_gatt_find_by_uuid(const struct bt_gatt_attr *attr,
                                          uint16_t attr_count,
                                          const struct bt_uuid *uuid);

uint16_t bt_gatt_attr_get_handle(const struct bt_gatt_attr *attr);

uint16_t bt_gatt_attr_value_handle(const struct bt_gatt_attr *attr);

ssize_t bt_gatt_attr_read(struct bt_conn *conn, const struct bt_gatt_attr *attr,
                          void *buf, uint16_t buf_len, uint16_t offset,
                          const void *value, uint16_t value_len);

ssize_t bt_gatt_attr_read_service(struct bt_conn *conn,
                                  const struct bt_gatt_attr *attr,
                                  void *buf, uint16_t len, uint16_t offset);

#define BT_GATT_SERVICE_DEFINE(_name, ...)                              \
        const struct bt_gatt_attr attr_##_name[] = { __VA_ARGS__ };     \
        const STRUCT_SECTION_ITERABLE(bt_gatt_service_static, _name) =  \
                                        BT_GATT_SERVICE(attr_##_name)

#define _BT_GATT_ATTRS_ARRAY_DEFINE(n, _instances, _attrs_def)  \
        static struct bt_gatt_attr attrs_##n[] = _attrs_def(_instances[n])

#define _BT_GATT_SERVICE_ARRAY_ITEM(_n, _) BT_GATT_SERVICE(attrs_##_n)

#define BT_GATT_SERVICE_INSTANCE_DEFINE(                                 \
        _name, _instances, _instance_num, _attrs_def)                    \
        BUILD_ASSERT(ARRAY_SIZE(_instances) == _instance_num,            \
                "The number of array elements does not match its size"); \
        LISTIFY(_instance_num, _BT_GATT_ATTRS_ARRAY_DEFINE, (;),         \
                _instances, _attrs_def);                                 \
        static struct bt_gatt_service _name[] = {                        \
                LISTIFY(_instance_num, _BT_GATT_SERVICE_ARRAY_ITEM, (,)) \
        }

#define BT_GATT_SERVICE(_attrs)                                         \
{                                                                       \
        .attrs = _attrs,                                                \
        .attr_count = ARRAY_SIZE(_attrs),                               \
}

#define BT_GATT_PRIMARY_SERVICE(_service)                               \
        BT_GATT_ATTRIBUTE(BT_UUID_GATT_PRIMARY, BT_GATT_PERM_READ,      \
                         bt_gatt_attr_read_service, NULL, (void *)_service)

#define BT_GATT_SECONDARY_SERVICE(_service)                             \
        BT_GATT_ATTRIBUTE(BT_UUID_GATT_SECONDARY, BT_GATT_PERM_READ,    \
                         bt_gatt_attr_read_service, NULL, (void *)_service)

ssize_t bt_gatt_attr_read_included(struct bt_conn *conn,
                                   const struct bt_gatt_attr *attr,
                                   void *buf, uint16_t len, uint16_t offset);

#define BT_GATT_INCLUDE_SERVICE(_service_incl)                          \
        BT_GATT_ATTRIBUTE(BT_UUID_GATT_INCLUDE, BT_GATT_PERM_READ,      \
                          bt_gatt_attr_read_included, NULL, _service_incl)

ssize_t bt_gatt_attr_read_chrc(struct bt_conn *conn,
                               const struct bt_gatt_attr *attr, void *buf,
                               uint16_t len, uint16_t offset);

#define BT_GATT_CHRC_INIT(_uuid, _handle, _props) \
{                                                 \
        .uuid = _uuid,                            \
        .value_handle = _handle,                  \
        .properties = _props,                     \
}

#define BT_GATT_CHARACTERISTIC(_uuid, _props, _perm, _read, _write, _user_data) \
        BT_GATT_ATTRIBUTE(BT_UUID_GATT_CHRC, BT_GATT_PERM_READ,                 \
                          bt_gatt_attr_read_chrc, NULL,                         \
                          ((struct bt_gatt_chrc[]) {                            \
                                BT_GATT_CHRC_INIT(_uuid, 0U, _props),           \
                                                   })),                         \
        BT_GATT_ATTRIBUTE(_uuid, _perm, _read, _write, _user_data)

#if defined(CONFIG_BT_SETTINGS_CCC_LAZY_LOADING)
        #define BT_GATT_CCC_MAX (CONFIG_BT_MAX_CONN)
#elif defined(CONFIG_BT_CONN)
        #define BT_GATT_CCC_MAX (CONFIG_BT_MAX_PAIRED + CONFIG_BT_MAX_CONN)
#else
        #define BT_GATT_CCC_MAX 0
#endif

struct bt_gatt_ccc_cfg {
        uint8_t id;
        bt_addr_le_t peer;
        uint16_t value;
};

struct bt_gatt_ccc_managed_user_data {
        struct bt_gatt_ccc_cfg cfg[BT_GATT_CCC_MAX];

        uint16_t value;

        void (*cfg_changed)(const struct bt_gatt_attr *attr, uint16_t value);

        ssize_t (*cfg_write)(struct bt_conn *conn,
                             const struct bt_gatt_attr *attr, uint16_t value);

        bool (*cfg_match)(struct bt_conn *conn,
                          const struct bt_gatt_attr *attr);
};

ssize_t bt_gatt_attr_read_ccc(struct bt_conn *conn,
                              const struct bt_gatt_attr *attr, void *buf,
                              uint16_t len, uint16_t offset);

ssize_t bt_gatt_attr_write_ccc(struct bt_conn *conn,
                               const struct bt_gatt_attr *attr, const void *buf,
                               uint16_t len, uint16_t offset, uint8_t flags);

#define BT_GATT_CCC_MANAGED_USER_DATA_INIT(_changed, _write, _match)                               \
        {                                                                                          \
                .cfg = {},                                                                         \
                .cfg_changed = _changed,                                                           \
                .cfg_write = _write,                                                               \
                .cfg_match = _match,                                                               \
        }

#define BT_GATT_CCC_MANAGED(_ccc, _perm)                                \
        BT_GATT_ATTRIBUTE(BT_UUID_GATT_CCC, _perm,                      \
                        bt_gatt_attr_read_ccc, bt_gatt_attr_write_ccc,  \
                        _ccc)

#define BT_GATT_CCC(_changed, _perm)                                                               \
        BT_GATT_CCC_MANAGED(((struct bt_gatt_ccc_managed_user_data[]){                             \
                                    BT_GATT_CCC_MANAGED_USER_DATA_INIT(_changed, NULL, NULL)}),    \
                            _perm)

#define BT_GATT_CCC_WITH_WRITE_CB(_changed, _write, _perm)                                         \
        BT_GATT_CCC_MANAGED(((struct bt_gatt_ccc_managed_user_data[]){                             \
                                    BT_GATT_CCC_MANAGED_USER_DATA_INIT(_changed, _write, NULL)}),  \
                            _perm)

ssize_t bt_gatt_attr_read_cep(struct bt_conn *conn,
                              const struct bt_gatt_attr *attr, void *buf,
                              uint16_t len, uint16_t offset);

#define BT_GATT_CEP(_value)                                             \
        BT_GATT_DESCRIPTOR(BT_UUID_GATT_CEP, BT_GATT_PERM_READ,         \
                          bt_gatt_attr_read_cep, NULL, (void *)_value)

ssize_t bt_gatt_attr_read_cud(struct bt_conn *conn,
                              const struct bt_gatt_attr *attr, void *buf,
                              uint16_t len, uint16_t offset);

#define BT_GATT_CUD(_value, _perm)                                      \
        BT_GATT_DESCRIPTOR(BT_UUID_GATT_CUD, _perm, bt_gatt_attr_read_cud, \
                           NULL, (void *)_value)

ssize_t bt_gatt_attr_read_cpf(struct bt_conn *conn,
                              const struct bt_gatt_attr *attr, void *buf,
                              uint16_t len, uint16_t offset);

#define BT_GATT_CPF(_value)                                             \
        BT_GATT_DESCRIPTOR(BT_UUID_GATT_CPF, BT_GATT_PERM_READ,         \
                          bt_gatt_attr_read_cpf, NULL, (void *)_value)

#define BT_GATT_DESCRIPTOR(_uuid, _perm, _read, _write, _user_data)     \
        BT_GATT_ATTRIBUTE(_uuid, _perm, _read, _write, _user_data)

#define BT_GATT_ATTRIBUTE(_uuid, _perm, _read, _write, _user_data)      \
{                                                                       \
        .uuid = _uuid,                                                  \
        .read = _read,                                                  \
        .write = _write,                                                \
        .user_data = _user_data,                                        \
        .handle = 0,                                                    \
        .perm = _perm,                                                  \
}

typedef void (*bt_gatt_complete_func_t) (struct bt_conn *conn, void *user_data);

struct bt_gatt_notify_params {
        const struct bt_uuid *uuid;
        const struct bt_gatt_attr *attr;
        const void *data;
        uint16_t len;
        bt_gatt_complete_func_t func;
        void *user_data;
#if defined(CONFIG_BT_EATT) || defined(__DOXYGEN__)
        enum bt_att_chan_opt chan_opt;
#endif /* CONFIG_BT_EATT */
};

int bt_gatt_notify_cb(struct bt_conn *conn,
                      struct bt_gatt_notify_params *params);

int bt_gatt_notify_multiple(struct bt_conn *conn,
                            uint16_t num_params,
                            struct bt_gatt_notify_params params[]);

static inline int bt_gatt_notify(struct bt_conn *conn,
                                 const struct bt_gatt_attr *attr,
                                 const void *data, uint16_t len)
{
        struct bt_gatt_notify_params params;

        memset(&params, 0, sizeof(params));

        params.attr = attr;
        params.data = data;
        params.len = len;
#if defined(CONFIG_BT_EATT)
        params.chan_opt = BT_ATT_CHAN_OPT_NONE;
#endif /* CONFIG_BT_EATT */

        return bt_gatt_notify_cb(conn, &params);
}

static inline int bt_gatt_notify_uuid(struct bt_conn *conn,
                                      const struct bt_uuid *uuid,
                                      const struct bt_gatt_attr *attr,
                                      const void *data, uint16_t len)
{
        struct bt_gatt_notify_params params;

        memset(&params, 0, sizeof(params));

        params.uuid = uuid;
        params.attr = attr;
        params.data = data;
        params.len = len;
#if defined(CONFIG_BT_EATT)
        params.chan_opt = BT_ATT_CHAN_OPT_NONE;
#endif /* CONFIG_BT_EATT */

        return bt_gatt_notify_cb(conn, &params);
}

/* Forward declaration of the bt_gatt_indicate_params structure */
struct bt_gatt_indicate_params;

typedef void (*bt_gatt_indicate_func_t)(struct bt_conn *conn,
                                        struct bt_gatt_indicate_params *params,
                                        uint8_t err);

typedef void (*bt_gatt_indicate_params_destroy_t)(
                struct bt_gatt_indicate_params *params);

struct bt_gatt_indicate_params {
        const struct bt_uuid *uuid;
        const struct bt_gatt_attr *attr;
        bt_gatt_indicate_func_t func;
        bt_gatt_indicate_params_destroy_t destroy;
        const void *data;
        uint16_t len;
        uint8_t _ref;
#if defined(CONFIG_BT_EATT) || defined(__DOXYGEN__)
        enum bt_att_chan_opt chan_opt;
#endif /* CONFIG_BT_EATT */
};

int bt_gatt_indicate(struct bt_conn *conn,
                     struct bt_gatt_indicate_params *params);

bool bt_gatt_is_subscribed(struct bt_conn *conn,
                           const struct bt_gatt_attr *attr, uint16_t ccc_type);

uint16_t bt_gatt_get_mtu(struct bt_conn *conn);

uint16_t bt_gatt_get_uatt_mtu(struct bt_conn *conn);



struct bt_gatt_exchange_params {
        void (*func)(struct bt_conn *conn, uint8_t err,
                     struct bt_gatt_exchange_params *params);
};

int bt_gatt_exchange_mtu(struct bt_conn *conn,
                         struct bt_gatt_exchange_params *params);

struct bt_gatt_discover_params;

typedef uint8_t (*bt_gatt_discover_func_t)(struct bt_conn *conn,
                                        const struct bt_gatt_attr *attr,
                                        struct bt_gatt_discover_params *params);

enum bt_gatt_discover_type {
        BT_GATT_DISCOVER_PRIMARY,
        BT_GATT_DISCOVER_SECONDARY,
        BT_GATT_DISCOVER_INCLUDE,
        BT_GATT_DISCOVER_CHARACTERISTIC,
        BT_GATT_DISCOVER_DESCRIPTOR,
        BT_GATT_DISCOVER_ATTRIBUTE,
        BT_GATT_DISCOVER_STD_CHAR_DESC,
};

#define BT_GATT_AUTO_DISCOVER_CCC_HANDLE 0x0000U

struct bt_gatt_discover_params {
        const struct bt_uuid *uuid;
        bt_gatt_discover_func_t func;
        union {
                struct {
                        uint16_t attr_handle;
                        uint16_t start_handle;
                        uint16_t end_handle;
                } _included;
                uint16_t start_handle;
        };
        uint16_t end_handle;
        uint8_t type;
#if defined(CONFIG_BT_GATT_AUTO_DISCOVER_CCC) || defined(__DOXYGEN__)
        struct bt_gatt_subscribe_params *sub_params;
#endif /* defined(CONFIG_BT_GATT_AUTO_DISCOVER_CCC) || defined(__DOXYGEN__) */
#if defined(CONFIG_BT_EATT) || defined(__DOXYGEN__)
        enum bt_att_chan_opt chan_opt;
#endif /* CONFIG_BT_EATT */
};

int bt_gatt_discover(struct bt_conn *conn,
                     struct bt_gatt_discover_params *params);

struct bt_gatt_read_params;

typedef uint8_t (*bt_gatt_read_func_t)(struct bt_conn *conn, uint8_t err,
                                    struct bt_gatt_read_params *params,
                                    const void *data, uint16_t length);

struct bt_gatt_read_params {
        bt_gatt_read_func_t func;
        size_t handle_count;
        union {
                struct {
                        uint16_t handle;
                        uint16_t offset;
                } single;
                struct {
                        uint16_t *handles;
                        bool variable;
                } multiple;
                struct {
                        uint16_t start_handle;
                        uint16_t end_handle;
                        const struct bt_uuid *uuid;
                } by_uuid;
        };
#if defined(CONFIG_BT_EATT) || defined(__DOXYGEN__)
        enum bt_att_chan_opt chan_opt;
#endif /* CONFIG_BT_EATT */
        uint16_t _att_mtu;
};

int bt_gatt_read(struct bt_conn *conn, struct bt_gatt_read_params *params);

struct bt_gatt_write_params;

typedef void (*bt_gatt_write_func_t)(struct bt_conn *conn, uint8_t err,
                                     struct bt_gatt_write_params *params);

struct bt_gatt_write_params {
        bt_gatt_write_func_t func;
        uint16_t handle;
        uint16_t offset;
        const void *data;
        uint16_t length;
#if defined(CONFIG_BT_EATT) || defined(__DOXYGEN__)
        enum bt_att_chan_opt chan_opt;
#endif /* CONFIG_BT_EATT */
};

int bt_gatt_write(struct bt_conn *conn, struct bt_gatt_write_params *params);

int bt_gatt_write_without_response_cb(struct bt_conn *conn, uint16_t handle,
                                      const void *data, uint16_t length,
                                      bool sign, bt_gatt_complete_func_t func,
                                      void *user_data);

static inline int bt_gatt_write_without_response(struct bt_conn *conn,
                                                 uint16_t handle, const void *data,
                                                 uint16_t length, bool sign)
{
        return bt_gatt_write_without_response_cb(conn, handle, data, length,
                                                 sign, NULL, NULL);
}

struct bt_gatt_subscribe_params;

typedef uint8_t (*bt_gatt_notify_func_t)(struct bt_conn *conn,
                                      struct bt_gatt_subscribe_params *params,
                                      const void *data, uint16_t length);

typedef void (*bt_gatt_subscribe_func_t)(struct bt_conn *conn, uint8_t err,
                                         struct bt_gatt_subscribe_params *params);

enum bt_gatt_sub_flag {
        BT_GATT_SUBSCRIBE_FLAG_VOLATILE,

        BT_GATT_SUBSCRIBE_FLAG_NO_RESUB,

        BT_GATT_SUBSCRIBE_FLAG_WRITE_PENDING,

        BT_GATT_SUBSCRIBE_FLAG_SENT,

        BT_GATT_SUBSCRIBE_NUM_FLAGS
};

struct bt_gatt_subscribe_params {
        bt_gatt_notify_func_t notify;
        bt_gatt_subscribe_func_t subscribe;

        uint16_t value_handle;
        uint16_t ccc_handle;
#if defined(CONFIG_BT_GATT_AUTO_DISCOVER_CCC) || defined(__DOXYGEN__)
        uint16_t end_handle;
        struct bt_gatt_discover_params *disc_params;
#endif /* defined(CONFIG_BT_GATT_AUTO_DISCOVER_CCC) || defined(__DOXYGEN__) */
        uint16_t value;
#if defined(CONFIG_BT_SMP) || defined(__DOXYGEN__)
        bt_security_t min_security;
#endif /* CONFIG_BT_SMP */
        ATOMIC_DEFINE(flags, BT_GATT_SUBSCRIBE_NUM_FLAGS);

        sys_snode_t node;
#if defined(CONFIG_BT_EATT) || defined(__DOXYGEN__)
        enum bt_att_chan_opt chan_opt;
#endif /* CONFIG_BT_EATT */
};

int bt_gatt_subscribe(struct bt_conn *conn,
                      struct bt_gatt_subscribe_params *params);

int bt_gatt_resubscribe(uint8_t id, const bt_addr_le_t *peer,
                        struct bt_gatt_subscribe_params *params);

int bt_gatt_unsubscribe(struct bt_conn *conn,
                        struct bt_gatt_subscribe_params *params);

void bt_gatt_cancel(struct bt_conn *conn, void *params);


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_GATT_H_ */
```

## 21.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2015-2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 161 行

GATT 属性（Attribute）结构体的前向声明。

### 注释 3：原第 1440 行

条件编译配置（Configuration）标记：`CONFIG_BT_EATT`。

### 注释 4：原第 1557 行

条件编译配置（Configuration）标记：`CONFIG_BT_EATT`。

### 注释 5：原第 1596 行

条件编译配置（Configuration）标记：`CONFIG_BT_EATT`。

### 注释 6：原第 1601 行

`bt_gatt_indicate_params` 结构体的前向声明。

### 注释 7：原第 1657 行

条件编译配置（Configuration）标记：`CONFIG_BT_EATT`。

### 注释 8：原第 1925 行

条件编译表达式：`defined(CONFIG_BT_GATT_AUTO_DISCOVER_CCC) || defined(__DOXYGEN__)`。

### 注释 9：原第 1929 行

条件编译配置（Configuration）标记：`CONFIG_BT_EATT`。

### 注释 10：原第 2057 行

条件编译配置（Configuration）标记：`CONFIG_BT_EATT`。

### 注释 11：原第 2133 行

条件编译配置（Configuration）标记：`CONFIG_BT_EATT`。

### 注释 12：原第 2314 行

条件编译表达式：`defined(CONFIG_BT_GATT_AUTO_DISCOVER_CCC) || defined(__DOXYGEN__)`。

### 注释 13：原第 2323 行

条件编译配置（Configuration）标记：`CONFIG_BT_SMP`。

### 注释 14：原第 2335 行

条件编译配置（Configuration）标记：`CONFIG_BT_EATT`。

### 注释 15：原第 2449 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_GATT_H_`。

## 21.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [zephyr/bluetooth/att.h](https://docs.zephyrproject.org/latest/doxygen/html/att_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [bt_gatt_perm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga96e57500d2340a45badb23701cc43833)
- [BT_GATT_PERM_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a)
- [BT_GATT_PERM_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_GATT_PERM_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf)
- [BT_GATT_PERM_READ_ENCRYPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d)
- [BT_GATT_PERM_WRITE_ENCRYPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f)
- [BT_GATT_PERM_READ_AUTHEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583)
- [BT_GATT_PERM_WRITE_AUTHEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266)
- [BT_GATT_PERM_PREPARE_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79)
- [BT_GATT_PERM_READ_LESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57)
- [BT_GATT_PERM_WRITE_LESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94)
- [bt_gatt_attr_write_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga830d437c8d0757f53af1de6aa3031906)
- [BT_GATT_WRITE_FLAG_PREPARE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga830d437c8d0757f53af1de6aa3031906a019cf6118a0cfacbfad20c1cc5838383)
- [BT_GATT_WRITE_FLAG_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga830d437c8d0757f53af1de6aa3031906a770df41b7d433e8ce349b19e4657ba78)
- [BT_GATT_WRITE_FLAG_EXECUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gga830d437c8d0757f53af1de6aa3031906ad4e8f43c03da10c15685bd1a0109708b)
- [bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [bt_gatt_attr_read_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga57e36bf94652531964fd4237c203fe7b)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_gatt_attr_write_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga3fd8527a0f3e8f3699dc0d3b0339eba1)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [uuid](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a6958f507f9ff172018be458ebc86106f)
- [read](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a074abc719494ca35997a452f526e7ecc)
- [write](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a1ecd78536067f4bded506e0daccefd35)
- [user_data](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#adeb063fb101fab45dd789c7212c43357)
- [handle](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#aeee42a3d3ca15e40cf11cc0c3fde106b)
- [perm](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a0849a40254622080d05e8559c4fdb9e2)
- [bt_gatt_service_static](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md)
- [attrs](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md#a38f9e02241fe37f68df5dd8782b59e9f)
- [attr_count](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md#a84c35a391e372396e2ec89eaf0d4d047)
- [bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)
- [attrs](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md#a0281e96ab54519df641f6c489fdc6b5b)
- [attr_count](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md#a87d8316a92ae04678d7be0ae76ed86cb)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_gatt_service_val](../bluetooth_connection_model_reference/P067_bt_gatt_service_val_结构体.md)
- [uuid](../bluetooth_connection_model_reference/P067_bt_gatt_service_val_结构体.md#a683e01db92400e76aed32b7a81369a55)
- [end_handle](../bluetooth_connection_model_reference/P067_bt_gatt_service_val_结构体.md#a75b6fcf0f9f29ad05ccac0e83bcb31b7)
- [bt_gatt_include](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md)
- [uuid](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md#afa028e8daae00e3b1bc0b866c4335af3)
- [start_handle](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md#ac7f6c1a8018f483dce14f0fe21031232)
- [end_handle](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md#a54d20cebfd6ba62b692c363acdc25d61)
- [bt_gatt_cb](../bluetooth_connection_model_reference/P051_bt_gatt_cb_结构体.md)
- [att_mtu_updated](../bluetooth_connection_model_reference/P051_bt_gatt_cb_结构体.md#a93fe1a626ab59c38ef56f02671f88980)
- [bt_gatt_authorization_cb](../bluetooth_connection_model_reference/P050_bt_gatt_authorization_cb_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [read_authorize](../bluetooth_connection_model_reference/P050_bt_gatt_authorization_cb_结构体.md#a7b1bcbe10f12c90ee4e3214e36e9c2a3)
- [write_authorize](../bluetooth_connection_model_reference/P050_bt_gatt_authorization_cb_结构体.md#a7c12bd14f87f91e672eaaf92e1aa6e7b)
- [bt_gatt_chrc](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md)
- [uuid](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md#af3b4c22ae37b912c8edf58294cc50702)
- [value_handle](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md#a2ca6aec1a621fdfd12142a1188d37bd3)
- [properties](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md#a81bb8257052d7c8d03b51acaa51e5011)
- [bt_gatt_cep](../bluetooth_connection_model_reference/P055_bt_gatt_cep_结构体.md)
- [properties](../bluetooth_connection_model_reference/P055_bt_gatt_cep_结构体.md#a317442dc204f7632b0c5da8a8a9a98b5)
- [bt_gatt_ccc](../bluetooth_connection_model_reference/P052_bt_gatt_ccc_结构体.md)
- [flags](../bluetooth_connection_model_reference/P052_bt_gatt_ccc_结构体.md#ac8fa1028c5e87aa025832257b18fa7c3)
- [bt_gatt_scc](../bluetooth_connection_model_reference/P064_bt_gatt_scc_结构体.md)
- [flags](../bluetooth_connection_model_reference/P064_bt_gatt_scc_结构体.md#aa7ddf1810f6d47e59c364b7489823d00)
- [bt_gatt_cpf](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md)
- [format](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md#ab0ca135a75130b3ffc0c5bf375f3528f)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [exponent](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md#a3690a86c942badb2d2698481b03e436d)
- [unit](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md#a2a9f3d3f72b9acb1ef7f2dc765e5a231)
- [name_space](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md#a1dfbb9fc1e1397d2abec04b216d7ae33)
- [description](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md#a3c48dd5ea717fbaf510d13c64a370c06)
- [bt_gatt_err_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaf6d3f1e904f1a847afeb30236bad98a2)
- [bt_att_err_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gad2305f28744276d97aefd26bdb79023c)
- [bt_gatt_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga270c8a52bf3d512defc373f8c29b59f2)
- [bt_gatt_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5fb25c5eec91045dc4c7fd61ef7e528e)
- [bt_gatt_authorization_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5eee6afc6db391ffeda295d298bf6a56)
- [bt_gatt_service_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gab4d9cfea04e44445d5dc30ad52842b64)
- [bt_gatt_service_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaf5bf0205fad5f7ad187b764d23deba6b)
- [bt_gatt_service_is_registered](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gae5c1e8b7bb1e673e228f03d1d084be9a)
- [bt_gatt_iter](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gab38994257f53473e62e01eff8f236ee1)
- [BT_GATT_ITER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ggab38994257f53473e62e01eff8f236ee1aa3f2a25e27c7065a2c7bb2a9ff09542e)
- [BT_GATT_ITER_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ggab38994257f53473e62e01eff8f236ee1aea569feffa4815d3443e12be78c684f5)
- [bt_gatt_attr_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga60284611c90729b289fe806524ba9209)
- [bt_gatt_foreach_attr_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gad8d8f513004f391167212d7bf9f7ff10)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_gatt_foreach_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaa93b5e0f2870ed135447bead903c175a)
- [bt_gatt_attr_next](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga35cecaa43b00b374062d29cca1479d85)
- [bt_gatt_find_by_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gad2f3272b1dc42378104b492ec7caf6b0)
- [bt_gatt_attr_get_handle](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga2d51136ea1bd6cdb50900639506fd9f7)
- [bt_gatt_attr_value_handle](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga99738cf4f05eae4c6da17cc3420827d8)
- [bt_gatt_attr_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gaf6d253849932b706ec7f303568980dfa)
- [bt_gatt_attr_read_service](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gacae81c0f272bad7e6ac93c0d13b678c6)
- [bt_gatt_attr_read_included](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga4313a63decac2c8b7c4a1764df3d53ea)
- [bt_gatt_attr_read_chrc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gad58b526a06334530c13292d14a11257c)
- [bt_gatt_ccc_cfg](../bluetooth_connection_model_reference/P053_bt_gatt_ccc_cfg_结构体.md)
- [id](../bluetooth_connection_model_reference/P053_bt_gatt_ccc_cfg_结构体.md#ac17ddefe7ca6dbac921ee4c6f44fbf51)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [peer](../bluetooth_connection_model_reference/P053_bt_gatt_ccc_cfg_结构体.md#ab316080693b2c4daf5fd45e2c0501c70)
- [value](../bluetooth_connection_model_reference/P053_bt_gatt_ccc_cfg_结构体.md#a92acf7329f66638ac6c657c8eaa795ac)
- [bt_gatt_ccc_managed_user_data](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md)
- [cfg](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md#a44987dc5be9442436f6033c30bbb42fd)
- [BT_GATT_CCC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00)
- [value](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md#a883177671ea068f1dcbab36197abfdfd)
- [cfg_changed](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md#a166073fca5a342b859fb42482547b80c)
- [cfg_write](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md#a7ba4c03ef2a0c2c85e17ef1147934536)
- [cfg_match](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md#afc0c5226be7d9b2d3d039f86960a2ed3)
- [bt_gatt_attr_read_ccc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga2e85b42136e2c6a4cb5b7ad8a2532573)
- [bt_gatt_attr_write_ccc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gabba965b676650a55cb9934072b34c75e)
- [bt_gatt_attr_read_cep](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5893166f1b24f437a94ccf1fc57c7917)
- [bt_gatt_attr_read_cud](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga29421c8788b47b6a648704d27d5f0d28)
- [bt_gatt_attr_read_cpf](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5ae96590a0aaa5c4c3863a4a14d80fdd)
- [bt_gatt_complete_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac55832607b95f394d26a64ed1cfe5bba)
- [bt_gatt_notify_params](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md)
- [uuid](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#a2994cbe737fad725c60427000c21c373)
- [attr](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#a6187d0457763a15a623129e3e9e98e13)
- [data](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#afaa276cff9cbf204c433ca776904ef32)
- [len](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#a4a511da0b099ca88d895594caf7aaa6a)
- [func](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#ace3c6b5f5ed78b9f64c25b868d3bfbe2)
- [user_data](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#adec9a6f6ea0604e82b90dd47bb9951fa)
- [bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)
- [chan_opt](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#a978d7a42c39a098cedf751936f280fac)
- [bt_gatt_notify_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga55e3ef7cb43b8acb0a27643c78390146)
- [bt_gatt_notify_multiple](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga8071d6063f85c0a78155f6b2ac2da635)
- [bt_gatt_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga74ee552864c563aa5bc939f37395c14a)
- [memset](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a4137694174d4ca2fad886a1db355015c)
- [BT_ATT_CHAN_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739)
- [bt_gatt_notify_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga24bae284dbc71cd4075649c4bc348b7c)
- [bt_gatt_indicate_params](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md)
- [bt_gatt_indicate_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga1294850e6bdcbe7a8f42f2956fd837a8)
- [bt_gatt_indicate_params_destroy_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5d47ed9eaea22c8f00db14329daee8fe)
- [uuid](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#afde06f47d7a817291e437593ea01bccd)
- [attr](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#acbbee3a71838492416b20bb5cff89801)
- [func](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#af9eb83c3fba49ee3cd6162d5a2791707)
- [destroy](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#aeb346dc4c0e4a298c66f394d037a6514)
- [data](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#ae1d657512c99d5bba6fc99a450a6da32)
- [len](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#a10ad44140371165951eeac18cb3d0e7f)
- [chan_opt](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#a0e536938123ecb4f3ba6736c1de2a599)
- [bt_gatt_indicate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga4f2272692cc0f1d44638828012296c80)
- [bt_gatt_is_subscribed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gabd4df0a264dae10e43797992a567be7d)
- [bt_gatt_get_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga351fd7658eaecbbfa60f1769119ef733)
- [bt_gatt_get_uatt_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga6653de5e245cae6dc12cd0b45acbe028)
- [bt_gatt_exchange_params](../bluetooth_connection_model_reference/P059_bt_gatt_exchange_params_结构体.md)
- [func](../bluetooth_connection_model_reference/P059_bt_gatt_exchange_params_结构体.md#a76f4d3e779da9c725914574ac2e22ad1)
- [bt_gatt_exchange_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga0f41da23c6559a8254b04295aff8198d)
- [bt_gatt_discover_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md)
- [bt_gatt_discover_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gabd3bcd3c1560956726574faed332fb13)
- [bt_gatt_discover_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gaea89c65f17050820d54568f636b6554a)
- [BT_GATT_DISCOVER_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aada9ac33aa77f6043da8133dcf269478f)
- [BT_GATT_DISCOVER_SECONDARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa21be62548b816c7960a54dd6e3b37a97)
- [BT_GATT_DISCOVER_INCLUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa80afff1c83bb5ebb5603af699f2c26da)
- [BT_GATT_DISCOVER_CHARACTERISTIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa71355dfe0bf30c88f9fe2f7da1ba10ae)
- [BT_GATT_DISCOVER_DESCRIPTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa0ccb2587aa8f21361c5d73847a33ecbe)
- [BT_GATT_DISCOVER_ATTRIBUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aafe2167b873b848935d56f6ee7f2c444c)
- [BT_GATT_DISCOVER_STD_CHAR_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaea89c65f17050820d54568f636b6554aa81a1f8737c415544a0f793f4e626bb61)
- [uuid](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#a77d6665c01902e4e23cf8de8a9436262)
- [func](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#a337d7366c12451938f12eec4dc60903e)
- [attr_handle](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#a65ca3c9aad7c02d48fd35c4d6f69dc70)
- [start_handle](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#a0d2604e7c3ee8969cb5096cbf5793fdb)
- [end_handle](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#a225868498c34411cc3fc2be8e678e85e)
- [type](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#ab0f056c90954e1246d897019abd1e7fc)
- [bt_gatt_subscribe_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md)
- [sub_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#a87b130c520ce50f835d0589fd22a844c)
- [chan_opt](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#aba7585e3d0eefb323fcde9bcc88e287d)
- [bt_gatt_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gac06a945e5f7939b6716bc4f2cea781bd)
- [bt_gatt_read_params](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md)
- [bt_gatt_read_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga1ca94b4f2b6c456b6134e05127993569)
- [func](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a3ea107db0b7537c9dccb2aa6d8f916fb)
- [handle_count](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a0a36063ac0b110fbf57ef6a66f7bece8)
- [handle](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#af37beb6a69b3a6b90da0594b099bd64d)
- [offset](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a27f685a45c405bb2784fe369513724ad)
- [single](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a4cf61907bb95a2be6513d214b7030723)
- [handles](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a2794b8806933d0e16cfc77f4087fdeda)
- [variable](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a77d05cbc54b125fc35d180cf91bf9cb9)
- [multiple](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a521f5d1859dd9271fa2c595012dacd25)
- [start_handle](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#ac11db1652cd5cee567d666d3697f3a4b)
- [end_handle](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a8b2a2b912efe557e24276a654087e75c)
- [uuid](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#ae2ba6ce4043769b86a050fd767248111)
- [by_uuid](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a86b81f185490e63a07d2a62dd26a7f74)
- [chan_opt](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a1335d1f9aefeff89a57efe78335cb41b)
- [bt_gatt_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga1a18dd726ab960a88d7f85f2a014141a)
- [bt_gatt_write_params](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md)
- [bt_gatt_write_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga2bca8c4a45f41e0400a9e0147f4baf50)
- [func](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md#a3468e3b75f3f9eda12bc4963f48cf9aa)
- [handle](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md#a384c5c15f248df5b327423ca32637bad)
- [offset](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md#add53cc08465d28f33bc48a1e8649ac1a)
- [data](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md#ab6510ef242e73325adb074322746c27c)
- [length](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md#aded956dac2d398b642faeec81fdb9ec3)
- [chan_opt](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md#ad79905c16f7ba5289817de552ece1a48)
- [bt_gatt_write](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga843a42e68e0497d88d3f655f8ffd58d4)
- [bt_gatt_write_without_response_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga49439413d12b5a8a1c68735e961ab6fa)
- [bt_gatt_write_without_response](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga9fc78e32230637a6f092da2400c50fe7)
- [bt_gatt_notify_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gab3e53eb5f9bb1eda7bf612ef95755b4d)
- [bt_gatt_subscribe_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga2e914e63b4b91fa56bc3295283c43714)
- [bt_gatt_sub_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gaa43f45658809908baa72bf4e0ea745ac)
- [BT_GATT_SUBSCRIBE_FLAG_VOLATILE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745acaecdcb3baa850505f459523091c92a1cb)
- [BT_GATT_SUBSCRIBE_FLAG_NO_RESUB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745aca30bfd3fb4bf4f17653ba00942ba2b2e6)
- [BT_GATT_SUBSCRIBE_FLAG_WRITE_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745acafe1c3dc9380c33debd32a275d5bce8ad)
- [BT_GATT_SUBSCRIBE_FLAG_SENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745aca56aa5f332d4098e3942d7a902198f7ab)
- [BT_GATT_SUBSCRIBE_NUM_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ggaa43f45658809908baa72bf4e0ea745aca5640a1e06740a89859c5f4b183d58e79)
- [notify](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#acf237ef097e8b847eb049fb0a5d4b759)
- [subscribe](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#a91595407b8de4e862652e41100668f0a)
- [value_handle](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#a9248418eb04a5b7a0faed5077c40bf22)
- [ccc_handle](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#a77c53cdfd4143483b33a8ecf6061561e)
- [end_handle](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#af806d24aa97db1f2e9a021e719598a6d)
- [disc_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#ad3a3b9335b85777d65bdf875486e292a)
- [value](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#a3bff1209b7a0b5908408a568622d0150)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [min_security](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#a5b34bad1cf39bb3efd5faf516473dd4a)
- [ATOMIC_DEFINE](../atomic_reference/P001_原子操作公共接口.md#ga249c575db9764486197709b327f7370e)
- [flags](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#aedd24024881e22372505355024cd716b)
- [chan_opt](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#ae139848da09705d37fe7c9de4c1a4087)
- [bt_gatt_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga7d4a8e18f51ba6476886a15f81f48e5c)
- [bt_gatt_resubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga791b8bb8a4c085b022fafc0535a63511)
- [bt_gatt_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga56509c9b8f73f729cfa5e75be22d79ae)
- [bt_gatt_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga5193dea59a016692f94cf950d6b4f4f7)
- [addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [att.h](https://docs.zephyrproject.org/latest/doxygen/html/att_8h.html)
- [uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_gatt_attr::read](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a074abc719494ca35997a452f526e7ecc)
- [bt_gatt_attr::perm](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a0849a40254622080d05e8559c4fdb9e2)
- [bt_gatt_attr::write](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a1ecd78536067f4bded506e0daccefd35)
- [bt_gatt_attr::uuid](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#a6958f507f9ff172018be458ebc86106f)
- [bt_gatt_attr::user_data](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#adeb063fb101fab45dd789c7212c43357)
- [bt_gatt_attr::handle](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md#aeee42a3d3ca15e40cf11cc0c3fde106b)
- [bt_gatt_authorization_cb::read_authorize](../bluetooth_connection_model_reference/P050_bt_gatt_authorization_cb_结构体.md#a7b1bcbe10f12c90ee4e3214e36e9c2a3)
- [bt_gatt_authorization_cb::write_authorize](../bluetooth_connection_model_reference/P050_bt_gatt_authorization_cb_结构体.md#a7c12bd14f87f91e672eaaf92e1aa6e7b)
- [bt_gatt_cb::att_mtu_updated](../bluetooth_connection_model_reference/P051_bt_gatt_cb_结构体.md#a93fe1a626ab59c38ef56f02671f88980)
- [bt_gatt_ccc_cfg::value](../bluetooth_connection_model_reference/P053_bt_gatt_ccc_cfg_结构体.md#a92acf7329f66638ac6c657c8eaa795ac)
- [bt_gatt_ccc_cfg::peer](../bluetooth_connection_model_reference/P053_bt_gatt_ccc_cfg_结构体.md#ab316080693b2c4daf5fd45e2c0501c70)
- [bt_gatt_ccc_cfg::id](../bluetooth_connection_model_reference/P053_bt_gatt_ccc_cfg_结构体.md#ac17ddefe7ca6dbac921ee4c6f44fbf51)
- [bt_gatt_ccc_managed_user_data::cfg_changed](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md#a166073fca5a342b859fb42482547b80c)
- [bt_gatt_ccc_managed_user_data::cfg](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md#a44987dc5be9442436f6033c30bbb42fd)
- [bt_gatt_ccc_managed_user_data::cfg_write](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md#a7ba4c03ef2a0c2c85e17ef1147934536)
- [bt_gatt_ccc_managed_user_data::value](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md#a883177671ea068f1dcbab36197abfdfd)
- [bt_gatt_ccc_managed_user_data::cfg_match](../bluetooth_connection_model_reference/P054_bt_gatt_ccc_managed_user_data_结构体.md#afc0c5226be7d9b2d3d039f86960a2ed3)
- [bt_gatt_ccc::flags](../bluetooth_connection_model_reference/P052_bt_gatt_ccc_结构体.md#ac8fa1028c5e87aa025832257b18fa7c3)
- [bt_gatt_cep::properties](../bluetooth_connection_model_reference/P055_bt_gatt_cep_结构体.md#a317442dc204f7632b0c5da8a8a9a98b5)
- [bt_gatt_chrc::value_handle](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md#a2ca6aec1a621fdfd12142a1188d37bd3)
- [bt_gatt_chrc::properties](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md#a81bb8257052d7c8d03b51acaa51e5011)
- [bt_gatt_chrc::uuid](../bluetooth_connection_model_reference/P056_bt_gatt_chrc_结构体.md#af3b4c22ae37b912c8edf58294cc50702)
- [bt_gatt_cpf::name_space](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md#a1dfbb9fc1e1397d2abec04b216d7ae33)
- [bt_gatt_cpf::unit](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md#a2a9f3d3f72b9acb1ef7f2dc765e5a231)
- [bt_gatt_cpf::exponent](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md#a3690a86c942badb2d2698481b03e436d)
- [bt_gatt_cpf::description](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md#a3c48dd5ea717fbaf510d13c64a370c06)
- [bt_gatt_cpf::format](../bluetooth_connection_model_reference/P057_bt_gatt_cpf_结构体.md#ab0ca135a75130b3ffc0c5bf375f3528f)
- [bt_gatt_discover_params::start_handle](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#a0d2604e7c3ee8969cb5096cbf5793fdb)
- [bt_gatt_discover_params::end_handle](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#a225868498c34411cc3fc2be8e678e85e)
- [bt_gatt_discover_params::func](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#a337d7366c12451938f12eec4dc60903e)
- [bt_gatt_discover_params::attr_handle](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#a65ca3c9aad7c02d48fd35c4d6f69dc70)
- [bt_gatt_discover_params::uuid](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#a77d6665c01902e4e23cf8de8a9436262)
- [bt_gatt_discover_params::sub_params](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#a87b130c520ce50f835d0589fd22a844c)
- [bt_gatt_discover_params::type](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#ab0f056c90954e1246d897019abd1e7fc)
- [bt_gatt_discover_params::chan_opt](../bluetooth_connection_model_reference/P058_bt_gatt_discover_params_结构体.md#aba7585e3d0eefb323fcde9bcc88e287d)
- [bt_gatt_exchange_params::func](../bluetooth_connection_model_reference/P059_bt_gatt_exchange_params_结构体.md#a76f4d3e779da9c725914574ac2e22ad1)
- [bt_gatt_include::end_handle](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md#a54d20cebfd6ba62b692c363acdc25d61)
- [bt_gatt_include::start_handle](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md#ac7f6c1a8018f483dce14f0fe21031232)
- [bt_gatt_include::uuid](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md#afa028e8daae00e3b1bc0b866c4335af3)
- [bt_gatt_indicate_params::chan_opt](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#a0e536938123ecb4f3ba6736c1de2a599)
- [bt_gatt_indicate_params::len](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#a10ad44140371165951eeac18cb3d0e7f)
- [bt_gatt_indicate_params::attr](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#acbbee3a71838492416b20bb5cff89801)
- [bt_gatt_indicate_params::data](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#ae1d657512c99d5bba6fc99a450a6da32)
- [bt_gatt_indicate_params::destroy](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#aeb346dc4c0e4a298c66f394d037a6514)
- [bt_gatt_indicate_params::func](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#af9eb83c3fba49ee3cd6162d5a2791707)
- [bt_gatt_indicate_params::uuid](../bluetooth_connection_model_reference/P061_bt_gatt_indicate_params_结构体.md#afde06f47d7a817291e437593ea01bccd)
- [bt_gatt_notify_params::uuid](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#a2994cbe737fad725c60427000c21c373)
- [bt_gatt_notify_params::len](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#a4a511da0b099ca88d895594caf7aaa6a)
- [bt_gatt_notify_params::attr](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#a6187d0457763a15a623129e3e9e98e13)
- [bt_gatt_notify_params::chan_opt](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#a978d7a42c39a098cedf751936f280fac)
- [bt_gatt_notify_params::func](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#ace3c6b5f5ed78b9f64c25b868d3bfbe2)
- [bt_gatt_notify_params::user_data](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#adec9a6f6ea0604e82b90dd47bb9951fa)
- [bt_gatt_notify_params::data](../bluetooth_connection_model_reference/P062_bt_gatt_notify_params_结构体.md#afaa276cff9cbf204c433ca776904ef32)
- [bt_gatt_read_params::handle_count](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a0a36063ac0b110fbf57ef6a66f7bece8)
- [bt_gatt_read_params::chan_opt](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a1335d1f9aefeff89a57efe78335cb41b)
- [bt_gatt_read_params::handles](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a2794b8806933d0e16cfc77f4087fdeda)
- [bt_gatt_read_params::offset](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a27f685a45c405bb2784fe369513724ad)
- [bt_gatt_read_params::func](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a3ea107db0b7537c9dccb2aa6d8f916fb)
- [bt_gatt_read_params::single](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a4cf61907bb95a2be6513d214b7030723)
- [bt_gatt_read_params::multiple](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a521f5d1859dd9271fa2c595012dacd25)
- [bt_gatt_read_params::variable](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a77d05cbc54b125fc35d180cf91bf9cb9)
- [bt_gatt_read_params::by_uuid](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a86b81f185490e63a07d2a62dd26a7f74)
- [bt_gatt_read_params::end_handle](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#a8b2a2b912efe557e24276a654087e75c)
- [bt_gatt_read_params::start_handle](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#ac11db1652cd5cee567d666d3697f3a4b)
- [bt_gatt_read_params::uuid](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#ae2ba6ce4043769b86a050fd767248111)
- [bt_gatt_read_params::handle](../bluetooth_connection_model_reference/P063_bt_gatt_read_params_结构体.md#af37beb6a69b3a6b90da0594b099bd64d)
- [bt_gatt_scc::flags](../bluetooth_connection_model_reference/P064_bt_gatt_scc_结构体.md#aa7ddf1810f6d47e59c364b7489823d00)
- [bt_gatt_service_static::attrs](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md#a38f9e02241fe37f68df5dd8782b59e9f)
- [bt_gatt_service_static::attr_count](../bluetooth_connection_model_reference/P066_bt_gatt_service_static_结构体.md#a84c35a391e372396e2ec89eaf0d4d047)
- [bt_gatt_service_val::uuid](../bluetooth_connection_model_reference/P067_bt_gatt_service_val_结构体.md#a683e01db92400e76aed32b7a81369a55)
- [bt_gatt_service_val::end_handle](../bluetooth_connection_model_reference/P067_bt_gatt_service_val_结构体.md#a75b6fcf0f9f29ad05ccac0e83bcb31b7)
- [bt_gatt_service::attrs](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md#a0281e96ab54519df641f6c489fdc6b5b)
- [bt_gatt_service::attr_count](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md#a87d8316a92ae04678d7be0ae76ed86cb)
- [bt_gatt_subscribe_params::value](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#a3bff1209b7a0b5908408a568622d0150)
- [bt_gatt_subscribe_params::min_security](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#a5b34bad1cf39bb3efd5faf516473dd4a)
- [bt_gatt_subscribe_params::ccc_handle](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#a77c53cdfd4143483b33a8ecf6061561e)
- [bt_gatt_subscribe_params::subscribe](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#a91595407b8de4e862652e41100668f0a)
- [bt_gatt_subscribe_params::value_handle](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#a9248418eb04a5b7a0faed5077c40bf22)
- [bt_gatt_subscribe_params::notify](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#acf237ef097e8b847eb049fb0a5d4b759)
- [bt_gatt_subscribe_params::disc_params](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#ad3a3b9335b85777d65bdf875486e292a)
- [bt_gatt_subscribe_params::chan_opt](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#ae139848da09705d37fe7c9de4c1a4087)
- [bt_gatt_subscribe_params::flags](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#aedd24024881e22372505355024cd716b)
- [bt_gatt_subscribe_params::end_handle](../bluetooth_connection_model_reference/P068_bt_gatt_subscribe_params_结构体.md#af806d24aa97db1f2e9a021e719598a6d)
- [bt_gatt_write_params::func](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md#a3468e3b75f3f9eda12bc4963f48cf9aa)
- [bt_gatt_write_params::handle](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md#a384c5c15f248df5b327423ca32637bad)
- [bt_gatt_write_params::data](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md#ab6510ef242e73325adb074322746c27c)
- [bt_gatt_write_params::chan_opt](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md#ad79905c16f7ba5289817de552ece1a48)
- [bt_gatt_write_params::offset](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md#add53cc08465d28f33bc48a1e8649ac1a)
- [bt_gatt_write_params::length](../bluetooth_connection_model_reference/P069_bt_gatt_write_params_结构体.md#aded956dac2d398b642faeec81fdb9ec3)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P020_flash_map.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P022_gd32a50x-clocks.h_源码浏览.md)
