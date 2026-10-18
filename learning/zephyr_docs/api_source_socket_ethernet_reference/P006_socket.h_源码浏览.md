---
id: learning.zephyr-docs.api-source-socket-ethernet-reference.page-6
title: socket.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_socket.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)。

## 6.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00069"></a>
<a id="l00072"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00109"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00119"></a>
<a id="l00124"></a>
<a id="l00130"></a>
<a id="l00135"></a>
<a id="l00146"></a>
<a id="l00155"></a>
<a id="l00161"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00178"></a>
<a id="l00189"></a>
<a id="l00200"></a>
<a id="l00204"></a>
<a id="l00216"></a>
<a id="l00226"></a>
<a id="l00231"></a>
<a id="l00238"></a>
<a id="l00246"></a>
<a id="l00256"></a>
<a id="l00269"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
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
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
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
<a id="foldopen00321"></a>
<a id="l00321"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="foldopen00341"></a>
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
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00394"></a>
<a id="l00395"></a>
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
<a id="l00425"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="foldopen00553"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="foldopen00608"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00624"></a>
<a id="l00625"></a>
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
<a id="l00646"></a>
<a id="l00663"></a>
<a id="l00664"></a>
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
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00682"></a>
<a id="foldopen00694"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="foldopen00779"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00781"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00805"></a>
<a id="l00811"></a>
<a id="l00813"></a>
<a id="l00815"></a>
<a id="l00817"></a>
<a id="l00819"></a>
<a id="l00821"></a>
<a id="l00823"></a>
<a id="l00825"></a>
<a id="l00827"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00852"></a>
<a id="l00853"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00871"></a>
<a id="l00873"></a>
<a id="l00875"></a>
<a id="l00877"></a>
<a id="l00879"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="l00882"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="l00888"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00955"></a>
<a id="l00961"></a>
<a id="l00962"></a>
<a id="l00963"></a>
<a id="l00964"></a>
<a id="l00966"></a>
<a id="l00968"></a>
<a id="l00970"></a>
<a id="l00972"></a>
<a id="l00974"></a>
<a id="l00976"></a>
<a id="l00977"></a>
<a id="l00979"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00984"></a>
<a id="l00986"></a>
<a id="l00988"></a>
<a id="l00990"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00995"></a>
<a id="l00997"></a>
<a id="l00998"></a>
<a id="l01003"></a>
<a id="l01005"></a>
<a id="l01006"></a>
<a id="l01008"></a>
<a id="l01009"></a>
<a id="l01011"></a>
<a id="l01012"></a>
<a id="l01014"></a>
<a id="l01015"></a>
<a id="l01017"></a>
<a id="l01018"></a>
<a id="l01020"></a>
<a id="l01021"></a>
<a id="l01023"></a>
<a id="l01024"></a>
<a id="l01026"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="l01031"></a>
<a id="l01033"></a>
<a id="l01038"></a>
<a id="l01039"></a>
<a id="l01041"></a>
<a id="l01043"></a>
<a id="l01048"></a>
<a id="l01050"></a>
<a id="l01052"></a>
<a id="l01054"></a>
<a id="l01056"></a>
<a id="l01057"></a>
<a id="l01059"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="l01067"></a>
<a id="l01069"></a>
<a id="l01071"></a>
<a id="l01073"></a>
<a id="l01075"></a>
<a id="l01077"></a>
<a id="l01079"></a>
<a id="l01081"></a>
<a id="l01083"></a>
<a id="l01085"></a>
<a id="l01087"></a>
<a id="l01089"></a>
<a id="l01091"></a>
<a id="l01093"></a>
<a id="l01095"></a>
<a id="l01097"></a>
<a id="l01098"></a>
<a id="l01100"></a>
<a id="l01101"></a>
<a id="l01102"></a>
<a id="l01103"></a>
<a id="l01104"></a>
<a id="l01105"></a>
<a id="l01106"></a>
<a id="l01108"></a>
<a id="l01114"></a>
<a id="l01119"></a>
<a id="l01120"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01125"></a>
<a id="l01126"></a>
<a id="l01131"></a>
<a id="l01132"></a>
<a id="l01136"></a>
<a id="l01137"></a>
<a id="l01142"></a>
<a id="l01143"></a>
<a id="l01157"></a>
<a id="l01158"></a>
<a id="l01160"></a>
<a id="l01162"></a>
<a id="l01164"></a>
<a id="l01166"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01175"></a>
<a id="l01185"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01190"></a>
<a id="l01191"></a>
<a id="l01193"></a>
<a id="l01194"></a>
<a id="l01196"></a>
<a id="l01197"></a>
<a id="l01199"></a>
<a id="l01200"></a>
<a id="l01202"></a>
<a id="l01203"></a>
<a id="l01205"></a>
<a id="l01206"></a>
<a id="l01208"></a>
<a id="l01209"></a>
<a id="l01215"></a>
<a id="l01216"></a>
<a id="l01229"></a>
<a id="l01230"></a>
<a id="l01232"></a>
<a id="l01233"></a>
<a id="l01238"></a>
<a id="l01239"></a>
<a id="l01241"></a>
<a id="l01242"></a>
<a id="l01246"></a>
<a id="l01247"></a>
<a id="l01249"></a>
<a id="l01250"></a>
<a id="l01252"></a>
<a id="l01253"></a>
<a id="l01255"></a>
<a id="l01257"></a>
<a id="l01262"></a>
<a id="l01264"></a>
<a id="l01266"></a>
<a id="l01268"></a>
<a id="l01270"></a>
<a id="l01271"></a>
<a id="l01273"></a>
<a id="l01276"></a>
<a id="l01282"></a>
<a id="l01284"></a>
<a id="foldopen01290"></a>
<a id="l01290"></a>
<a id="l01291"></a>
<a id="l01292"></a>
<a id="l01294"></a>
<a id="l01295"></a>
<a id="l01297"></a>
<a id="l01298"></a>
<a id="l01300"></a>
<a id="l01301"></a>
<a id="l01303"></a>
<a id="l01304"></a>
<a id="l01306"></a>
<a id="l01307"></a>
<a id="l01309"></a>
<a id="l01310"></a>
<a id="l01312"></a>
<a id="l01313"></a>
<a id="l01315"></a>
<a id="l01316"></a>
<a id="l01318"></a>
<a id="l01319"></a>
<a id="l01321"></a>
<a id="l01322"></a>
<a id="l01324"></a>
<a id="l01330"></a>
<a id="l01335"></a>
<a id="l01337"></a>
<a id="l01338"></a>
<a id="l01340"></a>
<a id="l01341"></a>
<a id="l01343"></a>
<a id="l01344"></a>
<a id="l01347"></a>
<a id="l01352"></a>
<a id="l01353"></a>
<a id="l01354"></a>
<a id="l01355"></a>
<a id="l01356"></a>
<a id="l01357"></a>
<a id="l01358"></a>
<a id="l01359"></a>
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
<a id="l01379"></a>
<a id="l01380"></a>
<a id="l01381"></a>
<a id="l01382"></a>
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
<a id="l01397"></a>
<a id="l01398"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01402"></a>
<a id="l01403"></a>
<a id="l01404"></a>
<a id="l01405"></a>
<a id="l01406"></a>
<a id="l01407"></a>
<a id="l01408"></a>
<a id="l01409"></a>
<a id="l01410"></a>
<a id="l01411"></a>
<a id="l01412"></a>
<a id="l01413"></a>
<a id="l01414"></a>
<a id="l01415"></a>
<a id="l01416"></a>
<a id="l01417"></a>
<a id="l01418"></a>
<a id="l01420"></a>
<a id="l01421"></a>
<a id="l01422"></a>
<a id="l01423"></a>
<a id="l01424"></a>
<a id="l01425"></a>
<a id="l01426"></a>
<a id="l01430"></a>
<a id="l01431"></a>
<a id="adevice_8h_html"></a>
<a id="adns__resolve_8h_html"></a>
<a id="afdtable_8h_html"></a>
<a id="afdtable_8h_html_a1a758fb84d99d0390b6a8d51ec7cda34"></a>
<a id="agroup__bsd__sockets_html_ga0255a43336642aaeeaa5bff4c29c9389"></a>
<a id="agroup__bsd__sockets_html_ga02b0de9a15c2d1133b87216d6afc203f"></a>
<a id="agroup__bsd__sockets_html_ga1532a65955c402cbb365becb58167f19"></a>
<a id="agroup__bsd__sockets_html_ga1f5e089c9fb39d3a8884502a11e389b3"></a>
<a id="agroup__bsd__sockets_html_ga21a871d1fa6b6beeed88408761877873"></a>
<a id="agroup__bsd__sockets_html_ga2d8c2173986f67dde6dc5721bf690855"></a>
<a id="agroup__bsd__sockets_html_ga4d2d0823ad8785ffdc2ae327e8651d3f"></a>
<a id="agroup__bsd__sockets_html_ga518361903c9fac3766164d38243872e3"></a>
<a id="agroup__bsd__sockets_html_ga5693d19a0bdff45a5cb09227683d8631"></a>
<a id="agroup__bsd__sockets_html_ga5b02979bf93763a9cc5711c7267d5de8"></a>
<a id="agroup__bsd__sockets_html_ga6aa12f0dbed8ded425555debba044a98"></a>
<a id="agroup__bsd__sockets_html_ga6bf17561e03600ed870dff702b513d9c"></a>
<a id="agroup__bsd__sockets_html_ga70909e3233d6523d0ad9566b5edd117c"></a>
<a id="agroup__bsd__sockets_html_ga71ac8d52c87b9182a9f1a03614e3dba7"></a>
<a id="agroup__bsd__sockets_html_ga78b0ca26c0aaf5e64b05da8caa8c253c"></a>
<a id="agroup__bsd__sockets_html_ga7953da2e52bcfad51b877de6d7fd6cc9"></a>
<a id="agroup__bsd__sockets_html_ga89271d76123b0a69e0c40ae4de58bd0a"></a>
<a id="agroup__bsd__sockets_html_ga8a7d82cfb02a45de59ccd05614eb78d6"></a>
<a id="agroup__bsd__sockets_html_ga8a8e90b68fb77179677f237bc22289ec"></a>
<a id="agroup__bsd__sockets_html_ga8b348d886f1bc4f4cdf6e2260844f6e1"></a>
<a id="agroup__bsd__sockets_html_ga9f4ff3d1637393cbe74bd111cc6f432a"></a>
<a id="agroup__bsd__sockets_html_gaa9d9e97c347b3854dc73d7ba33d8ca4b"></a>
<a id="agroup__bsd__sockets_html_gab069dc3ebc140af65801a73fcac4f629"></a>
<a id="agroup__bsd__sockets_html_gac56432bf901efaf8ef782430ac143f03"></a>
<a id="agroup__bsd__sockets_html_gad3274fe71d43caf8c4d92fffb589375e"></a>
<a id="agroup__bsd__sockets_html_gad3dbb44d7b49249c124e41041aca6536"></a>
<a id="agroup__bsd__sockets_html_gad858da9650c1270faf5229e3888d7db1"></a>
<a id="agroup__bsd__sockets_html_gae60d7ca486955dd79a2821d1f646c349"></a>
<a id="agroup__bsd__sockets_html_gae8ea59ea82063aa28a9b72da2f08c9fd"></a>
<a id="agroup__bsd__sockets_html_gaf0130ad342c6873d68bdc51d9cf1167b"></a>
<a id="agroup__bsd__sockets_html_gaf59c97c9bd07f188e3f06b2372ac1856"></a>
<a id="agroup__dns__resolve_html_gaba564a71c4fb4c44fae69015e880b0db"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="agroup__ip__4__6_html_ga8b4cfadf1b284e52d6905ca88657b48a"></a>
<a id="agroup__ip__4__6_html_gaf06819bf427cc58be1229b27b373ca31"></a>
<a id="agroup__ip__4__6_html_gafbc331616a5360c68804e8bc2f653cdd"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="anet__ip_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aposix_2sys_2socket_8h_html_a05b4e957a092db3e68281988ceb32df8"></a>
<a id="aposix_2sys_2socket_8h_html_a1c41b0d557d19b5031e668b1997dc73a"></a>
<a id="aposix_2sys_2socket_8h_html_a2d33f1c2b99a5d0df682f54c3ccb2ffa"></a>
<a id="aposix_2sys_2socket_8h_html_a5580f3aa0827aae89459c24b91f80cae"></a>
<a id="aposix_2sys_2socket_8h_html_a66e3de379c18201b21c889035ec54864"></a>
<a id="aposix_2sys_2socket_8h_html_a7005ffbeeff92be5394ff3244da79028"></a>
<a id="aposix_2sys_2socket_8h_html_a71c8788caef89a362e35ce5855e77077"></a>
<a id="aposix_2sys_2socket_8h_html_a8a2ad4261d3978ba299926f45d56ed74"></a>
<a id="aposix_2sys_2socket_8h_html_a8dadddc96fee56a9f8b0904aca02eab2"></a>
<a id="aposix_2sys_2socket_8h_html_a90f0aa598d0f4ab4ea99ecf289a6a7fb"></a>
<a id="aposix_2sys_2socket_8h_html_abef44fb98f476ef2adba92bbdb362a1b"></a>
<a id="aposix_2sys_2socket_8h_html_ac223969ed767c313123d06547db45ff8"></a>
<a id="aposix_2sys_2socket_8h_html_ae074d22829eb79c596fd60d0f9f9611f"></a>
<a id="asocket__poll_8h_html"></a>
<a id="asocket__select_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdlib_8h_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__msghdr_html"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructzsock__addrinfo_html"></a>
<a id="astructzsock__addrinfo_html_a1bf757d3c4eb2ee6c76136edb6c622da"></a>
<a id="astructzsock__addrinfo_html_a59a931d41fc1f512b030fa9bb9c45d37"></a>
<a id="astructzsock__addrinfo_html_a7fdc7a266b2f96766f8c4e79649bfa65"></a>
<a id="astructzsock__addrinfo_html_a83ef78e3347e69564e2663a769356d87"></a>
<a id="astructzsock__addrinfo_html_a971514adde66f5c1a04efc7f42f244d1"></a>
<a id="astructzsock__addrinfo_html_aa9a96f1d5d49833beea05558879867cf"></a>
<a id="astructzsock__addrinfo_html_aae090dcd0c1e73497560cbcc333a452d"></a>
<a id="astructzsock__addrinfo_html_adcb8a732921a11a35f89241cfe413b78"></a>
<a id="astructzsock__addrinfo_html_ae6c344fdb8ae4b15fe4986ce1fc84453"></a>
<a id="astructzsock__pollfd_html"></a>
<a id="astructzsock__tls__cert__verify__cb_html"></a>
<a id="astructzsock__tls__cert__verify__cb_html_a41240ca56bdbf02f6946b8b19df73463"></a>
<a id="astructzsock__tls__cert__verify__cb_html_acc073b829127224887c8da33bce19943"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c


