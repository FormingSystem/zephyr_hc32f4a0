---
id: learning.zephyr-docs.api-source-reference.page-183
title: video.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第183章\_video.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h.html)。

## 183.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
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
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="foldopen00087"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00107"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00148"></a>
<a id="l00153"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="foldopen00234"></a>
<a id="l00234"></a>
<a id="l00238"></a>
<a id="l00242"></a>
<a id="l00246"></a>
<a id="l00250"></a>
<a id="l00254"></a>
<a id="l00258"></a>
<a id="l00262"></a>
<a id="l00266"></a>
<a id="l00270"></a>
<a id="l00274"></a>
<a id="l00278"></a>
<a id="l00282"></a>
<a id="l00286"></a>
<a id="l00290"></a>
<a id="l00294"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00304"></a>
<a id="foldopen00317"></a>
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
<a id="foldopen00339"></a>
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
<a id="foldopen00362"></a>
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
<a id="foldopen00384"></a>
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
<a id="foldopen00410"></a>
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
<a id="foldopen00434"></a>
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
<a id="l00444"></a>
<a id="foldopen00458"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="foldopen00484"></a>
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
<a id="foldopen00507"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="foldopen00531"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="foldopen00554"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="foldopen00574"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="foldopen00600"></a>
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
<a id="foldopen00627"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="foldopen00655"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="foldopen00682"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00691"></a>
<a id="l00692"></a>
<a id="l00703"></a>
<a id="l00705"></a>
<a id="l00707"></a>
<a id="l00709"></a>
<a id="l00711"></a>
<a id="l00713"></a>
<a id="l00715"></a>
<a id="l00717"></a>
<a id="l00719"></a>
<a id="l00721"></a>
<a id="l00723"></a>
<a id="l00725"></a>
<a id="l00727"></a>
<a id="l00729"></a>
<a id="l00731"></a>
<a id="l00733"></a>
<a id="l00735"></a>
<a id="l00737"></a>
<a id="l00739"></a>
<a id="l00741"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="foldopen00758"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
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
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00820"></a>
<a id="l00821"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adlist_8h_html"></a>
<a id="agroup__doubly-linked-list__apis_html_ga57fdb936802a617d16c00ab08cd2ad98"></a>
<a id="agroup__doubly-linked-list__apis_html_gaa03f9557215b486fee1039dd4c07e683"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__video__formats_html_ga02d91ebf4b5150d5fa437bb3a7a6e872"></a>
<a id="agroup__video__formats_html_ga03e6be04b23b9735c96231eebc687158"></a>
<a id="agroup__video__formats_html_ga19d8dc905695229097dffe659f2a806e"></a>
<a id="agroup__video__formats_html_ga263e6553a77d00bc509c1b270efebb0b"></a>
<a id="agroup__video__formats_html_ga348c15cc77c728fdac773d58341cbc1d"></a>
<a id="agroup__video__formats_html_ga3751a8dce1c7459df06f83cd09449b5d"></a>
<a id="agroup__video__formats_html_ga502df4612995fc39e03d6de3ec675159"></a>
<a id="agroup__video__formats_html_ga604d2f3501407546aa924e2fdb37be2f"></a>
<a id="agroup__video__formats_html_ga66646a639518285810335a70337277d7"></a>
<a id="agroup__video__formats_html_ga89eb47d1dd60794781ee91cb5ae199ad"></a>
<a id="agroup__video__formats_html_gaa28c6306a3ed44a0e50c16e0eac86688"></a>
<a id="agroup__video__formats_html_gaa3af19adaf282b83a6c16f265a4260dc"></a>
<a id="agroup__video__formats_html_gaa9edb9c562fc3c86b61e071970fae60d"></a>
<a id="agroup__video__formats_html_gab5b5375f050d039e05032c77ac838b31"></a>
<a id="agroup__video__formats_html_gabc0205ce5c6426051fdec88d92f123e3"></a>
<a id="agroup__video__formats_html_gabf0dde810e75d37823891ed03811482c"></a>
<a id="agroup__video__formats_html_gac3413c36b3ce91e5658cd0f973c1f3d7"></a>
<a id="agroup__video__formats_html_gad69ab9041428488051bdb45f42ad4271"></a>
<a id="agroup__video__formats_html_gada0124aad9c10d403966b1e3851cd968"></a>
<a id="agroup__video__formats_html_gadca3ee56c798cf05b63cbfc87af98ce3"></a>
<a id="agroup__video__formats_html_gae06f742e31a62295d3ee16af8eec1b06"></a>
<a id="agroup__video__formats_html_gaecedece3398a6e2f62c20c2eb3f6d3c2"></a>
<a id="agroup__video__formats_html_gaf009d0eb7dbdb3bfd8883da03478c1ec"></a>
<a id="agroup__video__interface__backend_html_ga026c9a4531a125339e69b81f75343555"></a>
<a id="agroup__video__interface__backend_html_ga070cb5f5bf35b98e2e7dda3378114780"></a>
<a id="agroup__video__interface__backend_html_ga0a9e2ed76720f172b1b668e79220e968"></a>
<a id="agroup__video__interface__backend_html_ga4265087c8faf62bbc36e88c0587022a1"></a>
<a id="agroup__video__interface__backend_html_ga522b4027fc6f22bf59f4face3c97e303"></a>
<a id="agroup__video__interface__backend_html_ga964b301e45a42aa78799a1d9c9297ab1"></a>
<a id="agroup__video__interface__backend_html_ga990ba001531c7300a06ca02d64c31eaa"></a>
<a id="agroup__video__interface__backend_html_gab4d2eb34f8ccc95fa6dcda7848f4408a"></a>
<a id="agroup__video__interface__backend_html_gacda90bacb17a53e0bd11e5bfd37be57a"></a>
<a id="agroup__video__interface__backend_html_gad5aacb1386785a3587d41844c7854f83"></a>
<a id="agroup__video__interface__backend_html_gae6849a22140b3507bab219b579bc3d40"></a>
<a id="agroup__video__interface__backend_html_gaf63180944041a9e934c9f7567bdc1b88"></a>
<a id="agroup__video__interface__ctrls_html_gaf6e4edb13feb3bd422e19c438b435687"></a>
<a id="agroup__video__interface__ctrls_html_ggaf6e4edb13feb3bd422e19c438b435687a05a03f70b04c1ee7e05547cda9917950"></a>
<a id="agroup__video__interface__ctrls_html_ggaf6e4edb13feb3bd422e19c438b435687a06666e95282ce67b10a46ee8d32309a3"></a>
<a id="agroup__video__interface__ctrls_html_ggaf6e4edb13feb3bd422e19c438b435687a0a353803ba2af5f06c363b8d630e93bc"></a>
<a id="agroup__video__interface__ctrls_html_ggaf6e4edb13feb3bd422e19c438b435687a13da0d22cf3e12652424ca0d35f09071"></a>
<a id="agroup__video__interface__ctrls_html_ggaf6e4edb13feb3bd422e19c438b435687a7568dcc1abd061f4eaadd5f487523736"></a>
<a id="agroup__video__interface__ctrls_html_ggaf6e4edb13feb3bd422e19c438b435687ab2f378c2985335e39648fa200d9b7a13"></a>
<a id="agroup__video__interface_html_ga0d637375f7bf081967135139a8f6c5b6"></a>
<a id="agroup__video__interface_html_ga15d602806f0c30a1c28bcba7cf1fe82a"></a>
<a id="agroup__video__interface_html_ga18dac33c3f8afd80e08d69ed78aee5a9"></a>
<a id="agroup__video__interface_html_ga2037f560bb9a7a83d6cb23787d7bf167"></a>
<a id="agroup__video__interface_html_ga211f219e42890a6788b448c1c23fcd84"></a>
<a id="agroup__video__interface_html_ga224e26d848ff68d10452dd4d2a44fba5"></a>
<a id="agroup__video__interface_html_ga26d096ae93185ed1157a75d429dd145d"></a>
<a id="agroup__video__interface_html_ga2ad6b8870c5dca6a8d19b1f80d83b81b"></a>
<a id="agroup__video__interface_html_ga3d31ffde89ef76e72855ded34c6deb3c"></a>
<a id="agroup__video__interface_html_ga4eb2460636e70ddfa1b6f5187d882bfe"></a>
<a id="agroup__video__interface_html_ga57016218645ba4d98bab320545b80f1c"></a>
<a id="agroup__video__interface_html_ga59d6f35198b6412a9aa78c094ecfaa19"></a>
<a id="agroup__video__interface_html_ga64a52402a6883cb1b23a5524418528a9"></a>
<a id="agroup__video__interface_html_ga6d3881edac75ba2c12185dc119311945"></a>
<a id="agroup__video__interface_html_ga6f8b1924bf4a0ee1d7315a8e472614eb"></a>
<a id="agroup__video__interface_html_ga85a3064db275074f31494a364d17b51f"></a>
<a id="agroup__video__interface_html_ga8c19eb99330402975f6e6630e1b91436"></a>
<a id="agroup__video__interface_html_ga8ddced08604291df2eec55aadc3c217c"></a>
<a id="agroup__video__interface_html_ga9a29705addc34c59eb6406dd37519eaf"></a>
<a id="agroup__video__interface_html_gaaf4610cbab1caaf95070b7366cb4c4c6"></a>
<a id="agroup__video__interface_html_gabd3ca5bdb2915a78fd12182fde435c30"></a>
<a id="agroup__video__interface_html_gac50ea4ef6af09f0a6f72315db2ccd2d9"></a>
<a id="agroup__video__interface_html_gad5f04e5dd3d5e0c5f67c64e28cd91c56"></a>
<a id="agroup__video__interface_html_gadadb66f582b5e014336e29c1dafc3631"></a>
<a id="agroup__video__interface_html_gae73ac504f2d726ab9a88bc35e0e25b09"></a>
<a id="agroup__video__interface_html_gafc494071abdfb4c38dff515bda316379"></a>
<a id="agroup__video__types_html_gad386b2994b56844ebe713f156b9dfe4e"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructdevice_html"></a>
<a id="astructk__poll__signal_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructvideo__buffer_html"></a>
<a id="astructvideo__caps_html"></a>
<a id="astructvideo__ctrl__range_html"></a>
<a id="astructvideo__ctrl_html"></a>
<a id="astructvideo__ctrl_html_a027ae7809789cc010ec43cc4179428f9"></a>
<a id="astructvideo__ctrl_html_a3353754b98aac187d3e7305fed0b0d83"></a>
<a id="astructvideo__ctrl_html_a5130c8a873bcde98ec6722d1da7c238a"></a>
<a id="astructvideo__ctrl_html_a53aff4307d71d871064c9b7d26bba3e4"></a>
<a id="astructvideo__ctrl_html_a5e6741dde912d912a1c50048e96e274b"></a>
<a id="astructvideo__ctrl_html_a65ae06ab9371b2f9108d79a2f12ba1b9"></a>
<a id="astructvideo__ctrl_html_a77de7d9413b14fb33dc85232d14eaa5b"></a>
<a id="astructvideo__ctrl_html_a959eb36670223091c55743b8c3dfb288"></a>
<a id="astructvideo__ctrl_html_a96e406f3cf4bb48eec604ae9656b6206"></a>
<a id="astructvideo__ctrl_html_ac67db8a3797161a75389ced1d485375e"></a>
<a id="astructvideo__ctrl_html_ad3f25f434106a14be692a8846a21bf75"></a>
<a id="astructvideo__ctrl_html_ae0444d742950563cb13ae6cf4e0e5cd1"></a>
<a id="astructvideo__ctrl_html_ae62f16d3a3be845e512ba5e920f6c5d4"></a>
<a id="astructvideo__ctrl_html_ae85ae0efdd09df92416947515b0e395a"></a>
<a id="astructvideo__device_html"></a>
<a id="astructvideo__device_html_a1146fe8e0691c82d3d88ef5692dc215e"></a>
<a id="astructvideo__device_html_a55e683c881dc4d71f765af87050e73ee"></a>
<a id="astructvideo__device_html_acb7d3ba02fef218329a32e45466b11cb"></a>
<a id="astructvideo__driver__api_html"></a>
<a id="astructvideo__driver__api_html_a0d35d1501b91f9c6116cf38f85a342cc"></a>
<a id="astructvideo__driver__api_html_a1859e3a1db99d97c38ea24f2f9cd00be"></a>
<a id="astructvideo__driver__api_html_a41cd20fbb013bdb6b28d79822733695c"></a>
<a id="astructvideo__driver__api_html_a4762a3f103ca5999e3d3f790bb74af75"></a>
<a id="astructvideo__driver__api_html_a59dbaa93982c354c16d5de63c0d03ec2"></a>
<a id="astructvideo__driver__api_html_a6481a76f3f4d33629bbebb29ef9e8726"></a>
<a id="astructvideo__driver__api_html_a6ab4deb345d2138e63e0c6126eeb5078"></a>
<a id="astructvideo__driver__api_html_a6ad8559ae0c2f6dc102e26e3714ded5d"></a>
<a id="astructvideo__driver__api_html_a800a2e8aaf59fc3fbd4bd2caaaf40f51"></a>
<a id="astructvideo__driver__api_html_a8daefeec3cfc01de56f0168b32cdb640"></a>
<a id="astructvideo__driver__api_html_a963927cc38174c4703470df04ec73dc6"></a>
<a id="astructvideo__driver__api_html_a96ba1bb4b76c7efc445b3071ef3a05ef"></a>
<a id="astructvideo__driver__api_html_abddf2db6034d10f76ac90ed5974df788"></a>
<a id="astructvideo__driver__api_html_ac4b155a56c07bd8f7ecff9ec75dd0792"></a>
<a id="astructvideo__driver__api_html_adc08ef9eeeaac584c1b9ae5e6fb70c04"></a>
<a id="astructvideo__driver__api_html_af50329fd41db78f4c5a945f57a7c091e"></a>
<a id="astructvideo__format__cap_html"></a>
<a id="astructvideo__format_html"></a>
<a id="astructvideo__frmival__enum_html"></a>
<a id="astructvideo__frmival_html"></a>
<a id="astructvideo__selection_html"></a>
<a id="avideo_2video_8h_html"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited.
 * Copyright 2025 NXP
 * Copyright (c) 2025 STMicroelectronics
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_VIDEO_H
#define ZEPHYR_INCLUDE_DRIVERS_VIDEO_H


