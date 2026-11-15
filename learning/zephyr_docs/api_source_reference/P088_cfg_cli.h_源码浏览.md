---
id: learning.zephyr-docs.api-source-reference.page-88
title: cfg_cli.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_cfg\_cli.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h.html)。

## 88.1\_原始可见代码（Source Code）

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
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="foldopen00333"></a>
<a id="l00333"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="foldopen00349"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="foldopen00396"></a>
<a id="l00396"></a>
<a id="l00398"></a>
<a id="l00400"></a>
<a id="l00402"></a>
<a id="l00404"></a>
<a id="l00406"></a>
<a id="l00413"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="foldopen00422"></a>
<a id="l00422"></a>
<a id="l00424"></a>
<a id="l00426"></a>
<a id="l00432"></a>
<a id="l00440"></a>
<a id="l00448"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="foldopen00460"></a>
<a id="l00460"></a>
<a id="l00462"></a>
<a id="l00474"></a>
<a id="l00480"></a>
<a id="l00482"></a>
<a id="l00489"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00695"></a>
<a id="l00696"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00919"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="l00938"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00961"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="l00984"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="l01009"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01028"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01048"></a>
<a id="l01066"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="l01088"></a>
<a id="l01089"></a>
<a id="l01090"></a>
<a id="l01091"></a>
<a id="l01107"></a>
<a id="l01108"></a>
<a id="l01109"></a>
<a id="l01126"></a>
<a id="l01127"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01145"></a>
<a id="l01146"></a>
<a id="l01147"></a>
<a id="l01164"></a>
<a id="l01165"></a>
<a id="l01166"></a>
<a id="l01167"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01210"></a>
<a id="l01211"></a>
<a id="l01212"></a>
<a id="l01213"></a>
<a id="l01230"></a>
<a id="l01231"></a>
<a id="l01232"></a>
<a id="l01233"></a>
<a id="l01251"></a>
<a id="l01252"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="l01271"></a>
<a id="l01272"></a>
<a id="l01273"></a>
<a id="l01274"></a>
<a id="l01292"></a>
<a id="l01293"></a>
<a id="l01294"></a>
<a id="l01295"></a>
<a id="l01316"></a>
<a id="l01317"></a>
<a id="l01318"></a>
<a id="l01319"></a>
<a id="l01341"></a>
<a id="l01342"></a>
<a id="l01343"></a>
<a id="l01344"></a>
<a id="l01364"></a>
<a id="l01365"></a>
<a id="l01366"></a>
<a id="l01387"></a>
<a id="l01388"></a>
<a id="l01389"></a>
<a id="l01390"></a>
<a id="l01406"></a>
<a id="l01407"></a>
<a id="l01408"></a>
<a id="l01422"></a>
<a id="l01423"></a>
<a id="l01424"></a>
<a id="l01442"></a>
<a id="l01443"></a>
<a id="l01444"></a>
<a id="l01458"></a>
<a id="l01459"></a>
<a id="l01460"></a>
<a id="l01475"></a>
<a id="l01476"></a>
<a id="l01477"></a>
<a id="l01493"></a>
<a id="l01494"></a>
<a id="l01495"></a>
<a id="l01510"></a>
<a id="l01511"></a>
<a id="l01512"></a>
<a id="l01528"></a>
<a id="l01529"></a>
<a id="l01530"></a>
<a id="l01531"></a>
<a id="l01549"></a>
<a id="l01550"></a>
<a id="l01551"></a>
<a id="l01568"></a>
<a id="l01569"></a>
<a id="l01570"></a>
<a id="l01584"></a>
<a id="l01585"></a>
<a id="l01586"></a>
<a id="l01591"></a>
<a id="l01592"></a>
<a id="l01597"></a>
<a id="l01598"></a>
<a id="foldopen01605"></a>
<a id="l01605"></a>
<a id="l01607"></a>
<a id="l01609"></a>
<a id="l01611"></a>
<a id="l01613"></a>
<a id="l01615"></a>
<a id="l01616"></a>
<a id="l01617"></a>
<a id="l01618"></a>
<a id="l01619"></a>
<a id="foldopen01621"></a>
<a id="l01621"></a>
<a id="l01623"></a>
<a id="l01625"></a>
<a id="l01627"></a>
<a id="l01628"></a>
<a id="l01629"></a>
<a id="l01630"></a>
<a id="l01631"></a>
<a id="l01655"></a>
<a id="l01656"></a>
<a id="l01657"></a>
<a id="l01670"></a>
<a id="l01671"></a>
<a id="l01672"></a>
<a id="l01681"></a>
<a id="l01682"></a>
<a id="l01691"></a>
<a id="l01692"></a>
<a id="foldopen01694"></a>
<a id="l01694"></a>
<a id="l01696"></a>
<a id="l01698"></a>
<a id="l01700"></a>
<a id="l01701"></a>
<a id="l01702"></a>
<a id="foldopen01704"></a>
<a id="l01704"></a>
<a id="l01706"></a>
<a id="l01708"></a>
<a id="l01710"></a>
<a id="l01715"></a>
<a id="l01716"></a>
<a id="l01717"></a>
<a id="l01718"></a>
<a id="foldopen01720"></a>
<a id="l01720"></a>
<a id="l01722"></a>
<a id="l01724"></a>
<a id="l01725"></a>
<a id="l01726"></a>
<a id="foldopen01728"></a>
<a id="l01728"></a>
<a id="l01730"></a>
<a id="l01732"></a>
<a id="l01733"></a>
<a id="l01734"></a>
<a id="foldopen01736"></a>
<a id="l01736"></a>
<a id="l01737"></a>
<a id="l01738"></a>
<a id="l01739"></a>
<a id="l01741"></a>
<a id="l01743"></a>
<a id="l01744"></a>
<a id="l01745"></a>
<a id="l01746"></a>
<a id="l01759"></a>
<a id="l01760"></a>
<a id="l01761"></a>
<a id="l01774"></a>
<a id="l01775"></a>
<a id="l01776"></a>
<a id="l01787"></a>
<a id="l01788"></a>
<a id="l01789"></a>
<a id="foldopen01791"></a>
<a id="l01791"></a>
<a id="l01793"></a>
<a id="l01795"></a>
<a id="l01797"></a>
<a id="l01799"></a>
<a id="l01801"></a>
<a id="l01802"></a>
<a id="l01804"></a>
<a id="l01806"></a>
<a id="l01807"></a>
<a id="l01808"></a>
<a id="l01821"></a>
<a id="l01822"></a>
<a id="l01823"></a>
<a id="l01835"></a>
<a id="l01836"></a>
<a id="l01838"></a>
<a id="l01839"></a>
<a id="l01841"></a>
<a id="l01842"></a>
<a id="l01843"></a>
<a id="l01844"></a>
<a id="l01848"></a>
<a id="l01849"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga07c443476adef9c7bb573ffbb8d1b1ce"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga0854a494707a40b84beb8582f45e0470"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga09e751a9071402ae978c0355edfbdf03"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga0bc2c24403e0cd79a061ba1244b1a1db"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga0ee1d0849d632b5d806ee31c87bbc888"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga12a8618d2b73f30742f8e8d2bdddc138"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga1adae658bf8f4512a7d80d0194dcb362"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga1b36596a20ca8751006b0f7f2221067d"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga1f79d98273a984f1c49b4d5dd5bf8d30"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga1fb53b9a49be25e633cac9d668c5b209"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga2059ccbc689af9c2127e4e399ea5bd43"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga2671234d739c802fd080a19d01235352"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga283fb06ddb6427852ff0ac556d3c1852"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga2c8a79d1b70e91e0a09c848737bb4a22"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga2d22612cf9dc5030699bf7c6c58bf6d5"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga352eb00b78ff978a1a1e81ec5a0575b8"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga36259e9c811a8f1a21d642739cf297df"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga3ba34f8be138bc62a7eb7859b18dc441"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga4a50a6a5dcfdc42b7476f0b9e463ea45"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga4dd1534e9d5b04fc99231ba5dde23e05"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga4f656102982961b7bf2e3d3896a2240e"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga5140472c687584babf885bc08349c865"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga5a717835a416ba2930f65a975265649f"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga6391ce297ca0be73ccd51044a9e0a76f"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga660df68049110332ff21610fe4e520c6"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga67cf5ff993f2444cc66b2ae5353865d2"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga69809ad3f2cff8e1f394f6da6ed63264"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga69b2dfacc27ed94b9e1331ff4ac4b582"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga70d3bb7fb914fa3685f4ad9b561a48b6"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga74bad73184af2d6ce71134831f70680d"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga7e3521ae973dc825422c6dd5f07ef547"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga7fc2acda16f3f03a929c38796c67028e"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga7fe8418130568bdf2a5e56ed2ad027b0"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga86e5de1b216d62b7c77bf43b7af062fc"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga87f7c1e06b5c721c89031c527960bf40"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga8884786e3ec349bcb8b89b60aa11f198"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga8d8595f077267b7d784fde30cbc4b207"></a>
<a id="agroup__bt__mesh__cfg__cli_html_ga92ee7984b14590ed11a470c0dfea0bc9"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gaa141d4aabbed6c7780ac7f3955c8b580"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gaa3a10a54a18a99d0b4b0aa85330b1640"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gaa411ab7db2e71a114a8108eaec9ca12c"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gaa4a02dd0c1f67621ee71d011fe4a29c1"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gaa6d60ebad6dc4a4f5b022937dbae3120"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gaaf945377cf6a3d2b3e7c7cdb5a8df016"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gab2963ec5536cb4b941578bb490fdc013"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gab42c5bdff36bea35e967946462b12457"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gab513c82ebe434907a958cc6da990bd0b"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gac005f52e191c3e5628f063dbc1a19645"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gac02c170e260980d5b749b581910672d2"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gac527fe27308c8a61ac1831af9605e429"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gac6675d227749a69cedc5455c70626b76"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gac8b4b670c82b80a51834f7ef32206985"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gacd647905484fa8319a5377aa5777c254"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gacf1bd7a771a45981a82eeea0dcce01b7"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gacf8ad783910449c7cdc304c1b9b3fe0b"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gad2c602a2685ff38c0e78c1990b244e54"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gada33602562721c9f413eb06b34a823a8"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gadac1cc360c30d290a861bbd534fca58d"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gae51eee59090cfebed4561ed3bb4df005"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gae9a19b089d898af914ea5c287aca8fba"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gaf4ee720ce27eea9602b59a380278bb57"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gaf5262c0a27e4b9249ecf908c259cc7d7"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gaf7107373fc0c70d091e9a521d8b641ad"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gaf739e5e3a4b225e10bf2aedf143d7793"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gaf7e0f85bbbbfc382bfe4aea8298227d1"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gaf82b54a4b2d3176b10daf728272a0977"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gafabf4c0fa707eba1fd40cc9a403daa07"></a>
<a id="agroup__bt__mesh__cfg__cli_html_gafdaff279685b821a7b205e45feed9a05"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__cfg__cli__cb_html"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_a0ad46d1d4793577679f66c62175e14cf"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_a3ccff69f21e0f3c585b951eb60c1bf5c"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_a48ef4d0665d86d069b90533eb18e0fd0"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_a49a7a8cab34bb70d2edd87b0017f1cf7"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_a4d89033676eb4570cdd80f1715fd9bfb"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_a5cf2c17a88c53c514fcaa73a6fd81b67"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_a615852027a841b1779a50c9fd50bef6a"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_a66b5a8dd3bdd2468fe65496020b13495"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_a6ef3730e9469bffd81cdd49c50cac7d5"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_a89eab453e00662f6f3f8a5d78f20d120"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_a9487a159a6c838a9218b3d76fa53248d"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_aa60dfd72a43273e1ffae2160bcc0845d"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_aaae4e3f64e2033a466ad87d362ceb318"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_ab4130e909826aa7746092f49f8b4c52e"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_ab937311c41af68b1cd52a8a1c86145b1"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_abf8501e73f44ab5ea7e54b8f2ff1f866"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_ac331fc103d0f331093929f39e5b9d6ba"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_aca2d779401fa4521813e6578bd3bbd91"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_acce08dfa5cb356a2203f0ef6c4e4bf5b"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_acf88660364760442dfab5280ae735d2d"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_ad46ea40b75cc1d5d314fdefdca0076f8"></a>
<a id="astructbt__mesh__cfg__cli__cb_html_af4a43f4c65d111e95211b715048534cc"></a>
<a id="astructbt__mesh__cfg__cli__hb__pub_html"></a>
<a id="astructbt__mesh__cfg__cli__hb__pub_html_a13c7c155f30ca94d30090a25df50e4b2"></a>
<a id="astructbt__mesh__cfg__cli__hb__pub_html_a473df7dd958683d7502dcc983c4ceb8a"></a>
<a id="astructbt__mesh__cfg__cli__hb__pub_html_a8d17dd2df4be23cadad4b5746ddb50ad"></a>
<a id="astructbt__mesh__cfg__cli__hb__pub_html_a90a79d8b7ea91c6ba872dca15d87b356"></a>
<a id="astructbt__mesh__cfg__cli__hb__pub_html_a94598c9b733075abe22d70f62293b5a1"></a>
<a id="astructbt__mesh__cfg__cli__hb__pub_html_ac7f24f7bf942587ef83ca47d9ee4e7fb"></a>
<a id="astructbt__mesh__cfg__cli__hb__sub_html"></a>
<a id="astructbt__mesh__cfg__cli__hb__sub_html_a01ec0c3cab7bb7ed76d7728390eb4f25"></a>
<a id="astructbt__mesh__cfg__cli__hb__sub_html_a480b214e0e1974a6a54426c49e5d62d1"></a>
<a id="astructbt__mesh__cfg__cli__hb__sub_html_a5a75c924f0868c664652503335b1b012"></a>
<a id="astructbt__mesh__cfg__cli__hb__sub_html_a93624ab6c8a0c15c0b50490e0fcd3675"></a>
<a id="astructbt__mesh__cfg__cli__hb__sub_html_aac96c2ab606e38f412e94539795c5594"></a>
<a id="astructbt__mesh__cfg__cli__hb__sub_html_abc9ea18fbe86c260d6cf5d53c26a0248"></a>
<a id="astructbt__mesh__cfg__cli__mod__pub_html"></a>
<a id="astructbt__mesh__cfg__cli__mod__pub_html_a104afe2b8d9766e037293b09c0c1b91c"></a>
<a id="astructbt__mesh__cfg__cli__mod__pub_html_a29cbd50ad33f25ad3b98b4ec7ac56a6c"></a>
<a id="astructbt__mesh__cfg__cli__mod__pub_html_a2a5a0ead8155bf971c84f73dfa4ec282"></a>
<a id="astructbt__mesh__cfg__cli__mod__pub_html_a9513db038ec4f51734892bd1ce7d08f3"></a>
<a id="astructbt__mesh__cfg__cli__mod__pub_html_aa7452f697410fdf8a63808bcb29c53ee"></a>
<a id="astructbt__mesh__cfg__cli__mod__pub_html_ab52dd35df271ae5bd70a4640e6f3bea8"></a>
<a id="astructbt__mesh__cfg__cli__mod__pub_html_aefbe5449a10379b064dea054300cb9a0"></a>
<a id="astructbt__mesh__cfg__cli_html"></a>
<a id="astructbt__mesh__cfg__cli_html_a472bf5015857ab97e1a40ab6cfa70bb1"></a>
<a id="astructbt__mesh__cfg__cli_html_a525dd5391c83c525c012940575245cea"></a>
<a id="astructbt__mesh__cfg__cli_html_a7160cf5d22fa0b909482bbc76f27b6bd"></a>
<a id="astructbt__mesh__comp__p0__elem_html"></a>
<a id="astructbt__mesh__comp__p0__elem_html_a17f61eab2df28f2031f2fbab28254484"></a>
<a id="astructbt__mesh__comp__p0__elem_html_a2e1bd3146ebc934e9fab0242a06d5b99"></a>
<a id="astructbt__mesh__comp__p0__elem_html_a832cdb0a10d364a048971f59f51e841d"></a>
<a id="astructbt__mesh__comp__p0_html"></a>
<a id="astructbt__mesh__comp__p0_html_a009806e046583c99f56d271ecebbb8a3"></a>
<a id="astructbt__mesh__comp__p0_html_a0a44e3778f9d134a5c056ca184c3b527"></a>
<a id="astructbt__mesh__comp__p0_html_a27d910cdeb7b6b9d038898e3824dfb57"></a>
<a id="astructbt__mesh__comp__p0_html_a32bfead26f338aba892a5459615a65a2"></a>
<a id="astructbt__mesh__comp__p0_html_a3ed8f5ac643443bbcca308baff1c539c"></a>
<a id="astructbt__mesh__comp__p1__elem_html"></a>
<a id="astructbt__mesh__comp__p1__elem_html_a25492ac30a362e4490d11169ed98197b"></a>
<a id="astructbt__mesh__comp__p1__elem_html_aa6aa100992502cef0484a127224cf07b"></a>
<a id="astructbt__mesh__comp__p1__ext__item_html"></a>
<a id="astructbt__mesh__comp__p1__ext__item_html_a05a526a8448e7b8a4766eb038e4c1a39a23a15546d8722d7a4706ea34c5785658"></a>
<a id="astructbt__mesh__comp__p1__ext__item_html_a05a526a8448e7b8a4766eb038e4c1a39ae96bb3e960c4d2c356c0070f34740119"></a>
<a id="astructbt__mesh__comp__p1__ext__item_html_a3962046fc095348035a193dad60d1149"></a>
<a id="astructbt__mesh__comp__p1__ext__item_html_a43f50f35690e54d3680a6daa989ce1c0"></a>
<a id="astructbt__mesh__comp__p1__ext__item_html_ae17176001203ee8c282f06e994cee647"></a>
<a id="astructbt__mesh__comp__p1__item__long_html"></a>
<a id="astructbt__mesh__comp__p1__item__long_html_a12a0e2fb373e2e43b7c04a1130cdf018"></a>
<a id="astructbt__mesh__comp__p1__item__long_html_a61d541854c2d1671c60fc444978f0374"></a>
<a id="astructbt__mesh__comp__p1__item__short_html"></a>
<a id="astructbt__mesh__comp__p1__item__short_html_a1fb6c8134a2c02e3b83dfea12ab39410"></a>
<a id="astructbt__mesh__comp__p1__item__short_html_a7e2152fe608c52cbc0700a43a5653132"></a>
<a id="astructbt__mesh__comp__p1__model__item_html"></a>
<a id="astructbt__mesh__comp__p1__model__item_html_a95baa1acf3a82e8559ce4a47b7e03be8"></a>
<a id="astructbt__mesh__comp__p1__model__item_html_ae019a211eafeb20f323ad97328d938f7"></a>
<a id="astructbt__mesh__comp__p1__model__item_html_aee352e8563133dddbb37c1f31dfe7c09"></a>
<a id="astructbt__mesh__comp__p1__model__item_html_af2f213813440cb4a87884e3625a704e7"></a>
<a id="astructbt__mesh__comp__p2__record_html"></a>
<a id="astructbt__mesh__comp__p2__record_html_a0ceff9becd0eb14ca190c49f56ec0957"></a>
<a id="astructbt__mesh__comp__p2__record_html_a4d947193b1a0f46c9df1eca298135646"></a>
<a id="astructbt__mesh__comp__p2__record_html_a5377ce835db8ce408d8dabfd87c858f5"></a>
<a id="astructbt__mesh__comp__p2__record_html_a90e80906ef6d2b8b932215ad183db2d5"></a>
<a id="astructbt__mesh__comp__p2__record_html_aa718c024d6ce339ac8c352319b878c53"></a>
<a id="astructbt__mesh__comp__p2__record_html_abd0975a47c848265ad13044dfcd3b78d"></a>
<a id="astructbt__mesh__comp__p2__record_html_ad310f8c8e3a167492a6e698336b7f400"></a>
<a id="astructbt__mesh__mod__id__vnd_html"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ack__ctx_html"></a>
<a id="astructnet__buf__simple_html"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_CFG_CLI_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_CFG_CLI_H_