/*
 * Copyright (c) 2017-2018 Linaro Limited
 * Copyright (c) 2021 Nordic Semiconductor
 * Copyright (c) 2025 Aerlync Labs Inc.
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_SOCKET_H_
#define ZEPHYR_INCLUDE_NET_SOCKET_H_


#include <zephyr/kernel.h>
#include <sys/types.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/socket_select.h>
#include <zephyr/net/socket_poll.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/fdtable.h>
#include <zephyr/net/dns_resolve.h>
#include <stdlib.h>

#ifdef __cplusplus
extern "C" {
#endif

/* ZSOCK_POLL* values are compatible with Linux */
#define ZSOCK_POLLIN 1
#define ZSOCK_POLLPRI 2
#define ZSOCK_POLLOUT 4
#define ZSOCK_POLLERR 8
#define ZSOCK_POLLHUP 0x10
#define ZSOCK_POLLNVAL 0x20

#define ZSOCK_MSG_PEEK 0x02
#define ZSOCK_MSG_CTRUNC 0x08
#define ZSOCK_MSG_TRUNC 0x20
#define ZSOCK_MSG_DONTWAIT 0x40
#define ZSOCK_MSG_WAITALL 0x100

/* Well-known values, e.g. from Linux man 2 shutdown:
 * "The constants SHUT_RD, SHUT_WR, SHUT_RDWR have the value 0, 1, 2,
 * respectively". Some software uses numeric values.
 */
