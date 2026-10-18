---
id: learning.zephyr-docs.api-source-reference.page-120
title: dai.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dai_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第120章\_dai.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dai_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dai_8h.html)。

## 120.1\_原始可见代码（Source Code）

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
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00103"></a>
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
<a id="foldopen00128"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00168"></a>
<a id="l00174"></a>
<a id="l00184"></a>
<a id="l00192"></a>
<a id="l00198"></a>
<a id="l00207"></a>
<a id="l00214"></a>
<a id="l00220"></a>
<a id="l00226"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="foldopen00240"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="foldopen00257"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="foldopen00283"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="foldopen00303"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00317"></a>
<a id="foldopen00321"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00325"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00343"></a>
<a id="l00345"></a>
<a id="l00347"></a>
<a id="l00349"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00355"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
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
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="foldopen00448"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
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
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__dai__interface_html_ga040f4515aa67efb3a840b9b5e323d016"></a>
<a id="agroup__dai__interface_html_ga0b27e890e1612a8afaa7b59d5293dc51"></a>
<a id="agroup__dai__interface_html_ga0be1a87283a39f697e1eb4b4ab4bcdfe"></a>
<a id="agroup__dai__interface_html_ga18f708594ea85d6b893906336047c3a5"></a>
<a id="agroup__dai__interface_html_ga1adb2bf389fea3483361eaea078a7262"></a>
<a id="agroup__dai__interface_html_ga222336d75578f180ccf7f46f977fc12c"></a>
<a id="agroup__dai__interface_html_ga28ecaa76e8c6f4c32ffec6d6368bada0"></a>
<a id="agroup__dai__interface_html_ga3fa4c114ad6a3dd6a6015b6ab3d119a2"></a>
<a id="agroup__dai__interface_html_ga6588501e0369ddf1bc4c04a2e293bc2b"></a>
<a id="agroup__dai__interface_html_ga6d98d1f42bcaba0eefef41bc96a04bc5"></a>
<a id="agroup__dai__interface_html_ga840116b8b56fd0263a17791e7156975d"></a>
<a id="agroup__dai__interface_html_ga8e0fa728ad9353ed008ba293808ab371"></a>
<a id="agroup__dai__interface_html_gac732c8b3e737ecca187f38e308d95724"></a>
<a id="agroup__dai__interface_html_gac95242d83a2c2b477fcb9eb3da420797"></a>
<a id="agroup__dai__interface_html_gae6cf280d796744e2626e7b706af89003"></a>
<a id="agroup__dai__interface_html_gae6f142de581bbf17fa31cc9cefb695c6"></a>
<a id="agroup__dai__interface_html_gaee6445967afb3ecf2c0470ca0c104a1a"></a>
<a id="agroup__dai__interface_html_gaf66ca0bbc1f8ba2f2b81caf92bd09b60"></a>
<a id="agroup__dai__interface_html_gafa7b22e4250c6479301fc657fea8a60f"></a>
<a id="agroup__dai__interface_html_gga18f708594ea85d6b893906336047c3a5a095422b1a71b65e5a5902e0ca5cd3650"></a>
<a id="agroup__dai__interface_html_gga18f708594ea85d6b893906336047c3a5a234306cd9cc97674455f8a9321834953"></a>
<a id="agroup__dai__interface_html_gga18f708594ea85d6b893906336047c3a5a5030da046fda46120d9b54a686fb35ef"></a>
<a id="agroup__dai__interface_html_gga18f708594ea85d6b893906336047c3a5a8486be6ff6f6bf91ee4a8ad632377987"></a>
<a id="agroup__dai__interface_html_gga18f708594ea85d6b893906336047c3a5a8692bbb3fce619aec3dfe5ed9697f73f"></a>
<a id="agroup__dai__interface_html_gga18f708594ea85d6b893906336047c3a5aba10f89376d67abdc3dc704c6b283d2b"></a>
<a id="agroup__dai__interface_html_gga18f708594ea85d6b893906336047c3a5acb4e0c1f9df9eb0b7cf965b710a2ad13"></a>
<a id="agroup__dai__interface_html_gga3fa4c114ad6a3dd6a6015b6ab3d119a2a0d0f5db48e33cef8aa6c59a00792866b"></a>
<a id="agroup__dai__interface_html_gga3fa4c114ad6a3dd6a6015b6ab3d119a2a3235bf6888b65c9c6e3a0d2f95fc0758"></a>
<a id="agroup__dai__interface_html_gga3fa4c114ad6a3dd6a6015b6ab3d119a2a6ffdc334c0f64feeb95297293f747bc3"></a>
<a id="agroup__dai__interface_html_gga3fa4c114ad6a3dd6a6015b6ab3d119a2a9ed5273ee9ea0761ccf9cbc7f7295a3f"></a>
<a id="agroup__dai__interface_html_gga3fa4c114ad6a3dd6a6015b6ab3d119a2adf515857c95ea685a32bf18c0ebb9af2"></a>
<a id="agroup__dai__interface_html_gga3fa4c114ad6a3dd6a6015b6ab3d119a2aea1fd67c47f7d8d7e3ca18b2f2e806a0"></a>
<a id="agroup__dai__interface_html_gga840116b8b56fd0263a17791e7156975da347440e41adadd2b6a91076f53abe2e3"></a>
<a id="agroup__dai__interface_html_gga840116b8b56fd0263a17791e7156975da4baee3a3ab87e540b5f4caf26e8d8c4b"></a>
<a id="agroup__dai__interface_html_gga840116b8b56fd0263a17791e7156975da9f8f99d63e607d9603f54d535bd89f84"></a>
<a id="agroup__dai__interface_html_gga840116b8b56fd0263a17791e7156975daf4862a3af6fb46f6ac9ffc0cdbbcf0a1"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a15cf161a5126110860c89ce9a118045b"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a19dd111b0d7f7772415bc60c1256d141"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a1a591d4c0b7a70e175fc967b59929326"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a2560d8f844796f647ed774748c44adfe"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a2a12c2858722c553cb31f24aacd83976"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a366db52bd49557d047f091cdb96b5e36"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a37f79dfe1804d4abeb89a9767bf37c75"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a3d759f9665a4db0c974913c4aa71e6f2"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a6c0c4b31c71c9e779a2a9325dc119fd0"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a6d88cd52faa8d93716f81d68fabb794d"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a75bfaa3859321a283929ae033fcf22aa"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a8d75b1d72f5fcff348c15281001f9aaa"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797a9301e2ec67fa75aefc0e59df727adcc9"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797aa94ef995d95f9d0ad8b404e26b79faec"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797ab63816ace8bc3fc6f35d0435fd37931e"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797ab675d7b5204a2cbc09f1f60a44f4ff3b"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797ac5095e399162d248e638b87a61b59a00"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797ae58e4acd79cd16d98976fef1978a231c"></a>
<a id="agroup__dai__interface_html_ggac95242d83a2c2b477fcb9eb3da420797afd1f617fdd16363c1a10e9f45a67a99b"></a>
<a id="agroup__dai__interface_html_ggaee6445967afb3ecf2c0470ca0c104a1aa1c17da0f6a54c2c25f2dd2349b5c0e02"></a>
<a id="agroup__dai__interface_html_ggaee6445967afb3ecf2c0470ca0c104a1aa1f004f7d4dcb67d2c3a89298400b2234"></a>
<a id="agroup__dai__interface_html_ggaee6445967afb3ecf2c0470ca0c104a1aa23dd7f534a18f92cbf12ad957674ba35"></a>
<a id="agroup__dai__interface_html_ggaee6445967afb3ecf2c0470ca0c104a1aa6720f67f3bc6ab62eacf986316df0a9f"></a>
<a id="agroup__dai__interface_html_ggaee6445967afb3ecf2c0470ca0c104a1aabcbb4f151183d54d51dde07d09b3f222"></a>
<a id="agroup__dai__interface_html_ggaee6445967afb3ecf2c0470ca0c104a1aac7647bb0111f043abcdaa4b3e703b2ec"></a>
<a id="agroup__dai__interface_html_ggaee6445967afb3ecf2c0470ca0c104a1aad2fcfa3c229bfc0a82ec7841ab9f88c3"></a>
<a id="agroup__dai__interface_html_ggaee6445967afb3ecf2c0470ca0c104a1aad9d4e12f62ee2e106abaeb3bb341ee70"></a>
<a id="agroup__dai__interface_html_ggaee6445967afb3ecf2c0470ca0c104a1aadb17f3981cf0e248187c4006f527a3a5"></a>
<a id="agroup__dai__interface_html_ggaee6445967afb3ecf2c0470ca0c104a1aafa607dff411961ae22e44f1a972c4711"></a>
<a id="agroup__dai__interface_html_ggaf66ca0bbc1f8ba2f2b81caf92bd09b60a35606eb43c6d77204bff029bfab37698"></a>
<a id="agroup__dai__interface_html_ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ab35554010caadb69a5414c7f07649ee1"></a>
<a id="agroup__dai__interface_html_ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ad6622f24986622cf16fdeada99356c43"></a>
<a id="agroup__dai__interface_html_ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ae0a56f8334363d4a1aa916ffe5d70e5c"></a>
<a id="agroup__dai__interface_html_ggafa7b22e4250c6479301fc657fea8a60fa48cc817cda4907b94a03e13e8b9aa69b"></a>
<a id="agroup__dai__interface_html_ggafa7b22e4250c6479301fc657fea8a60fa58581d875a6a8c28adb0f6351a37f3e1"></a>
<a id="agroup__dai__interface_html_ggafa7b22e4250c6479301fc657fea8a60fadfdf2212e2d86296dbccc60cfd60368c"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdai__config_html"></a>
<a id="astructdai__config_html_a2d46087a3c94845d52b44386dd20cfc0"></a>
<a id="astructdai__config_html_a32830675c7bf7125c5006579d33e5e96"></a>
<a id="astructdai__config_html_ac2c2c4a39bfe917d5a784d8bc596eb10"></a>
<a id="astructdai__config_html_ac3f39c351ad9659356ad5ad4306585b8"></a>
<a id="astructdai__config_html_ac8b2936e194421f95d03e1c595017306"></a>
<a id="astructdai__config_html_acfb621417b789c71608ad50d0b54c1f6"></a>
<a id="astructdai__config_html_aecb9fe475d71d55d8b19eb3faa697606"></a>
<a id="astructdai__config_html_af3c768d9597298cea94bbdd6e5b5c4f3"></a>
<a id="astructdai__config_html_afd3bcee428b5359b7151a269973049a1"></a>
<a id="astructdai__config_html_afe7ab1b6c1163ca1bf4141bc6f2439ba"></a>
<a id="astructdai__driver__api_html"></a>
<a id="astructdai__driver__api_html_a0a59502c00c154c199f42e78cbd7d6b3"></a>
<a id="astructdai__driver__api_html_a22f84e02f1eb735075498066d62a08d3"></a>
<a id="astructdai__driver__api_html_a3cfd0430d2fdb7c7ab5719c142b9b7a4"></a>
<a id="astructdai__driver__api_html_a3ff217a5967a2b6657b01b766a7061b2"></a>
<a id="astructdai__driver__api_html_a4462ee3f3a8faab6b37454fae903ae01"></a>
<a id="astructdai__driver__api_html_a4610c94767bfb81ed6d601aa44f1596b"></a>
<a id="astructdai__driver__api_html_a5dbed6fe2ab663ef97dd4aea7e4ef1df"></a>
<a id="astructdai__driver__api_html_a6d6ca0c0a5cefda514dc23d3e61d6590"></a>
<a id="astructdai__driver__api_html_ac0f88957ca2fe0bfc7b9e1eca5f81f1e"></a>
<a id="astructdai__driver__api_html_ad2de08427255233cceaa7a2f0c2ba200"></a>
<a id="astructdai__driver__api_html_aed9c7791a77f71f68174ab02b85eebf8"></a>
<a id="astructdai__properties_html"></a>
<a id="astructdai__properties_html_a7203f5c97aaf8f48f9eb51d88424afce"></a>
<a id="astructdai__properties_html_a8fc2d359fe889b3a46ecc8918a82f680"></a>
<a id="astructdai__properties_html_a98053c85634b80b144bda05d83f2eb7e"></a>
<a id="astructdai__properties_html_a9b056f0ff59b473d3040851642d1601c"></a>
<a id="astructdai__properties_html_adab0f1199c7169a521329adc98c2f0ac"></a>
<a id="astructdai__ts__cfg_html"></a>
<a id="astructdai__ts__cfg_html_a2b0be9c840de941e4a87c422fa82356d"></a>
<a id="astructdai__ts__cfg_html_a37c6379686435994b9050d1e9c249756"></a>
<a id="astructdai__ts__cfg_html_aa87fc1e3072490e44f65bc7690f85ce8"></a>
<a id="astructdai__ts__cfg_html_ab874249dcb9377fafa35764b4f1c0ea0"></a>
<a id="astructdai__ts__cfg_html_ac17d3da9de6d860f2fa04286a4c43a1d"></a>
<a id="astructdai__ts__cfg_html_afdaf1a4ef6a00201b3790187ec44370f"></a>
<a id="astructdai__ts__cfg_html_aff3dc52737d1261cd56c084c104691eb"></a>
<a id="astructdai__ts__data_html"></a>
<a id="astructdai__ts__data_html_a11133d72485786e75a9d94f218fe699b"></a>
<a id="astructdai__ts__data_html_a933cbc19cc837683581db806702fba36"></a>
<a id="astructdai__ts__data_html_ace2686aa6ff5aed346705cbb0d198d36"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2022 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_DAI_H_
#define ZEPHYR_INCLUDE_DRIVERS_DAI_H_


