---
id: learning.zephyr-docs.api-source-runtime-reference.page-67
title: wifi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_wifi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h.html)。

## 67.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00067"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="foldopen00146"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="foldopen00156"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="foldopen00176"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="foldopen00204"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="foldopen00214"></a>
<a id="l00214"></a>
<a id="l00218"></a>
<a id="l00222"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="foldopen00230"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="foldopen00238"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="foldopen00254"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="foldopen00277"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="foldopen00298"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00310"></a>
<a id="l00312"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="foldopen00323"></a>
<a id="l00323"></a>
<a id="l00325"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00341"></a>
<a id="l00343"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00362"></a>
<a id="l00364"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00371"></a>
<a id="l00373"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="foldopen00381"></a>
<a id="l00381"></a>
<a id="l00383"></a>
<a id="l00385"></a>
<a id="l00387"></a>
<a id="l00389"></a>
<a id="l00391"></a>
<a id="l00393"></a>
<a id="l00395"></a>
<a id="l00397"></a>
<a id="l00399"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
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
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="foldopen00429"></a>
<a id="l00429"></a>
<a id="l00431"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="l00437"></a>
<a id="l00439"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="foldopen00457"></a>
<a id="l00457"></a>
<a id="l00459"></a>
<a id="l00461"></a>
<a id="l00463"></a>
<a id="l00465"></a>
<a id="l00467"></a>
<a id="l00469"></a>
<a id="l00471"></a>
<a id="l00473"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="foldopen00488"></a>
<a id="l00488"></a>
<a id="l00490"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="foldopen00496"></a>
<a id="l00496"></a>
<a id="l00498"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="foldopen00507"></a>
<a id="l00507"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00521"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="foldopen00526"></a>
<a id="l00526"></a>
<a id="l00528"></a>
<a id="l00530"></a>
<a id="l00532"></a>
<a id="l00534"></a>
<a id="l00536"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="foldopen00542"></a>
<a id="l00542"></a>
<a id="l00544"></a>
<a id="l00546"></a>
<a id="l00548"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="foldopen00554"></a>
<a id="l00554"></a>
<a id="l00556"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="foldopen00565"></a>
<a id="l00565"></a>
<a id="l00567"></a>
<a id="l00569"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="foldopen00578"></a>
<a id="l00578"></a>
<a id="l00580"></a>
<a id="l00582"></a>
<a id="l00584"></a>
<a id="l00586"></a>
<a id="l00588"></a>
<a id="l00590"></a>
<a id="l00592"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="foldopen00601"></a>
<a id="l00601"></a>
<a id="l00603"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="foldopen00609"></a>
<a id="l00609"></a>
<a id="l00611"></a>
<a id="l00613"></a>
<a id="l00615"></a>
<a id="l00617"></a>
<a id="l00619"></a>
<a id="l00621"></a>
<a id="l00623"></a>
<a id="l00625"></a>
<a id="l00627"></a>
<a id="l00629"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="foldopen00635"></a>
<a id="l00635"></a>
<a id="l00637"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
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
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00664"></a>
<a id="foldopen00666"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="foldopen00676"></a>
<a id="l00676"></a>
<a id="l00678"></a>
<a id="l00680"></a>
<a id="l00682"></a>
<a id="l00684"></a>
<a id="l00686"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="foldopen00692"></a>
<a id="l00692"></a>
<a id="l00694"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="foldopen00705"></a>
<a id="l00705"></a>
<a id="l00710"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="foldopen00726"></a>
<a id="l00726"></a>
<a id="l00728"></a>
<a id="l00730"></a>
<a id="l00732"></a>
<a id="l00734"></a>
<a id="l00736"></a>
<a id="l00738"></a>
<a id="l00740"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00744"></a>
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
<a id="l00761"></a>
<a id="foldopen00765"></a>
<a id="l00765"></a>
<a id="l00767"></a>
<a id="l00769"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
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
<a id="foldopen00785"></a>
<a id="l00785"></a>
<a id="l00787"></a>
<a id="l00789"></a>
<a id="l00791"></a>
<a id="l00793"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="foldopen00799"></a>
<a id="l00799"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00814"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="agroup__wifi__mgmt_html_ga034bfcd7891caeb31820579b5ee22a7b"></a>
<a id="agroup__wifi__mgmt_html_ga03d306912dc96178e21d3c82c104582f"></a>
<a id="agroup__wifi__mgmt_html_ga0d9d6e2150fb187025300904357f7b4d"></a>
<a id="agroup__wifi__mgmt_html_ga0fffeb57b68fb8cdef9d3d571368b8ca"></a>
<a id="agroup__wifi__mgmt_html_ga1e2f0439a322355fa7368ea880c9c15d"></a>
<a id="agroup__wifi__mgmt_html_ga1f252da47d9650023d7fff6d08e49c76"></a>
<a id="agroup__wifi__mgmt_html_ga218525a9d9ee64524f983e52d5767562"></a>
<a id="agroup__wifi__mgmt_html_ga22354241197a9227fdba77e67d471f5c"></a>
<a id="agroup__wifi__mgmt_html_ga2d424d1711389fb784e916a87ff854b7"></a>
<a id="agroup__wifi__mgmt_html_ga31c78afc89bfdc4b54cee177843f8022"></a>
<a id="agroup__wifi__mgmt_html_ga3b01cead3c2eb4581fe85e2aaaffbd49"></a>
<a id="agroup__wifi__mgmt_html_ga44f875bf0d931b66d582f5dca2d65ed5"></a>
<a id="agroup__wifi__mgmt_html_ga48fea1f0c7d2700cef47068f96c6b71a"></a>
<a id="agroup__wifi__mgmt_html_ga4a9243eeb974111d6047fd3d8d9cbf35"></a>
<a id="agroup__wifi__mgmt_html_ga4d03aedac13ee4512d7717ac624f319a"></a>
<a id="agroup__wifi__mgmt_html_ga4fced9c3627d8f65d75e1651b11916b0"></a>
<a id="agroup__wifi__mgmt_html_ga584f6239ac14e2bedc5e6bd72756423b"></a>
<a id="agroup__wifi__mgmt_html_ga695123cd534e2499f516a07fdc5cafa8"></a>
<a id="agroup__wifi__mgmt_html_ga6a74e999d63ee491df68447219ef2a0d"></a>
<a id="agroup__wifi__mgmt_html_ga6fd645f891234136b3028574a0af9666"></a>
<a id="agroup__wifi__mgmt_html_ga7ef91a39c2cc6bb454d870a8a80f8439"></a>
<a id="agroup__wifi__mgmt_html_ga7f7b23ac019ca504a2006f0376735645"></a>
<a id="agroup__wifi__mgmt_html_ga7ff13294abf2dc27acbb3021afb2faee"></a>
<a id="agroup__wifi__mgmt_html_ga83546cf946a9123c563609e8903d9642"></a>
<a id="agroup__wifi__mgmt_html_ga86a5741e54aeb3e290142b0de217b8a8"></a>
<a id="agroup__wifi__mgmt_html_ga8b72e7989964963a25f42ed1dba240a0"></a>
<a id="agroup__wifi__mgmt_html_ga92b6fa6755491c3bd61f895213d07331"></a>
<a id="agroup__wifi__mgmt_html_ga97fa304f9a1db2294a93cccd4c93bcf6"></a>
<a id="agroup__wifi__mgmt_html_ga981961f747b919d61d3ccbd41e4508b4"></a>
<a id="agroup__wifi__mgmt_html_ga9bb9f658d7806e42b3ee351fb3e7dfa0"></a>
<a id="agroup__wifi__mgmt_html_gaa60495242c66a3fac294886856121c1f"></a>
<a id="agroup__wifi__mgmt_html_gab2e6a6e1d8358a8f34d67bd632709b3d"></a>
<a id="agroup__wifi__mgmt_html_gabdb2a784d4727b71ab44cca04e422c62"></a>
<a id="agroup__wifi__mgmt_html_gabe45d132797047c098041331c8f6f912"></a>
<a id="agroup__wifi__mgmt_html_gac18305e124523b7cc9eb6adb05d987a8"></a>
<a id="agroup__wifi__mgmt_html_gac7f907644847e905d67c709fa4afae7f"></a>
<a id="agroup__wifi__mgmt_html_gad0e998aeb1b27c4f203ca76339d323a3"></a>
<a id="agroup__wifi__mgmt_html_gad30e29eda65ccafdbd7f11865937b8ea"></a>
<a id="agroup__wifi__mgmt_html_gad3709d07aaa3ed59b48f9dd7bd181989"></a>
<a id="agroup__wifi__mgmt_html_gad78536ce1f30accfa45f258b6bf8c73d"></a>
<a id="agroup__wifi__mgmt_html_gad98099584d2222ede93aba42b1fbaff0"></a>
<a id="agroup__wifi__mgmt_html_gadb125925e851bf7569424cd4295e7712"></a>
<a id="agroup__wifi__mgmt_html_gadb21d49f64e04fba59433e51d5b3481c"></a>
<a id="agroup__wifi__mgmt_html_gadde31a04fa25ed805115c6b31854cd9c"></a>
<a id="agroup__wifi__mgmt_html_gae3ca047cc6ef6b6a2e44ba6574d41a44"></a>
<a id="agroup__wifi__mgmt_html_gaf67f2900be88fdf3f282400d09f2ab88"></a>
<a id="agroup__wifi__mgmt_html_gaf84d5e1a68393483fc6063c06b8f26e0"></a>
<a id="agroup__wifi__mgmt_html_gaf957fd93d98988347e009038cb694c04"></a>
<a id="agroup__wifi__mgmt_html_gafbeb5f7fa97fd2ba0c691da0f8853ef2"></a>
<a id="agroup__wifi__mgmt_html_gafc901312b5988481b34d05a031d6c0db"></a>
<a id="agroup__wifi__mgmt_html_gaffae7d2a754be5eb952ad2b83edad54c"></a>
<a id="agroup__wifi__mgmt_html_gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47"></a>
<a id="agroup__wifi__mgmt_html_gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82"></a>
<a id="agroup__wifi__mgmt_html_gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0"></a>
<a id="agroup__wifi__mgmt_html_gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11"></a>
<a id="agroup__wifi__mgmt_html_gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5"></a>
<a id="agroup__wifi__mgmt_html_gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895"></a>
<a id="agroup__wifi__mgmt_html_gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5"></a>
<a id="agroup__wifi__mgmt_html_gga1e2f0439a322355fa7368ea880c9c15daeb2366af7a35fa929882f7842abb4211"></a>
<a id="agroup__wifi__mgmt_html_gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969"></a>
<a id="agroup__wifi__mgmt_html_gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf"></a>
<a id="agroup__wifi__mgmt_html_gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840"></a>
<a id="agroup__wifi__mgmt_html_gga218525a9d9ee64524f983e52d5767562a38f97de2297f9df6e4ac3cecfd0799df"></a>
<a id="agroup__wifi__mgmt_html_gga218525a9d9ee64524f983e52d5767562ac5436dc7d2bbeded043b1102ee592e17"></a>
<a id="agroup__wifi__mgmt_html_gga218525a9d9ee64524f983e52d5767562ae44c04c2d1510385fe43827dbe6026f9"></a>
<a id="agroup__wifi__mgmt_html_gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832"></a>
<a id="agroup__wifi__mgmt_html_gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5"></a>
<a id="agroup__wifi__mgmt_html_gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e"></a>
<a id="agroup__wifi__mgmt_html_gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd"></a>
<a id="agroup__wifi__mgmt_html_gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1"></a>
<a id="agroup__wifi__mgmt_html_gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279"></a>
<a id="agroup__wifi__mgmt_html_gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3"></a>
<a id="agroup__wifi__mgmt_html_gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648"></a>
<a id="agroup__wifi__mgmt_html_gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565"></a>
<a id="agroup__wifi__mgmt_html_gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a"></a>
<a id="agroup__wifi__mgmt_html_gga3b01cead3c2eb4581fe85e2aaaffbd49a2c445a7a6345a66a41248bde2f7bf8cb"></a>
<a id="agroup__wifi__mgmt_html_gga3b01cead3c2eb4581fe85e2aaaffbd49a4e45ec9ffe32912a5673f9bbffeeef2d"></a>
<a id="agroup__wifi__mgmt_html_gga3b01cead3c2eb4581fe85e2aaaffbd49a7f78a7780a1059bf6fcedda5d96b5510"></a>
<a id="agroup__wifi__mgmt_html_gga3b01cead3c2eb4581fe85e2aaaffbd49a94c8cbcef66fc09604cf5e1a033c4bdc"></a>
<a id="agroup__wifi__mgmt_html_gga3b01cead3c2eb4581fe85e2aaaffbd49a9f984c246be1976cf1b799c4aed02ea1"></a>
<a id="agroup__wifi__mgmt_html_gga3b01cead3c2eb4581fe85e2aaaffbd49aa9036134a2d668f8e86e617628c4b134"></a>
<a id="agroup__wifi__mgmt_html_gga3b01cead3c2eb4581fe85e2aaaffbd49ada0acd85e6a825be12fe2295c960b93c"></a>
<a id="agroup__wifi__mgmt_html_gga3b01cead3c2eb4581fe85e2aaaffbd49ae5efe45d5211477322968e55014d22d5"></a>
<a id="agroup__wifi__mgmt_html_gga3b01cead3c2eb4581fe85e2aaaffbd49af57b996c36f950143c9f23a25d402b90"></a>
<a id="agroup__wifi__mgmt_html_gga48fea1f0c7d2700cef47068f96c6b71aa577671035478f3a385b8e4fdf6abf5fa"></a>
<a id="agroup__wifi__mgmt_html_gga48fea1f0c7d2700cef47068f96c6b71aa7c34eb5cf3e76c3c1b45c424436adbb1"></a>
<a id="agroup__wifi__mgmt_html_gga48fea1f0c7d2700cef47068f96c6b71aaec90b38cb8fb95ff3a679da473537589"></a>
<a id="agroup__wifi__mgmt_html_gga48fea1f0c7d2700cef47068f96c6b71aaf13490bee764dd77f770f07bf3dac3fa"></a>
<a id="agroup__wifi__mgmt_html_gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74"></a>
<a id="agroup__wifi__mgmt_html_gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7"></a>
<a id="agroup__wifi__mgmt_html_gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd"></a>
<a id="agroup__wifi__mgmt_html_gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623"></a>
<a id="agroup__wifi__mgmt_html_gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696"></a>
<a id="agroup__wifi__mgmt_html_gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56"></a>
<a id="agroup__wifi__mgmt_html_gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286"></a>
<a id="agroup__wifi__mgmt_html_gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72"></a>
<a id="agroup__wifi__mgmt_html_gga4fced9c3627d8f65d75e1651b11916b0a41376bed59184da60f7c6558d2524c58"></a>
<a id="agroup__wifi__mgmt_html_gga4fced9c3627d8f65d75e1651b11916b0a5491f6eabeae1cd0faec69b5ced04f49"></a>
<a id="agroup__wifi__mgmt_html_gga4fced9c3627d8f65d75e1651b11916b0a718e2d9c2f18fafc70c389177a4a5257"></a>
<a id="agroup__wifi__mgmt_html_gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8"></a>
<a id="agroup__wifi__mgmt_html_gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b"></a>
<a id="agroup__wifi__mgmt_html_gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889"></a>
<a id="agroup__wifi__mgmt_html_gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521"></a>
<a id="agroup__wifi__mgmt_html_gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813"></a>
<a id="agroup__wifi__mgmt_html_gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68"></a>
<a id="agroup__wifi__mgmt_html_gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa"></a>
<a id="agroup__wifi__mgmt_html_gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978"></a>
<a id="agroup__wifi__mgmt_html_gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0"></a>
<a id="agroup__wifi__mgmt_html_gga7ef91a39c2cc6bb454d870a8a80f8439ab8ef08f95a3b287c0a8be2e5ab0480c3"></a>
<a id="agroup__wifi__mgmt_html_gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4"></a>
<a id="agroup__wifi__mgmt_html_gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d"></a>
<a id="agroup__wifi__mgmt_html_gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1"></a>
<a id="agroup__wifi__mgmt_html_gga83546cf946a9123c563609e8903d9642a1c9f37033909236e6a2259465dda4ef7"></a>
<a id="agroup__wifi__mgmt_html_gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c"></a>
<a id="agroup__wifi__mgmt_html_gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958"></a>
<a id="agroup__wifi__mgmt_html_gga83546cf946a9123c563609e8903d9642ac22e71c91a433674f0a96ec853539902"></a>
<a id="agroup__wifi__mgmt_html_gga83546cf946a9123c563609e8903d9642ac357562788ce489023e9e66296401199"></a>
<a id="agroup__wifi__mgmt_html_gga86a5741e54aeb3e290142b0de217b8a8a008abc5c55c4ea7409f5b16be4f68a91"></a>
<a id="agroup__wifi__mgmt_html_gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4"></a>
<a id="agroup__wifi__mgmt_html_gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd"></a>
<a id="agroup__wifi__mgmt_html_gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8"></a>
<a id="agroup__wifi__mgmt_html_gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44"></a>
<a id="agroup__wifi__mgmt_html_gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563"></a>
<a id="agroup__wifi__mgmt_html_gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18"></a>
<a id="agroup__wifi__mgmt_html_gga86a5741e54aeb3e290142b0de217b8a8aeaccd303a2c836347555886f746b54eb"></a>
<a id="agroup__wifi__mgmt_html_gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f"></a>
<a id="agroup__wifi__mgmt_html_gga92b6fa6755491c3bd61f895213d07331a35fce37fccb3d27596c4e0a531109dac"></a>
<a id="agroup__wifi__mgmt_html_gga92b6fa6755491c3bd61f895213d07331a37f7681b1fb5d7165010ec941018882f"></a>
<a id="agroup__wifi__mgmt_html_gga92b6fa6755491c3bd61f895213d07331a39edcc7a267ce608a1e818948b5d172b"></a>
<a id="agroup__wifi__mgmt_html_gga92b6fa6755491c3bd61f895213d07331a505b4b888231dd1fbc169d612d8f0c38"></a>
<a id="agroup__wifi__mgmt_html_gga92b6fa6755491c3bd61f895213d07331a64daad77662868322e638da6531a5c0f"></a>
<a id="agroup__wifi__mgmt_html_gga92b6fa6755491c3bd61f895213d07331a8e619153aa3dad398c6ced36605f5e3f"></a>
<a id="agroup__wifi__mgmt_html_gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee"></a>
<a id="agroup__wifi__mgmt_html_gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6"></a>
<a id="agroup__wifi__mgmt_html_gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556"></a>
<a id="agroup__wifi__mgmt_html_gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d"></a>
<a id="agroup__wifi__mgmt_html_gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef"></a>
<a id="agroup__wifi__mgmt_html_gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860"></a>
<a id="agroup__wifi__mgmt_html_gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831"></a>
<a id="agroup__wifi__mgmt_html_gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7"></a>
<a id="agroup__wifi__mgmt_html_gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce"></a>
<a id="agroup__wifi__mgmt_html_gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13"></a>
<a id="agroup__wifi__mgmt_html_gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c"></a>
<a id="agroup__wifi__mgmt_html_gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f"></a>
<a id="agroup__wifi__mgmt_html_gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e"></a>
<a id="agroup__wifi__mgmt_html_gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c"></a>
<a id="agroup__wifi__mgmt_html_gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969"></a>
<a id="agroup__wifi__mgmt_html_gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc"></a>
<a id="agroup__wifi__mgmt_html_gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b"></a>
<a id="agroup__wifi__mgmt_html_gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba"></a>
<a id="agroup__wifi__mgmt_html_gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f"></a>
<a id="agroup__wifi__mgmt_html_gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b"></a>
<a id="agroup__wifi__mgmt_html_gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598"></a>
<a id="agroup__wifi__mgmt_html_ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc"></a>
<a id="agroup__wifi__mgmt_html_ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b"></a>
<a id="agroup__wifi__mgmt_html_ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244"></a>
<a id="agroup__wifi__mgmt_html_ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de"></a>
<a id="agroup__wifi__mgmt_html_ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6"></a>
<a id="agroup__wifi__mgmt_html_ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824"></a>
<a id="agroup__wifi__mgmt_html_ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8"></a>
<a id="agroup__wifi__mgmt_html_ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934"></a>
<a id="agroup__wifi__mgmt_html_ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2"></a>
<a id="agroup__wifi__mgmt_html_ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9"></a>
<a id="agroup__wifi__mgmt_html_ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe"></a>
<a id="agroup__wifi__mgmt_html_ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c"></a>
<a id="agroup__wifi__mgmt_html_ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362"></a>
<a id="agroup__wifi__mgmt_html_ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90"></a>
<a id="agroup__wifi__mgmt_html_ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d"></a>
<a id="agroup__wifi__mgmt_html_ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03"></a>
<a id="agroup__wifi__mgmt_html_ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8"></a>
<a id="agroup__wifi__mgmt_html_ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab"></a>
<a id="agroup__wifi__mgmt_html_ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29"></a>
<a id="agroup__wifi__mgmt_html_ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30"></a>
<a id="agroup__wifi__mgmt_html_ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6"></a>
<a id="agroup__wifi__mgmt_html_ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45"></a>
<a id="agroup__wifi__mgmt_html_ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f"></a>
<a id="agroup__wifi__mgmt_html_ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9"></a>
<a id="agroup__wifi__mgmt_html_ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f"></a>
<a id="agroup__wifi__mgmt_html_ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965"></a>
<a id="agroup__wifi__mgmt_html_ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d"></a>
<a id="agroup__wifi__mgmt_html_ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3"></a>
<a id="agroup__wifi__mgmt_html_ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38"></a>
<a id="agroup__wifi__mgmt_html_ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394"></a>
<a id="agroup__wifi__mgmt_html_ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a"></a>
<a id="agroup__wifi__mgmt_html_ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f"></a>
<a id="agroup__wifi__mgmt_html_ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce"></a>
<a id="agroup__wifi__mgmt_html_ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093"></a>
<a id="agroup__wifi__mgmt_html_ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca0c9db910757c5a715a5e88089362fab5"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca1b6d3f896a853bd9c1f03409f0f32814"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca1e45d14be678d0693b3f03f73fc5b0df"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca3a20bf15c1e51313629789e6abe0273d"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca3a91d5c899e0789587a94ab5981d98ca"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca42e49ccccfed285d32aa9f36bcfd5fc5"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca4beacdae98f8ca155609d2fd660c5ed0"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca52aa23f908a4fae0864f2e187b89af93"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca64221ce0052ce510e16537a32c67bb02"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca6cf0bd5db90deaa6b35f7afe122e8b5f"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca6d2e5f72b8bf76f093ab79be2a4b9477"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca798e97bb232dfa2bc75b5e6865d78bf7"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9ca85bcce61e75c01eb95083523e8925a40"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9caaa1dbea0100af80ca48ad594cddb4212"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9caab329c818e10cbe98aac1f9c30849c91"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9cab7bcc9437586d4940126a2ae1efdb092"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9cace9ee870a64b87aa7f97a146bb61951f"></a>
<a id="agroup__wifi__mgmt_html_ggadde31a04fa25ed805115c6b31854cd9cadb96b16c24d4975e88f674b08cab7122"></a>
<a id="agroup__wifi__mgmt_html_ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8"></a>
<a id="agroup__wifi__mgmt_html_ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70"></a>
<a id="agroup__wifi__mgmt_html_ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096"></a>
<a id="agroup__wifi__mgmt_html_ggafc901312b5988481b34d05a031d6c0dba0a0b1dd584525ee634069c81b91cb97f"></a>
<a id="agroup__wifi__mgmt_html_ggafc901312b5988481b34d05a031d6c0dba58f0ce2c50683011de9e36b55879e104"></a>
<a id="agroup__wifi__mgmt_html_ggafc901312b5988481b34d05a031d6c0dba8f89728c41b4aac1b803a558474c1484"></a>
<a id="agroup__wifi__mgmt_html_ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5"></a>
<a id="agroup__wifi__mgmt_html_ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructwifi__cipher__desc_html"></a>
<a id="astructwifi__cipher__desc_html_a6751019bb6da3032ca2f7bc42a3469e3"></a>
<a id="astructwifi__cipher__desc_html_a9396239f38613b151232a4c5f3d66a8f"></a>
<a id="astructwifi__eap__cipher__config_html"></a>
<a id="astructwifi__eap__cipher__config_html_a14128465917447f38d3854444a9bf6e1"></a>
<a id="astructwifi__eap__cipher__config_html_a385d365bb70a70fa09d321c55988afcc"></a>
<a id="astructwifi__eap__cipher__config_html_a3917f94dfafb22df260db9c4a129c3c4"></a>
<a id="astructwifi__eap__cipher__config_html_aa505ae934897742078aa46f1fdb5d0d1"></a>
<a id="astructwifi__eap__cipher__config_html_ab53f5b5419b2b8c8a869ba4f9d645a41"></a>
<a id="astructwifi__eap__cipher__config_html_ae9a4b8a0f0b47ac1065562ce287473a5"></a>
<a id="astructwifi__eap__config_html"></a>
<a id="astructwifi__eap__config_html_a031a5c86551f90130ff74ed53977c49d"></a>
<a id="astructwifi__eap__config_html_aa7a42a1256ef26562e83f47498d87113"></a>
<a id="astructwifi__eap__config_html_aaf73f2f986d56f95d196d02dcecbaff1"></a>
<a id="astructwifi__eap__config_html_ab44893426c89416ab24e3bfb57bf49ad"></a>
<a id="astructwifi__eap__config_html_abeed60cdf6c01751a4bb3c7ab67ea4e6"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2018 Texas Instruments, Incorporated
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */



