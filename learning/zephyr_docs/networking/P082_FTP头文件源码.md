---
id: learning.zephyr-docs.networking.api-82
title: FTP头文件源码
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ftp__client_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_FTP头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ftp__client_8h_source.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 82.1\_阅读说明与来源

译注：先读[FTP客户端库](P075_FTP客户端库.md)和[客户端示例](P076_FTP客户端示例.md)，再按接口查询本组参考。

本组：[完整API参考](P080_FTP完整API参考.md) · [头文件参考](P081_FTP头文件参考.md) · [头文件源码](P082_FTP头文件源码.md)。

下方保留官方源码浏览页展示的全部代码、标识符、声明及版权／许可注释。仅移除网页行号，将展示用不换行空格还原为普通空格，并清除行尾空白。原页面已省略部分生成API文档的注释，因此行号原本存在跳跃；这不是完整原始头文件的替代品。接口注释译文见本组API及结构体页。

## 82.2\_原始源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00078"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="foldopen00250"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="foldopen00256"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="foldopen00271"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="agroup__ftp__client_html_ga1021a2168ba8e0955637807fdef4d692"></a>
<a id="agroup__ftp__client_html_ga132a310c8f7854623f203f7cddb53b76"></a>
<a id="agroup__ftp__client_html_ga133d01a5122050e71b9164b631347345"></a>
<a id="agroup__ftp__client_html_ga1fd1b76dd9faa02fdb72440c94851c9f"></a>
<a id="agroup__ftp__client_html_ga454863be9cb65d02ac59580f468ab355"></a>
<a id="agroup__ftp__client_html_ga488cc79e627f7974bb097a9ac54aaaf9"></a>
<a id="agroup__ftp__client_html_ga5d2fbddcb382dc2c4b082b32cb28ef82"></a>
<a id="agroup__ftp__client_html_ga6b7e18f2c7197825a0c8e7ea8128e628"></a>
<a id="agroup__ftp__client_html_ga7e44297d4ffa3dda684e8fe09a2f30d1"></a>
<a id="agroup__ftp__client_html_ga7e821b21f05c5366eac8fef730b7df5f"></a>
<a id="agroup__ftp__client_html_ga9c35334bbe9e0c7d86de7fea470e3742"></a>
<a id="agroup__ftp__client_html_gaaa49d1b2dc6c033285c36a745a7a988c"></a>
<a id="agroup__ftp__client_html_gaabd04bf684f643ce5e313c474f0bf33c"></a>
<a id="agroup__ftp__client_html_gab254efce8f6874498e577a05c5a05f28"></a>
<a id="agroup__ftp__client_html_gabaa6663c007b7e8c3d508b31d28d71ee"></a>
<a id="agroup__ftp__client_html_gac057b5a49b9788cae46b49d5a7e2a355"></a>
<a id="agroup__ftp__client_html_gacc35656664b3efeee20ec89c0e50e093"></a>
<a id="agroup__ftp__client_html_gad2e0517bed675c54f69e457815935da5"></a>
<a id="agroup__ftp__client_html_gad7aec38daf5f8595905293a9e52b217a"></a>
<a id="agroup__ftp__client_html_gadda7bc4206bc8a6b22be619b1ea0ecd8"></a>
<a id="agroup__ftp__client_html_gaf9f99979b6178b195574135e30146b51"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa01b4a58ab89cce0c7601fa12fe5c54f5"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa023293f5c686359a71ab467f34596452"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa02735b72822fed42af9addaa19da4afc"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa0c463837a30fc056dda3fd6861e08b8e"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa0f31db3b37502fa7fe35d9b4c3614bc8"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa1972ccdb2117b1fce8b07c6ce01c63f5"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa19a33a1e0797be0043bd601b14d8f26e"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa1d161d26f45fb34f92a3d90eb085ac43"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa1dd9d9d393289ec8c3b1637063124498"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa20be33d647b863ba7cf1a911ad5e890d"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa21038c2632abf047794844f8ad4745b3"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa24b50796bd736f92fd5cd699ffda309b"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa262af9766c244af4c48c2138d6ca69ee"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa2b00435a0c116dfdde586e9ba5ecee64"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa2b30ed8b504cd9c3934a7380ca9305dd"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa2c51597ca89a0c956da2dfde9c9ff189"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa2ecbe59151d8857b2069ef129ffb7124"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa30af249b9321a12f3afecd91d7a4c878"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa3413c670d2c6d7acf4db6ba32a1e65c8"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa362887c01cef49c24f857cb44b50745f"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa3812aa7f26553556d43e9de2e7334fb8"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa41addb3c6db5be11eff8b31bd95af73c"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa4a098c006025387894a44e98710ccfd4"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa4b2b8ebe26117024353db6839e965611"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa4b5ebacbf400d5cfa5becdb652bde3a1"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa4ce31dbbe2e3aa1829b33e26835198d6"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa50a6fe48a902b0ef77ca1edae9f3b621"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa57e289509dca21af5fa78a61fc787085"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa5c343ab624f0c93014d45b563caab935"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa5e9d356354c7ba6f71aaf662e500d921"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa5f6630cabd8f3164f9529514a2228a4b"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa61a8a385cf84bac33d4c5a8674698ab8"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa63f4ed70304926d9401d07df5b947fac"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa64748b689db68fa0cb339dd05a9c7d5f"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa67c57b5668c76e059122b5cef1f5aa7c"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa6861e5ca7f670c4535c068222564dca1"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa6f0da4302c0c47b9950a9638824b9071"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa73ea1be785d44a4295ed6a75d5f6dfb5"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa80e8cd999e1444210404fd6777297050"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa8d01634d86ff6225ccd632474c3ba24e"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa8e91f38038fb2845ed2cf1bb11633e06"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa9021858f8f1fb75455808cbe2858fe6d"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fa923d41feabbfabbf07d2af4b53c4f7e2"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9faa20686c639dd8ad6b8c34d3bcf81aa08"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9faa3cf4061361db61705d267161d8e2299"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9faa8ba47771c6ecc429e3f0249b2991853"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fab529849ab3807fedf4d1f8e5a4ef0f8e"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fab746dd2a6dbb241c7708876b068a0b3a"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9facb4dbe7ad6b21b3035c9dfaa4c6bd606"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9facb625cec2d6adf0acf4cabf1566a36b6"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9facff17031b4639ddc19969ea0fd46cb37"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fad1e65f88caad7e6410bd042405edebd2"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fad3170f0654f4125bb2283a5647111989"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fad57f89f9c561f2a11537d87943bbcb0f"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fad62ed521671902a07306f8693f57ad12"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fad775cb9ff8cc9e276b2da42a2411f7db"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fadba5c377a8a199036028342f23ff4efd"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fadc7cded100e930866d3d4688654261c9"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fae71d394182c338b54cb54fb43601efdc"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9faeb89d65f6cd5a982dfae8cca5e4caa4b"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9faf0d941ddc9c7cbbd331967bc89f56936"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9faf90ecdd5446eff36c6eee2bf217c47e3"></a>
<a id="agroup__ftp__client_html_gga1fd1b76dd9faa02fdb72440c94851c9fafe9ff46b8d55d6e49387182cbbc020f3"></a>
<a id="agroup__ftp__client_html_ggad2e0517bed675c54f69e457815935da5a3a21938d02227ad37c1fcad3cda67039"></a>
<a id="agroup__ftp__client_html_ggad2e0517bed675c54f69e457815935da5ab3a051eff6a65236e97811716b2ae9ff"></a>
<a id="agroup__ftp__client_html_ggaf9f99979b6178b195574135e30146b51a1daa8fd6fb897bb0b6bedcd95b257d53"></a>
<a id="agroup__ftp__client_html_ggaf9f99979b6178b195574135e30146b51a64c12215f266804fd8d64112ca11d56e"></a>
<a id="agroup__ftp__client_html_ggaf9f99979b6178b195574135e30146b51a86668e9c2d6905f8f270f353a015fc7d"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructftp__client_html"></a>
<a id="astructftp__client_html_a060735326fac26d737f0a4e2a32afcff"></a>
<a id="astructftp__client_html_a13b8191a83a656f96dd2d9d9352f08eb"></a>
<a id="astructftp__client_html_a19824800556b11ce885f2ea1864ee906"></a>
<a id="astructftp__client_html_a46ff461b642c07682cee9e6a1b4561a8"></a>
<a id="astructftp__client_html_a6667e43b6ad4288dd5ebdc37157ebcd2"></a>
<a id="astructftp__client_html_ac3d681a1065fd1584fc7fac1f9dc93c1"></a>
<a id="astructftp__client_html_acd13724b1c049a5fc48008bc3a65048f"></a>
<a id="astructftp__client_html_ad8c19ebc3725b3af345eaa86e0fe3e6a"></a>
<a id="astructftp__client_html_aec64cc9ae3dc8541cbf11d31f289af73"></a>
<a id="astructftp__client_html_af1223e38213f9cb64052a83572115ff4"></a>
<a id="astructk__mutex_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructnet__sockaddr_html"></a>

