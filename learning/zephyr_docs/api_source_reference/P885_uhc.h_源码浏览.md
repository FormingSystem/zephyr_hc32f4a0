---
id: learning.zephyr-docs.api-source-reference.page-885
title: uhc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uhc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第885章\_uhc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/uhc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/uhc_8h.html)。

## 885.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00031"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="foldopen00170"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="foldopen00204"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="foldopen00237"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00245"></a>
<a id="l00249"></a>
<a id="l00250"></a>
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
<a id="l00274"></a>
<a id="l00275"></a>
<a id="foldopen00283"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="foldopen00297"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
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
<a id="l00325"></a>
<a id="l00329"></a>
<a id="foldopen00341"></a>
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
<a id="foldopen00363"></a>
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
<a id="l00373"></a>
<a id="l00374"></a>
<a id="foldopen00386"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="foldopen00409"></a>
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
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="foldopen00625"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="foldopen00642"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adlist_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__atomic__apis_html_ga153c7d3a124e95ddf29e6f65bd124e44"></a>
<a id="agroup__doubly-linked-list__apis_html_ga57fdb936802a617d16c00ab08cd2ad98"></a>
<a id="agroup__doubly-linked-list__apis_html_gaa03f9557215b486fee1039dd4c07e683"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__uhc__api_html_ga09ad6fc9251212fa0dffececb767ff9e"></a>
<a id="agroup__uhc__api_html_ga09b71dc5c334f09fb92cf37e2ecf51eb"></a>
<a id="agroup__uhc__api_html_ga1b1ec49cb7649ece6ec5a31dac3e2537"></a>
<a id="agroup__uhc__api_html_ga230e104bd7be1d4b83b2d31ee72ac3c4"></a>
<a id="agroup__uhc__api_html_ga3251967d36b67169d7892a615323c14e"></a>
<a id="agroup__uhc__api_html_ga3cda056094ceef79dd62ad9c6852daf9"></a>
<a id="agroup__uhc__api_html_ga4468d1460d79dc30b2605e36ba478e40"></a>
<a id="agroup__uhc__api_html_ga4ceb0400168cd53201f0dde5f596452f"></a>
<a id="agroup__uhc__api_html_ga59ba7bbb99177a622f3c073fc48b7bc5"></a>
<a id="agroup__uhc__api_html_ga6669bc2ac56395b38292fa796b99bfd9"></a>
<a id="agroup__uhc__api_html_ga69748d0650399a51672b98b475ab8437"></a>
<a id="agroup__uhc__api_html_ga7127ac2a46b577f2aa1bb9a650e62a3f"></a>
<a id="agroup__uhc__api_html_ga75c2142698a15c547ab76ab76c89c177"></a>
<a id="agroup__uhc__api_html_ga779dbd7ee8ac5fce487e087706791ea7"></a>
<a id="agroup__uhc__api_html_ga7a07b598c00d53393e15f6dae5cf1c4a"></a>
<a id="agroup__uhc__api_html_ga7c362cba29e0181ffcc8f70060100e62"></a>
<a id="agroup__uhc__api_html_ga8796569eba96260ce332e611fb520033"></a>
<a id="agroup__uhc__api_html_ga897081ff02dab4377c68bcba343f492c"></a>
<a id="agroup__uhc__api_html_ga97beb6e3b3d4ad1b0b7664eae473e1be"></a>
<a id="agroup__uhc__api_html_ga9ec92df4497588adbf8da6f0777a4afd"></a>
<a id="agroup__uhc__api_html_gab2f6328e8051559edccc05ae3552f4f9"></a>
<a id="agroup__uhc__api_html_gab399b0ad7f6d856251af56cd92240351"></a>
<a id="agroup__uhc__api_html_gab4f7439fab8c57e203862bc408a6e46b"></a>
<a id="agroup__uhc__api_html_gab5a2df4d176d4c85751c3158b63e366b"></a>
<a id="agroup__uhc__api_html_gabaf69c1e69fe0fb3d912b92daf8754eb"></a>
<a id="agroup__uhc__api_html_gac4bd26a85f8abc2006ecf2622669d615"></a>
<a id="agroup__uhc__api_html_gac6d1feb9481882a711e58c3e55e915cb"></a>
<a id="agroup__uhc__api_html_gaef9b0703714676c1f7bd1cad57f49bc8"></a>
<a id="agroup__uhc__api_html_gafe55e97cbf31d163b10616c03da39414"></a>
<a id="agroup__uhc__api_html_gafe94b7f9e32aada9634166ebb2115c2f"></a>
<a id="agroup__uhc__api_html_gga59ba7bbb99177a622f3c073fc48b7bc5a36e25f2ed5532d6a281abaf521583fcc"></a>
<a id="agroup__uhc__api_html_gga59ba7bbb99177a622f3c073fc48b7bc5a46c4232a37347ac22ac14b240abddbdc"></a>
<a id="agroup__uhc__api_html_gga59ba7bbb99177a622f3c073fc48b7bc5a8cd687699d8afb4d818595d70b189e27"></a>
<a id="agroup__uhc__api_html_gga59ba7bbb99177a622f3c073fc48b7bc5aab0ef8e9a798d70fd3c93e68785c0968"></a>
<a id="agroup__uhc__api_html_gga59ba7bbb99177a622f3c073fc48b7bc5ac9755ae6b86f8148054fd6a342c74acc"></a>
<a id="agroup__uhc__api_html_gga7127ac2a46b577f2aa1bb9a650e62a3fa6566e87fb6d54f2da5b7564743df7a47"></a>
<a id="agroup__uhc__api_html_gga7127ac2a46b577f2aa1bb9a650e62a3fa70367cdc7b5d7d1f3ab046391f50df9d"></a>
<a id="agroup__uhc__api_html_gga7127ac2a46b577f2aa1bb9a650e62a3fabb0f4a1c2f62f028bec1d0b55b5d5554"></a>
<a id="agroup__uhc__api_html_gga7127ac2a46b577f2aa1bb9a650e62a3fad7f0841a21d3179c13f19d3ae8a8e3b6"></a>
<a id="agroup__uhc__api_html_ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483"></a>
<a id="agroup__uhc__api_html_ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f"></a>
<a id="agroup__uhc__api_html_ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce"></a>
<a id="agroup__uhc__api_html_ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e"></a>
<a id="agroup__uhc__api_html_ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a"></a>
<a id="agroup__uhc__api_html_ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30"></a>
<a id="agroup__uhc__api_html_ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848"></a>
<a id="agroup__uhc__api_html_ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70"></a>
<a id="agroup__uhc__api_html_ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7"></a>
<a id="agroup__uhc__api_html_ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3"></a>
<a id="agroup__uhc__api_html_ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5"></a>
<a id="agroup__uhc__api_html_ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8"></a>
<a id="agroup__uhc__api_html_ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f"></a>
<a id="agroup__usb__buf_html_ga5cfb8cab648a98fbc21ec1edbce057b7"></a>
<a id="agroup__usb__buf_html_ga7c04001e0a2fba2d343d7d2eee6aff37"></a>
<a id="akernel_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="aposix_2sys_2socket_8h_html_a8dadddc96fee56a9f8b0904aca02eab2"></a>
<a id="aref_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructk__mutex_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_a1522d81a002804223e25300a6961f527"></a>
<a id="astructsys__ref_html"></a>
<a id="astructuhc__data_html"></a>
<a id="astructuhc__data_html_a08772cdd5b42bd11ca4a06a75df846e9"></a>
<a id="astructuhc__data_html_a10852f2523cc733541cc9ea51706559f"></a>
<a id="astructuhc__data_html_a294120f6cf8563cb9564c51fcf56d883"></a>
<a id="astructuhc__data_html_a32eec449ffbe5e6c262c907e6e6b475a"></a>
<a id="astructuhc__data_html_a9f4904633f530748c8e3b2ac3ad0563f"></a>
<a id="astructuhc__data_html_ac2a48d1d6692931807e8985799c5bdb0"></a>
<a id="astructuhc__data_html_ac6214566324740c34a8bba42515d1d32"></a>
<a id="astructuhc__data_html_afd1a0828a0ca3e397dba09fe38fd8050"></a>
<a id="astructuhc__device__caps_html"></a>
<a id="astructuhc__device__caps_html_ab526337af28d25728780cb48dc43e722"></a>
<a id="astructuhc__event_html"></a>
<a id="astructuhc__event_html_a03f3cebee6edfaf620a98c198a70dbd0"></a>
<a id="astructuhc__event_html_a055be3fd47e16bc48498163be3e55d09"></a>
<a id="astructuhc__event_html_a30fddbbe0f15a16320fba3cb4fd81d84"></a>
<a id="astructuhc__event_html_a5d7e1cc1bcb25e10f009ac3a8acd94b6"></a>
<a id="astructuhc__event_html_acd04587fac14f9a8a91b75642f5b2e82"></a>
<a id="astructuhc__transfer_html"></a>
<a id="astructuhc__transfer_html_a0f2d4a735ce224260d100dc756b1900f"></a>
<a id="astructuhc__transfer_html_a105b30625208c612b4abe857e208a7f1"></a>
<a id="astructuhc__transfer_html_a11f002f91b1039c226b7c9feb8223e11"></a>
<a id="astructuhc__transfer_html_a170385b08171659f05ac7112faf8e587"></a>
<a id="astructuhc__transfer_html_a23e4115c774134ccd143189b0f4f2460"></a>
<a id="astructuhc__transfer_html_a584f5713acc9c191a5a3f4ff7d77435c"></a>
<a id="astructuhc__transfer_html_a61a6c74cc7c026404ccf42d1164765b8"></a>
<a id="astructuhc__transfer_html_a81a8a80809420787f4c0ab232a24a514"></a>
<a id="astructuhc__transfer_html_a9983482be9724e281e56c978ce27d93f"></a>
<a id="astructuhc__transfer_html_aaf664844dc9f1871cce3d38516c042ef"></a>
<a id="astructuhc__transfer_html_ad2b246c850c3b30f7d2b58fc9a47008b"></a>
<a id="astructuhc__transfer_html_ad4d80a3f20cdec7dd2237a98054dd287"></a>
<a id="astructuhc__transfer_html_ad4dbc766c6ded0ebfab7e36b19643b15"></a>
<a id="astructuhc__transfer_html_ae1fcb0b866e3d7c5b5ea9dff6221f37d"></a>
<a id="astructuhc__transfer_html_ae681c0078b8afedd3b6fba165861e114"></a>
<a id="astructuhc__transfer_html_af6d6de482f092e4f85679722ad609cbf"></a>
<a id="astructusb__association__descriptor_html"></a>
<a id="astructusb__desc__header_html"></a>
<a id="astructusb__device__descriptor_html"></a>
<a id="astructusb__device_html"></a>
<a id="astructusb__device_html_a0215608e40123de4a3a79ca440c6c593"></a>
<a id="astructusb__device_html_a101d30facb781bd410581fc6c2d3fa59"></a>
<a id="astructusb__device_html_a1b3f4becfd9fbfae80074fc2e76ea6a8"></a>
<a id="astructusb__device_html_a24be9609d416d3a184fdedbefa298490"></a>
<a id="astructusb__device_html_a4203b2cfd65f70096a43a20c7c37de27"></a>
<a id="astructusb__device_html_a475090912a408eaa2f04d582a1367114"></a>
<a id="astructusb__device_html_a4a66403ece2f186d59ff29e39dc78839"></a>
<a id="astructusb__device_html_a5cccbb483d91032f4a7f25f88270747f"></a>
<a id="astructusb__device_html_a658b9992a472574b1d88e49b7fea478d"></a>
<a id="astructusb__device_html_a72ee0e53efd86c91e0cea6c7e873d5ce"></a>
<a id="astructusb__device_html_aa75bbea6a879460b39216453323d177f"></a>
<a id="astructusb__device_html_aa9062a5b9da663863e6d51ef2e04197b"></a>
<a id="astructusb__device_html_ac98af9fb0d5bba21bc8037a8fcfb3126"></a>
<a id="astructusb__device_html_ad3091acb2a713b9e66c595bbf4a736a5"></a>
<a id="astructusb__device_html_ada9943f1917010381116cd778d6bc47c"></a>
<a id="astructusb__device_html_ae0c9c3454eea32432ddb4f8da7361182"></a>
<a id="astructusb__ep__descriptor_html"></a>
<a id="astructusb__host__ep_html"></a>
<a id="astructusb__host__ep_html_a25e9c4004ab03927476093ed4d167dbd"></a>
<a id="astructusb__host__interface_html"></a>
<a id="astructusb__host__interface_html_a4405cdfb6aa6fbbcd2ac27148b9ebea6"></a>
<a id="astructusb__host__interface_html_a8241bb80e15d8434802aad81ba0fc810"></a>
<a id="astructusb__host__interface_html_aa0170523367f9e1459a9ba897c0d88bf"></a>
<a id="ausb__buf_8h_html"></a>
<a id="ausb__ch9_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_UHC_H
#define ZEPHYR_INCLUDE_UHC_H

