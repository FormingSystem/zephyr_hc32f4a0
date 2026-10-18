---
id: learning.zephyr-docs.api-source-system-reference.page-16
title: l2cap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_l2cap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)。

## 16.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
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
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="foldopen00186"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="foldopen00201"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="foldopen00220"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="foldopen00232"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="foldopen00244"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00271"></a>
<a id="l00296"></a>
<a id="l00297"></a>
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
<a id="l00310"></a>
<a id="l00312"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="foldopen00342"></a>
<a id="l00342"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="foldopen00402"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00407"></a>
<a id="l00409"></a>
<a id="l00411"></a>
<a id="l00413"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="foldopen00423"></a>
<a id="l00423"></a>
<a id="l00425"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00432"></a>
<a id="l00442"></a>
<a id="l00450"></a>
<a id="l00457"></a>
<a id="l00462"></a>
<a id="l00464"></a>
<a id="l00470"></a>
<a id="l00481"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="foldopen00493"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00497"></a>
<a id="l00499"></a>
<a id="l00501"></a>
<a id="l00503"></a>
<a id="l00505"></a>
<a id="l00507"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="foldopen00517"></a>
<a id="l00517"></a>
<a id="l00519"></a>
<a id="l00521"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00529"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00539"></a>
<a id="l00541"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00565"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00578"></a>
<a id="l00582"></a>
<a id="l00586"></a>
<a id="l00594"></a>
<a id="l00597"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00607"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00612"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="foldopen00630"></a>
<a id="l00630"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="foldopen00809"></a>
<a id="l00809"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00960"></a>
<a id="l00961"></a>
<a id="l01005"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01097"></a>
<a id="l01098"></a>
<a id="l01120"></a>
<a id="l01121"></a>
<a id="l01134"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="aatomic_8h_html"></a>
<a id="abuf_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__atomic__apis_html_ga249c575db9764486197709b327f7370e"></a>
<a id="agroup__bt__conn_html_gaf0c56cd26c4147f6c9f0faa11fa01783"></a>
<a id="agroup__bt__l2cap_html_ga05d28a51d9fba08d609287957ea4c7ec"></a>
<a id="agroup__bt__l2cap_html_ga1a5e8c81c086872d7fb8da5329f982c6"></a>
<a id="agroup__bt__l2cap_html_ga371a747c8939a1156111dc03c774015c"></a>
<a id="agroup__bt__l2cap_html_ga3a1a88a8e87aefe9bea1dd01aa193b42"></a>
<a id="agroup__bt__l2cap_html_ga3c3cfb4b151c808c0a3d2562a5c26a20"></a>
<a id="agroup__bt__l2cap_html_ga5a80330e52ea0fa4ee3266094570bb16"></a>
<a id="agroup__bt__l2cap_html_ga5b0ae2abd714f46e6bb2394bce33e613"></a>
<a id="agroup__bt__l2cap_html_ga642436bdf29f79495763b10231c6b25b"></a>
<a id="agroup__bt__l2cap_html_ga67e13b0048eb68ef35c315a5276d832d"></a>
<a id="agroup__bt__l2cap_html_ga7165f82a05e3a19d6b2baf0ba292a3fe"></a>
<a id="agroup__bt__l2cap_html_ga723f47b211cd446d0980332f07211638"></a>
<a id="agroup__bt__l2cap_html_ga88baae9c159f3de4ccb34fd0e3cc8c3b"></a>
<a id="agroup__bt__l2cap_html_ga97b7909749667f910f83e6fcb54495c3"></a>
<a id="agroup__bt__l2cap_html_ga9bc950a929fc2bdb1463c268cea478b6"></a>
<a id="agroup__bt__l2cap_html_gad53f5fc31314121ff84e740879eae3cf"></a>
<a id="agroup__bt__l2cap_html_gaebc2d157fb5f013722e9c332b3d81804"></a>
<a id="agroup__bt__l2cap_html_gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e"></a>
<a id="agroup__bt__l2cap_html_gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5"></a>
<a id="agroup__bt__l2cap_html_gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c"></a>
<a id="agroup__bt__l2cap_html_gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af"></a>
<a id="agroup__bt__l2cap_html_gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c"></a>
<a id="agroup__bt__l2cap_html_gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064"></a>
<a id="agroup__bt__l2cap_html_gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68"></a>
<a id="agroup__bt__l2cap_html_gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8"></a>
<a id="agroup__bt__l2cap_html_gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ahci_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="anet__buf_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__l2cap__br__chan_html"></a>
<a id="astructbt__l2cap__br__chan_html_a00d49d2d73f2dafdc73a9f7b9393b98d"></a>
<a id="astructbt__l2cap__br__chan_html_a09ded589b7e1571fc5d021ceafa68b5f"></a>
<a id="astructbt__l2cap__br__chan_html_a0e637544c14d7d2b0ccd2af5424555fb"></a>
<a id="astructbt__l2cap__br__chan_html_a19bb2e243fb616b73d8b082df7c4a394"></a>
<a id="astructbt__l2cap__br__chan_html_a1ca3ed81f6f8edafc2993941de4c9771"></a>
<a id="astructbt__l2cap__br__chan_html_a21224ab26501eca21aaed468681d6274"></a>
<a id="astructbt__l2cap__br__chan_html_a28ed2b2541697390c325c706d4ad8f0b"></a>
<a id="astructbt__l2cap__br__chan_html_a3f9621b9d02b70f1dc9492520ff7cd03"></a>
<a id="astructbt__l2cap__br__chan_html_a556858a2e539bd4d5ed2ae66f392dc74"></a>
<a id="astructbt__l2cap__br__chan_html_a67aec1f3bef3afe689c164185bd77f98"></a>
<a id="astructbt__l2cap__br__chan_html_a6a1788de2f5c037b46070a65c2a1111d"></a>
<a id="astructbt__l2cap__br__chan_html_a6e559e94251ce9ef1c7d139695adf7ef"></a>
<a id="astructbt__l2cap__br__chan_html_a734b9699538989fa8e5cec11eb84609e"></a>
<a id="astructbt__l2cap__br__chan_html_a96cb3a6bb3f3c97372c314eb1bfca32b"></a>
<a id="astructbt__l2cap__br__chan_html_a97266be01c9ee7e5f64f182173d50418"></a>
<a id="astructbt__l2cap__br__chan_html_aa1fd44c5eb136e1fbd0f46f09d5fde0a"></a>
<a id="astructbt__l2cap__br__chan_html_ac887d3192240594de4d6cb8d4af9553b"></a>
<a id="astructbt__l2cap__br__chan_html_ace996412a41a168c37d60d5e4096dc94"></a>
<a id="astructbt__l2cap__br__chan_html_ad4c352f1d43dce110ddf47c665b7ae17"></a>
<a id="astructbt__l2cap__br__chan_html_ae48194e987caf3153738f3027ec7022d"></a>
<a id="astructbt__l2cap__br__chan_html_afa3dcfc293485a09d76a67c30ee0acf8"></a>
<a id="astructbt__l2cap__br__endpoint_html"></a>
<a id="astructbt__l2cap__br__endpoint_html_a2b27b7017ddc68d5b8a597d4be45074c"></a>
<a id="astructbt__l2cap__br__endpoint_html_a4f272e96d31b00a3e50d8dcbc2303c57"></a>
<a id="astructbt__l2cap__br__endpoint_html_a8c66377adf1681079fa446b05eff7e8a"></a>
<a id="astructbt__l2cap__br__endpoint_html_aaeb46128990fe08c926d34049bbc2d6a"></a>
<a id="astructbt__l2cap__br__endpoint_html_ab5789c43d09f18f89bffdd829af90a7b"></a>
<a id="astructbt__l2cap__br__endpoint_html_aba3184618ab6e8a3db1808041d3a0f8d"></a>
<a id="astructbt__l2cap__br__endpoint_html_ac63ef5c2ae54fbcce9380a379a551595"></a>
<a id="astructbt__l2cap__br__endpoint_html_acbe4f6cc15bb20703fca53e7084b2ea7"></a>
<a id="astructbt__l2cap__br__endpoint_html_ae5cdb992cd40ce925863e05c7f647f5e"></a>
<a id="astructbt__l2cap__br__endpoint_html_af49eacd8794e580adc285d95613547f6"></a>
<a id="astructbt__l2cap__br__endpoint_html_af64e45ea279960b3db213c9ad3e1828c"></a>
<a id="astructbt__l2cap__br__window_html"></a>
<a id="astructbt__l2cap__br__window_html_a3332cc2a424d1e2d1438232594b81a95"></a>
<a id="astructbt__l2cap__br__window_html_a39456c041bd7d8badde949008835f891"></a>
<a id="astructbt__l2cap__br__window_html_a65acb18fd339978960419ffb2c95111e"></a>
<a id="astructbt__l2cap__br__window_html_a781e76efc763c70a9c716f4737fb9243"></a>
<a id="astructbt__l2cap__br__window_html_ab7bb9eb3949b37973228630b8acacd2f"></a>
<a id="astructbt__l2cap__br__window_html_ac2deea3f4fd7893408412ff6599c1a1a"></a>
<a id="astructbt__l2cap__br__window_html_acff85df74b031445a69c75cad1765e90"></a>
<a id="astructbt__l2cap__br__window_html_af34fbcec08495401b2516dd7e2ca6190"></a>
<a id="astructbt__l2cap__br__window_html_afb66e50f934e763680200ce209ca940c"></a>
<a id="astructbt__l2cap__br__window_html_affc53286b080a6914935577ffc15959c"></a>
<a id="astructbt__l2cap__chan__ops_html"></a>
<a id="astructbt__l2cap__chan__ops_html_a0ab419d3c52c08e0dfda236466d7cadd"></a>
<a id="astructbt__l2cap__chan__ops_html_a12f3290f9bd04fb5fe562c620dff6984"></a>
<a id="astructbt__l2cap__chan__ops_html_a2e5fcc77a5174de6e3933bb6a14e4ad3"></a>
<a id="astructbt__l2cap__chan__ops_html_a3a4dd75a11c9867adcade6d288dec2de"></a>
<a id="astructbt__l2cap__chan__ops_html_a4be7fadf07368750cc33cf034d3073e7"></a>
<a id="astructbt__l2cap__chan__ops_html_a6d974d0e472626cb1e5cd898a3dcbca6"></a>
<a id="astructbt__l2cap__chan__ops_html_a770c09f3fb10c9d1e069333d22803d1a"></a>
<a id="astructbt__l2cap__chan__ops_html_a7759a713038d74748952d5f2eb712429"></a>
<a id="astructbt__l2cap__chan__ops_html_afba426353897bc3a57c936a98acab839"></a>
<a id="astructbt__l2cap__chan_html"></a>
<a id="astructbt__l2cap__chan_html_a007a7ef11a00c0dff22cd64961260d3d"></a>
<a id="astructbt__l2cap__chan_html_a123ae4bb1db6f4b41561b3d4691b1c02"></a>
<a id="astructbt__l2cap__chan_html_a3e370744f17ca4cff200cc0a2ee1a74b"></a>
<a id="astructbt__l2cap__chan_html_a7603e2c212e0522a1ffca2198224a994"></a>
<a id="astructbt__l2cap__chan_html_ac0fbde11b35e0b6b424970e73c945a40"></a>
<a id="astructbt__l2cap__fixed__chan_html"></a>
<a id="astructbt__l2cap__fixed__chan_html_a5fd07168ff8a38d6b393ef82a41af9db"></a>
<a id="astructbt__l2cap__fixed__chan_html_a83f7dc42454778eed6f446a3875d7663"></a>
<a id="astructbt__l2cap__le__chan_html"></a>
<a id="astructbt__l2cap__le__chan_html_a059f98cebf6f43a05937ac82815009e7"></a>
<a id="astructbt__l2cap__le__chan_html_a55d8ce850f365ac7ab7ff450ecb61f23"></a>
<a id="astructbt__l2cap__le__chan_html_a716ea69cb7261076023d0cf6384b3ebb"></a>
<a id="astructbt__l2cap__le__chan_html_a95808ad9bcd910b65bee31fa6bd4b638"></a>
<a id="astructbt__l2cap__le__chan_html_a980126cabc3824ab623d634d91f7d761"></a>
<a id="astructbt__l2cap__le__endpoint_html"></a>
<a id="astructbt__l2cap__le__endpoint_html_a598f0c7f0ad4cc029013358d35ce9dc2"></a>
<a id="astructbt__l2cap__le__endpoint_html_aa9e4f21e48eda61a3d0b777ee13c2599"></a>
<a id="astructbt__l2cap__le__endpoint_html_ab3f475c383791731c595845c80c27edf"></a>
<a id="astructbt__l2cap__le__endpoint_html_aeee85135541b17bede098891b820c63f"></a>
<a id="astructbt__l2cap__server_html"></a>
<a id="astructbt__l2cap__server_html_a07925dda8566ee7518b1809725e1b110"></a>
<a id="astructbt__l2cap__server_html_a76b478140d6a57038eb389eac91442c0"></a>
<a id="astructbt__l2cap__server_html_a9f082abf679a397264a7b51fa4400852"></a>
<a id="astructbt__l2cap__server_html_ad31a1908f7dc733f9497164ccabba2af"></a>
<a id="astructk__fifo_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructk__work__sync_html"></a>
<a id="astructk__work_html"></a>
<a id="astructnet__buf__simple__state_html"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="astructnet__buf_html"></a>
<a id="asys_2util_8h_html"></a>

