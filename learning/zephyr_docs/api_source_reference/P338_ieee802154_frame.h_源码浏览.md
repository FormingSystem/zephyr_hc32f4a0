---
id: learning.zephyr-docs.api-source-reference.page-338
title: ieee802154_frame.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第338章\_ieee802154\_frame.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html)。

## 338.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="foldopen00177"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="foldopen00263"></a>
<a id="l00263"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="foldopen00282"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="foldopen00292"></a>
<a id="l00292"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="foldopen00305"></a>
<a id="l00305"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="foldopen00324"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="foldopen00380"></a>
<a id="l00380"></a>
<a id="l00382"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="foldopen00424"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00427"></a>
<a id="l00429"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00434"></a>
<a id="l00436"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="foldopen00457"></a>
<a id="l00457"></a>
<a id="l00463"></a>
<a id="l00465"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00471"></a>
<a id="l00473"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00479"></a>
<a id="l00481"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="foldopen00493"></a>
<a id="l00493"></a>
<a id="l00495"></a>
<a id="l00497"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="foldopen00515"></a>
<a id="l00515"></a>
<a id="l00517"></a>
<a id="l00519"></a>
<a id="l00521"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="foldopen00531"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00534"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00539"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="foldopen00550"></a>
<a id="l00550"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00555"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00560"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="foldopen00571"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00574"></a>
<a id="l00576"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00581"></a>
<a id="l00583"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="foldopen00594"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00597"></a>
<a id="l00599"></a>
<a id="l00601"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00606"></a>
<a id="l00608"></a>
<a id="l00610"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="foldopen00621"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00624"></a>
<a id="l00626"></a>
<a id="l00628"></a>
<a id="l00630"></a>
<a id="l00632"></a>
<a id="l00634"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00639"></a>
<a id="l00641"></a>
<a id="l00643"></a>
<a id="l00645"></a>
<a id="l00647"></a>
<a id="l00649"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="foldopen00661"></a>
<a id="l00661"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="foldopen00674"></a>
<a id="l00674"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00679"></a>
<a id="l00681"></a>
<a id="l00683"></a>
<a id="l00685"></a>
<a id="l00687"></a>
<a id="l00689"></a>
<a id="l00691"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00696"></a>
<a id="l00698"></a>
<a id="l00700"></a>
<a id="l00702"></a>
<a id="l00704"></a>
<a id="l00706"></a>
<a id="l00708"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="foldopen00727"></a>
<a id="l00727"></a>
<a id="l00729"></a>
<a id="l00731"></a>
<a id="l00733"></a>
<a id="l00735"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="foldopen00745"></a>
<a id="l00745"></a>
<a id="l00747"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="foldopen00764"></a>
<a id="l00764"></a>
<a id="l00766"></a>
<a id="l00768"></a>
<a id="l00770"></a>
<a id="l00772"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="foldopen00782"></a>
<a id="l00782"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="foldopen00799"></a>
<a id="l00799"></a>
<a id="l00801"></a>
<a id="l00803"></a>
<a id="l00805"></a>
<a id="l00807"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="foldopen00824"></a>
<a id="l00824"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00829"></a>
<a id="l00831"></a>
<a id="l00833"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00838"></a>
<a id="l00840"></a>
<a id="l00842"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00846"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00854"></a>
<a id="l00855"></a>
<a id="foldopen00861"></a>
<a id="l00861"></a>
<a id="l00863"></a>
<a id="l00865"></a>
<a id="l00867"></a>
<a id="l00869"></a>
<a id="l00871"></a>
<a id="l00873"></a>
<a id="l00875"></a>
<a id="l00877"></a>
<a id="l00879"></a>
<a id="l00881"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="foldopen00893"></a>
<a id="l00893"></a>
<a id="l00895"></a>
<a id="l00901"></a>
<a id="l00903"></a>
<a id="l00905"></a>
<a id="l00907"></a>
<a id="l00909"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="foldopen00927"></a>
<a id="l00927"></a>
<a id="l00929"></a>
<a id="l00935"></a>
<a id="l00937"></a>
<a id="l00939"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="foldopen00953"></a>
<a id="l00953"></a>
<a id="l00955"></a>
<a id="l00961"></a>
<a id="l00963"></a>
<a id="l00965"></a>
<a id="l00966"></a>
<a id="l00967"></a>
<a id="l00969"></a>
<a id="l00971"></a>
<a id="l00972"></a>
<a id="l00973"></a>
<a id="l00975"></a>
<a id="l00977"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="l00984"></a>
<a id="l00985"></a>
<a id="l00986"></a>
<a id="l00987"></a>
<a id="l00988"></a>
<a id="l00989"></a>
<a id="l01002"></a>
<a id="l01003"></a>
<a id="l01004"></a>
<a id="l01005"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="l01009"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01012"></a>
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
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="l01032"></a>
<a id="l01034"></a>
<a id="l01035"></a>
<a id="agroup__ieee802154__l2_html_ga355350794ec26788bc855da53d311bea"></a>
<a id="aieee802154_8h_html"></a>
<a id="aieee802154__frame_8h_html_a16702b800d3e4a51df6cb6f909ff79fd"></a>
<a id="aieee802154__frame_8h_html_a16702b800d3e4a51df6cb6f909ff79fda59490f8a40d1c65c365b3370ccabd3d8"></a>
<a id="aieee802154__frame_8h_html_a16702b800d3e4a51df6cb6f909ff79fda6253c6948e0ecbc79878bd1fd73473ec"></a>
<a id="aieee802154__frame_8h_html_a16702b800d3e4a51df6cb6f909ff79fda69235bb8211a5a4a3c4fde6379d28644"></a>
<a id="aieee802154__frame_8h_html_a16702b800d3e4a51df6cb6f909ff79fda953e79789829eb3e220bccb94f21316f"></a>
<a id="aieee802154__frame_8h_html_a16702b800d3e4a51df6cb6f909ff79fdaaabec4197346f0d36903217c1f68b90f"></a>
<a id="aieee802154__frame_8h_html_a16702b800d3e4a51df6cb6f909ff79fdacb7f98a3d76846d411bc698572a5eeb5"></a>
<a id="aieee802154__frame_8h_html_a16702b800d3e4a51df6cb6f909ff79fdacd5ec548c6199b61912ed8a15df3b486"></a>
<a id="aieee802154__frame_8h_html_a16702b800d3e4a51df6cb6f909ff79fdaf14e1c3c75c77dcfaf54d2d637b9b4ae"></a>
<a id="aieee802154__frame_8h_html_a2ab06c343e03a4d6e28073780eb47648"></a>
<a id="aieee802154__frame_8h_html_a2ab06c343e03a4d6e28073780eb47648a2d69c0e06015471da07bce9314a900c7"></a>
<a id="aieee802154__frame_8h_html_a2ab06c343e03a4d6e28073780eb47648a3feadbd533ba9b31977e2fa7537fa8c1"></a>
<a id="aieee802154__frame_8h_html_a2ab06c343e03a4d6e28073780eb47648a8b04f0bae8a62282a8a7821a4db949cb"></a>
<a id="aieee802154__frame_8h_html_a2ab06c343e03a4d6e28073780eb47648ae09de01a9f7b2a7eba0ee0173765e1ef"></a>
<a id="aieee802154__frame_8h_html_a2ab06c343e03a4d6e28073780eb47648aec815962bcc4fe41d8a2223bc7b7e3c7"></a>
<a id="aieee802154__frame_8h_html_a49f3241733da0a6dd0003d7bcaf55965"></a>
<a id="aieee802154__frame_8h_html_a49f3241733da0a6dd0003d7bcaf55965a27c38f60597d1b202cbb0e6c8cad27fd"></a>
<a id="aieee802154__frame_8h_html_a49f3241733da0a6dd0003d7bcaf55965a50e45c02f42ef667e1216cfc1024860f"></a>
<a id="aieee802154__frame_8h_html_a49f3241733da0a6dd0003d7bcaf55965a6f5f3599146d548b541dd22fa1f6322c"></a>
<a id="aieee802154__frame_8h_html_a49f3241733da0a6dd0003d7bcaf55965aa51f0be0ff88addcd167b03051e2dc21"></a>
<a id="aieee802154__frame_8h_html_a7efde78911de6991098ba5d837157199"></a>
<a id="aieee802154__frame_8h_html_a7efde78911de6991098ba5d837157199a0a15cf36690a5224f8239f24687ca09f"></a>
<a id="aieee802154__frame_8h_html_a7efde78911de6991098ba5d837157199a0ee7d320f5923af196869ac9c348ec34"></a>
<a id="aieee802154__frame_8h_html_a7efde78911de6991098ba5d837157199a234e0cdb8bebaa8e9da8da2052babd71"></a>
<a id="aieee802154__frame_8h_html_a7efde78911de6991098ba5d837157199a2541a973cde011d980fe2565803a30f4"></a>
<a id="aieee802154__frame_8h_html_a7efde78911de6991098ba5d837157199a256265e47b2e4cdc50596153ee2a9018"></a>
<a id="aieee802154__frame_8h_html_a7efde78911de6991098ba5d837157199a446febb8ad088218de365cd86d406c94"></a>
<a id="aieee802154__frame_8h_html_a7efde78911de6991098ba5d837157199a867cc7c5b4c9e1b99dda26bfc1713d87"></a>
<a id="aieee802154__frame_8h_html_a7efde78911de6991098ba5d837157199a89935d04845589a5a8d4c4d6abeb4ef5"></a>
<a id="aieee802154__frame_8h_html_a7efde78911de6991098ba5d837157199a8d85bf1bc19b90562b854db227c74211"></a>
<a id="aieee802154__frame_8h_html_a7efde78911de6991098ba5d837157199a9371a4aeeab31f2f0eb52a188d8a2990"></a>
<a id="aieee802154__frame_8h_html_a7efde78911de6991098ba5d837157199a9ebdc4dfb6ca44098e9bdc2635dc7b18"></a>
<a id="aieee802154__frame_8h_html_aa2c9cb8ba5b7c397c695a9a591649b91"></a>
<a id="aieee802154__frame_8h_html_aa2c9cb8ba5b7c397c695a9a591649b91a15eb8c84a04a1642e7395a872eb5db59"></a>
<a id="aieee802154__frame_8h_html_aa2c9cb8ba5b7c397c695a9a591649b91a1cedbaa8a44fdb79041e6b5ad8af6031"></a>
<a id="aieee802154__frame_8h_html_aa2c9cb8ba5b7c397c695a9a591649b91a280571e677e992f5220f56818e52ccf4"></a>
<a id="aieee802154__frame_8h_html_aa2c9cb8ba5b7c397c695a9a591649b91a3a72c63164f925e7fe6d12d9cf572d81"></a>
<a id="aieee802154__frame_8h_html_aa2c9cb8ba5b7c397c695a9a591649b91a571c5b2f63cedf01857ce31ba1125517"></a>
<a id="aieee802154__frame_8h_html_aa6a4b34e9722f5ccd06b65cf64efe053"></a>
<a id="aieee802154__frame_8h_html_aa6a4b34e9722f5ccd06b65cf64efe053a3b2b709ecd3a2a1a4b997baf26c40bbc"></a>
<a id="aieee802154__frame_8h_html_aa6a4b34e9722f5ccd06b65cf64efe053a8112ae7940d211afe7a5a1a79071ad57"></a>
<a id="aieee802154__frame_8h_html_aa6a4b34e9722f5ccd06b65cf64efe053aa2a088916733a4de4d009caaea734ca2"></a>
<a id="aieee802154__frame_8h_html_aa6a4b34e9722f5ccd06b65cf64efe053aad3af323ce4f598be0256ec9c19dcf36"></a>
<a id="aieee802154__frame_8h_html_aaf5ffabf140bf36c9076662e4b46e4a2"></a>
<a id="aieee802154__frame_8h_html_aaf5ffabf140bf36c9076662e4b46e4a2a2155c782cf4074f240bcb087aecc8f06"></a>
<a id="aieee802154__frame_8h_html_aaf5ffabf140bf36c9076662e4b46e4a2a2b8b7e0d195c7fb33e3578b86bda99d7"></a>
<a id="aieee802154__frame_8h_html_aaf5ffabf140bf36c9076662e4b46e4a2a60e7720ffc14a08b0f4c90b567ce57bd"></a>
<a id="aieee802154__frame_8h_html_aaf5ffabf140bf36c9076662e4b46e4a2a649d558004918cacb4c9ec32d247c934"></a>
<a id="aieee802154__frame_8h_html_aaf5ffabf140bf36c9076662e4b46e4a2a95e1e7954023a5cd3c35aaf6596b0821"></a>
<a id="aieee802154__frame_8h_html_aaf5ffabf140bf36c9076662e4b46e4a2abaa5076f0f373c3f2e415a8f28a6e0ee"></a>
<a id="aieee802154__frame_8h_html_aaf5ffabf140bf36c9076662e4b46e4a2abe9a01bb053e5809e0f110cb0709d001"></a>
<a id="aieee802154__frame_8h_html_aaf5ffabf140bf36c9076662e4b46e4a2af5bff347e35ac0af5c86b65ef231df47"></a>
<a id="aieee802154__frame_8h_html_ac5819ed25fa7b56756e8e7962f579ec7"></a>
<a id="aieee802154__frame_8h_html_ac5819ed25fa7b56756e8e7962f579ec7a0c363713ca56c27961d5198a5ee7078f"></a>
<a id="aieee802154__frame_8h_html_ac5819ed25fa7b56756e8e7962f579ec7a2519ea53b9adf534707e7ce4401966f6"></a>
<a id="aieee802154__frame_8h_html_ac5819ed25fa7b56756e8e7962f579ec7a918058e16c48ecee20a8ce3968138c04"></a>
<a id="aieee802154__frame_8h_html_ac5819ed25fa7b56756e8e7962f579ec7ae351b9dc1ba1e546a706c861b4dfd841"></a>
<a id="akernel_8h_html"></a>
<a id="anet__pkt_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructieee802154__address__field__comp_html"></a>
<a id="astructieee802154__address__field__comp_html_a3c7f8e5bb1f015e02123669726fbcf6c"></a>
<a id="astructieee802154__address__field__plain_html"></a>
<a id="astructieee802154__address__field__plain_html_a8237aa26d9e3d564c349f90c8841cee7"></a>
<a id="astructieee802154__address__field__plain_html_aff9f5b6d0392c0ba401cb90d63631214"></a>
<a id="astructieee802154__address__field_html"></a>
<a id="astructieee802154__address__field_html_ae06d1451a3006bfe10abc6148ce8ebce"></a>
<a id="astructieee802154__address__field_html_af3df38a8424bfe75cd8ad9694b31074f"></a>
<a id="astructieee802154__address_html"></a>
<a id="astructieee802154__address_html_a3fecbe4e7ad6a32d57af1fbdaca5c881"></a>
<a id="astructieee802154__address_html_ac954ef5b107997dbb953a0efae865ab1"></a>
<a id="astructieee802154__aux__security__hdr_html"></a>
<a id="astructieee802154__aux__security__hdr_html_a4c9113e6ce77856e09822866c281d5eb"></a>
<a id="astructieee802154__aux__security__hdr_html_a75a365c8c642f17aedc5c08754272c79"></a>
<a id="astructieee802154__aux__security__hdr_html_a7c7facc1f1b9fa5fedd94e9a6afe2f0b"></a>
<a id="astructieee802154__beacon__sf_html"></a>
<a id="astructieee802154__beacon__sf_html_a33a47bde19ad49508c981b1e7940ad93"></a>
<a id="astructieee802154__beacon__sf_html_a4a6f895c5d3a86853647516d12073c32"></a>
<a id="astructieee802154__beacon__sf_html_a7f62606165bb7d2bd96cf0923de1326e"></a>
<a id="astructieee802154__beacon__sf_html_aa3f402e1ac43b609a366f0a7c87195bd"></a>
<a id="astructieee802154__beacon__sf_html_aa52c67ce1c7607dfeabbfe5706a75bb8"></a>
<a id="astructieee802154__beacon__sf_html_ac1e5e4c10de0ef0bb22ff12a5097aed9"></a>
<a id="astructieee802154__beacon__sf_html_af57a9ae07bb6adb029be235929ed903b"></a>
<a id="astructieee802154__beacon_html"></a>
<a id="astructieee802154__beacon_html_a1afd2b6d448a3c1dd4dfd471068f55ed"></a>
<a id="astructieee802154__beacon_html_a959331440b0fcdb24b4b624b607cdf3e"></a>
<a id="astructieee802154__cmd__assoc__req_html"></a>
<a id="astructieee802154__cmd__assoc__req_html_a035bc9f5639f91ca39ac0142279d7ccd"></a>
<a id="astructieee802154__cmd__assoc__req_html_a19039e164a4804a8f8d901206b0bd19c"></a>
<a id="astructieee802154__cmd__assoc__req_html_a22321a62b2049202c6eb84a25316bb9c"></a>
<a id="astructieee802154__cmd__assoc__req_html_a306becbe9dc40df9f897c222e0d9f222"></a>
<a id="astructieee802154__cmd__assoc__req_html_a43e69b46fe01aa8278e78abd341ff01e"></a>
<a id="astructieee802154__cmd__assoc__req_html_a75f60ccf3390f5371e8af6c9c2234bf5"></a>
<a id="astructieee802154__cmd__assoc__req_html_a99a5743d96b9ebc5153edcfb326eb38a"></a>
<a id="astructieee802154__cmd__assoc__req_html_adc81f209a8f17a90b50fb57f2990d5b8"></a>
<a id="astructieee802154__cmd__assoc__req_html_aea1e48101ca4ee67972e66b566e56259"></a>
<a id="astructieee802154__cmd__assoc__res_html"></a>
<a id="astructieee802154__cmd__assoc__res_html_a0aec016dd92112254d9d162734a9f2d6"></a>
<a id="astructieee802154__cmd__assoc__res_html_a372c5c7bee963eb890ccddcab9526fc4"></a>
<a id="astructieee802154__cmd__coord__realign_html"></a>
<a id="astructieee802154__cmd__coord__realign_html_a0602708c2dc512c12f2901d84d090f30"></a>
<a id="astructieee802154__cmd__coord__realign_html_a07775fefaf0f87425beb6371bd112b26"></a>
<a id="astructieee802154__cmd__coord__realign_html_a6f91305584cf44c910a95cf93e73c84d"></a>
<a id="astructieee802154__cmd__coord__realign_html_a9823ca16d8b99bb17583f402050aa80c"></a>
<a id="astructieee802154__cmd__coord__realign_html_ae8867213cecfe3342dd951b1e03bde2d"></a>
<a id="astructieee802154__cmd__disassoc__note_html"></a>
<a id="astructieee802154__cmd__disassoc__note_html_a2353dfa2ad8eb0efa8794cb09a65ea44"></a>
<a id="astructieee802154__command_html"></a>
<a id="astructieee802154__command_html_a1bc60b61ef82a58d080b07c1a0b27626"></a>
<a id="astructieee802154__command_html_a61700791f0e2148e23836340cbf9d0b8"></a>
<a id="astructieee802154__command_html_a6ad0a1fa2c4985b10e35ac282d27e3d1"></a>
<a id="astructieee802154__command_html_aa21a32878e544c284f6efb7c78ed079a"></a>
<a id="astructieee802154__command_html_addbd05e3e770199f71ecf20dd0b716a9"></a>
<a id="astructieee802154__command_html_ae5b9b8f7dc12ac73d2b392052a60b48d"></a>
<a id="astructieee802154__context_html"></a>
<a id="astructieee802154__fcf__seq_html"></a>
<a id="astructieee802154__fcf__seq_html_a3ad3dbf5ba7cd8b32b7ae5804c692f24"></a>
<a id="astructieee802154__fcf__seq_html_a432cd5c18caf466acab4b1274fcbd2dc"></a>
<a id="astructieee802154__fcf__seq_html_a49c3f394fc0fdc2d6eeb965204880aab"></a>
<a id="astructieee802154__fcf__seq_html_a4e3c453eff92ade1c9e7a80fa6773c1c"></a>
<a id="astructieee802154__fcf__seq_html_a610345dda1d427d03a3e3c633f64d39d"></a>
<a id="astructieee802154__fcf__seq_html_a6410a742c781cfa7bd4c29c14d9d9a4f"></a>
<a id="astructieee802154__fcf__seq_html_ac2233d00a5fa2fefc055d1630ba3f3d9"></a>
<a id="astructieee802154__fcf__seq_html_aca5c9dfc868ea8cfcfa36e07efe5c98a"></a>
<a id="astructieee802154__fcf__seq_html_acc6ddee048e3a443b6d8d577d32c3bfd"></a>
<a id="astructieee802154__fcf__seq_html_acf2a20dee02831538a456ef9d2932ddb"></a>
<a id="astructieee802154__fcf__seq_html_ad0f95976a3d42731c4b71cf69ea7f60c"></a>
<a id="astructieee802154__fcf__seq_html_ad531668d097300994f36b10b8beb5110"></a>
<a id="astructieee802154__fcf__seq_html_adc0f9964a40343d4f35f3c1ac9cc2fac"></a>
<a id="astructieee802154__frame__params_html"></a>
<a id="astructieee802154__frame__params_html_a410afc9ab9d85c0bb04de122ceabc38e"></a>
<a id="astructieee802154__frame__params_html_a9e1e16dfa5f5b093273c967910a89ee4"></a>
<a id="astructieee802154__frame__params_html_aaef4ec5c7a17547b416121d5e9ffb12c"></a>
<a id="astructieee802154__frame__params_html_ad45f0ac29e589c03905e7ecdcc0e38a6"></a>
<a id="astructieee802154__frame__params_html_af914ce32e424fb747d421862a5a125b6"></a>
<a id="astructieee802154__gts__dir_html"></a>
<a id="astructieee802154__gts__dir_html_a8f3e09bed02abb0b69234b10fb9604f7"></a>
<a id="astructieee802154__gts__dir_html_abdff100f062a94d5c1c90f2590e69053"></a>
<a id="astructieee802154__gts__request_html"></a>
<a id="astructieee802154__gts__request_html_a1a74a41c410151b226d70811c60de7e2"></a>
<a id="astructieee802154__gts__request_html_a1acd3d9aed7f810920a65648bddf382c"></a>
<a id="astructieee802154__gts__request_html_a4ac97f1eb0825cc2a0f7710fed1ddd05"></a>
<a id="astructieee802154__gts__request_html_a83571302ed121202cd86cf4e3e66995c"></a>
<a id="astructieee802154__gts__request_html_a92613246fdbb6ea22760cf973afb8c9e"></a>
<a id="astructieee802154__gts__spec_html"></a>
<a id="astructieee802154__gts__spec_html_a37d0ae20cb6da8ed68848d06b92013f5"></a>
<a id="astructieee802154__gts__spec_html_a5cea7b714d7f8ab2afe1261d96593491"></a>
<a id="astructieee802154__gts__spec_html_a81f217f576b60b71c84cb62d307400df"></a>
<a id="astructieee802154__gts_html"></a>
<a id="astructieee802154__gts_html_a078d4243d65ad85d3ee0beb2893e1488"></a>
<a id="astructieee802154__gts_html_a0bef800dfd406909151441a5f8377620"></a>
<a id="astructieee802154__gts_html_af10aaa68ded8215fa9ee3937ea0f5b35"></a>
<a id="astructieee802154__key__identifier__field_html"></a>
<a id="astructieee802154__key__identifier__field_html_a115e0904934594d97835794d557c67c8"></a>
<a id="astructieee802154__key__identifier__field_html_a62bd54d089679ad1fa3507aa51703a11"></a>
<a id="astructieee802154__key__identifier__field_html_a8808e859495b57da67517a43f0220f93"></a>
<a id="astructieee802154__key__identifier__field_html_a90c06bb718d4c41172d1a3bb593ecdea"></a>
<a id="astructieee802154__key__identifier__field_html_af3253a67435557031b548e44a6b32710"></a>
<a id="astructieee802154__mhr_html"></a>
<a id="astructieee802154__mhr_html_a0969c61b6aecb1bbec20b56fd3da0d75"></a>
<a id="astructieee802154__mhr_html_a3b818c1968863487e98750515fc2c8e3"></a>
<a id="astructieee802154__mhr_html_acd85befcf2ae1a1088661d6cab43e1fa"></a>
<a id="astructieee802154__mhr_html_adf0f4ed096d9992079efc4a78cba94d2"></a>
<a id="astructieee802154__mpdu_html"></a>
<a id="astructieee802154__mpdu_html_a3c63d608275c7939a5749aa125b7aa2c"></a>
<a id="astructieee802154__mpdu_html_a4672c27faba147276a5e6727087b9a69"></a>
<a id="astructieee802154__mpdu_html_a6787b11ba86fb7300287c4a599f5c59c"></a>
<a id="astructieee802154__mpdu_html_a7e364474043e879bbb4b38d58404e3d7"></a>
<a id="astructieee802154__mpdu_html_ab2646c3a52569fdfccf5639845461f60"></a>
<a id="astructieee802154__pas__spec_html"></a>
<a id="astructieee802154__pas__spec_html_a0429476706f4cbd91082d200963fc71a"></a>
<a id="astructieee802154__pas__spec_html_a18c098d3dfb15a1902ff90e63041447a"></a>
<a id="astructieee802154__pas__spec_html_a3d6cc7e71589d1ade099a823ec052923"></a>
<a id="astructieee802154__pas__spec_html_a607b544fb918ecd26c1448597e00c5f6"></a>
<a id="astructieee802154__security__control__field_html"></a>
<a id="astructieee802154__security__control__field_html_a7e497bc409cf73cea2b374418eeeb7cd"></a>
<a id="astructieee802154__security__control__field_html_ab4063e2e9715ef131e585ddaaea42090"></a>
<a id="astructieee802154__security__control__field_html_af57b19d0851fbda4c91c8cbaf79b0722"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_ac6eef59915e7ce167442fdacbbfb5e56"></a>
<a id="astructnet__buf_html_ae75b7ca728fb7440ea483be8bf88bc38"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__linkaddr_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnet__pkt_html_a1c27e50656b8c2713704d979b902c5d6"></a>
<a id="astructnet__pkt_html_a7590eeacf06469206cb7e7949acfa7b2"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_IEEE802154_FRAME_H_
#define ZEPHYR_INCLUDE_NET_IEEE802154_FRAME_H_