#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/net_buf.h>
#include <zephyr/drivers/usb/usb_buf.h>
#include <zephyr/usb/usb_ch9.h>
#include <zephyr/sys/dlist.h>
#include <zephyr/sys/ref.h>


enum usb_device_state {
        USB_STATE_NOTCONNECTED,
        USB_STATE_DEFAULT,
        USB_STATE_ADDRESSED,
        USB_STATE_CONFIGURED,
};

enum usb_device_speed {
        USB_SPEED_UNKNOWN,
        USB_SPEED_SPEED_LS,
        USB_SPEED_SPEED_FS,
        USB_SPEED_SPEED_HS,
        USB_SPEED_SPEED_SS,
};

#define UHC_INTERFACES_MAX 32

struct usb_host_interface {
        struct usb_desc_header *dhp;
        struct usb_association_descriptor *iad;
        uint8_t alternate;
};

struct usb_host_ep {
        struct usb_ep_descriptor *desc;
};

struct usb_device {
        sys_dnode_t node;
        void *ctx;
        struct k_mutex mutex;
        struct usb_device_descriptor dev_desc;
        enum usb_device_state state;
        enum usb_device_speed speed;
        uint8_t actual_cfg;
        uint8_t addr;
        void *cfg_desc;
        struct usb_host_interface ifaces[UHC_INTERFACES_MAX + 1];
        struct usb_host_ep ep_out[16];
        struct usb_host_ep ep_in[16];
        struct usb_device *hub;
        uint16_t tt;
        uint8_t hub_port;
        uint8_t level;
};