#define ZSOCK_SHUT_RD 0
#define ZSOCK_SHUT_WR 1
#define ZSOCK_SHUT_RDWR 2


#define ZSOCK_SOL_TLS 282

#define ZSOCK_TLS_SEC_TAG_LIST 1
#define ZSOCK_TLS_HOSTNAME 2
#define ZSOCK_TLS_CIPHERSUITE_LIST 3
#define ZSOCK_TLS_CIPHERSUITE_USED 4
#define ZSOCK_TLS_PEER_VERIFY 5
#define ZSOCK_TLS_DTLS_ROLE 6
#define ZSOCK_TLS_ALPN_LIST 7
#define ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MIN 8

#define ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MAX 9

#define ZSOCK_TLS_CERT_NOCOPY          10
#define ZSOCK_TLS_NATIVE 11
#define ZSOCK_TLS_SESSION_CACHE 12
#define ZSOCK_TLS_SESSION_CACHE_PURGE 13
#define ZSOCK_TLS_DTLS_CID 14
#define ZSOCK_TLS_DTLS_CID_STATUS 15
#define ZSOCK_TLS_DTLS_CID_VALUE 16
#define ZSOCK_TLS_DTLS_PEER_CID_VALUE 17
#define ZSOCK_TLS_DTLS_HANDSHAKE_ON_CONNECT 18
#define ZSOCK_TLS_CERT_VERIFY_RESULT 19
#define ZSOCK_TLS_CERT_VERIFY_CALLBACK 20
#define ZSOCK_TLS_MAX_FRAGMENT_LENGTH 21

/* Valid values for @ref ZSOCK_TLS_MAX_FRAGMENT_LENGTH option */
#define ZSOCK_TLS_MFL_DEFAULT -1
#define ZSOCK_TLS_MFL_DISABLED 0
#define ZSOCK_TLS_MFL_512 1
#define ZSOCK_TLS_MFL_1024 2
#define ZSOCK_TLS_MFL_2048 3
#define ZSOCK_TLS_MFL_4096 4