#include <zephyr/kernel.h>
#include <zephyr/net/ieee802154.h>
#include <zephyr/net/net_pkt.h>
#include <zephyr/toolchain.h>

#define IEEE802154_ACK_PKT_LENGTH 3

#define IEEE802154_MIN_LENGTH     IEEE802154_ACK_PKT_LENGTH

#define IEEE802154_FCF_SEQ_LENGTH 3

#define IEEE802154_PAN_ID_LENGTH  2

#define IEEE802154_BEACON_MIN_SIZE        4

#define IEEE802154_BEACON_SF_SIZE         2

#define IEEE802154_BEACON_GTS_SPEC_SIZE   1

#define IEEE802154_BEACON_GTS_IF_MIN_SIZE IEEE802154_BEACON_GTS_SPEC_SIZE

#define IEEE802154_BEACON_PAS_SPEC_SIZE   1

#define IEEE802154_BEACON_PAS_IF_MIN_SIZE IEEE802154_BEACON_PAS_SPEC_SIZE

#define IEEE802154_BEACON_GTS_DIR_SIZE    1

#define IEEE802154_BEACON_GTS_SIZE        3

#define IEEE802154_BEACON_GTS_RX          1

#define IEEE802154_BEACON_GTS_TX          0

enum ieee802154_frame_type {
        IEEE802154_FRAME_TYPE_BEACON = 0x0,
        IEEE802154_FRAME_TYPE_DATA = 0x1,
        IEEE802154_FRAME_TYPE_ACK = 0x2,
        IEEE802154_FRAME_TYPE_MAC_COMMAND = 0x3,
        IEEE802154_FRAME_TYPE_RESERVED = 0x4,
        IEEE802154_FRAME_TYPE_MULTIPURPOSE = 0x5,
        IEEE802154_FRAME_TYPE_FRAK = 0x6,
        IEEE802154_FRAME_TYPE_EXTENDED = 0x7,
};

