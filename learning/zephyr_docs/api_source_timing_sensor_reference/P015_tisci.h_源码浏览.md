---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-15
title: tisci.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_tisci.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html)。

## 15.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00054"></a>
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
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00096"></a>
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
<a id="foldopen00132"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
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
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="foldopen00187"></a>
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
<a id="l00223"></a>
<a id="foldopen00224"></a>
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
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="l00841"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00857"></a>
<a id="l00858"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00892"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00957"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="l00973"></a>
<a id="l00974"></a>
<a id="l00975"></a>
<a id="l00986"></a>
<a id="l00987"></a>
<a id="l00998"></a>
<a id="l00999"></a>
<a id="adevice_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructtisci__irq__release__req_html"></a>
<a id="astructtisci__irq__release__req_html_a032e94a7d3c7384dc1f36c08b2d73e71"></a>
<a id="astructtisci__irq__release__req_html_a068b9b4217d606f03898bdca2219bbf0"></a>
<a id="astructtisci__irq__release__req_html_a12eb81324f28254daece1170b1e6764d"></a>
<a id="astructtisci__irq__release__req_html_a3643554ea453300f33806b5128cc6c0a"></a>
<a id="astructtisci__irq__release__req_html_a754e7c93d218a58e2bc18fd4ec086e40"></a>
<a id="astructtisci__irq__release__req_html_aa6c09862a5e955a5ccbb78c7df2675fa"></a>
<a id="astructtisci__irq__release__req_html_abb9cedc15e5923125e57f153ee1ed22a"></a>
<a id="astructtisci__irq__release__req_html_adddef8e01c4ecd9b44327418bcc8a3ef"></a>
<a id="astructtisci__irq__release__req_html_ae646b23593b5f724fca6800c5c2e76bf"></a>
<a id="astructtisci__irq__release__req_html_aedc07d5425720146b75b6757ca17c0d3"></a>
<a id="astructtisci__irq__set__req_html"></a>
<a id="astructtisci__irq__set__req_html_a1b01430d7e9140891589f0e48e79590a"></a>
<a id="astructtisci__irq__set__req_html_a290247006f410254d3a4dbcdefc0ba75"></a>
<a id="astructtisci__irq__set__req_html_a2a17ba4d83290d1ca8ae8bf39760a31a"></a>
<a id="astructtisci__irq__set__req_html_a2b8fd0bc0825d47fba8c961f68fcaef4"></a>
<a id="astructtisci__irq__set__req_html_a2e3dd0054d9d0b029a6821f4df0af4ea"></a>
<a id="astructtisci__irq__set__req_html_a94ad73384be1f64054829a32ad70b066"></a>
<a id="astructtisci__irq__set__req_html_ab5f9849aef439771e81daf6a98303d17"></a>
<a id="astructtisci__irq__set__req_html_ac5dddf4f1bc933e82eb7dfdfdfb35307"></a>
<a id="astructtisci__irq__set__req_html_ad122a8cf2af3f3df9615c3ca70ed3b06"></a>
<a id="astructtisci__irq__set__req_html_af1c6cc734902f14d51ff46c971c1a576"></a>
<a id="astructtisci__msg__fwl__owner_html"></a>
<a id="astructtisci__msg__fwl__owner_html_a2010d9ee65f9a94e5477a0fc1f21774e"></a>
<a id="astructtisci__msg__fwl__owner_html_a31ec3f0e90fdb8cea887d67004b066a7"></a>
<a id="astructtisci__msg__fwl__owner_html_a370a1aff0233b53b035cbcd7b4c264b5"></a>
<a id="astructtisci__msg__fwl__owner_html_a5e5e33a9a2f7c04022ce51fa1dcb8eef"></a>
<a id="astructtisci__msg__fwl__owner_html_a7ccaf9d3c1bd3639e8c170acd5d535a8"></a>
<a id="astructtisci__msg__fwl__region_html"></a>
<a id="astructtisci__msg__fwl__region_html_a2cb0672482a7859294a1c95b7f42d265"></a>
<a id="astructtisci__msg__fwl__region_html_a4378cc7f160a86af3708284a7cb068a6"></a>
<a id="astructtisci__msg__fwl__region_html_a4c091b340c1dc21f866d623489ab8451"></a>
<a id="astructtisci__msg__fwl__region_html_a4e5c3b596b1e60524ac386c8506c3870"></a>
<a id="astructtisci__msg__fwl__region_html_a789bcad9536d23d0cca4e8791f01c95c"></a>
<a id="astructtisci__msg__fwl__region_html_aae2b9a8670d5e799347606d48408980f"></a>
<a id="astructtisci__msg__fwl__region_html_ab3b3ae28613a3ef9e7c83b9d2af9f4ce"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_a03ec736938d7b3eb05fcd56c62fd736a"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_a459ca9cb93410be5747595a57d88c7ed"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_a4e9720567203889d41fdccb769d56025"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_a54f4136011d83df5441004dde0d5e696"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_a554db2ab8742b2f15a6c7531638a6d74"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_a57c0675af1fdefd1c270d11183fa77d6"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_a691a478fa65af24279638789433dca6f"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_a7a36a9e37b22229c6ec90528aa7f9a9c"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_a88fa4f4bf94a290a035419a65054b544"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_a8e9b939089204b70469afedcb6c5ad8c"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_a9782a0a412413087ecf669beed77ff77"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_ab1245dc9783e74cd3cb1fcb648714e76"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_abde08f01f02f26e1538cd82d9e87b19a"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_ac10643f49f4d685af2bf14bb7b9b90f0"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_ad008f77af3d4edbfeedb863ee2f8dcd0"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_ad57a6d0dca932c95cff2a4675dc72990"></a>
<a id="astructtisci__msg__rm__udmap__rx__ch__cfg_html_aecf4e3eaaa8b8c604504eb525d3e1a5f"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_a01334fae8a1e94ffbbba28d9c59ed0b1"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_a14b9ea920df0ff044bd9cf45c2084f3a"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_a37b6f2565ccdf51fcc09801a72fde7e4"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_a646845b965fee520329a118ade711f02"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_a75147fe8091db6c41050ded22c9eefa3"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_a7e0bfdb950b1b285ddc0e58282bc224b"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_a89f3ac8683240274b5bbc635e08b659f"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_a90a701c601691c79cd37192fac02d052"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_a9d298e2ae456dcad3cbfdce595f0655c"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_aaa18a6837a0271781164a353ce729623"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_ab36b40f8989fa7cdc5419bc0e9dd5a68"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_ab8327c9b3896c8294f47349572546e70"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_ab9a869848d253d09f9fafc91dc8958cc"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_acb243dd0b94ab38fa50ddd14a758b33a"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_ad255f2c020bfc237f5f22a747e68c1b8"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_ad8aec84ccd12e9f02c4cafac7eadb4a4"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_ada34a3a63d1ed339a86804f906d4dbc5"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_aeaf51ae045dbc4079c02d61f13e487ed"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_af377d65e1fb43ed7fceda8a0665605d0"></a>
<a id="astructtisci__msg__rm__udmap__tx__ch__cfg_html_afd02dd108fd620f1bc9d66fac5a3e775"></a>
<a id="astructtisci__version__info_html"></a>
<a id="astructtisci__version__info_html_a62cb5c8e86a94dbf53430d73c9f241a9"></a>
<a id="astructtisci__version__info_html_a711c9ca4b063958fcb46ad0e298caa27"></a>
<a id="astructtisci__version__info_html_a7371d69f5f0993dfd1e582c165d2ddc5"></a>
<a id="astructtisci__version__info_html_a8547f04843609b8a324ea4ecb91c17a7"></a>
<a id="atisci_8h_html_a01393f21cb5a88388ce51e36ba1843fc"></a>
<a id="atisci_8h_html_a01625817d1a222c2979443413c7d712c"></a>
<a id="atisci_8h_html_a05f871388f68d9c71620ea43bde1e3ab"></a>
<a id="atisci_8h_html_a086d96bed3d789bf303f56405a791aa6"></a>
<a id="atisci_8h_html_a0d5c1b5afc2842e38de56c64c62f17fd"></a>
<a id="atisci_8h_html_a1a441bdad9bfef9a0136f0b737c9c7aa"></a>
<a id="atisci_8h_html_a1acfab0f8fd3b1db050f97aa21d26ce3"></a>
<a id="atisci_8h_html_a20276a83e2037db6895085770353a194"></a>
<a id="atisci_8h_html_a2a1873dd1b47f7437cfd8adbea2decab"></a>
<a id="atisci_8h_html_a2e0e3e88c635a4e6399941696056b8a9"></a>
<a id="atisci_8h_html_a3181b68860761b0060048a01d71888a8"></a>
<a id="atisci_8h_html_a3551276e98c3f03ea4beb9086c3b89c3"></a>
<a id="atisci_8h_html_a3d39780a18358066ec8f187474c18f71"></a>
<a id="atisci_8h_html_a3f8128fa6c8c6f10bb7e302e6e9cfeaf"></a>
<a id="atisci_8h_html_a4011bbe29370fb581ab2dd0fcaa151db"></a>
<a id="atisci_8h_html_a4a3b7acb3098f71b2a9f85fbb318d595"></a>
<a id="atisci_8h_html_a4f4072f951c0ebbeb75e8cd2f06b6e8f"></a>
<a id="atisci_8h_html_a5217423ca42a90a472777a907864128e"></a>
<a id="atisci_8h_html_a5a7c9ff34ad1ffa87c62fef6b2ac8719"></a>
<a id="atisci_8h_html_a5c69f5f12b79a0b37a1f704624106960"></a>
<a id="atisci_8h_html_a61d3ce5732bbd5a25d5d63af5a059666"></a>
<a id="atisci_8h_html_a64b6aa840b820beed84fc9a21ffde350"></a>
<a id="atisci_8h_html_a6ad9804cf3e23246955bcab1e98aecdb"></a>
<a id="atisci_8h_html_a7f0bafa6005d46d2786db590a27add25"></a>
<a id="atisci_8h_html_a86e0ed2c8711363dc5ea710b12a303af"></a>
<a id="atisci_8h_html_a8a29455ba732efa082c1a72922f46f9e"></a>
<a id="atisci_8h_html_a8b6d6f99df32eeba9131ce130ee4f12d"></a>
<a id="atisci_8h_html_a8ced32499c14aae81994368d4450422d"></a>
<a id="atisci_8h_html_a90613df222309651abc1adb2f4d82272"></a>
<a id="atisci_8h_html_a9110e6b0fd37057ea72c64c8c2067a21"></a>
<a id="atisci_8h_html_a94f43ead8c81320f651fa9c0450a2493"></a>
<a id="atisci_8h_html_a9801b388e5dc60f10aa624040cb8bfe2"></a>
<a id="atisci_8h_html_a98a90edf1033e5146c51da785ee29581"></a>
<a id="atisci_8h_html_a9a80ade10fb08159e3fdfbd85ac8dfbf"></a>
<a id="atisci_8h_html_a9e057dd13353ccdd7df3b2263ef22940"></a>
<a id="atisci_8h_html_aa261b08c9141360c5f4f9e50ab151ed5"></a>
<a id="atisci_8h_html_aa7b6bef27ce24be4762d28499197a8bd"></a>
<a id="atisci_8h_html_aa7bb463be840666d87a68c1e65496b19"></a>
<a id="atisci_8h_html_aaa3b1c5f5072b40e2eb1c626cb6f6f29"></a>
<a id="atisci_8h_html_aab1720913f75a771e041e2195b9deede"></a>
<a id="atisci_8h_html_aaebb0012c291ded1b9303d634b1bb245"></a>
<a id="atisci_8h_html_aafb0c859914130228e6c229725f87eca"></a>
<a id="atisci_8h_html_ab63106de04e579ba18f34763b3efa8b3"></a>
<a id="atisci_8h_html_ab8203c5d0b699ec726a889e7027ae034"></a>
<a id="atisci_8h_html_ac30ac2d3539999418f8b200e7b78d259"></a>
<a id="atisci_8h_html_ac83cc7874ddc4c42c35e6a9f41e64ee7"></a>
<a id="atisci_8h_html_ad3563b7ec2fa13eb4b1faa564062ae12"></a>
<a id="atisci_8h_html_ada78c57b3cb24e57a3f6cc155e3a3d09"></a>
<a id="atisci_8h_html_adc16227f1ec150d0c6cf32442fa3e915"></a>
<a id="atisci_8h_html_ae249d114c60b6b1a76f7de8dab5c3ce1"></a>
<a id="atisci_8h_html_ae48c6c78db3f4bee6520c0af66e37e7d"></a>
<a id="atisci_8h_html_ae93fb7c70a4f2299415a51b993d36741"></a>
<a id="atisci_8h_html_aea0b9addbd3cfcb2be691f0801128fe1"></a>
<a id="atisci_8h_html_aee60c2eb75e6786b91d9dc73c7a7e2c6"></a>
<a id="atisci_8h_html_af9ff6eee5bca675c50c28fbc4af3048c"></a>
<a id="atisci_8h_html_afe30856eaa98b6f30b11ab99daf1dc91"></a>