#ifndef ZEPHYR_INCLUDE_NET_WIFI_H_
#define ZEPHYR_INCLUDE_NET_WIFI_H_

#include <zephyr/sys/util.h>  /* for ARRAY_SIZE */

#define WIFI_COUNTRY_CODE_LEN 2


#define WIFI_LISTEN_INTERVAL_MIN 0
#define WIFI_LISTEN_INTERVAL_MAX 65535


#ifdef __cplusplus
extern "C" {
#endif

enum wifi_conn_status {
        WIFI_STATUS_CONN_SUCCESS = 0,
        WIFI_STATUS_CONN_FAIL,
        WIFI_STATUS_CONN_WRONG_PASSWORD,
        WIFI_STATUS_CONN_TIMEOUT,
        WIFI_STATUS_CONN_AP_NOT_FOUND,
        WIFI_STATUS_CONN_AUTH_REJECT,
        WIFI_STATUS_CONN_ASSOC_REJECT,
        WIFI_STATUS_CONN_LAST_STATUS,
        WIFI_STATUS_DISCONN_FIRST_STATUS = WIFI_STATUS_CONN_LAST_STATUS,
};

enum wifi_security_type {
        WIFI_SECURITY_TYPE_NONE = 0,
        WIFI_SECURITY_TYPE_PSK,
        WIFI_SECURITY_TYPE_PSK_SHA256,
        WIFI_SECURITY_TYPE_SAE,
        WIFI_SECURITY_TYPE_SAE_HNP = WIFI_SECURITY_TYPE_SAE,
        WIFI_SECURITY_TYPE_SAE_H2E,
        WIFI_SECURITY_TYPE_SAE_AUTO,
        WIFI_SECURITY_TYPE_WAPI,
        WIFI_SECURITY_TYPE_EAP,
        WIFI_SECURITY_TYPE_EAP_TLS = WIFI_SECURITY_TYPE_EAP,
        WIFI_SECURITY_TYPE_WEP,
        WIFI_SECURITY_TYPE_WPA_PSK,
        WIFI_SECURITY_TYPE_WPA_AUTO_PERSONAL,
        WIFI_SECURITY_TYPE_DPP,
        WIFI_SECURITY_TYPE_EAP_PEAP_MSCHAPV2,
        WIFI_SECURITY_TYPE_EAP_PEAP_GTC,
        WIFI_SECURITY_TYPE_EAP_TTLS_MSCHAPV2,
        WIFI_SECURITY_TYPE_EAP_PEAP_TLS,
        WIFI_SECURITY_TYPE_FT_PSK,
        WIFI_SECURITY_TYPE_FT_SAE,
        WIFI_SECURITY_TYPE_FT_EAP,
        WIFI_SECURITY_TYPE_FT_EAP_SHA384,
        WIFI_SECURITY_TYPE_SAE_EXT_KEY,
        WIFI_SECURITY_TYPE_WEP_OPEN,
        WIFI_SECURITY_TYPE_WEP_SHARED,
        WIFI_SECURITY_TYPE_OWE,
        WIFI_SECURITY_TYPE_PSK_SHA384,
        WIFI_SECURITY_TYPE_FT_PSK_SHA384,

        __WIFI_SECURITY_TYPE_AFTER_LAST,
        WIFI_SECURITY_TYPE_MAX = WIFI_SECURITY_TYPE_FT_PSK_SHA384,
        WIFI_SECURITY_TYPE_UNKNOWN = __WIFI_SECURITY_TYPE_AFTER_LAST
};

enum wifi_wep_key_type {
        WIFI_WEP_KEY_TYPE_UNKNOWN = 0,
        WIFI_WEP_KEY_TYPE_64,
        WIFI_WEP_KEY_TYPE_128,
};

enum wifi_eap_type {
        WIFI_EAP_TYPE_NONE = 0,
        WIFI_EAP_TYPE_GTC = 6,
        WIFI_EAP_TYPE_TLS = 13,
        WIFI_EAP_TYPE_TTLS = 21,
        WIFI_EAP_TYPE_PEAP = 25,
        WIFI_EAP_TYPE_MSCHAPV2 = 26,
};

enum wifi_wpa3_enterprise_type {
        WIFI_WPA3_ENTERPRISE_NA = 0,
        WIFI_WPA3_ENTERPRISE_SUITEB = 1,
        WIFI_WPA3_ENTERPRISE_SUITEB_192,
        WIFI_WPA3_ENTERPRISE_ONLY,

        __WIFI_WPA3_ENTERPRISE_AFTER_LAST,
        WIFI_WPA3_ENTERPRISE_MAX = __WIFI_WPA3_ENTERPRISE_AFTER_LAST - 1,
        WIFI_WPA3_ENTERPRISE_UNKNOWN
};

enum wifi_eap_tls_cipher_type {
        WIFI_EAP_TLS_NONE,
        WIFI_EAP_TLS_ECC_P384,
        WIFI_EAP_TLS_RSA_3K,
};

enum wifi_cipher_type {
        WPA_CAPA_ENC_CCMP,
        WPA_CAPA_ENC_GCMP,
        WPA_CAPA_ENC_GCMP_256,
};

enum wifi_group_mgmt_cipher_type {
        WPA_CAPA_ENC_BIP,
        WPA_CAPA_ENC_BIP_GMAC_128,
        WPA_CAPA_ENC_BIP_GMAC_256,
};

struct wifi_cipher_desc {
        unsigned int capa;
        char *name;
};

struct wifi_eap_cipher_config {
        char *key_mgmt;
        char *openssl_ciphers;
        char *group_cipher;
        char *pairwise_cipher;
        char *group_mgmt_cipher;
        char *tls_flags;
};

struct wifi_eap_config {
        enum wifi_security_type type;
        enum wifi_eap_type eap_type_phase1;
        enum wifi_eap_type eap_type_phase2;
        char *method;
        char *phase2;
};

const char *wifi_security_txt(enum wifi_security_type security);

const char *wifi_wpa3_enterprise_txt(enum wifi_wpa3_enterprise_type wpa3_ent);

const char *wifi_wep_key_type_txt(enum wifi_wep_key_type wep_key_type);

enum wifi_mfp_options {
        WIFI_MFP_DISABLE = 0,
        WIFI_MFP_OPTIONAL,
        WIFI_MFP_REQUIRED,

        __WIFI_MFP_AFTER_LAST,
        WIFI_MFP_MAX = __WIFI_MFP_AFTER_LAST - 1,
        WIFI_MFP_UNKNOWN
};

const char *wifi_mfp_txt(enum wifi_mfp_options mfp);

enum wifi_frequency_bands {
        WIFI_FREQ_BAND_2_4_GHZ = 0,
        WIFI_FREQ_BAND_5_GHZ,
        WIFI_FREQ_BAND_6_GHZ,

        WIFI_FREQ_BAND_SUB_1_GHZ,

        __WIFI_FREQ_BAND_AFTER_LAST,
        WIFI_FREQ_BAND_MAX = __WIFI_FREQ_BAND_AFTER_LAST - 1,
        WIFI_FREQ_BAND_UNKNOWN
};

const char *wifi_band_txt(enum wifi_frequency_bands band);

enum wifi_frequency_bandwidths {
        WIFI_FREQ_BANDWIDTH_20MHZ = 1,
        WIFI_FREQ_BANDWIDTH_40MHZ,
        WIFI_FREQ_BANDWIDTH_80MHZ,

        WIFI_FREQ_BANDWIDTH_1MHZ,
        WIFI_FREQ_BANDWIDTH_2MHZ,
        WIFI_FREQ_BANDWIDTH_4MHZ,
        WIFI_FREQ_BANDWIDTH_8MHZ,

        __WIFI_FREQ_BANDWIDTH_AFTER_LAST,
        WIFI_FREQ_BANDWIDTH_MAX = __WIFI_FREQ_BANDWIDTH_AFTER_LAST - 1,
        WIFI_FREQ_BANDWIDTH_UNKNOWN
};

const char *wifi_bandwidth_txt(enum wifi_frequency_bandwidths bandwidth);

#define WIFI_SSID_MAX_LEN 32
#define WIFI_PSK_MIN_LEN 8
#define WIFI_PSK_MAX_LEN 64
#define WIFI_WEP_KEY_MAX_LEN 26
#define WIFI_PSK_PBKDF2_KEY_LEN 32
#define WIFI_SAE_PSWD_MAX_LEN 128
#define WIFI_MAC_ADDR_LEN 6
#define WIFI_ENT_IDENTITY_MAX_LEN 64
#define WIFI_ENT_PSWD_MAX_LEN 128

#define WIFI_CHANNEL_MIN 1
#define WIFI_CHANNEL_MAX 233
#define WIFI_CHANNEL_ANY 255

enum wifi_iface_state {
        WIFI_STATE_DISCONNECTED = 0,
        WIFI_STATE_INTERFACE_DISABLED,
        WIFI_STATE_INACTIVE,
        WIFI_STATE_SCANNING,
        WIFI_STATE_AUTHENTICATING,
        WIFI_STATE_ASSOCIATING,
        WIFI_STATE_ASSOCIATED,
        WIFI_STATE_4WAY_HANDSHAKE,
        WIFI_STATE_GROUP_HANDSHAKE,
        WIFI_STATE_COMPLETED,

        __WIFI_STATE_AFTER_LAST,
        WIFI_STATE_MAX = __WIFI_STATE_AFTER_LAST - 1,
        WIFI_STATE_UNKNOWN
};

/* We rely on the strict order of the enum values, so, let's check it */
BUILD_ASSERT(WIFI_STATE_DISCONNECTED < WIFI_STATE_INTERFACE_DISABLED &&
             WIFI_STATE_INTERFACE_DISABLED < WIFI_STATE_INACTIVE &&
             WIFI_STATE_INACTIVE < WIFI_STATE_SCANNING &&
             WIFI_STATE_SCANNING < WIFI_STATE_AUTHENTICATING &&
             WIFI_STATE_AUTHENTICATING < WIFI_STATE_ASSOCIATING &&
             WIFI_STATE_ASSOCIATING < WIFI_STATE_ASSOCIATED &&
             WIFI_STATE_ASSOCIATED < WIFI_STATE_4WAY_HANDSHAKE &&
             WIFI_STATE_4WAY_HANDSHAKE < WIFI_STATE_GROUP_HANDSHAKE &&
             WIFI_STATE_GROUP_HANDSHAKE < WIFI_STATE_COMPLETED);


const char *wifi_state_txt(enum wifi_iface_state state);

enum wifi_iface_mode {
        WIFI_MODE_INFRA = 0,
        WIFI_MODE_IBSS = 1,
        WIFI_MODE_AP = 2,
        WIFI_MODE_P2P_GO = 3,
        WIFI_MODE_P2P_GROUP_FORMATION = 4,
        WIFI_MODE_MESH = 5,

        __WIFI_MODE_AFTER_LAST,
        WIFI_MODE_MAX = __WIFI_MODE_AFTER_LAST - 1,
        WIFI_MODE_UNKNOWN
};

const char *wifi_mode_txt(enum wifi_iface_mode mode);

enum wifi_link_mode {
        WIFI_0 = 0,
        WIFI_1,
        WIFI_2,
        WIFI_3,
        WIFI_4,
        WIFI_5,
        WIFI_6,
        WIFI_6E,
        WIFI_7,

        __WIFI_LINK_MODE_AFTER_LAST,
        WIFI_LINK_MODE_MAX = __WIFI_LINK_MODE_AFTER_LAST - 1,
        WIFI_LINK_MODE_UNKNOWN
};

const char *wifi_link_mode_txt(enum wifi_link_mode link_mode);

enum wifi_scan_type {
        WIFI_SCAN_TYPE_ACTIVE = 0,
        WIFI_SCAN_TYPE_PASSIVE,
};

enum wifi_ps {
        WIFI_PS_DISABLED = 0,
        WIFI_PS_ENABLED,
};

const char *wifi_ps_txt(enum wifi_ps ps_name);

enum wifi_ps_mode {
        WIFI_PS_MODE_LEGACY = 0,
        /* This has to be configured before connecting to the AP,
         * as support for ADDTS action frames is not available.
         */
        WIFI_PS_MODE_WMM,
};

const char *wifi_ps_mode_txt(enum wifi_ps_mode ps_mode);

#define WIFI_INTERFACE_INDEX_MIN 1
#define WIFI_INTERFACE_INDEX_MAX 255

enum wifi_operational_modes {
        WIFI_STA_MODE = BIT(0),
        WIFI_MONITOR_MODE = BIT(1),
        WIFI_TX_INJECTION_MODE = BIT(2),
        WIFI_PROMISCUOUS_MODE = BIT(3),
        WIFI_AP_MODE = BIT(4),
        WIFI_SOFTAP_MODE = BIT(5),
};

enum wifi_filter {
        WIFI_PACKET_FILTER_ALL = BIT(0),
        WIFI_PACKET_FILTER_MGMT = BIT(1),
        WIFI_PACKET_FILTER_DATA = BIT(2),
        WIFI_PACKET_FILTER_CTRL = BIT(3),
};

enum wifi_twt_operation {
        WIFI_TWT_SETUP = 0,
        WIFI_TWT_TEARDOWN,
};

const char *wifi_twt_operation_txt(enum wifi_twt_operation twt_operation);

enum wifi_twt_negotiation_type {
        WIFI_TWT_INDIVIDUAL = 0,
        WIFI_TWT_BROADCAST,
        WIFI_TWT_WAKE_TBTT
};

const char *wifi_twt_negotiation_type_txt(enum wifi_twt_negotiation_type twt_negotiation);

enum wifi_twt_setup_cmd {
        WIFI_TWT_SETUP_CMD_REQUEST = 0,
        WIFI_TWT_SETUP_CMD_SUGGEST,
        WIFI_TWT_SETUP_CMD_DEMAND,
        WIFI_TWT_SETUP_CMD_GROUPING,
        WIFI_TWT_SETUP_CMD_ACCEPT,
        WIFI_TWT_SETUP_CMD_ALTERNATE,
        WIFI_TWT_SETUP_CMD_DICTATE,
        WIFI_TWT_SETUP_CMD_REJECT,
};

const char *wifi_twt_setup_cmd_txt(enum wifi_twt_setup_cmd twt_setup);

enum wifi_twt_setup_resp_status {
        WIFI_TWT_RESP_RECEIVED = 0,
        WIFI_TWT_RESP_NOT_RECEIVED,
};

enum wifi_twt_fail_reason {
        WIFI_TWT_FAIL_UNSPECIFIED,
        WIFI_TWT_FAIL_CMD_EXEC_FAIL,
        WIFI_TWT_FAIL_OPERATION_NOT_SUPPORTED,
        WIFI_TWT_FAIL_UNABLE_TO_GET_IFACE_STATUS,
        WIFI_TWT_FAIL_DEVICE_NOT_CONNECTED,
        WIFI_TWT_FAIL_PEER_NOT_HE_CAPAB,
        WIFI_TWT_FAIL_PEER_NOT_TWT_CAPAB,
        WIFI_TWT_FAIL_OPERATION_IN_PROGRESS,
        WIFI_TWT_FAIL_INVALID_FLOW_ID,
        WIFI_TWT_FAIL_IP_NOT_ASSIGNED,
        WIFI_TWT_FAIL_FLOW_ALREADY_EXISTS,
};

enum wifi_twt_teardown_status {
        WIFI_TWT_TEARDOWN_SUCCESS = 0,
        WIFI_TWT_TEARDOWN_FAILED,
};

static const char * const wifi_twt_err_code_tbl[] = {
        [WIFI_TWT_FAIL_UNSPECIFIED] = "Unspecified",
        [WIFI_TWT_FAIL_CMD_EXEC_FAIL] = "Command Execution failed",
        [WIFI_TWT_FAIL_OPERATION_NOT_SUPPORTED] =
                "Operation not supported",
        [WIFI_TWT_FAIL_UNABLE_TO_GET_IFACE_STATUS] =
                "Unable to get iface status",
        [WIFI_TWT_FAIL_DEVICE_NOT_CONNECTED] =
                "Device not connected",
        [WIFI_TWT_FAIL_PEER_NOT_HE_CAPAB] = "Peer not HE capable",
        [WIFI_TWT_FAIL_PEER_NOT_TWT_CAPAB] = "Peer not TWT capable",
        [WIFI_TWT_FAIL_OPERATION_IN_PROGRESS] =
                "Operation already in progress",
        [WIFI_TWT_FAIL_INVALID_FLOW_ID] =
                "Invalid negotiated flow id",
        [WIFI_TWT_FAIL_IP_NOT_ASSIGNED] =
                "IP address not assigned",
        [WIFI_TWT_FAIL_FLOW_ALREADY_EXISTS] =
                "Flow already exists",
};

static inline const char *wifi_twt_get_err_code_str(int16_t err_no)
{
        if ((err_no) < (int16_t)ARRAY_SIZE(wifi_twt_err_code_tbl)) {
                return wifi_twt_err_code_tbl[err_no];
        }

        return "<unknown>";
}

enum wifi_ps_param_type {
        WIFI_PS_PARAM_STATE,
        WIFI_PS_PARAM_LISTEN_INTERVAL,
        WIFI_PS_PARAM_WAKEUP_MODE,
        WIFI_PS_PARAM_MODE,
        WIFI_PS_PARAM_EXIT_STRATEGY,
        WIFI_PS_PARAM_TIMEOUT,
};

enum wifi_ps_wakeup_mode {
        WIFI_PS_WAKEUP_MODE_DTIM = 0,
        WIFI_PS_WAKEUP_MODE_LISTEN_INTERVAL,
};

const char *wifi_ps_wakeup_mode_txt(enum wifi_ps_wakeup_mode ps_wakeup_mode);

enum wifi_ps_exit_strategy {
        WIFI_PS_EXIT_CUSTOM_ALGO = 0,
        WIFI_PS_EXIT_EVERY_TIM,

        WIFI_PS_EXIT_LAST,
        WIFI_PS_EXIT_MAX = WIFI_PS_EXIT_LAST - 1,
};

const char *wifi_ps_exit_strategy_txt(enum wifi_ps_exit_strategy ps_exit_strategy);

enum wifi_config_ps_param_fail_reason {
        WIFI_PS_PARAM_FAIL_UNSPECIFIED,
        WIFI_PS_PARAM_FAIL_CMD_EXEC_FAIL,
        WIFI_PS_PARAM_FAIL_OPERATION_NOT_SUPPORTED,
        WIFI_PS_PARAM_FAIL_UNABLE_TO_GET_IFACE_STATUS,
        WIFI_PS_PARAM_FAIL_DEVICE_NOT_CONNECTED,
        WIFI_PS_PARAM_FAIL_DEVICE_CONNECTED,
        WIFI_PS_PARAM_LISTEN_INTERVAL_RANGE_INVALID,
        WIFI_PS_PARAM_FAIL_INVALID_EXIT_STRATEGY,
};

static const char * const wifi_ps_param_config_err_code_tbl[] = {
        [WIFI_PS_PARAM_FAIL_UNSPECIFIED] = "Unspecified",
        [WIFI_PS_PARAM_FAIL_CMD_EXEC_FAIL] = "Command Execution failed",
        [WIFI_PS_PARAM_FAIL_OPERATION_NOT_SUPPORTED] =
                "Operation not supported",
        [WIFI_PS_PARAM_FAIL_UNABLE_TO_GET_IFACE_STATUS] =
                "Unable to get iface status",
        [WIFI_PS_PARAM_FAIL_DEVICE_NOT_CONNECTED] =
                "Cannot set parameters while device not connected",
        [WIFI_PS_PARAM_FAIL_DEVICE_CONNECTED] =
                "Cannot set parameters while device connected",
        [WIFI_PS_PARAM_LISTEN_INTERVAL_RANGE_INVALID] =
                "Parameter out of range",
};

enum wifi_btm_query_reason {
        WIFI_BTM_QUERY_REASON_UNSPECIFIED = 0,
        WIFI_BTM_QUERY_REASON_LOW_RSSI = 16,
        WIFI_BTM_QUERY_REASON_LEAVING_ESS = 20,
};

static inline const char *wifi_ps_get_config_err_code_str(int16_t err_no)
{
        if ((err_no) < (int16_t)ARRAY_SIZE(wifi_ps_param_config_err_code_tbl)) {
                return wifi_ps_param_config_err_code_tbl[err_no];
        }

        return "<unknown>";
}

enum wifi_ap_config_param {
        WIFI_AP_CONFIG_PARAM_MAX_INACTIVITY = BIT(0),
        WIFI_AP_CONFIG_PARAM_MAX_NUM_STA = BIT(1),
        WIFI_AP_CONFIG_PARAM_BANDWIDTH = BIT(2),
        WIFI_AP_CONFIG_PARAM_HT_CAPAB = BIT(3),
        WIFI_AP_CONFIG_PARAM_VHT_CAPAB = BIT(4),
};

enum wifi_config_param {
        WIFI_CONFIG_PARAM_OKC = BIT(0),
};

const char *wifi_conn_status_txt(enum wifi_conn_status status);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_WIFI_H_ */
```

## 67.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Texas Instruments, Incorporated。

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 26 行

供 `ARRAY_SIZE` 使用。

### 注释 3：原第 410 行

此处依赖枚举值的严格顺序，因此需要检查这一顺序。

### 注释 4：原第 510 行

必须在连接接入点（AP）之前进行此配置，因为不支持 ADDTS 动作帧（Action frames）。

### 注释 5：原第 814 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_WIFI_H_`。

## 67.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [wifi_conn_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga86a5741e54aeb3e290142b0de217b8a8)
- [WIFI_STATUS_CONN_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd)
- [WIFI_STATUS_CONN_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44)
- [WIFI_STATUS_CONN_WRONG_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8)
- [WIFI_STATUS_CONN_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563)
- [WIFI_STATUS_CONN_AP_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4)
- [WIFI_STATUS_CONN_AUTH_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a008abc5c55c4ea7409f5b16be4f68a91)
- [WIFI_STATUS_CONN_ASSOC_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8aeaccd303a2c836347555886f746b54eb)
- [WIFI_STATUS_CONN_LAST_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f)
- [WIFI_STATUS_DISCONN_FIRST_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [WIFI_SECURITY_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e)
- [WIFI_SECURITY_TYPE_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368)
- [WIFI_SECURITY_TYPE_PSK_SHA256](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e)
- [WIFI_SECURITY_TYPE_SAE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f)
- [WIFI_SECURITY_TYPE_SAE_HNP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9caab329c818e10cbe98aac1f9c30849c91)
- [WIFI_SECURITY_TYPE_SAE_H2E](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca1e45d14be678d0693b3f03f73fc5b0df)
- [WIFI_SECURITY_TYPE_SAE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca4beacdae98f8ca155609d2fd660c5ed0)
- [WIFI_SECURITY_TYPE_WAPI](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d)
- [WIFI_SECURITY_TYPE_EAP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80)
- [WIFI_SECURITY_TYPE_EAP_TLS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca85bcce61e75c01eb95083523e8925a40)
- [WIFI_SECURITY_TYPE_WEP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724)
- [WIFI_SECURITY_TYPE_WPA_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a)
- [WIFI_SECURITY_TYPE_WPA_AUTO_PERSONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff)
- [WIFI_SECURITY_TYPE_DPP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca6cf0bd5db90deaa6b35f7afe122e8b5f)
- [WIFI_SECURITY_TYPE_EAP_PEAP_MSCHAPV2](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9caaa1dbea0100af80ca48ad594cddb4212)
- [WIFI_SECURITY_TYPE_EAP_PEAP_GTC](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca0c9db910757c5a715a5e88089362fab5)
- [WIFI_SECURITY_TYPE_EAP_TTLS_MSCHAPV2](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca3a20bf15c1e51313629789e6abe0273d)
- [WIFI_SECURITY_TYPE_EAP_PEAP_TLS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca6d2e5f72b8bf76f093ab79be2a4b9477)
- [WIFI_SECURITY_TYPE_FT_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca42e49ccccfed285d32aa9f36bcfd5fc5)
- [WIFI_SECURITY_TYPE_FT_SAE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9cab7bcc9437586d4940126a2ae1efdb092)
- [WIFI_SECURITY_TYPE_FT_EAP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5)
- [WIFI_SECURITY_TYPE_FT_EAP_SHA384](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca52aa23f908a4fae0864f2e187b89af93)
- [WIFI_SECURITY_TYPE_SAE_EXT_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca64221ce0052ce510e16537a32c67bb02)
- [WIFI_SECURITY_TYPE_WEP_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca798e97bb232dfa2bc75b5e6865d78bf7)
- [WIFI_SECURITY_TYPE_WEP_SHARED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9cadb96b16c24d4975e88f674b08cab7122)
- [WIFI_SECURITY_TYPE_OWE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca3a91d5c899e0789587a94ab5981d98ca)
- [WIFI_SECURITY_TYPE_PSK_SHA384](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca1b6d3f896a853bd9c1f03409f0f32814)
- [WIFI_SECURITY_TYPE_FT_PSK_SHA384](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9cace9ee870a64b87aa7f97a146bb61951f)
- [wifi_wep_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gafc901312b5988481b34d05a031d6c0db)
- [WIFI_WEP_KEY_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggafc901312b5988481b34d05a031d6c0dba58f0ce2c50683011de9e36b55879e104)
- [WIFI_WEP_KEY_TYPE_64](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggafc901312b5988481b34d05a031d6c0dba8f89728c41b4aac1b803a558474c1484)
- [WIFI_WEP_KEY_TYPE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggafc901312b5988481b34d05a031d6c0dba0a0b1dd584525ee634069c81b91cb97f)
- [wifi_eap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga92b6fa6755491c3bd61f895213d07331)
- [WIFI_EAP_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a39edcc7a267ce608a1e818948b5d172b)
- [WIFI_EAP_TYPE_GTC](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a64daad77662868322e638da6531a5c0f)
- [WIFI_EAP_TYPE_TLS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a505b4b888231dd1fbc169d612d8f0c38)
- [WIFI_EAP_TYPE_TTLS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a35fce37fccb3d27596c4e0a531109dac)
- [WIFI_EAP_TYPE_PEAP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a8e619153aa3dad398c6ced36605f5e3f)
- [WIFI_EAP_TYPE_MSCHAPV2](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a37f7681b1fb5d7165010ec941018882f)
- [wifi_wpa3_enterprise_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga48fea1f0c7d2700cef47068f96c6b71a)
- [WIFI_WPA3_ENTERPRISE_NA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga48fea1f0c7d2700cef47068f96c6b71aa7c34eb5cf3e76c3c1b45c424436adbb1)
- [WIFI_WPA3_ENTERPRISE_SUITEB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga48fea1f0c7d2700cef47068f96c6b71aaec90b38cb8fb95ff3a679da473537589)
- [WIFI_WPA3_ENTERPRISE_SUITEB_192](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga48fea1f0c7d2700cef47068f96c6b71aa577671035478f3a385b8e4fdf6abf5fa)
- [WIFI_WPA3_ENTERPRISE_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga48fea1f0c7d2700cef47068f96c6b71aaf13490bee764dd77f770f07bf3dac3fa)
- [wifi_eap_tls_cipher_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga218525a9d9ee64524f983e52d5767562)
- [WIFI_EAP_TLS_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga218525a9d9ee64524f983e52d5767562a38f97de2297f9df6e4ac3cecfd0799df)
- [WIFI_EAP_TLS_ECC_P384](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga218525a9d9ee64524f983e52d5767562ae44c04c2d1510385fe43827dbe6026f9)
- [WIFI_EAP_TLS_RSA_3K](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga218525a9d9ee64524f983e52d5767562ac5436dc7d2bbeded043b1102ee592e17)
- [wifi_cipher_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7f7b23ac019ca504a2006f0376735645)
- [WPA_CAPA_ENC_CCMP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1)
- [WPA_CAPA_ENC_GCMP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d)
- [WPA_CAPA_ENC_GCMP_256](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4)
- [wifi_group_mgmt_cipher_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf84d5e1a68393483fc6063c06b8f26e0)
- [WPA_CAPA_ENC_BIP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8)
- [WPA_CAPA_ENC_BIP_GMAC_128](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70)
- [WPA_CAPA_ENC_BIP_GMAC_256](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096)
- [wifi_cipher_desc](../network_core_model_reference/P165_wifi_cipher_desc_结构体.md)
- [capa](../network_core_model_reference/P165_wifi_cipher_desc_结构体.md#a6751019bb6da3032ca2f7bc42a3469e3)
- [name](../network_core_model_reference/P165_wifi_cipher_desc_结构体.md#a9396239f38613b151232a4c5f3d66a8f)
- [wifi_eap_cipher_config](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md)
- [key_mgmt](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md#a385d365bb70a70fa09d321c55988afcc)
- [openssl_ciphers](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md#a14128465917447f38d3854444a9bf6e1)
- [group_cipher](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md#aa505ae934897742078aa46f1fdb5d0d1)
- [pairwise_cipher](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md#a3917f94dfafb22df260db9c4a129c3c4)
- [group_mgmt_cipher](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md#ab53f5b5419b2b8c8a869ba4f9d645a41)
- [tls_flags](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md#ae9a4b8a0f0b47ac1065562ce287473a5)
- [wifi_eap_config](../network_core_model_reference/P172_wifi_eap_config_结构体.md)
- [type](../network_core_model_reference/P172_wifi_eap_config_结构体.md#a031a5c86551f90130ff74ed53977c49d)
- [eap_type_phase1](../network_core_model_reference/P172_wifi_eap_config_结构体.md#ab44893426c89416ab24e3bfb57bf49ad)
- [eap_type_phase2](../network_core_model_reference/P172_wifi_eap_config_结构体.md#aaf73f2f986d56f95d196d02dcecbaff1)
- [method](../network_core_model_reference/P172_wifi_eap_config_结构体.md#aa7a42a1256ef26562e83f47498d87113)
- [phase2](../network_core_model_reference/P172_wifi_eap_config_结构体.md#abeed60cdf6c01751a4bb3c7ab67ea4e6)
- [wifi_security_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9bb9f658d7806e42b3ee351fb3e7dfa0)
- [wifi_wpa3_enterprise_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf67f2900be88fdf3f282400d09f2ab88)
- [wifi_wep_key_type_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf957fd93d98988347e009038cb694c04)
- [wifi_mfp_options](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1f252da47d9650023d7fff6d08e49c76)
- [WIFI_MFP_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969)
- [WIFI_MFP_OPTIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf)
- [WIFI_MFP_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840)
- [wifi_mfp_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga22354241197a9227fdba77e67d471f5c)
- [wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)
- [WIFI_FREQ_BAND_2_4_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11)
- [WIFI_FREQ_BAND_5_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895)
- [WIFI_FREQ_BAND_6_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0)
- [WIFI_FREQ_BAND_SUB_1_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15daeb2366af7a35fa929882f7842abb4211)
- [WIFI_FREQ_BAND_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5)
- [WIFI_FREQ_BAND_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5)
- [wifi_band_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga44f875bf0d931b66d582f5dca2d65ed5)
- [wifi_frequency_bandwidths](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3b01cead3c2eb4581fe85e2aaaffbd49)
- [WIFI_FREQ_BANDWIDTH_20MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49ae5efe45d5211477322968e55014d22d5)
- [WIFI_FREQ_BANDWIDTH_40MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a9f984c246be1976cf1b799c4aed02ea1)
- [WIFI_FREQ_BANDWIDTH_80MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a2c445a7a6345a66a41248bde2f7bf8cb)
- [WIFI_FREQ_BANDWIDTH_1MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a94c8cbcef66fc09604cf5e1a033c4bdc)
- [WIFI_FREQ_BANDWIDTH_2MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49aa9036134a2d668f8e86e617628c4b134)
- [WIFI_FREQ_BANDWIDTH_4MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a7f78a7780a1059bf6fcedda5d96b5510)
- [WIFI_FREQ_BANDWIDTH_8MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49ada0acd85e6a825be12fe2295c960b93c)
- [WIFI_FREQ_BANDWIDTH_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49af57b996c36f950143c9f23a25d402b90)
- [WIFI_FREQ_BANDWIDTH_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a4e45ec9ffe32912a5673f9bbffeeef2d)
- [wifi_bandwidth_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7ff13294abf2dc27acbb3021afb2faee)
- [wifi_iface_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga981961f747b919d61d3ccbd41e4508b4)
- [WIFI_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f)
- [WIFI_STATE_INTERFACE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c)
- [WIFI_STATE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598)
- [WIFI_STATE_SCANNING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b)
- [WIFI_STATE_AUTHENTICATING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba)
- [WIFI_STATE_ASSOCIATING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b)
- [WIFI_STATE_ASSOCIATED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc)
- [WIFI_STATE_4WAY_HANDSHAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969)
- [WIFI_STATE_GROUP_HANDSHAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e)
- [WIFI_STATE_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f)
- [wifi_state_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga03d306912dc96178e21d3c82c104582f)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [wifi_iface_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga584f6239ac14e2bedc5e6bd72756423b)
- [WIFI_MODE_INFRA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813)
- [WIFI_MODE_IBSS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b)
- [WIFI_MODE_AP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8)
- [WIFI_MODE_P2P_GO](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889)
- [WIFI_MODE_P2P_GROUP_FORMATION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521)
- [WIFI_MODE_MESH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68)
- [wifi_mode_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad78536ce1f30accfa45f258b6bf8c73d)
- [wifi_link_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabdb2a784d4727b71ab44cca04e422c62)
- [WIFI_0](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8)
- [WIFI_1](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c)
- [WIFI_2](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9)
- [WIFI_3](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362)
- [WIFI_4](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2)
- [WIFI_5](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824)
- [WIFI_6](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe)
- [WIFI_6E](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6)
- [WIFI_7](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934)
- [wifi_link_mode_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0d9d6e2150fb187025300904357f7b4d)
- [wifi_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad30e29eda65ccafdbd7f11865937b8ea)
- [WIFI_SCAN_TYPE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9)
- [WIFI_SCAN_TYPE_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f)
- [wifi_ps](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0fffeb57b68fb8cdef9d3d571368b8ca)
- [WIFI_PS_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82)
- [WIFI_PS_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47)
- [wifi_ps_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gafbeb5f7fa97fd2ba0c691da0f8853ef2)
- [wifi_ps_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaffae7d2a754be5eb952ad2b83edad54c)
- [WIFI_PS_MODE_LEGACY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd)
- [WIFI_PS_MODE_WMM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5)
- [wifi_ps_mode_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadb21d49f64e04fba59433e51d5b3481c)
- [wifi_operational_modes](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4a9243eeb974111d6047fd3d8d9cbf35)
- [WIFI_STA_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [WIFI_MONITOR_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696)
- [WIFI_TX_INJECTION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74)
- [WIFI_PROMISCUOUS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56)
- [WIFI_AP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd)
- [WIFI_SOFTAP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623)
- [wifi_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa60495242c66a3fac294886856121c1f)
- [WIFI_PACKET_FILTER_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b)
- [WIFI_PACKET_FILTER_MGMT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc)
- [WIFI_PACKET_FILTER_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244)
- [WIFI_PACKET_FILTER_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de)
- [wifi_twt_operation](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad0e998aeb1b27c4f203ca76339d323a3)
- [WIFI_TWT_SETUP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45)
- [WIFI_TWT_TEARDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f)
- [wifi_twt_operation_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadb125925e851bf7569424cd4295e7712)
- [wifi_twt_negotiation_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga695123cd534e2499f516a07fdc5cafa8)
- [WIFI_TWT_INDIVIDUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0)
- [WIFI_TWT_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa)
- [WIFI_TWT_WAKE_TBTT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978)
- [wifi_twt_negotiation_type_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6a74e999d63ee491df68447219ef2a0d)
- [wifi_twt_setup_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga31c78afc89bfdc4b54cee177843f8022)
- [WIFI_TWT_SETUP_CMD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd)
- [WIFI_TWT_SETUP_CMD_SUGGEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648)
- [WIFI_TWT_SETUP_CMD_DEMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e)
- [WIFI_TWT_SETUP_CMD_GROUPING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279)
- [WIFI_TWT_SETUP_CMD_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a)
- [WIFI_TWT_SETUP_CMD_ALTERNATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1)
- [WIFI_TWT_SETUP_CMD_DICTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3)
- [WIFI_TWT_SETUP_CMD_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565)
- [wifi_twt_setup_cmd_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae3ca047cc6ef6b6a2e44ba6574d41a44)
- [wifi_twt_setup_resp_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4d03aedac13ee4512d7717ac624f319a)
- [WIFI_TWT_RESP_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286)
- [WIFI_TWT_RESP_NOT_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72)
- [wifi_twt_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga97fa304f9a1db2294a93cccd4c93bcf6)
- [WIFI_TWT_FAIL_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13)
- [WIFI_TWT_FAIL_CMD_EXEC_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556)
- [WIFI_TWT_FAIL_OPERATION_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d)
- [WIFI_TWT_FAIL_UNABLE_TO_GET_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef)
- [WIFI_TWT_FAIL_DEVICE_NOT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831)
- [WIFI_TWT_FAIL_PEER_NOT_HE_CAPAB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860)
- [WIFI_TWT_FAIL_PEER_NOT_TWT_CAPAB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce)
- [WIFI_TWT_FAIL_OPERATION_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7)
- [WIFI_TWT_FAIL_INVALID_FLOW_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6)
- [WIFI_TWT_FAIL_IP_NOT_ASSIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee)
- [WIFI_TWT_FAIL_FLOW_ALREADY_EXISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c)
- [wifi_twt_teardown_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad3709d07aaa3ed59b48f9dd7bd181989)
- [WIFI_TWT_TEARDOWN_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965)
- [WIFI_TWT_TEARDOWN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d)
- [wifi_twt_get_err_code_str](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gab2e6a6e1d8358a8f34d67bd632709b3d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)
- [wifi_ps_param_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabe45d132797047c098041331c8f6f912)
- [WIFI_PS_PARAM_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d)
- [WIFI_PS_PARAM_LISTEN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90)
- [WIFI_PS_PARAM_WAKEUP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8)
- [WIFI_PS_PARAM_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab)
- [WIFI_PS_PARAM_EXIT_STRATEGY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03)
- [WIFI_PS_PARAM_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29)
- [wifi_ps_wakeup_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac7f907644847e905d67c709fa4afae7f)
- [WIFI_PS_WAKEUP_MODE_DTIM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6)
- [WIFI_PS_WAKEUP_MODE_LISTEN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30)
- [wifi_ps_wakeup_mode_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6fd645f891234136b3028574a0af9666)
- [wifi_ps_exit_strategy](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2d424d1711389fb784e916a87ff854b7)
- [WIFI_PS_EXIT_CUSTOM_ALGO](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5)
- [WIFI_PS_EXIT_EVERY_TIM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832)
- [wifi_ps_exit_strategy_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga034bfcd7891caeb31820579b5ee22a7b)
- [wifi_config_ps_param_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad98099584d2222ede93aba42b1fbaff0)
- [WIFI_PS_PARAM_FAIL_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38)
- [WIFI_PS_PARAM_FAIL_CMD_EXEC_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394)
- [WIFI_PS_PARAM_FAIL_OPERATION_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093)
- [WIFI_PS_PARAM_FAIL_UNABLE_TO_GET_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3)
- [WIFI_PS_PARAM_FAIL_DEVICE_NOT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a)
- [WIFI_PS_PARAM_FAIL_DEVICE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486)
- [WIFI_PS_PARAM_LISTEN_INTERVAL_RANGE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f)
- [WIFI_PS_PARAM_FAIL_INVALID_EXIT_STRATEGY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce)
- [wifi_btm_query_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4fced9c3627d8f65d75e1651b11916b0)
- [WIFI_BTM_QUERY_REASON_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4fced9c3627d8f65d75e1651b11916b0a41376bed59184da60f7c6558d2524c58)
- [WIFI_BTM_QUERY_REASON_LOW_RSSI](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4fced9c3627d8f65d75e1651b11916b0a718e2d9c2f18fafc70c389177a4a5257)
- [WIFI_BTM_QUERY_REASON_LEAVING_ESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4fced9c3627d8f65d75e1651b11916b0a5491f6eabeae1cd0faec69b5ced04f49)
- [wifi_ps_get_config_err_code_str](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga8b72e7989964963a25f42ed1dba240a0)
- [wifi_ap_config_param](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga83546cf946a9123c563609e8903d9642)
- [WIFI_AP_CONFIG_PARAM_MAX_INACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c)
- [WIFI_AP_CONFIG_PARAM_MAX_NUM_STA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958)
- [WIFI_AP_CONFIG_PARAM_BANDWIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642a1c9f37033909236e6a2259465dda4ef7)
- [WIFI_AP_CONFIG_PARAM_HT_CAPAB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642ac357562788ce489023e9e66296401199)
- [WIFI_AP_CONFIG_PARAM_VHT_CAPAB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642ac22e71c91a433674f0a96ec853539902)
- [wifi_config_param](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7ef91a39c2cc6bb454d870a8a80f8439)
- [WIFI_CONFIG_PARAM_OKC](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga7ef91a39c2cc6bb454d870a8a80f8439ab8ef08f95a3b287c0a8be2e5ab0480c3)
- [wifi_conn_status_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac18305e124523b7cc9eb6adb05d987a8)
- [wifi_cipher_desc::capa](../network_core_model_reference/P165_wifi_cipher_desc_结构体.md#a6751019bb6da3032ca2f7bc42a3469e3)
- [wifi_cipher_desc::name](../network_core_model_reference/P165_wifi_cipher_desc_结构体.md#a9396239f38613b151232a4c5f3d66a8f)
- [wifi_eap_cipher_config::openssl_ciphers](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md#a14128465917447f38d3854444a9bf6e1)
- [wifi_eap_cipher_config::key_mgmt](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md#a385d365bb70a70fa09d321c55988afcc)
- [wifi_eap_cipher_config::pairwise_cipher](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md#a3917f94dfafb22df260db9c4a129c3c4)
- [wifi_eap_cipher_config::group_cipher](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md#aa505ae934897742078aa46f1fdb5d0d1)
- [wifi_eap_cipher_config::group_mgmt_cipher](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md#ab53f5b5419b2b8c8a869ba4f9d645a41)
- [wifi_eap_cipher_config::tls_flags](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md#ae9a4b8a0f0b47ac1065562ce287473a5)
- [wifi_eap_config::type](../network_core_model_reference/P172_wifi_eap_config_结构体.md#a031a5c86551f90130ff74ed53977c49d)
- [wifi_eap_config::method](../network_core_model_reference/P172_wifi_eap_config_结构体.md#aa7a42a1256ef26562e83f47498d87113)
- [wifi_eap_config::eap_type_phase2](../network_core_model_reference/P172_wifi_eap_config_结构体.md#aaf73f2f986d56f95d196d02dcecbaff1)
- [wifi_eap_config::eap_type_phase1](../network_core_model_reference/P172_wifi_eap_config_结构体.md#ab44893426c89416ab24e3bfb57bf49ad)
- [wifi_eap_config::phase2](../network_core_model_reference/P172_wifi_eap_config_结构体.md#abeed60cdf6c01751a4bb3c7ab67ea4e6)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P066_usb_buf.h_源码浏览.md) · [返回大纲](大纲.md)
