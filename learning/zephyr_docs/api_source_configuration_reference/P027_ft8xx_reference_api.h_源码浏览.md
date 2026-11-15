---
id: learning.zephyr-docs.api-source-configuration-reference.page-27
title: ft8xx_reference_api.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__reference__api_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_ft8xx\_reference\_api.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__reference__api_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__reference__api_8h.html)。

## 27.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00040"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00105"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
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
<a id="l00136"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="foldopen00153"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="foldopen00169"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="foldopen00184"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="foldopen00199"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="foldopen00221"></a>
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
<a id="foldopen00250"></a>
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
<a id="l00261"></a>
<a id="foldopen00305"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="foldopen00328"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="foldopen00355"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="foldopen00375"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00382"></a>
<a id="l00384"></a>
<a id="l00389"></a>
<a id="l00391"></a>
<a id="l00393"></a>
<a id="l00395"></a>
<a id="l00397"></a>
<a id="l00399"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
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
<a id="foldopen00573"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
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
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
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
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
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
<a id="l00663"></a>
<a id="foldopen00665"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
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
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00745"></a>
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
<a id="l00760"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="aft8xx__common_8h_html"></a>
<a id="aft8xx__copro_8h_html"></a>
<a id="aft8xx__dl_8h_html"></a>
<a id="aft8xx__memory_8h_html"></a>
<a id="agroup__device__model_html_ga39c760429534ef9ae77f3d996987cd2b"></a>
<a id="agroup__ft8xx__common_html_ga2c8c5d06b09549ab041bbff4612b4620"></a>
<a id="agroup__ft8xx__common_html_ga743c2d25f728451e98417b2ebcc9c722"></a>
<a id="agroup__ft8xx__common_html_gaa6d306b1e2701e0de415c64d33e575a4"></a>
<a id="agroup__ft8xx__common_html_gab8235ed0c0f7373628457fcf64e15fbd"></a>
<a id="agroup__ft8xx__common_html_gada8d996d58f0f46f3f56534ee0da4c68"></a>
<a id="agroup__ft8xx__common_html_gaed670a8410224f8f3970fad86705f513"></a>
<a id="agroup__ft8xx__copro_html_ga35d0500600e8c1d1df653952fab5d86c"></a>
<a id="agroup__ft8xx__copro_html_ga3605bc23d9555ac51fc6292cb6f2a02c"></a>
<a id="agroup__ft8xx__copro_html_ga3b9454e8a6a824bd87c675037047c069"></a>
<a id="agroup__ft8xx__copro_html_ga72e1feafde7bb230cd798ba23f414de9"></a>
<a id="agroup__ft8xx__copro_html_ga93e61278bacec915bb360244ab43dbb7"></a>
<a id="agroup__ft8xx__copro_html_ga9d4ab3b53e4e11433d9c6a0d3e6cd3ea"></a>
<a id="agroup__ft8xx__copro_html_gab47b9c79db405686168cf1516ea0a00d"></a>
<a id="agroup__ft8xx__copro_html_gab7f5a1ea24eb9db4ac0e0a4f3d58e7b9"></a>
<a id="agroup__ft8xx__copro_html_gac946f044f2fbb6381ea4af268084d828"></a>
<a id="agroup__ft8xx__copro_html_gacc68ff73da90a9c822185f2ceba5a910"></a>
<a id="agroup__ft8xx__copro_html_gafa5c3fe004456cfd531edf781c11c00d"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a0187a790b87eca35892431c600248e71"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a097806c1c7281e5cbaf0e992888c2e97"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a0a6dcbe431ec103262ee805acaee9897"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a0a864b5230c4ed04ac4a18f7e9c85af5"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a13f744aa7a089e177a36623239d12961"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a15006a5d2ab004ca8b5a9a75be095b5b"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a161a252ef247cad31f812c88fbfcdf6f"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a1745bb57bcf9872b308c49a151a43f1f"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a183fd00d406e113b8b72b8c5b5fc5880"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a1ca1c284f1f3e2ae75c4874f0c569c7c"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a1d01f5fe890a4d7670cf91a7cd48402f"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a23f9fdc1d48d6410fc600359842b16ea"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a245e5594218702bc2c30c1b50ec44329"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a2b36ffdd93c6f41bd08f732099608a99"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a2ba06eef07c7b881c2b331aa090329ed"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a2c4d02cf887f3ec87b99cd32ae8b355b"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a2f0f00e3bbd1b9f9fb09c9d2b65382d7"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a2f17cc86a455d13b2f92ada17319a94e"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a3179545d22570761b9bf0598ff24219a"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a3397b2a86a97997d01780d52ec23b84c"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a382043bf7f2381a4fad71adeae73db2d"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a386a6293cd82485934b3865bd3f1956b"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a3c6f1a0898055d4eec3ddfbde56f6a51"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a3d5e1b30a5d1889b14b77f8a4bfecf7b"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a424e4e6fb301bb6833a46f813fc5895a"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a43bcc194c075b385073ed73a562b8cfa"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a4411395eca792d4d23f63242fea6307e"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a46376ddea2bccf9e0af33d78a05f635a"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a4911a990964958a6e2bf4842e87ab101"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a4b3e903dfed68a7eb7f7734e18aca9e0"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a4f0e1449b7ab28bf29f52bf3544c442f"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a4f188f88f9a032fdb6f3c87ed352d4bb"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a4fbbc34adc25d9147f2a8007a537ddbd"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a5672933c464d2408ad0a6a046fddc1d2"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a5d365f03f5dcd630191f050963c4fc9c"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a65b43042fe7dbc44bd15fb472bba33a4"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a69b981de24b4da81175c9ac74c8454f5"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a6bcedb4e986dba59c0c689356022d992"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a70f721a708b36ef255270d02680e4e7f"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a7946c63f4dd93692634c08ec0b4657e4"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a7b46068735f066e0d2fa6a0ccb073001"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a7c4d1b3a4a5dc128d52fd91352342a70"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a7d9903cc3452f77287ce411c831e6567"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a7f8c3d2a08a68b741ded594eafbfaae4"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a83136b05a9a6f64867f39c50fb0079d2"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a86ba740c280900a1dd4273422b9ca8b6"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a87e989861d85d683c95e8de44f74f58b"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a8947fb21fa7a7fa4a26bdaea5dbe79c5"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a8ef80aeaaffd974b2e246ad15c98f916"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a99fc0fc08ee942b7783951674837d57d"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a9bce17c193b9c809bef0770bc65b37cf"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a9ded0eeda09a9cce3bf111c0a49dd391"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6a9f726cc401387bbe8aa3366047467688"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6aa2b46aa7465a2e38a9947e0b5868f6c7"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6aa2cb7424ec77d9a35179824cd2fecb47"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6aa31af794f56d1f4f831ef65c3daf1087"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6aa45d948244f4decd8863f5def65a78db"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6aa6461f2c17d723ecd672babedbb1e9fc"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6aa8c6fb57011ad08bf0a1d0b48eb5599a"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6aaf65490a7a4b55309bc8943b065eef17"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6aaf8bdfc1924c2269c9db3933499cd23c"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6ab62b5bbfdf948265ad10129ead4d8a63"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6ab66136540b44e2f37a0f920fbd3cbcc4"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6ab9bf90e77f7946d4466e3b8d444d64e4"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6abcd84b4d56e71b558a79f10d97b66ea1"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6ac159bfb8d704e46aa4be4859d1e476af"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6ac321e2d68978123ab259a2d84d186719"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6acd3161021e315e1a2f91f21ccdc48d8a"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6ada6b5afbed95413c1988131384c02b1b"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6ae02db7afd08bd1c06f6e1f9e06e81d33"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6ae14e09a184dbe44390ce7d5576b30d4c"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6ae95328740c30d541b4dc79466734306c"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6aec4e118a3fe1cf3e1f2b5df6b376a651"></a>
<a id="agroup__ft8xx__memory_html_gga3c885b333acd851fed4d74886656d2c6af7d0154293ba1228a0e04bb923bf9b39"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a03912bde6f4ad32381c50772b89ec2bc"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a0558ac04acd45a6bf1e9100ec3a0a278"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a086b28d18b9c49e51ef734c2f6e6ce21"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a0b2882f45164307c678cba35232bcbf9"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a0e712682bd8d083f0ee25b284c242cdf"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a104e72273989d38213fc070b4fd4a676"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a1190faa2c60e6a2dc8661eb7da7461c6"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a1f9721ea190d82af17332d60cb8eb795"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a206979e1f9edf49aca24f8afb07e7f48"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a22089e51c2e0e4d373589c398a54ca05"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a222e9d43895af76d103f9fbd09c40832"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a2a155f858da556270114a3f9d989ef85"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a2bb9ad22a0d93b7facb92f49be1ac63a"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a304779eb0c7eca705a3c9fbf3d23fdb2"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a32f5dfe4ebc13114ecf9336670f74a31"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a359efc1f478e7653bb567fcfa20fb575"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a369d654c43692ef193493063338888aa"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a3deeabcda1f9453dc2d865e8b19715a8"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a3f09f2fd706996b97173f587637aee53"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a43adc41a79ea8af3bbf769b796f7c223"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a4449f285050e761b3fd78feebefe4335"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a4e6013b98cf73db7e09b7952f1f29e5b"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a533ec4682d3b9649a59e012a53ab55de"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a54935aeb6c13623f68c5c74c3db722ff"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a5a21ce38ac3699f4c9e5f8f0e7bc8555"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a5d019d200409c2dd4b57f727afedf815"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a60dd200c41f58057d20169ff833d4f82"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a61e1d7c2e2ed9a0ee4b372dd9c7df63a"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a67e068b57d9917ba093bfb8b073cf712"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a68ae24f87a50c7790ac987c6e2ccab2b"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a6a0dee898cc286ec6a2f91536fb0c8b4"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a6ad1c0050228bfdfca87bca6a4a0a571"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a6e302da1712f086b26d08e46f7a9f1d1"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a71f116560ffc21a45eece099f0155e52"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a75c68657acd7582c3028f0802d155771"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a779e92fbc0655c0889a3760025f8880a"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a81b9c8fd550b60b9b4cd1aae7a97efb9"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a8366bdc17c88345c80aab6f061090312"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a83d5ff35dc2d6af8e461a45ea2239af6"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a85c5d599f609c97e80cf87fd0d922784"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a8807a786fb4c6d42e739a32b3f6078f8"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a8da19290bfcd66b76ff929bb9dd3e568"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a8e81832420166c89993a4f0629d5765d"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a8f85d80231d8978144112e41b375ccc7"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a95853b0fc36aca1c168611334a39037f"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a97ef048be3e5f39cc5ce6e7f12326a23"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a98246b3329620a8e252d7ee4a302783e"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a9a887d54a3ba0dad157fafddc6573aed"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352a9e43b1a3872c21a26981a35c03fea93d"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aa102086576124d6931a3a08673e8fc0d"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aa2341295c30b0121eeb8d117764a5baf"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aa25eab9796730236361b037fc522509d"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aa61ca8fc286257f7f70057a5026b0867"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aa905904989c14075318323a10fac0abe"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aaafde672b6470275a6055520a0534bb2"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aade1a34c921a4d22fe87aa6575bef164"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ab45bcc55b80d016ef2ac8ea98ace2108"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ab45c8dab2a9d9e7f2c02e40205b957fe"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ab7400ab33f66708dd08fcf8ae543dba5"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ab75607baa4c4121c34364f4118f990d2"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ab83798a30fa11e5e6d7f8e197b0327a4"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aba2af4d5da3f34693261ef48710d22ee"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352abfa8c39566c4c41501588b815a5c52ad"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352acafecb336293cd24b363e33ca9fdce5a"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ad35d6fc19bc4fe86802105c48489553e"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ad439205ca55294a850c88e9f87fb08b4"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ad633919822dadc636420824948e75315"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ae2b2865e053ed356d915a6f9afd62caf"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ae2bae2d6191190c95a76e4cc1a6bc9d1"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ae393b55425eb2f67bb289e0e2041649c"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ae45783e98c43d87be2667155efbafbca"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352ae54293de74687bf2db5fdf9b0682ca44"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aea1698cade20d8ab5807d60a7e4dbb3b"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aeba859d489260879a08e922c04e9ca8e"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aebe60fc86ac3088108447de01191bc4e"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aec26223f49f0b0b2d418fb0f6a340f8b"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352af62bbcce8fca40ef48253ed77959ff55"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352af6d6ece41191d230932dbfaae10c0762"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352af8919f80edc86615089d8bafd40f68fd"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352af89832af70c53e320337f633985ce295"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352afb81eec26bd13732949ae8f8186fdd26"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352afcc92c93fe9dd983cd13dd5beb91ee9f"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352afd3caed713df1d318d62cbd73fdfe3c6"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aff03cfb6400f883999cc01c0cf832812"></a>
<a id="agroup__ft8xx__memory_html_gga495a8c0706389e9b3677846d772eb352aff30b9219c582c8ceac17f115a18375d"></a>
<a id="agroup__ft8xx__memory_html_gga6c8d08697812fb4e6292ff533e753aeea06a9355b36b87b1b0fa79a6f468e46bb"></a>
<a id="agroup__ft8xx__memory_html_gga6c8d08697812fb4e6292ff533e753aeea0f483ff9a2c538fccc2326f431201a57"></a>
<a id="agroup__ft8xx__memory_html_gga6c8d08697812fb4e6292ff533e753aeea408b88147f94626dabe1e8b81f72b9ea"></a>
<a id="agroup__ft8xx__memory_html_gga6c8d08697812fb4e6292ff533e753aeeaa5619b0f2ba721cfc070ee09886af264"></a>
<a id="agroup__ft8xx__memory_html_gga91adc1665d20e88c087ddb10b5e5ef69a0b846c1c3f54c88a66fee75ae1310893"></a>
<a id="agroup__ft8xx__memory_html_gga91adc1665d20e88c087ddb10b5e5ef69a0f292b470f74c0c625292850d1f6d91c"></a>
<a id="agroup__ft8xx__memory_html_gga91adc1665d20e88c087ddb10b5e5ef69a2c37aff19d6aa8801f257bc689428373"></a>
<a id="agroup__ft8xx__memory_html_gga91adc1665d20e88c087ddb10b5e5ef69a4a88dd5f6ec5d1adf451467db195604c"></a>
<a id="agroup__ft8xx__memory_html_gga91adc1665d20e88c087ddb10b5e5ef69a4f2b840d1343d34a13f5859f35241714"></a>
<a id="agroup__ft8xx__memory_html_gga91adc1665d20e88c087ddb10b5e5ef69a5a01dedda4d91a94bb7dd42eeef5f357"></a>
<a id="agroup__ft8xx__memory_html_gga91adc1665d20e88c087ddb10b5e5ef69ad7f0dc26c1313aa315bbeba0b648a013"></a>
<a id="agroup__ft8xx__memory_html_gga91adc1665d20e88c087ddb10b5e5ef69ae186b0781a832f3adedb21e9d2e05300"></a>
<a id="agroup__ft8xx__reference__api_html_ga0c6f11426fd5412a66e4f5de0a9f0847"></a>
<a id="agroup__ft8xx__reference__api_html_ga194d7e0d47b3d195155a22f86fbe7e7f"></a>
<a id="agroup__ft8xx__reference__api_html_ga1e9c6203ebb7cc15a736d074bd98c181"></a>
<a id="agroup__ft8xx__reference__api_html_ga1f01e0c91e369234362ed2bcf42da681"></a>
<a id="agroup__ft8xx__reference__api_html_ga26015112ae4c62a944fe671ea2cb0bda"></a>
<a id="agroup__ft8xx__reference__api_html_ga2f833e24c067f88801884c93766d7ac7"></a>
<a id="agroup__ft8xx__reference__api_html_ga3f6814650684e2c2100d8f9a36505ca0"></a>
<a id="agroup__ft8xx__reference__api_html_ga4467cd6c9672ac2b4c7d6b6b2e9b2f89"></a>
<a id="agroup__ft8xx__reference__api_html_ga4b77c199d909f946f7e271f11833533b"></a>
<a id="agroup__ft8xx__reference__api_html_ga7b9b6a41a878c449b107e51eba058799"></a>
<a id="agroup__ft8xx__reference__api_html_ga8fac4ed55f7ef9d82d8dcb0eb6f09eab"></a>
<a id="agroup__ft8xx__reference__api_html_gaa3f6afa02b5f4bed90093f659201d008"></a>
<a id="agroup__ft8xx__reference__api_html_gabbba9344e2d9b81af6313c6b7f12276c"></a>
<a id="agroup__ft8xx__reference__api_html_gabdaf9e6cd74c0d157d1673b99707e6f2"></a>
<a id="agroup__ft8xx__reference__api_html_gac4dc3208668383b58ec1010edeae3d2b"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__ft8xx__reference__api_html_gad642a54deaa36152ca4fea5e31294732"></a>
<a id="agroup__ft8xx__reference__api_html_gade51ff6f98a8d4cb575447bbb60cba92"></a>
<a id="agroup__ft8xx__reference__api_html_gae96efe5496139f508083a21b2299e3d8"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a041ffbb78a6572c5c1e515843f959315"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a04f552a92ffd030a0cbc07d522197265"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a11a7b5722d9de6c62222a5c76f0b692b"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a13b32d8ce6608067d1f816065547b559"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a1ecdf33453fe848f48f0535ca23b5541"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a1fbe40f257634301cca0229d68851c6b"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a21bec38288166e781f4e42f9e2cd88fb"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a2725ae9bcc184f701002e0824b6cfdfd"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a29570336f1d3a7b15d2f5b76a816faa3"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a2dd65dd2f5e8f97f27135c343681af64"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a2f0c46b14b1dced78eceb5f21c6a898e"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a3193050a59229830b80c5f637a09ecbb"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a327a78d411cf247a6ee6e4ea5541c90c"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a36c4f53d2e132c794695983e56cf627c"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a3bbab48e1bdad06303e631f62d7bcd76"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a3dd43d215eb4b5047b8a14406f85c8e0"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a43e6c3532c2f9573e31ddd4ce12fb8c0"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a47894772f07899e20c560b47a4b37208"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a49d311578982dec5afa589b0963d0622"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a50a3fe216944877cf4a55df00de4bd85"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a50c524cae48fcba2477cae9c422a3f5b"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a529da48e0b241ae16e8cbf1d38653c97"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a538bc67838a34c6f1dfbb8bdff984788"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a55841781abfc8d3452399c79d69a2009"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a56440ea6e79d6cb2c6374d8fab01277e"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a569c58d9a986415596b91856b02175b2"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a572feb4e0547d7b40c18c8ff7ed62b55"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a59764d36f28fcf060f164e8fdfb3aba8"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a5b712095cc16ff8866d55b95f6e081e5"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a6797b58f7ec24dbf469df8a17680fb7a"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a683a15e3c7578fe44f7cee9ca5796f74"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a68e60e0c855fff63e3a6f767f1b0179c"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a7546d5a7b068c0b23280a189c6345789"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a781bc22bc6c5671201a1740a282e1e0d"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a78cb160ba1d417523093ce222504df96"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a7f82f6066010b61ed49a7a8bd2b9b52e"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a81ad0d146fb392f9561bce00c6ed4e6b"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a84a2b99d9ea7f674f019f1d54c1cddc3"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a857a79d4d62ee1369f10fb746e0d0aa8"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a8717b3386b1e0ad11e34f7fae83ae793"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a87efcd914405639dcf24d762becd1ebd"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a884022eead52d6738a4f20f6a543dc50"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a8feeb5e4fbc73322825fdd392dbec950"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a95f7b2f9eb12abcdf6885ee984155d8e"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a966071326a92ac6e595b2acbb2445697"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a9988ada9b469290b9c886ba665fb4b48"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a9a09798569680c1a48880ec40502e019"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008a9cef87cf60803317580a4bd04762bc9f"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008aa024b09fec9d0440483a33e972550888"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008aa382cb5b65f2803e94ce4451ed75b848"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008aa63605dbe4cf7fdb4e1d7994f22aa878"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008aa9f1905d1f2488f5c9600dc4b27753c2"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008aac293daf5a8d5221d5c4167177069970"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ab6fd90f08477954798d5a54cb1ddce8f"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008aba6637892ddbceafb4e558fbcffe496d"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ac1e6dcc3e508a9f5b8f061a06cda7c87"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ac3f442ac6c0010066270e8373efeefcf"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ac41d85f3ba86087e0e0c5c071388d254"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ac447562a0543880a863929676c9a2c21"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ac4852d6d1ee6c7b69a3f4386354d5f2c"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ac785fd2e2498944eec5f404229c1a6f3"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ac8690647b7274feef7b7a0695eaf9a6b"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ac93146dd21c9a7e07353ae901ccea745"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008accb71ca34304a4276f6b8c5d2b2e4e6a"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ad1b8daf2ec9fe116c79d59b2d524a8a2"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ad360af56001df6e29616a11f087db26a"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ad63d6b6752e9a3b25c2d4eec38d9e455"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ad73c12cf386d92029bef895c52a21272"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ad878f3fc41274192245aa6c27209ea69"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ad92810bdf452c531a7dda338aff3aad1"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ad99a270479fd9ce96e1868fb708bacbb"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008adb67bd48114184e8ad04cadba731e9fe"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008adc4499b79053ad08a2279b3702b79ced"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ae07735ed3259a2112898ee9330cc2050"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ae53c8a1517586c00ce5e0d19b2bbea29"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ae86016e9d0fb6db20d2c585300759464"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008ae8dddb1bf87f77e70a03c4ad73ba51fd"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008aebeab047c1430f0165e36f83e0ff38a9"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008aec806fab0ed79a1a51e39395147feff2"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008aed471a111f18c5a92bcc5d7ca07e4b6d"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008af0baf00d792cf20622f3716ee6c7fa95"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008af1c9622660d41f1ebaf3c5151a8526f6"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008af5512106f5e7d41845b1cc01ca52bf68"></a>
<a id="agroup__ft8xx__reference__api_html_ggaa3f6afa02b5f4bed90093f659201d008af57b15505b903b9e8d940e1156bfa83d"></a>
<a id="agroup__ft8xx__reference__api_html_ggabbba9344e2d9b81af6313c6b7f12276ca0e42504c57b04103704eb19348fea779"></a>
<a id="agroup__ft8xx__reference__api_html_ggabbba9344e2d9b81af6313c6b7f12276ca8f7e484f38038b0a390e7cad119f2cb4"></a>
<a id="agroup__ft8xx__reference__api_html_ggabbba9344e2d9b81af6313c6b7f12276caf2eb368364f52dcfc067e40c2a252a84"></a>
<a id="agroup__ft8xx__reference__api_html_ggabbba9344e2d9b81af6313c6b7f12276caff47e90e4e3dd7901dfd1cde3fb132f5"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>