#include <errno.h>

#include <zephyr/types.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

#define DAI_FORMAT_CLOCK_PROVIDER_MASK  0xf000
#define DAI_FORMAT_PROTOCOL_MASK        0x000f
#define DAI_FORMAT_CLOCK_INVERSION_MASK 0x0f00

enum dai_clock_provider {
        DAI_CBP_CFP = (0 << 12),
        DAI_CBC_CFP = (2 << 12),
        DAI_CBP_CFC = (3 << 12),
        DAI_CBC_CFC = (4 << 12),
};

enum dai_protocol {
        DAI_PROTO_I2S = 1,
        DAI_PROTO_RIGHT_J,
        DAI_PROTO_LEFT_J,
        DAI_PROTO_DSP_A,
        DAI_PROTO_DSP_B,
        DAI_PROTO_PDM,
};

enum dai_clock_inversion {
        DAI_INVERSION_NB_NF = 0,
        DAI_INVERSION_NB_IF = (2 << 8),
        DAI_INVERSION_IB_NF = (3 << 8),
        DAI_INVERSION_IB_IF = (4 << 8),
};

enum dai_type {
        DAI_LEGACY_I2S = 0,
        DAI_INTEL_SSP,
        DAI_INTEL_DMIC,
        DAI_INTEL_HDA,
        DAI_INTEL_ALH,
        DAI_IMX_SAI,
        DAI_IMX_ESAI,
        DAI_AMD_BT,
        DAI_AMD_SP,
        DAI_AMD_DMIC,
        DAI_MEDIATEK_AFE,
        DAI_INTEL_SSP_NHLT,
        DAI_INTEL_DMIC_NHLT,
        DAI_INTEL_HDA_NHLT,
        DAI_INTEL_ALH_NHLT,
        DAI_IMX_MICFIL,
        DAI_INTEL_UAOL,
        DAI_AMD_SDW,
        DAI_AMD_TDM,
};

