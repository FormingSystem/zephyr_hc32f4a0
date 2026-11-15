---
id: learning.zephyr-docs.api-source-supplement-reference.page-73
title: formats.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/formats_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_formats.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/formats_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/formats_8h.html)。

## 73.1\_原始可见代码（Source Code）

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
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00053"></a>
<a id="l00054"></a>
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
<a id="l00086"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="foldopen00158"></a>
<a id="l00158"></a>
<a id="l00159"></a>
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
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="foldopen00288"></a>
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
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00476"></a>
<a id="l00488"></a>
<a id="foldopen00495"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="foldopen00508"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="foldopen00572"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="foldopen00591"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00625"></a>
<a id="l00631"></a>
<a id="foldopen00638"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="foldopen00652"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="foldopen00686"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="foldopen00716"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="foldopen00770"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00780"></a>
<a id="l00781"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00816"></a>
<a id="l00822"></a>
<a id="foldopen00829"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="foldopen00840"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00846"></a>
<a id="l00847"></a>
<a id="l00856"></a>
<a id="l00857"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00870"></a>
<a id="l00871"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="foldopen00903"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00933"></a>
<a id="l00934"></a>
<a id="l00957"></a>
<a id="l00958"></a>
<a id="l00983"></a>
<a id="l00984"></a>
<a id="l01009"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01036"></a>
<a id="l01037"></a>
<a id="l01062"></a>
<a id="l01063"></a>
<a id="foldopen01070"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="l01073"></a>
<a id="l01101"></a>
<a id="l01102"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01135"></a>
<a id="l01140"></a>
<a id="foldopen01147"></a>
<a id="l01147"></a>
<a id="l01148"></a>
<a id="l01149"></a>
<a id="l01150"></a>
<a id="l01151"></a>
<a id="l01152"></a>
<a id="l01156"></a>
<a id="l01157"></a>
<a id="l01161"></a>
<a id="l01162"></a>
<a id="l01166"></a>
<a id="l01167"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01176"></a>
<a id="l01178"></a>
<a id="l01180"></a>
<a id="foldopen01187"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="foldopen01196"></a>
<a id="l01196"></a>
<a id="l01197"></a>
<a id="l01198"></a>
<a id="foldopen01205"></a>
<a id="l01205"></a>
<a id="l01206"></a>
<a id="l01207"></a>
<a id="foldopen01214"></a>
<a id="l01214"></a>
<a id="l01215"></a>
<a id="l01216"></a>
<a id="foldopen01223"></a>
<a id="l01223"></a>
<a id="l01224"></a>
<a id="l01225"></a>
<a id="l01226"></a>
<a id="foldopen01233"></a>
<a id="l01233"></a>
<a id="l01234"></a>
<a id="l01235"></a>
<a id="l01236"></a>
<a id="foldopen01243"></a>
<a id="l01243"></a>
<a id="l01244"></a>
<a id="l01245"></a>
<a id="foldopen01252"></a>
<a id="l01252"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="foldopen01263"></a>
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
<a id="l01279"></a>
<a id="l01280"></a>
<a id="l01281"></a>
<a id="l01282"></a>
<a id="l01283"></a>
<a id="l01284"></a>
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
<a id="l01304"></a>
<a id="l01305"></a>
<a id="l01306"></a>
<a id="l01307"></a>
<a id="l01308"></a>
<a id="l01309"></a>
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
<a id="l01348"></a>
<a id="l01349"></a>
<a id="l01350"></a>
<a id="l01351"></a>
<a id="l01352"></a>
<a id="l01356"></a>
<a id="l01357"></a>
<a id="agroup__video__formats_html_ga011cc337bc54480d1e11c3e6833ae398"></a>
<a id="agroup__video__formats_html_ga017bcbec587314f569d6d0e4fbdda351"></a>
<a id="agroup__video__formats_html_ga02d91ebf4b5150d5fa437bb3a7a6e872"></a>
<a id="agroup__video__formats_html_ga03e6be04b23b9735c96231eebc687158"></a>
<a id="agroup__video__formats_html_ga0506f2c8aa1a82f02fc9383d99b43bc3"></a>
<a id="agroup__video__formats_html_ga06864b3b1b7d563a9cd2f15c33cdd2d8"></a>
<a id="agroup__video__formats_html_ga07b22957c7fdc64fd3089fbcb811d599"></a>
<a id="agroup__video__formats_html_ga0b55190a343fe891bdbb7b148e7feeae"></a>
<a id="agroup__video__formats_html_ga166b2144cec4b4f92fadda30e81b7d22"></a>
<a id="agroup__video__formats_html_ga171cb239b78ca49b9232dcb9d5e9f43f"></a>
<a id="agroup__video__formats_html_ga19d8dc905695229097dffe659f2a806e"></a>
<a id="agroup__video__formats_html_ga249cbf808658dab777a705fd9deb2986"></a>
<a id="agroup__video__formats_html_ga263e6553a77d00bc509c1b270efebb0b"></a>
<a id="agroup__video__formats_html_ga299af047675a110c109cee954f55fca6"></a>
<a id="agroup__video__formats_html_ga3463a33faa910f98280c96f40d3c65e7"></a>
<a id="agroup__video__formats_html_ga348c15cc77c728fdac773d58341cbc1d"></a>
<a id="agroup__video__formats_html_ga3751a8dce1c7459df06f83cd09449b5d"></a>
<a id="agroup__video__formats_html_ga403f40a7e15319365c6ca8f3f5f19d21"></a>
<a id="agroup__video__formats_html_ga4269984ce806e64ba5ccd41c1429769a"></a>
<a id="agroup__video__formats_html_ga4ae1acc3d44a1698e0d48f299f061a49"></a>
<a id="agroup__video__formats_html_ga4df33d1a41c2dbdc16c19113be13760b"></a>
<a id="agroup__video__formats_html_ga4f31b5d397868e952d53022c6c8e5823"></a>
<a id="agroup__video__formats_html_ga502df4612995fc39e03d6de3ec675159"></a>
<a id="agroup__video__formats_html_ga515e379bc7f59a8062f3e2a5980b0626"></a>
<a id="agroup__video__formats_html_ga5cd54fb54967a80576082cadd5941670"></a>
<a id="agroup__video__formats_html_ga604d2f3501407546aa924e2fdb37be2f"></a>
<a id="agroup__video__formats_html_ga63c825ce5dc6c863d355195fde40acb1"></a>
<a id="agroup__video__formats_html_ga66646a639518285810335a70337277d7"></a>
<a id="agroup__video__formats_html_ga6c98a7066d7d3bdd8fce3d3651772153"></a>
<a id="agroup__video__formats_html_ga6e5538e8f21a5be750eec38c2a16ad2f"></a>
<a id="agroup__video__formats_html_ga7b167f2b6a147d325a685825274cd2f2"></a>
<a id="agroup__video__formats_html_ga7d9379f19abcbac17bad3d6359a42d9d"></a>
<a id="agroup__video__formats_html_ga7f00eb633dd312ea89097edc82dc8f0c"></a>
<a id="agroup__video__formats_html_ga89eb47d1dd60794781ee91cb5ae199ad"></a>
<a id="agroup__video__formats_html_ga8be24c04210f8818d75082bd710db8b1"></a>
<a id="agroup__video__formats_html_ga8e0f47c16483b14b45a593e9e542a987"></a>
<a id="agroup__video__formats_html_ga8ee1e3b82eeeb02188157aa4b4b5d842"></a>
<a id="agroup__video__formats_html_ga9054aa564afdf3b6129539fbda30d9bf"></a>
<a id="agroup__video__formats_html_ga9294d7e95c9fe00df93248958b7bef0e"></a>
<a id="agroup__video__formats_html_gaa28c6306a3ed44a0e50c16e0eac86688"></a>
<a id="agroup__video__formats_html_gaa2d7712f655dfcb3c74b4f4ec9941402"></a>
<a id="agroup__video__formats_html_gaa3af19adaf282b83a6c16f265a4260dc"></a>
<a id="agroup__video__formats_html_gaa3df9d0af327e609b25e050a4362c2e2"></a>
<a id="agroup__video__formats_html_gaa65fe8bd917dd2fe95fa87530fc3055f"></a>
<a id="agroup__video__formats_html_gaa6e4c240372e53db8ea3472cc456af58"></a>
<a id="agroup__video__formats_html_gaa9edb9c562fc3c86b61e071970fae60d"></a>
<a id="agroup__video__formats_html_gab471cd15aa874a5deadf7b54b826a90e"></a>
<a id="agroup__video__formats_html_gab5b5375f050d039e05032c77ac838b31"></a>
<a id="agroup__video__formats_html_gabb167fd4b58db338de823dc285e62342"></a>
<a id="agroup__video__formats_html_gabbfecc5e0c2c4115c57d4772eaa4918f"></a>
<a id="agroup__video__formats_html_gabc0205ce5c6426051fdec88d92f123e3"></a>
<a id="agroup__video__formats_html_gabcdd44434323cc0e0634e94f23f83146"></a>
<a id="agroup__video__formats_html_gabdbd1b0f40af6663d81402deefdd387f"></a>
<a id="agroup__video__formats_html_gabf0dde810e75d37823891ed03811482c"></a>
<a id="agroup__video__formats_html_gac3413c36b3ce91e5658cd0f973c1f3d7"></a>
<a id="agroup__video__formats_html_gace39ba88d298b1991412f73fb4fe9d18"></a>
<a id="agroup__video__formats_html_gad186d3166acec11c893ae57a0ae68f11"></a>
<a id="agroup__video__formats_html_gad40f2d8628a39f0d87d5f0a337d7f8c4"></a>
<a id="agroup__video__formats_html_gad69ab9041428488051bdb45f42ad4271"></a>
<a id="agroup__video__formats_html_gada0124aad9c10d403966b1e3851cd968"></a>
<a id="agroup__video__formats_html_gadca3ee56c798cf05b63cbfc87af98ce3"></a>
<a id="agroup__video__formats_html_gadf53a84505c1299a5c97a0213c989103"></a>
<a id="agroup__video__formats_html_gadfdb271a780b10a29a356675014a25c2"></a>
<a id="agroup__video__formats_html_gae06f742e31a62295d3ee16af8eec1b06"></a>
<a id="agroup__video__formats_html_gae096669643176203199270317dc3449d"></a>
<a id="agroup__video__formats_html_gaecedece3398a6e2f62c20c2eb3f6d3c2"></a>
<a id="agroup__video__formats_html_gaf009d0eb7dbdb3bfd8883da03478c1ec"></a>
<a id="agroup__video__formats_html_gaf18e6647596613e07ec3c651574b08ba"></a>
<a id="agroup__video__formats_html_gaf1f8775bbdd0508c4e21a58dfcfc362d"></a>
<a id="agroup__video__formats_html_gaf58481956952b13b071b1a68541b9c21"></a>
<a id="agroup__video__formats_html_gaffb650a5f9b2b03890283ecfe95aee04"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited.
 * Copyright 2025 NXP
 * Copyright (c) 2025 STMicroelectronics
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_VIDEO_FORMATS_H
#define ZEPHYR_INCLUDE_VIDEO_FORMATS_H