#include <stddef.h>
#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/dlist.h>
#include <zephyr/types.h>
#include <zephyr/video/video.h>

#ifdef __cplusplus
extern "C" {
#endif

struct video_device {
        const struct device *dev;
        const struct device *src_dev;
        sys_dlist_t ctrls;
};

struct video_device *video_find_vdev(const struct device *dev);


#define VIDEO_CTRL_FLAG_READ_ONLY  BIT(0)
#define VIDEO_CTRL_FLAG_WRITE_ONLY BIT(1)
#define VIDEO_CTRL_FLAG_VOLATILE   BIT(2)
#define VIDEO_CTRL_FLAG_INACTIVE   BIT(3)
#define VIDEO_CTRL_FLAG_UPDATE     BIT(4)

enum video_ctrl_type {
        VIDEO_CTRL_TYPE_BOOLEAN = 1,
        VIDEO_CTRL_TYPE_INTEGER = 2,
        VIDEO_CTRL_TYPE_INTEGER64 = 3,
        VIDEO_CTRL_TYPE_MENU = 4,
        VIDEO_CTRL_TYPE_STRING = 5,
        VIDEO_CTRL_TYPE_INTEGER_MENU = 6,
};

struct video_ctrl {
        struct video_ctrl *cluster;
        uint8_t cluster_sz;
        bool is_auto;
        bool has_volatiles;

        const struct video_device *vdev;
        uint32_t id;
        enum video_ctrl_type type;
        unsigned long flags;
        struct video_ctrl_range range;
        union {
                int32_t val;
                int64_t val64;
        };
        union {
                const char *const *menu;
                const int64_t *int_menu;
        };
        sys_dnode_t node;
};



typedef int (*video_api_format_t)(const struct device *dev, struct video_format *fmt);

typedef int (*video_api_frmival_t)(const struct device *dev, struct video_frmival *frmival);

typedef int (*video_api_enum_frmival_t)(const struct device *dev, struct video_frmival_enum *fie);

typedef int (*video_api_enqueue_t)(const struct device *dev, struct video_buffer *buf);

typedef int (*video_api_dequeue_t)(const struct device *dev, struct video_buffer **buf,
                                   k_timeout_t timeout);

typedef int (*video_api_flush_t)(const struct device *dev, bool cancel);

typedef int (*video_api_set_stream_t)(const struct device *dev, bool enable,
                                      enum video_buf_type type);

typedef int (*video_api_ctrl_t)(const struct device *dev, uint32_t cid);

typedef int (*video_api_get_caps_t)(const struct device *dev, struct video_caps *caps);

typedef int (*video_api_transform_cap_t)(const struct device *const dev,
                                         const struct video_format_cap *const cap,
                                         struct video_format_cap *const res_cap,
                                         enum video_buf_type type, uint16_t ind);

typedef int (*video_api_set_signal_t)(const struct device *dev, struct k_poll_signal *sig);

typedef int (*video_api_selection_t)(const struct device *dev, struct video_selection *sel);

__subsystem struct video_driver_api {
        video_api_format_t set_format;
        video_api_format_t get_format;
        video_api_set_stream_t set_stream;
        video_api_get_caps_t get_caps;
        video_api_enqueue_t enqueue;
        video_api_dequeue_t dequeue;
        video_api_flush_t flush;
        video_api_ctrl_t set_ctrl;
        video_api_ctrl_t get_volatile_ctrl;
        video_api_set_signal_t set_signal;
        video_api_frmival_t set_frmival;
        video_api_frmival_t get_frmival;
        video_api_enum_frmival_t enum_frmival;
        video_api_selection_t set_selection;
        video_api_selection_t get_selection;
        video_api_transform_cap_t transform_cap;
};


static inline int video_driver_set_format(const struct device *dev, struct video_format *fmt)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->set_format == NULL) {
                return -ENOSYS;
        }

        return api->set_format(dev, fmt);
}