enum dai_dir {
        DAI_DIR_TX = 0,
        DAI_DIR_RX,
        DAI_DIR_BOTH,
};

enum dai_state {
        DAI_STATE_NOT_READY = 0,
        DAI_STATE_READY,
        DAI_STATE_RUNNING,
        DAI_STATE_PRE_RUNNING,
        DAI_STATE_PAUSED,
        DAI_STATE_STOPPING,
        DAI_STATE_ERROR,
};

enum dai_trigger_cmd {
        DAI_TRIGGER_START = 0,
        DAI_TRIGGER_PRE_START,
        DAI_TRIGGER_STOP,
        DAI_TRIGGER_PAUSE,
        DAI_TRIGGER_POST_STOP,
        DAI_TRIGGER_DRAIN,
        DAI_TRIGGER_DROP,
        DAI_TRIGGER_PREPARE,
        DAI_TRIGGER_RESET,
        DAI_TRIGGER_COPY,
};

struct dai_properties {
        uint32_t fifo_address;
        uint32_t fifo_depth;
        uint32_t dma_hs_id;
        uint32_t reg_init_delay;
        int stream_id;
};

struct dai_config {
        enum dai_type type;
        uint32_t dai_index;
        uint8_t channels;
        uint32_t rate;
        uint16_t format;
        uint8_t options;
        uint8_t word_size;
        size_t block_size;
        uint16_t link_config;
        uint32_t tdm_slot_group;
};