/* Valid values for @ref TLS_PEER_VERIFY option */
#define ZSOCK_TLS_PEER_VERIFY_NONE 0
#define ZSOCK_TLS_PEER_VERIFY_OPTIONAL 1
#define ZSOCK_TLS_PEER_VERIFY_REQUIRED 2

/* Valid values for @ref TLS_DTLS_ROLE option */
#define ZSOCK_TLS_DTLS_ROLE_CLIENT 0
#define ZSOCK_TLS_DTLS_ROLE_SERVER 1

/* Valid values for @ref TLS_CERT_NOCOPY option */
#define ZSOCK_TLS_CERT_NOCOPY_NONE 0
#define ZSOCK_TLS_CERT_NOCOPY_OPTIONAL 1

/* Valid values for @ref TLS_SESSION_CACHE option */
#define ZSOCK_TLS_SESSION_CACHE_DISABLED 0
#define ZSOCK_TLS_SESSION_CACHE_ENABLED 1

/* Valid values for @ref TLS_DTLS_CID (Connection ID) option */
#define ZSOCK_TLS_DTLS_CID_DISABLED             0
#define ZSOCK_TLS_DTLS_CID_SUPPORTED            1
#define ZSOCK_TLS_DTLS_CID_ENABLED              2

/* Valid values for @ref TLS_DTLS_CID_STATUS option */
#define ZSOCK_TLS_DTLS_CID_STATUS_DISABLED      0
#define ZSOCK_TLS_DTLS_CID_STATUS_DOWNLINK      1
#define ZSOCK_TLS_DTLS_CID_STATUS_UPLINK        2
#define ZSOCK_TLS_DTLS_CID_STATUS_BIDIRECTIONAL 3

struct zsock_tls_cert_verify_cb {
        void *cb;

        void *ctx;
};
 /* for @name */ /* for @defgroup */

struct zsock_addrinfo {
        struct zsock_addrinfo *ai_next;
        int ai_flags;
        int ai_family;
        int ai_socktype;
        int ai_protocol;
        int ai_eflags;
        net_socklen_t ai_addrlen;
        struct net_sockaddr *ai_addr;
        char *ai_canonname;

        struct net_sockaddr_storage _ai_addr;
        char _ai_canonname[DNS_MAX_NAME_SIZE + 1];
};

__syscall void *zsock_get_context_object(int sock);


/* Offloaded sockets bind their local port in the offload engine, outside the
 * net_context list, so net_context_port_in_use() cannot see them. The socket
 * layer tracks those bindings and answers this query for them.
 */
#if defined(CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING)
bool net_socket_offloaded_port_in_use(enum net_ip_protocol ip_proto, uint16_t local_port,
                                      const struct net_sockaddr *local_addr);
#else
static inline bool net_socket_offloaded_port_in_use(enum net_ip_protocol ip_proto,
                                                    uint16_t local_port,
                                                    const struct net_sockaddr *local_addr)
{
        ARG_UNUSED(ip_proto);
        ARG_UNUSED(local_port);
        ARG_UNUSED(local_addr);

        return false;
}
#endif /* CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING */

/* Port-in-use check across both socket backends: native sockets tracked by
 * net_context and offloaded sockets tracked by the socket layer.
 */
bool net_socket_port_in_use(enum net_ip_protocol ip_proto, uint16_t local_port,
                            const struct net_sockaddr *local_addr);


__syscall int zsock_socket(int family, int type, int proto);

__syscall int zsock_socketpair(int family, int type, int proto, int *sv);

__syscall int zsock_close(int sock);

__syscall int zsock_shutdown(int sock, int how);

__syscall int zsock_bind(int sock, const struct net_sockaddr *addr,
                         net_socklen_t addrlen);

__syscall int zsock_connect(int sock, const struct net_sockaddr *addr,
                            net_socklen_t addrlen);

__syscall int zsock_listen(int sock, int backlog);

__syscall int zsock_accept(int sock, struct net_sockaddr *addr, net_socklen_t *addrlen);

__syscall ssize_t zsock_sendto(int sock, const void *buf, size_t len,
                               int flags, const struct net_sockaddr *dest_addr,
                               net_socklen_t addrlen);

static inline ssize_t zsock_send(int sock, const void *buf, size_t len,
                                 int flags)
{
        return zsock_sendto(sock, buf, len, flags, NULL, 0);
}

__syscall ssize_t zsock_sendmsg(int sock, const struct net_msghdr *msg,
                                int flags);

__syscall ssize_t zsock_recvfrom(int sock, void *buf, size_t max_len,
                                 int flags, struct net_sockaddr *src_addr,
                                 net_socklen_t *addrlen);

__syscall ssize_t zsock_recvmsg(int sock, struct net_msghdr *msg, int flags);

static inline ssize_t zsock_recv(int sock, void *buf, size_t max_len,
                                 int flags)
{
        return zsock_recvfrom(sock, buf, max_len, flags, NULL, NULL);
}

__syscall int zsock_fcntl_impl(int sock, int cmd, int flags);


/*
 * Need this wrapper because newer GCC versions got too smart and "typecheck"
 * even macros.
 */
static inline int zsock_fcntl_wrapper(int sock, int cmd, ...)
{
        va_list args;
        int flags;

        va_start(args, cmd);
        flags = va_arg(args, int);
        va_end(args);
        return zsock_fcntl_impl(sock, cmd, flags);
}

#define zsock_fcntl zsock_fcntl_wrapper


__syscall int zsock_ioctl_impl(int sock, unsigned long request, va_list ap);


static inline int zsock_ioctl_wrapper(int sock, unsigned long request, ...)
{
        int ret;
        va_list args;

        va_start(args, request);
        ret = zsock_ioctl_impl(sock, request, args);
        va_end(args);

        return ret;
}

#define zsock_ioctl zsock_ioctl_wrapper


static inline int zsock_poll(struct zsock_pollfd *fds, int nfds, int timeout)
{
        return zvfs_poll(fds, nfds, timeout);
}

__syscall int zsock_getsockopt(int sock, int level, int optname,
                               void *optval, net_socklen_t *optlen);

__syscall int zsock_setsockopt(int sock, int level, int optname,
                               const void *optval, net_socklen_t optlen);

__syscall int zsock_getpeername(int sock, struct net_sockaddr *addr,
                                net_socklen_t *addrlen);

