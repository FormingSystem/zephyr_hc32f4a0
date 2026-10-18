---
id: learning.zephyr-docs.api-source-supplement-reference.page-102
title: main.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/main_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第102章\_main.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/main_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/main_8h.html)。

## 102.1\_原始可见代码（Source Code）

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
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
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
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="foldopen00069"></a>
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
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00136"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00580"></a>
<a id="l00587"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00592"></a>
<a id="l00594"></a>
<a id="l00596"></a>
<a id="l00598"></a>
<a id="foldopen00600"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="foldopen00701"></a>
<a id="l00701"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="foldopen00746"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="foldopen00752"></a>
<a id="l00752"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="foldopen00798"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00817"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00832"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00887"></a>
<a id="l00888"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="agroup__bt__mesh__prov_html_ga0307e62001ba7fa303ed311ebc47f116"></a>
<a id="agroup__bt__mesh__prov_html_ga0bfae4ebda53052cfa027c3a7ae51ec8"></a>
<a id="agroup__bt__mesh__prov_html_ga2592abf429b40ef9242bce26f5bd085e"></a>
<a id="agroup__bt__mesh__prov_html_ga4ed6e078c1c0f197758c8dbb23db30f6"></a>
<a id="agroup__bt__mesh__prov_html_ga5512b81ef7eeb45b0a12ef62234c8795"></a>
<a id="agroup__bt__mesh__prov_html_ga60666e0d7629caf36026974621bae664"></a>
<a id="agroup__bt__mesh__prov_html_ga6c8dc1b09d4cde8738be83c992b860a9"></a>
<a id="agroup__bt__mesh__prov_html_ga7b6024dc32f6ec7f26cbf91545911084"></a>
<a id="agroup__bt__mesh__prov_html_ga80be35bf7287e62cb47d8fba99d648a9"></a>
<a id="agroup__bt__mesh__prov_html_ga9fc414e4e15d6b3ab0dae5483ed62982"></a>
<a id="agroup__bt__mesh__prov_html_gaa02583390f635ac251d22ed9ff953974"></a>
<a id="agroup__bt__mesh__prov_html_gaa157eb0fee30c28092a11993872b8fdd"></a>
<a id="agroup__bt__mesh__prov_html_gabab41ebdcae2eaa109e03cb2d8fa78c6"></a>
<a id="agroup__bt__mesh__prov_html_gabc9d68157928c2b343eddd08ef314d27"></a>
<a id="agroup__bt__mesh__prov_html_gac7e084e7d12a93377d49b1c3d6313399"></a>
<a id="agroup__bt__mesh__prov_html_gad66ccc725a1cfdf2b79076f22f853f84"></a>
<a id="agroup__bt__mesh__prov_html_gae33b5b6e9650b49d46494b4a81b18674"></a>
<a id="agroup__bt__mesh__prov_html_gaf71f3dbdef6b8c085e9a4f068e1f60c5"></a>
<a id="agroup__bt__mesh__prov_html_gaf93f7b49dada5c3f7accc54663648e48"></a>
<a id="agroup__bt__mesh__prov_html_gga5512b81ef7eeb45b0a12ef62234c8795a3586ffa3e36247e0d90b83c3f075e591"></a>
<a id="agroup__bt__mesh__prov_html_gga5512b81ef7eeb45b0a12ef62234c8795aa07d600f2afe278729bb4e35d41bf29b"></a>
<a id="agroup__bt__mesh__prov_html_gga5512b81ef7eeb45b0a12ef62234c8795ab45021af96db0465f5edc6e0ea7b6079"></a>
<a id="agroup__bt__mesh__prov_html_gga5512b81ef7eeb45b0a12ef62234c8795ac38333011b4f76b036a04e41f1f71e83"></a>
<a id="agroup__bt__mesh__prov_html_gga5512b81ef7eeb45b0a12ef62234c8795ad009060fd1f501c8362a63e6c020b113"></a>
<a id="agroup__bt__mesh__prov_html_gga5512b81ef7eeb45b0a12ef62234c8795ae50031a39d19181df17ee6de1a12272c"></a>
<a id="agroup__bt__mesh__prov_html_ggaa157eb0fee30c28092a11993872b8fdda27c9c1278acc887214a4a30294bf52d8"></a>
<a id="agroup__bt__mesh__prov_html_ggaa157eb0fee30c28092a11993872b8fdda4222d03b09ba43b6ea772738b8987501"></a>
<a id="agroup__bt__mesh__prov_html_ggaa157eb0fee30c28092a11993872b8fdda5142f018a5426a047688c6507b3af4f8"></a>
<a id="agroup__bt__mesh__prov_html_ggabe5586cff0697e137730a52728978681a292bf2e4d29f0bd0d746bbb871f2ee5a"></a>
<a id="agroup__bt__mesh__prov_html_ggabe5586cff0697e137730a52728978681affa8679d8be1a12714a34ed09c3b05dd"></a>
<a id="agroup__bt__mesh__prov_html_ggabec90bd95082b9dc8fa3ca27a9d7bc66a30e46fe23e508029b570e1f107b38d40"></a>
<a id="agroup__bt__mesh__prov_html_ggabec90bd95082b9dc8fa3ca27a9d7bc66a61f859a15fabc8d9fd278dabe5a86a37"></a>
<a id="agroup__bt__mesh__prov_html_ggaf71f3dbdef6b8c085e9a4f068e1f60c5a5d6bd8e6110c8f53245840aead4201c2"></a>
<a id="agroup__bt__mesh__prov_html_ggaf71f3dbdef6b8c085e9a4f068e1f60c5aa0de3817e863d1f06888100de24fb4b0"></a>
<a id="agroup__bt__mesh__prov_html_ggaf71f3dbdef6b8c085e9a4f068e1f60c5ac721b070cad51f1cd9aa1f0b60e59056"></a>
<a id="agroup__bt__mesh__prov_html_ggaf71f3dbdef6b8c085e9a4f068e1f60c5ad6f22211d09614181cb5b0f42300a9ee"></a>
<a id="agroup__bt__mesh__prov_html_ggaf71f3dbdef6b8c085e9a4f068e1f60c5ae4902ce51142fa49d2d5e97165d6f51c"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48a00eb3ba6b7940b02d2fe3892100f497e"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48a137946e3d53b996b77bebeda5fa930cb"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48a34d005022a75446a386006f7690a473e"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48a487ffb56c8c15a37b69fa1699fff301a"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48a4a8a7e4ab87cf360abdb167076349072"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48a8553379d579a418a6453669323b18088"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48aa10724108397ab8d48a3aac2817992f2"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48aa73dd9517eec86e51b48d256fc9660da"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48abe8fd10b49a7bb6c7499eb73ae3876d3"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48ac5d40459453afebc841f32e1f0b33fbc"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48ad861e8de3c1fbc1658a6d0fba38785dd"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48ad9b4089a740d47950c02b4389d29df56"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48adbbc3c3829bb7caf1a4a5fd2066f3b4a"></a>
<a id="agroup__bt__mesh__prov_html_ggaf93f7b49dada5c3f7accc54663648e48ae855a27a18bfb6ea03f0ff6165e4a291"></a>
<a id="agroup__bt__mesh_html_ga20fe74e33e6a35c452cd076c78aa4f05"></a>
<a id="agroup__bt__mesh_html_ga28b9b1d7d732e300be8d4bbffdbad391"></a>
<a id="agroup__bt__mesh_html_ga3fd66605950a55e299ca3a7cc697d453"></a>
<a id="agroup__bt__mesh_html_ga3fdc601bd036477f6bdf212667c6b0c9"></a>
<a id="agroup__bt__mesh_html_ga521def6f74467a9bd3f2757c6aabd405"></a>
<a id="agroup__bt__mesh_html_ga62f9a72c4e9dc5e4f3f42bd4df4fe452"></a>
<a id="agroup__bt__mesh_html_ga69fc65f4e07e6007388473f139e5d8d8"></a>
<a id="agroup__bt__mesh_html_ga6c209dbad6881f1e9634d9b7d42f2c34"></a>
<a id="agroup__bt__mesh_html_ga7964f5b1abb7b12728e4ec224c95c849"></a>
<a id="agroup__bt__mesh_html_gaa9114ce8941e641dbb23828d7c0451fd"></a>
<a id="agroup__bt__mesh_html_gacdf00423b03057fdf3a4207ee579eb74"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="akernel_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__comp_html"></a>
<a id="astructbt__mesh__dev__capabilities_html"></a>
<a id="astructbt__mesh__dev__capabilities_html_a359caeaf64f45783b0c576ef8ef14975"></a>
<a id="astructbt__mesh__dev__capabilities_html_a59c959cbd8b1a2aa4e548e7f990cf1f4"></a>
<a id="astructbt__mesh__dev__capabilities_html_a6132c85094980f839cf9dca57d7969ea"></a>
<a id="astructbt__mesh__dev__capabilities_html_a744703091988432baa14a84347309bcf"></a>
<a id="astructbt__mesh__dev__capabilities_html_a762786d98c070d0ae79e09f22bad4b33"></a>
<a id="astructbt__mesh__dev__capabilities_html_a7f549f5b3923c0b4249e1b21368ee857"></a>
<a id="astructbt__mesh__dev__capabilities_html_ac9097c4d634683120509f4c1ac732928"></a>
<a id="astructbt__mesh__dev__capabilities_html_acfef4ecf5ca9324ddc584b9cb910bfe0"></a>
<a id="astructbt__mesh__friend__cb_html"></a>
<a id="astructbt__mesh__friend__cb_html_a1c0d570eb1b857c65b3b5b4ce31999d6"></a>
<a id="astructbt__mesh__friend__cb_html_a7b904967d89173f82ac26216e3849d23"></a>
<a id="astructbt__mesh__friend__cb_html_a824ed814a46a3954d2c6f669c8900156"></a>
<a id="astructbt__mesh__lpn__cb_html"></a>
<a id="astructbt__mesh__lpn__cb_html_a74b8b398b383518af069266cf3b0be91"></a>
<a id="astructbt__mesh__lpn__cb_html_a9805ad8578faec5b371d6f39178332ef"></a>
<a id="astructbt__mesh__lpn__cb_html_af2e2f5043503c62926f96a5fcb48890c"></a>
<a id="astructbt__mesh__prov_html"></a>
<a id="astructbt__mesh__prov_html_a0183cef77dda3978ef8a40ce7aad043a"></a>
<a id="astructbt__mesh__prov_html_a1152d77c4c4d9271bbd72514d94052f2"></a>
<a id="astructbt__mesh__prov_html_a1261ba69e785f005d5834ac49da00778"></a>
<a id="astructbt__mesh__prov_html_a1ab714e9be35242e02099884c3af45f5"></a>
<a id="astructbt__mesh__prov_html_a2717ddf38465b95452724078f780f9e5"></a>
<a id="astructbt__mesh__prov_html_a28284efee6478637446702d7839f6b8c"></a>
<a id="astructbt__mesh__prov_html_a31eff9c903ac721bbca7ab586dda9e80"></a>
<a id="astructbt__mesh__prov_html_a44efea3e9221c182cbcacce8219ef6b7"></a>
<a id="astructbt__mesh__prov_html_a4c51aa8e5887b3364d9480c92da3a0a0"></a>
<a id="astructbt__mesh__prov_html_a6a11cc0d36ca2f4c5aee67a023c295a2"></a>
<a id="astructbt__mesh__prov_html_a6ed61556291f7f9d9a32062d588b8f2a"></a>
<a id="astructbt__mesh__prov_html_a7eddf1f088264f8b6e3fb86dce4c108e"></a>
<a id="astructbt__mesh__prov_html_a8142a3b8120b1686f68513caeac09497"></a>
<a id="astructbt__mesh__prov_html_a8b88959c5eef7f47591468e9c9768b7c"></a>
<a id="astructbt__mesh__prov_html_a97394dded5fd55b553364a566a2441e8"></a>
<a id="astructbt__mesh__prov_html_a97cf41cf857479c8eefee640f7b66788"></a>
<a id="astructbt__mesh__prov_html_aaa49675e358ea4cba7552b3e855befba"></a>
<a id="astructbt__mesh__prov_html_ab9044f6dbf9780b3237f18270b2c8582"></a>
<a id="astructbt__mesh__prov_html_ac131476cdeb002f0027407b4cf80c2b5"></a>
<a id="astructbt__mesh__prov_html_ad55abc2b1632455bb23fbd8b03df85ea"></a>
<a id="astructbt__mesh__prov_html_ae7aec4a89f4260a99696bb46207c4338"></a>
<a id="astructbt__mesh__prov_html_ae87570de25c89e74bece2516ff957779"></a>
<a id="astructbt__mesh__prov_html_af928a9419f684bcbda0563dda2c34d76"></a>
<a id="astructbt__mesh__prov_html_afbc65bb8be99f7dc37ecc911f4ac2151"></a>
<a id="astructbt__mesh__rpr__cli_html"></a>
<a id="astructbt__mesh__rpr__node_html"></a>
<a id="astructbt__mesh__rpr__node_html_a10ec7b9c480513e742566c6c3b9c4973"></a>
<a id="astructbt__mesh__rpr__node_html_a2197a70aa97209a60136a09da1f513b2"></a>
<a id="astructuuid_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_MAIN_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_MAIN_H_