struct dai_ts_cfg {
        uint32_t walclk_rate;
        int type;
        int direction;
        int index;
        int dma_id;
        int dma_chan_index;
        int dma_chan_count;
};

struct dai_ts_data {
        uint64_t walclk;
        uint64_t sample;
        uint32_t walclk_rate;
};


__subsystem struct dai_driver_api {
        int (*probe)(const struct device *dev);
        int (*remove)(const struct device *dev);
        int (*config_set)(const struct device *dev, const struct dai_config *cfg,
                          const void *bespoke_cfg, size_t size);
        int (*config_get)(const struct device *dev, struct dai_config *cfg, enum dai_dir dir);

        const struct dai_properties *(*get_properties)(const struct device *dev, enum dai_dir dir,
                                                       int stream_id);
        int (*get_properties_copy)(const struct device *dev, enum dai_dir dir, int stream_id,
                                   struct dai_properties *dst);

        int (*trigger)(const struct device *dev, enum dai_dir dir, enum dai_trigger_cmd cmd);

        int (*ts_config)(const struct device *dev, struct dai_ts_cfg *cfg);
        int (*ts_start)(const struct device *dev, struct dai_ts_cfg *cfg);
        int (*ts_stop)(const struct device *dev, struct dai_ts_cfg *cfg);
        int (*ts_get)(const struct device *dev, struct dai_ts_cfg *cfg, struct dai_ts_data *tsd);
        int (*config_update)(const struct device *dev, const void *bespoke_cfg, size_t size);
};


__syscall int dai_probe(const struct device *dev);

static inline int z_impl_dai_probe(const struct device *dev)
{
        return DEVICE_API_GET(dai, dev)->probe(dev);
}

__syscall int dai_remove(const struct device *dev);

static inline int z_impl_dai_remove(const struct device *dev)
{
        return DEVICE_API_GET(dai, dev)->remove(dev);
}


__syscall int dai_config_set(const struct device *dev, const struct dai_config *cfg,
                             const void *bespoke_cfg, size_t size);

static inline int z_impl_dai_config_set(const struct device *dev, const struct dai_config *cfg,
                                        const void *bespoke_cfg, size_t size)
{
        return DEVICE_API_GET(dai, dev)->config_set(dev, cfg, bespoke_cfg, size);
}

__syscall int dai_config_get(const struct device *dev, struct dai_config *cfg, enum dai_dir dir);

static inline int z_impl_dai_config_get(const struct device *dev, struct dai_config *cfg,
                                        enum dai_dir dir)
{
        return DEVICE_API_GET(dai, dev)->config_get(dev, cfg, dir);
}

static inline const struct dai_properties *dai_get_properties(const struct device *dev,
                                                              enum dai_dir dir, int stream_id)
{
        return DEVICE_API_GET(dai, dev)->get_properties(dev, dir, stream_id);
}

__syscall int dai_get_properties_copy(const struct device *dev, enum dai_dir dir, int stream_id,
                                      struct dai_properties *dst);