#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

#define VIDEO_FOURCC(a, b, c, d)                                                                   \
        ((uint32_t)(a) | ((uint32_t)(b) << 8) | ((uint32_t)(c) << 16) | ((uint32_t)(d) << 24))

#define VIDEO_FOURCC_FROM_STR(str) VIDEO_FOURCC((str)[0], (str)[1], (str)[2], (str)[3])

#define VIDEO_FOURCC_TO_STR(fourcc)                                                                \
        ((char[]){                                                                                 \
                (char)((fourcc) & 0xFF),                                                           \
                (char)(((fourcc) >> 8) & 0xFF),                                                    \
                (char)(((fourcc) >> 16) & 0xFF),                                                   \
                (char)(((fourcc) >> 24) & 0xFF),                                                   \
                '\0'                                                                               \
        })


#define VIDEO_FOREACH_BAYER(X, ...)                                             \
        VIDEO_FOREACH_BAYER_PADDED(X, __VA_ARGS__)                              \
        VIDEO_FOREACH_BAYER_MIPI_PACKED(X, __VA_ARGS__)                         \
        VIDEO_FOREACH_BAYER_NON_PACKED(X, __VA_ARGS__)

#define VIDEO_FOREACH_BAYER_PADDED(X, ...)                                      \
        X(VIDEO_PIX_FMT_SBGGR8P16, __VA_ARGS__)                                 \
        X(VIDEO_PIX_FMT_SGBRG8P16, __VA_ARGS__)                                 \
        X(VIDEO_PIX_FMT_SGRBG8P16, __VA_ARGS__)                                 \
        X(VIDEO_PIX_FMT_SRGGB8P16, __VA_ARGS__)