__syscall int zsock_getsockname(int sock, struct net_sockaddr *addr,
                                net_socklen_t *addrlen);

__syscall int zsock_gethostname(char *buf, size_t len);

static inline char *zsock_inet_ntop(net_sa_family_t family, const void *src,
                                    char *dst, size_t size)
{
        return net_addr_ntop(family, src, dst, size);
}

__syscall int zsock_inet_pton(net_sa_family_t family, const char *src, void *dst);

__syscall int z_zsock_getaddrinfo_internal(const char *host,
                                           const char *service,
                                           const struct zsock_addrinfo *hints,
                                           struct zsock_addrinfo *res);

/* Flags for getaddrinfo() hints. */

#define ZSOCK_AI_PASSIVE 0x1
#define ZSOCK_AI_CANONNAME 0x2
#define ZSOCK_AI_NUMERICHOST 0x4
#define ZSOCK_AI_V4MAPPED 0x8
#define ZSOCK_AI_ALL 0x10
#define ZSOCK_AI_ADDRCONFIG 0x20
#define ZSOCK_AI_NUMERICSERV 0x400
#define ZSOCK_AI_EXTFLAGS 0x800

int zsock_getaddrinfo(const char *host, const char *service,
                      const struct zsock_addrinfo *hints,
                      struct zsock_addrinfo **res);

void zsock_freeaddrinfo(struct zsock_addrinfo *ai);

const char *zsock_gai_strerror(int errcode);

#define ZSOCK_NI_NUMERICHOST 1
#define ZSOCK_NI_NUMERICSERV 2
#define ZSOCK_NI_NOFQDN 4
#define ZSOCK_NI_NAMEREQD 8
#define ZSOCK_NI_DGRAM 16

/* POSIX extensions */

#ifndef ZSOCK_NI_MAXHOST
#define ZSOCK_NI_MAXHOST 64
#endif

int zsock_getnameinfo(const struct net_sockaddr *addr, net_socklen_t addrlen,
                      char *host, net_socklen_t hostlen,
                      char *serv, net_socklen_t servlen, int flags);

int zsock_send_all(int sock, const void *buf, size_t len, int flags,
                   k_timeout_t timeout, size_t *sent_len);

int zsock_sendmsg_all(int sock, const struct net_msghdr *msg, int flags,
                      k_timeout_t timeout, size_t *sent_len);

#define ZSOCK_SOL_SOCKET 1

/* Socket options for SOL_SOCKET level */

#define ZSOCK_SO_DEBUG 1
#define ZSOCK_SO_REUSEADDR 2
#define ZSOCK_SO_TYPE 3
#define ZSOCK_SO_ERROR 4
#define ZSOCK_SO_DONTROUTE 5
#define ZSOCK_SO_BROADCAST 6

#define ZSOCK_SO_SNDBUF 7
#define ZSOCK_SO_RCVBUF 8

#define ZSOCK_SO_KEEPALIVE 9
#define ZSOCK_SO_OOBINLINE 10
#define ZSOCK_SO_PRIORITY 12
#define ZSOCK_SO_LINGER 13
#define ZSOCK_SO_REUSEPORT 15

#define ZSOCK_SO_RCVLOWAT 18
#define ZSOCK_SO_SNDLOWAT 19

#define ZSOCK_SO_RCVTIMEO 20
#define ZSOCK_SO_SNDTIMEO 21

#define ZSOCK_SO_BINDTODEVICE   25

#define ZSOCK_SO_ACCEPTCONN 30

#define ZSOCK_SO_TIMESTAMPING 37

#define ZSOCK_SO_PROTOCOL 38

#define ZSOCK_SO_DOMAIN 39

#define ZSOCK_SO_SOCKS5 60

#define ZSOCK_SO_TXTIME 61
#define ZSOCK_SCM_TXTIME ZSOCK_SO_TXTIME


#define ZSOCK_SOF_TIMESTAMPING_RX_HARDWARE BIT(0)
#define ZSOCK_SOF_TIMESTAMPING_TX_HARDWARE BIT(1)



/* Socket options for NET_IPPROTO_TCP level */
#define ZSOCK_TCP_NODELAY 1
#define ZSOCK_TCP_KEEPIDLE 2
#define ZSOCK_TCP_KEEPINTVL 3
#define ZSOCK_TCP_KEEPCNT 4


/* Socket options for NET_IPPROTO_UDP level */

#define ZSOCK_UDP_OPT      1
#define ZSOCK_UDP_OPT_OCS  2
#define ZSOCK_UDP_OPT_APC  3
#define ZSOCK_UDP_OPT_FRAG 4
#define ZSOCK_UDP_OPT_MDS  5
#define ZSOCK_UDP_OPT_MRDS 6
#define ZSOCK_UDP_OPT_REQ  7
#define ZSOCK_UDP_OPT_RES  8
#define ZSOCK_UDP_OPT_TIME 9
#define ZSOCK_UDP_OPT_AUTH 10
#define ZSOCK_UDP_OPT_EXP  11
#define ZSOCK_UDP_OPT_UCMP 12
#define ZSOCK_UDP_OPT_UENC 13
#define ZSOCK_UDP_OPT_UEXP 14
#define ZSOCK_UDP_OPT_DPLPMTUD 15
#define ZSOCK_UDP_OPT_DPLPMTUD_APP_RESPOND 16

#define ZSOCK_UDP_OPT_CMSG_APC    1
#define ZSOCK_UDP_OPT_CMSG_MDS    2
#define ZSOCK_UDP_OPT_CMSG_MRDS   3
#define ZSOCK_UDP_OPT_CMSG_REQ    4
#define ZSOCK_UDP_OPT_CMSG_RES    5
#define ZSOCK_UDP_OPT_CMSG_TIME   6




/* Socket options for NET_IPPROTO_IP level */
#define ZSOCK_IP_TOS 1

#define ZSOCK_IP_TTL 2

#define ZSOCK_IP_PKTINFO 8

#define ZSOCK_IP_RECVTTL 12

#define ZSOCK_IP_MTU 14

#define ZSOCK_IP_DONTFRAG 15

#define ZSOCK_IP_MULTICAST_IF 32
#define ZSOCK_IP_MULTICAST_TTL 33
#define ZSOCK_IP_MULTICAST_LOOP 34
#define ZSOCK_IP_ADD_MEMBERSHIP 35
#define ZSOCK_IP_DROP_MEMBERSHIP 36

