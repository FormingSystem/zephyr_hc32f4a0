---
id: learning.zephyr-docs.api-source-configuration-reference.page-30
title: server.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_server.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h.html)。

## 30.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
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
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
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
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="foldopen00114"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="foldopen00133"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="foldopen00156"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="foldopen00162"></a>
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
<a id="l00172"></a>
<a id="foldopen00174"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="foldopen00186"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="foldopen00193"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="foldopen00210"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="foldopen00219"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="foldopen00257"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="foldopen00298"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
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
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00392"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00447"></a>
<a id="foldopen00451"></a>
<a id="l00451"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00505"></a>
<a id="l00507"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00560"></a>
<a id="l00561"></a>
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
<a id="l00576"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00606"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="foldopen00616"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="agroup__http__methods_html_gaacd5f203e33ac338ca5cb8f02a3ff3b8"></a>
<a id="agroup__http__server_html_ga23d0077fb99827b25491111bd74d00af"></a>
<a id="agroup__http__server_html_ga53f208642bc31b937ce0b330054604f6"></a>
<a id="agroup__http__server_html_ga6c15e872ece1b9a740b6dca3974101b3"></a>
<a id="agroup__http__server_html_ga79f434b5bbc6d2a6ebc65a0c560730cf"></a>
<a id="agroup__http__server_html_ga8125ef45732f81ec1c629a8f41e4c14d"></a>
<a id="agroup__http__server_html_gaa51ec52c8960a37566d2ac77d624be93"></a>
<a id="agroup__http__server_html_gae15ea0da7140b38609492bf23ec35b4c"></a>
<a id="agroup__http__server_html_gaf124b6ddd491dd6075b9c68db6686607"></a>
<a id="agroup__http__server_html_gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e"></a>
<a id="agroup__http__server_html_gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248"></a>
<a id="agroup__http__server_html_gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866"></a>
<a id="agroup__http__server_html_gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e"></a>
<a id="agroup__http__server_html_gga53f208642bc31b937ce0b330054604f6ab08486d8498944dd2b90a2ff57049474"></a>
<a id="agroup__http__server_html_gga53f208642bc31b937ce0b330054604f6ac2fa76992c5f220ced91fa80347b6521"></a>
<a id="agroup__http__server_html_gga53f208642bc31b937ce0b330054604f6acafd3ffbcec7a27be5fc71a8a20e51eb"></a>
<a id="agroup__http__server_html_gga53f208642bc31b937ce0b330054604f6ae2f616c4343f1939758bdbe5dcb38ae2"></a>
<a id="agroup__http__server_html_gga6c15e872ece1b9a740b6dca3974101b3a3f41dca87eecce1ac499389e72285621"></a>
<a id="agroup__http__server_html_gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed"></a>
<a id="agroup__http__server_html_gga6c15e872ece1b9a740b6dca3974101b3ad4ad497a135cc5855573cc0211e7b7ec"></a>
<a id="agroup__http__server_html_ggaf124b6ddd491dd6075b9c68db6686607a1a4a25c52411b1a87abca823223c7202"></a>
<a id="agroup__http__server_html_ggaf124b6ddd491dd6075b9c68db6686607a39d987341b53034e236ecc0a48f40ae8"></a>
<a id="agroup__http__server_html_ggaf124b6ddd491dd6075b9c68db6686607a710e784f734d4a574c302dc86f587aa0"></a>
<a id="agroup__http__server_html_ggaf124b6ddd491dd6075b9c68db6686607aa260077f859491f95c6ccb781a492e43"></a>
<a id="agroup__http__server_html_ggaf124b6ddd491dd6075b9c68db6686607ad7f9cc84c671c70f15bff03a2cf92c50"></a>
<a id="agroup__http__server_html_ggaf124b6ddd491dd6075b9c68db6686607ae0de360c2162dab5adddd76f47f55569"></a>
<a id="agroup__http__status__codes_html_gabc3b93f68c8bdd857ad32913628dfa8d"></a>
<a id="agroup__sys-util_html_gae67ffe50e848951dbde309ed569ea925"></a>
<a id="ahpack_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet_2socket_8h_html"></a>
<a id="aparser_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astatus_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructhttp__client__ctx_html"></a>
<a id="astructhttp__client__ctx_html_aaaa95f16bde409fab692fc193a692169"></a>
<a id="astructhttp__client__ctx_html_aab71d232273c8bb6374b44d15614a7e1"></a>
<a id="astructhttp__client__ctx_html_ab0695811450793361bc88ca0bb582c15"></a>
<a id="astructhttp__client__ctx_html_ac805cda657ee679d5ccbf80fcc6007b2"></a>
<a id="astructhttp__client__ctx_html_aca2c3fae568ad984d90646e6b543b959"></a>
<a id="astructhttp__client__ctx_html_ae20c4d4038a643bef49dbb77b497e7b1"></a>
<a id="astructhttp__client__ctx_html_ae8fe0bf1dd0e5015b077a01f01fa40e9"></a>
<a id="astructhttp__client__ctx_html_afcc28f111655bab47516d2e71468bc55"></a>
<a id="astructhttp__content__type_html"></a>
<a id="astructhttp__content__type_html_a78e378def414fd5d9ad9df45df9144fe"></a>
<a id="astructhttp__content__type_html_a9235678c39a82386df70ad5efdcc33ab"></a>
<a id="astructhttp__content__type_html_afe5cc6179e38766a3ee7a97a0e981cdd"></a>
<a id="astructhttp__header_html"></a>
<a id="astructhttp__header_html_acac6fa1c3ca33cd67119209dc981e5f9"></a>
<a id="astructhttp__header_html_afc8e4fa57f957f1fd34ce570c98537f5"></a>
<a id="astructhttp__hpack__header__buf_html"></a>
<a id="astructhttp__parser__settings_html"></a>
<a id="astructhttp__parser_html"></a>
<a id="astructhttp__request__ctx_html"></a>
<a id="astructhttp__request__ctx_html_a312cc4db494a0415a2c0342183b3a3c6"></a>
<a id="astructhttp__request__ctx_html_a404ff7f9946f162dc0ef6c0a872bf88b"></a>
<a id="astructhttp__request__ctx_html_a4de5c3114220bef60bcd587f4796603e"></a>
<a id="astructhttp__request__ctx_html_a9500727563dd6f33663c0a26299a16a6"></a>
<a id="astructhttp__request__ctx_html_aae773946b597bb7ca70d071daadf3c1d"></a>
<a id="astructhttp__resource__detail__dynamic_html"></a>
<a id="astructhttp__resource__detail__dynamic_html_a8b6170c4d98efa27616d1e3132c61cd4"></a>
<a id="astructhttp__resource__detail__dynamic_html_a9f131e0302bbdff94ae6d5147413bec7"></a>
<a id="astructhttp__resource__detail__dynamic_html_aa06123f6333e561d515a3d1468ec0856"></a>
<a id="astructhttp__resource__detail__dynamic_html_aed22a9df2725eab8fc1032903cecacab"></a>
<a id="astructhttp__resource__detail__static__fs_html"></a>
<a id="astructhttp__resource__detail__static__fs_html_a3cb3f688d0070ad3316f33bc05a78f78"></a>
<a id="astructhttp__resource__detail__static__fs_html_a5b25a03b953313b392096bab2faa3be8"></a>
<a id="astructhttp__resource__detail__static_html"></a>
<a id="astructhttp__resource__detail__static_html_a177c212ecfd8e0320200b4ed841f0484"></a>
<a id="astructhttp__resource__detail__static_html_a1ac562d11ee9b73c2cdcffe81f5a43b9"></a>
<a id="astructhttp__resource__detail__static_html_a67e4e9166d571d44763f3f7cecd34725"></a>
<a id="astructhttp__resource__detail__websocket_html"></a>
<a id="astructhttp__resource__detail__websocket_html_a512b5da3bdc20eca57c060160c823117"></a>
<a id="astructhttp__resource__detail__websocket_html_a8f6ceaee3ccae18974fbc2c6498737c8"></a>
<a id="astructhttp__resource__detail__websocket_html_acd10efe8ca1f82fb6e0557512f18d9ee"></a>
<a id="astructhttp__resource__detail__websocket_html_ad3a18df78d4ab4443bba2fbf00a0cbc0"></a>
<a id="astructhttp__resource__detail__websocket_html_adbfb331ad424fac889f5e53bb1240ed8"></a>
<a id="astructhttp__resource__detail__websocket_html_af9c3292e2d450b70831812cb9d084e3c"></a>
<a id="astructhttp__resource__detail_html"></a>
<a id="astructhttp__resource__detail_html_ac3aa9d4f3781a974739810af5a9e8860"></a>
<a id="astructhttp__resource__detail_html_acea8d8ff42d8b6ba7d451d3c4de40084"></a>
<a id="astructhttp__resource__detail_html_ae391e85a5713bceef9228b93e876c817"></a>
<a id="astructhttp__resource__detail_html_ae5b2415ad3e42c164c4e20fd5bb67bd4"></a>
<a id="astructhttp__resource__detail_html_af90b58f593a0c5c8506efc7a54a9cf68"></a>
<a id="astructhttp__response__ctx_html"></a>
<a id="astructhttp__response__ctx_html_a53162ff65b66567b31ec323558bc1fe2"></a>
<a id="astructhttp__response__ctx_html_a63acf00d5ff891ab51107458c545399d"></a>
<a id="astructhttp__response__ctx_html_a7a7b446baf1a1ab343437ee527ddde95"></a>
<a id="astructhttp__response__ctx_html_a88b128e354c85f574409abd55633d2e2"></a>
<a id="astructhttp__response__ctx_html_aa027d1577dd19db43a17cdd0959b8e39"></a>
<a id="astructhttp__response__ctx_html_ada151e7a981885622a79a5ae1f12b2e9"></a>
<a id="astructk__work__delayable_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="asys_2util_8h_html_afa27c06d0ad6b949289431ad75f104ab"></a>