#define VIDEO_PIX_FMT_SBGGR8P16 VIDEO_FOURCC('p', 'B', '8', '2')

#define VIDEO_PIX_FMT_SGBRG8P16 VIDEO_FOURCC('p', 'G', '8', '2')

#define VIDEO_PIX_FMT_SGRBG8P16 VIDEO_FOURCC('p', 'g', '8', '2')

#define VIDEO_PIX_FMT_SRGGB8P16 VIDEO_FOURCC('p', 'R', '8', '2')

#define VIDEO_FOREACH_BAYER_MIPI_PACKED(X, ...)                                 \
        X(VIDEO_PIX_FMT_SBGGR10P, __VA_ARGS__)                                  \
        X(VIDEO_PIX_FMT_SGBRG10P, __VA_ARGS__)                                  \
        X(VIDEO_PIX_FMT_SGRBG10P, __VA_ARGS__)                                  \
        X(VIDEO_PIX_FMT_SRGGB10P, __VA_ARGS__)                                  \
        X(VIDEO_PIX_FMT_SBGGR12P, __VA_ARGS__)                                  \
        X(VIDEO_PIX_FMT_SGBRG12P, __VA_ARGS__)                                  \
        X(VIDEO_PIX_FMT_SGRBG12P, __VA_ARGS__)                                  \
        X(VIDEO_PIX_FMT_SRGGB12P, __VA_ARGS__)                                  \
        X(VIDEO_PIX_FMT_SBGGR14P, __VA_ARGS__)                                  \
        X(VIDEO_PIX_FMT_SGBRG14P, __VA_ARGS__)                                  \
        X(VIDEO_PIX_FMT_SGRBG14P, __VA_ARGS__)                                  \
        X(VIDEO_PIX_FMT_SRGGB14P, __VA_ARGS__)

#define VIDEO_PIX_FMT_SBGGR10P VIDEO_FOURCC('p', 'B', 'A', 'A')

#define VIDEO_PIX_FMT_SGBRG10P VIDEO_FOURCC('p', 'G', 'A', 'A')

#define VIDEO_PIX_FMT_SGRBG10P VIDEO_FOURCC('p', 'g', 'A', 'A')

#define VIDEO_PIX_FMT_SRGGB10P VIDEO_FOURCC('p', 'R', 'A', 'A')

#define VIDEO_PIX_FMT_SBGGR12P VIDEO_FOURCC('p', 'B', 'C', 'C')

#define VIDEO_PIX_FMT_SGBRG12P VIDEO_FOURCC('p', 'G', 'C', 'C')

#define VIDEO_PIX_FMT_SGRBG12P VIDEO_FOURCC('p', 'g', 'C', 'C')

#define VIDEO_PIX_FMT_SRGGB12P VIDEO_FOURCC('p', 'R', 'C', 'C')

#define VIDEO_PIX_FMT_SBGGR14P VIDEO_FOURCC('p', 'B', 'E', 'E')

#define VIDEO_PIX_FMT_SGBRG14P VIDEO_FOURCC('p', 'G', 'E', 'E')

#define VIDEO_PIX_FMT_SGRBG14P VIDEO_FOURCC('p', 'g', 'E', 'E')

#define VIDEO_PIX_FMT_SRGGB14P VIDEO_FOURCC('p', 'R', 'E', 'E')

