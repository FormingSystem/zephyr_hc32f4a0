---
id: learning.zephyr-docs.api-source-reference.page-281
title: ft8xx_memory.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__memory_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第281章\_ft8xx\_memory.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__memory_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__memory_8h.html)。

## 281.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="foldopen00027"></a>
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
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00047"></a>
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
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
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
<a id="l00162"></a>
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
<a id="l00177"></a>
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
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="agroup__ft8xx__memory_html_ga3c885b333acd851fed4d74886656d2c6"></a>
<a id="agroup__ft8xx__memory_html_ga495a8c0706389e9b3677846d772eb352"></a>
<a id="agroup__ft8xx__memory_html_ga6c8d08697812fb4e6292ff533e753aee"></a>
<a id="agroup__ft8xx__memory_html_ga91adc1665d20e88c087ddb10b5e5ef69"></a>
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

```c
/*
 * Copyright (c) 2020 Hubert Miś
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_MEMORY_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_MEMORY_H_

#ifdef __cplusplus
extern "C" {
#endif


enum ft800_memory_map_t {
        FT800_RAM_G         = 0x000000,
        FT800_ROM_CHIPID    = 0x0C0000,
        FT800_ROM_FONT      = 0x0BB23C,
        FT800_ROM_FONT_ADDR = 0x0FFFFC,
        FT800_RAM_DL        = 0x100000,
        FT800_RAM_PAL       = 0x102000,
        FT800_REG_          = 0x102400,
        FT800_RAM_CMD       = 0x108000
};

enum ft810_memory_map_t {
        FT810_RAM_G         = 0x000000,
        FT810_RAM_DL        = 0x300000,
        FT810_REG_          = 0x302000,
        FT810_RAM_CMD       = 0x308000
};

enum ft800_register_address_t {
        FT800_REG_ID         = 0x102400,
        FT800_REG_FRAMES     = 0x102404,
        FT800_REG_CLOCK      = 0x102408,
        FT800_REG_FREQUENCY  = 0x10240C,
        FT800_REG_RENDERMODE = 0x102410,
        FT800_REG_SNAPY      = 0x102414,
        FT800_REG_SNAPSHOT   = 0x102418,
        FT800_REG_CPURESET   = 0x10241C,
        FT800_REG_TAP_CRC    = 0x102420,
        FT800_REG_TAP_MASK   = 0x102424,
        FT800_REG_HCYCLE     = 0x102428,
        FT800_REG_HOFFSET    = 0x10242C,
        FT800_REG_HSIZE      = 0x102430,
        FT800_REG_HSYNC0     = 0x102434,
        FT800_REG_HSYNC1     = 0x102438,
        FT800_REG_VCYCLE     = 0x10243C,
        FT800_REG_VOFFSET    = 0x102440,
        FT800_REG_VSIZE      = 0x102444,
        FT800_REG_VSYNC0     = 0x102448,
        FT800_REG_VSYNC1     = 0x10244C,
        FT800_REG_DLSWAP     = 0x102450,
        FT800_REG_ROTATE     = 0x102454,
        FT800_REG_OUTBITS    = 0x102458,
        FT800_REG_DITHER     = 0x10245C,
        FT800_REG_SWIZZLE    = 0x102460,
        FT800_REG_CSPREAD    = 0x102464,
        FT800_REG_PCLK_POL   = 0x102468,
        FT800_REG_PCLK       = 0x10246C,
        FT800_REG_TAG_X      = 0x102470,
        FT800_REG_TAG_Y      = 0x102474,
        FT800_REG_TAG        = 0x102478,
        FT800_REG_VOL_PB     = 0x10247C,
        FT800_REG_VOL_SOUND  = 0x102480,
        FT800_REG_SOUND      = 0x102484,
        FT800_REG_PLAY       = 0x102488,
        FT800_REG_GPIO_DIR   = 0x10248C,
        FT800_REG_GPIO       = 0x102490,

        FT800_REG_INT_FLAGS  = 0x102498,
        FT800_REG_INT_EN     = 0x10249C,
        FT800_REG_INT_MASK   = 0x1024A0,
        FT800_REG_PLAYBACK_START = 0x1024A4,
        FT800_REG_PLAYBACK_LENGTH = 0x1024A8,
        FT800_REG_PLAYBACK_READPTR = 0x1024AC,
        FT800_REG_PLAYBACK_FREQ = 0x1024B0,
        FT800_REG_PLAYBACK_FORMAT = 0x1024B4,
        FT800_REG_PLAYBACK_LOOP = 0x1024B8,
        FT800_REG_PLAYBACK_PLAY = 0x1024BC,
        FT800_REG_PWM_HZ     = 0x1024C0,
        FT800_REG_PWM_DUTY   = 0x1024C4,
        FT800_REG_MACRO_0    = 0x1024C8,
        FT800_REG_MACRO_1    = 0x1024CC,

        FT800_REG_CMD_READ   = 0x1024E4,
        FT800_REG_CMD_WRITE  = 0x1024E8,
        FT800_REG_CMD_DL     = 0x1024EC,
        FT800_REG_TOUCH_MODE = 0x1024F0,
        FT800_REG_TOUCH_ADC_MODE = 0x1024F4,
        FT800_REG_TOUCH_CHARGE = 0x1024F8,
        FT800_REG_TOUCH_SETTLE = 0x1024FC,
        FT800_REG_TOUCH_OVERSAMPLE = 0x102500,
        FT800_REG_TOUCH_RZTHRESH = 0x102504,
        FT800_REG_TOUCH_RAW_XY = 0x102508,
        FT800_REG_TOUCH_RZ   = 0x10250C,
        FT800_REG_TOUCH_SCREEN_XY = 0x102510,
        FT800_REG_TOUCH_TAG_XY = 0x102514,
        FT800_REG_TOUCH_TAG  = 0x102518,
        FT800_REG_TOUCH_TRANSFORM_A = 0x10251C,
        FT800_REG_TOUCH_TRANSFORM_B = 0x102520,
        FT800_REG_TOUCH_TRANSFORM_C = 0x102524,
        FT800_REG_TOUCH_TRANSFORM_D = 0x102528,
        FT800_REG_TOUCH_TRANSFORM_E = 0x10252C,
        FT800_REG_TOUCH_TRANSFORM_F = 0x102530,

        FT800_REG_TOUCH_DIRECT_XY = 0x102574,
        FT800_REG_TOUCH_DIRECT_Z1Z2 = 0x102578,

        FT800_REG_TRACKER    = 0x109000
};

enum ft810_register_address_t {
        FT810_REG_TRIM       = 0x10256C,

        FT810_REG_ID         = 0x302000,
        FT810_REG_FRAMES     = 0x302004,
        FT810_REG_CLOCK      = 0x302008,
        FT810_REG_FREQUENCY  = 0x30200C,
        FT810_REG_RENDERMODE = 0x302010,
        FT810_REG_SNAPY      = 0x302014,
        FT810_REG_SNAPSHOT   = 0x302018,
        FT810_REG_CPURESET   = 0x302020,
        FT810_REG_TAP_CRC    = 0x302020,
        FT810_REG_TAP_MASK   = 0x302024,
        FT810_REG_HCYCLE     = 0x30202C,
        FT810_REG_HOFFSET    = 0x302030,
        FT810_REG_HSIZE      = 0x302034,
        FT810_REG_HSYNC0     = 0x302038,
        FT810_REG_HSYNC1     = 0x30203C,
        FT810_REG_VCYCLE     = 0x302040,
        FT810_REG_VOFFSET    = 0x302044,
        FT810_REG_VSIZE      = 0x302048,
        FT810_REG_VSYNC0     = 0x30204C,
        FT810_REG_VSYNC1     = 0x302050,
        FT810_REG_DLSWAP     = 0x302054,
        FT810_REG_ROTATE     = 0x302058,
        FT810_REG_OUTBITS    = 0x30205C,
        FT810_REG_DITHER     = 0x302060,
        FT810_REG_SWIZZLE    = 0x302064,
        FT810_REG_CSPREAD    = 0x302068,
        FT810_REG_PCLK_POL   = 0x30206C,
        FT810_REG_PCLK       = 0x302070,
        FT810_REG_TAG_X      = 0x302074,
        FT810_REG_TAG_Y      = 0x302078,
        FT810_REG_TAG        = 0x30207C,
        FT810_REG_VOL_PB     = 0x302080,
        FT810_REG_VOL_SOUND  = 0x302084,
        FT810_REG_SOUND      = 0x302088,
        FT810_REG_PLAY       = 0x30208C,
        FT810_REG_GPIO_DIR   = 0x302090,
        FT810_REG_GPIO       = 0x302094,
        FT810_REG_GPIOX_DIR  = 0x302098,
        FT810_REG_GPIOX      = 0x30209C,

        FT810_REG_INT_FLAGS  = 0x3020A8,
        FT810_REG_INT_EN     = 0x3020AC,
        FT810_REG_INT_MASK   = 0x3020B0,
        FT810_REG_PLAYBACK_START = 0x3020B4,
        FT810_REG_PLAYBACK_LENGTH = 0x3020B8,
        FT810_REG_PLAYBACK_READPTR = 0x3020BC,
        FT810_REG_PLAYBACK_FREQ = 0x3020C0,
        FT810_REG_PLAYBACK_FORMAT = 0x3020C4,
        FT810_REG_PLAYBACK_LOOP = 0x3020C8,
        FT810_REG_PLAYBACK_PLAY = 0x3020CC,
        FT810_REG_PWM_HZ     = 0x3020D0,
        FT810_REG_PWM_DUTY   = 0x3020D4,

        FT810_REG_CMD_READ   = 0x3020F8,
        FT810_REG_CMD_WRITE  = 0x3020FC,
        FT810_REG_CMD_DL     = 0x302100,
        FT810_REG_TOUCH_MODE = 0x302104,
        FT810_REG_TOUCH_ADC_MODE = 0x302108,
        FT810_REG_TOUCH_CHARGE = 0x30210C,
        FT810_REG_TOUCH_SETTLE = 0x302110,
        FT810_REG_TOUCH_OVERSAMPLE = 0x302114,
        FT810_REG_TOUCH_RZTHRESH = 0x302118,
        FT810_REG_TOUCH_RAW_XY = 0x30211C,
        FT810_REG_TOUCH_RZ   = 0x302120,
        FT810_REG_TOUCH_SCREEN_XY = 0x302124,
        FT810_REG_TOUCH_TAG_XY = 0x302128,
        FT810_REG_TOUCH_TAG  = 0x30212C,
        FT810_REG_TOUCH_TRANSFORM_A = 0x302150,
        FT810_REG_TOUCH_TRANSFORM_B = 0x302154,
        FT810_REG_TOUCH_TRANSFORM_C = 0x302158,
        FT810_REG_TOUCH_TRANSFORM_D = 0x30215C,
        FT810_REG_TOUCH_TRANSFORM_E = 0x302160,
        FT810_REG_TOUCH_TRANSFORM_F = 0x302164,
        FT810_REG_TOUCH_CONFIG = 0x302168,

        FT810_REG_SPI_WIDTH  = 0x302180,

        FT810_REG_TOUCH_DIRECT_XY = 0x30218C,
        FT810_REG_TOUCH_DIRECT_Z1Z2 = 0x302190,

        FT810_REG_CMDB_SPACE = 0x302574,
        FT810_REG_CMDB_WRITE = 0x302578,

        FT810_REG_TRACKER    = 0x309000,
        FT810_REG_TRACKER1   = 0x309004,
        FT810_REG_TRACKER2   = 0x309008,
        FT810_REG_TRACKER3   = 0x30900C,
        FT810_REG_TRACKER4   = 0x309010,
        FT810_REG_MEDIAFIFO_READ = 0x309014,
        FT810_REG_MEDIAFIFO_WRITE = 0x309018,
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_MEMORY_H_ */
```