enum uhc_control_stage {
        UHC_CONTROL_STAGE_SETUP = 0,
        UHC_CONTROL_STAGE_DATA,
        UHC_CONTROL_STAGE_STATUS,
};

struct uhc_transfer {
        sys_dnode_t node;
        struct sys_ref ref;
        __aligned(USB_BUF_ALIGN) uint8_t setup_pkt[USB_BUF_ROUND_UP(8)];
        struct net_buf *buf;
        uint8_t ep;
        uint8_t type;
        uint16_t mps;
        uint16_t interval;
        uint16_t start_frame;
        unsigned int queued : 1;
        unsigned int stage : 2;
        unsigned int no_status : 1;
        struct usb_device *udev;
        void *cb;
        void *priv;
        int err;
};

enum uhc_event_type {
        UHC_EVT_DEV_CONNECTED_LS,
        UHC_EVT_DEV_CONNECTED_FS,
        UHC_EVT_DEV_CONNECTED_HS,
        UHC_EVT_DEV_REMOVED,
        UHC_EVT_RESETED,
        UHC_EVT_SUSPENDED,
        UHC_EVT_RESUMED,
        UHC_EVT_RWUP,
        UHC_EVT_EP_REQUEST,
        UHC_EVT_ERROR,
};

struct uhc_event {
        sys_snode_t node;
        enum uhc_event_type type;
        union {
                int status;
                struct uhc_transfer *xfer;
        };
        const struct device *dev;
};