```c
/*
 * Copyright (c) 2020-2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_FTP_CLIENT_H_
#define ZEPHYR_INCLUDE_NET_FTP_CLIENT_H_

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/net/net_ip.h>

#ifdef __cplusplus
extern "C" {
#endif


#if defined(CONFIG_FTP_CLIENT)
#define FTP_BUFFER_SIZE CONFIG_FTP_CLIENT_BUF_SIZE
#else
#define FTP_BUFFER_SIZE 1
#endif

enum ftp_reply_code {
        /* 100 Series   The requested action is being initiated, expect another
         * reply before proceeding with a new command
         */

        FTP_CODE_110_RESTART_MARKER_REPLAY = 110,
        FTP_CODE_120_SERVICE_READY_IN_NNN_MINUTES = 120,
        FTP_CODE_125_DATA_CONN_ALREADY_OPEN = 125,
        FTP_CODE_150_FILE_STATUS_OK = 150,

        /* 200 Series   The requested action has been successfully completed */

        FTP_CODE_200_OK = 200,
        FTP_CODE_202_NOT_IMPLEMENTED = 202,
        FTP_CODE_211_SYSTEM_STATUS = 211,
        FTP_CODE_212_DIR_STATUS = 212,
        FTP_CODE_213_FILE_STATUS = 213,
        FTP_CODE_214_HELP_MSG = 214,
        FTP_CODE_215_NAME_SYSTEM_TYPE = 215,
        FTP_CODE_220_SERVICE_READY = 220,
        FTP_CODE_221_SERVICE_CLOSING_CONN = 221,
        FTP_CODE_225_DATA_CONN_OPEN = 225,
        FTP_CODE_226_CLOSING_DATA_CONN_SUCCESS = 226,
        FTP_CODE_227_ENTERING_PASSIVE_MODE = 227,
        FTP_CODE_228_ENTERING_LONG_PASSIVE_MODE = 228,
        FTP_CODE_229_ENTERING_EXT_PASSIVE_MODE = 229,
        FTP_CODE_230_USER_LOGGED_IN = 230,
        FTP_CODE_231_USER_LOGGED_OUT = 231,
        FTP_CODE_233_LOGOUT_COMMAND_NOTED = 233,
        FTP_CODE_234_SECURITY_ACCEPTED = 234,
        FTP_CODE_250_FILE_ACTION_COMPLETED = 250,
        FTP_CODE_257_PATHNAME_CREATED = 257,

        /* 300 Series   The command has been accepted, but the requested action
         *is on hold, pending receipt of further information
         */

        FTP_CODE_331_USERNAME_OK_NEED_PASSWORD = 331,
        FTP_CODE_332_NEED_ACCOUNT = 332,
        FTP_CODE_350_FILE_ACTION_PENDING = 350,

        /* 400 Series   The command was not accepted and the requested action
         * did not take place, but the error condition is temporary and the
         * action may be requested again
         */

        FTP_CODE_421_SERVICE_UNAVAILABLE = 421,
        FTP_CODE_425_CANNOT_OPEN_DATA_CONN = 425,
        FTP_CODE_426_CONN_CLOSED = 426,
        FTP_CODE_430_INVALID_USERNAME_OR_PASSWORD = 430,
        FTP_CODE_434_HOST_UNAVAILABLE = 434,
        FTP_CODE_450_FILE_ACTION_NOT_TAKEN = 450,
        FTP_CODE_451_ACTION_ABORTED = 451,
        FTP_CODE_452_ACTION_NOT_TAKEN = 452,

        /* 500 Series   Syntax error, command unrecognized and the requested
         * action did not take place. This may include errors such as command
         * line too long
         */

        FTP_CODE_500_GENERAL_ERROR = 500,
        FTP_CODE_501_SYNTAX_ERROR = 501,
        FTP_CODE_502_COMMAND_NOT_COMPLETED = 502,
        FTP_CODE_503_BAD_SEQUENCE_OF_COMMANDS = 503,
        FTP_CODE_504_COMMAND_NOT_IMPLEMENTED = 504,
        FTP_CODE_530_NOT_LOGGED_IN = 530,
        FTP_CODE_532_NEED_ACCOUNT = 532,
        FTP_CODE_534_CANNOT_CONNECT_SSL_REQUIRED = 534,
        FTP_CODE_550_FILE_UNAVAILABLE = 550,
        FTP_CODE_551_PAGE_TYPE_UNKNOWN = 551,
        FTP_CODE_552_FILE_EXCEEDED_STORAGE_LOCATION = 552,
        FTP_CODE_553_FILE_NAME_NOT_ALLOWED = 553,

        /* Replies regarding confidentiality and integrity */

        FTP_CODE_631_INTEGRITY_PROTECTED_REPLY = 631,
        FTP_CODE_632_INT_AND_CONF_PROTECTED_REPLY = 632,
        FTP_CODE_633_CONFIDENTIALITY_PROTECTED_REPLY = 633,

        /* Proprietary reply codes */

        FTP_CODE_900_UNKNOWN_ERROR = 900,

        FTP_CODE_901_DISCONNECTED_BY_REMOTE = 901,
        FTP_CODE_902_CONNECTION_ABORTED = 902,
        FTP_CODE_903_SOCKET_POLL_ERROR = 903,
        FTP_CODE_904_UNEXPECTED_POLL_EVENT = 904,
        FTP_CODE_905_NETWORK_DOWN = 905,
        FTP_CODE_909_UNEXPECTED_ERROR = 909,

        /* Non-fatal errors */
        FTP_CODE_910_DATA_TRANSFER_TIMEOUT = 910,

        /* 10000 Series Common Winsock Error Codes[2] (These are not FTP
         * return codes)
         */

        FTP_CODE_10054_CONNECTION_RESET_BY_PEER = 10054,
        FTP_CODE_10060_CANNOT_CONNECT = 10060,
        FTP_CODE_10061_CONNECTION_REFUSED = 10061,
        FTP_CODE_10066_DIRECTORY_NOT_EMPTY = 10066,
        FTP_CODE_10068_TOO_MANY_USERS = 10068
};

#define FTP_PRELIMINARY_POS(code)       ((code) >= 100 && (code) < 200)
#define FTP_COMPLETION_POS(code)        ((code) >= 200 && (code) < 300)
#define FTP_INTERMEDIATE_POS(code)      ((code) >= 300 && (code) < 400)
#define FTP_TRANSIENT_NEG(code)         ((code) >= 400 && (code) < 500)
#define FTP_COMPLETION_NEG(code)        ((code) >= 500 && (code) < 600)
#define FTP_PROTECTED(code)             ((code) >= 600 && (code) < 700)
#define FTP_PROPRIETARY(code)           ((code) >= 900 && (code) < 1000)
#define FTP_WINSOCK_ERR(code)           ((code) >= 10000)

enum ftp_transfer_type {
        FTP_TYPE_ASCII,
        FTP_TYPE_BINARY,
};

enum ftp_put_type {
        FTP_PUT_NORMAL,
        FTP_PUT_UNIQUE,
        FTP_PUT_APPEND,
};

typedef void (*ftp_client_callback_t)(const uint8_t *msg, uint16_t len);

struct ftp_client {
        union {
                struct net_sockaddr_storage remote_addr;
                struct net_sockaddr remote;
        };
        bool connected;
        int ctrl_sock;
        int data_sock;
        int sec_tag;
        uint8_t ctrl_buf[FTP_BUFFER_SIZE];
        size_t ctrl_len;
        uint8_t data_buf[FTP_BUFFER_SIZE];
        ftp_client_callback_t ctrl_callback;
        ftp_client_callback_t data_callback;
        struct k_mutex lock;
        struct k_work_delayable keepalive_work;
};

int ftp_init(struct ftp_client *client, ftp_client_callback_t ctrl_callback,
             ftp_client_callback_t data_callback);

int ftp_uninit(struct ftp_client *client);

int ftp_open(struct ftp_client *client, const char *hostname, uint16_t port,
             int sec_tag);

int ftp_login(struct ftp_client *client, const char *username,
              const char *password);

int ftp_close(struct ftp_client *client);

int ftp_status(struct ftp_client *client);

int ftp_type(struct ftp_client *client, enum ftp_transfer_type type);

int ftp_pwd(struct ftp_client *client);

int ftp_list(struct ftp_client *client, const char *options, const char *target);

int ftp_cwd(struct ftp_client *client, const char *folder);

int ftp_mkd(struct ftp_client *client, const char *folder);

int ftp_rmd(struct ftp_client *client, const char *folder);

int ftp_rename(struct ftp_client *client, const char *old_name,
               const char *new_name);

int ftp_delete(struct ftp_client *client, const char *file);

int ftp_get(struct ftp_client *client, const char *file);

int ftp_put(struct ftp_client *client, const char *file, const uint8_t *data,
            uint16_t length, int type);

int ftp_keepalive(struct ftp_client *client);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_FTP_CLIENT_H_ */
```

