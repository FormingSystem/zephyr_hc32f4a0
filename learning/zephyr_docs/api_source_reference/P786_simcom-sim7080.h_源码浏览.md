---
id: learning.zephyr-docs.api-source-reference.page-786
title: simcom-sim7080.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/simcom-sim7080_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第786章\_simcom-sim7080.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/simcom-sim7080_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/simcom-sim7080_8h.html)。

## 786.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
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
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="foldopen00089"></a>
<a id="l00089"></a>
<a id="l00093"></a>
<a id="l00097"></a>
<a id="l00101"></a>
<a id="l00105"></a>
<a id="l00109"></a>
<a id="l00113"></a>
<a id="l00117"></a>
<a id="l00121"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00147"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="foldopen00175"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="foldopen00183"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="foldopen00191"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="foldopen00202"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="foldopen00226"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="foldopen00260"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="agroup__simcom__sim7080__interface_html_ga017a7dc143628ff5ff5646c7be6d4579"></a>
<a id="agroup__simcom__sim7080__interface_html_ga02721f95826487567017ebf780dff635"></a>
<a id="agroup__simcom__sim7080__interface_html_ga04f3c0bce4f7d2b35762dc92f0aa20eb"></a>
<a id="agroup__simcom__sim7080__interface_html_ga1e082cf652a5b34efdf50b30fe55f631"></a>
<a id="agroup__simcom__sim7080__interface_html_ga25692018fd26087e093b666a5884726c"></a>
<a id="agroup__simcom__sim7080__interface_html_ga25a5a23ca32dbd4bc7991274d3d1ce04"></a>
<a id="agroup__simcom__sim7080__interface_html_ga26d1291993cdcd44982c95bad2dd7b4f"></a>
<a id="agroup__simcom__sim7080__interface_html_ga2895183848c33177c5b788e08382ba09"></a>
<a id="agroup__simcom__sim7080__interface_html_ga313d94f1005e562f6646867813d97fb2"></a>
<a id="agroup__simcom__sim7080__interface_html_ga35c2b87170079e5700021969d01d7f8b"></a>
<a id="agroup__simcom__sim7080__interface_html_ga43d7e807a3f3a51a63ad86055d8d7af2"></a>
<a id="agroup__simcom__sim7080__interface_html_ga454c0078f17532f8e77bb036f9c0d707"></a>
<a id="agroup__simcom__sim7080__interface_html_ga48afa6e777af6010488fbf726f467e63"></a>
<a id="agroup__simcom__sim7080__interface_html_ga4a4fbc695dc92fdf57cb7faf1f104f42"></a>
<a id="agroup__simcom__sim7080__interface_html_ga53a7c0d347cfacf0d7fadaf073fbff6c"></a>
<a id="agroup__simcom__sim7080__interface_html_ga557ec2729649fd92c5588f6dd0a04f15"></a>
<a id="agroup__simcom__sim7080__interface_html_ga5d90415d319a9939f03752ff38a7c25a"></a>
<a id="agroup__simcom__sim7080__interface_html_ga6106a7d04282af2130471d26f6080ed4"></a>
<a id="agroup__simcom__sim7080__interface_html_ga617c649ba2524884d8bf11c91bd2c492"></a>
<a id="agroup__simcom__sim7080__interface_html_ga6cea6acdf6f02868a9f97c10b909a097"></a>
<a id="agroup__simcom__sim7080__interface_html_ga71b0423009ee53ea6d2f4497820e775c"></a>
<a id="agroup__simcom__sim7080__interface_html_ga74f00c0b99f71f7340740fb199db58a5"></a>
<a id="agroup__simcom__sim7080__interface_html_ga79837aee512ae6f2fed52f3162e39868"></a>
<a id="agroup__simcom__sim7080__interface_html_ga7dc8062da9814bdee91b1e88092eee4b"></a>
<a id="agroup__simcom__sim7080__interface_html_ga810526ebd0e2bec22c1dac87b5425d5d"></a>
<a id="agroup__simcom__sim7080__interface_html_ga83acdbbe8cde8d73eec066f7e6829941"></a>
<a id="agroup__simcom__sim7080__interface_html_ga93395c2713539db360cdcf0170075ea1"></a>
<a id="agroup__simcom__sim7080__interface_html_ga9759bf93bc2e8e15869858853a9499de"></a>
<a id="agroup__simcom__sim7080__interface_html_gaa07958866afaf9b9cc65517abf65d08c"></a>
<a id="agroup__simcom__sim7080__interface_html_gaa33f561bff0c1a0c8fe484ae226fe421"></a>
<a id="agroup__simcom__sim7080__interface_html_gaacf368bc85d27d49709bde170a0db2ec"></a>
<a id="agroup__simcom__sim7080__interface_html_gab64ab50adf37f68e036db2901dd839a7"></a>
<a id="agroup__simcom__sim7080__interface_html_gacce71e254dd7854052678319227c3f5b"></a>
<a id="agroup__simcom__sim7080__interface_html_gace6ac2be37e58af15aeda674923c8201"></a>
<a id="agroup__simcom__sim7080__interface_html_gad7e8d5c7cecb9b6150ad1148c81cf3ab"></a>
<a id="agroup__simcom__sim7080__interface_html_gad84438b511f6fed71668273470294420"></a>
<a id="agroup__simcom__sim7080__interface_html_gad857dd548490d40e6b9082c0b72e8d2b"></a>
<a id="agroup__simcom__sim7080__interface_html_gae7137523b94c96d4816e4c19cb48313c"></a>
<a id="agroup__simcom__sim7080__interface_html_gaeda25db4347c7fcfbee69e8d6edace64"></a>
<a id="agroup__simcom__sim7080__interface_html_gafe348fd71a838e6d3628e4025e859ba6"></a>
<a id="agroup__simcom__sim7080__interface_html_gafefcd23a6ce4c292b1cfc2bbcfa98784"></a>
<a id="agroup__simcom__sim7080__interface_html_gga02721f95826487567017ebf780dff635a1eabca23c4eda124b2ff759978f951e6"></a>
<a id="agroup__simcom__sim7080__interface_html_gga02721f95826487567017ebf780dff635a4338e0ab236bf3858ea88d6a5b1f5d36"></a>
<a id="agroup__simcom__sim7080__interface_html_gga02721f95826487567017ebf780dff635a7939b7de8fece8cc1021b29394231671"></a>
<a id="agroup__simcom__sim7080__interface_html_gga02721f95826487567017ebf780dff635a9deadb1d3ade4641f22d08bd7bd6c3b3"></a>
<a id="agroup__simcom__sim7080__interface_html_gga04f3c0bce4f7d2b35762dc92f0aa20eba403ca4efe4553c0e4a6d2b2da5be4165"></a>
<a id="agroup__simcom__sim7080__interface_html_gga04f3c0bce4f7d2b35762dc92f0aa20eba60957e1589dd8ce57c45ecc5fa114f86"></a>
<a id="agroup__simcom__sim7080__interface_html_gga04f3c0bce4f7d2b35762dc92f0aa20eba770fe2a07f5dbb73221ff48eaedfb669"></a>
<a id="agroup__simcom__sim7080__interface_html_gga04f3c0bce4f7d2b35762dc92f0aa20eba7afe21ab7bda162b25dc2c7daa127c35"></a>
<a id="agroup__simcom__sim7080__interface_html_gga04f3c0bce4f7d2b35762dc92f0aa20ebab5c1ccc0cf53a21abc5f4d0145c414c5"></a>
<a id="agroup__simcom__sim7080__interface_html_gga25a5a23ca32dbd4bc7991274d3d1ce04a2279138ee4bbb5ed114fc13c7a058f00"></a>
<a id="agroup__simcom__sim7080__interface_html_gga25a5a23ca32dbd4bc7991274d3d1ce04a30f4173c0221c5066cdd4d82ba254b8c"></a>
<a id="agroup__simcom__sim7080__interface_html_gga25a5a23ca32dbd4bc7991274d3d1ce04a6cf88dc2ac93074d74c36f59c4469e14"></a>
<a id="agroup__simcom__sim7080__interface_html_gga25a5a23ca32dbd4bc7991274d3d1ce04ab18bd882eec9368c2e65c45fdadc7ff2"></a>
<a id="agroup__simcom__sim7080__interface_html_gga48afa6e777af6010488fbf726f467e63a6bc03b17b206166e04ec04a2638dc241"></a>
<a id="agroup__simcom__sim7080__interface_html_gga48afa6e777af6010488fbf726f467e63a6cc1c6e5f12101e8202deddf3667bbda"></a>
<a id="agroup__simcom__sim7080__interface_html_gga48afa6e777af6010488fbf726f467e63af744651290c73069148c0726bcdf95ce"></a>
<a id="agroup__simcom__sim7080__interface_html_gga5d90415d319a9939f03752ff38a7c25aa369ac733e64b26f64ec1070bd38c92d8"></a>
<a id="agroup__simcom__sim7080__interface_html_gga5d90415d319a9939f03752ff38a7c25aa3fa46c5fc0fc7d94255ee13280c88f8b"></a>
<a id="agroup__simcom__sim7080__interface_html_gga5d90415d319a9939f03752ff38a7c25aab024ba55594ab204a65f1a34a9b7b56a"></a>
<a id="agroup__simcom__sim7080__interface_html_gga5d90415d319a9939f03752ff38a7c25aac0bc355a3c8e0a996bb6a7a7f580cb6c"></a>
<a id="agroup__simcom__sim7080__interface_html_gga5d90415d319a9939f03752ff38a7c25aad90e03decaa89043d355447982133cf0"></a>
<a id="agroup__simcom__sim7080__interface_html_ggaeda25db4347c7fcfbee69e8d6edace64a036b486a3039accb70a4f771a66ec000"></a>
<a id="agroup__simcom__sim7080__interface_html_ggaeda25db4347c7fcfbee69e8d6edace64a37a34e81132c5d5615e0692c6c3d10ff"></a>
<a id="agroup__simcom__sim7080__interface_html_ggaeda25db4347c7fcfbee69e8d6edace64a5dcc819c05e2d77067a6c26c32f1e16c"></a>
<a id="agroup__simcom__sim7080__interface_html_ggaeda25db4347c7fcfbee69e8d6edace64a600e1474544a7a78bdcd76204fe435b5"></a>
<a id="agroup__simcom__sim7080__interface_html_ggaeda25db4347c7fcfbee69e8d6edace64aa4cff001bbfd8549d26a427fd4159d14"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784a045d79d61b1f995edb75801e3b095465"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784a1cd7fc42302f32e4cc82f11b65fad528"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784a1d9dc9cfd0704de467f20330ef73337a"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784a40e43ece45afd379aa071277f648649e"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784a5eaf600aed0d8079818929fa3a8f8d70"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784a77c5d67140903e0c42292e1b92c23666"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784a7a65a1af619a8451cd1fe77e18b00e67"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784a892159a544473dc0e37ae22bbd1f7050"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784a970ee528bb955d0a90e76f09ff0ed5d0"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784a99777d6c606515e2f1cbdfdbf8c9877e"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784a9ce491762e30d7dc50f77b6a9b8af831"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784ab63b58736416d738f381c991b509aba9"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784ab951b91a48e106c2bd34503a6408100c"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784abf07653aa5c5c7fc38c6c0e9a530b09a"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784ae967bd6f2a449b56acc647af6ecb6749"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784aea11bd338ab8542e5e8083628a5603b9"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784af1fed81428e04fa1ed1102b754468e24"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784af337a56637a986f63e50c95165d3e28c"></a>
<a id="agroup__simcom__sim7080__interface_html_ggafefcd23a6ce4c292b1cfc2bbcfa98784afc275bd937ca24a8dcab084205a0fe9e"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a99ef1cb2c789827dd5db3886dccf9067"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructpasswd_html"></a>
<a id="astructsim7080__gnss__data_html"></a>
<a id="astructsim7080__gnss__data_html_a23dc6e7aa0cc507cf5141aa5329e17ef"></a>
<a id="astructsim7080__gnss__data_html_a545077bd8eb1d6827c50b59d469bdc4a"></a>
<a id="astructsim7080__gnss__data_html_a62b8a5072942a325156a90607888612b"></a>
<a id="astructsim7080__gnss__data_html_a7dee72b39dc718ade2cc27bedc691d6e"></a>
<a id="astructsim7080__gnss__data_html_a881db8b7b52d481416bc5f373446bfc2"></a>
<a id="astructsim7080__gnss__data_html_a8a42fbb4a716a0eefe317996f8fe7a8a"></a>
<a id="astructsim7080__gnss__data_html_aa481937aedd2817e3a301663648d9f7d"></a>
<a id="astructsim7080__gnss__data_html_ab917d70a3c5adffb8aecc9e521c36599"></a>
<a id="astructsim7080__gnss__data_html_aca6603b72f8ac67a0a0084a3fc8a60a1"></a>
<a id="astructsim7080__sms__buffer_html"></a>
<a id="astructsim7080__sms__buffer_html_a54e1885be2e809fd360738d11547b79f"></a>
<a id="astructsim7080__sms__buffer_html_a7477db7ff124999b95f50f3ae32aca6a"></a>
<a id="astructsim7080__sms_html"></a>
<a id="astructsim7080__sms_html_a30773852fece821bd82fc97e02667bd9"></a>
<a id="astructsim7080__sms_html_a343f290be0f3ca62618c47ff7e54cda2"></a>
<a id="astructsim7080__sms_html_a3db8a08ab147d1765eec75a0b93f3cb7"></a>
<a id="astructsim7080__sms_html_a705e0cbd5654677e6b99cd6ed22767be"></a>
<a id="astructsim7080__sms_html_a7dd5c165eafbf70f3e1f01efa71bf640"></a>
<a id="astructsim7080__sms_html_a8c41c51b2bfaea343b5340ba8c02b56a"></a>
<a id="astructsim7080__sms_html_a9dc5291721c65a949a8d351b2408a253"></a>
<a id="astructsim7080__sms_html_aaaa3957cf7e0597dfbf309da0b64b54f"></a>
<a id="astructsim7080__sms_html_abd559c83ec2896660cffbe8df1be687b"></a>
<a id="astructsim7080__sms_html_ac5a04784c883710d8794bf4762bb9078"></a>
<a id="astructsim7080__sms_html_af207e345f8c024258c5c011a28ad28c0"></a>
<a id="astructsim7080__sms_html_af9aeb3cb06325e0d1e52db6d78567feb"></a>
<a id="astructsim7080__sms_html_afdb63d3e307c3368149f6d0183541379"></a>
<a id="astructsim7080__ue__sys__info__gsm_html"></a>
<a id="astructsim7080__ue__sys__info__gsm_html_a481f9b9426f6deebeb019bf7f7d61e03"></a>
<a id="astructsim7080__ue__sys__info__gsm_html_a60b655f5dd03137c67f3990d9584f579"></a>
<a id="astructsim7080__ue__sys__info__gsm_html_a6514320e087362edf623e1b35ac2f4ec"></a>
<a id="astructsim7080__ue__sys__info__gsm_html_a7109571a82f669173c0dffbfc91e6706"></a>
<a id="astructsim7080__ue__sys__info__gsm_html_a7566a16cdd2a7ffbcbb575cce97c0dd8"></a>
<a id="astructsim7080__ue__sys__info__gsm_html_a84678a3a6dbdbf0f4e2cecfd7ebfe96a"></a>
<a id="astructsim7080__ue__sys__info__gsm_html_a91dc051575f95177042aa63fbea8b409"></a>
<a id="astructsim7080__ue__sys__info__gsm_html_ac15deea095cc6316bb56505be968ad92"></a>
<a id="astructsim7080__ue__sys__info__gsm_html_ae12054693fa10b41be19ebcad14f1683"></a>
<a id="astructsim7080__ue__sys__info__lte_html"></a>
<a id="astructsim7080__ue__sys__info__lte_html_a0f6a10da2ac1b67f29cf3307597764ed"></a>
<a id="astructsim7080__ue__sys__info__lte_html_a110fae03ebc62ef7ec83bd885d920f8a"></a>
<a id="astructsim7080__ue__sys__info__lte_html_a243f34e1ccd63716883f8246feeeb1b8"></a>
<a id="astructsim7080__ue__sys__info__lte_html_a2978455bb41a4d1ae888aaa0e2242807"></a>
<a id="astructsim7080__ue__sys__info__lte_html_a2b230db49b10f285fded288664d25d9f"></a>
<a id="astructsim7080__ue__sys__info__lte_html_a30b6a65590be8198f57baf54191c2d97"></a>
<a id="astructsim7080__ue__sys__info__lte_html_aadfaabd5692fd42619edaf8c16c4efef"></a>
<a id="astructsim7080__ue__sys__info__lte_html_acce77829b8bcc16d16367c1aec7d4323"></a>
<a id="astructsim7080__ue__sys__info__lte_html_ada937e5906995e3b0c1487bf572e30e5"></a>
<a id="astructsim7080__ue__sys__info__lte_html_adce93c6c4192d090c06622aaebaa87e0"></a>
<a id="astructsim7080__ue__sys__info__lte_html_ae398efdcfd7c31e42ea135b334c51946"></a>
<a id="astructsim7080__ue__sys__info__lte_html_aed7ef4908901397958bc121138807c1e"></a>
<a id="astructsim7080__ue__sys__info__lte_html_af0072ee8fa216a544b9b762672279ebd"></a>
<a id="astructsim7080__ue__sys__info__lte_html_af3f5afa6ba5bc07de4f01886c7083a44"></a>
<a id="astructsim7080__ue__sys__info_html"></a>
<a id="astructsim7080__ue__sys__info_html_a47f14459263b13749a3722107a20631c"></a>
<a id="astructsim7080__ue__sys__info_html_a77e0794049df94d1c6c106a1554fa6ea"></a>
<a id="astructsim7080__ue__sys__info_html_ab42417fa5673818a5236e61a791d6c20"></a>
<a id="astructsim7080__ue__sys__info_html_ace117d5d35a3b6a41b87b05315f7a19e"></a>
<a id="astructsim7080__ue__sys__info_html_ae2010949f786b1ee107cbfc34e207412"></a>
<a id="astructtm_html"></a>