#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_mesh_cfg_cli;
struct bt_mesh_cfg_cli_hb_pub;
struct bt_mesh_cfg_cli_hb_sub;
struct bt_mesh_cfg_cli_mod_pub;

struct bt_mesh_cfg_cli_cb {

        void (*comp_data)(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t page,
                          struct net_buf_simple *buf);

        void (*mod_pub_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status,
                               uint16_t elem_addr, uint16_t mod_id, uint16_t cid,
                               struct bt_mesh_cfg_cli_mod_pub *pub);

        void (*mod_sub_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                             uint8_t status, uint16_t elem_addr,
                             uint16_t sub_addr, uint32_t mod_id);

        void (*mod_sub_list)(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status,
                             uint16_t elem_addr, uint16_t mod_id, uint16_t cid,
                             struct net_buf_simple *buf);

        void (*node_reset_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr);

        void (*beacon_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                                uint8_t status);

        void (*ttl_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                           uint8_t status);

        void (*friend_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                              uint8_t status);

        void (*gatt_proxy_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                                  uint8_t status);

        void (*network_transmit_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                                        uint8_t status);

        void (*relay_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                             uint8_t status, uint8_t transmit);

        void (*net_key_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                               uint8_t status, uint16_t net_idx);

        void (*net_key_list)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                             struct net_buf_simple *buf);

        void (*app_key_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                               uint8_t status, uint16_t net_idx,
                               uint16_t app_idx);

        void (*app_key_list)(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status,
                             uint16_t net_idx, struct net_buf_simple *buf);

        void (*mod_app_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                               uint8_t status, uint16_t elem_addr,
                               uint16_t app_idx, uint32_t mod_id);

        void (*mod_app_list)(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status,
                             uint16_t elem_addr, uint16_t mod_id, uint16_t cid,
                             struct net_buf_simple *buf);

        void (*node_identity_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                                     uint8_t status, uint16_t net_idx,
                                     uint8_t identity);

        void (*lpn_timeout_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr,
                                   uint16_t elem_addr, uint32_t timeout);

        void (*krp_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status,
                           uint16_t net_idx, uint8_t phase);

        void (*hb_pub_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status,
                              struct bt_mesh_cfg_cli_hb_pub *pub);

        void (*hb_sub_status)(struct bt_mesh_cfg_cli *cli, uint16_t addr, uint8_t status,
                              struct bt_mesh_cfg_cli_hb_sub *sub);
};

