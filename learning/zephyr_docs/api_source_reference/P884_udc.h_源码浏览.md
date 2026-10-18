---
id: learning.zephyr-docs.api-source-reference.page-884
title: udc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/udc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第884章\_udc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html)。

## 884.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="foldopen00024"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00094"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="foldopen00112"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="foldopen00133"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="foldopen00163"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="foldopen00185"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="foldopen00227"></a>
<a id="l00227"></a>
<a id="l00228"></a>
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
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00261"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="foldopen00276"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00307"></a>
<a id="foldopen00315"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="foldopen00329"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="foldopen00343"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="foldopen00419"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="foldopen00449"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="foldopen00480"></a>
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
<a id="foldopen00511"></a>
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
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00690"></a>
<a id="l00691"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="foldopen00752"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="foldopen00770"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="foldopen00787"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="foldopen00801"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00805"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="aatomic_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__atomic__apis_html_ga153c7d3a124e95ddf29e6f65bd124e44"></a>
<a id="agroup__net__buf_html_gaf2df457abe3e56d47107b76bdc004756"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="agroup__system__errno_html_gadd669d31505a077f769cff8e66c780b3"></a>
<a id="agroup__udc__api_html_ga0670bec8b55c013fb607ba53a8634ad4"></a>
<a id="agroup__udc__api_html_ga073a51222ac639d3c70af7b57970b42a"></a>
<a id="agroup__udc__api_html_ga075edc81fb3e39c2b377fc56c8c0915c"></a>
<a id="agroup__udc__api_html_ga19488ec4c93d81592bb5ffccfc1eadc4"></a>
<a id="agroup__udc__api_html_ga2c09f2a1e89c91527a8492019089d13f"></a>
<a id="agroup__udc__api_html_ga2d89f013b2e1279d1ec4cbd869e0cae6"></a>
<a id="agroup__udc__api_html_ga352ad356c5ec38dc5d18f076b97867b9"></a>
<a id="agroup__udc__api_html_ga3ee738bad8e1ee3928d32f57f82bef70"></a>
<a id="agroup__udc__api_html_ga409efee6a62a656a1349c07ba3a42bad"></a>
<a id="agroup__udc__api_html_ga40e50cf79b40d3792513e8fea3347f59"></a>
<a id="agroup__udc__api_html_ga50f6bde28b6a5fcab6b685107570e081"></a>
<a id="agroup__udc__api_html_ga52da2366ac5da1a695caa8826b342cbc"></a>
<a id="agroup__udc__api_html_ga59a92eb60575ca80d205cc29b4fb4f21"></a>
<a id="agroup__udc__api_html_ga68791ba18df95c8caf5f62c25a275baa"></a>
<a id="agroup__udc__api_html_ga6da3d836e868f2d09fe24854c2d76aeb"></a>
<a id="agroup__udc__api_html_ga6e6fb62fb8ebceca7e8e6b590c32efc2"></a>
<a id="agroup__udc__api_html_ga6feb32a2263307bdde9acc63d3c2ebb1"></a>
<a id="agroup__udc__api_html_ga7f575b548833cc1e5109e0d919630b3f"></a>
<a id="agroup__udc__api_html_ga81307ae4ab17ccd86be64bdf1653df0e"></a>
<a id="agroup__udc__api_html_ga88786eda763fce5c2a51521650ccc9f4"></a>
<a id="agroup__udc__api_html_gaa7c2eaa52bdbe1d763b2961124570e8a"></a>
<a id="agroup__udc__api_html_gaaf80c4d3b09686e8956cf121bfeb5e6c"></a>
<a id="agroup__udc__api_html_gab936f04015b0fee584756bcdf40d2f50"></a>
<a id="agroup__udc__api_html_gaca5f39f41358237966c37b280d92a0a5"></a>
<a id="agroup__udc__api_html_gacb2dc96353f1cffcc3d5e9710133fc0d"></a>
<a id="agroup__udc__api_html_gacc4b5c127532c994406df30bacab5684"></a>
<a id="agroup__udc__api_html_gad3fb1d64b6e0cf051627011ce673bb1e"></a>
<a id="agroup__udc__api_html_gadec9c8af89b28984028fd8e0b1a8c776"></a>
<a id="agroup__udc__api_html_gaedd615defad234b001e74448f89488e1"></a>
<a id="agroup__udc__api_html_gafbb0dec089f83fd674bd19670a882c65"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructdevice_html_a4a2e6a2cfeb6efed7d5383c33458f46d"></a>
<a id="astructk__fifo_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_a1522d81a002804223e25300a6961f527"></a>
<a id="astructudc__api_html"></a>
<a id="astructudc__api_html_a01f803a2d258072df102b831cf184b27"></a>
<a id="astructudc__api_html_a023fcfa0fa251dcadcb379347fe7531a"></a>
<a id="astructudc__api_html_a1af05b484e9c9d1f2a0dbfb822f09c98"></a>
<a id="astructudc__api_html_a1e3d733665cd609381e02929907c9837"></a>
<a id="astructudc__api_html_a27291ab4d2acda207f6a6a2313d50793"></a>
<a id="astructudc__api_html_a2be8523215fd255112bb03d9cd54c26b"></a>
<a id="astructudc__api_html_a2e8b88743ab56144a199b3ad0618755f"></a>
<a id="astructudc__api_html_a775a18f5555f1c518762ff7dc016559c"></a>
<a id="astructudc__api_html_a8997bba956d264463b71aae0b1a4e3dc"></a>
<a id="astructudc__api_html_a923a684868721d0b7232c86eed15e121"></a>
<a id="astructudc__api_html_aa1d3dadf63cb156ce5346712e1c65069"></a>
<a id="astructudc__api_html_ab06839ded48cbc671b2b915fe0010959"></a>
<a id="astructudc__api_html_ad7135abf78eb372730dddbba7dc6a75d"></a>
<a id="astructudc__api_html_adf2adaea90b53999d1e98756062a2050"></a>
<a id="astructudc__api_html_adf2b8f76158d7bd2d3918628c8a9fc22"></a>
<a id="astructudc__api_html_aeca6c3a8a6b7af469d96bec8c9a8e5eb"></a>
<a id="astructudc__api_html_af8b916f6b8c211ad82ddcfdaa12de5ae"></a>
<a id="astructudc__buf__info_html"></a>
<a id="astructudc__buf__info_html_a0a1c09f587d3f6847cb7ce77514a3321"></a>
<a id="astructudc__buf__info_html_a33e927f23d227a4974915c65927284ec"></a>
<a id="astructudc__buf__info_html_a4cd2e83000a0551d126bebe89552eab9"></a>
<a id="astructudc__buf__info_html_a84cf74496eddc4a69a47d23dcdbf753f"></a>
<a id="astructudc__buf__info_html_a9664e1f7cddd36dbc7d206b52da45170"></a>
<a id="astructudc__buf__info_html_a9b03b6dd8418d4200733a612aac73daa"></a>
<a id="astructudc__buf__info_html_ab500ff0bf12ecdbbd4f3cb48d0556ed2"></a>
<a id="astructudc__buf__info_html_af1c92f1cdd6e0474a19f788140fdc573"></a>
<a id="astructudc__buf__info_html_afc2d0c391aca7f68a1ae5539a1fed8a0"></a>
<a id="astructudc__data_html"></a>
<a id="astructudc__data_html_a1ba1b93af26bca4f4554a43a65ab3c2a"></a>
<a id="astructudc__data_html_a2222bd71ecbb8051dfab7b6134f9a2c9"></a>
<a id="astructudc__data_html_a849581d1e3692c6c585e9fb24e9bbb4f"></a>
<a id="astructudc__data_html_a9bb216d0c87b9ff4e2e99f0c3cfbb381"></a>
<a id="astructudc__data_html_a9c1ae6e5e204b5a0ed15e92f8b3b384f"></a>
<a id="astructudc__data_html_aae68bfba2e92894851c36dd40c33c0f0"></a>
<a id="astructudc__data_html_aaf98e53580a27635a7b02acbcf29ae14"></a>
<a id="astructudc__data_html_ac58682fa2f37bf2034a69cc9b6b10dfb"></a>
<a id="astructudc__data_html_acc471b34bb24453377b1ae54d33fa415"></a>
<a id="astructudc__data_html_ae301e1a80165ae90d7d09dbb6463c88c"></a>
<a id="astructudc__device__caps_html"></a>
<a id="astructudc__device__caps_html_a0adada5003bccfbd6df8329198639dc0"></a>
<a id="astructudc__device__caps_html_a63affa3fe08cbaec8351297ad9d26911"></a>
<a id="astructudc__device__caps_html_a7aaf6ecac2904acb5560f2f90cfef8d1"></a>
<a id="astructudc__device__caps_html_aab85e74e40876040c3d2f961c36b9780"></a>
<a id="astructudc__device__caps_html_aea376ff4a0c5a27c3b8f7d4416e17b5b"></a>
<a id="astructudc__device__caps_html_aefef262532e3eab3baa90eb8e79f9dc8"></a>
<a id="astructudc__ep__caps_html"></a>
<a id="astructudc__ep__caps_html_a15ce10028e09b3af021a83dc36eba99a"></a>
<a id="astructudc__ep__caps_html_a3a944cda429c916b60cff3a332b970a7"></a>
<a id="astructudc__ep__caps_html_a5e90d1362855dd77a1f7ef9e0cd82ef8"></a>
<a id="astructudc__ep__caps_html_a73ec7e7c7fd043065a7c59c89c6cc36e"></a>
<a id="astructudc__ep__caps_html_a73f06f9e2af5770cab84d2adb76d42de"></a>
<a id="astructudc__ep__caps_html_a98afb85c03ff01ba82d55884cea0ea31"></a>
<a id="astructudc__ep__caps_html_ad556a4c17a01bb6b8355fb6b5ea9d418"></a>
<a id="astructudc__ep__caps_html_afc424ee2bb31c19451facc0b79bb73c7"></a>
<a id="astructudc__ep__config_html"></a>
<a id="astructudc__ep__config_html_a1f2afc2d5e512229688764e1b7cd0171"></a>
<a id="astructudc__ep__config_html_a706987205ac971574d1b81bf72d03248"></a>
<a id="astructudc__ep__config_html_aa62ff3f308771d51563df88439570918"></a>
<a id="astructudc__ep__config_html_ac795b839cbd426d233a1f91d10d5fc7e"></a>
<a id="astructudc__ep__config_html_acbeab755d1b03da0c58f43aff5bd7d00"></a>
<a id="astructudc__ep__config_html_ad42f77d1a9d65239cdb142209050e38e"></a>
<a id="astructudc__ep__config_html_ae4f75e52d1c822f5d873095a761c6b48"></a>
<a id="astructudc__ep__stat_html"></a>
<a id="astructudc__ep__stat_html_a250eed32f2945cb89df8033ae2781969"></a>
<a id="astructudc__ep__stat_html_a2c9522c3f5e4f1a9cba90cd73092c07f"></a>
<a id="astructudc__ep__stat_html_a47a7b3247c2aee78c3b58835081aed0c"></a>
<a id="astructudc__ep__stat_html_a5273e8e99fb6943babcb573f10c90c76"></a>
<a id="astructudc__event_html"></a>
<a id="astructudc__event_html_a0707d65716a4b1e6dd3132a0bb370770"></a>
<a id="astructudc__event_html_a3acfe5d21d16f6edfa24e9964b636434"></a>
<a id="astructudc__event_html_a900404c46850d34cd7121eeedc2fce9d"></a>
<a id="astructudc__event_html_ac1ff3bc9d629eb9b6c55602e7861e945"></a>
<a id="astructudc__event_html_ada24e0e920c39bc60a6c7fbbe54277f4"></a>
<a id="audc_8h_html_a03749f5acb64ff8cfddc3c0b6b81a040"></a>
<a id="audc_8h_html_a03749f5acb64ff8cfddc3c0b6b81a040a010cfc9f43a6faf68323201ae02fa00d"></a>
<a id="audc_8h_html_a03749f5acb64ff8cfddc3c0b6b81a040a0e0da320fe601eb1de24c142fc60f332"></a>
<a id="audc_8h_html_a03749f5acb64ff8cfddc3c0b6b81a040a120dc649618040f41da7542bf639159f"></a>
<a id="audc_8h_html_a03749f5acb64ff8cfddc3c0b6b81a040a4bdf374daa2aeb4f7b6b6c5fe2a46432"></a>
<a id="audc_8h_html_a03749f5acb64ff8cfddc3c0b6b81a040a52bb5ea941db9a025ccb73de3fc6d55b"></a>
<a id="audc_8h_html_a03749f5acb64ff8cfddc3c0b6b81a040a8ff69c0bc684eb113f1d4e0ec02dd70d"></a>
<a id="audc_8h_html_a03749f5acb64ff8cfddc3c0b6b81a040aa174f33c3802cec8d6c37606bc5ba9bb"></a>
<a id="audc_8h_html_a03749f5acb64ff8cfddc3c0b6b81a040af20153f2fde8ea2bb1a985f2e17a2f78"></a>
<a id="audc_8h_html_a32d61ab6dbb734009102b5239a834d1b"></a>
<a id="audc_8h_html_a32d61ab6dbb734009102b5239a834d1ba71b0e0a870859cf1f0c11380833f790a"></a>
<a id="audc_8h_html_a32d61ab6dbb734009102b5239a834d1ba8177d4c8e8cb0456f9c2a553c76dc0d5"></a>
<a id="audc_8h_html_a32d61ab6dbb734009102b5239a834d1ba872aa49861a213ad970012f43db7d35d"></a>
<a id="audc_8h_html_a32d61ab6dbb734009102b5239a834d1ba9fc26a4b4ba8db446731274b67182599"></a>
<a id="audc_8h_html_a8c96946734085924e2afc591ac502551"></a>
<a id="audc_8h_html_aa3ff247fd5234f65d91f84ebc38e384a"></a>
<a id="audc_8h_html_ac254f8a970f890d14e35c43474c915fd"></a>
<a id="audc_8h_html_ac254f8a970f890d14e35c43474c915fda1930322c1c7b053f3b9da2e319ed11e7"></a>
<a id="audc_8h_html_ac254f8a970f890d14e35c43474c915fda4a8ba94e9dced296d0e269390931e85a"></a>
<a id="audc_8h_html_ac254f8a970f890d14e35c43474c915fdab481546bd71839266d4d881d6610633a"></a>
<a id="audc_8h_html_ac254f8a970f890d14e35c43474c915fdad961e13d52b708c9e6b8d951affd31bb"></a>
<a id="audc_8h_html_ac3a36aa8cb3aab95d7931cb602631c36"></a>
<a id="audc_8h_html_ad10596af54465c3cb10cc59ae9a507d2"></a>
<a id="ausb__buf_8h_html"></a>
<a id="ausb__ch9_8h_html"></a>
<a id="ausb__ch9_8h_html_a495d790dfb00609ce029631f40d0a422"></a>
<a id="ausb__ch9_8h_html_ae028a023a157a29a0e83dee304c6267a"></a>