#define ZSOCK_IP_LOCAL_PORT_RANGE 51
 /* for @name */ /* for @defgroup */

/* Socket options for NET_IPPROTO_IPV6 level */
#define ZSOCK_IPV6_UNICAST_HOPS 16

#define ZSOCK_IPV6_MULTICAST_IF       17

#define ZSOCK_IPV6_MULTICAST_HOPS 18

#define ZSOCK_IPV6_MULTICAST_LOOP 19

#define ZSOCK_IPV6_ADD_MEMBERSHIP 20

#define ZSOCK_IPV6_DROP_MEMBERSHIP 21

#define ZSOCK_IPV6_JOIN_GROUP ZSOCK_IPV6_ADD_MEMBERSHIP

#define ZSOCK_IPV6_LEAVE_GROUP ZSOCK_IPV6_DROP_MEMBERSHIP

#define ZSOCK_IPV6_MTU 24

#define ZSOCK_IPV6_DONTFRAG 62

#define ZSOCK_IPV6_V6ONLY 26

#define ZSOCK_IPV6_RECVPKTINFO 49

#define ZSOCK_IPV6_PKTINFO 50

#define ZSOCK_IPV6_RECVHOPLIMIT 51

#define ZSOCK_IPV6_HOPLIMIT 52

#define ZSOCK_IPV6_ADDR_PREFERENCES   72

#define ZSOCK_IPV6_PREFER_SRC_TMP             0x0001
#define ZSOCK_IPV6_PREFER_SRC_PUBLIC          0x0002
#define ZSOCK_IPV6_PREFER_SRC_PUBTMP_DEFAULT  0x0100
#define ZSOCK_IPV6_PREFER_SRC_COA             0x0004
#define ZSOCK_IPV6_PREFER_SRC_HOME            0x0400
#define ZSOCK_IPV6_PREFER_SRC_CGA             0x0008
#define ZSOCK_IPV6_PREFER_SRC_NONCGA          0x0800

#define ZSOCK_IPV6_TCLASS 67 /* for @name */ /* for @defgroup */

#define ZSOCK_SOMAXCONN 128

#define ZSOCK_IN6_IS_ADDR_UNSPECIFIED(addr) \
        net_ipv6_addr_cmp(net_ipv6_unspecified_address(), addr)

#define ZSOCK_IN6_IS_ADDR_LOOPBACK(addr) net_ipv6_is_addr_loopback(addr)

#define ZSOCK_IN6_IS_ADDR_MULTICAST(addr) net_ipv6_is_addr_mcast(addr)

#define ZSOCK_IN6_IS_ADDR_LINKLOCAL(addr) net_ipv6_is_ll_addr(addr)

#define ZSOCK_IN6_IS_ADDR_SITELOCAL(addr) net_ipv6_is_sl_addr(addr)

#define ZSOCK_IN6_IS_ADDR_V4MAPPED(addr) net_ipv6_addr_is_v4_mapped(addr)

#define ZSOCK_IN6_IS_ADDR_MC_GLOBAL(addr) net_ipv6_is_addr_mcast_global(addr)

#define ZSOCK_IN6_IS_ADDR_MC_NODELOCAL(addr) net_ipv6_is_addr_mcast_iface(addr)

#define ZSOCK_IN6_IS_ADDR_MC_LINKLOCAL(addr) net_ipv6_is_addr_mcast_link(addr)

#define ZSOCK_IN6_IS_ADDR_MC_SITELOCAL(addr) net_ipv6_is_addr_mcast_site(addr)

#define ZSOCK_IN6_IS_ADDR_MC_ORGLOCAL(addr) net_ipv6_is_addr_mcast_org(addr)




#define ZSOCK_SOL_PACKET 263

#define ZSOCK_PACKET_ADD_MEMBERSHIP           1

#define ZSOCK_PACKET_DROP_MEMBERSHIP          2
 /* for @name */ /* for @defgroup */

struct net_socket_register {
        int family;
        bool is_offloaded;
        bool (*is_supported)(int family, int type, int proto);
        int (*handler)(int family, int type, int proto);
#if defined(CONFIG_NET_SOCKETS_OBJ_CORE)
        /* Store also the name of the socket type in order to be able to
         * print it later.
         */
        const char * const name;
#endif
};

#define NET_SOCKET_DEFAULT_PRIO CONFIG_NET_SOCKETS_PRIORITY_DEFAULT

#define NET_SOCKET_GET_NAME(socket_name, prio)  \
        __net_socket_register_##prio##_##socket_name

#if defined(CONFIG_NET_SOCKETS_OBJ_CORE)
#define K_OBJ_TYPE_SOCK  K_OBJ_TYPE_ID_GEN("SOCK")

#define NET_SOCKET_REGISTER_NAME(_name)         \
        .name = STRINGIFY(_name),
#else
#define NET_SOCKET_REGISTER_NAME(_name)
#endif

#define _NET_SOCKET_REGISTER(socket_name, prio, _family, _is_supported, _handler, _is_offloaded) \
        static const STRUCT_SECTION_ITERABLE(net_socket_register,       \
                        NET_SOCKET_GET_NAME(socket_name, prio)) = {     \
                .family = _family,                                      \
                .is_offloaded = _is_offloaded,                          \
                .is_supported = _is_supported,                          \
                .handler = _handler,                                    \
                NET_SOCKET_REGISTER_NAME(socket_name)                   \
        }

#define NET_SOCKET_REGISTER(socket_name, prio, _family, _is_supported, _handler) \
        _NET_SOCKET_REGISTER(socket_name, prio, _family, _is_supported, _handler, false)

#define NET_SOCKET_OFFLOAD_REGISTER(socket_name, prio, _family, _is_supported, _handler) \
        _NET_SOCKET_REGISTER(socket_name, prio, _family, _is_supported, _handler, true)