```c
/*
 * Copyright (c) 2025, Texas Instruments
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_TISCI_TISCI_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_TISCI_TISCI_H_

#include <zephyr/device.h>

#define MAILBOX_MBOX_SIZE 60

struct tisci_version_info {
        uint8_t abi_major;
        uint8_t abi_minor;
        uint16_t firmware_revision;
        char firmware_description[32];
};

struct tisci_msg_fwl_region {
        uint16_t fwl_id;
        uint16_t region;
        uint32_t n_permission_regs;
        uint32_t control;
        uint32_t permissions[3];
        uint64_t start_address;
        uint64_t end_address;
};

struct tisci_msg_fwl_owner {
        uint16_t fwl_id;
        uint16_t region;
        uint8_t owner_index;
        uint8_t owner_privid;
        uint16_t owner_permission_bits;
};

struct tisci_msg_rm_udmap_tx_ch_cfg {
        uint32_t valid_params;
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FILT_EINFO_VALID    BIT(9)
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FILT_PSWORDS_VALID  BIT(10)
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_SUPR_TDPKT_VALID    BIT(11)
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_CREDIT_COUNT_VALID  BIT(12)
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FDEPTH_VALID        BIT(13)
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_TDTYPE_VALID        BIT(15)
#define TISCI_MSG_VALUE_RM_UDMAP_CH_EXTENDED_CH_TYPE_VALID BIT(16)
        uint16_t nav_id;
        uint16_t index;
        uint8_t tx_pause_on_err;
        uint8_t tx_filt_einfo;
        uint8_t tx_filt_pswords;
        uint8_t tx_atype;
        uint8_t tx_chan_type;
        uint8_t tx_supr_tdpkt;
        uint16_t tx_fetch_size;
        uint8_t tx_credit_count;
        uint16_t txcq_qnum;
        uint8_t tx_priority;
        uint8_t tx_qos;
        uint8_t tx_orderid;
        uint16_t fdepth;
        uint8_t tx_sched_priority;
        uint8_t tx_burst_size;
        uint8_t tx_tdtype;
        uint8_t extended_ch_type;
};

struct tisci_msg_rm_udmap_rx_ch_cfg {
        uint32_t valid_params;
#define TISCI_MSG_VALUE_RM_UDMAP_CH_RX_FLOWID_START_VALID BIT(9)
#define TISCI_MSG_VALUE_RM_UDMAP_CH_RX_FLOWID_CNT_VALID   BIT(10)
#define TISCI_MSG_VALUE_RM_UDMAP_CH_RX_IGNORE_SHORT_VALID BIT(11)
#define TISCI_MSG_VALUE_RM_UDMAP_CH_RX_IGNORE_LONG_VALID  BIT(12)
        uint16_t nav_id;
        uint16_t index;
        uint16_t rx_fetch_size;
        uint16_t rxcq_qnum;
        uint8_t rx_priority;
        uint8_t rx_qos;
        uint8_t rx_orderid;
        uint8_t rx_sched_priority;
        uint16_t flowid_start;
        uint16_t flowid_cnt;
        uint8_t rx_pause_on_err;
        uint8_t rx_atype;
        uint8_t rx_chan_type;
        uint8_t rx_ignore_short;
        uint8_t rx_ignore_long;
        uint8_t rx_burst_size;
};

#define TISCI_MSG_VALUE_RM_DST_ID_VALID                (1u << 0u)
#define TISCI_MSG_VALUE_RM_DST_HOST_IRQ_VALID          (1u << 1u)
#define TISCI_MSG_VALUE_RM_IA_ID_VALID                 (1u << 2u)
#define TISCI_MSG_VALUE_RM_VINT_VALID                  (1u << 3u)
#define TISCI_MSG_VALUE_RM_GLOBAL_EVENT_VALID          (1u << 4u)
#define TISCI_MSG_VALUE_RM_VINT_STATUS_BIT_INDEX_VALID (1u << 5u)

struct tisci_irq_set_req {
        uint32_t valid_params;
        uint16_t src_id;
        uint16_t src_index;
        uint16_t dst_id;
        uint16_t dst_host_irq;
        uint16_t ia_id;
        uint16_t vint;
        uint16_t global_event;
        uint8_t vint_status_bit_index;
        uint8_t secondary_host;
};


struct tisci_irq_release_req {
        uint32_t valid_params;
        uint16_t src_id;
        uint16_t src_index;
        uint16_t dst_id;
        uint16_t dst_host_irq;
        uint16_t ia_id;
        uint16_t vint;
        uint16_t global_event;
        uint8_t vint_status_bit_index;
        uint8_t secondary_host;
};

/* Version/Revision Functions */

int tisci_cmd_get_revision(const struct device *dev, struct tisci_version_info *ver);

/* Clock Management Functions */

int tisci_cmd_get_clock_state(const struct device *dev, uint32_t dev_id, uint8_t clk_id,
                              uint8_t *programmed_state, uint8_t *current_state);

int tisci_set_clock_state(const struct device *dev, uint32_t dev_id, uint8_t clk_id, uint32_t flags,
                          uint8_t state);

int tisci_cmd_clk_is_on(const struct device *dev, uint32_t dev_id, uint8_t clk_id, bool *req_state,
                        bool *curr_state);

int tisci_cmd_clk_is_off(const struct device *dev, uint32_t dev_id, uint8_t clk_id, bool *req_state,
                         bool *curr_state);

int tisci_cmd_clk_is_auto(const struct device *dev, uint32_t dev_id, uint8_t clk_id,
                          bool *req_state);

int tisci_cmd_clk_get_freq(const struct device *dev, uint32_t dev_id, uint8_t clk_id,
                           uint64_t *freq);

int tisci_cmd_clk_set_freq(const struct device *dev, uint32_t dev_id, uint8_t clk_id,
                           uint64_t min_freq, uint64_t target_freq, uint64_t max_freq);

int tisci_cmd_clk_get_match_freq(const struct device *dev, uint32_t dev_id, uint8_t clk_id,
                                 uint64_t min_freq, uint64_t target_freq, uint64_t max_freq,
                                 uint64_t *match_freq);

int tisci_cmd_clk_set_parent(const struct device *dev, uint32_t dev_id, uint8_t clk_id,
                             uint8_t parent_id);

int tisci_cmd_clk_get_parent(const struct device *dev, uint32_t dev_id, uint8_t clk_id,
                             uint8_t *parent_id);

int tisci_cmd_clk_get_num_parents(const struct device *dev, uint32_t dev_id, uint8_t clk_id,
                                  uint8_t *num_parents);

int tisci_cmd_get_clock(const struct device *dev, uint32_t dev_id, uint8_t clk_id, bool needs_ssc,
                        bool can_change_freq, bool enable_input_term);

int tisci_cmd_idle_clock(const struct device *dev, uint32_t dev_id, uint8_t clk_id);

int tisci_cmd_put_clock(const struct device *dev, uint32_t dev_id, uint8_t clk_id);

/* Device Management Functions */

int tisci_set_device_state(const struct device *dev, uint32_t dev_id, uint32_t flags,
                           uint8_t state);

int tisci_set_device_state_no_wait(const struct device *dev, uint32_t dev_id, uint32_t flags,
                                   uint8_t state);

int tisci_get_device_state(const struct device *dev, uint32_t dev_id, uint32_t *clcnt,
                           uint32_t *resets, uint8_t *p_state, uint8_t *c_state);

int tisci_cmd_get_device(const struct device *dev, uint32_t dev_id);
int tisci_cmd_get_device_exclusive(const struct device *dev, uint32_t dev_id);

int tisci_cmd_idle_device(const struct device *dev, uint32_t dev_id);
int tisci_cmd_idle_device_exclusive(const struct device *dev, uint32_t dev_id);

int tisci_cmd_put_device(const struct device *dev, uint32_t dev_id);

int tisci_cmd_dev_is_valid(const struct device *dev, uint32_t dev_id);

int tisci_cmd_dev_get_clcnt(const struct device *dev, uint32_t dev_id, uint32_t *count);

int tisci_cmd_dev_is_idle(const struct device *dev, uint32_t dev_id, bool *r_state);

int tisci_cmd_dev_is_stop(const struct device *dev, uint32_t dev_id, bool *r_state,
                          bool *curr_state);

int tisci_cmd_dev_is_on(const struct device *dev, uint32_t dev_id, bool *r_state, bool *curr_state);

int tisci_cmd_dev_is_trans(const struct device *dev, uint32_t dev_id, bool *curr_state);

int tisci_cmd_set_device_resets(const struct device *dev, uint32_t dev_id, uint32_t reset_state);

int tisci_cmd_get_device_resets(const struct device *dev, uint32_t dev_id, uint32_t *reset_state);

/* Resource Management Functions */

int tisci_get_resource_range(const struct device *dev, uint32_t dev_id, uint8_t subtype,
                             uint8_t s_host, uint16_t *range_start, uint16_t *range_num);

int tisci_cmd_get_resource_range(const struct device *dev, uint32_t dev_id, uint8_t subtype,
                                 uint16_t *range_start, uint16_t *range_num);

int tisci_cmd_get_resource_range_from_shost(const struct device *dev, uint32_t dev_id,
                                            uint8_t subtype, uint8_t s_host, uint16_t *range_start,
                                            uint16_t *range_num);

/* Processor Management Functions */

int tisci_cmd_proc_request(const struct device *dev, uint8_t proc_id);

int tisci_cmd_proc_release(const struct device *dev, uint8_t proc_id);

int tisci_cmd_proc_handover(const struct device *dev, uint8_t proc_id, uint8_t host_id);

int tisci_cmd_set_proc_boot_cfg(const struct device *dev, uint8_t proc_id, uint64_t bootvector,
                                uint32_t config_flags_set, uint32_t config_flags_clear);

int tisci_cmd_set_proc_boot_ctrl(const struct device *dev, uint8_t proc_id,
                                 uint32_t control_flags_set, uint32_t control_flags_clear);

int tisci_cmd_proc_auth_boot_image(const struct device *dev, uint64_t *image_addr,
                                   uint32_t *image_size);

int tisci_cmd_get_proc_boot_status(const struct device *dev, uint8_t proc_id, uint64_t *bv,
                                   uint32_t *cfg_flags, uint32_t *ctrl_flags, uint32_t *sts_flags);

int tisci_proc_wait_boot_status_no_wait(const struct device *dev, uint8_t proc_id,
                                        uint8_t num_wait_iterations, uint8_t num_match_iterations,
                                        uint8_t delay_per_iteration_us,
                                        uint8_t delay_before_iterations_us,
                                        uint32_t status_flags_1_set_all_wait,
                                        uint32_t status_flags_1_set_any_wait,
                                        uint32_t status_flags_1_clr_all_wait,
                                        uint32_t status_flags_1_clr_any_wait);

int tisci_cmd_proc_shutdown_no_wait(const struct device *dev, uint8_t proc_id);

/* Board Configuration Functions */

int cmd_set_board_config_using_msg(const struct device *dev, uint16_t msg_type, uint64_t addr,
                                   uint32_t size);

/* Ring Configuration Function */

int tisci_cmd_ring_config(const struct device *dev, uint32_t valid_params, uint16_t nav_id,
                          uint16_t index, uint32_t addr_lo, uint32_t addr_hi, uint32_t count,
                          uint8_t mode, uint8_t size, uint8_t order_id);

/* System Control Functions */

int tisci_cmd_sys_reset(const struct device *dev);

/* Memory Management Functions */

int tisci_cmd_query_msmc(const struct device *dev, uint64_t *msmc_start, uint64_t *msmc_end);

/* Firewall Management Functions */

int tisci_cmd_set_fwl_region(const struct device *dev, const struct tisci_msg_fwl_region *region);

/* INCLUDE_ZEPHYR_DRIVERS_TISCI_H_ */

/* Firewall Management Functions */
/* ... previous firewall functions ... */

int tisci_cmd_get_fwl_region(const struct device *dev, struct tisci_msg_fwl_region *region);

/* Firewall Management Functions */
/* ... previous firewall functions ... */

int tisci_cmd_change_fwl_owner(const struct device *dev, struct tisci_msg_fwl_owner *owner);

/* UDMAP Management Functions */

int tisci_cmd_rm_udmap_tx_ch_cfg(const struct device *dev,
                                 const struct tisci_msg_rm_udmap_tx_ch_cfg *params);

int tisci_cmd_rm_udmap_rx_ch_cfg(const struct device *dev,
                                 const struct tisci_msg_rm_udmap_rx_ch_cfg *params);

/* PSI-L Management Functions */

int tisci_cmd_rm_psil_pair(const struct device *dev, uint32_t nav_id, uint32_t src_thread,
                           uint32_t dst_thread);

int tisci_cmd_rm_psil_unpair(const struct device *dev, uint32_t nav_id, uint32_t src_thread,
                             uint32_t dst_thread);

int tisci_cmd_rm_irq_set(const struct device *dev, struct tisci_irq_set_req *req);

int tisci_cmd_rm_irq_release(const struct device *dev, struct tisci_irq_release_req *req);
#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_TISCI_TISCI_H_ */
```

