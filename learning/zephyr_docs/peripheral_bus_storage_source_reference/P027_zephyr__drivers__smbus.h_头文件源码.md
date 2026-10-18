---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-27
title: zephyr__drivers__smbus.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smbus_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr__drivers__smbus.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/smbus_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P027_zephyr__drivers__smbus.h_头文件参考.md)。

## 27.1\_原始可见代码（Source Code）

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
<a id="l00040"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00236"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00251"></a>
<a id="foldopen00253"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="foldopen00288"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="foldopen00302"></a>
<a id="l00302"></a>
<a id="l00304"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="foldopen00319"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00339"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="foldopen00443"></a>
<a id="l00443"></a>
<a id="l00445"></a>
<a id="l00447"></a>
<a id="l00449"></a>
<a id="l00451"></a>
<a id="l00453"></a>
<a id="l00455"></a>
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
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="foldopen00542"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00581"></a>
<a id="l00582"></a>
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
<a id="foldopen00625"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
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
<a id="foldopen00691"></a>
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
<a id="foldopen00714"></a>
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
<a id="foldopen00737"></a>
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
<a id="foldopen00760"></a>
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
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00852"></a>
<a id="l00853"></a>
<a id="l00854"></a>
<a id="l00855"></a>
<a id="l00856"></a>
<a id="l00857"></a>
<a id="l00858"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00888"></a>
<a id="l00889"></a>
<a id="l00890"></a>
<a id="l00891"></a>
<a id="l00892"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="l00915"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="l00922"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00947"></a>
<a id="l00948"></a>
<a id="l00949"></a>
<a id="l00950"></a>
<a id="l00951"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00955"></a>
<a id="l00956"></a>
<a id="l00957"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00961"></a>
<a id="l00962"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="l00984"></a>
<a id="l00985"></a>
<a id="l00986"></a>
<a id="l00987"></a>
<a id="l00988"></a>
<a id="l00989"></a>
<a id="l00990"></a>
<a id="l00991"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l01013"></a>
<a id="l01014"></a>
<a id="l01015"></a>
<a id="l01016"></a>
<a id="l01017"></a>
<a id="l01018"></a>
<a id="l01019"></a>
<a id="l01020"></a>
<a id="l01021"></a>
<a id="l01022"></a>
<a id="l01023"></a>
<a id="l01024"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01028"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01054"></a>
<a id="l01055"></a>
<a id="l01056"></a>
<a id="l01057"></a>
<a id="l01058"></a>
<a id="l01059"></a>
<a id="l01060"></a>
<a id="l01061"></a>
<a id="l01062"></a>
<a id="l01063"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="l01083"></a>
<a id="l01084"></a>
<a id="l01085"></a>
<a id="l01086"></a>
<a id="l01087"></a>
<a id="l01088"></a>
<a id="l01089"></a>
<a id="l01090"></a>
<a id="l01091"></a>
<a id="l01092"></a>
<a id="l01093"></a>
<a id="l01094"></a>
<a id="l01095"></a>
<a id="l01096"></a>
<a id="l01097"></a>
<a id="l01098"></a>
<a id="l01119"></a>
<a id="l01120"></a>
<a id="l01121"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="l01125"></a>
<a id="l01126"></a>
<a id="l01127"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01132"></a>
<a id="l01133"></a>
<a id="l01134"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01141"></a>
<a id="l01142"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="l01146"></a>
<a id="l01150"></a>
<a id="l01151"></a>
<a id="l01152"></a>
<a id="l01153"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__smbus__interface__backend_html_ga2a59de36841ca4ff5fb65e29c512cd4e"></a>
<a id="agroup__smbus__interface__backend_html_ga31f2a46f83fe193f05cc5494435e2e6f"></a>
<a id="agroup__smbus__interface__backend_html_ga36f67cfe281dea020b6036399e433f4a"></a>
<a id="agroup__smbus__interface__backend_html_ga5fa53c3cd255001a2c34b36a3d23be6f"></a>
<a id="agroup__smbus__interface__backend_html_ga7827a1f9c5cf8c2b33c79e09d05019ca"></a>
<a id="agroup__smbus__interface__backend_html_ga82dc504437f78c488df25ecd63a83a5e"></a>
<a id="agroup__smbus__interface__backend_html_ga8e71f105c10414e4ae86b87345e70837"></a>
<a id="agroup__smbus__interface__backend_html_ga93ce314c2797a21ed0b01bb28c69aeaf"></a>
<a id="agroup__smbus__interface__backend_html_ga94b1bf5e10799ab1f07cccb289033ca6"></a>
<a id="agroup__smbus__interface__backend_html_ga9a81152429fd1f70e699f6767feb8702"></a>
<a id="agroup__smbus__interface__backend_html_gaabd1e34153c852469e74e9fdc4118c84"></a>
<a id="agroup__smbus__interface__backend_html_gace2a4372975b44428fb39015e4b4bb25"></a>
<a id="agroup__smbus__interface__backend_html_gad118b4dc6c7bdea57a6d70240d804b02"></a>
<a id="agroup__smbus__interface__backend_html_gad7453c161b4fa3c6085c186b39301659"></a>
<a id="agroup__smbus__interface__backend_html_gae25c3c8652730085ec31701a48f086b5"></a>
<a id="agroup__smbus__interface_html_ga0a63b800c14f5831730372b9bad41864"></a>
<a id="agroup__smbus__interface_html_ga1f1148a7cb92e0e0aef7ae3a84615c9b"></a>
<a id="agroup__smbus__interface_html_ga2c1369835d3783bb5b5c3cb3711fec92"></a>
<a id="agroup__smbus__interface_html_ga5054a6de634b015f54dacbe81427d0d2"></a>
<a id="agroup__smbus__interface_html_ga517305aa7cc9c93ae449b3c548d6c835"></a>
<a id="agroup__smbus__interface_html_ga55a867cdcb504039f274abae2d1a99e4"></a>
<a id="agroup__smbus__interface_html_ga5ccde036931dc54e684ae5b955ff80d3"></a>
<a id="agroup__smbus__interface_html_ga67603db9b44636b0b62a24fd623cfb1c"></a>
<a id="agroup__smbus__interface_html_ga680c3d713a615f4b62503d6f84de4290"></a>
<a id="agroup__smbus__interface_html_ga6d6ee9d29de5c0007d34328eb7c9f7c9"></a>
<a id="agroup__smbus__interface_html_ga72a789110c7286a51c5cd5e2215abce1"></a>
<a id="agroup__smbus__interface_html_ga7dd01c1e00a0f8b0315e442707332251"></a>
<a id="agroup__smbus__interface_html_ga9190cfe3ce0c41c0a37d5345bad812d4"></a>
<a id="agroup__smbus__interface_html_ga9ca38ca95c0576bdc75b7eb8d0ca29ef"></a>
<a id="agroup__smbus__interface_html_gaa18281b8f9859e46a138a874a8873366"></a>
<a id="agroup__smbus__interface_html_gab008499bca4a4096672d5909fa71b21d"></a>
<a id="agroup__smbus__interface_html_gad0c28687977d0a7866bdea87aef88016"></a>
<a id="agroup__smbus__interface_html_gadaef9dad3470a7e4d3360e0246271ca1"></a>
<a id="agroup__smbus__interface_html_gadd7ec1eb3db981efceb8f959546a3b6a"></a>
<a id="agroup__smbus__interface_html_gade05f9bbbba609832df91fe804dd5d3c"></a>
<a id="agroup__smbus__interface_html_gadff533a6bc198815ee56d03a36b949e0"></a>
<a id="agroup__smbus__interface_html_ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54"></a>
<a id="agroup__smbus__interface_html_ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f"></a>
<a id="agroup__stats__apis_html_ga4124f8c0a9ffb78d8be608a780676785"></a>
<a id="agroup__stats__apis_html_ga498c4ee3baf1a4e21a6a5b0766d9b74e"></a>
<a id="agroup__stats__apis_html_ga592329613cc77cfa5dee3e1d3b16dd93"></a>
<a id="agroup__stats__apis_html_ga5fba46e743c05b4f36df91a86c37e30d"></a>
<a id="agroup__stats__apis_html_ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce"></a>
<a id="agroup__stats__apis_html_ga725e1bf6b2c486de9603954974d6315a"></a>
<a id="agroup__stats__apis_html_gac5d5050e8684027a3efb5a8e7a830be6"></a>
<a id="agroup__stats__apis_html_gae8e85c3ce2d901f4668d7237b19999fe"></a>
<a id="agroup__sys-util_html_gac5bc561d1bfd1bf68877fe577779bd2f"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aposix_2sys_2socket_8h_html_adee01662b0cf762a014efd87ab811276"></a>
<a id="aslist_8h_html"></a>
<a id="astats_2stats_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice__state_html"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_abe18f600adc4ab760963928477cc944e"></a>
<a id="astructsmbus__callback_html"></a>
<a id="astructsmbus__callback_html_a2017d57f8b1bbed10d37cb24a5212bc1"></a>
<a id="astructsmbus__callback_html_a707cc2c4cd2abf214343686d84cd1594"></a>
<a id="astructsmbus__callback_html_a89fb6ad70aa53dba53aa85ebaea91f60"></a>
<a id="astructsmbus__driver__api_html"></a>
<a id="astructsmbus__driver__api_html_a14bb86acc41a9f6ff04a28c763cd1fc9"></a>
<a id="astructsmbus__driver__api_html_a163f4394378189c3b62a7d0edbd7bcf4"></a>
<a id="astructsmbus__driver__api_html_a1eefcd01d72102861706d426b00a0ef7"></a>
<a id="astructsmbus__driver__api_html_a29c68f15c646a9593d128996ed90857e"></a>
<a id="astructsmbus__driver__api_html_a409d8088579e0ad683dd277ef90f7054"></a>
<a id="astructsmbus__driver__api_html_a423f6ecc1ee690c3fde883eccd0b51f7"></a>
<a id="astructsmbus__driver__api_html_a4649b200f714e74109d9123caff24e7f"></a>
<a id="astructsmbus__driver__api_html_a56e1a43e417c7fbae3ac46a844f468fd"></a>
<a id="astructsmbus__driver__api_html_a5c55f74e8f1b77290c561e2401da105b"></a>
<a id="astructsmbus__driver__api_html_a5e710554c29d1f2c18436558ba8b5eef"></a>
<a id="astructsmbus__driver__api_html_a6f87df6a6e1357aa4e596a846ab7c84e"></a>
<a id="astructsmbus__driver__api_html_a84f25a372c9bffce838dab75dd6d2d57"></a>
<a id="astructsmbus__driver__api_html_a93f02fcdb7627add8d0e61d34e9d92c4"></a>
<a id="astructsmbus__driver__api_html_a9a7c94ae7e2a45ddb80205a2f49aadcd"></a>
<a id="astructsmbus__driver__api_html_aa4132b2215173c4856962668344239ef"></a>
<a id="astructsmbus__driver__api_html_aa96bb1fb738fc8607e6c883ce7cf339c"></a>
<a id="astructsmbus__driver__api_html_af023009a650c30d4eb2774f904b20dc1"></a>
<a id="astructsmbus__dt__spec_html"></a>
<a id="astructsmbus__dt__spec_html_a0f6080e33e04405a42e9d29118512d08"></a>
<a id="astructsmbus__dt__spec_html_a2b34afb2bc5d55382bc11e0a5ee72684"></a>