#include <stdbool.h>
#include <stdint.h>

#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>


#ifdef __cplusplus
extern "C" {
#endif

enum {
        BT_MESH_PROV_AUTH_CMAC_AES128_AES_CCM,
        BT_MESH_PROV_AUTH_HMAC_SHA256_AES_CCM,
};

enum {
        BT_MESH_STATIC_OOB_AVAILABLE = BIT(0),
        BT_MESH_OOB_AUTH_REQUIRED    = BIT(1)
};

typedef enum {
        BT_MESH_NO_OUTPUT       = 0,
        BT_MESH_BLINK           = BIT(0),
        BT_MESH_BEEP            = BIT(1),
        BT_MESH_VIBRATE         = BIT(2),
        BT_MESH_DISPLAY_NUMBER  = BIT(3),
        BT_MESH_DISPLAY_STRING  = BIT(4),
} bt_mesh_output_action_t;

typedef enum {
        BT_MESH_NO_INPUT      = 0,
        BT_MESH_PUSH          = BIT(0),
        BT_MESH_TWIST         = BIT(1),
        BT_MESH_ENTER_NUMBER  = BIT(2),
        BT_MESH_ENTER_STRING  = BIT(3),
} bt_mesh_input_action_t;

typedef enum {
        BT_MESH_PROV_ADV    = BIT(0),
        BT_MESH_PROV_GATT   = BIT(1),
        BT_MESH_PROV_REMOTE = BIT(2),
} bt_mesh_prov_bearer_t;

typedef enum {
        BT_MESH_PROV_OOB_OTHER       = BIT(0),
        BT_MESH_PROV_OOB_URI         = BIT(1),
        BT_MESH_PROV_OOB_2D_CODE     = BIT(2),
        BT_MESH_PROV_OOB_BAR_CODE    = BIT(3),
        BT_MESH_PROV_OOB_NFC         = BIT(4),
        BT_MESH_PROV_OOB_NUMBER      = BIT(5),
        BT_MESH_PROV_OOB_STRING      = BIT(6),
        BT_MESH_PROV_OOB_CERTIFICATE = BIT(7),
        BT_MESH_PROV_OOB_RECORDS     = BIT(8),
        /* 9 - 10 are reserved */
        BT_MESH_PROV_OOB_ON_BOX      = BIT(11),
        BT_MESH_PROV_OOB_IN_BOX      = BIT(12),
        BT_MESH_PROV_OOB_ON_PAPER    = BIT(13),
        BT_MESH_PROV_OOB_IN_MANUAL   = BIT(14),
        BT_MESH_PROV_OOB_ON_DEV      = BIT(15),
} bt_mesh_prov_oob_info_t;

struct bt_mesh_dev_capabilities {
        uint8_t elem_count;

        uint16_t algorithms;

        uint8_t pub_key_type;

        uint8_t oob_type;

        bt_mesh_output_action_t output_actions;

        bt_mesh_input_action_t input_actions;

        uint8_t output_size;

        uint8_t input_size;
};

struct bt_mesh_prov {
        const uint8_t *uuid;

        const char *uri;

        bt_mesh_prov_oob_info_t oob_info;

        const uint8_t *public_key_be;
        const uint8_t *private_key_be;

        const uint8_t *static_val;
        uint8_t        static_val_len;

        uint8_t        output_size;
        uint16_t       output_actions;

        uint8_t        input_size;
        uint16_t       input_actions;

        void         (*capabilities)(const struct bt_mesh_dev_capabilities *cap);

#if defined CONFIG_BT_MESH_PROV_OOB_API_LEGACY
        int         (*output_number)(bt_mesh_output_action_t act, uint32_t num) __deprecated;
#else
        int         (*output_numeric)(bt_mesh_output_action_t act, uint8_t *numeric, size_t size);
#endif

        int         (*output_string)(const char *str);

        int         (*input)(bt_mesh_input_action_t act, uint8_t size);

        void        (*input_complete)(void);

        void        (*unprovisioned_beacon)(uint8_t uuid[16],
                                            bt_mesh_prov_oob_info_t oob_info,
                                            uint32_t *uri_hash);

        void        (*unprovisioned_beacon_gatt)(uint8_t uuid[16],
                                                 bt_mesh_prov_oob_info_t oob_info);

        void        (*link_open)(bt_mesh_prov_bearer_t bearer);

        void        (*link_close)(bt_mesh_prov_bearer_t bearer);

        void        (*complete)(uint16_t net_idx, uint16_t addr);

        void        (*reprovisioned)(uint16_t addr);

        void        (*node_added)(uint16_t net_idx, uint8_t uuid[16], uint16_t addr,
                                  uint8_t num_elem);

        void        (*reset)(void);
};

struct bt_mesh_rpr_cli;
struct bt_mesh_rpr_node;

int bt_mesh_input_string(const char *str);

#if defined CONFIG_BT_MESH_PROV_OOB_API_LEGACY
__deprecated int bt_mesh_input_number(uint32_t num);
#endif

int bt_mesh_input_numeric(uint8_t *numeric, size_t size);

int bt_mesh_prov_remote_pub_key_set(const uint8_t public_key[64]);

int bt_mesh_auth_method_set_input(bt_mesh_input_action_t action, uint8_t size);

int bt_mesh_auth_method_set_output(bt_mesh_output_action_t action, uint8_t size);

int bt_mesh_auth_method_set_static(const uint8_t *static_val, uint8_t size);

int bt_mesh_auth_method_set_none(void);

int bt_mesh_prov_enable(bt_mesh_prov_bearer_t bearers);

int bt_mesh_prov_disable(bt_mesh_prov_bearer_t bearers);

int bt_mesh_provision(const uint8_t net_key[16], uint16_t net_idx,
                      uint8_t flags, uint32_t iv_index, uint16_t addr,
                      const uint8_t dev_key[16]);

int bt_mesh_provision_adv(const uint8_t uuid[16], uint16_t net_idx, uint16_t addr,
                          uint8_t attention_duration);

int bt_mesh_provision_gatt(const uint8_t uuid[16], uint16_t net_idx, uint16_t addr,
                           uint8_t attention_duration);

int bt_mesh_provision_remote(struct bt_mesh_rpr_cli *cli,
                             const struct bt_mesh_rpr_node *srv,
                             const uint8_t uuid[16], uint16_t net_idx,
                             uint16_t addr);

int bt_mesh_reprovision_remote(struct bt_mesh_rpr_cli *cli,
                               struct bt_mesh_rpr_node *srv,
                               uint16_t addr, bool comp_change);

bool bt_mesh_is_provisioned(void);



#define BT_MESH_NET_PRIMARY                 0x000

#define BT_MESH_FEAT_RELAY                  BIT(0)
#define BT_MESH_FEAT_PROXY                  BIT(1)
#define BT_MESH_FEAT_FRIEND                 BIT(2)
#define BT_MESH_FEAT_LOW_POWER              BIT(3)
#define BT_MESH_FEAT_SUPPORTED              (BT_MESH_FEAT_RELAY |   \
                                             BT_MESH_FEAT_PROXY |   \
                                             BT_MESH_FEAT_FRIEND |  \
                                             BT_MESH_FEAT_LOW_POWER)