```c


#ifndef ZEPHYR_INCLUDE_DRIVERS_MODEM_SIMCOM_SIM7080_H
#define ZEPHYR_INCLUDE_DRIVERS_MODEM_SIMCOM_SIM7080_H

#include <zephyr/types.h>

#include <stdbool.h>
#include <stdint.h>
#include <time.h>

#ifdef __cplusplus
extern "C" {
#endif


#define SIM7080_GNSS_DATA_UTC_LEN 20
#define SIM7080_SMS_MAX_LEN 160
#define SIM7080_UE_SYS_INFO_BAND_SIZE 32
#define SIM7080_DNS_MAX_RECOUNT 10
#define SIM7080_DNS_MAX_TIMEOUT_MS 60000

#define SIM7080_LTE_CHANNEL_MASK_NB1 0x7BEFFU
#define SIM7080_LTE_CHANNEL_MASK_M1  0x5FFFFU
#define SIM7080_NUM_LTE_CHANNELS     19U

enum sim7080_state {
        SIM7080_STATE_INIT = 0,
        SIM7080_STATE_IDLE,
        SIM7080_STATE_NETWORKING,
        SIM7080_STATE_GNSS,
        SIM7080_STATE_OFF,
};

enum sim7080_rat {
        SIM7080_RAT_LTE_NB1,
        SIM7080_RAT_LTE_M1,
        SIM7080_RAT_LTE_AUTO,
        SIM7080_RAT_GSM,
};

enum sim7080_lte_chan {
        SIM7080_LTE_CHAN_B1 = BIT(0),
        SIM7080_LTE_CHAN_B2 = BIT(1),
        SIM7080_LTE_CHAN_B3 = BIT(2),
        SIM7080_LTE_CHAN_B4 = BIT(3),
        SIM7080_LTE_CHAN_B5 = BIT(4),
        SIM7080_LTE_CHAN_B8 = BIT(5),
        SIM7080_LTE_CHAN_B12 = BIT(6),
        SIM7080_LTE_CHAN_B13 = BIT(7),
        SIM7080_LTE_CHAN_B14 = BIT(8),
        SIM7080_LTE_CHAN_B18 = BIT(9),
        SIM7080_LTE_CHAN_B19 = BIT(10),
        SIM7080_LTE_CHAN_B20 = BIT(11),
        SIM7080_LTE_CHAN_B25 = BIT(12),
        SIM7080_LTE_CHAN_B26 = BIT(13),
        SIM7080_LTE_CHAN_B27 = BIT(14),
        SIM7080_LTE_CHAN_B28 = BIT(15),
        SIM7080_LTE_CHAN_B66 = BIT(16),
        SIM7080_LTE_CHAN_B71 = BIT(17),
        SIM7080_LTE_CHAN_B85 = BIT(18),
};

struct sim7080_gnss_data {
        bool run_status;
        bool fix_status;
        char utc[SIM7080_GNSS_DATA_UTC_LEN];
        int32_t lat;
        int32_t lon;
        int32_t alt;
        uint16_t hdop;
        uint16_t cog;
        uint16_t kmh;
};

enum sim7080_sms_stat {
        SIM7080_SMS_STAT_REC_UNREAD = 0,
        SIM7080_SMS_STAT_REC_READ,
        SIM7080_SMS_STAT_STO_UNSENT,
        SIM7080_SMS_STAT_STO_SENT,
        SIM7080_SMS_STAT_ALL,
};

enum sim7080_ftp_rc {
        SIM7080_FTP_RC_OK = 0,
        SIM7080_FTP_RC_FINISHED,
        SIM7080_FTP_RC_ERROR,
};

struct sim7080_sms {
        uint8_t first_octet;
        uint8_t tp_pid;
        enum sim7080_sms_stat stat;
        uint16_t index;
        struct {
                uint8_t year;
                uint8_t month;
                uint8_t day;
                uint8_t hour;
                uint8_t minute;
                uint8_t second;
                uint8_t timezone;
        } time;
        char data[SIM7080_SMS_MAX_LEN + 1];
        uint8_t data_len;
};

struct sim7080_sms_buffer {
        struct sim7080_sms *sms;
        uint8_t nsms;
};

enum sim7080_ue_sys_mode {
        SIM7080_UE_SYS_MODE_NO_SERVICE,
        SIM7080_UE_SYS_MODE_GSM,
        SIM7080_UE_SYS_MODE_LTE_CAT_M1,
        SIM7080_UE_SYS_MODE_LTE_NB_IOT,
};

enum sim7080_ue_op_mode {
        SIM7080_UE_OP_MODE_ONLINE,
        SIM7080_UE_OP_MODE_OFFLINE,
        SIM7080_UE_OP_MODE_FACTORY_TEST_MODE,
        SIM7080_UE_OP_MODE_RESET,
        SIM7080_UE_OP_MODE_LOW_POWER_MODE,
};

struct sim7080_ue_sys_info_gsm {
        uint16_t mcc;
        uint16_t mcn;
        uint16_t lac;
        uint16_t cid;
        uint8_t arfcn[SIM7080_UE_SYS_INFO_BAND_SIZE + 1];
        int16_t rx_lvl;
        int16_t track_lo_adjust;
        uint16_t c1;
        uint16_t c2;
};

struct sim7080_ue_sys_info_lte {
        uint16_t mcc;
        uint16_t mcn;
        uint16_t tac;
        uint32_t sci;
        uint16_t pci;
        uint8_t band[SIM7080_UE_SYS_INFO_BAND_SIZE + 1];
        uint16_t earfcn;
        uint16_t dlbw;
        uint16_t ulbw;
        int16_t rsrq;
        int16_t rsrp;
        int16_t rssi;
        int16_t rssnr;
        int16_t sinr;
};

struct sim7080_ue_sys_info {
        enum sim7080_ue_sys_mode sys_mode;
        enum sim7080_ue_op_mode op_mode;
        union {
                struct sim7080_ue_sys_info_gsm gsm;
                struct sim7080_ue_sys_info_lte lte;
        } cell;
};

enum sim7080_state mdm_sim7080_get_state(void);

int mdm_sim7080_power_on(void);

int mdm_sim7080_power_off(void);

void mdm_sim7080_force_reset(void);

int mdm_sim7080_start_network(void);

int mdm_sim7080_stop_network(void);

int mdm_sim7080_start_gnss(void);

int mdm_sim7080_start_gnss_xtra(void);

int mdm_sim7080_stop_gnss(void);

int mdm_sim7080_download_xtra(uint8_t server_id, const char *f_name);

int mdm_sim7080_query_xtra_validity(int16_t *diff_h, int16_t *duration_h, struct tm *inject);

int mdm_sim7080_query_gnss(struct sim7080_gnss_data *data);

const char *mdm_sim7080_get_manufacturer(void);

const char *mdm_sim7080_get_model(void);

const char *mdm_sim7080_get_revision(void);

const char *mdm_sim7080_get_imei(void);

const char *mdm_sim7080_get_iccid(void);

int mdm_sim7080_read_sms(struct sim7080_sms_buffer *buffer);

int mdm_sim7080_delete_sms(uint16_t index);

int mdm_sim7080_set_gpio(int gpio, int level);

int mdm_sim7080_ftp_get_start(const char *server, const char *user, const char *passwd,
                                  const char *file, const char *path);

int mdm_sim7080_ftp_get_read(char *dst, size_t *size);

int mdm_sim7080_get_battery_charge(uint8_t *bcs, uint8_t *bcl, uint16_t *voltage);

int mdm_sim7080_get_ue_sys_info(struct sim7080_ue_sys_info *info);

int mdm_sim7080_get_local_time(struct tm *t);

int mdm_sim7080_dns_set_lookup_params(uint8_t recount, uint16_t timeout);

void mdm_sim7080_dns_get_lookup_params(uint8_t *recount, uint16_t *timeout);

#if defined(CONFIG_MODEM_SIMCOM_SIM7080_SOCKETS_SOCKOPT_TLS)
typedef int (*sim7080_tls_cert_read_func)(uint8_t *buf, size_t max_len, size_t offset);

int mdm_sim7080_import_root_ca(const char *cert_name, sim7080_tls_cert_read_func read_func,
                               size_t cert_len);

int mdm_sim7080_import_client_cert(const char *cert_name, sim7080_tls_cert_read_func cert_read_func,
                                   size_t cert_len, const char *key_name,
                                   sim7080_tls_cert_read_func key_read_func, size_t key_len,
                                   const char *passwd);

int mdm_sim7080_import_dtls_psk(const char *psk_name, sim7080_tls_cert_read_func read_func,
                                size_t psk_len);

int mdm_sim7080_configure_tls_certs(int fd, const char *root_ca, const char *client_cert);

int mdm_sim7080_configure_dtls_psktable(int fd, const char *psktable);
#endif

void mdm_sim7080_get_rat(enum sim7080_rat *rat);

int mdm_sim7080_set_rat(enum sim7080_rat rat);

void mdm_sim7080_get_lte_bands(uint32_t *nb1, uint32_t *m1);

int mdm_sim7080_set_lte_bands(uint32_t nb1, uint32_t m1);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_MODEM_SIMCOM_SIM7080_H */
```

