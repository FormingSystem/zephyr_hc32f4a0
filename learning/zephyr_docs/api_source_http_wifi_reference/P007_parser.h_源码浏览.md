---
id: learning.zephyr-docs.api-source-http-wifi-reference.page-7
title: parser.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/parser_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_parser.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md)。

## 7.1\_原始可见代码（Source Code）

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
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
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
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
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
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
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
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
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
<a id="foldopen00189"></a>
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
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
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
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
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
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="agroup__http__methods_html_gaacd5f203e33ac338ca5cb8f02a3ff3b8"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="amethod_8h_html"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a008e232118d6133c4dbdd9770d926694"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a18b873c41a1d7aa9ee9486f719aa7509"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a1b9ec4aeef6f168f9d711c27a0c6faa8"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a2406df24d500b1228fc5ef4a8d60e7c3"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a36842cc306c491da8c42023be68585e9"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a36cb81d8c40b00602b558f82a38eaecc"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a383ef24f0ac59de1c128ca776d813865"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a3e7c3b8a95f34bbd40ea047fcd43ffa5"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a4103809c185fee62b11c188ff0eab39a"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a5270cdc2f8af1802ccf3a2f33fde9307"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a5a1b7ae13c36ef37fd52b2b68112b501"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a5b44995fcd173cf38a88fc3ceaf0cb41"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a5d82bb467f93eed296d892408c44816a"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a5dc4b0888f48cd87fc3ded374ffac8a2"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a6391e880280eda55707145bda1170294"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a69ccadce5be8074b104b19aa74dce556"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a69e17a8b5a35b9f93ea914224c2d4f2a"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a7f92de0f01b2d0e37209854069183f16"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a7fbc6a25f20237b1cc795db489312e8e"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64a9adad03852eddb1f361abe9d856a1a0f"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64aa4a2007f1dc03bf22aff5ca8885f6b59"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64ab725a62450a5246e98fb5deeb0a250b5"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64abb98b653c0972e3e22bc5ff8b57d0d55"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64ac031cfd48285e22ddec18964f6281f6e"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64ac0348f1ca04bf4d882affcd0249336b5"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64aceed4040be7acf32b6bceb3aace8405e"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64ad92573bf62e7b0a13d398926a984fa9d"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64ade6f685cd47ad03c836aeee97efff1ed"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64adf532f653497f3085108a5e1f097aa8e"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64ae0f56ef0ecc6638fb0594d130a1ee490"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64ae15b73f73f8aad8c5e39d03b29414f9b"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64aed64f2a65634183e8f708ac80af3f6f2"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64af880c7a160717f01bba7bb98169c5011"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64af9f23325bd502239af0326a0b407b41d"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64afa80e3a0c0dd1c93cf0a11cacbd59079"></a>
<a id="aparser_8h_html_a1aab76595c275d0615cbea1cee1807c8"></a>
<a id="aparser_8h_html_a2559b4d373c7f0d85c77a2a3c308a5ee"></a>
<a id="aparser_8h_html_a5156a631a251516a6e78b17e1faadbb2"></a>
<a id="aparser_8h_html_a54f1346f15b326f6308a3ff7f0f75b52"></a>
<a id="aparser_8h_html_a76d2e1f7225617f6941042fc95d888fe"></a>
<a id="aparser_8h_html_a88adfab20d97366aac1fe05aa7dde7da"></a>
<a id="aparser_8h_html_a903c39c3abea292860780856ba90d560"></a>
<a id="aparser_8h_html_aa0f8424a6e7d3dd0b2f3b6358b57f1a1"></a>
<a id="aparser_8h_html_aa3764343ba4d2bb13fe39b05425633ba"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9a092619f8f7babc8fc3fa7533e78c3c29"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9a133e98dc07339e6c1605f32fc4fd6c78"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9a5c5e8921e5747d1128ad9611a6d4a782"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9a600ff486c803dcf2ec13453bdaf1100c"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9a9b2f205685c9ce94d3d73148de48decb"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9aa75b5b1dcec2decaa7386264d4e1dc29"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9ae71592851a69f477b80b1947399c1740"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9af0eea4f6920c6ff5c68cdd1f2e27d044"></a>
<a id="aparser_8h_html_ab8ae8e721c5c9f7309e94c174c72a940"></a>
<a id="aparser_8h_html_abb207665b6ff41700e5bbb260b580cb6"></a>
<a id="aparser_8h_html_acce1b9056442d75d4d609e797bcce2fd"></a>
<a id="aparser_8h_html_af9d6d304f8c255158175951b434cfa7a"></a>
<a id="aparser_8h_html_af9d6d304f8c255158175951b434cfa7aa132597b93208763e8e81c4a4a0e8a642"></a>
<a id="aparser_8h_html_af9d6d304f8c255158175951b434cfa7aa9f727b57e9e9c1651ee0df29aa1b1713"></a>
<a id="aparser_8h_html_af9d6d304f8c255158175951b434cfa7aadac18fbd072752213fd5308bb5fc8684"></a>
<a id="aparser__state_8h_html"></a>
<a id="aparser__url_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructhttp__content__range_html"></a>
<a id="astructhttp__content__range_html_a3c96329567d948ecc2f5be5febf48bf4"></a>
<a id="astructhttp__content__range_html_a4be2d7ae61240cc739ac14971946abfa"></a>
<a id="astructhttp__content__range_html_af32a14a0b8ae40722278c8839ab9429c"></a>
<a id="astructhttp__parser__settings_html"></a>
<a id="astructhttp__parser__settings_html_a2af4e9085fa79ee52b31e626179bc561"></a>
<a id="astructhttp__parser__settings_html_a497cf8f9d68e06e54684b71ee0f9f828"></a>
<a id="astructhttp__parser__settings_html_a6d0f0203f3461a8889ad471de119c993"></a>
<a id="astructhttp__parser__settings_html_a743b24c8f33e0f1cf60a96c824c42071"></a>
<a id="astructhttp__parser__settings_html_a9c24dfa900b49bf3439bbfba572b42fb"></a>
<a id="astructhttp__parser__settings_html_aaa145d7c24c91f471b2079ecb6368ae4"></a>
<a id="astructhttp__parser__settings_html_ac1c8453573094795ef41d4ba26e78846"></a>
<a id="astructhttp__parser__settings_html_ac44144daecc8e8adbd477b7e6a794e26"></a>
<a id="astructhttp__parser__settings_html_acfb3fd7947c5ff3e16649c71aa13bff2"></a>
<a id="astructhttp__parser__settings_html_afdd5beef93a4a7b32bc61ae088da64d2"></a>
<a id="astructhttp__parser_html"></a>
<a id="astructhttp__parser_html_a4cad8367f35e6739a9ffc45b851f49aa"></a>
<a id="astructhttp__parser_html_a5e54708e0cb3f9ced19bd829dcdeaf53"></a>
<a id="astructhttp__parser_html_a6f5952e0b47c83aeacf64fc287fd8003"></a>
<a id="astructhttp__parser_html_a6f7ba706f975f447b3bf72be97facdf8"></a>
<a id="astructhttp__parser_html_a748f476eacc5ac56b84dd07dbafb42a4"></a>
<a id="astructhttp__parser_html_a78085ca896bb3b9aa1ecb0f6fddc039d"></a>
<a id="astructhttp__parser_html_a7955de339fafd81ad54380845913457d"></a>
<a id="astructhttp__parser_html_a7e87ce57b97f60f1fdb7039a8ecb0bca"></a>
<a id="astructhttp__parser_html_a7fd5a194802b1206bb773e096d291f29"></a>
<a id="astructhttp__parser_html_a82f5aed92ca3566489def7bc384bab26"></a>
<a id="astructhttp__parser_html_ab8638d65fa174bc1925d77e2533117fa"></a>
<a id="astructhttp__parser_html_ac5b254b99c6472ca19ae1f426758ce75"></a>
<a id="astructhttp__parser_html_ac6c327558547d55eb64a8aea1310cc2e"></a>
<a id="astructhttp__parser_html_ac994a4a8268652f5ce82de5bde5c3f9d"></a>
<a id="astructhttp__parser_html_acd80a931fcc87d41999397af1662fc3c"></a>
<a id="astructhttp__parser_html_ade28251e8473212ad8b9b28dcd343c93"></a>
<a id="astructhttp__parser_html_ae8af6433c824f5348773842db62ad4ab"></a>
<a id="astructhttp__parser_html_af2c5cbcfbecce1cce001fe2531a6bd8c"></a>
<a id="astructnet__sockaddr_html"></a>