#define VIDEO_FOREACH_BAYER_NON_PACKED(X, ...)                                  \
        X(VIDEO_PIX_FMT_SBGGR8, __VA_ARGS__)                                    \
        X(VIDEO_PIX_FMT_SGBRG8, __VA_ARGS__)                                    \
        X(VIDEO_PIX_FMT_SGRBG8, __VA_ARGS__)                                    \
        X(VIDEO_PIX_FMT_SRGGB8, __VA_ARGS__)                                    \
        X(VIDEO_PIX_FMT_SGBRG10, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SGRBG10, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SRGGB10, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SBGGR12, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SGBRG12, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SGRBG12, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SRGGB12, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SBGGR14, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SGBRG14, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SGRBG14, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SRGGB14, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SBGGR16, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SGBRG16, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SGRBG16, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_SRGGB16, __VA_ARGS__)

#define VIDEO_PIX_FMT_SBGGR8 VIDEO_FOURCC('B', 'A', '8', '1')

#define VIDEO_PIX_FMT_SGBRG8 VIDEO_FOURCC('G', 'B', 'R', 'G')

#define VIDEO_PIX_FMT_SGRBG8 VIDEO_FOURCC('G', 'R', 'B', 'G')

#define VIDEO_PIX_FMT_SRGGB8 VIDEO_FOURCC('R', 'G', 'G', 'B')

#define VIDEO_PIX_FMT_SBGGR10 VIDEO_FOURCC('B', 'G', '1', '0')

#define VIDEO_PIX_FMT_SGBRG10 VIDEO_FOURCC('G', 'B', '1', '0')

#define VIDEO_PIX_FMT_SGRBG10 VIDEO_FOURCC('B', 'A', '1', '0')

#define VIDEO_PIX_FMT_SRGGB10 VIDEO_FOURCC('R', 'G', '1', '0')

#define VIDEO_PIX_FMT_SBGGR12 VIDEO_FOURCC('B', 'G', '1', '2')

#define VIDEO_PIX_FMT_SGBRG12 VIDEO_FOURCC('G', 'B', '1', '2')

#define VIDEO_PIX_FMT_SGRBG12 VIDEO_FOURCC('B', 'A', '1', '2')

#define VIDEO_PIX_FMT_SRGGB12 VIDEO_FOURCC('R', 'G', '1', '2')

#define VIDEO_PIX_FMT_SBGGR14 VIDEO_FOURCC('B', 'G', '1', '4')

#define VIDEO_PIX_FMT_SGBRG14 VIDEO_FOURCC('G', 'B', '1', '4')

#define VIDEO_PIX_FMT_SGRBG14 VIDEO_FOURCC('G', 'R', '1', '4')

#define VIDEO_PIX_FMT_SRGGB14 VIDEO_FOURCC('R', 'G', '1', '4')

#define VIDEO_PIX_FMT_SBGGR16 VIDEO_FOURCC('B', 'Y', 'R', '2')

#define VIDEO_PIX_FMT_SGBRG16 VIDEO_FOURCC('G', 'B', '1', '6')

#define VIDEO_PIX_FMT_SGRBG16 VIDEO_FOURCC('G', 'R', '1', '6')

#define VIDEO_PIX_FMT_SRGGB16 VIDEO_FOURCC('R', 'G', '1', '6')



#define VIDEO_FOREACH_GRAYSCALE(X, ...)                                         \
        VIDEO_FOREACH_GRAYSCALE_NON_PACKED(X, __VA_ARGS__)                      \
        VIDEO_FOREACH_GRAYSCALE_PADDED(X, __VA_ARGS__)                          \
        VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED(X, __VA_ARGS__)

#define VIDEO_FOREACH_GRAYSCALE_NON_PACKED(X, ...)                              \
        X(VIDEO_PIX_FMT_GREY, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_Y10, __VA_ARGS__)                                       \
        X(VIDEO_PIX_FMT_Y12, __VA_ARGS__)                                       \
        X(VIDEO_PIX_FMT_Y14, __VA_ARGS__)                                       \
        X(VIDEO_PIX_FMT_Y16, __VA_ARGS__)

#define VIDEO_PIX_FMT_GREY VIDEO_FOURCC('G', 'R', 'E', 'Y')

#define VIDEO_PIX_FMT_Y10 VIDEO_FOURCC('Y', '1', '0', ' ')

#define VIDEO_PIX_FMT_Y12 VIDEO_FOURCC('Y', '1', '2', ' ')

#define VIDEO_PIX_FMT_Y14 VIDEO_FOURCC('Y', '1', '4', ' ')

#define VIDEO_PIX_FMT_Y16 VIDEO_FOURCC('Y', '1', '6', ' ')

#define VIDEO_FOREACH_GRAYSCALE_PADDED(X, ...)                                  \
        X(VIDEO_PIX_FMT_Y8P16, __VA_ARGS__)

#define VIDEO_PIX_FMT_Y8P16 VIDEO_FOURCC('Y', '8', 'P', '2')

#define VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED(X, ...)                             \
        X(VIDEO_PIX_FMT_Y10P, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_Y12P, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_Y14P, __VA_ARGS__)

#define VIDEO_PIX_FMT_Y10P VIDEO_FOURCC('Y', '1', '0', 'P')

#define VIDEO_PIX_FMT_Y12P VIDEO_FOURCC('Y', '1', '2', 'P')

#define VIDEO_PIX_FMT_Y14P VIDEO_FOURCC('Y', '1', '4', 'P')



