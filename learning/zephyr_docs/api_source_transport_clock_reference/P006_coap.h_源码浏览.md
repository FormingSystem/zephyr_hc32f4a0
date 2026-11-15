---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-6
title: coap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_coap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)。

## 6.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
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
<a id="foldopen00050"></a>
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
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00116"></a>
<a id="l00123"></a>
<a id="l00129"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="foldopen00154"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="foldopen00250"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="foldopen00268"></a>
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
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="foldopen00316"></a>
<a id="l00316"></a>
<a id="l00318"></a>
<a id="l00320"></a>
<a id="l00322"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="foldopen00336"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="foldopen00357"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="foldopen00383"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="foldopen00409"></a>
<a id="l00409"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00420"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="foldopen00428"></a>
<a id="l00428"></a>
<a id="l00430"></a>
<a id="l00432"></a>
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
<a id="foldopen00449"></a>
<a id="l00449"></a>
<a id="l00451"></a>
<a id="l00453"></a>
<a id="l00455"></a>
<a id="l00457"></a>
<a id="l00459"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="foldopen00797"></a>
<a id="l00797"></a>
<a id="l00798"></a>
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
<a id="l00826"></a>
<a id="foldopen00835"></a>
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
<a id="foldopen00855"></a>
<a id="l00855"></a>
<a id="l00857"></a>
<a id="l00859"></a>
<a id="l00861"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00876"></a>
<a id="l00889"></a>
<a id="l00890"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00934"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00948"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00970"></a>
<a id="l00971"></a>
<a id="l00972"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="l00995"></a>
<a id="l00996"></a>
<a id="l01009"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01021"></a>
<a id="l01022"></a>
<a id="l01023"></a>
<a id="l01036"></a>
<a id="l01037"></a>
<a id="l01038"></a>
<a id="l01039"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01069"></a>
<a id="l01070"></a>
<a id="l01079"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01082"></a>
<a id="l01083"></a>
<a id="l01096"></a>
<a id="l01097"></a>
<a id="l01098"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01110"></a>
<a id="l01111"></a>
<a id="l01112"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="l01141"></a>
<a id="l01142"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="l01159"></a>
<a id="l01160"></a>
<a id="l01161"></a>
<a id="l01162"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="l01179"></a>
<a id="l01180"></a>
<a id="l01190"></a>
<a id="l01191"></a>
<a id="l01192"></a>
<a id="l01199"></a>
<a id="l01200"></a>
<a id="l01201"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01220"></a>
<a id="l01221"></a>
<a id="l01222"></a>
<a id="l01233"></a>
<a id="l01234"></a>
<a id="l01235"></a>
<a id="l01246"></a>
<a id="l01247"></a>
<a id="l01248"></a>
<a id="l01262"></a>
<a id="l01263"></a>
<a id="l01264"></a>
<a id="l01265"></a>
<a id="l01278"></a>
<a id="l01279"></a>
<a id="l01280"></a>
<a id="l01281"></a>
<a id="l01282"></a>
<a id="l01293"></a>
<a id="l01294"></a>
<a id="l01295"></a>
<a id="l01304"></a>
<a id="l01305"></a>
<a id="l01312"></a>
<a id="l01313"></a>
<a id="l01321"></a>
<a id="l01322"></a>
<a id="l01330"></a>
<a id="l01331"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="l01346"></a>
<a id="l01347"></a>
<a id="l01356"></a>
<a id="l01357"></a>
<a id="l01366"></a>
<a id="l01367"></a>
<a id="l01373"></a>
<a id="l01374"></a>
<a id="l01380"></a>
<a id="l01381"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01410"></a>
<a id="l01411"></a>
<a id="l01412"></a>
<a id="l01420"></a>
<a id="l01421"></a>
<a id="l01431"></a>
<a id="l01432"></a>
<a id="l01433"></a>
<a id="l01450"></a>
<a id="l01451"></a>
<a id="l01452"></a>
<a id="l01465"></a>
<a id="l01466"></a>
<a id="l01467"></a>
<a id="l01468"></a>
<a id="l01476"></a>
<a id="l01477"></a>
<a id="l01487"></a>
<a id="l01488"></a>
<a id="l01489"></a>
<a id="l01499"></a>
<a id="l01500"></a>
<a id="l01501"></a>
<a id="l01513"></a>
<a id="l01514"></a>
<a id="l01515"></a>
<a id="l01516"></a>
<a id="l01517"></a>
<a id="l01518"></a>
<a id="l01519"></a>
<a id="l01523"></a>
<a id="l01524"></a>
<a id="agroup__coap_html_ga03129c8f853862f8395cc567edbf4642"></a>
<a id="agroup__coap_html_ga03287eb3187aa28e0e83e0e0c72e2631"></a>
<a id="agroup__coap_html_ga0b84eee85b854bf087bceb7566e93086"></a>
<a id="agroup__coap_html_ga10c4a0d7e2052f3116fbf3b355fe75db"></a>
<a id="agroup__coap_html_ga1244716ecf06fad1013131c42eab8c5c"></a>
<a id="agroup__coap_html_ga196390e6f016b72b3ae2ae9e69bed1b7"></a>
<a id="agroup__coap_html_ga1adc19283d0b41f6af152d41b32b86d7"></a>
<a id="agroup__coap_html_ga1bd7be0a5390f0599e7bec0cbd79daf8"></a>
<a id="agroup__coap_html_ga1ea81a365834e96f43ab7be573069d26"></a>
<a id="agroup__coap_html_ga21b8f4ffeecc7900f6bf299836d2b5b3"></a>
<a id="agroup__coap_html_ga24000def8534acdcd2c61836dc690367"></a>
<a id="agroup__coap_html_ga2410e973bf3192244426df346230608b"></a>
<a id="agroup__coap_html_ga262f21fdad778db96c8bd700ba66ce1b"></a>
<a id="agroup__coap_html_ga27a58a69f632551aa7a2394ae2badacf"></a>
<a id="agroup__coap_html_ga27e3008b8511333e0c0115ba928017f3"></a>
<a id="agroup__coap_html_ga28ccf00fb1f5f13f747e61c2e3008b5c"></a>
<a id="agroup__coap_html_ga2a323287262bbb6a4932e7911ddb652c"></a>
<a id="agroup__coap_html_ga2aa4140ee83ca4090a5604e34d1f1446"></a>
<a id="agroup__coap_html_ga2bcfc7340ed2347862b0f003e1b00a4b"></a>
<a id="agroup__coap_html_ga2fd0613e61274ec4b9b7bab3ab11ccce"></a>
<a id="agroup__coap_html_ga323644931c927b8988aafd89dacb993c"></a>
<a id="agroup__coap_html_ga33c351ac06b5ae9217cd53d8cf330fbd"></a>
<a id="agroup__coap_html_ga34c1c3b75e0787d8526b7a7a5b5a1633"></a>
<a id="agroup__coap_html_ga34c5eac86081ea46b63c1cbb7c1315e9"></a>
<a id="agroup__coap_html_ga361c17b698bdaa0fc529b7338efefd8c"></a>
<a id="agroup__coap_html_ga37b58c38c150751d31207ece416529d8"></a>
<a id="agroup__coap_html_ga3b0cc9bfabdddeffd98f36d7f15dd416"></a>
<a id="agroup__coap_html_ga3b375b7580246d1266293d09902f3d9f"></a>
<a id="agroup__coap_html_ga3c42861f8442e548f560acf3deca6baa"></a>
<a id="agroup__coap_html_ga3f66d5935dcacfeebcac2b3001d7b57a"></a>
<a id="agroup__coap_html_ga4180b2476430fbe4a5e0418fb628ea91"></a>
<a id="agroup__coap_html_ga44ca9e8b0fe2544b8da73efda10b187b"></a>
<a id="agroup__coap_html_ga46b315c30b642eec65bcb84e9c937ee7"></a>
<a id="agroup__coap_html_ga50f7837da003601479dbc470ba9898ae"></a>
<a id="agroup__coap_html_ga518d5f4422ff45f2b4a296f249da89cd"></a>
<a id="agroup__coap_html_ga57486e764f0feb6544fa3b0d19935afd"></a>
<a id="agroup__coap_html_ga59f6d6ff09861ab3df9cda894f45de40"></a>
<a id="agroup__coap_html_ga5d9fd91c714705b56780264823c56fe6"></a>
<a id="agroup__coap_html_ga63388c629da5370d2e711cdc9aabd837"></a>
<a id="agroup__coap_html_ga6542f6350f6e4ed861d6c482617dd5d0"></a>
<a id="agroup__coap_html_ga65cb5f7ac01ea5ebe1c6e30a7c70ad4e"></a>
<a id="agroup__coap_html_ga66f986f8a1157236bea27133c2a2538b"></a>
<a id="agroup__coap_html_ga6a5049accfa0cd7106a3a6593c598545"></a>
<a id="agroup__coap_html_ga6a6547e3c755cf7a5033302c8294e0b7"></a>
<a id="agroup__coap_html_ga6bec94992ac450dca03436a6ad74efb4"></a>
<a id="agroup__coap_html_ga6e0947048052e733a3571fdc8955b2d7"></a>
<a id="agroup__coap_html_ga712c1468f936a3af7dc39a86a5961922"></a>
<a id="agroup__coap_html_ga7b8b3041e2f4ae26e663ff7431a6e6e3"></a>
<a id="agroup__coap_html_ga800831ddfe19b1a5637a5edd9e78c470"></a>
<a id="agroup__coap_html_ga84eda10c4bf3e62241e686fdfa828868"></a>
<a id="agroup__coap_html_ga8b5966a29054ace04cae81d4da588e72"></a>
<a id="agroup__coap_html_ga8b621232b740d8e8e1771fba24897121"></a>
<a id="agroup__coap_html_ga90e6aab174f8977f0a3b5fbe1a20297c"></a>
<a id="agroup__coap_html_ga941ee9d68f1a628755aa79c249cbae58"></a>
<a id="agroup__coap_html_ga94a8f9956742d3928fc3c63b8d01ae73"></a>
<a id="agroup__coap_html_ga94ceba78cbd2440f91d9b30d6b06594d"></a>
<a id="agroup__coap_html_ga9626781d73d18c1305f654ef4723e5db"></a>
<a id="agroup__coap_html_ga998a3b01a3a535614183ac08da101811"></a>
<a id="agroup__coap_html_ga99e8ff6696fb7916932ae32c3e3ec8a2"></a>
<a id="agroup__coap_html_ga9d63518c701ebdb4c7f65c5368d00d27"></a>
<a id="agroup__coap_html_gaa170f8dbe1633e2b02c9c2d8dd27f181"></a>
<a id="agroup__coap_html_gaa715f58474d6f668f47dc66e478ba6b2"></a>
<a id="agroup__coap_html_gaabdfa8cf28cc2c3a14ae0af5fa7e7212"></a>
<a id="agroup__coap_html_gab045e6e61ef8c35f85591b8792d88952"></a>
<a id="agroup__coap_html_gab2dc876158b3248fa35fbc61a1faf19a"></a>
<a id="agroup__coap_html_gab8ab58c900a4b0396ca7722c754fb1ec"></a>
<a id="agroup__coap_html_gab8f9e9cdfa20920d5d25fb1507a2286d"></a>
<a id="agroup__coap_html_gabdcc1f443e89bd035522cbab7dfee879"></a>
<a id="agroup__coap_html_gaca300a216781d360d2cd64e8e9f1ae8f"></a>
<a id="agroup__coap_html_gacfe30c84434dc8adbf3d399ec0e51bec"></a>
<a id="agroup__coap_html_gad0c738d308f9cca8ea5cdb79449282cb"></a>
<a id="agroup__coap_html_gad9db2ced9b882265c16e3039f893ca03"></a>
<a id="agroup__coap_html_gadcd3a93a702a2a0b428f39b71dd67954"></a>
<a id="agroup__coap_html_gaddb02509934f5bac20b7c7f83aea4cd8"></a>
<a id="agroup__coap_html_gade5f4995c6419db03ce3e7ff7ca1cfcb"></a>
<a id="agroup__coap_html_gadeaa59fd7b6eab454d5930289b4e08f7"></a>
<a id="agroup__coap_html_gae4bf952fdf9e3d03ab0b0df4c3c0d054"></a>
<a id="agroup__coap_html_gae5829b14002cc4d24cf8501ab960c35a"></a>
<a id="agroup__coap_html_gae6d93b1f93734302be75ee417813e5d1"></a>
<a id="agroup__coap_html_gaed883ea6cec3acc5eb570e152dc52e25"></a>
<a id="agroup__coap_html_gaf006c8048ed7b863e70dbdd64bc3d608"></a>
<a id="agroup__coap_html_gaf2cd52a5976556c2093bc770bb61c192"></a>
<a id="agroup__coap_html_gaf3275841a174b4438c20a1e6e364ea8a"></a>
<a id="agroup__coap_html_gaf361fd233f1aa650650108ae1e205ede"></a>
<a id="agroup__coap_html_gafbc8c15ef03b762f9411c38b03aa403b"></a>
<a id="agroup__coap_html_gafc61a6878d82f81565ab752ced0ce2be"></a>
<a id="agroup__coap_html_gafd01c39fac8f173edc04337161e92264"></a>
<a id="agroup__coap_html_gafdaecca5ad26bab4fb7c9ee3477318f8"></a>
<a id="agroup__coap_html_gafffadd4a837e48fd72af20468ccd86f2"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a026916ae7964a98edeadd3f09e9d18ad"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a289ade02833b57bffd915e648e050e52"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a301eb722445472dba93d5accd6e0dd31"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a4d77322514521e8dfea01f4a1a6e5886"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a5e5e31cc4647d5e0fdd1c8fe6cfa2661"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a5f49a566d37b2cda0c624d76aee08bd1"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a671730c6d2f1a339fcd557c5452150af"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a7390f381b1aa8a4aa21d98527950a152"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a85c04541bc8580c2ae915946fd677c15"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a86c2bff8add69428d164431b3091a8e9"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a8de29a7ee6bb960a97d6b415217b4640"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a95a8d4bee68a3829dfb4f3a024c8bf68"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a989a6528edc653c0b693ed875481e82d"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26aaa43062a8146c1e2e09183228a540d2e"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26aabd72cff6669d382aa04c53e764d0b49"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26ab447505d233aed9fd8ad28070d317544"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26abc76b74967e491c10f320bf19c9026d4"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26abf324915aa498c64a733a0098de4a082"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26ac528f38c3e8553d83e0455097f4fbdf9"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26acb76dbf11b47477144cc4ece3357283c"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26ad2d9fe8dd5beda74b522377c0b76275b"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26adfd3e5e3c6ad5715127bb444c205fbce"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26ae4e3ff451c626421b9b329790f019dd8"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26aecaac4a0e9c821dfc20536951409dd48"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26aef6b165b9d3f8f4b477431058815c16b"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26af6d379fef704c269406b782c60772ecd"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26afebd274586351951ffe9c8f26b270dec"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26afeee555ef54f138db58b14ad2c328d04"></a>
<a id="agroup__coap_html_gga2a323287262bbb6a4932e7911ddb652ca19ebfb46899b440124322bb67c906cb3"></a>
<a id="agroup__coap_html_gga2a323287262bbb6a4932e7911ddb652ca21758021d7f3a36bf6ede06daa82dbf0"></a>
<a id="agroup__coap_html_gga2a323287262bbb6a4932e7911ddb652cae8b0b1231d095b3e7a972ca4c86d8dce"></a>
<a id="agroup__coap_html_gga2a323287262bbb6a4932e7911ddb652caeeb51bb18780c20df5b25183d52d42de"></a>
<a id="agroup__coap_html_gga3b375b7580246d1266293d09902f3d9fa287b951159fd51b84a2e0491b012f84c"></a>
<a id="agroup__coap_html_gga3b375b7580246d1266293d09902f3d9fa629a304bea0c85c7b2bf746b26216a4f"></a>
<a id="agroup__coap_html_gga3b375b7580246d1266293d09902f3d9fa65c04ee4847d0c595238079ac9564e8d"></a>
<a id="agroup__coap_html_gga3b375b7580246d1266293d09902f3d9fa7b2fe2187018bce9132af2763b57307d"></a>
<a id="agroup__coap_html_gga6a6547e3c755cf7a5033302c8294e0b7a025300cb0dc4c4de8eb0b0e0b4eb5317"></a>
<a id="agroup__coap_html_gga6a6547e3c755cf7a5033302c8294e0b7a78f97b895f29819bf3f8b0314967f20e"></a>
<a id="agroup__coap_html_gga6a6547e3c755cf7a5033302c8294e0b7a91637ef7c9f57cdcc65d0118008251db"></a>
<a id="agroup__coap_html_gga6a6547e3c755cf7a5033302c8294e0b7aba51bcab79bf75080ccf75c1ec38a3d6"></a>
<a id="agroup__coap_html_gga6a6547e3c755cf7a5033302c8294e0b7adca55e3d2b4b41b249f6b2f67074d708"></a>
<a id="agroup__coap_html_gga6a6547e3c755cf7a5033302c8294e0b7adccbea1fe9a43433cf8471e32208a5ac"></a>
<a id="agroup__coap_html_gga6a6547e3c755cf7a5033302c8294e0b7afa4070fed5c01b28bb1a59e3f0c021f4"></a>
<a id="agroup__coap_html_gga712c1468f936a3af7dc39a86a5961922a147ddf4b0e5d1a8c11f0da2c71dee4d8"></a>
<a id="agroup__coap_html_gga712c1468f936a3af7dc39a86a5961922a1aaf8f841c18e281b176793bb331993d"></a>
<a id="agroup__coap_html_gga712c1468f936a3af7dc39a86a5961922a549135603208a878cdefd6c5ca1a039b"></a>
<a id="agroup__coap_html_gga712c1468f936a3af7dc39a86a5961922a6998c79e63cf65e7f86ddd5713d48dce"></a>
<a id="agroup__coap_html_gga712c1468f936a3af7dc39a86a5961922a7266f448a391ea2a2763f1ded5397520"></a>
<a id="agroup__coap_html_gga712c1468f936a3af7dc39a86a5961922a834d479806b513818e2237f3f1c56968"></a>
<a id="agroup__coap_html_gga712c1468f936a3af7dc39a86a5961922acfc37f84eabccdde4bd84b06c6a5e753"></a>
<a id="agroup__coap_html_gga712c1468f936a3af7dc39a86a5961922ad2052905aff08c58585dcf6c6caddc19"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a06e91bbb4fa2144543d4148d3245ad25"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a07ea6f395818a7019bb9e6a6e34d2d74"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a0efdc30ce5551daffd093b2a8466978a"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a26c1bcd7af4fccd949e3de35fc2d88e6"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a2a47428ec35972d256da05104ea6396f"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a2b6f7575ff75fbc51ac5800a693b19af"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a30da986503e1e15243b74a16b161901c"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a344707b9f4cb71310f2ccf5e8050d17a"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a402bb0a642a07d951c35d69736fd3f33"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a4aa7cdfa66bd89f21f592eaf3ebe0972"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a4c61e26d11841c76debe2f99de5e9756"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a53169a1c7b07c9e97f79dfc06af3eb51"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a620e8b59f67f89de8a38dc76c8fcc594"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a649cb25887a08fc21eb0cac51f58d3e5"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a7984f2c4845610491bda964111a1c8e7"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a8aaa54af114fd1db631566afa69f162d"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a96b5a15937e875b3087307cc5faab1af"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3a9aa645f3c03f818848d5b728432998e3"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3aaa6222533e1a6f1284fc5857884ad24d"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3ab4cda4d3732fd12b9f203a2475c20981"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3ac3166e67b5f5bf3cefee58c8ff58e5b8"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3ac728800fc8f0d80e37dcf322e75eb27d"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3adb4d27052247b9a79ad7fcc0cc30c71c"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3ae4d2c93b545708926813217cd36a96ac"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3ae82be3591d43f0d1c7e89ab764d969bd"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3aeed15ed39751b1533f4a1f825c73d0a2"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3af71df6b0647047115c20790eebb3ce30"></a>
<a id="agroup__coap_html_gga7b8b3041e2f4ae26e663ff7431a6e6e3afd0725f0ceb5ce22a6c7b390ca7efc9d"></a>
<a id="agroup__coap_html_gga94a8f9956742d3928fc3c63b8d01ae73a141f183724ad6da14c3992c0990d6239"></a>
<a id="agroup__coap_html_gga94a8f9956742d3928fc3c63b8d01ae73a1fbd90fd5cb309e2de6954f46174dc4f"></a>
<a id="agroup__coap_html_gga94a8f9956742d3928fc3c63b8d01ae73a2797149fb3811d706dab291e9edc9436"></a>
<a id="agroup__coap_html_gga94a8f9956742d3928fc3c63b8d01ae73a483a382550b38468cc66bdce9f4743ea"></a>
<a id="agroup__coap_html_gga94a8f9956742d3928fc3c63b8d01ae73a7ca73ff57a6c7fb1517b44f2ce17d3f9"></a>
<a id="agroup__coap_html_gga94a8f9956742d3928fc3c63b8d01ae73a88d952174bb3e4ffb9ab11a599952760"></a>
<a id="agroup__coap_html_gga94a8f9956742d3928fc3c63b8d01ae73a975381d286c1e9b998e41ef0a234d17a"></a>
<a id="agroup__coap_html_gga94a8f9956742d3928fc3c63b8d01ae73adb96bf55e914f4852e92dc65752c372a"></a>
<a id="agroup__coap_html_gga94a8f9956742d3928fc3c63b8d01ae73af068aa8d09032352799bc60868607997"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="agroup__math__extras_html_ga4cb313f98c3fd3b00d6f4db74a9a0076"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="amath__extras_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructcoap__block__context_html"></a>
<a id="astructcoap__block__context_html_a27db79dc3a2af6dd9f41e3008dcde87a"></a>
<a id="astructcoap__block__context_html_a27eb897fa2d455eb79220f1654509da3"></a>
<a id="astructcoap__block__context_html_a474f54e2a29d41b9d449f8574e747067"></a>
<a id="astructcoap__core__metadata_html"></a>
<a id="astructcoap__observer_html"></a>
<a id="astructcoap__observer_html_a24a9f853db17ff623f4c510fd0892eb5"></a>
<a id="astructcoap__observer_html_a5d5e9494804ef64bc705f2bb08ac7afd"></a>
<a id="astructcoap__observer_html_a6d7d792120b935bf61c739f95dd7361c"></a>
<a id="astructcoap__observer_html_a7486199db30c9aaaba693ce64fd46879"></a>
<a id="astructcoap__observer_html_a901f148d2eb697206fde732050c3d8b4"></a>
<a id="astructcoap__option_html"></a>
<a id="astructcoap__option_html_a01c8abdf27c3f8c5a816af33c0c093d4"></a>
<a id="astructcoap__option_html_abca15b0a8f9bdcb3f493ab3801d4b58f"></a>
<a id="astructcoap__option_html_aff07b5d3673169b6316b91dc27780891"></a>
<a id="astructcoap__packet_html"></a>
<a id="astructcoap__packet_html_a46c0842c785b8de5eb8564950a786c02"></a>
<a id="astructcoap__packet_html_a48c216a7da37e85942d271c85a79bcb6"></a>
<a id="astructcoap__packet_html_a8116711bcdff1fa6b0cf5c4fa9ab88d1"></a>
<a id="astructcoap__packet_html_a95dd8c6fb08ac61a1571c84258579475"></a>
<a id="astructcoap__packet_html_ab302c002da88f6d3a44c3a2215082be4"></a>
<a id="astructcoap__packet_html_ab496dabc7cc0d9b588d7b1bfdd6967dc"></a>
<a id="astructcoap__packet_html_ab4c2196669f38bf3057e83c44c839ff4"></a>
<a id="astructcoap__packet_html_acc5542ba2a69db8957155b90e75fd563"></a>
<a id="astructcoap__pending_html"></a>
<a id="astructcoap__pending_html_a05ca08379d13e10dfe86322f666c3d97"></a>
<a id="astructcoap__pending_html_a0a506507e472b3813e672f2b455e4bcc"></a>
<a id="astructcoap__pending_html_a4eb95f8fadef7d42aecdf25cc5ee3b1d"></a>
<a id="astructcoap__pending_html_a8aebb187845bcb6cb07dee68927f1aa6"></a>
<a id="astructcoap__pending_html_a8b1952271bd0c733c2fbcb158b60ca99"></a>
<a id="astructcoap__pending_html_a8b95f80a6eaac759ed0895201ff089d9"></a>
<a id="astructcoap__pending_html_ab06a3561fd9ce0477862babe18e44a1e"></a>
<a id="astructcoap__pending_html_ab31339cc91df71ee6f90d5702f722fd6"></a>
<a id="astructcoap__reply_html"></a>
<a id="astructcoap__reply_html_a038ccb29c2abff6168db3247241a8cc3"></a>
<a id="astructcoap__reply_html_a18d40c327933c30681b924446c21ea9d"></a>
<a id="astructcoap__reply_html_a6a888bbb5652761002ce26aba09352cc"></a>
<a id="astructcoap__reply_html_a94d17732056de3d8ecb3412c686091f8"></a>
<a id="astructcoap__reply_html_aa951d9ba4eb7f8041e8e82df9c1401dc"></a>
<a id="astructcoap__reply_html_aea6b98e109e270c08df1554c5eee65fe"></a>
<a id="astructcoap__resource_html"></a>
<a id="astructcoap__resource_html_a1efed8197d44aba3b63aaa9d9bb0f5bb"></a>
<a id="astructcoap__resource_html_a202a83a5aa024a62bd25cc40f42e8d65"></a>
<a id="astructcoap__resource_html_a3152a778e27e36fad7dd62985621d58b"></a>
<a id="astructcoap__resource_html_a3199679fd990d757e9a500fbd7c653d7"></a>
<a id="astructcoap__resource_html_a5035dc9c88c2b0ae557608e34ec14433"></a>
<a id="astructcoap__resource_html_a6975e84ebc67d6aff2efb755695518f5"></a>
<a id="astructcoap__resource_html_a6c1fe25539ecbe4ec2ed7446fff84861"></a>
<a id="astructcoap__resource_html_a7657cb2e9bbac7f98e35b4ed33f13163"></a>
<a id="astructcoap__resource_html_a77dfb6d59c25e6e58141226023bf59ea"></a>
<a id="astructcoap__resource_html_aa0a5465fc5b49a566e3803a9f1638724"></a>
<a id="astructcoap__resource_html_ada7a41309b6ca11612b17fabf6cd56c5"></a>
<a id="astructcoap__resource_html_ae8e1b2b1920689913e0910a82a30e009"></a>
<a id="astructcoap__resource_html_aebe880e3ccbd2441854dfa899dc72c13"></a>
<a id="astructcoap__transmission__parameters_html"></a>
<a id="astructcoap__transmission__parameters_html_a0b43d9e3adfbf7cac09e1ffbbe1f8ce8"></a>
<a id="astructcoap__transmission__parameters_html_a3a9b8bf0f2e00fc0981acdd86d404190"></a>
<a id="astructcoap__transmission__parameters_html_a74c91235bf64fab5e7abc0c9f581e44c"></a>
<a id="astructcoap__transmission__parameters_html_aca76954d785d04312fb834dc524f102c"></a>
<a id="astructnet__sockaddr_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 * Copyright (c) 2021 Nordic Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_COAP_H_
#define ZEPHYR_INCLUDE_NET_COAP_H_