static inline int video_driver_get_format(const struct device *dev, struct video_format *fmt)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->get_format == NULL) {
                return -ENOSYS;
        }

        return api->get_format(dev, fmt);
}

static inline int video_driver_set_frmival(const struct device *dev, struct video_frmival *frmival)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->set_frmival == NULL) {
                return -ENOSYS;
        }

        return api->set_frmival(dev, frmival);
}

static inline int video_driver_get_frmival(const struct device *dev, struct video_frmival *frmival)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->get_frmival == NULL) {
                return -ENOSYS;
        }

        return api->get_frmival(dev, frmival);
}

static inline int video_driver_enum_frmival(const struct device *dev,
                                            struct video_frmival_enum *fie)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->enum_frmival == NULL) {
                return -ENOSYS;
        }

        return api->enum_frmival(dev, fie);
}

static inline int video_driver_enqueue(const struct device *dev, struct video_buffer *vbuf)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->enqueue == NULL) {
                return -ENOSYS;
        }

        return api->enqueue(dev, vbuf);
}

static inline int video_driver_dequeue(const struct device *dev, struct video_buffer **vbuf,
                                       k_timeout_t timeout)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->dequeue == NULL) {
                return -ENOSYS;
        }

        return api->dequeue(dev, vbuf, timeout);
}