static inline int z_impl_dai_get_properties_copy(const struct device *dev, enum dai_dir dir,
                                                 int stream_id, struct dai_properties *dst)
{
        const struct dai_driver_api *api = DEVICE_API_GET(dai, dev);

        if (!api->get_properties_copy) {
                return -ENOSYS;
        }

        return api->get_properties_copy(dev, dir, stream_id, dst);
}

__syscall int dai_trigger(const struct device *dev, enum dai_dir dir, enum dai_trigger_cmd cmd);

static inline int z_impl_dai_trigger(const struct device *dev, enum dai_dir dir,
                                     enum dai_trigger_cmd cmd)
{
        return DEVICE_API_GET(dai, dev)->trigger(dev, dir, cmd);
}

__syscall int dai_ts_config(const struct device *dev, struct dai_ts_cfg *cfg);

static inline int z_impl_dai_ts_config(const struct device *dev, struct dai_ts_cfg *cfg)
{
        const struct dai_driver_api *api = DEVICE_API_GET(dai, dev);

        if (!api->ts_config) {
                return -EINVAL;
        }

        return api->ts_config(dev, cfg);
}

__syscall int dai_ts_start(const struct device *dev, struct dai_ts_cfg *cfg);

static inline int z_impl_dai_ts_start(const struct device *dev, struct dai_ts_cfg *cfg)
{
        const struct dai_driver_api *api = DEVICE_API_GET(dai, dev);

        if (!api->ts_start) {
                return -EINVAL;
        }

        return api->ts_start(dev, cfg);
}

__syscall int dai_ts_stop(const struct device *dev, struct dai_ts_cfg *cfg);

static inline int z_impl_dai_ts_stop(const struct device *dev, struct dai_ts_cfg *cfg)
{
        const struct dai_driver_api *api = DEVICE_API_GET(dai, dev);

        if (!api->ts_stop) {
                return -EINVAL;
        }

        return api->ts_stop(dev, cfg);
}

__syscall int dai_ts_get(const struct device *dev, struct dai_ts_cfg *cfg, struct dai_ts_data *tsd);

static inline int z_impl_dai_ts_get(const struct device *dev, struct dai_ts_cfg *cfg,
                                    struct dai_ts_data *tsd)
{
        const struct dai_driver_api *api = DEVICE_API_GET(dai, dev);

        if (!api->ts_get) {
                return -EINVAL;
        }

        return api->ts_get(dev, cfg, tsd);
}

__syscall int dai_config_update(const struct device *dev, const void *bespoke_cfg, size_t size);

static inline int z_impl_dai_config_update(const struct device *dev, const void *bespoke_cfg,
                                           size_t size)
{
        const struct dai_driver_api *api = DEVICE_API_GET(dai, dev);

        if (!api->config_update) {
                return -ENOSYS;
        }

        return api->config_update(dev, bespoke_cfg, size);
}


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/dai.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_DAI_H_ */
```

## 120.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 642 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DAI_H_`。