```c
/*
 * Copyright (c) 2021 Hubert Miś
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_REFERENCE_API_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_REFERENCE_API_H_

#include <stdint.h>

#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
#include <zephyr/drivers/misc/ft8xx/ft8xx_common.h>
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
#include <zephyr/drivers/misc/ft8xx/ft8xx_memory.h>

#ifdef __cplusplus
extern "C" {
#endif


static inline void wr8(uint32_t address, uint8_t data)
{
        ft8xx_wr8(DEVICE_DT_GET_ONE(ftdi_ft800), address, data);
}

static inline void wr16(uint32_t address, uint16_t data)
{
        ft8xx_wr16(DEVICE_DT_GET_ONE(ftdi_ft800), address, data);
}

static inline void wr32(uint32_t address, uint32_t data)
{
        ft8xx_wr32(DEVICE_DT_GET_ONE(ftdi_ft800), address, data);
}

static inline uint8_t rd8(uint32_t address)
{
        return ft8xx_rd8(DEVICE_DT_GET_ONE(ftdi_ft800), address);
}

static inline uint16_t rd16(uint32_t address)
{
        return ft8xx_rd16(DEVICE_DT_GET_ONE(ftdi_ft800), address);
}

static inline uint32_t rd32(uint32_t address)
{
        return ft8xx_rd32(DEVICE_DT_GET_ONE(ftdi_ft800), address);
}


#define OPT_3D        FT8XX_OPT_3D
#define OPT_RGB565    FT8XX_OPT_RGB565
#define OPT_MONO      FT8XX_OPT_MONO
#define OPT_NODL      FT8XX_OPT_NODL
#define OPT_FLAT      FT8XX_OPT_FLAT
#define OPT_SIGNED    FT8XX_OPT_SIGNED
#define OPT_CENTERX   FT8XX_OPT_CENTERX
#define OPT_CENTERY   FT8XX_OPT_CENTERY
#define OPT_CENTER    FT8XX_OPT_CENTER
#define OPT_RIGHTX    FT8XX_OPT_RIGHTX
#define OPT_NOBACK    FT8XX_OPT_NOBACK
#define OPT_NOTICKS   FT8XX_OPT_NOTICKS
#define OPT_NOHM      FT8XX_OPT_NOHM
#define OPT_NOPOINTER FT8XX_OPT_NOPOINTER
#define OPT_NOSECS    FT8XX_OPT_NOSECS
#define OPT_NOHANDS   FT8XX_OPT_NOHANDS

static inline void cmd(uint32_t command)
{
        ft8xx_copro_cmd(DEVICE_DT_GET_ONE(ftdi_ft800), command);
}

static inline void cmd_dlstart(void)
{
        ft8xx_copro_cmd_dlstart(DEVICE_DT_GET_ONE(ftdi_ft800));
}

static inline void cmd_swap(void)
{
        ft8xx_copro_cmd_swap(DEVICE_DT_GET_ONE(ftdi_ft800));
}

static inline void cmd_fgcolor(uint32_t c)
{
        ft8xx_copro_cmd_fgcolor(DEVICE_DT_GET_ONE(ftdi_ft800), c);
}

static inline void cmd_bgcolor(uint32_t c)
{
        ft8xx_copro_cmd_bgcolor(DEVICE_DT_GET_ONE(ftdi_ft800), c);
}

static inline void cmd_slider(int16_t x,
                              int16_t y,
                              int16_t w,
                              int16_t h,
                              uint16_t options,
                              uint16_t val,
                              uint16_t range)
{
        ft8xx_copro_cmd_slider(DEVICE_DT_GET_ONE(ftdi_ft800), x, y, w, h, options, val,
                               range);
}

static inline void cmd_toggle(int16_t x,
                              int16_t y,
                              int16_t w,
                              int16_t font,
                              uint16_t options,
                              uint16_t state,
                              const char *s)
{
        ft8xx_copro_cmd_toggle(DEVICE_DT_GET_ONE(ftdi_ft800), x, y, w, font, options,
                               state, s);
}

static inline void cmd_track(int16_t x,
                             int16_t y,
                             int16_t w,
                             int16_t h,
                             int16_t tag)
{
        ft8xx_copro_cmd_track(DEVICE_DT_GET_ONE(ftdi_ft800), x, y, w, h, tag);
}

static inline void cmd_text(int16_t x,
                           int16_t y,
                           int16_t font,
                           uint16_t options,
                           const char *s)
{
        ft8xx_copro_cmd_text(DEVICE_DT_GET_ONE(ftdi_ft800), x, y, font, options, s);
}

static inline void cmd_number(int16_t x,
                             int16_t y,
                             int16_t font,
                             uint16_t options,
                             int32_t n)
{
        ft8xx_copro_cmd_number(DEVICE_DT_GET_ONE(ftdi_ft800), x, y, font, options, n);
}

static inline void cmd_calibrate(uint32_t *result)
{
        ft8xx_copro_cmd_calibrate(DEVICE_DT_GET_ONE(ftdi_ft800), result);
}


#define BITMAPS      FT8XX_BITMAPS
#define POINTS       FT8XX_POINTS
#define LINES        FT8XX_LINES
#define LINE_STRIP   FT8XX_LINE_STRIP
#define EDGE_STRIP_R FT8XX_EDGE_STRIP_R
#define EDGE_STRIP_L FT8XX_EDGE_STRIP_L
#define EDGE_STRIP_A FT8XX_EDGE_STRIP_A
#define EDGE_STRIP_B FT8XX_EDGE_STRIP_B
#define RECTS        FT8XX_RECTS

#define BEGIN(prim) FT8XX_BEGIN(prim)

#define CLEAR(c, s, t) FT8XX_CLEAR(c, s, t)

#define CLEAR_COLOR_RGB(red, green, blue) FT8XX_CLEAR_COLOR_RGB(red, green, blue)

#define COLOR_RGB(red, green, blue) FT8XX_COLOR_RGB(red, green, blue)

#define DISPLAY() FT8XX_DISPLAY()

#define END() FT8XX_END()

#define LINE_WIDTH(width) FT8XX_LINE_WIDTH(width)

#define TAG(s) FT8XX_TAG(s)

#define VERTEX2F(x, y) FT8XX_VERTEX2F(x, y)

#define VERTEX2II(x, y, handle, cell) FT8XX_VERTEX2II(x, y, handle, cell)


#if defined(CONFIG_FT800)
enum ft8xx_memory_map_t {
        RAM_G         = FT800_RAM_G,
        ROM_CHIPID    = FT800_ROM_CHIPID,
        ROM_FONT      = FT800_ROM_FONT,
        ROM_FONT_ADDR = FT800_ROM_FONT_ADDR,
        RAM_DL        = FT800_RAM_DL,
        RAM_PAL       = FT800_RAM_PAL,
        REG_          = FT800_REG_,
        RAM_CMD       = FT800_RAM_CMD
};
#else /* Definition of FT810 memory map */
enum ft8xx_memory_map_t {
        RAM_G         = FT810_RAM_G,
        RAM_DL        = FT810_RAM_DL,
        REG_          = FT810_REG_,
        RAM_CMD       = FT810_RAM_CMD
};
#endif

#if defined(CONFIG_FT800)
enum ft8xx_register_address_t {
        REG_ID         = FT800_REG_ID,
        REG_FRAMES     = FT800_REG_FRAMES,
        REG_CLOCK      = FT800_REG_CLOCK,
        REG_FREQUENCY  = FT800_REG_FREQUENCY,
        REG_RENDERMODE = FT800_REG_RENDERMODE,
        REG_SNAPY      = FT800_REG_SNAPY,
        REG_SNAPSHOT   = FT800_REG_SNAPSHOT,
        REG_CPURESET   = FT800_REG_CPURESET,
        REG_TAP_CRC    = FT800_REG_TAP_CRC,
        REG_TAP_MASK   = FT800_REG_TAP_MASK,
        REG_HCYCLE     = FT800_REG_HCYCLE,
        REG_HOFFSET    = FT800_REG_HOFFSET,
        REG_HSIZE      = FT800_REG_HSIZE,
        REG_HSYNC0     = FT800_REG_HSYNC0,
        REG_HSYNC1     = FT800_REG_HSYNC1,
        REG_VCYCLE     = FT800_REG_VCYCLE,
        REG_VOFFSET    = FT800_REG_VOFFSET,
        REG_VSIZE      = FT800_REG_VSIZE,
        REG_VSYNC0     = FT800_REG_VSYNC0,
        REG_VSYNC1     = FT800_REG_VSYNC1,
        REG_DLSWAP     = FT800_REG_DLSWAP,
        REG_ROTATE     = FT800_REG_ROTATE,
        REG_OUTBITS    = FT800_REG_OUTBITS,
        REG_DITHER     = FT800_REG_DITHER,
        REG_SWIZZLE    = FT800_REG_SWIZZLE,
        REG_CSPREAD    = FT800_REG_CSPREAD,
        REG_PCLK_POL   = FT800_REG_PCLK_POL,
        REG_PCLK       = FT800_REG_PCLK,
        REG_TAG_X      = FT800_REG_TAG_X,
        REG_TAG_Y      = FT800_REG_TAG_Y,
        REG_TAG        = FT800_REG_TAG,
        REG_VOL_PB     = FT800_REG_VOL_PB,
        REG_VOL_SOUND  = FT800_REG_VOL_SOUND,
        REG_SOUND      = FT800_REG_SOUND,
        REG_PLAY       = FT800_REG_PLAY,
        REG_GPIO_DIR   = FT800_REG_GPIO_DIR,
        REG_GPIO       = FT800_REG_GPIO,

        REG_INT_FLAGS  = FT800_REG_INT_FLAGS,
        REG_INT_EN     = FT800_REG_INT_EN,
        REG_INT_MASK   = FT800_REG_INT_MASK,
        REG_PLAYBACK_START = FT800_REG_PLAYBACK_START,
        REG_PLAYBACK_LENGTH = FT800_REG_PLAYBACK_LENGTH,
        REG_PLAYBACK_READPTR = FT800_REG_PLAYBACK_READPTR,
        REG_PLAYBACK_FREQ = FT800_REG_PLAYBACK_FREQ,
        REG_PLAYBACK_FORMAT = FT800_REG_PLAYBACK_FORMAT,
        REG_PLAYBACK_LOOP = FT800_REG_PLAYBACK_LOOP,
        REG_PLAYBACK_PLAY = FT800_REG_PLAYBACK_PLAY,
        REG_PWM_HZ     = FT800_REG_PWM_HZ,
        REG_PWM_DUTY   = FT800_REG_PWM_DUTY,
        REG_MACRO_0    = FT800_REG_MACRO_0,
        REG_MACRO_1    = FT800_REG_MACRO_1,

        REG_CMD_READ   = FT800_REG_CMD_READ,
        REG_CMD_WRITE  = FT800_REG_CMD_WRITE,
        REG_CMD_DL     = FT800_REG_CMD_DL,
        REG_TOUCH_MODE = FT800_REG_TOUCH_MODE,
        REG_TOUCH_ADC_MODE = FT800_REG_TOUCH_ADC_MODE,
        REG_TOUCH_CHARGE = FT800_REG_TOUCH_CHARGE,
        REG_TOUCH_SETTLE = FT800_REG_TOUCH_SETTLE,
        REG_TOUCH_OVERSAMPLE = FT800_REG_TOUCH_OVERSAMPLE,
        REG_TOUCH_RZTHRESH = FT800_REG_TOUCH_RZTHRESH,
        REG_TOUCH_RAW_XY = FT800_REG_TOUCH_RAW_XY,
        REG_TOUCH_RZ   = FT800_REG_TOUCH_RZ,
        REG_TOUCH_SCREEN_XY = FT800_REG_TOUCH_SCREEN_XY,
        REG_TOUCH_TAG_XY = FT800_REG_TOUCH_TAG_XY,
        REG_TOUCH_TAG  = FT800_REG_TOUCH_TAG,
        REG_TOUCH_TRANSFORM_A = FT800_REG_TOUCH_TRANSFORM_A,
        REG_TOUCH_TRANSFORM_B = FT800_REG_TOUCH_TRANSFORM_B,
        REG_TOUCH_TRANSFORM_C = FT800_REG_TOUCH_TRANSFORM_C,
        REG_TOUCH_TRANSFORM_D = FT800_REG_TOUCH_TRANSFORM_D,
        REG_TOUCH_TRANSFORM_E = FT800_REG_TOUCH_TRANSFORM_E,
        REG_TOUCH_TRANSFORM_F = FT800_REG_TOUCH_TRANSFORM_F,

        REG_TOUCH_DIRECT_XY = FT800_REG_TOUCH_DIRECT_XY,
        REG_TOUCH_DIRECT_Z1Z2 = FT800_REG_TOUCH_DIRECT_Z1Z2,

        REG_TRACKER    = FT800_REG_TRACKER
};
#else /* Definition of FT810 registers */
enum ft8xx_register_address_t {
        REG_TRIM       = FT810_REG_TRIM,

        REG_ID         = FT810_REG_ID,
        REG_FRAMES     = FT810_REG_FRAMES,
        REG_CLOCK      = FT810_REG_CLOCK,
        REG_FREQUENCY  = FT810_REG_FREQUENCY,
        REG_RENDERMODE = FT810_REG_RENDERMODE,
        REG_SNAPY      = FT810_REG_SNAPY,
        REG_SNAPSHOT   = FT810_REG_SNAPSHOT,
        REG_CPURESET   = FT810_REG_CPURESET,
        REG_TAP_CRC    = FT810_REG_TAP_CRC,
        REG_TAP_MASK   = FT810_REG_TAP_MASK,
        REG_HCYCLE     = FT810_REG_HCYCLE,
        REG_HOFFSET    = FT810_REG_HOFFSET,
        REG_HSIZE      = FT810_REG_HSIZE,
        REG_HSYNC0     = FT810_REG_HSYNC0,
        REG_HSYNC1     = FT810_REG_HSYNC1,
        REG_VCYCLE     = FT810_REG_VCYCLE,
        REG_VOFFSET    = FT810_REG_VOFFSET,
        REG_VSIZE      = FT810_REG_VSIZE,
        REG_VSYNC0     = FT810_REG_VSYNC0,
        REG_VSYNC1     = FT810_REG_VSYNC1,
        REG_DLSWAP     = FT810_REG_DLSWAP,
        REG_ROTATE     = FT810_REG_ROTATE,
        REG_OUTBITS    = FT810_REG_OUTBITS,
        REG_DITHER     = FT810_REG_DITHER,
        REG_SWIZZLE    = FT810_REG_SWIZZLE,
        REG_CSPREAD    = FT810_REG_CSPREAD,
        REG_PCLK_POL   = FT810_REG_PCLK_POL,
        REG_PCLK       = FT810_REG_PCLK,
        REG_TAG_X      = FT810_REG_TAG_X,
        REG_TAG_Y      = FT810_REG_TAG_Y,
        REG_TAG        = FT810_REG_TAG,
        REG_VOL_PB     = FT810_REG_VOL_PB,
        REG_VOL_SOUND  = FT810_REG_VOL_SOUND,
        REG_SOUND      = FT810_REG_SOUND,
        REG_PLAY       = FT810_REG_PLAY,
        REG_GPIO_DIR   = FT810_REG_GPIO_DIR,
        REG_GPIO       = FT810_REG_GPIO,
        REG_GPIOX_DIR  = FT810_REG_GPIOX_DIR,
        REG_GPIOX      = FT810_REG_GPIOX,

        REG_INT_FLAGS  = FT810_REG_INT_FLAGS,
        REG_INT_EN     = FT810_REG_INT_EN,
        REG_INT_MASK   = FT810_REG_INT_MASK,
        REG_PLAYBACK_START = FT810_REG_PLAYBACK_START,
        REG_PLAYBACK_LENGTH = FT810_REG_PLAYBACK_LENGTH,
        REG_PLAYBACK_READPTR = FT810_REG_PLAYBACK_READPTR,
        REG_PLAYBACK_FREQ = FT810_REG_PLAYBACK_FREQ,
        REG_PLAYBACK_FORMAT = FT810_REG_PLAYBACK_FORMAT,
        REG_PLAYBACK_LOOP = FT810_REG_PLAYBACK_LOOP,
        REG_PLAYBACK_PLAY = FT810_REG_PLAYBACK_PLAY,
        REG_PWM_HZ     = FT810_REG_PWM_HZ,
        REG_PWM_DUTY   = FT810_REG_PWM_DUTY,

        REG_CMD_READ   = FT810_REG_CMD_READ,
        REG_CMD_WRITE  = FT810_REG_CMD_WRITE,
        REG_CMD_DL     = FT810_REG_CMD_DL,
        REG_TOUCH_MODE = FT810_REG_TOUCH_MODE,
        REG_TOUCH_ADC_MODE = FT810_REG_TOUCH_ADC_MODE,
        REG_TOUCH_CHARGE = FT810_REG_TOUCH_CHARGE,
        REG_TOUCH_SETTLE = FT810_REG_TOUCH_SETTLE,
        REG_TOUCH_OVERSAMPLE = FT810_REG_TOUCH_OVERSAMPLE,
        REG_TOUCH_RZTHRESH = FT810_REG_TOUCH_RZTHRESH,
        REG_TOUCH_RAW_XY = FT810_REG_TOUCH_RAW_XY,
        REG_TOUCH_RZ   = FT810_REG_TOUCH_RZ,
        REG_TOUCH_SCREEN_XY = FT810_REG_TOUCH_SCREEN_XY,
        REG_TOUCH_TAG_XY = FT810_REG_TOUCH_TAG_XY,
        REG_TOUCH_TAG  = FT810_REG_TOUCH_TAG,
        REG_TOUCH_TRANSFORM_A = FT810_REG_TOUCH_TRANSFORM_A,
        REG_TOUCH_TRANSFORM_B = FT810_REG_TOUCH_TRANSFORM_B,
        REG_TOUCH_TRANSFORM_C = FT810_REG_TOUCH_TRANSFORM_C,
        REG_TOUCH_TRANSFORM_D = FT810_REG_TOUCH_TRANSFORM_D,
        REG_TOUCH_TRANSFORM_E = FT810_REG_TOUCH_TRANSFORM_E,
        REG_TOUCH_TRANSFORM_F = FT810_REG_TOUCH_TRANSFORM_F,
        REG_TOUCH_CONFIG = FT810_REG_TOUCH_CONFIG,

        REG_SPI_WIDTH  = FT810_REG_SPI_WIDTH,

        REG_TOUCH_DIRECT_XY = FT810_REG_TOUCH_DIRECT_XY,
        REG_TOUCH_DIRECT_Z1Z2 = FT810_REG_TOUCH_DIRECT_Z1Z2,

        REG_CMDB_SPACE = FT810_REG_CMDB_SPACE,
        REG_CMDB_WRITE = FT810_REG_CMDB_WRITE,

        REG_TRACKER    = FT810_REG_TRACKER,
        REG_TRACKER1   = FT810_REG_TRACKER1,
        REG_TRACKER2   = FT810_REG_TRACKER2,
        REG_TRACKER3   = FT810_REG_TRACKER3,
        REG_TRACKER4   = FT810_REG_TRACKER4,
        REG_MEDIAFIFO_READ = FT810_REG_MEDIAFIFO_READ,
        REG_MEDIAFIFO_WRITE = FT810_REG_MEDIAFIFO_WRITE,
};
#endif


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_REFERENCE_API_H_ */
```