## 82.3\_源码注释译文

版权：2020—2026年Nordic Semiconductor ASA；许可证标识为`Apache-2.0`。应答码分组注释如下：

| 分组 | 原注释译文 |
| --- | --- |
| 100系列 | 请求的操作正在启动；继续发送新命令之前应等待另一次应答。 |
| 200系列 | 请求的操作已成功完成。 |
| 300系列 | 命令已接受，但请求的操作暂缓，等待进一步信息。 |
| 400系列 | 命令未被接受，请求的操作未发生；错误条件是暂时的，可以再次请求该操作。 |
| 500系列 | 语法错误，命令无法识别，请求的操作未发生；也可能包括命令行过长等错误。 |
| 600系列 | 与机密性和完整性（Confidentiality and Integrity）有关的应答。 |
| 900系列 | 专用应答码（Proprietary Reply Codes）；其中后续的910项归于非致命错误（Non-fatal Errors）。 |
| 10000系列 | 常见Winsock错误码（Common Winsock Error Codes），原注释保留引用标记`[2]`；这些不是FTP返回码。 |

末尾`#endif`注释标明结束对应的头文件包含保护（Header Include Guard）。原始法律署名与许可证标识保持原样。

[上一章](P081_FTP头文件参考.md) · [返回大纲](大纲.md) · [下一章](P083_FTP客户端上下文.md)
