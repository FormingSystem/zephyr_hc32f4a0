---
id: learning.zephyr-docs.api-source-reference.page-69
title: cap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_cap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h.html)。

## 69.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="foldopen00084"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="foldopen00298"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="foldopen00306"></a>
<a id="l00306"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="foldopen00320"></a>
<a id="l00320"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="foldopen00391"></a>
<a id="l00391"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="foldopen00405"></a>
<a id="l00405"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="foldopen00414"></a>
<a id="l00414"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="foldopen00558"></a>
<a id="l00558"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="foldopen00576"></a>
<a id="l00576"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="foldopen00600"></a>
<a id="l00600"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="foldopen00612"></a>
<a id="l00612"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="foldopen00628"></a>
<a id="l00628"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="foldopen00640"></a>
<a id="l00640"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00691"></a>
<a id="l00692"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="foldopen00762"></a>
<a id="l00762"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="foldopen00780"></a>
<a id="l00780"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="foldopen00792"></a>
<a id="l00792"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00845"></a>
<a id="l00846"></a>
<a id="l00854"></a>
<a id="l00855"></a>
<a id="l00856"></a>
<a id="l00857"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00879"></a>
<a id="l00880"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="l00950"></a>
<a id="l00951"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l00995"></a>
<a id="foldopen00997"></a>
<a id="l00997"></a>
<a id="l00999"></a>
<a id="l01000"></a>
<a id="l01002"></a>
<a id="l01003"></a>
<a id="l01012"></a>
<a id="l01013"></a>
<a id="l01015"></a>
<a id="l01016"></a>
<a id="l01018"></a>
<a id="l01019"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="foldopen01029"></a>
<a id="l01029"></a>
<a id="l01042"></a>
<a id="l01043"></a>
<a id="l01054"></a>
<a id="l01055"></a>
<a id="l01056"></a>
<a id="l01057"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01090"></a>
<a id="l01091"></a>
<a id="l01109"></a>
<a id="l01110"></a>
<a id="l01111"></a>
<a id="foldopen01113"></a>
<a id="l01113"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01134"></a>
<a id="l01135"></a>
<a id="l01140"></a>
<a id="l01141"></a>
<a id="l01147"></a>
<a id="l01148"></a>
<a id="l01150"></a>
<a id="l01151"></a>
<a id="l01153"></a>
<a id="l01154"></a>
<a id="l01155"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="l01170"></a>
<a id="l01198"></a>
<a id="l01199"></a>
<a id="foldopen01201"></a>
<a id="l01201"></a>
<a id="l01215"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01230"></a>
<a id="l01231"></a>
<a id="l01242"></a>
<a id="l01243"></a>
<a id="l01244"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01258"></a>
<a id="l01269"></a>
<a id="l01270"></a>
<a id="l01281"></a>
<a id="l01282"></a>
<a id="l01283"></a>
<a id="l01284"></a>
<a id="l01285"></a>
<a id="l01296"></a>
<a id="l01307"></a>
<a id="l01318"></a>
<a id="l01319"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="l01331"></a>
<a id="l01332"></a>
<a id="l01341"></a>
<a id="l01342"></a>
<a id="l01361"></a>
<a id="l01362"></a>
<a id="l01390"></a>
<a id="l01391"></a>
<a id="foldopen01396"></a>
<a id="l01396"></a>
<a id="l01398"></a>
<a id="l01399"></a>
<a id="l01401"></a>
<a id="l01402"></a>
<a id="l01404"></a>
<a id="l01405"></a>
<a id="l01411"></a>
<a id="l01412"></a>
<a id="l01414"></a>
<a id="l01415"></a>
<a id="l01421"></a>
<a id="l01422"></a>
<a id="l01424"></a>
<a id="l01425"></a>
<a id="l01426"></a>
<a id="foldopen01428"></a>
<a id="l01428"></a>
<a id="l01430"></a>
<a id="l01431"></a>
<a id="l01433"></a>
<a id="l01434"></a>
<a id="l01436"></a>
<a id="l01437"></a>
<a id="l01438"></a>
<a id="l01447"></a>
<a id="l01448"></a>
<a id="l01449"></a>
<a id="foldopen01451"></a>
<a id="l01451"></a>
<a id="l01453"></a>
<a id="l01454"></a>
<a id="l01456"></a>
<a id="l01457"></a>
<a id="l01459"></a>
<a id="l01460"></a>
<a id="l01461"></a>
<a id="foldopen01463"></a>
<a id="l01463"></a>
<a id="l01465"></a>
<a id="l01466"></a>
<a id="l01468"></a>
<a id="l01469"></a>
<a id="l01471"></a>
<a id="l01472"></a>
<a id="l01473"></a>
<a id="l01482"></a>
<a id="l01483"></a>
<a id="l01484"></a>
<a id="foldopen01486"></a>
<a id="l01486"></a>
<a id="l01488"></a>
<a id="l01489"></a>
<a id="l01491"></a>
<a id="l01492"></a>
<a id="l01493"></a>
<a id="foldopen01495"></a>
<a id="l01495"></a>
<a id="l01497"></a>
<a id="l01498"></a>
<a id="l01500"></a>
<a id="l01501"></a>
<a id="l01503"></a>
<a id="l01504"></a>
<a id="l01515"></a>
<a id="l01516"></a>
<a id="l01517"></a>
<a id="l01526"></a>
<a id="l01527"></a>
<a id="l01528"></a>
<a id="foldopen01530"></a>
<a id="l01530"></a>
<a id="l01532"></a>
<a id="l01533"></a>
<a id="l01535"></a>
<a id="l01536"></a>
<a id="l01538"></a>
<a id="l01539"></a>
<a id="l01541"></a>
<a id="l01542"></a>
<a id="l01543"></a>
<a id="l01551"></a>
<a id="l01552"></a>
<a id="foldopen01557"></a>
<a id="l01557"></a>
<a id="l01559"></a>
<a id="l01560"></a>
<a id="l01566"></a>
<a id="l01567"></a>
<a id="l01568"></a>
<a id="foldopen01570"></a>
<a id="l01570"></a>
<a id="l01572"></a>
<a id="l01573"></a>
<a id="l01575"></a>
<a id="l01576"></a>
<a id="l01578"></a>
<a id="l01579"></a>
<a id="l01580"></a>
<a id="l01588"></a>
<a id="l01589"></a>
<a id="l01590"></a>
<a id="foldopen01592"></a>
<a id="l01592"></a>
<a id="l01594"></a>
<a id="l01595"></a>
<a id="l01597"></a>
<a id="l01598"></a>
<a id="l01600"></a>
<a id="l01601"></a>
<a id="l01607"></a>
<a id="l01608"></a>
<a id="l01609"></a>
<a id="l01617"></a>
<a id="l01618"></a>
<a id="l01619"></a>
<a id="foldopen01621"></a>
<a id="l01621"></a>
<a id="l01623"></a>
<a id="l01624"></a>
<a id="l01626"></a>
<a id="l01627"></a>
<a id="l01629"></a>
<a id="l01630"></a>
<a id="l01636"></a>
<a id="l01637"></a>
<a id="l01638"></a>
<a id="l01646"></a>
<a id="l01647"></a>
<a id="l01648"></a>
<a id="foldopen01653"></a>
<a id="l01653"></a>
<a id="l01655"></a>
<a id="l01656"></a>
<a id="l01658"></a>
<a id="l01659"></a>
<a id="l01660"></a>
<a id="foldopen01662"></a>
<a id="l01662"></a>
<a id="l01664"></a>
<a id="l01665"></a>
<a id="l01667"></a>
<a id="l01668"></a>
<a id="l01670"></a>
<a id="l01671"></a>
<a id="l01672"></a>
<a id="l01680"></a>
<a id="l01681"></a>
<a id="l01682"></a>
<a id="l01683"></a>
<a id="l01684"></a>
<a id="l01685"></a>
<a id="l01689"></a>
<a id="l01690"></a>
<a id="aaddr_8h_html"></a>
<a id="abap_8h_html"></a>
<a id="abluetooth_2audio_2audio_8h_html"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="acsip_8h_html"></a>
<a id="agroup__bt__bap_html_ga443c212a736852305715452e7f165a9e"></a>
<a id="agroup__bt__cap_html_ga165c67bddcbe220050293a4c73fb6ede"></a>
<a id="agroup__bt__cap_html_ga19cc7ed5992a528a7795b76e7add6d54"></a>
<a id="agroup__bt__cap_html_ga23618d1ab7690c4d3a567228c857c89e"></a>
<a id="agroup__bt__cap_html_ga25be83bb53c8e2ab76f311eaf4f615b9"></a>
<a id="agroup__bt__cap_html_ga2bd5f9c9de719a14ffc69827dbd4fa24"></a>
<a id="agroup__bt__cap_html_ga2c6dc73fb44bca1f5bf8d39d46690b30"></a>
<a id="agroup__bt__cap_html_ga2d8b15543105078b793462b762e27741"></a>
<a id="agroup__bt__cap_html_ga38928945e67835983de3fc639c8f2764"></a>
<a id="agroup__bt__cap_html_ga45fa73b787bb4fefc73928acf3592e20"></a>
<a id="agroup__bt__cap_html_ga54d7ad68f376998510aad9c3702e9364"></a>
<a id="agroup__bt__cap_html_ga5d8c66b3890e051b838d123a1911cfd6"></a>
<a id="agroup__bt__cap_html_ga6c13996298c3e3aa33eb40f74b7bfe44"></a>
<a id="agroup__bt__cap_html_ga6c862b49aa1339225aeb05fad32c2f06"></a>
<a id="agroup__bt__cap_html_ga71b1a73b9fd4b1be8a63a79e05c1c0aa"></a>
<a id="agroup__bt__cap_html_ga78697225c6b1291dfc016e20fd605fc4"></a>
<a id="agroup__bt__cap_html_ga7abf029533fed391930257605f3c752c"></a>
<a id="agroup__bt__cap_html_ga7b5d30c07e57f4db23f72836a3b12b2b"></a>
<a id="agroup__bt__cap_html_ga7f3f6e98e7720a4711b658c4b7c85235"></a>
<a id="agroup__bt__cap_html_ga808f0e5b671689196ba6f0fc1aea7427"></a>
<a id="agroup__bt__cap_html_ga86aca9c7f2f8658f4486925c68148850"></a>
<a id="agroup__bt__cap_html_ga92336c4a56c667b608a86e45eb8d5073"></a>
<a id="agroup__bt__cap_html_ga92e4e2c12720ec25c4050cde307cd639"></a>
<a id="agroup__bt__cap_html_ga92ff8b3133b8f5cb3d3029b5d556fe77"></a>
<a id="agroup__bt__cap_html_ga958cd5925699624d23479ad2ace6b55b"></a>
<a id="agroup__bt__cap_html_ga9af37b30b6c858c24892eb1739b5330a"></a>
<a id="agroup__bt__cap_html_ga9fbddf102e29e8e969eade40fd60da4f"></a>
<a id="agroup__bt__cap_html_gaa7286837f37da38afec8c5c955306b61"></a>
<a id="agroup__bt__cap_html_gaae56deae3792740bc3e8074882c87837"></a>
<a id="agroup__bt__cap_html_gab49e8c2032a824516dc8d5f2f880dd8f"></a>
<a id="agroup__bt__cap_html_gab6239c91b9d210872396860619fb8687"></a>
<a id="agroup__bt__cap_html_gab7b273d06abf9a3cb43afdd4e3c30c8d"></a>
<a id="agroup__bt__cap_html_gac5b2b6d617a092fb98b23c41b2f52d15"></a>
<a id="agroup__bt__cap_html_gac5f94baa82fa6deade6f83346a56b5e4"></a>
<a id="agroup__bt__cap_html_gac909b00d53cf35103382f0e1d9f426b7"></a>
<a id="agroup__bt__cap_html_gac98ed5112d0ce0659bde86d149ea7b4c"></a>
<a id="agroup__bt__cap_html_gac9d750d0a22fab7852f0a04757feab6a"></a>
<a id="agroup__bt__cap_html_gacd17de17ac1d96ff17ae15a63f43ad03"></a>
<a id="agroup__bt__cap_html_gae19686be7f8aef1cc92c70fea93e1184"></a>
<a id="agroup__bt__cap_html_gae2cd451b387659b0a2021a9023d74dfa"></a>
<a id="agroup__bt__cap_html_gae4e348f74e3c12e73879082d00cdb17e"></a>
<a id="agroup__bt__cap_html_gaeaad4ea5142afe5dca741b72795ae3aa"></a>
<a id="agroup__bt__cap_html_gaf86582ad529b6ee801d1154db7e33827"></a>
<a id="agroup__bt__cap_html_gafcb9ea2122ff8058321cf85a22326abe"></a>
<a id="agroup__bt__cap_html_gafdf6f1656249ab3ae6296272dc36b66f"></a>
<a id="agroup__bt__cap_html_gaff96953334eab1a38b30720b41c0d1a6"></a>
<a id="agroup__bt__cap_html_ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4"></a>
<a id="agroup__bt__cap_html_ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468"></a>
<a id="agroup__bt__iso_html_ga5551cab9896764eec39b8e6102e561e5"></a>
<a id="aiso_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructbt__addr__le__t_html"></a>
<a id="astructbt__audio__codec__cfg_html"></a>
<a id="astructbt__bap__bass__subgroup_html"></a>
<a id="astructbt__bap__ep_html"></a>
<a id="astructbt__bap__qos__cfg_html"></a>
<a id="astructbt__bap__stream__ops_html"></a>
<a id="astructbt__bap__stream_html"></a>
<a id="astructbt__bap__unicast__group_html"></a>
<a id="astructbt__cap__broadcast__source_html"></a>
<a id="astructbt__cap__commander__broadcast__reception__start__member__param_html"></a>
<a id="astructbt__cap__commander__broadcast__reception__start__member__param_html_a184f2623ab759832a3ec9770b14c9c63"></a>
<a id="astructbt__cap__commander__broadcast__reception__start__member__param_html_a1ba6b20f822f38dd4a0ce1f8b2f2671c"></a>
<a id="astructbt__cap__commander__broadcast__reception__start__member__param_html_a2222f8ae46afed4760db56079779532d"></a>
<a id="astructbt__cap__commander__broadcast__reception__start__member__param_html_a8e6d5d1004d13069739229a7eec3abc0"></a>
<a id="astructbt__cap__commander__broadcast__reception__start__member__param_html_a93d6b4c76e730f282d24b2086c10aa3e"></a>
<a id="astructbt__cap__commander__broadcast__reception__start__member__param_html_abf47aafab0b076da675182308d89bff7"></a>
<a id="astructbt__cap__commander__broadcast__reception__start__member__param_html_acc52738756124db042ea884c82163362"></a>
<a id="astructbt__cap__commander__broadcast__reception__start__param_html"></a>
<a id="astructbt__cap__commander__broadcast__reception__start__param_html_a8bac9170f48f34fd2239da9a6d994041"></a>
<a id="astructbt__cap__commander__broadcast__reception__start__param_html_ab0fe6fe27946a349ac33f11526ca13b7"></a>
<a id="astructbt__cap__commander__broadcast__reception__start__param_html_ae4c1e6d7b345b8764f695ada56483aa1"></a>
<a id="astructbt__cap__commander__broadcast__reception__stop__member__param_html"></a>
<a id="astructbt__cap__commander__broadcast__reception__stop__member__param_html_a72d606f6a83b1c84aa41d9db22cb955a"></a>
<a id="astructbt__cap__commander__broadcast__reception__stop__member__param_html_aa934af2e197c129b1fcb1eea9359ea6d"></a>
<a id="astructbt__cap__commander__broadcast__reception__stop__member__param_html_aeeab53e8bd7ae4f36433c0d4b60c313b"></a>
<a id="astructbt__cap__commander__broadcast__reception__stop__param_html"></a>
<a id="astructbt__cap__commander__broadcast__reception__stop__param_html_a35bc972b00c10b90544da19c659fc460"></a>
<a id="astructbt__cap__commander__broadcast__reception__stop__param_html_a36ce7cd132cd41a55872985433c2934d"></a>
<a id="astructbt__cap__commander__broadcast__reception__stop__param_html_add81cdf1e3bad07b43602c8ce7c47593"></a>
<a id="astructbt__cap__commander__cb_html"></a>
<a id="astructbt__cap__commander__cb_html_a14f6a51db5a76aac015a5de617712af3"></a>
<a id="astructbt__cap__commander__cb_html_a1e83872924e1aa1293c499184ade9173"></a>
<a id="astructbt__cap__commander__cb_html_a2188c52e3daf0a695d7c42e6cac561cf"></a>
<a id="astructbt__cap__commander__cb_html_a3a7777603c23c14bc9d01cf29bc70ef7"></a>
<a id="astructbt__cap__commander__cb_html_a3bacfffef8d122db4574463777dfd507"></a>
<a id="astructbt__cap__commander__cb_html_a7dfa1903f5cd71e67b6da0f5ff2fb299"></a>
<a id="astructbt__cap__commander__cb_html_aa49e7eaf5c45d70c800f28b81f9967e5"></a>
<a id="astructbt__cap__commander__cb_html_acc9fcedf7f7abe86e055d48e6df124c7"></a>
<a id="astructbt__cap__commander__cb_html_af989b3ebe7e5cc83a1ca4b2ef080e14d"></a>
<a id="astructbt__cap__commander__change__microphone__gain__setting__member__param_html"></a>
<a id="astructbt__cap__commander__change__microphone__gain__setting__member__param_html_a5cc34236153e6a737f71cbc77f5f840e"></a>
<a id="astructbt__cap__commander__change__microphone__gain__setting__member__param_html_a8fdcc5ec143b5a73c369d6e15d276196"></a>
<a id="astructbt__cap__commander__change__microphone__gain__setting__param_html"></a>
<a id="astructbt__cap__commander__change__microphone__gain__setting__param_html_abac0f4da7b8b05067636539b2e9f9673"></a>
<a id="astructbt__cap__commander__change__microphone__gain__setting__param_html_ade5a93aee8bcff628228664c4a8428a8"></a>
<a id="astructbt__cap__commander__change__microphone__gain__setting__param_html_ae78e5d4761df00c8c8e2cfcb3e727349"></a>
<a id="astructbt__cap__commander__change__microphone__mute__state__param_html"></a>
<a id="astructbt__cap__commander__change__microphone__mute__state__param_html_a1b6e22c9c41eb24b3961927b45c98af8"></a>
<a id="astructbt__cap__commander__change__microphone__mute__state__param_html_a96007101444d3cd61dda067fa072580e"></a>
<a id="astructbt__cap__commander__change__microphone__mute__state__param_html_a9c989fe2446ee2e055778c063a6b6de1"></a>
<a id="astructbt__cap__commander__change__microphone__mute__state__param_html_a9cdb1eda2108fc341a6d7268fac689b0"></a>
<a id="astructbt__cap__commander__change__volume__mute__state__param_html"></a>
<a id="astructbt__cap__commander__change__volume__mute__state__param_html_a784542a30164a62d44fcd3f801bc29f8"></a>
<a id="astructbt__cap__commander__change__volume__mute__state__param_html_ad4cc775dc74540a2b40126dba96776cd"></a>
<a id="astructbt__cap__commander__change__volume__mute__state__param_html_ae4b664c4b8da062a83dfcc32ebd28775"></a>
<a id="astructbt__cap__commander__change__volume__mute__state__param_html_af54b6898bfcd42188cf45d65c72217d1"></a>
<a id="astructbt__cap__commander__change__volume__offset__member__param_html"></a>
<a id="astructbt__cap__commander__change__volume__offset__member__param_html_a7d9e94cd9eb79f1f7a14c8b9bb84e5a8"></a>
<a id="astructbt__cap__commander__change__volume__offset__member__param_html_a8e2e4f07be565ef1067d4955ebef50d4"></a>
<a id="astructbt__cap__commander__change__volume__offset__param_html"></a>
<a id="astructbt__cap__commander__change__volume__offset__param_html_a2610505f60d1a67ffef916dadefe841d"></a>
<a id="astructbt__cap__commander__change__volume__offset__param_html_a8c22810a91d3109c3d633156bf16dffd"></a>
<a id="astructbt__cap__commander__change__volume__offset__param_html_ae3d416680196b0ee753a80d6fccb468b"></a>
<a id="astructbt__cap__commander__change__volume__param_html"></a>
<a id="astructbt__cap__commander__change__volume__param_html_a37198e9118f80e5521f140b6aa1d2640"></a>
<a id="astructbt__cap__commander__change__volume__param_html_a983656766a28118b018a70fef186f531"></a>
<a id="astructbt__cap__commander__change__volume__param_html_ad98625aa08f54759efd349921d104c88"></a>
<a id="astructbt__cap__commander__change__volume__param_html_ada17f89c8948246d68818f2e44d5ea49"></a>
<a id="astructbt__cap__commander__distribute__broadcast__code__member__param_html"></a>
<a id="astructbt__cap__commander__distribute__broadcast__code__member__param_html_acd5d185c590ea9a64faebd354a3d5d4a"></a>
<a id="astructbt__cap__commander__distribute__broadcast__code__member__param_html_ad240bb7e1e9ad5c40eb1a031a6fbc2fe"></a>
<a id="astructbt__cap__commander__distribute__broadcast__code__param_html"></a>
<a id="astructbt__cap__commander__distribute__broadcast__code__param_html_a03be4b2fac7803de233c8a1024640cc2"></a>
<a id="astructbt__cap__commander__distribute__broadcast__code__param_html_a86316e3bf53edca67e0743072f0f2ee3"></a>
<a id="astructbt__cap__commander__distribute__broadcast__code__param_html_a9605ad1590ff0279b46d639d38278933"></a>
<a id="astructbt__cap__commander__distribute__broadcast__code__param_html_ac7d426c975c1e2324f52486abf9298b9"></a>
<a id="astructbt__cap__handover__broadcast__to__unicast__param_html"></a>
<a id="astructbt__cap__handover__broadcast__to__unicast__param_html_a1d94cd5237f209fd8617bc10dd953b18"></a>
<a id="astructbt__cap__handover__broadcast__to__unicast__param_html_a39721b75c4cf2bd626427a63602d4aef"></a>
<a id="astructbt__cap__handover__broadcast__to__unicast__param_html_a3f476e4ff18e4ca2b54fa495ec862718"></a>
<a id="astructbt__cap__handover__broadcast__to__unicast__param_html_a7cfe18cca6342c653e30de247d896c84"></a>
<a id="astructbt__cap__handover__broadcast__to__unicast__param_html_aa43bd1c2e14ecb1c652a170893f7d1ab"></a>
<a id="astructbt__cap__handover__broadcast__to__unicast__param_html_ac133453b820f16472ee1537ee84b5205"></a>
<a id="astructbt__cap__handover__broadcast__to__unicast__param_html_af0e79651b30c14a6bfd218203236e954"></a>
<a id="astructbt__cap__handover__cb_html"></a>
<a id="astructbt__cap__handover__cb_html_a0506740ed704332c3f86648bfbdd5a24"></a>
<a id="astructbt__cap__handover__cb_html_a46892bfd9ac055ae73634520b385fa51"></a>
<a id="astructbt__cap__handover__cb_html_abd00a0e3ebc35be604194de00986d6d2"></a>
<a id="astructbt__cap__handover__unicast__to__broadcast__param_html"></a>
<a id="astructbt__cap__handover__unicast__to__broadcast__param_html_a079b91898031113b6126465307bed6d0"></a>
<a id="astructbt__cap__handover__unicast__to__broadcast__param_html_a0d8ccf04a751e775581c07e89b956b6c"></a>
<a id="astructbt__cap__handover__unicast__to__broadcast__param_html_a399a28aa6eb43f892ae0810c5e90d6e6"></a>
<a id="astructbt__cap__handover__unicast__to__broadcast__param_html_a58442e418a8fb01d67560aa68bfbd2cc"></a>
<a id="astructbt__cap__handover__unicast__to__broadcast__param_html_abf15dec430b51c9c5e83ea4cb56b7845"></a>
<a id="astructbt__cap__handover__unicast__to__broadcast__param_html_acb23afa394cd883b444ece27b1784adf"></a>
<a id="astructbt__cap__initiator__broadcast__create__param_html"></a>
<a id="astructbt__cap__initiator__broadcast__create__param_html_a01d6ffb369caaf808d4b55b3b1748890"></a>
<a id="astructbt__cap__initiator__broadcast__create__param_html_a2eafc157450237cf311d6144e7431839"></a>
<a id="astructbt__cap__initiator__broadcast__create__param_html_a4432bee0e365c189996b9f70c7226542"></a>
<a id="astructbt__cap__initiator__broadcast__create__param_html_a6f562b7a696472b7784ca2e1ced4997a"></a>
<a id="astructbt__cap__initiator__broadcast__create__param_html_a8eedd8f9a896931f75642576ca37c7d5"></a>
<a id="astructbt__cap__initiator__broadcast__create__param_html_aa4d6fbd5bd13963004e381b987bbeb4d"></a>
<a id="astructbt__cap__initiator__broadcast__create__param_html_aaa6f2828416b0624b8ca15fb2139413f"></a>
<a id="astructbt__cap__initiator__broadcast__create__param_html_ae81ee3dada58a3354c70401380916cbc"></a>
<a id="astructbt__cap__initiator__broadcast__create__param_html_aee3e0244b59503311bc445f36977a85b"></a>
<a id="astructbt__cap__initiator__broadcast__stream__param_html"></a>
<a id="astructbt__cap__initiator__broadcast__stream__param_html_a72720e8423dbeb0341041cc24a9e0869"></a>
<a id="astructbt__cap__initiator__broadcast__stream__param_html_a7e5ddb85024b58d6ecbb6d7f70ef5c6a"></a>
<a id="astructbt__cap__initiator__broadcast__stream__param_html_aa4677e278d6d4823551ccfd9c27c68a4"></a>
<a id="astructbt__cap__initiator__broadcast__subgroup__param_html"></a>
<a id="astructbt__cap__initiator__broadcast__subgroup__param_html_a252140d260f47404302a721a928f4765"></a>
<a id="astructbt__cap__initiator__broadcast__subgroup__param_html_a32e99898ee97a56105497c3ae480692a"></a>
<a id="astructbt__cap__initiator__broadcast__subgroup__param_html_a577a27836a02c7a6219182f1cb0bd769"></a>
<a id="astructbt__cap__initiator__cb_html"></a>
<a id="astructbt__cap__initiator__cb_html_a06b2f73a6f6f8f3f88cd4c5bd87f4fbc"></a>
<a id="astructbt__cap__initiator__cb_html_a2e910a82209d144878b6c69c1b2723ba"></a>
<a id="astructbt__cap__initiator__cb_html_a5ef6349113a1c786a0441b6c494286d1"></a>
<a id="astructbt__cap__initiator__cb_html_a642a2f48e8f870bb1681ba58aa119de9"></a>
<a id="astructbt__cap__initiator__cb_html_a64c9b0fb0bdfcc7434d8f2854a20a666"></a>
<a id="astructbt__cap__initiator__cb_html_a65d8dd89661f92b2e71e90b69a8b4320"></a>
<a id="astructbt__cap__initiator__cb_html_a8001c24d64df0881dbfd78382c2a2db7"></a>
<a id="astructbt__cap__initiator__cb_html_a8452b3c6775d1608272893719dd3887d"></a>
<a id="astructbt__cap__initiator__cb_html_a85451f4cbf0c8e4d061a2b50b892529d"></a>
<a id="astructbt__cap__initiator__cb_html_a8c20d933b9ee1c1412d7ad719ff24683"></a>
<a id="astructbt__cap__initiator__cb_html_a8f659ac17a242eab12c404f59e42d149"></a>
<a id="astructbt__cap__initiator__cb_html_a95266741841fca83cd2769c76652154e"></a>
<a id="astructbt__cap__initiator__cb_html_aa70de1dda73ffdcbb8287f8f174984ea"></a>
<a id="astructbt__cap__initiator__cb_html_afd9b20a78b9115409d4301c8d71c4405"></a>
<a id="astructbt__cap__stream_html"></a>
<a id="astructbt__cap__stream_html_aa58c47ace3f844533ab545906ede52ba"></a>
<a id="astructbt__cap__stream_html_ad9d974d18ec42079b81107485b43bc18"></a>
<a id="astructbt__cap__unicast__audio__start__param_html"></a>
<a id="astructbt__cap__unicast__audio__start__param_html_a7d0055719cee1cb1b0a7c1b6dc88bda5"></a>
<a id="astructbt__cap__unicast__audio__start__param_html_acacd3692c807c536882dccaea074f667"></a>
<a id="astructbt__cap__unicast__audio__start__param_html_af3e7a147448a19d2fb1ef802c525636b"></a>
<a id="astructbt__cap__unicast__audio__start__stream__param_html"></a>
<a id="astructbt__cap__unicast__audio__start__stream__param_html_a109acdedd1249ea8342f06de28989d4e"></a>
<a id="astructbt__cap__unicast__audio__start__stream__param_html_a9613a24e05a362a2f70d8e433ca6b42b"></a>
<a id="astructbt__cap__unicast__audio__start__stream__param_html_aa9a13263d287a2ddb241a8dc13baeffb"></a>
<a id="astructbt__cap__unicast__audio__start__stream__param_html_abbc53d6bfad43e1b211bb8003b7eea88"></a>
<a id="astructbt__cap__unicast__audio__stop__param_html"></a>
<a id="astructbt__cap__unicast__audio__stop__param_html_a11b5ac19301ce8ebd2c35df45c60bfe2"></a>
<a id="astructbt__cap__unicast__audio__stop__param_html_a1cbd7ee2e4ceafd2da2858dc7c941d78"></a>
<a id="astructbt__cap__unicast__audio__stop__param_html_a773eedda9ae8969e8749d56ffa3d1afa"></a>
<a id="astructbt__cap__unicast__audio__stop__param_html_a94707060a6ef15dd8d3e48eae526aa82"></a>
<a id="astructbt__cap__unicast__audio__update__param_html"></a>
<a id="astructbt__cap__unicast__audio__update__param_html_a3d8f940d8401b8524764e7ecab3cfacb"></a>
<a id="astructbt__cap__unicast__audio__update__param_html_a768029ce89b74e0bcc06bb50f1fd8dcd"></a>
<a id="astructbt__cap__unicast__audio__update__param_html_ac8982f313161380af536d41ec48dcba1"></a>
<a id="astructbt__cap__unicast__audio__update__stream__param_html"></a>
<a id="astructbt__cap__unicast__audio__update__stream__param_html_a07c1ab3158377ce51d94084ad7dc3e9c"></a>
<a id="astructbt__cap__unicast__audio__update__stream__param_html_a7a2042834b79ca37e3b3df9fc2f8a7a1"></a>
<a id="astructbt__cap__unicast__audio__update__stream__param_html_a87833f9e91b47513a27db0aa7692d8c0"></a>
<a id="astructbt__cap__unicast__group__info_html"></a>
<a id="astructbt__cap__unicast__group__info_html_afbfd6705742d15081f6cf4dca21e242b"></a>
<a id="astructbt__cap__unicast__group__param_html"></a>
<a id="astructbt__cap__unicast__group__param_html_a64ca2c5cc4f34821e567841ec8efe67b"></a>
<a id="astructbt__cap__unicast__group__param_html_a97e67b903e72dd1f0fef4961810288b1"></a>
<a id="astructbt__cap__unicast__group__param_html_ab424be389b026ac5857e3bec1c3d686f"></a>
<a id="astructbt__cap__unicast__group__param_html_ab9748e9e230048af64ce9c9ce1006952"></a>
<a id="astructbt__cap__unicast__group__param_html_ac52a0e09e3978a084e4fe558e4a5a848"></a>
<a id="astructbt__cap__unicast__group__param_html_adb6cb5686b3d827156aef325b3dcdc84"></a>
<a id="astructbt__cap__unicast__group__stream__pair__param_html"></a>
<a id="astructbt__cap__unicast__group__stream__pair__param_html_a19d49ab8c0daa7e6a4c73563952ae461"></a>
<a id="astructbt__cap__unicast__group__stream__pair__param_html_a6edeca159371f3a70cc5a1f662a0e45c"></a>
<a id="astructbt__cap__unicast__group__stream__param_html"></a>
<a id="astructbt__cap__unicast__group__stream__param_html_a02672d241f243a7530eeff191e9a034b"></a>
<a id="astructbt__cap__unicast__group__stream__param_html_a16aacd43bb7b449648ab6a5a89999fba"></a>
<a id="astructbt__cap__unicast__group_html"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__csip__set__coordinator__csis__inst_html"></a>
<a id="astructbt__csip__set__coordinator__set__member_html"></a>
<a id="astructbt__csip__set__member__register__param_html"></a>
<a id="astructbt__csip__set__member__svc__inst_html"></a>
<a id="astructbt__iso__tx__info_html"></a>
<a id="astructbt__le__ext__adv_html"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="astructnet__buf_html"></a>
<a id="aunionbt__cap__set__member_html"></a>
<a id="aunionbt__cap__set__member_html_a692a1be2fbd79c4b6a0fbce564ff2973"></a>
<a id="aunionbt__cap__set__member_html_ac17db41d21a92d8d128b70962e4eb2d6"></a>