struct bt_mesh_cfg_cli {
        const struct bt_mesh_model *model;

        const struct bt_mesh_cfg_cli_cb *cb;

        /* Internal parameters for tracking message responses. */
        struct bt_mesh_msg_ack_ctx ack_ctx;
};

#define BT_MESH_MODEL_CFG_CLI(cli_data)                 \
        BT_MESH_MODEL_CNT_CB(BT_MESH_MODEL_ID_CFG_CLI,  \
                             bt_mesh_cfg_cli_op, NULL,  \
                             cli_data, 1, 0, &bt_mesh_cfg_cli_cb)

#define BT_MESH_PUB_PERIOD_100MS(steps)  ((steps) & BIT_MASK(6))

#define BT_MESH_PUB_PERIOD_SEC(steps)   (((steps) & BIT_MASK(6)) | (1 << 6))

#define BT_MESH_PUB_PERIOD_10SEC(steps) (((steps) & BIT_MASK(6)) | (2 << 6))

#define BT_MESH_PUB_PERIOD_10MIN(steps) (((steps) & BIT_MASK(6)) | (3 << 6))

struct bt_mesh_cfg_cli_mod_pub {
        uint16_t addr;
        const uint8_t *uuid;
        uint16_t  app_idx;
        bool   cred_flag;
        uint8_t   ttl;
        uint8_t   period;
        uint8_t   transmit;
};