#define VIDEO_FOREACH_RGB(X, ...)                                               \
        VIDEO_FOREACH_RGB_PACKED(X, __VA_ARGS__)                                \
        VIDEO_FOREACH_RGB_NON_PACKED(X, __VA_ARGS__)                            \
        VIDEO_FOREACH_RGB_ALPHA(X, __VA_ARGS__)                                 \
        VIDEO_FOREACH_RGB_PADDED(X, __VA_ARGS__)

#define VIDEO_FOREACH_RGB_PACKED(X, ...)                                        \
        X(VIDEO_PIX_FMT_RGB565X, __VA_ARGS__)                                   \
        X(VIDEO_PIX_FMT_RGB565, __VA_ARGS__)

#define VIDEO_PIX_FMT_RGB565X VIDEO_FOURCC('R', 'G', 'B', 'R')

#define VIDEO_PIX_FMT_RGB565 VIDEO_FOURCC('R', 'G', 'B', 'P')

#define VIDEO_FOREACH_RGB_NON_PACKED(X, ...)                                    \
        X(VIDEO_PIX_FMT_BGR24, __VA_ARGS__)                                     \
        X(VIDEO_PIX_FMT_RGB24, __VA_ARGS__)

#define VIDEO_PIX_FMT_BGR24 VIDEO_FOURCC('B', 'G', 'R', '3')

#define VIDEO_PIX_FMT_RGB24 VIDEO_FOURCC('R', 'G', 'B', '3')

#define VIDEO_FOREACH_RGB_ALPHA(X, ...)                                         \
        X(VIDEO_PIX_FMT_ARGB32, __VA_ARGS__)                                    \
        X(VIDEO_PIX_FMT_ABGR32, __VA_ARGS__)                                    \
        X(VIDEO_PIX_FMT_RGBA32, __VA_ARGS__)                                    \
        X(VIDEO_PIX_FMT_BGRA32, __VA_ARGS__)

#define VIDEO_PIX_FMT_ARGB32 VIDEO_FOURCC('B', 'A', '2', '4')

#define VIDEO_PIX_FMT_BGRA32 VIDEO_FOURCC('A', 'R', '2', '4')

#define VIDEO_PIX_FMT_RGBA32 VIDEO_FOURCC('A', 'B', '2', '4')

#define VIDEO_PIX_FMT_ABGR32 VIDEO_FOURCC('R', 'A', '2', '4')

#define VIDEO_FOREACH_RGB_PADDED(X, ...)                                        \
        X(VIDEO_PIX_FMT_XRGB32, __VA_ARGS__)

#define VIDEO_PIX_FMT_XRGB32 VIDEO_FOURCC('B', 'X', '2', '4')

#define VIDEO_PIX_FMT_XBGR32 VIDEO_FOURCC('R', 'X', '2', '4')

#define VIDEO_PIX_FMT_BGRX32 VIDEO_FOURCC('X', 'R', '2', '4')

#define VIDEO_PIX_FMT_RGBX32 VIDEO_FOURCC('X', 'B', '2', '4')



#define VIDEO_FOREACH_YUV(X, ...)                                               \
        VIDEO_FOREACH_YUV_FULL_PLANAR(X, __VA_ARGS__)                           \
        VIDEO_FOREACH_YUV_NON_PLANAR(X, __VA_ARGS__)                            \
        VIDEO_FOREACH_YUV_SEMI_PLANAR(X, __VA_ARGS__)

#define VIDEO_FOREACH_YUV_NON_PLANAR(X, ...)                                    \
        X(VIDEO_PIX_FMT_YUYV, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_YVYU, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_VYUY, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_UYVY, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_YUV24, __VA_ARGS__)                                     \
        X(VIDEO_PIX_FMT_XYUV32, __VA_ARGS__)

#define VIDEO_PIX_FMT_YUYV VIDEO_FOURCC('Y', 'U', 'Y', 'V')

#define VIDEO_PIX_FMT_YVYU VIDEO_FOURCC('Y', 'V', 'Y', 'U')

#define VIDEO_PIX_FMT_VYUY VIDEO_FOURCC('V', 'Y', 'U', 'Y')

#define VIDEO_PIX_FMT_UYVY VIDEO_FOURCC('U', 'Y', 'V', 'Y')

#define VIDEO_PIX_FMT_XYUV32 VIDEO_FOURCC('X', 'Y', 'U', 'V')

#define VIDEO_PIX_FMT_YUV24 VIDEO_FOURCC('Y', 'U', 'V', '3')

#define VIDEO_FOREACH_YUV_SEMI_PLANAR(X, ...)                                   \
        X(VIDEO_PIX_FMT_NV12, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_NV21, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_NV16, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_NV61, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_NV24, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_NV42, __VA_ARGS__)

#define VIDEO_PIX_FMT_NV12 VIDEO_FOURCC('N', 'V', '1', '2')

#define VIDEO_PIX_FMT_NV21 VIDEO_FOURCC('N', 'V', '2', '1')

#define VIDEO_PIX_FMT_NV16 VIDEO_FOURCC('N', 'V', '1', '6')


#define VIDEO_PIX_FMT_NV61 VIDEO_FOURCC('N', 'V', '6', '1')

#define VIDEO_PIX_FMT_NV24 VIDEO_FOURCC('N', 'V', '2', '4')

#define VIDEO_PIX_FMT_NV42 VIDEO_FOURCC('N', 'V', '4', '2')