static inline int video_driver_flush(const struct device *dev, bool cancel)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->flush == NULL) {
                return -ENOSYS;
        }

        return api->flush(dev, cancel);
}

static inline int video_driver_set_stream(const struct device *dev, bool enable,
                                          enum video_buf_type type)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->set_stream == NULL) {
                return -ENOSYS;
        }

        return api->set_stream(dev, enable, type);
}

static inline int video_driver_get_volatile_ctrl(const struct device *dev, uint32_t cid)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->get_volatile_ctrl == NULL) {
                return -ENOSYS;
        }

        return api->get_volatile_ctrl(dev, cid);
}

static inline int video_driver_set_ctrl(const struct device *dev, uint32_t cid)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->set_ctrl == NULL) {
                return -ENOSYS;
        }

        return api->set_ctrl(dev, cid);
}

static inline int video_driver_get_caps(const struct device *dev, struct video_caps *caps)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->get_caps == NULL) {
                return -ENOSYS;
        }

        return api->get_caps(dev, caps);
}

static inline int video_driver_transform_cap(const struct device *const dev,
                                             const struct video_format_cap *const cap,
                                             struct video_format_cap *const res_cap,
                                             enum video_buf_type type, uint16_t ind)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->transform_cap == NULL) {
                return -ENOSYS;
        }

        return api->transform_cap(dev, cap, res_cap, type, ind);
}

static inline int video_driver_set_signal(const struct device *dev, struct k_poll_signal *sig)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->set_signal == NULL) {
                return -ENOSYS;
        }

        return api->set_signal(dev, sig);
}

static inline int video_driver_set_selection(const struct device *dev, struct video_selection *sel)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->set_selection == NULL) {
                return -ENOSYS;
        }

        return api->set_selection(dev, sel);
}

static inline int video_driver_get_selection(const struct device *dev, struct video_selection *sel)
{
        const struct video_driver_api *api = DEVICE_API_GET(video, dev);

        if (api->get_selection == NULL) {
                return -ENOSYS;
        }

        return api->get_selection(dev, sel);
}