struct bt_mesh_cfg_cli_hb_sub {
        uint16_t src;
        uint16_t dst;
        uint8_t  period;
        uint8_t  count;
        uint8_t  min;
        uint8_t  max;
};

struct bt_mesh_cfg_cli_hb_pub {
        uint16_t dst;
        uint8_t  count;
        uint8_t  period;
        uint8_t  ttl;
        uint16_t feat;
        uint16_t net_idx;
};

int bt_mesh_cfg_cli_node_reset(uint16_t net_idx, uint16_t addr, bool *status);

int bt_mesh_cfg_cli_comp_data_get(uint16_t net_idx, uint16_t addr, uint8_t page, uint8_t *rsp,
                                  struct net_buf_simple *comp);

int bt_mesh_cfg_cli_beacon_get(uint16_t net_idx, uint16_t addr, uint8_t *status);

int bt_mesh_cfg_cli_krp_get(uint16_t net_idx, uint16_t addr, uint16_t key_net_idx, uint8_t *status,
                            uint8_t *phase);

int bt_mesh_cfg_cli_krp_set(uint16_t net_idx, uint16_t addr, uint16_t key_net_idx,
                            uint8_t transition, uint8_t *status, uint8_t *phase);

int bt_mesh_cfg_cli_beacon_set(uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *status);

int bt_mesh_cfg_cli_ttl_get(uint16_t net_idx, uint16_t addr, uint8_t *ttl);

int bt_mesh_cfg_cli_ttl_set(uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *ttl);

int bt_mesh_cfg_cli_friend_get(uint16_t net_idx, uint16_t addr, uint8_t *status);

int bt_mesh_cfg_cli_friend_set(uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *status);

int bt_mesh_cfg_cli_gatt_proxy_get(uint16_t net_idx, uint16_t addr, uint8_t *status);

int bt_mesh_cfg_cli_gatt_proxy_set(uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *status);

int bt_mesh_cfg_cli_net_transmit_get(uint16_t net_idx, uint16_t addr, uint8_t *transmit);

int bt_mesh_cfg_cli_net_transmit_set(uint16_t net_idx, uint16_t addr, uint8_t val,
                                     uint8_t *transmit);

int bt_mesh_cfg_cli_relay_get(uint16_t net_idx, uint16_t addr, uint8_t *status, uint8_t *transmit);

int bt_mesh_cfg_cli_relay_set(uint16_t net_idx, uint16_t addr, uint8_t new_relay,
                              uint8_t new_transmit, uint8_t *status, uint8_t *transmit);

int bt_mesh_cfg_cli_net_key_add(uint16_t net_idx, uint16_t addr, uint16_t key_net_idx,
                                const uint8_t net_key[16], uint8_t *status);

int bt_mesh_cfg_cli_net_key_get(uint16_t net_idx, uint16_t addr, uint16_t *keys, size_t *key_cnt);

int bt_mesh_cfg_cli_net_key_del(uint16_t net_idx, uint16_t addr, uint16_t key_net_idx,
                                uint8_t *status);

int bt_mesh_cfg_cli_app_key_add(uint16_t net_idx, uint16_t addr, uint16_t key_net_idx,
                                uint16_t key_app_idx, const uint8_t app_key[16], uint8_t *status);

int bt_mesh_cfg_cli_app_key_get(uint16_t net_idx, uint16_t addr, uint16_t key_net_idx,
                                uint8_t *status, uint16_t *keys, size_t *key_cnt);

int bt_mesh_cfg_cli_app_key_del(uint16_t net_idx, uint16_t addr, uint16_t key_net_idx,
                                uint16_t key_app_idx, uint8_t *status);

int bt_mesh_cfg_cli_mod_app_bind(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                 uint16_t mod_app_idx, uint16_t mod_id, uint8_t *status);

int bt_mesh_cfg_cli_mod_app_unbind(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                   uint16_t mod_app_idx, uint16_t mod_id, uint8_t *status);

int bt_mesh_cfg_cli_mod_app_bind_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                     uint16_t mod_app_idx, uint16_t mod_id, uint16_t cid,
                                     uint8_t *status);

int bt_mesh_cfg_cli_mod_app_unbind_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                       uint16_t mod_app_idx, uint16_t mod_id, uint16_t cid,
                                       uint8_t *status);

int bt_mesh_cfg_cli_mod_app_get(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                uint16_t mod_id, uint8_t *status, uint16_t *apps, size_t *app_cnt);

int bt_mesh_cfg_cli_mod_app_get_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                    uint16_t mod_id, uint16_t cid, uint8_t *status, uint16_t *apps,
                                    size_t *app_cnt);

int bt_mesh_cfg_cli_mod_pub_get(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                uint16_t mod_id, struct bt_mesh_cfg_cli_mod_pub *pub,
                                uint8_t *status);

int bt_mesh_cfg_cli_mod_pub_get_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                    uint16_t mod_id, uint16_t cid,
                                    struct bt_mesh_cfg_cli_mod_pub *pub, uint8_t *status);

int bt_mesh_cfg_cli_mod_pub_set(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                uint16_t mod_id, struct bt_mesh_cfg_cli_mod_pub *pub,
                                uint8_t *status);

