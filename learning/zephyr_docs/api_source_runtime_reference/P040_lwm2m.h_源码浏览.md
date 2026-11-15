---
id: learning.zephyr-docs.api-source-runtime-reference.page-40
title: lwm2m.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_lwm2m.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h.html)。

## 40.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="l00065"></a>
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
<a id="l00094"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00114"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00143"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="foldopen00199"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="foldopen00210"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="foldopen00340"></a>
<a id="l00340"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00487"></a>
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
<a id="l00506"></a>
<a id="l00514"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00527"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00545"></a>
<a id="l00549"></a>
<a id="l00553"></a>
<a id="l00557"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00564"></a>
<a id="l00572"></a>
<a id="l00573"></a>
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
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00786"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="foldopen00812"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00888"></a>
<a id="l00889"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00919"></a>
<a id="l00920"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00949"></a>
<a id="l00950"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00969"></a>
<a id="l00970"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00989"></a>
<a id="l00990"></a>
<a id="l00999"></a>
<a id="l01000"></a>
<a id="l01009"></a>
<a id="l01010"></a>
<a id="l01019"></a>
<a id="l01020"></a>
<a id="foldopen01044"></a>
<a id="l01044"></a>
<a id="l01046"></a>
<a id="l01048"></a>
<a id="l01050"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01065"></a>
<a id="l01066"></a>
<a id="l01076"></a>
<a id="l01077"></a>
<a id="l01087"></a>
<a id="l01088"></a>
<a id="l01097"></a>
<a id="l01098"></a>
<a id="l01107"></a>
<a id="l01108"></a>
<a id="l01117"></a>
<a id="l01118"></a>
<a id="l01127"></a>
<a id="l01128"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="l01147"></a>
<a id="l01148"></a>
<a id="l01157"></a>
<a id="l01158"></a>
<a id="l01167"></a>
<a id="l01168"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01197"></a>
<a id="l01198"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01231"></a>
<a id="l01232"></a>
<a id="l01233"></a>
<a id="l01254"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="l01271"></a>
<a id="l01272"></a>
<a id="l01273"></a>
<a id="l01284"></a>
<a id="l01285"></a>
<a id="l01296"></a>
<a id="l01297"></a>
<a id="l01298"></a>
<a id="l01309"></a>
<a id="l01310"></a>
<a id="l01311"></a>
<a id="l01315"></a>
<a id="l01316"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="l01325"></a>
<a id="l01326"></a>
<a id="l01341"></a>
<a id="l01342"></a>
<a id="l01343"></a>
<a id="l01354"></a>
<a id="l01355"></a>
<a id="l01375"></a>
<a id="l01376"></a>
<a id="l01377"></a>
<a id="l01389"></a>
<a id="l01390"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01412"></a>
<a id="l01413"></a>
<a id="l01425"></a>
<a id="l01426"></a>
<a id="l01438"></a>
<a id="l01439"></a>
<a id="l01451"></a>
<a id="l01452"></a>
<a id="l01464"></a>
<a id="l01465"></a>
<a id="l01466"></a>
<a id="l01467"></a>
<a id="l01468"></a>
<a id="l01469"></a>
<a id="l01473"></a>
<a id="l01474"></a>
<a id="l01496"></a>
<a id="l01497"></a>
<a id="l01498"></a>
<a id="l01499"></a>
<a id="l01515"></a>
<a id="l01516"></a>
<a id="l01517"></a>
<a id="l01527"></a>
<a id="l01528"></a>
<a id="l01539"></a>
<a id="l01540"></a>
<a id="l01544"></a>
<a id="l01545"></a>
<a id="l01549"></a>
<a id="l01550"></a>
<a id="l01559"></a>
<a id="l01560"></a>
<a id="foldopen01567"></a>
<a id="l01567"></a>
<a id="l01568"></a>
<a id="l01569"></a>
<a id="l01570"></a>
<a id="l01571"></a>
<a id="l01572"></a>
<a id="l01577"></a>
<a id="l01578"></a>
<a id="l01590"></a>
<a id="l01591"></a>
<a id="l01592"></a>
<a id="l01599"></a>
<a id="l01600"></a>
<a id="l01614"></a>
<a id="l01615"></a>
<a id="l01616"></a>
<a id="l01629"></a>
<a id="l01630"></a>
<a id="l01631"></a>
<a id="l01639"></a>
<a id="l01640"></a>
<a id="foldopen01644"></a>
<a id="l01644"></a>
<a id="l01645"></a>
<a id="l01646"></a>
<a id="l01647"></a>
<a id="l01648"></a>
<a id="l01649"></a>
<a id="l01650"></a>
<a id="l01651"></a>
<a id="l01660"></a>
<a id="l01661"></a>
<a id="l01672"></a>
<a id="l01673"></a>
<a id="l01683"></a>
<a id="l01684"></a>
<a id="l01685"></a>
<a id="l01686"></a>
<a id="l01687"></a>
<a id="l01688"></a>
<a id="l01689"></a>
<a id="a__timespec_8h_html_aa17c461cd5eca7fc12a66daa803c7fd7"></a>
<a id="acoap_8h_html"></a>
<a id="agroup__lwm2m__api_html_ga00d29a0c4935fc255e74b8c22ac49de1"></a>
<a id="agroup__lwm2m__api_html_ga026cc9288d2de17ec557e08b9b987ebc"></a>
<a id="agroup__lwm2m__api_html_ga03b72e96a67fcbf85feb5bf0b9df81ce"></a>
<a id="agroup__lwm2m__api_html_ga04a18bd8a4eeea41a47803c16567d67b"></a>
<a id="agroup__lwm2m__api_html_ga077e1abd612d31dd33fab52b7d205c39"></a>
<a id="agroup__lwm2m__api_html_ga0bc84cb39a7a537925ec7d62e54b8b48"></a>
<a id="agroup__lwm2m__api_html_ga0f2b115d231bea6622135d72b51f55ca"></a>
<a id="agroup__lwm2m__api_html_ga1065c729d5caa8ca13de7766fce77953"></a>
<a id="agroup__lwm2m__api_html_ga11de8078091631cb88b26a9a460097ab"></a>
<a id="agroup__lwm2m__api_html_ga12817bfbf0a0cbb742568ee974a1c337"></a>
<a id="agroup__lwm2m__api_html_ga178fea0407a5e98c4f5d5ad69688853a"></a>
<a id="agroup__lwm2m__api_html_ga18fcee379640c0dda32d6e3d14827260"></a>
<a id="agroup__lwm2m__api_html_ga1a4dadb822a8241c5bdf339c21cc57a4"></a>
<a id="agroup__lwm2m__api_html_ga1aa3ff424b7190d0fbd9366626b2685c"></a>
<a id="agroup__lwm2m__api_html_ga1b96848f96bdab9939bb2619d3e1059b"></a>
<a id="agroup__lwm2m__api_html_ga1e4b8ba1b19ac9025dca3c4799bba84a"></a>
<a id="agroup__lwm2m__api_html_ga1f06bb65571efee18db5d061f95399c3"></a>
<a id="agroup__lwm2m__api_html_ga20848e0942882e8c2cc40ee8a48b7bfd"></a>
<a id="agroup__lwm2m__api_html_ga20fc58b25468bf309175db59d67b820b"></a>
<a id="agroup__lwm2m__api_html_ga2426db6720b3f3e15e63022cabae5ece"></a>
<a id="agroup__lwm2m__api_html_ga293904118f972ae387c8aa85a1028b54"></a>
<a id="agroup__lwm2m__api_html_ga29cc5cdd697e94d7379b1fb178487916"></a>
<a id="agroup__lwm2m__api_html_ga2e1d41866b5ea35c5aa29bca9bb43812"></a>
<a id="agroup__lwm2m__api_html_ga31d0f3e40b5e3d608d16a4268b2f1b29"></a>
<a id="agroup__lwm2m__api_html_ga327e086959fc5649a5ef14f1f2943e88"></a>
<a id="agroup__lwm2m__api_html_ga3386d3f2ad8d9713fc2283ed6921c2fc"></a>
<a id="agroup__lwm2m__api_html_ga346d547e02bd53ee83f83b2248449e98"></a>
<a id="agroup__lwm2m__api_html_ga34995e902b63c4d7d37ebd709d88a72a"></a>
<a id="agroup__lwm2m__api_html_ga37261a4b9e54eab3d1d855a084d082aa"></a>
<a id="agroup__lwm2m__api_html_ga38dbaf038426efc75d889c4a0666dac9"></a>
<a id="agroup__lwm2m__api_html_ga3955dca5cd6d67807ed75e61a4d84d84"></a>
<a id="agroup__lwm2m__api_html_ga3afac013b0cf731f9c86dc3791131585"></a>
<a id="agroup__lwm2m__api_html_ga3dd8b38e797173dae902404fb5b7a3f4"></a>
<a id="agroup__lwm2m__api_html_ga41b673986e11748b2ded8e1f8f05e0a7"></a>
<a id="agroup__lwm2m__api_html_ga4bf0bbedf5573ac18a11ac4fced11284"></a>
<a id="agroup__lwm2m__api_html_ga4de941c36cf678e12da6e05c378a92e5"></a>
<a id="agroup__lwm2m__api_html_ga53f5b4c5967e93c7dd224fce8f416265"></a>
<a id="agroup__lwm2m__api_html_ga56a2aecd38baedb5dc17258610c4780d"></a>
<a id="agroup__lwm2m__api_html_ga573e128348fb2f43a33bd09332dd677f"></a>
<a id="agroup__lwm2m__api_html_ga5e531aade0537eb5e3f5756e9287e384"></a>
<a id="agroup__lwm2m__api_html_ga61eb38e42d9e1b3f467c43a324f2fc65"></a>
<a id="agroup__lwm2m__api_html_ga647018abc15cd65c894d9acb6c866486"></a>
<a id="agroup__lwm2m__api_html_ga6878ea0ebb512b19a4fb0859756f51d0"></a>
<a id="agroup__lwm2m__api_html_ga6975c5c4825afaccc52741eb54aca4cb"></a>
<a id="agroup__lwm2m__api_html_ga6acccbcd879901574aceab53a21800fc"></a>
<a id="agroup__lwm2m__api_html_ga6c05640737cfc4da71841a77de128be0"></a>
<a id="agroup__lwm2m__api_html_ga6f4b3e08c7e03cff4bf31e2f2999971e"></a>
<a id="agroup__lwm2m__api_html_ga6f775837e07ba9b0032be8917a593e16"></a>
<a id="agroup__lwm2m__api_html_ga7194ad24842e35130d8af7f5104c0844"></a>
<a id="agroup__lwm2m__api_html_ga7217f33bf705011d91ba66c86a4d5747"></a>
<a id="agroup__lwm2m__api_html_ga7611c1aebb0309ee8340e06dd8ee234d"></a>
<a id="agroup__lwm2m__api_html_ga7a0bb9d5652f7f0fd0cc4a1139be6f37"></a>
<a id="agroup__lwm2m__api_html_ga7a2b93b918257bece819dc44804f27f5"></a>
<a id="agroup__lwm2m__api_html_ga896caab5473eadff860872023d13b6c0"></a>
<a id="agroup__lwm2m__api_html_ga919c7d6f418cda99c77fdaf54ae1a7b0"></a>
<a id="agroup__lwm2m__api_html_ga92d2227f37e7d382bc4f1a7bae21b872"></a>
<a id="agroup__lwm2m__api_html_ga92d7e6d81ef674a6c311e1717c6bf373"></a>
<a id="agroup__lwm2m__api_html_ga9481e570b121404dc1be1ce23d904894"></a>
<a id="agroup__lwm2m__api_html_ga950557bce8c510bcc8b0704e7bc4a9dc"></a>
<a id="agroup__lwm2m__api_html_ga9561c1b8407d888f6fbe1e0ceab1c235"></a>
<a id="agroup__lwm2m__api_html_ga956c4fc742a588b7b8b95ce8481f09bf"></a>
<a id="agroup__lwm2m__api_html_ga971c0636c19fe7f0a6e918622560a750"></a>
<a id="agroup__lwm2m__api_html_ga99d7189efa25881dbcddd99e2a795f1b"></a>
<a id="agroup__lwm2m__api_html_ga9a0cdcc9fc6d37462eddeb54e5d1f87a"></a>
<a id="agroup__lwm2m__api_html_ga9dfd46b8a535b1f28e644dc18f57fd79"></a>
<a id="agroup__lwm2m__api_html_ga9ef21d06bef8a97b7666c0aa7fa753b4"></a>
<a id="agroup__lwm2m__api_html_ga9f72fbd0163b15c48ea09cf7d511e444"></a>
<a id="agroup__lwm2m__api_html_gaa200b524e505f64247f1e7472c5f36d4"></a>
<a id="agroup__lwm2m__api_html_gaaef33bdf3f48fd91abdb50db4d5460f9"></a>
<a id="agroup__lwm2m__api_html_gaaffe06ca9ee5302fb6e26164f250653e"></a>
<a id="agroup__lwm2m__api_html_gab09b62982c34887cdd16c30659d3349a"></a>
<a id="agroup__lwm2m__api_html_gab45cebf6f0b6b70974367ca453d16aeb"></a>
<a id="agroup__lwm2m__api_html_gab4ec7a22d01259b6ba9d3a7b6681e6f0"></a>
<a id="agroup__lwm2m__api_html_gab59370ce4fdc94adb4903f22ab1f95b2"></a>
<a id="agroup__lwm2m__api_html_gabcbca483b310e0c4cd68aef2d9cda0bf"></a>
<a id="agroup__lwm2m__api_html_gabf8726f0438477863423947a7bb77ce2"></a>
<a id="agroup__lwm2m__api_html_gac0b6669d8a19b03eb8b08cbbcdb0c192"></a>
<a id="agroup__lwm2m__api_html_gac374d0559056ddb9cf43deae932fd128"></a>
<a id="agroup__lwm2m__api_html_gac4e4a819e54344657d70ec479eb6ec8d"></a>
<a id="agroup__lwm2m__api_html_gac4e7da0353914601c3ec101415c2e110"></a>
<a id="agroup__lwm2m__api_html_gac56e804962e529799c771d81ac1fd027"></a>
<a id="agroup__lwm2m__api_html_gac69c40474180fe14c3761185b2db1c0c"></a>
<a id="agroup__lwm2m__api_html_gac8d63952ec94ca6cfb1dbe12a6c53bfb"></a>
<a id="agroup__lwm2m__api_html_gaca90ab8960a4ff01d44735dbc0405862"></a>
<a id="agroup__lwm2m__api_html_gacf209563efdc5f3201152088c52d05c3"></a>
<a id="agroup__lwm2m__api_html_gacfeb63db0423e6730ffaa826a87eb262"></a>
<a id="agroup__lwm2m__api_html_gad548ffedcb8328b23eb32476a97be6ee"></a>
<a id="agroup__lwm2m__api_html_gad6e5fd4815f409ad59ad631b03199333"></a>
<a id="agroup__lwm2m__api_html_gad7334f06c3bdb14485597794a417152d"></a>
<a id="agroup__lwm2m__api_html_gad7bea67e16e1e831e0f949dbf83d5afe"></a>
<a id="agroup__lwm2m__api_html_gadd163806d70713d8349a9db484ba88bf"></a>
<a id="agroup__lwm2m__api_html_gadfc00060c0b538ed576b5e3edd7dac80"></a>
<a id="agroup__lwm2m__api_html_gae245a9a1d9456af7e6283b1074944606"></a>
<a id="agroup__lwm2m__api_html_gae7bf50f9abf1b82b76ac3e9175e685ac"></a>
<a id="agroup__lwm2m__api_html_gaeb32bcd4981b4c7bd891f99668ebc0fe"></a>
<a id="agroup__lwm2m__api_html_gaf33bd6a527b6d399f3d92b666ac77dfb"></a>
<a id="agroup__lwm2m__api_html_gaf5394884da53edb28fe4afc92bf40e6a"></a>
<a id="agroup__lwm2m__api_html_gaf921d4bc96090ef8735d90d173feab94"></a>
<a id="agroup__lwm2m__api_html_gafd87e5d975c4d88973ac3e95e4d156ac"></a>
<a id="agroup__lwm2m__api_html_gafdc72844ce0ca417e297d76288155aa4"></a>
<a id="agroup__lwm2m__api_html_gga11de8078091631cb88b26a9a460097aba0d4e9d5160e91fc93e062dfb812edb25"></a>
<a id="agroup__lwm2m__api_html_gga11de8078091631cb88b26a9a460097aba431ac48d7f0fed72ce5ab2c8ea823716"></a>
<a id="agroup__lwm2m__api_html_gga11de8078091631cb88b26a9a460097aba6eef062c9f54bc9698a050c8bb2915ba"></a>
<a id="agroup__lwm2m__api_html_gga11de8078091631cb88b26a9a460097abaefb45683a68002dab267c3fb2e876824"></a>
<a id="agroup__lwm2m__api_html_gga11de8078091631cb88b26a9a460097abaf6bb17f06d89124076810c132005f8d7"></a>
<a id="agroup__lwm2m__api_html_gga20848e0942882e8c2cc40ee8a48b7bfda127cca7752ab3f00d5a4705f815b14b4"></a>
<a id="agroup__lwm2m__api_html_gga20848e0942882e8c2cc40ee8a48b7bfda7a7f1720f39bedba28110fad09939dcd"></a>
<a id="agroup__lwm2m__api_html_gga20848e0942882e8c2cc40ee8a48b7bfda7c0144cafd4f91a76d229b40df9cb82a"></a>
<a id="agroup__lwm2m__api_html_gga7611c1aebb0309ee8340e06dd8ee234da2487ae8e93929bf62fd333cd04c5b915"></a>
<a id="agroup__lwm2m__api_html_gga7611c1aebb0309ee8340e06dd8ee234da76aa03f71f44096d9413b1f5718d9711"></a>
<a id="agroup__lwm2m__api_html_gga7611c1aebb0309ee8340e06dd8ee234daa0f06bc70659598b0f51b3ce8094c6ab"></a>
<a id="agroup__lwm2m__api_html_gga7611c1aebb0309ee8340e06dd8ee234daed676a6deffe2de7c916bb6eb2906100"></a>
<a id="agroup__lwm2m__api_html_ggac8d63952ec94ca6cfb1dbe12a6c53bfba22f4341d713417110d9866b0cbd318e3"></a>
<a id="agroup__lwm2m__api_html_ggac8d63952ec94ca6cfb1dbe12a6c53bfba55494fd6e76f585894e34dc9004fbc9e"></a>
<a id="agroup__lwm2m__api_html_ggac8d63952ec94ca6cfb1dbe12a6c53bfbaab4e1cf0451ba926b90ea21152cac885"></a>
<a id="agroup__lwm2m__api_html_ggac8d63952ec94ca6cfb1dbe12a6c53bfbae3f4af98b52ee191229c660748c7dd6c"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862a32552b56152f9a714675fc6bba3b3d5f"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862a7c7853536c452da2f74e9f43a024fcbe"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862a7c7c3115b6ff16dfa722b6b82c2cd1bc"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862a873a4a3190dc7c24d2518dc8d7268763"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862a8994ea8c025cbbd56adcc050a7e86541"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862a90341c0d9584681f18d1cae91c9f6404"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862a9f53175c5e935f061a83aa1fcfe9f683"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862aac3938a209800a0de0a05b21fab02c13"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862ab48772aeed0ead72f3a9289a618af1cd"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862ac089b900494522de565e36d31ea3b0c4"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862ac30dd8520e591c8e51c74ce1a53cd524"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862ac6703e7d0809cc9cfcdd1cbd48e2318b"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862aca4ebc8d550af02f1891eed1a7b1afcc"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862ae89498cad338b1dc9cbd3b23838bf0b6"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862afd4eda5dee31b18b1da5414481e33525"></a>
<a id="agroup__lwm2m__api_html_ggaca90ab8960a4ff01d44735dbc0405862aff939a86c623ab8258c707361b95aef4"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a99ef1cb2c789827dd5db3886dccf9067"></a>
<a id="alwm2m__path_8h_html"></a>
<a id="amutex_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructcoap__pending_html"></a>
<a id="astructcoap__reply_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructlwm2m__ctx_html"></a>
<a id="astructlwm2m__ctx_html_a1b90780926f3cda2d48dfa8f94b1efd8"></a>
<a id="astructlwm2m__ctx_html_a342cb5a0aaf9e5bc53228d3b0cc0fd43"></a>
<a id="astructlwm2m__ctx_html_a412bd706adcd17ec8c00f1779012a845"></a>
<a id="astructlwm2m__ctx_html_a574b50b9ec4cdfb5fac53a9b6d8c31d5"></a>
<a id="astructlwm2m__ctx_html_a5f17296cd4600b25515e0952dc61ea97"></a>
<a id="astructlwm2m__ctx_html_a6c4c9025a17a3dc3451651cb1f83d575"></a>
<a id="astructlwm2m__ctx_html_a76d92a14bf1729d7b0fee174c51ed4bf"></a>
<a id="astructlwm2m__ctx_html_a8714a3ee6870515631fd75e74644d39c"></a>
<a id="astructlwm2m__ctx_html_a9b56ad9b3f2202d25b8c48f34a898dd3"></a>
<a id="astructlwm2m__ctx_html_aafa787c2b7ea7599c51d9247ea9f1090"></a>
<a id="astructlwm2m__ctx_html_ab01ec6be0effa24dde31363a476eccbb"></a>
<a id="astructlwm2m__ctx_html_ab5fe85963a265f9c059a25138a637e02"></a>
<a id="astructlwm2m__ctx_html_ac6709d32a87ece72c7cdf283c4ff60c0"></a>
<a id="astructlwm2m__ctx_html_ad3d66164415325e7009d1a4c1111f4b3"></a>
<a id="astructlwm2m__ctx_html_ae8d889dafd8df676e76542d5a65a8dfc"></a>
<a id="astructlwm2m__ctx_html_aeb1e3ffc83853f74f2201f582917c2ce"></a>
<a id="astructlwm2m__ctx_html_afed1a599a72f131e4f196848c3e6fe85"></a>
<a id="astructlwm2m__ctx_html_aff084b28e547a81bd71215125c28f705"></a>
<a id="astructlwm2m__ctx_html_aff523bc7473073c917ff1c888da7bece"></a>
<a id="astructlwm2m__obj__path_html"></a>
<a id="astructlwm2m__obj__path_html_a7ae1a626b6f4b4c9cdc3e1a99d644ff2"></a>
<a id="astructlwm2m__obj__path_html_a924d75187c05b64989b6eed69b563c29"></a>
<a id="astructlwm2m__obj__path_html_aaeb8482037aa5d9b389236eb9f3e2984"></a>
<a id="astructlwm2m__obj__path_html_ac52cc68142a270b4bab8edfc7cb8b106"></a>
<a id="astructlwm2m__obj__path_html_ad1cf2b4f67b059e92853a05e2d070bb7"></a>
<a id="astructlwm2m__objlnk_html"></a>
<a id="astructlwm2m__objlnk_html_a67193c8612b3a3d2a6a9685f7d1a0053"></a>
<a id="astructlwm2m__objlnk_html_aa51649798b00bc0bb9887c9739b83d27"></a>
<a id="astructlwm2m__res__item_html"></a>
<a id="astructlwm2m__res__item_html_a7693d039248f61eaed193b131a7f6d5a"></a>
<a id="astructlwm2m__res__item_html_a7edf4cf404d4fae3ba0193fde76a66ff"></a>
<a id="astructlwm2m__res__item_html_ab1aecc059a1f88d84b37131884afbf2f"></a>
<a id="astructlwm2m__time__series__elem_html"></a>
<a id="astructlwm2m__time__series__elem_html_acd00227c551b6ee1960b3881819ef90b"></a>
<a id="astructnet__sockaddr_html"></a>