typedef int (*uhc_event_cb_t)(const struct device *dev,
                              const struct uhc_event *const event);

struct uhc_device_caps {
        uint32_t hs : 1;
};

#define UHC_STATUS_INITIALIZED          0
#define UHC_STATUS_ENABLED              1

struct uhc_data {
        struct uhc_device_caps caps;
        struct k_mutex mutex;
        sys_dlist_t ctrl_xfers;
        sys_dlist_t bulk_xfers;
        uhc_event_cb_t event_cb;
        const void *event_ctx;
        atomic_t status;
        void *priv;
};

static inline bool uhc_is_initialized(const struct device *dev)
{
        struct uhc_data *data = dev->data;

        return atomic_test_bit(&data->status, UHC_STATUS_INITIALIZED);
}

static inline bool uhc_is_enabled(const struct device *dev)
{
        struct uhc_data *data = dev->data;

        return atomic_test_bit(&data->status, UHC_STATUS_ENABLED);
}

__subsystem struct uhc_driver_api {
        int (*lock)(const struct device *dev);
        int (*unlock)(const struct device *dev);

        int (*init)(const struct device *dev);
        int (*enable)(const struct device *dev);
        int (*disable)(const struct device *dev);
        int (*shutdown)(const struct device *dev);

        int (*bus_reset)(const struct device *dev);
        int (*sof_enable)(const struct device *dev);
        int (*bus_suspend)(const struct device *dev);
        int (*bus_resume)(const struct device *dev);

        int (*ep_enqueue)(const struct device *dev,
                          struct uhc_transfer *const xfer);
        int (*ep_dequeue)(const struct device *dev,
                          struct uhc_transfer *const xfer);
};

static inline int uhc_bus_reset(const struct device *dev)
{
        const struct uhc_driver_api *api = DEVICE_API_GET(uhc, dev);
        int ret;

        api->lock(dev);
        ret = api->bus_reset(dev);
        api->unlock(dev);

        return ret;
}

static inline int uhc_sof_enable(const struct device *dev)
{
        const struct uhc_driver_api *api = DEVICE_API_GET(uhc, dev);
        int ret;

        api->lock(dev);
        ret = api->sof_enable(dev);
        api->unlock(dev);

        return ret;
}

static inline int uhc_bus_suspend(const struct device *dev)
{
        const struct uhc_driver_api *api = DEVICE_API_GET(uhc, dev);
        int ret;

        api->lock(dev);
        ret = api->bus_suspend(dev);
        api->unlock(dev);

        return ret;
}

static inline int uhc_bus_resume(const struct device *dev)
{
        const struct uhc_driver_api *api = DEVICE_API_GET(uhc, dev);
        int ret;

        api->lock(dev);
        ret = api->bus_resume(dev);
        api->unlock(dev);

        return ret;
}

struct uhc_transfer *uhc_xfer_alloc(const struct device *dev,
                                    const uint8_t ep,
                                    struct usb_device *const udev,
                                    void *const cb,
                                    void *const cb_priv);

struct uhc_transfer *uhc_xfer_alloc_with_buf(const struct device *dev,
                                             const uint8_t ep,
                                             struct usb_device *const udev,
                                             void *const cb,
                                             void *const cb_priv,
                                             size_t size);

void uhc_xfer_ref(struct uhc_transfer *const xfer);

bool uhc_xfer_unref(struct uhc_transfer *const xfer);

int uhc_xfer_free(const struct device *dev,
                  struct uhc_transfer *const xfer);

int uhc_xfer_buf_add(const struct device *dev,
                     struct uhc_transfer *const xfer,
                     struct net_buf *buf);
struct net_buf *uhc_xfer_buf_alloc(const struct device *dev,
                                   const size_t size);

void uhc_xfer_buf_free(const struct device *dev, struct net_buf *const buf);

int uhc_ep_enqueue(const struct device *dev, struct uhc_transfer *const xfer);

int uhc_ep_dequeue(const struct device *dev, struct uhc_transfer *const xfer);

int uhc_init(const struct device *dev,
             uhc_event_cb_t event_cb, const void *const event_ctx);

int uhc_enable(const struct device *dev);

int uhc_disable(const struct device *dev);

int uhc_shutdown(const struct device *dev);

static inline struct uhc_device_caps uhc_caps(const struct device *dev)
{
        struct uhc_data *data = dev->data;

        return data->caps;
}

static inline const void *uhc_get_event_ctx(const struct device *dev)
{
        struct uhc_data *data = dev->data;

        return data->event_ctx;
}


#endif /* ZEPHYR_INCLUDE_UHC_H */
```

## 885.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 653 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_UHC_H`。