```c
/*
 * Copyright (c) 2021-2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_UDC_H
#define ZEPHYR_INCLUDE_UDC_H

#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/usb/usb_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/usb/usb_ch9.h>

enum udc_mps0 {
        UDC_MPS0_8,
        UDC_MPS0_16,
        UDC_MPS0_32,
        UDC_MPS0_64,
};

struct udc_device_caps {
        uint32_t hs : 1;
        uint32_t rwup : 1;
        uint32_t out_ack : 1;
        uint32_t addr_before_status : 1;
        uint32_t can_detect_vbus : 1;
        enum udc_mps0 mps0 : 2;
};

enum udc_bus_speed {
        UDC_BUS_UNKNOWN,
        UDC_BUS_SPEED_FS,
        UDC_BUS_SPEED_HS,
        UDC_BUS_SPEED_SS,
};

struct udc_ep_caps {
        uint32_t mps : 16;
        uint32_t control : 1;
        uint32_t interrupt : 1;
        uint32_t bulk : 1;
        uint32_t iso : 1;
        uint32_t high_bandwidth : 1;
        uint32_t in : 1;
        uint32_t out : 1;
};

struct udc_ep_stat {
        bool enabled;
        bool halted;
        bool data1;
        bool busy;
};

struct udc_ep_config {
        struct k_fifo fifo;
        struct udc_ep_caps caps;
        struct udc_ep_stat stat;
        uint8_t addr;
        uint8_t attributes;
        uint16_t mps;
        uint8_t interval;
};


enum udc_event_type {
        UDC_EVT_VBUS_READY,
        UDC_EVT_VBUS_REMOVED,
        UDC_EVT_RESUME,
        UDC_EVT_SUSPEND,
        UDC_EVT_RESET,
        UDC_EVT_SOF,
        UDC_EVT_EP_REQUEST,
        UDC_EVT_ERROR,
};

struct udc_event {
        enum udc_event_type type;
        union {
                uint32_t value;
                int status;
                struct net_buf *buf;
        };
        const struct device *dev;
};

struct udc_buf_info {
        uint8_t ep;
        unsigned int setup : 1;
        unsigned int data : 1;
        unsigned int status : 1;
        unsigned int zlp : 1;
        unsigned int claimed : 1;
        unsigned int queued : 1;
        void *owner;
        int err;
} __packed;

typedef int (*udc_event_cb_t)(const struct device *dev,
                              const struct udc_event *const event);

struct udc_api {
        enum udc_bus_speed (*device_speed)(const struct device *dev);
        int (*ep_enqueue)(const struct device *dev,
                          struct udc_ep_config *const cfg,
                          struct net_buf *const buf);
        int (*ep_dequeue)(const struct device *dev,
                          struct udc_ep_config *const cfg);
        int (*ep_set_halt)(const struct device *dev,
                           struct udc_ep_config *const cfg);
        int (*ep_clear_halt)(const struct device *dev,
                             struct udc_ep_config *const cfg);
        int (*ep_try_config)(const struct device *dev,
                             struct udc_ep_config *const cfg);
        int (*ep_enable)(const struct device *dev,
                         struct udc_ep_config *const cfg);
        int (*ep_disable)(const struct device *dev,
                          struct udc_ep_config *const cfg);
        int (*host_wakeup)(const struct device *dev);
        int (*set_address)(const struct device *dev,
                           const uint8_t addr);
        int (*test_mode)(const struct device *dev,
                         const uint8_t mode, const bool dryrun);
        int (*enable)(const struct device *dev);
        int (*disable)(const struct device *dev);
        int (*init)(const struct device *dev);
        int (*shutdown)(const struct device *dev);
        void (*lock)(const struct device *dev);
        void (*unlock)(const struct device *dev);
};

#define UDC_STATUS_INITIALIZED          0
#define UDC_STATUS_ENABLED              1
#define UDC_STATUS_SUSPENDED            2

struct udc_data {
        struct udc_ep_config *ep_lut[32];
        struct udc_device_caps caps;
        struct k_mutex mutex;
        udc_event_cb_t event_cb;
        const void *event_ctx;
        atomic_t status;
        void *priv;
        uint8_t setup[8];
        bool setup_pending;
        bool setup_valid;
};


static inline bool udc_is_initialized(const struct device *dev)
{
        struct udc_data *data = (struct udc_data *)dev->data;

        return atomic_test_bit(&data->status, UDC_STATUS_INITIALIZED);
}

static inline bool udc_is_enabled(const struct device *dev)
{
        struct udc_data *data = (struct udc_data *)dev->data;

        return atomic_test_bit(&data->status, UDC_STATUS_ENABLED);
}

static inline bool udc_is_suspended(const struct device *dev)
{
        struct udc_data *data = (struct udc_data *)dev->data;

        return atomic_test_bit(&data->status, UDC_STATUS_SUSPENDED);
}

int udc_init(const struct device *dev,
             udc_event_cb_t event_cb, const void *const event_ctx);

int udc_enable(const struct device *dev);

int udc_disable(const struct device *dev);

int udc_shutdown(const struct device *dev);

static inline struct udc_device_caps udc_caps(const struct device *dev)
{
        struct udc_data *data = (struct udc_data *)dev->data;

        return data->caps;
}

enum udc_bus_speed udc_device_speed(const struct device *dev);

static inline int udc_set_address(const struct device *dev, const uint8_t addr)
{
        const struct udc_api *api = (const struct udc_api *)dev->api;
        int ret;

        if (!udc_is_enabled(dev)) {
                return -EPERM;
        }

        api->lock(dev);
        ret = api->set_address(dev, addr);
        api->unlock(dev);

        return ret;
}

static inline int udc_test_mode(const struct device *dev,
                                const uint8_t mode, const bool dryrun)
{
        const struct udc_api *api = (const struct udc_api *)dev->api;
        int ret;

        if (!udc_is_enabled(dev)) {
                return -EPERM;
        }

        if (api->test_mode != NULL) {
                api->lock(dev);
                ret = api->test_mode(dev, mode, dryrun);
                api->unlock(dev);
        } else {
                ret = -ENOTSUP;
        }

        return ret;
}

static inline int udc_host_wakeup(const struct device *dev)
{
        const struct udc_api *api = (const struct udc_api *)dev->api;
        int ret;

        if (!udc_is_enabled(dev)) {
                return -EPERM;
        }

        api->lock(dev);
        ret = api->host_wakeup(dev);
        api->unlock(dev);

        return ret;
}

int udc_ep_try_config(const struct device *dev,
                      const uint8_t ep,
                      const uint8_t attributes,
                      uint16_t *const mps,
                      const uint8_t interval);

int udc_ep_enable(const struct device *dev,
                  const uint8_t ep,
                  const uint8_t attributes,
                  const uint16_t mps,
                  const uint8_t interval);

int udc_ep_disable(const struct device *dev, const uint8_t ep);

int udc_ep_set_halt(const struct device *dev, const uint8_t ep);

int udc_ep_clear_halt(const struct device *dev, const uint8_t ep);

int udc_ep_enqueue(const struct device *dev, struct net_buf *const buf);

int udc_purge_queues(const struct device *dev);

bool udc_ep_queue_is_empty(const struct device *dev, const uint8_t ep);

int udc_ep_dequeue(const struct device *dev, const uint8_t ep);

struct net_buf *udc_ep_buf_alloc(const struct device *dev,
                                 const uint8_t ep,
                                 const size_t size);

struct net_buf *udc_ctrl_setup_alloc(const struct device *dev);

struct net_buf *udc_ctrl_data_alloc(const struct device *dev,
                                    const uint8_t ep,
                                    const size_t size);

struct net_buf *udc_ctrl_status_alloc(const struct device *dev,
                                      const uint8_t ep);

int udc_ep_buf_free(const struct device *dev, struct net_buf *const buf);

static inline void udc_ep_buf_set_zlp(struct net_buf *const buf)
{
        struct udc_buf_info *bi;

        __ASSERT_NO_MSG(buf);
        bi = (struct udc_buf_info *)net_buf_user_data(buf);
        if (USB_EP_DIR_IS_IN(bi->ep)) {
                bi->zlp = 1;
        }
}

static inline struct udc_buf_info *udc_get_buf_info(const struct net_buf *const buf)
{
        __ASSERT_NO_MSG(buf);
        return (struct udc_buf_info *)net_buf_user_data(buf);
}


static inline const void *udc_get_event_ctx(const struct device *dev)
{
        struct udc_data *data = (struct udc_data *)dev->data;

        return data->event_ctx;
}

static inline uint16_t udc_mps_ep_size(const struct udc_ep_config *const cfg)
{
        return USB_MPS_EP_SIZE(cfg->mps);
}


#endif /* ZEPHYR_INCLUDE_UDC_H */
```