## 786.2\_可见注释译文（Comments）

### 注释 1：原第 650 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MODEM_SIMCOM_SIM7080_H`。

## 786.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/simcom-sim7080_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [sim7080_state](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga5d90415d319a9939f03752ff38a7c25a)
- [SIM7080_STATE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aac0bc355a3c8e0a996bb6a7a7f580cb6c)
- [SIM7080_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aab024ba55594ab204a65f1a34a9b7b56a)
- [SIM7080_STATE_NETWORKING](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aa369ac733e64b26f64ec1070bd38c92d8)
- [SIM7080_STATE_GNSS](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aad90e03decaa89043d355447982133cf0)
- [SIM7080_STATE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aa3fa46c5fc0fc7d94255ee13280c88f8b)
- [sim7080_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga02721f95826487567017ebf780dff635)
- [SIM7080_RAT_LTE_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga02721f95826487567017ebf780dff635a7939b7de8fece8cc1021b29394231671)
- [SIM7080_RAT_LTE_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga02721f95826487567017ebf780dff635a1eabca23c4eda124b2ff759978f951e6)
- [SIM7080_RAT_LTE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga02721f95826487567017ebf780dff635a4338e0ab236bf3858ea88d6a5b1f5d36)
- [SIM7080_RAT_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga02721f95826487567017ebf780dff635a9deadb1d3ade4641f22d08bd7bd6c3b3)
- [sim7080_lte_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gafefcd23a6ce4c292b1cfc2bbcfa98784)
- [SIM7080_LTE_CHAN_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784af1fed81428e04fa1ed1102b754468e24)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SIM7080_LTE_CHAN_B2](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784ab951b91a48e106c2bd34503a6408100c)
- [SIM7080_LTE_CHAN_B3](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784abf07653aa5c5c7fc38c6c0e9a530b09a)
- [SIM7080_LTE_CHAN_B4](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a7a65a1af619a8451cd1fe77e18b00e67)
- [SIM7080_LTE_CHAN_B5](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784ab63b58736416d738f381c991b509aba9)
- [SIM7080_LTE_CHAN_B8](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a892159a544473dc0e37ae22bbd1f7050)
- [SIM7080_LTE_CHAN_B12](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784af337a56637a986f63e50c95165d3e28c)
- [SIM7080_LTE_CHAN_B13](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a1d9dc9cfd0704de467f20330ef73337a)
- [SIM7080_LTE_CHAN_B14](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a99777d6c606515e2f1cbdfdbf8c9877e)
- [SIM7080_LTE_CHAN_B18](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a77c5d67140903e0c42292e1b92c23666)
- [SIM7080_LTE_CHAN_B19](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a40e43ece45afd379aa071277f648649e)
- [SIM7080_LTE_CHAN_B20](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a045d79d61b1f995edb75801e3b095465)
- [SIM7080_LTE_CHAN_B25](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a970ee528bb955d0a90e76f09ff0ed5d0)
- [SIM7080_LTE_CHAN_B26](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a5eaf600aed0d8079818929fa3a8f8d70)
- [SIM7080_LTE_CHAN_B27](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a1cd7fc42302f32e4cc82f11b65fad528)
- [SIM7080_LTE_CHAN_B28](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784ae967bd6f2a449b56acc647af6ecb6749)
- [SIM7080_LTE_CHAN_B66](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784afc275bd937ca24a8dcab084205a0fe9e)
- [SIM7080_LTE_CHAN_B71](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784aea11bd338ab8542e5e8083628a5603b9)
- [SIM7080_LTE_CHAN_B85](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a9ce491762e30d7dc50f77b6a9b8af831)
- [sim7080_gnss_data](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md)
- [run_status](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#ab917d70a3c5adffb8aecc9e521c36599)
- [fix_status](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#a881db8b7b52d481416bc5f373446bfc2)
- [utc](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#a8a42fbb4a716a0eefe317996f8fe7a8a)
- [SIM7080_GNSS_DATA_UTC_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gace6ac2be37e58af15aeda674923c8201)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [lat](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#a545077bd8eb1d6827c50b59d469bdc4a)
- [lon](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#a23dc6e7aa0cc507cf5141aa5329e17ef)
- [alt](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#aa481937aedd2817e3a301663648d9f7d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [hdop](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#aca6603b72f8ac67a0a0084a3fc8a60a1)
- [cog](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#a7dee72b39dc718ade2cc27bedc691d6e)
- [kmh](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#a62b8a5072942a325156a90607888612b)
- [sim7080_sms_stat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga04f3c0bce4f7d2b35762dc92f0aa20eb)
- [SIM7080_SMS_STAT_REC_UNREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20eba60957e1589dd8ce57c45ecc5fa114f86)
- [SIM7080_SMS_STAT_REC_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20eba403ca4efe4553c0e4a6d2b2da5be4165)
- [SIM7080_SMS_STAT_STO_UNSENT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20eba770fe2a07f5dbb73221ff48eaedfb669)
- [SIM7080_SMS_STAT_STO_SENT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20ebab5c1ccc0cf53a21abc5f4d0145c414c5)
- [SIM7080_SMS_STAT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20eba7afe21ab7bda162b25dc2c7daa127c35)
- [sim7080_ftp_rc](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga48afa6e777af6010488fbf726f467e63)
- [SIM7080_FTP_RC_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga48afa6e777af6010488fbf726f467e63a6cc1c6e5f12101e8202deddf3667bbda)
- [SIM7080_FTP_RC_FINISHED](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga48afa6e777af6010488fbf726f467e63a6bc03b17b206166e04ec04a2638dc241)
- [SIM7080_FTP_RC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga48afa6e777af6010488fbf726f467e63af744651290c73069148c0726bcdf95ce)
- [sim7080_sms](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [first_octet](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a8c41c51b2bfaea343b5340ba8c02b56a)
- [tp_pid](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#aaaa3957cf7e0597dfbf309da0b64b54f)
- [stat](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a9dc5291721c65a949a8d351b2408a253)
- [index](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#abd559c83ec2896660cffbe8df1be687b)
- [year](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#afdb63d3e307c3368149f6d0183541379)
- [month](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a3db8a08ab147d1765eec75a0b93f3cb7)
- [day](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a30773852fece821bd82fc97e02667bd9)
- [hour](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#af207e345f8c024258c5c011a28ad28c0)
- [minute](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a705e0cbd5654677e6b99cd6ed22767be)
- [second](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a343f290be0f3ca62618c47ff7e54cda2)
- [timezone](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#ac5a04784c883710d8794bf4762bb9078)
- [time](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a99ef1cb2c789827dd5db3886dccf9067)
- [data](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a7dd5c165eafbf70f3e1f01efa71bf640)
- [SIM7080_SMS_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gab64ab50adf37f68e036db2901dd839a7)
- [data_len](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#af9aeb3cb06325e0d1e52db6d78567feb)
- [sim7080_sms_buffer](../modem_wireless_model_reference/P067_sim7080_sms_buffer_结构体.md)
- [sms](../modem_wireless_model_reference/P067_sim7080_sms_buffer_结构体.md#a7477db7ff124999b95f50f3ae32aca6a)
- [nsms](../modem_wireless_model_reference/P067_sim7080_sms_buffer_结构体.md#a54e1885be2e809fd360738d11547b79f)
- [sim7080_ue_sys_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga25a5a23ca32dbd4bc7991274d3d1ce04)
- [SIM7080_UE_SYS_MODE_NO_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga25a5a23ca32dbd4bc7991274d3d1ce04a30f4173c0221c5066cdd4d82ba254b8c)
- [SIM7080_UE_SYS_MODE_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga25a5a23ca32dbd4bc7991274d3d1ce04a6cf88dc2ac93074d74c36f59c4469e14)
- [SIM7080_UE_SYS_MODE_LTE_CAT_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga25a5a23ca32dbd4bc7991274d3d1ce04ab18bd882eec9368c2e65c45fdadc7ff2)
- [SIM7080_UE_SYS_MODE_LTE_NB_IOT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga25a5a23ca32dbd4bc7991274d3d1ce04a2279138ee4bbb5ed114fc13c7a058f00)
- [sim7080_ue_op_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaeda25db4347c7fcfbee69e8d6edace64)
- [SIM7080_UE_OP_MODE_ONLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64a600e1474544a7a78bdcd76204fe435b5)
- [SIM7080_UE_OP_MODE_OFFLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64a036b486a3039accb70a4f771a66ec000)
- [SIM7080_UE_OP_MODE_FACTORY_TEST_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64a5dcc819c05e2d77067a6c26c32f1e16c)
- [SIM7080_UE_OP_MODE_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64a37a34e81132c5d5615e0692c6c3d10ff)
- [SIM7080_UE_OP_MODE_LOW_POWER_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64aa4cff001bbfd8549d26a427fd4159d14)
- [sim7080_ue_sys_info_gsm](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md)
- [mcc](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#ae12054693fa10b41be19ebcad14f1683)
- [mcn](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a481f9b9426f6deebeb019bf7f7d61e03)
- [lac](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a6514320e087362edf623e1b35ac2f4ec)
- [cid](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a7109571a82f669173c0dffbfc91e6706)
- [arfcn](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a84678a3a6dbdbf0f4e2cecfd7ebfe96a)
- [SIM7080_UE_SYS_INFO_BAND_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga43d7e807a3f3a51a63ad86055d8d7af2)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [rx_lvl](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#ac15deea095cc6316bb56505be968ad92)
- [track_lo_adjust](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a91dc051575f95177042aa63fbea8b409)
- [c1](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a7566a16cdd2a7ffbcbb575cce97c0dd8)
- [c2](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a60b655f5dd03137c67f3990d9584f579)
- [sim7080_ue_sys_info_lte](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md)
- [mcc](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#a110fae03ebc62ef7ec83bd885d920f8a)
- [mcn](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#a2978455bb41a4d1ae888aaa0e2242807)
- [tac](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#aed7ef4908901397958bc121138807c1e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sci](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#aadfaabd5692fd42619edaf8c16c4efef)
- [pci](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#af0072ee8fa216a544b9b762672279ebd)
- [band](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#ada937e5906995e3b0c1487bf572e30e5)
- [earfcn](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#adce93c6c4192d090c06622aaebaa87e0)
- [dlbw](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#a0f6a10da2ac1b67f29cf3307597764ed)
- [ulbw](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#acce77829b8bcc16d16367c1aec7d4323)
- [rsrq](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#af3f5afa6ba5bc07de4f01886c7083a44)
- [rsrp](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#ae398efdcfd7c31e42ea135b334c51946)
- [rssi](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#a243f34e1ccd63716883f8246feeeb1b8)
- [rssnr](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#a30b6a65590be8198f57baf54191c2d97)
- [sinr](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#a2b230db49b10f285fded288664d25d9f)
- [sim7080_ue_sys_info](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md)
- [sys_mode](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md#a47f14459263b13749a3722107a20631c)
- [op_mode](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md#a77e0794049df94d1c6c106a1554fa6ea)
- [gsm](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md#ae2010949f786b1ee107cbfc34e207412)
- [lte](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md#ace117d5d35a3b6a41b87b05315f7a19e)
- [cell](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md#ab42417fa5673818a5236e61a791d6c20)
- [mdm_sim7080_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga1e082cf652a5b34efdf50b30fe55f631)
- [mdm_sim7080_power_on](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga93395c2713539db360cdcf0170075ea1)
- [mdm_sim7080_power_off](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga35c2b87170079e5700021969d01d7f8b)
- [mdm_sim7080_force_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga454c0078f17532f8e77bb036f9c0d707)
- [mdm_sim7080_start_network](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gad857dd548490d40e6b9082c0b72e8d2b)
- [mdm_sim7080_stop_network](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaa07958866afaf9b9cc65517abf65d08c)
- [mdm_sim7080_start_gnss](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga6106a7d04282af2130471d26f6080ed4)
- [mdm_sim7080_start_gnss_xtra](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga7dc8062da9814bdee91b1e88092eee4b)
- [mdm_sim7080_stop_gnss](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga617c649ba2524884d8bf11c91bd2c492)
- [mdm_sim7080_download_xtra](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gad84438b511f6fed71668273470294420)
- [mdm_sim7080_query_xtra_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga25692018fd26087e093b666a5884726c)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [mdm_sim7080_query_gnss](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gacce71e254dd7854052678319227c3f5b)
- [mdm_sim7080_get_manufacturer](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga79837aee512ae6f2fed52f3162e39868)
- [mdm_sim7080_get_model](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga557ec2729649fd92c5588f6dd0a04f15)
- [mdm_sim7080_get_revision](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga9759bf93bc2e8e15869858853a9499de)
- [mdm_sim7080_get_imei](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga26d1291993cdcd44982c95bad2dd7b4f)
- [mdm_sim7080_get_iccid](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gad7e8d5c7cecb9b6150ad1148c81cf3ab)
- [mdm_sim7080_read_sms](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaacf368bc85d27d49709bde170a0db2ec)
- [mdm_sim7080_delete_sms](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gae7137523b94c96d4816e4c19cb48313c)
- [mdm_sim7080_set_gpio](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga6cea6acdf6f02868a9f97c10b909a097)
- [mdm_sim7080_ftp_get_start](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga53a7c0d347cfacf0d7fadaf073fbff6c)
- [passwd](../posix_system_model_reference/P009_passwd_结构体.md)
- [mdm_sim7080_ftp_get_read](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga74f00c0b99f71f7340740fb199db58a5)
- [mdm_sim7080_get_battery_charge](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga313d94f1005e562f6646867813d97fb2)
- [mdm_sim7080_get_ue_sys_info](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga2895183848c33177c5b788e08382ba09)
- [mdm_sim7080_get_local_time](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga71b0423009ee53ea6d2f4497820e775c)
- [mdm_sim7080_dns_set_lookup_params](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga017a7dc143628ff5ff5646c7be6d4579)
- [mdm_sim7080_dns_get_lookup_params](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga83acdbbe8cde8d73eec066f7e6829941)
- [mdm_sim7080_get_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gafe348fd71a838e6d3628e4025e859ba6)
- [mdm_sim7080_set_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaa33f561bff0c1a0c8fe484ae226fe421)
- [mdm_sim7080_get_lte_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga810526ebd0e2bec22c1dac87b5425d5d)
- [mdm_sim7080_set_lte_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga4a4fbc695dc92fdf57cb7faf1f104f42)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [sim7080_gnss_data::lon](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#a23dc6e7aa0cc507cf5141aa5329e17ef)
- [sim7080_gnss_data::lat](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#a545077bd8eb1d6827c50b59d469bdc4a)
- [sim7080_gnss_data::kmh](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#a62b8a5072942a325156a90607888612b)
- [sim7080_gnss_data::cog](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#a7dee72b39dc718ade2cc27bedc691d6e)
- [sim7080_gnss_data::fix_status](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#a881db8b7b52d481416bc5f373446bfc2)
- [sim7080_gnss_data::utc](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#a8a42fbb4a716a0eefe317996f8fe7a8a)
- [sim7080_gnss_data::alt](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#aa481937aedd2817e3a301663648d9f7d)
- [sim7080_gnss_data::run_status](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#ab917d70a3c5adffb8aecc9e521c36599)
- [sim7080_gnss_data::hdop](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md#aca6603b72f8ac67a0a0084a3fc8a60a1)
- [sim7080_sms_buffer::nsms](../modem_wireless_model_reference/P067_sim7080_sms_buffer_结构体.md#a54e1885be2e809fd360738d11547b79f)
- [sim7080_sms_buffer::sms](../modem_wireless_model_reference/P067_sim7080_sms_buffer_结构体.md#a7477db7ff124999b95f50f3ae32aca6a)
- [sim7080_sms::day](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a30773852fece821bd82fc97e02667bd9)
- [sim7080_sms::second](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a343f290be0f3ca62618c47ff7e54cda2)
- [sim7080_sms::month](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a3db8a08ab147d1765eec75a0b93f3cb7)
- [sim7080_sms::minute](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a705e0cbd5654677e6b99cd6ed22767be)
- [sim7080_sms::data](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a7dd5c165eafbf70f3e1f01efa71bf640)
- [sim7080_sms::first_octet](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a8c41c51b2bfaea343b5340ba8c02b56a)
- [sim7080_sms::stat](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#a9dc5291721c65a949a8d351b2408a253)
- [sim7080_sms::tp_pid](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#aaaa3957cf7e0597dfbf309da0b64b54f)
- [sim7080_sms::index](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#abd559c83ec2896660cffbe8df1be687b)
- [sim7080_sms::timezone](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#ac5a04784c883710d8794bf4762bb9078)
- [sim7080_sms::hour](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#af207e345f8c024258c5c011a28ad28c0)
- [sim7080_sms::data_len](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#af9aeb3cb06325e0d1e52db6d78567feb)
- [sim7080_sms::year](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md#afdb63d3e307c3368149f6d0183541379)
- [sim7080_ue_sys_info_gsm::mcn](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a481f9b9426f6deebeb019bf7f7d61e03)
- [sim7080_ue_sys_info_gsm::c2](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a60b655f5dd03137c67f3990d9584f579)
- [sim7080_ue_sys_info_gsm::lac](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a6514320e087362edf623e1b35ac2f4ec)
- [sim7080_ue_sys_info_gsm::cid](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a7109571a82f669173c0dffbfc91e6706)
- [sim7080_ue_sys_info_gsm::c1](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a7566a16cdd2a7ffbcbb575cce97c0dd8)
- [sim7080_ue_sys_info_gsm::arfcn](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a84678a3a6dbdbf0f4e2cecfd7ebfe96a)
- [sim7080_ue_sys_info_gsm::track_lo_adjust](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#a91dc051575f95177042aa63fbea8b409)
- [sim7080_ue_sys_info_gsm::rx_lvl](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#ac15deea095cc6316bb56505be968ad92)
- [sim7080_ue_sys_info_gsm::mcc](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md#ae12054693fa10b41be19ebcad14f1683)
- [sim7080_ue_sys_info_lte::dlbw](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#a0f6a10da2ac1b67f29cf3307597764ed)
- [sim7080_ue_sys_info_lte::mcc](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#a110fae03ebc62ef7ec83bd885d920f8a)
- [sim7080_ue_sys_info_lte::rssi](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#a243f34e1ccd63716883f8246feeeb1b8)
- [sim7080_ue_sys_info_lte::mcn](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#a2978455bb41a4d1ae888aaa0e2242807)
- [sim7080_ue_sys_info_lte::sinr](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#a2b230db49b10f285fded288664d25d9f)
- [sim7080_ue_sys_info_lte::rssnr](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#a30b6a65590be8198f57baf54191c2d97)
- [sim7080_ue_sys_info_lte::sci](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#aadfaabd5692fd42619edaf8c16c4efef)
- [sim7080_ue_sys_info_lte::ulbw](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#acce77829b8bcc16d16367c1aec7d4323)
- [sim7080_ue_sys_info_lte::band](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#ada937e5906995e3b0c1487bf572e30e5)
- [sim7080_ue_sys_info_lte::earfcn](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#adce93c6c4192d090c06622aaebaa87e0)
- [sim7080_ue_sys_info_lte::rsrp](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#ae398efdcfd7c31e42ea135b334c51946)
- [sim7080_ue_sys_info_lte::tac](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#aed7ef4908901397958bc121138807c1e)
- [sim7080_ue_sys_info_lte::pci](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#af0072ee8fa216a544b9b762672279ebd)
- [sim7080_ue_sys_info_lte::rsrq](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md#af3f5afa6ba5bc07de4f01886c7083a44)
- [sim7080_ue_sys_info::sys_mode](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md#a47f14459263b13749a3722107a20631c)
- [sim7080_ue_sys_info::op_mode](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md#a77e0794049df94d1c6c106a1554fa6ea)
- [sim7080_ue_sys_info::cell](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md#ab42417fa5673818a5236e61a791d6c20)
- [sim7080_ue_sys_info::lte](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md#ace117d5d35a3b6a41b87b05315f7a19e)
- [sim7080_ue_sys_info::gsm](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md#ae2010949f786b1ee107cbfc34e207412)

---

[上一章](P785_silabs_dcdc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P787_sip_svc.h_源码浏览.md)