## 885.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/uhc_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/drivers/usb/usb_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/usb__buf_8h.html)
- [zephyr/usb/usb_ch9.h](../usb/P172_USB标准请求与描述符常量.md)
- [zephyr/sys/dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [zephyr/sys/ref.h](../sysref_reference/P003_引用计数头文件参考.md)
- [usb_device_state](../usb/P073_USB主机控制器API.md#ga7127ac2a46b577f2aa1bb9a650e62a3f)
- [USB_STATE_NOTCONNECTED](../usb/P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa70367cdc7b5d7d1f3ab046391f50df9d)
- [USB_STATE_DEFAULT](../usb/P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fabb0f4a1c2f62f028bec1d0b55b5d5554)
- [USB_STATE_ADDRESSED](../usb/P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fad7f0841a21d3179c13f19d3ae8a8e3b6)
- [USB_STATE_CONFIGURED](../usb/P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa6566e87fb6d54f2da5b7564743df7a47)
- [usb_device_speed](../usb/P073_USB主机控制器API.md#ga59ba7bbb99177a622f3c073fc48b7bc5)
- [USB_SPEED_UNKNOWN](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5ac9755ae6b86f8148054fd6a342c74acc)
- [USB_SPEED_SPEED_LS](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5a46c4232a37347ac22ac14b240abddbdc)
- [USB_SPEED_SPEED_FS](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5a8cd687699d8afb4d818595d70b189e27)
- [USB_SPEED_SPEED_HS](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5aab0ef8e9a798d70fd3c93e68785c0968)
- [USB_SPEED_SPEED_SS](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5a36e25f2ed5532d6a281abaf521583fcc)
- [usb_host_interface](../usb/P081_USB主机接口对象.md)
- [usb_desc_header](../usb/P161_USB通用描述符头.md)
- [dhp](../usb/P081_USB主机接口对象.md#aa0170523367f9e1459a9ba897c0d88bf)
- [usb_association_descriptor](../usb/P167_USB接口关联描述符.md)
- [iad](../usb/P081_USB主机接口对象.md#a8241bb80e15d8434802aad81ba0fc810)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [alternate](../usb/P081_USB主机接口对象.md#a4405cdfb6aa6fbbcd2ac27148b9ebea6)
- [usb_host_ep](../usb/P082_USB主机端点对象.md)
- [usb_ep_descriptor](../usb/P166_USB端点描述符.md)
- [desc](../usb/P082_USB主机端点对象.md#a25e9c4004ab03927476093ed4d167dbd)
- [usb_device](../usb/P080_USB主机设备对象.md)
- [sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)
- [node](../usb/P080_USB主机设备对象.md#a0215608e40123de4a3a79ca440c6c593)
- [ctx](../usb/P080_USB主机设备对象.md#a72ee0e53efd86c91e0cea6c7e873d5ce)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [mutex](../usb/P080_USB主机设备对象.md#a4203b2cfd65f70096a43a20c7c37de27)
- [usb_device_descriptor](../usb/P163_USB设备描述符.md)
- [dev_desc](../usb/P080_USB主机设备对象.md#a24be9609d416d3a184fdedbefa298490)
- [state](../usb/P080_USB主机设备对象.md#aa75bbea6a879460b39216453323d177f)
- [speed](../usb/P080_USB主机设备对象.md#a1b3f4becfd9fbfae80074fc2e76ea6a8)
- [actual_cfg](../usb/P080_USB主机设备对象.md#a101d30facb781bd410581fc6c2d3fa59)
- [addr](../usb/P080_USB主机设备对象.md#aa9062a5b9da663863e6d51ef2e04197b)
- [cfg_desc](../usb/P080_USB主机设备对象.md#ac98af9fb0d5bba21bc8037a8fcfb3126)
- [ifaces](../usb/P080_USB主机设备对象.md#a5cccbb483d91032f4a7f25f88270747f)
- [UHC_INTERFACES_MAX](../usb/P073_USB主机控制器API.md#ga1b1ec49cb7649ece6ec5a31dac3e2537)
- [ep_out](../usb/P080_USB主机设备对象.md#a658b9992a472574b1d88e49b7fea478d)
- [ep_in](../usb/P080_USB主机设备对象.md#ad3091acb2a713b9e66c595bbf4a736a5)
- [hub](../usb/P080_USB主机设备对象.md#a475090912a408eaa2f04d582a1367114)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [tt](../usb/P080_USB主机设备对象.md#ae0c9c3454eea32432ddb4f8da7361182)
- [hub_port](../usb/P080_USB主机设备对象.md#a4a66403ece2f186d59ff29e39dc78839)
- [level](../usb/P080_USB主机设备对象.md#ada9943f1917010381116cd778d6bc47c)
- [uhc_control_stage](../usb/P073_USB主机控制器API.md#gaef9b0703714676c1f7bd1cad57f49bc8)
- [UHC_CONTROL_STAGE_SETUP](../usb/P073_USB主机控制器API.md#ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8)
- [UHC_CONTROL_STAGE_DATA](../usb/P073_USB主机控制器API.md#ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5)
- [UHC_CONTROL_STAGE_STATUS](../usb/P073_USB主机控制器API.md#ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f)
- [uhc_transfer](../usb/P077_USB主机传输结构.md)
- [node](../usb/P077_USB主机传输结构.md#ae1fcb0b866e3d7c5b5ea9dff6221f37d)
- [sys_ref](../sysref_reference/P002_引用计数对象.md)
- [ref](../usb/P077_USB主机传输结构.md#a105b30625208c612b4abe857e208a7f1)
- [USB_BUF_ALIGN](../usb/P039_USB缓冲区宏与定义.md#ga7c04001e0a2fba2d343d7d2eee6aff37)
- [setup_pkt](../usb/P077_USB主机传输结构.md#ae681c0078b8afedd3b6fba165861e114)
- [USB_BUF_ROUND_UP](../usb/P039_USB缓冲区宏与定义.md#ga5cfb8cab648a98fbc21ec1edbce057b7)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [buf](../usb/P077_USB主机传输结构.md#a170385b08171659f05ac7112faf8e587)
- [ep](../usb/P077_USB主机传输结构.md#aaf664844dc9f1871cce3d38516c042ef)
- [type](../usb/P077_USB主机传输结构.md#ad4dbc766c6ded0ebfab7e36b19643b15)
- [mps](../usb/P077_USB主机传输结构.md#a61a6c74cc7c026404ccf42d1164765b8)
- [interval](../usb/P077_USB主机传输结构.md#af6d6de482f092e4f85679722ad609cbf)
- [start_frame](../usb/P077_USB主机传输结构.md#a23e4115c774134ccd143189b0f4f2460)
- [queued](../usb/P077_USB主机传输结构.md#ad2b246c850c3b30f7d2b58fc9a47008b)
- [stage](../usb/P077_USB主机传输结构.md#a9983482be9724e281e56c978ce27d93f)
- [no_status](../usb/P077_USB主机传输结构.md#a584f5713acc9c191a5a3f4ff7d77435c)
- [udev](../usb/P077_USB主机传输结构.md#a81a8a80809420787f4c0ab232a24a514)
- [cb](../usb/P077_USB主机传输结构.md#ad4d80a3f20cdec7dd2237a98054dd287)
- [priv](../usb/P077_USB主机传输结构.md#a0f2d4a735ce224260d100dc756b1900f)
- [err](../usb/P077_USB主机传输结构.md#a11f002f91b1039c226b7c9feb8223e11)
- [uhc_event_type](../usb/P073_USB主机控制器API.md#gabaf69c1e69fe0fb3d912b92daf8754eb)
- [UHC_EVT_DEV_CONNECTED_LS](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70)
- [UHC_EVT_DEV_CONNECTED_FS](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce)
- [UHC_EVT_DEV_CONNECTED_HS](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f)
- [UHC_EVT_DEV_REMOVED](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30)
- [UHC_EVT_RESETED](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3)
- [UHC_EVT_SUSPENDED](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a)
- [UHC_EVT_RESUMED](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848)
- [UHC_EVT_RWUP](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e)
- [UHC_EVT_EP_REQUEST](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483)
- [UHC_EVT_ERROR](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7)
- [uhc_event](../usb/P076_USB主机控制器事件.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../usb/P076_USB主机控制器事件.md#acd04587fac14f9a8a91b75642f5b2e82)
- [type](../usb/P076_USB主机控制器事件.md#a30fddbbe0f15a16320fba3cb4fd81d84)
- [status](../usb/P076_USB主机控制器事件.md#a5d7e1cc1bcb25e10f009ac3a8acd94b6)
- [xfer](../usb/P076_USB主机控制器事件.md#a03f3cebee6edfaf620a98c198a70dbd0)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../usb/P076_USB主机控制器事件.md#a055be3fd47e16bc48498163be3e55d09)
- [uhc_event_cb_t](../usb/P073_USB主机控制器API.md#ga3cda056094ceef79dd62ad9c6852daf9)
- [uhc_device_caps](../usb/P075_USB主机控制器能力.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [hs](../usb/P075_USB主机控制器能力.md#ab526337af28d25728780cb48dc43e722)
- [uhc_data](../usb/P074_USB主机控制器数据.md)
- [caps](../usb/P074_USB主机控制器数据.md#ac2a48d1d6692931807e8985799c5bdb0)
- [mutex](../usb/P074_USB主机控制器数据.md#a08772cdd5b42bd11ca4a06a75df846e9)
- [sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)
- [ctrl_xfers](../usb/P074_USB主机控制器数据.md#a32eec449ffbe5e6c262c907e6e6b475a)
- [bulk_xfers](../usb/P074_USB主机控制器数据.md#ac6214566324740c34a8bba42515d1d32)
- [event_cb](../usb/P074_USB主机控制器数据.md#afd1a0828a0ca3e397dba09fe38fd8050)
- [event_ctx](../usb/P074_USB主机控制器数据.md#a9f4904633f530748c8e3b2ac3ad0563f)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [status](../usb/P074_USB主机控制器数据.md#a10852f2523cc733541cc9ea51706559f)
- [priv](../usb/P074_USB主机控制器数据.md#a294120f6cf8563cb9564c51fcf56d883)
- [uhc_is_initialized](../usb/P073_USB主机控制器API.md#ga3251967d36b67169d7892a615323c14e)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [atomic_test_bit](https://docs.zephyrproject.org/latest/doxygen/html/group__atomic__apis.html#ga153c7d3a124e95ddf29e6f65bd124e44)
- [UHC_STATUS_INITIALIZED](../usb/P073_USB主机控制器API.md#ga09ad6fc9251212fa0dffececb767ff9e)
- [uhc_is_enabled](../usb/P073_USB主机控制器API.md#ga09b71dc5c334f09fb92cf37e2ecf51eb)
- [UHC_STATUS_ENABLED](../usb/P073_USB主机控制器API.md#ga230e104bd7be1d4b83b2d31ee72ac3c4)
- [shutdown](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a8dadddc96fee56a9f8b0904aca02eab2)
- [uhc_bus_reset](../usb/P073_USB主机控制器API.md#ga4ceb0400168cd53201f0dde5f596452f)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [uhc_sof_enable](../usb/P073_USB主机控制器API.md#gafe55e97cbf31d163b10616c03da39414)
- [uhc_bus_suspend](../usb/P073_USB主机控制器API.md#ga897081ff02dab4377c68bcba343f492c)
- [uhc_bus_resume](../usb/P073_USB主机控制器API.md#ga6669bc2ac56395b38292fa796b99bfd9)
- [uhc_xfer_alloc](../usb/P073_USB主机控制器API.md#gab5a2df4d176d4c85751c3158b63e366b)
- [uhc_xfer_alloc_with_buf](../usb/P073_USB主机控制器API.md#ga75c2142698a15c547ab76ab76c89c177)
- [uhc_xfer_ref](../usb/P073_USB主机控制器API.md#ga69748d0650399a51672b98b475ab8437)
- [uhc_xfer_unref](../usb/P073_USB主机控制器API.md#gab399b0ad7f6d856251af56cd92240351)
- [uhc_xfer_free](../usb/P073_USB主机控制器API.md#gab2f6328e8051559edccc05ae3552f4f9)
- [uhc_xfer_buf_add](../usb/P073_USB主机控制器API.md#ga779dbd7ee8ac5fce487e087706791ea7)
- [uhc_xfer_buf_alloc](../usb/P073_USB主机控制器API.md#gab4f7439fab8c57e203862bc408a6e46b)
- [size](../network_core_model_reference/P046_net_buf_结构体.md#a1522d81a002804223e25300a6961f527)
- [uhc_xfer_buf_free](../usb/P073_USB主机控制器API.md#gac4bd26a85f8abc2006ecf2622669d615)
- [uhc_ep_enqueue](../usb/P073_USB主机控制器API.md#ga7a07b598c00d53393e15f6dae5cf1c4a)
- [uhc_ep_dequeue](../usb/P073_USB主机控制器API.md#ga7c362cba29e0181ffcc8f70060100e62)
- [uhc_init](../usb/P073_USB主机控制器API.md#ga97beb6e3b3d4ad1b0b7664eae473e1be)
- [uhc_enable](../usb/P073_USB主机控制器API.md#gafe94b7f9e32aada9634166ebb2115c2f)
- [uhc_disable](../usb/P073_USB主机控制器API.md#ga9ec92df4497588adbf8da6f0777a4afd)
- [uhc_shutdown](../usb/P073_USB主机控制器API.md#gac6d1feb9481882a711e58c3e55e915cb)
- [uhc_caps](../usb/P073_USB主机控制器API.md#ga8796569eba96260ce332e611fb520033)
- [uhc_get_event_ctx](../usb/P073_USB主机控制器API.md#ga4468d1460d79dc30b2605e36ba478e40)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [ref.h](../sysref_reference/P003_引用计数头文件参考.md)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [net_buf::size](../network_core_model_reference/P046_net_buf_结构体.md#a1522d81a002804223e25300a6961f527)
- [uhc_data::mutex](../usb/P074_USB主机控制器数据.md#a08772cdd5b42bd11ca4a06a75df846e9)
- [uhc_data::status](../usb/P074_USB主机控制器数据.md#a10852f2523cc733541cc9ea51706559f)
- [uhc_data::priv](../usb/P074_USB主机控制器数据.md#a294120f6cf8563cb9564c51fcf56d883)
- [uhc_data::ctrl_xfers](../usb/P074_USB主机控制器数据.md#a32eec449ffbe5e6c262c907e6e6b475a)
- [uhc_data::event_ctx](../usb/P074_USB主机控制器数据.md#a9f4904633f530748c8e3b2ac3ad0563f)
- [uhc_data::caps](../usb/P074_USB主机控制器数据.md#ac2a48d1d6692931807e8985799c5bdb0)
- [uhc_data::bulk_xfers](../usb/P074_USB主机控制器数据.md#ac6214566324740c34a8bba42515d1d32)
- [uhc_data::event_cb](../usb/P074_USB主机控制器数据.md#afd1a0828a0ca3e397dba09fe38fd8050)
- [uhc_device_caps::hs](../usb/P075_USB主机控制器能力.md#ab526337af28d25728780cb48dc43e722)
- [uhc_event::xfer](../usb/P076_USB主机控制器事件.md#a03f3cebee6edfaf620a98c198a70dbd0)
- [uhc_event::dev](../usb/P076_USB主机控制器事件.md#a055be3fd47e16bc48498163be3e55d09)
- [uhc_event::type](../usb/P076_USB主机控制器事件.md#a30fddbbe0f15a16320fba3cb4fd81d84)
- [uhc_event::status](../usb/P076_USB主机控制器事件.md#a5d7e1cc1bcb25e10f009ac3a8acd94b6)
- [uhc_event::node](../usb/P076_USB主机控制器事件.md#acd04587fac14f9a8a91b75642f5b2e82)
- [uhc_transfer::priv](../usb/P077_USB主机传输结构.md#a0f2d4a735ce224260d100dc756b1900f)
- [uhc_transfer::ref](../usb/P077_USB主机传输结构.md#a105b30625208c612b4abe857e208a7f1)
- [uhc_transfer::err](../usb/P077_USB主机传输结构.md#a11f002f91b1039c226b7c9feb8223e11)
- [uhc_transfer::buf](../usb/P077_USB主机传输结构.md#a170385b08171659f05ac7112faf8e587)
- [uhc_transfer::start_frame](../usb/P077_USB主机传输结构.md#a23e4115c774134ccd143189b0f4f2460)
- [uhc_transfer::no_status](../usb/P077_USB主机传输结构.md#a584f5713acc9c191a5a3f4ff7d77435c)
- [uhc_transfer::mps](../usb/P077_USB主机传输结构.md#a61a6c74cc7c026404ccf42d1164765b8)
- [uhc_transfer::udev](../usb/P077_USB主机传输结构.md#a81a8a80809420787f4c0ab232a24a514)
- [uhc_transfer::stage](../usb/P077_USB主机传输结构.md#a9983482be9724e281e56c978ce27d93f)
- [uhc_transfer::ep](../usb/P077_USB主机传输结构.md#aaf664844dc9f1871cce3d38516c042ef)
- [uhc_transfer::queued](../usb/P077_USB主机传输结构.md#ad2b246c850c3b30f7d2b58fc9a47008b)
- [uhc_transfer::cb](../usb/P077_USB主机传输结构.md#ad4d80a3f20cdec7dd2237a98054dd287)
- [uhc_transfer::type](../usb/P077_USB主机传输结构.md#ad4dbc766c6ded0ebfab7e36b19643b15)
- [uhc_transfer::node](../usb/P077_USB主机传输结构.md#ae1fcb0b866e3d7c5b5ea9dff6221f37d)
- [uhc_transfer::setup_pkt](../usb/P077_USB主机传输结构.md#ae681c0078b8afedd3b6fba165861e114)
- [uhc_transfer::interval](../usb/P077_USB主机传输结构.md#af6d6de482f092e4f85679722ad609cbf)
- [usb_device::node](../usb/P080_USB主机设备对象.md#a0215608e40123de4a3a79ca440c6c593)
- [usb_device::actual_cfg](../usb/P080_USB主机设备对象.md#a101d30facb781bd410581fc6c2d3fa59)
- [usb_device::speed](../usb/P080_USB主机设备对象.md#a1b3f4becfd9fbfae80074fc2e76ea6a8)
- [usb_device::dev_desc](../usb/P080_USB主机设备对象.md#a24be9609d416d3a184fdedbefa298490)
- [usb_device::mutex](../usb/P080_USB主机设备对象.md#a4203b2cfd65f70096a43a20c7c37de27)
- [usb_device::hub](../usb/P080_USB主机设备对象.md#a475090912a408eaa2f04d582a1367114)
- [usb_device::hub_port](../usb/P080_USB主机设备对象.md#a4a66403ece2f186d59ff29e39dc78839)
- [usb_device::ifaces](../usb/P080_USB主机设备对象.md#a5cccbb483d91032f4a7f25f88270747f)
- [usb_device::ep_out](../usb/P080_USB主机设备对象.md#a658b9992a472574b1d88e49b7fea478d)
- [usb_device::ctx](../usb/P080_USB主机设备对象.md#a72ee0e53efd86c91e0cea6c7e873d5ce)
- [usb_device::state](../usb/P080_USB主机设备对象.md#aa75bbea6a879460b39216453323d177f)
- [usb_device::addr](../usb/P080_USB主机设备对象.md#aa9062a5b9da663863e6d51ef2e04197b)
- [usb_device::cfg_desc](../usb/P080_USB主机设备对象.md#ac98af9fb0d5bba21bc8037a8fcfb3126)
- [usb_device::ep_in](../usb/P080_USB主机设备对象.md#ad3091acb2a713b9e66c595bbf4a736a5)
- [usb_device::level](../usb/P080_USB主机设备对象.md#ada9943f1917010381116cd778d6bc47c)
- [usb_device::tt](../usb/P080_USB主机设备对象.md#ae0c9c3454eea32432ddb4f8da7361182)
- [usb_host_ep::desc](../usb/P082_USB主机端点对象.md#a25e9c4004ab03927476093ed4d167dbd)
- [usb_host_interface::alternate](../usb/P081_USB主机接口对象.md#a4405cdfb6aa6fbbcd2ac27148b9ebea6)
- [usb_host_interface::iad](../usb/P081_USB主机接口对象.md#a8241bb80e15d8434802aad81ba0fc810)
- [usb_host_interface::dhp](../usb/P081_USB主机接口对象.md#aa0170523367f9e1459a9ba897c0d88bf)
- [usb_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/usb__buf_8h.html)
- [usb_ch9.h](../usb/P172_USB标准请求与描述符常量.md)

---

[上一章](P884_udc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P886_ump_stream_responder.h_源码浏览.md)