enum ieee802154_addressing_mode {
        IEEE802154_ADDR_MODE_NONE = 0x0,
        IEEE802154_ADDR_MODE_RESERVED = 0x1,
        IEEE802154_ADDR_MODE_SHORT = 0x2,
        IEEE802154_ADDR_MODE_EXTENDED = 0x3,
};

enum ieee802154_version {
        IEEE802154_VERSION_802154_2003 = 0x0,
        IEEE802154_VERSION_802154_2006 = 0x1,
        IEEE802154_VERSION_802154 = 0x2,
        IEEE802154_VERSION_RESERVED = 0x3,
};

struct ieee802154_fcf_seq {
        struct {
#ifdef CONFIG_LITTLE_ENDIAN
                uint16_t frame_type: 3;
                uint16_t security_enabled: 1;
                uint16_t frame_pending: 1;
                uint16_t ar: 1;
                uint16_t pan_id_comp: 1;
                uint16_t reserved: 1;
                uint16_t seq_num_suppr: 1;
                uint16_t ie_list: 1;
                uint16_t dst_addr_mode: 2;
                uint16_t frame_version: 2;
                uint16_t src_addr_mode: 2;
#else
                uint16_t reserved: 1;
                uint16_t pan_id_comp: 1;
                uint16_t ar: 1;
                uint16_t frame_pending: 1;
                uint16_t security_enabled: 1;
                uint16_t frame_type: 3;
                uint16_t src_addr_mode: 2;
                uint16_t frame_version: 2;
                uint16_t dst_addr_mode: 2;
                uint16_t ie_list: 1;
                uint16_t seq_num_suppr: 1;
#endif
        } fc __packed;