## 15.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025, Texas Instruments。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 237 行

版本／修订版本函数（Version/Revision Functions）。

### 注释 3：原第 252 行

时钟管理函数（Clock Management Functions）。

### 注释 4：原第 446 行

设备管理函数（Device Management Functions）。

### 注释 5：原第 619 行

资源管理函数（Resource Management Functions）。

### 注释 6：原第 666 行

处理器管理函数（Processor Management Functions）。

### 注释 7：原第 790 行

开发板配置函数（Board Configuration Functions）。

### 注释 8：原第 808 行

环形队列配置函数（Ring Configuration Function）。

### 注释 9：原第 830 行

系统控制函数（System Control Functions）。

### 注释 10：原第 843 行

内存管理函数（Memory Management Functions）。

### 注释 11：原第 859 行

防火墙管理函数（Firewall Management Functions）。

### 注释 12：原第 874 行

头文件保护宏（Header guard）标记：`INCLUDE_ZEPHYR_DRIVERS_TISCI_H_`。

### 注释 13：原第 876 行

防火墙管理函数（Firewall Management Functions）。

### 注释 14：原第 877 行

……前面的防火墙函数（firewall functions）……

### 注释 15：原第 894 行

防火墙管理函数（Firewall Management Functions）。

### 注释 16：原第 895 行

