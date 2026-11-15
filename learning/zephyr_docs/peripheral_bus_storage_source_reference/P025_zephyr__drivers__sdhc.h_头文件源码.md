---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-25
title: zephyr__drivers__sdhc.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sdhc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr__drivers__sdhc.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sdhc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P025_zephyr__drivers__sdhc.h_头文件参考.md)。

## 25.1\_原始可见代码（Source Code）

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
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="foldopen00048"></a>
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
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00066"></a>
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
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00108"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="foldopen00121"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00151"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="foldopen00169"></a>
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
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
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
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="foldopen00214"></a>
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
<a id="foldopen00230"></a>
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
<a id="foldopen00250"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00272"></a>
<a id="foldopen00276"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00303"></a>
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
<a id="l00329"></a>
<a id="l00330"></a>
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
<a id="l00354"></a>
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
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__sdhc__interface_html_ga0e6d8259cca442bd1356d00f668d35c4"></a>
<a id="agroup__sdhc__interface_html_ga34041edf280f125b8500809226b3de5d"></a>
<a id="agroup__sdhc__interface_html_ga5d207e3b3d76ed9dbfa7d68a92755cbe"></a>
<a id="agroup__sdhc__interface_html_ga6264f62c6427973749c8d49fb908f569"></a>
<a id="agroup__sdhc__interface_html_ga6f006ca8fd9ff8a68ac46a0bb7d4bc90"></a>
<a id="agroup__sdhc__interface_html_ga85184688da845759dbfb706aac5eac7d"></a>
<a id="agroup__sdhc__interface_html_ga8e4beb1135aa5c0d32f999ca953224d2"></a>
<a id="agroup__sdhc__interface_html_ga91acdc4a6bc2aecc988fdde6ee61ed46"></a>
<a id="agroup__sdhc__interface_html_gab449b2f6b41e791d327f7d92b2b58c2d"></a>
<a id="agroup__sdhc__interface_html_gab55cf88ae79e5aa9e2110b298048df8e"></a>
<a id="agroup__sdhc__interface_html_gab5c2711c99573e031938faaa41862971"></a>
<a id="agroup__sdhc__interface_html_gac708d55e92a7705f92b90ee6baa65f74"></a>
<a id="agroup__sdhc__interface_html_gad63742820bb18ca18cd2f96547e12eb9"></a>
<a id="agroup__sdhc__interface_html_gad6b082a75f1272620b79a7d3a08862f7"></a>
<a id="agroup__sdhc__interface_html_gad8bab66ec505c8356fac7785a8955448"></a>
<a id="agroup__sdhc__interface_html_gaf26909ae9fffdc6ac02abd8094d16dc8"></a>
<a id="agroup__sdhc__interface_html_gga34041edf280f125b8500809226b3de5da186c3fbdedaf8840a8204d770de1e56d"></a>
<a id="agroup__sdhc__interface_html_gga34041edf280f125b8500809226b3de5da6dd8c2d9590dfe38bb77a21c350d36af"></a>
<a id="agroup__sdhc__interface_html_gga34041edf280f125b8500809226b3de5daad6c30a3ea2280c9235ba538b52edf11"></a>
<a id="agroup__sdhc__interface_html_gga34041edf280f125b8500809226b3de5dafeed0c640efe6df6f13f76b95138373d"></a>
<a id="agroup__sdhc__interface_html_gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a56909869d92eb1c212051c8a23449ebc"></a>
<a id="agroup__sdhc__interface_html_gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a80c5035dc9976f8ee4d7b1f20f21e692"></a>
<a id="agroup__sdhc__interface_html_gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a836ffb1abaf681d2992c8c906f5e2c94"></a>
<a id="agroup__sdhc__interface_html_gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c5c11b75f76771dfedebc6d4a844e55"></a>
<a id="agroup__sdhc__interface_html_gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c77db56b6a006c1cff9f70e20f6d016"></a>
<a id="agroup__sdhc__interface_html_gga6f006ca8fd9ff8a68ac46a0bb7d4bc90aa48069d7a8a43308d308c9fe67543d86"></a>
<a id="agroup__sdhc__interface_html_gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae2b69f73212e34bbbfb1c02c27740bd1"></a>
<a id="agroup__sdhc__interface_html_gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae892594e6a91a70ade2dc983bda2d145"></a>
<a id="agroup__sdhc__interface_html_gga6f006ca8fd9ff8a68ac46a0bb7d4bc90af5f82fc8f4b281e44b5e78f229d9564b"></a>
<a id="agroup__sdhc__interface_html_gga6f006ca8fd9ff8a68ac46a0bb7d4bc90afc9b5aa9339c4ffdea8d6452c10ba5fa"></a>
<a id="agroup__sdhc__interface_html_ggab449b2f6b41e791d327f7d92b2b58c2da6e0a03105c6aba203daa53acb6b7c15c"></a>
<a id="agroup__sdhc__interface_html_ggab449b2f6b41e791d327f7d92b2b58c2dab9df16a6ed1c7961bb9cab34ebe99f87"></a>
<a id="agroup__sdhc__interface_html_ggab449b2f6b41e791d327f7d92b2b58c2dae3a741e98cdb1e8c0ddc8c3baaf64b59"></a>
<a id="agroup__sdhc__interface_html_ggad63742820bb18ca18cd2f96547e12eb9a621f9456dbce2647567e2e2d049a4c07"></a>
<a id="agroup__sdhc__interface_html_ggad63742820bb18ca18cd2f96547e12eb9a9442e1400bdfa373a6874cd1434ab604"></a>
<a id="agroup__sdhc__interface_html_ggad8bab66ec505c8356fac7785a8955448a2b28e7702abe63e03d2b77994d30e156"></a>
<a id="agroup__sdhc__interface_html_ggad8bab66ec505c8356fac7785a8955448a4e679800f8863d5650827a0330ef22b6"></a>
<a id="agroup__sdhc__interface_html_ggad8bab66ec505c8356fac7785a8955448a875995b349ed5c81e6f34569c35079a0"></a>
<a id="agroup__sdhc__interface_html_ggaf26909ae9fffdc6ac02abd8094d16dc8a5408bfd39f7ab8c79735d8a956dc9b1a"></a>
<a id="agroup__sdhc__interface_html_ggaf26909ae9fffdc6ac02abd8094d16dc8ae47425099c55e2191de84a8cbfa17959"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="anet__buf_8h_html"></a>
<a id="asd__spec_8h_html"></a>
<a id="asd__spec_8h_html_a314c38b1b0603c003e67b5dec2228d4b"></a>
<a id="asd__spec_8h_html_a9660a61775e481ae4093e11ce9336539"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructsdhc__command_html"></a>
<a id="astructsdhc__command_html_a320ad415df67e1d9b4c09f95993dd17f"></a>
<a id="astructsdhc__command_html_a37a3c1608b5c13311c833c4ad24ff1f9"></a>
<a id="astructsdhc__command_html_a39ba0b1e99814471939dc7bbb7d098eb"></a>
<a id="astructsdhc__command_html_a92cf023d28aa6106d603ff7f67a7e04b"></a>
<a id="astructsdhc__command_html_af6b98d5f1cecf25af2480b1d359f200e"></a>
<a id="astructsdhc__command_html_af758a4e0e3b090912f6e9abd7c4be8f3"></a>
<a id="astructsdhc__data_html"></a>
<a id="astructsdhc__data_html_a0f656d093a5cdf3bd09ffee279ad452d"></a>
<a id="astructsdhc__data_html_a20b0ca14adadcdb8d3681240faf5e7b6"></a>
<a id="astructsdhc__data_html_a47b378d455167bb8d7d05d2f058977fa"></a>
<a id="astructsdhc__data_html_a4f7ca31c9cee1ace999a46cce75b9f65"></a>
<a id="astructsdhc__data_html_aad1e8462d94b4243c981147eab6c962d"></a>
<a id="astructsdhc__data_html_ae68f1e7f1fbff14c24bd42fa300f9e15"></a>
<a id="astructsdhc__data_html_afcf3942de27cd164b6da8dfefa864a8a"></a>
<a id="astructsdhc__driver__api_html"></a>
<a id="astructsdhc__driver__api_html_a06fb6fdfd0c528056c36476f914f94c9"></a>
<a id="astructsdhc__driver__api_html_a42941f226f2adfe5b8275923bff434ff"></a>
<a id="astructsdhc__driver__api_html_a577d162b282b2f9eeb91cf07e7578905"></a>
<a id="astructsdhc__driver__api_html_a6075f8ef38200e700ec133fbeb8c8121"></a>
<a id="astructsdhc__driver__api_html_aa50466e31e01d639e459bab204cf1ee5"></a>
<a id="astructsdhc__driver__api_html_ac034dfc17e064170e76280394005c76c"></a>
<a id="astructsdhc__driver__api_html_ac642c06d5ec9f697be8fa46cede3bc64"></a>
<a id="astructsdhc__driver__api_html_adb40a93f64a1a8dc1548a4651091ecf9"></a>
<a id="astructsdhc__driver__api_html_af2b83b0ea2afbbdf065b5919c6b822c2"></a>
<a id="astructsdhc__host__caps_html"></a>
<a id="astructsdhc__host__caps_html_a0f33c7e168ade12675795d2c0d5b5ea2"></a>
<a id="astructsdhc__host__caps_html_a146c7403d7ecbbffbd6aa0c1c4fad1b5"></a>
<a id="astructsdhc__host__caps_html_a20ada015fecce002d233fefac5c4ead4"></a>
<a id="astructsdhc__host__caps_html_a22f2877854669589f0483cf91e504df6"></a>
<a id="astructsdhc__host__caps_html_a2f5d5859cbe06ab449f95c0a108c2250"></a>
<a id="astructsdhc__host__caps_html_a3231007bc5fcc731e97236b29333f7ee"></a>
<a id="astructsdhc__host__caps_html_a3a57e12aa8f53ad1c1fb44696622f587"></a>
<a id="astructsdhc__host__caps_html_a3e6f73ea9df9c207cddda31de45621be"></a>
<a id="astructsdhc__host__caps_html_a43086e5bc5d6384b8eb0709c1cf1756e"></a>
<a id="astructsdhc__host__caps_html_a48680d522d417e68ec3371b3831faa01"></a>
<a id="astructsdhc__host__caps_html_a63dabbc7c24dc41c8103be81ee6e673f"></a>
<a id="astructsdhc__host__caps_html_a6fa0525ee3b2a0313cc9b83dc820b831"></a>
<a id="astructsdhc__host__caps_html_a7fdf6832fbcc9dce7e20ee87d9063665"></a>
<a id="astructsdhc__host__caps_html_a8af558ed3b7af437f1782aea9ee6794e"></a>
<a id="astructsdhc__host__caps_html_a90a90218bcd866cbfae2354c5b0af3de"></a>
<a id="astructsdhc__host__caps_html_a97dbad3360b56a44fb1ab0d77aa90bc4"></a>
<a id="astructsdhc__host__caps_html_aa22adb0079aa3864df4461d841852684"></a>
<a id="astructsdhc__host__caps_html_aa39ef2d70314dbf2517bd3df6fbd4694"></a>
<a id="astructsdhc__host__caps_html_aaec0cd01cc4e8bf334e5c3ee151d5d98"></a>
<a id="astructsdhc__host__caps_html_aafcfb75fd131430df0a372e6ac2c8b34"></a>
<a id="astructsdhc__host__caps_html_ab7a145bf44747d7d9e68ff743520cc2c"></a>
<a id="astructsdhc__host__caps_html_ac54a191e04ff6c266390d1fb8d4f84d3"></a>
<a id="astructsdhc__host__caps_html_ac6e2eb088ed7d7c3f3f5011ad55ba543"></a>
<a id="astructsdhc__host__caps_html_acfa1c5e96f2afeab40185a1ef37d7efb"></a>
<a id="astructsdhc__host__caps_html_ad09f103fc8ce341d25e1f824e97bd665"></a>
<a id="astructsdhc__host__caps_html_ad2c9e66bbd9a442d872fd559fd7a833c"></a>
<a id="astructsdhc__host__caps_html_ad8e4ca0d2fb39486b469224218d2eb7b"></a>
<a id="astructsdhc__host__caps_html_af343879ebc21f5c2d57ffa962dacb796"></a>
<a id="astructsdhc__host__caps_html_afffade3ad661ead23ed0f74b770172ff"></a>
<a id="astructsdhc__host__props_html"></a>
<a id="astructsdhc__host__props_html_a28c69ba3fdae1393daa551f3f9b91057"></a>
<a id="astructsdhc__host__props_html_a43d2b80ec0a5682783e4297c734a3c88"></a>
<a id="astructsdhc__host__props_html_a4a6ebccaddfc4bb99b0bbb628ffabb21"></a>
<a id="astructsdhc__host__props_html_a6401a11a8ac85cf3951ec138173f87b7"></a>
<a id="astructsdhc__host__props_html_a7af8f0a9564db9ef0630a8bc85ac34a9"></a>
<a id="astructsdhc__host__props_html_a7f7b22b7b8fb46df0ec19e2bef2a4702"></a>
<a id="astructsdhc__host__props_html_abb18e33d99ed1e4a4400dccd2149816f"></a>
<a id="astructsdhc__host__props_html_ac247312c9b10768fe878afc5c85d9eba"></a>
<a id="astructsdhc__host__props_html_ad60bf89e594a031f6be015888466a113"></a>
<a id="astructsdhc__host__props_html_aec7874d1012fe5fb881c3ca5e913391e"></a>
<a id="astructsdhc__host__props_html_aef7123dfa5690bc0525aa40dc623307c"></a>
<a id="astructsdhc__host__props_html_afebe4aad820c1672635fd30aacec20e4"></a>
<a id="astructsdhc__io_html"></a>
<a id="astructsdhc__io_html_a0c62aaa1a8a7700ebb00a38ce2e57d11"></a>
<a id="astructsdhc__io_html_a2b4456b108778aada0d42b8c8107b3e9"></a>
<a id="astructsdhc__io_html_a85c50f625d8606bb4c07a228c0de24e4"></a>
<a id="astructsdhc__io_html_a904b05c7e73e80bb7326b0bfcb6b7103"></a>
<a id="astructsdhc__io_html_aaa15197b8f1947a67dcd8522aa62afc5"></a>
<a id="astructsdhc__io_html_ac503fb9fba7ffdb01695a77780972930"></a>
<a id="astructsdhc__io_html_ade8b8cd4e4f4b21f5fa8e3fb2661917e"></a>
<a id="astructsdhc__io_html_afa9a07a8734e9d39b29da0697cf60289"></a>