```c
/* SPDX-License-Identifier: MIT */

/* Copyright Joyent, Inc. and other Node contributors. All rights reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */
#ifndef ZEPHYR_INCLUDE_NET_HTTP_PARSER_H_
#define ZEPHYR_INCLUDE_NET_HTTP_PARSER_H_

/* Also update SONAME in the Makefile whenever you change these. */
#define HTTP_PARSER_VERSION_MAJOR 2
#define HTTP_PARSER_VERSION_MINOR 7
#define HTTP_PARSER_VERSION_PATCH 1

#include <sys/types.h>
#if defined(_WIN32) && !defined(__MINGW32__) && \
        (!defined(_MSC_VER) || _MSC_VER < 1600) && !defined(__WINE__)
#include <BaseTsd.h>
#include <stddef.h>
typedef __int8 int8_t;
typedef unsigned __int8 uint8_t;
typedef __int16 int16_t;
typedef unsigned __int16 uint16_t;
typedef __int32 int32_t;
typedef unsigned __int32 uint32_t;
typedef __int64 int64_t;
typedef unsigned __int64 uint64_t;
#else
#include <zephyr/types.h>
#include <stddef.h>
#endif
#include <zephyr/net/http/method.h>
#include <zephyr/net/http/parser_state.h>
#include <zephyr/net/http/parser_url.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

struct http_parser;
struct http_parser_settings;


/* Callbacks should return non-zero to indicate an error. The parser will
 * then halt execution.
 *
 * The one exception is on_headers_complete. In a HTTP_RESPONSE parser
 * returning '1' from on_headers_complete will tell the parser that it
 * should not expect a body. This is used when receiving a response to a
 * HEAD request which may contain 'Content-Length' or 'Transfer-Encoding:
 * chunked' headers that indicate the presence of a body.
 *
 * Returning `2` from on_headers_complete will tell parser that it should not
 * expect neither a body nor any further responses on this connection. This is
 * useful for handling responses to a CONNECT request which may not contain
 * `Upgrade` or `Connection: upgrade` headers.
 *
 * http_data_cb does not return data chunks. It will be called arbitrarily
 * many times for each string. E.G. you might get 10 callbacks for "on_url"
 * each providing just a few characters more data.
 */
typedef int (*http_data_cb)(struct http_parser *, const char *at,
                            size_t length);
typedef int (*http_cb)(struct http_parser *);

enum http_parser_type { HTTP_REQUEST, HTTP_RESPONSE, HTTP_BOTH };

/* Flag values for http_parser.flags field */
enum flags {
        F_CHUNKED               = 1 << 0,
        F_CONNECTION_KEEP_ALIVE = 1 << 1,
        F_CONNECTION_CLOSE      = 1 << 2,
        F_CONNECTION_UPGRADE    = 1 << 3,
        F_TRAILING              = 1 << 4,
        F_UPGRADE               = 1 << 5,
        F_SKIPBODY              = 1 << 6,
        F_CONTENTLENGTH         = 1 << 7
};

enum http_errno {
        HPE_OK,
        HPE_CB_message_begin,
        HPE_CB_url,
        HPE_CB_header_field,
        HPE_CB_header_value,
        HPE_CB_headers_complete,
        HPE_CB_body,
        HPE_CB_message_complete,
        HPE_CB_status,
        HPE_CB_chunk_header,
        HPE_CB_chunk_complete,
        HPE_INVALID_EOF_STATE,
        HPE_HEADER_OVERFLOW,
        HPE_CLOSED_CONNECTION,
        HPE_INVALID_VERSION,
        HPE_INVALID_STATUS,
        HPE_INVALID_METHOD,
        HPE_INVALID_URL,
        HPE_INVALID_HOST,
        HPE_INVALID_PORT,
        HPE_INVALID_PATH,
        HPE_INVALID_QUERY_STRING,
        HPE_INVALID_FRAGMENT,
        HPE_LF_EXPECTED,
        HPE_INVALID_HEADER_TOKEN,
        HPE_INVALID_CONTENT_LENGTH,
        HPE_UNEXPECTED_CONTENT_LENGTH,
        HPE_INVALID_CHUNK_SIZE,
        HPE_INVALID_CONTENT_RANGE,
        HPE_UNEXPECTED_CONTENT_RANGE,
        HPE_INVALID_CONSTANT,
        HPE_INVALID_INTERNAL_STATE,
        HPE_STRICT,
        HPE_PAUSED,
        HPE_UNKNOWN
};

/* Get an http_errno value from an http_parser */
#define HTTP_PARSER_ERRNO(p)            ((enum http_errno) (p)->http_errno)

struct http_content_range {
        uint64_t start;
        uint64_t end;
        uint64_t total;
};

struct http_parser {
        unsigned int type : 2;         /* enum http_parser_type */
        unsigned int flags : 8;         /* F_xxx values from 'flags' enum;
                                         * semi-public
                                         */
        unsigned int state : 7;        /* enum state from http_parser.c */
        unsigned int header_state : 7; /* enum header_state from http_parser.c
                                        */
        unsigned int index : 7;        /* index into current matcher */
        unsigned int lenient_http_headers : 1;

        uint32_t nread;          /* # bytes read in various scenarios */
        uint64_t content_length; /* # bytes in body (0 if no Content-Length
                                  * header)
                                  */
        bool content_range_present;
        struct http_content_range content_range;
        unsigned short http_major;
        unsigned short http_minor;
        unsigned int status_code : 16; /* responses only */
        unsigned int method : 8;       /* requests only */
        unsigned int http_errno : 7;

        /* 1 = Upgrade header was present and the parser has exited because of
         * that.
         * 0 = No upgrade header present.
         * Should be checked when http_parser_execute() returns in addition to
         * error checking.
         */
        unsigned int upgrade : 1;

        void *data; /* A pointer to get hook to the "connection" or "socket"
                     * object
                     */

        /* Remote socket address of http connection, where parser can initiate
         * replies if necessary.
         */
        const struct net_sockaddr *addr;
};


struct http_parser_settings {
        http_cb      on_message_begin;
        http_data_cb on_url;
        http_data_cb on_status;
        http_data_cb on_header_field;
        http_data_cb on_header_value;
        http_cb      on_headers_complete;
        http_data_cb on_body;
        http_cb      on_message_complete;
        /* When on_chunk_header is called, the current chunk length is stored
         * in parser->content_length.
         */
        http_cb      on_chunk_header;
        http_cb      on_chunk_complete;
};


/* Returns the library version. Bits 16-23 contain the major version number,
 * bits 8-15 the minor version number and bits 0-7 the patch level.
 * Usage example:
 *
 *   unsigned long version = http_parser_version();
 *   unsigned major = (version >> 16) & 255;
 *   unsigned minor = (version >> 8) & 255;
 *   unsigned patch = version & 255;
 *   printf("http_parser v%u.%u.%u\n", major, minor, patch);
 */
unsigned long http_parser_version(void);

void http_parser_init(struct http_parser *parser, enum http_parser_type type);


/* Initialize http_parser_settings members to 0
 */
void http_parser_settings_init(struct http_parser_settings *settings);


/* Executes the parser. Returns number of parsed bytes. Sets
 * `parser->http_errno` on error.
 */

size_t http_parser_execute(struct http_parser *parser,
                           const struct http_parser_settings *settings,
                           const char *data, size_t len);

/* If http_should_keep_alive() in the on_headers_complete or
 * on_message_complete callback returns 0, then this should be
 * the last message on the connection.
 * If you are the server, respond with the "Connection: close" header.
 * If you are the client, close the connection.
 */
int http_should_keep_alive(const struct http_parser *parser);

/* Returns a string version of the HTTP method. */
const char *http_method_str(enum http_method m);

/* Return a string name of the given error */
const char *http_errno_name(enum http_errno err);

/* Return a string description of the given error */
const char *http_errno_description(enum http_errno err);

/* Pause or un-pause the parser; a nonzero value pauses */
void http_parser_pause(struct http_parser *parser, int paused);

/* Checks if this is the final chunk of the body. */
int http_body_is_final(const struct http_parser *parser);

#ifdef __cplusplus
}
#endif
#endif
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`MIT`。

### 注释 2：原第 3 行

版权（Copyright）归 Joyent, Inc. 及其他 Node 贡献者所有。保留所有权利（All rights reserved）。

特此免费授予任何获得本软件及相关文档文件（以下称“软件”）副本的人不受限制地处理本软件的许可，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售本软件副本的权利，以及允许获提供本软件的人实施上述行为的权利，但须符合以下条件：

上述版权声明和本许可声明必须包含在本软件的所有副本或实质性部分中。

本软件按“原样”（AS IS）提供，不附带任何形式的明示或默示担保，包括但不限于适销性、特定用途适用性以及不侵权的担保。无论是基于合同、侵权或其他诉讼事由，作者或版权持有人均不对因本软件、使用本软件或对本软件进行其他处理而产生、引起或相关的任何索赔、损害或其他责任承担责任。

### 注释 3：原第 26 行

每次修改这些内容时，还要更新 Makefile 中的共享对象名称（SONAME）。

### 注释 4：原第 61 行

回调应以非零返回值表示错误，解析器（Parser）随后停止执行。

唯一例外是 `on_headers_complete`。在 `HTTP_RESPONSE` 解析器中，此回调返回 1 表示不应期待消息体（Body）。这用于处理 HEAD 请求的响应：该响应可能包含 `Content-Length` 或 `Transfer-Encoding: chunked` 头，看起来表示存在消息体。

`on_headers_complete` 返回 2，表示解析器既不应期待消息体，也不应期待该连接上有后续响应。这适合处理 CONNECT 请求的响应，因为响应可能不包含 `Upgrade` 或 `Connection: upgrade` 头。

`http_data_cb` 不返回数据分块（Data Chunks）。对于每个字符串，它可能被调用任意多次。例如 `on_url` 可能触发 10 次回调，每次仅多提供几个字符的数据。

### 注释 5：原第 85 行

`http_parser.flags` 字段的标志值（Flag Values）。

### 注释 6：原第 135 行

从 `http_parser` 获取 `http_errno` 值。

### 注释 7：原第 146 行

`enum http_parser_type` 枚举类型。

### 注释 8：原第 147 行

来自 `flags` 枚举的 `F_xxx` 值，属于半公开（Semi-public）内容。

### 注释 9：原第 150 行

来自 `http_parser.c` 的 `enum state` 枚举。

### 注释 10：原第 151 行

来自 `http_parser.c` 的 `enum header_state` 枚举。

### 注释 11：原第 153 行

当前匹配器（Matcher）中的索引。

### 注释 12：原第 156 行

各种情况下已读取的字节数。

### 注释 13：原第 157 行

消息体（Body）中的字节数；没有 `Content-Length` 头时为 0。

### 注释 14：原第 165 行

仅用于响应（Responses）。

### 注释 15：原第 166 行

仅用于请求（Requests）。

### 注释 16：原第 169 行

1 表示存在 `Upgrade` 头，且解析器因此退出；0 表示不存在升级头。在 `http_parser_execute()` 返回后，除检查错误外，还应检查此值。

### 注释 17：原第 178 行

用于关联连接（Connection）或套接字（Socket）对象的指针。

### 注释 18：原第 182 行

HTTP 连接的远端套接字地址（Remote Socket Address），解析器可在需要时向其发送响应。

### 注释 19：原第 198 行

调用 `on_chunk_header` 时，当前分块长度（Chunk Length）保存在 `parser->content_length` 中。

### 注释 20：原第 206 行

返回库版本（Library Version）。位 16–23 保存主版本号（Major），位 8–15 保存次版本号（Minor），位 0–7 保存补丁版本号（Patch）。使用示例如下。

```c
unsigned long version = http_parser_version();
unsigned major = (version >> 16) & 255;
unsigned minor = (version >> 8) & 255;
unsigned patch = version & 255;
printf("http_parser v%u.%u.%u\n", major, minor, patch);
```

### 注释 21：原第 221 行

将 `http_parser_settings` 各成员初始化为 0。

### 注释 22：原第 226 行

执行解析器（Parser），返回已解析的字节数；出错时设置 `parser->http_errno`。

### 注释 23：原第 234 行

若在 `on_headers_complete` 或 `on_message_complete` 回调中，`http_should_keep_alive()` 返回 0，则当前消息应是此连接上的最后一条消息。作为服务器时，应在响应中发送 `Connection: close` 头；作为客户端时，应关闭连接。

### 注释 24：原第 242 行

返回 HTTP 方法（Method）的字符串形式。

### 注释 25：原第 245 行

返回指定错误的字符串名称（Error Name）。

### 注释 26：原第 248 行

返回指定错误的字符串说明（Error Description）。

### 注释 27：原第 251 行

暂停或恢复解析器（Parser）；非零值表示暂停。

### 注释 28：原第 254 行

检查当前分块是否为消息体的最后一个分块（Final Chunk）。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md)
- [sys/types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/net/http/method.h](../api_file_supplement_reference/P065_zephyr__net__http__method.h_文件参考.md)
- [zephyr/net/http/parser_state.h](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md)
- [zephyr/net/http/parser_url.h](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [http_parser](../network_application_model_reference/P032_http_parser_结构体.md)
- [http_parser_settings](../network_application_model_reference/P033_http_parser_settings_结构体.md)
- [http_data_cb](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a1aab76595c275d0615cbea1cee1807c8)
- [http_cb](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1)
- [http_parser_type](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#af9d6d304f8c255158175951b434cfa7a)
- [HTTP_REQUEST](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#af9d6d304f8c255158175951b434cfa7aa9f727b57e9e9c1651ee0df29aa1b1713)
- [HTTP_RESPONSE](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#af9d6d304f8c255158175951b434cfa7aa132597b93208763e8e81c4a4a0e8a642)
- [HTTP_BOTH](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#af9d6d304f8c255158175951b434cfa7aadac18fbd072752213fd5308bb5fc8684)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [F_CHUNKED](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a092619f8f7babc8fc3fa7533e78c3c29)
- [F_CONNECTION_KEEP_ALIVE](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a5c5e8921e5747d1128ad9611a6d4a782)
- [F_CONNECTION_CLOSE](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a133e98dc07339e6c1605f32fc4fd6c78)
- [F_CONNECTION_UPGRADE](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9af0eea4f6920c6ff5c68cdd1f2e27d044)
- [F_TRAILING](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9aa75b5b1dcec2decaa7386264d4e1dc29)
- [F_UPGRADE](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a600ff486c803dcf2ec13453bdaf1100c)
- [F_SKIPBODY](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9ae71592851a69f477b80b1947399c1740)
- [F_CONTENTLENGTH](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a9b2f205685c9ce94d3d73148de48decb)
- [http_errno](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64)
- [HPE_OK](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64adf532f653497f3085108a5e1f097aa8e)
- [HPE_CB_message_begin](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a5b44995fcd173cf38a88fc3ceaf0cb41)
- [HPE_CB_url](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64ae15b73f73f8aad8c5e39d03b29414f9b)
- [HPE_CB_header_field](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64ade6f685cd47ad03c836aeee97efff1ed)
- [HPE_CB_header_value](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64aceed4040be7acf32b6bceb3aace8405e)
- [HPE_CB_headers_complete](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a5d82bb467f93eed296d892408c44816a)
- [HPE_CB_body](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a5dc4b0888f48cd87fc3ded374ffac8a2)
- [HPE_CB_message_complete](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64ae0f56ef0ecc6638fb0594d130a1ee490)
- [HPE_CB_status](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a9adad03852eddb1f361abe9d856a1a0f)
- [HPE_CB_chunk_header](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a69ccadce5be8074b104b19aa74dce556)
- [HPE_CB_chunk_complete](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a008e232118d6133c4dbdd9770d926694)
- [HPE_INVALID_EOF_STATE](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a4103809c185fee62b11c188ff0eab39a)
- [HPE_HEADER_OVERFLOW](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a5270cdc2f8af1802ccf3a2f33fde9307)
- [HPE_CLOSED_CONNECTION](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a7fbc6a25f20237b1cc795db489312e8e)
- [HPE_INVALID_VERSION](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a5a1b7ae13c36ef37fd52b2b68112b501)
- [HPE_INVALID_STATUS](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64aa4a2007f1dc03bf22aff5ca8885f6b59)
- [HPE_INVALID_METHOD](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64ac031cfd48285e22ddec18964f6281f6e)
- [HPE_INVALID_URL](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64ad92573bf62e7b0a13d398926a984fa9d)
- [HPE_INVALID_HOST](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a6391e880280eda55707145bda1170294)
- [HPE_INVALID_PORT](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a3e7c3b8a95f34bbd40ea047fcd43ffa5)
- [HPE_INVALID_PATH](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a69e17a8b5a35b9f93ea914224c2d4f2a)
- [HPE_INVALID_QUERY_STRING](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a383ef24f0ac59de1c128ca776d813865)
- [HPE_INVALID_FRAGMENT](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64afa80e3a0c0dd1c93cf0a11cacbd59079)
- [HPE_LF_EXPECTED](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64af9f23325bd502239af0326a0b407b41d)
- [HPE_INVALID_HEADER_TOKEN](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64ac0348f1ca04bf4d882affcd0249336b5)
- [HPE_INVALID_CONTENT_LENGTH](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a18b873c41a1d7aa9ee9486f719aa7509)
- [HPE_UNEXPECTED_CONTENT_LENGTH](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a2406df24d500b1228fc5ef4a8d60e7c3)
- [HPE_INVALID_CHUNK_SIZE](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a36842cc306c491da8c42023be68585e9)
- [HPE_INVALID_CONTENT_RANGE](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64ab725a62450a5246e98fb5deeb0a250b5)
- [HPE_UNEXPECTED_CONTENT_RANGE](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64af880c7a160717f01bba7bb98169c5011)
- [HPE_INVALID_CONSTANT](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a1b9ec4aeef6f168f9d711c27a0c6faa8)
- [HPE_INVALID_INTERNAL_STATE](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64abb98b653c0972e3e22bc5ff8b57d0d55)
- [HPE_STRICT](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a7f92de0f01b2d0e37209854069183f16)
- [HPE_PAUSED](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64aed64f2a65634183e8f708ac80af3f6f2)
- [HPE_UNKNOWN](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a14687aec2341ce0e62db2e543dd1da64a36cb81d8c40b00602b558f82a38eaecc)
- [http_content_range](../network_application_model_reference/P028_http_content_range_结构体.md)
- [start](../network_application_model_reference/P028_http_content_range_结构体.md#af32a14a0b8ae40722278c8839ab9429c)
- [end](../network_application_model_reference/P028_http_content_range_结构体.md#a4be2d7ae61240cc739ac14971946abfa)
- [total](../network_application_model_reference/P028_http_content_range_结构体.md#a3c96329567d948ecc2f5be5febf48bf4)
- [type](../network_application_model_reference/P032_http_parser_结构体.md#ac6c327558547d55eb64a8aea1310cc2e)
- [flags](../network_application_model_reference/P032_http_parser_结构体.md#a5e54708e0cb3f9ced19bd829dcdeaf53)
- [state](../network_application_model_reference/P032_http_parser_结构体.md#a6f5952e0b47c83aeacf64fc287fd8003)
- [header_state](../network_application_model_reference/P032_http_parser_结构体.md#ac5b254b99c6472ca19ae1f426758ce75)
- [index](../network_application_model_reference/P032_http_parser_结构体.md#a6f7ba706f975f447b3bf72be97facdf8)
- [lenient_http_headers](../network_application_model_reference/P032_http_parser_结构体.md#acd80a931fcc87d41999397af1662fc3c)
- [nread](../network_application_model_reference/P032_http_parser_结构体.md#a78085ca896bb3b9aa1ecb0f6fddc039d)
- [content_length](../network_application_model_reference/P032_http_parser_结构体.md#a7fd5a194802b1206bb773e096d291f29)
- [content_range_present](../network_application_model_reference/P032_http_parser_结构体.md#a4cad8367f35e6739a9ffc45b851f49aa)
- [content_range](../network_application_model_reference/P032_http_parser_结构体.md#ade28251e8473212ad8b9b28dcd343c93)
- [http_major](../network_application_model_reference/P032_http_parser_结构体.md#ac994a4a8268652f5ce82de5bde5c3f9d)
- [http_minor](../network_application_model_reference/P032_http_parser_结构体.md#ae8af6433c824f5348773842db62ad4ab)
- [status_code](../network_application_model_reference/P032_http_parser_结构体.md#a82f5aed92ca3566489def7bc384bab26)
- [method](../network_application_model_reference/P032_http_parser_结构体.md#a7955de339fafd81ad54380845913457d)
- [http_errno](../network_application_model_reference/P032_http_parser_结构体.md#ab8638d65fa174bc1925d77e2533117fa)
- [upgrade](../network_application_model_reference/P032_http_parser_结构体.md#a748f476eacc5ac56b84dd07dbafb42a4)
- [data](../network_application_model_reference/P032_http_parser_结构体.md#a7e87ce57b97f60f1fdb7039a8ecb0bca)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [addr](../network_application_model_reference/P032_http_parser_结构体.md#af2c5cbcfbecce1cce001fe2531a6bd8c)
- [on_message_begin](../network_application_model_reference/P033_http_parser_settings_结构体.md#ac44144daecc8e8adbd477b7e6a794e26)
- [on_url](../network_application_model_reference/P033_http_parser_settings_结构体.md#a9c24dfa900b49bf3439bbfba572b42fb)
- [on_status](../network_application_model_reference/P033_http_parser_settings_结构体.md#a6d0f0203f3461a8889ad471de119c993)
- [on_header_field](../network_application_model_reference/P033_http_parser_settings_结构体.md#acfb3fd7947c5ff3e16649c71aa13bff2)
- [on_header_value](../network_application_model_reference/P033_http_parser_settings_结构体.md#a2af4e9085fa79ee52b31e626179bc561)
- [on_headers_complete](../network_application_model_reference/P033_http_parser_settings_结构体.md#a743b24c8f33e0f1cf60a96c824c42071)
- [on_body](../network_application_model_reference/P033_http_parser_settings_结构体.md#aaa145d7c24c91f471b2079ecb6368ae4)
- [on_message_complete](../network_application_model_reference/P033_http_parser_settings_结构体.md#afdd5beef93a4a7b32bc61ae088da64d2)
- [on_chunk_header](../network_application_model_reference/P033_http_parser_settings_结构体.md#a497cf8f9d68e06e54684b71ee0f9f828)
- [on_chunk_complete](../network_application_model_reference/P033_http_parser_settings_结构体.md#ac1c8453573094795ef41d4ba26e78846)
- [http_parser_version](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a2559b4d373c7f0d85c77a2a3c308a5ee)
- [http_parser_init](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab8ae8e721c5c9f7309e94c174c72a940)
- [http_parser_settings_init](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a76d2e1f7225617f6941042fc95d888fe)
- [http_parser_execute](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a54f1346f15b326f6308a3ff7f0f75b52)
- [http_should_keep_alive](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a903c39c3abea292860780856ba90d560)
- [http_method_str](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#abb207665b6ff41700e5bbb260b580cb6)
- [http_method](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#gaacd5f203e33ac338ca5cb8f02a3ff3b8)
- [http_errno_name](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#acce1b9056442d75d4d609e797bcce2fd)
- [http_errno_description](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a88adfab20d97366aac1fe05aa7dde7da)
- [http_parser_pause](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#aa3764343ba4d2bb13fe39b05425633ba)
- [http_body_is_final](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#a5156a631a251516a6e78b17e1faadbb2)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [method.h](../api_file_supplement_reference/P065_zephyr__net__http__method.h_文件参考.md)
- [parser_state.h](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md)
- [parser_url.h](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md)
- [http_content_range::total](../network_application_model_reference/P028_http_content_range_结构体.md#a3c96329567d948ecc2f5be5febf48bf4)
- [http_content_range::end](../network_application_model_reference/P028_http_content_range_结构体.md#a4be2d7ae61240cc739ac14971946abfa)
- [http_content_range::start](../network_application_model_reference/P028_http_content_range_结构体.md#af32a14a0b8ae40722278c8839ab9429c)
- [http_parser_settings::on_header_value](../network_application_model_reference/P033_http_parser_settings_结构体.md#a2af4e9085fa79ee52b31e626179bc561)
- [http_parser_settings::on_chunk_header](../network_application_model_reference/P033_http_parser_settings_结构体.md#a497cf8f9d68e06e54684b71ee0f9f828)
- [http_parser_settings::on_status](../network_application_model_reference/P033_http_parser_settings_结构体.md#a6d0f0203f3461a8889ad471de119c993)
- [http_parser_settings::on_headers_complete](../network_application_model_reference/P033_http_parser_settings_结构体.md#a743b24c8f33e0f1cf60a96c824c42071)
- [http_parser_settings::on_url](../network_application_model_reference/P033_http_parser_settings_结构体.md#a9c24dfa900b49bf3439bbfba572b42fb)
- [http_parser_settings::on_body](../network_application_model_reference/P033_http_parser_settings_结构体.md#aaa145d7c24c91f471b2079ecb6368ae4)
- [http_parser_settings::on_chunk_complete](../network_application_model_reference/P033_http_parser_settings_结构体.md#ac1c8453573094795ef41d4ba26e78846)
- [http_parser_settings::on_message_begin](../network_application_model_reference/P033_http_parser_settings_结构体.md#ac44144daecc8e8adbd477b7e6a794e26)
- [http_parser_settings::on_header_field](../network_application_model_reference/P033_http_parser_settings_结构体.md#acfb3fd7947c5ff3e16649c71aa13bff2)
- [http_parser_settings::on_message_complete](../network_application_model_reference/P033_http_parser_settings_结构体.md#afdd5beef93a4a7b32bc61ae088da64d2)
- [http_parser::content_range_present](../network_application_model_reference/P032_http_parser_结构体.md#a4cad8367f35e6739a9ffc45b851f49aa)
- [http_parser::flags](../network_application_model_reference/P032_http_parser_结构体.md#a5e54708e0cb3f9ced19bd829dcdeaf53)
- [http_parser::state](../network_application_model_reference/P032_http_parser_结构体.md#a6f5952e0b47c83aeacf64fc287fd8003)
- [http_parser::index](../network_application_model_reference/P032_http_parser_结构体.md#a6f7ba706f975f447b3bf72be97facdf8)
- [http_parser::upgrade](../network_application_model_reference/P032_http_parser_结构体.md#a748f476eacc5ac56b84dd07dbafb42a4)
- [http_parser::nread](../network_application_model_reference/P032_http_parser_结构体.md#a78085ca896bb3b9aa1ecb0f6fddc039d)
- [http_parser::method](../network_application_model_reference/P032_http_parser_结构体.md#a7955de339fafd81ad54380845913457d)
- [http_parser::data](../network_application_model_reference/P032_http_parser_结构体.md#a7e87ce57b97f60f1fdb7039a8ecb0bca)
- [http_parser::content_length](../network_application_model_reference/P032_http_parser_结构体.md#a7fd5a194802b1206bb773e096d291f29)
- [http_parser::status_code](../network_application_model_reference/P032_http_parser_结构体.md#a82f5aed92ca3566489def7bc384bab26)
- [http_parser::http_errno](../network_application_model_reference/P032_http_parser_结构体.md#ab8638d65fa174bc1925d77e2533117fa)
- [http_parser::header_state](../network_application_model_reference/P032_http_parser_结构体.md#ac5b254b99c6472ca19ae1f426758ce75)
- [http_parser::type](../network_application_model_reference/P032_http_parser_结构体.md#ac6c327558547d55eb64a8aea1310cc2e)
- [http_parser::http_major](../network_application_model_reference/P032_http_parser_结构体.md#ac994a4a8268652f5ce82de5bde5c3f9d)
- [http_parser::lenient_http_headers](../network_application_model_reference/P032_http_parser_结构体.md#acd80a931fcc87d41999397af1662fc3c)
- [http_parser::content_range](../network_application_model_reference/P032_http_parser_结构体.md#ade28251e8473212ad8b9b28dcd343c93)
- [http_parser::http_minor](../network_application_model_reference/P032_http_parser_结构体.md#ae8af6433c824f5348773842db62ad4ab)
- [http_parser::addr](../network_application_model_reference/P032_http_parser_结构体.md#af2c5cbcfbecce1cce001fe2531a6bd8c)

---

[上一章](P006_ite-it51xxx-intc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_posix_signal.h_源码浏览.md)
