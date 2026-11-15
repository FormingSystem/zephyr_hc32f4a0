---
id: learning.zephyr-docs.api-source-reference.page-291
title: gnss.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第291章\_gnss.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h.html)。

## 291.1\_原始可见代码（Source Code）

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
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00099"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="foldopen00143"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="foldopen00198"></a>
<a id="l00198"></a>
<a id="l00202"></a>
<a id="l00206"></a>
<a id="l00210"></a>
<a id="l00214"></a>
<a id="l00218"></a>
<a id="l00222"></a>
<a id="l00226"></a>
<a id="l00230"></a>
<a id="l00234"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00243"></a>
<a id="foldopen00245"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="foldopen00258"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="foldopen00266"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00272"></a>
<a id="l00274"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="foldopen00289"></a>
<a id="l00289"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
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
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
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
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
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
<a id="l00465"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00559"></a>
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
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__clock__apis_html_ga9832cb0adc2d1866420e5c370a0863e2"></a>
<a id="agroup__gnss__interface__backend_html_ga63a98e08bc7e4b9c70a27de48dc9cd8c"></a>
<a id="agroup__gnss__interface__backend_html_ga79e5975d5ec6c0557af4a71004a6da93"></a>
<a id="agroup__gnss__interface__backend_html_ga8f617e5c8a0938e5eef4d69a3f753303"></a>
<a id="agroup__gnss__interface__backend_html_ga906cecc7e7173893106d6154c7421fc6"></a>
<a id="agroup__gnss__interface__backend_html_ga91948cc0567c343bee62b6c70a2f461d"></a>
<a id="agroup__gnss__interface__backend_html_ga9705b36019161fde431e78d943eff604"></a>
<a id="agroup__gnss__interface__backend_html_gaa482aa8a996b743aba7e68f36b4780a8"></a>
<a id="agroup__gnss__interface__backend_html_gad87bd07c46ea1f79caf9a484c51ec0c9"></a>
<a id="agroup__gnss__interface__backend_html_gae946fce6ecced7c8fa09e06d75855abe"></a>
<a id="agroup__gnss__interface__backend_html_gaf52a65dee0d28286ac40e5c8bc86825a"></a>
<a id="agroup__gnss__interface_html_ga025c965369275ad8e5ab5ad44c14a23b"></a>
<a id="agroup__gnss__interface_html_ga155126e113195c08158ef49e2a6b4f6a"></a>
<a id="agroup__gnss__interface_html_ga15536308e2229a45493d06e8b61e63d9"></a>
<a id="agroup__gnss__interface_html_ga16e8326737f114bd6017983812c7f28d"></a>
<a id="agroup__gnss__interface_html_ga2b43ac2fec33053a769b7070c4ed3263"></a>
<a id="agroup__gnss__interface_html_ga43f285927c94079e3b72e81303cff520"></a>
<a id="agroup__gnss__interface_html_ga598609846ff196ff300fcad8237b2d51"></a>
<a id="agroup__gnss__interface_html_ga6bdabc1e89f5c7b10c1099fa74e6c6ca"></a>
<a id="agroup__gnss__interface_html_ga7106633a65ddaa29e19ba9f15b86f0f9"></a>
<a id="agroup__gnss__interface_html_ga731907f9ae501909bf26ecae5441a5ce"></a>
<a id="agroup__gnss__interface_html_ga80cf700468d1c942cfa064368e212e6f"></a>
<a id="agroup__gnss__interface_html_ga818e42c7a979623679eba26887662823"></a>
<a id="agroup__gnss__interface_html_ga8e625fb3f8758eab78c115d12bef6a72"></a>
<a id="agroup__gnss__interface_html_ga8eb37446d71c020e0517a406ea240fc2"></a>
<a id="agroup__gnss__interface_html_ga928a05b4e820a9fcc8bc2db81f5f8c79"></a>
<a id="agroup__gnss__interface_html_ga9d0347640e68d5702b1cb43ddf8380df"></a>
<a id="agroup__gnss__interface_html_gacf5a3464c487ae7609d526c73ccc758a"></a>
<a id="agroup__gnss__interface_html_gadb734bb12433276d3014e08a1d21bb18"></a>
<a id="agroup__gnss__interface_html_gae5614f8125dad02a3ebd30400b575e6d"></a>
<a id="agroup__gnss__interface_html_gga15536308e2229a45493d06e8b61e63d9a19c4e932246f410ee702122d80fbfbeb"></a>
<a id="agroup__gnss__interface_html_gga15536308e2229a45493d06e8b61e63d9a213553f5fa30cfa99317fcc28d0af1cc"></a>
<a id="agroup__gnss__interface_html_gga15536308e2229a45493d06e8b61e63d9a508bbeea1550d5020e579e6a311fbdbe"></a>
<a id="agroup__gnss__interface_html_gga15536308e2229a45493d06e8b61e63d9a8ad1fb7bf9f4d2607cb86f40a901e343"></a>
<a id="agroup__gnss__interface_html_gga2b43ac2fec33053a769b7070c4ed3263a2df416ad912a84135eff1e30977b4507"></a>
<a id="agroup__gnss__interface_html_gga2b43ac2fec33053a769b7070c4ed3263a5e9af4b08bd41a1aa1bf01c0e290d9fc"></a>
<a id="agroup__gnss__interface_html_gga2b43ac2fec33053a769b7070c4ed3263a9cdbb144191c83f4a7a2cc27268eacfa"></a>
<a id="agroup__gnss__interface_html_gga2b43ac2fec33053a769b7070c4ed3263afc82bd9ebcfd9d3b6111c9e82fc79ecc"></a>
<a id="agroup__gnss__interface_html_gga7106633a65ddaa29e19ba9f15b86f0f9ad0ecfd51dd2e99b5bd7e8abd49143da7"></a>
<a id="agroup__gnss__interface_html_gga7106633a65ddaa29e19ba9f15b86f0f9adff054d3999e9f0c2f3c6efc96772cc8"></a>
<a id="agroup__gnss__interface_html_gga7106633a65ddaa29e19ba9f15b86f0f9af594a76c0f37da20791b1ce4e2a4f5a3"></a>
<a id="agroup__gnss__interface_html_gga928a05b4e820a9fcc8bc2db81f5f8c79a1456923f0dd999b26e167fccc2461d5c"></a>
<a id="agroup__gnss__interface_html_gga928a05b4e820a9fcc8bc2db81f5f8c79a25a0162daa071267b63d2c7331a46c55"></a>
<a id="agroup__gnss__interface_html_gga928a05b4e820a9fcc8bc2db81f5f8c79a3e759b71b7e531d6c2c3068108e263dd"></a>
<a id="agroup__gnss__interface_html_gga928a05b4e820a9fcc8bc2db81f5f8c79a6a216ab95d09806435af4257b4d189e9"></a>
<a id="agroup__gnss__interface_html_gga928a05b4e820a9fcc8bc2db81f5f8c79a6f5a6de0d8196df55ade83d1f09de7dd"></a>
<a id="agroup__gnss__interface_html_gga928a05b4e820a9fcc8bc2db81f5f8c79a833e14eb77d70b3c5eb2843026b63242"></a>
<a id="agroup__gnss__interface_html_gga928a05b4e820a9fcc8bc2db81f5f8c79a84d3fc7ebefad4b20c58335bb7ca3e33"></a>
<a id="agroup__gnss__interface_html_gga928a05b4e820a9fcc8bc2db81f5f8c79aac9ccafec388c071468ef16981679dff"></a>
<a id="agroup__gnss__interface_html_ggacf5a3464c487ae7609d526c73ccc758aa316ea7e84abca8f04bbf95d3d73cea3f"></a>
<a id="agroup__gnss__interface_html_ggacf5a3464c487ae7609d526c73ccc758aa5256b22bb56e93c788d52a641c2a15a6"></a>
<a id="agroup__gnss__interface_html_ggacf5a3464c487ae7609d526c73ccc758aa65df312eef5cd8b24384440629f534f8"></a>
<a id="agroup__gnss__interface_html_ggacf5a3464c487ae7609d526c73ccc758aa67256fb63beab67ba6e7cbb63916af30"></a>
<a id="agroup__gnss__interface_html_ggacf5a3464c487ae7609d526c73ccc758aa851d88a47c1314eed8bc25e5cc7ba35a"></a>
<a id="agroup__gnss__interface_html_ggacf5a3464c487ae7609d526c73ccc758aab4de07a3891e7c89d5bd23fec7add20f"></a>
<a id="agroup__gnss__interface_html_ggacf5a3464c487ae7609d526c73ccc758aaedd76bb21200df49fd82243d4a394ac6"></a>
<a id="agroup__gnss__interface_html_ggadb734bb12433276d3014e08a1d21bb18a5f57c5f13e22a94c003f582e8c41a27f"></a>
<a id="agroup__gnss__interface_html_ggadb734bb12433276d3014e08a1d21bb18a96f01438a205c0d557eb5ea4f80425ff"></a>
<a id="agroup__gnss__interface_html_ggadb734bb12433276d3014e08a1d21bb18ab7fd6073a1e7d28ebf6ae9bc51ded88d"></a>
<a id="agroup__gnss__interface_html_ggadb734bb12433276d3014e08a1d21bb18ac5f4b57f2b0f732f9ae8051cb8ac9453"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anavigation_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructgnss__data__callback_html"></a>
<a id="astructgnss__data__callback_html_a07e9c7fd6192fd5b58ff37aabdbff11e"></a>
<a id="astructgnss__data__callback_html_afdf273ceed2d2038b6415840f9ecdd7b"></a>
<a id="astructgnss__data_html"></a>
<a id="astructgnss__data_html_a2470031921179cb30172441163d80052"></a>
<a id="astructgnss__data_html_a78155e6d2c981b9121b2ee42c1700988"></a>
<a id="astructgnss__data_html_ae6bfc0c6a53901963a1d20bad025fb99"></a>
<a id="astructgnss__driver__api_html"></a>
<a id="astructgnss__driver__api_html_a0d79083d56a7a35c3a2c858e2c6627f5"></a>
<a id="astructgnss__driver__api_html_a1f4c78c928301ede626a9bcb92c5050d"></a>
<a id="astructgnss__driver__api_html_a2a1604472e2a0249a766534b05a11133"></a>
<a id="astructgnss__driver__api_html_a6ab6ea8cb9588ad1a64c1ca6e99be137"></a>
<a id="astructgnss__driver__api_html_a77247b70ca41bea5b29f579e67c878a9"></a>
<a id="astructgnss__driver__api_html_a7b77dbf9b49fec76dd9374b97a025b08"></a>
<a id="astructgnss__driver__api_html_abc82a5f3ede200cd40982581ddf9d02f"></a>
<a id="astructgnss__driver__api_html_abd0d989e810fa0bdffe0f68a10622bbf"></a>
<a id="astructgnss__driver__api_html_ae62ee87f9380b9ea28bf9efa75f04352"></a>
<a id="astructgnss__driver__api_html_af3ad59e6495183f9b45dfbfe0e54fbb6"></a>
<a id="astructgnss__info_html"></a>
<a id="astructgnss__info_html_a54396dd23fd05185bcb1104ee529984e"></a>
<a id="astructgnss__info_html_a5de15dd2a9843c05b8805d4519b49a73"></a>
<a id="astructgnss__info_html_a5f87d86da1ea290fb3951fab1f95459d"></a>
<a id="astructgnss__info_html_a718e95833c4d07ad530669035ca21f8c"></a>
<a id="astructgnss__info_html_a81160955c4b9d3a746280d88a74f07eb"></a>
<a id="astructgnss__satellite_html"></a>
<a id="astructgnss__satellite_html_a03543a7425f27c78e743b0ec180ccea7"></a>
<a id="astructgnss__satellite_html_a27a864422f5207b5d38efbd8b50893a3"></a>
<a id="astructgnss__satellite_html_a3d99c5ad18242a42f95b5de496ca501d"></a>
<a id="astructgnss__satellite_html_a4296fad8444a7ebcd938f7550332ec52"></a>
<a id="astructgnss__satellite_html_a6818083aad878aa8b06d2cbeca53b1da"></a>
<a id="astructgnss__satellite_html_ad9b31c85dd0e162979d384b049142549"></a>
<a id="astructgnss__satellite_html_ae4c596c298ed158a188ea4a5fbd6181c"></a>
<a id="astructgnss__satellites__callback_html"></a>
<a id="astructgnss__satellites__callback_html_a19e64ff2450c00080ae39528f7d07b2b"></a>
<a id="astructgnss__satellites__callback_html_af12fc64ff9c696b5862b5adfef31269b"></a>
<a id="astructgnss__time_html"></a>
<a id="astructgnss__time_html_a1c6730dc08cd3dfb48aee08154f5f2de"></a>
<a id="astructgnss__time_html_a2ab6b41452491ec34966fda0ddbdd9da"></a>
<a id="astructgnss__time_html_a3e8b96861e45cc2a6222961e92ab62f5"></a>
<a id="astructgnss__time_html_a4daa514f38a7b7d88bf49cb5d664b2ac"></a>
<a id="astructgnss__time_html_a5c8a280736741d8d07dacba30d48ed6f"></a>
<a id="astructgnss__time_html_a766744149009588f83cca930ef53ff10"></a>
<a id="astructnavigation__data_html"></a>