        uint8_t sequence;
} __packed;

struct ieee802154_address {
        union {
                uint16_t short_addr;
                uint8_t ext_addr[0];
        };
} __packed;

struct ieee802154_address_field_comp {
        struct ieee802154_address addr;
} __packed;

struct ieee802154_address_field_plain {
        uint16_t pan_id;
        struct ieee802154_address addr;
} __packed;

struct ieee802154_address_field {
        union {
                struct ieee802154_address_field_plain plain;
                struct ieee802154_address_field_comp comp;
        };
} __packed;

enum ieee802154_security_level {
        IEEE802154_SECURITY_LEVEL_NONE = 0x0,
        IEEE802154_SECURITY_LEVEL_MIC_32 = 0x1,
        IEEE802154_SECURITY_LEVEL_MIC_64 = 0x2,
        IEEE802154_SECURITY_LEVEL_MIC_128 = 0x3,
        IEEE802154_SECURITY_LEVEL_RESERVED = 0x4,
        IEEE802154_SECURITY_LEVEL_ENC_MIC_32 = 0x5,
        IEEE802154_SECURITY_LEVEL_ENC_MIC_64 = 0x6,
        IEEE802154_SECURITY_LEVEL_ENC_MIC_128 = 0x7,
};

#define IEEE802154_SECURITY_LEVEL_ENC IEEE802154_SECURITY_LEVEL_RESERVED

#define IEEE802154_AUTH_TAG_LENGTH_32  4

#define IEEE802154_AUTH_TAG_LENGTH_64  8

#define IEEE802154_AUTH_TAG_LENGTH_128 16

enum ieee802154_key_id_mode {
        IEEE802154_KEY_ID_MODE_IMPLICIT = 0x0,
        IEEE802154_KEY_ID_MODE_INDEX = 0x1,
        IEEE802154_KEY_ID_MODE_SRC_4_INDEX = 0x2,
        IEEE802154_KEY_ID_MODE_SRC_8_INDEX = 0x3,
};

#define IEEE802154_KEY_ID_FIELD_INDEX_LENGTH       1

#define IEEE802154_KEY_ID_FIELD_SRC_4_INDEX_LENGTH 5

#define IEEE802154_KEY_ID_FIELD_SRC_8_INDEX_LENGTH 9

#define IEEE802154_KEY_MAX_LEN 16

struct ieee802154_security_control_field {
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t security_level: 3;
        uint8_t key_id_mode: 2;
        uint8_t reserved: 3;
#else
        uint8_t reserved: 3;
        uint8_t key_id_mode: 2;
        uint8_t security_level: 3;
#endif
} __packed;

#define IEEE802154_SECURITY_CF_LENGTH 1

struct ieee802154_key_identifier_field {
        union {
                struct {
                        uint8_t key_index;
                } mode_1;

                struct {
                        uint8_t key_src[4];
                        uint8_t key_index;
                } mode_2;

                struct {
                        uint8_t key_src[8];
                        uint8_t key_index;
                } mode_3;
        };
} __packed;

struct ieee802154_aux_security_hdr {
        struct ieee802154_security_control_field control;
        uint32_t frame_counter;
        struct ieee802154_key_identifier_field kif;
} __packed;

#define IEEE802154_SECURITY_FRAME_COUNTER_LENGTH 4

struct ieee802154_mhr {
        struct ieee802154_fcf_seq *fs;
        struct ieee802154_address_field *dst_addr;
        struct ieee802154_address_field *src_addr;
        struct ieee802154_aux_security_hdr *aux_sec;
};

struct ieee802154_gts_dir {
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t mask: 7;
        uint8_t reserved: 1;
#else
        uint8_t reserved: 1;
        uint8_t mask: 7;
#endif
} __packed;

struct ieee802154_gts {
        uint16_t short_address;
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t starting_slot: 4;
        uint8_t length: 4;
#else
        uint8_t length: 4;
        uint8_t starting_slot: 4;
#endif
} __packed;

struct ieee802154_gts_spec {
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t desc_count: 3;
        uint8_t reserved: 4;
        uint8_t permit: 1;
#else
        uint8_t permit: 1;
        uint8_t reserved: 4;
        uint8_t desc_count: 3;
#endif
} __packed;

struct ieee802154_pas_spec {
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t nb_sap: 3;
        uint8_t reserved_1: 1;
        uint8_t nb_eap: 3;
        uint8_t reserved_2: 1;
#else
        uint8_t reserved_1: 1;
        uint8_t nb_eap: 3;
        uint8_t reserved_2: 1;
        uint8_t nb_sap: 3;
#endif
} __packed;

struct ieee802154_beacon_sf {
#ifdef CONFIG_LITTLE_ENDIAN
        uint16_t bc_order: 4;
        uint16_t sf_order: 4;
        uint16_t cap_slot: 4;
        uint16_t ble: 1;
        uint16_t reserved: 1;
        uint16_t coordinator: 1;
        uint16_t association: 1;
#else
        uint16_t sf_order: 4;
        uint16_t bc_order: 4;
        uint16_t association: 1;
        uint16_t coordinator: 1;
        uint16_t reserved: 1;
        uint16_t ble: 1;
        uint16_t cap_slot: 4;
#endif
} __packed;

struct ieee802154_beacon {
        struct ieee802154_beacon_sf sf;

        struct ieee802154_gts_spec gts;
} __packed;

struct ieee802154_cmd_assoc_req {
        struct {
#ifdef CONFIG_LITTLE_ENDIAN
                uint8_t reserved_1: 1;
                uint8_t dev_type: 1;
                uint8_t power_src: 1;
                uint8_t rx_on: 1;
                uint8_t association_type: 1;
                uint8_t reserved_2: 1;
                uint8_t sec_capability: 1;
                uint8_t alloc_addr: 1;
#else
                uint8_t alloc_addr: 1;
                uint8_t sec_capability: 1;
                uint8_t reserved_2: 1;
                uint8_t association_type: 1;
                uint8_t rx_on: 1;
                uint8_t power_src: 1;
                uint8_t dev_type: 1;
                uint8_t reserved_1: 1;
#endif
        } ci;
} __packed;

#define IEEE802154_CMD_ASSOC_REQ_LENGTH 1

enum ieee802154_association_status_field {
        IEEE802154_ASF_SUCCESSFUL = 0x00,
        IEEE802154_ASF_PAN_AT_CAPACITY = 0x01,
        IEEE802154_ASF_PAN_ACCESS_DENIED = 0x02,
        IEEE802154_ASF_RESERVED = 0x03,
        IEEE802154_ASF_RESERVED_PRIMITIVES = 0x80,
};

struct ieee802154_cmd_assoc_res {
        uint16_t short_addr;
        uint8_t status;
} __packed;

#define IEEE802154_CMD_ASSOC_RES_LENGTH 3

enum ieee802154_disassociation_reason_field {
        IEEE802154_DRF_RESERVED_1 = 0x00,
        IEEE802154_DRF_COORDINATOR_WISH = 0x01,
        IEEE802154_DRF_DEVICE_WISH = 0x02,
        IEEE802154_DRF_RESERVED_2 = 0x03,
        IEEE802154_DRF_RESERVED_PRIMITIVES = 0x80,
};

struct ieee802154_cmd_disassoc_note {
        uint8_t reason;
} __packed;

#define IEEE802154_CMD_DISASSOC_NOTE_LENGTH 1

struct ieee802154_cmd_coord_realign {
        uint16_t pan_id;
        uint16_t coordinator_short_addr;
        uint8_t channel;
        uint16_t short_addr;
        uint8_t channel_page;
} __packed;

#define IEEE802154_CMD_COORD_REALIGN_LENGTH 3

struct ieee802154_gts_request {
        struct {
#ifdef CONFIG_LITTLE_ENDIAN
                uint8_t length: 4;
                uint8_t direction: 1;
                uint8_t type: 1;
                uint8_t reserved: 2;
#else
                uint8_t reserved: 2;
                uint8_t type: 1;
                uint8_t direction: 1;
                uint8_t length: 4;
#endif
        } gts;
} __packed;

#define IEEE802154_GTS_REQUEST_LENGTH 1

enum ieee802154_cfi {
        IEEE802154_CFI_UNKNOWN = 0x00,
        IEEE802154_CFI_ASSOCIATION_REQUEST = 0x01,
        IEEE802154_CFI_ASSOCIATION_RESPONSE = 0x02,
        IEEE802154_CFI_DISASSOCIATION_NOTIFICATION = 0x03,
        IEEE802154_CFI_DATA_REQUEST = 0x04,
        IEEE802154_CFI_PAN_ID_CONFLICT_NOTIFICATION = 0x05,
        IEEE802154_CFI_ORPHAN_NOTIFICATION = 0x06,
        IEEE802154_CFI_BEACON_REQUEST = 0x07,
        IEEE802154_CFI_COORDINATOR_REALIGNEMENT = 0x08,
        IEEE802154_CFI_GTS_REQUEST = 0x09,
        IEEE802154_CFI_RESERVED = 0x0a,
};