## 884.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021-2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 810 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_UDC_H`。

## 884.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/usb/usb_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/usb__buf_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/usb/usb_ch9.h](../usb/P172_USB标准请求与描述符常量.md)
- [udc_mps0](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#ac254f8a970f890d14e35c43474c915fd)
- [UDC_MPS0_8](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#ac254f8a970f890d14e35c43474c915fdad961e13d52b708c9e6b8d951affd31bb)
- [UDC_MPS0_16](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#ac254f8a970f890d14e35c43474c915fda4a8ba94e9dced296d0e269390931e85a)
- [UDC_MPS0_32](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#ac254f8a970f890d14e35c43474c915fda1930322c1c7b053f3b9da2e319ed11e7)
- [UDC_MPS0_64](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#ac254f8a970f890d14e35c43474c915fdab481546bd71839266d4d881d6610633a)
- [udc_device_caps](../usb/P034_USB设备控制器设备能力.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [hs](../usb/P034_USB设备控制器设备能力.md#aea376ff4a0c5a27c3b8f7d4416e17b5b)
- [rwup](../usb/P034_USB设备控制器设备能力.md#aab85e74e40876040c3d2f961c36b9780)
- [out_ack](../usb/P034_USB设备控制器设备能力.md#a0adada5003bccfbd6df8329198639dc0)
- [addr_before_status](../usb/P034_USB设备控制器设备能力.md#aefef262532e3eab3baa90eb8e79f9dc8)
- [can_detect_vbus](../usb/P034_USB设备控制器设备能力.md#a7aaf6ecac2904acb5560f2f90cfef8d1)
- [mps0](../usb/P034_USB设备控制器设备能力.md#a63affa3fe08cbaec8351297ad9d26911)
- [udc_bus_speed](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a32d61ab6dbb734009102b5239a834d1b)
- [UDC_BUS_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a32d61ab6dbb734009102b5239a834d1ba872aa49861a213ad970012f43db7d35d)
- [UDC_BUS_SPEED_FS](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a32d61ab6dbb734009102b5239a834d1ba8177d4c8e8cb0456f9c2a553c76dc0d5)
- [UDC_BUS_SPEED_HS](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a32d61ab6dbb734009102b5239a834d1ba9fc26a4b4ba8db446731274b67182599)
- [UDC_BUS_SPEED_SS](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a32d61ab6dbb734009102b5239a834d1ba71b0e0a870859cf1f0c11380833f790a)
- [udc_ep_caps](../usb/P035_USB设备控制器端点能力.md)
- [mps](../usb/P035_USB设备控制器端点能力.md#a5e90d1362855dd77a1f7ef9e0cd82ef8)
- [control](../usb/P035_USB设备控制器端点能力.md#a98afb85c03ff01ba82d55884cea0ea31)
- [interrupt](../usb/P035_USB设备控制器端点能力.md#a73f06f9e2af5770cab84d2adb76d42de)
- [bulk](../usb/P035_USB设备控制器端点能力.md#a73ec7e7c7fd043065a7c59c89c6cc36e)
- [iso](../usb/P035_USB设备控制器端点能力.md#a15ce10028e09b3af021a83dc36eba99a)
- [high_bandwidth](../usb/P035_USB设备控制器端点能力.md#ad556a4c17a01bb6b8355fb6b5ea9d418)
- [in](../usb/P035_USB设备控制器端点能力.md#a3a944cda429c916b60cff3a332b970a7)
- [out](../usb/P035_USB设备控制器端点能力.md#afc424ee2bb31c19451facc0b79bb73c7)
- [udc_ep_stat](../usb/P037_USB设备控制器端点状态.md)
- [enabled](../usb/P037_USB设备控制器端点状态.md#a250eed32f2945cb89df8033ae2781969)
- [halted](../usb/P037_USB设备控制器端点状态.md#a5273e8e99fb6943babcb573f10c90c76)
- [data1](../usb/P037_USB设备控制器端点状态.md#a2c9522c3f5e4f1a9cba90cd73092c07f)
- [busy](../usb/P037_USB设备控制器端点状态.md#a47a7b3247c2aee78c3b58835081aed0c)
- [udc_ep_config](../usb/P036_USB设备控制器端点配置.md)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [fifo](../usb/P036_USB设备控制器端点配置.md#aa62ff3f308771d51563df88439570918)
- [caps](../usb/P036_USB设备控制器端点配置.md#a706987205ac971574d1b81bf72d03248)
- [stat](../usb/P036_USB设备控制器端点配置.md#ad42f77d1a9d65239cdb142209050e38e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [addr](../usb/P036_USB设备控制器端点配置.md#ac795b839cbd426d233a1f91d10d5fc7e)
- [attributes](../usb/P036_USB设备控制器端点配置.md#acbeab755d1b03da0c58f43aff5bd7d00)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [mps](../usb/P036_USB设备控制器端点配置.md#ae4f75e52d1c822f5d873095a761c6b48)
- [interval](../usb/P036_USB设备控制器端点配置.md#a1f2afc2d5e512229688764e1b7cd0171)
- [udc_event_type](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a03749f5acb64ff8cfddc3c0b6b81a040)
- [UDC_EVT_VBUS_READY](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a03749f5acb64ff8cfddc3c0b6b81a040a010cfc9f43a6faf68323201ae02fa00d)
- [UDC_EVT_VBUS_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a03749f5acb64ff8cfddc3c0b6b81a040a4bdf374daa2aeb4f7b6b6c5fe2a46432)
- [UDC_EVT_RESUME](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a03749f5acb64ff8cfddc3c0b6b81a040a0e0da320fe601eb1de24c142fc60f332)
- [UDC_EVT_SUSPEND](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a03749f5acb64ff8cfddc3c0b6b81a040a120dc649618040f41da7542bf639159f)
- [UDC_EVT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a03749f5acb64ff8cfddc3c0b6b81a040aa174f33c3802cec8d6c37606bc5ba9bb)
- [UDC_EVT_SOF](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a03749f5acb64ff8cfddc3c0b6b81a040af20153f2fde8ea2bb1a985f2e17a2f78)
- [UDC_EVT_EP_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a03749f5acb64ff8cfddc3c0b6b81a040a52bb5ea941db9a025ccb73de3fc6d55b)
- [UDC_EVT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a03749f5acb64ff8cfddc3c0b6b81a040a8ff69c0bc684eb113f1d4e0ec02dd70d)
- [udc_event](../usb/P038_USB设备控制器事件结构.md)
- [type](../usb/P038_USB设备控制器事件结构.md#a3acfe5d21d16f6edfa24e9964b636434)
- [value](../usb/P038_USB设备控制器事件结构.md#ada24e0e920c39bc60a6c7fbbe54277f4)
- [status](../usb/P038_USB设备控制器事件结构.md#a0707d65716a4b1e6dd3132a0bb370770)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [buf](../usb/P038_USB设备控制器事件结构.md#ac1ff3bc9d629eb9b6c55602e7861e945)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../usb/P038_USB设备控制器事件结构.md#a900404c46850d34cd7121eeedc2fce9d)
- [udc_buf_info](../usb/P032_USB设备控制器缓冲区信息.md)
- [ep](../usb/P032_USB设备控制器缓冲区信息.md#a0a1c09f587d3f6847cb7ce77514a3321)
- [setup](../usb/P032_USB设备控制器缓冲区信息.md#a9664e1f7cddd36dbc7d206b52da45170)
- [data](../usb/P032_USB设备控制器缓冲区信息.md#ab500ff0bf12ecdbbd4f3cb48d0556ed2)
- [status](../usb/P032_USB设备控制器缓冲区信息.md#a84cf74496eddc4a69a47d23dcdbf753f)
- [zlp](../usb/P032_USB设备控制器缓冲区信息.md#afc2d0c391aca7f68a1ae5539a1fed8a0)
- [claimed](../usb/P032_USB设备控制器缓冲区信息.md#a9b03b6dd8418d4200733a612aac73daa)
- [queued](../usb/P032_USB设备控制器缓冲区信息.md#a4cd2e83000a0551d126bebe89552eab9)
- [owner](../usb/P032_USB设备控制器缓冲区信息.md#a33e927f23d227a4974915c65927284ec)
- [err](../usb/P032_USB设备控制器缓冲区信息.md#af1c92f1cdd6e0474a19f788140fdc573)
- [udc_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#aa3ff247fd5234f65d91f84ebc38e384a)
- [udc_api](../usb/P031_USB设备控制器驱动接口.md)
- [device_speed](../usb/P031_USB设备控制器驱动接口.md#adf2b8f76158d7bd2d3918628c8a9fc22)
- [ep_enqueue](../usb/P031_USB设备控制器驱动接口.md#aa1d3dadf63cb156ce5346712e1c65069)
- [ep_dequeue](../usb/P031_USB设备控制器驱动接口.md#a023fcfa0fa251dcadcb379347fe7531a)
- [ep_set_halt](../usb/P031_USB设备控制器驱动接口.md#adf2adaea90b53999d1e98756062a2050)
- [ep_clear_halt](../usb/P031_USB设备控制器驱动接口.md#a923a684868721d0b7232c86eed15e121)
- [ep_try_config](../usb/P031_USB设备控制器驱动接口.md#a775a18f5555f1c518762ff7dc016559c)
- [ep_enable](../usb/P031_USB设备控制器驱动接口.md#a27291ab4d2acda207f6a6a2313d50793)
- [ep_disable](../usb/P031_USB设备控制器驱动接口.md#a1af05b484e9c9d1f2a0dbfb822f09c98)
- [host_wakeup](../usb/P031_USB设备控制器驱动接口.md#aeca6c3a8a6b7af469d96bec8c9a8e5eb)
- [set_address](../usb/P031_USB设备控制器驱动接口.md#a2e8b88743ab56144a199b3ad0618755f)
- [test_mode](../usb/P031_USB设备控制器驱动接口.md#ab06839ded48cbc671b2b915fe0010959)
- [enable](../usb/P031_USB设备控制器驱动接口.md#af8b916f6b8c211ad82ddcfdaa12de5ae)
- [disable](../usb/P031_USB设备控制器驱动接口.md#a8997bba956d264463b71aae0b1a4e3dc)
- [init](../usb/P031_USB设备控制器驱动接口.md#a01f803a2d258072df102b831cf184b27)
- [shutdown](../usb/P031_USB设备控制器驱动接口.md#ad7135abf78eb372730dddbba7dc6a75d)
- [lock](../usb/P031_USB设备控制器驱动接口.md#a1e3d733665cd609381e02929907c9837)
- [unlock](../usb/P031_USB设备控制器驱动接口.md#a2be8523215fd255112bb03d9cd54c26b)
- [udc_data](../usb/P033_USB设备控制器驱动数据.md)
- [ep_lut](../usb/P033_USB设备控制器驱动数据.md#acc471b34bb24453377b1ae54d33fa415)
- [caps](../usb/P033_USB设备控制器驱动数据.md#aae68bfba2e92894851c36dd40c33c0f0)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [mutex](../usb/P033_USB设备控制器驱动数据.md#a1ba1b93af26bca4f4554a43a65ab3c2a)
- [event_cb](../usb/P033_USB设备控制器驱动数据.md#a9bb216d0c87b9ff4e2e99f0c3cfbb381)
- [event_ctx](../usb/P033_USB设备控制器驱动数据.md#aaf98e53580a27635a7b02acbcf29ae14)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [status](../usb/P033_USB设备控制器驱动数据.md#a9c1ae6e5e204b5a0ed15e92f8b3b384f)
- [priv](../usb/P033_USB设备控制器驱动数据.md#ac58682fa2f37bf2034a69cc9b6b10dfb)
- [setup](../usb/P033_USB设备控制器驱动数据.md#ae301e1a80165ae90d7d09dbb6463c88c)
- [setup_pending](../usb/P033_USB设备控制器驱动数据.md#a849581d1e3692c6c585e9fb24e9bbb4f)
- [setup_valid](../usb/P033_USB设备控制器驱动数据.md#a2222bd71ecbb8051dfab7b6134f9a2c9)
- [udc_is_initialized](../usb/P030_USB设备控制器API.md#ga40e50cf79b40d3792513e8fea3347f59)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [atomic_test_bit](https://docs.zephyrproject.org/latest/doxygen/html/group__atomic__apis.html#ga153c7d3a124e95ddf29e6f65bd124e44)
- [UDC_STATUS_INITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a8c96946734085924e2afc591ac502551)
- [udc_is_enabled](../usb/P030_USB设备控制器API.md#ga2c09f2a1e89c91527a8492019089d13f)
- [UDC_STATUS_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#ad10596af54465c3cb10cc59ae9a507d2)
- [udc_is_suspended](../usb/P030_USB设备控制器API.md#ga88786eda763fce5c2a51521650ccc9f4)
- [UDC_STATUS_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#ac3a36aa8cb3aab95d7931cb602631c36)
- [udc_init](../usb/P030_USB设备控制器API.md#ga0670bec8b55c013fb607ba53a8634ad4)
- [udc_enable](../usb/P030_USB设备控制器API.md#gafbb0dec089f83fd674bd19670a882c65)
- [udc_disable](../usb/P030_USB设备控制器API.md#gaa7c2eaa52bdbe1d763b2961124570e8a)
- [udc_shutdown](../usb/P030_USB设备控制器API.md#ga59a92eb60575ca80d205cc29b4fb4f21)
- [udc_caps](../usb/P030_USB设备控制器API.md#ga3ee738bad8e1ee3928d32f57f82bef70)
- [udc_device_speed](../usb/P030_USB设备控制器API.md#gab936f04015b0fee584756bcdf40d2f50)
- [udc_set_address](../usb/P030_USB设备控制器API.md#ga6feb32a2263307bdde9acc63d3c2ebb1)
- [api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [EPERM](../error_reference/P003_系统错误号公共接口.md#gadd669d31505a077f769cff8e66c780b3)
- [udc_test_mode](../usb/P030_USB设备控制器API.md#ga7f575b548833cc1e5109e0d919630b3f)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [udc_host_wakeup](../usb/P030_USB设备控制器API.md#ga075edc81fb3e39c2b377fc56c8c0915c)
- [udc_ep_try_config](../usb/P030_USB设备控制器API.md#ga81307ae4ab17ccd86be64bdf1653df0e)
- [udc_ep_enable](../usb/P030_USB设备控制器API.md#gacc4b5c127532c994406df30bacab5684)
- [udc_ep_disable](../usb/P030_USB设备控制器API.md#ga52da2366ac5da1a695caa8826b342cbc)
- [udc_ep_set_halt](../usb/P030_USB设备控制器API.md#ga19488ec4c93d81592bb5ffccfc1eadc4)
- [udc_ep_clear_halt](../usb/P030_USB设备控制器API.md#gadec9c8af89b28984028fd8e0b1a8c776)
- [udc_ep_enqueue](../usb/P030_USB设备控制器API.md#gacb2dc96353f1cffcc3d5e9710133fc0d)
- [udc_purge_queues](../usb/P030_USB设备控制器API.md#ga409efee6a62a656a1349c07ba3a42bad)
- [udc_ep_queue_is_empty](../usb/P030_USB设备控制器API.md#ga352ad356c5ec38dc5d18f076b97867b9)
- [udc_ep_dequeue](../usb/P030_USB设备控制器API.md#ga6e6fb62fb8ebceca7e8e6b590c32efc2)
- [udc_ep_buf_alloc](../usb/P030_USB设备控制器API.md#gad3fb1d64b6e0cf051627011ce673bb1e)
- [size](../network_core_model_reference/P046_net_buf_结构体.md#a1522d81a002804223e25300a6961f527)
- [udc_ctrl_setup_alloc](../usb/P030_USB设备控制器API.md#gaaf80c4d3b09686e8956cf121bfeb5e6c)
- [udc_ctrl_data_alloc](../usb/P030_USB设备控制器API.md#ga68791ba18df95c8caf5f62c25a275baa)
- [udc_ctrl_status_alloc](../usb/P030_USB设备控制器API.md#gaca5f39f41358237966c37b280d92a0a5)
- [udc_ep_buf_free](../usb/P030_USB设备控制器API.md#gaedd615defad234b001e74448f89488e1)
- [udc_ep_buf_set_zlp](../usb/P030_USB设备控制器API.md#ga50f6bde28b6a5fcab6b685107570e081)
- [net_buf_user_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf2df457abe3e56d47107b76bdc004756)
- [USB_EP_DIR_IS_IN](../usb/P172_USB标准请求与描述符常量.md#a495d790dfb00609ce029631f40d0a422)
- [udc_get_buf_info](../usb/P030_USB设备控制器API.md#ga073a51222ac639d3c70af7b57970b42a)
- [udc_get_event_ctx](../usb/P030_USB设备控制器API.md#ga2d89f013b2e1279d1ec4cbd869e0cae6)
- [udc_mps_ep_size](../usb/P030_USB设备控制器API.md#ga6da3d836e868f2d09fe24854c2d76aeb)
- [USB_MPS_EP_SIZE](../usb/P172_USB标准请求与描述符常量.md#ae028a023a157a29a0e83dee304c6267a)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [device::api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [net_buf::size](../network_core_model_reference/P046_net_buf_结构体.md#a1522d81a002804223e25300a6961f527)
- [udc_api::init](../usb/P031_USB设备控制器驱动接口.md#a01f803a2d258072df102b831cf184b27)
- [udc_api::ep_dequeue](../usb/P031_USB设备控制器驱动接口.md#a023fcfa0fa251dcadcb379347fe7531a)
- [udc_api::ep_disable](../usb/P031_USB设备控制器驱动接口.md#a1af05b484e9c9d1f2a0dbfb822f09c98)
- [udc_api::lock](../usb/P031_USB设备控制器驱动接口.md#a1e3d733665cd609381e02929907c9837)
- [udc_api::ep_enable](../usb/P031_USB设备控制器驱动接口.md#a27291ab4d2acda207f6a6a2313d50793)
- [udc_api::unlock](../usb/P031_USB设备控制器驱动接口.md#a2be8523215fd255112bb03d9cd54c26b)
- [udc_api::set_address](../usb/P031_USB设备控制器驱动接口.md#a2e8b88743ab56144a199b3ad0618755f)
- [udc_api::ep_try_config](../usb/P031_USB设备控制器驱动接口.md#a775a18f5555f1c518762ff7dc016559c)
- [udc_api::disable](../usb/P031_USB设备控制器驱动接口.md#a8997bba956d264463b71aae0b1a4e3dc)
- [udc_api::ep_clear_halt](../usb/P031_USB设备控制器驱动接口.md#a923a684868721d0b7232c86eed15e121)
- [udc_api::ep_enqueue](../usb/P031_USB设备控制器驱动接口.md#aa1d3dadf63cb156ce5346712e1c65069)
- [udc_api::test_mode](../usb/P031_USB设备控制器驱动接口.md#ab06839ded48cbc671b2b915fe0010959)
- [udc_api::shutdown](../usb/P031_USB设备控制器驱动接口.md#ad7135abf78eb372730dddbba7dc6a75d)
- [udc_api::ep_set_halt](../usb/P031_USB设备控制器驱动接口.md#adf2adaea90b53999d1e98756062a2050)
- [udc_api::device_speed](../usb/P031_USB设备控制器驱动接口.md#adf2b8f76158d7bd2d3918628c8a9fc22)
- [udc_api::host_wakeup](../usb/P031_USB设备控制器驱动接口.md#aeca6c3a8a6b7af469d96bec8c9a8e5eb)
- [udc_api::enable](../usb/P031_USB设备控制器驱动接口.md#af8b916f6b8c211ad82ddcfdaa12de5ae)
- [udc_buf_info::ep](../usb/P032_USB设备控制器缓冲区信息.md#a0a1c09f587d3f6847cb7ce77514a3321)
- [udc_buf_info::owner](../usb/P032_USB设备控制器缓冲区信息.md#a33e927f23d227a4974915c65927284ec)
- [udc_buf_info::queued](../usb/P032_USB设备控制器缓冲区信息.md#a4cd2e83000a0551d126bebe89552eab9)
- [udc_buf_info::status](../usb/P032_USB设备控制器缓冲区信息.md#a84cf74496eddc4a69a47d23dcdbf753f)
- [udc_buf_info::setup](../usb/P032_USB设备控制器缓冲区信息.md#a9664e1f7cddd36dbc7d206b52da45170)
- [udc_buf_info::claimed](../usb/P032_USB设备控制器缓冲区信息.md#a9b03b6dd8418d4200733a612aac73daa)
- [udc_buf_info::data](../usb/P032_USB设备控制器缓冲区信息.md#ab500ff0bf12ecdbbd4f3cb48d0556ed2)
- [udc_buf_info::err](../usb/P032_USB设备控制器缓冲区信息.md#af1c92f1cdd6e0474a19f788140fdc573)
- [udc_buf_info::zlp](../usb/P032_USB设备控制器缓冲区信息.md#afc2d0c391aca7f68a1ae5539a1fed8a0)
- [udc_data::mutex](../usb/P033_USB设备控制器驱动数据.md#a1ba1b93af26bca4f4554a43a65ab3c2a)
- [udc_data::setup_valid](../usb/P033_USB设备控制器驱动数据.md#a2222bd71ecbb8051dfab7b6134f9a2c9)
- [udc_data::setup_pending](../usb/P033_USB设备控制器驱动数据.md#a849581d1e3692c6c585e9fb24e9bbb4f)
- [udc_data::event_cb](../usb/P033_USB设备控制器驱动数据.md#a9bb216d0c87b9ff4e2e99f0c3cfbb381)
- [udc_data::status](../usb/P033_USB设备控制器驱动数据.md#a9c1ae6e5e204b5a0ed15e92f8b3b384f)
- [udc_data::caps](../usb/P033_USB设备控制器驱动数据.md#aae68bfba2e92894851c36dd40c33c0f0)
- [udc_data::event_ctx](../usb/P033_USB设备控制器驱动数据.md#aaf98e53580a27635a7b02acbcf29ae14)
- [udc_data::priv](../usb/P033_USB设备控制器驱动数据.md#ac58682fa2f37bf2034a69cc9b6b10dfb)
- [udc_data::ep_lut](../usb/P033_USB设备控制器驱动数据.md#acc471b34bb24453377b1ae54d33fa415)
- [udc_data::setup](../usb/P033_USB设备控制器驱动数据.md#ae301e1a80165ae90d7d09dbb6463c88c)
- [udc_device_caps::out_ack](../usb/P034_USB设备控制器设备能力.md#a0adada5003bccfbd6df8329198639dc0)
- [udc_device_caps::mps0](../usb/P034_USB设备控制器设备能力.md#a63affa3fe08cbaec8351297ad9d26911)
- [udc_device_caps::can_detect_vbus](../usb/P034_USB设备控制器设备能力.md#a7aaf6ecac2904acb5560f2f90cfef8d1)
- [udc_device_caps::rwup](../usb/P034_USB设备控制器设备能力.md#aab85e74e40876040c3d2f961c36b9780)
- [udc_device_caps::hs](../usb/P034_USB设备控制器设备能力.md#aea376ff4a0c5a27c3b8f7d4416e17b5b)
- [udc_device_caps::addr_before_status](../usb/P034_USB设备控制器设备能力.md#aefef262532e3eab3baa90eb8e79f9dc8)
- [udc_ep_caps::iso](../usb/P035_USB设备控制器端点能力.md#a15ce10028e09b3af021a83dc36eba99a)
- [udc_ep_caps::in](../usb/P035_USB设备控制器端点能力.md#a3a944cda429c916b60cff3a332b970a7)
- [udc_ep_caps::mps](../usb/P035_USB设备控制器端点能力.md#a5e90d1362855dd77a1f7ef9e0cd82ef8)
- [udc_ep_caps::bulk](../usb/P035_USB设备控制器端点能力.md#a73ec7e7c7fd043065a7c59c89c6cc36e)
- [udc_ep_caps::interrupt](../usb/P035_USB设备控制器端点能力.md#a73f06f9e2af5770cab84d2adb76d42de)
- [udc_ep_caps::control](../usb/P035_USB设备控制器端点能力.md#a98afb85c03ff01ba82d55884cea0ea31)
- [udc_ep_caps::high_bandwidth](../usb/P035_USB设备控制器端点能力.md#ad556a4c17a01bb6b8355fb6b5ea9d418)
- [udc_ep_caps::out](../usb/P035_USB设备控制器端点能力.md#afc424ee2bb31c19451facc0b79bb73c7)
- [udc_ep_config::interval](../usb/P036_USB设备控制器端点配置.md#a1f2afc2d5e512229688764e1b7cd0171)
- [udc_ep_config::caps](../usb/P036_USB设备控制器端点配置.md#a706987205ac971574d1b81bf72d03248)
- [udc_ep_config::fifo](../usb/P036_USB设备控制器端点配置.md#aa62ff3f308771d51563df88439570918)
- [udc_ep_config::addr](../usb/P036_USB设备控制器端点配置.md#ac795b839cbd426d233a1f91d10d5fc7e)
- [udc_ep_config::attributes](../usb/P036_USB设备控制器端点配置.md#acbeab755d1b03da0c58f43aff5bd7d00)
- [udc_ep_config::stat](../usb/P036_USB设备控制器端点配置.md#ad42f77d1a9d65239cdb142209050e38e)
- [udc_ep_config::mps](../usb/P036_USB设备控制器端点配置.md#ae4f75e52d1c822f5d873095a761c6b48)
- [udc_ep_stat::enabled](../usb/P037_USB设备控制器端点状态.md#a250eed32f2945cb89df8033ae2781969)
- [udc_ep_stat::data1](../usb/P037_USB设备控制器端点状态.md#a2c9522c3f5e4f1a9cba90cd73092c07f)
- [udc_ep_stat::busy](../usb/P037_USB设备控制器端点状态.md#a47a7b3247c2aee78c3b58835081aed0c)
- [udc_ep_stat::halted](../usb/P037_USB设备控制器端点状态.md#a5273e8e99fb6943babcb573f10c90c76)
- [udc_event::status](../usb/P038_USB设备控制器事件结构.md#a0707d65716a4b1e6dd3132a0bb370770)
- [udc_event::type](../usb/P038_USB设备控制器事件结构.md#a3acfe5d21d16f6edfa24e9964b636434)
- [udc_event::dev](../usb/P038_USB设备控制器事件结构.md#a900404c46850d34cd7121eeedc2fce9d)
- [udc_event::buf](../usb/P038_USB设备控制器事件结构.md#ac1ff3bc9d629eb9b6c55602e7861e945)
- [udc_event::value](../usb/P038_USB设备控制器事件结构.md#ada24e0e920c39bc60a6c7fbbe54277f4)
- [usb_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/usb__buf_8h.html)
- [usb_ch9.h](../usb/P172_USB标准请求与描述符常量.md)

---

[上一章](P883_ubx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P885_uhc.h_源码浏览.md)