```c
/*
 * Copyright (c) 2023 Trackunit Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_GNSS_H_
#define ZEPHYR_INCLUDE_DRIVERS_GNSS_H_


#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/data/navigation.h>
#include <errno.h>

#ifdef __cplusplus
extern "C" {
#endif

enum gnss_start_mode {
        GNSS_HOT_START = 0,
        GNSS_WARM_START = 1,
        GNSS_COLD_START = 2,
};

enum gnss_pps_mode {
        GNSS_PPS_MODE_DISABLED = 0,
        GNSS_PPS_MODE_ENABLED = 1,
        GNSS_PPS_MODE_ENABLED_AFTER_LOCK = 2,
        GNSS_PPS_MODE_ENABLED_WHILE_LOCKED = 3
};



enum gnss_navigation_mode {
        GNSS_NAVIGATION_MODE_ZERO_DYNAMICS = 0,
        GNSS_NAVIGATION_MODE_LOW_DYNAMICS = 1,
        GNSS_NAVIGATION_MODE_BALANCED_DYNAMICS = 2,
        GNSS_NAVIGATION_MODE_HIGH_DYNAMICS = 3
};



enum gnss_system {
        GNSS_SYSTEM_GPS = BIT(0),
        GNSS_SYSTEM_GLONASS = BIT(1),
        GNSS_SYSTEM_GALILEO = BIT(2),
        GNSS_SYSTEM_BEIDOU = BIT(3),
        GNSS_SYSTEM_QZSS = BIT(4),
        GNSS_SYSTEM_IRNSS = BIT(5),
        GNSS_SYSTEM_SBAS = BIT(6),
        GNSS_SYSTEM_IMES = BIT(7),
};

typedef uint32_t gnss_systems_t;



enum gnss_fix_status {
        GNSS_FIX_STATUS_NO_FIX = 0,
        GNSS_FIX_STATUS_GNSS_FIX = 1,
        GNSS_FIX_STATUS_DGNSS_FIX = 2,
        GNSS_FIX_STATUS_ESTIMATED_FIX = 3,
};

enum gnss_fix_quality {
        GNSS_FIX_QUALITY_INVALID = 0,
        GNSS_FIX_QUALITY_GNSS_SPS = 1,
        GNSS_FIX_QUALITY_DGNSS = 2,
        GNSS_FIX_QUALITY_GNSS_PPS = 3,
        GNSS_FIX_QUALITY_RTK = 4,
        GNSS_FIX_QUALITY_FLOAT_RTK = 5,
        GNSS_FIX_QUALITY_ESTIMATED = 6,
};

struct gnss_info {
        uint16_t satellites_cnt;
        uint32_t hdop;
        int32_t geoid_separation;
        enum gnss_fix_status fix_status;
        enum gnss_fix_quality fix_quality;
};

struct gnss_time {
        uint8_t hour;
        uint8_t minute;
        uint16_t millisecond;
        uint8_t month_day;
        uint8_t month;
        uint8_t century_year;
};


typedef int (*gnss_start_t)(const struct device *dev, enum gnss_start_mode mode);

typedef int (*gnss_stop_t)(const struct device *dev);

typedef int (*gnss_set_fix_rate_t)(const struct device *dev, uint32_t fix_interval_ms);

typedef int (*gnss_get_fix_rate_t)(const struct device *dev, uint32_t *fix_interval_ms);

typedef int (*gnss_set_navigation_mode_t)(const struct device *dev,
                                          enum gnss_navigation_mode mode);

typedef int (*gnss_get_navigation_mode_t)(const struct device *dev,
                                          enum gnss_navigation_mode *mode);

typedef int (*gnss_set_enabled_systems_t)(const struct device *dev, gnss_systems_t systems);

typedef int (*gnss_get_enabled_systems_t)(const struct device *dev, gnss_systems_t *systems);

typedef int (*gnss_get_supported_systems_t)(const struct device *dev, gnss_systems_t *systems);

typedef int (*gnss_get_latest_timepulse_t)(const struct device *dev, k_ticks_t *timestamp);

__subsystem struct gnss_driver_api {
        gnss_start_t start;
        gnss_stop_t stop;
        gnss_set_fix_rate_t set_fix_rate;
        gnss_get_fix_rate_t get_fix_rate;
        gnss_set_navigation_mode_t set_navigation_mode;
        gnss_get_navigation_mode_t get_navigation_mode;
        gnss_set_enabled_systems_t set_enabled_systems;
        gnss_get_enabled_systems_t get_enabled_systems;
        gnss_get_supported_systems_t get_supported_systems;
        gnss_get_latest_timepulse_t get_latest_timepulse;
};


struct gnss_data {
        struct navigation_data nav_data;
        struct gnss_info info;
        struct gnss_time utc;
};

typedef void (*gnss_data_callback_t)(const struct device *dev, const struct gnss_data *data);

struct gnss_data_callback {
        const struct device *dev;
        gnss_data_callback_t callback;
};

struct gnss_satellite {
        uint8_t prn;
        uint8_t snr;
        uint8_t elevation;
        uint16_t azimuth;
        enum gnss_system system;
        uint8_t is_tracked : 1;
        uint8_t is_corrected : 1;
};

typedef void (*gnss_satellites_callback_t)(const struct device *dev,
                                           const struct gnss_satellite *satellites,
                                           uint16_t size);

struct gnss_satellites_callback {
        const struct device *dev;
        gnss_satellites_callback_t callback;
};

__syscall int gnss_start(const struct device *dev, enum gnss_start_mode mode);

static inline int z_impl_gnss_start(const struct device *dev, enum gnss_start_mode mode)
{
        const struct gnss_driver_api *api = DEVICE_API_GET(gnss, dev);

        if (api->start == NULL) {
                return -ENOSYS;
        }

        return api->start(dev, mode);
}

__syscall int gnss_stop(const struct device *dev);

static inline int z_impl_gnss_stop(const struct device *dev)
{
        const struct gnss_driver_api *api = DEVICE_API_GET(gnss, dev);

        if (api->stop == NULL) {
                return -ENOSYS;
        }

        return api->stop(dev);
}

__syscall int gnss_set_fix_rate(const struct device *dev, uint32_t fix_interval_ms);

static inline int z_impl_gnss_set_fix_rate(const struct device *dev, uint32_t fix_interval_ms)
{
        const struct gnss_driver_api *api = DEVICE_API_GET(gnss, dev);

        if (api->set_fix_rate == NULL) {
                return -ENOSYS;
        }

        return api->set_fix_rate(dev, fix_interval_ms);
}

__syscall int gnss_get_fix_rate(const struct device *dev, uint32_t *fix_interval_ms);

static inline int z_impl_gnss_get_fix_rate(const struct device *dev, uint32_t *fix_interval_ms)
{
        const struct gnss_driver_api *api = DEVICE_API_GET(gnss, dev);

        if (api->get_fix_rate == NULL) {
                return -ENOSYS;
        }

        return api->get_fix_rate(dev, fix_interval_ms);
}

__syscall int gnss_set_navigation_mode(const struct device *dev,
                                       enum gnss_navigation_mode mode);

static inline int z_impl_gnss_set_navigation_mode(const struct device *dev,
                                                  enum gnss_navigation_mode mode)
{
        const struct gnss_driver_api *api = DEVICE_API_GET(gnss, dev);

        if (api->set_navigation_mode == NULL) {
                return -ENOSYS;
        }

        return api->set_navigation_mode(dev, mode);
}

__syscall int gnss_get_navigation_mode(const struct device *dev,
                                       enum gnss_navigation_mode *mode);

static inline int z_impl_gnss_get_navigation_mode(const struct device *dev,
                                                  enum gnss_navigation_mode *mode)
{
        const struct gnss_driver_api *api = DEVICE_API_GET(gnss, dev);

        if (api->get_navigation_mode == NULL) {
                return -ENOSYS;
        }

        return api->get_navigation_mode(dev, mode);
}

__syscall int gnss_set_enabled_systems(const struct device *dev, gnss_systems_t systems);

static inline int z_impl_gnss_set_enabled_systems(const struct device *dev,
                                                  gnss_systems_t systems)
{
        const struct gnss_driver_api *api = DEVICE_API_GET(gnss, dev);

        if (api->set_enabled_systems == NULL) {
                return -ENOSYS;
        }

        return api->set_enabled_systems(dev, systems);
}

__syscall int gnss_get_enabled_systems(const struct device *dev, gnss_systems_t *systems);

static inline int z_impl_gnss_get_enabled_systems(const struct device *dev,
                                                  gnss_systems_t *systems)
{
        const struct gnss_driver_api *api = DEVICE_API_GET(gnss, dev);

        if (api->get_enabled_systems == NULL) {
                return -ENOSYS;
        }

        return api->get_enabled_systems(dev, systems);
}

__syscall int gnss_get_supported_systems(const struct device *dev, gnss_systems_t *systems);

static inline int z_impl_gnss_get_supported_systems(const struct device *dev,
                                                    gnss_systems_t *systems)
{
        const struct gnss_driver_api *api = DEVICE_API_GET(gnss, dev);

        if (api->get_supported_systems == NULL) {
                return -ENOSYS;
        }

        return api->get_supported_systems(dev, systems);
}

__syscall int gnss_get_latest_timepulse(const struct device *dev, k_ticks_t *timestamp);

static inline int z_impl_gnss_get_latest_timepulse(const struct device *dev,
                                                    k_ticks_t *timestamp)
{
        const struct gnss_driver_api *api = DEVICE_API_GET(gnss, dev);

        if (api->get_latest_timepulse == NULL) {
                return -ENOSYS;
        }

        return api->get_latest_timepulse(dev, timestamp);
}

#if CONFIG_GNSS
#define GNSS_DATA_CALLBACK_DEFINE(_dev, _callback)                                              \
        static const STRUCT_SECTION_ITERABLE(gnss_data_callback,                                \
                                             _gnss_data_callback__##_callback) = {              \
                .dev = _dev,                                                                    \
                .callback = _callback,                                                          \
        }

#define GNSS_DT_DATA_CALLBACK_DEFINE(_node_id, _callback)                                          \
        static const STRUCT_SECTION_ITERABLE(                                                      \
                gnss_data_callback,                                                                \
                CONCAT(_gnss_data_callback_, DT_DEP_ORD(_node_id), _, _callback)) = {              \
                .dev = DEVICE_DT_GET(_node_id),                                                    \
                .callback = _callback,                                                             \
        }
#else
#define GNSS_DATA_CALLBACK_DEFINE(_dev, _callback)
#define GNSS_DT_DATA_CALLBACK_DEFINE(_node_id, _callback)
#endif

#if CONFIG_GNSS_SATELLITES
#define GNSS_SATELLITES_CALLBACK_DEFINE(_dev, _callback)                                        \
        static const STRUCT_SECTION_ITERABLE(gnss_satellites_callback,                          \
                                             _gnss_satellites_callback__##_callback) = {        \
                .dev = _dev,                                                                    \
                .callback = _callback,                                                          \
        }

#define GNSS_DT_SATELLITES_CALLBACK_DEFINE(_node_id, _callback)                                    \
        static const STRUCT_SECTION_ITERABLE(                                                      \
                gnss_satellites_callback,                                                          \
                CONCAT(_gnss_satellites_callback_, DT_DEP_ORD(_node_id), _, _callback)) = {        \
                .dev = DEVICE_DT_GET(_node_id),                                                    \
                .callback = _callback,                                                             \
        }
#else
#define GNSS_SATELLITES_CALLBACK_DEFINE(_dev, _callback)
#define GNSS_DT_SATELLITES_CALLBACK_DEFINE(_node_id, _callback)
#endif


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/gnss.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_GNSS_H_ */
```

