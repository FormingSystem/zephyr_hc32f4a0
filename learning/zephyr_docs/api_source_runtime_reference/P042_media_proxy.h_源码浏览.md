---
id: learning.zephyr-docs.api-source-runtime-reference.page-42
title: media_proxy.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_media\_proxy.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h.html)。

## 42.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="foldopen00061"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00231"></a>
<a id="l00236"></a>
<a id="l00241"></a>
<a id="l00246"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00286"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00304"></a>
<a id="l00306"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00315"></a>
<a id="l00317"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00322"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="l00332"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00346"></a>
<a id="l00351"></a>
<a id="l00353"></a>
<a id="l00359"></a>
<a id="l00361"></a>
<a id="l00363"></a>
<a id="l00365"></a>
<a id="l00367"></a>
<a id="l00369"></a>
<a id="l00371"></a>
<a id="l00373"></a>
<a id="l00375"></a>
<a id="l00377"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00395"></a>
<a id="l00397"></a>
<a id="l00399"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="foldopen00412"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00690"></a>
<a id="l00691"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00816"></a>
<a id="l00817"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00852"></a>
<a id="l00853"></a>
<a id="l00871"></a>
<a id="l00872"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="l00890"></a>
<a id="l00891"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="l00987"></a>
<a id="l00988"></a>
<a id="l01008"></a>
<a id="l01009"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01060"></a>
<a id="l01061"></a>
<a id="l01075"></a>
<a id="l01076"></a>
<a id="l01089"></a>
<a id="l01090"></a>
<a id="l01103"></a>
<a id="l01104"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01154"></a>
<a id="l01155"></a>
<a id="l01163"></a>
<a id="l01164"></a>
<a id="l01175"></a>
<a id="l01176"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01198"></a>
<a id="l01199"></a>
<a id="l01213"></a>
<a id="l01214"></a>
<a id="l01225"></a>
<a id="l01226"></a>
<a id="l01246"></a>
<a id="l01247"></a>
<a id="l01264"></a>
<a id="l01265"></a>
<a id="l01277"></a>
<a id="l01278"></a>
<a id="foldopen01284"></a>
<a id="l01284"></a>
<a id="l01285"></a>
<a id="l01291"></a>
<a id="l01292"></a>
<a id="l01298"></a>
<a id="l01299"></a>
<a id="l01311"></a>
<a id="l01312"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="l01327"></a>
<a id="l01328"></a>
<a id="l01337"></a>
<a id="l01338"></a>
<a id="l01348"></a>
<a id="l01349"></a>
<a id="l01361"></a>
<a id="l01362"></a>
<a id="l01378"></a>
<a id="l01379"></a>
<a id="l01396"></a>
<a id="l01397"></a>
<a id="l01412"></a>
<a id="l01413"></a>
<a id="l01425"></a>
<a id="l01426"></a>
<a id="l01438"></a>
<a id="l01439"></a>
<a id="l01448"></a>
<a id="l01449"></a>
<a id="l01458"></a>
<a id="l01459"></a>
<a id="l01467"></a>
<a id="l01468"></a>
<a id="l01482"></a>
<a id="l01483"></a>
<a id="l01495"></a>
<a id="l01496"></a>
<a id="l01505"></a>
<a id="l01506"></a>
<a id="l01512"></a>
<a id="l01513"></a>
<a id="l01522"></a>
<a id="l01523"></a>
<a id="l01533"></a>
<a id="l01534"></a>
<a id="l01543"></a>
<a id="l01544"></a>
<a id="l01554"></a>
<a id="l01555"></a>
<a id="l01565"></a>
<a id="l01566"></a>
<a id="l01576"></a>
<a id="l01577"></a>
<a id="l01590"></a>
<a id="l01591"></a>
<a id="l01601"></a>
<a id="l01602"></a>
<a id="l01603"></a>
<a id="l01617"></a>
<a id="l01618"></a>
<a id="l01624"></a>
<a id="l01625"></a>
<a id="l01631"></a>
<a id="l01632"></a>
<a id="l01640"></a>
<a id="l01641"></a>
<a id="l01649"></a>
<a id="l01650"></a>
<a id="l01656"></a>
<a id="l01657"></a>
<a id="l01665"></a>
<a id="l01666"></a>
<a id="l01677"></a>
<a id="l01678"></a>
<a id="l01694"></a>
<a id="l01695"></a>
<a id="l01703"></a>
<a id="l01704"></a>
<a id="l01712"></a>
<a id="l01713"></a>
<a id="l01722"></a>
<a id="l01723"></a>
<a id="l01731"></a>
<a id="l01732"></a>
<a id="l01740"></a>
<a id="l01741"></a>
<a id="l01749"></a>
<a id="l01750"></a>
<a id="l01758"></a>
<a id="l01759"></a>
<a id="l01767"></a>
<a id="l01768"></a>
<a id="l01778"></a>
<a id="l01779"></a>
<a id="l01787"></a>
<a id="l01788"></a>
<a id="l01801"></a>
<a id="l01802"></a>
<a id="l01811"></a>
<a id="l01812"></a>
<a id="l01813"></a>
<a id="l01814"></a>
<a id="l01815"></a>
<a id="l01816"></a>
<a id="l01818"></a>
<a id="l01819"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="agroup__bt__mcs_html_ga81665fd87487cbaf1c0f90f1e0b2126a"></a>
<a id="agroup__bt__mcs_html_gaf771b17acd202a20450b6ea939ddee3b"></a>
<a id="agroup__bt__media__proxy_html_ga030899757b79251f1d5a1055f65fe989"></a>
<a id="agroup__bt__media__proxy_html_ga052c3fabac4a44ee2802ddd4a6c5c9ac"></a>
<a id="agroup__bt__media__proxy_html_ga0a70dc60a4d6acbcc58e220b75dad92a"></a>
<a id="agroup__bt__media__proxy_html_ga12dc878be39814660900ba875e13e537"></a>
<a id="agroup__bt__media__proxy_html_ga15804287093b20d4a1616380729b33c8"></a>
<a id="agroup__bt__media__proxy_html_ga17c2ca149050e1382eb556f6dcccad21"></a>
<a id="agroup__bt__media__proxy_html_ga1afcc097cb36c4f11141b82ce28e8126"></a>
<a id="agroup__bt__media__proxy_html_ga2261222d8581ed86e91a276b13359126"></a>
<a id="agroup__bt__media__proxy_html_ga23488e77985a04216ec7c7fa785f09fc"></a>
<a id="agroup__bt__media__proxy_html_ga2ae50a1988305b4247ff0af796b6d93e"></a>
<a id="agroup__bt__media__proxy_html_ga2d64a23b3f881579a603a04baeb64088"></a>
<a id="agroup__bt__media__proxy_html_ga2f93bcde2460c6638880f8e6631eb68e"></a>
<a id="agroup__bt__media__proxy_html_ga352228fb77498b61205a22b0f3a75c8e"></a>
<a id="agroup__bt__media__proxy_html_ga35896de266f2a2bd101279e4ce9900c7"></a>
<a id="agroup__bt__media__proxy_html_ga43b797717fb9b36b94a606dfabeb0fa7"></a>
<a id="agroup__bt__media__proxy_html_ga488441418a8f2d358092019bbfe16788"></a>
<a id="agroup__bt__media__proxy_html_ga4a93a18cb0b75cb16828243f0d37b4b4"></a>
<a id="agroup__bt__media__proxy_html_ga580a0c9fa47460be59f0571ee11a41b4"></a>
<a id="agroup__bt__media__proxy_html_ga590762e7272b99fb8ac50a7841424670"></a>
<a id="agroup__bt__media__proxy_html_ga5aaa486e0c3663e21477984e54642ed1"></a>
<a id="agroup__bt__media__proxy_html_ga5efccb39cdb97eed476e0c0bff461ec1"></a>
<a id="agroup__bt__media__proxy_html_ga61d494d7e149cfa2c3f9546c1e3b99bd"></a>
<a id="agroup__bt__media__proxy_html_ga64730f46b87cf9089aff65b6be12f42d"></a>
<a id="agroup__bt__media__proxy_html_ga694e83401835149833024cf094b98cd1"></a>
<a id="agroup__bt__media__proxy_html_ga70ea8a24a4e853a191e0947e1c2d1145"></a>
<a id="agroup__bt__media__proxy_html_ga776bb5f16cf1f4f6cc3842aabd86b781"></a>
<a id="agroup__bt__media__proxy_html_ga7b0f9633a5322557b91ea97eafac9f34"></a>
<a id="agroup__bt__media__proxy_html_ga817ca4ab611e214493fbc918036def0f"></a>
<a id="agroup__bt__media__proxy_html_ga842d7951a04702d6f819de44c47b9cac"></a>
<a id="agroup__bt__media__proxy_html_ga8c0d75f61120047bacd0b933534e1b41"></a>
<a id="agroup__bt__media__proxy_html_ga9433aaf24776c30557ea694795e75b3e"></a>
<a id="agroup__bt__media__proxy_html_ga9489b517e4baa215f0b7b59243cee11c"></a>
<a id="agroup__bt__media__proxy_html_ga96e8156b0267f3d55ee52ab307d81985"></a>
<a id="agroup__bt__media__proxy_html_gaa4040e97100f6e70527e6ad201309bbe"></a>
<a id="agroup__bt__media__proxy_html_gab0b10b3de5674f2172e1a2f779cbe8d5"></a>
<a id="agroup__bt__media__proxy_html_gab6df6fe71c8273eca855eb3be27290dd"></a>
<a id="agroup__bt__media__proxy_html_gabafbc857c3e6befe98e339acb58f17fb"></a>
<a id="agroup__bt__media__proxy_html_gabfbb49e79204130cb004f217af771b80"></a>
<a id="agroup__bt__media__proxy_html_gac75e27a4a5e169481723cd6b39678274"></a>
<a id="agroup__bt__media__proxy_html_gad02f2924e1aa765c04cbbc6441e7d063"></a>
<a id="agroup__bt__media__proxy_html_gadcad4efdd714159d5d9611bbf74d5fae"></a>
<a id="agroup__bt__media__proxy_html_gadd348a8d5aff193f7a9113a759e85b1d"></a>
<a id="agroup__bt__media__proxy_html_gae077bc84648137460a9aeb6cfd4acb4c"></a>
<a id="agroup__bt__media__proxy_html_gae0bb75feb49a68b495150c6fba2f21a7"></a>
<a id="agroup__bt__media__proxy_html_gae32da32bd504061801730805729242e1"></a>
<a id="agroup__bt__media__proxy_html_gae496885d0124f4e3fc2c0f203fcff118"></a>
<a id="agroup__bt__media__proxy_html_gaea6adacedaded10f7c2c0f91b7159f74"></a>
<a id="agroup__bt__media__proxy_html_gaeaf89f4b760870896ed42687562971ca"></a>
<a id="agroup__bt__media__proxy_html_gaebe7e3683041e28bef40df75cc991dea"></a>
<a id="agroup__bt__media__proxy_html_gaf0bd3447e64b6128710c07461766a0c9"></a>
<a id="agroup__bt__media__proxy_html_gaf535f1ab028407432ef890d278d936e0"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="amcs_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__ots_html"></a>
<a id="astructmedia__proxy__ctrl__cbs_html"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a0678ad4950c6f526c78d2143e9b7c385"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a06fadb043fd0a795f872063b7950d414"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a08b6fe1079b759de1f5a9f7751a22f21"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a08f3f55a5b56d1ede9141013fe456119"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a2ba0e73f7e67c38f5abe555305753d0f"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a3c2b39bc46f8b2a7155c14dd430add8e"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a53c4809b7a10b9057f565411429d691b"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a54f9f50e3b8f99b586a2c522a67da213"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a5692c0d142977b8ec7a4ffb765fd0687"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a5eb1466e8ba100c9d3cb12f097328b9e"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a66f35a59821f53f4ed9aa7dea0e4d654"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a67cf70c9b72a87b03009f1da0a8980f2"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a6aa029523978e02dc1c8c7ff798e2433"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a85182342b606c78127f2690ac1beab7d"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a858a8854259c8e7a09164b916fae309a"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a85c0bfc83bb26c74b11b5cb8182ff1e0"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a89bb28499c989a9a2ad13d40dda6c6db"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a90481b6563033a4520b85307e07e2e3a"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a92a3b0e3254d6b26e0d18476dce3b01e"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_a94b5ec6bc20299b722bd0e2cb28aed5e"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_aa3c2bd1734c6235eb2026915dbebc6c2"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_aa7e7f7724689844491a4885544fc450c"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_aaa7ba216e604be1c447a93231a0857d0"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_ac1afc71ed04faa87e644d095ef14946f"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_ad1a65519a958aa27091a2ba41260db04"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_ad4199644afcf356a565b884129ca0cf3"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_ad84d5caca4be208bd5e5d93f5c801ddf"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_ade71f132ef66c7bfd13b1b1f3200681d"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_aee4a556023d56c3a0d4c2036b3bc0799"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_af067e55ef7f676ad3c05f838160ed21e"></a>
<a id="astructmedia__proxy__ctrl__cbs_html_af2cd0f93aadd451f1b358e2d2d6a0049"></a>
<a id="astructmedia__proxy__pl__calls_html"></a>
<a id="astructmedia__proxy__pl__calls_html_a001ae07161b8a6c7dfc9c2e471f229e5"></a>
<a id="astructmedia__proxy__pl__calls_html_a11ea1cf984a7d11ac7e61405df84ee06"></a>
<a id="astructmedia__proxy__pl__calls_html_a1409764199d47d0c27d07e13c8fa8f68"></a>
<a id="astructmedia__proxy__pl__calls_html_a1b852ccc45a6ee1174b9d58df3b599b6"></a>
<a id="astructmedia__proxy__pl__calls_html_a416ca20a05a66f4ce28635159173f064"></a>
<a id="astructmedia__proxy__pl__calls_html_a422cec33063313a9aab86baf0bd65ef1"></a>
<a id="astructmedia__proxy__pl__calls_html_a5049e21965e7fd08aaeafcbedf76809c"></a>
<a id="astructmedia__proxy__pl__calls_html_a64bc23cc61e69b1b6c4050f76a9bc674"></a>
<a id="astructmedia__proxy__pl__calls_html_a6a339aa7ee564acacffd2637eeb8e7ea"></a>
<a id="astructmedia__proxy__pl__calls_html_a7535dad9be2f4b83c8a7c55fccc8a7af"></a>
<a id="astructmedia__proxy__pl__calls_html_a7f19bd75114835d151ff5b26733ed450"></a>
<a id="astructmedia__proxy__pl__calls_html_a86a71b788b54a4e7c966f162fcab6433"></a>
<a id="astructmedia__proxy__pl__calls_html_a98989105d01265de4b268b623a26df2e"></a>
<a id="astructmedia__proxy__pl__calls_html_a98b02d4689cd5e279f43094f3ca09339"></a>
<a id="astructmedia__proxy__pl__calls_html_a9b733c3187cc032ef6644a16ffd3f7c9"></a>
<a id="astructmedia__proxy__pl__calls_html_abae1ff89136b93ce4dee5dbe12e6791d"></a>
<a id="astructmedia__proxy__pl__calls_html_acb3d3656aaed8c2801b7f4a5d40206f5"></a>
<a id="astructmedia__proxy__pl__calls_html_acbf8dc9dcc8fbaba44d436310c92f3a9"></a>
<a id="astructmedia__proxy__pl__calls_html_ad1215725454c6b76dcdc197a275c03cf"></a>
<a id="astructmedia__proxy__pl__calls_html_ad6fad92957146aeaf1bec0e56606da72"></a>
<a id="astructmedia__proxy__pl__calls_html_adf4003ba8ef1a5c38b75876f864564c5"></a>
<a id="astructmedia__proxy__pl__calls_html_ae0a4457fcc35d32541f2557698d5aa83"></a>
<a id="astructmedia__proxy__pl__calls_html_ae1006d5c684e12e1e1c927f71aa93930"></a>
<a id="astructmedia__proxy__pl__calls_html_aebf24b582cf33786f2dc17765d858a15"></a>
<a id="astructmedia__proxy__pl__calls_html_af939a96fbcfe474dfcdcfb353ae0aac5"></a>
<a id="astructmpl__cmd__ntf_html"></a>
<a id="astructmpl__cmd__ntf_html_a776bd9459d320e609697905067c0b284"></a>
<a id="astructmpl__cmd__ntf_html_adcd5228cef8b7629d54053b155a91aa7"></a>
<a id="astructmpl__cmd_html"></a>
<a id="astructmpl__cmd_html_a5cb29ca9e5a6b8249c69cc975b345e2f"></a>
<a id="astructmpl__cmd_html_aca5e50b9f883a3c81f10ad51032a31f9"></a>
<a id="astructmpl__cmd_html_ade5ed4d0ff2aeb192b8ed6b586c9bc9e"></a>
<a id="astructmpl__sci_html"></a>
<a id="astructmpl__sci_html_a1dfc87f7e8b509ca05cbcd97a245953f"></a>
<a id="astructmpl__sci_html_a348314407c7b46d5ed583b97dfe932bc"></a>
<a id="astructmpl__sci_html_af093a6cd52a74cb2a0989727fc89f3aa"></a>
<a id="astructmpl__search_html"></a>
<a id="astructmpl__search_html_a836bebfaadb56672a7e76c0ac2e450a9"></a>
<a id="astructmpl__search_html_a9b9c64d3d9a25951da58ebf47bb63617"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2019 - 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MEDIA_PROXY_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MEDIA_PROXY_H_