……前面的防火墙函数（firewall functions）……

### 注释 17：原第 912 行

UDMAP 管理函数（Management Functions）。

### 注释 18：原第 942 行

PSI-L 管理函数（Management Functions）。

### 注释 19：原第 999 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_TISCI_TISCI_H_`。

## 15.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [tisci_version_info](../platform_security_model_reference/P072_tisci_version_info_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [abi_major](../platform_security_model_reference/P072_tisci_version_info_结构体.md#a7371d69f5f0993dfd1e582c165d2ddc5)
- [abi_minor](../platform_security_model_reference/P072_tisci_version_info_结构体.md#a8547f04843609b8a324ea4ecb91c17a7)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [firmware_revision](../platform_security_model_reference/P072_tisci_version_info_结构体.md#a711c9ca4b063958fcb46ad0e298caa27)
- [firmware_description](../platform_security_model_reference/P072_tisci_version_info_结构体.md#a62cb5c8e86a94dbf53430d73c9f241a9)
- [tisci_msg_fwl_region](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md)
- [fwl_id](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#ab3b3ae28613a3ef9e7c83b9d2af9f4ce)
- [region](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#a2cb0672482a7859294a1c95b7f42d265)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [n_permission_regs](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#aae2b9a8670d5e799347606d48408980f)
- [control](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#a4e5c3b596b1e60524ac386c8506c3870)
- [permissions](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#a4c091b340c1dc21f866d623489ab8451)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [start_address](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#a4378cc7f160a86af3708284a7cb068a6)
- [end_address](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#a789bcad9536d23d0cca4e8791f01c95c)
- [tisci_msg_fwl_owner](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md)
- [fwl_id](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md#a370a1aff0233b53b035cbcd7b4c264b5)
- [region](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md#a7ccaf9d3c1bd3639e8c170acd5d535a8)
- [owner_index](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md#a2010d9ee65f9a94e5477a0fc1f21774e)
- [owner_privid](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md#a5e5e33a9a2f7c04022ce51fa1dcb8eef)
- [owner_permission_bits](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md#a31ec3f0e90fdb8cea887d67004b066a7)
- [tisci_msg_rm_udmap_tx_ch_cfg](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md)
- [valid_params](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#acb243dd0b94ab38fa50ddd14a758b33a)
- [nav_id](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a646845b965fee520329a118ade711f02)
- [index](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#ab8327c9b3896c8294f47349572546e70)
- [tx_pause_on_err](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#ad255f2c020bfc237f5f22a747e68c1b8)
- [tx_filt_einfo](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a9d298e2ae456dcad3cbfdce595f0655c)
- [tx_filt_pswords](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#ab9a869848d253d09f9fafc91dc8958cc)
- [tx_atype](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a75147fe8091db6c41050ded22c9eefa3)
- [tx_chan_type](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a14b9ea920df0ff044bd9cf45c2084f3a)
- [tx_supr_tdpkt](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#aaa18a6837a0271781164a353ce729623)
- [tx_fetch_size](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#afd02dd108fd620f1bc9d66fac5a3e775)
- [tx_credit_count](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a90a701c601691c79cd37192fac02d052)
- [txcq_qnum](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a89f3ac8683240274b5bbc635e08b659f)
- [tx_priority](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#aeaf51ae045dbc4079c02d61f13e487ed)
- [tx_qos](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#af377d65e1fb43ed7fceda8a0665605d0)
- [tx_orderid](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#ada34a3a63d1ed339a86804f906d4dbc5)
- [fdepth](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#ad8aec84ccd12e9f02c4cafac7eadb4a4)
- [tx_sched_priority](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a01334fae8a1e94ffbbba28d9c59ed0b1)
- [tx_burst_size](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a7e0bfdb950b1b285ddc0e58282bc224b)
- [tx_tdtype](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#ab36b40f8989fa7cdc5419bc0e9dd5a68)
- [extended_ch_type](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a37b6f2565ccdf51fcc09801a72fde7e4)
- [tisci_msg_rm_udmap_rx_ch_cfg](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md)
- [valid_params](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a88fa4f4bf94a290a035419a65054b544)
- [nav_id](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a691a478fa65af24279638789433dca6f)
- [index](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a459ca9cb93410be5747595a57d88c7ed)
- [rx_fetch_size](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#ad57a6d0dca932c95cff2a4675dc72990)
- [rxcq_qnum](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a554db2ab8742b2f15a6c7531638a6d74)
- [rx_priority](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a03ec736938d7b3eb05fcd56c62fd736a)
- [rx_qos](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a54f4136011d83df5441004dde0d5e696)
- [rx_orderid](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a9782a0a412413087ecf669beed77ff77)
- [rx_sched_priority](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a4e9720567203889d41fdccb769d56025)
- [flowid_start](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#abde08f01f02f26e1538cd82d9e87b19a)
- [flowid_cnt](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#ac10643f49f4d685af2bf14bb7b9b90f0)
- [rx_pause_on_err](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#ad008f77af3d4edbfeedb863ee2f8dcd0)
- [rx_atype](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a7a36a9e37b22229c6ec90528aa7f9a9c)
- [rx_chan_type](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#aecf4e3eaaa8b8c604504eb525d3e1a5f)
- [rx_ignore_short](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#ab1245dc9783e74cd3cb1fcb648714e76)
- [rx_ignore_long](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a8e9b939089204b70469afedcb6c5ad8c)
- [rx_burst_size](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a57c0675af1fdefd1c270d11183fa77d6)
- [tisci_irq_set_req](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md)
- [valid_params](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#ac5dddf4f1bc933e82eb7dfdfdfb35307)
- [src_id](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#af1c6cc734902f14d51ff46c971c1a576)
- [src_index](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#a290247006f410254d3a4dbcdefc0ba75)
- [dst_id](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#a2a17ba4d83290d1ca8ae8bf39760a31a)
- [dst_host_irq](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#a1b01430d7e9140891589f0e48e79590a)
- [ia_id](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#a2b8fd0bc0825d47fba8c961f68fcaef4)
- [vint](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#a2e3dd0054d9d0b029a6821f4df0af4ea)
- [global_event](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#ab5f9849aef439771e81daf6a98303d17)
- [vint_status_bit_index](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#a94ad73384be1f64054829a32ad70b066)
- [secondary_host](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#ad122a8cf2af3f3df9615c3ca70ed3b06)
- [tisci_irq_release_req](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md)
- [valid_params](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#a068b9b4217d606f03898bdca2219bbf0)
- [src_id](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#adddef8e01c4ecd9b44327418bcc8a3ef)
- [src_index](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#abb9cedc15e5923125e57f153ee1ed22a)
- [dst_id](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#ae646b23593b5f724fca6800c5c2e76bf)
- [dst_host_irq](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#a3643554ea453300f33806b5128cc6c0a)
- [ia_id](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#aa6c09862a5e955a5ccbb78c7df2675fa)
- [vint](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#a754e7c93d218a58e2bc18fd4ec086e40)
- [global_event](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#a12eb81324f28254daece1170b1e6764d)
- [vint_status_bit_index](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#aedc07d5425720146b75b6757ca17c0d3)
- [secondary_host](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#a032e94a7d3c7384dc1f36c08b2d73e71)
- [tisci_cmd_get_revision](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#aea0b9addbd3cfcb2be691f0801128fe1)
- [device](../device_reference/P002_设备对象结构.md)
- [tisci_cmd_get_clock_state](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a3f8128fa6c8c6f10bb7e302e6e9cfeaf)
- [tisci_set_clock_state](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a086d96bed3d789bf303f56405a791aa6)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [tisci_cmd_clk_is_on](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a7f0bafa6005d46d2786db590a27add25)
- [tisci_cmd_clk_is_off](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a20276a83e2037db6895085770353a194)
- [tisci_cmd_clk_is_auto](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#aaebb0012c291ded1b9303d634b1bb245)
- [tisci_cmd_clk_get_freq](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a5c69f5f12b79a0b37a1f704624106960)
- [tisci_cmd_clk_set_freq](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#ad3563b7ec2fa13eb4b1faa564062ae12)
- [tisci_cmd_clk_get_match_freq](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a9801b388e5dc60f10aa624040cb8bfe2)
- [tisci_cmd_clk_set_parent](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a6ad9804cf3e23246955bcab1e98aecdb)
- [tisci_cmd_clk_get_parent](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a86e0ed2c8711363dc5ea710b12a303af)
- [tisci_cmd_clk_get_num_parents](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#ae93fb7c70a4f2299415a51b993d36741)
- [tisci_cmd_get_clock](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#ab63106de04e579ba18f34763b3efa8b3)
- [tisci_cmd_idle_clock](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a3d39780a18358066ec8f187474c18f71)
- [tisci_cmd_put_clock](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#ae48c6c78db3f4bee6520c0af66e37e7d)
- [tisci_set_device_state](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a8b6d6f99df32eeba9131ce130ee4f12d)
- [tisci_set_device_state_no_wait](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a05f871388f68d9c71620ea43bde1e3ab)
- [tisci_get_device_state](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#ada78c57b3cb24e57a3f6cc155e3a3d09)
- [tisci_cmd_get_device](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a4011bbe29370fb581ab2dd0fcaa151db)
- [tisci_cmd_get_device_exclusive](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#adc16227f1ec150d0c6cf32442fa3e915)
- [tisci_cmd_idle_device](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#ab8203c5d0b699ec726a889e7027ae034)
- [tisci_cmd_idle_device_exclusive](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#aab1720913f75a771e041e2195b9deede)
- [tisci_cmd_put_device](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a5a7c9ff34ad1ffa87c62fef6b2ac8719)
- [tisci_cmd_dev_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a4f4072f951c0ebbeb75e8cd2f06b6e8f)
- [tisci_cmd_dev_get_clcnt](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a01393f21cb5a88388ce51e36ba1843fc)
- [tisci_cmd_dev_is_idle](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#af9ff6eee5bca675c50c28fbc4af3048c)
- [tisci_cmd_dev_is_stop](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a1a441bdad9bfef9a0136f0b737c9c7aa)
- [tisci_cmd_dev_is_on](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#aa7bb463be840666d87a68c1e65496b19)
- [tisci_cmd_dev_is_trans](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a4a3b7acb3098f71b2a9f85fbb318d595)
- [tisci_cmd_set_device_resets](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a94f43ead8c81320f651fa9c0450a2493)
- [tisci_cmd_get_device_resets](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a90613df222309651abc1adb2f4d82272)
- [tisci_get_resource_range](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a8ced32499c14aae81994368d4450422d)
- [tisci_cmd_get_resource_range](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#ae249d114c60b6b1a76f7de8dab5c3ce1)
- [tisci_cmd_get_resource_range_from_shost](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#aa261b08c9141360c5f4f9e50ab151ed5)
- [tisci_cmd_proc_request](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a3181b68860761b0060048a01d71888a8)
- [tisci_cmd_proc_release](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a2e0e3e88c635a4e6399941696056b8a9)
- [tisci_cmd_proc_handover](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a1acfab0f8fd3b1db050f97aa21d26ce3)
- [tisci_cmd_set_proc_boot_cfg](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a3551276e98c3f03ea4beb9086c3b89c3)
- [tisci_cmd_set_proc_boot_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#aee60c2eb75e6786b91d9dc73c7a7e2c6)
- [tisci_cmd_proc_auth_boot_image](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#aaa3b1c5f5072b40e2eb1c626cb6f6f29)
- [tisci_cmd_get_proc_boot_status](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a9e057dd13353ccdd7df3b2263ef22940)
- [tisci_proc_wait_boot_status_no_wait](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a8a29455ba732efa082c1a72922f46f9e)
- [tisci_cmd_proc_shutdown_no_wait](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a9a80ade10fb08159e3fdfbd85ac8dfbf)
- [cmd_set_board_config_using_msg](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#ac83cc7874ddc4c42c35e6a9f41e64ee7)
- [tisci_cmd_ring_config](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a9110e6b0fd37057ea72c64c8c2067a21)
- [tisci_cmd_sys_reset](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#aa7b6bef27ce24be4762d28499197a8bd)
- [tisci_cmd_query_msmc](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a01625817d1a222c2979443413c7d712c)
- [tisci_cmd_set_fwl_region](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a2a1873dd1b47f7437cfd8adbea2decab)
- [tisci_cmd_get_fwl_region](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#aafb0c859914130228e6c229725f87eca)
- [tisci_cmd_change_fwl_owner](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#afe30856eaa98b6f30b11ab99daf1dc91)
- [tisci_cmd_rm_udmap_tx_ch_cfg](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a98a90edf1033e5146c51da785ee29581)
- [tisci_cmd_rm_udmap_rx_ch_cfg](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a5217423ca42a90a472777a907864128e)
- [tisci_cmd_rm_psil_pair](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a64b6aa840b820beed84fc9a21ffde350)
- [tisci_cmd_rm_psil_unpair](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a61d3ce5732bbd5a25d5d63af5a059666)
- [tisci_cmd_rm_irq_set](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#a0d5c1b5afc2842e38de56c64c62f17fd)
- [tisci_cmd_rm_irq_release](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html#ac30ac2d3539999418f8b200e7b78d259)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [tisci_irq_release_req::secondary_host](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#a032e94a7d3c7384dc1f36c08b2d73e71)
- [tisci_irq_release_req::valid_params](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#a068b9b4217d606f03898bdca2219bbf0)
- [tisci_irq_release_req::global_event](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#a12eb81324f28254daece1170b1e6764d)
- [tisci_irq_release_req::dst_host_irq](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#a3643554ea453300f33806b5128cc6c0a)
- [tisci_irq_release_req::vint](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#a754e7c93d218a58e2bc18fd4ec086e40)
- [tisci_irq_release_req::ia_id](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#aa6c09862a5e955a5ccbb78c7df2675fa)
- [tisci_irq_release_req::src_index](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#abb9cedc15e5923125e57f153ee1ed22a)
- [tisci_irq_release_req::src_id](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#adddef8e01c4ecd9b44327418bcc8a3ef)
- [tisci_irq_release_req::dst_id](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#ae646b23593b5f724fca6800c5c2e76bf)
- [tisci_irq_release_req::vint_status_bit_index](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md#aedc07d5425720146b75b6757ca17c0d3)
- [tisci_irq_set_req::dst_host_irq](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#a1b01430d7e9140891589f0e48e79590a)
- [tisci_irq_set_req::src_index](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#a290247006f410254d3a4dbcdefc0ba75)
- [tisci_irq_set_req::dst_id](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#a2a17ba4d83290d1ca8ae8bf39760a31a)
- [tisci_irq_set_req::ia_id](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#a2b8fd0bc0825d47fba8c961f68fcaef4)
- [tisci_irq_set_req::vint](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#a2e3dd0054d9d0b029a6821f4df0af4ea)
- [tisci_irq_set_req::vint_status_bit_index](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#a94ad73384be1f64054829a32ad70b066)
- [tisci_irq_set_req::global_event](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#ab5f9849aef439771e81daf6a98303d17)
- [tisci_irq_set_req::valid_params](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#ac5dddf4f1bc933e82eb7dfdfdfb35307)
- [tisci_irq_set_req::secondary_host](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#ad122a8cf2af3f3df9615c3ca70ed3b06)
- [tisci_irq_set_req::src_id](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md#af1c6cc734902f14d51ff46c971c1a576)
- [tisci_msg_fwl_owner::owner_index](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md#a2010d9ee65f9a94e5477a0fc1f21774e)
- [tisci_msg_fwl_owner::owner_permission_bits](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md#a31ec3f0e90fdb8cea887d67004b066a7)
- [tisci_msg_fwl_owner::fwl_id](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md#a370a1aff0233b53b035cbcd7b4c264b5)
- [tisci_msg_fwl_owner::owner_privid](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md#a5e5e33a9a2f7c04022ce51fa1dcb8eef)
- [tisci_msg_fwl_owner::region](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md#a7ccaf9d3c1bd3639e8c170acd5d535a8)
- [tisci_msg_fwl_region::region](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#a2cb0672482a7859294a1c95b7f42d265)
- [tisci_msg_fwl_region::start_address](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#a4378cc7f160a86af3708284a7cb068a6)
- [tisci_msg_fwl_region::permissions](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#a4c091b340c1dc21f866d623489ab8451)
- [tisci_msg_fwl_region::control](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#a4e5c3b596b1e60524ac386c8506c3870)
- [tisci_msg_fwl_region::end_address](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#a789bcad9536d23d0cca4e8791f01c95c)
- [tisci_msg_fwl_region::n_permission_regs](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#aae2b9a8670d5e799347606d48408980f)
- [tisci_msg_fwl_region::fwl_id](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md#ab3b3ae28613a3ef9e7c83b9d2af9f4ce)
- [tisci_msg_rm_udmap_rx_ch_cfg::rx_priority](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a03ec736938d7b3eb05fcd56c62fd736a)
- [tisci_msg_rm_udmap_rx_ch_cfg::index](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a459ca9cb93410be5747595a57d88c7ed)
- [tisci_msg_rm_udmap_rx_ch_cfg::rx_sched_priority](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a4e9720567203889d41fdccb769d56025)
- [tisci_msg_rm_udmap_rx_ch_cfg::rx_qos](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a54f4136011d83df5441004dde0d5e696)
- [tisci_msg_rm_udmap_rx_ch_cfg::rxcq_qnum](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a554db2ab8742b2f15a6c7531638a6d74)
- [tisci_msg_rm_udmap_rx_ch_cfg::rx_burst_size](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a57c0675af1fdefd1c270d11183fa77d6)
- [tisci_msg_rm_udmap_rx_ch_cfg::nav_id](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a691a478fa65af24279638789433dca6f)
- [tisci_msg_rm_udmap_rx_ch_cfg::rx_atype](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a7a36a9e37b22229c6ec90528aa7f9a9c)
- [tisci_msg_rm_udmap_rx_ch_cfg::valid_params](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a88fa4f4bf94a290a035419a65054b544)
- [tisci_msg_rm_udmap_rx_ch_cfg::rx_ignore_long](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a8e9b939089204b70469afedcb6c5ad8c)
- [tisci_msg_rm_udmap_rx_ch_cfg::rx_orderid](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#a9782a0a412413087ecf669beed77ff77)
- [tisci_msg_rm_udmap_rx_ch_cfg::rx_ignore_short](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#ab1245dc9783e74cd3cb1fcb648714e76)
- [tisci_msg_rm_udmap_rx_ch_cfg::flowid_start](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#abde08f01f02f26e1538cd82d9e87b19a)
- [tisci_msg_rm_udmap_rx_ch_cfg::flowid_cnt](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#ac10643f49f4d685af2bf14bb7b9b90f0)
- [tisci_msg_rm_udmap_rx_ch_cfg::rx_pause_on_err](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#ad008f77af3d4edbfeedb863ee2f8dcd0)
- [tisci_msg_rm_udmap_rx_ch_cfg::rx_fetch_size](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#ad57a6d0dca932c95cff2a4675dc72990)
- [tisci_msg_rm_udmap_rx_ch_cfg::rx_chan_type](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md#aecf4e3eaaa8b8c604504eb525d3e1a5f)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_sched_priority](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a01334fae8a1e94ffbbba28d9c59ed0b1)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_chan_type](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a14b9ea920df0ff044bd9cf45c2084f3a)
- [tisci_msg_rm_udmap_tx_ch_cfg::extended_ch_type](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a37b6f2565ccdf51fcc09801a72fde7e4)
- [tisci_msg_rm_udmap_tx_ch_cfg::nav_id](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a646845b965fee520329a118ade711f02)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_atype](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a75147fe8091db6c41050ded22c9eefa3)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_burst_size](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a7e0bfdb950b1b285ddc0e58282bc224b)
- [tisci_msg_rm_udmap_tx_ch_cfg::txcq_qnum](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a89f3ac8683240274b5bbc635e08b659f)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_credit_count](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a90a701c601691c79cd37192fac02d052)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_filt_einfo](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#a9d298e2ae456dcad3cbfdce595f0655c)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_supr_tdpkt](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#aaa18a6837a0271781164a353ce729623)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_tdtype](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#ab36b40f8989fa7cdc5419bc0e9dd5a68)
- [tisci_msg_rm_udmap_tx_ch_cfg::index](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#ab8327c9b3896c8294f47349572546e70)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_filt_pswords](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#ab9a869848d253d09f9fafc91dc8958cc)
- [tisci_msg_rm_udmap_tx_ch_cfg::valid_params](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#acb243dd0b94ab38fa50ddd14a758b33a)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_pause_on_err](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#ad255f2c020bfc237f5f22a747e68c1b8)
- [tisci_msg_rm_udmap_tx_ch_cfg::fdepth](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#ad8aec84ccd12e9f02c4cafac7eadb4a4)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_orderid](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#ada34a3a63d1ed339a86804f906d4dbc5)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_priority](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#aeaf51ae045dbc4079c02d61f13e487ed)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_qos](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#af377d65e1fb43ed7fceda8a0665605d0)
- [tisci_msg_rm_udmap_tx_ch_cfg::tx_fetch_size](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md#afd02dd108fd620f1bc9d66fac5a3e775)
- [tisci_version_info::firmware_description](../platform_security_model_reference/P072_tisci_version_info_结构体.md#a62cb5c8e86a94dbf53430d73c9f241a9)
- [tisci_version_info::firmware_revision](../platform_security_model_reference/P072_tisci_version_info_结构体.md#a711c9ca4b063958fcb46ad0e298caa27)
- [tisci_version_info::abi_major](../platform_security_model_reference/P072_tisci_version_info_结构体.md#a7371d69f5f0993dfd1e582c165d2ddc5)
- [tisci_version_info::abi_minor](../platform_security_model_reference/P072_tisci_version_info_结构体.md#a8547f04843609b8a324ea4ecb91c17a7)

---

[上一章](P014_timestamp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P016_uart_async_rx.h_源码浏览.md)