## 120.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dai_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [dai_clock_provider](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga840116b8b56fd0263a17791e7156975d)
- [DAI_CBP_CFP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga840116b8b56fd0263a17791e7156975da347440e41adadd2b6a91076f53abe2e3)
- [DAI_CBC_CFP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga840116b8b56fd0263a17791e7156975daf4862a3af6fb46f6ac9ffc0cdbbcf0a1)
- [DAI_CBP_CFC](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga840116b8b56fd0263a17791e7156975da4baee3a3ab87e540b5f4caf26e8d8c4b)
- [DAI_CBC_CFC](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga840116b8b56fd0263a17791e7156975da9f8f99d63e607d9603f54d535bd89f84)
- [dai_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga3fa4c114ad6a3dd6a6015b6ab3d119a2)
- [DAI_PROTO_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2adf515857c95ea685a32bf18c0ebb9af2)
- [DAI_PROTO_RIGHT_J](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a9ed5273ee9ea0761ccf9cbc7f7295a3f)
- [DAI_PROTO_LEFT_J](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a0d0f5db48e33cef8aa6c59a00792866b)
- [DAI_PROTO_DSP_A](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a6ffdc334c0f64feeb95297293f747bc3)
- [DAI_PROTO_DSP_B](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2aea1fd67c47f7d8d7e3ca18b2f2e806a0)
- [DAI_PROTO_PDM](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a3235bf6888b65c9c6e3a0d2f95fc0758)
- [dai_clock_inversion](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gaf66ca0bbc1f8ba2f2b81caf92bd09b60)
- [DAI_INVERSION_NB_NF](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60a35606eb43c6d77204bff029bfab37698)
- [DAI_INVERSION_NB_IF](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ad6622f24986622cf16fdeada99356c43)
- [DAI_INVERSION_IB_NF](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ae0a56f8334363d4a1aa916ffe5d70e5c)
- [DAI_INVERSION_IB_IF](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ab35554010caadb69a5414c7f07649ee1)
- [dai_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gac95242d83a2c2b477fcb9eb3da420797)
- [DAI_LEGACY_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a2560d8f844796f647ed774748c44adfe)
- [DAI_INTEL_SSP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a9301e2ec67fa75aefc0e59df727adcc9)
- [DAI_INTEL_DMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a366db52bd49557d047f091cdb96b5e36)
- [DAI_INTEL_HDA](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a1a591d4c0b7a70e175fc967b59929326)
- [DAI_INTEL_ALH](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a19dd111b0d7f7772415bc60c1256d141)
- [DAI_IMX_SAI](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797aa94ef995d95f9d0ad8b404e26b79faec)
- [DAI_IMX_ESAI](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a75bfaa3859321a283929ae033fcf22aa)
- [DAI_AMD_BT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a6c0c4b31c71c9e779a2a9325dc119fd0)
- [DAI_AMD_SP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797ab675d7b5204a2cbc09f1f60a44f4ff3b)
- [DAI_AMD_DMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a37f79dfe1804d4abeb89a9767bf37c75)
- [DAI_MEDIATEK_AFE](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797ac5095e399162d248e638b87a61b59a00)
- [DAI_INTEL_SSP_NHLT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a8d75b1d72f5fcff348c15281001f9aaa)
- [DAI_INTEL_DMIC_NHLT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a3d759f9665a4db0c974913c4aa71e6f2)
- [DAI_INTEL_HDA_NHLT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797afd1f617fdd16363c1a10e9f45a67a99b)
- [DAI_INTEL_ALH_NHLT](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a2a12c2858722c553cb31f24aacd83976)
- [DAI_IMX_MICFIL](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a15cf161a5126110860c89ce9a118045b)
- [DAI_INTEL_UAOL](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797a6d88cd52faa8d93716f81d68fabb794d)
- [DAI_AMD_SDW](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797ae58e4acd79cd16d98976fef1978a231c)
- [DAI_AMD_TDM](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggac95242d83a2c2b477fcb9eb3da420797ab63816ace8bc3fc6f35d0435fd37931e)
- [dai_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gafa7b22e4250c6479301fc657fea8a60f)
- [DAI_DIR_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggafa7b22e4250c6479301fc657fea8a60fadfdf2212e2d86296dbccc60cfd60368c)
- [DAI_DIR_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggafa7b22e4250c6479301fc657fea8a60fa48cc817cda4907b94a03e13e8b9aa69b)
- [DAI_DIR_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggafa7b22e4250c6479301fc657fea8a60fa58581d875a6a8c28adb0f6351a37f3e1)
- [dai_state](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga18f708594ea85d6b893906336047c3a5)
- [DAI_STATE_NOT_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a8486be6ff6f6bf91ee4a8ad632377987)
- [DAI_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a095422b1a71b65e5a5902e0ca5cd3650)
- [DAI_STATE_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a8692bbb3fce619aec3dfe5ed9697f73f)
- [DAI_STATE_PRE_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a234306cd9cc97674455f8a9321834953)
- [DAI_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5acb4e0c1f9df9eb0b7cf965b710a2ad13)
- [DAI_STATE_STOPPING](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5aba10f89376d67abdc3dc704c6b283d2b)
- [DAI_STATE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gga18f708594ea85d6b893906336047c3a5a5030da046fda46120d9b54a686fb35ef)
- [dai_trigger_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gaee6445967afb3ecf2c0470ca0c104a1a)
- [DAI_TRIGGER_START](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aabcbb4f151183d54d51dde07d09b3f222)
- [DAI_TRIGGER_PRE_START](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aac7647bb0111f043abcdaa4b3e703b2ec)
- [DAI_TRIGGER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aa23dd7f534a18f92cbf12ad957674ba35)
- [DAI_TRIGGER_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aadb17f3981cf0e248187c4006f527a3a5)
- [DAI_TRIGGER_POST_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aad2fcfa3c229bfc0a82ec7841ab9f88c3)
- [DAI_TRIGGER_DRAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aa1c17da0f6a54c2c25f2dd2349b5c0e02)
- [DAI_TRIGGER_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aa1f004f7d4dcb67d2c3a89298400b2234)
- [DAI_TRIGGER_PREPARE](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aad9d4e12f62ee2e106abaeb3bb341ee70)
- [DAI_TRIGGER_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aafa607dff411961ae22e44f1a972c4711)
- [DAI_TRIGGER_COPY](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ggaee6445967afb3ecf2c0470ca0c104a1aa6720f67f3bc6ab62eacf986316df0a9f)
- [dai_properties](../audio_video_model_reference/P003_dai_properties_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [fifo_address](../audio_video_model_reference/P003_dai_properties_结构体.md#a98053c85634b80b144bda05d83f2eb7e)
- [fifo_depth](../audio_video_model_reference/P003_dai_properties_结构体.md#a9b056f0ff59b473d3040851642d1601c)
- [dma_hs_id](../audio_video_model_reference/P003_dai_properties_结构体.md#a7203f5c97aaf8f48f9eb51d88424afce)
- [reg_init_delay](../audio_video_model_reference/P003_dai_properties_结构体.md#a8fc2d359fe889b3a46ecc8918a82f680)
- [stream_id](../audio_video_model_reference/P003_dai_properties_结构体.md#adab0f1199c7169a521329adc98c2f0ac)
- [dai_config](../audio_video_model_reference/P001_dai_config_结构体.md)
- [type](../audio_video_model_reference/P001_dai_config_结构体.md#acfb621417b789c71608ad50d0b54c1f6)
- [dai_index](../audio_video_model_reference/P001_dai_config_结构体.md#aecb9fe475d71d55d8b19eb3faa697606)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [channels](../audio_video_model_reference/P001_dai_config_结构体.md#ac3f39c351ad9659356ad5ad4306585b8)
- [rate](../audio_video_model_reference/P001_dai_config_结构体.md#a2d46087a3c94845d52b44386dd20cfc0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [format](../audio_video_model_reference/P001_dai_config_结构体.md#ac2c2c4a39bfe917d5a784d8bc596eb10)
- [options](../audio_video_model_reference/P001_dai_config_结构体.md#ac8b2936e194421f95d03e1c595017306)
- [word_size](../audio_video_model_reference/P001_dai_config_结构体.md#afe7ab1b6c1163ca1bf4141bc6f2439ba)
- [block_size](../audio_video_model_reference/P001_dai_config_结构体.md#af3c768d9597298cea94bbdd6e5b5c4f3)
- [link_config](../audio_video_model_reference/P001_dai_config_结构体.md#afd3bcee428b5359b7151a269973049a1)
- [tdm_slot_group](../audio_video_model_reference/P001_dai_config_结构体.md#a32830675c7bf7125c5006579d33e5e96)
- [dai_ts_cfg](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md)
- [walclk_rate](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#ac17d3da9de6d860f2fa04286a4c43a1d)
- [type](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#a2b0be9c840de941e4a87c422fa82356d)
- [direction](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#afdaf1a4ef6a00201b3790187ec44370f)
- [index](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#aff3dc52737d1261cd56c084c104691eb)
- [dma_id](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#ab874249dcb9377fafa35764b4f1c0ea0)
- [dma_chan_index](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#aa87fc1e3072490e44f65bc7690f85ce8)
- [dma_chan_count](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#a37c6379686435994b9050d1e9c249756)
- [dai_ts_data](../audio_video_model_reference/P005_dai_ts_data_结构体.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [walclk](../audio_video_model_reference/P005_dai_ts_data_结构体.md#a11133d72485786e75a9d94f218fe699b)
- [sample](../audio_video_model_reference/P005_dai_ts_data_结构体.md#a933cbc19cc837683581db806702fba36)
- [walclk_rate](../audio_video_model_reference/P005_dai_ts_data_结构体.md#ace2686aa6ff5aed346705cbb0d198d36)
- [dai_driver_api](../audio_video_model_reference/P002_dai_driver_api_结构体.md)
- [probe](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a4462ee3f3a8faab6b37454fae903ae01)
- [device](../device_reference/P002_设备对象结构.md)
- [remove](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a0a59502c00c154c199f42e78cbd7d6b3)
- [config_set](../audio_video_model_reference/P002_dai_driver_api_结构体.md#aed9c7791a77f71f68174ab02b85eebf8)
- [config_get](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a6d6ca0c0a5cefda514dc23d3e61d6590)
- [get_properties_copy](../audio_video_model_reference/P002_dai_driver_api_结构体.md#ad2de08427255233cceaa7a2f0c2ba200)
- [trigger](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a3ff217a5967a2b6657b01b766a7061b2)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [ts_config](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a3cfd0430d2fdb7c7ab5719c142b9b7a4)
- [ts_start](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a22f84e02f1eb735075498066d62a08d3)
- [ts_stop](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a5dbed6fe2ab663ef97dd4aea7e4ef1df)
- [ts_get](../audio_video_model_reference/P002_dai_driver_api_结构体.md#ac0f88957ca2fe0bfc7b9e1eca5f81f1e)
- [config_update](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a4610c94767bfb81ed6d601aa44f1596b)
- [dai_probe](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga0be1a87283a39f697e1eb4b4ab4bcdfe)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [dai_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga28ecaa76e8c6f4c32ffec6d6368bada0)
- [dai_config_set](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga8e0fa728ad9353ed008ba293808ab371)
- [dai_config_get](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga0b27e890e1612a8afaa7b59d5293dc51)
- [dai_get_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gac732c8b3e737ecca187f38e308d95724)
- [dai_get_properties_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gae6f142de581bbf17fa31cc9cefb695c6)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [dai_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga6d98d1f42bcaba0eefef41bc96a04bc5)
- [dai_ts_config](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga222336d75578f180ccf7f46f977fc12c)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [dai_ts_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga1adb2bf389fea3483361eaea078a7262)
- [dai_ts_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga040f4515aa67efb3a840b9b5e323d016)
- [dai_ts_get](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#ga6588501e0369ddf1bc4c04a2e293bc2b)
- [dai_config_update](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html#gae6cf280d796744e2626e7b706af89003)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [dai_config::rate](../audio_video_model_reference/P001_dai_config_结构体.md#a2d46087a3c94845d52b44386dd20cfc0)
- [dai_config::tdm_slot_group](../audio_video_model_reference/P001_dai_config_结构体.md#a32830675c7bf7125c5006579d33e5e96)
- [dai_config::format](../audio_video_model_reference/P001_dai_config_结构体.md#ac2c2c4a39bfe917d5a784d8bc596eb10)
- [dai_config::channels](../audio_video_model_reference/P001_dai_config_结构体.md#ac3f39c351ad9659356ad5ad4306585b8)
- [dai_config::options](../audio_video_model_reference/P001_dai_config_结构体.md#ac8b2936e194421f95d03e1c595017306)
- [dai_config::type](../audio_video_model_reference/P001_dai_config_结构体.md#acfb621417b789c71608ad50d0b54c1f6)
- [dai_config::dai_index](../audio_video_model_reference/P001_dai_config_结构体.md#aecb9fe475d71d55d8b19eb3faa697606)
- [dai_config::block_size](../audio_video_model_reference/P001_dai_config_结构体.md#af3c768d9597298cea94bbdd6e5b5c4f3)
- [dai_config::link_config](../audio_video_model_reference/P001_dai_config_结构体.md#afd3bcee428b5359b7151a269973049a1)
- [dai_config::word_size](../audio_video_model_reference/P001_dai_config_结构体.md#afe7ab1b6c1163ca1bf4141bc6f2439ba)
- [dai_driver_api::remove](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a0a59502c00c154c199f42e78cbd7d6b3)
- [dai_driver_api::ts_start](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a22f84e02f1eb735075498066d62a08d3)
- [dai_driver_api::ts_config](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a3cfd0430d2fdb7c7ab5719c142b9b7a4)
- [dai_driver_api::trigger](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a3ff217a5967a2b6657b01b766a7061b2)
- [dai_driver_api::probe](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a4462ee3f3a8faab6b37454fae903ae01)
- [dai_driver_api::config_update](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a4610c94767bfb81ed6d601aa44f1596b)
- [dai_driver_api::ts_stop](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a5dbed6fe2ab663ef97dd4aea7e4ef1df)
- [dai_driver_api::config_get](../audio_video_model_reference/P002_dai_driver_api_结构体.md#a6d6ca0c0a5cefda514dc23d3e61d6590)
- [dai_driver_api::ts_get](../audio_video_model_reference/P002_dai_driver_api_结构体.md#ac0f88957ca2fe0bfc7b9e1eca5f81f1e)
- [dai_driver_api::get_properties_copy](../audio_video_model_reference/P002_dai_driver_api_结构体.md#ad2de08427255233cceaa7a2f0c2ba200)
- [dai_driver_api::config_set](../audio_video_model_reference/P002_dai_driver_api_结构体.md#aed9c7791a77f71f68174ab02b85eebf8)
- [dai_properties::dma_hs_id](../audio_video_model_reference/P003_dai_properties_结构体.md#a7203f5c97aaf8f48f9eb51d88424afce)
- [dai_properties::reg_init_delay](../audio_video_model_reference/P003_dai_properties_结构体.md#a8fc2d359fe889b3a46ecc8918a82f680)
- [dai_properties::fifo_address](../audio_video_model_reference/P003_dai_properties_结构体.md#a98053c85634b80b144bda05d83f2eb7e)
- [dai_properties::fifo_depth](../audio_video_model_reference/P003_dai_properties_结构体.md#a9b056f0ff59b473d3040851642d1601c)
- [dai_properties::stream_id](../audio_video_model_reference/P003_dai_properties_结构体.md#adab0f1199c7169a521329adc98c2f0ac)
- [dai_ts_cfg::type](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#a2b0be9c840de941e4a87c422fa82356d)
- [dai_ts_cfg::dma_chan_count](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#a37c6379686435994b9050d1e9c249756)
- [dai_ts_cfg::dma_chan_index](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#aa87fc1e3072490e44f65bc7690f85ce8)
- [dai_ts_cfg::dma_id](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#ab874249dcb9377fafa35764b4f1c0ea0)
- [dai_ts_cfg::walclk_rate](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#ac17d3da9de6d860f2fa04286a4c43a1d)
- [dai_ts_cfg::direction](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#afdaf1a4ef6a00201b3790187ec44370f)
- [dai_ts_cfg::index](../audio_video_model_reference/P004_dai_ts_cfg_结构体.md#aff3dc52737d1261cd56c084c104691eb)
- [dai_ts_data::walclk](../audio_video_model_reference/P005_dai_ts_data_结构体.md#a11133d72485786e75a9d94f218fe699b)
- [dai_ts_data::sample](../audio_video_model_reference/P005_dai_ts_data_结构体.md#a933cbc19cc837683581db806702fba36)
- [dai_ts_data::walclk_rate](../audio_video_model_reference/P005_dai_ts_data_结构体.md#ace2686aa6ff5aed346705cbb0d198d36)

---

[上一章](P119_cst8xx-gesture-codes.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P121_data.h_源码浏览.md)