struct socket_op_vtable {
        struct fd_op_vtable fd_vtable;
        int (*shutdown)(void *obj, int how);
        int (*bind)(void *obj, const struct net_sockaddr *addr, net_socklen_t addrlen);
        int (*connect)(void *obj, const struct net_sockaddr *addr,
                       net_socklen_t addrlen);
        int (*listen)(void *obj, int backlog);
        int (*accept)(void *obj, struct net_sockaddr *addr, net_socklen_t *addrlen);
        ssize_t (*sendto)(void *obj, const void *buf, size_t len, int flags,
                          const struct net_sockaddr *dest_addr, net_socklen_t addrlen);
        ssize_t (*recvfrom)(void *obj, void *buf, size_t max_len, int flags,
                            struct net_sockaddr *src_addr, net_socklen_t *addrlen);
        int (*getsockopt)(void *obj, int level, int optname,
                          void *optval, net_socklen_t *optlen);
        int (*setsockopt)(void *obj, int level, int optname,
                          const void *optval, net_socklen_t optlen);
        ssize_t (*sendmsg)(void *obj, const struct net_msghdr *msg, int flags);
        ssize_t (*recvmsg)(void *obj, struct net_msghdr *msg, int flags);
        int (*getpeername)(void *obj, struct net_sockaddr *addr,
                           net_socklen_t *addrlen);
        int (*getsockname)(void *obj, struct net_sockaddr *addr,
                           net_socklen_t *addrlen);
};


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/socket.h>


#endif /* ZEPHYR_INCLUDE_NET_SOCKET_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 8 行

版权（Copyright）：© 2017-2018 Linaro Limited。

版权（Copyright）：© 2021 Nordic Semiconductor。

版权（Copyright）：© 2025 Aerlync Labs Inc.。

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 49 行

`ZSOCK_POLL*` 的取值与 Linux 兼容。

### 注释 3：原第 87 行

采用通行取值，例如 Linux 的 `man 2 shutdown` 所述：常量 `SHUT_RD`、`SHUT_WR` 和 `SHUT_RDWR` 的值分别为 0、1、2。有些软件会直接使用这些数值。

### 注释 4：原第 284 行

`@ref ZSOCK_TLS_MAX_FRAGMENT_LENGTH` 选项的有效值（Valid Values）。

### 注释 5：原第 292 行

`@ref TLS_PEER_VERIFY` 选项的有效值（Valid Values）。

### 注释 6：原第 297 行

`@ref TLS_DTLS_ROLE` 选项的有效值（Valid Values）。

### 注释 7：原第 301 行

`@ref TLS_CERT_NOCOPY` 选项的有效值（Valid Values）。

### 注释 8：原第 305 行

`@ref TLS_SESSION_CACHE` 选项的有效值（Valid Values）。

### 注释 9：原第 309 行

`@ref TLS_DTLS_CID` 连接标识（Connection ID）选项的有效值。

### 注释 10：原第 314 行

`@ref TLS_DTLS_CID_STATUS` 选项的有效值（Valid Values）。

### 注释 11：原第 332 行

供 Doxygen 的 `@name` 使用。

### 注释 12：原第 332 行

用于 `@defgroup` 分组定义。

### 注释 13：原第 398 行

卸载套接字（Offloaded Sockets）在卸载引擎内绑定本地端口，不在 `net_context` 列表中，因此 `net_context_port_in_use()` 无法发现这些绑定。套接字层跟踪这些绑定，并代为回答此查询。

### 注释 14：原第 416 行

条件编译配置（Configuration）标记：`CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING`。

### 注释 15：原第 418 行

跨两个套接字后端（Socket Backends）检查端口是否占用：包括由 `net_context` 跟踪的原生套接字（Native Sockets），以及由套接字层跟踪的卸载套接字（Offloaded Sockets）。

### 注释 16：原第 628 行

需要此包装器（Wrapper），因为较新的 GCC 版本变得过于“聪明”，甚至会对宏进行“类型检查”（Typecheck）。

### 注释 17：原第 804 行

`getaddrinfo()` 提示参数（Hints）的标志。

### 注释 18：原第 881 行

POSIX 扩展（Extensions）。

### 注释 19：原第 963 行

`SOL_SOCKET` 层级的套接字选项（Socket Options）。

### 注释 20：原第 1048 行

`NET_IPPROTO_TCP` 层级的套接字选项（Socket Options）。

### 注释 21：原第 1064 行

`NET_IPPROTO_UDP` 层级的套接字选项（Socket Options）。

### 注释 22：原第 1120 行

`NET_IPPROTO_IP` 层级的套接字选项（Socket Options）。

### 注释 23：原第 1172 行

供 Doxygen 的 `@name` 使用。

### 注释 24：原第 1172 行

用于 `@defgroup` 分组定义。

### 注释 25：原第 1185 行

`NET_IPPROTO_IPV6` 层级的套接字选项（Socket Options）。

### 注释 26：原第 1273 行

供 Doxygen 的 `@name` 使用。

### 注释 27：原第 1273 行

用于 `@defgroup` 分组定义。

### 注释 28：原第 1344 行

供 Doxygen 的 `@name` 使用。

### 注释 29：原第 1344 行

用于 `@defgroup` 分组定义。

### 注释 30：原第 1358 行

同时保存套接字类型（Socket Type）的名称，以便稍后打印。