```c
/*
 * Copyright 2022, 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SDHC_H_
#define ZEPHYR_INCLUDE_DRIVERS_SDHC_H_

#include <errno.h>
#include <zephyr/device.h>
#include <zephyr/net_buf.h>
#include <zephyr/sd/sd_spec.h>


#ifdef __cplusplus
extern "C" {
#endif


#define SDHC_TIMEOUT_FOREVER (-1)

struct sdhc_command {
        uint32_t opcode;
        uint32_t arg;
        uint32_t response[4];
        uint32_t response_type;
        unsigned int retries;
        int timeout_ms;
};

#define SDHC_NATIVE_RESPONSE_MASK 0xF
#define SDHC_SPI_RESPONSE_TYPE_MASK 0xF0

struct sdhc_data {
        unsigned int block_addr;
        unsigned int block_size;
        unsigned int blocks;
        unsigned int bytes_xfered;
#if defined(CONFIG_SDHC_SCATTER_GATHER_TRANSFER) || defined(__DOXYGEN__)
        bool is_sg_data;
#endif
        void *data;
        int timeout_ms;
};

enum sdhc_bus_mode {
        SDHC_BUSMODE_OPENDRAIN = 1,
        SDHC_BUSMODE_PUSHPULL = 2,
};

enum sdhc_power {
        SDHC_POWER_OFF = 1,
        SDHC_POWER_ON = 2,
};

enum sdhc_bus_width {
        SDHC_BUS_WIDTH1BIT = 1U,
        SDHC_BUS_WIDTH4BIT = 4U,
        SDHC_BUS_WIDTH8BIT = 8U,
};

enum sdhc_timing_mode {
        SDHC_TIMING_LEGACY = 1U,
        SDHC_TIMING_HS = 2U,
        SDHC_TIMING_SDR12 = 3U,
        SDHC_TIMING_SDR25 = 4U,
        SDHC_TIMING_SDR50 = 5U,
        SDHC_TIMING_SDR104 = 6U,
        SDHC_TIMING_DDR50 = 7U,
        SDHC_TIMING_DDR52 = 8U,
        SDHC_TIMING_HS200 = 9U,
        SDHC_TIMING_HS400 = 10U,
};

enum sd_voltage {
        SD_VOL_3_3_V = 1U,
        SD_VOL_3_0_V = 2U,
        SD_VOL_1_8_V = 3U,
        SD_VOL_1_2_V = 4U,
};

struct sdhc_host_caps {
        unsigned int timeout_clk_freq: 6;
        unsigned int _rsvd_6: 1;
        unsigned int timeout_clk_unit: 1;
        unsigned int sd_base_clk: 8;
        unsigned int max_blk_len: 2;
        unsigned int bus_8_bit_support: 1;
        unsigned int adma_2_support: 1;
        unsigned int _rsvd_20: 1;
        unsigned int high_spd_support: 1;
        unsigned int sdma_support: 1;
        unsigned int suspend_res_support: 1;
        unsigned int vol_330_support: 1;
        unsigned int vol_300_support: 1;
        unsigned int vol_180_support: 1;
        unsigned int address_64_bit_support_v4: 1;
        unsigned int address_64_bit_support_v3: 1;
        unsigned int sdio_async_interrupt_support: 1;
        unsigned int slot_type: 2;
        unsigned int sdr50_support: 1;
        unsigned int sdr104_support: 1;
        unsigned int ddr50_support: 1;
        unsigned int uhs_2_support: 1;
        unsigned int drv_type_a_support: 1;
        unsigned int drv_type_c_support: 1;
        unsigned int drv_type_d_support: 1;
        unsigned int _rsvd_39: 1;
        unsigned int retune_timer_count: 4;
        unsigned int _rsvd_44: 1;
        unsigned int sdr50_needs_tuning: 1;
        unsigned int retuning_mode: 2;
        unsigned int clk_multiplier: 8;
        unsigned int _rsvd_56: 3;
        unsigned int adma3_support: 1;
        unsigned int vdd2_180_support: 1;
        unsigned int _rsvd_61: 3;
};

struct sdhc_io {
        enum sdhc_clock_speed clock;
        enum sdhc_bus_mode bus_mode;
        enum sdhc_power power_mode;
        enum sdhc_bus_width bus_width;
        enum sdhc_timing_mode timing;
        bool enhanced_strobe;
        enum sd_driver_type driver_type;
        enum sd_voltage signal_voltage;
};

struct sdhc_host_props {
        unsigned int f_max;
        unsigned int f_min;
        unsigned int power_delay;
        struct sdhc_host_caps host_caps;
        uint32_t max_current_330;
        uint32_t max_current_300;
        uint32_t max_current_180;
        bool bus_4_bit_support;
        bool hs200_support;
        bool hs400_support;
        bool hs400_enhanced_strobe_support;
        bool is_spi;
};

enum sdhc_interrupt_source {
        SDHC_INT_SDIO = BIT(0),
        SDHC_INT_INSERTED = BIT(1),
        SDHC_INT_REMOVED = BIT(2),
};

typedef void (*sdhc_interrupt_cb_t)(const struct device *dev, int reason,
                                    const void *user_data);


__subsystem struct sdhc_driver_api {
        int (*reset)(const struct device *dev);
        int (*request)(const struct device *dev,
                       struct sdhc_command *cmd,
                       struct sdhc_data *data);
        int (*set_io)(const struct device *dev, struct sdhc_io *ios);
        int (*get_card_present)(const struct device *dev);
        int (*execute_tuning)(const struct device *dev);
        int (*card_busy)(const struct device *dev);
        int (*get_host_props)(const struct device *dev,
                              struct sdhc_host_props *props);
        int (*enable_interrupt)(const struct device *dev,
                                sdhc_interrupt_cb_t callback,
                                int sources, void *user_data);
        int (*disable_interrupt)(const struct device *dev, int sources);
};


__syscall int sdhc_hw_reset(const struct device *dev);

static inline int z_impl_sdhc_hw_reset(const struct device *dev)
{
        const struct sdhc_driver_api *api = DEVICE_API_GET(sdhc, dev);

        if (!api->reset) {
                return -ENOSYS;
        }

        return api->reset(dev);
}


__syscall int sdhc_request(const struct device *dev, struct sdhc_command *cmd,
                           struct sdhc_data *data);

static inline int z_impl_sdhc_request(const struct device *dev,
                                      struct sdhc_command *cmd,
                                      struct sdhc_data *data)
{
        const struct sdhc_driver_api *api = DEVICE_API_GET(sdhc, dev);

        return api->request(dev, cmd, data);
}

__syscall int sdhc_set_io(const struct device *dev, struct sdhc_io *io);

static inline int z_impl_sdhc_set_io(const struct device *dev,
                                     struct sdhc_io *io)
{
        const struct sdhc_driver_api *api = DEVICE_API_GET(sdhc, dev);

        return api->set_io(dev, io);
}

__syscall int sdhc_card_present(const struct device *dev);

static inline int z_impl_sdhc_card_present(const struct device *dev)
{
        const struct sdhc_driver_api *api = DEVICE_API_GET(sdhc, dev);

        return api->get_card_present(dev);
}


__syscall int sdhc_execute_tuning(const struct device *dev);

static inline int z_impl_sdhc_execute_tuning(const struct device *dev)
{
        const struct sdhc_driver_api *api = DEVICE_API_GET(sdhc, dev);

        if (!api->execute_tuning) {
                return -ENOSYS;
        }

        return api->execute_tuning(dev);
}

__syscall int sdhc_card_busy(const struct device *dev);

static inline int z_impl_sdhc_card_busy(const struct device *dev)
{
        const struct sdhc_driver_api *api = DEVICE_API_GET(sdhc, dev);

        return api->card_busy(dev);
}


__syscall int sdhc_get_host_props(const struct device *dev,
                                  struct sdhc_host_props *props);

static inline int z_impl_sdhc_get_host_props(const struct device *dev,
                                             struct sdhc_host_props *props)
{
        const struct sdhc_driver_api *api = DEVICE_API_GET(sdhc, dev);

        return api->get_host_props(dev, props);
}

__syscall int sdhc_enable_interrupt(const struct device *dev,
                                    sdhc_interrupt_cb_t callback,
                                    int sources, void *user_data);

static inline int z_impl_sdhc_enable_interrupt(const struct device *dev,
                                               sdhc_interrupt_cb_t callback,
                                               int sources, void *user_data)
{
        const struct sdhc_driver_api *api = DEVICE_API_GET(sdhc, dev);

        if (!api->enable_interrupt) {
                return -ENOSYS;
        }

        return api->enable_interrupt(dev, callback, sources, user_data);
}

__syscall int sdhc_disable_interrupt(const struct device *dev, int sources);

static inline int z_impl_sdhc_disable_interrupt(const struct device *dev,
                                                int sources)
{
        const struct sdhc_driver_api *api = DEVICE_API_GET(sdhc, dev);

        if (!api->disable_interrupt) {
                return -ENOSYS;
        }

        return api->disable_interrupt(dev, sources);
}


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/sdhc.h>
#endif /* ZEPHYR_INCLUDE_DRIVERS_SDHC_H_ */
```