```c


/*
 * Copyright (c) 2022-2025 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CAP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CAP_H_


#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/audio/bap.h>
#include <zephyr/bluetooth/audio/csip.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/iso.h>
#include <zephyr/net_buf.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_cap_broadcast_source;

struct bt_cap_unicast_group;

int bt_cap_acceptor_register(const struct bt_csip_set_member_register_param *param,
                             struct bt_csip_set_member_svc_inst **svc_inst);

struct bt_cap_initiator_cb {
#if defined(CONFIG_BT_BAP_UNICAST_CLIENT) || defined(__DOXYGEN__)
        void (*unicast_discovery_complete)(
                struct bt_conn *conn, int err,
                const struct bt_csip_set_coordinator_set_member *member,
                const struct bt_csip_set_coordinator_csis_inst *csis_inst);

        void (*unicast_start_complete)(int err, struct bt_conn *conn);

        void (*unicast_start_codec_configured)(void);

        void (*unicast_start_qos_configured)(void);

        void (*unicast_start_enabled)(void);

        void (*unicast_start_connected)(void);

        void (*unicast_start_started)(void);

        void (*unicast_update_complete)(int err, struct bt_conn *conn);

        void (*unicast_stop_complete)(int err, struct bt_conn *conn);

        void (*unicast_stop_disabled)(void);

        void (*unicast_stop_stopped)(void);

        void (*unicast_stop_released)(void);
#endif /* CONFIG_BT_BAP_UNICAST_CLIENT */
#if defined(CONFIG_BT_BAP_BROADCAST_SOURCE) || defined(__DOXYGEN__)
        void (*broadcast_started)(struct bt_cap_broadcast_source *source);

        void (*broadcast_stopped)(struct bt_cap_broadcast_source *source, uint8_t reason);
#endif /* CONFIG_BT_BAP_BROADCAST_SOURCE */
};

int bt_cap_initiator_unicast_discover(struct bt_conn *conn);

enum bt_cap_set_type {
        BT_CAP_SET_TYPE_AD_HOC,
        BT_CAP_SET_TYPE_CSIP,
};

union bt_cap_set_member {
        struct bt_conn *member;

        struct bt_csip_set_coordinator_csis_inst *csip;
};

struct bt_cap_stream {
        struct bt_bap_stream bap_stream;

        struct bt_bap_stream_ops *ops;
};

void bt_cap_stream_ops_register(struct bt_cap_stream *stream, struct bt_bap_stream_ops *ops);

int bt_cap_stream_send(struct bt_cap_stream *stream, struct net_buf *buf, uint16_t seq_num);

int bt_cap_stream_send_ts(struct bt_cap_stream *stream, struct net_buf *buf, uint16_t seq_num,
                          uint32_t ts);

int bt_cap_stream_get_tx_sync(struct bt_cap_stream *stream, struct bt_iso_tx_info *info);

struct bt_cap_unicast_group_stream_param {
        struct bt_cap_stream *stream;

        const struct bt_bap_qos_cfg *qos_cfg;
};

struct bt_cap_unicast_group_stream_pair_param {
        struct bt_cap_unicast_group_stream_param *rx_param;

        struct bt_cap_unicast_group_stream_param *tx_param;
};

struct bt_cap_unicast_group_param {
        size_t params_count;

        struct bt_cap_unicast_group_stream_pair_param *params;

        uint8_t packing;

#if defined(CONFIG_BT_ISO_TEST_PARAMS) || defined(__DOXYGEN__)
        uint8_t c_to_p_ft;

        uint8_t p_to_c_ft;

        uint16_t iso_interval;
#endif /* CONFIG_BT_ISO_TEST_PARAMS */
};

int bt_cap_unicast_group_create(const struct bt_cap_unicast_group_param *param,
                                struct bt_cap_unicast_group **out_unicast_group);

int bt_cap_unicast_group_reconfig(struct bt_cap_unicast_group *unicast_group,
                                  const struct bt_cap_unicast_group_param *param);

int bt_cap_unicast_group_add_streams(struct bt_cap_unicast_group *unicast_group,
                                     const struct bt_cap_unicast_group_stream_pair_param params[],
                                     size_t num_param);

int bt_cap_unicast_group_delete(struct bt_cap_unicast_group *unicast_group);

typedef bool (*bt_cap_unicast_group_foreach_stream_func_t)(struct bt_cap_stream *stream,
                                                           void *user_data);

int bt_cap_unicast_group_foreach_stream(struct bt_cap_unicast_group *unicast_group,
                                        bt_cap_unicast_group_foreach_stream_func_t func,
                                        void *user_data);

struct bt_cap_unicast_group_info {
        const struct bt_bap_unicast_group *unicast_group;
};

int bt_cap_unicast_group_get_info(const struct bt_cap_unicast_group *unicast_group,
                                  struct bt_cap_unicast_group_info *info);

struct bt_cap_unicast_audio_start_stream_param {
        union bt_cap_set_member member;

        struct bt_cap_stream *stream;

        struct bt_bap_ep *ep;

        const struct bt_audio_codec_cfg *codec_cfg;
};

struct bt_cap_unicast_audio_start_param {
        enum bt_cap_set_type type;

        size_t count;

        struct bt_cap_unicast_audio_start_stream_param *stream_params;
};

struct bt_cap_unicast_audio_update_stream_param {
        struct bt_cap_stream *stream;

        size_t meta_len;

        uint8_t *meta;
};

struct bt_cap_unicast_audio_update_param {
        enum bt_cap_set_type type;

        size_t count;

        struct bt_cap_unicast_audio_update_stream_param *stream_params;
};

struct bt_cap_unicast_audio_stop_param {
        enum bt_cap_set_type type;

        size_t count;

        struct bt_cap_stream **streams;

        bool release;
};

int bt_cap_initiator_register_cb(const struct bt_cap_initiator_cb *cb);

int bt_cap_initiator_unregister_cb(const struct bt_cap_initiator_cb *cb);

int bt_cap_initiator_unicast_audio_start(const struct bt_cap_unicast_audio_start_param *param);

int bt_cap_initiator_unicast_audio_update(const struct bt_cap_unicast_audio_update_param *param);

int bt_cap_initiator_unicast_audio_stop(const struct bt_cap_unicast_audio_stop_param *param);

int bt_cap_initiator_unicast_audio_cancel(void);

struct bt_cap_initiator_broadcast_stream_param {
        struct bt_cap_stream *stream;

        size_t data_len;

        uint8_t *data;
};

struct bt_cap_initiator_broadcast_subgroup_param {
        size_t stream_count;

        struct bt_cap_initiator_broadcast_stream_param *stream_params;

        const struct bt_audio_codec_cfg *codec_cfg;
};

struct bt_cap_initiator_broadcast_create_param {
        size_t subgroup_count;

        struct bt_cap_initiator_broadcast_subgroup_param *subgroup_params;

        const struct bt_bap_qos_cfg *qos;

        uint8_t packing;

        bool encryption;

        uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE];

#if defined(CONFIG_BT_ISO_TEST_PARAMS) || defined(__DOXYGEN__)
        uint8_t irc;

        uint8_t pto;

        uint16_t iso_interval;
#endif /* CONFIG_BT_ISO_TEST_PARAMS */
};

int bt_cap_initiator_broadcast_audio_create(
        const struct bt_cap_initiator_broadcast_create_param *param,
        struct bt_cap_broadcast_source **broadcast_source);

int bt_cap_initiator_broadcast_audio_start(struct bt_cap_broadcast_source *broadcast_source,
                                           struct bt_le_ext_adv *adv);
int bt_cap_initiator_broadcast_audio_update(struct bt_cap_broadcast_source *broadcast_source,
                                            const uint8_t meta[], size_t meta_len);

int bt_cap_initiator_broadcast_audio_stop(struct bt_cap_broadcast_source *broadcast_source);

int bt_cap_initiator_broadcast_audio_delete(struct bt_cap_broadcast_source *broadcast_source);

int bt_cap_initiator_broadcast_get_base(struct bt_cap_broadcast_source *broadcast_source,
                                        struct net_buf_simple *base_buf);

typedef bool (*bt_cap_initiator_broadcast_foreach_stream_func_t)(struct bt_cap_stream *stream,
                                                                 void *user_data);

int bt_cap_initiator_broadcast_foreach_stream(struct bt_cap_broadcast_source *broadcast_source,
                                              bt_cap_initiator_broadcast_foreach_stream_func_t func,
                                              void *user_data);

struct bt_cap_handover_unicast_to_broadcast_param {
        enum bt_cap_set_type type;

        struct bt_cap_unicast_group *unicast_group;

        struct bt_le_ext_adv *ext_adv;

        uint16_t pa_interval;

        uint32_t broadcast_id;

        struct bt_cap_initiator_broadcast_create_param *broadcast_create_param;
};

struct bt_cap_handover_cb {
        void (*unicast_to_broadcast_created)(struct bt_cap_broadcast_source *broadcast_source);

        void (*unicast_to_broadcast_complete)(int err, struct bt_conn *conn,
                                              struct bt_cap_unicast_group *unicast_group,
                                              struct bt_cap_broadcast_source *broadcast_source);

        void (*broadcast_to_unicast_complete)(int err, struct bt_conn *conn,
                                              struct bt_cap_broadcast_source *broadcast_source,
                                              struct bt_cap_unicast_group *unicast_group);
};

int bt_cap_handover_register_cb(const struct bt_cap_handover_cb *cb);

int bt_cap_handover_unregister_cb(const struct bt_cap_handover_cb *cb);

int bt_cap_handover_unicast_to_broadcast(
        const struct bt_cap_handover_unicast_to_broadcast_param *param);

struct bt_cap_handover_broadcast_to_unicast_param {
        struct bt_cap_commander_broadcast_reception_stop_param *reception_stop_param;

        uint32_t broadcast_id;

        uint8_t adv_sid;

        uint8_t adv_type;

        struct bt_cap_broadcast_source *broadcast_source;

        struct bt_cap_unicast_group_param *unicast_group_param;

        struct bt_cap_unicast_audio_start_param *unicast_start_param;
};

int bt_cap_handover_broadcast_to_unicast(
        const struct bt_cap_handover_broadcast_to_unicast_param *param);

int bt_cap_handover_cancel(void);

struct bt_cap_commander_cb {
        void (*discovery_complete)(struct bt_conn *conn, int err,
                                   const struct bt_csip_set_coordinator_set_member *member,
                                   const struct bt_csip_set_coordinator_csis_inst *csis_inst);

#if defined(CONFIG_BT_VCP_VOL_CTLR) || defined(__DOXYGEN__)
        void (*volume_changed)(struct bt_conn *conn, int err);

        void (*volume_mute_changed)(struct bt_conn *conn, int err);

#if defined(CONFIG_BT_VCP_VOL_CTLR_VOCS) || defined(__DOXYGEN__)
        void (*volume_offset_changed)(struct bt_conn *conn, int err);
#endif /* CONFIG_BT_VCP_VOL_CTLR_VOCS */
#endif /* CONFIG_BT_VCP_VOL_CTLR */
#if defined(CONFIG_BT_MICP_MIC_CTLR) || defined(__DOXYGEN__)
        void (*microphone_mute_changed)(struct bt_conn *conn, int err);
#if defined(CONFIG_BT_MICP_MIC_CTLR_AICS) || defined(__DOXYGEN__)
        void (*microphone_gain_changed)(struct bt_conn *conn, int err);
#endif /* CONFIG_BT_MICP_MIC_CTLR_AICS */
#endif /* CONFIG_BT_MICP_MIC_CTLR */

#if defined(CONFIG_BT_BAP_BROADCAST_ASSISTANT) || defined(__DOXYGEN__)
        void (*broadcast_reception_start)(struct bt_conn *conn, int err);
        void (*broadcast_reception_stop)(struct bt_conn *conn, int err);
        void (*distribute_broadcast_code)(struct bt_conn *conn, int err);
#endif /* CONFIG_BT_BAP_BROADCAST_ASSISTANT */
};

int bt_cap_commander_register_cb(const struct bt_cap_commander_cb *cb);

int bt_cap_commander_unregister_cb(const struct bt_cap_commander_cb *cb);

int bt_cap_commander_discover(struct bt_conn *conn);

int bt_cap_commander_cancel(void);

struct bt_cap_commander_broadcast_reception_start_member_param {
        union bt_cap_set_member member;

        bt_addr_le_t addr;

        uint8_t adv_sid;

        uint16_t pa_interval;

        uint32_t broadcast_id;

        struct bt_bap_bass_subgroup subgroups[BT_BAP_BASS_MAX_SUBGROUPS];

        size_t num_subgroups;
};

struct bt_cap_commander_broadcast_reception_start_param {
        enum bt_cap_set_type type;

        struct bt_cap_commander_broadcast_reception_start_member_param *param;

        size_t count;
};

int bt_cap_commander_broadcast_reception_start(
        const struct bt_cap_commander_broadcast_reception_start_param *param);

struct bt_cap_commander_broadcast_reception_stop_member_param {
        union bt_cap_set_member member;

        uint8_t src_id;

        size_t num_subgroups;
};

struct bt_cap_commander_broadcast_reception_stop_param {
        enum bt_cap_set_type type;

        struct bt_cap_commander_broadcast_reception_stop_member_param *param;

        size_t count;
};

int bt_cap_commander_broadcast_reception_stop(
        const struct bt_cap_commander_broadcast_reception_stop_param *param);

struct bt_cap_commander_distribute_broadcast_code_member_param {
        union bt_cap_set_member member;

        uint8_t src_id;
};

struct bt_cap_commander_distribute_broadcast_code_param {
        enum bt_cap_set_type type;

        struct bt_cap_commander_distribute_broadcast_code_member_param *param;

        size_t count;

        uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE];
};

int bt_cap_commander_distribute_broadcast_code(
        const struct bt_cap_commander_distribute_broadcast_code_param *param);

struct bt_cap_commander_change_volume_param {
        enum bt_cap_set_type type;

        union bt_cap_set_member *members;

        size_t count;

        uint8_t volume;
};

int bt_cap_commander_change_volume(const struct bt_cap_commander_change_volume_param *param);

struct bt_cap_commander_change_volume_offset_member_param {
        union bt_cap_set_member member;

        int16_t offset;
};

struct bt_cap_commander_change_volume_offset_param {
        enum bt_cap_set_type type;

        struct bt_cap_commander_change_volume_offset_member_param *param;

        size_t count;
};

int bt_cap_commander_change_volume_offset(
        const struct bt_cap_commander_change_volume_offset_param *param);

struct bt_cap_commander_change_volume_mute_state_param {
        enum bt_cap_set_type type;

        union bt_cap_set_member *members;

        size_t count;

        bool mute;
};

int bt_cap_commander_change_volume_mute_state(
        const struct bt_cap_commander_change_volume_mute_state_param *param);

struct bt_cap_commander_change_microphone_mute_state_param {
        enum bt_cap_set_type type;

        union bt_cap_set_member *members;

        size_t count;

        bool mute;
};

int bt_cap_commander_change_microphone_mute_state(
        const struct bt_cap_commander_change_microphone_mute_state_param *param);

struct bt_cap_commander_change_microphone_gain_setting_member_param {
        union bt_cap_set_member member;

        int8_t gain;
};

struct bt_cap_commander_change_microphone_gain_setting_param {
        enum bt_cap_set_type type;

        struct bt_cap_commander_change_microphone_gain_setting_member_param *param;

        size_t count;
};

int bt_cap_commander_change_microphone_gain_setting(
        const struct bt_cap_commander_change_microphone_gain_setting_param *param);
#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CAP_H_ */
```