int bt_mesh_init(const struct bt_mesh_prov *prov,
                 const struct bt_mesh_comp *comp);

void bt_mesh_reset(void);

int bt_mesh_suspend(void);

int bt_mesh_resume(void);

void bt_mesh_iv_update_test(bool enable);

bool bt_mesh_iv_update(void);

int bt_mesh_lpn_set(bool enable);

int bt_mesh_lpn_poll(void);

struct bt_mesh_lpn_cb {
        void (*established)(uint16_t net_idx, uint16_t friend_addr,
                            uint8_t queue_size, uint8_t recv_window);

        void (*terminated)(uint16_t net_idx, uint16_t friend_addr);

        void (*polled)(uint16_t net_idx, uint16_t friend_addr, bool retry);
};

#define BT_MESH_LPN_CB_DEFINE(_name)                                  \
        static const STRUCT_SECTION_ITERABLE(bt_mesh_lpn_cb,          \
                                             _CONCAT(bt_mesh_lpn_cb_, \
                                                     _name))

struct bt_mesh_friend_cb {
        void (*established)(uint16_t net_idx, uint16_t lpn_addr,
                            uint8_t recv_delay, uint32_t polltimeout);

        void (*terminated)(uint16_t net_idx, uint16_t lpn_addr);

        void (*polled)(uint16_t net_idx, uint16_t lpn_addr);
};