## 25.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022, 2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 533 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SDHC_H_`。

## 25.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P025_zephyr__drivers__sdhc.h_头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sd/sd_spec.h](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md)
- [sdhc_command](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [opcode](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md#a320ad415df67e1d9b4c09f95993dd17f)
- [arg](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md#af6b98d5f1cecf25af2480b1d359f200e)
- [response](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md#a37a3c1608b5c13311c833c4ad24ff1f9)
- [response_type](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md#af758a4e0e3b090912f6e9abd7c4be8f3)
- [retries](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md#a39ba0b1e99814471939dc7bbb7d098eb)
- [timeout_ms](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md#a92cf023d28aa6106d603ff7f67a7e04b)
- [sdhc_data](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md)
- [block_addr](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#aad1e8462d94b4243c981147eab6c962d)
- [block_size](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#a20b0ca14adadcdb8d3681240faf5e7b6)
- [blocks](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#a47b378d455167bb8d7d05d2f058977fa)
- [bytes_xfered](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#ae68f1e7f1fbff14c24bd42fa300f9e15)
- [is_sg_data](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#a4f7ca31c9cee1ace999a46cce75b9f65)
- [data](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#a0f656d093a5cdf3bd09ffee279ad452d)
- [timeout_ms](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#afcf3942de27cd164b6da8dfefa864a8a)
- [sdhc_bus_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gaf26909ae9fffdc6ac02abd8094d16dc8)
- [SDHC_BUSMODE_OPENDRAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggaf26909ae9fffdc6ac02abd8094d16dc8a5408bfd39f7ab8c79735d8a956dc9b1a)
- [SDHC_BUSMODE_PUSHPULL](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggaf26909ae9fffdc6ac02abd8094d16dc8ae47425099c55e2191de84a8cbfa17959)
- [sdhc_power](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad63742820bb18ca18cd2f96547e12eb9)
- [SDHC_POWER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad63742820bb18ca18cd2f96547e12eb9a621f9456dbce2647567e2e2d049a4c07)
- [SDHC_POWER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad63742820bb18ca18cd2f96547e12eb9a9442e1400bdfa373a6874cd1434ab604)
- [sdhc_bus_width](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad8bab66ec505c8356fac7785a8955448)
- [SDHC_BUS_WIDTH1BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad8bab66ec505c8356fac7785a8955448a875995b349ed5c81e6f34569c35079a0)
- [SDHC_BUS_WIDTH4BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad8bab66ec505c8356fac7785a8955448a4e679800f8863d5650827a0330ef22b6)
- [SDHC_BUS_WIDTH8BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad8bab66ec505c8356fac7785a8955448a2b28e7702abe63e03d2b77994d30e156)
- [sdhc_timing_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90)
- [SDHC_TIMING_LEGACY](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c5c11b75f76771dfedebc6d4a844e55)
- [SDHC_TIMING_HS](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90af5f82fc8f4b281e44b5e78f229d9564b)
- [SDHC_TIMING_SDR12](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90aa48069d7a8a43308d308c9fe67543d86)
- [SDHC_TIMING_SDR25](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c77db56b6a006c1cff9f70e20f6d016)
- [SDHC_TIMING_SDR50](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a836ffb1abaf681d2992c8c906f5e2c94)
- [SDHC_TIMING_SDR104](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae2b69f73212e34bbbfb1c02c27740bd1)
- [SDHC_TIMING_DDR50](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90afc9b5aa9339c4ffdea8d6452c10ba5fa)
- [SDHC_TIMING_DDR52](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a80c5035dc9976f8ee4d7b1f20f21e692)
- [SDHC_TIMING_HS200](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae892594e6a91a70ade2dc983bda2d145)
- [SDHC_TIMING_HS400](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a56909869d92eb1c212051c8a23449ebc)
- [sd_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga34041edf280f125b8500809226b3de5d)
- [SD_VOL_3_3_V](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga34041edf280f125b8500809226b3de5da186c3fbdedaf8840a8204d770de1e56d)
- [SD_VOL_3_0_V](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga34041edf280f125b8500809226b3de5daad6c30a3ea2280c9235ba538b52edf11)
- [SD_VOL_1_8_V](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga34041edf280f125b8500809226b3de5dafeed0c640efe6df6f13f76b95138373d)
- [SD_VOL_1_2_V](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga34041edf280f125b8500809226b3de5da6dd8c2d9590dfe38bb77a21c350d36af)
- [sdhc_host_caps](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md)
- [timeout_clk_freq](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a3a57e12aa8f53ad1c1fb44696622f587)
- [timeout_clk_unit](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a8af558ed3b7af437f1782aea9ee6794e)
- [sd_base_clk](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a20ada015fecce002d233fefac5c4ead4)
- [max_blk_len](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a97dbad3360b56a44fb1ab0d77aa90bc4)
- [bus_8_bit_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#ad09f103fc8ce341d25e1f824e97bd665)
- [adma_2_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#acfa1c5e96f2afeab40185a1ef37d7efb)
- [high_spd_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#aaec0cd01cc4e8bf334e5c3ee151d5d98)
- [sdma_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a22f2877854669589f0483cf91e504df6)
- [suspend_res_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#af343879ebc21f5c2d57ffa962dacb796)
- [vol_330_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#ac6e2eb088ed7d7c3f3f5011ad55ba543)
- [vol_300_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a7fdf6832fbcc9dce7e20ee87d9063665)
- [vol_180_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#aa39ef2d70314dbf2517bd3df6fbd4694)
- [address_64_bit_support_v4](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#ad8e4ca0d2fb39486b469224218d2eb7b)
- [address_64_bit_support_v3](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a0f33c7e168ade12675795d2c0d5b5ea2)
- [sdio_async_interrupt_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a6fa0525ee3b2a0313cc9b83dc820b831)
- [slot_type](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a3231007bc5fcc731e97236b29333f7ee)
- [sdr50_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a63dabbc7c24dc41c8103be81ee6e673f)
- [sdr104_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a3e6f73ea9df9c207cddda31de45621be)
- [ddr50_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#aa22adb0079aa3864df4461d841852684)
- [uhs_2_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a146c7403d7ecbbffbd6aa0c1c4fad1b5)
- [drv_type_a_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a43086e5bc5d6384b8eb0709c1cf1756e)
- [drv_type_c_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#aafcfb75fd131430df0a372e6ac2c8b34)
- [drv_type_d_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#ad2c9e66bbd9a442d872fd559fd7a833c)
- [retune_timer_count](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#ab7a145bf44747d7d9e68ff743520cc2c)
- [sdr50_needs_tuning](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#ac54a191e04ff6c266390d1fb8d4f84d3)
- [retuning_mode](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a48680d522d417e68ec3371b3831faa01)
- [clk_multiplier](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#afffade3ad661ead23ed0f74b770172ff)
- [adma3_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a90a90218bcd866cbfae2354c5b0af3de)
- [vdd2_180_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a2f5d5859cbe06ab449f95c0a108c2250)
- [sdhc_io](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md)
- [sdhc_clock_speed](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a9660a61775e481ae4093e11ce9336539)
- [clock](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#aaa15197b8f1947a67dcd8522aa62afc5)
- [bus_mode](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#a2b4456b108778aada0d42b8c8107b3e9)
- [power_mode](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#ac503fb9fba7ffdb01695a77780972930)
- [bus_width](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#a904b05c7e73e80bb7326b0bfcb6b7103)
- [timing](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#a85c50f625d8606bb4c07a228c0de24e4)
- [enhanced_strobe](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#afa9a07a8734e9d39b29da0697cf60289)
- [sd_driver_type](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a314c38b1b0603c003e67b5dec2228d4b)
- [driver_type](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#a0c62aaa1a8a7700ebb00a38ce2e57d11)
- [signal_voltage](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#ade8b8cd4e4f4b21f5fa8e3fb2661917e)
- [sdhc_host_props](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md)
- [f_max](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#aef7123dfa5690bc0525aa40dc623307c)
- [f_min](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#a28c69ba3fdae1393daa551f3f9b91057)
- [power_delay](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#a7f7b22b7b8fb46df0ec19e2bef2a4702)
- [host_caps](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#ad60bf89e594a031f6be015888466a113)
- [max_current_330](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#afebe4aad820c1672635fd30aacec20e4)
- [max_current_300](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#ac247312c9b10768fe878afc5c85d9eba)
- [max_current_180](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#a43d2b80ec0a5682783e4297c734a3c88)
- [bus_4_bit_support](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#a4a6ebccaddfc4bb99b0bbb628ffabb21)
- [hs200_support](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#a6401a11a8ac85cf3951ec138173f87b7)
- [hs400_support](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#aec7874d1012fe5fb881c3ca5e913391e)
- [hs400_enhanced_strobe_support](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#a7af8f0a9564db9ef0630a8bc85ac34a9)
- [is_spi](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#abb18e33d99ed1e4a4400dccd2149816f)
- [sdhc_interrupt_source](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gab449b2f6b41e791d327f7d92b2b58c2d)
- [SDHC_INT_SDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggab449b2f6b41e791d327f7d92b2b58c2dae3a741e98cdb1e8c0ddc8c3baaf64b59)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SDHC_INT_INSERTED](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggab449b2f6b41e791d327f7d92b2b58c2dab9df16a6ed1c7961bb9cab34ebe99f87)
- [SDHC_INT_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggab449b2f6b41e791d327f7d92b2b58c2da6e0a03105c6aba203daa53acb6b7c15c)
- [sdhc_interrupt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga5d207e3b3d76ed9dbfa7d68a92755cbe)
- [device](../device_reference/P002_设备对象结构.md)
- [sdhc_driver_api](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md)
- [reset](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#ac034dfc17e064170e76280394005c76c)
- [request](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#a577d162b282b2f9eeb91cf07e7578905)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [set_io](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#adb40a93f64a1a8dc1548a4651091ecf9)
- [get_card_present](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#a06fb6fdfd0c528056c36476f914f94c9)
- [execute_tuning](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#a6075f8ef38200e700ec133fbeb8c8121)
- [card_busy](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#ac642c06d5ec9f697be8fa46cede3bc64)
- [get_host_props](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#af2b83b0ea2afbbdf065b5919c6b822c2)
- [enable_interrupt](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#a42941f226f2adfe5b8275923bff434ff)
- [disable_interrupt](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#aa50466e31e01d639e459bab204cf1ee5)
- [sdhc_hw_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad6b082a75f1272620b79a7d3a08862f7)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [sdhc_request](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gac708d55e92a7705f92b90ee6baa65f74)
- [sdhc_set_io](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga0e6d8259cca442bd1356d00f668d35c4)
- [sdhc_card_present](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga85184688da845759dbfb706aac5eac7d)
- [sdhc_execute_tuning](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gab5c2711c99573e031938faaa41862971)
- [sdhc_card_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga91acdc4a6bc2aecc988fdde6ee61ed46)
- [sdhc_get_host_props](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gab55cf88ae79e5aa9e2110b298048df8e)
- [sdhc_enable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga8e4beb1135aa5c0d32f999ca953224d2)
- [sdhc_disable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga6264f62c6427973749c8d49fb908f569)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [sd_spec.h](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md)
- [sdhc_command::opcode](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md#a320ad415df67e1d9b4c09f95993dd17f)
- [sdhc_command::response](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md#a37a3c1608b5c13311c833c4ad24ff1f9)
- [sdhc_command::retries](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md#a39ba0b1e99814471939dc7bbb7d098eb)
- [sdhc_command::timeout_ms](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md#a92cf023d28aa6106d603ff7f67a7e04b)
- [sdhc_command::arg](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md#af6b98d5f1cecf25af2480b1d359f200e)
- [sdhc_command::response_type](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md#af758a4e0e3b090912f6e9abd7c4be8f3)
- [sdhc_data::data](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#a0f656d093a5cdf3bd09ffee279ad452d)
- [sdhc_data::block_size](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#a20b0ca14adadcdb8d3681240faf5e7b6)
- [sdhc_data::blocks](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#a47b378d455167bb8d7d05d2f058977fa)
- [sdhc_data::is_sg_data](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#a4f7ca31c9cee1ace999a46cce75b9f65)
- [sdhc_data::block_addr](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#aad1e8462d94b4243c981147eab6c962d)
- [sdhc_data::bytes_xfered](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#ae68f1e7f1fbff14c24bd42fa300f9e15)
- [sdhc_data::timeout_ms](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md#afcf3942de27cd164b6da8dfefa864a8a)
- [sdhc_driver_api::get_card_present](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#a06fb6fdfd0c528056c36476f914f94c9)
- [sdhc_driver_api::enable_interrupt](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#a42941f226f2adfe5b8275923bff434ff)
- [sdhc_driver_api::request](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#a577d162b282b2f9eeb91cf07e7578905)
- [sdhc_driver_api::execute_tuning](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#a6075f8ef38200e700ec133fbeb8c8121)
- [sdhc_driver_api::disable_interrupt](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#aa50466e31e01d639e459bab204cf1ee5)
- [sdhc_driver_api::reset](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#ac034dfc17e064170e76280394005c76c)
- [sdhc_driver_api::card_busy](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#ac642c06d5ec9f697be8fa46cede3bc64)
- [sdhc_driver_api::set_io](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#adb40a93f64a1a8dc1548a4651091ecf9)
- [sdhc_driver_api::get_host_props](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md#af2b83b0ea2afbbdf065b5919c6b822c2)
- [sdhc_host_caps::address_64_bit_support_v3](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a0f33c7e168ade12675795d2c0d5b5ea2)
- [sdhc_host_caps::uhs_2_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a146c7403d7ecbbffbd6aa0c1c4fad1b5)
- [sdhc_host_caps::sd_base_clk](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a20ada015fecce002d233fefac5c4ead4)
- [sdhc_host_caps::sdma_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a22f2877854669589f0483cf91e504df6)
- [sdhc_host_caps::vdd2_180_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a2f5d5859cbe06ab449f95c0a108c2250)
- [sdhc_host_caps::slot_type](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a3231007bc5fcc731e97236b29333f7ee)
- [sdhc_host_caps::timeout_clk_freq](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a3a57e12aa8f53ad1c1fb44696622f587)
- [sdhc_host_caps::sdr104_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a3e6f73ea9df9c207cddda31de45621be)
- [sdhc_host_caps::drv_type_a_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a43086e5bc5d6384b8eb0709c1cf1756e)
- [sdhc_host_caps::retuning_mode](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a48680d522d417e68ec3371b3831faa01)
- [sdhc_host_caps::sdr50_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a63dabbc7c24dc41c8103be81ee6e673f)
- [sdhc_host_caps::sdio_async_interrupt_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a6fa0525ee3b2a0313cc9b83dc820b831)
- [sdhc_host_caps::vol_300_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a7fdf6832fbcc9dce7e20ee87d9063665)
- [sdhc_host_caps::timeout_clk_unit](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a8af558ed3b7af437f1782aea9ee6794e)
- [sdhc_host_caps::adma3_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a90a90218bcd866cbfae2354c5b0af3de)
- [sdhc_host_caps::max_blk_len](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#a97dbad3360b56a44fb1ab0d77aa90bc4)
- [sdhc_host_caps::ddr50_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#aa22adb0079aa3864df4461d841852684)
- [sdhc_host_caps::vol_180_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#aa39ef2d70314dbf2517bd3df6fbd4694)
- [sdhc_host_caps::high_spd_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#aaec0cd01cc4e8bf334e5c3ee151d5d98)
- [sdhc_host_caps::drv_type_c_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#aafcfb75fd131430df0a372e6ac2c8b34)
- [sdhc_host_caps::retune_timer_count](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#ab7a145bf44747d7d9e68ff743520cc2c)
- [sdhc_host_caps::sdr50_needs_tuning](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#ac54a191e04ff6c266390d1fb8d4f84d3)
- [sdhc_host_caps::vol_330_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#ac6e2eb088ed7d7c3f3f5011ad55ba543)
- [sdhc_host_caps::adma_2_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#acfa1c5e96f2afeab40185a1ef37d7efb)
- [sdhc_host_caps::bus_8_bit_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#ad09f103fc8ce341d25e1f824e97bd665)
- [sdhc_host_caps::drv_type_d_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#ad2c9e66bbd9a442d872fd559fd7a833c)
- [sdhc_host_caps::address_64_bit_support_v4](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#ad8e4ca0d2fb39486b469224218d2eb7b)
- [sdhc_host_caps::suspend_res_support](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#af343879ebc21f5c2d57ffa962dacb796)
- [sdhc_host_caps::clk_multiplier](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md#afffade3ad661ead23ed0f74b770172ff)
- [sdhc_host_props::f_min](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#a28c69ba3fdae1393daa551f3f9b91057)
- [sdhc_host_props::max_current_180](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#a43d2b80ec0a5682783e4297c734a3c88)
- [sdhc_host_props::bus_4_bit_support](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#a4a6ebccaddfc4bb99b0bbb628ffabb21)
- [sdhc_host_props::hs200_support](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#a6401a11a8ac85cf3951ec138173f87b7)
- [sdhc_host_props::hs400_enhanced_strobe_support](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#a7af8f0a9564db9ef0630a8bc85ac34a9)
- [sdhc_host_props::power_delay](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#a7f7b22b7b8fb46df0ec19e2bef2a4702)
- [sdhc_host_props::is_spi](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#abb18e33d99ed1e4a4400dccd2149816f)
- [sdhc_host_props::max_current_300](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#ac247312c9b10768fe878afc5c85d9eba)
- [sdhc_host_props::host_caps](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#ad60bf89e594a031f6be015888466a113)
- [sdhc_host_props::hs400_support](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#aec7874d1012fe5fb881c3ca5e913391e)
- [sdhc_host_props::f_max](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#aef7123dfa5690bc0525aa40dc623307c)
- [sdhc_host_props::max_current_330](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md#afebe4aad820c1672635fd30aacec20e4)
- [sdhc_io::driver_type](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#a0c62aaa1a8a7700ebb00a38ce2e57d11)
- [sdhc_io::bus_mode](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#a2b4456b108778aada0d42b8c8107b3e9)
- [sdhc_io::timing](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#a85c50f625d8606bb4c07a228c0de24e4)
- [sdhc_io::bus_width](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#a904b05c7e73e80bb7326b0bfcb6b7103)
- [sdhc_io::clock](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#aaa15197b8f1947a67dcd8522aa62afc5)
- [sdhc_io::power_mode](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#ac503fb9fba7ffdb01695a77780972930)
- [sdhc_io::signal_voltage](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#ade8b8cd4e4f4b21f5fa8e3fb2661917e)
- [sdhc_io::enhanced_strobe](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md#afa9a07a8734e9d39b29da0697cf60289)

---

[上一章](P024_zephyr__sd__sd.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__drivers__sent__sent.h_头文件源码.md)