int bt_mesh_cfg_cli_mod_pub_set_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                    uint16_t mod_id, uint16_t cid,
                                    struct bt_mesh_cfg_cli_mod_pub *pub, uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_add(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                uint16_t sub_addr, uint16_t mod_id, uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_add_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                    uint16_t sub_addr, uint16_t mod_id, uint16_t cid,
                                    uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_del(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                uint16_t sub_addr, uint16_t mod_id, uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_del_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                    uint16_t sub_addr, uint16_t mod_id, uint16_t cid,
                                    uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_overwrite(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                      uint16_t sub_addr, uint16_t mod_id, uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_overwrite_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                          uint16_t sub_addr, uint16_t mod_id, uint16_t cid,
                                          uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_va_add(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                   const uint8_t label[16], uint16_t mod_id, uint16_t *virt_addr,
                                   uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_va_add_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                       const uint8_t label[16], uint16_t mod_id, uint16_t cid,
                                       uint16_t *virt_addr, uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_va_del(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                   const uint8_t label[16], uint16_t mod_id, uint16_t *virt_addr,
                                   uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_va_del_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                       const uint8_t label[16], uint16_t mod_id, uint16_t cid,
                                       uint16_t *virt_addr, uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_va_overwrite(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                         const uint8_t label[16], uint16_t mod_id,
                                         uint16_t *virt_addr, uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_va_overwrite_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                             const uint8_t label[16], uint16_t mod_id, uint16_t cid,
                                             uint16_t *virt_addr, uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_get(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                uint16_t mod_id, uint8_t *status, uint16_t *subs, size_t *sub_cnt);

int bt_mesh_cfg_cli_mod_sub_get_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                    uint16_t mod_id, uint16_t cid, uint8_t *status, uint16_t *subs,
                                    size_t *sub_cnt);

int bt_mesh_cfg_cli_hb_sub_set(uint16_t net_idx, uint16_t addr, struct bt_mesh_cfg_cli_hb_sub *sub,
                               uint8_t *status);

int bt_mesh_cfg_cli_hb_sub_get(uint16_t net_idx, uint16_t addr, struct bt_mesh_cfg_cli_hb_sub *sub,
                               uint8_t *status);

int bt_mesh_cfg_cli_hb_pub_set(uint16_t net_idx, uint16_t addr,
                               const struct bt_mesh_cfg_cli_hb_pub *pub, uint8_t *status);

int bt_mesh_cfg_cli_hb_pub_get(uint16_t net_idx, uint16_t addr, struct bt_mesh_cfg_cli_hb_pub *pub,
                               uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_del_all(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                    uint16_t mod_id, uint8_t *status);

int bt_mesh_cfg_cli_mod_sub_del_all_vnd(uint16_t net_idx, uint16_t addr, uint16_t elem_addr,
                                        uint16_t mod_id, uint16_t cid, uint8_t *status);

int bt_mesh_cfg_cli_net_key_update(uint16_t net_idx, uint16_t addr, uint16_t key_net_idx,
                                   const uint8_t net_key[16], uint8_t *status);

int bt_mesh_cfg_cli_app_key_update(uint16_t net_idx, uint16_t addr, uint16_t key_net_idx,
                                   uint16_t key_app_idx, const uint8_t app_key[16],
                                   uint8_t *status);

int bt_mesh_cfg_cli_node_identity_set(uint16_t net_idx, uint16_t addr, uint16_t key_net_idx,
                                      uint8_t new_identity, uint8_t *status, uint8_t *identity);

int bt_mesh_cfg_cli_node_identity_get(uint16_t net_idx, uint16_t addr, uint16_t key_net_idx,
                                      uint8_t *status, uint8_t *identity);

int bt_mesh_cfg_cli_lpn_timeout_get(uint16_t net_idx, uint16_t addr, uint16_t unicast_addr,
                                    int32_t *polltimeout);

int32_t bt_mesh_cfg_cli_timeout_get(void);

void bt_mesh_cfg_cli_timeout_set(int32_t timeout);

struct bt_mesh_comp_p0 {
        uint16_t cid;
        uint16_t pid;
        uint16_t vid;
        uint16_t crpl;
        uint16_t feat;

        struct net_buf_simple *_buf;
};

struct bt_mesh_comp_p0_elem {
        uint16_t loc;
        size_t nsig;
        size_t nvnd;

        uint8_t *_buf;
};

int bt_mesh_comp_p0_get(struct bt_mesh_comp_p0 *comp,
                        struct net_buf_simple *buf);

struct bt_mesh_comp_p0_elem *bt_mesh_comp_p0_elem_pull(const struct bt_mesh_comp_p0 *comp,
                                                       struct bt_mesh_comp_p0_elem *elem);

uint16_t bt_mesh_comp_p0_elem_mod(struct bt_mesh_comp_p0_elem *elem, int idx);

struct bt_mesh_mod_id_vnd bt_mesh_comp_p0_elem_mod_vnd(struct bt_mesh_comp_p0_elem *elem, int idx);

struct bt_mesh_comp_p1_elem {
        size_t nsig;
        size_t nvnd;
        struct net_buf_simple *_buf;
};

struct bt_mesh_comp_p1_model_item {
        bool cor_present;
        bool format;
        uint8_t ext_item_cnt : 6;
        uint8_t cor_id;
        struct net_buf_simple *_buf;
};

struct bt_mesh_comp_p1_item_short {
        uint8_t elem_offset : 3;
        uint8_t mod_item_idx : 5;
};

struct bt_mesh_comp_p1_item_long {
        uint8_t elem_offset;
        uint8_t mod_item_idx;
};

struct bt_mesh_comp_p1_ext_item {
        enum { SHORT, LONG } type;

        union {
                struct bt_mesh_comp_p1_item_short short_item;
                struct bt_mesh_comp_p1_item_long long_item;
        };
};

struct bt_mesh_comp_p1_elem *bt_mesh_comp_p1_elem_pull(
        struct net_buf_simple *buf, struct bt_mesh_comp_p1_elem *elem);

struct bt_mesh_comp_p1_model_item *bt_mesh_comp_p1_item_pull(
        struct bt_mesh_comp_p1_elem *elem, struct bt_mesh_comp_p1_model_item *item);

struct bt_mesh_comp_p1_ext_item *bt_mesh_comp_p1_pull_ext_item(
        struct bt_mesh_comp_p1_model_item *item, struct bt_mesh_comp_p1_ext_item *ext_item);

struct bt_mesh_comp_p2_record {
        uint16_t id;
        struct {
                uint8_t x;
                uint8_t y;
                uint8_t z;
        } version;
        struct net_buf_simple *elem_buf;
        struct net_buf_simple *data_buf;
};

struct bt_mesh_comp_p2_record *bt_mesh_comp_p2_record_pull(struct net_buf_simple *buf,
                                                           struct bt_mesh_comp_p2_record *record);

int bt_mesh_key_idx_unpack_list(struct net_buf_simple *buf, uint16_t *dst_arr, size_t *dst_cnt);

extern const struct bt_mesh_model_op bt_mesh_cfg_cli_op[];
extern const struct bt_mesh_model_cb bt_mesh_cfg_cli_cb;

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_CFG_CLI_H_ */
```

## 88.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 340 行

用于跟踪消息响应的内部参数（Internal parameters）。

### 注释 3：原第 1849 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_CFG_CLI_H_`。

## 88.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [bt_mesh_cfg_cli](../bluetooth_mesh_model_reference/P027_bt_mesh_cfg_cli_结构体.md)
- [bt_mesh_cfg_cli_hb_pub](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md)
- [bt_mesh_cfg_cli_hb_sub](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md)
- [bt_mesh_cfg_cli_mod_pub](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md)
- [bt_mesh_cfg_cli_cb](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md)
- [comp_data](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#aaae4e3f64e2033a466ad87d362ceb318)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [mod_pub_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#ab4130e909826aa7746092f49f8b4c52e)
- [mod_sub_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#af4a43f4c65d111e95211b715048534cc)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mod_sub_list](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a0ad46d1d4793577679f66c62175e14cf)
- [node_reset_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#acf88660364760442dfab5280ae735d2d)
- [beacon_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a5cf2c17a88c53c514fcaa73a6fd81b67)
- [ttl_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#ab937311c41af68b1cd52a8a1c86145b1)
- [friend_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a9487a159a6c838a9218b3d76fa53248d)
- [gatt_proxy_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a6ef3730e9469bffd81cdd49c50cac7d5)
- [network_transmit_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#ad46ea40b75cc1d5d314fdefdca0076f8)
- [relay_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a89eab453e00662f6f3f8a5d78f20d120)
- [net_key_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a49a7a8cab34bb70d2edd87b0017f1cf7)
- [net_key_list](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#acce08dfa5cb356a2203f0ef6c4e4bf5b)
- [app_key_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a48ef4d0665d86d069b90533eb18e0fd0)
- [app_key_list](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#ac331fc103d0f331093929f39e5b9d6ba)
- [mod_app_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a3ccff69f21e0f3c585b951eb60c1bf5c)
- [mod_app_list](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#abf8501e73f44ab5ea7e54b8f2ff1f866)
- [node_identity_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#aca2d779401fa4521813e6578bd3bbd91)
- [lpn_timeout_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a66b5a8dd3bdd2468fe65496020b13495)
- [krp_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a4d89033676eb4570cdd80f1715fd9bfb)
- [hb_pub_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a615852027a841b1779a50c9fd50bef6a)
- [hb_sub_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#aa60dfd72a43273e1ffae2160bcc0845d)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [model](../bluetooth_mesh_model_reference/P027_bt_mesh_cfg_cli_结构体.md#a525dd5391c83c525c012940575245cea)
- [cb](../bluetooth_mesh_model_reference/P027_bt_mesh_cfg_cli_结构体.md#a7160cf5d22fa0b909482bbc76f27b6bd)
- [bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)
- [ack_ctx](../bluetooth_mesh_model_reference/P027_bt_mesh_cfg_cli_结构体.md#a472bf5015857ab97e1a40ab6cfa70bb1)
- [addr](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#ab52dd35df271ae5bd70a4640e6f3bea8)
- [uuid](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#a29cbd50ad33f25ad3b98b4ec7ac56a6c)
- [app_idx](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#aefbe5449a10379b064dea054300cb9a0)
- [cred_flag](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#aa7452f697410fdf8a63808bcb29c53ee)
- [ttl](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#a9513db038ec4f51734892bd1ce7d08f3)
- [period](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#a104afe2b8d9766e037293b09c0c1b91c)
- [transmit](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#a2a5a0ead8155bf971c84f73dfa4ec282)
- [src](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md#a01ec0c3cab7bb7ed76d7728390eb4f25)
- [dst](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md#abc9ea18fbe86c260d6cf5d53c26a0248)
- [period](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md#a5a75c924f0868c664652503335b1b012)
- [count](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md#a93624ab6c8a0c15c0b50490e0fcd3675)
- [min](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md#a480b214e0e1974a6a54426c49e5d62d1)
- [max](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md#aac96c2ab606e38f412e94539795c5594)
- [dst](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md#a473df7dd958683d7502dcc983c4ceb8a)
- [count](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md#a13c7c155f30ca94d30090a25df50e4b2)
- [period](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md#a8d17dd2df4be23cadad4b5746ddb50ad)
- [ttl](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md#ac7f24f7bf942587ef83ca47d9ee4e7fb)
- [feat](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md#a94598c9b733075abe22d70f62293b5a1)
- [net_idx](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md#a90a79d8b7ea91c6ba872dca15d87b356)
- [bt_mesh_cfg_cli_node_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac6675d227749a69cedc5455c70626b76)
- [bt_mesh_cfg_cli_comp_data_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga36259e9c811a8f1a21d642739cf297df)
- [bt_mesh_cfg_cli_beacon_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2c8a79d1b70e91e0a09c848737bb4a22)
- [bt_mesh_cfg_cli_krp_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga660df68049110332ff21610fe4e520c6)
- [bt_mesh_cfg_cli_krp_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gae51eee59090cfebed4561ed3bb4df005)
- [bt_mesh_cfg_cli_beacon_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gab513c82ebe434907a958cc6da990bd0b)
- [bt_mesh_cfg_cli_ttl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa141d4aabbed6c7780ac7f3955c8b580)
- [bt_mesh_cfg_cli_ttl_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2671234d739c802fd080a19d01235352)
- [bt_mesh_cfg_cli_friend_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga4dd1534e9d5b04fc99231ba5dde23e05)
- [bt_mesh_cfg_cli_friend_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gacf8ad783910449c7cdc304c1b9b3fe0b)
- [bt_mesh_cfg_cli_gatt_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaaf945377cf6a3d2b3e7c7cdb5a8df016)
- [bt_mesh_cfg_cli_gatt_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga5a717835a416ba2930f65a975265649f)
- [bt_mesh_cfg_cli_net_transmit_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga92ee7984b14590ed11a470c0dfea0bc9)
- [bt_mesh_cfg_cli_net_transmit_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga87f7c1e06b5c721c89031c527960bf40)
- [bt_mesh_cfg_cli_relay_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga4a50a6a5dcfdc42b7476f0b9e463ea45)
- [bt_mesh_cfg_cli_relay_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga7fe8418130568bdf2a5e56ed2ad027b0)
- [bt_mesh_cfg_cli_net_key_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga283fb06ddb6427852ff0ac556d3c1852)
- [bt_mesh_cfg_cli_net_key_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gab42c5bdff36bea35e967946462b12457)
- [bt_mesh_cfg_cli_net_key_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gab2963ec5536cb4b941578bb490fdc013)
- [bt_mesh_cfg_cli_app_key_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gafabf4c0fa707eba1fd40cc9a403daa07)
- [bt_mesh_cfg_cli_app_key_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga6391ce297ca0be73ccd51044a9e0a76f)
- [bt_mesh_cfg_cli_app_key_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga5140472c687584babf885bc08349c865)
- [bt_mesh_cfg_cli_mod_app_bind](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa4a02dd0c1f67621ee71d011fe4a29c1)
- [bt_mesh_cfg_cli_mod_app_unbind](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf82b54a4b2d3176b10daf728272a0977)
- [bt_mesh_cfg_cli_mod_app_bind_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gada33602562721c9f413eb06b34a823a8)
- [bt_mesh_cfg_cli_mod_app_unbind_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1fb53b9a49be25e633cac9d668c5b209)
- [bt_mesh_cfg_cli_mod_app_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga67cf5ff993f2444cc66b2ae5353865d2)
- [bt_mesh_cfg_cli_mod_app_get_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf7e0f85bbbbfc382bfe4aea8298227d1)
- [bt_mesh_cfg_cli_mod_pub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1b36596a20ca8751006b0f7f2221067d)
- [bt_mesh_cfg_cli_mod_pub_get_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga0bc2c24403e0cd79a061ba1244b1a1db)
- [bt_mesh_cfg_cli_mod_pub_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga7fc2acda16f3f03a929c38796c67028e)
- [bt_mesh_cfg_cli_mod_pub_set_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gad2c602a2685ff38c0e78c1990b244e54)
- [bt_mesh_cfg_cli_mod_sub_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf4ee720ce27eea9602b59a380278bb57)
- [bt_mesh_cfg_cli_mod_sub_add_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga3ba34f8be138bc62a7eb7859b18dc441)
- [bt_mesh_cfg_cli_mod_sub_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga8d8595f077267b7d784fde30cbc4b207)
- [bt_mesh_cfg_cli_mod_sub_del_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga74bad73184af2d6ce71134831f70680d)
- [bt_mesh_cfg_cli_mod_sub_overwrite](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gadac1cc360c30d290a861bbd534fca58d)
- [bt_mesh_cfg_cli_mod_sub_overwrite_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga69b2dfacc27ed94b9e1331ff4ac4b582)
- [bt_mesh_cfg_cli_mod_sub_va_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2d22612cf9dc5030699bf7c6c58bf6d5)
- [bt_mesh_cfg_cli_mod_sub_va_add_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa3a10a54a18a99d0b4b0aa85330b1640)
- [bt_mesh_cfg_cli_mod_sub_va_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf7107373fc0c70d091e9a521d8b641ad)
- [bt_mesh_cfg_cli_mod_sub_va_del_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga8884786e3ec349bcb8b89b60aa11f198)
- [bt_mesh_cfg_cli_mod_sub_va_overwrite](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga69809ad3f2cff8e1f394f6da6ed63264)
- [bt_mesh_cfg_cli_mod_sub_va_overwrite_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga70d3bb7fb914fa3685f4ad9b561a48b6)
- [bt_mesh_cfg_cli_mod_sub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf739e5e3a4b225e10bf2aedf143d7793)
- [bt_mesh_cfg_cli_mod_sub_get_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga09e751a9071402ae978c0355edfbdf03)
- [bt_mesh_cfg_cli_hb_sub_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1adae658bf8f4512a7d80d0194dcb362)
- [bt_mesh_cfg_cli_hb_sub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga86e5de1b216d62b7c77bf43b7af062fc)
- [bt_mesh_cfg_cli_hb_pub_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga352eb00b78ff978a1a1e81ec5a0575b8)
- [bt_mesh_cfg_cli_hb_pub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga07c443476adef9c7bb573ffbb8d1b1ce)
- [bt_mesh_cfg_cli_mod_sub_del_all](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gacd647905484fa8319a5377aa5777c254)
- [bt_mesh_cfg_cli_mod_sub_del_all_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga2059ccbc689af9c2127e4e399ea5bd43)
- [bt_mesh_cfg_cli_net_key_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gafdaff279685b821a7b205e45feed9a05)
- [bt_mesh_cfg_cli_app_key_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gacf1bd7a771a45981a82eeea0dcce01b7)
- [bt_mesh_cfg_cli_node_identity_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga12a8618d2b73f30742f8e8d2bdddc138)
- [bt_mesh_cfg_cli_node_identity_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac02c170e260980d5b749b581910672d2)
- [bt_mesh_cfg_cli_lpn_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga0ee1d0849d632b5d806ee31c87bbc888)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_cfg_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaf5262c0a27e4b9249ecf908c259cc7d7)
- [bt_mesh_cfg_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga7e3521ae973dc825422c6dd5f07ef547)
- [bt_mesh_comp_p0](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md)
- [cid](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md#a3ed8f5ac643443bbcca308baff1c539c)
- [pid](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md#a009806e046583c99f56d271ecebbb8a3)
- [vid](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md#a27d910cdeb7b6b9d038898e3824dfb57)
- [crpl](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md#a32bfead26f338aba892a5459615a65a2)
- [feat](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md#a0a44e3778f9d134a5c056ca184c3b527)
- [bt_mesh_comp_p0_elem](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md)
- [loc](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md#a832cdb0a10d364a048971f59f51e841d)
- [nsig](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md#a17f61eab2df28f2031f2fbab28254484)
- [nvnd](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md#a2e1bd3146ebc934e9fab0242a06d5b99)
- [bt_mesh_comp_p0_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1f79d98273a984f1c49b4d5dd5bf8d30)
- [bt_mesh_comp_p0_elem_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa6d60ebad6dc4a4f5b022937dbae3120)
- [bt_mesh_comp_p0_elem_mod](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac005f52e191c3e5628f063dbc1a19645)
- [bt_mesh_mod_id_vnd](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md)
- [bt_mesh_comp_p0_elem_mod_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga4f656102982961b7bf2e3d3896a2240e)
- [bt_mesh_comp_p1_elem](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md)
- [nsig](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md#aa6aa100992502cef0484a127224cf07b)
- [nvnd](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md#a25492ac30a362e4490d11169ed98197b)
- [bt_mesh_comp_p1_model_item](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md)
- [cor_present](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md#aee352e8563133dddbb37c1f31dfe7c09)
- [format](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md#af2f213813440cb4a87884e3625a704e7)
- [ext_item_cnt](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md#ae019a211eafeb20f323ad97328d938f7)
- [cor_id](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md#a95baa1acf3a82e8559ce4a47b7e03be8)
- [bt_mesh_comp_p1_item_short](../bluetooth_mesh_model_reference/P040_bt_mesh_comp_p1_item_short_结构体.md)
- [elem_offset](../bluetooth_mesh_model_reference/P040_bt_mesh_comp_p1_item_short_结构体.md#a1fb6c8134a2c02e3b83dfea12ab39410)
- [mod_item_idx](../bluetooth_mesh_model_reference/P040_bt_mesh_comp_p1_item_short_结构体.md#a7e2152fe608c52cbc0700a43a5653132)
- [bt_mesh_comp_p1_item_long](../bluetooth_mesh_model_reference/P039_bt_mesh_comp_p1_item_long_结构体.md)
- [elem_offset](../bluetooth_mesh_model_reference/P039_bt_mesh_comp_p1_item_long_结构体.md#a12a0e2fb373e2e43b7c04a1130cdf018)
- [mod_item_idx](../bluetooth_mesh_model_reference/P039_bt_mesh_comp_p1_item_long_结构体.md#a61d541854c2d1671c60fc444978f0374)
- [bt_mesh_comp_p1_ext_item](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md)
- [SHORT](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md#a05a526a8448e7b8a4766eb038e4c1a39a23a15546d8722d7a4706ea34c5785658)
- [LONG](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md#a05a526a8448e7b8a4766eb038e4c1a39ae96bb3e960c4d2c356c0070f34740119)
- [type](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md#a43f50f35690e54d3680a6daa989ce1c0)
- [short_item](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md#ae17176001203ee8c282f06e994cee647)
- [long_item](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md#a3962046fc095348035a193dad60d1149)
- [bt_mesh_comp_p1_elem_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gae9a19b089d898af914ea5c287aca8fba)
- [bt_mesh_comp_p1_item_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac8b4b670c82b80a51834f7ef32206985)
- [bt_mesh_comp_p1_pull_ext_item](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gac527fe27308c8a61ac1831af9605e429)
- [bt_mesh_comp_p2_record](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md)
- [id](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#a4d947193b1a0f46c9df1eca298135646)
- [x](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#a5377ce835db8ce408d8dabfd87c858f5)
- [y](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#a0ceff9becd0eb14ca190c49f56ec0957)
- [z](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#a90e80906ef6d2b8b932215ad183db2d5)
- [version](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#aa718c024d6ce339ac8c352319b878c53)
- [elem_buf](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#ad310f8c8e3a167492a6e698336b7f400)
- [data_buf](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#abd0975a47c848265ad13044dfcd3b78d)
- [bt_mesh_comp_p2_record_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga0854a494707a40b84beb8582f45e0470)
- [bt_mesh_key_idx_unpack_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#gaa411ab7db2e71a114a8108eaec9ca12c)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [bt_mesh_cfg_cli_cb::mod_sub_list](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a0ad46d1d4793577679f66c62175e14cf)
- [bt_mesh_cfg_cli_cb::mod_app_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a3ccff69f21e0f3c585b951eb60c1bf5c)
- [bt_mesh_cfg_cli_cb::app_key_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a48ef4d0665d86d069b90533eb18e0fd0)
- [bt_mesh_cfg_cli_cb::net_key_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a49a7a8cab34bb70d2edd87b0017f1cf7)
- [bt_mesh_cfg_cli_cb::krp_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a4d89033676eb4570cdd80f1715fd9bfb)
- [bt_mesh_cfg_cli_cb::beacon_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a5cf2c17a88c53c514fcaa73a6fd81b67)
- [bt_mesh_cfg_cli_cb::hb_pub_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a615852027a841b1779a50c9fd50bef6a)
- [bt_mesh_cfg_cli_cb::lpn_timeout_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a66b5a8dd3bdd2468fe65496020b13495)
- [bt_mesh_cfg_cli_cb::gatt_proxy_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a6ef3730e9469bffd81cdd49c50cac7d5)
- [bt_mesh_cfg_cli_cb::relay_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a89eab453e00662f6f3f8a5d78f20d120)
- [bt_mesh_cfg_cli_cb::friend_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#a9487a159a6c838a9218b3d76fa53248d)
- [bt_mesh_cfg_cli_cb::hb_sub_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#aa60dfd72a43273e1ffae2160bcc0845d)
- [bt_mesh_cfg_cli_cb::comp_data](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#aaae4e3f64e2033a466ad87d362ceb318)
- [bt_mesh_cfg_cli_cb::mod_pub_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#ab4130e909826aa7746092f49f8b4c52e)
- [bt_mesh_cfg_cli_cb::ttl_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#ab937311c41af68b1cd52a8a1c86145b1)
- [bt_mesh_cfg_cli_cb::mod_app_list](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#abf8501e73f44ab5ea7e54b8f2ff1f866)
- [bt_mesh_cfg_cli_cb::app_key_list](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#ac331fc103d0f331093929f39e5b9d6ba)
- [bt_mesh_cfg_cli_cb::node_identity_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#aca2d779401fa4521813e6578bd3bbd91)
- [bt_mesh_cfg_cli_cb::net_key_list](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#acce08dfa5cb356a2203f0ef6c4e4bf5b)
- [bt_mesh_cfg_cli_cb::node_reset_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#acf88660364760442dfab5280ae735d2d)
- [bt_mesh_cfg_cli_cb::network_transmit_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#ad46ea40b75cc1d5d314fdefdca0076f8)
- [bt_mesh_cfg_cli_cb::mod_sub_status](../bluetooth_mesh_model_reference/P028_bt_mesh_cfg_cli_cb_结构体.md#af4a43f4c65d111e95211b715048534cc)
- [bt_mesh_cfg_cli_hb_pub::count](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md#a13c7c155f30ca94d30090a25df50e4b2)
- [bt_mesh_cfg_cli_hb_pub::dst](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md#a473df7dd958683d7502dcc983c4ceb8a)
- [bt_mesh_cfg_cli_hb_pub::period](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md#a8d17dd2df4be23cadad4b5746ddb50ad)
- [bt_mesh_cfg_cli_hb_pub::net_idx](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md#a90a79d8b7ea91c6ba872dca15d87b356)
- [bt_mesh_cfg_cli_hb_pub::feat](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md#a94598c9b733075abe22d70f62293b5a1)
- [bt_mesh_cfg_cli_hb_pub::ttl](../bluetooth_mesh_model_reference/P029_bt_mesh_cfg_cli_hb_pub_结构体.md#ac7f24f7bf942587ef83ca47d9ee4e7fb)
- [bt_mesh_cfg_cli_hb_sub::src](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md#a01ec0c3cab7bb7ed76d7728390eb4f25)
- [bt_mesh_cfg_cli_hb_sub::min](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md#a480b214e0e1974a6a54426c49e5d62d1)
- [bt_mesh_cfg_cli_hb_sub::period](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md#a5a75c924f0868c664652503335b1b012)
- [bt_mesh_cfg_cli_hb_sub::count](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md#a93624ab6c8a0c15c0b50490e0fcd3675)
- [bt_mesh_cfg_cli_hb_sub::max](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md#aac96c2ab606e38f412e94539795c5594)
- [bt_mesh_cfg_cli_hb_sub::dst](../bluetooth_mesh_model_reference/P030_bt_mesh_cfg_cli_hb_sub_结构体.md#abc9ea18fbe86c260d6cf5d53c26a0248)
- [bt_mesh_cfg_cli_mod_pub::period](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#a104afe2b8d9766e037293b09c0c1b91c)
- [bt_mesh_cfg_cli_mod_pub::uuid](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#a29cbd50ad33f25ad3b98b4ec7ac56a6c)
- [bt_mesh_cfg_cli_mod_pub::transmit](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#a2a5a0ead8155bf971c84f73dfa4ec282)
- [bt_mesh_cfg_cli_mod_pub::ttl](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#a9513db038ec4f51734892bd1ce7d08f3)
- [bt_mesh_cfg_cli_mod_pub::cred_flag](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#aa7452f697410fdf8a63808bcb29c53ee)
- [bt_mesh_cfg_cli_mod_pub::addr](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#ab52dd35df271ae5bd70a4640e6f3bea8)
- [bt_mesh_cfg_cli_mod_pub::app_idx](../bluetooth_mesh_model_reference/P031_bt_mesh_cfg_cli_mod_pub_结构体.md#aefbe5449a10379b064dea054300cb9a0)
- [bt_mesh_cfg_cli::ack_ctx](../bluetooth_mesh_model_reference/P027_bt_mesh_cfg_cli_结构体.md#a472bf5015857ab97e1a40ab6cfa70bb1)
- [bt_mesh_cfg_cli::model](../bluetooth_mesh_model_reference/P027_bt_mesh_cfg_cli_结构体.md#a525dd5391c83c525c012940575245cea)
- [bt_mesh_cfg_cli::cb](../bluetooth_mesh_model_reference/P027_bt_mesh_cfg_cli_结构体.md#a7160cf5d22fa0b909482bbc76f27b6bd)
- [bt_mesh_comp_p0_elem::nsig](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md#a17f61eab2df28f2031f2fbab28254484)
- [bt_mesh_comp_p0_elem::nvnd](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md#a2e1bd3146ebc934e9fab0242a06d5b99)
- [bt_mesh_comp_p0_elem::loc](../bluetooth_mesh_model_reference/P036_bt_mesh_comp_p0_elem_结构体.md#a832cdb0a10d364a048971f59f51e841d)
- [bt_mesh_comp_p0::pid](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md#a009806e046583c99f56d271ecebbb8a3)
- [bt_mesh_comp_p0::feat](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md#a0a44e3778f9d134a5c056ca184c3b527)
- [bt_mesh_comp_p0::vid](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md#a27d910cdeb7b6b9d038898e3824dfb57)
- [bt_mesh_comp_p0::crpl](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md#a32bfead26f338aba892a5459615a65a2)
- [bt_mesh_comp_p0::cid](../bluetooth_mesh_model_reference/P035_bt_mesh_comp_p0_结构体.md#a3ed8f5ac643443bbcca308baff1c539c)
- [bt_mesh_comp_p1_elem::nvnd](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md#a25492ac30a362e4490d11169ed98197b)
- [bt_mesh_comp_p1_elem::nsig](../bluetooth_mesh_model_reference/P037_bt_mesh_comp_p1_elem_结构体.md#aa6aa100992502cef0484a127224cf07b)
- [bt_mesh_comp_p1_ext_item::SHORT](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md#a05a526a8448e7b8a4766eb038e4c1a39a23a15546d8722d7a4706ea34c5785658)
- [bt_mesh_comp_p1_ext_item::LONG](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md#a05a526a8448e7b8a4766eb038e4c1a39ae96bb3e960c4d2c356c0070f34740119)
- [bt_mesh_comp_p1_ext_item::long_item](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md#a3962046fc095348035a193dad60d1149)
- [bt_mesh_comp_p1_ext_item::type](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md#a43f50f35690e54d3680a6daa989ce1c0)
- [bt_mesh_comp_p1_ext_item::short_item](../bluetooth_mesh_model_reference/P038_bt_mesh_comp_p1_ext_item_结构体.md#ae17176001203ee8c282f06e994cee647)
- [bt_mesh_comp_p1_item_long::elem_offset](../bluetooth_mesh_model_reference/P039_bt_mesh_comp_p1_item_long_结构体.md#a12a0e2fb373e2e43b7c04a1130cdf018)
- [bt_mesh_comp_p1_item_long::mod_item_idx](../bluetooth_mesh_model_reference/P039_bt_mesh_comp_p1_item_long_结构体.md#a61d541854c2d1671c60fc444978f0374)
- [bt_mesh_comp_p1_item_short::elem_offset](../bluetooth_mesh_model_reference/P040_bt_mesh_comp_p1_item_short_结构体.md#a1fb6c8134a2c02e3b83dfea12ab39410)
- [bt_mesh_comp_p1_item_short::mod_item_idx](../bluetooth_mesh_model_reference/P040_bt_mesh_comp_p1_item_short_结构体.md#a7e2152fe608c52cbc0700a43a5653132)
- [bt_mesh_comp_p1_model_item::cor_id](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md#a95baa1acf3a82e8559ce4a47b7e03be8)
- [bt_mesh_comp_p1_model_item::ext_item_cnt](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md#ae019a211eafeb20f323ad97328d938f7)
- [bt_mesh_comp_p1_model_item::cor_present](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md#aee352e8563133dddbb37c1f31dfe7c09)
- [bt_mesh_comp_p1_model_item::format](../bluetooth_mesh_model_reference/P041_bt_mesh_comp_p1_model_item_结构体.md#af2f213813440cb4a87884e3625a704e7)
- [bt_mesh_comp_p2_record::y](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#a0ceff9becd0eb14ca190c49f56ec0957)
- [bt_mesh_comp_p2_record::id](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#a4d947193b1a0f46c9df1eca298135646)
- [bt_mesh_comp_p2_record::x](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#a5377ce835db8ce408d8dabfd87c858f5)
- [bt_mesh_comp_p2_record::z](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#a90e80906ef6d2b8b932215ad183db2d5)
- [bt_mesh_comp_p2_record::version](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#aa718c024d6ce339ac8c352319b878c53)
- [bt_mesh_comp_p2_record::data_buf](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#abd0975a47c848265ad13044dfcd3b78d)
- [bt_mesh_comp_p2_record::elem_buf](../bluetooth_mesh_model_reference/P042_bt_mesh_comp_p2_record_结构体.md#ad310f8c8e3a167492a6e698336b7f400)

---

[上一章](P087_cfb.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P089_cfg_srv.h_源码浏览.md)