struct ieee802154_command {
        uint8_t cfi;
        union {
                struct ieee802154_cmd_assoc_req assoc_req;
                struct ieee802154_cmd_assoc_res assoc_res;
                struct ieee802154_cmd_disassoc_note disassoc_note;
                struct ieee802154_cmd_coord_realign coord_realign;
                struct ieee802154_gts_request gts_request;
        };
} __packed;

#define IEEE802154_CMD_CFI_LENGTH 1

struct ieee802154_mpdu {
        struct ieee802154_mhr mhr;
        union {
                void *payload;
                struct ieee802154_beacon *beacon;
                struct ieee802154_command *command;
        };
        uint16_t payload_length;
};

struct ieee802154_frame_params {
        struct {
                union {
                        uint8_t ext_addr[IEEE802154_EXT_ADDR_LENGTH];
                        uint16_t short_addr;
                };

                uint16_t len;
                uint16_t pan_id;
        } dst;

        uint16_t short_addr;
        uint16_t pan_id;
} __packed;


#ifdef CONFIG_NET_L2_IEEE802154_SECURITY
struct ieee802154_aux_security_hdr *
ieee802154_validate_aux_security_hdr(uint8_t *buf, uint8_t **p_buf, uint8_t *length);
#endif

struct ieee802154_fcf_seq *ieee802154_validate_fc_seq(uint8_t *buf, uint8_t **p_buf,
                                                      uint8_t *length);

int ieee802514_beacon_header_length(uint8_t *buf, uint8_t length);

bool ieee802154_validate_frame(uint8_t *buf, uint8_t length, struct ieee802154_mpdu *mpdu);

void ieee802154_compute_header_and_authtag_len(struct net_if *iface, struct net_linkaddr *dst,
                                               struct net_linkaddr *src, uint8_t *ll_hdr_len,
                                               uint8_t *authtag_len);

bool ieee802154_create_data_frame(struct ieee802154_context *ctx, struct net_linkaddr *dst,
                                  struct net_linkaddr *src, struct net_buf *buf,
                                  uint8_t ll_hdr_len);

struct net_pkt *ieee802154_create_mac_cmd_frame(struct net_if *iface, enum ieee802154_cfi type,
                                                struct ieee802154_frame_params *params);

void ieee802154_mac_cmd_finalize(struct net_pkt *pkt, enum ieee802154_cfi type);

static inline struct ieee802154_command *ieee802154_get_mac_command(struct net_pkt *pkt)
{
        return (struct ieee802154_command *)(pkt->frags->data + pkt->frags->len);
}

bool ieee802154_create_ack_frame(struct net_if *iface, struct net_pkt *pkt, uint8_t seq);

#ifdef CONFIG_NET_L2_IEEE802154_SECURITY
bool ieee802154_decipher_data_frame(struct net_if *iface, struct net_pkt *pkt,
                                    struct ieee802154_mpdu *mpdu);
#else
#define ieee802154_decipher_data_frame(...) true
#endif /* CONFIG_NET_L2_IEEE802154_SECURITY */


#endif /* ZEPHYR_INCLUDE_NET_IEEE802154_FRAME_H_ */
```

## 338.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 1031 行

条件编译配置（Configuration）标记：`CONFIG_NET_L2_IEEE802154_SECURITY`。

### 注释 3：原第 1035 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_IEEE802154_FRAME_H_`。