```c
/*
 * Copyright (c) 2023, Emna Rekik
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_HTTP_SERVER_H_
#define ZEPHYR_INCLUDE_NET_HTTP_SERVER_H_


#include <stdint.h>

#include <zephyr/kernel.h>
#include <zephyr/net/http/parser.h>
#include <zephyr/net/http/hpack.h>
#include <zephyr/net/http/status.h>
#include <zephyr/net/socket.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif


#if defined(CONFIG_HTTP_SERVER)
#define HTTP_SERVER_CLIENT_BUFFER_SIZE   CONFIG_HTTP_SERVER_CLIENT_BUFFER_SIZE
#define HTTP_SERVER_MAX_STREAMS          CONFIG_HTTP_SERVER_MAX_STREAMS
#define HTTP_SERVER_MAX_CONTENT_TYPE_LEN CONFIG_HTTP_SERVER_MAX_CONTENT_TYPE_LENGTH
#define HTTP_SERVER_MAX_URL_LENGTH       CONFIG_HTTP_SERVER_MAX_URL_LENGTH
#define HTTP_SERVER_MAX_HEADER_LEN       CONFIG_HTTP_SERVER_MAX_HEADER_LEN
#else
#define HTTP_SERVER_CLIENT_BUFFER_SIZE   0
#define HTTP_SERVER_MAX_STREAMS          0
#define HTTP_SERVER_MAX_CONTENT_TYPE_LEN 0
#define HTTP_SERVER_MAX_URL_LENGTH       0
#define HTTP_SERVER_MAX_HEADER_LEN       0
#endif

#if defined(CONFIG_HTTP_SERVER_CAPTURE_HEADERS)
#define HTTP_SERVER_CAPTURE_HEADER_BUFFER_SIZE CONFIG_HTTP_SERVER_CAPTURE_HEADER_BUFFER_SIZE
#define HTTP_SERVER_CAPTURE_HEADER_COUNT       CONFIG_HTTP_SERVER_CAPTURE_HEADER_COUNT
#else
#define HTTP_SERVER_CAPTURE_HEADER_BUFFER_SIZE 0
#define HTTP_SERVER_CAPTURE_HEADER_COUNT       0
#endif

#define HTTP2_PREFACE "PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n"


enum http_resource_type {
        HTTP_RESOURCE_TYPE_STATIC,

        HTTP_RESOURCE_TYPE_STATIC_FS,

        HTTP_RESOURCE_TYPE_DYNAMIC,

        HTTP_RESOURCE_TYPE_WEBSOCKET,
};

struct http_resource_detail {
        uint32_t bitmask_of_supported_http_methods;

        enum http_resource_type type;

        int path_len;

        const char *content_encoding;

        const char *content_type;
};

BUILD_ASSERT(NUM_BITS(
             sizeof(((struct http_resource_detail *)0)->bitmask_of_supported_http_methods))
             >= (HTTP_METHOD_END_VALUE - 1));

struct http_resource_detail_static {
        struct http_resource_detail common;

        const void *static_data;

        size_t static_data_len;
};

/* Make sure that the common is the first in the struct. */
BUILD_ASSERT(offsetof(struct http_resource_detail_static, common) == 0);

struct http_resource_detail_static_fs {
        struct http_resource_detail common;

        const char *fs_path;
};

enum http_compression {
        HTTP_NONE = 0,
        HTTP_GZIP = 1,
        HTTP_COMPRESS = 2,
        HTTP_DEFLATE = 3,
        HTTP_BR = 4,
        HTTP_ZSTD = 5
};

/* Make sure that the common is the first in the struct. */
BUILD_ASSERT(offsetof(struct http_resource_detail_static_fs, common) == 0);

struct http_content_type {
        const char *extension;
        size_t extension_len;
        const char *content_type;
};

#define HTTP_SERVER_CONTENT_TYPE(_extension, _content_type)                                        \
        const STRUCT_SECTION_ITERABLE(http_content_type, _extension) = {                           \
                .extension = STRINGIFY(_extension),                                                \
                .extension_len = sizeof(STRINGIFY(_extension)) - 1,                                \
                .content_type = _content_type,                                                     \
        };

#define HTTP_SERVER_CONTENT_TYPE_FOREACH(_it) STRUCT_SECTION_FOREACH(http_content_type, _it)

struct http_client_ctx;

enum http_transaction_status {
        HTTP_SERVER_TRANSACTION_ABORTED = -1,
        HTTP_SERVER_REQUEST_DATA_MORE = 0,
        HTTP_SERVER_REQUEST_DATA_FINAL = 1,
        HTTP_SERVER_TRANSACTION_COMPLETE = 2,
};

enum http_header_status {
        HTTP_HEADER_STATUS_OK,
        HTTP_HEADER_STATUS_DROPPED,
        HTTP_HEADER_STATUS_NONE,
};

struct http_header {
        const char *name;
        const char *value;
};

struct http_request_ctx {
        uint8_t *data;
        size_t data_len;
        struct http_header *headers;
        size_t header_count;
        enum http_header_status headers_status;
};

struct http_response_ctx {
        enum http_status status;
        const struct http_header *headers;
        size_t header_count;
        const uint8_t *body;
        size_t body_len;
        bool final_chunk;
};

typedef int (*http_resource_dynamic_cb_t)(struct http_client_ctx *client,
                                          enum http_transaction_status status,
                                          const struct http_request_ctx *request_ctx,
                                          struct http_response_ctx *response_ctx,
                                          void *user_data);

struct http_resource_detail_dynamic {
        struct http_resource_detail common;

        http_resource_dynamic_cb_t cb;

        struct http_client_ctx *holder;

        void *user_data;
};

BUILD_ASSERT(offsetof(struct http_resource_detail_dynamic, common) == 0);

typedef int (*http_resource_websocket_cb_t)(int ws_socket, struct http_request_ctx *request_ctx,
                                            void *user_data);

struct http_resource_detail_websocket {
        struct http_resource_detail common;

        int ws_sock;

        http_resource_websocket_cb_t cb;

        uint8_t *data_buffer;

        size_t data_buffer_len;

        void *user_data;
};

BUILD_ASSERT(offsetof(struct http_resource_detail_websocket, common) == 0);

enum http2_stream_state {
        HTTP2_STREAM_IDLE,
        HTTP2_STREAM_RESERVED_LOCAL,
        HTTP2_STREAM_RESERVED_REMOTE,
        HTTP2_STREAM_OPEN,
        HTTP2_STREAM_HALF_CLOSED_LOCAL,
        HTTP2_STREAM_HALF_CLOSED_REMOTE,
        HTTP2_STREAM_CLOSED
};

enum http_server_state {
        HTTP_SERVER_FRAME_HEADER_STATE,
        HTTP_SERVER_PREFACE_STATE,
        HTTP_SERVER_REQUEST_STATE,
        HTTP_SERVER_FRAME_DATA_STATE,
        HTTP_SERVER_FRAME_HEADERS_STATE,
        HTTP_SERVER_FRAME_SETTINGS_STATE,
        HTTP_SERVER_FRAME_PRIORITY_STATE,
        HTTP_SERVER_FRAME_WINDOW_UPDATE_STATE,
        HTTP_SERVER_FRAME_CONTINUATION_STATE,
        HTTP_SERVER_FRAME_PING_STATE,
        HTTP_SERVER_FRAME_RST_STREAM_STATE,
        HTTP_SERVER_FRAME_GOAWAY_STATE,
        HTTP_SERVER_FRAME_PADDING_STATE,
        HTTP_SERVER_DONE_STATE,
        HTTP_SERVER_H3_STREAM_STATE,
};

enum http1_parser_state {
        HTTP1_INIT_HEADER_STATE,
        HTTP1_WAITING_HEADER_STATE,
        HTTP1_RECEIVING_HEADER_STATE,
        HTTP1_RECEIVED_HEADER_STATE,
        HTTP1_RECEIVING_DATA_STATE,
        HTTP1_MESSAGE_COMPLETE_STATE,
};

#define HTTP_SERVER_INITIAL_WINDOW_SIZE 65536
#define HTTP_SERVER_WS_MAX_SEC_KEY_LEN 32
#define HTTP_SERVER_WS_MAX_SEC_PROTOCOL_LEN 64

struct http2_stream_ctx {
        int stream_id;
        enum http2_stream_state stream_state;
        int window_size;

        struct http_resource_detail *current_detail;

        bool headers_sent : 1;

        bool end_stream_sent : 1;
};

struct http2_frame {
        uint32_t length;
        uint32_t stream_identifier;
        uint8_t type;
        uint8_t flags;
        uint8_t padding_len;
};

struct http_header_capture_ctx {
        unsigned char buffer[HTTP_SERVER_CAPTURE_HEADER_BUFFER_SIZE];

        struct http_header headers[HTTP_SERVER_CAPTURE_HEADER_COUNT];

        enum http_header_status status;

        size_t count;

        size_t cursor;

        struct http2_stream_ctx *current_stream;

        bool store_next_value;
};

struct http3_stream_ctx {
        unsigned char buffer[HTTP_SERVER_CLIENT_BUFFER_SIZE];

        size_t data_len;

        struct http_resource_detail *current_detail;

        unsigned char url_buffer[HTTP_SERVER_MAX_URL_LENGTH];

        enum http_method method;

        struct http_header_capture_ctx header_capture_ctx;

        bool request_headers_pending;

        bool early_data;
};

struct http_header_name {
        const char *name;
};

struct http_client_ctx {
        int fd;

        const struct http_service_desc *service;

        unsigned char buffer[HTTP_SERVER_CLIENT_BUFFER_SIZE];

        unsigned char *cursor;

        size_t data_len;

        int window_size;

        enum http_server_state server_state;

        struct http2_frame current_frame;

        struct http_resource_detail *current_detail;

        struct http2_stream_ctx *current_stream;

        struct http_hpack_header_buf header_field;

        struct http2_stream_ctx streams[HTTP_SERVER_MAX_STREAMS];

        struct http_parser_settings parser_settings;

        struct http_parser parser;

        struct http_header_capture_ctx header_capture_ctx;

        unsigned char url_buffer[HTTP_SERVER_MAX_URL_LENGTH];

        unsigned char content_type[HTTP_SERVER_MAX_CONTENT_TYPE_LEN];

        unsigned char header_buffer[HTTP_SERVER_MAX_HEADER_LEN];

        size_t content_len;

        enum http_method method;

        enum http1_parser_state parser_state;

        int http1_frag_data_len;

        struct k_work_delayable inactivity_timer;

        IF_ENABLED(CONFIG_WEBSOCKET, (uint8_t ws_sec_key[HTTP_SERVER_WS_MAX_SEC_KEY_LEN]));

        IF_ENABLED(CONFIG_WEBSOCKET,
                   (char ws_sec_protocol[HTTP_SERVER_WS_MAX_SEC_PROTOCOL_LEN]));

        IF_ENABLED(CONFIG_HTTP_SERVER_COMPRESSION, (uint8_t supported_compression));

        struct {
#if defined(CONFIG_HTTP_SERVER_VERSION_3)
                int conn_sock;

#define HTTP3_SERVER_MAX_STREAMS (CONFIG_QUIC_MAX_STREAMS_UNI + CONFIG_QUIC_MAX_STREAMS_BIDI)

                int stream_sock[HTTP3_SERVER_MAX_STREAMS];

                bool headers_sent[HTTP3_SERVER_MAX_STREAMS];

                struct http3_stream_ctx streams[HTTP3_SERVER_MAX_STREAMS];
#else
                /* This is here in order to avoid adding #ifdefs in the code related
                 * to the HTTP/3.
                 */
                union {
                        int conn_sock;
                        int stream_sock[0];
                        bool headers_sent[0];
                        struct http3_stream_ctx streams[0];
                };

#define HTTP3_SERVER_MAX_STREAMS 0
#endif /* CONFIG_HTTP_SERVER_VERSION_3 */
        } h3;

        bool is_h3 : 1;

        bool preface_sent : 1;

        bool http1_headers_sent : 1;

        bool has_upgrade_header : 1;

        bool http2_upgrade : 1;

        bool websocket_upgrade : 1;

        bool websocket_sec_key_next : 1;

        bool websocket_sec_protocol_next : 1;

        IF_ENABLED(CONFIG_HTTP_SERVER_COMPRESSION, (bool accept_encoding_next: 1));

        bool expect_continuation : 1;
};

#define HTTP_SERVER_REGISTER_HEADER_CAPTURE(_id, _header)                                          \
        BUILD_ASSERT(sizeof(_header) <= CONFIG_HTTP_SERVER_MAX_HEADER_LEN,                         \
                     "Header is too long to be captured, try increasing "                          \
                     "CONFIG_HTTP_SERVER_MAX_HEADER_LEN");                                         \
        static const char *const _id##_str = _header;                                              \
        static const STRUCT_SECTION_ITERABLE(http_header_name, _id) = {                            \
                .name = _id##_str,                                                                 \
        }

int http_server_start(void);

int http_server_stop(void);

#ifdef __cplusplus
}
#endif


#endif
```