```c


/*
 * Copyright (c) 2015-2016 Intel Corporation
 * Copyright (c) 2023 Nordic Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_L2CAP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_L2CAP_H_


#include <stddef.h>
#include <stdint.h>

#include <zephyr/bluetooth/buf.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/hci.h>
#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util.h>
#include <sys/types.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_L2CAP_HDR_SIZE               4

#define BT_L2CAP_TX_MTU (CONFIG_BT_L2CAP_TX_MTU)

#define BT_L2CAP_RX_MTU (CONFIG_BT_BUF_ACL_RX_SIZE - BT_L2CAP_HDR_SIZE)

#define BT_L2CAP_BUF_SIZE(mtu) BT_BUF_ACL_SIZE(BT_L2CAP_HDR_SIZE + (mtu))

#define BT_L2CAP_SDU_HDR_SIZE           2

#define BT_L2CAP_SDU_TX_MTU (BT_L2CAP_TX_MTU - BT_L2CAP_SDU_HDR_SIZE)

#define BT_L2CAP_SDU_RX_MTU (BT_L2CAP_RX_MTU - BT_L2CAP_SDU_HDR_SIZE)

#define BT_L2CAP_SDU_BUF_SIZE(mtu) BT_L2CAP_BUF_SIZE(BT_L2CAP_SDU_HDR_SIZE + (mtu))

#define BT_L2CAP_ECRED_MIN_MTU 64

#define BT_L2CAP_ECRED_MIN_MPS 64

#define BT_L2CAP_MAX_MTU UINT16_MAX

#define BT_L2CAP_MAX_MPS 65533

#define BT_L2CAP_ECRED_CHAN_MAX_PER_REQ 5


#define BT_L2CAP_CID_BR_SIG             0x0001
#define BT_L2CAP_CID_ATT                0x0004
#define BT_L2CAP_CID_LE_SIG             0x0005
#define BT_L2CAP_CID_SMP                0x0006
#define BT_L2CAP_CID_BR_SMP             0x0007


struct bt_l2cap_chan;

typedef void (*bt_l2cap_chan_destroy_t)(struct bt_l2cap_chan *chan);

typedef enum bt_l2cap_chan_state {
        BT_L2CAP_DISCONNECTED,
        BT_L2CAP_CONNECTING,
        BT_L2CAP_CONFIG,
        BT_L2CAP_CONNECTED,
        BT_L2CAP_DISCONNECTING,

} __packed bt_l2cap_chan_state_t;

typedef enum bt_l2cap_chan_status {
        BT_L2CAP_STATUS_OUT,

        BT_L2CAP_STATUS_SHUTDOWN,

        BT_L2CAP_STATUS_ENCRYPT_PENDING,

        /* Total number of status - must be at the end of the enum */
        BT_L2CAP_NUM_STATUS,
} __packed bt_l2cap_chan_status_t;

struct bt_l2cap_chan {
        struct bt_conn                  *conn;
        const struct bt_l2cap_chan_ops  *ops;
        sys_snode_t                     node;
        bt_l2cap_chan_destroy_t         destroy;

        ATOMIC_DEFINE(status, BT_L2CAP_NUM_STATUS);
};

struct bt_l2cap_le_endpoint {
        uint16_t                                cid;
        uint16_t                                mtu;
        uint16_t                                mps;
        atomic_t                        credits;
};

struct bt_l2cap_le_chan {
        struct bt_l2cap_chan            chan;
        struct bt_l2cap_le_endpoint     rx;

        uint16_t pending_rx_mtu;

        struct bt_l2cap_le_endpoint     tx;
        struct k_fifo                   tx_queue;
#if defined(CONFIG_BT_L2CAP_DYNAMIC_CHANNEL)
        struct net_buf                  *_sdu;
        uint16_t                        _sdu_len;
#if defined(CONFIG_BT_L2CAP_SEG_RECV)
        uint16_t                        _sdu_len_done;
#endif /* CONFIG_BT_L2CAP_SEG_RECV */

        struct k_work                   rx_work;
        struct k_fifo                   rx_queue;

        bt_l2cap_chan_state_t           state;
        uint16_t                        psm;
        uint8_t                         ident;
        uint8_t                         pending_req;
        bt_security_t                   required_sec_level;

        /* Response Timeout eXpired (RTX) timer */
        struct k_work_delayable         rtx_work;
        struct k_work_sync              rtx_sync;
#endif

        sys_snode_t                     _pdu_ready;
        size_t                          _pdu_remaining;
};

#define BT_L2CAP_LE_CHAN(_ch) CONTAINER_OF(_ch, struct bt_l2cap_le_chan, chan)

struct bt_l2cap_fixed_chan {
        uint16_t cid;

        int (*accept)(struct bt_conn *conn, struct bt_l2cap_chan **chan);
};

#define BT_L2CAP_FIXED_CHANNEL_DEFINE(_name)                                                       \
        static const STRUCT_SECTION_ITERABLE(bt_l2cap_fixed_chan,                                  \
                                             _CONCAT(bt_l2cap_fixed_chan, _name))

#define BT_L2CAP_BR_LINK_MODE_BASIC  0x00
#define BT_L2CAP_BR_LINK_MODE_RET    0x01
#define BT_L2CAP_BR_LINK_MODE_FC     0x02
#define BT_L2CAP_BR_LINK_MODE_ERET   0x03
#define BT_L2CAP_BR_LINK_MODE_STREAM 0x04

#define BT_L2CAP_BR_FCS_NO    0x00
#define BT_L2CAP_BR_FCS_16BIT 0x01

struct bt_l2cap_br_endpoint {
        uint16_t                                cid;
        uint16_t                                mtu;
#if defined(CONFIG_BT_L2CAP_RET_FC) || defined(__DOXYGEN__)
        uint8_t                                 mode;
        bool                                    optional;
        uint8_t                                 max_transmit;
        uint16_t                                ret_timeout;
        uint16_t                                monitor_timeout;
        uint16_t                                mps;
        uint16_t                                max_window;
        uint8_t                                 fcs;
        bool                                    extended_control;
#endif /* CONFIG_BT_L2CAP_RET_FC */
};

struct bt_l2cap_br_window {
        sys_snode_t node;

        uint16_t tx_seq;
        uint16_t len;
        uint8_t *data;
        uint8_t transmit_counter;
        uint8_t sar;
        bool srej;
        bool retransmit;
        /* Save PDU state */
        struct net_buf_simple_state sdu_state;
        struct net_buf *sdu;
};

struct bt_l2cap_br_chan {
        struct bt_l2cap_chan            chan;
        struct bt_l2cap_br_endpoint     rx;
        struct bt_l2cap_br_endpoint     tx;
        /* For internal use only */
        atomic_t                        flags[1];

        bt_l2cap_chan_state_t           state;
        uint16_t                        psm;
        uint8_t                         ident;
        bt_security_t                   required_sec_level;

        /* Response Timeout eXpired (RTX) timer */
        struct k_work_delayable         rtx_work;
        struct k_work_sync              rtx_sync;

        sys_snode_t                     _pdu_ready;
        atomic_t                        _pdu_ready_lock;
        sys_slist_t                     _pdu_tx_queue;

#if defined(CONFIG_BT_L2CAP_RET_FC) || defined(__DOXYGEN__)
        size_t                          _pdu_remaining;

        struct net_buf                  *_pdu_buf;

        sys_slist_t                     _pdu_outstanding;

        struct net_buf_simple_state     _pdu_state;

        struct k_fifo                   _free_tx_win;

        struct bt_l2cap_br_window       tx_win[CONFIG_BT_L2CAP_MAX_WINDOW_SIZE];

        struct net_buf                  *_sdu;
        uint16_t                        _sdu_len;
#if defined(CONFIG_BT_L2CAP_SEG_RECV) || defined(__DOXYGEN__)
        uint16_t                        _sdu_len_done;
#endif /* CONFIG_BT_L2CAP_SEG_RECV */
        uint16_t                        tx_seq;
        uint16_t                        next_tx_seq;
        uint16_t                        expected_ack_seq;
        uint16_t                        req_seq;
        uint16_t                        expected_tx_seq;
        uint16_t                        buffer_seq;

        uint16_t                        retry_count;
        uint16_t                        srej_save_req_seq;

        struct k_work_delayable         ret_work;
        struct k_work_delayable         monitor_work;
#endif /* CONFIG_BT_L2CAP_RET_FC */
};

struct bt_l2cap_chan_ops {
        void (*connected)(struct bt_l2cap_chan *chan);

        void (*disconnected)(struct bt_l2cap_chan *chan);

        void (*encrypt_change)(struct bt_l2cap_chan *chan, uint8_t hci_status);

        struct net_buf *(*alloc_seg)(struct bt_l2cap_chan *chan);

        struct net_buf *(*alloc_buf)(struct bt_l2cap_chan *chan);

        int (*recv)(struct bt_l2cap_chan *chan, struct net_buf *buf);

        void (*sent)(struct bt_l2cap_chan *chan);

        void (*status)(struct bt_l2cap_chan *chan, atomic_t *status);

        /* @brief Channel released callback
         *
         * If this callback is set it is called when the stack has release all
         * references to the channel object.
         */
        void (*released)(struct bt_l2cap_chan *chan);

        void (*reconfigured)(struct bt_l2cap_chan *chan);

#if defined(CONFIG_BT_L2CAP_SEG_RECV) || defined(__DOXYGEN__)
        void (*seg_recv)(struct bt_l2cap_chan *chan, size_t sdu_len,
                         off_t seg_offset, struct net_buf_simple *seg);
#endif /* CONFIG_BT_L2CAP_SEG_RECV */
};

#define BT_L2CAP_CHAN_SEND_RESERVE (BT_L2CAP_BUF_SIZE(0))

#define BT_L2CAP_SDU_CHAN_SEND_RESERVE (BT_L2CAP_SDU_BUF_SIZE(0))

struct bt_l2cap_server {
        uint16_t                        psm;

        bt_security_t           sec_level;

        int (*accept)(struct bt_conn *conn, struct bt_l2cap_server *server,
                      struct bt_l2cap_chan **chan);

        sys_snode_t node;
};

int bt_l2cap_server_register(struct bt_l2cap_server *server);

int bt_l2cap_br_server_register(struct bt_l2cap_server *server);

int bt_l2cap_br_server_unregister(struct bt_l2cap_server *server);

int bt_l2cap_ecred_chan_connect(struct bt_conn *conn,
                                struct bt_l2cap_chan **chans, uint16_t psm);

int bt_l2cap_ecred_chan_reconfigure(struct bt_l2cap_chan **chans, uint16_t mtu);

int bt_l2cap_ecred_chan_reconfigure_explicit(struct bt_l2cap_chan **chans, size_t chan_count,
                                             uint16_t mtu, uint16_t mps);

int bt_l2cap_chan_connect(struct bt_conn *conn, struct bt_l2cap_chan *chan,
                          uint16_t psm);

int bt_l2cap_chan_disconnect(struct bt_l2cap_chan *chan);

int bt_l2cap_chan_send(struct bt_l2cap_chan *chan, struct net_buf *buf);

int bt_l2cap_chan_give_credits(struct bt_l2cap_chan *chan, uint16_t additional_credits);

int bt_l2cap_chan_recv_complete(struct bt_l2cap_chan *chan,
                                struct net_buf *buf);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_L2CAP_H_ */
```