```c
/*
 * Copyright (c) 2017 Linaro Limited
 * Copyright (c) 2017-2019 Foundries.io
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_LWM2M_H_
#define ZEPHYR_INCLUDE_NET_LWM2M_H_

#include <time.h>
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/sys/mutex.h>
#include <zephyr/net/coap.h>
#include <zephyr/net/lwm2m_path.h>

#ifdef __cplusplus
extern "C" {
#endif


/* clang-format off */
#define LWM2M_OBJECT_SECURITY_ID                0
#define LWM2M_OBJECT_SERVER_ID                  1
#define LWM2M_OBJECT_ACCESS_CONTROL_ID          2
#define LWM2M_OBJECT_DEVICE_ID                  3
#define LWM2M_OBJECT_CONNECTIVITY_MONITORING_ID 4
#define LWM2M_OBJECT_FIRMWARE_ID                5
#define LWM2M_OBJECT_LOCATION_ID                6
#define LWM2M_OBJECT_CONNECTIVITY_STATISTICS_ID 7
#define LWM2M_OBJECT_SOFTWARE_MANAGEMENT_ID     9
#define LWM2M_OBJECT_PORTFOLIO_ID               16
#define LWM2M_OBJECT_BINARYAPPDATACONTAINER_ID  19
#define LWM2M_OBJECT_EVENT_LOG_ID               20
#define LWM2M_OBJECT_OSCORE_ID                  21
#define LWM2M_OBJECT_GATEWAY_ID                 25
/* clang-format on */



/* clang-format off */
#define IPSO_OBJECT_GENERIC_SENSOR_ID       3300
#define IPSO_OBJECT_TEMP_SENSOR_ID          3303
#define IPSO_OBJECT_HUMIDITY_SENSOR_ID      3304
#define IPSO_OBJECT_LIGHT_CONTROL_ID        3311
#define IPSO_OBJECT_ACCELEROMETER_ID        3313
#define IPSO_OBJECT_MAGNETOMETER_ID         3314
#define IPSO_OBJECT_VOLTAGE_SENSOR_ID       3316
#define IPSO_OBJECT_CURRENT_SENSOR_ID       3317
#define IPSO_OBJECT_PRESSURE_ID             3323
#define IPSO_OBJECT_TIME_ID                 3333
#define IPSO_OBJECT_BUZZER_ID               3338
#define IPSO_OBJECT_TIMER_ID                3340
#define IPSO_OBJECT_ONOFF_SWITCH_ID         3342
#define IPSO_OBJECT_PUSH_BUTTON_ID          3347
#define UCIFI_OBJECT_BATTERY_ID             3411
#define IPSO_OBJECT_FILLING_LEVEL_SENSOR_ID 3435
/* clang-format on */


typedef void (*lwm2m_socket_fault_cb_t)(int error);

struct lwm2m_obj_path {
        uint16_t obj_id;
        uint16_t obj_inst_id;
        uint16_t res_id;
        uint16_t res_inst_id;
        uint8_t  level;
};

enum lwm2m_observe_event {
        LWM2M_OBSERVE_EVENT_OBSERVER_ADDED,
        LWM2M_OBSERVE_EVENT_OBSERVER_REMOVED,
        LWM2M_OBSERVE_EVENT_NOTIFY_ACK,
        LWM2M_OBSERVE_EVENT_NOTIFY_TIMEOUT,
};

typedef void (*lwm2m_observe_cb_t)(enum lwm2m_observe_event event, struct lwm2m_obj_path *path,
                                   void *user_data);


struct lwm2m_ctx;

enum lwm2m_rd_client_event {
        LWM2M_RD_CLIENT_EVENT_NONE,
        LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_FAILURE,
        LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_COMPLETE,
        LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_TRANSFER_COMPLETE,
        LWM2M_RD_CLIENT_EVENT_REGISTRATION_FAILURE,
        LWM2M_RD_CLIENT_EVENT_REGISTRATION_COMPLETE,
        LWM2M_RD_CLIENT_EVENT_REG_TIMEOUT,
        LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE,
        LWM2M_RD_CLIENT_EVENT_DEREGISTER_FAILURE,
        LWM2M_RD_CLIENT_EVENT_DISCONNECT,
        LWM2M_RD_CLIENT_EVENT_QUEUE_MODE_RX_OFF,
        LWM2M_RD_CLIENT_EVENT_ENGINE_SUSPENDED,
        LWM2M_RD_CLIENT_EVENT_NETWORK_ERROR,
        LWM2M_RD_CLIENT_EVENT_REG_UPDATE,
        LWM2M_RD_CLIENT_EVENT_DEREGISTER,
        LWM2M_RD_CLIENT_EVENT_SERVER_DISABLED,
};


typedef void (*lwm2m_ctx_event_cb_t)(struct lwm2m_ctx *ctx,
                                     enum lwm2m_rd_client_event event);

typedef int (*lwm2m_set_sockopt_cb_t)(struct lwm2m_ctx *client_ctx);

enum lwm2m_socket_states {
        LWM2M_SOCKET_STATE_ONGOING,
        LWM2M_SOCKET_STATE_ONE_RESPONSE,
        LWM2M_SOCKET_STATE_LAST,
        LWM2M_SOCKET_STATE_NO_DATA,
};

struct lwm2m_ctx {
        union {
                struct net_sockaddr_storage remote_addr_storage;
                /* Use remote_addr_storage instead of remote_addr */
                struct net_sockaddr remote_addr;
        };

        struct coap_pending pendings[CONFIG_LWM2M_ENGINE_MAX_PENDING + 1];
        struct coap_reply replies[CONFIG_LWM2M_ENGINE_MAX_REPLIES + 1];
        sys_slist_t pending_sends;
#if defined(CONFIG_LWM2M_QUEUE_MODE_ENABLED)
        sys_slist_t queued_messages;
#endif
        sys_slist_t observer;
        struct k_mutex lock;

        void *processed_req;

#if defined(CONFIG_LWM2M_DTLS_SUPPORT) || defined(__DOXYGEN__)
        int tls_tag;

        char *desthostname;
        uint16_t desthostnamelen;

        int (*load_credentials)(struct lwm2m_ctx *client_ctx);
#endif
        lwm2m_set_sockopt_cb_t set_socketoptions;

        bool use_dtls;

        bool connection_suspended;

#if defined(CONFIG_LWM2M_QUEUE_MODE_ENABLED) || defined(__DOXYGEN__)
        bool buffer_client_messages;
#endif
        int sec_obj_inst;

        int srv_obj_inst;

        bool bootstrap_mode;

        int sock_fd;

        lwm2m_socket_fault_cb_t fault_cb;

        lwm2m_observe_cb_t observe_cb;

        lwm2m_ctx_event_cb_t event_cb;

        uint8_t validate_buf[CONFIG_LWM2M_ENGINE_VALIDATION_BUFFER_SIZE];

        void (*set_socket_state)(int fd, enum lwm2m_socket_states state);
};

struct lwm2m_time_series_elem {
        time_t t;
        union {
                uint8_t u8;
                uint16_t u16;
                uint32_t u32;
                uint64_t u64;
                int8_t i8;
                int16_t i16;
                int32_t i32;
                int64_t i64;
                time_t time;
                double f;
                bool b;
        };
};

typedef bool (*lwm2m_cache_filter_cb_t)(const struct lwm2m_obj_path *path,
                                        const struct lwm2m_time_series_elem *element);

typedef void *(*lwm2m_engine_get_data_cb_t)(uint16_t obj_inst_id,
                                            uint16_t res_id,
                                            uint16_t res_inst_id,
                                            size_t *data_len);

typedef int (*lwm2m_engine_set_data_cb_t)(uint16_t obj_inst_id,
                                          uint16_t res_id, uint16_t res_inst_id,
                                          uint8_t *data, uint16_t data_len,
                                          bool last_block, size_t total_size, size_t offset);

typedef int (*lwm2m_engine_user_cb_t)(uint16_t obj_inst_id);

typedef int (*lwm2m_engine_execute_cb_t)(uint16_t obj_inst_id,
                                         uint8_t *args, uint16_t args_len);

#define LWM2M_DEVICE_PWR_SRC_TYPE_DC_POWER      0
#define LWM2M_DEVICE_PWR_SRC_TYPE_BAT_INT       1
#define LWM2M_DEVICE_PWR_SRC_TYPE_BAT_EXT       2
#define LWM2M_DEVICE_PWR_SRC_TYPE_FUEL_CELL     3
#define LWM2M_DEVICE_PWR_SRC_TYPE_PWR_OVER_ETH  4
#define LWM2M_DEVICE_PWR_SRC_TYPE_USB           5
#define LWM2M_DEVICE_PWR_SRC_TYPE_AC_POWER      6
#define LWM2M_DEVICE_PWR_SRC_TYPE_SOLAR         7
#define LWM2M_DEVICE_PWR_SRC_TYPE_MAX           8

#define LWM2M_DEVICE_ERROR_NONE                 0
#define LWM2M_DEVICE_ERROR_LOW_POWER            1
#define LWM2M_DEVICE_ERROR_EXT_POWER_SUPPLY_OFF 2
#define LWM2M_DEVICE_ERROR_GPS_FAILURE          3
#define LWM2M_DEVICE_ERROR_LOW_SIGNAL_STRENGTH  4
#define LWM2M_DEVICE_ERROR_OUT_OF_MEMORY        5
#define LWM2M_DEVICE_ERROR_SMS_FAILURE          6
#define LWM2M_DEVICE_ERROR_NETWORK_FAILURE      7
#define LWM2M_DEVICE_ERROR_PERIPHERAL_FAILURE   8


#define LWM2M_DEVICE_BATTERY_STATUS_NORMAL      0
#define LWM2M_DEVICE_BATTERY_STATUS_CHARGING    1
#define LWM2M_DEVICE_BATTERY_STATUS_CHARGE_COMP 2
#define LWM2M_DEVICE_BATTERY_STATUS_DAMAGED     3
#define LWM2M_DEVICE_BATTERY_STATUS_LOW         4
#define LWM2M_DEVICE_BATTERY_STATUS_NOT_INST    5
#define LWM2M_DEVICE_BATTERY_STATUS_UNKNOWN     6


int lwm2m_device_add_err(uint8_t error_code);



#define STATE_IDLE              0
#define STATE_DOWNLOADING       1
#define STATE_DOWNLOADED        2
#define STATE_UPDATING          3



#define RESULT_DEFAULT          0
#define RESULT_SUCCESS          1
#define RESULT_NO_STORAGE       2
#define RESULT_OUT_OF_MEM       3
#define RESULT_CONNECTION_LOST  4
#define RESULT_INTEGRITY_FAILED 5
#define RESULT_UNSUP_FW         6
#define RESULT_INVALID_URI      7
#define RESULT_UPDATE_FAILED    8
#define RESULT_UNSUP_PROTO      9


#if defined(CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT) || defined(__DOXYGEN__)
void lwm2m_firmware_set_write_cb(lwm2m_engine_set_data_cb_t cb);

lwm2m_engine_set_data_cb_t lwm2m_firmware_get_write_cb(void);

void lwm2m_firmware_set_write_cb_inst(uint16_t obj_inst_id, lwm2m_engine_set_data_cb_t cb);

lwm2m_engine_set_data_cb_t lwm2m_firmware_get_write_cb_inst(uint16_t obj_inst_id);

void lwm2m_firmware_set_cancel_cb(lwm2m_engine_user_cb_t cb);

lwm2m_engine_user_cb_t lwm2m_firmware_get_cancel_cb(void);

void lwm2m_firmware_set_cancel_cb_inst(uint16_t obj_inst_id, lwm2m_engine_user_cb_t cb);

lwm2m_engine_user_cb_t lwm2m_firmware_get_cancel_cb_inst(uint16_t obj_inst_id);

void lwm2m_firmware_set_update_cb(lwm2m_engine_execute_cb_t cb);

lwm2m_engine_execute_cb_t lwm2m_firmware_get_update_cb(void);

void lwm2m_firmware_set_update_cb_inst(uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb);

lwm2m_engine_execute_cb_t lwm2m_firmware_get_update_cb_inst(uint16_t obj_inst_id);
#endif

#if defined(CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT) || defined(__DOXYGEN__)

int lwm2m_swmgmt_set_activate_cb(uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb);

int lwm2m_swmgmt_set_deactivate_cb(uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb);

int lwm2m_swmgmt_set_install_package_cb(uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb);

int lwm2m_swmgmt_set_delete_package_cb(uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb);

int lwm2m_swmgmt_set_read_package_version_cb(uint16_t obj_inst_id, lwm2m_engine_get_data_cb_t cb);

int lwm2m_swmgmt_set_write_package_cb(uint16_t obj_inst_id, lwm2m_engine_set_data_cb_t cb);

int lwm2m_swmgmt_install_completed(uint16_t obj_inst_id, int error_code);

#endif

#if defined(CONFIG_LWM2M_EVENT_LOG_OBJ_SUPPORT) || defined(__DOXYGEN__)

void lwm2m_event_log_set_read_log_data_cb(lwm2m_engine_get_data_cb_t cb);

#endif

#define LWM2M_OBJLNK_MAX_ID USHRT_MAX

struct lwm2m_objlnk {
        uint16_t obj_id;
        uint16_t obj_inst;
};

int lwm2m_update_observer_min_period(struct lwm2m_ctx *client_ctx,
                                     const struct lwm2m_obj_path *path, uint32_t period_s);

int lwm2m_update_observer_max_period(struct lwm2m_ctx *client_ctx,
                                     const struct lwm2m_obj_path *path, uint32_t period_s);

int lwm2m_create_object_inst(const struct lwm2m_obj_path *path);

int lwm2m_delete_object_inst(const struct lwm2m_obj_path *path);

void lwm2m_registry_lock(void);

void lwm2m_registry_unlock(void);

int lwm2m_set_opaque(const struct lwm2m_obj_path *path, const char *data_ptr, uint16_t data_len);

int lwm2m_set_string(const struct lwm2m_obj_path *path, const char *data_ptr);

int lwm2m_set_u8(const struct lwm2m_obj_path *path, uint8_t value);

int lwm2m_set_u16(const struct lwm2m_obj_path *path, uint16_t value);

int lwm2m_set_u32(const struct lwm2m_obj_path *path, uint32_t value);

int lwm2m_set_s8(const struct lwm2m_obj_path *path, int8_t value);

int lwm2m_set_s16(const struct lwm2m_obj_path *path, int16_t value);

int lwm2m_set_s32(const struct lwm2m_obj_path *path, int32_t value);

int lwm2m_set_s64(const struct lwm2m_obj_path *path, int64_t value);

int lwm2m_set_bool(const struct lwm2m_obj_path *path, bool value);

int lwm2m_set_f64(const struct lwm2m_obj_path *path, const double value);

int lwm2m_set_objlnk(const struct lwm2m_obj_path *path, const struct lwm2m_objlnk *value);

int lwm2m_set_time(const struct lwm2m_obj_path *path, time_t value);

struct lwm2m_res_item {
        struct lwm2m_obj_path *path;
        void *value;
        uint16_t size;
};

int lwm2m_set_bulk(const struct lwm2m_res_item res_list[], size_t res_list_size);

int lwm2m_get_opaque(const struct lwm2m_obj_path *path, void *buf, uint16_t buflen);

int lwm2m_get_string(const struct lwm2m_obj_path *path, void *str, uint16_t buflen);

int lwm2m_get_u8(const struct lwm2m_obj_path *path, uint8_t *value);

int lwm2m_get_u16(const struct lwm2m_obj_path *path, uint16_t *value);

int lwm2m_get_u32(const struct lwm2m_obj_path *path, uint32_t *value);

int lwm2m_get_s8(const struct lwm2m_obj_path *path, int8_t *value);

int lwm2m_get_s16(const struct lwm2m_obj_path *path, int16_t *value);

int lwm2m_get_s32(const struct lwm2m_obj_path *path, int32_t *value);

int lwm2m_get_s64(const struct lwm2m_obj_path *path, int64_t *value);

int lwm2m_get_bool(const struct lwm2m_obj_path *path, bool *value);

int lwm2m_get_f64(const struct lwm2m_obj_path *path, double *value);

int lwm2m_get_objlnk(const struct lwm2m_obj_path *path, struct lwm2m_objlnk *buf);

int lwm2m_get_time(const struct lwm2m_obj_path *path, time_t *buf);

int lwm2m_register_read_callback(const struct lwm2m_obj_path *path, lwm2m_engine_get_data_cb_t cb);

int lwm2m_register_pre_write_callback(const struct lwm2m_obj_path *path,
                                      lwm2m_engine_get_data_cb_t cb);

int lwm2m_register_validate_callback(const struct lwm2m_obj_path *path,
                                     lwm2m_engine_set_data_cb_t cb);

int lwm2m_register_post_write_callback(const struct lwm2m_obj_path *path,
                                       lwm2m_engine_set_data_cb_t cb);

int lwm2m_register_exec_callback(const struct lwm2m_obj_path *path, lwm2m_engine_execute_cb_t cb);

int lwm2m_register_create_callback(uint16_t obj_id,
                                   lwm2m_engine_user_cb_t cb);

int lwm2m_register_delete_callback(uint16_t obj_id,
                                          lwm2m_engine_user_cb_t cb);

#define LWM2M_RES_DATA_READ_ONLY        0

#define LWM2M_RES_DATA_FLAG_RO          BIT(LWM2M_RES_DATA_READ_ONLY)

#define LWM2M_HAS_RES_FLAG(res, f)      ((res->data_flags & f) == f)

int lwm2m_set_res_buf(const struct lwm2m_obj_path *path, void *buffer_ptr, uint16_t buffer_len,
                      uint16_t data_len, uint8_t data_flags);

int lwm2m_set_res_data_len(const struct lwm2m_obj_path *path, uint16_t data_len);

int lwm2m_get_res_buf(const struct lwm2m_obj_path *path, void **buffer_ptr, uint16_t *buffer_len,
                      uint16_t *data_len, uint8_t *data_flags);

int lwm2m_create_res_inst(const struct lwm2m_obj_path *path);

int lwm2m_delete_res_inst(const struct lwm2m_obj_path *path);

int lwm2m_update_device_service_period(uint32_t period_ms);

bool lwm2m_path_is_observed(const struct lwm2m_obj_path *path);

int lwm2m_engine_stop(struct lwm2m_ctx *client_ctx);

int lwm2m_engine_start(struct lwm2m_ctx *client_ctx);

void lwm2m_acknowledge(struct lwm2m_ctx *client_ctx);

/*
 * LwM2M RD client flags, used to configure LwM2M session.
 */

#define LWM2M_RD_CLIENT_FLAG_BOOTSTRAP BIT(0)

int lwm2m_rd_client_start(struct lwm2m_ctx *client_ctx, const char *ep_name,
                           uint32_t flags, lwm2m_ctx_event_cb_t event_cb,
                           lwm2m_observe_cb_t observe_cb);

int lwm2m_rd_client_stop(struct lwm2m_ctx *client_ctx,
                          lwm2m_ctx_event_cb_t event_cb, bool deregister);

int lwm2m_engine_pause(void);

int lwm2m_engine_resume(void);

void lwm2m_rd_client_update(void);

#define LWM2M_MAX_PATH_STR_SIZE sizeof("/65535/65535/65535/65535")

char *lwm2m_path_log_buf(char *buf, struct lwm2m_obj_path *path);

enum lwm2m_send_status {
        LWM2M_SEND_STATUS_SUCCESS,
        LWM2M_SEND_STATUS_FAILURE,
        LWM2M_SEND_STATUS_TIMEOUT,
};

typedef void (*lwm2m_send_cb_t)(enum lwm2m_send_status status);

int lwm2m_send_cb(struct lwm2m_ctx *ctx, const struct lwm2m_obj_path path_list[],
                          uint8_t path_list_size, lwm2m_send_cb_t reply_cb);

struct lwm2m_ctx *lwm2m_rd_client_ctx(void);

int lwm2m_enable_cache(const struct lwm2m_obj_path *path, struct lwm2m_time_series_elem *data_cache,
                       size_t cache_len);

int lwm2m_set_cache_filter(const struct lwm2m_obj_path *path,
                           lwm2m_cache_filter_cb_t filter_cb);

int lwm2m_cache_free_slots_get(const struct lwm2m_obj_path *path);

enum lwm2m_security_mode_e {
        LWM2M_SECURITY_PSK = 0,
        LWM2M_SECURITY_RAW_PK = 1,
        LWM2M_SECURITY_CERT = 2,
        LWM2M_SECURITY_NOSEC = 3,
        LWM2M_SECURITY_CERT_EST = 4,
};

int lwm2m_security_mode(struct lwm2m_ctx *ctx);

int lwm2m_set_default_sockopt(struct lwm2m_ctx *ctx);

void lwm2m_pull_context_set_sockopt_callback(lwm2m_set_sockopt_cb_t set_sockopt_cb);

#ifdef __cplusplus
}
#endif

#endif  /* ZEPHYR_INCLUDE_NET_LWM2M_H_ */
```