#define VIDEO_FOREACH_YUV_FULL_PLANAR(X, ...)                                   \
        X(VIDEO_PIX_FMT_YUV420, __VA_ARGS__)                                    \
        X(VIDEO_PIX_FMT_YVU420, __VA_ARGS__)

#define VIDEO_PIX_FMT_YUV420 VIDEO_FOURCC('Y', 'U', '1', '2')

#define VIDEO_PIX_FMT_YVU420 VIDEO_FOURCC('Y', 'V', '1', '2')



#define VIDEO_FOREACH_COMPRESSED(X, ...)                                        \
        X(VIDEO_PIX_FMT_JPEG, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_H264, __VA_ARGS__)                                      \
        X(VIDEO_PIX_FMT_H264_NO_SC, __VA_ARGS__)                                \
        X(VIDEO_PIX_FMT_PNG, __VA_ARGS__)

#define VIDEO_PIX_FMT_JPEG VIDEO_FOURCC('J', 'P', 'E', 'G')

#define VIDEO_PIX_FMT_H264 VIDEO_FOURCC('H', '2', '6', '4')

#define VIDEO_PIX_FMT_H264_NO_SC VIDEO_FOURCC('A', 'V', 'C', '1')

#define VIDEO_PIX_FMT_PNG VIDEO_FOURCC('P', 'N', 'G', ' ')


#define _VIDEO_FMT_OR_EQ(pixfmt_a, pixfmt_b) || ((pixfmt_a) == (pixfmt_b))

#define VIDEO_FMT_IS_GRAYSCALE(pixfmt)                                          \
        (0 VIDEO_FOREACH_GRAYSCALE(_VIDEO_FMT_OR_EQ, pixfmt))

#define VIDEO_FMT_IS_BAYER(pixfmt)                                              \
        (0 VIDEO_FOREACH_BAYER(_VIDEO_FMT_OR_EQ, pixfmt))

#define VIDEO_FMT_IS_RGB(pixfmt)                                                \
        (0 VIDEO_FOREACH_RGB(_VIDEO_FMT_OR_EQ, pixfmt))

#define VIDEO_FMT_IS_YUV(pixfmt)                                                \
        (0 VIDEO_FOREACH_YUV(_VIDEO_FMT_OR_EQ, pixfmt))

#define VIDEO_FMT_IS_MIPI_PACKED(pixfmt)                                        \
        (0 VIDEO_FOREACH_BAYER_MIPI_PACKED(_VIDEO_FMT_OR_EQ, pixfmt)            \
           VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED(_VIDEO_FMT_OR_EQ, pixfmt))

#define VIDEO_FMT_IS_PADDED(pixfmt)                                             \
        (0 VIDEO_FOREACH_BAYER_PADDED(_VIDEO_FMT_OR_EQ, pixfmt)                 \
           VIDEO_FOREACH_GRAYSCALE_PADDED(_VIDEO_FMT_OR_EQ, pixfmt))

#define VIDEO_FMT_IS_SEMI_PLANAR(pixfmt)                                        \
        (0 VIDEO_FOREACH_YUV_SEMI_PLANAR(_VIDEO_FMT_OR_EQ, pixfmt))

#define VIDEO_FMT_IS_FULL_PLANAR(pixfmt)                                        \
        (0 VIDEO_FOREACH_YUV_FULL_PLANAR(_VIDEO_FMT_OR_EQ, pixfmt))