#define VIDEO_MIPI_CSI2_DT_NULL                 0x10
#define VIDEO_MIPI_CSI2_DT_BLANKING             0x11
#define VIDEO_MIPI_CSI2_DT_EMBEDDED_8           0x12
#define VIDEO_MIPI_CSI2_DT_YUV420_8             0x18
#define VIDEO_MIPI_CSI2_DT_YUV420_10            0x19
#define VIDEO_MIPI_CSI2_DT_YUV420_CSPS_8        0x1c
#define VIDEO_MIPI_CSI2_DT_YUV420_CSPS_10       0x1d
#define VIDEO_MIPI_CSI2_DT_YUV422_8             0x1e
#define VIDEO_MIPI_CSI2_DT_YUV422_10            0x1f
#define VIDEO_MIPI_CSI2_DT_RGB444               0x20
#define VIDEO_MIPI_CSI2_DT_RGB555               0x21
#define VIDEO_MIPI_CSI2_DT_RGB565               0x22
#define VIDEO_MIPI_CSI2_DT_RGB666               0x23
#define VIDEO_MIPI_CSI2_DT_RGB888               0x24
#define VIDEO_MIPI_CSI2_DT_RAW6                 0x28
#define VIDEO_MIPI_CSI2_DT_RAW7                 0x29
#define VIDEO_MIPI_CSI2_DT_RAW8                 0x2a
#define VIDEO_MIPI_CSI2_DT_RAW10                0x2b
#define VIDEO_MIPI_CSI2_DT_RAW12                0x2c
#define VIDEO_MIPI_CSI2_DT_RAW14                0x2d

static inline uint8_t video_mipi_data_type(uint32_t pixfmt)
{
        switch (pixfmt) {
        case VIDEO_PIX_FMT_GREY:
        case VIDEO_PIX_FMT_SBGGR8:
        case VIDEO_PIX_FMT_SGBRG8:
        case VIDEO_PIX_FMT_SGRBG8:
        case VIDEO_PIX_FMT_SRGGB8:
                return VIDEO_MIPI_CSI2_DT_RAW8;
        case VIDEO_PIX_FMT_Y10P:
        case VIDEO_PIX_FMT_SBGGR10P:
        case VIDEO_PIX_FMT_SGBRG10P:
        case VIDEO_PIX_FMT_SGRBG10P:
        case VIDEO_PIX_FMT_SRGGB10P:
                return VIDEO_MIPI_CSI2_DT_RAW10;
        case VIDEO_PIX_FMT_Y12P:
        case VIDEO_PIX_FMT_SBGGR12P:
        case VIDEO_PIX_FMT_SGBRG12P:
        case VIDEO_PIX_FMT_SGRBG12P:
        case VIDEO_PIX_FMT_SRGGB12P:
                return VIDEO_MIPI_CSI2_DT_RAW12;
        case VIDEO_PIX_FMT_Y14P:
        case VIDEO_PIX_FMT_SBGGR14P:
        case VIDEO_PIX_FMT_SGBRG14P:
        case VIDEO_PIX_FMT_SGRBG14P:
        case VIDEO_PIX_FMT_SRGGB14P:
                return VIDEO_MIPI_CSI2_DT_RAW14;
        case VIDEO_PIX_FMT_UYVY:
                return VIDEO_MIPI_CSI2_DT_YUV422_8;
        case VIDEO_PIX_FMT_RGB565:
                return VIDEO_MIPI_CSI2_DT_RGB565;
        case VIDEO_PIX_FMT_RGB24:
                return VIDEO_MIPI_CSI2_DT_RGB888;
        default:
                return VIDEO_MIPI_CSI2_DT_NULL;
        }
}

#define VIDEO_MIPI_CSI2_DT_USER(n)      (0x30 + (n))


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_VIDEO_H */
```

## 183.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited.。

版权（Copyright）：2025 NXP。

版权（Copyright）：© 2025 STMicroelectronics。

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 821 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_VIDEO_H`。