```c
/*
 * Copyright (c) 2022 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SMBUS_H_
#define ZEPHYR_INCLUDE_DRIVERS_SMBUS_H_


#include <errno.h>
#include <zephyr/sys/slist.h>
#include <zephyr/types.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


#define SMBUS_CMD_QUICK                 0b000

#define SMBUS_CMD_BYTE                  0b001

#define SMBUS_CMD_BYTE_DATA             0b010

#define SMBUS_CMD_WORD_DATA             0b011

#define SMBUS_CMD_PROC_CALL             0b100

#define SMBUS_CMD_BLOCK                 0b101

#define SMBUS_CMD_BLOCK_PROC            0b111

#define SMBUS_BLOCK_BYTES_MAX           32


#define SMBUS_MODE_CONTROLLER           BIT(0)

#define SMBUS_MODE_PEC                  BIT(1)

#define SMBUS_MODE_HOST_NOTIFY          BIT(2)

#define SMBUS_MODE_SMBALERT             BIT(3)



#define SMBUS_ADDRESS_ARA               0x0c



enum smbus_direction {
        SMBUS_MSG_WRITE = 0,
        SMBUS_MSG_READ = 1,
};


#define SMBUS_MSG_RW_MASK               BIT(0)

struct smbus_callback;

typedef void (*smbus_callback_handler_t)(const struct device *dev,
                                         struct smbus_callback *cb,
                                         uint8_t addr);

struct smbus_callback {
        sys_snode_t node;

        smbus_callback_handler_t handler;

        uint8_t addr;
};

struct smbus_dt_spec {
        const struct device *bus;
        uint16_t addr;
};

#define SMBUS_DT_SPEC_GET(node_id)                              \
        {                                                       \
                .bus = DEVICE_DT_GET(DT_BUS(node_id)),          \
                .addr = DT_REG_ADDR(node_id)                    \
        }

#define SMBUS_DT_SPEC_INST_GET(inst) SMBUS_DT_SPEC_GET(DT_DRV_INST(inst))


typedef int (*smbus_api_configure_t)(const struct device *dev,
                                     uint32_t dev_config);
typedef int (*smbus_api_get_config_t)(const struct device *dev,
                                      uint32_t *dev_config);
typedef int (*smbus_api_quick_t)(const struct device *dev,
                                 uint16_t addr, enum smbus_direction);
typedef int (*smbus_api_byte_write_t)(const struct device *dev,
                                      uint16_t addr, uint8_t byte);
typedef int (*smbus_api_byte_read_t)(const struct device *dev,
                                     uint16_t addr, uint8_t *byte);
typedef int (*smbus_api_byte_data_write_t)(const struct device *dev,
                                           uint16_t addr, uint8_t cmd,
                                           uint8_t byte);
typedef int (*smbus_api_byte_data_read_t)(const struct device *dev,
                                          uint16_t addr, uint8_t cmd,
                                          uint8_t *byte);
typedef int (*smbus_api_word_data_write_t)(const struct device *dev,
                                           uint16_t addr, uint8_t cmd,
                                           uint16_t word);
typedef int (*smbus_api_word_data_read_t)(const struct device *dev,
                                          uint16_t addr, uint8_t cmd,
                                          uint16_t *word);
typedef int (*smbus_api_pcall_t)(const struct device *dev,
                                 uint16_t addr, uint8_t cmd,
                                 uint16_t send_word, uint16_t *recv_word);
typedef int (*smbus_api_block_write_t)(const struct device *dev,
                                       uint16_t addr, uint8_t cmd,
                                       uint8_t count, uint8_t *buf);
typedef int (*smbus_api_block_read_t)(const struct device *dev,
                                      uint16_t addr, uint8_t cmd,
                                      uint8_t *count, uint8_t *buf);
typedef int (*smbus_api_block_pcall_t)(const struct device *dev,
                                       uint16_t addr, uint8_t cmd,
                                       uint8_t send_count, uint8_t *send_buf,
                                       uint8_t *recv_count, uint8_t *recv_buf);
typedef int (*smbus_api_smbalert_cb_t)(const struct device *dev,
                                       struct smbus_callback *cb);
typedef int (*smbus_api_host_notify_cb_t)(const struct device *dev,
                                          struct smbus_callback *cb);

__subsystem struct smbus_driver_api {
        smbus_api_configure_t configure;
        smbus_api_get_config_t get_config;
        smbus_api_quick_t smbus_quick;
        smbus_api_byte_write_t smbus_byte_write;
        smbus_api_byte_read_t smbus_byte_read;
        smbus_api_byte_data_write_t smbus_byte_data_write;
        smbus_api_byte_data_read_t smbus_byte_data_read;
        smbus_api_word_data_write_t smbus_word_data_write;
        smbus_api_word_data_read_t smbus_word_data_read;
        smbus_api_pcall_t smbus_pcall;
        smbus_api_block_write_t smbus_block_write;
        smbus_api_block_read_t smbus_block_read;
        smbus_api_block_pcall_t smbus_block_pcall;
        smbus_api_smbalert_cb_t smbus_smbalert_set_cb;
        smbus_api_smbalert_cb_t smbus_smbalert_remove_cb;
        smbus_api_host_notify_cb_t smbus_host_notify_set_cb;
        smbus_api_host_notify_cb_t smbus_host_notify_remove_cb;
};


#if defined(CONFIG_SMBUS_STATS) || defined(__DOXYGEN__)

#include <zephyr/stats/stats.h>


STATS_SECT_START(smbus)
STATS_SECT_ENTRY32(bytes_read)
STATS_SECT_ENTRY32(bytes_written)
STATS_SECT_ENTRY32(command_count)
STATS_SECT_END;

STATS_NAME_START(smbus)
STATS_NAME(smbus, bytes_read)
STATS_NAME(smbus, bytes_written)
STATS_NAME(smbus, command_count)
STATS_NAME_END(smbus);

struct smbus_device_state {
        struct device_state devstate;
        struct stats_smbus stats;
};

#define Z_SMBUS_DEVICE_STATE_DEFINE(node_id, dev_name)                  \
        static struct smbus_device_state Z_DEVICE_STATE_NAME(dev_name)  \
        __attribute__((__section__(".z_devstate")));

#define Z_SMBUS_INIT_FN(dev_name, init_fn)                              \
        static inline int                                               \
                UTIL_CAT(dev_name, _init)(const struct device *dev)     \
        {                                                               \
                struct smbus_device_state *state =                      \
                        CONTAINER_OF(dev->state,                        \
                                     struct smbus_device_state,         \
                                     devstate);                         \
                stats_init(&state->stats.s_hdr, STATS_SIZE_32, 4,       \
                           STATS_NAME_INIT_PARMS(smbus));               \
                stats_register(dev->name, &(state->stats.s_hdr));       \
                return init_fn(dev);                                    \
        }


static inline void smbus_xfer_stats(const struct device *dev, uint8_t sent,
                                    uint8_t recv)
{
        struct smbus_device_state *state =
                CONTAINER_OF(dev->state, struct smbus_device_state, devstate);

        STATS_INC(state->stats, command_count);
        STATS_INCN(state->stats, bytes_read, recv);
        STATS_INCN(state->stats, bytes_written, sent);
}

#define SMBUS_DEVICE_DT_DEFINE(node_id, init_fn, pm_device,             \
                               data_ptr, cfg_ptr, level, prio,          \
                               api_ptr, ...)                            \
        Z_SMBUS_DEVICE_STATE_DEFINE(node_id,                            \
                                    Z_DEVICE_DT_DEV_NAME(node_id));     \
        Z_SMBUS_INIT_FN(Z_DEVICE_DT_DEV_NAME(node_id), init_fn)         \
        Z_DEVICE_DEFINE(node_id, Z_DEVICE_DT_DEV_NAME(node_id),         \
                        DEVICE_DT_NAME(node_id),                        \
                        &UTIL_CAT(Z_DEVICE_DT_DEV_NAME(node_id), _init),\
                        NULL, Z_DEVICE_DT_FLAGS(node_id), pm_device,    \
                        data_ptr, cfg_ptr, level, prio,                 \
                        api_ptr,                                        \
                        &(Z_DEVICE_STATE_NAME(Z_DEVICE_DT_DEV_NAME      \
                                              (node_id)).devstate),     \
                        __VA_ARGS__)

#else /* CONFIG_SMBUS_STATS */

static inline void smbus_xfer_stats(const struct device *dev, uint8_t sent,
                                    uint8_t recv)
{
        ARG_UNUSED(dev);
        ARG_UNUSED(sent);
        ARG_UNUSED(recv);
}

#define SMBUS_DEVICE_DT_DEFINE(node_id, init_fn, pm_device,             \
                             data_ptr, cfg_ptr, level, prio,            \
                             api_ptr, ...)                              \
        DEVICE_DT_DEFINE(node_id, &init_fn, pm_device,                  \
                             data_ptr, cfg_ptr, level, prio,            \
                             api_ptr, __VA_ARGS__)

#endif /* CONFIG_SMBUS_STATS */

#define SMBUS_DEVICE_DT_INST_DEFINE(inst, ...)          \
        SMBUS_DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)

__syscall int smbus_configure(const struct device *dev, uint32_t dev_config);

static inline int z_impl_smbus_configure(const struct device *dev,
                                         uint32_t dev_config)
{
        return DEVICE_API_GET(smbus, dev)->configure(dev, dev_config);
}

__syscall int smbus_get_config(const struct device *dev, uint32_t *dev_config);

static inline int z_impl_smbus_get_config(const struct device *dev,
                                          uint32_t *dev_config)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->get_config == NULL) {
                return -ENOSYS;
        }

        return api->get_config(dev, dev_config);
}

static inline int smbus_smbalert_set_cb(const struct device *dev,
                                        struct smbus_callback *cb)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_smbalert_set_cb == NULL) {
                return -ENOSYS;
        }

        return api->smbus_smbalert_set_cb(dev, cb);
}

static inline int smbus_smbalert_remove_cb(const struct device *dev,
                                           struct smbus_callback *cb)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_smbalert_remove_cb == NULL) {
                return -ENOSYS;
        }

        return api->smbus_smbalert_remove_cb(dev, cb);
}

static inline int smbus_host_notify_set_cb(const struct device *dev,
                                           struct smbus_callback *cb)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_host_notify_set_cb == NULL) {
                return -ENOSYS;
        }

        return api->smbus_host_notify_set_cb(dev, cb);
}

static inline int smbus_host_notify_remove_cb(const struct device *dev,
                                              struct smbus_callback *cb)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_host_notify_remove_cb == NULL) {
                return -ENOSYS;
        }

        return api->smbus_host_notify_remove_cb(dev, cb);
}

__syscall int smbus_quick(const struct device *dev, uint16_t addr,
                          enum smbus_direction direction);

static inline int z_impl_smbus_quick(const struct device *dev, uint16_t addr,
                                     enum smbus_direction direction)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_quick == NULL) {
                return -ENOSYS;
        }

        if (direction != SMBUS_MSG_READ && direction != SMBUS_MSG_WRITE) {
                return -EINVAL;
        }

        return  api->smbus_quick(dev, addr, direction);
}

__syscall int smbus_byte_write(const struct device *dev, uint16_t addr,
                               uint8_t byte);

static inline int z_impl_smbus_byte_write(const struct device *dev,
                                          uint16_t addr, uint8_t byte)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_byte_write == NULL) {
                return -ENOSYS;
        }

        return  api->smbus_byte_write(dev, addr, byte);
}

__syscall int smbus_byte_read(const struct device *dev, uint16_t addr,
                              uint8_t *byte);

static inline int z_impl_smbus_byte_read(const struct device *dev,
                                         uint16_t addr, uint8_t *byte)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_byte_read == NULL) {
                return -ENOSYS;
        }

        return  api->smbus_byte_read(dev, addr, byte);
}

__syscall int smbus_byte_data_write(const struct device *dev, uint16_t addr,
                                    uint8_t cmd, uint8_t byte);

static inline int z_impl_smbus_byte_data_write(const struct device *dev,
                                               uint16_t addr, uint8_t cmd,
                                               uint8_t byte)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_byte_data_write == NULL) {
                return -ENOSYS;
        }

        return  api->smbus_byte_data_write(dev, addr, cmd, byte);
}

__syscall int smbus_byte_data_read(const struct device *dev, uint16_t addr,
                                   uint8_t cmd, uint8_t *byte);

static inline int z_impl_smbus_byte_data_read(const struct device *dev,
                                              uint16_t addr, uint8_t cmd,
                                              uint8_t *byte)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_byte_data_read == NULL) {
                return -ENOSYS;
        }

        return  api->smbus_byte_data_read(dev, addr, cmd, byte);
}

__syscall int smbus_word_data_write(const struct device *dev, uint16_t addr,
                                    uint8_t cmd, uint16_t word);

static inline int z_impl_smbus_word_data_write(const struct device *dev,
                                               uint16_t addr, uint8_t cmd,
                                               uint16_t word)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_word_data_write == NULL) {
                return -ENOSYS;
        }

        return  api->smbus_word_data_write(dev, addr, cmd, word);
}

__syscall int smbus_word_data_read(const struct device *dev, uint16_t addr,
                                   uint8_t cmd, uint16_t *word);

static inline int z_impl_smbus_word_data_read(const struct device *dev,
                                              uint16_t addr, uint8_t cmd,
                                              uint16_t *word)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_word_data_read == NULL) {
                return -ENOSYS;
        }

        return  api->smbus_word_data_read(dev, addr, cmd, word);
}

__syscall int smbus_pcall(const struct device *dev, uint16_t addr,
                          uint8_t cmd, uint16_t send_word, uint16_t *recv_word);

static inline int z_impl_smbus_pcall(const struct device *dev,
                                     uint16_t addr, uint8_t cmd,
                                     uint16_t send_word, uint16_t *recv_word)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_pcall == NULL) {
                return -ENOSYS;
        }

        return  api->smbus_pcall(dev, addr, cmd, send_word, recv_word);
}

__syscall int smbus_block_write(const struct device *dev, uint16_t addr,
                                uint8_t cmd, uint8_t count, uint8_t *buf);

static inline int z_impl_smbus_block_write(const struct device *dev,
                                           uint16_t addr, uint8_t cmd,
                                           uint8_t count, uint8_t *buf)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_block_write == NULL) {
                return -ENOSYS;
        }

        if (count < 1 || count > SMBUS_BLOCK_BYTES_MAX) {
                return -EINVAL;
        }

        return  api->smbus_block_write(dev, addr, cmd, count, buf);
}

__syscall int smbus_block_read(const struct device *dev, uint16_t addr,
                               uint8_t cmd, uint8_t *count, uint8_t *buf);

static inline int z_impl_smbus_block_read(const struct device *dev,
                                          uint16_t addr, uint8_t cmd,
                                          uint8_t *count, uint8_t *buf)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_block_read == NULL) {
                return -ENOSYS;
        }

        return  api->smbus_block_read(dev, addr, cmd, count, buf);
}

__syscall int smbus_block_pcall(const struct device *dev,
                                uint16_t addr, uint8_t cmd,
                                uint8_t snd_count, uint8_t *snd_buf,
                                uint8_t *rcv_count, uint8_t *rcv_buf);

static inline int z_impl_smbus_block_pcall(const struct device *dev,
                                           uint16_t addr, uint8_t cmd,
                                           uint8_t snd_count, uint8_t *snd_buf,
                                           uint8_t *rcv_count, uint8_t *rcv_buf)
{
        const struct smbus_driver_api *api = DEVICE_API_GET(smbus, dev);

        if (api->smbus_block_pcall == NULL) {
                return -ENOSYS;
        }

        if (snd_count < 1 || snd_count > SMBUS_BLOCK_BYTES_MAX) {
                return -EINVAL;
        }

        return  api->smbus_block_pcall(dev, addr, cmd, snd_count, snd_buf,
                                       rcv_count, rcv_buf);
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/smbus.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_SMBUS_H_ */
```