## 16.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2015-2016 Intel Corporation。

版权（Copyright）：© 2023 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 215 行

状态总数（Total Number of Status），必须位于枚举（Enum）的末尾。

### 注释 3：原第 303 行

条件编译配置（Configuration）标记：`CONFIG_BT_L2CAP_SEG_RECV`。

### 注释 4：原第 317 行

响应超时计时器（Response Timeout eXpired，RTX Timer）。

### 注释 5：原第 489 行

条件编译配置（Configuration）标记：`CONFIG_BT_L2CAP_RET_FC`。

### 注释 6：原第 510 行

保存协议数据单元状态（PDU State）。

### 注释 7：原第 524 行

仅供内部使用（Internal Use Only）。

### 注释 8：原第 534 行

响应超时计时器（Response Timeout eXpired，RTX Timer）。

### 注释 9：原第 570 行

条件编译配置（Configuration）标记：`CONFIG_BT_L2CAP_SEG_RECV`。

### 注释 10：原第 615 行

条件编译配置（Configuration）标记：`CONFIG_BT_L2CAP_RET_FC`。

### 注释 11：原第 744 行

通道释放回调（Channel Released Callback）。

若设置了此回调，则协议栈（Stack）释放对通道对象（Channel Object）的全部引用（References）后会调用它。

