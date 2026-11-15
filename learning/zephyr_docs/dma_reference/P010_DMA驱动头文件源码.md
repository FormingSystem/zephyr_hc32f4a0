---
id: learning.zephyr-docs.dma-reference.page-10
title: DMA驱动头文件源码
kind: reference
status: maintained
domains: [zephyr, dma, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2dma_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_DMA驱动头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2dma_8h_source.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。原网页省略了用于生成接口文档的部分注释，因此原行号会跳跃；这里的“全部可见代码”不等于包含所有文档注释的原始文件。接口说明、参数与返回值见[对应头文件参考](P009_DMA驱动头文件参考.md)及[本册大纲](大纲.md)。

## 10.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00031"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
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
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00144"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="foldopen00201"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00224"></a>
<a id="l00231"></a>
<a id="l00238"></a>
<a id="l00245"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="foldopen00281"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="foldopen00303"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00319"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="foldopen00407"></a>
<a id="l00407"></a>
<a id="l00409"></a>
<a id="l00411"></a>
<a id="l00413"></a>
<a id="l00415"></a>
<a id="l00417"></a>
<a id="l00419"></a>
<a id="l00421"></a>
<a id="l00423"></a>
<a id="l00425"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="foldopen00446"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="foldopen00468"></a>
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
<a id="l00479"></a>
<a id="l00480"></a>
<a id="foldopen00499"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="foldopen00523"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="foldopen00548"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="foldopen00573"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="foldopen00598"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
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
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="foldopen00668"></a>
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
<a id="foldopen00694"></a>
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
<a id="l00704"></a>
<a id="l00705"></a>
<a id="foldopen00722"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="foldopen00746"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00751"></a>
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
<a id="foldopen00775"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00781"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="affs_8h_html_a088db7d02e8f1fc559cbe1ec048494e8"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__atomic__apis_html_ga1c1693d524c49d11fd32b323a39d718e"></a>
<a id="agroup__atomic__apis_html_ga7ff45e13aa5f8be5d7a550e49f5c720b"></a>
<a id="agroup__dma__interface__backend_html_ga035b4982cae52df4ce1911ad007d3a64"></a>
<a id="agroup__dma__interface__backend_html_ga06781c37590c23e6df82471aac4923dc"></a>
<a id="agroup__dma__interface__backend_html_ga1c65fe109d52e477f3bafa56e4afefb7"></a>
<a id="agroup__dma__interface__backend_html_ga1cd1fc992eb0e95690a50e2696247da0"></a>
<a id="agroup__dma__interface__backend_html_ga2cc72d829ce7f47eb2a326faaedf3fc5"></a>
<a id="agroup__dma__interface__backend_html_ga5073bb15b75cbbbcdbd3f859f28e3473"></a>
<a id="agroup__dma__interface__backend_html_gab00e7199fa8dafa541e4ef5f63c391b4"></a>
<a id="agroup__dma__interface__backend_html_gab15e273c0f3b1978d17ad448d98f56bb"></a>
<a id="agroup__dma__interface__backend_html_gad3742f6c4218b6a648e9aa5734516818"></a>
<a id="agroup__dma__interface__backend_html_gad63e7dc2e41adc03f4a338bda760f2ff"></a>
<a id="agroup__dma__interface_html_ga08c366c8d47672eeeb37b258af20101b"></a>
<a id="agroup__dma__interface_html_ga1b1eeef68f1aa4818c9baf95b83b9e1e"></a>
<a id="agroup__dma__interface_html_ga2cae500f1f9ed42ad338a40ec8655544"></a>
<a id="agroup__dma__interface_html_ga55bd5d550349c11c63ef47c2ed861f36"></a>
<a id="agroup__dma__interface_html_ga641f3fa492bfb17cf9f0a0361d429257"></a>
<a id="agroup__dma__interface_html_ga6d4c3e63bc4382215774e86893bc3072"></a>
<a id="agroup__dma__interface_html_ga6df1a6b89f271a0eae01c17b748bd2df"></a>
<a id="agroup__dma__interface_html_ga93b49d4d0910ceed88fa8aaa22b73098"></a>
<a id="agroup__dma__interface_html_ga94745b4472ee1addd4f82db4e59e9fb5"></a>
<a id="agroup__dma__interface_html_ga97bf9807b7fde7671a378333f01463d6"></a>
<a id="agroup__dma__interface_html_gaac27f2ee664671884087ee3d2a2863ce"></a>
<a id="agroup__dma__interface_html_gaadc34e0ea92d9fd2f1242789367b1dd5"></a>
<a id="agroup__dma__interface_html_gadd1724a843bba4ccc1c65c9fb9d3d921"></a>
<a id="agroup__dma__interface_html_gade594552920aabbfd2106059a338498b"></a>
<a id="agroup__dma__interface_html_gae28ba5114dc2e9ecb89ccf9b623e938f"></a>
<a id="agroup__dma__interface_html_gae442d8ba73be7e53b68165647b0ea402"></a>
<a id="agroup__dma__interface_html_gaf1184de07811702ffe89737b79e4a338"></a>
<a id="agroup__dma__interface_html_gafd602ee8386e10bb9ac7d386b3dc6a83"></a>
<a id="agroup__dma__interface_html_gafe0877ef4bd7790a4bcd46052088231c"></a>
<a id="agroup__dma__interface_html_gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f"></a>
<a id="agroup__dma__interface_html_gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b"></a>
<a id="agroup__dma__interface_html_gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873"></a>
<a id="agroup__dma__interface_html_gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18"></a>
<a id="agroup__dma__interface_html_ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f"></a>
<a id="agroup__dma__interface_html_ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c"></a>
<a id="agroup__dma__interface_html_ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037"></a>
<a id="agroup__dma__interface_html_ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a"></a>
<a id="agroup__dma__interface_html_ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5"></a>
<a id="agroup__dma__interface_html_ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165"></a>
<a id="agroup__dma__interface_html_ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60"></a>
<a id="agroup__dma__interface_html_ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c"></a>
<a id="agroup__dma__interface_html_ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02"></a>
<a id="agroup__dma__interface_html_ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449"></a>
<a id="agroup__dma__interface_html_ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a"></a>
<a id="agroup__dma__interface_html_ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717"></a>
<a id="agroup__dma__interface_html_ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e"></a>
<a id="agroup__dma__interface_html_ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f"></a>
<a id="agroup__sys-util_html_gadfe7046eb6c39bb3c84c18d8ac7a230e"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="akernel_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructdma__block__config_html"></a>
<a id="astructdma__block__config_html_a18bafb80538bca9c12197955770b6511"></a>
<a id="astructdma__block__config_html_a3180ef98f007ad9be7f6ff363dc125c3"></a>
<a id="astructdma__block__config_html_a3fdab19df16d5e96054aabffbf27fcc1"></a>
<a id="astructdma__block__config_html_a4f8f5b65002f65eaacdd3dde26c47170"></a>
<a id="astructdma__block__config_html_a778935d5b806002b902b72304b845ea0"></a>
<a id="astructdma__block__config_html_a7dedf429f44f3af6fcc0db125d6494c8"></a>
<a id="astructdma__block__config_html_a877a30b62fd8e0e1773890a10c8a2751"></a>
<a id="astructdma__block__config_html_a8ffcde07d02317b3cc1b327bd0b88395"></a>
<a id="astructdma__block__config_html_a9110f948520186aa5718f57b4bbbd24a"></a>
<a id="astructdma__block__config_html_a937168582c7473fe1b2b696cd1433605"></a>
<a id="astructdma__block__config_html_a9a66e0a647c55e94423ababf44c04325"></a>
<a id="astructdma__block__config_html_a9fbd1deae8936a806ecc79bad3f3b9bb"></a>
<a id="astructdma__block__config_html_abbac399f6c6e18ad2ed25359ebb799ef"></a>
<a id="astructdma__block__config_html_ad69502226d2c60adbdb9fe5e93dc0a05"></a>
<a id="astructdma__block__config_html_ae38027f6262c34d9f1abe4f923d904b4"></a>
<a id="astructdma__block__config_html_aecf6805b898a70922c58d15127bafc92"></a>
<a id="astructdma__config_html"></a>
<a id="astructdma__config_html_a0e2da7a8f4439ceb3f2acf02e4681396"></a>
<a id="astructdma__config_html_a284d96c59945aaa851d235802aee979a"></a>
<a id="astructdma__config_html_a2927e31730c6ca2f5ac8db38c255d9f7"></a>
<a id="astructdma__config_html_a39526177f03017d245651b4f51820161"></a>
<a id="astructdma__config_html_a416a0ef20318fe77d7e383caeee67e94"></a>
<a id="astructdma__config_html_a510eed1cadbf411c9e94e1d1fb43d39d"></a>
<a id="astructdma__config_html_a69110abc43227bd7df217c4e25bb964b"></a>
<a id="astructdma__config_html_a7c77afc1f546efda6ce22f50560b8840"></a>
<a id="astructdma__config_html_a8a304fdada9ec7fc87402449e1410486"></a>
<a id="astructdma__config_html_a8e6c5cab5ec030066a3e57e0507fbf9f"></a>
<a id="astructdma__config_html_aaf903b1badff8b0fc4ef18a34c2773d7"></a>
<a id="astructdma__config_html_ac9144783b4843182451b440d97ecd273"></a>
<a id="astructdma__config_html_aca47b00f817e55bf662fdd6767a59ed0"></a>
<a id="astructdma__config_html_aca6a1cb9b580a61bf91490fecf10cb16"></a>
<a id="astructdma__config_html_ace2dc918fcfea264a579b1084fcb7fe5"></a>
<a id="astructdma__config_html_ad750b724bab1503ded7c163d8228aa80"></a>
<a id="astructdma__config_html_adb776a4940c71b61cab60eb05159b2d4"></a>
<a id="astructdma__config_html_adfa9efbfbef3ed41b2f8dd5b9c441e08"></a>
<a id="astructdma__config_html_af570b4050200ec510df323bd31558233"></a>
<a id="astructdma__config_html_afa70dbf1ee7bb5fb6a771f634783b7a2"></a>
<a id="astructdma__context_html"></a>
<a id="astructdma__context_html_a25355c8cc60df536c9a37cdef52aa653"></a>
<a id="astructdma__context_html_a5b5776088155c9f19488d479924bec8e"></a>
<a id="astructdma__context_html_ac6685cf14ca69c7b77160e5031c0a800"></a>
<a id="astructdma__driver__api_html"></a>
<a id="astructdma__driver__api_html_a0a2ca7aae0cf9bc65d34c2332c646296"></a>
<a id="astructdma__driver__api_html_a282e408e1fee4f63dea11a8b10e43986"></a>
<a id="astructdma__driver__api_html_a2daa5d977f3d62b910bcd188d9fe535c"></a>
<a id="astructdma__driver__api_html_a56d9d2f5dfe9638691c43dd2e8a9a84d"></a>
<a id="astructdma__driver__api_html_a5fb4a9ee5dbffb3d71a5bc1b81c5728b"></a>
<a id="astructdma__driver__api_html_a6c5e9147e23ab14ff00c35da101ab5c3"></a>
<a id="astructdma__driver__api_html_a812b5d3118965c0387f362de31b6debb"></a>
<a id="astructdma__driver__api_html_ac526f6bca144e3fa4366b232cd694a1c"></a>
<a id="astructdma__driver__api_html_ad51378a0d3e4f74ecb9c56e85984aec2"></a>
<a id="astructdma__driver__api_html_aebc286d4576223b1d1873d5b0ebe225e"></a>
<a id="astructdma__status_html"></a>
<a id="astructdma__status_html_a2b481bf13de03e49146eb6a26563776e"></a>
<a id="astructdma__status_html_a3a33f92b1d100f988fca2bea0a6deb24"></a>
<a id="astructdma__status_html_a92ec05d9207caa828064661897f2f31c"></a>
<a id="astructdma__status_html_a9f743c98e6343d55eccc27e528b79b1a"></a>
<a id="astructdma__status_html_aa7288b85f41098e59ad4f96dcea4ccde"></a>
<a id="astructdma__status_html_aacfe94ad8e60ea77bca2423bd9bf8409"></a>
<a id="astructdma__status_html_afa401acfb26cd26b73e4a52066989847"></a>
<a id="astructstat_html"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_DMA_H_
#define ZEPHYR_INCLUDE_DRIVERS_DMA_H_

#include <zephyr/kernel.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


enum dma_channel_direction {
        MEMORY_TO_MEMORY = 0x0,
        MEMORY_TO_PERIPHERAL,
        PERIPHERAL_TO_MEMORY,
        PERIPHERAL_TO_PERIPHERAL,
        HOST_TO_MEMORY,
        MEMORY_TO_HOST,

        DMA_CHANNEL_DIRECTION_COMMON_COUNT,

        DMA_CHANNEL_DIRECTION_PRIV_START = DMA_CHANNEL_DIRECTION_COMMON_COUNT,

        DMA_CHANNEL_DIRECTION_MAX = 0x7
};

enum dma_addr_adj {
        DMA_ADDR_ADJ_INCREMENT,
        DMA_ADDR_ADJ_DECREMENT,
        DMA_ADDR_ADJ_NO_CHANGE,
};

enum dma_channel_filter {
        DMA_CHANNEL_NORMAL,
        DMA_CHANNEL_PERIODIC,
};

enum dma_attribute_type {
        DMA_ATTR_BUFFER_ADDRESS_ALIGNMENT,
        DMA_ATTR_BUFFER_SIZE_ALIGNMENT,
        DMA_ATTR_COPY_ALIGNMENT,
        DMA_ATTR_MAX_BLOCK_COUNT,
};

struct dma_block_config {
#ifdef CONFIG_DMA_64BIT
        uint64_t source_address;
        uint64_t dest_address;
#else
        uint32_t source_address;
        uint32_t dest_address;
#endif
        uint32_t source_gather_interval;
        uint32_t dest_scatter_interval;
        uint16_t dest_scatter_count;
        uint16_t source_gather_count;
        uint32_t block_size;
        struct dma_block_config *next_block;
        uint16_t  source_gather_en :  1;
        uint16_t  dest_scatter_en :   1;
        uint16_t  source_addr_adj :   2;
        uint16_t  dest_addr_adj :     2;
        uint16_t  source_reload_en :  1;
        uint16_t  dest_reload_en :    1;
        uint16_t  fifo_mode_control : 4;
        uint16_t  flow_control_mode : 1;

        uint16_t  _reserved :          3;
};

#define DMA_STATUS_COMPLETE                     0
#define DMA_STATUS_BLOCK                        1
#define DMA_STATUS_HALF_COMPLETE        2

typedef void (*dma_callback_t)(const struct device *dev, void *user_data,
                               uint32_t channel, int status);

struct dma_config {
        uint32_t  dma_slot :             8;
        uint32_t  channel_direction :    3;
        uint32_t  half_complete_callback_en : 1;
        uint32_t  complete_callback_en : 1;
        uint32_t  error_callback_dis :    1;
        uint32_t  source_handshake :     1;
        uint32_t  dest_handshake :       1;
        uint32_t  channel_priority :     4;
        uint32_t  source_chaining_en :   1;
        uint32_t  dest_chaining_en :     1;
        uint32_t  linked_channel   :     7;
        uint32_t  cyclic :                               1;

        uint32_t  _reserved :             2;
        uint32_t  source_data_size :    16;
        uint32_t  dest_data_size :      16;
        uint32_t  source_burst_length : 16;
        uint32_t  dest_burst_length :   16;
        uint32_t block_count;
        struct dma_block_config *head_block;
        void *user_data;
        dma_callback_t dma_callback;
};

struct dma_status {
        bool busy;
        enum dma_channel_direction dir;
        uint32_t pending_length;
        uint32_t free;
        uint32_t write_position;
        uint32_t read_position;
        uint64_t total_copied;
};

struct dma_context {
        int32_t magic;
        int dma_channels;
        atomic_t *atomic;
};

#define DMA_MAGIC 0x47494749


typedef int (*dma_api_config)(const struct device *dev, uint32_t channel,
                              struct dma_config *config);

#ifdef CONFIG_DMA_64BIT
typedef int (*dma_api_reload)(const struct device *dev, uint32_t channel,
                              uint64_t src, uint64_t dst, size_t size);
#else
typedef int (*dma_api_reload)(const struct device *dev, uint32_t channel,
                              uint32_t src, uint32_t dst, size_t size);
#endif

typedef int (*dma_api_start)(const struct device *dev, uint32_t channel);

typedef int (*dma_api_stop)(const struct device *dev, uint32_t channel);

typedef int (*dma_api_suspend)(const struct device *dev, uint32_t channel);

typedef int (*dma_api_resume)(const struct device *dev, uint32_t channel);

typedef int (*dma_api_get_status)(const struct device *dev, uint32_t channel,
                                  struct dma_status *status);

typedef int (*dma_api_get_attribute)(const struct device *dev, uint32_t type, uint32_t *value);

typedef bool (*dma_api_chan_filter)(const struct device *dev,
                                int channel, void *filter_param);

typedef void (*dma_api_chan_release)(const struct device *dev,
                                     uint32_t channel);

__subsystem struct dma_driver_api {
        dma_api_config config;
        dma_api_reload reload;
        dma_api_start start;
        dma_api_stop stop;
        dma_api_suspend suspend;
        dma_api_resume resume;
        dma_api_get_status get_status;
        dma_api_get_attribute get_attribute;
        dma_api_chan_filter chan_filter;
        dma_api_chan_release chan_release;
};


static inline int dma_config(const struct device *dev, uint32_t channel,
                             struct dma_config *config)
{
        return DEVICE_API_GET(dma, dev)->config(dev, channel, config);
}

#ifdef CONFIG_DMA_64BIT
static inline int dma_reload(const struct device *dev, uint32_t channel,
                             uint64_t src, uint64_t dst, size_t size)
#else
static inline int dma_reload(const struct device *dev, uint32_t channel,
                uint32_t src, uint32_t dst, size_t size)
#endif
{
        const struct dma_driver_api *api = DEVICE_API_GET(dma, dev);

        if (api->reload) {
                return api->reload(dev, channel, src, dst, size);
        }

        return -ENOSYS;
}

static inline int dma_start(const struct device *dev, uint32_t channel)
{
        return DEVICE_API_GET(dma, dev)->start(dev, channel);
}

static inline int dma_stop(const struct device *dev, uint32_t channel)
{
        const struct dma_driver_api *api = DEVICE_API_GET(dma, dev);

        if (api->stop == NULL) {
                return -ENOSYS;
        }
        return api->stop(dev, channel);
}

static inline int dma_suspend(const struct device *dev, uint32_t channel)
{
        const struct dma_driver_api *api = DEVICE_API_GET(dma, dev);

        if (api->suspend == NULL) {
                return -ENOSYS;
        }
        return api->suspend(dev, channel);
}

static inline int dma_resume(const struct device *dev, uint32_t channel)
{
        const struct dma_driver_api *api = DEVICE_API_GET(dma, dev);

        if (api->resume == NULL) {
                return -ENOSYS;
        }
        return api->resume(dev, channel);
}

static inline int dma_request_channel(const struct device *dev, void *filter_param)
{
        int i = 0;
        int channel = -EINVAL;
        const struct dma_driver_api *api = DEVICE_API_GET(dma, dev);
        /* dma_context shall be the first one in dev data */
        struct dma_context *dma_ctx = (struct dma_context *)dev->data;

        if (dma_ctx->magic != DMA_MAGIC) {
                return channel;
        }

        for (i = 0; i < dma_ctx->dma_channels; i++) {
                if (!atomic_test_and_set_bit(dma_ctx->atomic, i)) {
                        if (api->chan_filter &&
                            !api->chan_filter(dev, i, filter_param)) {
                                atomic_clear_bit(dma_ctx->atomic, i);
                                continue;
                        }
                        channel = i;
                        break;
                }
        }

        return channel;
}

static inline void dma_release_channel(const struct device *dev, uint32_t channel)
{
        const struct dma_driver_api *api = DEVICE_API_GET(dma, dev);
        struct dma_context *dma_ctx = (struct dma_context *)dev->data;

        if (dma_ctx->magic != DMA_MAGIC) {
                return;
        }

        if ((int)channel < dma_ctx->dma_channels) {
                if (api->chan_release) {
                        api->chan_release(dev, channel);
                }

                atomic_clear_bit(dma_ctx->atomic, channel);
        }

}

static inline int dma_chan_filter(const struct device *dev, int channel, void *filter_param)
{
        const struct dma_driver_api *api = DEVICE_API_GET(dma, dev);

        if (api->chan_filter) {
                return api->chan_filter(dev, channel, filter_param);
        }

        return -ENOSYS;
}

static inline int dma_get_status(const struct device *dev, uint32_t channel,
                                 struct dma_status *stat)
{
        const struct dma_driver_api *api = DEVICE_API_GET(dma, dev);

        if (api->get_status) {
                return api->get_status(dev, channel, stat);
        }

        return -ENOSYS;
}

static inline int dma_get_attribute(const struct device *dev, uint32_t type, uint32_t *value)
{
        const struct dma_driver_api *api = DEVICE_API_GET(dma, dev);

        if (api->get_attribute) {
                return api->get_attribute(dev, type, value);
        }

        return -ENOSYS;
}

static inline uint32_t dma_width_index(uint32_t size)
{
        /* Check boundaries (max supported width is 32 Bytes) */
        if (size < 1 || size > 32) {
                return 0; /* Zero is the default (8 Bytes) */
        }

        /* Ensure size is a power of 2 */
        if (!is_power_of_two(size)) {
                return 0; /* Zero is the default (8 Bytes) */
        }

        /* Convert to bit pattern for writing to a register */
        return find_msb_set(size);
}

static inline uint32_t dma_burst_index(uint32_t burst)
{
        /* Check boundaries (max supported burst length is 256) */
        if (burst < 1 || burst > 256) {
                return 0; /* Zero is the default (1 burst length) */
        }

        /* Ensure burst is a power of 2 */
        if (!(burst & (burst - 1))) {
                return 0; /* Zero is the default (1 burst length) */
        }

        /* Convert to bit pattern for writing to a register */
        return find_msb_set(burst);
}

#define DMA_BUF_ADDR_ALIGNMENT(node) DT_PROP(node, dma_buf_addr_alignment)

#define DMA_BUF_SIZE_ALIGNMENT(node) DT_PROP(node, dma_buf_size_alignment)

#define DMA_COPY_ALIGNMENT(node) DT_PROP(node, dma_copy_alignment)


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_DMA_H_ */
```

## 10.2\_可见注释译文（Comments）

1. 版权为2016年Intel Corporation，许可证为Apache-2.0；法律署名原样保留。

2. dma_context必须是设备运行数据dev->data中的第一个成员。

3. 检查边界：支持的最大传输宽度为32字节。

4. 0为默认值；原注释将其描述为8字节。

5. 确保size为2的幂。

6. 0为默认值；原注释将其描述为8字节。

7. 转换为可写入寄存器的位模式（Bit Pattern）。

8. 检查边界：支持的最大突发长度为256。

9. 0为默认值，原注释称其表示突发长度1。

10. 确保burst为2的幂。注意这只是原注释的翻译，代码实际分支与之不一致，见下方译注。

11. 0为默认值，原注释称其表示突发长度1。

12. 转换为可写入寄存器的位模式（Bit Pattern）。

13. 结束ZEPHYR_INCLUDE_DRIVERS_DMA_H_头文件包含保护（Header Include Guard）。

## 10.3\_源码跟踪译注

> 译注——条件分支与资源操作：CONFIG_DMA_64BIT控制传输块地址及reload参数的32／64位类型。dma_request_channel先占位再筛选，拒绝时清位；dma_release_channel执行可选释放回调后清位，不调用dma_stop。公共接口详情见[P001](P001_DMA公共接口.md)。

> 译注——原注释与实际条件：dma_width_index对1～32的2的幂返回find_msb_set，其他输入返回0；不要把注释中的默认8字节解释为所有硬件的统一编码。dma_burst_index的if (!(burst & (burst - 1)))实际在burst为2的幂时返回0，尽管旁边注释写“确保为2的幂”。源代码保留原样，使用前须核对所用版本和硬件寄存器定义。

仓库相对定位：[include/zephyr/drivers/dma.h](../../../include/zephyr/drivers/dma.h)；本次核对的[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/dma.h)摘要见[来源记录](../SOURCES.md)。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致；不能把这种一致性推广到以后滚动更新的main。

本批未构建、烧录、擦写或实板运行；代码阅读和文档核验不代表硬件操作通过。

## 10.4\_原页交叉引用（Cross References）

- [查看此文件参考说明](P009_DMA驱动头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [dma_channel_direction](P001_DMA公共接口.md#gae442d8ba73be7e53b68165647b0ea402)
- [MEMORY_TO_MEMORY](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5)
- [MEMORY_TO_PERIPHERAL](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a)
- [PERIPHERAL_TO_MEMORY](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165)
- [PERIPHERAL_TO_PERIPHERAL](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449)
- [HOST_TO_MEMORY](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c)
- [MEMORY_TO_HOST](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60)
- [DMA_CHANNEL_DIRECTION_COMMON_COUNT](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a)
- [DMA_CHANNEL_DIRECTION_PRIV_START](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037)
- [DMA_CHANNEL_DIRECTION_MAX](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02)
- [dma_addr_adj](P001_DMA公共接口.md#gafe0877ef4bd7790a4bcd46052088231c)
- [DMA_ADDR_ADJ_INCREMENT](P001_DMA公共接口.md#ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e)
- [DMA_ADDR_ADJ_DECREMENT](P001_DMA公共接口.md#ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717)
- [DMA_ADDR_ADJ_NO_CHANGE](P001_DMA公共接口.md#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f)
- [dma_channel_filter](P001_DMA公共接口.md#gade594552920aabbfd2106059a338498b)
- [DMA_CHANNEL_NORMAL](P001_DMA公共接口.md#ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f)
- [DMA_CHANNEL_PERIODIC](P001_DMA公共接口.md#ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c)
- [dma_attribute_type](P001_DMA公共接口.md#ga08c366c8d47672eeeb37b258af20101b)
- [DMA_ATTR_BUFFER_ADDRESS_ALIGNMENT](P001_DMA公共接口.md#gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f)
- [DMA_ATTR_BUFFER_SIZE_ALIGNMENT](P001_DMA公共接口.md#gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873)
- [DMA_ATTR_COPY_ALIGNMENT](P001_DMA公共接口.md#gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b)
- [DMA_ATTR_MAX_BLOCK_COUNT](P001_DMA公共接口.md#gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18)
- [dma_block_config](P003_DMA传输块配置.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [source_address](P003_DMA传输块配置.md#a9fbd1deae8936a806ecc79bad3f3b9bb)
- [dest_address](P003_DMA传输块配置.md#a9a66e0a647c55e94423ababf44c04325)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [source_gather_interval](P003_DMA传输块配置.md#a3180ef98f007ad9be7f6ff363dc125c3)
- [dest_scatter_interval](P003_DMA传输块配置.md#a18bafb80538bca9c12197955770b6511)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [dest_scatter_count](P003_DMA传输块配置.md#ae38027f6262c34d9f1abe4f923d904b4)
- [source_gather_count](P003_DMA传输块配置.md#a8ffcde07d02317b3cc1b327bd0b88395)
- [block_size](P003_DMA传输块配置.md#a3fdab19df16d5e96054aabffbf27fcc1)
- [next_block](P003_DMA传输块配置.md#a937168582c7473fe1b2b696cd1433605)
- [source_gather_en](P003_DMA传输块配置.md#abbac399f6c6e18ad2ed25359ebb799ef)
- [dest_scatter_en](P003_DMA传输块配置.md#a778935d5b806002b902b72304b845ea0)
- [source_addr_adj](P003_DMA传输块配置.md#a9110f948520186aa5718f57b4bbbd24a)
- [dest_addr_adj](P003_DMA传输块配置.md#ad69502226d2c60adbdb9fe5e93dc0a05)
- [source_reload_en](P003_DMA传输块配置.md#a4f8f5b65002f65eaacdd3dde26c47170)
- [dest_reload_en](P003_DMA传输块配置.md#a7dedf429f44f3af6fcc0db125d6494c8)
- [fifo_mode_control](P003_DMA传输块配置.md#a877a30b62fd8e0e1773890a10c8a2751)
- [flow_control_mode](P003_DMA传输块配置.md#aecf6805b898a70922c58d15127bafc92)
- [dma_callback_t](P001_DMA公共接口.md#ga94745b4472ee1addd4f82db4e59e9fb5)
- [device](../device_reference/P002_设备对象结构.md)
- [dma_config](P004_DMA通道配置.md)
- [dma_slot](P004_DMA通道配置.md#a8e6c5cab5ec030066a3e57e0507fbf9f)
- [channel_direction](P004_DMA通道配置.md#aaf903b1badff8b0fc4ef18a34c2773d7)
- [half_complete_callback_en](P004_DMA通道配置.md#a0e2da7a8f4439ceb3f2acf02e4681396)
- [complete_callback_en](P004_DMA通道配置.md#a39526177f03017d245651b4f51820161)
- [error_callback_dis](P004_DMA通道配置.md#a416a0ef20318fe77d7e383caeee67e94)
- [source_handshake](P004_DMA通道配置.md#a2927e31730c6ca2f5ac8db38c255d9f7)
- [dest_handshake](P004_DMA通道配置.md#af570b4050200ec510df323bd31558233)
- [channel_priority](P004_DMA通道配置.md#a284d96c59945aaa851d235802aee979a)
- [source_chaining_en](P004_DMA通道配置.md#a7c77afc1f546efda6ce22f50560b8840)
- [dest_chaining_en](P004_DMA通道配置.md#a8a304fdada9ec7fc87402449e1410486)
- [linked_channel](P004_DMA通道配置.md#ace2dc918fcfea264a579b1084fcb7fe5)
- [cyclic](P004_DMA通道配置.md#afa70dbf1ee7bb5fb6a771f634783b7a2)
- [source_data_size](P004_DMA通道配置.md#ac9144783b4843182451b440d97ecd273)
- [dest_data_size](P004_DMA通道配置.md#adfa9efbfbef3ed41b2f8dd5b9c441e08)
- [source_burst_length](P004_DMA通道配置.md#ad750b724bab1503ded7c163d8228aa80)
- [dest_burst_length](P004_DMA通道配置.md#aca47b00f817e55bf662fdd6767a59ed0)
- [block_count](P004_DMA通道配置.md#adb776a4940c71b61cab60eb05159b2d4)
- [head_block](P004_DMA通道配置.md#aca6a1cb9b580a61bf91490fecf10cb16)
- [user_data](P004_DMA通道配置.md#a510eed1cadbf411c9e94e1d1fb43d39d)
- [dma_callback](P004_DMA通道配置.md#a69110abc43227bd7df217c4e25bb964b)
- [dma_status](P005_DMA运行状态.md)
- [busy](P005_DMA运行状态.md#a92ec05d9207caa828064661897f2f31c)
- [dir](P005_DMA运行状态.md#aacfe94ad8e60ea77bca2423bd9bf8409)
- [pending_length](P005_DMA运行状态.md#a3a33f92b1d100f988fca2bea0a6deb24)
- [free](P005_DMA运行状态.md#a2b481bf13de03e49146eb6a26563776e)
- [write_position](P005_DMA运行状态.md#aa7288b85f41098e59ad4f96dcea4ccde)
- [read_position](P005_DMA运行状态.md#afa401acfb26cd26b73e4a52066989847)
- [total_copied](P005_DMA运行状态.md#a9f743c98e6343d55eccc27e528b79b1a)
- [dma_context](P006_DMA通道分配上下文.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [magic](P006_DMA通道分配上下文.md#a25355c8cc60df536c9a37cdef52aa653)
- [dma_channels](P006_DMA通道分配上下文.md#ac6685cf14ca69c7b77160e5031c0a800)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [atomic](P006_DMA通道分配上下文.md#a5b5776088155c9f19488d479924bec8e)
- [dma_api_config](P002_DMA驱动后端接口.md#gab15e273c0f3b1978d17ad448d98f56bb)
- [dma_api_reload](P002_DMA驱动后端接口.md#gab00e7199fa8dafa541e4ef5f63c391b4)
- [dma_api_start](P002_DMA驱动后端接口.md#ga1cd1fc992eb0e95690a50e2696247da0)
- [dma_api_stop](P002_DMA驱动后端接口.md#gad63e7dc2e41adc03f4a338bda760f2ff)
- [dma_api_suspend](P002_DMA驱动后端接口.md#gad3742f6c4218b6a648e9aa5734516818)
- [dma_api_resume](P002_DMA驱动后端接口.md#ga5073bb15b75cbbbcdbd3f859f28e3473)
- [dma_api_get_status](P002_DMA驱动后端接口.md#ga06781c37590c23e6df82471aac4923dc)
- [dma_api_get_attribute](P002_DMA驱动后端接口.md#ga2cc72d829ce7f47eb2a326faaedf3fc5)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [dma_api_chan_filter](P002_DMA驱动后端接口.md#ga1c65fe109d52e477f3bafa56e4afefb7)
- [dma_api_chan_release](P002_DMA驱动后端接口.md#ga035b4982cae52df4ce1911ad007d3a64)
- [dma_driver_api](P007_DMA驱动操作结构.md)
- [config](P007_DMA驱动操作结构.md#a0a2ca7aae0cf9bc65d34c2332c646296)
- [reload](P007_DMA驱动操作结构.md#a5fb4a9ee5dbffb3d71a5bc1b81c5728b)
- [start](P007_DMA驱动操作结构.md#a812b5d3118965c0387f362de31b6debb)
- [stop](P007_DMA驱动操作结构.md#a282e408e1fee4f63dea11a8b10e43986)
- [suspend](P007_DMA驱动操作结构.md#a56d9d2f5dfe9638691c43dd2e8a9a84d)
- [resume](P007_DMA驱动操作结构.md#ad51378a0d3e4f74ecb9c56e85984aec2)
- [get_status](P007_DMA驱动操作结构.md#ac526f6bca144e3fa4366b232cd694a1c)
- [get_attribute](P007_DMA驱动操作结构.md#aebc286d4576223b1d1873d5b0ebe225e)
- [chan_filter](P007_DMA驱动操作结构.md#a6c5e9147e23ab14ff00c35da101ab5c3)
- [chan_release](P007_DMA驱动操作结构.md#a2daa5d977f3d62b910bcd188d9fe535c)
- [dma_config](P001_DMA公共接口.md#ga6df1a6b89f271a0eae01c17b748bd2df)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [dma_reload](P001_DMA公共接口.md#ga55bd5d550349c11c63ef47c2ed861f36)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [dma_start](P001_DMA公共接口.md#gaf1184de07811702ffe89737b79e4a338)
- [dma_stop](P001_DMA公共接口.md#gafd602ee8386e10bb9ac7d386b3dc6a83)
- [dma_suspend](P001_DMA公共接口.md#ga97bf9807b7fde7671a378333f01463d6)
- [dma_resume](P001_DMA公共接口.md#ga1b1eeef68f1aa4818c9baf95b83b9e1e)
- [dma_request_channel](P001_DMA公共接口.md#gaadc34e0ea92d9fd2f1242789367b1dd5)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [DMA_MAGIC](P001_DMA公共接口.md#gae28ba5114dc2e9ecb89ccf9b623e938f)
- [atomic_test_and_set_bit](../atomic_reference/P001_原子操作公共接口.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)
- [atomic_clear_bit](../atomic_reference/P001_原子操作公共接口.md#ga1c1693d524c49d11fd32b323a39d718e)
- [dma_release_channel](P001_DMA公共接口.md#ga93b49d4d0910ceed88fa8aaa22b73098)
- [dma_chan_filter](P001_DMA公共接口.md#ga6d4c3e63bc4382215774e86893bc3072)
- [dma_get_status](P001_DMA公共接口.md#ga2cae500f1f9ed42ad338a40ec8655544)
- [stat](https://docs.zephyrproject.org/latest/doxygen/html/structstat.html)
- [dma_get_attribute](P001_DMA公共接口.md#ga641f3fa492bfb17cf9f0a0361d429257)
- [dma_width_index](P001_DMA公共接口.md#gadd1724a843bba4ccc1c65c9fb9d3d921)
- [is_power_of_two](../util_reference/P001_通用工具公共接口.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)
- [find_msb_set](../numeric_reference/P006_置位扫描头文件参考.md#a088db7d02e8f1fc559cbe1ec048494e8)
- [dma_burst_index](P001_DMA公共接口.md#gaac27f2ee664671884087ee3d2a2863ce)

---

[上一章](P009_DMA驱动头文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_DMA设备树头文件参考.md)