## 69.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2022-2025 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 263 行

条件编译配置（Configuration）标记：`CONFIG_BT_BAP_UNICAST_CLIENT`。

### 注释 3：原第 279 行

条件编译配置（Configuration）标记：`CONFIG_BT_BAP_BROADCAST_SOURCE`。

### 注释 4：原第 459 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_TEST_PARAMS`。

### 注释 5：原第 855 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_TEST_PARAMS`。

### 注释 6：原第 1256 行

条件编译配置（Configuration）标记：`CONFIG_BT_VCP_VOL_CTLR_VOCS`。

### 注释 7：原第 1257 行

条件编译配置（Configuration）标记：`CONFIG_BT_VCP_VOL_CTLR`。

### 注释 8：原第 1282 行

条件编译配置（Configuration）标记：`CONFIG_BT_MICP_MIC_CTLR_AICS`。

### 注释 9：原第 1283 行

条件编译配置（Configuration）标记：`CONFIG_BT_MICP_MIC_CTLR`。

### 注释 10：原第 1319 行

条件编译配置（Configuration）标记：`CONFIG_BT_BAP_BROADCAST_ASSISTANT`。

### 注释 11：原第 1690 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CAP_H_`。

## 69.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)
- [zephyr/bluetooth/audio/csip.h](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h.html)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)
- [bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)
- [bt_cap_acceptor_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gafcb9ea2122ff8058321cf85a22326abe)
- [bt_csip_set_member_register_param](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md)
- [bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)
- [bt_cap_initiator_cb](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md)
- [unicast_discovery_complete](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a642a2f48e8f870bb1681ba58aa119de9)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)
- [bt_csip_set_coordinator_csis_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md)
- [unicast_start_complete](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#aa70de1dda73ffdcbb8287f8f174984ea)
- [unicast_start_codec_configured](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a64c9b0fb0bdfcc7434d8f2854a20a666)
- [unicast_start_qos_configured](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a5ef6349113a1c786a0441b6c494286d1)
- [unicast_start_enabled](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a06b2f73a6f6f8f3f88cd4c5bd87f4fbc)
- [unicast_start_connected](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a8452b3c6775d1608272893719dd3887d)
- [unicast_start_started](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a65d8dd89661f92b2e71e90b69a8b4320)
- [unicast_update_complete](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a95266741841fca83cd2769c76652154e)
- [unicast_stop_complete](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a2e910a82209d144878b6c69c1b2723ba)
- [unicast_stop_disabled](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a8001c24d64df0881dbfd78382c2a2db7)
- [unicast_stop_stopped](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a8c20d933b9ee1c1412d7ad719ff24683)
- [unicast_stop_released](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a8f659ac17a242eab12c404f59e42d149)
- [broadcast_started](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#afd9b20a78b9115409d4301c8d71c4405)
- [broadcast_stopped](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a85451f4cbf0c8e4d061a2b50b892529d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_cap_initiator_unicast_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab7b273d06abf9a3cb43afdd4e3c30c8d)
- [bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)
- [BT_CAP_SET_TYPE_AD_HOC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468)
- [BT_CAP_SET_TYPE_CSIP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4)
- [bt_cap_set_member](../bluetooth_service_model_reference/P188_bt_cap_set_member_联合体.md)
- [member](../bluetooth_service_model_reference/P188_bt_cap_set_member_联合体.md#a692a1be2fbd79c4b6a0fbce564ff2973)
- [csip](../bluetooth_service_model_reference/P188_bt_cap_set_member_联合体.md#ac17db41d21a92d8d128b70962e4eb2d6)
- [bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)
- [bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)
- [bap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md#ad9d974d18ec42079b81107485b43bc18)
- [bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)
- [ops](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md#aa58c47ace3f844533ab545906ede52ba)
- [bt_cap_stream_ops_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac909b00d53cf35103382f0e1d9f426b7)
- [bt_cap_stream_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga2d8b15543105078b793462b762e27741)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_cap_stream_send_ts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga23618d1ab7690c4d3a567228c857c89e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_cap_stream_get_tx_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga7f3f6e98e7720a4711b658c4b7c85235)
- [bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)
- [bt_cap_unicast_group_stream_param](../bluetooth_service_model_reference/P049_bt_cap_unicast_group_stream_param_结构体.md)
- [stream](../bluetooth_service_model_reference/P049_bt_cap_unicast_group_stream_param_结构体.md#a16aacd43bb7b449648ab6a5a89999fba)
- [bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)
- [qos_cfg](../bluetooth_service_model_reference/P049_bt_cap_unicast_group_stream_param_结构体.md#a02672d241f243a7530eeff191e9a034b)
- [bt_cap_unicast_group_stream_pair_param](../bluetooth_service_model_reference/P048_bt_cap_unicast_group_stream_pair_param_结构体.md)
- [rx_param](../bluetooth_service_model_reference/P048_bt_cap_unicast_group_stream_pair_param_结构体.md#a19d49ab8c0daa7e6a4c73563952ae461)
- [tx_param](../bluetooth_service_model_reference/P048_bt_cap_unicast_group_stream_pair_param_结构体.md#a6edeca159371f3a70cc5a1f662a0e45c)
- [bt_cap_unicast_group_param](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md)
- [params_count](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md#ab9748e9e230048af64ce9c9ce1006952)
- [params](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md#a64ca2c5cc4f34821e567841ec8efe67b)
- [packing](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md#a97e67b903e72dd1f0fef4961810288b1)
- [c_to_p_ft](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md#adb6cb5686b3d827156aef325b3dcdc84)
- [p_to_c_ft](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md#ab424be389b026ac5857e3bec1c3d686f)
- [iso_interval](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md#ac52a0e09e3978a084e4fe558e4a5a848)
- [bt_cap_unicast_group_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab49e8c2032a824516dc8d5f2f880dd8f)
- [bt_cap_unicast_group_reconfig](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga6c862b49aa1339225aeb05fad32c2f06)
- [bt_cap_unicast_group_add_streams](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga7b5d30c07e57f4db23f72836a3b12b2b)
- [bt_cap_unicast_group_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga9af37b30b6c858c24892eb1739b5330a)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_cap_unicast_group_foreach_stream_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaeaad4ea5142afe5dca741b72795ae3aa)
- [bt_cap_unicast_group_foreach_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga6c13996298c3e3aa33eb40f74b7bfe44)
- [bt_cap_unicast_group_info](../bluetooth_service_model_reference/P046_bt_cap_unicast_group_info_结构体.md)
- [bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)
- [unicast_group](../bluetooth_service_model_reference/P046_bt_cap_unicast_group_info_结构体.md#afbfd6705742d15081f6cf4dca21e242b)
- [bt_cap_unicast_group_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga86aca9c7f2f8658f4486925c68148850)
- [bt_cap_unicast_audio_start_stream_param](../bluetooth_service_model_reference/P041_bt_cap_unicast_audio_start_stream_param_结构体.md)
- [member](../bluetooth_service_model_reference/P041_bt_cap_unicast_audio_start_stream_param_结构体.md#a9613a24e05a362a2f70d8e433ca6b42b)
- [stream](../bluetooth_service_model_reference/P041_bt_cap_unicast_audio_start_stream_param_结构体.md#a109acdedd1249ea8342f06de28989d4e)
- [bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)
- [ep](../bluetooth_service_model_reference/P041_bt_cap_unicast_audio_start_stream_param_结构体.md#aa9a13263d287a2ddb241a8dc13baeffb)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [codec_cfg](../bluetooth_service_model_reference/P041_bt_cap_unicast_audio_start_stream_param_结构体.md#abbc53d6bfad43e1b211bb8003b7eea88)
- [bt_cap_unicast_audio_start_param](../bluetooth_service_model_reference/P040_bt_cap_unicast_audio_start_param_结构体.md)
- [type](../bluetooth_service_model_reference/P040_bt_cap_unicast_audio_start_param_结构体.md#a7d0055719cee1cb1b0a7c1b6dc88bda5)
- [count](../bluetooth_service_model_reference/P040_bt_cap_unicast_audio_start_param_结构体.md#acacd3692c807c536882dccaea074f667)
- [stream_params](../bluetooth_service_model_reference/P040_bt_cap_unicast_audio_start_param_结构体.md#af3e7a147448a19d2fb1ef802c525636b)
- [bt_cap_unicast_audio_update_stream_param](../bluetooth_service_model_reference/P044_bt_cap_unicast_audio_update_stream_param_结构体.md)
- [stream](../bluetooth_service_model_reference/P044_bt_cap_unicast_audio_update_stream_param_结构体.md#a7a2042834b79ca37e3b3df9fc2f8a7a1)
- [meta_len](../bluetooth_service_model_reference/P044_bt_cap_unicast_audio_update_stream_param_结构体.md#a07c1ab3158377ce51d94084ad7dc3e9c)
- [meta](../bluetooth_service_model_reference/P044_bt_cap_unicast_audio_update_stream_param_结构体.md#a87833f9e91b47513a27db0aa7692d8c0)
- [bt_cap_unicast_audio_update_param](../bluetooth_service_model_reference/P043_bt_cap_unicast_audio_update_param_结构体.md)
- [type](../bluetooth_service_model_reference/P043_bt_cap_unicast_audio_update_param_结构体.md#a768029ce89b74e0bcc06bb50f1fd8dcd)
- [count](../bluetooth_service_model_reference/P043_bt_cap_unicast_audio_update_param_结构体.md#ac8982f313161380af536d41ec48dcba1)
- [stream_params](../bluetooth_service_model_reference/P043_bt_cap_unicast_audio_update_param_结构体.md#a3d8f940d8401b8524764e7ecab3cfacb)
- [bt_cap_unicast_audio_stop_param](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md)
- [type](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md#a773eedda9ae8969e8749d56ffa3d1afa)
- [count](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md#a11b5ac19301ce8ebd2c35df45c60bfe2)
- [streams](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md#a94707060a6ef15dd8d3e48eae526aa82)
- [release](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md#a1cbd7ee2e4ceafd2da2858dc7c941d78)
- [bt_cap_initiator_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga54d7ad68f376998510aad9c3702e9364)
- [bt_cap_initiator_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaa7286837f37da38afec8c5c955306b61)
- [bt_cap_initiator_unicast_audio_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae19686be7f8aef1cc92c70fea93e1184)
- [bt_cap_initiator_unicast_audio_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92e4e2c12720ec25c4050cde307cd639)
- [bt_cap_initiator_unicast_audio_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gafdf6f1656249ab3ae6296272dc36b66f)
- [bt_cap_initiator_unicast_audio_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga9fbddf102e29e8e969eade40fd60da4f)
- [bt_cap_initiator_broadcast_stream_param](../bluetooth_service_model_reference/P036_bt_cap_initiator_broadcast_stream_param_结构体.md)
- [stream](../bluetooth_service_model_reference/P036_bt_cap_initiator_broadcast_stream_param_结构体.md#a7e5ddb85024b58d6ecbb6d7f70ef5c6a)
- [data_len](../bluetooth_service_model_reference/P036_bt_cap_initiator_broadcast_stream_param_结构体.md#aa4677e278d6d4823551ccfd9c27c68a4)
- [data](../bluetooth_service_model_reference/P036_bt_cap_initiator_broadcast_stream_param_结构体.md#a72720e8423dbeb0341041cc24a9e0869)
- [bt_cap_initiator_broadcast_subgroup_param](../bluetooth_service_model_reference/P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md)
- [stream_count](../bluetooth_service_model_reference/P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md#a577a27836a02c7a6219182f1cb0bd769)
- [stream_params](../bluetooth_service_model_reference/P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md#a32e99898ee97a56105497c3ae480692a)
- [codec_cfg](../bluetooth_service_model_reference/P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md#a252140d260f47404302a721a928f4765)
- [bt_cap_initiator_broadcast_create_param](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md)
- [subgroup_count](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#aee3e0244b59503311bc445f36977a85b)
- [subgroup_params](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#a2eafc157450237cf311d6144e7431839)
- [qos](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#aaa6f2828416b0624b8ca15fb2139413f)
- [packing](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#ae81ee3dada58a3354c70401380916cbc)
- [encryption](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#a4432bee0e365c189996b9f70c7226542)
- [broadcast_code](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#aa4d6fbd5bd13963004e381b987bbeb4d)
- [BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)
- [irc](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#a6f562b7a696472b7784ca2e1ced4997a)
- [pto](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#a01d6ffb369caaf808d4b55b3b1748890)
- [iso_interval](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#a8eedd8f9a896931f75642576ca37c7d5)
- [bt_cap_initiator_broadcast_audio_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga78697225c6b1291dfc016e20fd605fc4)
- [bt_cap_initiator_broadcast_audio_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga2bd5f9c9de719a14ffc69827dbd4fa24)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_cap_initiator_broadcast_audio_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92336c4a56c667b608a86e45eb8d5073)
- [bt_cap_initiator_broadcast_audio_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae4e348f74e3c12e73879082d00cdb17e)
- [bt_cap_initiator_broadcast_audio_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac98ed5112d0ce0659bde86d149ea7b4c)
- [bt_cap_initiator_broadcast_get_base](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_cap_initiator_broadcast_foreach_stream_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga2c6dc73fb44bca1f5bf8d39d46690b30)
- [bt_cap_initiator_broadcast_foreach_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga45fa73b787bb4fefc73928acf3592e20)
- [bt_cap_handover_unicast_to_broadcast_param](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md)
- [type](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md#a079b91898031113b6126465307bed6d0)
- [unicast_group](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md#abf15dec430b51c9c5e83ea4cb56b7845)
- [ext_adv](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md#a399a28aa6eb43f892ae0810c5e90d6e6)
- [pa_interval](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md#a0d8ccf04a751e775581c07e89b956b6c)
- [broadcast_id](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md#acb23afa394cd883b444ece27b1784adf)
- [broadcast_create_param](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md#a58442e418a8fb01d67560aa68bfbd2cc)
- [bt_cap_handover_cb](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md)
- [unicast_to_broadcast_created](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md#a46892bfd9ac055ae73634520b385fa51)
- [unicast_to_broadcast_complete](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md#abd00a0e3ebc35be604194de00986d6d2)
- [broadcast_to_unicast_complete](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md#a0506740ed704332c3f86648bfbdd5a24)
- [bt_cap_handover_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga5d8c66b3890e051b838d123a1911cfd6)
- [bt_cap_handover_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga808f0e5b671689196ba6f0fc1aea7427)
- [bt_cap_handover_unicast_to_broadcast](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaae56deae3792740bc3e8074882c87837)
- [bt_cap_handover_broadcast_to_unicast_param](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md)
- [bt_cap_commander_broadcast_reception_stop_param](../bluetooth_service_model_reference/P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md)
- [reception_stop_param](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#af0e79651b30c14a6bfd218203236e954)
- [broadcast_id](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#a39721b75c4cf2bd626427a63602d4aef)
- [adv_sid](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#aa43bd1c2e14ecb1c652a170893f7d1ab)
- [adv_type](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#a3f476e4ff18e4ca2b54fa495ec862718)
- [broadcast_source](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#a7cfe18cca6342c653e30de247d896c84)
- [unicast_group_param](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#ac133453b820f16472ee1537ee84b5205)
- [unicast_start_param](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#a1d94cd5237f209fd8617bc10dd953b18)
- [bt_cap_handover_broadcast_to_unicast](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92ff8b3133b8f5cb3d3029b5d556fe77)
- [bt_cap_handover_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gacd17de17ac1d96ff17ae15a63f43ad03)
- [bt_cap_commander_cb](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md)
- [discovery_complete](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#af989b3ebe7e5cc83a1ca4b2ef080e14d)
- [volume_changed](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#a3a7777603c23c14bc9d01cf29bc70ef7)
- [volume_mute_changed](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#acc9fcedf7f7abe86e055d48e6df124c7)
- [volume_offset_changed](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#a3bacfffef8d122db4574463777dfd507)
- [microphone_mute_changed](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#aa49e7eaf5c45d70c800f28b81f9967e5)
- [microphone_gain_changed](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#a1e83872924e1aa1293c499184ade9173)
- [broadcast_reception_start](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#a14f6a51db5a76aac015a5de617712af3)
- [broadcast_reception_stop](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#a2188c52e3daf0a695d7c42e6cac561cf)
- [distribute_broadcast_code](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#a7dfa1903f5cd71e67b6da0f5ff2fb299)
- [bt_cap_commander_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab6239c91b9d210872396860619fb8687)
- [bt_cap_commander_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga38928945e67835983de3fc639c8f2764)
- [bt_cap_commander_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga165c67bddcbe220050293a4c73fb6ede)
- [bt_cap_commander_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga7abf029533fed391930257605f3c752c)
- [bt_cap_commander_broadcast_reception_start_member_param](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md)
- [member](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#abf47aafab0b076da675182308d89bff7)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [addr](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#a93d6b4c76e730f282d24b2086c10aa3e)
- [adv_sid](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#acc52738756124db042ea884c82163362)
- [pa_interval](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#a1ba6b20f822f38dd4a0ce1f8b2f2671c)
- [broadcast_id](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#a8e6d5d1004d13069739229a7eec3abc0)
- [bt_bap_bass_subgroup](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md)
- [subgroups](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#a2222f8ae46afed4760db56079779532d)
- [BT_BAP_BASS_MAX_SUBGROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga443c212a736852305715452e7f165a9e)
- [num_subgroups](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#a184f2623ab759832a3ec9770b14c9c63)
- [bt_cap_commander_broadcast_reception_start_param](../bluetooth_service_model_reference/P019_bt_cap_commander_broadcast_reception_start_param_结构体.md)
- [type](../bluetooth_service_model_reference/P019_bt_cap_commander_broadcast_reception_start_param_结构体.md#ae4c1e6d7b345b8764f695ada56483aa1)
- [param](../bluetooth_service_model_reference/P019_bt_cap_commander_broadcast_reception_start_param_结构体.md#a8bac9170f48f34fd2239da9a6d994041)
- [count](../bluetooth_service_model_reference/P019_bt_cap_commander_broadcast_reception_start_param_结构体.md#ab0fe6fe27946a349ac33f11526ca13b7)
- [bt_cap_commander_broadcast_reception_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga25be83bb53c8e2ab76f311eaf4f615b9)
- [bt_cap_commander_broadcast_reception_stop_member_param](../bluetooth_service_model_reference/P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md)
- [member](../bluetooth_service_model_reference/P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md#aa934af2e197c129b1fcb1eea9359ea6d)
- [src_id](../bluetooth_service_model_reference/P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md#a72d606f6a83b1c84aa41d9db22cb955a)
- [num_subgroups](../bluetooth_service_model_reference/P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md#aeeab53e8bd7ae4f36433c0d4b60c313b)
- [type](../bluetooth_service_model_reference/P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md#a35bc972b00c10b90544da19c659fc460)
- [param](../bluetooth_service_model_reference/P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md#a36ce7cd132cd41a55872985433c2934d)
- [count](../bluetooth_service_model_reference/P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md#add81cdf1e3bad07b43602c8ce7c47593)
- [bt_cap_commander_broadcast_reception_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac5b2b6d617a092fb98b23c41b2f52d15)
- [bt_cap_commander_distribute_broadcast_code_member_param](../bluetooth_service_model_reference/P030_bt_cap_commander_distribute_broadcast_code_member_param_结构体.md)
- [member](../bluetooth_service_model_reference/P030_bt_cap_commander_distribute_broadcast_code_member_param_结构体.md#acd5d185c590ea9a64faebd354a3d5d4a)
- [src_id](../bluetooth_service_model_reference/P030_bt_cap_commander_distribute_broadcast_code_member_param_结构体.md#ad240bb7e1e9ad5c40eb1a031a6fbc2fe)
- [bt_cap_commander_distribute_broadcast_code_param](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md)
- [type](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md#a9605ad1590ff0279b46d639d38278933)
- [param](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md#a03be4b2fac7803de233c8a1024640cc2)
- [count](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md#a86316e3bf53edca67e0743072f0f2ee3)
- [broadcast_code](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md#ac7d426c975c1e2324f52486abf9298b9)
- [bt_cap_commander_distribute_broadcast_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaf86582ad529b6ee801d1154db7e33827)
- [bt_cap_commander_change_volume_param](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md)
- [type](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md#ad98625aa08f54759efd349921d104c88)
- [members](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md#a983656766a28118b018a70fef186f531)
- [count](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md#a37198e9118f80e5521f140b6aa1d2640)
- [volume](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md#ada17f89c8948246d68818f2e44d5ea49)
- [bt_cap_commander_change_volume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaff96953334eab1a38b30720b41c0d1a6)
- [bt_cap_commander_change_volume_offset_member_param](../bluetooth_service_model_reference/P027_bt_cap_commander_change_volume_offset_member_param_结构体.md)
- [member](../bluetooth_service_model_reference/P027_bt_cap_commander_change_volume_offset_member_param_结构体.md#a8e2e4f07be565ef1067d4955ebef50d4)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [offset](../bluetooth_service_model_reference/P027_bt_cap_commander_change_volume_offset_member_param_结构体.md#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8)
- [bt_cap_commander_change_volume_offset_param](../bluetooth_service_model_reference/P028_bt_cap_commander_change_volume_offset_param_结构体.md)
- [type](../bluetooth_service_model_reference/P028_bt_cap_commander_change_volume_offset_param_结构体.md#a8c22810a91d3109c3d633156bf16dffd)
- [param](../bluetooth_service_model_reference/P028_bt_cap_commander_change_volume_offset_param_结构体.md#a2610505f60d1a67ffef916dadefe841d)
- [count](../bluetooth_service_model_reference/P028_bt_cap_commander_change_volume_offset_param_结构体.md#ae3d416680196b0ee753a80d6fccb468b)
- [bt_cap_commander_change_volume_offset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae2cd451b387659b0a2021a9023d74dfa)
- [bt_cap_commander_change_volume_mute_state_param](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md)
- [type](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md#ae4b664c4b8da062a83dfcc32ebd28775)
- [members](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md#af54b6898bfcd42188cf45d65c72217d1)
- [count](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md#a784542a30164a62d44fcd3f801bc29f8)
- [mute](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md#ad4cc775dc74540a2b40126dba96776cd)
- [bt_cap_commander_change_volume_mute_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac5f94baa82fa6deade6f83346a56b5e4)
- [bt_cap_commander_change_microphone_mute_state_param](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md)
- [type](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md#a9cdb1eda2108fc341a6d7268fac689b0)
- [members](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md#a9c989fe2446ee2e055778c063a6b6de1)
- [count](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md#a96007101444d3cd61dda067fa072580e)
- [mute](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md#a1b6e22c9c41eb24b3961927b45c98af8)
- [bt_cap_commander_change_microphone_mute_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga19cc7ed5992a528a7795b76e7add6d54)
- [bt_cap_commander_change_microphone_gain_setting_member_param](../bluetooth_service_model_reference/P023_bt_cap_commander_change_microphone_gain_setting_member_param_结构体.md)
- [member](../bluetooth_service_model_reference/P023_bt_cap_commander_change_microphone_gain_setting_member_param_结构体.md#a5cc34236153e6a737f71cbc77f5f840e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [gain](../bluetooth_service_model_reference/P023_bt_cap_commander_change_microphone_gain_setting_member_param_结构体.md#a8fdcc5ec143b5a73c369d6e15d276196)
- [bt_cap_commander_change_microphone_gain_setting_param](../bluetooth_service_model_reference/P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md)
- [type](../bluetooth_service_model_reference/P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md#abac0f4da7b8b05067636539b2e9f9673)
- [param](../bluetooth_service_model_reference/P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md#ade5a93aee8bcff628228664c4a8428a8)
- [count](../bluetooth_service_model_reference/P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md#ae78e5d4761df00c8c8e2cfcb3e727349)
- [bt_cap_commander_change_microphone_gain_setting](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga958cd5925699624d23479ad2ace6b55b)
- [addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)
- [audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [csip.h](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h.html)
- [iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_cap_commander_broadcast_reception_start_member_param::num_subgroups](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#a184f2623ab759832a3ec9770b14c9c63)
- [bt_cap_commander_broadcast_reception_start_member_param::pa_interval](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#a1ba6b20f822f38dd4a0ce1f8b2f2671c)
- [bt_cap_commander_broadcast_reception_start_member_param::subgroups](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#a2222f8ae46afed4760db56079779532d)
- [bt_cap_commander_broadcast_reception_start_member_param::broadcast_id](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#a8e6d5d1004d13069739229a7eec3abc0)
- [bt_cap_commander_broadcast_reception_start_member_param::addr](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#a93d6b4c76e730f282d24b2086c10aa3e)
- [bt_cap_commander_broadcast_reception_start_member_param::member](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#abf47aafab0b076da675182308d89bff7)
- [bt_cap_commander_broadcast_reception_start_member_param::adv_sid](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md#acc52738756124db042ea884c82163362)
- [bt_cap_commander_broadcast_reception_start_param::param](../bluetooth_service_model_reference/P019_bt_cap_commander_broadcast_reception_start_param_结构体.md#a8bac9170f48f34fd2239da9a6d994041)
- [bt_cap_commander_broadcast_reception_start_param::count](../bluetooth_service_model_reference/P019_bt_cap_commander_broadcast_reception_start_param_结构体.md#ab0fe6fe27946a349ac33f11526ca13b7)
- [bt_cap_commander_broadcast_reception_start_param::type](../bluetooth_service_model_reference/P019_bt_cap_commander_broadcast_reception_start_param_结构体.md#ae4c1e6d7b345b8764f695ada56483aa1)
- [bt_cap_commander_broadcast_reception_stop_member_param::src_id](../bluetooth_service_model_reference/P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md#a72d606f6a83b1c84aa41d9db22cb955a)
- [bt_cap_commander_broadcast_reception_stop_member_param::member](../bluetooth_service_model_reference/P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md#aa934af2e197c129b1fcb1eea9359ea6d)
- [bt_cap_commander_broadcast_reception_stop_member_param::num_subgroups](../bluetooth_service_model_reference/P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md#aeeab53e8bd7ae4f36433c0d4b60c313b)
- [bt_cap_commander_broadcast_reception_stop_param::type](../bluetooth_service_model_reference/P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md#a35bc972b00c10b90544da19c659fc460)
- [bt_cap_commander_broadcast_reception_stop_param::param](../bluetooth_service_model_reference/P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md#a36ce7cd132cd41a55872985433c2934d)
- [bt_cap_commander_broadcast_reception_stop_param::count](../bluetooth_service_model_reference/P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md#add81cdf1e3bad07b43602c8ce7c47593)
- [bt_cap_commander_cb::broadcast_reception_start](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#a14f6a51db5a76aac015a5de617712af3)
- [bt_cap_commander_cb::microphone_gain_changed](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#a1e83872924e1aa1293c499184ade9173)
- [bt_cap_commander_cb::broadcast_reception_stop](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#a2188c52e3daf0a695d7c42e6cac561cf)
- [bt_cap_commander_cb::volume_changed](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#a3a7777603c23c14bc9d01cf29bc70ef7)
- [bt_cap_commander_cb::volume_offset_changed](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#a3bacfffef8d122db4574463777dfd507)
- [bt_cap_commander_cb::distribute_broadcast_code](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#a7dfa1903f5cd71e67b6da0f5ff2fb299)
- [bt_cap_commander_cb::microphone_mute_changed](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#aa49e7eaf5c45d70c800f28b81f9967e5)
- [bt_cap_commander_cb::volume_mute_changed](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#acc9fcedf7f7abe86e055d48e6df124c7)
- [bt_cap_commander_cb::discovery_complete](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md#af989b3ebe7e5cc83a1ca4b2ef080e14d)
- [bt_cap_commander_change_microphone_gain_setting_member_param::member](../bluetooth_service_model_reference/P023_bt_cap_commander_change_microphone_gain_setting_member_param_结构体.md#a5cc34236153e6a737f71cbc77f5f840e)
- [bt_cap_commander_change_microphone_gain_setting_member_param::gain](../bluetooth_service_model_reference/P023_bt_cap_commander_change_microphone_gain_setting_member_param_结构体.md#a8fdcc5ec143b5a73c369d6e15d276196)
- [bt_cap_commander_change_microphone_gain_setting_param::type](../bluetooth_service_model_reference/P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md#abac0f4da7b8b05067636539b2e9f9673)
- [bt_cap_commander_change_microphone_gain_setting_param::param](../bluetooth_service_model_reference/P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md#ade5a93aee8bcff628228664c4a8428a8)
- [bt_cap_commander_change_microphone_gain_setting_param::count](../bluetooth_service_model_reference/P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md#ae78e5d4761df00c8c8e2cfcb3e727349)
- [bt_cap_commander_change_microphone_mute_state_param::mute](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md#a1b6e22c9c41eb24b3961927b45c98af8)
- [bt_cap_commander_change_microphone_mute_state_param::count](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md#a96007101444d3cd61dda067fa072580e)
- [bt_cap_commander_change_microphone_mute_state_param::members](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md#a9c989fe2446ee2e055778c063a6b6de1)
- [bt_cap_commander_change_microphone_mute_state_param::type](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md#a9cdb1eda2108fc341a6d7268fac689b0)
- [bt_cap_commander_change_volume_mute_state_param::count](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md#a784542a30164a62d44fcd3f801bc29f8)
- [bt_cap_commander_change_volume_mute_state_param::mute](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md#ad4cc775dc74540a2b40126dba96776cd)
- [bt_cap_commander_change_volume_mute_state_param::type](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md#ae4b664c4b8da062a83dfcc32ebd28775)
- [bt_cap_commander_change_volume_mute_state_param::members](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md#af54b6898bfcd42188cf45d65c72217d1)
- [bt_cap_commander_change_volume_offset_member_param::offset](../bluetooth_service_model_reference/P027_bt_cap_commander_change_volume_offset_member_param_结构体.md#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8)
- [bt_cap_commander_change_volume_offset_member_param::member](../bluetooth_service_model_reference/P027_bt_cap_commander_change_volume_offset_member_param_结构体.md#a8e2e4f07be565ef1067d4955ebef50d4)
- [bt_cap_commander_change_volume_offset_param::param](../bluetooth_service_model_reference/P028_bt_cap_commander_change_volume_offset_param_结构体.md#a2610505f60d1a67ffef916dadefe841d)
- [bt_cap_commander_change_volume_offset_param::type](../bluetooth_service_model_reference/P028_bt_cap_commander_change_volume_offset_param_结构体.md#a8c22810a91d3109c3d633156bf16dffd)
- [bt_cap_commander_change_volume_offset_param::count](../bluetooth_service_model_reference/P028_bt_cap_commander_change_volume_offset_param_结构体.md#ae3d416680196b0ee753a80d6fccb468b)
- [bt_cap_commander_change_volume_param::count](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md#a37198e9118f80e5521f140b6aa1d2640)
- [bt_cap_commander_change_volume_param::members](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md#a983656766a28118b018a70fef186f531)
- [bt_cap_commander_change_volume_param::type](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md#ad98625aa08f54759efd349921d104c88)
- [bt_cap_commander_change_volume_param::volume](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md#ada17f89c8948246d68818f2e44d5ea49)
- [bt_cap_commander_distribute_broadcast_code_member_param::member](../bluetooth_service_model_reference/P030_bt_cap_commander_distribute_broadcast_code_member_param_结构体.md#acd5d185c590ea9a64faebd354a3d5d4a)
- [bt_cap_commander_distribute_broadcast_code_member_param::src_id](../bluetooth_service_model_reference/P030_bt_cap_commander_distribute_broadcast_code_member_param_结构体.md#ad240bb7e1e9ad5c40eb1a031a6fbc2fe)
- [bt_cap_commander_distribute_broadcast_code_param::param](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md#a03be4b2fac7803de233c8a1024640cc2)
- [bt_cap_commander_distribute_broadcast_code_param::count](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md#a86316e3bf53edca67e0743072f0f2ee3)
- [bt_cap_commander_distribute_broadcast_code_param::type](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md#a9605ad1590ff0279b46d639d38278933)
- [bt_cap_commander_distribute_broadcast_code_param::broadcast_code](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md#ac7d426c975c1e2324f52486abf9298b9)
- [bt_cap_handover_broadcast_to_unicast_param::unicast_start_param](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#a1d94cd5237f209fd8617bc10dd953b18)
- [bt_cap_handover_broadcast_to_unicast_param::broadcast_id](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#a39721b75c4cf2bd626427a63602d4aef)
- [bt_cap_handover_broadcast_to_unicast_param::adv_type](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#a3f476e4ff18e4ca2b54fa495ec862718)
- [bt_cap_handover_broadcast_to_unicast_param::broadcast_source](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#a7cfe18cca6342c653e30de247d896c84)
- [bt_cap_handover_broadcast_to_unicast_param::adv_sid](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#aa43bd1c2e14ecb1c652a170893f7d1ab)
- [bt_cap_handover_broadcast_to_unicast_param::unicast_group_param](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#ac133453b820f16472ee1537ee84b5205)
- [bt_cap_handover_broadcast_to_unicast_param::reception_stop_param](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md#af0e79651b30c14a6bfd218203236e954)
- [bt_cap_handover_cb::broadcast_to_unicast_complete](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md#a0506740ed704332c3f86648bfbdd5a24)
- [bt_cap_handover_cb::unicast_to_broadcast_created](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md#a46892bfd9ac055ae73634520b385fa51)
- [bt_cap_handover_cb::unicast_to_broadcast_complete](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md#abd00a0e3ebc35be604194de00986d6d2)
- [bt_cap_handover_unicast_to_broadcast_param::type](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md#a079b91898031113b6126465307bed6d0)
- [bt_cap_handover_unicast_to_broadcast_param::pa_interval](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md#a0d8ccf04a751e775581c07e89b956b6c)
- [bt_cap_handover_unicast_to_broadcast_param::ext_adv](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md#a399a28aa6eb43f892ae0810c5e90d6e6)
- [bt_cap_handover_unicast_to_broadcast_param::broadcast_create_param](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md#a58442e418a8fb01d67560aa68bfbd2cc)
- [bt_cap_handover_unicast_to_broadcast_param::unicast_group](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md#abf15dec430b51c9c5e83ea4cb56b7845)
- [bt_cap_handover_unicast_to_broadcast_param::broadcast_id](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md#acb23afa394cd883b444ece27b1784adf)
- [bt_cap_initiator_broadcast_create_param::pto](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#a01d6ffb369caaf808d4b55b3b1748890)
- [bt_cap_initiator_broadcast_create_param::subgroup_params](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#a2eafc157450237cf311d6144e7431839)
- [bt_cap_initiator_broadcast_create_param::encryption](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#a4432bee0e365c189996b9f70c7226542)
- [bt_cap_initiator_broadcast_create_param::irc](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#a6f562b7a696472b7784ca2e1ced4997a)
- [bt_cap_initiator_broadcast_create_param::iso_interval](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#a8eedd8f9a896931f75642576ca37c7d5)
- [bt_cap_initiator_broadcast_create_param::broadcast_code](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#aa4d6fbd5bd13963004e381b987bbeb4d)
- [bt_cap_initiator_broadcast_create_param::qos](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#aaa6f2828416b0624b8ca15fb2139413f)
- [bt_cap_initiator_broadcast_create_param::packing](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#ae81ee3dada58a3354c70401380916cbc)
- [bt_cap_initiator_broadcast_create_param::subgroup_count](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md#aee3e0244b59503311bc445f36977a85b)
- [bt_cap_initiator_broadcast_stream_param::data](../bluetooth_service_model_reference/P036_bt_cap_initiator_broadcast_stream_param_结构体.md#a72720e8423dbeb0341041cc24a9e0869)
- [bt_cap_initiator_broadcast_stream_param::stream](../bluetooth_service_model_reference/P036_bt_cap_initiator_broadcast_stream_param_结构体.md#a7e5ddb85024b58d6ecbb6d7f70ef5c6a)
- [bt_cap_initiator_broadcast_stream_param::data_len](../bluetooth_service_model_reference/P036_bt_cap_initiator_broadcast_stream_param_结构体.md#aa4677e278d6d4823551ccfd9c27c68a4)
- [bt_cap_initiator_broadcast_subgroup_param::codec_cfg](../bluetooth_service_model_reference/P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md#a252140d260f47404302a721a928f4765)
- [bt_cap_initiator_broadcast_subgroup_param::stream_params](../bluetooth_service_model_reference/P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md#a32e99898ee97a56105497c3ae480692a)
- [bt_cap_initiator_broadcast_subgroup_param::stream_count](../bluetooth_service_model_reference/P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md#a577a27836a02c7a6219182f1cb0bd769)
- [bt_cap_initiator_cb::unicast_start_enabled](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a06b2f73a6f6f8f3f88cd4c5bd87f4fbc)
- [bt_cap_initiator_cb::unicast_stop_complete](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a2e910a82209d144878b6c69c1b2723ba)
- [bt_cap_initiator_cb::unicast_start_qos_configured](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a5ef6349113a1c786a0441b6c494286d1)
- [bt_cap_initiator_cb::unicast_discovery_complete](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a642a2f48e8f870bb1681ba58aa119de9)
- [bt_cap_initiator_cb::unicast_start_codec_configured](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a64c9b0fb0bdfcc7434d8f2854a20a666)
- [bt_cap_initiator_cb::unicast_start_started](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a65d8dd89661f92b2e71e90b69a8b4320)
- [bt_cap_initiator_cb::unicast_stop_disabled](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a8001c24d64df0881dbfd78382c2a2db7)
- [bt_cap_initiator_cb::unicast_start_connected](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a8452b3c6775d1608272893719dd3887d)
- [bt_cap_initiator_cb::broadcast_stopped](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a85451f4cbf0c8e4d061a2b50b892529d)
- [bt_cap_initiator_cb::unicast_stop_stopped](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a8c20d933b9ee1c1412d7ad719ff24683)
- [bt_cap_initiator_cb::unicast_stop_released](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a8f659ac17a242eab12c404f59e42d149)
- [bt_cap_initiator_cb::unicast_update_complete](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#a95266741841fca83cd2769c76652154e)
- [bt_cap_initiator_cb::unicast_start_complete](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#aa70de1dda73ffdcbb8287f8f174984ea)
- [bt_cap_initiator_cb::broadcast_started](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md#afd9b20a78b9115409d4301c8d71c4405)
- [bt_cap_stream::ops](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md#aa58c47ace3f844533ab545906ede52ba)
- [bt_cap_stream::bap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md#ad9d974d18ec42079b81107485b43bc18)
- [bt_cap_unicast_audio_start_param::type](../bluetooth_service_model_reference/P040_bt_cap_unicast_audio_start_param_结构体.md#a7d0055719cee1cb1b0a7c1b6dc88bda5)
- [bt_cap_unicast_audio_start_param::count](../bluetooth_service_model_reference/P040_bt_cap_unicast_audio_start_param_结构体.md#acacd3692c807c536882dccaea074f667)
- [bt_cap_unicast_audio_start_param::stream_params](../bluetooth_service_model_reference/P040_bt_cap_unicast_audio_start_param_结构体.md#af3e7a147448a19d2fb1ef802c525636b)
- [bt_cap_unicast_audio_start_stream_param::stream](../bluetooth_service_model_reference/P041_bt_cap_unicast_audio_start_stream_param_结构体.md#a109acdedd1249ea8342f06de28989d4e)
- [bt_cap_unicast_audio_start_stream_param::member](../bluetooth_service_model_reference/P041_bt_cap_unicast_audio_start_stream_param_结构体.md#a9613a24e05a362a2f70d8e433ca6b42b)
- [bt_cap_unicast_audio_start_stream_param::ep](../bluetooth_service_model_reference/P041_bt_cap_unicast_audio_start_stream_param_结构体.md#aa9a13263d287a2ddb241a8dc13baeffb)
- [bt_cap_unicast_audio_start_stream_param::codec_cfg](../bluetooth_service_model_reference/P041_bt_cap_unicast_audio_start_stream_param_结构体.md#abbc53d6bfad43e1b211bb8003b7eea88)
- [bt_cap_unicast_audio_stop_param::count](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md#a11b5ac19301ce8ebd2c35df45c60bfe2)
- [bt_cap_unicast_audio_stop_param::release](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md#a1cbd7ee2e4ceafd2da2858dc7c941d78)
- [bt_cap_unicast_audio_stop_param::type](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md#a773eedda9ae8969e8749d56ffa3d1afa)
- [bt_cap_unicast_audio_stop_param::streams](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md#a94707060a6ef15dd8d3e48eae526aa82)
- [bt_cap_unicast_audio_update_param::stream_params](../bluetooth_service_model_reference/P043_bt_cap_unicast_audio_update_param_结构体.md#a3d8f940d8401b8524764e7ecab3cfacb)
- [bt_cap_unicast_audio_update_param::type](../bluetooth_service_model_reference/P043_bt_cap_unicast_audio_update_param_结构体.md#a768029ce89b74e0bcc06bb50f1fd8dcd)
- [bt_cap_unicast_audio_update_param::count](../bluetooth_service_model_reference/P043_bt_cap_unicast_audio_update_param_结构体.md#ac8982f313161380af536d41ec48dcba1)
- [bt_cap_unicast_audio_update_stream_param::meta_len](../bluetooth_service_model_reference/P044_bt_cap_unicast_audio_update_stream_param_结构体.md#a07c1ab3158377ce51d94084ad7dc3e9c)
- [bt_cap_unicast_audio_update_stream_param::stream](../bluetooth_service_model_reference/P044_bt_cap_unicast_audio_update_stream_param_结构体.md#a7a2042834b79ca37e3b3df9fc2f8a7a1)
- [bt_cap_unicast_audio_update_stream_param::meta](../bluetooth_service_model_reference/P044_bt_cap_unicast_audio_update_stream_param_结构体.md#a87833f9e91b47513a27db0aa7692d8c0)
- [bt_cap_unicast_group_info::unicast_group](../bluetooth_service_model_reference/P046_bt_cap_unicast_group_info_结构体.md#afbfd6705742d15081f6cf4dca21e242b)
- [bt_cap_unicast_group_param::params](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md#a64ca2c5cc4f34821e567841ec8efe67b)
- [bt_cap_unicast_group_param::packing](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md#a97e67b903e72dd1f0fef4961810288b1)
- [bt_cap_unicast_group_param::p_to_c_ft](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md#ab424be389b026ac5857e3bec1c3d686f)
- [bt_cap_unicast_group_param::params_count](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md#ab9748e9e230048af64ce9c9ce1006952)
- [bt_cap_unicast_group_param::iso_interval](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md#ac52a0e09e3978a084e4fe558e4a5a848)
- [bt_cap_unicast_group_param::c_to_p_ft](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md#adb6cb5686b3d827156aef325b3dcdc84)
- [bt_cap_unicast_group_stream_pair_param::rx_param](../bluetooth_service_model_reference/P048_bt_cap_unicast_group_stream_pair_param_结构体.md#a19d49ab8c0daa7e6a4c73563952ae461)
- [bt_cap_unicast_group_stream_pair_param::tx_param](../bluetooth_service_model_reference/P048_bt_cap_unicast_group_stream_pair_param_结构体.md#a6edeca159371f3a70cc5a1f662a0e45c)
- [bt_cap_unicast_group_stream_param::qos_cfg](../bluetooth_service_model_reference/P049_bt_cap_unicast_group_stream_param_结构体.md#a02672d241f243a7530eeff191e9a034b)
- [bt_cap_unicast_group_stream_param::stream](../bluetooth_service_model_reference/P049_bt_cap_unicast_group_stream_param_结构体.md#a16aacd43bb7b449648ab6a5a89999fba)
- [bt_cap_set_member::member](../bluetooth_service_model_reference/P188_bt_cap_set_member_联合体.md#a692a1be2fbd79c4b6a0fbce564ff2973)
- [bt_cap_set_member::csip](../bluetooth_service_model_reference/P188_bt_cap_set_member_联合体.md#ac17db41d21a92d8d128b70962e4eb2d6)

---

[上一章](P068_blob.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P070_hid.h_源码浏览.md)