## 40.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Linaro Limited。

版权（Copyright）：© 2017-2019 Foundries.io。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 47 行

关闭 clang-format 自动排版（clang-format off）。

### 注释 3：原第 62 行

开启 clang-format 自动排版（clang-format on）。

### 注释 4：原第 74 行

关闭 clang-format 自动排版（clang-format off）。

### 注释 5：原第 91 行

开启 clang-format 自动排版（clang-format on）。

### 注释 6：原第 216 行

使用 `remote_addr_storage` 代替 `remote_addr`。

### 注释 7：原第 1466 行

LwM2M RD 客户端标志，用于配置 LwM2M 会话。

### 注释 8：原第 1689 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_LWM2M_H_`。

## 40.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/sys/mutex.h](../userspace_sync_reference/P005_用户模式互斥量头文件参考.md)
- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)
- [zephyr/net/lwm2m_path.h](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__path_8h.html)
- [lwm2m_socket_fault_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae7bf50f9abf1b82b76ac3e9175e685ac)
- [lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [obj_id](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md#ad1cf2b4f67b059e92853a05e2d070bb7)
- [obj_inst_id](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md#a7ae1a626b6f4b4c9cdc3e1a99d644ff2)
- [res_id](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md#ac52cc68142a270b4bab8edfc7cb8b106)
- [res_inst_id](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md#a924d75187c05b64989b6eed69b563c29)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [level](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md#aaeb8482037aa5d9b389236eb9f3e2984)
- [lwm2m_observe_event](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac8d63952ec94ca6cfb1dbe12a6c53bfb)
- [LWM2M_OBSERVE_EVENT_OBSERVER_ADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggac8d63952ec94ca6cfb1dbe12a6c53bfba22f4341d713417110d9866b0cbd318e3)
- [LWM2M_OBSERVE_EVENT_OBSERVER_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggac8d63952ec94ca6cfb1dbe12a6c53bfbae3f4af98b52ee191229c660748c7dd6c)
- [LWM2M_OBSERVE_EVENT_NOTIFY_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggac8d63952ec94ca6cfb1dbe12a6c53bfbaab4e1cf0451ba926b90ea21152cac885)
- [LWM2M_OBSERVE_EVENT_NOTIFY_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggac8d63952ec94ca6cfb1dbe12a6c53bfba55494fd6e76f585894e34dc9004fbc9e)
- [lwm2m_observe_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad7bea67e16e1e831e0f949dbf83d5afe)
- [lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)
- [lwm2m_rd_client_event](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaca90ab8960a4ff01d44735dbc0405862)
- [LWM2M_RD_CLIENT_EVENT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862aca4ebc8d550af02f1891eed1a7b1afcc)
- [LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ac089b900494522de565e36d31ea3b0c4)
- [LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ac30dd8520e591c8e51c74ce1a53cd524)
- [LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_TRANSFER_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a7c7c3115b6ff16dfa722b6b82c2cd1bc)
- [LWM2M_RD_CLIENT_EVENT_REGISTRATION_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ae89498cad338b1dc9cbd3b23838bf0b6)
- [LWM2M_RD_CLIENT_EVENT_REGISTRATION_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a8994ea8c025cbbd56adcc050a7e86541)
- [LWM2M_RD_CLIENT_EVENT_REG_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a90341c0d9584681f18d1cae91c9f6404)
- [LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a9f53175c5e935f061a83aa1fcfe9f683)
- [LWM2M_RD_CLIENT_EVENT_DEREGISTER_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a32552b56152f9a714675fc6bba3b3d5f)
- [LWM2M_RD_CLIENT_EVENT_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ac6703e7d0809cc9cfcdd1cbd48e2318b)
- [LWM2M_RD_CLIENT_EVENT_QUEUE_MODE_RX_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a7c7853536c452da2f74e9f43a024fcbe)
- [LWM2M_RD_CLIENT_EVENT_ENGINE_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862afd4eda5dee31b18b1da5414481e33525)
- [LWM2M_RD_CLIENT_EVENT_NETWORK_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862aff939a86c623ab8258c707361b95aef4)
- [LWM2M_RD_CLIENT_EVENT_REG_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ab48772aeed0ead72f3a9289a618af1cd)
- [LWM2M_RD_CLIENT_EVENT_DEREGISTER](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862aac3938a209800a0de0a05b21fab02c13)
- [LWM2M_RD_CLIENT_EVENT_SERVER_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a873a4a3190dc7c24d2518dc8d7268763)
- [lwm2m_ctx_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga38dbaf038426efc75d889c4a0666dac9)
- [lwm2m_set_sockopt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga92d2227f37e7d382bc4f1a7bae21b872)
- [lwm2m_socket_states](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7611c1aebb0309ee8340e06dd8ee234d)
- [LWM2M_SOCKET_STATE_ONGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga7611c1aebb0309ee8340e06dd8ee234daa0f06bc70659598b0f51b3ce8094c6ab)
- [LWM2M_SOCKET_STATE_ONE_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga7611c1aebb0309ee8340e06dd8ee234da76aa03f71f44096d9413b1f5718d9711)
- [LWM2M_SOCKET_STATE_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga7611c1aebb0309ee8340e06dd8ee234daed676a6deffe2de7c916bb6eb2906100)
- [LWM2M_SOCKET_STATE_NO_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga7611c1aebb0309ee8340e06dd8ee234da2487ae8e93929bf62fd333cd04c5b915)
- [remote_addr_storage](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#ae8d889dafd8df676e76542d5a65a8dfc)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)
- [coap_reply](../network_application_model_reference/P015_coap_reply_结构体.md)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [processed_req](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a9b56ad9b3f2202d25b8c48f34a898dd3)
- [tls_tag](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a6c4c9025a17a3dc3451651cb1f83d575)
- [desthostname](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a342cb5a0aaf9e5bc53228d3b0cc0fd43)
- [desthostnamelen](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#aff084b28e547a81bd71215125c28f705)
- [load_credentials](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a5f17296cd4600b25515e0952dc61ea97)
- [set_socketoptions](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a8714a3ee6870515631fd75e74644d39c)
- [use_dtls](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#aeb1e3ffc83853f74f2201f582917c2ce)
- [connection_suspended](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#aff523bc7473073c917ff1c888da7bece)
- [buffer_client_messages](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#ac6709d32a87ece72c7cdf283c4ff60c0)
- [sec_obj_inst](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#ab5fe85963a265f9c059a25138a637e02)
- [srv_obj_inst](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a76d92a14bf1729d7b0fee174c51ed4bf)
- [bootstrap_mode](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#aafa787c2b7ea7599c51d9247ea9f1090)
- [sock_fd](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#afed1a599a72f131e4f196848c3e6fe85)
- [fault_cb](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a1b90780926f3cda2d48dfa8f94b1efd8)
- [observe_cb](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a412bd706adcd17ec8c00f1779012a845)
- [event_cb](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#ab01ec6be0effa24dde31363a476eccbb)
- [validate_buf](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a574b50b9ec4cdfb5fac53a9b6d8c31d5)
- [set_socket_state](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#ad3d66164415325e7009d1a4c1111f4b3)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [lwm2m_time_series_elem](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [t](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md#acd00227c551b6ee1960b3881819ef90b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [time](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a99ef1cb2c789827dd5db3886dccf9067)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [lwm2m_cache_filter_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7a0bb9d5652f7f0fd0cc4a1139be6f37)
- [lwm2m_engine_set_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3afac013b0cf731f9c86dc3791131585)
- [lwm2m_engine_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabcbca483b310e0c4cd68aef2d9cda0bf)
- [lwm2m_engine_execute_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb32bcd4981b4c7bd891f99668ebc0fe)
- [lwm2m_device_add_err](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabf8726f0438477863423947a7bb77ce2)
- [lwm2m_firmware_set_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6878ea0ebb512b19a4fb0859756f51d0)
- [lwm2m_firmware_get_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4bf0bbedf5573ac18a11ac4fced11284)
- [lwm2m_firmware_set_write_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac4e4a819e54344657d70ec479eb6ec8d)
- [lwm2m_firmware_get_write_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad7334f06c3bdb14485597794a417152d)
- [lwm2m_firmware_set_cancel_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3955dca5cd6d67807ed75e61a4d84d84)
- [lwm2m_firmware_get_cancel_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9561c1b8407d888f6fbe1e0ceab1c235)
- [lwm2m_firmware_set_cancel_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaa200b524e505f64247f1e7472c5f36d4)
- [lwm2m_firmware_get_cancel_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6f4b3e08c7e03cff4bf31e2f2999971e)
- [lwm2m_firmware_set_update_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga61eb38e42d9e1b3f467c43a324f2fc65)
- [lwm2m_firmware_get_update_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1e4b8ba1b19ac9025dca3c4799bba84a)
- [lwm2m_firmware_set_update_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga31d0f3e40b5e3d608d16a4268b2f1b29)
- [lwm2m_firmware_get_update_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga34995e902b63c4d7d37ebd709d88a72a)
- [lwm2m_swmgmt_set_activate_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac374d0559056ddb9cf43deae932fd128)
- [lwm2m_swmgmt_set_deactivate_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7a2b93b918257bece819dc44804f27f5)
- [lwm2m_swmgmt_set_install_package_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gadfc00060c0b538ed576b5e3edd7dac80)
- [lwm2m_swmgmt_set_delete_package_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gacf209563efdc5f3201152088c52d05c3)
- [lwm2m_swmgmt_set_read_package_version_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab59370ce4fdc94adb4903f22ab1f95b2)
- [lwm2m_engine_get_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga5e531aade0537eb5e3f5756e9287e384)
- [lwm2m_swmgmt_set_write_package_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga293904118f972ae387c8aa85a1028b54)
- [lwm2m_swmgmt_install_completed](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga573e128348fb2f43a33bd09332dd677f)
- [lwm2m_event_log_set_read_log_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga950557bce8c510bcc8b0704e7bc4a9dc)
- [lwm2m_objlnk](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md)
- [obj_id](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md#a67193c8612b3a3d2a6a9685f7d1a0053)
- [obj_inst](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md#aa51649798b00bc0bb9887c9739b83d27)
- [lwm2m_update_observer_min_period](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gadd163806d70713d8349a9db484ba88bf)
- [lwm2m_update_observer_max_period](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6acccbcd879901574aceab53a21800fc)
- [lwm2m_create_object_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga53f5b4c5967e93c7dd224fce8f416265)
- [lwm2m_delete_object_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf921d4bc96090ef8735d90d173feab94)
- [lwm2m_registry_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9a0cdcc9fc6d37462eddeb54e5d1f87a)
- [lwm2m_registry_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab09b62982c34887cdd16c30659d3349a)
- [lwm2m_set_opaque](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaaef33bdf3f48fd91abdb50db4d5460f9)
- [lwm2m_set_string](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7217f33bf705011d91ba66c86a4d5747)
- [lwm2m_set_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1aa3ff424b7190d0fbd9366626b2685c)
- [lwm2m_set_u16](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1f06bb65571efee18db5d061f95399c3)
- [lwm2m_set_u32](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9481e570b121404dc1be1ce23d904894)
- [lwm2m_set_s8](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga37261a4b9e54eab3d1d855a084d082aa)
- [lwm2m_set_s16](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad548ffedcb8328b23eb32476a97be6ee)
- [lwm2m_set_s32](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga327e086959fc5649a5ef14f1f2943e88)
- [lwm2m_set_s64](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga18fcee379640c0dda32d6e3d14827260)
- [lwm2m_set_bool](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9ef21d06bef8a97b7666c0aa7fa753b4)
- [lwm2m_set_f64](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3386d3f2ad8d9713fc2283ed6921c2fc)
- [lwm2m_set_objlnk](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga04a18bd8a4eeea41a47803c16567d67b)
- [lwm2m_set_time](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7194ad24842e35130d8af7f5104c0844)
- [lwm2m_res_item](../network_application_model_reference/P050_lwm2m_res_item_结构体.md)
- [path](../network_application_model_reference/P050_lwm2m_res_item_结构体.md#ab1aecc059a1f88d84b37131884afbf2f)
- [value](../network_application_model_reference/P050_lwm2m_res_item_结构体.md#a7edf4cf404d4fae3ba0193fde76a66ff)
- [size](../network_application_model_reference/P050_lwm2m_res_item_结构体.md#a7693d039248f61eaed193b131a7f6d5a)
- [lwm2m_set_bulk](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga41b673986e11748b2ded8e1f8f05e0a7)
- [lwm2m_get_opaque](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae245a9a1d9456af7e6283b1074944606)
- [lwm2m_get_string](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga20fc58b25468bf309175db59d67b820b)
- [lwm2m_get_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac56e804962e529799c771d81ac1fd027)
- [lwm2m_get_u16](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1b96848f96bdab9939bb2619d3e1059b)
- [lwm2m_get_u32](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga0bc84cb39a7a537925ec7d62e54b8b48)
- [lwm2m_get_s8](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga12817bfbf0a0cbb742568ee974a1c337)
- [lwm2m_get_s16](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga2426db6720b3f3e15e63022cabae5ece)
- [lwm2m_get_s32](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga99d7189efa25881dbcddd99e2a795f1b)
- [lwm2m_get_s64](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaaffe06ca9ee5302fb6e26164f250653e)
- [lwm2m_get_bool](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gafdc72844ce0ca417e297d76288155aa4)
- [lwm2m_get_f64](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga03b72e96a67fcbf85feb5bf0b9df81ce)
- [lwm2m_get_objlnk](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4de941c36cf678e12da6e05c378a92e5)
- [lwm2m_get_time](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga2e1d41866b5ea35c5aa29bca9bb43812)
- [lwm2m_register_read_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf33bd6a527b6d399f3d92b666ac77dfb)
- [lwm2m_register_pre_write_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6f775837e07ba9b0032be8917a593e16)
- [lwm2m_register_validate_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad6e5fd4815f409ad59ad631b03199333)
- [lwm2m_register_post_write_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3dd8b38e797173dae902404fb5b7a3f4)
- [lwm2m_register_exec_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga29cc5cdd697e94d7379b1fb178487916)
- [lwm2m_register_create_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga346d547e02bd53ee83f83b2248449e98)
- [lwm2m_register_delete_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga92d7e6d81ef674a6c311e1717c6bf373)
- [lwm2m_set_res_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga56a2aecd38baedb5dc17258610c4780d)
- [lwm2m_set_res_data_len](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga0f2b115d231bea6622135d72b51f55ca)
- [lwm2m_get_res_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac0b6669d8a19b03eb8b08cbbcdb0c192)
- [lwm2m_create_res_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac69c40474180fe14c3761185b2db1c0c)
- [lwm2m_delete_res_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gacfeb63db0423e6730ffaa826a87eb262)
- [lwm2m_update_device_service_period](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab45cebf6f0b6b70974367ca453d16aeb)
- [lwm2m_path_is_observed](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1065c729d5caa8ca13de7766fce77953)
- [lwm2m_engine_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga077e1abd612d31dd33fab52b7d205c39)
- [lwm2m_engine_start](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9f72fbd0163b15c48ea09cf7d511e444)
- [lwm2m_acknowledge](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga919c7d6f418cda99c77fdaf54ae1a7b0)
- [lwm2m_rd_client_start](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9dfd46b8a535b1f28e644dc18f57fd79)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [lwm2m_rd_client_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gafd87e5d975c4d88973ac3e95e4d156ac)
- [lwm2m_engine_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1a4dadb822a8241c5bdf339c21cc57a4)
- [lwm2m_engine_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga178fea0407a5e98c4f5d5ad69688853a)
- [lwm2m_rd_client_update](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab4ec7a22d01259b6ba9d3a7b6681e6f0)
- [lwm2m_path_log_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga971c0636c19fe7f0a6e918622560a750)
- [lwm2m_send_status](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga20848e0942882e8c2cc40ee8a48b7bfd)
- [LWM2M_SEND_STATUS_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga20848e0942882e8c2cc40ee8a48b7bfda127cca7752ab3f00d5a4705f815b14b4)
- [LWM2M_SEND_STATUS_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga20848e0942882e8c2cc40ee8a48b7bfda7a7f1720f39bedba28110fad09939dcd)
- [LWM2M_SEND_STATUS_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga20848e0942882e8c2cc40ee8a48b7bfda7c0144cafd4f91a76d229b40df9cb82a)
- [lwm2m_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf5394884da53edb28fe4afc92bf40e6a)
- [lwm2m_send_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga026cc9288d2de17ec557e08b9b987ebc)
- [lwm2m_rd_client_ctx](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga896caab5473eadff860872023d13b6c0)
- [lwm2m_enable_cache](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6975c5c4825afaccc52741eb54aca4cb)
- [lwm2m_set_cache_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac4e7da0353914601c3ec101415c2e110)
- [lwm2m_cache_free_slots_get](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga00d29a0c4935fc255e74b8c22ac49de1)
- [lwm2m_security_mode_e](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga11de8078091631cb88b26a9a460097ab)
- [LWM2M_SECURITY_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097aba0d4e9d5160e91fc93e062dfb812edb25)
- [LWM2M_SECURITY_RAW_PK](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097aba431ac48d7f0fed72ce5ab2c8ea823716)
- [LWM2M_SECURITY_CERT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097aba6eef062c9f54bc9698a050c8bb2915ba)
- [LWM2M_SECURITY_NOSEC](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097abaf6bb17f06d89124076810c132005f8d7)
- [LWM2M_SECURITY_CERT_EST](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097abaefb45683a68002dab267c3fb2e876824)
- [lwm2m_security_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6c05640737cfc4da71841a77de128be0)
- [lwm2m_set_default_sockopt](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga956c4fc742a588b7b8b95ce8481f09bf)
- [lwm2m_pull_context_set_sockopt_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga647018abc15cd65c894d9acb6c866486)
- [coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [lwm2m_path.h](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__path_8h.html)
- [mutex.h](../userspace_sync_reference/P005_用户模式互斥量头文件参考.md)
- [lwm2m_ctx::fault_cb](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a1b90780926f3cda2d48dfa8f94b1efd8)
- [lwm2m_ctx::desthostname](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a342cb5a0aaf9e5bc53228d3b0cc0fd43)
- [lwm2m_ctx::observe_cb](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a412bd706adcd17ec8c00f1779012a845)
- [lwm2m_ctx::validate_buf](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a574b50b9ec4cdfb5fac53a9b6d8c31d5)
- [lwm2m_ctx::load_credentials](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a5f17296cd4600b25515e0952dc61ea97)
- [lwm2m_ctx::tls_tag](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a6c4c9025a17a3dc3451651cb1f83d575)
- [lwm2m_ctx::srv_obj_inst](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a76d92a14bf1729d7b0fee174c51ed4bf)
- [lwm2m_ctx::set_socketoptions](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a8714a3ee6870515631fd75e74644d39c)
- [lwm2m_ctx::processed_req](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a9b56ad9b3f2202d25b8c48f34a898dd3)
- [lwm2m_ctx::bootstrap_mode](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#aafa787c2b7ea7599c51d9247ea9f1090)
- [lwm2m_ctx::event_cb](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#ab01ec6be0effa24dde31363a476eccbb)
- [lwm2m_ctx::sec_obj_inst](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#ab5fe85963a265f9c059a25138a637e02)
- [lwm2m_ctx::buffer_client_messages](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#ac6709d32a87ece72c7cdf283c4ff60c0)
- [lwm2m_ctx::set_socket_state](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#ad3d66164415325e7009d1a4c1111f4b3)
- [lwm2m_ctx::remote_addr_storage](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#ae8d889dafd8df676e76542d5a65a8dfc)
- [lwm2m_ctx::use_dtls](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#aeb1e3ffc83853f74f2201f582917c2ce)
- [lwm2m_ctx::sock_fd](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#afed1a599a72f131e4f196848c3e6fe85)
- [lwm2m_ctx::desthostnamelen](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#aff084b28e547a81bd71215125c28f705)
- [lwm2m_ctx::connection_suspended](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#aff523bc7473073c917ff1c888da7bece)
- [lwm2m_obj_path::obj_inst_id](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md#a7ae1a626b6f4b4c9cdc3e1a99d644ff2)
- [lwm2m_obj_path::res_inst_id](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md#a924d75187c05b64989b6eed69b563c29)
- [lwm2m_obj_path::level](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md#aaeb8482037aa5d9b389236eb9f3e2984)
- [lwm2m_obj_path::res_id](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md#ac52cc68142a270b4bab8edfc7cb8b106)
- [lwm2m_obj_path::obj_id](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md#ad1cf2b4f67b059e92853a05e2d070bb7)
- [lwm2m_objlnk::obj_id](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md#a67193c8612b3a3d2a6a9685f7d1a0053)
- [lwm2m_objlnk::obj_inst](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md#aa51649798b00bc0bb9887c9739b83d27)
- [lwm2m_res_item::size](../network_application_model_reference/P050_lwm2m_res_item_结构体.md#a7693d039248f61eaed193b131a7f6d5a)
- [lwm2m_res_item::value](../network_application_model_reference/P050_lwm2m_res_item_结构体.md#a7edf4cf404d4fae3ba0193fde76a66ff)
- [lwm2m_res_item::path](../network_application_model_reference/P050_lwm2m_res_item_结构体.md#ab1aecc059a1f88d84b37131884afbf2f)
- [lwm2m_time_series_elem::t](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md#acd00227c551b6ee1960b3881819ef90b)

---

[上一章](P039_limits.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P041_mcux_lpc_syscon_clock.h_源码浏览.md)