## 291.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Trackunit Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 613 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_GNSS_H_`。

## 291.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/data/navigation.h](https://docs.zephyrproject.org/latest/doxygen/html/navigation_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [gnss_start_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga7106633a65ddaa29e19ba9f15b86f0f9)
- [GNSS_HOT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga7106633a65ddaa29e19ba9f15b86f0f9ad0ecfd51dd2e99b5bd7e8abd49143da7)
- [GNSS_WARM_START](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga7106633a65ddaa29e19ba9f15b86f0f9adff054d3999e9f0c2f3c6efc96772cc8)
- [GNSS_COLD_START](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga7106633a65ddaa29e19ba9f15b86f0f9af594a76c0f37da20791b1ce4e2a4f5a3)
- [gnss_pps_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga2b43ac2fec33053a769b7070c4ed3263)
- [GNSS_PPS_MODE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga2b43ac2fec33053a769b7070c4ed3263a5e9af4b08bd41a1aa1bf01c0e290d9fc)
- [GNSS_PPS_MODE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga2b43ac2fec33053a769b7070c4ed3263a9cdbb144191c83f4a7a2cc27268eacfa)
- [GNSS_PPS_MODE_ENABLED_AFTER_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga2b43ac2fec33053a769b7070c4ed3263a2df416ad912a84135eff1e30977b4507)
- [GNSS_PPS_MODE_ENABLED_WHILE_LOCKED](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga2b43ac2fec33053a769b7070c4ed3263afc82bd9ebcfd9d3b6111c9e82fc79ecc)
- [gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)
- [GNSS_NAVIGATION_MODE_ZERO_DYNAMICS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggadb734bb12433276d3014e08a1d21bb18a96f01438a205c0d557eb5ea4f80425ff)
- [GNSS_NAVIGATION_MODE_LOW_DYNAMICS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggadb734bb12433276d3014e08a1d21bb18ac5f4b57f2b0f732f9ae8051cb8ac9453)
- [GNSS_NAVIGATION_MODE_BALANCED_DYNAMICS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggadb734bb12433276d3014e08a1d21bb18ab7fd6073a1e7d28ebf6ae9bc51ded88d)
- [GNSS_NAVIGATION_MODE_HIGH_DYNAMICS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggadb734bb12433276d3014e08a1d21bb18a5f57c5f13e22a94c003f582e8c41a27f)
- [gnss_system](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga928a05b4e820a9fcc8bc2db81f5f8c79)
- [GNSS_SYSTEM_GPS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a84d3fc7ebefad4b20c58335bb7ca3e33)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [GNSS_SYSTEM_GLONASS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a6f5a6de0d8196df55ade83d1f09de7dd)
- [GNSS_SYSTEM_GALILEO](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a1456923f0dd999b26e167fccc2461d5c)
- [GNSS_SYSTEM_BEIDOU](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a25a0162daa071267b63d2c7331a46c55)
- [GNSS_SYSTEM_QZSS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79aac9ccafec388c071468ef16981679dff)
- [GNSS_SYSTEM_IRNSS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a833e14eb77d70b3c5eb2843026b63242)
- [GNSS_SYSTEM_SBAS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a3e759b71b7e531d6c2c3068108e263dd)
- [GNSS_SYSTEM_IMES](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a6a216ab95d09806435af4257b4d189e9)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)
- [gnss_fix_status](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga15536308e2229a45493d06e8b61e63d9)
- [GNSS_FIX_STATUS_NO_FIX](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga15536308e2229a45493d06e8b61e63d9a508bbeea1550d5020e579e6a311fbdbe)
- [GNSS_FIX_STATUS_GNSS_FIX](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga15536308e2229a45493d06e8b61e63d9a8ad1fb7bf9f4d2607cb86f40a901e343)
- [GNSS_FIX_STATUS_DGNSS_FIX](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga15536308e2229a45493d06e8b61e63d9a213553f5fa30cfa99317fcc28d0af1cc)
- [GNSS_FIX_STATUS_ESTIMATED_FIX](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga15536308e2229a45493d06e8b61e63d9a19c4e932246f410ee702122d80fbfbeb)
- [gnss_fix_quality](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gacf5a3464c487ae7609d526c73ccc758a)
- [GNSS_FIX_QUALITY_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa67256fb63beab67ba6e7cbb63916af30)
- [GNSS_FIX_QUALITY_GNSS_SPS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa316ea7e84abca8f04bbf95d3d73cea3f)
- [GNSS_FIX_QUALITY_DGNSS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa65df312eef5cd8b24384440629f534f8)
- [GNSS_FIX_QUALITY_GNSS_PPS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aab4de07a3891e7c89d5bd23fec7add20f)
- [GNSS_FIX_QUALITY_RTK](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa5256b22bb56e93c788d52a641c2a15a6)
- [GNSS_FIX_QUALITY_FLOAT_RTK](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aaedd76bb21200df49fd82243d4a394ac6)
- [GNSS_FIX_QUALITY_ESTIMATED](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa851d88a47c1314eed8bc25e5cc7ba35a)
- [gnss_info](../sensor_navigation_model_reference/P012_gnss_info_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [satellites_cnt](../sensor_navigation_model_reference/P012_gnss_info_结构体.md#a81160955c4b9d3a746280d88a74f07eb)
- [hdop](../sensor_navigation_model_reference/P012_gnss_info_结构体.md#a5de15dd2a9843c05b8805d4519b49a73)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [geoid_separation](../sensor_navigation_model_reference/P012_gnss_info_结构体.md#a5f87d86da1ea290fb3951fab1f95459d)
- [fix_status](../sensor_navigation_model_reference/P012_gnss_info_结构体.md#a718e95833c4d07ad530669035ca21f8c)
- [fix_quality](../sensor_navigation_model_reference/P012_gnss_info_结构体.md#a54396dd23fd05185bcb1104ee529984e)
- [gnss_time](../sensor_navigation_model_reference/P017_gnss_time_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [hour](../sensor_navigation_model_reference/P017_gnss_time_结构体.md#a5c8a280736741d8d07dacba30d48ed6f)
- [minute](../sensor_navigation_model_reference/P017_gnss_time_结构体.md#a3e8b96861e45cc2a6222961e92ab62f5)
- [millisecond](../sensor_navigation_model_reference/P017_gnss_time_结构体.md#a2ab6b41452491ec34966fda0ddbdd9da)
- [month_day](../sensor_navigation_model_reference/P017_gnss_time_结构体.md#a766744149009588f83cca930ef53ff10)
- [month](../sensor_navigation_model_reference/P017_gnss_time_结构体.md#a1c6730dc08cd3dfb48aee08154f5f2de)
- [century_year](../sensor_navigation_model_reference/P017_gnss_time_结构体.md#a4daa514f38a7b7d88bf49cb5d664b2ac)
- [gnss_start_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga8f617e5c8a0938e5eef4d69a3f753303)
- [device](../device_reference/P002_设备对象结构.md)
- [gnss_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga906cecc7e7173893106d6154c7421fc6)
- [gnss_set_fix_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga79e5975d5ec6c0557af4a71004a6da93)
- [gnss_get_fix_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga63a98e08bc7e4b9c70a27de48dc9cd8c)
- [gnss_set_navigation_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gae946fce6ecced7c8fa09e06d75855abe)
- [gnss_get_navigation_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga9705b36019161fde431e78d943eff604)
- [gnss_set_enabled_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga91948cc0567c343bee62b6c70a2f461d)
- [gnss_get_enabled_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gad87bd07c46ea1f79caf9a484c51ec0c9)
- [gnss_get_supported_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gaf52a65dee0d28286ac40e5c8bc86825a)
- [gnss_get_latest_timepulse_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gaa482aa8a996b743aba7e68f36b4780a8)
- [k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)
- [gnss_driver_api](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md)
- [start](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#a6ab6ea8cb9588ad1a64c1ca6e99be137)
- [stop](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#ae62ee87f9380b9ea28bf9efa75f04352)
- [set_fix_rate](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#a0d79083d56a7a35c3a2c858e2c6627f5)
- [get_fix_rate](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#abd0d989e810fa0bdffe0f68a10622bbf)
- [set_navigation_mode](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#a7b77dbf9b49fec76dd9374b97a025b08)
- [get_navigation_mode](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#a77247b70ca41bea5b29f579e67c878a9)
- [set_enabled_systems](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#a1f4c78c928301ede626a9bcb92c5050d)
- [get_enabled_systems](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#abc82a5f3ede200cd40982581ddf9d02f)
- [get_supported_systems](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#af3ad59e6495183f9b45dfbfe0e54fbb6)
- [get_latest_timepulse](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#a2a1604472e2a0249a766534b05a11133)
- [gnss_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md)
- [navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)
- [nav_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md#a2470031921179cb30172441163d80052)
- [info](../sensor_navigation_model_reference/P009_gnss_data_结构体.md#a78155e6d2c981b9121b2ee42c1700988)
- [utc](../sensor_navigation_model_reference/P009_gnss_data_结构体.md#ae6bfc0c6a53901963a1d20bad025fb99)
- [gnss_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga025c965369275ad8e5ab5ad44c14a23b)
- [gnss_data_callback](../sensor_navigation_model_reference/P010_gnss_data_callback_结构体.md)
- [dev](../sensor_navigation_model_reference/P010_gnss_data_callback_结构体.md#afdf273ceed2d2038b6415840f9ecdd7b)
- [callback](../sensor_navigation_model_reference/P010_gnss_data_callback_结构体.md#a07e9c7fd6192fd5b58ff37aabdbff11e)
- [gnss_satellite](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md)
- [prn](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#a03543a7425f27c78e743b0ec180ccea7)
- [snr](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#a6818083aad878aa8b06d2cbeca53b1da)
- [elevation](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#a3d99c5ad18242a42f95b5de496ca501d)
- [azimuth](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#a27a864422f5207b5d38efbd8b50893a3)
- [system](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#ad9b31c85dd0e162979d384b049142549)
- [is_tracked](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#ae4c596c298ed158a188ea4a5fbd6181c)
- [is_corrected](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#a4296fad8444a7ebcd938f7550332ec52)
- [gnss_satellites_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga80cf700468d1c942cfa064368e212e6f)
- [gnss_satellites_callback](../sensor_navigation_model_reference/P016_gnss_satellites_callback_结构体.md)
- [dev](../sensor_navigation_model_reference/P016_gnss_satellites_callback_结构体.md#a19e64ff2450c00080ae39528f7d07b2b)
- [callback](../sensor_navigation_model_reference/P016_gnss_satellites_callback_结构体.md#af12fc64ff9c696b5862b5adfef31269b)
- [gnss_start](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga6bdabc1e89f5c7b10c1099fa74e6c6ca)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [gnss_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga43f285927c94079e3b72e81303cff520)
- [gnss_set_fix_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga16e8326737f114bd6017983812c7f28d)
- [gnss_get_fix_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga8e625fb3f8758eab78c115d12bef6a72)
- [gnss_set_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga9d0347640e68d5702b1cb43ddf8380df)
- [gnss_get_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gae5614f8125dad02a3ebd30400b575e6d)
- [gnss_set_enabled_systems](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga818e42c7a979623679eba26887662823)
- [gnss_get_enabled_systems](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga155126e113195c08158ef49e2a6b4f6a)
- [gnss_get_supported_systems](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga598609846ff196ff300fcad8237b2d51)
- [gnss_get_latest_timepulse](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga8eb37446d71c020e0517a406ea240fc2)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [navigation.h](https://docs.zephyrproject.org/latest/doxygen/html/navigation_8h.html)
- [gnss_data_callback::callback](../sensor_navigation_model_reference/P010_gnss_data_callback_结构体.md#a07e9c7fd6192fd5b58ff37aabdbff11e)
- [gnss_data_callback::dev](../sensor_navigation_model_reference/P010_gnss_data_callback_结构体.md#afdf273ceed2d2038b6415840f9ecdd7b)
- [gnss_data::nav_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md#a2470031921179cb30172441163d80052)
- [gnss_data::info](../sensor_navigation_model_reference/P009_gnss_data_结构体.md#a78155e6d2c981b9121b2ee42c1700988)
- [gnss_data::utc](../sensor_navigation_model_reference/P009_gnss_data_结构体.md#ae6bfc0c6a53901963a1d20bad025fb99)
- [gnss_driver_api::set_fix_rate](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#a0d79083d56a7a35c3a2c858e2c6627f5)
- [gnss_driver_api::set_enabled_systems](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#a1f4c78c928301ede626a9bcb92c5050d)
- [gnss_driver_api::get_latest_timepulse](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#a2a1604472e2a0249a766534b05a11133)
- [gnss_driver_api::start](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#a6ab6ea8cb9588ad1a64c1ca6e99be137)
- [gnss_driver_api::get_navigation_mode](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#a77247b70ca41bea5b29f579e67c878a9)
- [gnss_driver_api::set_navigation_mode](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#a7b77dbf9b49fec76dd9374b97a025b08)
- [gnss_driver_api::get_enabled_systems](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#abc82a5f3ede200cd40982581ddf9d02f)
- [gnss_driver_api::get_fix_rate](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#abd0d989e810fa0bdffe0f68a10622bbf)
- [gnss_driver_api::stop](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#ae62ee87f9380b9ea28bf9efa75f04352)
- [gnss_driver_api::get_supported_systems](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md#af3ad59e6495183f9b45dfbfe0e54fbb6)
- [gnss_info::fix_quality](../sensor_navigation_model_reference/P012_gnss_info_结构体.md#a54396dd23fd05185bcb1104ee529984e)
- [gnss_info::hdop](../sensor_navigation_model_reference/P012_gnss_info_结构体.md#a5de15dd2a9843c05b8805d4519b49a73)
- [gnss_info::geoid_separation](../sensor_navigation_model_reference/P012_gnss_info_结构体.md#a5f87d86da1ea290fb3951fab1f95459d)
- [gnss_info::fix_status](../sensor_navigation_model_reference/P012_gnss_info_结构体.md#a718e95833c4d07ad530669035ca21f8c)
- [gnss_info::satellites_cnt](../sensor_navigation_model_reference/P012_gnss_info_结构体.md#a81160955c4b9d3a746280d88a74f07eb)
- [gnss_satellite::prn](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#a03543a7425f27c78e743b0ec180ccea7)
- [gnss_satellite::azimuth](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#a27a864422f5207b5d38efbd8b50893a3)
- [gnss_satellite::elevation](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#a3d99c5ad18242a42f95b5de496ca501d)
- [gnss_satellite::is_corrected](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#a4296fad8444a7ebcd938f7550332ec52)
- [gnss_satellite::snr](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#a6818083aad878aa8b06d2cbeca53b1da)
- [gnss_satellite::system](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#ad9b31c85dd0e162979d384b049142549)
- [gnss_satellite::is_tracked](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md#ae4c596c298ed158a188ea4a5fbd6181c)
- [gnss_satellites_callback::dev](../sensor_navigation_model_reference/P016_gnss_satellites_callback_结构体.md#a19e64ff2450c00080ae39528f7d07b2b)
- [gnss_satellites_callback::callback](../sensor_navigation_model_reference/P016_gnss_satellites_callback_结构体.md#af12fc64ff9c696b5862b5adfef31269b)
- [gnss_time::month](../sensor_navigation_model_reference/P017_gnss_time_结构体.md#a1c6730dc08cd3dfb48aee08154f5f2de)
- [gnss_time::millisecond](../sensor_navigation_model_reference/P017_gnss_time_结构体.md#a2ab6b41452491ec34966fda0ddbdd9da)
- [gnss_time::minute](../sensor_navigation_model_reference/P017_gnss_time_结构体.md#a3e8b96861e45cc2a6222961e92ab62f5)
- [gnss_time::century_year](../sensor_navigation_model_reference/P017_gnss_time_结构体.md#a4daa514f38a7b7d88bf49cb5d664b2ac)
- [gnss_time::hour](../sensor_navigation_model_reference/P017_gnss_time_结构体.md#a5c8a280736741d8d07dacba30d48ed6f)
- [gnss_time::month_day](../sensor_navigation_model_reference/P017_gnss_time_结构体.md#a766744149009588f83cca930ef53ff10)

---

[上一章](P290_gicv3_its.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P292_gnss_emul.h_源码浏览.md)