## 183.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/video/video.h](https://docs.zephyrproject.org/latest/doxygen/html/video_2video_8h.html)
- [video_device](../audio_video_model_reference/P057_video_device_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../audio_video_model_reference/P057_video_device_结构体.md#a1146fe8e0691c82d3d88ef5692dc215e)
- [src_dev](../audio_video_model_reference/P057_video_device_结构体.md#a55e683c881dc4d71f765af87050e73ee)
- [sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)
- [ctrls](../audio_video_model_reference/P057_video_device_结构体.md#acb7d3ba02fef218329a32e45466b11cb)
- [video_find_vdev](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga3d31ffde89ef76e72855ded34c6deb3c)
- [video_ctrl_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html#gaf6e4edb13feb3bd422e19c438b435687)
- [VIDEO_CTRL_TYPE_BOOLEAN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html#ggaf6e4edb13feb3bd422e19c438b435687a7568dcc1abd061f4eaadd5f487523736)
- [VIDEO_CTRL_TYPE_INTEGER](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html#ggaf6e4edb13feb3bd422e19c438b435687a0a353803ba2af5f06c363b8d630e93bc)
- [VIDEO_CTRL_TYPE_INTEGER64](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html#ggaf6e4edb13feb3bd422e19c438b435687ab2f378c2985335e39648fa200d9b7a13)
- [VIDEO_CTRL_TYPE_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html#ggaf6e4edb13feb3bd422e19c438b435687a05a03f70b04c1ee7e05547cda9917950)
- [VIDEO_CTRL_TYPE_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html#ggaf6e4edb13feb3bd422e19c438b435687a06666e95282ce67b10a46ee8d32309a3)
- [VIDEO_CTRL_TYPE_INTEGER_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html#ggaf6e4edb13feb3bd422e19c438b435687a13da0d22cf3e12652424ca0d35f09071)
- [video_ctrl](../audio_video_model_reference/P054_video_ctrl_结构体.md)
- [cluster](../audio_video_model_reference/P054_video_ctrl_结构体.md#ae85ae0efdd09df92416947515b0e395a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cluster_sz](../audio_video_model_reference/P054_video_ctrl_结构体.md#a53aff4307d71d871064c9b7d26bba3e4)
- [is_auto](../audio_video_model_reference/P054_video_ctrl_结构体.md#a027ae7809789cc010ec43cc4179428f9)
- [has_volatiles](../audio_video_model_reference/P054_video_ctrl_结构体.md#ae0444d742950563cb13ae6cf4e0e5cd1)
- [vdev](../audio_video_model_reference/P054_video_ctrl_结构体.md#ad3f25f434106a14be692a8846a21bf75)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [id](../audio_video_model_reference/P054_video_ctrl_结构体.md#a65ae06ab9371b2f9108d79a2f12ba1b9)
- [type](../audio_video_model_reference/P054_video_ctrl_结构体.md#a3353754b98aac187d3e7305fed0b0d83)
- [flags](../audio_video_model_reference/P054_video_ctrl_结构体.md#a5130c8a873bcde98ec6722d1da7c238a)
- [video_ctrl_range](../audio_video_model_reference/P056_video_ctrl_range_结构体.md)
- [range](../audio_video_model_reference/P054_video_ctrl_结构体.md#a96e406f3cf4bb48eec604ae9656b6206)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [val](../audio_video_model_reference/P054_video_ctrl_结构体.md#a959eb36670223091c55743b8c3dfb288)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [val64](../audio_video_model_reference/P054_video_ctrl_结构体.md#a5e6741dde912d912a1c50048e96e274b)
- [menu](../audio_video_model_reference/P054_video_ctrl_结构体.md#a77de7d9413b14fb33dc85232d14eaa5b)
- [int_menu](../audio_video_model_reference/P054_video_ctrl_结构体.md#ac67db8a3797161a75389ced1d485375e)
- [sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)
- [node](../audio_video_model_reference/P054_video_ctrl_结构体.md#ae62f16d3a3be845e512ba5e920f6c5d4)
- [video_api_format_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga964b301e45a42aa78799a1d9c9297ab1)
- [video_format](../audio_video_model_reference/P059_video_format_结构体.md)
- [video_api_frmival_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gaf63180944041a9e934c9f7567bdc1b88)
- [video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)
- [video_api_enum_frmival_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga026c9a4531a125339e69b81f75343555)
- [video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)
- [video_api_enqueue_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gae6849a22140b3507bab219b579bc3d40)
- [video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)
- [video_api_dequeue_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga4265087c8faf62bbc36e88c0587022a1)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [video_api_flush_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga990ba001531c7300a06ca02d64c31eaa)
- [video_api_set_stream_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gacda90bacb17a53e0bd11e5bfd37be57a)
- [video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)
- [video_api_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga522b4027fc6f22bf59f4face3c97e303)
- [video_api_get_caps_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga070cb5f5bf35b98e2e7dda3378114780)
- [video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)
- [video_api_transform_cap_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga0a9e2ed76720f172b1b668e79220e968)
- [video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [video_api_set_signal_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gad5aacb1386785a3587d41844c7854f83)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [video_api_selection_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gab4d2eb34f8ccc95fa6dcda7848f4408a)
- [video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)
- [video_driver_api](../audio_video_model_reference/P058_video_driver_api_结构体.md)
- [set_format](../audio_video_model_reference/P058_video_driver_api_结构体.md#a1859e3a1db99d97c38ea24f2f9cd00be)
- [get_format](../audio_video_model_reference/P058_video_driver_api_结构体.md#a8daefeec3cfc01de56f0168b32cdb640)
- [set_stream](../audio_video_model_reference/P058_video_driver_api_结构体.md#adc08ef9eeeaac584c1b9ae5e6fb70c04)
- [get_caps](../audio_video_model_reference/P058_video_driver_api_结构体.md#a6ab4deb345d2138e63e0c6126eeb5078)
- [enqueue](../audio_video_model_reference/P058_video_driver_api_结构体.md#a4762a3f103ca5999e3d3f790bb74af75)
- [dequeue](../audio_video_model_reference/P058_video_driver_api_结构体.md#a96ba1bb4b76c7efc445b3071ef3a05ef)
- [flush](../audio_video_model_reference/P058_video_driver_api_结构体.md#a963927cc38174c4703470df04ec73dc6)
- [set_ctrl](../audio_video_model_reference/P058_video_driver_api_结构体.md#a41cd20fbb013bdb6b28d79822733695c)
- [get_volatile_ctrl](../audio_video_model_reference/P058_video_driver_api_结构体.md#af50329fd41db78f4c5a945f57a7c091e)
- [set_signal](../audio_video_model_reference/P058_video_driver_api_结构体.md#a59dbaa93982c354c16d5de63c0d03ec2)
- [set_frmival](../audio_video_model_reference/P058_video_driver_api_结构体.md#ac4b155a56c07bd8f7ecff9ec75dd0792)
- [get_frmival](../audio_video_model_reference/P058_video_driver_api_结构体.md#abddf2db6034d10f76ac90ed5974df788)
- [enum_frmival](../audio_video_model_reference/P058_video_driver_api_结构体.md#a6481a76f3f4d33629bbebb29ef9e8726)
- [set_selection](../audio_video_model_reference/P058_video_driver_api_结构体.md#a800a2e8aaf59fc3fbd4bd2caaaf40f51)
- [get_selection](../audio_video_model_reference/P058_video_driver_api_结构体.md#a6ad8559ae0c2f6dc102e26e3714ded5d)
- [transform_cap](../audio_video_model_reference/P058_video_driver_api_结构体.md#a0d35d1501b91f9c6116cf38f85a342cc)
- [video_driver_set_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga9a29705addc34c59eb6406dd37519eaf)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [video_driver_get_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gabd3ca5bdb2915a78fd12182fde435c30)
- [video_driver_set_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga57016218645ba4d98bab320545b80f1c)
- [video_driver_get_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga4eb2460636e70ddfa1b6f5187d882bfe)
- [video_driver_enum_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga26d096ae93185ed1157a75d429dd145d)
- [video_driver_enqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gae73ac504f2d726ab9a88bc35e0e25b09)
- [video_driver_dequeue](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gaaf4610cbab1caaf95070b7366cb4c4c6)
- [video_driver_flush](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga8ddced08604291df2eec55aadc3c217c)
- [video_driver_set_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga8c19eb99330402975f6e6630e1b91436)
- [video_driver_get_volatile_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga15d602806f0c30a1c28bcba7cf1fe82a)
- [video_driver_set_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga211f219e42890a6788b448c1c23fcd84)
- [video_driver_get_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga85a3064db275074f31494a364d17b51f)
- [video_driver_transform_cap](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga224e26d848ff68d10452dd4d2a44fba5)
- [video_driver_set_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga6f8b1924bf4a0ee1d7315a8e472614eb)
- [video_driver_set_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gafc494071abdfb4c38dff515bda316379)
- [video_driver_get_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga2037f560bb9a7a83d6cb23787d7bf167)
- [video_mipi_data_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gac50ea4ef6af09f0a6f72315db2ccd2d9)
- [VIDEO_PIX_FMT_GREY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa3af19adaf282b83a6c16f265a4260dc)
- [VIDEO_PIX_FMT_SBGGR8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabc0205ce5c6426051fdec88d92f123e3)
- [VIDEO_PIX_FMT_SGBRG8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa9edb9c562fc3c86b61e071970fae60d)
- [VIDEO_PIX_FMT_SGRBG8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga19d8dc905695229097dffe659f2a806e)
- [VIDEO_PIX_FMT_SRGGB8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabf0dde810e75d37823891ed03811482c)
- [VIDEO_MIPI_CSI2_DT_RAW8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga6d3881edac75ba2c12185dc119311945)
- [VIDEO_PIX_FMT_Y10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga502df4612995fc39e03d6de3ec675159)
- [VIDEO_PIX_FMT_SBGGR10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga3751a8dce1c7459df06f83cd09449b5d)
- [VIDEO_PIX_FMT_SGBRG10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gad69ab9041428488051bdb45f42ad4271)
- [VIDEO_PIX_FMT_SGRBG10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa28c6306a3ed44a0e50c16e0eac86688)
- [VIDEO_PIX_FMT_SRGGB10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga604d2f3501407546aa924e2fdb37be2f)
- [VIDEO_MIPI_CSI2_DT_RAW10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga64a52402a6883cb1b23a5524418528a9)
- [VIDEO_PIX_FMT_Y12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga263e6553a77d00bc509c1b270efebb0b)
- [VIDEO_PIX_FMT_SBGGR12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gab5b5375f050d039e05032c77ac838b31)
- [VIDEO_PIX_FMT_SGBRG12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaecedece3398a6e2f62c20c2eb3f6d3c2)
- [VIDEO_PIX_FMT_SGRBG12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga02d91ebf4b5150d5fa437bb3a7a6e872)
- [VIDEO_PIX_FMT_SRGGB12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga348c15cc77c728fdac773d58341cbc1d)
- [VIDEO_MIPI_CSI2_DT_RAW12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gadadb66f582b5e014336e29c1dafc3631)
- [VIDEO_PIX_FMT_Y14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gada0124aad9c10d403966b1e3851cd968)
- [VIDEO_PIX_FMT_SBGGR14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gac3413c36b3ce91e5658cd0f973c1f3d7)
- [VIDEO_PIX_FMT_SGBRG14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga89eb47d1dd60794781ee91cb5ae199ad)
- [VIDEO_PIX_FMT_SGRBG14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae06f742e31a62295d3ee16af8eec1b06)
- [VIDEO_PIX_FMT_SRGGB14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga66646a639518285810335a70337277d7)
- [VIDEO_MIPI_CSI2_DT_RAW14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga2ad6b8870c5dca6a8d19b1f80d83b81b)
- [VIDEO_PIX_FMT_UYVY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadca3ee56c798cf05b63cbfc87af98ce3)
- [VIDEO_MIPI_CSI2_DT_YUV422_8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga18dac33c3f8afd80e08d69ed78aee5a9)
- [VIDEO_PIX_FMT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf009d0eb7dbdb3bfd8883da03478c1ec)
- [VIDEO_MIPI_CSI2_DT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gad5f04e5dd3d5e0c5f67c64e28cd91c56)
- [VIDEO_PIX_FMT_RGB24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga03e6be04b23b9735c96231eebc687158)
- [VIDEO_MIPI_CSI2_DT_RGB888](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga0d637375f7bf081967135139a8f6c5b6)
- [VIDEO_MIPI_CSI2_DT_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga59d6f35198b6412a9aa78c094ecfaa19)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [video_ctrl::is_auto](../audio_video_model_reference/P054_video_ctrl_结构体.md#a027ae7809789cc010ec43cc4179428f9)
- [video_ctrl::type](../audio_video_model_reference/P054_video_ctrl_结构体.md#a3353754b98aac187d3e7305fed0b0d83)
- [video_ctrl::flags](../audio_video_model_reference/P054_video_ctrl_结构体.md#a5130c8a873bcde98ec6722d1da7c238a)
- [video_ctrl::cluster_sz](../audio_video_model_reference/P054_video_ctrl_结构体.md#a53aff4307d71d871064c9b7d26bba3e4)
- [video_ctrl::val64](../audio_video_model_reference/P054_video_ctrl_结构体.md#a5e6741dde912d912a1c50048e96e274b)
- [video_ctrl::id](../audio_video_model_reference/P054_video_ctrl_结构体.md#a65ae06ab9371b2f9108d79a2f12ba1b9)
- [video_ctrl::menu](../audio_video_model_reference/P054_video_ctrl_结构体.md#a77de7d9413b14fb33dc85232d14eaa5b)
- [video_ctrl::val](../audio_video_model_reference/P054_video_ctrl_结构体.md#a959eb36670223091c55743b8c3dfb288)
- [video_ctrl::range](../audio_video_model_reference/P054_video_ctrl_结构体.md#a96e406f3cf4bb48eec604ae9656b6206)
- [video_ctrl::int_menu](../audio_video_model_reference/P054_video_ctrl_结构体.md#ac67db8a3797161a75389ced1d485375e)
- [video_ctrl::vdev](../audio_video_model_reference/P054_video_ctrl_结构体.md#ad3f25f434106a14be692a8846a21bf75)
- [video_ctrl::has_volatiles](../audio_video_model_reference/P054_video_ctrl_结构体.md#ae0444d742950563cb13ae6cf4e0e5cd1)
- [video_ctrl::node](../audio_video_model_reference/P054_video_ctrl_结构体.md#ae62f16d3a3be845e512ba5e920f6c5d4)
- [video_ctrl::cluster](../audio_video_model_reference/P054_video_ctrl_结构体.md#ae85ae0efdd09df92416947515b0e395a)
- [video_device::dev](../audio_video_model_reference/P057_video_device_结构体.md#a1146fe8e0691c82d3d88ef5692dc215e)
- [video_device::src_dev](../audio_video_model_reference/P057_video_device_结构体.md#a55e683c881dc4d71f765af87050e73ee)
- [video_device::ctrls](../audio_video_model_reference/P057_video_device_结构体.md#acb7d3ba02fef218329a32e45466b11cb)
- [video_driver_api::transform_cap](../audio_video_model_reference/P058_video_driver_api_结构体.md#a0d35d1501b91f9c6116cf38f85a342cc)
- [video_driver_api::set_format](../audio_video_model_reference/P058_video_driver_api_结构体.md#a1859e3a1db99d97c38ea24f2f9cd00be)
- [video_driver_api::set_ctrl](../audio_video_model_reference/P058_video_driver_api_结构体.md#a41cd20fbb013bdb6b28d79822733695c)
- [video_driver_api::enqueue](../audio_video_model_reference/P058_video_driver_api_结构体.md#a4762a3f103ca5999e3d3f790bb74af75)
- [video_driver_api::set_signal](../audio_video_model_reference/P058_video_driver_api_结构体.md#a59dbaa93982c354c16d5de63c0d03ec2)
- [video_driver_api::enum_frmival](../audio_video_model_reference/P058_video_driver_api_结构体.md#a6481a76f3f4d33629bbebb29ef9e8726)
- [video_driver_api::get_caps](../audio_video_model_reference/P058_video_driver_api_结构体.md#a6ab4deb345d2138e63e0c6126eeb5078)
- [video_driver_api::get_selection](../audio_video_model_reference/P058_video_driver_api_结构体.md#a6ad8559ae0c2f6dc102e26e3714ded5d)
- [video_driver_api::set_selection](../audio_video_model_reference/P058_video_driver_api_结构体.md#a800a2e8aaf59fc3fbd4bd2caaaf40f51)
- [video_driver_api::get_format](../audio_video_model_reference/P058_video_driver_api_结构体.md#a8daefeec3cfc01de56f0168b32cdb640)
- [video_driver_api::flush](../audio_video_model_reference/P058_video_driver_api_结构体.md#a963927cc38174c4703470df04ec73dc6)
- [video_driver_api::dequeue](../audio_video_model_reference/P058_video_driver_api_结构体.md#a96ba1bb4b76c7efc445b3071ef3a05ef)
- [video_driver_api::get_frmival](../audio_video_model_reference/P058_video_driver_api_结构体.md#abddf2db6034d10f76ac90ed5974df788)
- [video_driver_api::set_frmival](../audio_video_model_reference/P058_video_driver_api_结构体.md#ac4b155a56c07bd8f7ecff9ec75dd0792)
- [video_driver_api::set_stream](../audio_video_model_reference/P058_video_driver_api_结构体.md#adc08ef9eeeaac584c1b9ae5e6fb70c04)
- [video_driver_api::get_volatile_ctrl](../audio_video_model_reference/P058_video_driver_api_结构体.md#af50329fd41db78f4c5a945f57a7c091e)
- [video.h](https://docs.zephyrproject.org/latest/doxygen/html/video_2video_8h.html)

---

[上一章](P182_tmp11x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P184_wuc.h_源码浏览.md)