#define BT_MESH_FRIEND_CB_DEFINE(_name)                                  \
        static const STRUCT_SECTION_ITERABLE(bt_mesh_friend_cb,          \
                                             _CONCAT(bt_mesh_friend_cb_, \
                                                     _name))
#if defined(CONFIG_BT_TESTING)
struct bt_mesh_snb {
        uint8_t flags;

        uint64_t net_id;

        uint32_t iv_idx;

        uint64_t auth_val;
};

struct bt_mesh_prb {
        uint8_t random[13];

        uint8_t flags;

        uint32_t iv_idx;

        uint64_t auth_tag;
};

struct bt_mesh_beacon_cb {
        void (*snb_received)(const struct bt_mesh_snb *snb);

        void (*priv_received)(const struct bt_mesh_prb *prb);
};

#define BT_MESH_BEACON_CB_DEFINE(_name)                                  \
        static const STRUCT_SECTION_ITERABLE(bt_mesh_beacon_cb,          \
                                             _CONCAT(bt_mesh_beacon_cb_, \
                                                     _name))
#endif

int bt_mesh_friend_terminate(uint16_t lpn_addr);

void bt_mesh_rpl_pending_store(uint16_t addr);

const uint8_t *bt_mesh_va_uuid_get(uint16_t addr, const uint8_t *uuid, uint16_t *retaddr);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_MAIN_H_ */
```

## 102.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 79 行

9–10 保留。

### 注释 3：原第 914 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_MAIN_H_`。