## 27.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 597 行

条件编译配置（Configuration）标记：`CONFIG_SMBUS_STATS`。

### 注释 3：原第 614 行

条件编译配置（Configuration）标记：`CONFIG_SMBUS_STATS`。

### 注释 4：原第 1153 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SMBUS_H_`。

## 27.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P027_zephyr__drivers__smbus.h_头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [smbus_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gad0c28687977d0a7866bdea87aef88016)
- [SMBUS_MSG_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54)
- [SMBUS_MSG_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f)
- [smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)
- [smbus_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga6d6ee9d29de5c0007d34328eb7c9f7c9)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [addr](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md#a707cc2c4cd2abf214343686d84cd1594)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md#a89fb6ad70aa53dba53aa85ebaea91f60)
- [handler](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md#a2017d57f8b1bbed10d37cb24a5212bc1)
- [smbus_dt_spec](../peripheral_bus_storage_model_reference/P093_smbus_dt_spec_结构体.md)
- [bus](../peripheral_bus_storage_model_reference/P093_smbus_dt_spec_结构体.md#a2b34afb2bc5d55382bc11e0a5ee72684)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [addr](../peripheral_bus_storage_model_reference/P093_smbus_dt_spec_结构体.md#a0f6080e33e04405a42e9d29118512d08)
- [smbus_api_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga5fa53c3cd255001a2c34b36a3d23be6f)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [smbus_api_get_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gace2a4372975b44428fb39015e4b4bb25)
- [smbus_api_quick_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga93ce314c2797a21ed0b01bb28c69aeaf)
- [smbus_api_byte_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga2a59de36841ca4ff5fb65e29c512cd4e)
- [smbus_api_byte_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gae25c3c8652730085ec31701a48f086b5)
- [smbus_api_byte_data_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga7827a1f9c5cf8c2b33c79e09d05019ca)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [smbus_api_byte_data_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga36f67cfe281dea020b6036399e433f4a)
- [smbus_api_word_data_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga31f2a46f83fe193f05cc5494435e2e6f)
- [smbus_api_word_data_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga94b1bf5e10799ab1f07cccb289033ca6)
- [smbus_api_pcall_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gaabd1e34153c852469e74e9fdc4118c84)
- [smbus_api_block_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gad118b4dc6c7bdea57a6d70240d804b02)
- [smbus_api_block_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gad7453c161b4fa3c6085c186b39301659)
- [smbus_api_block_pcall_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga8e71f105c10414e4ae86b87345e70837)
- [smbus_api_smbalert_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga9a81152429fd1f70e699f6767feb8702)
- [smbus_api_host_notify_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga82dc504437f78c488df25ecd63a83a5e)
- [smbus_driver_api](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md)
- [configure](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#af023009a650c30d4eb2774f904b20dc1)
- [get_config](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a163f4394378189c3b62a7d0edbd7bcf4)
- [smbus_quick](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#aa4132b2215173c4856962668344239ef)
- [smbus_byte_write](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a93f02fcdb7627add8d0e61d34e9d92c4)
- [smbus_byte_read](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a9a7c94ae7e2a45ddb80205a2f49aadcd)
- [smbus_byte_data_write](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a14bb86acc41a9f6ff04a28c763cd1fc9)
- [smbus_byte_data_read](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a6f87df6a6e1357aa4e596a846ab7c84e)
- [smbus_word_data_write](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a56e1a43e417c7fbae3ac46a844f468fd)
- [smbus_word_data_read](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a1eefcd01d72102861706d426b00a0ef7)
- [smbus_pcall](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a29c68f15c646a9593d128996ed90857e)
- [smbus_block_write](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a5c55f74e8f1b77290c561e2401da105b)
- [smbus_block_read](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a409d8088579e0ad683dd277ef90f7054)
- [smbus_block_pcall](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#aa96bb1fb738fc8607e6c883ce7cf339c)
- [smbus_smbalert_set_cb](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a5e710554c29d1f2c18436558ba8b5eef)
- [smbus_smbalert_remove_cb](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a84f25a372c9bffce838dab75dd6d2d57)
- [smbus_host_notify_set_cb](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a4649b200f714e74109d9123caff24e7f)
- [smbus_host_notify_remove_cb](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a423f6ecc1ee690c3fde883eccd0b51f7)
- [zephyr/stats/stats.h](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h.html)
- [STATS_SECT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gae8e85c3ce2d901f4668d7237b19999fe)
- [STATS_SECT_ENTRY32](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga592329613cc77cfa5dee3e1d3b16dd93)
- [STATS_SECT_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga4124f8c0a9ffb78d8be608a780676785)
- [STATS_NAME_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga5fba46e743c05b4f36df91a86c37e30d)
- [STATS_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga498c4ee3baf1a4e21a6a5b0766d9b74e)
- [STATS_NAME_END](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga65fd76fb9bc5dd7d5ef8a1f0e82d36ce)
- [device_state](../device_reference/P003_设备运行状态结构.md)
- [smbus_xfer_stats](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga0a63b800c14f5831730372b9bad41864)
- [recv](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#adee01662b0cf762a014efd87ab811276)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [CONTAINER_OF](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f)
- [state](../device_reference/P002_设备对象结构.md#abe18f600adc4ab760963928477cc944e)
- [STATS_INC](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga725e1bf6b2c486de9603954974d6315a)
- [STATS_INCN](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gac5d5050e8684027a3efb5a8e7a830be6)
- [smbus_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga517305aa7cc9c93ae449b3c548d6c835)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [smbus_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga9ca38ca95c0576bdc75b7eb8d0ca29ef)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [smbus_smbalert_set_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gadff533a6bc198815ee56d03a36b949e0)
- [smbus_smbalert_remove_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gaa18281b8f9859e46a138a874a8873366)
- [smbus_host_notify_set_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga5054a6de634b015f54dacbe81427d0d2)
- [smbus_host_notify_remove_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga9190cfe3ce0c41c0a37d5345bad812d4)
- [smbus_quick](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gab008499bca4a4096672d5909fa71b21d)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [smbus_byte_write](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga7dd01c1e00a0f8b0315e442707332251)
- [smbus_byte_read](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gadaef9dad3470a7e4d3360e0246271ca1)
- [smbus_byte_data_write](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gadd7ec1eb3db981efceb8f959546a3b6a)
- [smbus_byte_data_read](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga1f1148a7cb92e0e0aef7ae3a84615c9b)
- [smbus_word_data_write](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gade05f9bbbba609832df91fe804dd5d3c)
- [smbus_word_data_read](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga72a789110c7286a51c5cd5e2215abce1)
- [smbus_pcall](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga2c1369835d3783bb5b5c3cb3711fec92)
- [smbus_block_write](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga55a867cdcb504039f274abae2d1a99e4)
- [SMBUS_BLOCK_BYTES_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga5ccde036931dc54e684ae5b955ff80d3)
- [smbus_block_read](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga67603db9b44636b0b62a24fd623cfb1c)
- [smbus_block_pcall](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga680c3d713a615f4b62503d6f84de4290)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [stats.h](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h.html)
- [device::state](../device_reference/P002_设备对象结构.md#abe18f600adc4ab760963928477cc944e)
- [smbus_callback::handler](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md#a2017d57f8b1bbed10d37cb24a5212bc1)
- [smbus_callback::addr](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md#a707cc2c4cd2abf214343686d84cd1594)
- [smbus_callback::node](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md#a89fb6ad70aa53dba53aa85ebaea91f60)
- [smbus_driver_api::smbus_byte_data_write](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a14bb86acc41a9f6ff04a28c763cd1fc9)
- [smbus_driver_api::get_config](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a163f4394378189c3b62a7d0edbd7bcf4)
- [smbus_driver_api::smbus_word_data_read](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a1eefcd01d72102861706d426b00a0ef7)
- [smbus_driver_api::smbus_pcall](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a29c68f15c646a9593d128996ed90857e)
- [smbus_driver_api::smbus_block_read](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a409d8088579e0ad683dd277ef90f7054)
- [smbus_driver_api::smbus_host_notify_remove_cb](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a423f6ecc1ee690c3fde883eccd0b51f7)
- [smbus_driver_api::smbus_host_notify_set_cb](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a4649b200f714e74109d9123caff24e7f)
- [smbus_driver_api::smbus_word_data_write](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a56e1a43e417c7fbae3ac46a844f468fd)
- [smbus_driver_api::smbus_block_write](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a5c55f74e8f1b77290c561e2401da105b)
- [smbus_driver_api::smbus_smbalert_set_cb](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a5e710554c29d1f2c18436558ba8b5eef)
- [smbus_driver_api::smbus_byte_data_read](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a6f87df6a6e1357aa4e596a846ab7c84e)
- [smbus_driver_api::smbus_smbalert_remove_cb](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a84f25a372c9bffce838dab75dd6d2d57)
- [smbus_driver_api::smbus_byte_write](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a93f02fcdb7627add8d0e61d34e9d92c4)
- [smbus_driver_api::smbus_byte_read](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#a9a7c94ae7e2a45ddb80205a2f49aadcd)
- [smbus_driver_api::smbus_quick](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#aa4132b2215173c4856962668344239ef)
- [smbus_driver_api::smbus_block_pcall](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#aa96bb1fb738fc8607e6c883ce7cf339c)
- [smbus_driver_api::configure](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md#af023009a650c30d4eb2774f904b20dc1)
- [smbus_dt_spec::addr](../peripheral_bus_storage_model_reference/P093_smbus_dt_spec_结构体.md#a0f6080e33e04405a42e9d29118512d08)
- [smbus_dt_spec::bus](../peripheral_bus_storage_model_reference/P093_smbus_dt_spec_结构体.md#a2b34afb2bc5d55382bc11e0a5ee72684)

---

[上一章](P026_zephyr__drivers__sent__sent.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__drivers__swdp.h_头文件源码.md)