## 338.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net/ieee802154.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154_8h.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [ieee802154_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a16702b800d3e4a51df6cb6f909ff79fd)
- [IEEE802154_FRAME_TYPE_BEACON](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a16702b800d3e4a51df6cb6f909ff79fda6253c6948e0ecbc79878bd1fd73473ec)
- [IEEE802154_FRAME_TYPE_DATA](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a16702b800d3e4a51df6cb6f909ff79fda59490f8a40d1c65c365b3370ccabd3d8)
- [IEEE802154_FRAME_TYPE_ACK](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a16702b800d3e4a51df6cb6f909ff79fdacd5ec548c6199b61912ed8a15df3b486)
- [IEEE802154_FRAME_TYPE_MAC_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a16702b800d3e4a51df6cb6f909ff79fda69235bb8211a5a4a3c4fde6379d28644)
- [IEEE802154_FRAME_TYPE_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a16702b800d3e4a51df6cb6f909ff79fdaf14e1c3c75c77dcfaf54d2d637b9b4ae)
- [IEEE802154_FRAME_TYPE_MULTIPURPOSE](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a16702b800d3e4a51df6cb6f909ff79fda953e79789829eb3e220bccb94f21316f)
- [IEEE802154_FRAME_TYPE_FRAK](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a16702b800d3e4a51df6cb6f909ff79fdaaabec4197346f0d36903217c1f68b90f)
- [IEEE802154_FRAME_TYPE_EXTENDED](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a16702b800d3e4a51df6cb6f909ff79fdacb7f98a3d76846d411bc698572a5eeb5)
- [ieee802154_addressing_mode](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a49f3241733da0a6dd0003d7bcaf55965)
- [IEEE802154_ADDR_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a49f3241733da0a6dd0003d7bcaf55965a50e45c02f42ef667e1216cfc1024860f)
- [IEEE802154_ADDR_MODE_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a49f3241733da0a6dd0003d7bcaf55965a6f5f3599146d548b541dd22fa1f6322c)
- [IEEE802154_ADDR_MODE_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a49f3241733da0a6dd0003d7bcaf55965aa51f0be0ff88addcd167b03051e2dc21)
- [IEEE802154_ADDR_MODE_EXTENDED](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a49f3241733da0a6dd0003d7bcaf55965a27c38f60597d1b202cbb0e6c8cad27fd)
- [ieee802154_version](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa6a4b34e9722f5ccd06b65cf64efe053)
- [IEEE802154_VERSION_802154_2003](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa6a4b34e9722f5ccd06b65cf64efe053aad3af323ce4f598be0256ec9c19dcf36)
- [IEEE802154_VERSION_802154_2006](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa6a4b34e9722f5ccd06b65cf64efe053a3b2b709ecd3a2a1a4b997baf26c40bbc)
- [IEEE802154_VERSION_802154](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa6a4b34e9722f5ccd06b65cf64efe053aa2a088916733a4de4d009caaea734ca2)
- [IEEE802154_VERSION_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa6a4b34e9722f5ccd06b65cf64efe053a8112ae7940d211afe7a5a1a79071ad57)
- [ieee802154_fcf_seq](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [frame_type](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#a4e3c453eff92ade1c9e7a80fa6773c1c)
- [security_enabled](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#adc0f9964a40343d4f35f3c1ac9cc2fac)
- [frame_pending](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#a6410a742c781cfa7bd4c29c14d9d9a4f)
- [ar](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#ac2233d00a5fa2fefc055d1630ba3f3d9)
- [pan_id_comp](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#ad0f95976a3d42731c4b71cf69ea7f60c)
- [reserved](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#a3ad3dbf5ba7cd8b32b7ae5804c692f24)
- [seq_num_suppr](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#ad531668d097300994f36b10b8beb5110)
- [ie_list](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#aca5c9dfc868ea8cfcfa36e07efe5c98a)
- [dst_addr_mode](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#acf2a20dee02831538a456ef9d2932ddb)
- [frame_version](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#a610345dda1d427d03a3e3c633f64d39d)
- [src_addr_mode](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#a432cd5c18caf466acab4b1274fcbd2dc)
- [fc](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#acc6ddee048e3a443b6d8d577d32c3bfd)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sequence](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#a49c3f394fc0fdc2d6eeb965204880aab)
- [ieee802154_address](../network_core_model_reference/P001_ieee802154_address_结构体.md)
- [short_addr](../network_core_model_reference/P001_ieee802154_address_结构体.md#a3fecbe4e7ad6a32d57af1fbdaca5c881)
- [ext_addr](../network_core_model_reference/P001_ieee802154_address_结构体.md#ac954ef5b107997dbb953a0efae865ab1)
- [ieee802154_address_field_comp](../network_core_model_reference/P003_ieee802154_address_field_comp_结构体.md)
- [addr](../network_core_model_reference/P003_ieee802154_address_field_comp_结构体.md#a3c7f8e5bb1f015e02123669726fbcf6c)
- [ieee802154_address_field_plain](../network_core_model_reference/P004_ieee802154_address_field_plain_结构体.md)
- [pan_id](../network_core_model_reference/P004_ieee802154_address_field_plain_结构体.md#a8237aa26d9e3d564c349f90c8841cee7)
- [addr](../network_core_model_reference/P004_ieee802154_address_field_plain_结构体.md#aff9f5b6d0392c0ba401cb90d63631214)
- [ieee802154_address_field](../network_core_model_reference/P002_ieee802154_address_field_结构体.md)
- [plain](../network_core_model_reference/P002_ieee802154_address_field_结构体.md#ae06d1451a3006bfe10abc6148ce8ebce)
- [comp](../network_core_model_reference/P002_ieee802154_address_field_结构体.md#af3df38a8424bfe75cd8ad9694b31074f)
- [ieee802154_security_level](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aaf5ffabf140bf36c9076662e4b46e4a2)
- [IEEE802154_SECURITY_LEVEL_NONE](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aaf5ffabf140bf36c9076662e4b46e4a2af5bff347e35ac0af5c86b65ef231df47)
- [IEEE802154_SECURITY_LEVEL_MIC_32](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aaf5ffabf140bf36c9076662e4b46e4a2a2b8b7e0d195c7fb33e3578b86bda99d7)
- [IEEE802154_SECURITY_LEVEL_MIC_64](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aaf5ffabf140bf36c9076662e4b46e4a2abe9a01bb053e5809e0f110cb0709d001)
- [IEEE802154_SECURITY_LEVEL_MIC_128](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aaf5ffabf140bf36c9076662e4b46e4a2a60e7720ffc14a08b0f4c90b567ce57bd)
- [IEEE802154_SECURITY_LEVEL_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aaf5ffabf140bf36c9076662e4b46e4a2a2155c782cf4074f240bcb087aecc8f06)
- [IEEE802154_SECURITY_LEVEL_ENC_MIC_32](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aaf5ffabf140bf36c9076662e4b46e4a2a95e1e7954023a5cd3c35aaf6596b0821)
- [IEEE802154_SECURITY_LEVEL_ENC_MIC_64](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aaf5ffabf140bf36c9076662e4b46e4a2a649d558004918cacb4c9ec32d247c934)
- [IEEE802154_SECURITY_LEVEL_ENC_MIC_128](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aaf5ffabf140bf36c9076662e4b46e4a2abaa5076f0f373c3f2e415a8f28a6e0ee)
- [ieee802154_key_id_mode](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#ac5819ed25fa7b56756e8e7962f579ec7)
- [IEEE802154_KEY_ID_MODE_IMPLICIT](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#ac5819ed25fa7b56756e8e7962f579ec7a2519ea53b9adf534707e7ce4401966f6)
- [IEEE802154_KEY_ID_MODE_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#ac5819ed25fa7b56756e8e7962f579ec7a918058e16c48ecee20a8ce3968138c04)
- [IEEE802154_KEY_ID_MODE_SRC_4_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#ac5819ed25fa7b56756e8e7962f579ec7ae351b9dc1ba1e546a706c861b4dfd841)
- [IEEE802154_KEY_ID_MODE_SRC_8_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#ac5819ed25fa7b56756e8e7962f579ec7a0c363713ca56c27961d5198a5ee7078f)
- [ieee802154_security_control_field](../network_core_model_reference/P043_ieee802154_security_control_field_结构体.md)
- [security_level](../network_core_model_reference/P043_ieee802154_security_control_field_结构体.md#af57b19d0851fbda4c91c8cbaf79b0722)
- [key_id_mode](../network_core_model_reference/P043_ieee802154_security_control_field_结构体.md#ab4063e2e9715ef131e585ddaaea42090)
- [reserved](../network_core_model_reference/P043_ieee802154_security_control_field_结构体.md#a7e497bc409cf73cea2b374418eeeb7cd)
- [ieee802154_key_identifier_field](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md)
- [key_index](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md#a115e0904934594d97835794d557c67c8)
- [mode_1](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md#a90c06bb718d4c41172d1a3bb593ecdea)
- [key_src](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md#af3253a67435557031b548e44a6b32710)
- [mode_2](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md#a62bd54d089679ad1fa3507aa51703a11)
- [mode_3](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md#a8808e859495b57da67517a43f0220f93)
- [ieee802154_aux_security_hdr](../network_core_model_reference/P006_ieee802154_aux_security_hdr_结构体.md)
- [control](../network_core_model_reference/P006_ieee802154_aux_security_hdr_结构体.md#a75a365c8c642f17aedc5c08754272c79)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [frame_counter](../network_core_model_reference/P006_ieee802154_aux_security_hdr_结构体.md#a4c9113e6ce77856e09822866c281d5eb)
- [kif](../network_core_model_reference/P006_ieee802154_aux_security_hdr_结构体.md#a7c7facc1f1b9fa5fedd94e9a6afe2f0b)
- [ieee802154_mhr](../network_core_model_reference/P034_ieee802154_mhr_结构体.md)
- [fs](../network_core_model_reference/P034_ieee802154_mhr_结构体.md#a0969c61b6aecb1bbec20b56fd3da0d75)
- [dst_addr](../network_core_model_reference/P034_ieee802154_mhr_结构体.md#adf0f4ed096d9992079efc4a78cba94d2)
- [src_addr](../network_core_model_reference/P034_ieee802154_mhr_结构体.md#acd85befcf2ae1a1088661d6cab43e1fa)
- [aux_sec](../network_core_model_reference/P034_ieee802154_mhr_结构体.md#a3b818c1968863487e98750515fc2c8e3)
- [ieee802154_gts_dir](../network_core_model_reference/P020_ieee802154_gts_dir_结构体.md)
- [mask](../network_core_model_reference/P020_ieee802154_gts_dir_结构体.md#abdff100f062a94d5c1c90f2590e69053)
- [reserved](../network_core_model_reference/P020_ieee802154_gts_dir_结构体.md#a8f3e09bed02abb0b69234b10fb9604f7)
- [ieee802154_gts](../network_core_model_reference/P019_ieee802154_gts_结构体.md)
- [short_address](../network_core_model_reference/P019_ieee802154_gts_结构体.md#a078d4243d65ad85d3ee0beb2893e1488)
- [starting_slot](../network_core_model_reference/P019_ieee802154_gts_结构体.md#a0bef800dfd406909151441a5f8377620)
- [length](../network_core_model_reference/P019_ieee802154_gts_结构体.md#af10aaa68ded8215fa9ee3937ea0f5b35)
- [ieee802154_gts_spec](../network_core_model_reference/P022_ieee802154_gts_spec_结构体.md)
- [desc_count](../network_core_model_reference/P022_ieee802154_gts_spec_结构体.md#a81f217f576b60b71c84cb62d307400df)
- [reserved](../network_core_model_reference/P022_ieee802154_gts_spec_结构体.md#a37d0ae20cb6da8ed68848d06b92013f5)
- [permit](../network_core_model_reference/P022_ieee802154_gts_spec_结构体.md#a5cea7b714d7f8ab2afe1261d96593491)
- [ieee802154_pas_spec](../network_core_model_reference/P038_ieee802154_pas_spec_结构体.md)
- [nb_sap](../network_core_model_reference/P038_ieee802154_pas_spec_结构体.md#a0429476706f4cbd91082d200963fc71a)
- [reserved_1](../network_core_model_reference/P038_ieee802154_pas_spec_结构体.md#a607b544fb918ecd26c1448597e00c5f6)
- [nb_eap](../network_core_model_reference/P038_ieee802154_pas_spec_结构体.md#a3d6cc7e71589d1ade099a823ec052923)
- [reserved_2](../network_core_model_reference/P038_ieee802154_pas_spec_结构体.md#a18c098d3dfb15a1902ff90e63041447a)
- [ieee802154_beacon_sf](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md)
- [bc_order](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#aa3f402e1ac43b609a366f0a7c87195bd)
- [sf_order](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#aa52c67ce1c7607dfeabbfe5706a75bb8)
- [cap_slot](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#ac1e5e4c10de0ef0bb22ff12a5097aed9)
- [ble](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#af57a9ae07bb6adb029be235929ed903b)
- [reserved](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#a4a6f895c5d3a86853647516d12073c32)
- [coordinator](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#a7f62606165bb7d2bd96cf0923de1326e)
- [association](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#a33a47bde19ad49508c981b1e7940ad93)
- [ieee802154_beacon](../network_core_model_reference/P007_ieee802154_beacon_结构体.md)
- [sf](../network_core_model_reference/P007_ieee802154_beacon_结构体.md#a1afd2b6d448a3c1dd4dfd471068f55ed)
- [gts](../network_core_model_reference/P007_ieee802154_beacon_结构体.md#a959331440b0fcdb24b4b624b607cdf3e)
- [ieee802154_cmd_assoc_req](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md)
- [reserved_1](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a19039e164a4804a8f8d901206b0bd19c)
- [dev_type](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a75f60ccf3390f5371e8af6c9c2234bf5)
- [power_src](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a306becbe9dc40df9f897c222e0d9f222)
- [rx_on](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#aea1e48101ca4ee67972e66b566e56259)
- [association_type](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#adc81f209a8f17a90b50fb57f2990d5b8)
- [reserved_2](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a43e69b46fe01aa8278e78abd341ff01e)
- [sec_capability](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a99a5743d96b9ebc5153edcfb326eb38a)
- [alloc_addr](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a22321a62b2049202c6eb84a25316bb9c)
- [ci](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a035bc9f5639f91ca39ac0142279d7ccd)
- [ieee802154_association_status_field](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa2c9cb8ba5b7c397c695a9a591649b91)
- [IEEE802154_ASF_SUCCESSFUL](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa2c9cb8ba5b7c397c695a9a591649b91a280571e677e992f5220f56818e52ccf4)
- [IEEE802154_ASF_PAN_AT_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa2c9cb8ba5b7c397c695a9a591649b91a571c5b2f63cedf01857ce31ba1125517)
- [IEEE802154_ASF_PAN_ACCESS_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa2c9cb8ba5b7c397c695a9a591649b91a1cedbaa8a44fdb79041e6b5ad8af6031)
- [IEEE802154_ASF_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa2c9cb8ba5b7c397c695a9a591649b91a3a72c63164f925e7fe6d12d9cf572d81)
- [IEEE802154_ASF_RESERVED_PRIMITIVES](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa2c9cb8ba5b7c397c695a9a591649b91a15eb8c84a04a1642e7395a872eb5db59)
- [ieee802154_cmd_assoc_res](../network_core_model_reference/P010_ieee802154_cmd_assoc_res_结构体.md)
- [short_addr](../network_core_model_reference/P010_ieee802154_cmd_assoc_res_结构体.md#a0aec016dd92112254d9d162734a9f2d6)
- [status](../network_core_model_reference/P010_ieee802154_cmd_assoc_res_结构体.md#a372c5c7bee963eb890ccddcab9526fc4)
- [ieee802154_disassociation_reason_field](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a2ab06c343e03a4d6e28073780eb47648)
- [IEEE802154_DRF_RESERVED_1](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a2ab06c343e03a4d6e28073780eb47648aec815962bcc4fe41d8a2223bc7b7e3c7)
- [IEEE802154_DRF_COORDINATOR_WISH](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a2ab06c343e03a4d6e28073780eb47648a8b04f0bae8a62282a8a7821a4db949cb)
- [IEEE802154_DRF_DEVICE_WISH](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a2ab06c343e03a4d6e28073780eb47648a3feadbd533ba9b31977e2fa7537fa8c1)
- [IEEE802154_DRF_RESERVED_2](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a2ab06c343e03a4d6e28073780eb47648ae09de01a9f7b2a7eba0ee0173765e1ef)
- [IEEE802154_DRF_RESERVED_PRIMITIVES](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a2ab06c343e03a4d6e28073780eb47648a2d69c0e06015471da07bce9314a900c7)
- [ieee802154_cmd_disassoc_note](../network_core_model_reference/P012_ieee802154_cmd_disassoc_note_结构体.md)
- [reason](../network_core_model_reference/P012_ieee802154_cmd_disassoc_note_结构体.md#a2353dfa2ad8eb0efa8794cb09a65ea44)
- [ieee802154_cmd_coord_realign](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md)
- [pan_id](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md#a9823ca16d8b99bb17583f402050aa80c)
- [coordinator_short_addr](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md#a07775fefaf0f87425beb6371bd112b26)
- [channel](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md#a6f91305584cf44c910a95cf93e73c84d)
- [short_addr](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md#ae8867213cecfe3342dd951b1e03bde2d)
- [channel_page](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md#a0602708c2dc512c12f2901d84d090f30)
- [ieee802154_gts_request](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md)
- [length](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md#a4ac97f1eb0825cc2a0f7710fed1ddd05)
- [direction](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md#a92613246fdbb6ea22760cf973afb8c9e)
- [type](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md#a83571302ed121202cd86cf4e3e66995c)
- [reserved](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md#a1acd3d9aed7f810920a65648bddf382c)
- [gts](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md#a1a74a41c410151b226d70811c60de7e2)
- [ieee802154_cfi](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199)
- [IEEE802154_CFI_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199a9371a4aeeab31f2f0eb52a188d8a2990)
- [IEEE802154_CFI_ASSOCIATION_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199a867cc7c5b4c9e1b99dda26bfc1713d87)
- [IEEE802154_CFI_ASSOCIATION_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199a2541a973cde011d980fe2565803a30f4)
- [IEEE802154_CFI_DISASSOCIATION_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199a0ee7d320f5923af196869ac9c348ec34)
- [IEEE802154_CFI_DATA_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199a8d85bf1bc19b90562b854db227c74211)
- [IEEE802154_CFI_PAN_ID_CONFLICT_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199a446febb8ad088218de365cd86d406c94)
- [IEEE802154_CFI_ORPHAN_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199a0a15cf36690a5224f8239f24687ca09f)
- [IEEE802154_CFI_BEACON_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199a89935d04845589a5a8d4c4d6abeb4ef5)
- [IEEE802154_CFI_COORDINATOR_REALIGNEMENT](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199a234e0cdb8bebaa8e9da8da2052babd71)
- [IEEE802154_CFI_GTS_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199a256265e47b2e4cdc50596153ee2a9018)
- [IEEE802154_CFI_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199a9ebdc4dfb6ca44098e9bdc2635dc7b18)
- [ieee802154_command](../network_core_model_reference/P013_ieee802154_command_结构体.md)
- [cfi](../network_core_model_reference/P013_ieee802154_command_结构体.md#a1bc60b61ef82a58d080b07c1a0b27626)
- [assoc_req](../network_core_model_reference/P013_ieee802154_command_结构体.md#aa21a32878e544c284f6efb7c78ed079a)
- [assoc_res](../network_core_model_reference/P013_ieee802154_command_结构体.md#addbd05e3e770199f71ecf20dd0b716a9)
- [disassoc_note](../network_core_model_reference/P013_ieee802154_command_结构体.md#a61700791f0e2148e23836340cbf9d0b8)
- [coord_realign](../network_core_model_reference/P013_ieee802154_command_结构体.md#ae5b9b8f7dc12ac73d2b392052a60b48d)
- [gts_request](../network_core_model_reference/P013_ieee802154_command_结构体.md#a6ad0a1fa2c4985b10e35ac282d27e3d1)
- [ieee802154_mpdu](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md)
- [mhr](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md#a7e364474043e879bbb4b38d58404e3d7)
- [payload](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md#a4672c27faba147276a5e6727087b9a69)
- [beacon](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md#a3c63d608275c7939a5749aa125b7aa2c)
- [command](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md#ab2646c3a52569fdfccf5639845461f60)
- [payload_length](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md#a6787b11ba86fb7300287c4a599f5c59c)
- [ieee802154_frame_params](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md)
- [ext_addr](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md#a410afc9ab9d85c0bb04de122ceabc38e)
- [IEEE802154_EXT_ADDR_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga355350794ec26788bc855da53d311bea)
- [short_addr](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md#af914ce32e424fb747d421862a5a125b6)
- [len](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md#ad45f0ac29e589c03905e7ecdcc0e38a6)
- [pan_id](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md#aaef4ec5c7a17547b416121d5e9ffb12c)
- [dst](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md#a9e1e16dfa5f5b093273c967910a89ee4)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)
- [ieee802154_context](../network_core_model_reference/P015_ieee802154_context_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [iface](../network_core_model_reference/P114_net_pkt_结构体.md#a7590eeacf06469206cb7e7949acfa7b2)
- [frags](../network_core_model_reference/P114_net_pkt_结构体.md#a1c27e50656b8c2713704d979b902c5d6)
- [data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [ieee802154.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [ieee802154_address_field_comp::addr](../network_core_model_reference/P003_ieee802154_address_field_comp_结构体.md#a3c7f8e5bb1f015e02123669726fbcf6c)
- [ieee802154_address_field_plain::pan_id](../network_core_model_reference/P004_ieee802154_address_field_plain_结构体.md#a8237aa26d9e3d564c349f90c8841cee7)
- [ieee802154_address_field_plain::addr](../network_core_model_reference/P004_ieee802154_address_field_plain_结构体.md#aff9f5b6d0392c0ba401cb90d63631214)
- [ieee802154_address_field::plain](../network_core_model_reference/P002_ieee802154_address_field_结构体.md#ae06d1451a3006bfe10abc6148ce8ebce)
- [ieee802154_address_field::comp](../network_core_model_reference/P002_ieee802154_address_field_结构体.md#af3df38a8424bfe75cd8ad9694b31074f)
- [ieee802154_address::short_addr](../network_core_model_reference/P001_ieee802154_address_结构体.md#a3fecbe4e7ad6a32d57af1fbdaca5c881)
- [ieee802154_address::ext_addr](../network_core_model_reference/P001_ieee802154_address_结构体.md#ac954ef5b107997dbb953a0efae865ab1)
- [ieee802154_aux_security_hdr::frame_counter](../network_core_model_reference/P006_ieee802154_aux_security_hdr_结构体.md#a4c9113e6ce77856e09822866c281d5eb)
- [ieee802154_aux_security_hdr::control](../network_core_model_reference/P006_ieee802154_aux_security_hdr_结构体.md#a75a365c8c642f17aedc5c08754272c79)
- [ieee802154_aux_security_hdr::kif](../network_core_model_reference/P006_ieee802154_aux_security_hdr_结构体.md#a7c7facc1f1b9fa5fedd94e9a6afe2f0b)
- [ieee802154_beacon_sf::association](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#a33a47bde19ad49508c981b1e7940ad93)
- [ieee802154_beacon_sf::reserved](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#a4a6f895c5d3a86853647516d12073c32)
- [ieee802154_beacon_sf::coordinator](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#a7f62606165bb7d2bd96cf0923de1326e)
- [ieee802154_beacon_sf::bc_order](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#aa3f402e1ac43b609a366f0a7c87195bd)
- [ieee802154_beacon_sf::sf_order](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#aa52c67ce1c7607dfeabbfe5706a75bb8)
- [ieee802154_beacon_sf::cap_slot](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#ac1e5e4c10de0ef0bb22ff12a5097aed9)
- [ieee802154_beacon_sf::ble](../network_core_model_reference/P008_ieee802154_beacon_sf_结构体.md#af57a9ae07bb6adb029be235929ed903b)
- [ieee802154_beacon::sf](../network_core_model_reference/P007_ieee802154_beacon_结构体.md#a1afd2b6d448a3c1dd4dfd471068f55ed)
- [ieee802154_beacon::gts](../network_core_model_reference/P007_ieee802154_beacon_结构体.md#a959331440b0fcdb24b4b624b607cdf3e)
- [ieee802154_cmd_assoc_req::ci](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a035bc9f5639f91ca39ac0142279d7ccd)
- [ieee802154_cmd_assoc_req::reserved_1](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a19039e164a4804a8f8d901206b0bd19c)
- [ieee802154_cmd_assoc_req::alloc_addr](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a22321a62b2049202c6eb84a25316bb9c)
- [ieee802154_cmd_assoc_req::power_src](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a306becbe9dc40df9f897c222e0d9f222)
- [ieee802154_cmd_assoc_req::reserved_2](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a43e69b46fe01aa8278e78abd341ff01e)
- [ieee802154_cmd_assoc_req::dev_type](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a75f60ccf3390f5371e8af6c9c2234bf5)
- [ieee802154_cmd_assoc_req::sec_capability](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#a99a5743d96b9ebc5153edcfb326eb38a)
- [ieee802154_cmd_assoc_req::association_type](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#adc81f209a8f17a90b50fb57f2990d5b8)
- [ieee802154_cmd_assoc_req::rx_on](../network_core_model_reference/P009_ieee802154_cmd_assoc_req_结构体.md#aea1e48101ca4ee67972e66b566e56259)
- [ieee802154_cmd_assoc_res::short_addr](../network_core_model_reference/P010_ieee802154_cmd_assoc_res_结构体.md#a0aec016dd92112254d9d162734a9f2d6)
- [ieee802154_cmd_assoc_res::status](../network_core_model_reference/P010_ieee802154_cmd_assoc_res_结构体.md#a372c5c7bee963eb890ccddcab9526fc4)
- [ieee802154_cmd_coord_realign::channel_page](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md#a0602708c2dc512c12f2901d84d090f30)
- [ieee802154_cmd_coord_realign::coordinator_short_addr](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md#a07775fefaf0f87425beb6371bd112b26)
- [ieee802154_cmd_coord_realign::channel](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md#a6f91305584cf44c910a95cf93e73c84d)
- [ieee802154_cmd_coord_realign::pan_id](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md#a9823ca16d8b99bb17583f402050aa80c)
- [ieee802154_cmd_coord_realign::short_addr](../network_core_model_reference/P011_ieee802154_cmd_coord_realign_结构体.md#ae8867213cecfe3342dd951b1e03bde2d)
- [ieee802154_cmd_disassoc_note::reason](../network_core_model_reference/P012_ieee802154_cmd_disassoc_note_结构体.md#a2353dfa2ad8eb0efa8794cb09a65ea44)
- [ieee802154_command::cfi](../network_core_model_reference/P013_ieee802154_command_结构体.md#a1bc60b61ef82a58d080b07c1a0b27626)
- [ieee802154_command::disassoc_note](../network_core_model_reference/P013_ieee802154_command_结构体.md#a61700791f0e2148e23836340cbf9d0b8)
- [ieee802154_command::gts_request](../network_core_model_reference/P013_ieee802154_command_结构体.md#a6ad0a1fa2c4985b10e35ac282d27e3d1)
- [ieee802154_command::assoc_req](../network_core_model_reference/P013_ieee802154_command_结构体.md#aa21a32878e544c284f6efb7c78ed079a)
- [ieee802154_command::assoc_res](../network_core_model_reference/P013_ieee802154_command_结构体.md#addbd05e3e770199f71ecf20dd0b716a9)
- [ieee802154_command::coord_realign](../network_core_model_reference/P013_ieee802154_command_结构体.md#ae5b9b8f7dc12ac73d2b392052a60b48d)
- [ieee802154_fcf_seq::reserved](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#a3ad3dbf5ba7cd8b32b7ae5804c692f24)
- [ieee802154_fcf_seq::src_addr_mode](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#a432cd5c18caf466acab4b1274fcbd2dc)
- [ieee802154_fcf_seq::sequence](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#a49c3f394fc0fdc2d6eeb965204880aab)
- [ieee802154_fcf_seq::frame_type](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#a4e3c453eff92ade1c9e7a80fa6773c1c)
- [ieee802154_fcf_seq::frame_version](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#a610345dda1d427d03a3e3c633f64d39d)
- [ieee802154_fcf_seq::frame_pending](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#a6410a742c781cfa7bd4c29c14d9d9a4f)
- [ieee802154_fcf_seq::ar](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#ac2233d00a5fa2fefc055d1630ba3f3d9)
- [ieee802154_fcf_seq::ie_list](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#aca5c9dfc868ea8cfcfa36e07efe5c98a)
- [ieee802154_fcf_seq::fc](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#acc6ddee048e3a443b6d8d577d32c3bfd)
- [ieee802154_fcf_seq::dst_addr_mode](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#acf2a20dee02831538a456ef9d2932ddb)
- [ieee802154_fcf_seq::pan_id_comp](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#ad0f95976a3d42731c4b71cf69ea7f60c)
- [ieee802154_fcf_seq::seq_num_suppr](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#ad531668d097300994f36b10b8beb5110)
- [ieee802154_fcf_seq::security_enabled](../network_core_model_reference/P016_ieee802154_fcf_seq_结构体.md#adc0f9964a40343d4f35f3c1ac9cc2fac)
- [ieee802154_frame_params::ext_addr](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md#a410afc9ab9d85c0bb04de122ceabc38e)
- [ieee802154_frame_params::dst](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md#a9e1e16dfa5f5b093273c967910a89ee4)
- [ieee802154_frame_params::pan_id](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md#aaef4ec5c7a17547b416121d5e9ffb12c)
- [ieee802154_frame_params::len](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md#ad45f0ac29e589c03905e7ecdcc0e38a6)
- [ieee802154_frame_params::short_addr](../network_core_model_reference/P018_ieee802154_frame_params_结构体.md#af914ce32e424fb747d421862a5a125b6)
- [ieee802154_gts_dir::reserved](../network_core_model_reference/P020_ieee802154_gts_dir_结构体.md#a8f3e09bed02abb0b69234b10fb9604f7)
- [ieee802154_gts_dir::mask](../network_core_model_reference/P020_ieee802154_gts_dir_结构体.md#abdff100f062a94d5c1c90f2590e69053)
- [ieee802154_gts_request::gts](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md#a1a74a41c410151b226d70811c60de7e2)
- [ieee802154_gts_request::reserved](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md#a1acd3d9aed7f810920a65648bddf382c)
- [ieee802154_gts_request::length](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md#a4ac97f1eb0825cc2a0f7710fed1ddd05)
- [ieee802154_gts_request::type](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md#a83571302ed121202cd86cf4e3e66995c)
- [ieee802154_gts_request::direction](../network_core_model_reference/P021_ieee802154_gts_request_结构体.md#a92613246fdbb6ea22760cf973afb8c9e)
- [ieee802154_gts_spec::reserved](../network_core_model_reference/P022_ieee802154_gts_spec_结构体.md#a37d0ae20cb6da8ed68848d06b92013f5)
- [ieee802154_gts_spec::permit](../network_core_model_reference/P022_ieee802154_gts_spec_结构体.md#a5cea7b714d7f8ab2afe1261d96593491)
- [ieee802154_gts_spec::desc_count](../network_core_model_reference/P022_ieee802154_gts_spec_结构体.md#a81f217f576b60b71c84cb62d307400df)
- [ieee802154_gts::short_address](../network_core_model_reference/P019_ieee802154_gts_结构体.md#a078d4243d65ad85d3ee0beb2893e1488)
- [ieee802154_gts::starting_slot](../network_core_model_reference/P019_ieee802154_gts_结构体.md#a0bef800dfd406909151441a5f8377620)
- [ieee802154_gts::length](../network_core_model_reference/P019_ieee802154_gts_结构体.md#af10aaa68ded8215fa9ee3937ea0f5b35)
- [ieee802154_key_identifier_field::key_index](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md#a115e0904934594d97835794d557c67c8)
- [ieee802154_key_identifier_field::mode_2](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md#a62bd54d089679ad1fa3507aa51703a11)
- [ieee802154_key_identifier_field::mode_3](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md#a8808e859495b57da67517a43f0220f93)
- [ieee802154_key_identifier_field::mode_1](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md#a90c06bb718d4c41172d1a3bb593ecdea)
- [ieee802154_key_identifier_field::key_src](../network_core_model_reference/P033_ieee802154_key_identifier_field_结构体.md#af3253a67435557031b548e44a6b32710)
- [ieee802154_mhr::fs](../network_core_model_reference/P034_ieee802154_mhr_结构体.md#a0969c61b6aecb1bbec20b56fd3da0d75)
- [ieee802154_mhr::aux_sec](../network_core_model_reference/P034_ieee802154_mhr_结构体.md#a3b818c1968863487e98750515fc2c8e3)
- [ieee802154_mhr::src_addr](../network_core_model_reference/P034_ieee802154_mhr_结构体.md#acd85befcf2ae1a1088661d6cab43e1fa)
- [ieee802154_mhr::dst_addr](../network_core_model_reference/P034_ieee802154_mhr_结构体.md#adf0f4ed096d9992079efc4a78cba94d2)
- [ieee802154_mpdu::beacon](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md#a3c63d608275c7939a5749aa125b7aa2c)
- [ieee802154_mpdu::payload](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md#a4672c27faba147276a5e6727087b9a69)
- [ieee802154_mpdu::payload_length](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md#a6787b11ba86fb7300287c4a599f5c59c)
- [ieee802154_mpdu::mhr](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md#a7e364474043e879bbb4b38d58404e3d7)
- [ieee802154_mpdu::command](../network_core_model_reference/P035_ieee802154_mpdu_结构体.md#ab2646c3a52569fdfccf5639845461f60)
- [ieee802154_pas_spec::nb_sap](../network_core_model_reference/P038_ieee802154_pas_spec_结构体.md#a0429476706f4cbd91082d200963fc71a)
- [ieee802154_pas_spec::reserved_2](../network_core_model_reference/P038_ieee802154_pas_spec_结构体.md#a18c098d3dfb15a1902ff90e63041447a)
- [ieee802154_pas_spec::nb_eap](../network_core_model_reference/P038_ieee802154_pas_spec_结构体.md#a3d6cc7e71589d1ade099a823ec052923)
- [ieee802154_pas_spec::reserved_1](../network_core_model_reference/P038_ieee802154_pas_spec_结构体.md#a607b544fb918ecd26c1448597e00c5f6)
- [ieee802154_security_control_field::reserved](../network_core_model_reference/P043_ieee802154_security_control_field_结构体.md#a7e497bc409cf73cea2b374418eeeb7cd)
- [ieee802154_security_control_field::key_id_mode](../network_core_model_reference/P043_ieee802154_security_control_field_结构体.md#ab4063e2e9715ef131e585ddaaea42090)
- [ieee802154_security_control_field::security_level](../network_core_model_reference/P043_ieee802154_security_control_field_结构体.md#af57b19d0851fbda4c91c8cbaf79b0722)
- [net_buf::data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [net_buf::len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [net_pkt::frags](../network_core_model_reference/P114_net_pkt_结构体.md#a1c27e50656b8c2713704d979b902c5d6)
- [net_pkt::iface](../network_core_model_reference/P114_net_pkt_结构体.md#a7590eeacf06469206cb7e7949acfa7b2)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P337_icmp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P339_ieee802154_mgmt.h_源码浏览.md)