## 102.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/main_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [BT_MESH_PROV_AUTH_CMAC_AES128_AES_CCM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggabe5586cff0697e137730a52728978681affa8679d8be1a12714a34ed09c3b05dd)
- [BT_MESH_PROV_AUTH_HMAC_SHA256_AES_CCM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggabe5586cff0697e137730a52728978681a292bf2e4d29f0bd0d746bbb871f2ee5a)
- [BT_MESH_STATIC_OOB_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggabec90bd95082b9dc8fa3ca27a9d7bc66a30e46fe23e508029b570e1f107b38d40)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_MESH_OOB_AUTH_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggabec90bd95082b9dc8fa3ca27a9d7bc66a61f859a15fabc8d9fd278dabe5a86a37)
- [BT_MESH_NO_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795ad009060fd1f501c8362a63e6c020b113)
- [BT_MESH_BLINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795ac38333011b4f76b036a04e41f1f71e83)
- [BT_MESH_BEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795ae50031a39d19181df17ee6de1a12272c)
- [BT_MESH_VIBRATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795ab45021af96db0465f5edc6e0ea7b6079)
- [BT_MESH_DISPLAY_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795a3586ffa3e36247e0d90b83c3f075e591)
- [BT_MESH_DISPLAY_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gga5512b81ef7eeb45b0a12ef62234c8795aa07d600f2afe278729bb4e35d41bf29b)
- [bt_mesh_output_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga5512b81ef7eeb45b0a12ef62234c8795)
- [BT_MESH_NO_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ac721b070cad51f1cd9aa1f0b60e59056)
- [BT_MESH_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ae4902ce51142fa49d2d5e97165d6f51c)
- [BT_MESH_TWIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ad6f22211d09614181cb5b0f42300a9ee)
- [BT_MESH_ENTER_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5aa0de3817e863d1f06888100de24fb4b0)
- [BT_MESH_ENTER_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf71f3dbdef6b8c085e9a4f068e1f60c5a5d6bd8e6110c8f53245840aead4201c2)
- [bt_mesh_input_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf71f3dbdef6b8c085e9a4f068e1f60c5)
- [BT_MESH_PROV_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaa157eb0fee30c28092a11993872b8fdda5142f018a5426a047688c6507b3af4f8)
- [BT_MESH_PROV_GATT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaa157eb0fee30c28092a11993872b8fdda27c9c1278acc887214a4a30294bf52d8)
- [BT_MESH_PROV_REMOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaa157eb0fee30c28092a11993872b8fdda4222d03b09ba43b6ea772738b8987501)
- [bt_mesh_prov_bearer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaa157eb0fee30c28092a11993872b8fdd)
- [BT_MESH_PROV_OOB_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a487ffb56c8c15a37b69fa1699fff301a)
- [BT_MESH_PROV_OOB_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48ad861e8de3c1fbc1658a6d0fba38785dd)
- [BT_MESH_PROV_OOB_2D_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a34d005022a75446a386006f7690a473e)
- [BT_MESH_PROV_OOB_BAR_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48abe8fd10b49a7bb6c7499eb73ae3876d3)
- [BT_MESH_PROV_OOB_NFC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48ad9b4089a740d47950c02b4389d29df56)
- [BT_MESH_PROV_OOB_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48ac5d40459453afebc841f32e1f0b33fbc)
- [BT_MESH_PROV_OOB_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a8553379d579a418a6453669323b18088)
- [BT_MESH_PROV_OOB_CERTIFICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a00eb3ba6b7940b02d2fe3892100f497e)
- [BT_MESH_PROV_OOB_RECORDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48aa10724108397ab8d48a3aac2817992f2)
- [BT_MESH_PROV_OOB_ON_BOX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48adbbc3c3829bb7caf1a4a5fd2066f3b4a)
- [BT_MESH_PROV_OOB_IN_BOX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48ae855a27a18bfb6ea03f0ff6165e4a291)
- [BT_MESH_PROV_OOB_ON_PAPER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a137946e3d53b996b77bebeda5fa930cb)
- [BT_MESH_PROV_OOB_IN_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48a4a8a7e4ab87cf360abdb167076349072)
- [BT_MESH_PROV_OOB_ON_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaf93f7b49dada5c3f7accc54663648e48aa73dd9517eec86e51b48d256fc9660da)
- [bt_mesh_prov_oob_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf93f7b49dada5c3f7accc54663648e48)
- [bt_mesh_dev_capabilities](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [elem_count](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#acfef4ecf5ca9324ddc584b9cb910bfe0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [algorithms](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#a762786d98c070d0ae79e09f22bad4b33)
- [pub_key_type](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#a7f549f5b3923c0b4249e1b21368ee857)
- [oob_type](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#a744703091988432baa14a84347309bcf)
- [output_actions](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#a359caeaf64f45783b0c576ef8ef14975)
- [input_actions](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#a6132c85094980f839cf9dca57d7969ea)
- [output_size](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#a59c959cbd8b1a2aa4e548e7f990cf1f4)
- [input_size](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#ac9097c4d634683120509f4c1ac732928)
- [bt_mesh_prov](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md)
- [uuid](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a1152d77c4c4d9271bbd72514d94052f2)
- [uri](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a6a11cc0d36ca2f4c5aee67a023c295a2)
- [oob_info](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a6ed61556291f7f9d9a32062d588b8f2a)
- [public_key_be](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a1261ba69e785f005d5834ac49da00778)
- [private_key_be](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a1ab714e9be35242e02099884c3af45f5)
- [static_val](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a97cf41cf857479c8eefee640f7b66788)
- [static_val_len](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a97394dded5fd55b553364a566a2441e8)
- [output_size](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a4c51aa8e5887b3364d9480c92da3a0a0)
- [output_actions](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a8b88959c5eef7f47591468e9c9768b7c)
- [input_size](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#ab9044f6dbf9780b3237f18270b2c8582)
- [input_actions](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#af928a9419f684bcbda0563dda2c34d76)
- [capabilities](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#afbc65bb8be99f7dc37ecc911f4ac2151)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [output_numeric](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#ae7aec4a89f4260a99696bb46207c4338)
- [output_string](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a28284efee6478637446702d7839f6b8c)
- [input](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a31eff9c903ac721bbca7ab586dda9e80)
- [input_complete](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a2717ddf38465b95452724078f780f9e5)
- [unprovisioned_beacon](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a8142a3b8120b1686f68513caeac09497)
- [unprovisioned_beacon_gatt](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a7eddf1f088264f8b6e3fb86dce4c108e)
- [link_open](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a44efea3e9221c182cbcacce8219ef6b7)
- [link_close](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a0183cef77dda3978ef8a40ce7aad043a)
- [complete](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#ad55abc2b1632455bb23fbd8b03df85ea)
- [reprovisioned](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#ac131476cdeb002f0027407b4cf80c2b5)
- [node_added](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#aaa49675e358ea4cba7552b3e855befba)
- [reset](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#ae87570de25c89e74bece2516ff957779)
- [bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)
- [bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)
- [bt_mesh_input_string](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga2592abf429b40ef9242bce26f5bd085e)
- [bt_mesh_input_numeric](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gabc9d68157928c2b343eddd08ef314d27)
- [bt_mesh_prov_remote_pub_key_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gae33b5b6e9650b49d46494b4a81b18674)
- [bt_mesh_auth_method_set_input](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga80be35bf7287e62cb47d8fba99d648a9)
- [bt_mesh_auth_method_set_output](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gad66ccc725a1cfdf2b79076f22f853f84)
- [bt_mesh_auth_method_set_static](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga7b6024dc32f6ec7f26cbf91545911084)
- [bt_mesh_auth_method_set_none](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gabab41ebdcae2eaa109e03cb2d8fa78c6)
- [bt_mesh_prov_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga6c8dc1b09d4cde8738be83c992b860a9)
- [bt_mesh_prov_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gac7e084e7d12a93377d49b1c3d6313399)
- [bt_mesh_provision](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga4ed6e078c1c0f197758c8dbb23db30f6)
- [net_idx](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md#a2197a70aa97209a60136a09da1f513b2)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [addr](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md#a10ec7b9c480513e742566c6c3b9c4973)
- [bt_mesh_provision_adv](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga0bfae4ebda53052cfa027c3a7ae51ec8)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_mesh_provision_gatt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga60666e0d7629caf36026974621bae664)
- [bt_mesh_provision_remote](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga9fc414e4e15d6b3ab0dae5483ed62982)
- [bt_mesh_reprovision_remote](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaa02583390f635ac251d22ed9ff953974)
- [bt_mesh_is_provisioned](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga0307e62001ba7fa303ed311ebc47f116)
- [bt_mesh_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga521def6f74467a9bd3f2757c6aabd405)
- [bt_mesh_comp](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md)
- [bt_mesh_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga69fc65f4e07e6007388473f139e5d8d8)
- [bt_mesh_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga6c209dbad6881f1e9634d9b7d42f2c34)
- [bt_mesh_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gaa9114ce8941e641dbb23828d7c0451fd)
- [bt_mesh_iv_update_test](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga3fdc601bd036477f6bdf212667c6b0c9)
- [bt_mesh_iv_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gacdf00423b03057fdf3a4207ee579eb74)
- [bt_mesh_lpn_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga7964f5b1abb7b12728e4ec224c95c849)
- [bt_mesh_lpn_poll](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga3fd66605950a55e299ca3a7cc697d453)
- [bt_mesh_lpn_cb](../bluetooth_mesh_model_reference/P072_bt_mesh_lpn_cb_结构体.md)
- [established](../bluetooth_mesh_model_reference/P072_bt_mesh_lpn_cb_结构体.md#a74b8b398b383518af069266cf3b0be91)
- [terminated](../bluetooth_mesh_model_reference/P072_bt_mesh_lpn_cb_结构体.md#af2e2f5043503c62926f96a5fcb48890c)
- [polled](../bluetooth_mesh_model_reference/P072_bt_mesh_lpn_cb_结构体.md#a9805ad8578faec5b371d6f39178332ef)
- [bt_mesh_friend_cb](../bluetooth_mesh_model_reference/P061_bt_mesh_friend_cb_结构体.md)
- [established](../bluetooth_mesh_model_reference/P061_bt_mesh_friend_cb_结构体.md#a824ed814a46a3954d2c6f669c8900156)
- [terminated](../bluetooth_mesh_model_reference/P061_bt_mesh_friend_cb_结构体.md#a1c0d570eb1b857c65b3b5b4ce31999d6)
- [polled](../bluetooth_mesh_model_reference/P061_bt_mesh_friend_cb_结构体.md#a7b904967d89173f82ac26216e3849d23)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [bt_mesh_friend_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga28b9b1d7d732e300be8d4bbffdbad391)
- [bt_mesh_rpl_pending_store](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga62f9a72c4e9dc5e4f3f42bd4df4fe452)
- [bt_mesh_va_uuid_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga20fe74e33e6a35c452cd076c78aa4f05)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [bt_mesh_dev_capabilities::output_actions](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#a359caeaf64f45783b0c576ef8ef14975)
- [bt_mesh_dev_capabilities::output_size](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#a59c959cbd8b1a2aa4e548e7f990cf1f4)
- [bt_mesh_dev_capabilities::input_actions](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#a6132c85094980f839cf9dca57d7969ea)
- [bt_mesh_dev_capabilities::oob_type](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#a744703091988432baa14a84347309bcf)
- [bt_mesh_dev_capabilities::algorithms](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#a762786d98c070d0ae79e09f22bad4b33)
- [bt_mesh_dev_capabilities::pub_key_type](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#a7f549f5b3923c0b4249e1b21368ee857)
- [bt_mesh_dev_capabilities::input_size](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#ac9097c4d634683120509f4c1ac732928)
- [bt_mesh_dev_capabilities::elem_count](../bluetooth_mesh_model_reference/P043_bt_mesh_dev_capabilities_结构体.md#acfef4ecf5ca9324ddc584b9cb910bfe0)
- [bt_mesh_friend_cb::terminated](../bluetooth_mesh_model_reference/P061_bt_mesh_friend_cb_结构体.md#a1c0d570eb1b857c65b3b5b4ce31999d6)
- [bt_mesh_friend_cb::polled](../bluetooth_mesh_model_reference/P061_bt_mesh_friend_cb_结构体.md#a7b904967d89173f82ac26216e3849d23)
- [bt_mesh_friend_cb::established](../bluetooth_mesh_model_reference/P061_bt_mesh_friend_cb_结构体.md#a824ed814a46a3954d2c6f669c8900156)
- [bt_mesh_lpn_cb::established](../bluetooth_mesh_model_reference/P072_bt_mesh_lpn_cb_结构体.md#a74b8b398b383518af069266cf3b0be91)
- [bt_mesh_lpn_cb::polled](../bluetooth_mesh_model_reference/P072_bt_mesh_lpn_cb_结构体.md#a9805ad8578faec5b371d6f39178332ef)
- [bt_mesh_lpn_cb::terminated](../bluetooth_mesh_model_reference/P072_bt_mesh_lpn_cb_结构体.md#af2e2f5043503c62926f96a5fcb48890c)
- [bt_mesh_prov::link_close](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a0183cef77dda3978ef8a40ce7aad043a)
- [bt_mesh_prov::uuid](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a1152d77c4c4d9271bbd72514d94052f2)
- [bt_mesh_prov::public_key_be](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a1261ba69e785f005d5834ac49da00778)
- [bt_mesh_prov::private_key_be](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a1ab714e9be35242e02099884c3af45f5)
- [bt_mesh_prov::input_complete](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a2717ddf38465b95452724078f780f9e5)
- [bt_mesh_prov::output_string](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a28284efee6478637446702d7839f6b8c)
- [bt_mesh_prov::input](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a31eff9c903ac721bbca7ab586dda9e80)
- [bt_mesh_prov::link_open](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a44efea3e9221c182cbcacce8219ef6b7)
- [bt_mesh_prov::output_size](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a4c51aa8e5887b3364d9480c92da3a0a0)
- [bt_mesh_prov::uri](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a6a11cc0d36ca2f4c5aee67a023c295a2)
- [bt_mesh_prov::oob_info](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a6ed61556291f7f9d9a32062d588b8f2a)
- [bt_mesh_prov::unprovisioned_beacon_gatt](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a7eddf1f088264f8b6e3fb86dce4c108e)
- [bt_mesh_prov::unprovisioned_beacon](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a8142a3b8120b1686f68513caeac09497)
- [bt_mesh_prov::output_actions](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a8b88959c5eef7f47591468e9c9768b7c)
- [bt_mesh_prov::static_val_len](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a97394dded5fd55b553364a566a2441e8)
- [bt_mesh_prov::static_val](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#a97cf41cf857479c8eefee640f7b66788)
- [bt_mesh_prov::node_added](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#aaa49675e358ea4cba7552b3e855befba)
- [bt_mesh_prov::input_size](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#ab9044f6dbf9780b3237f18270b2c8582)
- [bt_mesh_prov::reprovisioned](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#ac131476cdeb002f0027407b4cf80c2b5)
- [bt_mesh_prov::complete](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#ad55abc2b1632455bb23fbd8b03df85ea)
- [bt_mesh_prov::output_numeric](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#ae7aec4a89f4260a99696bb46207c4338)
- [bt_mesh_prov::reset](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#ae87570de25c89e74bece2516ff957779)
- [bt_mesh_prov::input_actions](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#af928a9419f684bcbda0563dda2c34d76)
- [bt_mesh_prov::capabilities](../bluetooth_mesh_model_reference/P088_bt_mesh_prov_结构体.md#afbc65bb8be99f7dc37ecc911f4ac2151)
- [bt_mesh_rpr_node::addr](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md#a10ec7b9c480513e742566c6c3b9c4973)
- [bt_mesh_rpr_node::net_idx](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md#a2197a70aa97209a60136a09da1f513b2)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P101_lock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P103_max22017.h_源码浏览.md)