### 注释 31：原第 1431 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SOCKET_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [sys/types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/socket_select.h](../api_file_system_device_reference/P047_zephyr__net__socket_select.h_文件参考.md)
- [zephyr/net/socket_poll.h](../api_file_reference/P401_zephyr__net__socket_poll.h_文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/sys/fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html)
- [zephyr/net/dns_resolve.h](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h.html)
- [stdlib.h](../api_file_reference/P410_____w__zephyr__zephyr__lib__libc__minimal__include__stdlib.h_文件参考.md)
- [zsock_tls_cert_verify_cb](../posix_system_model_reference/P031_zsock_tls_cert_verify_cb_结构体.md)
- [cb](../posix_system_model_reference/P031_zsock_tls_cert_verify_cb_结构体.md#a41240ca56bdbf02f6946b8b19df73463)
- [ctx](../posix_system_model_reference/P031_zsock_tls_cert_verify_cb_结构体.md#acc073b829127224887c8da33bce19943)
- [zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)
- [ai_next](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#a7fdc7a266b2f96766f8c4e79649bfa65)
- [ai_flags](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#a971514adde66f5c1a04efc7f42f244d1)
- [ai_family](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#a83ef78e3347e69564e2663a769356d87)
- [ai_socktype](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#adcb8a732921a11a35f89241cfe413b78)
- [ai_protocol](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#aae090dcd0c1e73497560cbcc333a452d)
- [ai_eflags](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#ae6c344fdb8ae4b15fe4986ce1fc84453)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [ai_addrlen](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#a1bf757d3c4eb2ee6c76136edb6c622da)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [ai_addr](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#a59a931d41fc1f512b030fa9bb9c45d37)
- [ai_canonname](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#aa9a96f1d5d49833beea05558879867cf)
- [DNS_MAX_NAME_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaba564a71c4fb4c44fae69015e880b0db)
- [zsock_get_context_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga21a871d1fa6b6beeed88408761877873)
- [net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zsock_socket](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5693d19a0bdff45a5cb09227683d8631)
- [zsock_socketpair](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1f5e089c9fb39d3a8884502a11e389b3)
- [zsock_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae60d7ca486955dd79a2821d1f646c349)
- [zsock_shutdown](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gac56432bf901efaf8ef782430ac143f03)
- [zsock_bind](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga70909e3233d6523d0ad9566b5edd117c)
- [zsock_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad858da9650c1270faf5229e3888d7db1)
- [zsock_listen](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae8ea59ea82063aa28a9b72da2f08c9fd)
- [zsock_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1532a65955c402cbb365becb58167f19)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [zsock_sendto](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga9f4ff3d1637393cbe74bd111cc6f432a)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zsock_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2d8c2173986f67dde6dc5721bf690855)
- [zsock_sendmsg](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad3274fe71d43caf8c4d92fffb589375e)
- [net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)
- [zsock_recvfrom](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga89271d76123b0a69e0c40ae4de58bd0a)
- [zsock_recvmsg](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga02b0de9a15c2d1133b87216d6afc203f)
- [zsock_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8a7d82cfb02a45de59ccd05614eb78d6)
- [zsock_fcntl_impl](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gab069dc3ebc140af65801a73fcac4f629)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [zsock_ioctl_impl](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga0255a43336642aaeeaa5bff4c29c9389)
- [zsock_poll](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga518361903c9fac3766164d38243872e3)
- [zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)
- [zvfs_poll](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a1a758fb84d99d0390b6a8d51ec7cda34)
- [zsock_getsockopt](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6aa12f0dbed8ded425555debba044a98)
- [zsock_setsockopt](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga71ac8d52c87b9182a9f1a03614e3dba7)
- [zsock_getpeername](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga78b0ca26c0aaf5e64b05da8caa8c253c)
- [zsock_getsockname](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6bf17561e03600ed870dff702b513d9c)
- [zsock_gethostname](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8b348d886f1bc4f4cdf6e2260844f6e1)
- [zsock_inet_ntop](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad3dbb44d7b49249c124e41041aca6536)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [net_addr_ntop](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gafbc331616a5360c68804e8bc2f653cdd)
- [zsock_inet_pton](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf0130ad342c6873d68bdc51d9cf1167b)
- [zsock_getaddrinfo](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf59c97c9bd07f188e3f06b2372ac1856)
- [zsock_freeaddrinfo](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga7953da2e52bcfad51b877de6d7fd6cc9)
- [zsock_gai_strerror](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaa9d9e97c347b3854dc73d7ba33d8ca4b)
- [zsock_getnameinfo](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5b02979bf93763a9cc5711c7267d5de8)
- [zsock_send_all](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8a8e90b68fb77179677f237bc22289ec)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [zsock_sendmsg_all](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga4d2d0823ad8785ffdc2ae327e8651d3f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [shutdown](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a8dadddc96fee56a9f8b0904aca02eab2)
- [bind](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a05b4e957a092db3e68281988ceb32df8)
- [connect](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)
- [listen](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a7005ffbeeff92be5394ff3244da79028)
- [accept](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a66e3de379c18201b21c889035ec54864)
- [sendto](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#ac223969ed767c313123d06547db45ff8)
- [recvfrom](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a1c41b0d557d19b5031e668b1997dc73a)
- [getsockopt](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa)
- [setsockopt](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a71c8788caef89a362e35ce5855e77077)
- [sendmsg](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a8a2ad4261d3978ba299926f45d56ed74)
- [recvmsg](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#ae074d22829eb79c596fd60d0f9f9611f)
- [getpeername](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a5580f3aa0827aae89459c24b91f80cae)
- [getsockname](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#abef44fb98f476ef2adba92bbdb362a1b)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [dns_resolve.h](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h.html)
- [fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [socket_poll.h](../api_file_reference/P401_zephyr__net__socket_poll.h_文件参考.md)
- [socket_select.h](../api_file_system_device_reference/P047_zephyr__net__socket_select.h_文件参考.md)
- [zsock_addrinfo::ai_addrlen](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#a1bf757d3c4eb2ee6c76136edb6c622da)
- [zsock_addrinfo::ai_addr](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#a59a931d41fc1f512b030fa9bb9c45d37)
- [zsock_addrinfo::ai_next](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#a7fdc7a266b2f96766f8c4e79649bfa65)
- [zsock_addrinfo::ai_family](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#a83ef78e3347e69564e2663a769356d87)
- [zsock_addrinfo::ai_flags](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#a971514adde66f5c1a04efc7f42f244d1)
- [zsock_addrinfo::ai_canonname](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#aa9a96f1d5d49833beea05558879867cf)
- [zsock_addrinfo::ai_protocol](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#aae090dcd0c1e73497560cbcc333a452d)
- [zsock_addrinfo::ai_socktype](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#adcb8a732921a11a35f89241cfe413b78)
- [zsock_addrinfo::ai_eflags](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md#ae6c344fdb8ae4b15fe4986ce1fc84453)
- [zsock_tls_cert_verify_cb::cb](../posix_system_model_reference/P031_zsock_tls_cert_verify_cb_结构体.md#a41240ca56bdbf02f6946b8b19df73463)
- [zsock_tls_cert_verify_cb::ctx](../posix_system_model_reference/P031_zsock_tls_cert_verify_cb_结构体.md#acc073b829127224887c8da33bce19943)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P005_intc_vim.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_tbs.h_源码浏览.md)