#include <zephyr/types.h>
#include <stddef.h>
#include <stdbool.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/sys/math_extras.h>
#include <zephyr/sys/slist.h>

#if defined(CONFIG_COAP_OSCORE)
struct coap_oscore_context;
#endif /* defined(CONFIG_COAP_OSCORE) */

#ifdef __cplusplus
extern "C" {
#endif

enum coap_option_num {
        COAP_OPTION_IF_MATCH = 1,
        COAP_OPTION_URI_HOST = 3,
        COAP_OPTION_ETAG = 4,
        COAP_OPTION_IF_NONE_MATCH = 5,
        COAP_OPTION_OBSERVE = 6,
        COAP_OPTION_URI_PORT = 7,
        COAP_OPTION_LOCATION_PATH = 8,
        COAP_OPTION_OSCORE = 9,
        COAP_OPTION_URI_PATH = 11,
        COAP_OPTION_CONTENT_FORMAT = 12,
        COAP_OPTION_MAX_AGE = 14,
        COAP_OPTION_URI_QUERY = 15,
        COAP_OPTION_ACCEPT = 17,
        COAP_OPTION_LOCATION_QUERY = 20,
        COAP_OPTION_BLOCK2 = 23,
        COAP_OPTION_BLOCK1 = 27,
        COAP_OPTION_SIZE2 = 28,
        COAP_OPTION_PROXY_URI = 35,
        COAP_OPTION_PROXY_SCHEME = 39,
        COAP_OPTION_SIZE1 = 60,
        COAP_OPTION_ECHO = 252,
        COAP_OPTION_NO_RESPONSE = 258,
        COAP_OPTION_REQUEST_TAG = 292,
        COAP_OPTION_SIGNAL_701_MMS = 2,
        COAP_OPTION_SIGNAL_701_BWT = 4,
        COAP_OPTION_SIGNAL_704_ALT_ADDR = 2,
        COAP_OPTION_SIGNAL_704_HOLD_OFF = 4,
        COAP_OPTION_SIGNAL_705_BAD_CSM = 2
};

enum coap_method {
        COAP_METHOD_GET = 1,
        COAP_METHOD_POST = 2,
        COAP_METHOD_PUT = 3,
        COAP_METHOD_DELETE = 4,
        COAP_METHOD_FETCH = 5,
        COAP_METHOD_PATCH = 6,
        COAP_METHOD_IPATCH = 7,
};


#define COAP_REQUEST_MASK 0x07

#define COAP_VERSION_1 1U

#define COAP_OBSERVE_MAX_AGE 0xFFFFFF


enum coap_msgtype {
        COAP_TYPE_CON = 0,
        COAP_TYPE_NON_CON = 1,
        COAP_TYPE_ACK = 2,
        COAP_TYPE_RESET = 3
};

#define COAP_MAKE_RESPONSE_CODE(class, det) ((class << 5) | (det))

enum coap_response_code {
        COAP_RESPONSE_CODE_CREATED = COAP_MAKE_RESPONSE_CODE(2, 1),
        COAP_RESPONSE_CODE_DELETED = COAP_MAKE_RESPONSE_CODE(2, 2),
        COAP_RESPONSE_CODE_VALID = COAP_MAKE_RESPONSE_CODE(2, 3),
        COAP_RESPONSE_CODE_CHANGED = COAP_MAKE_RESPONSE_CODE(2, 4),
        COAP_RESPONSE_CODE_CONTENT = COAP_MAKE_RESPONSE_CODE(2, 5),
        COAP_RESPONSE_CODE_CONTINUE = COAP_MAKE_RESPONSE_CODE(2, 31),
        COAP_RESPONSE_CODE_BAD_REQUEST = COAP_MAKE_RESPONSE_CODE(4, 0),
        COAP_RESPONSE_CODE_UNAUTHORIZED = COAP_MAKE_RESPONSE_CODE(4, 1),
        COAP_RESPONSE_CODE_BAD_OPTION = COAP_MAKE_RESPONSE_CODE(4, 2),
        COAP_RESPONSE_CODE_FORBIDDEN = COAP_MAKE_RESPONSE_CODE(4, 3),
        COAP_RESPONSE_CODE_NOT_FOUND = COAP_MAKE_RESPONSE_CODE(4, 4),
        COAP_RESPONSE_CODE_NOT_ALLOWED = COAP_MAKE_RESPONSE_CODE(4, 5),
        COAP_RESPONSE_CODE_NOT_ACCEPTABLE = COAP_MAKE_RESPONSE_CODE(4, 6),
        COAP_RESPONSE_CODE_INCOMPLETE = COAP_MAKE_RESPONSE_CODE(4, 8),
        COAP_RESPONSE_CODE_CONFLICT = COAP_MAKE_RESPONSE_CODE(4, 9),
        COAP_RESPONSE_CODE_PRECONDITION_FAILED = COAP_MAKE_RESPONSE_CODE(4, 12),
        COAP_RESPONSE_CODE_REQUEST_TOO_LARGE = COAP_MAKE_RESPONSE_CODE(4, 13),
        COAP_RESPONSE_CODE_UNSUPPORTED_CONTENT_FORMAT =
                                                COAP_MAKE_RESPONSE_CODE(4, 15),
        COAP_RESPONSE_CODE_UNPROCESSABLE_ENTITY = COAP_MAKE_RESPONSE_CODE(4, 22),
        COAP_RESPONSE_CODE_TOO_MANY_REQUESTS = COAP_MAKE_RESPONSE_CODE(4, 29),
        COAP_RESPONSE_CODE_INTERNAL_ERROR = COAP_MAKE_RESPONSE_CODE(5, 0),
        COAP_RESPONSE_CODE_NOT_IMPLEMENTED = COAP_MAKE_RESPONSE_CODE(5, 1),
        COAP_RESPONSE_CODE_BAD_GATEWAY = COAP_MAKE_RESPONSE_CODE(5, 2),
        COAP_RESPONSE_CODE_SERVICE_UNAVAILABLE = COAP_MAKE_RESPONSE_CODE(5, 3),
        COAP_RESPONSE_CODE_GATEWAY_TIMEOUT = COAP_MAKE_RESPONSE_CODE(5, 4),
        COAP_RESPONSE_CODE_PROXYING_NOT_SUPPORTED =
                                                COAP_MAKE_RESPONSE_CODE(5, 5),
        COAP_SIGNAL_CODE_CSM = COAP_MAKE_RESPONSE_CODE(7, 1),
        COAP_SIGNAL_CODE_PING = COAP_MAKE_RESPONSE_CODE(7, 2),
        COAP_SIGNAL_CODE_PONG = COAP_MAKE_RESPONSE_CODE(7, 3),
        COAP_SIGNAL_CODE_RELEASE = COAP_MAKE_RESPONSE_CODE(7, 4),
        COAP_SIGNAL_CODE_ABORT = COAP_MAKE_RESPONSE_CODE(7, 5)
};


#define COAP_CODE_EMPTY (0)

#define COAP_TOKEN_MAX_LEN 8UL
#define COAP_FIXED_HEADER_SIZE 4UL

#define COAP_ETAG_MAX_LEN 8UL

/* CoAP TCP header constants (RFC 8323) */
/* Len/TKL + Code */
#define COAP_TCP_BASIC_HEADER_SIZE        (2)
/* Extended length field values */
#define COAP_TCP_HEADER_LEN_EXT_1B        (13)
#define COAP_TCP_HEADER_LEN_EXT_2B        (14)
#define COAP_TCP_HEADER_LEN_EXT_4B        (15)
/* Extended length offset values */
#define COAP_TCP_HEADER_LEN_EXT_0B_MAX    (13)
#define COAP_TCP_HEADER_LEN_EXT_1B_MAX    (269)
#define COAP_TCP_HEADER_LEN_EXT_2B_MAX    (65805)


enum coap_content_format {
        COAP_CONTENT_FORMAT_TEXT_PLAIN = 0,
        COAP_CONTENT_FORMAT_APP_LINK_FORMAT = 40,
        COAP_CONTENT_FORMAT_APP_XML = 41,
        COAP_CONTENT_FORMAT_APP_OCTET_STREAM = 42,
        COAP_CONTENT_FORMAT_APP_EXI = 47,
        COAP_CONTENT_FORMAT_APP_JSON = 50,
        COAP_CONTENT_FORMAT_APP_JSON_PATCH_JSON = 51,
        COAP_CONTENT_FORMAT_APP_MERGE_PATCH_JSON = 52,
        COAP_CONTENT_FORMAT_APP_CBOR = 60
};

enum coap_no_response {
        COAP_NO_RESPONSE_SUPPRESS_2_XX = 0x02,
        COAP_NO_RESPONSE_SUPPRESS_4_XX = 0x08,
        COAP_NO_RESPONSE_SUPPRESS_5_XX = 0x10,

        COAP_NO_RESPONSE_SUPPRESS_ALL = COAP_NO_RESPONSE_SUPPRESS_2_XX |
                                        COAP_NO_RESPONSE_SUPPRESS_4_XX |
                                        COAP_NO_RESPONSE_SUPPRESS_5_XX,
};


/* block option helper */
#define GET_BLOCK_NUM(v)        ((v) >> 4)
#define GET_BLOCK_SIZE(v)       (((v) & 0x7))
#define GET_MORE(v)             (!!((v) & 0x08))


struct coap_observer;
struct coap_packet;
struct coap_pending;
struct coap_reply;
struct coap_resource;

typedef int (*coap_method_t)(struct coap_resource *resource,
                             struct coap_packet *request,
                             struct net_sockaddr *addr, net_socklen_t addr_len);

typedef void (*coap_notify_t)(struct coap_resource *resource,
                              struct coap_observer *observer);

struct coap_resource {
        coap_method_t get, post, put, del, fetch, patch, ipatch;
        coap_notify_t notify;
        const char * const *path;
        void *user_data;
        struct coap_core_metadata *metadata;
        sys_slist_t observers;
        int age;
};

struct coap_observer {
        sys_snode_t list;
        struct net_sockaddr_storage addr;
        uint8_t token[8];
        uint8_t tkl;
#if defined(CONFIG_COAP_OSCORE) || defined(__DOXYGEN__)
        struct coap_oscore_context *oscore_ctx;
#endif
};

struct coap_packet {
        uint8_t *data;
        uint16_t offset;
        uint16_t max_len;
        uint8_t hdr_len;
        uint16_t opt_len;
        uint16_t delta;
#if defined(CONFIG_COAP_KEEP_USER_DATA) || defined(__DOXYGEN__)
        void *user_data;
#endif
#if defined(CONFIG_COAP_OSCORE) || defined(__DOXYGEN__)
        struct coap_oscore_context *oscore_ctx;
#endif
};

struct coap_option {
        uint16_t delta;
#if defined(CONFIG_COAP_EXTENDED_OPTIONS_LEN)
        uint16_t len;
        uint8_t value[CONFIG_COAP_EXTENDED_OPTIONS_LEN_VALUE];
#else
        uint8_t len;
        uint8_t value[12];
#endif
};

typedef int (*coap_reply_t)(const struct coap_packet *response,
                            struct coap_reply *reply,
                            const struct net_sockaddr *from);

struct coap_transmission_parameters {
        uint32_t ack_timeout;
#if defined(CONFIG_COAP_RANDOMIZE_ACK_TIMEOUT) || defined(__DOXYGEN__)
        uint16_t ack_random_percent;
#endif /* defined(CONFIG_COAP_RANDOMIZE_ACK_TIMEOUT) */
        uint16_t coap_backoff_percent;
        uint8_t max_retransmission;
};

struct coap_pending {
        union {
                struct net_sockaddr addr;
                struct net_sockaddr_storage addr_storage;
        };
        int64_t t0;
        uint32_t timeout;
        uint16_t id;
        uint8_t *data;
        uint16_t len;
        uint8_t retries;
        struct coap_transmission_parameters params;
};

struct coap_reply {
        coap_reply_t reply;
        void *user_data;
        int age;
        uint16_t id;
        uint8_t token[8];
        uint8_t tkl;
};

uint8_t coap_header_get_version(const struct coap_packet *cpkt);

uint8_t coap_header_get_type(const struct coap_packet *cpkt);

uint8_t coap_header_get_token(const struct coap_packet *cpkt, uint8_t *token);

uint8_t coap_header_get_code(const struct coap_packet *cpkt);

int coap_header_set_code(const struct coap_packet *cpkt, uint8_t code);

uint16_t coap_header_get_id(const struct coap_packet *cpkt);

const uint8_t *coap_packet_get_payload(const struct coap_packet *cpkt,
                                       uint16_t *len);

bool coap_uri_path_match(const char * const *path,
                         struct coap_option *options,
                         uint8_t opt_num);

int coap_packet_parse(struct coap_packet *cpkt, uint8_t *data, uint16_t len,
                      struct coap_option *options, uint8_t opt_num);

int coap_packet_set_path(struct coap_packet *cpkt, const char *path);

int coap_packet_init(struct coap_packet *cpkt, uint8_t *data, uint16_t max_len,
                     uint8_t ver, uint8_t type, uint8_t token_len,
                     const uint8_t *token, uint8_t code, uint16_t id);

int coap_ack_init(struct coap_packet *cpkt, const struct coap_packet *req,
                  uint8_t *data, uint16_t max_len, uint8_t code);

int coap_rst_init(struct coap_packet *cpkt, const struct coap_packet *req,
                  uint8_t *data, uint16_t max_len);
uint8_t *coap_next_token(void);

uint16_t coap_next_id(void);

int coap_find_options(const struct coap_packet *cpkt, uint16_t code,
                      struct coap_option *options, uint16_t veclen);

int coap_packet_append_option(struct coap_packet *cpkt, uint16_t code,
                              const uint8_t *value, uint16_t len);

int coap_packet_remove_option(struct coap_packet *cpkt, uint16_t code);

unsigned int coap_option_value_to_int(const struct coap_option *option);

int coap_append_option_int(struct coap_packet *cpkt, uint16_t code,
                           unsigned int val);

int coap_packet_append_payload_marker(struct coap_packet *cpkt);

int coap_packet_append_payload(struct coap_packet *cpkt, const uint8_t *payload,
                               uint16_t payload_len);

bool coap_packet_is_request(const struct coap_packet *cpkt);

int coap_handle_request_len(struct coap_packet *cpkt,
                            struct coap_resource *resources,
                            size_t resources_len,
                            struct coap_option *options,
                            uint8_t opt_num,
                            struct net_sockaddr *addr, net_socklen_t addr_len);

int coap_handle_request(struct coap_packet *cpkt,
                        struct coap_resource *resources,
                        struct coap_option *options,
                        uint8_t opt_num,
                        struct net_sockaddr *addr, net_socklen_t addr_len);

enum coap_block_size {
        COAP_BLOCK_16,
        COAP_BLOCK_32,
        COAP_BLOCK_64,
        COAP_BLOCK_128,
        COAP_BLOCK_256,
        COAP_BLOCK_512,
        COAP_BLOCK_1024,
        COAP_BLOCK_BERT,
};

static inline uint16_t coap_block_size_to_bytes(
        enum coap_block_size block_size)
{
        /* BERT (SZX=7) acts like 1024 bytes for size calculations per RFC 8323 */
        if (block_size == COAP_BLOCK_BERT) {
                return 1024;
        }

        return (1 << (block_size + 4));
}

static inline enum coap_block_size coap_bytes_to_block_size(uint16_t bytes)
{
        int sz = u32_count_trailing_zeros(bytes) - 4;

        if (sz < COAP_BLOCK_16) {
                return COAP_BLOCK_16;
        }
        if (sz > COAP_BLOCK_1024) {
#if defined(CONFIG_COAP_OVER_RELIABLE_TRANSPORT)
                return COAP_BLOCK_BERT;
#else
                return COAP_BLOCK_1024;
#endif /* defined(CONFIG_COAP_OVER_RELIABLE_TRANSPORT) */
        }
        return (enum coap_block_size)sz;
}

struct coap_block_context {
        size_t total_size;
        size_t current;
        enum coap_block_size block_size;
};

int coap_block_transfer_init(struct coap_block_context *ctx,
                             enum coap_block_size block_size,
                             size_t total_size);

int coap_append_descriptive_block_option(struct coap_packet *cpkt, struct coap_block_context *ctx);

bool coap_has_descriptive_block_option(struct coap_packet *cpkt);

int coap_remove_descriptive_block_option(struct coap_packet *cpkt);

bool coap_block_has_more(struct coap_packet *cpkt);

int coap_append_block1_option(struct coap_packet *cpkt,
                              struct coap_block_context *ctx);

int coap_append_block2_option(struct coap_packet *cpkt,
                              struct coap_block_context *ctx);

int coap_append_size1_option(struct coap_packet *cpkt,
                             struct coap_block_context *ctx);

int coap_append_size2_option(struct coap_packet *cpkt,
                             struct coap_block_context *ctx);

int coap_get_option_int(const struct coap_packet *cpkt, uint16_t code);

int coap_get_block1_option(const struct coap_packet *cpkt, bool *has_more, uint32_t *block_number);

int coap_get_block2_option(const struct coap_packet *cpkt, bool *has_more,
                           uint32_t *block_number);

int coap_update_from_block(const struct coap_packet *cpkt,
                           struct coap_block_context *ctx);

int coap_next_block_for_option(const struct coap_packet *cpkt,
                               struct coap_block_context *ctx,
                               enum coap_option_num option);

size_t coap_next_block(const struct coap_packet *cpkt,
                       struct coap_block_context *ctx);

bool coap_age_is_newer(uint32_t v1, uint32_t v2);

void coap_observer_init(struct coap_observer *observer,
                        const struct coap_packet *request,
                        const struct net_sockaddr *addr);

#if defined(CONFIG_COAP_OSCORE) || defined(__DOXYGEN__)
void coap_observer_init_oscore(struct coap_observer *observer, const struct coap_packet *request,
                               const struct net_sockaddr *addr,
                               struct coap_oscore_context *oscore_ctx);
#endif /* CONFIG_COAP_OSCORE */

bool coap_register_observer(struct coap_resource *resource,
                            struct coap_observer *observer);

bool coap_remove_observer(struct coap_resource *resource,
                          struct coap_observer *observer);

struct coap_observer *coap_find_observer(
        struct coap_observer *observers, size_t len,
        const struct net_sockaddr *addr,
        const uint8_t *token, uint8_t token_len);

struct coap_observer *coap_find_observer_by_addr(
        struct coap_observer *observers, size_t len,
        const struct net_sockaddr *addr);

struct coap_observer *coap_find_observer_by_token(
        struct coap_observer *observers, size_t len,
        const uint8_t *token, uint8_t token_len);

struct coap_observer *coap_observer_next_unused(
        struct coap_observer *observers, size_t len);

void coap_reply_init(struct coap_reply *reply,
                     const struct coap_packet *request);

int coap_pending_init(struct coap_pending *pending,
                      const struct coap_packet *request,
                      const struct net_sockaddr *addr,
                      const struct coap_transmission_parameters *params);

struct coap_pending *coap_pending_next_unused(
        struct coap_pending *pendings, size_t len);

struct coap_reply *coap_reply_next_unused(
        struct coap_reply *replies, size_t len);

struct coap_pending *coap_pending_received(
        const struct coap_packet *response,
        struct coap_pending *pendings, size_t len);

struct coap_reply *coap_response_received(
        const struct coap_packet *response,
        const struct net_sockaddr *from,
        struct coap_reply *replies, size_t len);

struct coap_pending *coap_pending_next_to_expire(
        struct coap_pending *pendings, size_t len);

bool coap_pending_cycle(struct coap_pending *pending);

void coap_pending_clear(struct coap_pending *pending);

void coap_pendings_clear(struct coap_pending *pendings, size_t len);

size_t coap_pendings_count(struct coap_pending *pendings, size_t len);

void coap_reply_clear(struct coap_reply *reply);

void coap_replies_clear(struct coap_reply *replies, size_t len);

int coap_resource_notify(struct coap_resource *resource);

bool coap_request_is_observe(const struct coap_packet *request);

struct coap_transmission_parameters coap_get_transmission_parameters(void);

void coap_set_transmission_parameters(const struct coap_transmission_parameters *params);

int coap_check_unsupported_critical_options(const struct coap_packet *cpkt, uint16_t *opt);

uint8_t coap_tcp_header_get_token(const struct coap_packet *cpkt,
                                  uint8_t *token);

uint8_t coap_tcp_header_get_code(const struct coap_packet *cpkt);

const uint8_t *coap_tcp_packet_get_payload(const struct coap_packet *cpkt,
                                           uint32_t *len);

int coap_tcp_packet_parse(struct coap_packet *cpkt, uint8_t *data, uint16_t len,
                          struct coap_option *options, uint8_t opt_num);

int coap_tcp_packet_init(struct coap_packet *cpkt, uint8_t *data,
                         uint16_t max_len, uint8_t token_len,
                         const uint8_t *token, uint8_t code);

int coap_tcp_packet_update_len(struct coap_packet *cpkt);

int coap_tcp_append_block2_option(struct coap_packet *cpkt,
                                  struct coap_block_context *ctx);

int coap_tcp_update_from_block(const struct coap_packet *cpkt,
                               struct coap_block_context *ctx);

size_t coap_tcp_next_block(const struct coap_packet *cpkt,
                           struct coap_block_context *ctx);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_COAP_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

版权（Copyright）：© 2021 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 35 行

条件表达式：`defined(CONFIG_COAP_OSCORE)`。

### 注释 3：原第 231 行

CoAP TCP 首部常量（header constants），参见 RFC 8323。

### 注释 4：原第 232 行

长度／令牌长度加代码字段（Len/TKL + Code）。

### 注释 5：原第 234 行

扩展长度字段（extended length field）的取值。

### 注释 6：原第 238 行

扩展长度偏移（extended length offset）的取值。

### 注释 7：原第 280 行

块选项（block option）辅助定义。

### 注释 8：原第 418 行

条件表达式：`defined(CONFIG_COAP_RANDOMIZE_ACK_TIMEOUT)`。

### 注释 9：原第 819 行

根据 RFC 8323，执行大小计算时，块传输扩展（BERT，`SZX=7`）按 1024 字节处理。

### 注释 10：原第 847 行

条件表达式：`defined(CONFIG_COAP_OVER_RELIABLE_TRANSPORT)`。

### 注释 11：原第 1099 行

条件编译配置（Configuration）标记：`CONFIG_COAP_OSCORE`。

### 注释 12：原第 1524 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_COAP_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/sys/math_extras.h](../math_reference/P002_数学辅助头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [coap_option_num](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga7b8b3041e2f4ae26e663ff7431a6e6e3)
- [COAP_OPTION_IF_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4c61e26d11841c76debe2f99de5e9756)
- [COAP_OPTION_URI_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a402bb0a642a07d951c35d69736fd3f33)
- [COAP_OPTION_ETAG](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a0efdc30ce5551daffd093b2a8466978a)
- [COAP_OPTION_IF_NONE_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a07ea6f395818a7019bb9e6a6e34d2d74)
- [COAP_OPTION_OBSERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a06e91bbb4fa2144543d4148d3245ad25)
- [COAP_OPTION_URI_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a344707b9f4cb71310f2ccf5e8050d17a)
- [COAP_OPTION_LOCATION_PATH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae82be3591d43f0d1c7e89ab764d969bd)
- [COAP_OPTION_OSCORE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3aaa6222533e1a6f1284fc5857884ad24d)
- [COAP_OPTION_URI_PATH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a96b5a15937e875b3087307cc5faab1af)
- [COAP_OPTION_CONTENT_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac3166e67b5f5bf3cefee58c8ff58e5b8)
- [COAP_OPTION_MAX_AGE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ab4cda4d3732fd12b9f203a2475c20981)
- [COAP_OPTION_URI_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3adb4d27052247b9a79ad7fcc0cc30c71c)
- [COAP_OPTION_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3afd0725f0ceb5ce22a6c7b390ca7efc9d)
- [COAP_OPTION_LOCATION_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac728800fc8f0d80e37dcf322e75eb27d)
- [COAP_OPTION_BLOCK2](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4aa7cdfa66bd89f21f592eaf3ebe0972)
- [COAP_OPTION_BLOCK1](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a8aaa54af114fd1db631566afa69f162d)
- [COAP_OPTION_SIZE2](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a26c1bcd7af4fccd949e3de35fc2d88e6)
- [COAP_OPTION_PROXY_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae4d2c93b545708926813217cd36a96ac)
- [COAP_OPTION_PROXY_SCHEME](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a30da986503e1e15243b74a16b161901c)
- [COAP_OPTION_SIZE1](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a53169a1c7b07c9e97f79dfc06af3eb51)
- [COAP_OPTION_ECHO](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a620e8b59f67f89de8a38dc76c8fcc594)
- [COAP_OPTION_NO_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a7984f2c4845610491bda964111a1c8e7)
- [COAP_OPTION_REQUEST_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a2a47428ec35972d256da05104ea6396f)
- [COAP_OPTION_SIGNAL_701_MMS](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a2b6f7575ff75fbc51ac5800a693b19af)
- [COAP_OPTION_SIGNAL_701_BWT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3aeed15ed39751b1533f4a1f825c73d0a2)
- [COAP_OPTION_SIGNAL_704_ALT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a9aa645f3c03f818848d5b728432998e3)
- [COAP_OPTION_SIGNAL_704_HOLD_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3af71df6b0647047115c20790eebb3ce30)
- [COAP_OPTION_SIGNAL_705_BAD_CSM](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a649cb25887a08fc21eb0cac51f58d3e5)
- [coap_method](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6a6547e3c755cf7a5033302c8294e0b7)
- [COAP_METHOD_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7a025300cb0dc4c4de8eb0b0e0b4eb5317)
- [COAP_METHOD_POST](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7aba51bcab79bf75080ccf75c1ec38a3d6)
- [COAP_METHOD_PUT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7a91637ef7c9f57cdcc65d0118008251db)
- [COAP_METHOD_DELETE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7adccbea1fe9a43433cf8471e32208a5ac)
- [COAP_METHOD_FETCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7afa4070fed5c01b28bb1a59e3f0c021f4)
- [COAP_METHOD_PATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7adca55e3d2b4b41b249f6b2f67074d708)
- [COAP_METHOD_IPATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7a78f97b895f29819bf3f8b0314967f20e)
- [coap_msgtype](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3b375b7580246d1266293d09902f3d9f)
- [COAP_TYPE_CON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga3b375b7580246d1266293d09902f3d9fa65c04ee4847d0c595238079ac9564e8d)
- [COAP_TYPE_NON_CON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga3b375b7580246d1266293d09902f3d9fa629a304bea0c85c7b2bf746b26216a4f)
- [COAP_TYPE_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga3b375b7580246d1266293d09902f3d9fa7b2fe2187018bce9132af2763b57307d)
- [COAP_TYPE_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga3b375b7580246d1266293d09902f3d9fa287b951159fd51b84a2e0491b012f84c)
- [coap_response_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1ea81a365834e96f43ab7be573069d26)
- [COAP_RESPONSE_CODE_CREATED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26ad2d9fe8dd5beda74b522377c0b76275b)
- [COAP_MAKE_RESPONSE_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gabdcc1f443e89bd035522cbab7dfee879)
- [COAP_RESPONSE_CODE_DELETED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26abf324915aa498c64a733a0098de4a082)
- [COAP_RESPONSE_CODE_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26aecaac4a0e9c821dfc20536951409dd48)
- [COAP_RESPONSE_CODE_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3)
- [COAP_RESPONSE_CODE_CONTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26adfd3e5e3c6ad5715127bb444c205fbce)
- [COAP_RESPONSE_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26ae4e3ff451c626421b9b329790f019dd8)
- [COAP_RESPONSE_CODE_BAD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5)
- [COAP_RESPONSE_CODE_UNAUTHORIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26acb76dbf11b47477144cc4ece3357283c)
- [COAP_RESPONSE_CODE_BAD_OPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a989a6528edc653c0b693ed875481e82d)
- [COAP_RESPONSE_CODE_FORBIDDEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26afeee555ef54f138db58b14ad2c328d04)
- [COAP_RESPONSE_CODE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a86c2bff8add69428d164431b3091a8e9)
- [COAP_RESPONSE_CODE_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a301eb722445472dba93d5accd6e0dd31)
- [COAP_RESPONSE_CODE_NOT_ACCEPTABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a4d77322514521e8dfea01f4a1a6e5886)
- [COAP_RESPONSE_CODE_INCOMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a671730c6d2f1a339fcd557c5452150af)
- [COAP_RESPONSE_CODE_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26ab447505d233aed9fd8ad28070d317544)
- [COAP_RESPONSE_CODE_PRECONDITION_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a289ade02833b57bffd915e648e050e52)
- [COAP_RESPONSE_CODE_REQUEST_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26aaa43062a8146c1e2e09183228a540d2e)
- [COAP_RESPONSE_CODE_UNSUPPORTED_CONTENT_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26aef6b165b9d3f8f4b477431058815c16b)
- [COAP_RESPONSE_CODE_UNPROCESSABLE_ENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a5e5e31cc4647d5e0fdd1c8fe6cfa2661)
- [COAP_RESPONSE_CODE_TOO_MANY_REQUESTS](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26aabd72cff6669d382aa04c53e764d0b49)
- [COAP_RESPONSE_CODE_INTERNAL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499)
- [COAP_RESPONSE_CODE_NOT_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a85c04541bc8580c2ae915946fd677c15)
- [COAP_RESPONSE_CODE_BAD_GATEWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a8de29a7ee6bb960a97d6b415217b4640)
- [COAP_RESPONSE_CODE_SERVICE_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26afebd274586351951ffe9c8f26b270dec)
- [COAP_RESPONSE_CODE_GATEWAY_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26af6d379fef704c269406b782c60772ecd)
- [COAP_RESPONSE_CODE_PROXYING_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a5f49a566d37b2cda0c624d76aee08bd1)
- [COAP_SIGNAL_CODE_CSM](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26ac528f38c3e8553d83e0455097f4fbdf9)
- [COAP_SIGNAL_CODE_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a7390f381b1aa8a4aa21d98527950a152)
- [COAP_SIGNAL_CODE_PONG](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26abc76b74967e491c10f320bf19c9026d4)
- [COAP_SIGNAL_CODE_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a026916ae7964a98edeadd3f09e9d18ad)
- [COAP_SIGNAL_CODE_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a95a8d4bee68a3829dfb4f3a024c8bf68)
- [coap_content_format](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga94a8f9956742d3928fc3c63b8d01ae73)
- [COAP_CONTENT_FORMAT_TEXT_PLAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73af068aa8d09032352799bc60868607997)
- [COAP_CONTENT_FORMAT_APP_LINK_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a1fbd90fd5cb309e2de6954f46174dc4f)
- [COAP_CONTENT_FORMAT_APP_XML](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73adb96bf55e914f4852e92dc65752c372a)
- [COAP_CONTENT_FORMAT_APP_OCTET_STREAM](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a88d952174bb3e4ffb9ab11a599952760)
- [COAP_CONTENT_FORMAT_APP_EXI](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a483a382550b38468cc66bdce9f4743ea)
- [COAP_CONTENT_FORMAT_APP_JSON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a975381d286c1e9b998e41ef0a234d17a)
- [COAP_CONTENT_FORMAT_APP_JSON_PATCH_JSON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a141f183724ad6da14c3992c0990d6239)
- [COAP_CONTENT_FORMAT_APP_MERGE_PATCH_JSON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a2797149fb3811d706dab291e9edc9436)
- [COAP_CONTENT_FORMAT_APP_CBOR](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a7ca73ff57a6c7fb1517b44f2ce17d3f9)
- [coap_no_response](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2a323287262bbb6a4932e7911ddb652c)
- [COAP_NO_RESPONSE_SUPPRESS_2_XX](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga2a323287262bbb6a4932e7911ddb652caeeb51bb18780c20df5b25183d52d42de)
- [COAP_NO_RESPONSE_SUPPRESS_4_XX](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga2a323287262bbb6a4932e7911ddb652cae8b0b1231d095b3e7a972ca4c86d8dce)
- [COAP_NO_RESPONSE_SUPPRESS_5_XX](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga2a323287262bbb6a4932e7911ddb652ca19ebfb46899b440124322bb67c906cb3)
- [COAP_NO_RESPONSE_SUPPRESS_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga2a323287262bbb6a4932e7911ddb652ca21758021d7f3a36bf6ede06daa82dbf0)
- [coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)
- [coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)
- [coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)
- [coap_reply](../network_application_model_reference/P015_coap_reply_结构体.md)
- [coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)
- [coap_method_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03129c8f853862f8395cc567edbf4642)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [coap_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga4180b2476430fbe4a5e0418fb628ea91)
- [get](../network_application_model_reference/P016_coap_resource_结构体.md#aebe880e3ccbd2441854dfa899dc72c13)
- [post](../network_application_model_reference/P016_coap_resource_结构体.md#a1efed8197d44aba3b63aaa9d9bb0f5bb)
- [put](../network_application_model_reference/P016_coap_resource_结构体.md#a3152a778e27e36fad7dd62985621d58b)
- [del](../network_application_model_reference/P016_coap_resource_结构体.md#a77dfb6d59c25e6e58141226023bf59ea)
- [fetch](../network_application_model_reference/P016_coap_resource_结构体.md#a6975e84ebc67d6aff2efb755695518f5)
- [patch](../network_application_model_reference/P016_coap_resource_结构体.md#aa0a5465fc5b49a566e3803a9f1638724)
- [ipatch](../network_application_model_reference/P016_coap_resource_结构体.md#a7657cb2e9bbac7f98e35b4ed33f13163)
- [notify](../network_application_model_reference/P016_coap_resource_结构体.md#a3199679fd990d757e9a500fbd7c653d7)
- [path](../network_application_model_reference/P016_coap_resource_结构体.md#ada7a41309b6ca11612b17fabf6cd56c5)
- [user_data](../network_application_model_reference/P016_coap_resource_结构体.md#a202a83a5aa024a62bd25cc40f42e8d65)
- [coap_core_metadata](../network_application_model_reference/P008_coap_core_metadata_结构体.md)
- [metadata](../network_application_model_reference/P016_coap_resource_结构体.md#a6c1fe25539ecbe4ec2ed7446fff84861)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [observers](../network_application_model_reference/P016_coap_resource_结构体.md#a5035dc9c88c2b0ae557608e34ec14433)
- [age](../network_application_model_reference/P016_coap_resource_结构体.md#ae8e1b2b1920689913e0910a82a30e009)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [list](../network_application_model_reference/P009_coap_observer_结构体.md#a24a9f853db17ff623f4c510fd0892eb5)
- [addr](../network_application_model_reference/P009_coap_observer_结构体.md#a5d5e9494804ef64bc705f2bb08ac7afd)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [token](../network_application_model_reference/P009_coap_observer_结构体.md#a6d7d792120b935bf61c739f95dd7361c)
- [tkl](../network_application_model_reference/P009_coap_observer_结构体.md#a901f148d2eb697206fde732050c3d8b4)
- [oscore_ctx](../network_application_model_reference/P009_coap_observer_结构体.md#a7486199db30c9aaaba693ce64fd46879)
- [data](../network_application_model_reference/P013_coap_packet_结构体.md#a8116711bcdff1fa6b0cf5c4fa9ab88d1)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [offset](../network_application_model_reference/P013_coap_packet_结构体.md#a46c0842c785b8de5eb8564950a786c02)
- [max_len](../network_application_model_reference/P013_coap_packet_结构体.md#a48c216a7da37e85942d271c85a79bcb6)
- [hdr_len](../network_application_model_reference/P013_coap_packet_结构体.md#ab302c002da88f6d3a44c3a2215082be4)
- [opt_len](../network_application_model_reference/P013_coap_packet_结构体.md#acc5542ba2a69db8957155b90e75fd563)
- [delta](../network_application_model_reference/P013_coap_packet_结构体.md#a95dd8c6fb08ac61a1571c84258579475)
- [user_data](../network_application_model_reference/P013_coap_packet_结构体.md#ab4c2196669f38bf3057e83c44c839ff4)
- [oscore_ctx](../network_application_model_reference/P013_coap_packet_结构体.md#ab496dabc7cc0d9b588d7b1bfdd6967dc)
- [coap_option](../network_application_model_reference/P010_coap_option_结构体.md)
- [delta](../network_application_model_reference/P010_coap_option_结构体.md#abca15b0a8f9bdcb3f493ab3801d4b58f)
- [len](../network_application_model_reference/P010_coap_option_结构体.md#a01c8abdf27c3f8c5a816af33c0c093d4)
- [value](../network_application_model_reference/P010_coap_option_结构体.md#aff07b5d3673169b6316b91dc27780891)
- [coap_reply_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga84eda10c4bf3e62241e686fdfa828868)
- [reply](../network_application_model_reference/P015_coap_reply_结构体.md#a6a888bbb5652761002ce26aba09352cc)
- [coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ack_timeout](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md#aca76954d785d04312fb834dc524f102c)
- [ack_random_percent](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md#a0b43d9e3adfbf7cac09e1ffbbe1f8ce8)
- [coap_backoff_percent](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md#a74c91235bf64fab5e7abc0c9f581e44c)
- [max_retransmission](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md#a3a9b8bf0f2e00fc0981acdd86d404190)
- [addr_storage](../network_application_model_reference/P014_coap_pending_结构体.md#ab06a3561fd9ce0477862babe18e44a1e)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [t0](../network_application_model_reference/P014_coap_pending_结构体.md#a8b95f80a6eaac759ed0895201ff089d9)
- [timeout](../network_application_model_reference/P014_coap_pending_结构体.md#ab31339cc91df71ee6f90d5702f722fd6)
- [id](../network_application_model_reference/P014_coap_pending_结构体.md#a8b1952271bd0c733c2fbcb158b60ca99)
- [data](../network_application_model_reference/P014_coap_pending_结构体.md#a0a506507e472b3813e672f2b455e4bcc)
- [len](../network_application_model_reference/P014_coap_pending_结构体.md#a4eb95f8fadef7d42aecdf25cc5ee3b1d)
- [retries](../network_application_model_reference/P014_coap_pending_结构体.md#a8aebb187845bcb6cb07dee68927f1aa6)
- [params](../network_application_model_reference/P014_coap_pending_结构体.md#a05ca08379d13e10dfe86322f666c3d97)
- [user_data](../network_application_model_reference/P015_coap_reply_结构体.md#aa951d9ba4eb7f8041e8e82df9c1401dc)
- [age](../network_application_model_reference/P015_coap_reply_结构体.md#aea6b98e109e270c08df1554c5eee65fe)
- [id](../network_application_model_reference/P015_coap_reply_结构体.md#a94d17732056de3d8ecb3412c686091f8)
- [token](../network_application_model_reference/P015_coap_reply_结构体.md#a18d40c327933c30681b924446c21ea9d)
- [tkl](../network_application_model_reference/P015_coap_reply_结构体.md#a038ccb29c2abff6168db3247241a8cc3)
- [coap_header_get_version](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafd01c39fac8f173edc04337161e92264)
- [coap_header_get_type](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaed883ea6cec3acc5eb570e152dc52e25)
- [coap_header_get_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6a5049accfa0cd7106a3a6593c598545)
- [coap_header_get_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gae4bf952fdf9e3d03ab0b0df4c3c0d054)
- [coap_header_set_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafdaecca5ad26bab4fb7c9ee3477318f8)
- [coap_header_get_id](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga63388c629da5370d2e711cdc9aabd837)
- [coap_packet_get_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga28ccf00fb1f5f13f747e61c2e3008b5c)
- [coap_uri_path_match](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga8b621232b740d8e8e1771fba24897121)
- [coap_packet_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga27a58a69f632551aa7a2394ae2badacf)
- [coap_packet_set_path](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gab8f9e9cdfa20920d5d25fb1507a2286d)
- [coap_packet_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga90e6aab174f8977f0a3b5fbe1a20297c)
- [coap_ack_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gae6d93b1f93734302be75ee417813e5d1)
- [coap_rst_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga9626781d73d18c1305f654ef4723e5db)
- [coap_next_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga66f986f8a1157236bea27133c2a2538b)
- [coap_next_id](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gade5f4995c6419db03ce3e7ff7ca1cfcb)
- [coap_find_options](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaf006c8048ed7b863e70dbdd64bc3d608)
- [coap_packet_append_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2aa4140ee83ca4090a5604e34d1f1446)
- [coap_packet_remove_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaca300a216781d360d2cd64e8e9f1ae8f)
- [coap_option_value_to_int](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2fd0613e61274ec4b9b7bab3ab11ccce)
- [coap_append_option_int](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6bec94992ac450dca03436a6ad74efb4)
- [coap_packet_append_payload_marker](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga24000def8534acdcd2c61836dc690367)
- [coap_packet_append_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gadcd3a93a702a2a0b428f39b71dd67954)
- [coap_packet_is_request](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga323644931c927b8988aafd89dacb993c)
- [coap_handle_request_len](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gab8ab58c900a4b0396ca7722c754fb1ec)
- [coap_handle_request](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaa170f8dbe1633e2b02c9c2d8dd27f181)
- [coap_block_size](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga712c1468f936a3af7dc39a86a5961922)
- [COAP_BLOCK_16](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a834d479806b513818e2237f3f1c56968)
- [COAP_BLOCK_32](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a1aaf8f841c18e281b176793bb331993d)
- [COAP_BLOCK_64](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a7266f448a391ea2a2763f1ded5397520)
- [COAP_BLOCK_128](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a147ddf4b0e5d1a8c11f0da2c71dee4d8)
- [COAP_BLOCK_256](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922acfc37f84eabccdde4bd84b06c6a5e753)
- [COAP_BLOCK_512](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922ad2052905aff08c58585dcf6c6caddc19)
- [COAP_BLOCK_1024](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a6998c79e63cf65e7f86ddd5713d48dce)
- [COAP_BLOCK_BERT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a549135603208a878cdefd6c5ca1a039b)
- [coap_block_size_to_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafffadd4a837e48fd72af20468ccd86f2)
- [coap_bytes_to_block_size](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga27e3008b8511333e0c0115ba928017f3)
- [u32_count_trailing_zeros](../math_reference/P001_数学辅助公共接口.md#ga4cb313f98c3fd3b00d6f4db74a9a0076)
- [coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)
- [total_size](../network_application_model_reference/P001_coap_block_context_结构体.md#a27db79dc3a2af6dd9f41e3008dcde87a)
- [current](../network_application_model_reference/P001_coap_block_context_结构体.md#a474f54e2a29d41b9d449f8574e747067)
- [block_size](../network_application_model_reference/P001_coap_block_context_结构体.md#a27eb897fa2d455eb79220f1654509da3)
- [coap_block_transfer_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga57486e764f0feb6544fa3b0d19935afd)
- [coap_append_descriptive_block_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga8b5966a29054ace04cae81d4da588e72)
- [coap_has_descriptive_block_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaabdfa8cf28cc2c3a14ae0af5fa7e7212)
- [coap_remove_descriptive_block_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga941ee9d68f1a628755aa79c249cbae58)
- [coap_block_has_more](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafc61a6878d82f81565ab752ced0ce2be)
- [coap_append_block1_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga518d5f4422ff45f2b4a296f249da89cd)
- [coap_append_block2_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga361c17b698bdaa0fc529b7338efefd8c)
- [coap_append_size1_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3f66d5935dcacfeebcac2b3001d7b57a)
- [coap_append_size2_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafbc8c15ef03b762f9411c38b03aa403b)
- [coap_get_option_int](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga21b8f4ffeecc7900f6bf299836d2b5b3)
- [coap_get_block1_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga10c4a0d7e2052f3116fbf3b355fe75db)
- [coap_get_block2_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga196390e6f016b72b3ae2ae9e69bed1b7)
- [coap_update_from_block](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3b0cc9bfabdddeffd98f36d7f15dd416)
- [coap_next_block_for_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga50f7837da003601479dbc470ba9898ae)
- [coap_next_block](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1244716ecf06fad1013131c42eab8c5c)
- [coap_age_is_newer](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga998a3b01a3a535614183ac08da101811)
- [coap_observer_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga262f21fdad778db96c8bd700ba66ce1b)
- [coap_observer_init_oscore](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga34c5eac86081ea46b63c1cbb7c1315e9)
- [coap_register_observer](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3c42861f8442e548f560acf3deca6baa)
- [coap_remove_observer](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga33c351ac06b5ae9217cd53d8cf330fbd)
- [coap_find_observer](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gab045e6e61ef8c35f85591b8792d88952)
- [coap_find_observer_by_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6542f6350f6e4ed861d6c482617dd5d0)
- [coap_find_observer_by_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gadeaa59fd7b6eab454d5930289b4e08f7)
- [coap_observer_next_unused](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2410e973bf3192244426df346230608b)
- [coap_reply_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gacfe30c84434dc8adbf3d399ec0e51bec)
- [coap_pending_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga0b84eee85b854bf087bceb7566e93086)
- [coap_pending_next_unused](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga800831ddfe19b1a5637a5edd9e78c470)
- [coap_reply_next_unused](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga65cb5f7ac01ea5ebe1c6e30a7c70ad4e)
- [coap_pending_received](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga94ceba78cbd2440f91d9b30d6b06594d)
- [coap_response_received](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga44ca9e8b0fe2544b8da73efda10b187b)
- [coap_pending_next_to_expire](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga9d63518c701ebdb4c7f65c5368d00d27)
- [coap_pending_cycle](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2bcfc7340ed2347862b0f003e1b00a4b)
- [coap_pending_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03287eb3187aa28e0e83e0e0c72e2631)
- [coap_pendings_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6e0947048052e733a3571fdc8955b2d7)
- [coap_pendings_count](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gad9db2ced9b882265c16e3039f893ca03)
- [coap_reply_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga37b58c38c150751d31207ece416529d8)
- [coap_replies_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaddb02509934f5bac20b7c7f83aea4cd8)
- [coap_resource_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gad0c738d308f9cca8ea5cdb79449282cb)
- [coap_request_is_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga46b315c30b642eec65bcb84e9c937ee7)
- [coap_get_transmission_parameters](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1bd7be0a5390f0599e7bec0cbd79daf8)
- [coap_set_transmission_parameters](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaf361fd233f1aa650650108ae1e205ede)
- [coap_check_unsupported_critical_options](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga59f6d6ff09861ab3df9cda894f45de40)
- [coap_tcp_header_get_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaa715f58474d6f668f47dc66e478ba6b2)
- [coap_tcp_header_get_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gab2dc876158b3248fa35fbc61a1faf19a)
- [coap_tcp_packet_get_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1adc19283d0b41f6af152d41b32b86d7)
- [coap_tcp_packet_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaf2cd52a5976556c2093bc770bb61c192)
- [coap_tcp_packet_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga5d9fd91c714705b56780264823c56fe6)
- [coap_tcp_packet_update_len](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gae5829b14002cc4d24cf8501ab960c35a)
- [coap_tcp_append_block2_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaf3275841a174b4438c20a1e6e364ea8a)
- [coap_tcp_update_from_block](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga34c1c3b75e0787d8526b7a7a5b5a1633)
- [coap_tcp_next_block](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga99e8ff6696fb7916932ae32c3e3ec8a2)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [math_extras.h](../math_reference/P002_数学辅助头文件参考.md)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [coap_block_context::total_size](../network_application_model_reference/P001_coap_block_context_结构体.md#a27db79dc3a2af6dd9f41e3008dcde87a)
- [coap_block_context::block_size](../network_application_model_reference/P001_coap_block_context_结构体.md#a27eb897fa2d455eb79220f1654509da3)
- [coap_block_context::current](../network_application_model_reference/P001_coap_block_context_结构体.md#a474f54e2a29d41b9d449f8574e747067)
- [coap_observer::list](../network_application_model_reference/P009_coap_observer_结构体.md#a24a9f853db17ff623f4c510fd0892eb5)
- [coap_observer::addr](../network_application_model_reference/P009_coap_observer_结构体.md#a5d5e9494804ef64bc705f2bb08ac7afd)
- [coap_observer::token](../network_application_model_reference/P009_coap_observer_结构体.md#a6d7d792120b935bf61c739f95dd7361c)
- [coap_observer::oscore_ctx](../network_application_model_reference/P009_coap_observer_结构体.md#a7486199db30c9aaaba693ce64fd46879)
- [coap_observer::tkl](../network_application_model_reference/P009_coap_observer_结构体.md#a901f148d2eb697206fde732050c3d8b4)
- [coap_option::len](../network_application_model_reference/P010_coap_option_结构体.md#a01c8abdf27c3f8c5a816af33c0c093d4)
- [coap_option::delta](../network_application_model_reference/P010_coap_option_结构体.md#abca15b0a8f9bdcb3f493ab3801d4b58f)
- [coap_option::value](../network_application_model_reference/P010_coap_option_结构体.md#aff07b5d3673169b6316b91dc27780891)
- [coap_packet::offset](../network_application_model_reference/P013_coap_packet_结构体.md#a46c0842c785b8de5eb8564950a786c02)
- [coap_packet::max_len](../network_application_model_reference/P013_coap_packet_结构体.md#a48c216a7da37e85942d271c85a79bcb6)
- [coap_packet::data](../network_application_model_reference/P013_coap_packet_结构体.md#a8116711bcdff1fa6b0cf5c4fa9ab88d1)
- [coap_packet::delta](../network_application_model_reference/P013_coap_packet_结构体.md#a95dd8c6fb08ac61a1571c84258579475)
- [coap_packet::hdr_len](../network_application_model_reference/P013_coap_packet_结构体.md#ab302c002da88f6d3a44c3a2215082be4)
- [coap_packet::oscore_ctx](../network_application_model_reference/P013_coap_packet_结构体.md#ab496dabc7cc0d9b588d7b1bfdd6967dc)
- [coap_packet::user_data](../network_application_model_reference/P013_coap_packet_结构体.md#ab4c2196669f38bf3057e83c44c839ff4)
- [coap_packet::opt_len](../network_application_model_reference/P013_coap_packet_结构体.md#acc5542ba2a69db8957155b90e75fd563)
- [coap_pending::params](../network_application_model_reference/P014_coap_pending_结构体.md#a05ca08379d13e10dfe86322f666c3d97)
- [coap_pending::data](../network_application_model_reference/P014_coap_pending_结构体.md#a0a506507e472b3813e672f2b455e4bcc)
- [coap_pending::len](../network_application_model_reference/P014_coap_pending_结构体.md#a4eb95f8fadef7d42aecdf25cc5ee3b1d)
- [coap_pending::retries](../network_application_model_reference/P014_coap_pending_结构体.md#a8aebb187845bcb6cb07dee68927f1aa6)
- [coap_pending::id](../network_application_model_reference/P014_coap_pending_结构体.md#a8b1952271bd0c733c2fbcb158b60ca99)
- [coap_pending::t0](../network_application_model_reference/P014_coap_pending_结构体.md#a8b95f80a6eaac759ed0895201ff089d9)
- [coap_pending::addr_storage](../network_application_model_reference/P014_coap_pending_结构体.md#ab06a3561fd9ce0477862babe18e44a1e)
- [coap_pending::timeout](../network_application_model_reference/P014_coap_pending_结构体.md#ab31339cc91df71ee6f90d5702f722fd6)
- [coap_reply::tkl](../network_application_model_reference/P015_coap_reply_结构体.md#a038ccb29c2abff6168db3247241a8cc3)
- [coap_reply::token](../network_application_model_reference/P015_coap_reply_结构体.md#a18d40c327933c30681b924446c21ea9d)
- [coap_reply::reply](../network_application_model_reference/P015_coap_reply_结构体.md#a6a888bbb5652761002ce26aba09352cc)
- [coap_reply::id](../network_application_model_reference/P015_coap_reply_结构体.md#a94d17732056de3d8ecb3412c686091f8)
- [coap_reply::user_data](../network_application_model_reference/P015_coap_reply_结构体.md#aa951d9ba4eb7f8041e8e82df9c1401dc)
- [coap_reply::age](../network_application_model_reference/P015_coap_reply_结构体.md#aea6b98e109e270c08df1554c5eee65fe)
- [coap_resource::post](../network_application_model_reference/P016_coap_resource_结构体.md#a1efed8197d44aba3b63aaa9d9bb0f5bb)
- [coap_resource::user_data](../network_application_model_reference/P016_coap_resource_结构体.md#a202a83a5aa024a62bd25cc40f42e8d65)
- [coap_resource::put](../network_application_model_reference/P016_coap_resource_结构体.md#a3152a778e27e36fad7dd62985621d58b)
- [coap_resource::notify](../network_application_model_reference/P016_coap_resource_结构体.md#a3199679fd990d757e9a500fbd7c653d7)
- [coap_resource::observers](../network_application_model_reference/P016_coap_resource_结构体.md#a5035dc9c88c2b0ae557608e34ec14433)
- [coap_resource::fetch](../network_application_model_reference/P016_coap_resource_结构体.md#a6975e84ebc67d6aff2efb755695518f5)
- [coap_resource::metadata](../network_application_model_reference/P016_coap_resource_结构体.md#a6c1fe25539ecbe4ec2ed7446fff84861)
- [coap_resource::ipatch](../network_application_model_reference/P016_coap_resource_结构体.md#a7657cb2e9bbac7f98e35b4ed33f13163)
- [coap_resource::del](../network_application_model_reference/P016_coap_resource_结构体.md#a77dfb6d59c25e6e58141226023bf59ea)
- [coap_resource::patch](../network_application_model_reference/P016_coap_resource_结构体.md#aa0a5465fc5b49a566e3803a9f1638724)
- [coap_resource::path](../network_application_model_reference/P016_coap_resource_结构体.md#ada7a41309b6ca11612b17fabf6cd56c5)
- [coap_resource::age](../network_application_model_reference/P016_coap_resource_结构体.md#ae8e1b2b1920689913e0910a82a30e009)
- [coap_resource::get](../network_application_model_reference/P016_coap_resource_结构体.md#aebe880e3ccbd2441854dfa899dc72c13)
- [coap_transmission_parameters::ack_random_percent](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md#a0b43d9e3adfbf7cac09e1ffbbe1f8ce8)
- [coap_transmission_parameters::max_retransmission](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md#a3a9b8bf0f2e00fc0981acdd86d404190)
- [coap_transmission_parameters::coap_backoff_percent](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md#a74c91235bf64fab5e7abc0c9f581e44c)
- [coap_transmission_parameters::ack_timeout](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md#aca76954d785d04312fb834dc524f102c)

---

[上一章](P005_bee-dma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_dma_mcux_lpc.h_源码浏览.md)