### 注释 12：原第 795 行

条件编译配置（Configuration）标记：`CONFIG_BT_L2CAP_SEG_RECV`。

### 注释 13：原第 1145 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_L2CAP_H_`。

## 16.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/bluetooth/buf.h](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [sys/types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)
- [bt_l2cap_chan_destroy_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga88baae9c159f3de4ccb34fd0e3cc8c3b)
- [bt_l2cap_chan_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga642436bdf29f79495763b10231c6b25b)
- [BT_L2CAP_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c)
- [BT_L2CAP_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd)
- [BT_L2CAP_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064)
- [BT_L2CAP_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68)
- [BT_L2CAP_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8)
- [bt_l2cap_chan_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga5a80330e52ea0fa4ee3266094570bb16)
- [bt_l2cap_chan_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga371a747c8939a1156111dc03c774015c)
- [BT_L2CAP_STATUS_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5)
- [BT_L2CAP_STATUS_SHUTDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e)
- [BT_L2CAP_STATUS_ENCRYPT_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af)
- [BT_L2CAP_NUM_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c)
- [bt_l2cap_chan_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga3a1a88a8e87aefe9bea1dd01aa193b42)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [conn](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md#a007a7ef11a00c0dff22cd64961260d3d)
- [bt_l2cap_chan_ops](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md)
- [ops](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md#a3e370744f17ca4cff200cc0a2ee1a74b)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md#a123ae4bb1db6f4b41561b3d4691b1c02)
- [destroy](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md#ac0fbde11b35e0b6b424970e73c945a40)
- [ATOMIC_DEFINE](../atomic_reference/P001_原子操作公共接口.md#ga249c575db9764486197709b327f7370e)
- [status](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md#a7603e2c212e0522a1ffca2198224a994)
- [bt_l2cap_le_endpoint](../bluetooth_service_model_reference/P105_bt_l2cap_le_endpoint_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [cid](../bluetooth_service_model_reference/P105_bt_l2cap_le_endpoint_结构体.md#aeee85135541b17bede098891b820c63f)
- [mtu](../bluetooth_service_model_reference/P105_bt_l2cap_le_endpoint_结构体.md#a598f0c7f0ad4cc029013358d35ce9dc2)
- [mps](../bluetooth_service_model_reference/P105_bt_l2cap_le_endpoint_结构体.md#aa9e4f21e48eda61a3d0b777ee13c2599)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [credits](../bluetooth_service_model_reference/P105_bt_l2cap_le_endpoint_结构体.md#ab3f475c383791731c595845c80c27edf)
- [bt_l2cap_le_chan](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md)
- [chan](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md#a980126cabc3824ab623d634d91f7d761)
- [rx](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md#a95808ad9bcd910b65bee31fa6bd4b638)
- [pending_rx_mtu](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md#a55d8ce850f365ac7ab7ff450ecb61f23)
- [tx](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md#a059f98cebf6f43a05937ac82815009e7)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [tx_queue](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md#a716ea69cb7261076023d0cf6384b3ebb)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)
- [bt_l2cap_fixed_chan](../bluetooth_service_model_reference/P103_bt_l2cap_fixed_chan_结构体.md)
- [cid](../bluetooth_service_model_reference/P103_bt_l2cap_fixed_chan_结构体.md#a5fd07168ff8a38d6b393ef82a41af9db)
- [accept](../bluetooth_service_model_reference/P103_bt_l2cap_fixed_chan_结构体.md#a83f7dc42454778eed6f446a3875d7663)
- [bt_l2cap_br_endpoint](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md)
- [cid](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#acbe4f6cc15bb20703fca53e7084b2ea7)
- [mtu](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#aaeb46128990fe08c926d34049bbc2d6a)
- [mode](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#af49eacd8794e580adc285d95613547f6)
- [optional](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#af64e45ea279960b3db213c9ad3e1828c)
- [max_transmit](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#a8c66377adf1681079fa446b05eff7e8a)
- [ret_timeout](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#ae5cdb992cd40ce925863e05c7f647f5e)
- [monitor_timeout](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#a4f272e96d31b00a3e50d8dcbc2303c57)
- [mps](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#ab5789c43d09f18f89bffdd829af90a7b)
- [max_window](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#a2b27b7017ddc68d5b8a597d4be45074c)
- [fcs](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#ac63ef5c2ae54fbcce9380a379a551595)
- [extended_control](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#aba3184618ab6e8a3db1808041d3a0f8d)
- [bt_l2cap_br_window](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md)
- [node](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#acff85df74b031445a69c75cad1765e90)
- [tx_seq](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#afb66e50f934e763680200ce209ca940c)
- [len](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#a781e76efc763c70a9c716f4737fb9243)
- [data](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#a3332cc2a424d1e2d1438232594b81a95)
- [transmit_counter](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#ab7bb9eb3949b37973228630b8acacd2f)
- [sar](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#ac2deea3f4fd7893408412ff6599c1a1a)
- [srej](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#a39456c041bd7d8badde949008835f891)
- [retransmit](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#af34fbcec08495401b2516dd7e2ca6190)
- [net_buf_simple_state](../network_core_model_reference/P049_net_buf_simple_state_结构体.md)
- [sdu_state](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#a65acb18fd339978960419ffb2c95111e)
- [sdu](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#affc53286b080a6914935577ffc15959c)
- [bt_l2cap_br_chan](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md)
- [chan](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a28ed2b2541697390c325c706d4ad8f0b)
- [rx](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a00d49d2d73f2dafdc73a9f7b9393b98d)
- [tx](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a67aec1f3bef3afe689c164185bd77f98)
- [flags](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a09ded589b7e1571fc5d021ceafa68b5f)
- [state](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a556858a2e539bd4d5ed2ae66f392dc74)
- [psm](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a1ca3ed81f6f8edafc2993941de4c9771)
- [ident](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#ace996412a41a168c37d60d5e4096dc94)
- [required_sec_level](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a19bb2e243fb616b73d8b082df7c4a394)
- [rtx_work](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a0e637544c14d7d2b0ccd2af5424555fb)
- [rtx_sync](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a21224ab26501eca21aaed468681d6274)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [tx_win](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a96cb3a6bb3f3c97372c314eb1bfca32b)
- [tx_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#ad4c352f1d43dce110ddf47c665b7ae17)
- [next_tx_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a6e559e94251ce9ef1c7d139695adf7ef)
- [expected_ack_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#ae48194e987caf3153738f3027ec7022d)
- [req_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#afa3dcfc293485a09d76a67c30ee0acf8)
- [expected_tx_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a734b9699538989fa8e5cec11eb84609e)
- [buffer_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#aa1fd44c5eb136e1fbd0f46f09d5fde0a)
- [retry_count](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a3f9621b9d02b70f1dc9492520ff7cd03)
- [srej_save_req_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a97266be01c9ee7e5f64f182173d50418)
- [ret_work](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a6a1788de2f5c037b46070a65c2a1111d)
- [monitor_work](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#ac887d3192240594de4d6cb8d4af9553b)
- [connected](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a3a4dd75a11c9867adcade6d288dec2de)
- [disconnected](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a2e5fcc77a5174de6e3933bb6a14e4ad3)
- [encrypt_change](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a12f3290f9bd04fb5fe562c620dff6984)
- [recv](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a0ab419d3c52c08e0dfda236466d7cadd)
- [sent](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a770c09f3fb10c9d1e069333d22803d1a)
- [status](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a4be7fadf07368750cc33cf034d3073e7)
- [released](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a6d974d0e472626cb1e5cd898a3dcbca6)
- [reconfigured](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#afba426353897bc3a57c936a98acab839)
- [seg_recv](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a7759a713038d74748952d5f2eb712429)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_l2cap_server](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md)
- [psm](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md#a07925dda8566ee7518b1809725e1b110)
- [sec_level](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md#a9f082abf679a397264a7b51fa4400852)
- [accept](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md#ad31a1908f7dc733f9497164ccabba2af)
- [node](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md#a76b478140d6a57038eb389eac91442c0)
- [bt_l2cap_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga1a5e8c81c086872d7fb8da5329f982c6)
- [bt_l2cap_br_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga5b0ae2abd714f46e6bb2394bce33e613)
- [bt_l2cap_br_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga723f47b211cd446d0980332f07211638)
- [bt_l2cap_ecred_chan_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaebc2d157fb5f013722e9c332b3d81804)
- [bt_l2cap_ecred_chan_reconfigure](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga05d28a51d9fba08d609287957ea4c7ec)
- [bt_l2cap_ecred_chan_reconfigure_explicit](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga67e13b0048eb68ef35c315a5276d832d)
- [bt_l2cap_chan_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga3c3cfb4b151c808c0a3d2562a5c26a20)
- [bt_l2cap_chan_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga7165f82a05e3a19d6b2baf0ba292a3fe)
- [bt_l2cap_chan_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga97b7909749667f910f83e6fcb54495c3)
- [bt_l2cap_chan_give_credits](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga9bc950a929fc2bdb1463c268cea478b6)
- [bt_l2cap_chan_recv_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gad53f5fc31314121ff84e740879eae3cf)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [buf.h](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_l2cap_br_chan::rx](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a00d49d2d73f2dafdc73a9f7b9393b98d)
- [bt_l2cap_br_chan::flags](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a09ded589b7e1571fc5d021ceafa68b5f)
- [bt_l2cap_br_chan::rtx_work](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a0e637544c14d7d2b0ccd2af5424555fb)
- [bt_l2cap_br_chan::required_sec_level](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a19bb2e243fb616b73d8b082df7c4a394)
- [bt_l2cap_br_chan::psm](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a1ca3ed81f6f8edafc2993941de4c9771)
- [bt_l2cap_br_chan::rtx_sync](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a21224ab26501eca21aaed468681d6274)
- [bt_l2cap_br_chan::chan](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a28ed2b2541697390c325c706d4ad8f0b)
- [bt_l2cap_br_chan::retry_count](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a3f9621b9d02b70f1dc9492520ff7cd03)
- [bt_l2cap_br_chan::state](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a556858a2e539bd4d5ed2ae66f392dc74)
- [bt_l2cap_br_chan::tx](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a67aec1f3bef3afe689c164185bd77f98)
- [bt_l2cap_br_chan::ret_work](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a6a1788de2f5c037b46070a65c2a1111d)
- [bt_l2cap_br_chan::next_tx_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a6e559e94251ce9ef1c7d139695adf7ef)
- [bt_l2cap_br_chan::expected_tx_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a734b9699538989fa8e5cec11eb84609e)
- [bt_l2cap_br_chan::tx_win](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a96cb3a6bb3f3c97372c314eb1bfca32b)
- [bt_l2cap_br_chan::srej_save_req_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#a97266be01c9ee7e5f64f182173d50418)
- [bt_l2cap_br_chan::buffer_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#aa1fd44c5eb136e1fbd0f46f09d5fde0a)
- [bt_l2cap_br_chan::monitor_work](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#ac887d3192240594de4d6cb8d4af9553b)
- [bt_l2cap_br_chan::ident](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#ace996412a41a168c37d60d5e4096dc94)
- [bt_l2cap_br_chan::tx_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#ad4c352f1d43dce110ddf47c665b7ae17)
- [bt_l2cap_br_chan::expected_ack_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#ae48194e987caf3153738f3027ec7022d)
- [bt_l2cap_br_chan::req_seq](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md#afa3dcfc293485a09d76a67c30ee0acf8)
- [bt_l2cap_br_endpoint::max_window](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#a2b27b7017ddc68d5b8a597d4be45074c)
- [bt_l2cap_br_endpoint::monitor_timeout](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#a4f272e96d31b00a3e50d8dcbc2303c57)
- [bt_l2cap_br_endpoint::max_transmit](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#a8c66377adf1681079fa446b05eff7e8a)
- [bt_l2cap_br_endpoint::mtu](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#aaeb46128990fe08c926d34049bbc2d6a)
- [bt_l2cap_br_endpoint::mps](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#ab5789c43d09f18f89bffdd829af90a7b)
- [bt_l2cap_br_endpoint::extended_control](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#aba3184618ab6e8a3db1808041d3a0f8d)
- [bt_l2cap_br_endpoint::fcs](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#ac63ef5c2ae54fbcce9380a379a551595)
- [bt_l2cap_br_endpoint::cid](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#acbe4f6cc15bb20703fca53e7084b2ea7)
- [bt_l2cap_br_endpoint::ret_timeout](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#ae5cdb992cd40ce925863e05c7f647f5e)
- [bt_l2cap_br_endpoint::mode](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#af49eacd8794e580adc285d95613547f6)
- [bt_l2cap_br_endpoint::optional](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md#af64e45ea279960b3db213c9ad3e1828c)
- [bt_l2cap_br_window::data](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#a3332cc2a424d1e2d1438232594b81a95)
- [bt_l2cap_br_window::srej](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#a39456c041bd7d8badde949008835f891)
- [bt_l2cap_br_window::sdu_state](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#a65acb18fd339978960419ffb2c95111e)
- [bt_l2cap_br_window::len](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#a781e76efc763c70a9c716f4737fb9243)
- [bt_l2cap_br_window::transmit_counter](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#ab7bb9eb3949b37973228630b8acacd2f)
- [bt_l2cap_br_window::sar](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#ac2deea3f4fd7893408412ff6599c1a1a)
- [bt_l2cap_br_window::node](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#acff85df74b031445a69c75cad1765e90)
- [bt_l2cap_br_window::retransmit](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#af34fbcec08495401b2516dd7e2ca6190)
- [bt_l2cap_br_window::tx_seq](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#afb66e50f934e763680200ce209ca940c)
- [bt_l2cap_br_window::sdu](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md#affc53286b080a6914935577ffc15959c)
- [bt_l2cap_chan_ops::recv](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a0ab419d3c52c08e0dfda236466d7cadd)
- [bt_l2cap_chan_ops::encrypt_change](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a12f3290f9bd04fb5fe562c620dff6984)
- [bt_l2cap_chan_ops::disconnected](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a2e5fcc77a5174de6e3933bb6a14e4ad3)
- [bt_l2cap_chan_ops::connected](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a3a4dd75a11c9867adcade6d288dec2de)
- [bt_l2cap_chan_ops::status](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a4be7fadf07368750cc33cf034d3073e7)
- [bt_l2cap_chan_ops::released](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a6d974d0e472626cb1e5cd898a3dcbca6)
- [bt_l2cap_chan_ops::sent](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a770c09f3fb10c9d1e069333d22803d1a)
- [bt_l2cap_chan_ops::seg_recv](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a7759a713038d74748952d5f2eb712429)
- [bt_l2cap_chan_ops::reconfigured](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#afba426353897bc3a57c936a98acab839)
- [bt_l2cap_chan::conn](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md#a007a7ef11a00c0dff22cd64961260d3d)
- [bt_l2cap_chan::node](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md#a123ae4bb1db6f4b41561b3d4691b1c02)
- [bt_l2cap_chan::ops](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md#a3e370744f17ca4cff200cc0a2ee1a74b)
- [bt_l2cap_chan::status](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md#a7603e2c212e0522a1ffca2198224a994)
- [bt_l2cap_chan::destroy](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md#ac0fbde11b35e0b6b424970e73c945a40)
- [bt_l2cap_fixed_chan::cid](../bluetooth_service_model_reference/P103_bt_l2cap_fixed_chan_结构体.md#a5fd07168ff8a38d6b393ef82a41af9db)
- [bt_l2cap_fixed_chan::accept](../bluetooth_service_model_reference/P103_bt_l2cap_fixed_chan_结构体.md#a83f7dc42454778eed6f446a3875d7663)
- [bt_l2cap_le_chan::tx](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md#a059f98cebf6f43a05937ac82815009e7)
- [bt_l2cap_le_chan::pending_rx_mtu](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md#a55d8ce850f365ac7ab7ff450ecb61f23)
- [bt_l2cap_le_chan::tx_queue](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md#a716ea69cb7261076023d0cf6384b3ebb)
- [bt_l2cap_le_chan::rx](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md#a95808ad9bcd910b65bee31fa6bd4b638)
- [bt_l2cap_le_chan::chan](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md#a980126cabc3824ab623d634d91f7d761)
- [bt_l2cap_le_endpoint::mtu](../bluetooth_service_model_reference/P105_bt_l2cap_le_endpoint_结构体.md#a598f0c7f0ad4cc029013358d35ce9dc2)
- [bt_l2cap_le_endpoint::mps](../bluetooth_service_model_reference/P105_bt_l2cap_le_endpoint_结构体.md#aa9e4f21e48eda61a3d0b777ee13c2599)
- [bt_l2cap_le_endpoint::credits](../bluetooth_service_model_reference/P105_bt_l2cap_le_endpoint_结构体.md#ab3f475c383791731c595845c80c27edf)
- [bt_l2cap_le_endpoint::cid](../bluetooth_service_model_reference/P105_bt_l2cap_le_endpoint_结构体.md#aeee85135541b17bede098891b820c63f)
- [bt_l2cap_server::psm](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md#a07925dda8566ee7518b1809725e1b110)
- [bt_l2cap_server::node](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md#a76b478140d6a57038eb389eac91442c0)
- [bt_l2cap_server::sec_level](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md#a9f082abf679a397264a7b51fa4400852)
- [bt_l2cap_server::accept](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md#ad31a1908f7dc733f9497164ccabba2af)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P015_isotp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P017_mchp-xec-pinctrl.h_源码浏览.md)