static inline unsigned int video_bits_per_pixel(uint32_t pixfmt)
{
        switch (pixfmt) {
        case VIDEO_PIX_FMT_SBGGR8:
        case VIDEO_PIX_FMT_SGBRG8:
        case VIDEO_PIX_FMT_SGRBG8:
        case VIDEO_PIX_FMT_SRGGB8:
        case VIDEO_PIX_FMT_GREY:
                return 8;
        case VIDEO_PIX_FMT_SBGGR10P:
        case VIDEO_PIX_FMT_SGBRG10P:
        case VIDEO_PIX_FMT_SGRBG10P:
        case VIDEO_PIX_FMT_SRGGB10P:
        case VIDEO_PIX_FMT_Y10P:
                return 10;
        case VIDEO_PIX_FMT_SBGGR12P:
        case VIDEO_PIX_FMT_SGBRG12P:
        case VIDEO_PIX_FMT_SGRBG12P:
        case VIDEO_PIX_FMT_SRGGB12P:
        case VIDEO_PIX_FMT_Y12P:
        case VIDEO_PIX_FMT_NV12:
        case VIDEO_PIX_FMT_NV21:
        case VIDEO_PIX_FMT_YUV420:
        case VIDEO_PIX_FMT_YVU420:
                return 12;
        case VIDEO_PIX_FMT_SBGGR14P:
        case VIDEO_PIX_FMT_SGBRG14P:
        case VIDEO_PIX_FMT_SGRBG14P:
        case VIDEO_PIX_FMT_SRGGB14P:
        case VIDEO_PIX_FMT_Y14P:
                return 14;
        case VIDEO_PIX_FMT_RGB565:
        case VIDEO_PIX_FMT_YUYV:
        case VIDEO_PIX_FMT_YVYU:
        case VIDEO_PIX_FMT_UYVY:
        case VIDEO_PIX_FMT_VYUY:
        case VIDEO_PIX_FMT_SBGGR8P16:
        case VIDEO_PIX_FMT_SGBRG8P16:
        case VIDEO_PIX_FMT_SGRBG8P16:
        case VIDEO_PIX_FMT_SRGGB8P16:
        case VIDEO_PIX_FMT_SBGGR10:
        case VIDEO_PIX_FMT_SGBRG10:
        case VIDEO_PIX_FMT_SGRBG10:
        case VIDEO_PIX_FMT_SRGGB10:
        case VIDEO_PIX_FMT_SBGGR12:
        case VIDEO_PIX_FMT_SGBRG12:
        case VIDEO_PIX_FMT_SGRBG12:
        case VIDEO_PIX_FMT_SRGGB12:
        case VIDEO_PIX_FMT_SBGGR14:
        case VIDEO_PIX_FMT_SGBRG14:
        case VIDEO_PIX_FMT_SGRBG14:
        case VIDEO_PIX_FMT_SRGGB14:
        case VIDEO_PIX_FMT_SBGGR16:
        case VIDEO_PIX_FMT_SGBRG16:
        case VIDEO_PIX_FMT_SGRBG16:
        case VIDEO_PIX_FMT_SRGGB16:
        case VIDEO_PIX_FMT_Y8P16:
        case VIDEO_PIX_FMT_Y10:
        case VIDEO_PIX_FMT_Y12:
        case VIDEO_PIX_FMT_Y14:
        case VIDEO_PIX_FMT_Y16:
        case VIDEO_PIX_FMT_NV16:
        case VIDEO_PIX_FMT_NV61:
                return 16;
        case VIDEO_PIX_FMT_BGR24:
        case VIDEO_PIX_FMT_RGB24:
        case VIDEO_PIX_FMT_NV24:
        case VIDEO_PIX_FMT_NV42:
        case VIDEO_PIX_FMT_YUV24:
                return 24;
        case VIDEO_PIX_FMT_XYUV32:
        case VIDEO_PIX_FMT_ARGB32:
        case VIDEO_PIX_FMT_ABGR32:
        case VIDEO_PIX_FMT_RGBA32:
        case VIDEO_PIX_FMT_BGRA32:
        case VIDEO_PIX_FMT_XRGB32:
        case VIDEO_PIX_FMT_XBGR32:
        case VIDEO_PIX_FMT_RGBX32:
        case VIDEO_PIX_FMT_BGRX32:
                return 32;
        default:
                /* Variable number of bits per pixel or unknown format */
                return 0;
        }
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_VIDEO_FORMATS_H */
```

## 73.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited.。

版权（Copyright）：2025 NXP。

版权（Copyright）：© 2025 STMicroelectronics。

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 1344 行

每像素位数可变，或格式未知。

### 注释 3：原第 1357 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_VIDEO_FORMATS_H`。

## 73.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/formats_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [video_bits_per_pixel](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabdbd1b0f40af6663d81402deefdd387f)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [VIDEO_PIX_FMT_SBGGR8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabc0205ce5c6426051fdec88d92f123e3)
- [VIDEO_PIX_FMT_SGBRG8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa9edb9c562fc3c86b61e071970fae60d)
- [VIDEO_PIX_FMT_SGRBG8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga19d8dc905695229097dffe659f2a806e)
- [VIDEO_PIX_FMT_SRGGB8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabf0dde810e75d37823891ed03811482c)
- [VIDEO_PIX_FMT_GREY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa3af19adaf282b83a6c16f265a4260dc)
- [VIDEO_PIX_FMT_SBGGR10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga3751a8dce1c7459df06f83cd09449b5d)
- [VIDEO_PIX_FMT_SGBRG10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gad69ab9041428488051bdb45f42ad4271)
- [VIDEO_PIX_FMT_SGRBG10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa28c6306a3ed44a0e50c16e0eac86688)
- [VIDEO_PIX_FMT_SRGGB10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga604d2f3501407546aa924e2fdb37be2f)
- [VIDEO_PIX_FMT_Y10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga502df4612995fc39e03d6de3ec675159)
- [VIDEO_PIX_FMT_SBGGR12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gab5b5375f050d039e05032c77ac838b31)
- [VIDEO_PIX_FMT_SGBRG12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaecedece3398a6e2f62c20c2eb3f6d3c2)
- [VIDEO_PIX_FMT_SGRBG12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga02d91ebf4b5150d5fa437bb3a7a6e872)
- [VIDEO_PIX_FMT_SRGGB12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga348c15cc77c728fdac773d58341cbc1d)
- [VIDEO_PIX_FMT_Y12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga263e6553a77d00bc509c1b270efebb0b)
- [VIDEO_PIX_FMT_NV12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga6e5538e8f21a5be750eec38c2a16ad2f)
- [VIDEO_PIX_FMT_NV21](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga171cb239b78ca49b9232dcb9d5e9f43f)
- [VIDEO_PIX_FMT_YUV420](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga9054aa564afdf3b6129539fbda30d9bf)
- [VIDEO_PIX_FMT_YVU420](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga9294d7e95c9fe00df93248958b7bef0e)
- [VIDEO_PIX_FMT_SBGGR14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gac3413c36b3ce91e5658cd0f973c1f3d7)
- [VIDEO_PIX_FMT_SGBRG14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga89eb47d1dd60794781ee91cb5ae199ad)
- [VIDEO_PIX_FMT_SGRBG14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae06f742e31a62295d3ee16af8eec1b06)
- [VIDEO_PIX_FMT_SRGGB14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga66646a639518285810335a70337277d7)
- [VIDEO_PIX_FMT_Y14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gada0124aad9c10d403966b1e3851cd968)
- [VIDEO_PIX_FMT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf009d0eb7dbdb3bfd8883da03478c1ec)
- [VIDEO_PIX_FMT_YUYV](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gad186d3166acec11c893ae57a0ae68f11)
- [VIDEO_PIX_FMT_YVYU](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga299af047675a110c109cee954f55fca6)
- [VIDEO_PIX_FMT_UYVY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadca3ee56c798cf05b63cbfc87af98ce3)
- [VIDEO_PIX_FMT_VYUY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga63c825ce5dc6c863d355195fde40acb1)
- [VIDEO_PIX_FMT_SBGGR8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabb167fd4b58db338de823dc285e62342)
- [VIDEO_PIX_FMT_SGBRG8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga07b22957c7fdc64fd3089fbcb811d599)
- [VIDEO_PIX_FMT_SGRBG8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4df33d1a41c2dbdc16c19113be13760b)
- [VIDEO_PIX_FMT_SRGGB8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gab471cd15aa874a5deadf7b54b826a90e)
- [VIDEO_PIX_FMT_SBGGR10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga0b55190a343fe891bdbb7b148e7feeae)
- [VIDEO_PIX_FMT_SGBRG10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8e0f47c16483b14b45a593e9e542a987)
- [VIDEO_PIX_FMT_SGRBG10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga011cc337bc54480d1e11c3e6833ae398)
- [VIDEO_PIX_FMT_SRGGB10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga249cbf808658dab777a705fd9deb2986)
- [VIDEO_PIX_FMT_SBGGR12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa2d7712f655dfcb3c74b4f4ec9941402)
- [VIDEO_PIX_FMT_SGBRG12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa3df9d0af327e609b25e050a4362c2e2)
- [VIDEO_PIX_FMT_SGRBG12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf18e6647596613e07ec3c651574b08ba)
- [VIDEO_PIX_FMT_SRGGB12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga7b167f2b6a147d325a685825274cd2f2)
- [VIDEO_PIX_FMT_SBGGR14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga403f40a7e15319365c6ca8f3f5f19d21)
- [VIDEO_PIX_FMT_SGBRG14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga6c98a7066d7d3bdd8fce3d3651772153)
- [VIDEO_PIX_FMT_SGRBG14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf58481956952b13b071b1a68541b9c21)
- [VIDEO_PIX_FMT_SRGGB14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa6e4c240372e53db8ea3472cc456af58)
- [VIDEO_PIX_FMT_SBGGR16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae096669643176203199270317dc3449d)
- [VIDEO_PIX_FMT_SGBRG16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga7f00eb633dd312ea89097edc82dc8f0c)
- [VIDEO_PIX_FMT_SGRBG16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4269984ce806e64ba5ccd41c1429769a)
- [VIDEO_PIX_FMT_SRGGB16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4f31b5d397868e952d53022c6c8e5823)
- [VIDEO_PIX_FMT_Y8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gad40f2d8628a39f0d87d5f0a337d7f8c4)
- [VIDEO_PIX_FMT_Y10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga0506f2c8aa1a82f02fc9383d99b43bc3)
- [VIDEO_PIX_FMT_Y12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga166b2144cec4b4f92fadda30e81b7d22)
- [VIDEO_PIX_FMT_Y14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga7d9379f19abcbac17bad3d6359a42d9d)
- [VIDEO_PIX_FMT_Y16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa65fe8bd917dd2fe95fa87530fc3055f)
- [VIDEO_PIX_FMT_NV16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabbfecc5e0c2c4115c57d4772eaa4918f)
- [VIDEO_PIX_FMT_NV61](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga3463a33faa910f98280c96f40d3c65e7)
- [VIDEO_PIX_FMT_BGR24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf1f8775bbdd0508c4e21a58dfcfc362d)
- [VIDEO_PIX_FMT_RGB24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga03e6be04b23b9735c96231eebc687158)
- [VIDEO_PIX_FMT_NV24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga06864b3b1b7d563a9cd2f15c33cdd2d8)
- [VIDEO_PIX_FMT_NV42](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gace39ba88d298b1991412f73fb4fe9d18)
- [VIDEO_PIX_FMT_YUV24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabcdd44434323cc0e0634e94f23f83146)
- [VIDEO_PIX_FMT_XYUV32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga017bcbec587314f569d6d0e4fbdda351)
- [VIDEO_PIX_FMT_ARGB32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga5cd54fb54967a80576082cadd5941670)
- [VIDEO_PIX_FMT_ABGR32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaffb650a5f9b2b03890283ecfe95aee04)
- [VIDEO_PIX_FMT_RGBA32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8ee1e3b82eeeb02188157aa4b4b5d842)
- [VIDEO_PIX_FMT_BGRA32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga515e379bc7f59a8062f3e2a5980b0626)
- [VIDEO_PIX_FMT_XRGB32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8be24c04210f8818d75082bd710db8b1)
- [VIDEO_PIX_FMT_XBGR32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4ae1acc3d44a1698e0d48f299f061a49)
- [VIDEO_PIX_FMT_RGBX32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadfdb271a780b10a29a356675014a25c2)
- [VIDEO_PIX_FMT_BGRX32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadf53a84505c1299a5c97a0213c989103)

---

[上一章](P072_focaltech_ft9001_pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P074_fs.h_源码浏览.md)