## 281.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Hubert Miś。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 232 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_MEMORY_H_`。

## 281.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__memory_8h.html)
- [ft800_memory_map_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#ga91adc1665d20e88c087ddb10b5e5ef69)
- [FT800_RAM_G](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69a0f292b470f74c0c625292850d1f6d91c)
- [FT800_ROM_CHIPID](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69ae186b0781a832f3adedb21e9d2e05300)
- [FT800_ROM_FONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69a4f2b840d1343d34a13f5859f35241714)
- [FT800_ROM_FONT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69a0b846c1c3f54c88a66fee75ae1310893)
- [FT800_RAM_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69ad7f0dc26c1313aa315bbeba0b648a013)
- [FT800_RAM_PAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69a5a01dedda4d91a94bb7dd42eeef5f357)
- [FT800_REG_](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69a4a88dd5f6ec5d1adf451467db195604c)
- [FT800_RAM_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga91adc1665d20e88c087ddb10b5e5ef69a2c37aff19d6aa8801f257bc689428373)
- [ft810_memory_map_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#ga6c8d08697812fb4e6292ff533e753aee)
- [FT810_RAM_G](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga6c8d08697812fb4e6292ff533e753aeeaa5619b0f2ba721cfc070ee09886af264)
- [FT810_RAM_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga6c8d08697812fb4e6292ff533e753aeea408b88147f94626dabe1e8b81f72b9ea)
- [FT810_REG_](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga6c8d08697812fb4e6292ff533e753aeea0f483ff9a2c538fccc2326f431201a57)
- [FT810_RAM_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga6c8d08697812fb4e6292ff533e753aeea06a9355b36b87b1b0fa79a6f468e46bb)
- [ft800_register_address_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#ga3c885b333acd851fed4d74886656d2c6)
- [FT800_REG_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a7946c63f4dd93692634c08ec0b4657e4)
- [FT800_REG_FRAMES](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aa45d948244f4decd8863f5def65a78db)
- [FT800_REG_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a46376ddea2bccf9e0af33d78a05f635a)
- [FT800_REG_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a0a864b5230c4ed04ac4a18f7e9c85af5)
- [FT800_REG_RENDERMODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a1ca1c284f1f3e2ae75c4874f0c569c7c)
- [FT800_REG_SNAPY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a6bcedb4e986dba59c0c689356022d992)
- [FT800_REG_SNAPSHOT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a382043bf7f2381a4fad71adeae73db2d)
- [FT800_REG_CPURESET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a4411395eca792d4d23f63242fea6307e)
- [FT800_REG_TAP_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a2b36ffdd93c6f41bd08f732099608a99)
- [FT800_REG_TAP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a3c6f1a0898055d4eec3ddfbde56f6a51)
- [FT800_REG_HCYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aa2b46aa7465a2e38a9947e0b5868f6c7)
- [FT800_REG_HOFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a3179545d22570761b9bf0598ff24219a)
- [FT800_REG_HSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a7b46068735f066e0d2fa6a0ccb073001)
- [FT800_REG_HSYNC0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a5d365f03f5dcd630191f050963c4fc9c)
- [FT800_REG_HSYNC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a7c4d1b3a4a5dc128d52fd91352342a70)
- [FT800_REG_VCYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aaf8bdfc1924c2269c9db3933499cd23c)
- [FT800_REG_VOFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a7d9903cc3452f77287ce411c831e6567)
- [FT800_REG_VSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a2f17cc86a455d13b2f92ada17319a94e)
- [FT800_REG_VSYNC0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a0a6dcbe431ec103262ee805acaee9897)
- [FT800_REG_VSYNC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6abcd84b4d56e71b558a79f10d97b66ea1)
- [FT800_REG_DLSWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a9f726cc401387bbe8aa3366047467688)
- [FT800_REG_ROTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ab9bf90e77f7946d4466e3b8d444d64e4)
- [FT800_REG_OUTBITS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a3d5e1b30a5d1889b14b77f8a4bfecf7b)
- [FT800_REG_DITHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a2ba06eef07c7b881c2b331aa090329ed)
- [FT800_REG_SWIZZLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a161a252ef247cad31f812c88fbfcdf6f)
- [FT800_REG_CSPREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aaf65490a7a4b55309bc8943b065eef17)
- [FT800_REG_PCLK_POL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a9ded0eeda09a9cce3bf111c0a49dd391)
- [FT800_REG_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a8947fb21fa7a7fa4a26bdaea5dbe79c5)
- [FT800_REG_TAG_X](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a424e4e6fb301bb6833a46f813fc5895a)
- [FT800_REG_TAG_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a7f8c3d2a08a68b741ded594eafbfaae4)
- [FT800_REG_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a83136b05a9a6f64867f39c50fb0079d2)
- [FT800_REG_VOL_PB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a4f0e1449b7ab28bf29f52bf3544c442f)
- [FT800_REG_VOL_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a5672933c464d2408ad0a6a046fddc1d2)
- [FT800_REG_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a2f0f00e3bbd1b9f9fb09c9d2b65382d7)
- [FT800_REG_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a0187a790b87eca35892431c600248e71)
- [FT800_REG_GPIO_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a2c4d02cf887f3ec87b99cd32ae8b355b)
- [FT800_REG_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6af7d0154293ba1228a0e04bb923bf9b39)
- [FT800_REG_INT_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a4fbbc34adc25d9147f2a8007a537ddbd)
- [FT800_REG_INT_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aa31af794f56d1f4f831ef65c3daf1087)
- [FT800_REG_INT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aa6461f2c17d723ecd672babedbb1e9fc)
- [FT800_REG_PLAYBACK_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ac159bfb8d704e46aa4be4859d1e476af)
- [FT800_REG_PLAYBACK_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a097806c1c7281e5cbaf0e992888c2e97)
- [FT800_REG_PLAYBACK_READPTR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aec4e118a3fe1cf3e1f2b5df6b376a651)
- [FT800_REG_PLAYBACK_FREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aa8c6fb57011ad08bf0a1d0b48eb5599a)
- [FT800_REG_PLAYBACK_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a13f744aa7a089e177a36623239d12961)
- [FT800_REG_PLAYBACK_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ab62b5bbfdf948265ad10129ead4d8a63)
- [FT800_REG_PLAYBACK_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a15006a5d2ab004ca8b5a9a75be095b5b)
- [FT800_REG_PWM_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ac321e2d68978123ab259a2d84d186719)
- [FT800_REG_PWM_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ae14e09a184dbe44390ce7d5576b30d4c)
- [FT800_REG_MACRO_0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ae95328740c30d541b4dc79466734306c)
- [FT800_REG_MACRO_1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a9bce17c193b9c809bef0770bc65b37cf)
- [FT800_REG_CMD_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6aa2cb7424ec77d9a35179824cd2fecb47)
- [FT800_REG_CMD_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a4911a990964958a6e2bf4842e87ab101)
- [FT800_REG_CMD_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a23f9fdc1d48d6410fc600359842b16ea)
- [FT800_REG_TOUCH_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ada6b5afbed95413c1988131384c02b1b)
- [FT800_REG_TOUCH_ADC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a65b43042fe7dbc44bd15fb472bba33a4)
- [FT800_REG_TOUCH_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a69b981de24b4da81175c9ac74c8454f5)
- [FT800_REG_TOUCH_SETTLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ae02db7afd08bd1c06f6e1f9e06e81d33)
- [FT800_REG_TOUCH_OVERSAMPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a87e989861d85d683c95e8de44f74f58b)
- [FT800_REG_TOUCH_RZTHRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a70f721a708b36ef255270d02680e4e7f)
- [FT800_REG_TOUCH_RAW_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a8ef80aeaaffd974b2e246ad15c98f916)
- [FT800_REG_TOUCH_RZ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6ab66136540b44e2f37a0f920fbd3cbcc4)
- [FT800_REG_TOUCH_SCREEN_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a99fc0fc08ee942b7783951674837d57d)
- [FT800_REG_TOUCH_TAG_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a86ba740c280900a1dd4273422b9ca8b6)
- [FT800_REG_TOUCH_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a245e5594218702bc2c30c1b50ec44329)
- [FT800_REG_TOUCH_TRANSFORM_A](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a183fd00d406e113b8b72b8c5b5fc5880)
- [FT800_REG_TOUCH_TRANSFORM_B](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6acd3161021e315e1a2f91f21ccdc48d8a)
- [FT800_REG_TOUCH_TRANSFORM_C](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a4b3e903dfed68a7eb7f7734e18aca9e0)
- [FT800_REG_TOUCH_TRANSFORM_D](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a386a6293cd82485934b3865bd3f1956b)
- [FT800_REG_TOUCH_TRANSFORM_E](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a4f188f88f9a032fdb6f3c87ed352d4bb)
- [FT800_REG_TOUCH_TRANSFORM_F](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a1d01f5fe890a4d7670cf91a7cd48402f)
- [FT800_REG_TOUCH_DIRECT_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a1745bb57bcf9872b308c49a151a43f1f)
- [FT800_REG_TOUCH_DIRECT_Z1Z2](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a43bcc194c075b385073ed73a562b8cfa)
- [FT800_REG_TRACKER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga3c885b333acd851fed4d74886656d2c6a3397b2a86a97997d01780d52ec23b84c)
- [ft810_register_address_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#ga495a8c0706389e9b3677846d772eb352)
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
- [FT810_REG_GPIOX_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aec26223f49f0b0b2d418fb0f6a340f8b)
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
- [FT810_REG_TOUCH_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a1190faa2c60e6a2dc8661eb7da7461c6)
- [FT810_REG_SPI_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a8366bdc17c88345c80aab6f061090312)
- [FT810_REG_TOUCH_DIRECT_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a8807a786fb4c6d42e739a32b3f6078f8)
- [FT810_REG_TOUCH_DIRECT_Z1Z2](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352ad439205ca55294a850c88e9f87fb08b4)
- [FT810_REG_CMDB_SPACE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a85c5d599f609c97e80cf87fd0d922784)
- [FT810_REG_CMDB_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aea1698cade20d8ab5807d60a7e4dbb3b)
- [FT810_REG_TRACKER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a43adc41a79ea8af3bbf769b796f7c223)
- [FT810_REG_TRACKER1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aebe60fc86ac3088108447de01191bc4e)
- [FT810_REG_TRACKER2](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352af6d6ece41191d230932dbfaae10c0762)
- [FT810_REG_TRACKER3](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a4449f285050e761b3fd78feebefe4335)
- [FT810_REG_TRACKER4](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a9a887d54a3ba0dad157fafddc6573aed)
- [FT810_REG_MEDIAFIFO_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352a8da19290bfcd66b76ff929bb9dd3e568)
- [FT810_REG_MEDIAFIFO_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__memory.html#gga495a8c0706389e9b3677846d772eb352aa905904989c14075318323a10fac0abe)

---

[上一章](P280_ft8xx_dl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P282_fwargs.h_源码浏览.md)