## 30.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023, Emna Rekik。

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 126 行

确保公共部分（Common）是结构体中的第一个成员。

### 注释 3：原第 152 行

确保公共部分（Common）是结构体中的第一个成员。

### 注释 4：原第 562 行

将此项放在这里，是为了避免在 HTTP/3 相关代码中增加 `#ifdef`。

### 注释 5：原第 573 行

条件编译配置（Configuration）标记：`CONFIG_HTTP_SERVER_VERSION_3`。

## 30.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net/http/parser.h](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html)
- [zephyr/net/http/hpack.h](https://docs.zephyrproject.org/latest/doxygen/html/hpack_8h.html)
- [zephyr/net/http/status.h](https://docs.zephyrproject.org/latest/doxygen/html/status_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [http_resource_type](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga23d0077fb99827b25491111bd74d00af)
- [HTTP_RESOURCE_TYPE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248)
- [HTTP_RESOURCE_TYPE_STATIC_FS](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e)
- [HTTP_RESOURCE_TYPE_DYNAMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e)
- [HTTP_RESOURCE_TYPE_WEBSOCKET](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866)
- [http_resource_detail](../network_application_model_reference/P038_http_resource_detail_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bitmask_of_supported_http_methods](../network_application_model_reference/P038_http_resource_detail_结构体.md#ae391e85a5713bceef9228b93e876c817)
- [type](../network_application_model_reference/P038_http_resource_detail_结构体.md#af90b58f593a0c5c8506efc7a54a9cf68)
- [path_len](../network_application_model_reference/P038_http_resource_detail_结构体.md#ac3aa9d4f3781a974739810af5a9e8860)
- [content_encoding](../network_application_model_reference/P038_http_resource_detail_结构体.md#ae5b2415ad3e42c164c4e20fd5bb67bd4)
- [content_type](../network_application_model_reference/P038_http_resource_detail_结构体.md#acea8d8ff42d8b6ba7d451d3c4de40084)
- [NUM_BITS](../util_reference/P002_通用工具头文件参考.md#afa27c06d0ad6b949289431ad75f104ab)
- [http_resource_detail_static](../network_application_model_reference/P040_http_resource_detail_static_结构体.md)
- [common](../network_application_model_reference/P040_http_resource_detail_static_结构体.md#a67e4e9166d571d44763f3f7cecd34725)
- [static_data](../network_application_model_reference/P040_http_resource_detail_static_结构体.md#a1ac562d11ee9b73c2cdcffe81f5a43b9)
- [static_data_len](../network_application_model_reference/P040_http_resource_detail_static_结构体.md#a177c212ecfd8e0320200b4ed841f0484)
- [http_resource_detail_static_fs](../network_application_model_reference/P041_http_resource_detail_static_fs_结构体.md)
- [common](../network_application_model_reference/P041_http_resource_detail_static_fs_结构体.md#a3cb3f688d0070ad3316f33bc05a78f78)
- [fs_path](../network_application_model_reference/P041_http_resource_detail_static_fs_结构体.md#a5b25a03b953313b392096bab2faa3be8)
- [http_compression](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gaf124b6ddd491dd6075b9c68db6686607)
- [HTTP_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607a1a4a25c52411b1a87abca823223c7202)
- [HTTP_GZIP](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607a39d987341b53034e236ecc0a48f40ae8)
- [HTTP_COMPRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607ad7f9cc84c671c70f15bff03a2cf92c50)
- [HTTP_DEFLATE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607aa260077f859491f95c6ccb781a492e43)
- [HTTP_BR](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607ae0de360c2162dab5adddd76f47f55569)
- [HTTP_ZSTD](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ggaf124b6ddd491dd6075b9c68db6686607a710e784f734d4a574c302dc86f587aa0)
- [http_content_type](../network_application_model_reference/P029_http_content_type_结构体.md)
- [extension](../network_application_model_reference/P029_http_content_type_结构体.md#afe5cc6179e38766a3ee7a97a0e981cdd)
- [extension_len](../network_application_model_reference/P029_http_content_type_结构体.md#a9235678c39a82386df70ad5efdcc33ab)
- [content_type](../network_application_model_reference/P029_http_content_type_结构体.md#a78e378def414fd5d9ad9df45df9144fe)
- [http_client_ctx](../network_application_model_reference/P026_http_client_ctx_结构体.md)
- [http_transaction_status](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga53f208642bc31b937ce0b330054604f6)
- [HTTP_SERVER_TRANSACTION_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6ac2fa76992c5f220ced91fa80347b6521)
- [HTTP_SERVER_REQUEST_DATA_MORE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6ab08486d8498944dd2b90a2ff57049474)
- [HTTP_SERVER_REQUEST_DATA_FINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6ae2f616c4343f1939758bdbe5dcb38ae2)
- [HTTP_SERVER_TRANSACTION_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga53f208642bc31b937ce0b330054604f6acafd3ffbcec7a27be5fc71a8a20e51eb)
- [http_header_status](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga6c15e872ece1b9a740b6dca3974101b3)
- [HTTP_HEADER_STATUS_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga6c15e872ece1b9a740b6dca3974101b3ad4ad497a135cc5855573cc0211e7b7ec)
- [HTTP_HEADER_STATUS_DROPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga6c15e872ece1b9a740b6dca3974101b3a3f41dca87eecce1ac499389e72285621)
- [HTTP_HEADER_STATUS_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed)
- [http_header](../network_application_model_reference/P030_http_header_结构体.md)
- [name](../network_application_model_reference/P030_http_header_结构体.md#afc8e4fa57f957f1fd34ce570c98537f5)
- [value](../network_application_model_reference/P030_http_header_结构体.md#acac6fa1c3ca33cd67119209dc981e5f9)
- [http_request_ctx](../network_application_model_reference/P036_http_request_ctx_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../network_application_model_reference/P036_http_request_ctx_结构体.md#aae773946b597bb7ca70d071daadf3c1d)
- [data_len](../network_application_model_reference/P036_http_request_ctx_结构体.md#a4de5c3114220bef60bcd587f4796603e)
- [headers](../network_application_model_reference/P036_http_request_ctx_结构体.md#a9500727563dd6f33663c0a26299a16a6)
- [header_count](../network_application_model_reference/P036_http_request_ctx_结构体.md#a404ff7f9946f162dc0ef6c0a872bf88b)
- [headers_status](../network_application_model_reference/P036_http_request_ctx_结构体.md#a312cc4db494a0415a2c0342183b3a3c6)
- [http_response_ctx](../network_application_model_reference/P044_http_response_ctx_结构体.md)
- [http_status](https://docs.zephyrproject.org/latest/doxygen/html/group__http__status__codes.html#gabc3b93f68c8bdd857ad32913628dfa8d)
- [status](../network_application_model_reference/P044_http_response_ctx_结构体.md#ada151e7a981885622a79a5ae1f12b2e9)
- [headers](../network_application_model_reference/P044_http_response_ctx_结构体.md#a63acf00d5ff891ab51107458c545399d)
- [header_count](../network_application_model_reference/P044_http_response_ctx_结构体.md#a7a7b446baf1a1ab343437ee527ddde95)
- [body](../network_application_model_reference/P044_http_response_ctx_结构体.md#aa027d1577dd19db43a17cdd0959b8e39)
- [body_len](../network_application_model_reference/P044_http_response_ctx_结构体.md#a88b128e354c85f574409abd55633d2e2)
- [final_chunk](../network_application_model_reference/P044_http_response_ctx_结构体.md#a53162ff65b66567b31ec323558bc1fe2)
- [http_resource_dynamic_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gae15ea0da7140b38609492bf23ec35b4c)
- [http_resource_detail_dynamic](../network_application_model_reference/P039_http_resource_detail_dynamic_结构体.md)
- [common](../network_application_model_reference/P039_http_resource_detail_dynamic_结构体.md#aed22a9df2725eab8fc1032903cecacab)
- [cb](../network_application_model_reference/P039_http_resource_detail_dynamic_结构体.md#a9f131e0302bbdff94ae6d5147413bec7)
- [holder](../network_application_model_reference/P039_http_resource_detail_dynamic_结构体.md#aa06123f6333e561d515a3d1468ec0856)
- [user_data](../network_application_model_reference/P039_http_resource_detail_dynamic_结构体.md#a8b6170c4d98efa27616d1e3132c61cd4)
- [http_resource_websocket_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gaa51ec52c8960a37566d2ac77d624be93)
- [http_resource_detail_websocket](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md)
- [common](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md#acd10efe8ca1f82fb6e0557512f18d9ee)
- [ws_sock](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md#adbfb331ad424fac889f5e53bb1240ed8)
- [cb](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md#ad3a18df78d4ab4443bba2fbf00a0cbc0)
- [data_buffer](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md#af9c3292e2d450b70831812cb9d084e3c)
- [data_buffer_len](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md#a512b5da3bdc20eca57c060160c823117)
- [user_data](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md#a8f6ceaee3ccae18974fbc2c6498737c8)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [http_method](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#gaacd5f203e33ac338ca5cb8f02a3ff3b8)
- [http_hpack_header_buf](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md)
- [http_parser_settings](../network_application_model_reference/P033_http_parser_settings_结构体.md)
- [http_parser](../network_application_model_reference/P032_http_parser_结构体.md)
- [content_len](../network_application_model_reference/P026_http_client_ctx_结构体.md#aca2c3fae568ad984d90646e6b543b959)
- [method](../network_application_model_reference/P026_http_client_ctx_结构体.md#ab0695811450793361bc88ca0bb582c15)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [IF_ENABLED](../util_reference/P001_通用工具公共接口.md#gae67ffe50e848951dbde309ed569ea925)
- [is_h3](../network_application_model_reference/P026_http_client_ctx_结构体.md#aaaa95f16bde409fab692fc193a692169)
- [preface_sent](../network_application_model_reference/P026_http_client_ctx_结构体.md#aab71d232273c8bb6374b44d15614a7e1)
- [http1_headers_sent](../network_application_model_reference/P026_http_client_ctx_结构体.md#ac805cda657ee679d5ccbf80fcc6007b2)
- [has_upgrade_header](../network_application_model_reference/P026_http_client_ctx_结构体.md#ae8fe0bf1dd0e5015b077a01f01fa40e9)
- [http2_upgrade](../network_application_model_reference/P026_http_client_ctx_结构体.md#afcc28f111655bab47516d2e71468bc55)
- [websocket_upgrade](../network_application_model_reference/P026_http_client_ctx_结构体.md#ae20c4d4038a643bef49dbb77b497e7b1)
- [http_server_start](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga8125ef45732f81ec1c629a8f41e4c14d)
- [http_server_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga79f434b5bbc6d2a6ebc65a0c560730cf)
- [hpack.h](https://docs.zephyrproject.org/latest/doxygen/html/hpack_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [parser.h](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html)
- [status.h](https://docs.zephyrproject.org/latest/doxygen/html/status_8h.html)
- [http_client_ctx::is_h3](../network_application_model_reference/P026_http_client_ctx_结构体.md#aaaa95f16bde409fab692fc193a692169)
- [http_client_ctx::preface_sent](../network_application_model_reference/P026_http_client_ctx_结构体.md#aab71d232273c8bb6374b44d15614a7e1)
- [http_client_ctx::method](../network_application_model_reference/P026_http_client_ctx_结构体.md#ab0695811450793361bc88ca0bb582c15)
- [http_client_ctx::http1_headers_sent](../network_application_model_reference/P026_http_client_ctx_结构体.md#ac805cda657ee679d5ccbf80fcc6007b2)
- [http_client_ctx::content_len](../network_application_model_reference/P026_http_client_ctx_结构体.md#aca2c3fae568ad984d90646e6b543b959)
- [http_client_ctx::websocket_upgrade](../network_application_model_reference/P026_http_client_ctx_结构体.md#ae20c4d4038a643bef49dbb77b497e7b1)
- [http_client_ctx::has_upgrade_header](../network_application_model_reference/P026_http_client_ctx_结构体.md#ae8fe0bf1dd0e5015b077a01f01fa40e9)
- [http_client_ctx::http2_upgrade](../network_application_model_reference/P026_http_client_ctx_结构体.md#afcc28f111655bab47516d2e71468bc55)
- [http_content_type::content_type](../network_application_model_reference/P029_http_content_type_结构体.md#a78e378def414fd5d9ad9df45df9144fe)
- [http_content_type::extension_len](../network_application_model_reference/P029_http_content_type_结构体.md#a9235678c39a82386df70ad5efdcc33ab)
- [http_content_type::extension](../network_application_model_reference/P029_http_content_type_结构体.md#afe5cc6179e38766a3ee7a97a0e981cdd)
- [http_header::value](../network_application_model_reference/P030_http_header_结构体.md#acac6fa1c3ca33cd67119209dc981e5f9)
- [http_header::name](../network_application_model_reference/P030_http_header_结构体.md#afc8e4fa57f957f1fd34ce570c98537f5)
- [http_request_ctx::headers_status](../network_application_model_reference/P036_http_request_ctx_结构体.md#a312cc4db494a0415a2c0342183b3a3c6)
- [http_request_ctx::header_count](../network_application_model_reference/P036_http_request_ctx_结构体.md#a404ff7f9946f162dc0ef6c0a872bf88b)
- [http_request_ctx::data_len](../network_application_model_reference/P036_http_request_ctx_结构体.md#a4de5c3114220bef60bcd587f4796603e)
- [http_request_ctx::headers](../network_application_model_reference/P036_http_request_ctx_结构体.md#a9500727563dd6f33663c0a26299a16a6)
- [http_request_ctx::data](../network_application_model_reference/P036_http_request_ctx_结构体.md#aae773946b597bb7ca70d071daadf3c1d)
- [http_resource_detail_dynamic::user_data](../network_application_model_reference/P039_http_resource_detail_dynamic_结构体.md#a8b6170c4d98efa27616d1e3132c61cd4)
- [http_resource_detail_dynamic::cb](../network_application_model_reference/P039_http_resource_detail_dynamic_结构体.md#a9f131e0302bbdff94ae6d5147413bec7)
- [http_resource_detail_dynamic::holder](../network_application_model_reference/P039_http_resource_detail_dynamic_结构体.md#aa06123f6333e561d515a3d1468ec0856)
- [http_resource_detail_dynamic::common](../network_application_model_reference/P039_http_resource_detail_dynamic_结构体.md#aed22a9df2725eab8fc1032903cecacab)
- [http_resource_detail_static_fs::common](../network_application_model_reference/P041_http_resource_detail_static_fs_结构体.md#a3cb3f688d0070ad3316f33bc05a78f78)
- [http_resource_detail_static_fs::fs_path](../network_application_model_reference/P041_http_resource_detail_static_fs_结构体.md#a5b25a03b953313b392096bab2faa3be8)
- [http_resource_detail_static::static_data_len](../network_application_model_reference/P040_http_resource_detail_static_结构体.md#a177c212ecfd8e0320200b4ed841f0484)
- [http_resource_detail_static::static_data](../network_application_model_reference/P040_http_resource_detail_static_结构体.md#a1ac562d11ee9b73c2cdcffe81f5a43b9)
- [http_resource_detail_static::common](../network_application_model_reference/P040_http_resource_detail_static_结构体.md#a67e4e9166d571d44763f3f7cecd34725)
- [http_resource_detail_websocket::data_buffer_len](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md#a512b5da3bdc20eca57c060160c823117)
- [http_resource_detail_websocket::user_data](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md#a8f6ceaee3ccae18974fbc2c6498737c8)
- [http_resource_detail_websocket::common](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md#acd10efe8ca1f82fb6e0557512f18d9ee)
- [http_resource_detail_websocket::cb](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md#ad3a18df78d4ab4443bba2fbf00a0cbc0)
- [http_resource_detail_websocket::ws_sock](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md#adbfb331ad424fac889f5e53bb1240ed8)
- [http_resource_detail_websocket::data_buffer](../network_application_model_reference/P042_http_resource_detail_websocket_结构体.md#af9c3292e2d450b70831812cb9d084e3c)
- [http_resource_detail::path_len](../network_application_model_reference/P038_http_resource_detail_结构体.md#ac3aa9d4f3781a974739810af5a9e8860)
- [http_resource_detail::content_type](../network_application_model_reference/P038_http_resource_detail_结构体.md#acea8d8ff42d8b6ba7d451d3c4de40084)
- [http_resource_detail::bitmask_of_supported_http_methods](../network_application_model_reference/P038_http_resource_detail_结构体.md#ae391e85a5713bceef9228b93e876c817)
- [http_resource_detail::content_encoding](../network_application_model_reference/P038_http_resource_detail_结构体.md#ae5b2415ad3e42c164c4e20fd5bb67bd4)
- [http_resource_detail::type](../network_application_model_reference/P038_http_resource_detail_结构体.md#af90b58f593a0c5c8506efc7a54a9cf68)
- [http_response_ctx::final_chunk](../network_application_model_reference/P044_http_response_ctx_结构体.md#a53162ff65b66567b31ec323558bc1fe2)
- [http_response_ctx::headers](../network_application_model_reference/P044_http_response_ctx_结构体.md#a63acf00d5ff891ab51107458c545399d)
- [http_response_ctx::header_count](../network_application_model_reference/P044_http_response_ctx_结构体.md#a7a7b446baf1a1ab343437ee527ddde95)
- [http_response_ctx::body_len](../network_application_model_reference/P044_http_response_ctx_结构体.md#a88b128e354c85f574409abd55633d2e2)
- [http_response_ctx::body](../network_application_model_reference/P044_http_response_ctx_结构体.md#aa027d1577dd19db43a17cdd0959b8e39)
- [http_response_ctx::status](../network_application_model_reference/P044_http_response_ctx_结构体.md#ada151e7a981885622a79a5ae1f12b2e9)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P029_hl7800.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P031_ieee802154.h_源码浏览.md)