## 27.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Hubert Miś。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 571 行

FT810 内存映射（Memory map）定义。

### 注释 3：原第 663 行

FT810 寄存器定义。

### 注释 4：原第 769 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_REFERENCE_API_H_`。

## 27.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__reference__api_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/drivers/misc/ft8xx/ft8xx_copro.h](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__copro_8h.html)
- [zephyr/drivers/misc/ft8xx/ft8xx_common.h](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__common_8h.html)
- [zephyr/drivers/misc/ft8xx/ft8xx_dl.h](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__dl_8h.html)
- [zephyr/drivers/misc/ft8xx/ft8xx_memory.h](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__memory_8h.html)
- [wr8](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga1e9c6203ebb7cc15a736d074bd98c181)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ft8xx_wr8](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html#ga2c8c5d06b09549ab041bbff4612b4620)
- [DEVICE_DT_GET_ONE](../device_reference/P001_设备模型公共接口.md#ga39c760429534ef9ae77f3d996987cd2b)
- [wr16](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga8fac4ed55f7ef9d82d8dcb0eb6f09eab)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [ft8xx_wr16](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html#gaa6d306b1e2701e0de415c64d33e575a4)
- [wr32](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga3f6814650684e2c2100d8f9a36505ca0)
- [ft8xx_wr32](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html#gada8d996d58f0f46f3f56534ee0da4c68)
- [rd8](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae96efe5496139f508083a21b2299e3d8)
- [ft8xx_rd8](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html#gab8235ed0c0f7373628457fcf64e15fbd)
- [rd16](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga2f833e24c067f88801884c93766d7ac7)
- [ft8xx_rd16](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html#ga743c2d25f728451e98417b2ebcc9c722)
- [rd32](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga0c6f11426fd5412a66e4f5de0a9f0847)
- [ft8xx_rd32](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html#gaed670a8410224f8f3970fad86705f513)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [ft8xx_copro_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga9d4ab3b53e4e11433d9c6a0d3e6cd3ea)
- [cmd_dlstart](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga7b9b6a41a878c449b107e51eba058799)
- [ft8xx_copro_cmd_dlstart](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gab7f5a1ea24eb9db4ac0e0a4f3d58e7b9)
- [cmd_swap](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga194d7e0d47b3d195155a22f86fbe7e7f)
- [ft8xx_copro_cmd_swap](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga3605bc23d9555ac51fc6292cb6f2a02c)
- [cmd_fgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga4b77c199d909f946f7e271f11833533b)
- [ft8xx_copro_cmd_fgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gab47b9c79db405686168cf1516ea0a00d)
- [cmd_bgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga4467cd6c9672ac2b4c7d6b6b2e9b2f89)
- [ft8xx_copro_cmd_bgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gafa5c3fe004456cfd531edf781c11c00d)
- [cmd_slider](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga1f01e0c91e369234362ed2bcf42da681)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [ft8xx_copro_cmd_slider](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga3b9454e8a6a824bd87c675037047c069)
- [cmd_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gade51ff6f98a8d4cb575447bbb60cba92)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [ft8xx_copro_cmd_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga93e61278bacec915bb360244ab43dbb7)
- [cmd_track](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gac4dc3208668383b58ec1010edeae3d2b)
- [ft8xx_copro_cmd_track](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac946f044f2fbb6381ea4af268084d828)
- [cmd_text](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gad642a54deaa36152ca4fea5e31294732)
- [ft8xx_copro_cmd_text](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga35d0500600e8c1d1df653952fab5d86c)
- [cmd_number](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gabdaf9e6cd74c0d157d1673b99707e6f2)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [ft8xx_copro_cmd_number](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga72e1feafde7bb230cd798ba23f414de9)
- [cmd_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga26015112ae4c62a944fe671ea2cb0bda)
- [ft8xx_copro_cmd_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gacc68ff73da90a9c822185f2ceba5a910)
- [ft8xx_memory_map_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gabbba9344e2d9b81af6313c6b7f12276c)
- [RAM_G](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggabbba9344e2d9b81af6313c6b7f12276ca8f7e484f38038b0a390e7cad119f2cb4)
- [FT800_RAM_G](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69a0f292b470f74c0c625292850d1f6d91c)
- [FT800_ROM_CHIPID](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69ae186b0781a832f3adedb21e9d2e05300)
- [FT800_ROM_FONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69a4f2b840d1343d34a13f5859f35241714)
- [FT800_ROM_FONT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69a0b846c1c3f54c88a66fee75ae1310893)
- [RAM_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggabbba9344e2d9b81af6313c6b7f12276caf2eb368364f52dcfc067e40c2a252a84)
- [FT800_RAM_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69ad7f0dc26c1313aa315bbeba0b648a013)
- [FT800_RAM_PAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69a5a01dedda4d91a94bb7dd42eeef5f357)
- [REG_](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggabbba9344e2d9b81af6313c6b7f12276ca0e42504c57b04103704eb19348fea779)
- [FT800_REG_](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69a4a88dd5f6ec5d1adf451467db195604c)
- [RAM_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggabbba9344e2d9b81af6313c6b7f12276caff47e90e4e3dd7901dfd1cde3fb132f5)
- [FT800_RAM_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69a2c37aff19d6aa8801f257bc689428373)
- [FT810_RAM_G](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga6c8d08697812fb4e6292ff533e753aeeaa5619b0f2ba721cfc070ee09886af264)
- [FT810_RAM_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga6c8d08697812fb4e6292ff533e753aeea408b88147f94626dabe1e8b81f72b9ea)
- [FT810_REG_](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga6c8d08697812fb4e6292ff533e753aeea0f483ff9a2c538fccc2326f431201a57)
- [FT810_RAM_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga6c8d08697812fb4e6292ff533e753aeea06a9355b36b87b1b0fa79a6f468e46bb)
- [ft8xx_register_address_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaa3f6afa02b5f4bed90093f659201d008)
- [REG_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a6797b58f7ec24dbf469df8a17680fb7a)
- [FT800_REG_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a7946c63f4dd93692634c08ec0b4657e4)
- [REG_FRAMES](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad73c12cf386d92029bef895c52a21272)
- [FT800_REG_FRAMES](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aa45d948244f4decd8863f5def65a78db)
- [REG_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a2dd65dd2f5e8f97f27135c343681af64)
- [FT800_REG_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a46376ddea2bccf9e0af33d78a05f635a)
- [REG_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac447562a0543880a863929676c9a2c21)
- [FT800_REG_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a0a864b5230c4ed04ac4a18f7e9c85af5)
- [REG_RENDERMODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aebeab047c1430f0165e36f83e0ff38a9)
- [FT800_REG_RENDERMODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a1ca1c284f1f3e2ae75c4874f0c569c7c)
- [REG_SNAPY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a9cef87cf60803317580a4bd04762bc9f)
- [FT800_REG_SNAPY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a6bcedb4e986dba59c0c689356022d992)
- [REG_SNAPSHOT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a81ad0d146fb392f9561bce00c6ed4e6b)
- [FT800_REG_SNAPSHOT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a382043bf7f2381a4fad71adeae73db2d)
- [REG_CPURESET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a569c58d9a986415596b91856b02175b2)
- [FT800_REG_CPURESET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a4411395eca792d4d23f63242fea6307e)
- [REG_TAP_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a47894772f07899e20c560b47a4b37208)
- [FT800_REG_TAP_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a2b36ffdd93c6f41bd08f732099608a99)
- [REG_TAP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a87efcd914405639dcf24d762becd1ebd)
- [FT800_REG_TAP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a3c6f1a0898055d4eec3ddfbde56f6a51)
- [REG_HCYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aec806fab0ed79a1a51e39395147feff2)
- [FT800_REG_HCYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aa2b46aa7465a2e38a9947e0b5868f6c7)
- [REG_HOFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a50a3fe216944877cf4a55df00de4bd85)
- [FT800_REG_HOFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a3179545d22570761b9bf0598ff24219a)
- [REG_HSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a3dd43d215eb4b5047b8a14406f85c8e0)
- [FT800_REG_HSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a7b46068735f066e0d2fa6a0ccb073001)
- [REG_HSYNC0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008accb71ca34304a4276f6b8c5d2b2e4e6a)
- [FT800_REG_HSYNC0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a5d365f03f5dcd630191f050963c4fc9c)
- [REG_HSYNC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a13b32d8ce6608067d1f816065547b559)
- [FT800_REG_HSYNC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a7c4d1b3a4a5dc128d52fd91352342a70)
- [REG_VCYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad360af56001df6e29616a11f087db26a)
- [FT800_REG_VCYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aaf8bdfc1924c2269c9db3933499cd23c)
- [REG_VOFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad1b8daf2ec9fe116c79d59b2d524a8a2)
- [FT800_REG_VOFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a7d9903cc3452f77287ce411c831e6567)
- [REG_VSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aa63605dbe4cf7fdb4e1d7994f22aa878)
- [FT800_REG_VSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a2f17cc86a455d13b2f92ada17319a94e)
- [REG_VSYNC0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ae07735ed3259a2112898ee9330cc2050)
- [FT800_REG_VSYNC0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a0a6dcbe431ec103262ee805acaee9897)
- [REG_VSYNC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a3193050a59229830b80c5f637a09ecbb)
- [FT800_REG_VSYNC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6abcd84b4d56e71b558a79f10d97b66ea1)
- [REG_DLSWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a9a09798569680c1a48880ec40502e019)
- [FT800_REG_DLSWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a9f726cc401387bbe8aa3366047467688)
- [REG_ROTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac785fd2e2498944eec5f404229c1a6f3)
- [FT800_REG_ROTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ab9bf90e77f7946d4466e3b8d444d64e4)
- [REG_OUTBITS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a55841781abfc8d3452399c79d69a2009)
- [FT800_REG_OUTBITS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a3d5e1b30a5d1889b14b77f8a4bfecf7b)
- [REG_DITHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a50c524cae48fcba2477cae9c422a3f5b)
- [FT800_REG_DITHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a2ba06eef07c7b881c2b331aa090329ed)
- [REG_SWIZZLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008af1c9622660d41f1ebaf3c5151a8526f6)
- [FT800_REG_SWIZZLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a161a252ef247cad31f812c88fbfcdf6f)
- [REG_CSPREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008af57b15505b903b9e8d940e1156bfa83d)
- [FT800_REG_CSPREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aaf65490a7a4b55309bc8943b065eef17)
- [REG_PCLK_POL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a1fbe40f257634301cca0229d68851c6b)
- [FT800_REG_PCLK_POL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a9ded0eeda09a9cce3bf111c0a49dd391)
- [REG_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a572feb4e0547d7b40c18c8ff7ed62b55)
- [FT800_REG_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a8947fb21fa7a7fa4a26bdaea5dbe79c5)
- [REG_TAG_X](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a1ecdf33453fe848f48f0535ca23b5541)
- [FT800_REG_TAG_X](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a424e4e6fb301bb6833a46f813fc5895a)
- [REG_TAG_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac41d85f3ba86087e0e0c5c071388d254)
- [FT800_REG_TAG_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a7f8c3d2a08a68b741ded594eafbfaae4)
- [REG_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac8690647b7274feef7b7a0695eaf9a6b)
- [FT800_REG_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a83136b05a9a6f64867f39c50fb0079d2)
- [REG_VOL_PB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aa024b09fec9d0440483a33e972550888)
- [FT800_REG_VOL_PB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a4f0e1449b7ab28bf29f52bf3544c442f)
- [REG_VOL_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aac293daf5a8d5221d5c4167177069970)
- [FT800_REG_VOL_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a5672933c464d2408ad0a6a046fddc1d2)
- [REG_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008adb67bd48114184e8ad04cadba731e9fe)
- [FT800_REG_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a2f0f00e3bbd1b9f9fb09c9d2b65382d7)
- [REG_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a29570336f1d3a7b15d2f5b76a816faa3)
- [FT800_REG_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a0187a790b87eca35892431c600248e71)
- [REG_GPIO_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a7f82f6066010b61ed49a7a8bd2b9b52e)
- [FT800_REG_GPIO_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a2c4d02cf887f3ec87b99cd32ae8b355b)
- [REG_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad92810bdf452c531a7dda338aff3aad1)
- [FT800_REG_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6af7d0154293ba1228a0e04bb923bf9b39)
- [REG_INT_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ab6fd90f08477954798d5a54cb1ddce8f)
- [FT800_REG_INT_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a4fbbc34adc25d9147f2a8007a537ddbd)
- [REG_INT_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a966071326a92ac6e595b2acbb2445697)
- [FT800_REG_INT_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aa31af794f56d1f4f831ef65c3daf1087)
- [REG_INT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aba6637892ddbceafb4e558fbcffe496d)
- [FT800_REG_INT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aa6461f2c17d723ecd672babedbb1e9fc)
- [REG_PLAYBACK_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a95f7b2f9eb12abcdf6885ee984155d8e)
- [FT800_REG_PLAYBACK_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ac159bfb8d704e46aa4be4859d1e476af)
- [REG_PLAYBACK_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aa9f1905d1f2488f5c9600dc4b27753c2)
- [FT800_REG_PLAYBACK_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a097806c1c7281e5cbaf0e992888c2e97)
- [REG_PLAYBACK_READPTR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aed471a111f18c5a92bcc5d7ca07e4b6d)
- [FT800_REG_PLAYBACK_READPTR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aec4e118a3fe1cf3e1f2b5df6b376a651)
- [REG_PLAYBACK_FREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a84a2b99d9ea7f674f019f1d54c1cddc3)
- [FT800_REG_PLAYBACK_FREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aa8c6fb57011ad08bf0a1d0b48eb5599a)
- [REG_PLAYBACK_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a68e60e0c855fff63e3a6f767f1b0179c)
- [FT800_REG_PLAYBACK_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a13f744aa7a089e177a36623239d12961)
- [REG_PLAYBACK_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a5b712095cc16ff8866d55b95f6e081e5)
- [FT800_REG_PLAYBACK_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ab62b5bbfdf948265ad10129ead4d8a63)
- [REG_PLAYBACK_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a59764d36f28fcf060f164e8fdfb3aba8)
- [FT800_REG_PLAYBACK_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a15006a5d2ab004ca8b5a9a75be095b5b)
- [REG_PWM_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a884022eead52d6738a4f20f6a543dc50)
- [FT800_REG_PWM_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ac321e2d68978123ab259a2d84d186719)
- [REG_PWM_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a04f552a92ffd030a0cbc07d522197265)
- [FT800_REG_PWM_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ae14e09a184dbe44390ce7d5576b30d4c)
- [FT800_REG_MACRO_0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ae95328740c30d541b4dc79466734306c)
- [FT800_REG_MACRO_1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a9bce17c193b9c809bef0770bc65b37cf)
- [REG_CMD_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008af5512106f5e7d41845b1cc01ca52bf68)
- [FT800_REG_CMD_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aa2cb7424ec77d9a35179824cd2fecb47)
- [REG_CMD_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad878f3fc41274192245aa6c27209ea69)
- [FT800_REG_CMD_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a4911a990964958a6e2bf4842e87ab101)
- [REG_CMD_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac1e6dcc3e508a9f5b8f061a06cda7c87)
- [FT800_REG_CMD_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a23f9fdc1d48d6410fc600359842b16ea)
- [REG_TOUCH_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ae53c8a1517586c00ce5e0d19b2bbea29)
- [FT800_REG_TOUCH_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ada6b5afbed95413c1988131384c02b1b)
- [REG_TOUCH_ADC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a2f0c46b14b1dced78eceb5f21c6a898e)
- [FT800_REG_TOUCH_ADC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a65b43042fe7dbc44bd15fb472bba33a4)
- [REG_TOUCH_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008af0baf00d792cf20622f3716ee6c7fa95)
- [FT800_REG_TOUCH_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a69b981de24b4da81175c9ac74c8454f5)
- [REG_TOUCH_SETTLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a21bec38288166e781f4e42f9e2cd88fb)
- [FT800_REG_TOUCH_SETTLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ae02db7afd08bd1c06f6e1f9e06e81d33)
- [REG_TOUCH_OVERSAMPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a78cb160ba1d417523093ce222504df96)
- [FT800_REG_TOUCH_OVERSAMPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a87e989861d85d683c95e8de44f74f58b)
- [REG_TOUCH_RZTHRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a56440ea6e79d6cb2c6374d8fab01277e)
- [FT800_REG_TOUCH_RZTHRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a70f721a708b36ef255270d02680e4e7f)
- [REG_TOUCH_RAW_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a781bc22bc6c5671201a1740a282e1e0d)
- [FT800_REG_TOUCH_RAW_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a8ef80aeaaffd974b2e246ad15c98f916)
- [REG_TOUCH_RZ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad63d6b6752e9a3b25c2d4eec38d9e455)
- [FT800_REG_TOUCH_RZ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ab66136540b44e2f37a0f920fbd3cbcc4)
- [REG_TOUCH_SCREEN_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a857a79d4d62ee1369f10fb746e0d0aa8)
- [FT800_REG_TOUCH_SCREEN_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a99fc0fc08ee942b7783951674837d57d)
- [REG_TOUCH_TAG_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a7546d5a7b068c0b23280a189c6345789)
- [FT800_REG_TOUCH_TAG_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a86ba740c280900a1dd4273422b9ca8b6)
- [REG_TOUCH_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af)
- [FT800_REG_TOUCH_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a245e5594218702bc2c30c1b50ec44329)
- [REG_TOUCH_TRANSFORM_A](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a2725ae9bcc184f701002e0824b6cfdfd)
- [FT800_REG_TOUCH_TRANSFORM_A](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a183fd00d406e113b8b72b8c5b5fc5880)
- [REG_TOUCH_TRANSFORM_B](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac93146dd21c9a7e07353ae901ccea745)
- [FT800_REG_TOUCH_TRANSFORM_B](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6acd3161021e315e1a2f91f21ccdc48d8a)
- [REG_TOUCH_TRANSFORM_C](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a8717b3386b1e0ad11e34f7fae83ae793)
- [FT800_REG_TOUCH_TRANSFORM_C](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a4b3e903dfed68a7eb7f7734e18aca9e0)
- [REG_TOUCH_TRANSFORM_D](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a9988ada9b469290b9c886ba665fb4b48)
- [FT800_REG_TOUCH_TRANSFORM_D](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a386a6293cd82485934b3865bd3f1956b)
- [REG_TOUCH_TRANSFORM_E](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a36c4f53d2e132c794695983e56cf627c)
- [FT800_REG_TOUCH_TRANSFORM_E](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a4f188f88f9a032fdb6f3c87ed352d4bb)
- [REG_TOUCH_TRANSFORM_F](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a041ffbb78a6572c5c1e515843f959315)
- [FT800_REG_TOUCH_TRANSFORM_F](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a1d01f5fe890a4d7670cf91a7cd48402f)
- [REG_TOUCH_DIRECT_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ae8dddb1bf87f77e70a03c4ad73ba51fd)
- [FT800_REG_TOUCH_DIRECT_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a1745bb57bcf9872b308c49a151a43f1f)
- [REG_TOUCH_DIRECT_Z1Z2](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a43e6c3532c2f9573e31ddd4ce12fb8c0)
- [FT800_REG_TOUCH_DIRECT_Z1Z2](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a43bcc194c075b385073ed73a562b8cfa)
- [REG_TRACKER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad99a270479fd9ce96e1868fb708bacbb)
- [FT800_REG_TRACKER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a3397b2a86a97997d01780d52ec23b84c)
- [REG_TRIM](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a683a15e3c7578fe44f7cee9ca5796f74)
- [FT810_REG_TRIM](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ad35d6fc19bc4fe86802105c48489553e)
- [FT810_REG_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a8e81832420166c89993a4f0629d5765d)
- [FT810_REG_FRAMES](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ab75607baa4c4121c34364f4118f990d2)
- [FT810_REG_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a222e9d43895af76d103f9fbd09c40832)
- [FT810_REG_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a3f09f2fd706996b97173f587637aee53)
- [FT810_REG_RENDERMODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a32f5dfe4ebc13114ecf9336670f74a31)
- [FT810_REG_SNAPY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a1f9721ea190d82af17332d60cb8eb795)
- [FT810_REG_SNAPSHOT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a104e72273989d38213fc070b4fd4a676)
- [FT810_REG_CPURESET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ae2bae2d6191190c95a76e4cc1a6bc9d1)
- [FT810_REG_TAP_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a6e302da1712f086b26d08e46f7a9f1d1)
- [FT810_REG_TAP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a369d654c43692ef193493063338888aa)
- [FT810_REG_HCYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a68ae24f87a50c7790ac987c6e2ccab2b)
- [FT810_REG_HOFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a95853b0fc36aca1c168611334a39037f)
- [FT810_REG_HSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352af89832af70c53e320337f633985ce295)
- [FT810_REG_HSYNC0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a086b28d18b9c49e51ef734c2f6e6ce21)
- [FT810_REG_HSYNC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a533ec4682d3b9649a59e012a53ab55de)
- [FT810_REG_VCYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a9e43b1a3872c21a26981a35c03fea93d)
- [FT810_REG_VOFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a2a155f858da556270114a3f9d989ef85)
- [FT810_REG_VSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352acafecb336293cd24b363e33ca9fdce5a)
- [FT810_REG_VSYNC0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352afd3caed713df1d318d62cbd73fdfe3c6)
- [FT810_REG_VSYNC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a3deeabcda1f9453dc2d865e8b19715a8)
- [FT810_REG_DLSWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352afb81eec26bd13732949ae8f8186fdd26)
- [FT810_REG_ROTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a54935aeb6c13623f68c5c74c3db722ff)
- [FT810_REG_OUTBITS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aff30b9219c582c8ceac17f115a18375d)
- [FT810_REG_DITHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a61e1d7c2e2ed9a0ee4b372dd9c7df63a)
- [FT810_REG_SWIZZLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ad633919822dadc636420824948e75315)
- [FT810_REG_CSPREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352abfa8c39566c4c41501588b815a5c52ad)
- [FT810_REG_PCLK_POL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a83d5ff35dc2d6af8e461a45ea2239af6)
- [FT810_REG_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aff03cfb6400f883999cc01c0cf832812)
- [FT810_REG_TAG_X](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ab45bcc55b80d016ef2ac8ea98ace2108)
- [FT810_REG_TAG_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a22089e51c2e0e4d373589c398a54ca05)
- [FT810_REG_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352af8919f80edc86615089d8bafd40f68fd)
- [FT810_REG_VOL_PB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aade1a34c921a4d22fe87aa6575bef164)
- [FT810_REG_VOL_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a98246b3329620a8e252d7ee4a302783e)
- [FT810_REG_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a5d019d200409c2dd4b57f727afedf815)
- [FT810_REG_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ab83798a30fa11e5e6d7f8e197b0327a4)
- [FT810_REG_GPIO_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aba2af4d5da3f34693261ef48710d22ee)
- [FT810_REG_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ab7400ab33f66708dd08fcf8ae543dba5)
- [REG_GPIOX_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a538bc67838a34c6f1dfbb8bdff984788)
- [FT810_REG_GPIOX_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aec26223f49f0b0b2d418fb0f6a340f8b)
- [REG_GPIOX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008adc4499b79053ad08a2279b3702b79ced)
- [FT810_REG_GPIOX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ae45783e98c43d87be2667155efbafbca)
- [FT810_REG_INT_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352afcc92c93fe9dd983cd13dd5beb91ee9f)
- [FT810_REG_INT_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a6ad1c0050228bfdfca87bca6a4a0a571)
- [FT810_REG_INT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a5a21ce38ac3699f4c9e5f8f0e7bc8555)
- [FT810_REG_PLAYBACK_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ab45c8dab2a9d9e7f2c02e40205b957fe)
- [FT810_REG_PLAYBACK_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a206979e1f9edf49aca24f8afb07e7f48)
- [FT810_REG_PLAYBACK_READPTR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a60dd200c41f58057d20169ff833d4f82)
- [FT810_REG_PLAYBACK_FREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a8f85d80231d8978144112e41b375ccc7)
- [FT810_REG_PLAYBACK_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a304779eb0c7eca705a3c9fbf3d23fdb2)
- [FT810_REG_PLAYBACK_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a0b2882f45164307c678cba35232bcbf9)
- [FT810_REG_PLAYBACK_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aeba859d489260879a08e922c04e9ca8e)
- [FT810_REG_PWM_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a75c68657acd7582c3028f0802d155771)
- [FT810_REG_PWM_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a0558ac04acd45a6bf1e9100ec3a0a278)
- [FT810_REG_CMD_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a81b9c8fd550b60b9b4cd1aae7a97efb9)
- [FT810_REG_CMD_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ae2b2865e053ed356d915a6f9afd62caf)
- [FT810_REG_CMD_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ae393b55425eb2f67bb289e0e2041649c)
- [FT810_REG_TOUCH_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a67e068b57d9917ba093bfb8b073cf712)
- [FT810_REG_TOUCH_ADC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a2bb9ad22a0d93b7facb92f49be1ac63a)
- [FT810_REG_TOUCH_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ae54293de74687bf2db5fdf9b0682ca44)
- [FT810_REG_TOUCH_SETTLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a0e712682bd8d083f0ee25b284c242cdf)
- [FT810_REG_TOUCH_OVERSAMPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a779e92fbc0655c0889a3760025f8880a)
- [FT810_REG_TOUCH_RZTHRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aa102086576124d6931a3a08673e8fc0d)
- [FT810_REG_TOUCH_RAW_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a359efc1f478e7653bb567fcfa20fb575)
- [FT810_REG_TOUCH_RZ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a6a0dee898cc286ec6a2f91536fb0c8b4)
- [FT810_REG_TOUCH_SCREEN_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352af62bbcce8fca40ef48253ed77959ff55)
- [FT810_REG_TOUCH_TAG_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a4e6013b98cf73db7e09b7952f1f29e5b)
- [FT810_REG_TOUCH_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a97ef048be3e5f39cc5ce6e7f12326a23)
- [FT810_REG_TOUCH_TRANSFORM_A](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aa2341295c30b0121eeb8d117764a5baf)
- [FT810_REG_TOUCH_TRANSFORM_B](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aa25eab9796730236361b037fc522509d)
- [FT810_REG_TOUCH_TRANSFORM_C](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aaafde672b6470275a6055520a0534bb2)
- [FT810_REG_TOUCH_TRANSFORM_D](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a71f116560ffc21a45eece099f0155e52)
- [FT810_REG_TOUCH_TRANSFORM_E](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aa61ca8fc286257f7f70057a5026b0867)
- [FT810_REG_TOUCH_TRANSFORM_F](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a03912bde6f4ad32381c50772b89ec2bc)
- [REG_TOUCH_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a8feeb5e4fbc73322825fdd392dbec950)
- [FT810_REG_TOUCH_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a1190faa2c60e6a2dc8661eb7da7461c6)
- [REG_SPI_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aa382cb5b65f2803e94ce4451ed75b848)
- [FT810_REG_SPI_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a8366bdc17c88345c80aab6f061090312)
- [FT810_REG_TOUCH_DIRECT_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a8807a786fb4c6d42e739a32b3f6078f8)
- [FT810_REG_TOUCH_DIRECT_Z1Z2](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ad439205ca55294a850c88e9f87fb08b4)
- [REG_CMDB_SPACE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a327a78d411cf247a6ee6e4ea5541c90c)
- [FT810_REG_CMDB_SPACE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a85c5d599f609c97e80cf87fd0d922784)
- [REG_CMDB_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ae86016e9d0fb6db20d2c585300759464)
- [FT810_REG_CMDB_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aea1698cade20d8ab5807d60a7e4dbb3b)
- [FT810_REG_TRACKER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a43adc41a79ea8af3bbf769b796f7c223)
- [REG_TRACKER1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a49d311578982dec5afa589b0963d0622)
- [FT810_REG_TRACKER1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aebe60fc86ac3088108447de01191bc4e)
- [REG_TRACKER2](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a3bbab48e1bdad06303e631f62d7bcd76)
- [FT810_REG_TRACKER2](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352af6d6ece41191d230932dbfaae10c0762)
- [REG_TRACKER3](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac4852d6d1ee6c7b69a3f4386354d5f2c)
- [FT810_REG_TRACKER3](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a4449f285050e761b3fd78feebefe4335)
- [REG_TRACKER4](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac3f442ac6c0010066270e8373efeefcf)
- [FT810_REG_TRACKER4](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a9a887d54a3ba0dad157fafddc6573aed)
- [REG_MEDIAFIFO_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a529da48e0b241ae16e8cbf1d38653c97)
- [FT810_REG_MEDIAFIFO_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a8da19290bfcd66b76ff929bb9dd3e568)
- [REG_MEDIAFIFO_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a11a7b5722d9de6c62222a5c76f0b692b)
- [FT810_REG_MEDIAFIFO_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aa905904989c14075318323a10fac0abe)
- [ft8xx_common.h](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__common_8h.html)
- [ft8xx_copro.h](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__copro_8h.html)
- [ft8xx_dl.h](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__dl_8h.html)
- [ft8xx_memory.h](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__memory_8h.html)

---

[上一章](P026_espi_emul.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P028_heap_kasan.h_源码浏览.md)