#include <stdint.h>
#include <stdbool.h>

#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/sys/util_macro.h>

/* TODO: Remove dependency on mcs.h */
#include "mcs.h"

#ifdef __cplusplus
extern "C" {
#endif

struct mpl_cmd {
        uint8_t  opcode;
        bool  use_param;
        int32_t param;
};

struct mpl_cmd_ntf {
        uint8_t requested_opcode;
        uint8_t result_code;
};

struct mpl_sci {
        uint8_t len;
        uint8_t type;
        char    param[SEARCH_PARAM_MAX];
};

struct mpl_search {
        uint8_t len;
        char search[SEARCH_LEN_MAX];
};

#define MEDIA_PROXY_PLAYBACK_SPEED_MIN     -128
#define MEDIA_PROXY_PLAYBACK_SPEED_QUARTER -128
#define MEDIA_PROXY_PLAYBACK_SPEED_HALF    -64
#define MEDIA_PROXY_PLAYBACK_SPEED_UNITY   0
#define MEDIA_PROXY_PLAYBACK_SPEED_DOUBLE  64
#define MEDIA_PROXY_PLAYBACK_SPEED_MAX     127

#define MEDIA_PROXY_SEEKING_SPEED_FACTOR_MAX  64
#define MEDIA_PROXY_SEEKING_SPEED_FACTOR_MIN  4
#define MEDIA_PROXY_SEEKING_SPEED_FACTOR_ZERO 0

#define MEDIA_PROXY_PLAYING_ORDER_SINGLE_ONCE    0x01U
#define MEDIA_PROXY_PLAYING_ORDER_SINGLE_REPEAT  0x02U
#define MEDIA_PROXY_PLAYING_ORDER_INORDER_ONCE   0x03U
#define MEDIA_PROXY_PLAYING_ORDER_INORDER_REPEAT 0x04U
#define MEDIA_PROXY_PLAYING_ORDER_OLDEST_ONCE    0x05U
#define MEDIA_PROXY_PLAYING_ORDER_OLDEST_REPEAT  0x06U
#define MEDIA_PROXY_PLAYING_ORDER_NEWEST_ONCE    0x07U
#define MEDIA_PROXY_PLAYING_ORDER_NEWEST_REPEAT  0x08U
#define MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_ONCE   0x09U
#define MEDIA_PROXY_PLAYING_ORDER_SHUFFLE_REPEAT 0x0AU

#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE    BIT(0U)
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT  BIT(1U)
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE   BIT(2U)
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT BIT(3U)
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE    BIT(4U)
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT  BIT(5U)
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE    BIT(6U)
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT  BIT(7U)
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE   BIT(8U)
#define MEDIA_PROXY_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT BIT(9U)

#define MEDIA_PROXY_STATE_INACTIVE 0x00U
#define MEDIA_PROXY_STATE_PLAYING  0x01U
#define MEDIA_PROXY_STATE_PAUSED   0x02U
#define MEDIA_PROXY_STATE_SEEKING  0x03U
#define MEDIA_PROXY_STATE_LAST     0x04U

#define MEDIA_PROXY_OP_PLAY         0x01U
#define MEDIA_PROXY_OP_PAUSE        0x02U
#define MEDIA_PROXY_OP_FAST_REWIND  0x03U
#define MEDIA_PROXY_OP_FAST_FORWARD 0x04U
#define MEDIA_PROXY_OP_STOP         0x05U

#define MEDIA_PROXY_OP_MOVE_RELATIVE 0x10U

#define MEDIA_PROXY_OP_PREV_SEGMENT  0x20U
#define MEDIA_PROXY_OP_NEXT_SEGMENT  0x21U
#define MEDIA_PROXY_OP_FIRST_SEGMENT 0x22U
#define MEDIA_PROXY_OP_LAST_SEGMENT  0x23U
#define MEDIA_PROXY_OP_GOTO_SEGMENT  0x24U

#define MEDIA_PROXY_OP_PREV_TRACK  0x30U
#define MEDIA_PROXY_OP_NEXT_TRACK  0x31U
#define MEDIA_PROXY_OP_FIRST_TRACK 0x32U
#define MEDIA_PROXY_OP_LAST_TRACK  0x33U
#define MEDIA_PROXY_OP_GOTO_TRACK  0x34U

#define MEDIA_PROXY_OP_PREV_GROUP  0x40U
#define MEDIA_PROXY_OP_NEXT_GROUP  0x41U
#define MEDIA_PROXY_OP_FIRST_GROUP 0x42U
#define MEDIA_PROXY_OP_LAST_GROUP  0x43U
#define MEDIA_PROXY_OP_GOTO_GROUP  0x44U

#define MEDIA_PROXY_OPCODES_SUPPORTED_LEN 4U

#define MEDIA_PROXY_OP_SUP_PLAY         BIT(0U)
#define MEDIA_PROXY_OP_SUP_PAUSE        BIT(1U)
#define MEDIA_PROXY_OP_SUP_FAST_REWIND  BIT(2U)
#define MEDIA_PROXY_OP_SUP_FAST_FORWARD BIT(3U)
#define MEDIA_PROXY_OP_SUP_STOP         BIT(4U)

#define MEDIA_PROXY_OP_SUP_MOVE_RELATIVE BIT(5U)

#define MEDIA_PROXY_OP_SUP_PREV_SEGMENT  BIT(6U)
#define MEDIA_PROXY_OP_SUP_NEXT_SEGMENT  BIT(7U)
#define MEDIA_PROXY_OP_SUP_FIRST_SEGMENT BIT(8U)
#define MEDIA_PROXY_OP_SUP_LAST_SEGMENT  BIT(9U)
#define MEDIA_PROXY_OP_SUP_GOTO_SEGMENT  BIT(10U)

#define MEDIA_PROXY_OP_SUP_PREV_TRACK  BIT(11U)
#define MEDIA_PROXY_OP_SUP_NEXT_TRACK  BIT(12U)
#define MEDIA_PROXY_OP_SUP_FIRST_TRACK BIT(13U)
#define MEDIA_PROXY_OP_SUP_LAST_TRACK  BIT(14U)
#define MEDIA_PROXY_OP_SUP_GOTO_TRACK  BIT(15U)

#define MEDIA_PROXY_OP_SUP_PREV_GROUP  BIT(16U)
#define MEDIA_PROXY_OP_SUP_NEXT_GROUP  BIT(17U)
#define MEDIA_PROXY_OP_SUP_FIRST_GROUP BIT(18U)
#define MEDIA_PROXY_OP_SUP_LAST_GROUP  BIT(19U)
#define MEDIA_PROXY_OP_SUP_GOTO_GROUP  BIT(20U)

#define MEDIA_PROXY_CMD_SUCCESS             0x01U
#define MEDIA_PROXY_CMD_NOT_SUPPORTED       0x02U
#define MEDIA_PROXY_CMD_PLAYER_INACTIVE     0x03U
#define MEDIA_PROXY_CMD_CANNOT_BE_COMPLETED 0x04U

#define MEDIA_PROXY_SEARCH_TYPE_TRACK_NAME    0x01U
#define MEDIA_PROXY_SEARCH_TYPE_ARTIST_NAME   0x02U
#define MEDIA_PROXY_SEARCH_TYPE_ALBUM_NAME    0x03U
#define MEDIA_PROXY_SEARCH_TYPE_GROUP_NAME    0x04U
#define MEDIA_PROXY_SEARCH_TYPE_EARLIEST_YEAR 0x05U
#define MEDIA_PROXY_SEARCH_TYPE_LATEST_YEAR   0x06U
#define MEDIA_PROXY_SEARCH_TYPE_GENRE         0x07U
#define MEDIA_PROXY_SEARCH_TYPE_ONLY_TRACKS   0x08U
#define MEDIA_PROXY_SEARCH_TYPE_ONLY_GROUPS   0x09U

#define MEDIA_PROXY_SEARCH_SUCCESS 0x01U
#define MEDIA_PROXY_SEARCH_FAILURE 0x02U

#define MEDIA_PROXY_GROUP_OBJECT_TRACK_TYPE 0x00U
#define MEDIA_PROXY_GROUP_OBJECT_GROUP_TYPE 0x01U

struct media_player;

/* PUBLIC API FOR CONTROLLERS */

struct media_proxy_ctrl_cbs {

        void (*local_player_instance)(struct media_player *player, int err);

#ifdef CONFIG_MCTL_REMOTE_PLAYER_CONTROL
        void (*discover_player)(struct media_player *player, int err);
#endif /* CONFIG_MCTL_REMOTE_PLAYER_CONTROL */

        void (*player_name_recv)(struct media_player *player, int err, const char *name);

        void (*icon_id_recv)(struct media_player *player, int err, uint64_t id);

        void (*icon_url_recv)(struct media_player *player, int err, const char *url);

        void (*track_changed_recv)(struct media_player *player, int err);

        void (*track_title_recv)(struct media_player *player, int err, const char *title);

        void (*track_duration_recv)(struct media_player *player, int err, int32_t duration);

        void (*track_position_recv)(struct media_player *player, int err, int32_t position);

        void (*track_position_write)(struct media_player *player, int err, int32_t position);

        void (*playback_speed_recv)(struct media_player *player, int err, int8_t speed);

        void (*playback_speed_write)(struct media_player *player, int err, int8_t speed);

        void (*seeking_speed_recv)(struct media_player *player, int err, int8_t speed);

        void (*track_segments_id_recv)(struct media_player *player, int err, uint64_t id);

        void (*current_track_id_recv)(struct media_player *player, int err, uint64_t id);

        void (*current_track_id_write)(struct media_player *player, int err, uint64_t id);

        void (*next_track_id_recv)(struct media_player *player, int err, uint64_t id);

        void (*next_track_id_write)(struct media_player *player, int err, uint64_t id);

        void (*parent_group_id_recv)(struct media_player *player, int err, uint64_t id);

        void (*current_group_id_recv)(struct media_player *player, int err, uint64_t id);

        void (*current_group_id_write)(struct media_player *player, int err, uint64_t id);

        void (*playing_order_recv)(struct media_player *player, int err, uint8_t order);

        void (*playing_order_write)(struct media_player *player, int err, uint8_t order);

        void (*playing_orders_supported_recv)(struct media_player *player, int err,
                                              uint16_t orders);

        void (*media_state_recv)(struct media_player *player, int err, uint8_t state);

        void (*command_send)(struct media_player *player, int err, const struct mpl_cmd *cmd);

        void (*command_recv)(struct media_player *player, int err,
                             const struct mpl_cmd_ntf *result);

        void (*commands_supported_recv)(struct media_player *player, int err, uint32_t opcodes);

        void (*search_send)(struct media_player *player, int err, const struct mpl_search *search);

        void (*search_recv)(struct media_player *player, int err, uint8_t result_code);

        void (*search_results_id_recv)(struct media_player *player, int err, uint64_t id);

        void (*content_ctrl_id_recv)(struct media_player *player, int err, uint8_t ccid);
};

int media_proxy_ctrl_register(struct media_proxy_ctrl_cbs *ctrl_cbs);

int media_proxy_ctrl_discover_player(struct bt_conn *conn);

int media_proxy_ctrl_get_player_name(struct media_player *player);

int media_proxy_ctrl_set_player_name(struct media_player *player, const char *name);

int media_proxy_ctrl_get_icon_id(struct media_player *player);

int media_proxy_ctrl_get_icon_url(struct media_player *player);

int media_proxy_ctrl_get_track_title(struct media_player *player);

int media_proxy_ctrl_get_track_duration(struct media_player *player);

int media_proxy_ctrl_get_track_position(struct media_player *player);

int media_proxy_ctrl_set_track_position(struct media_player *player, int32_t position);

int media_proxy_ctrl_get_playback_speed(struct media_player *player);

int media_proxy_ctrl_set_playback_speed(struct media_player *player, int8_t speed);

int media_proxy_ctrl_get_seeking_speed(struct media_player *player);

int media_proxy_ctrl_get_track_segments_id(struct media_player *player);

int media_proxy_ctrl_get_current_track_id(struct media_player *player);

int media_proxy_ctrl_set_current_track_id(struct media_player *player, uint64_t id);

int media_proxy_ctrl_get_next_track_id(struct media_player *player);

int media_proxy_ctrl_set_next_track_id(struct media_player *player, uint64_t id);

int media_proxy_ctrl_get_parent_group_id(struct media_player *player);

int media_proxy_ctrl_get_current_group_id(struct media_player *player);

int media_proxy_ctrl_set_current_group_id(struct media_player *player, uint64_t id);

int media_proxy_ctrl_get_playing_order(struct media_player *player);

int media_proxy_ctrl_set_playing_order(struct media_player *player, uint8_t order);

int media_proxy_ctrl_get_playing_orders_supported(struct media_player *player);

int media_proxy_ctrl_get_media_state(struct media_player *player);

int media_proxy_ctrl_send_command(struct media_player *player, const struct mpl_cmd *command);

int media_proxy_ctrl_get_commands_supported(struct media_player *player);

int media_proxy_ctrl_send_search(struct media_player *player, const struct mpl_search *search);

int media_proxy_ctrl_get_search_results_id(struct media_player *player);

uint8_t media_proxy_ctrl_get_content_ctrl_id(struct media_player *player);

struct media_proxy_pl_calls {

        const char *(*get_player_name)(void);

        void (*set_player_name)(const char *name);

        uint64_t (*get_icon_id)(void);

        const char *(*get_icon_url)(void);

        const char *(*get_track_title)(void);

        int32_t (*get_track_duration)(void);

        int32_t (*get_track_position)(void);

        void (*set_track_position)(int32_t position);

        int8_t (*get_playback_speed)(void);

        void (*set_playback_speed)(int8_t speed);

        int8_t (*get_seeking_speed)(void);

        uint64_t (*get_track_segments_id)(void);

        uint64_t (*get_current_track_id)(void);

        void (*set_current_track_id)(uint64_t id);

        uint64_t (*get_next_track_id)(void);

        void (*set_next_track_id)(uint64_t id);

        uint64_t (*get_parent_group_id)(void);

        uint64_t (*get_current_group_id)(void);

        void (*set_current_group_id)(uint64_t id);

        uint8_t (*get_playing_order)(void);

        void (*set_playing_order)(uint8_t order);

        uint16_t (*get_playing_orders_supported)(void);

        uint8_t (*get_media_state)(void);

        void (*send_command)(const struct mpl_cmd *command);

        uint32_t (*get_commands_supported)(void);

        void (*send_search)(const struct mpl_search *search);

        uint64_t (*get_search_results_id)(void);

        uint8_t (*get_content_ctrl_id)(void);
};

int media_proxy_pl_register(struct media_proxy_pl_calls *pl_calls);

int media_proxy_pl_init(void);

struct bt_ots *bt_mcs_get_ots(void);

void media_proxy_pl_name_cb(const char *name);

void media_proxy_pl_icon_url_cb(const char *url);

void media_proxy_pl_track_changed_cb(void);

void media_proxy_pl_track_title_cb(char *title);

void media_proxy_pl_track_duration_cb(int32_t duration);

void media_proxy_pl_track_position_cb(int32_t position);

void media_proxy_pl_playback_speed_cb(int8_t speed);

void media_proxy_pl_seeking_speed_cb(int8_t speed);

void media_proxy_pl_current_track_id_cb(uint64_t id);

void media_proxy_pl_next_track_id_cb(uint64_t id);

void media_proxy_pl_parent_group_id_cb(uint64_t id);

void media_proxy_pl_current_group_id_cb(uint64_t id);

void media_proxy_pl_playing_order_cb(uint8_t order);

void media_proxy_pl_media_state_cb(uint8_t state);

void media_proxy_pl_command_cb(const struct mpl_cmd_ntf *cmd_ntf);

void media_proxy_pl_commands_supported_cb(uint32_t opcodes);

void media_proxy_pl_search_cb(uint8_t result_code);

void media_proxy_pl_search_results_id_cb(uint64_t id);

#ifdef __cplusplus
}
#endif
 /* End of group bt_media_proxy */

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MEDIA_PROXY_H_ */
```

## 42.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2019 - 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 51 行

待办（TODO）：移除对 `mcs.h` 的依赖。

### 注释 3：原第 405 行

面向控制器的公共 API（PUBLIC API FOR CONTROLLERS）。

### 注释 4：原第 440 行

条件编译配置（Configuration）标记：`CONFIG_MCTL_REMOTE_PLAYER_CONTROL`。

### 注释 5：原第 1816 行

`bt_media_proxy` 分组结束。

### 注释 6：原第 1819 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MEDIA_PROXY_H_`。

## 42.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [mcs.h](https://docs.zephyrproject.org/latest/doxygen/html/mcs_8h.html)
- [mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [opcode](../audio_video_model_reference/P037_mpl_cmd_结构体.md#a5cb29ca9e5a6b8249c69cc975b345e2f)
- [use_param](../audio_video_model_reference/P037_mpl_cmd_结构体.md#aca5e50b9f883a3c81f10ad51032a31f9)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [param](../audio_video_model_reference/P037_mpl_cmd_结构体.md#ade5ed4d0ff2aeb192b8ed6b586c9bc9e)
- [mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)
- [requested_opcode](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md#adcd5228cef8b7629d54053b155a91aa7)
- [result_code](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md#a776bd9459d320e609697905067c0b284)
- [mpl_sci](../audio_video_model_reference/P039_mpl_sci_结构体.md)
- [len](../audio_video_model_reference/P039_mpl_sci_结构体.md#a348314407c7b46d5ed583b97dfe932bc)
- [type](../audio_video_model_reference/P039_mpl_sci_结构体.md#a1dfc87f7e8b509ca05cbcd97a245953f)
- [param](../audio_video_model_reference/P039_mpl_sci_结构体.md#af093a6cd52a74cb2a0989727fc89f3aa)
- [SEARCH_PARAM_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#ga81665fd87487cbaf1c0f90f1e0b2126a)
- [mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)
- [len](../audio_video_model_reference/P040_mpl_search_结构体.md#a9b9c64d3d9a25951da58ebf47bb63617)
- [search](../audio_video_model_reference/P040_mpl_search_结构体.md#a836bebfaadb56672a7e76c0ac2e450a9)
- [SEARCH_LEN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html#gaf771b17acd202a20450b6ea939ddee3b)
- [media_proxy_ctrl_cbs](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md)
- [local_player_instance](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#af2cd0f93aadd451f1b358e2d2d6a0049)
- [player_name_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a94b5ec6bc20299b722bd0e2cb28aed5e)
- [icon_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#aaa7ba216e604be1c447a93231a0857d0)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [icon_url_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a53c4809b7a10b9057f565411429d691b)
- [track_changed_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#ade71f132ef66c7bfd13b1b1f3200681d)
- [track_title_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#ac1afc71ed04faa87e644d095ef14946f)
- [track_duration_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a85c0bfc83bb26c74b11b5cb8182ff1e0)
- [track_position_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a6aa029523978e02dc1c8c7ff798e2433)
- [track_position_write](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a54f9f50e3b8f99b586a2c522a67da213)
- [playback_speed_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a5eb1466e8ba100c9d3cb12f097328b9e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [playback_speed_write](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#ad84d5caca4be208bd5e5d93f5c801ddf)
- [seeking_speed_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a2ba0e73f7e67c38f5abe555305753d0f)
- [track_segments_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#aa7e7f7724689844491a4885544fc450c)
- [current_track_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#aa3c2bd1734c6235eb2026915dbebc6c2)
- [current_track_id_write](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a66f35a59821f53f4ed9aa7dea0e4d654)
- [next_track_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a5692c0d142977b8ec7a4ffb765fd0687)
- [next_track_id_write](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a08b6fe1079b759de1f5a9f7751a22f21)
- [parent_group_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a3c2b39bc46f8b2a7155c14dd430add8e)
- [current_group_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a858a8854259c8e7a09164b916fae309a)
- [current_group_id_write](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#ad1a65519a958aa27091a2ba41260db04)
- [playing_order_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a92a3b0e3254d6b26e0d18476dce3b01e)
- [playing_order_write](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a67cf70c9b72a87b03009f1da0a8980f2)
- [playing_orders_supported_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a85182342b606c78127f2690ac1beab7d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [media_state_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#ad4199644afcf356a565b884129ca0cf3)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [command_send](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a89bb28499c989a9a2ad13d40dda6c6db)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [command_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a90481b6563033a4520b85307e07e2e3a)
- [commands_supported_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a06fadb043fd0a795f872063b7950d414)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [search_send](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#aee4a556023d56c3a0d4c2036b3bc0799)
- [search_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a0678ad4950c6f526c78d2143e9b7c385)
- [search_results_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#af067e55ef7f676ad3c05f838160ed21e)
- [content_ctrl_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a08f3f55a5b56d1ede9141013fe456119)
- [media_proxy_ctrl_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga352228fb77498b61205a22b0f3a75c8e)
- [media_proxy_ctrl_discover_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5aaa486e0c3663e21477984e54642ed1)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [media_proxy_ctrl_get_player_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2261222d8581ed86e91a276b13359126)
- [media_proxy_ctrl_set_player_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae077bc84648137460a9aeb6cfd4acb4c)
- [media_proxy_ctrl_get_icon_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga5efccb39cdb97eed476e0c0bff461ec1)
- [media_proxy_ctrl_get_icon_url](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab6df6fe71c8273eca855eb3be27290dd)
- [media_proxy_ctrl_get_track_title](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gabfbb49e79204130cb004f217af771b80)
- [media_proxy_ctrl_get_track_duration](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga488441418a8f2d358092019bbfe16788)
- [media_proxy_ctrl_get_track_position](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae0bb75feb49a68b495150c6fba2f21a7)
- [media_proxy_ctrl_set_track_position](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga776bb5f16cf1f4f6cc3842aabd86b781)
- [media_proxy_ctrl_get_playback_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2d64a23b3f881579a603a04baeb64088)
- [media_proxy_ctrl_set_playback_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gabafbc857c3e6befe98e339acb58f17fb)
- [media_proxy_ctrl_get_seeking_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga817ca4ab611e214493fbc918036def0f)
- [media_proxy_ctrl_get_track_segments_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga1afcc097cb36c4f11141b82ce28e8126)
- [media_proxy_ctrl_get_current_track_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaebe7e3683041e28bef40df75cc991dea)
- [media_proxy_ctrl_set_current_track_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaea6adacedaded10f7c2c0f91b7159f74)
- [media_proxy_ctrl_get_next_track_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae32da32bd504061801730805729242e1)
- [media_proxy_ctrl_set_next_track_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga43b797717fb9b36b94a606dfabeb0fa7)
- [media_proxy_ctrl_get_parent_group_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga12dc878be39814660900ba875e13e537)
- [media_proxy_ctrl_get_current_group_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2ae50a1988305b4247ff0af796b6d93e)
- [media_proxy_ctrl_set_current_group_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gae496885d0124f4e3fc2c0f203fcff118)
- [media_proxy_ctrl_get_playing_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga2f93bcde2460c6638880f8e6631eb68e)
- [media_proxy_ctrl_set_playing_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaa4040e97100f6e70527e6ad201309bbe)
- [media_proxy_ctrl_get_playing_orders_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga030899757b79251f1d5a1055f65fe989)
- [media_proxy_ctrl_get_media_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga9433aaf24776c30557ea694795e75b3e)
- [media_proxy_ctrl_send_command](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga590762e7272b99fb8ac50a7841424670)
- [media_proxy_ctrl_get_commands_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga15804287093b20d4a1616380729b33c8)
- [media_proxy_ctrl_send_search](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga052c3fabac4a44ee2802ddd4a6c5c9ac)
- [media_proxy_ctrl_get_search_results_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga580a0c9fa47460be59f0571ee11a41b4)
- [media_proxy_ctrl_get_content_ctrl_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga23488e77985a04216ec7c7fa785f09fc)
- [media_proxy_pl_calls](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md)
- [set_player_name](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#acb3d3656aaed8c2801b7f4a5d40206f5)
- [get_icon_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#ad1215725454c6b76dcdc197a275c03cf)
- [get_track_duration](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a1b852ccc45a6ee1174b9d58df3b599b6)
- [get_track_position](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a11ea1cf984a7d11ac7e61405df84ee06)
- [set_track_position](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a001ae07161b8a6c7dfc9c2e471f229e5)
- [get_playback_speed](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#ae1006d5c684e12e1e1c927f71aa93930)
- [set_playback_speed](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a7535dad9be2f4b83c8a7c55fccc8a7af)
- [get_seeking_speed](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#aebf24b582cf33786f2dc17765d858a15)
- [get_track_segments_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a86a71b788b54a4e7c966f162fcab6433)
- [get_current_track_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a7f19bd75114835d151ff5b26733ed450)
- [set_current_track_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a422cec33063313a9aab86baf0bd65ef1)
- [get_next_track_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#af939a96fbcfe474dfcdcfb353ae0aac5)
- [set_next_track_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#acbf8dc9dcc8fbaba44d436310c92f3a9)
- [get_parent_group_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a1409764199d47d0c27d07e13c8fa8f68)
- [get_current_group_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a98b02d4689cd5e279f43094f3ca09339)
- [set_current_group_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a5049e21965e7fd08aaeafcbedf76809c)
- [get_playing_order](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a98989105d01265de4b268b623a26df2e)
- [set_playing_order](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#ad6fad92957146aeaf1bec0e56606da72)
- [get_playing_orders_supported](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a9b733c3187cc032ef6644a16ffd3f7c9)
- [get_media_state](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a6a339aa7ee564acacffd2637eeb8e7ea)
- [send_command](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#abae1ff89136b93ce4dee5dbe12e6791d)
- [get_commands_supported](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#ae0a4457fcc35d32541f2557698d5aa83)
- [send_search](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a416ca20a05a66f4ce28635159173f064)
- [get_search_results_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#adf4003ba8ef1a5c38b75876f864564c5)
- [get_content_ctrl_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a64bc23cc61e69b1b6c4050f76a9bc674)
- [media_proxy_pl_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gac75e27a4a5e169481723cd6b39678274)
- [media_proxy_pl_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gab0b10b3de5674f2172e1a2f779cbe8d5)
- [bt_ots](../bluetooth_service_model_reference/P135_bt_ots_结构体.md)
- [bt_mcs_get_ots](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf535f1ab028407432ef890d278d936e0)
- [media_proxy_pl_name_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga0a70dc60a4d6acbcc58e220b75dad92a)
- [media_proxy_pl_icon_url_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gadd348a8d5aff193f7a9113a759e85b1d)
- [media_proxy_pl_track_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga4a93a18cb0b75cb16828243f0d37b4b4)
- [media_proxy_pl_track_title_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga9489b517e4baa215f0b7b59243cee11c)
- [media_proxy_pl_track_duration_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga7b0f9633a5322557b91ea97eafac9f34)
- [media_proxy_pl_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga61d494d7e149cfa2c3f9546c1e3b99bd)
- [media_proxy_pl_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga17c2ca149050e1382eb556f6dcccad21)
- [media_proxy_pl_seeking_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaeaf89f4b760870896ed42687562971ca)
- [media_proxy_pl_current_track_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gadcad4efdd714159d5d9611bbf74d5fae)
- [media_proxy_pl_next_track_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gaf0bd3447e64b6128710c07461766a0c9)
- [media_proxy_pl_parent_group_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga64730f46b87cf9089aff65b6be12f42d)
- [media_proxy_pl_current_group_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#gad02f2924e1aa765c04cbbc6441e7d063)
- [media_proxy_pl_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga96e8156b0267f3d55ee52ab307d81985)
- [media_proxy_pl_media_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga842d7951a04702d6f819de44c47b9cac)
- [media_proxy_pl_command_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga694e83401835149833024cf094b98cd1)
- [media_proxy_pl_commands_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga70ea8a24a4e853a191e0947e1c2d1145)
- [media_proxy_pl_search_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga8c0d75f61120047bacd0b933534e1b41)
- [media_proxy_pl_search_results_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html#ga35896de266f2a2bd101279e4ce9900c7)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [media_proxy_ctrl_cbs::search_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a0678ad4950c6f526c78d2143e9b7c385)
- [media_proxy_ctrl_cbs::commands_supported_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a06fadb043fd0a795f872063b7950d414)
- [media_proxy_ctrl_cbs::next_track_id_write](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a08b6fe1079b759de1f5a9f7751a22f21)
- [media_proxy_ctrl_cbs::content_ctrl_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a08f3f55a5b56d1ede9141013fe456119)
- [media_proxy_ctrl_cbs::seeking_speed_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a2ba0e73f7e67c38f5abe555305753d0f)
- [media_proxy_ctrl_cbs::parent_group_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a3c2b39bc46f8b2a7155c14dd430add8e)
- [media_proxy_ctrl_cbs::icon_url_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a53c4809b7a10b9057f565411429d691b)
- [media_proxy_ctrl_cbs::track_position_write](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a54f9f50e3b8f99b586a2c522a67da213)
- [media_proxy_ctrl_cbs::next_track_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a5692c0d142977b8ec7a4ffb765fd0687)
- [media_proxy_ctrl_cbs::playback_speed_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a5eb1466e8ba100c9d3cb12f097328b9e)
- [media_proxy_ctrl_cbs::current_track_id_write](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a66f35a59821f53f4ed9aa7dea0e4d654)
- [media_proxy_ctrl_cbs::playing_order_write](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a67cf70c9b72a87b03009f1da0a8980f2)
- [media_proxy_ctrl_cbs::track_position_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a6aa029523978e02dc1c8c7ff798e2433)
- [media_proxy_ctrl_cbs::playing_orders_supported_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a85182342b606c78127f2690ac1beab7d)
- [media_proxy_ctrl_cbs::current_group_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a858a8854259c8e7a09164b916fae309a)
- [media_proxy_ctrl_cbs::track_duration_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a85c0bfc83bb26c74b11b5cb8182ff1e0)
- [media_proxy_ctrl_cbs::command_send](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a89bb28499c989a9a2ad13d40dda6c6db)
- [media_proxy_ctrl_cbs::command_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a90481b6563033a4520b85307e07e2e3a)
- [media_proxy_ctrl_cbs::playing_order_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a92a3b0e3254d6b26e0d18476dce3b01e)
- [media_proxy_ctrl_cbs::player_name_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#a94b5ec6bc20299b722bd0e2cb28aed5e)
- [media_proxy_ctrl_cbs::current_track_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#aa3c2bd1734c6235eb2026915dbebc6c2)
- [media_proxy_ctrl_cbs::track_segments_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#aa7e7f7724689844491a4885544fc450c)
- [media_proxy_ctrl_cbs::icon_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#aaa7ba216e604be1c447a93231a0857d0)
- [media_proxy_ctrl_cbs::track_title_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#ac1afc71ed04faa87e644d095ef14946f)
- [media_proxy_ctrl_cbs::current_group_id_write](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#ad1a65519a958aa27091a2ba41260db04)
- [media_proxy_ctrl_cbs::media_state_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#ad4199644afcf356a565b884129ca0cf3)
- [media_proxy_ctrl_cbs::playback_speed_write](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#ad84d5caca4be208bd5e5d93f5c801ddf)
- [media_proxy_ctrl_cbs::track_changed_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#ade71f132ef66c7bfd13b1b1f3200681d)
- [media_proxy_ctrl_cbs::search_send](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#aee4a556023d56c3a0d4c2036b3bc0799)
- [media_proxy_ctrl_cbs::search_results_id_recv](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#af067e55ef7f676ad3c05f838160ed21e)
- [media_proxy_ctrl_cbs::local_player_instance](../device_power_control_model_reference/P029_media_proxy_ctrl_cbs_结构体.md#af2cd0f93aadd451f1b358e2d2d6a0049)
- [media_proxy_pl_calls::set_track_position](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a001ae07161b8a6c7dfc9c2e471f229e5)
- [media_proxy_pl_calls::get_track_position](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a11ea1cf984a7d11ac7e61405df84ee06)
- [media_proxy_pl_calls::get_parent_group_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a1409764199d47d0c27d07e13c8fa8f68)
- [media_proxy_pl_calls::get_track_duration](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a1b852ccc45a6ee1174b9d58df3b599b6)
- [media_proxy_pl_calls::send_search](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a416ca20a05a66f4ce28635159173f064)
- [media_proxy_pl_calls::set_current_track_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a422cec33063313a9aab86baf0bd65ef1)
- [media_proxy_pl_calls::set_current_group_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a5049e21965e7fd08aaeafcbedf76809c)
- [media_proxy_pl_calls::get_content_ctrl_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a64bc23cc61e69b1b6c4050f76a9bc674)
- [media_proxy_pl_calls::get_media_state](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a6a339aa7ee564acacffd2637eeb8e7ea)
- [media_proxy_pl_calls::set_playback_speed](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a7535dad9be2f4b83c8a7c55fccc8a7af)
- [media_proxy_pl_calls::get_current_track_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a7f19bd75114835d151ff5b26733ed450)
- [media_proxy_pl_calls::get_track_segments_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a86a71b788b54a4e7c966f162fcab6433)
- [media_proxy_pl_calls::get_playing_order](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a98989105d01265de4b268b623a26df2e)
- [media_proxy_pl_calls::get_current_group_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a98b02d4689cd5e279f43094f3ca09339)
- [media_proxy_pl_calls::get_playing_orders_supported](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#a9b733c3187cc032ef6644a16ffd3f7c9)
- [media_proxy_pl_calls::send_command](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#abae1ff89136b93ce4dee5dbe12e6791d)
- [media_proxy_pl_calls::set_player_name](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#acb3d3656aaed8c2801b7f4a5d40206f5)
- [media_proxy_pl_calls::set_next_track_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#acbf8dc9dcc8fbaba44d436310c92f3a9)
- [media_proxy_pl_calls::get_icon_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#ad1215725454c6b76dcdc197a275c03cf)
- [media_proxy_pl_calls::set_playing_order](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#ad6fad92957146aeaf1bec0e56606da72)
- [media_proxy_pl_calls::get_search_results_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#adf4003ba8ef1a5c38b75876f864564c5)
- [media_proxy_pl_calls::get_commands_supported](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#ae0a4457fcc35d32541f2557698d5aa83)
- [media_proxy_pl_calls::get_playback_speed](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#ae1006d5c684e12e1e1c927f71aa93930)
- [media_proxy_pl_calls::get_seeking_speed](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#aebf24b582cf33786f2dc17765d858a15)
- [media_proxy_pl_calls::get_next_track_id](../device_power_control_model_reference/P030_media_proxy_pl_calls_结构体.md#af939a96fbcfe474dfcdcfb353ae0aac5)
- [mpl_cmd_ntf::result_code](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md#a776bd9459d320e609697905067c0b284)
- [mpl_cmd_ntf::requested_opcode](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md#adcd5228cef8b7629d54053b155a91aa7)
- [mpl_cmd::opcode](../audio_video_model_reference/P037_mpl_cmd_结构体.md#a5cb29ca9e5a6b8249c69cc975b345e2f)
- [mpl_cmd::use_param](../audio_video_model_reference/P037_mpl_cmd_结构体.md#aca5e50b9f883a3c81f10ad51032a31f9)
- [mpl_cmd::param](../audio_video_model_reference/P037_mpl_cmd_结构体.md#ade5ed4d0ff2aeb192b8ed6b586c9bc9e)
- [mpl_sci::type](../audio_video_model_reference/P039_mpl_sci_结构体.md#a1dfc87f7e8b509ca05cbcd97a245953f)
- [mpl_sci::len](../audio_video_model_reference/P039_mpl_sci_结构体.md#a348314407c7b46d5ed583b97dfe932bc)
- [mpl_sci::param](../audio_video_model_reference/P039_mpl_sci_结构体.md#af093a6cd52a74cb2a0989727fc89f3aa)
- [mpl_search::search](../audio_video_model_reference/P040_mpl_search_结构体.md#a836bebfaadb56672a7e76c0ac2e450a9)
- [mpl_search::len](../audio_video_model_reference/P040_mpl_search_结构体.md#a9b9c64d3d9a25951da58ebf47bb63617)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P041_mcux_lpc_syscon_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P043_mipi_dsi_mcux_2l.h_源码浏览.md)
